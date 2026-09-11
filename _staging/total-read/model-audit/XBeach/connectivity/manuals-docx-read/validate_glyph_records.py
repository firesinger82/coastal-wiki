"""Reproduce four bounded MTEF reads and exercise malformed input rejection."""
import hashlib
import importlib.util
import io
import json
import zipfile
import olefile
from lxml import etree


def validate(root, folder):
    receipt = json.loads((folder / 'glyph-record-read/receipt.json').read_text())
    prior = json.loads((root / receipt['prior_receipt']['path']).read_text())
    checks = []

    def check(name, result):
        checks.append({'check': 'glyph-record-' + name, 'pass': bool(result)})

    def bound(a):
        return hashlib.sha256((root / a['path']).read_bytes()).hexdigest() == a['sha256']

    check('input-bindings', all(bound(receipt[k]) for k in ('prior_receipt', 'decoder', 'prefix_decoder')))
    spec = importlib.util.spec_from_file_location('glyph_reader', root / receipt['decoder']['path'])
    decoder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(decoder)
    check('selected-four', sorted(r['base'] for r in receipt['records']) == sorted(
        ['kingsday-2-5-0', 'master-2-5-0', 'kingsday-B-37-0', 'master-C-37-0']))

    def rejects(b):
        try:
            decoder.inspect(b)
        except (ValueError, UnicodeError):
            return True
        return False

    for item in receipt['records']:
        label = item['base']
        a = item['artifacts']
        previous = next(r for r in prior['preview_records'] if r['base'] == label)
        check(label + '-prior-binding', all(item[k] == previous[k] for k in
              ('source', 'ole_member', 'paragraph_id', 'ole_rid')) and
              all(a[k] == previous['artifacts'][k] for k in ('ole', 'paragraph')))
        check(label + '-hashes', bound(item['source']) and all(bound(v) for v in a.values()))
        with zipfile.ZipFile(root / item['source']['path']) as z:
            blob = z.read(item['ole_member'])
            rels = {n.get('Id'): n.get('Target') for n in etree.fromstring(z.read('word/_rels/document.xml.rels'))}
            check(label + '-relationship', 'word/' + rels[item['ole_rid']] == item['ole_member'])
        with olefile.OleFileIO(io.BytesIO(blob)) as ole:
            b = ole.openstream('Equation Native').read()
        decoded = decoder.inspect(b)
        check(label + '-reproduction', blob == (root / a['ole']['path']).read_bytes() and
              b == (root / a['native']['path']).read_bytes() and
              decoded == json.loads((root / a['decoded']['path']).read_text()))
        chars = decoded['characters']
        targets = [c for c in chars if c['mtcode'] in (8764, 97)]
        check(label + '-record-evidence', targets == item['selected_characters'])
        pile = decoded['tree'][0]
        lines = [n for n in pile['children'] if n['tag'] == 1]
        if '-2-5-' in label:
            check(label + '-tilde-values', [(c['offset'], c['mtcode'], c['typeface'], c.get('font_position'))
                  for c in targets] == [(322, 8764, 11, 58), (430, 8764, 11, 58)])
            templates = [next(n for n in line['children'] if n.get('offset') == off)
                         for line, off in zip(lines, (306, 414))]
            check(label + '-nested-placement', len(templates) == 2 and all(t['selector'] == 29 and
                  [n for n in t['children'] if n['tag'] == 1][1]['children'][0] == c
                  for t, c in zip(templates, targets)))
        else:
            direct = [[n for n in line['children'] if n['tag'] == 2] for line in lines]
            check(label + '-literal-a', [(c['offset'], c['mtcode'], c['typeface']) for c in targets] == [(469, 97, 3)])
            check(label + '-first-line-adjacency', [(c['offset'], c['mtcode']) for c in direct[0][-2:]] ==
                  [(464, 48), (469, 97)] and direct[1][-1]['mtcode'] == 48)
        check(label + '-all-truncations', all(rejects(b[:i]) for i in range(len(b))))
        check(label + '-trailing-and-unknown', rejects(b + b'\x00') and
              rejects(b[:220] + b'\x64' + b[221:]) and rejects(b[:221] + b'\x80' + b[222:]))
        changed = bytearray(b)
        changed[targets[0]['offset'] + 3:targets[0]['offset'] + 5] = b'b\x00'
        check(label + '-character-mutation', next(c for c in decoder.inspect(bytes(changed))['characters']
              if c['offset'] == targets[0]['offset'])['mtcode'] == 98)
    synthetic = b[:220] + b'\x01\x00\x02\x00\x83a\x00\x00\x00'
    d = decoder.inspect(synthetic)
    check('independent-simple-body', len(d['characters']) == 1 and d['characters'][0]['mtcode'] == 97 and
          d['tree'][0]['tag'] == 1 and d['tree'][-1]['end_offset'] == len(synthetic))
    check('no-approval', receipt['whole_model_read_gate'] == 'NOT_PASSED' and receipt['human_approval_issued'] is False)
    return checks
