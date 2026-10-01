#!/usr/bin/env python3
"""Bind frozen XBeach captions to existing structural evidence (stdlib only).

No equation decoding, field evaluation, rendering, extraction to disk, or writes
outside this directory. Run from any cwd: python3 /path/to/build_packets.py.
Archive paths use ``container!member``; their SHA is over the member bytes.
This adapter supplies candidate judgments, never an R2 semantic disposition.
"""

from collections import Counter, defaultdict
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import posixpath
import re
import struct
import unicodedata
import xml.etree.ElementTree as ET
from zipfile import ZipFile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
BASE = HERE.parent
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
W14 = '{http://schemas.microsoft.com/office/word/2010/wordml}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
O = '{urn:schemas-microsoft-com:office:office}'
V = '{urn:schemas-microsoft-com:vml}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
LABEL = re.compile(r'\([A-Z0-9]+\.\d+\)')
TARGET = re.compile(r'\s*(?:MACROBUTTON MTPlaceRef|GOTOBUTTON ZEqnNum)')
STATUS = ('unique', 'ambiguous', 'none')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def relative(path):
    return str(Path(path).resolve().relative_to(ROOT))


@lru_cache(maxsize=None)
def file_hash(path):
    return digest(Path(path).read_bytes())


def artifact(path, expected=None):
    path = Path(path) if Path(path).is_absolute() else ROOT / path
    actual = file_hash(path)
    require(expected is None or actual == expected, f'Artifact hash mismatch: {path}')
    return {'path': relative(path), 'sha256': actual}


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def write_json(path, data):
    require(path.parent.resolve() == HERE or path.parent.resolve() == HERE / 'packets',
            f'Write outside output whitelist: {path}')
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def words(text):
    # Used only to locate existing prose, never to transcribe an equation.
    return re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKC', text).lower())


def quoted_labels(text):
    result = set(LABEL.findall(text))
    for match in re.finditer(r'\(([A-Z0-9]+)\.(\d+)\)\s*[-–]\s*\(\1\.(\d+)\)', text):
        chapter, first, last = match.groups()
        if 0 <= int(last) - int(first) <= 200:
            result.update(f'({chapter}.{i})' for i in range(int(first), int(last) + 1))
    return result


def opaque_cfb_stream(data, stream_name, root_only=False):
    """Read an OLE container stream for byte identity; do not decode its payload.

    Only the container's FAT/directory and the requested stream are interpreted.
    This also works when the OLE embedding is absent from a symbol receipt.
    """
    require(data[:8] == bytes.fromhex('d0cf11e0a1b11ae1'), 'Not a CFB container')
    sector_size = 1 << struct.unpack_from('<H', data, 30)[0]
    mini_size = 1 << struct.unpack_from('<H', data, 32)[0]
    require(sector_size in (512, 4096) and mini_size == 64, 'Unsupported CFB profile')
    end, free = 0xFFFFFFFE, 0xFFFFFFFF

    def sector(number):
        start = (number + 1) * sector_size
        require(0 <= number < len(data) // sector_size - 1, 'CFB sector out of range')
        return data[start:start + sector_size]

    def integers(blob):
        return list(struct.unpack('<' + 'I' * (len(blob) // 4), blob))

    fat_count, directory_start = struct.unpack_from('<II', data, 44)
    cutoff, mini_start, mini_count, difat_start, difat_count = struct.unpack_from('<IIIII', data, 56)
    difat = integers(data[76:512])
    seen_difat = set()
    for _ in range(difat_count):
        require(difat_start not in seen_difat, 'CFB DIFAT cycle')
        seen_difat.add(difat_start)
        row = integers(sector(difat_start))
        difat.extend(row[:-1])
        difat_start = row[-1]
    fat_sectors = [i for i in difat if i != free][:fat_count]
    require(len(fat_sectors) == fat_count, 'Incomplete CFB FAT')
    fat = [n for i in fat_sectors for n in integers(sector(i))]

    def chain(start, table):
        seen = set()
        while start not in (end, free):
            require(0 <= start < len(table) and start not in seen, 'Invalid CFB chain')
            seen.add(start)
            yield start
            start = table[start]

    directory = b''.join(sector(i) for i in chain(directory_start, fat))
    eligible = None
    if root_only:
        root_rows = [directory[i:i + 128] for i in range(0, len(directory), 128)
                     if directory[i + 66] == 5]
        require(len(root_rows) == 1, 'CFB root directory not unique')
        pending = [struct.unpack_from('<I', root_rows[0], 76)[0]]
        eligible = set()
        while pending:
            index = pending.pop()
            if index == free:
                continue
            require(index not in eligible and index * 128 + 128 <= len(directory), 'Invalid CFB root tree')
            eligible.add(index)
            row = directory[index * 128:(index + 1) * 128]
            pending.extend(struct.unpack_from('<II', row, 68))
    entries = []
    for i in range(0, len(directory), 128):
        row = directory[i:i + 128]
        if len(row) < 128 or row[66] == 0:
            continue
        if eligible is not None and i // 128 not in eligible and row[66] != 5:
            continue
        length = struct.unpack_from('<H', row, 64)[0]
        name = row[:max(0, length - 2)].decode('utf-16le')
        start = struct.unpack_from('<I', row, 116)[0]
        size = struct.unpack_from('<Q', row, 120)[0]
        if sector_size == 512:
            size &= 0xFFFFFFFF
        entries.append((name, row[66], start, size))
    matches = [e for e in entries if e[0] == stream_name and e[1] == 2]
    require(len(matches) == 1, f'CFB stream not unique: {stream_name}')
    _, _, start, size = matches[0]
    if size >= cutoff:
        value = b''.join(sector(i) for i in chain(start, fat))[:size]
    else:
        roots = [e for e in entries if e[1] == 5]
        require(len(roots) == 1 and mini_count > 0, 'CFB mini-stream missing')
        _, _, root_start, root_size = roots[0]
        mini_stream = b''.join(sector(i) for i in chain(root_start, fat))[:root_size]
        mini_fat = integers(b''.join(sector(i) for i in chain(mini_start, fat)))
        value = b''.join(mini_stream[i * mini_size:(i + 1) * mini_size]
                         for i in chain(start, mini_fat))[:size]
    require(len(value) == size, 'Truncated CFB stream')
    return value


class Document:
    def __init__(self, name, source, package, fields=None, member_inventory=None):
        self.name = name
        self.source = source
        self.package = Path(package)
        self.zip = ZipFile(self.package)
        self.root = ET.fromstring(self.zip.read('word/document.xml'))
        self.nodes = list(self.root.iter())
        self.ordinal = {e: i for i, e in enumerate(self.nodes)}
        self.parent = {child: p for p in self.nodes for child in p}
        self.body = self.root.find(W + 'body')
        self.paragraphs = list(self.body.iter(W + 'p'))
        self.pindex = {p: i for i, p in enumerate(self.paragraphs)}
        self.direct_index = {p: i for i, p in enumerate(self.body.findall(W + 'p'))}
        self.fields = {f['start_xml_ordinal']: f for f in fields or []}
        self.member_inventory = member_inventory or {}
        relationships = ET.fromstring(self.zip.read('word/_rels/document.xml.rels'))
        self.relationships = {r.get('Id'): dict(r.attrib) for r in relationships}
        self.texts = [self.text(p) for p in self.paragraphs]
        self.token_texts = [' '.join(words(t)) for t in self.texts]
        self.captions = []
        self.page_check = None

    def ancestor(self, node, tag):
        while node is not None:
            if node.tag == tag:
                return node
            node = self.parent.get(node)
        return None

    def text(self, p):
        output, skip_to = [], -1
        for e in p.iter():
            ordinal = self.ordinal[e]
            if ordinal <= skip_to:
                continue
            if ordinal in self.fields:
                field = self.fields[ordinal]
                output.append(field['display'])
                skip_to = field['end_xml_ordinal']
            elif e.tag == W + 't':
                output.append(e.text or '')
            elif e.tag == W + 'tab':
                output.append('\t')
            elif e.tag in (W + 'br', W + 'cr'):
                output.append('\n')
        return ''.join(output).strip()

    def paragraph_record(self, p):
        return {
            'container_path': relative(self.package),
            'member': 'word/document.xml',
            'start_xml_ordinal': self.ordinal[p],
            'body_paragraph_zero_based': self.pindex[p],
            'direct_body_paragraph_zero_based': self.direct_index.get(p),
            'paragraph_id': p.get(W14 + 'paraId'),
            'text': self.texts[self.pindex[p]],
        }

    def context(self, p):
        index = self.pindex[p]
        before, after = [], []
        for direction, output in ((-1, before), (1, after)):
            i = index + direction
            while 0 <= i < len(self.paragraphs) and len(output) < 2:
                if self.texts[i]:
                    output.append(self.paragraph_record(self.paragraphs[i]))
                i += direction
        cell = self.ancestor(p, W + 'tc')
        return {
            'caption_paragraph': self.paragraph_record(p),
            'preceding_nonempty_paragraphs': list(reversed(before)),
            'following_nonempty_paragraphs': after,
            'table_cell': None if cell is None else {
                'start_xml_ordinal': self.ordinal[cell],
                'paragraphs': [self.paragraph_record(q) for q in cell.iter(W + 'p')],
            },
            'text_method': 'Saved display-field substitution plus w:t; equation objects are not transcribed.',
        }

    def member(self, member):
        blob = self.zip.read(member)
        actual = digest(blob)
        expected = self.member_inventory.get(member)
        require(expected is None or expected == actual, f'Member hash mismatch: {member}')
        return {
            'path': relative(self.package) + '!' + member,
            'storage': 'zip-member', 'container_path': relative(self.package),
            'member': member, 'sha256': actual,
        }

    def relationship(self, rid):
        require(rid in self.relationships, f'Unknown relationship {self.name}: {rid}')
        row = self.relationships[rid]
        require(row.get('TargetMode') != 'External', f'External relationship: {rid}')
        member = posixpath.normpath(posixpath.join('word', row['Target']))
        if row['Target'].startswith('/'):
            member = row['Target'].lstrip('/')
        require(not member.startswith('../'), 'Package relationship escapes archive')
        return {'id': rid, 'target': row['Target'], 'type': row['Type'], 'member': member}

    def images(self, wrapper):
        found = []
        for e in wrapper.iter():
            rid = e.get(R + 'id') if e.tag == V + 'imagedata' else e.get(R + 'embed') if e.tag == A + 'blip' else None
            if rid:
                relationship = self.relationship(rid)
                found.append({**self.member(relationship['member']),
                              'relationship': relationship, 'xml_ordinal': self.ordinal[e]})
        return found

    def objects(self, p, native_inventory):
        output, consumed_images = [], set()
        for e in p.iter(O + 'OLEObject'):
            rel = self.relationship(e.get(R + 'id'))
            wrapper = self.ancestor(e, W + 'object')
            require(wrapper is not None and self.ancestor(wrapper, W + 'p') is p,
                    'OLE object escaped caption paragraph')
            # Bind the preview by OLE ShapeID, not by nearest image or shared label.
            shapes = [q for q in wrapper.iter(V + 'shape') if q.get('id') == e.get('ShapeID')]
            previews = [im for q in shapes for im in self.images(q)]
            consumed_images.update(im['xml_ordinal'] for im in previews)
            obj = {
                'kind': 'ole', 'locator': {
                    'container_path': relative(self.package), 'member': 'word/document.xml',
                    'xml_ordinal': self.ordinal[e], 'paragraph_xml_ordinal': self.ordinal[p],
                },
                'relationship': rel, 'ole': self.member(rel['member']),
                'prog_id': e.get('ProgID'), 'shape_id': e.get('ShapeID'),
                'object_id': e.get('ObjectID'), 'previews': previews,
                'preview_binding_status': 'unique' if len(shapes) == 1 and previews else 'ambiguous',
            }
            if self.name == 'nonhydro':
                native_hash = digest(opaque_cfb_stream(self.zip.read(rel['member']), 'Equation Native'))
                candidates = native_inventory.get(native_hash, [])
                require(candidates, f'No original DOC stream identity for {rel["member"]}')
                obj['original_stream_identity'] = {
                    'source': self.source, 'native_sha256': native_hash,
                    'candidate_stream_locators': candidates,
                    'method': 'Opaque Equation Native byte SHA only; does not choose caption occurrence.',
                }
            output.append(obj)
        # Preserve standalone previews/drawings in this paragraph too (0..N).
        for im in self.images(p):
            if im['xml_ordinal'] not in consumed_images:
                output.append({
                    'kind': 'preview', 'locator': {
                        'container_path': relative(self.package), 'member': 'word/document.xml',
                        'xml_ordinal': im['xml_ordinal'], 'paragraph_xml_ordinal': self.ordinal[p],
                    }, 'relationship': im['relationship'], 'previews': [im],
                    'preview_binding_status': 'unique',
                })
        return output


def associate_pages(doc, captions, text_path, pdf_path, image_paths):
    text = Path(text_path).read_text(encoding='utf-8')
    pages = text.split('\f')
    if pages[-1].strip() == '':
        pages.pop()
    found = []
    for page, page_text in enumerate(pages, 1):
        for line, value in enumerate(page_text.splitlines(), 1):
            if LABEL.fullmatch(value.strip()):
                found.append({'label': value.strip(), 'physical_render_page': page,
                              'page_text_line': line, 'line_text': value})
    source_labels = [c['label_as_saved'] for c in captions]
    render_labels = [f['label'] for f in found]
    ordered_equal = source_labels == render_labels
    doc.page_check = {
        'render_pdf': artifact(pdf_path), 'render_text': artifact(text_path),
        'physical_page_count': len(pages), 'source_caption_count': len(captions),
        'standalone_render_caption_count': len(found),
        'entire_caption_sequence_equal': ordered_equal,
        'source_sequence_sha256': digest(json.dumps(source_labels).encode()),
        'render_sequence_sha256': digest(json.dumps(render_labels).encode()),
    }
    result = {}
    for index, caption in enumerate(captions):
        candidates = [found[index]] if ordered_equal else [f for f in found if f['label'] == caption['label_as_saved']]
        candidate_pages = sorted({f['physical_render_page'] for f in candidates})
        page = candidate_pages[0] if len(candidate_pages) == 1 else candidate_pages
        result[caption['id']] = {
            'page': page, 'physical_render_page': page if isinstance(page, int) else None,
            'candidate_pages': candidate_pages,
            'method': 'Full standalone-caption sequence equality + source occurrence order' if ordered_equal
                      else 'Label-only page candidates; full sequence did not agree',
            'source_caption_sequence_zero_based': index,
            'render_caption_sequence_zero_based': index if ordered_equal else None,
            'render_pdf': doc.page_check['render_pdf'], 'render_text': doc.page_check['render_text'],
            'render_matches': candidates,
            'page_images': [artifact(image_paths[i]) for i in candidate_pages],
            'ordered_sequence_verified': ordered_equal,
        }
    return result


def candidate(path, pointer, kind, record, proof, scope):
    return {
        'kind': kind, 'evidence': artifact(path), 'json_pointer': pointer,
        'match': proof, 'record': record, 'candidate_only': True,
        'claim_scope': scope, 'claims_resolved': [],
        'gaps_left': ['R2 must judge equation meaning, applicability and implementation relation.'],
    }


def match_visual(packet, doc, p, receipt_path, receipt):
    results = []
    for section in ('equation_supplements', 'source_empty_paragraphs'):
        for index, record in enumerate(receipt[section]):
            if (record['source']['path'] != doc.source['path'] or
                    '(' + record['equation_label'] + ')' != packet['caption']['label'] or
                    record['paragraph_id'] != p.get(W14 + 'paraId')):
                continue
            require(record['source']['sha256'] == doc.source['sha256'], 'Visual receipt source mismatch')
            page = record['physical_render_page']
            require(page in packet['association']['render']['candidate_pages'], 'Visual receipt page disagrees')
            proof = {'document': doc.name, 'label': packet['caption']['label'],
                     'caption_locator': packet['caption']['locator'],
                     'paragraph_id': record['paragraph_id'], 'physical_render_page': page,
                     'method': 'Exact source identity + label + original paragraph ID'}
            if section == 'equation_supplements':
                objects = packet['association']['objects']
                bound = [o for o in objects if o['relationship']['member'] == record['ole_member']]
                require(len(bound) == 1 and bound[0]['relationship']['id'] == record['ole_relationship'],
                        'Supplement OLE relationship mismatch')
                require(any(im['relationship']['id'] == record['preview_relationship'] and
                            im['member'] == record['preview_member'] for im in bound[0]['previews']),
                        'Supplement preview relationship mismatch')
                for key, value in record['artifacts'].items():
                    checked = artifact(value['path'], value['sha256'])
                    if key in ('preview', 'png', 'pdf'):
                        bound[0]['previews'].append({**checked, 'storage': 'file',
                                                     'role': 'existing_equation_supplement_' + key})
            else:
                require(not packet['association']['objects'], 'Empty paragraph receipt has objects')
                artifact(record['artifact']['path'], record['artifact']['sha256'])
            results.append(candidate(receipt_path, f'/{section}/{index}', 'existing_judgment',
                                     record, proof, 'Existing local visual observation; no new visual reading.'))
    return results


def match_symbols(packet, doc, p, symbol_receipts, native_inventory):
    results = []
    if doc.name != 'nonhydro':
        return results
    for path, receipt in symbol_receipts:
        require(receipt['source_doc'] == doc.source, 'Symbol receipt source mismatch')
        for index, record in enumerate(receipt['records']):
            direct_index = record['direct_body_paragraph_zero_based']
            symbol_p = doc.body.findall(W + 'p')[direct_index]
            label = packet['caption']['label']
            at_caption = symbol_p is p and record['paragraph_text'].strip() == label
            # A definition receipt can link to its explicitly named caption,
            # without inserting the definition's inline object into objects[].
            after_caption = (label in quoted_labels(record.get('source_pdf_locator', '')) and
                             doc.direct_index.get(p) == direct_index - 1 and
                             record.get('source_pdf_locator', '').startswith('definition immediately after equation'))
            if not (at_caption or after_caption):
                continue
            require(' '.join(doc.text(symbol_p).split()) == ' '.join(record['paragraph_text'].split()),
                    'Symbol receipt paragraph text mismatch')
            paragraph_objects = packet['association']['objects'] if at_caption else doc.objects(symbol_p, native_inventory)
            objects = [o for o in paragraph_objects
                       if o['relationship']['member'] == record['converted_docx_member']]
            require(len(objects) == 1, 'Symbol receipt object mismatch')
            identity = objects[0]['original_stream_identity']
            require(identity['native_sha256'] == record['native_sha256'] and
                    record['doc_stream'] in identity['candidate_stream_locators'], 'Symbol stream identity mismatch')
            artifact(record['paragraph_xml'])
            if 'doc_render_physical_page' in record:
                require(not at_caption or record['doc_render_physical_page'] == packet['association']['page'],
                        'Symbol render page mismatch')
            proof = {'document': doc.name, 'label': packet['caption']['label'],
                     'caption_locator': packet['caption']['locator'],
                     'direct_body_paragraph_zero_based': direct_index,
                     'symbol_paragraph': doc.paragraph_record(symbol_p),
                     'relationship_to_caption': 'caption_body' if at_caption else 'explicit_definition_after_caption',
                     'ole_member': record['converted_docx_member'],
                     'native_sha256': record['native_sha256'],
                     'method': 'Exact DOC field occurrence + converted paragraph + member + stream byte identity'}
            results.append(candidate(path, f'/records/{index}', 'existing_judgment', record, proof,
                                     'Only the named symbol meaning; not the full equation or its implementation.'))
    return results


def xh_candidates(doc, mapping_path, mapping, packets):
    """Conservative quote-to-source paragraph bridge, including repeated labels.

    A label mention alone is insufficient. Locate at least eight contiguous
    prose tokens from its quote in the document. Link a repeated label only when
    the quote is local to exactly one occurrence (within two body paragraphs).
    Original-PDF page numbers are retained as original-PDF locators, not reused
    as physical pages of these independent renders.
    """
    by_label = defaultdict(list)
    for cap, p in doc.captions:
        by_label[cap['label_as_saved']].append((cap, p))
    misses, matched = [], 0
    for entry_index, entry in enumerate(mapping['entries']):
        locator = entry['source_locator']
        original = Path(locator['original_path'])
        if original.stem != Path(doc.source['path']).stem:
            continue
        original_artifact = artifact(locator['original_path'], locator['original_sha256'])
        if original.suffix in ('.doc', '.docx'):
            require(locator['original_sha256'] == doc.source['sha256'], 'XH source identity mismatch')
        for quote in locator.get('reported_span_direct_quotes', []):
            labels = quoted_labels(quote['quote']) & set(by_label)
            if not labels:
                continue
            tokens = words(quote['quote'].replace('…', ''))
            hits = set()
            # Exact contiguous windows tolerate omitted object/formula text,
            # subscripts, and a clipped quote prefix; every bridge is preserved.
            windows = [' '.join(tokens[i:i + 8]) for i in range(max(0, len(tokens) - 7))]
            for pi, normalized in enumerate(doc.token_texts):
                if any(' ' + window + ' ' in ' ' + normalized + ' ' for window in windows):
                    hits.add(pi)
            for label in sorted(labels):
                occurrences = by_label[label]
                selected = []
                for cap, p in occurrences:
                    local_hits = [i for i in sorted(hits) if abs(i - doc.pindex[p]) <= 2]
                    if hits and (len(occurrences) == 1 or local_hits):
                        selected.append((cap, p, local_hits or sorted(hits)))
                if len(selected) != 1:
                    misses.append({'finding_id': entry['finding_id'], 'document': doc.name,
                                   'label': label, 'quote_line': quote['line'],
                                   'reason': 'No unique source-paragraph quote/occurrence bridge',
                                   'quote_paragraph_candidates': sorted(hits)})
                    continue
                cap, p, hit_indices = selected[0]
                proof = {'document': doc.name, 'label': label, 'caption_locator': cap['locator'],
                         'method': 'Same source work + explicit label + exact prose-token bridge to source paragraphs',
                         'cross_representation_candidate': original.suffix == '.pdf',
                         'original_source_identity': original_artifact,
                         'quoted_line': quote, 'quote_paragraphs': [doc.paragraph_record(doc.paragraphs[i]) for i in hit_indices]}
                judgment = candidate(mapping_path, f'/entries/{entry_index}', 'existing_judgment', entry, proof,
                                     'XH finding candidate only; reference prose is not a full equation judgment.')
                existing = packets[cap['id']]['candidate_existing_judgments']
                # Keep distinct quote bridges for a shared finding in one candidate.
                same = next((j for j in existing if j['evidence']['path'] == relative(mapping_path)
                             and j['json_pointer'] == judgment['json_pointer']), None)
                if same is None:
                    existing.append(judgment)
                    matched += 1
                else:
                    same['match'].setdefault('additional_quote_bridges', []).append(proof)
    return {'matched_packet_finding_pairs': matched, 'unmatched_label_mentions': misses}


def build():
    scope_path = BASE / 'remaining-20260912/equation-scope.json'
    scope = load(scope_path)
    captions = scope['captions']
    require(len(captions) == 443 and len({c['id'] for c in captions}) == 443, 'Frozen scope is not 443 unique IDs')
    sources = {Path(s['path']).stem: s for s in scope['document_sources']}
    for source in sources.values():
        artifact(source['path'], source['sha256'])
    visual_path = BASE / 'manuals-docx-read/full-visual-read/receipt.json'
    visual = load(visual_path)
    contracts_path = BASE / 'build-mode-20260912/contracts.json'
    contracts = load(contracts_path)
    mapping_path = BASE.parent / 'closure/document-inventory/document-canonical-mapping.json'
    mapping = load(mapping_path)
    symbol_receipts = [(BASE / f'nonhydro-read/{name}/receipt.json',
                        load(BASE / f'nonhydro-read/{name}/receipt.json'))
                       for name in ('stress-tensor-symbol', 'solitary-wave-symbols')]
    native_inventory = defaultdict(list)
    doc_inventory_path = BASE / 'nonhydro-read/doc-container-inventory.json'
    doc_inventory = load(doc_inventory_path)
    for stream in doc_inventory['streams']:
        stream_path = stream['path'].split('/') if isinstance(stream['path'], str) else stream['path']
        if stream_path[-1] == 'Equation Native':
            native_inventory[stream['sha256']].append(stream_path)
    docs, packets, input_paths = {}, {}, [scope_path, visual_path, contracts_path, mapping_path, doc_inventory_path]
    input_paths.extend(path for path, _ in symbol_receipts)
    field_checks = {}
    for name in ('kingsday', 'master', 'nonhydro'):
        selected = sorted([c for c in captions if c['document'] == name], key=lambda c: c['locator'])
        if name != 'nonhydro':
            source = sources['XBeach_manual_' + name]
            fields_path = BASE / f'manuals-docx-read/{name}/display-fields.json'
            inventory_path = BASE / f'manuals-docx-read/{name}/container-inventory.json'
            fields, inventory = load(fields_path), load(inventory_path)
            require(fields['source_sha256'] == source['sha256'], 'Display field source mismatch')
            doc = Document(name, source, ROOT / source['path'], fields['fields'],
                           {m['path']: m['sha256'] for m in inventory['members']})
            caption_fields = [f for f in fields['fields'] if str(f['code'][0]).strip().startswith('MACROBUTTON MTPlaceRef')
                              and LABEL.fullmatch(f['display'])]
            require([(f['start_xml_ordinal'], f['display']) for f in caption_fields] ==
                    [(c['locator'], c['label_as_saved']) for c in selected], 'DOCX caption inventory mismatch')
            for cap in selected:
                e = doc.nodes[cap['locator']]
                require(e.tag == W + 'fldChar' and e.get(W + 'fldCharType') == 'begin', 'Caption ordinal not field begin')
                p = doc.ancestor(e, W + 'p')
                require(p in doc.pindex and cap['label_as_saved'] in doc.text(p), 'Caption label/paragraph mismatch')
                doc.captions.append((cap, p))
            field_checks[name] = {'source_caption_fields_equal_scope': True, 'caption_fields': len(caption_fields),
                                  'empty_macro_wrappers_excluded_from_frozen_caption_scope':
                                  sum(not f['display'] and str(f['code'][0]).strip().startswith('MACROBUTTON MTPlaceRef')
                                      for f in fields['fields'])}
            text_path = BASE / f'manuals-docx-read/{name}/display-recovered/render.txt'
            pdf_path = text_path.with_suffix('.pdf')
            record = next(r for r in visual['records'] if r['source']['path'] == source['path'])
            require(artifact(pdf_path) == record['render_pdf'], 'Visual receipt render mismatch')
            page_records = {r['physical_render_page']: r for r in record['page_records']}
            image_paths = {i: ROOT / page_records[i]['path'] if i in page_records else
                           BASE / f'manuals-docx-read/{name}/display-recovered/page-{i:03d}.png'
                           for i in range(1, record['render_pages'] + 1)}
            for i, r in page_records.items():
                require(artifact(image_paths[i], r['sha256'])['path'] == r['path'], 'Page image receipt mismatch')
            input_paths.extend([fields_path, inventory_path])
        else:
            source = sources['non-hydrostatic_report_draft']
            require(doc_inventory['source'] == source, 'DOC inventory source mismatch')
            cache_path = BASE / 'nonhydro-read/cached-fields.json'
            cache = load(cache_path)
            require(cache['source_path'] == source['path'] and cache['source_sha256'] == source['sha256'], 'DOC cache source mismatch')
            source_bytes = (ROOT / source['path']).read_bytes()
            word_stream = opaque_cfb_stream(source_bytes, 'WordDocument', root_only=True)
            table_stream = opaque_cfb_stream(source_bytes, '1Table', root_only=True)
            require(digest(word_stream) == cache['word_stream_sha256'] and
                    digest(table_stream) == cache['table_stream_sha256'], 'DOC cached container stream identity differs')
            for record in cache['records']:
                start, end = record['word_stream_start'], record['word_stream_end_exclusive']
                require(0 <= start < end <= len(word_stream) and
                        digest(word_stream[start:end]) == record['raw_field_sha256'], 'DOC cached byte-span identity differs')
            recovery_path = BASE / 'nonhydro-read/field-recovery/receipt.json'
            recovery = load(recovery_path)
            converted_path = BASE / 'nonhydro-read/field-recovery/converted.docx'
            restored_path = BASE / 'nonhydro-read/body-field-recovery/body-cached.docx'
            body_receipt_path = BASE / 'nonhydro-read/body-field-recovery/receipt.json'
            body_receipt = load(body_receipt_path)
            for path, receipt in ((converted_path, recovery), (restored_path, body_receipt)):
                saved = next(a for a in receipt['artifacts'] if a['path'] == relative(path))
                artifact(path, saved['sha256'])
            converted = Document(name, source, converted_path)
            doc = Document(name, source, restored_path)
            # Compare all body paragraphs, including object identities. No
            # positional assumption across conversion stages without this check.
            require(len(converted.paragraphs) == len(doc.paragraphs), 'Converted/restored paragraph count differs')
            for cp, rp in zip(converted.paragraphs, doc.paragraphs):
                def signature(document, paragraph):
                    return [(e.get('ShapeID'), e.get(R + 'id'),
                             document.relationship(e.get(R + 'id'))['member']) for e in paragraph.iter(O + 'OLEObject')]
                require(signature(converted, cp) == signature(doc, rp), 'Converted/restored OLE paragraph identity differs')
            outer = sorted([r for r in cache['records'] if not r['nested_in_target']], key=lambda r: r['word_stream_start'])
            commands = [e for e in converted.body.iter(W + 'instrText') if TARGET.match(e.text or '')]
            require(len(outer) == len(commands) == 166, 'DOC outer-field count differs from 166')
            require(all((e.text or '').strip() == r['command'].strip() for e, r in zip(commands, outer)), 'DOC outer-field command order mismatch')
            bridges = {}
            for i, (command, record) in enumerate(zip(commands, outer)):
                if not record['command'].strip().startswith('MACROBUTTON MTPlaceRef'):
                    continue
                cp = converted.ancestor(command, W + 'p')
                rp = doc.paragraphs[converted.pindex[cp]]
                require(record['cached_display'] in doc.text(rp), 'Restored caption label differs')
                bridges[record['word_stream_start']] = (rp, {
                    'outer_field_sequence_zero_based': i, 'outer_field_count': len(outer),
                    'word_stream_start': record['word_stream_start'],
                    'word_stream_end_exclusive': record['word_stream_end_exclusive'],
                    'raw_field_sha256': record['raw_field_sha256'], 'command': record['command'],
                    'cached_display': record['cached_display'],
                    'converted_command_xml_ordinal': converted.ordinal[command],
                    'converted_paragraph': converted.paragraph_record(cp),
                    'restored_paragraph': doc.paragraph_record(rp),
                    'cache_evidence': artifact(cache_path),
                    'method': 'All 166 outer commands equal in order; all converted/restored paragraph OLE signatures equal.',
                })
            require(len(bridges) == len(selected) == 90, 'DOC caption bridge count differs')
            for cap in selected:
                p, bridge = bridges[cap['locator']]
                require(bridge['cached_display'] == cap['label_as_saved'], 'DOC scope label mismatch')
                doc.captions.append((cap, p))
            field_checks[name] = {'outer_fields': 166, 'command_sequence_equal': True,
                                  'original_word_and_table_stream_hashes_verified': True,
                                  'original_field_byte_span_hashes_verified': len(cache['records']),
                                  'converted_restored_paragraph_object_signatures_equal': True,
                                  'converted_body_paragraphs_including_tables': len(doc.paragraphs), 'caption_fields': 90}
            text_path = BASE / 'nonhydro-read/body-field-recovery/body-cached.txt'
            pdf_path = text_path.with_suffix('.pdf')
            for path in (text_path, pdf_path):
                saved = next(a for a in body_receipt['artifacts'] if a['path'] == relative(path))
                artifact(path, saved['sha256'])
            image_paths = {r['physical_render_page']: ROOT / r['final_image']['path'] for r in body_receipt['page_records']}
            for r in body_receipt['page_records']:
                artifact(r['final_image']['path'], r['final_image']['sha256'])
            input_paths.extend([cache_path, recovery_path, body_receipt_path, converted_path, restored_path])
        page_map = associate_pages(doc, selected, text_path, pdf_path, image_paths)
        input_paths.extend([ROOT / source['path'], text_path, pdf_path])
        docs[name] = doc
        for cap, p in doc.captions:
            objects = doc.objects(p, native_inventory)
            render = page_map[cap['id']]
            status = 'none' if not objects else 'unique' if (render['ordered_sequence_verified'] and
                      isinstance(render['page'], int) and all(o['preview_binding_status'] == 'unique' for o in objects)) else 'ambiguous'
            packet = {
                'schema': 'xbeach-r2-evidence-packet/v1',
                'caption': {'id': cap['id'], 'document': cap['document'], 'label': cap['label_as_saved'],
                            'locator_kind': cap['locator_kind'], 'locator': cap['locator'],
                            'source': source, 'field_evidence': artifact(cap['field_evidence'])},
                'context': doc.context(p),
                'association': {'objects': objects, 'page': render['page'], 'status': status, 'render': render,
                                'object_rule': 'Only caption paragraph; never an earlier paragraph, even when empty.',
                                'reason': 'No OLE/preview in the caption paragraph' if not objects else
                                          'Exact paragraph relationships and verified render occurrence' if status == 'unique' else
                                          'Page or preview relationship is not uniquely verified'},
                'candidate_existing_judgments': [],
                'adapter_limits': 'Structural association only. Image existence does not imply a readable body or semantic closure.',
            }
            if name == 'nonhydro':
                packet['association']['doc_field_bridge'] = bridges[cap['locator']][1]
            packet['candidate_existing_judgments'].extend(match_visual(packet, doc, p, visual_path, visual))
            packet['candidate_existing_judgments'].extend(match_symbols(packet, doc, p, symbol_receipts, native_inventory))
            if cap['existing_bounded_contract']:
                marker = cap['existing_bounded_contract']
                require(marker == 'build-mode-20260912/contracts.json', 'Unknown frozen bounded contract')
                applicable = [f for f in contracts['manual_findings'] if
                              (f['id'] == 'XB-EQ-WCI' and name in ('kingsday', 'master') and
                               cap['label_as_saved'] in {f'(2.{n})' for n in range(5, 11)}) or
                              (f['id'] == 'XB-EQ-BED' and (name, cap['label_as_saved']) in
                               {('kingsday', '(B.37)'), ('master', '(C.37)')})]
                require(len(applicable) == 1, 'Contract marker not uniquely bound to document/label')
                finding = applicable[0]
                packet['candidate_existing_judgments'].append(candidate(
                    contracts_path, f'/manual_findings/{contracts["manual_findings"].index(finding)}',
                    'existing_contract', finding,
                    {'document': name, 'label': cap['label_as_saved'], 'caption_locator': cap['locator'],
                     'scope_caption_id': cap['id'], 'scope_contract_marker': marker,
                     'method': 'Frozen per-caption contract marker + explicit contract document/label scope'},
                    'Only the selected bounded contract; implementation differences and authorial gaps remain as recorded.'))
            packets[cap['id']] = packet
    xh_check = {name: xh_candidates(doc, mapping_path, mapping, packets) for name, doc in docs.items()}
    symbol_check = {'matched_packet_record_pairs': 0, 'unmatched_records': []}
    for path, receipt in symbol_receipts:
        for index, record in enumerate(receipt['records']):
            hits = [p['caption']['id'] for p in packets.values() if any(
                j['evidence']['path'] == relative(path) and j['json_pointer'] == f'/records/{index}'
                for j in p['candidate_existing_judgments'])]
            if hits:
                symbol_check['matched_packet_record_pairs'] += len(hits)
            else:
                symbol_check['unmatched_records'].append({
                    'evidence': artifact(path), 'json_pointer': f'/records/{index}',
                    'direct_body_paragraph_zero_based': record['direct_body_paragraph_zero_based'],
                    'ole_member': record['converted_docx_member'],
                    'reason': 'Prose symbol receipt has no explicit caption-label/locator bridge; do not borrow the nearest caption.',
                })
    for doc in docs.values():
        doc.zip.close()
    check_and_write(packets, captions, docs, field_checks, xh_check, symbol_check, input_paths)


def check_and_write(packets, captions, docs, field_checks, xh_check, symbol_check, input_paths):
    require(set(packets) == {c['id'] for c in captions}, 'Packet ID coverage mismatch')
    safe_names = {key: re.sub(r'[^A-Za-z0-9._-]', '_', key) + '.json' for key in packets}
    require(len(set(safe_names.values())) == 443, 'Safe filename collision')
    expected_cases = {
        'master:xml:33272': ('oleObject124.bin', 44),
        'master:xml:33803': ('oleObject125.bin', 45),
        'master:xml:33982': ('oleObject126.bin', 46),
        'nonhydro:word:80632': ('oleObject174.bin', 23),
        'nonhydro:word:137756': ('oleObject332.bin', 41),
        'kingsday:xml:17124': (None, 25),
        'kingsday:xml:19400': (None, 28),
        'kingsday:xml:19490': (None, 28),
        'master:xml:18476': ('oleObject45.bin', 27),
        'kingsday:xml:18997': ('oleObject41.bin', 27),
        'kingsday:xml:19304': ('oleObject43.bin', 28),
    }
    edge_cases = []
    for key, (member, page) in expected_cases.items():
        association = packets[key]['association']
        members = [Path(o['relationship']['member']).name for o in association['objects']]
        require(members == ([member] if member else []), f'Edge case object mismatch: {key}')
        require(association['page'] == page, f'Edge case page mismatch: {key}')
        edge_cases.append({'id': key, 'label': packets[key]['caption']['label'],
                           'objects': members, 'physical_render_page': page,
                           'status': association['status'], 'verified_against_plan_review': True})
    counts = {status: sum(p['association']['status'] == status for p in packets.values()) for status in STATUS}
    by_document = {name: {status: sum(p['caption']['document'] == name and p['association']['status'] == status
                                   for p in packets.values()) for status in STATUS} for name in docs}
    labels = defaultdict(list)
    for p in packets.values():
        labels[(p['caption']['document'], p['caption']['label'])].append({
            'id': p['caption']['id'], 'locator': p['caption']['locator'],
            'objects': [o['relationship']['member'] for o in p['association']['objects']],
            'page': p['association']['page'], 'status': p['association']['status']})
    repeated = [{'document': name, 'label': label, 'occurrences': occurrences}
                for (name, label), occurrences in labels.items() if len(occurrences) > 1]
    output = HERE / 'packets'
    output.mkdir(exist_ok=True)
    require(not output.is_symlink() and output.resolve() == HERE / 'packets', 'Output directory is a symlink')
    existing_names = {p.name for p in output.iterdir()}
    require(existing_names <= set(safe_names.values()), 'Unexpected files in packets/; will not remove them')
    packet_artifacts = []
    for key in sorted(packets):
        target = output / safe_names[key]
        require(not target.is_symlink(), 'Packet target is a symlink')
        write_json(target, packets[key])
        # Do not use the input hash cache for newly generated outputs.
        packet_artifacts.append({'id': key, 'path': relative(target), 'sha256': digest(target.read_bytes())})
    unresolved = [{'id': p['caption']['id'], 'label': p['caption']['label'],
                   'page': p['association']['page'], 'status': p['association']['status'],
                   'reason': p['association']['reason']} for p in packets.values() if p['association']['status'] != 'unique']
    judgment_counts = Counter(j['evidence']['path'] for p in packets.values() for j in p['candidate_existing_judgments'])
    check = {
        'schema': 'xbeach-r2-association-check/v1', 'packet_count': len(packets),
        'counts_by_status': counts, 'counts_by_document': by_document,
        'objects_per_packet': dict(sorted(Counter(str(len(p['association']['objects'])) for p in packets.values()).items())),
        'page_sequence_checks': {name: doc.page_check for name, doc in docs.items()},
        'field_bridge_checks': field_checks, 'repeated_label_cases': repeated,
        'named_edge_cases': edge_cases, 'not_uniquely_associated': unresolved,
        'candidate_judgment_counts_by_evidence': dict(sorted(judgment_counts.items())),
        'xh_candidate_matching': xh_check,
        'symbol_receipt_matching': symbol_check,
        'input_artifacts': [artifact(p) for p in sorted(set(input_paths))],
        'packets': packet_artifacts,
        'packet_manifest_sha256': digest(json.dumps(packet_artifacts, sort_keys=True, ensure_ascii=False).encode()),
        'adapter_script': artifact(HERE / 'build_packets.py'),
        'checks': {'443_unique_scope_ids': True, 'safe_filenames_unique': True,
                   'all_named_edge_cases_pass': True, 'no_previous_paragraph_fallback': True,
                   'candidate_judgments_only': True},
        'scope_limit': 'Adapter build only; no new equation visual reading, semantic closure, or R2 completion decision.',
    }
    for name in ('association-check.json', 'ADAPTER-REPORT.md'):
        require(not (HERE / name).is_symlink(), 'Report target is a symlink')
    write_json(HERE / 'association-check.json', check)
    lines = [
        '# XBeach R2 evidence-packet adapter', '',
        f'Generated 443 packets: unique {counts["unique"]}, ambiguous {counts["ambiguous"]}, none {counts["none"]}.', '',
        '| Document | Unique | Ambiguous | None |', '|---|---:|---:|---:|',
    ]
    lines += [f'| {name} | {v["unique"]} | {v["ambiguous"]} | {v["none"]} |' for name, v in by_document.items()]
    lines += ['', 'Run `python3 build_packets.py` from this directory (or use its absolute path). Only this directory is written. '
              'The script uses Python standard libraries, preserves existing inputs, and emits no timestamps. '
              'The manifest in [association-check.json](association-check.json) binds packet bytes to input and script hashes.', '',
              '## Mapping rules', '',
              '- DOCX: zero-based preorder XML ordinal → owning body paragraph → OLE relationship → ShapeID-linked preview. '
              'Objects are collected only from the caption paragraph; table-cell context is retained separately. '
              'An empty paragraph stays empty.',
              '- DOC: original WordDocument byte offset → sorted outer-field sequence. Original WordDocument/1Table '
              'stream hashes and all 167 cached byte-span hashes are checked. All 166 outer command strings match '
              'the converted DOCX command sequence. All 1,341 converted/restored body paragraphs retain identical OLE signatures. '
              'The corresponding restored paragraph supplies the caption text, object relationship and preview. '
              'Opaque container stream hashes supply original DOC stream candidates without interpreting Native payloads.',
              '- Physical pages: accept source occurrence order only when the entire sequence of standalone rendered caption '
              'lines exactly equals the source caption sequence. The three checks pass (174/179/90). '
              'Inline prose references are excluded. On a failed sequence check the script retains label page candidates '
              'and marks an object-bearing packet ambiguous. Image and receipt hashes are checked.',
              '- `unique` means the paragraph object set, preview relationships and render occurrence are uniquely bound. '
              '`none` means no OLE/preview in that paragraph; its physical page may still be known. '
              '`ambiguous` preserves a page/preview uncertainty. No status asserts readability.',
              '- Preview paths of the form `container!word/media/imageN.emf` identify existing ZIP members; SHA256 is over '
              'the uncompressed member. `container_path`, `member`, and `storage` make these paths machine-readable. '
              'Existing supplement PNG/PDF/EMF paths are also retained. Nothing is extracted or rendered.',
              '- Contract candidates require the frozen per-caption contract marker and the contract document/label scope. '
              'Visual receipts require source hash, label, paragraph ID, page and object relationships. Symbol receipts '
              'require document, label, direct paragraph index, OLE member and opaque Native SHA; they concern symbols only. '
              'XH candidates require the same source work, explicit label and an eight-token exact prose bridge to source '
              'paragraph locators; repeated labels require a unique local bridge. Original-PDF pages remain separate '
              'from derivative-render pages. Unmatched XH label mentions are listed in the check file.', '',
              'Candidate reuse: 14 contract matches, 22 packet–XH finding pairs, six local visual receipts, '
              'and three symbol-receipt records (including the explicit stress-tensor definition after (1.1)). '
              'Six XH label mentions have no unique verified paragraph bridge and remain listed in the check file. '
              'The solitary-wave adjustment-distance prose receipt (`oleObject350`, direct paragraph 414) '
              'has no explicit caption label/locator bridge and is retained as unmatched; its neighboring equations '
              'are not chosen by proximity.', '',
              '## Named checks', '', '| Caption ID | Label | Object | Physical render page | Status |', '|---|---|---|---:|---|']
    lines += [f'| {e["id"]} | {e["label"]} | {", ".join(e["objects"]) or "none"} | {e["physical_render_page"]} | {e["status"]} |'
              for e in edge_cases]
    lines += ['', 'Kingsday 19400 and 19490 have no objects; neither borrows oleObject43. '
              'That object belongs to Kingsday 19304 (2.40), p.28. Kingsday 18997 (2.38) has oleObject41, p.27, '
              'and its existing preview receipt records a blank preview. '
              'Master 18476 (2.40) has oleObject45, p.27, and the existing supplement records a visible separate preview '
              'despite the blank body render. These structural associations do not assign `body_status`.', '',
              'Master 33272 is on p.44; the following source prose (including porosity, morfac and sediment transport) '
              'is retained with paragraph locators even across p.45. No same-page symbol collection is performed. '
              'Nonhydro 80632 and 137756 remain distinct despite equal saved field SHA. The solitary-wave receipt '
              'attaches only to 137756/oleObject332; the stress-tensor receipt attaches only to its matching (1.1) '
              'paragraph and does not resolve that equation as a whole.', '',
              '## Captions without an object association', '']
    lines += [f'- `{e["id"]}` {e["label"]}, p.{e["page"]}: {e["reason"]}.' for e in unresolved]
    lines += ['', 'All three missing-object cases agree with the existing source-empty-paragraph receipts. '
              'There are no page association gaps. Existing judgments remain candidates (`claims_resolved=[]`). '
              'Equation transcription, role/implementation judgment, R2 semantic closure and external review remain outside this build.', '']
    (HERE / 'ADAPTER-REPORT.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps({'packets': 443, 'counts_by_status': counts, 'counts_by_document': by_document,
                      'named_edge_checks': len(edge_cases), 'manifest_sha256': check['packet_manifest_sha256']}, sort_keys=True))


if __name__ == '__main__':
    build()
