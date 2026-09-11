"""Bounded embellishment parser regression and malformed-input checks."""
import io
import json
import zipfile
import olefile
from inspect_embell_records import inspect
from inspect_glyph_records import inspect as old_inspect
from survey_native_embell import build


def validate(root, folder):
    r=json.loads((folder/'native-embell-survey.json').read_text())
    sources=json.loads((folder/'native-survey.json').read_text())['records']
    checks=[]
    def check(name,v): checks.append({'check':'embell-'+name,'pass':bool(v)})
    check('reproduction',build()==r)
    check('complete-set',len(r['records'])==486 and len({(x['document'],x['member']) for x in r['records']})==486)
    old_equal=True; examples={}
    for x in r['records']:
        if x['status']!='mechanically-accepted-not-semantically-reviewed': continue
        a=next(a for a in sources if (a['document'],a['member'])==(x['document'],x['member']))
        with zipfile.ZipFile(root/a['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(a['member']))) as ole: b=ole.openstream('Equation Native').read()
        if x['prior_status']==x['status']:
            old_equal &= inspect(b,x['body_offset'])==old_inspect(b,x['body_offset'])
        else:
            for c in x['embellished_characters']:
                for e in c['embellishments']:
                    if e['tag']==6: examples.setdefault(e['embellishment_type'],(b,x['body_offset']))
    check('all-prior-accepted-identical',old_equal and sum(x['prior_status']==x['status']=='mechanically-accepted-not-semantically-reviewed' for x in r['records'])==361)
    def rejects(b,offset):
        try: inspect(b,offset)
        except (ValueError,UnicodeError): return True
        return False
    for kind,(data,offset) in sorted(examples.items()):
        check('source-truncations-type-'+str(kind),all(rejects(data[:i],offset) for i in range(len(data))) and rejects(data+b'\x00',offset))
    # Independent byte fixture: LINE, CHAR a with over-right-arrow, list END,
    # line END, top-level END. Check ownership and exact byte boundaries.
    prefix=data[:offset]
    body=b'\x01\x00\x02\x01\x83a\x00\x06\x00\x0b\x00\x00\x00'
    d=inspect(prefix+body,offset);c=d['characters'][0]
    check('independent-arrow-fixture',len(d['characters'])==1 and c['mtcode']==97 and
          c['end_offset']==offset+11 and c['embellishments'][0]['embellishment_type']==11 and
          c['embellishments'][0]['offset']==offset+7)
    check('reject-nudge-and-unknown-type',rejects(prefix+body[:8]+b'\x08'+body[9:],offset) and
          rejects(prefix+body[:9]+b'\x01'+body[10:],offset))
    check('reject-non-embellishment-list',rejects(prefix+body[:7]+b'\x0a\x00\x00\x00',offset))
    check('reject-unknown-char-option',rejects(prefix+body[:3]+b'\x81'+body[4:],offset))
    check('no-approval',r['whole_model_read_gate']=='NOT_PASSED' and r['human_approval_issued'] is False)
    return checks
