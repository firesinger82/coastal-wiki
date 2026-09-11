"""Find unique validated settings prefixes without adding body record support."""
import collections
import io
import json
import zipfile
import olefile
from inspect_nudge_records import inspect as inspect_body
from survey_native import FOLDER, ROOT, artifact, sha


def build():
    prior = json.loads((FOLDER/'native-layout-survey.json').read_text())
    sources = json.loads((FOLDER/'native-survey.json').read_text())['records']
    records = []
    for item in prior['records']:
        a = next(a for a in sources if (a['document'], a['member']) == (item['document'], item['member']))
        with zipfile.ZipFile(ROOT/a['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(a['member']))) as ole:
                native = ole.openstream('Equation Native').read()
        assert sha(native) == item['native_sha256']
        r = dict(item)
        r['prior_status'] = item['status']
        if 'body_offset' in item:
            try:
                d = inspect_body(native, item['body_offset'])
                r.pop('reason', None)
                r.update(status='mechanically-accepted-not-semantically-reviewed',
                         character_count=len(d['characters']),
                         embellished_characters=[c for c in d['characters'] if 'embellishments' in c],
                         decoded_sha256=sha(json.dumps(d, sort_keys=True, ensure_ascii=False).encode()))
            except (ValueError, UnicodeError) as exc:
                r.update(status='unsupported-body', reason=str(exc))
        records.append(r)
    return {'date':'2026-09-11', 'attribution':'AI bounded nudge analysis',
            'prior_receipt':artifact(FOLDER/'native-layout-survey.json'),
            'decoder':artifact(FOLDER/'inspect_nudge_records.py'),
            'generator':artifact(FOLDER/'survey_native_nudge.py'),
            'specification':{'url':'https://docs.wiris.com/en_US/mathtype-mtef-v5-mathtype-40-and-later',
                             'access':'Official indexed excerpts consulted 2026-09-11; not a full downloaded specification'},
            'records':records, 'counts':dict(collections.Counter(r['status'] for r in records)),
            'newly_accepted':sum(r['prior_status']=='unsupported-body' and r['status'].startswith('mechanically-accepted') for r in records),
            'limitations':['Nudge added for LINE/CHAR/TMPL/PILE and LINE spacing; matrices and embellishments with nudge remain unsupported.',
                           'No complete mathematical interpretation or rendering equivalence.',
                           'Existing decoders and receipts unchanged; unsupported options fail closed.'],
            'whole_model_read_gate':'NOT_PASSED','human_approval_issued':False}


if __name__ == '__main__':
    r=build()
    (FOLDER/'native-nudge-survey.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ('counts','newly_accepted')}))
