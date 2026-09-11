"""Check report font-definition support against source and prior decoded results."""
import json
import olefile
from inspect_font_records import inspect
from inspect_future_records import inspect as old_inspect


def validate(root,folder,builder):
    receipt=json.loads((folder/'native-font-survey.json').read_text())
    prior=json.loads((folder/'native-survey.json').read_text())
    checks=[]
    def check(name,v):checks.append({'check':'report-font-'+name,'pass':bool(v)})
    check('reproduction',builder()==receipt)
    check('exact-388',len(receipt['records'])==388 and {tuple(r['stream']) for r in receipt['records']}=={tuple(r['stream']) for r in prior['records']})
    unchanged=True;selected=[]
    with olefile.OleFileIO(str(root/receipt['source']['path'])) as ole:
        for r,p in zip(receipt['records'],prior['records']):
            b=ole.openstream(r['stream']).read();offset=r['candidate_offsets'][0]
            if p['status']=='mechanically-parsed-not-semantically-reviewed':unchanged &= inspect(b,offset)==old_inspect(b,offset)
            else:selected.append((b,offset,r))
    check('prior-386-identical',unchanged and len(selected)==2)
    for b,offset,r in selected:
        d=inspect(b,offset);c=d['characters'][-1]
        check(r['stream'][1]+'-glyph',c['mtcode']==0xf093 and c['typeface']==-1 and c['font_position']==84 and d==r['private_glyph_structure'])
        def rejects(data):
            try:inspect(data,offset)
            except (ValueError,UnicodeError):return True
            return False
        check(r['stream'][1]+'-truncations',all(rejects(b[:i]) for i in range(len(b))) and rejects(b+b'\x00'))
    prefix=b[:offset]
    # Independent new encoding, font, and style definitions in a LINE.
    body=b'\x01\x00\x13Test\x00\x11\x06Demo\x00\x08\x06\x03\x02\x00\x7fa\x00\x00\x00'
    d=inspect(prefix+body,offset)['tree'][0]['children']
    check('independent-definitions',d[0]['encoding_index']==6 and d[1]['font_index']==6 and d[2]['character_style']==3 and d[3]['typeface']==-1)
    check('undefined-encoding',rejects(prefix+body.replace(b'\x11\x06',b'\x11\x07')))
    check('undefined-font-style',rejects(prefix+body.replace(b'\x08\x06',b'\x08\x07')))
    check('unsupported-style',rejects(prefix+body.replace(b'\x08\x06\x03',b'\x08\x06\x04')))
    check('no-approval',receipt['whole_model_read_gate']=='NOT_PASSED' and receipt['human_approval_issued'] is False)
    return checks
