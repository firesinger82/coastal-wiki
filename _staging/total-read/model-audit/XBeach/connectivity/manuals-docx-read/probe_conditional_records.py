"""Diagnostic parsing of source exceptions, retaining unresolved interpretations."""
import io
import json
import zipfile
import olefile
from inspect_conditional_records import inspect
from survey_native import ROOT,FOLDER,artifact,sha


def build():
    prior=json.loads((FOLDER/'native-nudge-survey.json').read_text())
    sources=json.loads((FOLDER/'native-survey.json').read_text())['records']
    result=[]
    for item in prior['records']:
        if item['status']!='unsupported-body':continue
        a=next(a for a in sources if (a['document'],a['member'])==(item['document'],item['member']))
        with zipfile.ZipFile(ROOT/a['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(a['member']))) as o:data=o.openstream('Equation Native').read()
        options={'embedded_ruler_without_tag':item['reason']=='expected ruler',
                 'retain_zero_color':item['reason']=='undefined color reference'}
        r={'source':a['source'],'member':item['member'],'native_sha256':sha(data),'body_offset':item['body_offset'],
           'prior_error':item['reason'],'diagnostic_options':options}
        try:
            r['decoded']=inspect(data,item['body_offset'],**options)
            r['status']='conditional-structure-only-unresolved-source-exception'
        except (ValueError,UnicodeError) as exc:r.update(status='unsupported-body',error=str(exc))
        result.append(r)
    return {'date':'2026-09-11','attribution':'AI diagnostic interpretation; source exceptions not resolved',
            'prior_receipt':artifact(FOLDER/'native-nudge-survey.json'),'decoder':artifact(FOLDER/'inspect_conditional_records.py'),
            'generator':artifact(FOLDER/'probe_conditional_records.py'),'records':result,
            'whole_model_read_gate':'NOT_PASSED','human_approval_issued':False}

if __name__=='__main__':
    r=build();(FOLDER/'native-conditional-probe.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print([(x['member'],x['status'],x.get('error')) for x in r['records']])
