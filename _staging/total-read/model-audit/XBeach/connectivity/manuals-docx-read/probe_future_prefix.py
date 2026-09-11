"""Bounded future-prefix probe; opaque payloads remain unresolved."""
import collections
import io
import json
import zipfile
import olefile
from inspect_future_prefix import inspect as inspect_prefix
from inspect_future_records import inspect as inspect_body
from survey_native import FOLDER, ROOT, artifact, sha

def candidates(data):
    result = []
    # Explicit bounded search; each candidate must be a complete settings parse
    # ending in FULL. A matching byte alone is never sufficient.
    for offset in range(40, min(len(data), 513)):
        if data[offset-1] != 10:
            continue
        try:
            p = inspect_prefix(data[:offset] + b'\x00', 28)
        except (ValueError, UnicodeError):
            continue
        if p['records'][-2]['tag'] == 10 and any(r['tag'] == 18 for r in p['records']):
            result.append(offset)
    return result


def build():
    prior=json.loads((FOLDER/'native-nudge-survey.json').read_text())
    sources=json.loads((FOLDER/'native-survey.json').read_text())['records']
    records=[]
    for item in prior['records']:
        if item['status'] != 'unresolved-prefix': continue
        a=next(a for a in sources if (a['document'],a['member'])==(item['document'],item['member']))
        with zipfile.ZipFile(ROOT/a['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(a['member']))) as ole: native=ole.openstream('Equation Native').read()
        r={'source':a['source'],'member':item['member'],'native_sha256':sha(native),'candidate_offsets':candidates(native)}
        if len(r['candidate_offsets']) == 1:
            offset=r['candidate_offsets'][0]
            prefix=inspect_prefix(native[:offset]+b'\x00',28)
            r['opaque_records']=[x for x in prefix['records'] if x['tag']>=100]
            try:
                d=inspect_body(native,offset)
                r.update(status='body-parsed-with-opaque-prefix',decoded=d)
            except (ValueError,UnicodeError) as exc:
                r.update(status='body-unsupported-with-opaque-prefix',reason=str(exc))
        else:r['status']='unresolved-prefix'
        records.append(r)
    return {'date':'2026-09-11','attribution':'AI structural analysis; FUTURE payload interpretation remains unresolved',
            'prior_receipt':artifact(FOLDER/'native-nudge-survey.json'),
            'generator':artifact(FOLDER/'probe_future_prefix.py'),
            'prefix_decoder':artifact(FOLDER/'inspect_future_prefix.py'),
            'body_decoder':artifact(FOLDER/'inspect_future_records.py'),
            'records':records,'whole_model_read_gate':'NOT_PASSED','human_approval_issued':False}

if __name__=='__main__':
    r=build()
    (FOLDER/'native-future-probe.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print([(x['member'],x['candidate_offsets'],x['status'],x.get('reason'),x.get('opaque_records')) for x in r['records']])
