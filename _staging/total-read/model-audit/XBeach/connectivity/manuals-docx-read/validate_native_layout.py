"""Layout record regression, byte fixtures and malformed-input checks."""
import io
import json
import zipfile
import olefile
from inspect_layout_records import inspect
from inspect_embell_records import inspect as old_inspect
from survey_native_layout import build


def validate(root, folder):
    r=json.loads((folder/'native-layout-survey.json').read_text())
    sources=json.loads((folder/'native-survey.json').read_text())['records']
    checks=[]
    def check(name,v): checks.append({'check':'layout-'+name,'pass':bool(v)})
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
            for tag in set(tags(d['tree'])) & {5,9,15,16}:examples.setdefault(tag,(b,x['body_offset']))
    check('prior-441-identical',old_equal and sum(x['prior_status']==x['status']=='mechanically-accepted-not-semantically-reviewed' for x in r['records'])==441)
    def rejects(b,offset):
        try:inspect(b,offset)
        except (ValueError,UnicodeError):return True
        return False
    for tag,(data,offset) in examples.items():
        check('source-truncations-tag-'+str(tag),all(rejects(data[:i],offset) for i in range(len(data))) and rejects(data+b'\x00',offset))
    prefix=data[:offset]
    # Independent 1x1 matrix with a NULL cell, packed borders preserved.
    matrix=bytes([5,0,1,1,1,1,1,0,0,1,1,0,0])
    d=inspect(prefix+matrix,offset)['tree'][0]
    check('matrix-fixture',d['rows']==d['columns']==1 and d['children'][0]['options']==1 and d['end_offset']==offset+12)
    check('reject-matrix-count-and-options',rejects(prefix+matrix[:5]+b'\x02'+matrix[6:],offset) and rejects(prefix+b'\x05\x08'+matrix[2:],offset))
    color=bytes([16,0,0,0,232,3,0,0,15,1,0])
    d=inspect(prefix+color,offset)['tree']
    check('rgb-fixture',d[0]['rgb']==[0,1000,0] and d[1]['color_index']==1)
    check('reject-color-range-reference-options',rejects(prefix+color[:4]+b'\xff\xff'+color[6:],offset) and rejects(prefix+bytes([15,1,0]),offset) and rejects(prefix+bytes([16,8])+color[2:],offset))
    ruler=bytes([4,2,1,1,7,1,2,64,0,1,1,0,0])
    d=inspect(prefix+ruler,offset)['tree'][0]
    check('ruler-fixture',d['ruler']['stops']==[{'type':2,'offset':64}])
    check('reject-ruler-type',rejects(prefix+ruler[:6]+b'\x05'+ruler[7:],offset))
    sizes=bytes([9,0,130,9,100,1,0,1,9,101,0,254,0])
    d=inspect(prefix+sizes,offset)['tree']
    check('size-three-forms',d[0]['delta']==2 and d[1]['delta']==256 and d[2]['explicit_size_raw']==-512)
    check('no-approval',r['whole_model_read_gate']=='NOT_PASSED' and r['human_approval_issued'] is False)
    return checks
