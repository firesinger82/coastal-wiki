"""Bounded MTEF5 structure/character reader with bounded nudge support.

Uses the previously consulted Wiris MTEF5 record specification. Does not render
equations or infer the mathematical intent of stored characters. Unsupported
records/options fail closed. OLE prefix and explicit body offset are caller data.
"""
import hashlib
import importlib.util
from pathlib import Path


def inspect(data, body_offset=220):
    spec = importlib.util.spec_from_file_location('empty_prefix', Path(__file__).with_name('inspect_future_prefix.py'))
    prefix = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(prefix)
    # Validate the entire settings prefix with a synthetic top-level terminator.
    # This result is NOT evidence that the actual equation is empty.
    settings = prefix.inspect(data[:body_offset] + b'\x00', 28)
    pos = body_offset
    chars = []

    def byte():
        nonlocal pos
        if pos >= len(data):
            raise ValueError('truncated at ' + str(pos))
        v = data[pos]
        pos += 1
        return v

    def word():
        return byte() | byte() << 8

    def uint():
        v = byte()
        return word() if v == 255 else v

    def signed_word():
        v = word()
        return v - 65536 if v & 32768 else v

    def nudge():
        dx, dy = byte(), byte()
        if dx == dy == 128:
            return {'dx': signed_word(), 'dy': signed_word(), 'encoding_bytes': 6}
        return {'dx': dx - 128, 'dy': dy - 128, 'encoding_bytes': 2}

    def ruler():
        start = pos
        if byte() != 7:
            raise ValueError('expected ruler')
        stops = []
        for _ in range(byte()):
            kind = byte()
            if kind > 4:
                raise ValueError('unknown tab type')
            stops.append({'type': kind, 'offset': word()})
        return {'offset': start, 'tag': 7, 'stops': stops, 'end_offset': pos}

    colors = []

    def objects(depth=0):
        if depth > 64:
            raise ValueError('nesting too deep')
        nodes = []
        while True:
            start = pos
            tag = byte()
            node = {'offset': start, 'tag': tag}
            if tag == 0:
                nodes.append({**node, 'end_offset': pos})
                return nodes
            if 10 <= tag <= 14:
                node['size_code'] = tag - 10
            elif tag == 9:
                mode = byte()
                node['mode'] = mode
                if mode == 101:
                    node['explicit_size_raw'] = signed_word()
                elif mode == 100:
                    node['logical_size'] = byte()
                    node['delta'] = signed_word()
                elif mode <= 4:
                    node['logical_size'] = mode
                    node['delta'] = byte() - 128
                else:
                    raise ValueError('unsupported size mode')
            elif tag == 15:
                node['color_index'] = uint()
                if not 1 <= node['color_index'] <= len(colors):
                    raise ValueError('undefined color reference')
            elif tag == 16:
                options = byte()
                if options != 0:
                    raise ValueError('only unnamed process RGB supported')
                node['options'] = options
                node['rgb'] = [word() for _ in range(3)]
                if any(v > 1000 for v in node['rgb']):
                    raise ValueError('color component out of range')
                colors.append(node)
            elif tag == 5:
                node['options'] = byte()
                if node['options'] != 0:
                    raise ValueError('unsupported matrix options')
                for key in ('vertical_alignment', 'horizontal_justification', 'vertical_justification', 'rows', 'columns'):
                    node[key] = byte()
                if not node['rows'] or not node['columns']:
                    raise ValueError('zero matrix dimension')
                # Preserve packed partitions without guessing bit order.
                node['row_partition_bytes'] = [byte() for _ in range((node['rows'] + 4)//4)]
                node['column_partition_bytes'] = [byte() for _ in range((node['columns'] + 4)//4)]
                node['children'] = objects(depth+1)
                if sum(c['tag'] == 1 for c in node['children']) != node['rows'] * node['columns']:
                    raise ValueError('matrix cell count mismatch')
            elif tag == 6:
                node['options'] = byte()
                if node['options'] != 0:
                    raise ValueError('unsupported embellishment options')
                node['embellishment_type'] = byte()
                if not 2 <= node['embellishment_type'] <= 22:
                    raise ValueError('unsupported embellishment type')
            elif tag in (1, 2, 3, 4):
                options = byte()
                node['options'] = options
                allowed = {1: 15, 2: 0x3f, 3: 8, 4: 10}[tag]
                if options & ~allowed:
                    raise ValueError(f'unsupported options {options} at {start}')
                if options & 8:
                    node['nudge'] = nudge()
                if tag == 1:
                    if options & 4:
                        node['line_spacing_raw'] = word()
                    if options & 2:
                        node['ruler'] = ruler()
                    if not options & 1:
                        node['children'] = objects(depth+1)
                elif tag == 2:
                    face = byte()
                    node['typeface'] = word() - 32768 if face == 255 else face - 128
                    if not options & 32:
                        node['mtcode'] = word()
                    if options & 4 and options & 16:
                        raise ValueError('mutually exclusive font encodings')
                    if options & 4:
                        node['font_position'] = byte()
                    if options & 16:
                        node['font_position'] = word()
                    if 'mtcode' not in node:
                        raise ValueError('font-only character unsupported')
                    if options & 1:
                        node['embellishments'] = objects(depth+1)
                        if any(n['tag'] not in (0, 6) for n in node['embellishments']):
                            raise ValueError('non-embellishment in character embellishment list')
                    chars.append(node)
                elif tag == 3:
                    node['selector'] = byte()
                    variation = byte()
                    node['variation'] = (variation & 127) | byte() << 8 if variation & 128 else variation
                    node['template_options'] = byte()
                    node['children'] = objects(depth+1)
                else:
                    node['horizontal_alignment'] = byte()
                    node['vertical_alignment'] = byte()
                    if options & 2:
                        node['ruler'] = ruler()
                    node['children'] = objects(depth+1)
            else:
                raise ValueError(f'unsupported record {tag} at {start}')
            node['end_offset'] = pos
            nodes.append(node)

    tree = objects()
    if pos != len(data):
        raise ValueError('trailing bytes')
    return {'stream_sha256': hashlib.sha256(data).hexdigest(), 'stream_bytes': len(data),
            'body_offset': body_offset, 'prefix_validation': {
                'method': 'settings bytes followed by a synthetic END for prefix validation only',
                'application_key': settings['application_key'], 'header': settings['header'],
                'settings_records': settings['records'][:-1]},
            'tree': tree, 'characters': chars,
            'scope': 'Stored record structure and MTCode values only; no general mathematical interpretation or font rendering equivalence.'}
