"""Bounded MTEF5 settings reader retaining length-delimited FUTURE payloads.

Record layout: https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later
The caller supplies the MTEF offset. The preceding OLE wrapper is opaque here.
Unknown records/options, truncation, and trailing bytes fail closed.
"""
import hashlib


def inspect(data, offset):
    if not 0 <= offset < len(data):
        raise ValueError('invalid MTEF offset')
    pos = offset

    def take(n=1):
        nonlocal pos
        if pos + n > len(data):
            raise ValueError('truncated at ' + str(pos))
        b = data[pos:pos+n]
        pos += n
        return b

    def byte():
        return take()[0]

    def uint():
        b = byte()
        return int.from_bytes(take(2), 'little') if b == 255 else b

    def string():
        out = bytearray()
        while (b := byte()) != 0:
            out.append(b)
        return out.decode('ascii')

    def dimensions():
        count = byte()
        values = []
        high = True
        current = 0

        def nibble():
            nonlocal high, current
            if high:
                current = byte()
                high = False
                return current >> 4
            high = True
            return current & 15

        for _ in range(count):
            unit = nibble()
            if unit > 4:
                raise ValueError('unknown dimension unit')
            value = ''
            while (n := nibble()) != 15:
                if n > 11:
                    raise ValueError('unknown dimension nibble')
                value += '0123456789.-'[n]
            values.append({'unit_code': unit, 'value': value})
        if not high and nibble() != 0:
            raise ValueError('nonzero dimension padding')
        return values

    head = list(take(5))
    if head[0] != 5:
        raise ValueError('only MTEF5 supported')
    app = string()
    options = byte()
    if options & ~1:
        raise ValueError('unknown equation options')
    records = []
    fonts = []
    encoding_count = 4
    while True:
        start = pos
        tag = byte()
        r = {'offset': start, 'tag': tag}
        if tag >= 100:
            length = uint()
            r['opaque_payload_hex'] = take(length).hex()
            r['payload_bytes'] = length
            r['interpretation'] = 'uninterpreted future record'
        elif tag == 19:
            r['encoding'] = string()
            encoding_count += 1
        elif tag == 17:
            r['encoding_index'] = uint()
            if not 1 <= r['encoding_index'] <= encoding_count:
                raise ValueError('invalid encoding reference')
            r['font'] = string()
            fonts.append(r['font'])
        elif tag == 18:
            if byte() != 0:
                raise ValueError('unknown preferences options')
            r['sizes'] = dimensions()
            r['spaces'] = dimensions()
            r['styles'] = []
            for _ in range(byte()):
                index = uint()
                if index > len(fonts):
                    raise ValueError('invalid font reference')
                style = byte() if index else None
                if style is not None and style > 3:
                    raise ValueError('unknown character style')
                r['styles'].append({'font_index': index, 'style': style})
        elif 10 <= tag <= 14:
            r['size_code'] = tag - 10
        elif tag == 0:
            r['end_offset'] = pos
            records.append(r)
            if pos != len(data):
                raise ValueError('bytes after top-level END')
            break
        else:
            raise ValueError(f'body or unsupported record {tag} at {start}')
        r['end_offset'] = pos
        records.append(r)
    return {'stream_sha256': hashlib.sha256(data).hexdigest(), 'stream_bytes': len(data),
            'mtef_offset': offset, 'opaque_prefix_hex': data[:offset].hex(),
            'header': head, 'application_key': app, 'equation_options': options,
            'records': records, 'body_structure_records': 0,
            'result': 'settings-only-with-opaque-future-records',
            'scope': 'Exact MTEF5 stream only. No general OLE semantics, rendering equivalence, or missing formula reconstruction.'}
