"""Source reproduction and future-record framing checks."""
import io
import json
import zipfile
import olefile
from probe_future_prefix import build
from inspect_future_prefix import inspect as prefix_inspect
from inspect_future_records import inspect


def validate(root,folder):
    r=json.loads((folder/'native-future-probe.json').read_text());checks=[]
    def check(n,v):checks.append({'check':'future-'+n,'pass':bool(v)})
    check('reproduction',build()==r)
    check('exact-members',[x['member'] for x in r['records']]==['word/embeddings/oleObject1.bin','word/embeddings/oleObject45.bin','word/embeddings/oleObject48.bin'])
    for x in r['records']:
        with zipfile.ZipFile(root/x['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(x['member']))) as o:data=o.openstream('Equation Native').read()
        def rejects(b):
            try:inspect(b,204)
            except (ValueError,UnicodeError):return True
            return False
        check(x['member']+'-framing',x['candidate_offsets']==[204] and
              x['opaque_records']==[{'offset':41,'tag':100,'opaque_payload_hex':'000000','payload_bytes':3,'interpretation':'uninterpreted future record','end_offset':46}])
        check(x['member']+'-truncations',all(rejects(data[:i]) for i in range(len(data))) and rejects(data+b'\x00'))
        check(x['member']+'-bad-length',rejects(data[:42]+b'\xff\xff\xff'+data[43:]))
    # Independent extended length field, exactly 255 preserved bytes.
    synthetic=data[:41]+b'\x64\xff\xff\x00'+bytes(255)+data[46:204]+b'\x00'
    d=prefix_inspect(synthetic,28)
    check('extended-length-fixture',d['records'][0]['payload_bytes']==255 and d['records'][0]['opaque_payload_hex']=='00'*255)
    check('no-approval',r['whole_model_read_gate']=='NOT_PASSED' and r['human_approval_issued'] is False)
    return checks
