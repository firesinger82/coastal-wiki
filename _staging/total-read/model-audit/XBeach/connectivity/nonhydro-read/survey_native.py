"""Mechanical native-stream survey of the original binary DOC, not semantic approval."""
import collections
import json
from pathlib import Path
import sys
import olefile
FOLDER=Path(__file__).resolve().parent
ROOT=FOLDER.parents[5]
sys.path.insert(0,str(FOLDER.parent/'manuals-docx-read'))
from probe_future_prefix import candidates
from inspect_future_records import inspect
from survey_native import artifact, sha


def build():
    source=ROOT/'models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.doc'
    records=[]
    with olefile.OleFileIO(str(source)) as ole:
        for stream in ole.listdir():
            if stream[-1]!='Equation Native':continue
            data=ole.openstream(stream).read()
            offsets=candidates(data)
            r={'stream':stream,'native_sha256':sha(data),'native_bytes':len(data),'candidate_offsets':offsets}
            if len(offsets)==1:
                try:
                    d=inspect(data,offsets[0])
                    r.update(status='mechanically-parsed-not-semantically-reviewed',character_count=len(d['characters']),
                             decoded_sha256=sha(json.dumps(d,sort_keys=True,ensure_ascii=False).encode()))
                except (ValueError,UnicodeError) as exc:r.update(status='unsupported-body',reason=str(exc))
            else:r.update(status='unresolved-prefix',header_hex=data[28:48].hex())
            records.append(r)
    return {'date':'2026-09-11','source':artifact(source),'generator':artifact(Path(__file__)),
            'prefix_decoder':artifact(FOLDER.parent/'manuals-docx-read/inspect_future_prefix.py'),
            'body_decoder':artifact(FOLDER.parent/'manuals-docx-read/inspect_future_records.py'),
            'candidate_finder':artifact(FOLDER.parent/'manuals-docx-read/probe_future_prefix.py'),
            'records':records,'counts':dict(collections.Counter(r['status'] for r in records)),
            'scope':'Original DOC Equation Native streams only; no semantics or preview fidelity approval.',
            'whole_model_read_gate':'NOT_PASSED','human_approval_issued':False}

if __name__=='__main__':
    r=build();(FOLDER/'native-survey.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(r['counts']))
