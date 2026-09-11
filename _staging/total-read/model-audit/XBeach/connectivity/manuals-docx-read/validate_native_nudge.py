"""Layout record regression, byte fixtures and malformed-input checks."""
import io
import json
import zipfile
import olefile
from inspect_nudge_records import inspect
from inspect_layout_records import inspect as old_inspect
from survey_native_nudge import build


def validate(root, folder):
    r=json.loads((folder/'native-nudge-survey.json').read_text())
    sources=json.loads((folder/'native-survey.json').read_text())['records']
    checks=[]
    def check(name,v): checks.append({'check':'nudge-'+name,'pass':bool(v)})
    check('reproduction',build()==r)
    check('complete-set',len(r['records'])==486 and len({(x['document'],x['member']) for x in r['records']})==486)
    old_equal=True; examples={}
    def tags(nodes):
        for n in nodes:
            yield n['tag']
            yield from tags(n.get('children',[]))
    for x in r['records']:
        if x['status']!='mechanically-accepted-not-semantically-reviewed':continue
        a=next(a for a in sources if (a['document'],a['member'])==(x['document'],x['member']))
        with zipfile.ZipFile(root/a['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(a['member']))) as ole:b=ole.openstream('Equation Native').read()
        d=inspect(b,x['body_offset'])
        if x['prior_status']==x['status']:old_equal &= d==old_inspect(b,x['body_offset'])
        else:
            examples.setdefault(x['body_offset'],(b,x['body_offset']))
    check('prior-459-identical',old_equal and sum(x['prior_status']==x['status']=='mechanically-accepted-not-semantically-reviewed' for x in r['records'])==459)
    def rejects(b,offset):
        try:inspect(b,offset)
        except (ValueError,UnicodeError):return True
        return False
    for tag,(data,offset) in examples.items():
        check('source-truncations-tag-'+str(tag),all(rejects(data[:i],offset) for i in range(len(data))) and rejects(data+b'\x00',offset))
    prefix=data[:offset]
    short=bytes([1,0,2,8,140,128,131,97,0,0,0])
    d=inspect(prefix+short,offset)['characters'][0]
    check('short-nudge-fixture',d['nudge']=={'dx':12,'dy':0,'encoding_bytes':2} and d['mtcode']==97)
    long=bytes([1,0,2,8,128,128,0,1,0,255,131,97,0,0,0])
    d=inspect(prefix+long,offset)['characters'][0]
    check('long-nudge-fixture',d['nudge']=={'dx':256,'dy':-256,'encoding_bytes':6} and d['mtcode']==97)
    line=bytes([1,12,140,128,64,0,2,0,131,97,0,0,0])
    d=inspect(prefix+line,offset)['tree'][0]
    check('line-nudge-spacing-order',d['nudge']['dx']==12 and d['line_spacing_raw']==64 and d['children'][0]['mtcode']==97)
    check('fixture-truncations',all(rejects(prefix+body[:i],offset) for body in (short,long,line) for i in range(len(body))))
    check('unknown-option',rejects(prefix+bytes([1,128,0,0]),offset))
    check('no-approval',r['whole_model_read_gate']=='NOT_PASSED' and r['human_approval_issued'] is False)
    return checks
