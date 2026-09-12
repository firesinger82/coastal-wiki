"""Inspect model-generated include calls against the prior generation hashes."""
import hashlib,json,re,shutil,subprocess,sys,tempfile
from pathlib import Path
from index_calls import DEF, statements
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[5];SRC=ROOT/'models/XBeach/raw/source_code/trunk'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
prior=json.loads((HERE.parent/'build-mode-20260912/generation-probe.json').read_text())
build=json.loads((HERE.parent/'build-mode-20260912/build-map.json').read_text())
outputs={x['name']:x for x in prior['outputs']}
records=[]
with tempfile.TemporaryDirectory(prefix='xbeach-runtime-includes-') as td:
    tmp=Path(td)
    for x in prior['inputs']:
        p=ROOT/x['path'];assert sha(p)==x['sha256'],p
        target=tmp/p.relative_to(SRC);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
    run=subprocess.run([sys.executable,str(tmp/'scripts/generate.py')],capture_output=True,text=True,check=True)
    for p in sorted((tmp/'src/xbeachlibrary').glob('*.inc')):
        assert sha(p)==outputs[p.name]['sha256'],p.name
        definitions=[];calls=[];generic=[]
        for st in statements(p):
            text=st['text'];m=DEF.match(text)
            if m:definitions.append({'name':m[2].lower(),'kind':m[1].lower(),'line':st['line_start'],'declaration':text})
            m=re.match(r'module\s+procedure\s+(\w+)',text,re.I)
            if m:generic.append({'specific':m[1].lower(),'line':st['line_start']})
            for m in re.finditer(r'\bcall\s+(\w+)',text,re.I):
                calls.append({'symbol':m[1].lower(),'line_start':st['line_start'],'line_end':st['line_end'],
                              'statement':text,'cpp':st['cpp']})
        spec=next(x for x in build['generation'] if x['output']==p.name)
        records.append({'name':p.name,'sha256':sha(p),'bytes':p.stat().st_size,'template':spec['template'],
                        'template_sha256':spec['sha256'],'consumers':spec['consumers'],
                        'definitions':definitions,'generic_specifics':generic,'call_statements':calls})
result={'scope':'Model-generated include interface/call inventory, same 27 output hashes as prior probe',
        'prior_probe':{'path':str((HERE.parent/'build-mode-20260912/generation-probe.json').relative_to(ROOT)),
                       'sha256':sha(HERE.parent/'build-mode-20260912/generation-probe.json')},
        'inputs':prior['inputs'],'records':records,'human_approval_issued':False,
        'limits':['Generated-line locations bind to output SHA, template SHA and consumer include sites; they are not raw-source line numbers',
                  'A generic specific list does not prove per-call overload/type/guard compatibility',
                  'Generated declarations/macro interfaces are model scope; external library implementations not inspected']}
(HERE/'generated-links.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Reused generation hashes:',len(records),'includes;',sum(len(x['definitions']) for x in records),'generated definitions')
