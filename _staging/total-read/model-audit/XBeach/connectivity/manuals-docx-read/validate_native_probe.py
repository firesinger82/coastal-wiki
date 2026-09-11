"""Checks for the bounded no-body native-stream evidence."""
import hashlib
import importlib.util
import io
import json
import zipfile
from pathlib import Path

import olefile
from lxml import etree


def validate(root, folder):
    receipt = json.loads((folder / 'native-probe/receipt.json').read_text())
    checks = []

    def check(name, value):
        checks.append({'check': 'native-probe-' + name, 'pass': bool(value)})

    def sha(p):
        return hashlib.sha256(p.read_bytes()).hexdigest()

    def bound(a):
        return sha(root / a['path']) == a['sha256']

    check('prior-and-decoder', all(bound(receipt[k]) for k in ('prior_visual_receipt', 'decoder')))
    spec = importlib.util.spec_from_file_location('bounded_empty_native', root / receipt['decoder']['path'])
    decoder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(decoder)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
          'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
          'o': 'urn:schemas-microsoft-com:office:office', 'v': 'urn:schemas-microsoft-com:vml',
          'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
    empty = receipt['empty_native_records']
    previews = receipt['preview_records']
    check('selected-counts', len(empty) == 5 and len(previews) == 10)
    check('selected-empty-members', sorted((Path(x['source']['path']).stem, x['ole_member']) for x in empty) == sorted(
        [('XBeach_manual_kingsday', 'word/embeddings/oleObject' + str(i) + '.bin') for i in (41, 124, 153)] +
        [('XBeach_manual_master', 'word/embeddings/oleObject' + str(i) + '.bin') for i in (134, 163)]))
    natives = []
    for index, item in enumerate(empty + previews):
        label = str(index)
        a = item['artifacts']
        check(label + '-hashes', bound(item['source']) and all(bound(x) for x in a.values()))
        with zipfile.ZipFile(root / item['source']['path']) as z:
            rels = {n.get('Id'): n.get('Target') for n in etree.fromstring(z.read('word/_rels/document.xml.rels'))}
            p = etree.fromstring(z.read('word/document.xml')).xpath(
                '//w:p[@w14:paraId="' + item['paragraph_id'] + '"]', namespaces=ns)[0]
            rid = item['ole_relationship'] if index < 5 else item['ole_rid']
            blob = z.read(item['ole_member'])
            check(label + '-source-binding', 'word/' + rels[rid] == item['ole_member'] and
                  rid in p.xpath('.//o:OLEObject/@r:id', namespaces=ns) and
                  etree.tostring(p) == (root / a['paragraph']['path']).read_bytes() and
                  blob == (root / a['ole']['path']).read_bytes())
            if index < 5:
                with olefile.OleFileIO(io.BytesIO(blob)) as ole:
                    native = ole.openstream('Equation Native').read()
                natives.append(native)
                check(label + '-native-reproduction', native == (root / a['native']['path']).read_bytes() and
                      decoder.inspect(native, 28) == json.loads((root / a['decoded']['path']).read_text()))
            else:
                check(label + '-preview-binding', 'word/' + rels[item['preview_rid']] == item['preview_member'] and
                      item['preview_rid'] in p.xpath('.//v:imagedata/@r:id', namespaces=ns) and
                      z.read(item['preview_member']) == (root / a['preview']['path']).read_bytes())
    check('identical-mtef-body', len({b[28:] for b in natives}) == 1)
    b = natives[0]

    def rejects(data, offset=28):
        try:
            decoder.inspect(data, offset)
        except (ValueError, UnicodeError):
            return True
        return False

    check('reject-all-truncations', all(rejects(b[:i]) for i in range(len(b))))
    check('reject-trailing-bytes', rejects(b + b'\x00') and rejects(b + b'\x02\x00\x83a\x00'))
    check('reject-inserted-body-and-unknown-records', all(rejects(b[:-1] + bytes([tag]) + b'\x00')
          for tag in (1, 2, 3, 4, 5, 6, 20, 100)))
    check('reject-wrong-version-and-offset', rejects(b[:28] + b'\x03' + b[29:]) and rejects(b, 27))
    check('reject-unknown-options', rejects(b[:39] + b'\x02' + b[40:]) and
          rejects(b[:115] + b'\x01' + b[116:]))
    check('read-contact-hash', bound(receipt['viewed_contact_sheet']))
    check('no-whole-model-or-human-pass', receipt['whole_model_read_gate'] == 'NOT_PASSED' and
          receipt['human_approval_issued'] is False)
    return checks


if __name__ == '__main__':
    folder = Path(__file__).resolve().parent
    result = validate(folder.parents[5], folder)
    print(json.dumps({'checks': len(result), 'pass': all(x['pass'] for x in result),
                      'failed': [x['check'] for x in result if not x['pass']]}))
