"""Regenerate XBeach include files from an untouched temporary input copy."""
import argparse,hashlib,importlib.metadata,json,shutil,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SRC=ROOT/'models/XBeach/raw/source_code/trunk'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=[SRC/'scripts/generate.py',SRC/'src/xbeachlibrary/variables.def',SRC/'src/xbeachlibrary/params.def',*sorted((SRC/'src/xbeachlibrary/templates').glob('*.mako'))]
with tempfile.TemporaryDirectory(prefix='xbeach-generation-') as td:
 tmp=Path(td)
 for p in files:
  target=tmp/p.relative_to(SRC);target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,target)
 r=subprocess.run([sys.executable,str(tmp/'scripts/generate.py')],capture_output=True,text=True)
 result={'scope':'Unmodified source generator on copied inputs only; no solver build or Windows frozen-generator equivalence claim','python':sys.version.split()[0],'mako':importlib.metadata.version('Mako'),'markupsafe':importlib.metadata.version('MarkupSafe'),'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in files],'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'outputs':[{'name':p.name,'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted((tmp/'src/xbeachlibrary').glob('*.inc'))]}
 assert r.returncode==0,(r.returncode,r.stderr)
 assert {f['name'] for f in result['outputs']}=={p.stem+'.inc' for p in files if p.suffix=='.mako'}
(HERE/'generation-probe.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('Original generator completed:',len(result['outputs']),'include files; inputs unchanged')
