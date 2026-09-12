"""Inventory checked XBeach build declarations and src roles, not a call-graph verifier."""
import collections,hashlib,json,posixpath,re,xml.etree.ElementTree as ET
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SRC=ROOT/'models/XBeach/raw/source_code/trunk'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text(p):
 raw=p.read_bytes()
 try:s=raw.decode('utf-8-sig')
 except UnicodeDecodeError:s=raw.decode('cp1252')
 return s.replace('\r\n','\n')
def evidence(p,a,b=None):
 raw=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'line_start':a,'line_end':b or a,'sha256':sha(p),'quote_exact_utf8':b'\n'.join(raw.split(b'\n')[a-1:b or a]).decode()}
def make_list(p,key):
 lines=text(p).splitlines();start=next(i for i,l in enumerate(lines) if re.match(re.escape(key)+r'\s*=',l));parts=[];i=start
 while True:
  line=lines[i].split('=',1)[1] if i==start else lines[i]
  parts+=line.replace('\\',' ').split()
  if not lines[i].endswith('\\'):break
  i+=1
 return parts,evidence(p,start+1,i+1)
allpaths={str(p.relative_to(SRC)).lower():p for p in SRC.rglob('*') if p.is_file()}
libmake=SRC/'src/xbeachlibrary/Makefile.am';exemake=SRC/'src/xbeach/Makefile.am'
lib,lib_ev=make_list(libmake,'libxbeach_la_SOURCES');exe,exe_ev=make_list(exemake,'xbeach_SOURCES');built,built_ev=make_list(libmake,'BUILT_SOURCES')
projects=[]
for p in sorted((SRC/'src').rglob('*.vfproj')):
 root=ET.fromstring(p.read_bytes());lines=text(p).splitlines();configs=[]
 for c in root.findall('./Configurations/Configuration'):
  keep={'PreprocessorDefinitions','AdditionalOptions','AdditionalIncludeDirectories','Preprocess','AdditionalDependencies','AdditionalLibraryDirectories','CommandLine','LinkLibraryDependencies'}
  tools={t.attrib['Name']:{k:v for k,v in t.attrib.items() if k in keep} for t in c.findall('Tool') if any(k in keep for k in t.attrib)}
  start=next(i+1 for i,l in enumerate(lines) if '<Configuration Name="'+c.attrib['Name']+'"' in l)
  configs.append({'name':c.attrib['Name'],'attributes':{k:v for k,v in c.attrib.items() if k in {'Name','UseCompiler','ConfigurationType','InheritedPropertySheets'}},'tools':tools,'line_start':start})
 files=[]
 for f in root.findall('.//Files//File'):
  raw=f.attrib['RelativePath'];rel=posixpath.normpath(str(p.parent.relative_to(SRC))+'/'+raw.replace('\\','/'));actual=allpaths.get(rel.lower())
  files.append({'declared_path':raw,'resolved_path':str(actual.relative_to(SRC)) if actual else None,'external_interface':not rel.startswith('src/'),'overrides':[c.attrib for c in f.findall('FileConfiguration')],'line':next(i+1 for i,l in enumerate(lines) if '<File RelativePath="'+raw+'"' in l)})
 projects.append({'path':str(p.relative_to(SRC)),'sha256':sha(p),'type':root.attrib.get('ProjectType','executable'),'configs':configs,'files':files})
domain_groups={
 'entry and lifecycle':'xbeach input libxbeach libxbeach_dynamic xbeach_bmi introspection demo',
 'wave boundary forcing':'boundaryconditions waveparams waveparamsnew wave_bc_nextgen wave_boundary_datastore wave_boundary_init wave_boundary_main wave_boundary_update',
 'wave propagation and breaking':'wave_timestep wave_functions wave_instationary wave_stationary_directions wave_stationary wave_directions roelvink',
 'flow and nonhydrostatic numerics':'flow_timestep flow_secondorder nonh solver wetcells vsm_u_XB',
 'sediment morphology and bottom friction':'morphevolution bedroughness beachwizard',
 'groundwater rainfall vegetation ships drifters':'groundwater rainfall vegetation ship drifters',
 'initialization external forcing and timestep':'initialize readtide readwind compute_tide_zs0 timestep',
 'output statistics logging':'output ncoutput varoutput postprocess varianceupdate logging debugging',
 'model MPI and domain transfer':'xmpi xmpinew general_mpi general_mpi_new',
 'state configuration and utilities':'spaceparams spaceparamsdef params paramsconst constants typesandkinds iso_c_utils filefunctions readkey getkey mnemonic mnemoniciso math_tools interp loopcounters sleeper'
}
domain_by_stem={name.lower():role for role,names in domain_groups.items() for name in names.split()}
solutions=[]
for p in sorted(SRC.glob('*.sln')):
 lines=text(p).splitlines();entries=[];cfg=[]
 for n,line in enumerate(lines,1):
  m=re.match(r'Project\("[^"]+"\) = "([^"]+)", "([^"]+\.vfproj)", "([^"]+)"',line)
  if m:
   end=next(i for i in range(n,len(lines)) if lines[i]=='EndProject')
   dependencies=[x.strip().split(' = ')[0] for x in lines[n:end] if re.match(r'\s*\{[^}]+\} = \{',x)]
   entries.append({'name':m[1],'project':m[2].replace('\\','/'),'guid':m[3],'line':n,'dependency_guids':dependencies})
  if re.match(r'\s*\{[^}]+\}\..*\.(ActiveCfg|Build\.0)\s*=',line):cfg.append({'line':n,'declaration':line.strip()})
 solutions.append({'path':p.name,'sha256':sha(p),'projects':entries,'configuration_mappings':cfg})
libset={'src/xbeachlibrary/'+n for n in lib};exeset={'src/xbeach/'+n for n in exe}
compiled=libset|exeset|{f['resolved_path'] for p in projects for f in p['files'] if f['resolved_path'] and not f['external_interface']}
roles=[];includes=[];modules=[]
for p in sorted((SRC/'src').rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(SRC));suffix=p.suffix.lower();name=p.name
 targets=[]
 if rel in libset:targets.append('autotools:libxbeach')
 if rel in exeset:targets.append('autotools:xbeach')
 targets += [proj['path'] for proj in projects if any(f['resolved_path']==rel for f in proj['files'])]
 anchor=[]
 if suffix=='.f90':
  role='compiled_fortran_unit' if targets else 'unlisted_fortran_unit'
  for n,line in enumerate(text(p).splitlines(),1):
   m=re.match(r'\s*(module|program)\s+(\w+)\b',line,re.I)
   if m and m[2].lower()!='procedure':anchor.append({'line':n,'kind':m[1].lower(),'name':m[2]})
   m=re.match(r'\s*(?:#\s*)?include\s*[\'\"]([^\'\"]+)',line,re.I)
   if m:includes.append({'consumer':rel,'line':n,'include':m[1],'consumer_listed':rel in compiled})
   m=re.match(r'\s*use\s+(\w+)\b',line,re.I)
   if m:modules.append({'consumer':rel,'line':n,'module':m[1].lower(),'consumer_listed':rel in compiled})
 elif suffix=='.mako':role='source_generation_template'
 elif suffix=='.vfproj' or name=='Makefile.am':role='build_declaration'
 elif suffix=='.exe':role='excluded_bundled_packaging_tool'
 elif suffix=='.bat':role='model_build_or_distribution_caller'
 elif suffix=='.py':role='python_wrapper_test' if '/test/' in rel else ('python_packaging' if name=='setup.py' else 'python_wrapper')
 elif name in ['params.def','variables.def']:role='source_generation_input'
 elif name in ['s.ind','s.inp','RFtable.inp']:role='legacy_state_or_lookup_data'
 elif name.startswith('version.') :role='build_version_input'
 elif name=='README.genfiles':role='historical_generation_directory_note'
 elif name=='setup.cfg':role='python_packaging'
 else:raise RuntimeError(('unmapped src file',rel))
 roles.append({'path':rel,'sha256':sha(p),'role':role,'build_targets':targets,'domain_role':domain_by_stem[p.stem.lower()] if suffix=='.f90' else role,'definition_anchors':anchor})
templates=sorted((SRC/'src/xbeachlibrary/templates').glob('*.mako'));generation=[]
for p in templates:
 inc=p.stem+'.inc';generation.append({'template':str(p.relative_to(SRC)),'sha256':sha(p),'output':inc,'declared_built_source':inc in built,'consumers':[i for i in includes if i['include']==inc]})
providers=collections.defaultdict(list)
for f in roles:
 for a in f['definition_anchors']:
  if a['kind']=='module':providers[a['name'].lower()].append(f['path'])
for m in modules:m['local_providers']=providers.get(m['module'],[])
result={'schema':'xbeach-build-mode-map/v1','source_root':str(SRC.relative_to(ROOT)),'scope':'All files under src plus checked root solutions/configure, not vendor internals; declarations are not executable reachability','human_approval_issued':False,'autotools':{'library_sources':lib,'executable_sources':exe,'built_sources':built,'evidence':[lib_ev,exe_ev,built_ev,evidence(SRC/'configure.ac',42,54),evidence(SRC/'configure.ac',71,80)],'configurations':[{'mpi':m,'netcdf':n,'defines':(['USEMPI','HAVE_MPI_WTIME'] if m else [])+(['USENETCDF'] if n else [])} for m in [False,True] for n in [False,True]]},'projects':projects,'solutions':solutions,'src_files':roles,'generation':generation,'module_use_index':modules,'include_index':includes,'limits':['Module USE index is lexical discovery, not routine-call reachability or mode/CPP evaluation; legacy non-UTF8 comments decoded with CP1252 and raw SHA preserved','Visual Fortran source filenames resolve case-insensitively; exclusions and per-project flags are retained','Windows frozen generator is only identified as a caller dependency, not executed or proven byte-equivalent to generate.py','Whole-model formula and runtime validation is not asserted']}
(HERE/'build-map.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'src_files':len(roles),'projects':len(projects),'project_configurations':sum(len(p['configs']) for p in projects),'solutions':len(solutions),'roles':dict(collections.Counter(f['role'] for f in roles)),'unlisted_fortran':[f['path'] for f in roles if f['role']=='unlisted_fortran_unit'],'generated_not_declared':[g['output'] for g in generation if not g['declared_built_source']],'compiled_includes_without_template':[i for i in includes if i['consumer_listed'] and i['include'].endswith('.inc') and i['include'] not in [g['output'] for g in generation]]},ensure_ascii=False,indent=2))
