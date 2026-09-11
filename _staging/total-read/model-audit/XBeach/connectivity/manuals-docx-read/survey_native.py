"""Mechanical applicability survey; success is not semantic or visual approval."""
import collections
import hashlib
import io
import json
from pathlib import Path
import zipfile
import olefile
from lxml import etree as E
from inspect_glyph_records import inspect

FOLDER = Path(__file__).resolve().parent
ROOT = FOLDER.parents[5]
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
      'w14': 'http://schemas.microsoft.com/office/word/2010/wordml'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def artifact(p):
    return {'path': str(p.relative_to(ROOT)), 'sha256': sha(p.read_bytes())}


def build():
    records = []
    for name in ('kingsday', 'master'):
        source = ROOT / ('models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_' + name + '.docx')
        with zipfile.ZipFile(source) as z:
            for member in sorted(n for n in z.namelist() if n.startswith('word/embeddings/')):
                blob = z.read(member)
                with olefile.OleFileIO(io.BytesIO(blob)) as ole:
                    native = ole.openstream('Equation Native').read()
                item = {'document': name, 'source': artifact(source), 'member': member,
                        'ole_sha256': sha(blob), 'native_sha256': sha(native), 'native_bytes': len(native)}
                try:
                    decoded = inspect(native)
                    item.update(status='mechanically-accepted-not-semantically-reviewed',
                                character_count=len(decoded['characters']),
                                decoded_sha256=sha(json.dumps(decoded, sort_keys=True, ensure_ascii=False).encode()))
                except (ValueError, UnicodeError) as exc:
                    item.update(status='rejected-by-bounded-reader', reason=str(exc))
                records.append(item)
            if name == 'kingsday':
                document = E.fromstring(z.read('word/document.xml'))
                p = document.xpath('//w:p[@w14:paraId="441D49D0"]', namespaces=NS)[0]
                num = E.fromstring(z.read('word/numbering.xml'))
                n = num.xpath('./w:num[@w:numId="18"]', namespaces=NS)[0]
                aid = n.find('w:abstractNumId', NS).get('{'+NS['w']+'}val')
                abstract = num.xpath('./w:abstractNum[@w:abstractNumId="'+aid+'"]', namespaces=NS)[0]
                level = abstract.xpath('./w:lvl[@w:ilvl="1"]', namespaces=NS)[0]
                bullet = {'source': artifact(source), 'paragraph_id': '441D49D0',
                          'paragraph_xml': E.tostring(p).decode(), 'num_xml': E.tostring(n).decode(),
                          'abstract_xml': E.tostring(abstract).decode(),
                          'text_nodes': p.xpath('.//w:t/text()', namespaces=NS),
                          'level_format': level.find('w:numFmt', NS).get('{'+NS['w']+'}val'),
                          'level_text': level.find('w:lvlText', NS).get('{'+NS['w']+'}val')}
    visual = json.loads((FOLDER/'full-visual-read/receipt.json').read_text())
    bullet['viewed_page'] = next(a for a in visual['records'][0]['page_records'] if a['physical_render_page']==15)
    return {'date': '2026-09-11', 'attribution': 'AI mechanical survey and source XML analysis',
            'decoder': artifact(FOLDER/'inspect_glyph_records.py'),
            'prefix_decoder': artifact(FOLDER/'inspect_empty_native.py'),
            'records': records, 'counts': dict(collections.Counter(r['status'] for r in records)),
            'rejection_reasons': dict(collections.Counter(r['reason'] for r in records if 'reason' in r)),
            'kingsday_page15': bullet,
            'limitations': ['Fixed body offset 220 and existing supported record subset only.',
                            'Mechanical acceptance does not establish formula semantics, glyph fidelity or human review.',
                            'Rejection can indicate an unsupported prefix/layout; it is not proof of source corruption.'],
            'whole_model_read_gate': 'NOT_PASSED', 'human_approval_issued': False}


if __name__ == '__main__':
    result = build()
    (FOLDER/'native-survey.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('counts', 'rejection_reasons')}, ensure_ascii=False))
    print(json.dumps({k: result['kingsday_page15'][k] for k in ('text_nodes','level_format','level_text')}))
