import importlib.util,json,hashlib,zipfile,io
from pathlib import Path
src=Path('_staging/total-read/model-audit/XBeach/closure/local-refutations/mpich-identity/extract_mpich_identity.py').resolve()
spec=importlib.util.spec_from_file_location('identity',src);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
base=Path('models/XBeach/raw/source_code');raw_by_sha={}
for p in base.rglob('*'):
 if p.is_file():raw_by_sha.setdefault(m.sha256(p.read_bytes()),[]).append(str(p))
result=[];scratch=Path('/tmp/xbeach-msi-all');scratch.mkdir(exist_ok=True)
for p in sorted(base.rglob('*.msi')):
 m.MSI=p;streams=m.read_streams();strings=m.read_string_table(streams);cols=m.read_columns(streams['!_Columns'],strings);rows=m.read_file_table(streams['!File'],strings,cols);labels={str(r['File']):str(r['FileName']).split('|')[-1] for r in rows};cabs=[(n,b) for n,b in streams.items() if b.startswith(b'MSCF')];assert len(cabs)==1
 try:contents=m.extract(cabs[0][1],labels)
 except AssertionError as e:
  print(p.name,'libarchive failed; cabextract fallback',e);contents={ident:(scratch/'ia32-cab'/ident).read_bytes() for ident in labels}
 records=[]
 for r in rows:
  ident=str(r['File']);b=contents[ident];assert len(b)==r['FileSize'];sha=m.sha256(b);target=scratch/p.stem/ident;target.parent.mkdir(exist_ok=True);target.write_bytes(b)
  records.append({'id':ident,'name':labels[ident],'bytes':len(b),'sha256':sha,'identical_raw_paths':raw_by_sha.get(sha,[]),'scratch_path':str(target),'semantic_status':'requires-read-evidence-reconciliation'})
 result.append({'path':str(p),'sha256':m.sha256(p.read_bytes()),'streams':[{'name':n,'bytes':len(b),'sha256':m.sha256(b)} for n,b in streams.items()],'members':records})
 print(p.name,'members',len(records),'same-raw',sum(bool(r['identical_raw_paths']) for r in records),'new',[(r['name'],r['bytes']) for r in records if not r['identical_raw_paths']])
Path('_staging/total-read/model-audit/XBeach/connectivity/msi-content-inventory.json').write_text(json.dumps({'method':'Read MSI OLE tables and every cabinet member; identity/size/hash checked, no installation. Inventory not semantic read.','archives':result},indent=2)+'\n')
