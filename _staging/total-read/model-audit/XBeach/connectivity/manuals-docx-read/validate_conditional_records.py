"""Validate diagnostics without promoting source exceptions to resolved."""
import io
import json
import zipfile
import olefile
from inspect_conditional_records import inspect
from probe_conditional_records import build


def validate(root,folder):
    r=json.loads((folder/'native-conditional-probe.json').read_text());checks=[]
    def check(n,v):checks.append({'check':'conditional-'+n,'pass':bool(v)})
    check('reproduction',build()==r)
    check('exact-scope',len(r['records'])==20 and sum(x['diagnostic_options']['embedded_ruler_without_tag'] for x in r['records'])==8 and sum(x['diagnostic_options']['retain_zero_color'] for x in r['records'])==12)
    examples={}
    for i,x in enumerate(r['records']):
        with zipfile.ZipFile(root/x['source']['path']) as z:
            with olefile.OleFileIO(io.BytesIO(z.read(x['member']))) as o:b=o.openstream('Equation Native').read()
        offset=x['body_offset'];options=x['diagnostic_options']
        try:inspect(b,offset);rejected=False
        except ValueError:rejected=True
        check(str(i)+'-strict-still-rejects',rejected)
        def nodes(seq):
            for n in seq:
                yield n
                if 'ruler' in n:yield n['ruler']
                yield from nodes(n.get('children',[]))
        d=x['decoded'];markers=list(nodes(d['tree']))
        check(str(i)+'-explicit-unresolved',x['status']=='conditional-structure-only-unresolved-source-exception' and
              (any(n.get('tag_omitted_in_source') for n in markers) if options['embedded_ruler_without_tag'] else any(n.get('unresolved_color_reference') for n in markers)))
        examples.setdefault(x['prior_error'],(b,offset,options))
    for error,(b,offset,options) in examples.items():
        def rejects(data):
            try:inspect(data,offset,**options)
            except (ValueError,UnicodeError):return True
            return False
        check(error+'-truncations',all(rejects(b[:i]) for i in range(len(b))) and rejects(b+b'\x00'))
    check('no-approval',r['whole_model_read_gate']=='NOT_PASSED' and r['human_approval_issued'] is False)
    return checks
