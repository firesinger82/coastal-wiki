#!/usr/bin/env python3
"""Classify the frozen 456-file audit inventory without mutating approved artifacts."""
import collections, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
AUDIT = ROOT / '_staging/total-read/model-audit/XBeach'
SOURCE = ROOT / 'models/XBeach/raw/source_code'
OUT = AUDIT / 'closure'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def classify(path):
    """Component attribution is operational, not a copyright/authorship judgment."""
    p=Path(path); name=p.name.lower(); component='project-distribution'; origin='project-integration'; role='build-tooling'; reason='Distribution placement only: no upstream rule matched; authorship UNKNOWN, not an own-solver attribution'
    generated=name in {'makefile.in','aclocal.m4'} or p.suffix.lower() in {'.eps','.dll','.exe','.lib','.mod','.pyd','.jar','.msi','.zip','.manifest'}
    if '/mpich/' in path: component,origin,reason='mpich','vendor','Bundled MPICH distribution directory; COPYRIGHT/README and headers retained'
    elif '/netcdff90/' in path or '/netcdf/' in path: component,origin,reason='netcdf','vendor','Bundled netCDF Fortran interface or netCDF binary distribution directory'
    elif '/ftnunit/' in path and path.startswith('trunk/lib/'): component,origin,reason='ftnunit','vendor','Independent Deltares ftnunit framework; source header HeadURL points to delft3d utils_lgpl/ftnunit'
    elif '/findent/' in path: component,origin,reason='findent-integration','project-integration','Project wrapper scripts for external formatter; not formatter implementation'
    elif path.startswith('trunk/lib/') and '/all/' in path:
        component,origin,reason='bundled-support-runtime','vendor','Bundled HDF5/compression/Microsoft runtime filename and distribution path'
    elif path=='trunk/config/texinfo.tex': component,origin,reason='texinfo','vendor','Texinfo source identity and copyright header'
    elif path=='trunk/autogen.sh': component,origin,reason='arl-autogen','vendor','US Army Research Laboratory copyright at source lines 4-5'
    elif path in {'trunk/m4/libtool.m4','trunk/m4/ltoptions.m4','trunk/m4/ltsugar.m4','trunk/m4/ltversion.m4','trunk/m4/lt~obsolete.m4'}: component,origin,reason='libtool','vendor','Libtool macro identity/header'
    elif path=='trunk/m4/pkg.m4': component,origin,reason='pkg-config','vendor','pkg-config macro identity and Scott James Remnant copyright header'
    elif path in {'trunk/m4/acx_mpi.m4','trunk/m4/fortran.m4','trunk/m4/fortranextra.m4'}: component,origin,reason='external-fortran-mpi-macros','vendor','Reusable ACX_MPI/Fortran macro source headers; external authors or AC_FC_LINE_LENGTH contract'
    elif path=='trunk/aclocal.m4': component,origin,reason='autotools-aggregate','mixed','Generated aggregation of upstream macros and project includes'
    elif path.startswith('trunk/scripts/dist/') and name not in {'generate.exe','generate.exe.manifest'}: component,origin,reason='bundled-python-runtime','vendor','Bundled interpreter/modules; pyconfig.h identifies standard Python distribution'
    elif path in {'trunk/doc/doxygen/bin/doxygen.exe','trunk/doc/doxygen/bin/doxytag.exe','trunk/src/xbeach/build/7za.exe','trunk/config/pscp.exe'}: component,origin,reason='bundled-external-tools','vendor','Named external Doxygen/7-Zip/PuTTY binary; no XBeach implementation attribution'
    elif path in {'trunk/COPYING','trunk/LICENSE'}: component,origin,reason='license-text','vendor','External license document; not solver implementation'
    if component=='project-distribution' and path.startswith(('trunk/src/xbeachlibrary/','trunk/src/xbeach/','trunk/src/pybeach/','trunk/test/','trunk/doc/')):
        component='xbeach'; reason='Explicit XBeach source/test/document tree placement; operational component only, not legal authorship'
    if origin=='vendor': role='dependency-or-external-tool'
    elif path.startswith('trunk/src/xbeachlibrary/') and p.suffix.lower() in {'.f90','.def','.inp','.ind'}: role='solver-library'
    elif path.startswith('trunk/src/pybeach/'): role='python-interface'
    elif path.startswith('trunk/test/'): role='project-tests'
    elif path.startswith('trunk/doc/') or path=='trunk/lib/README.txt.txt': role='documentation'
    elif path.startswith('trunk/src/xbeach/') and p.suffix.lower()=='.f90': role='solver-driver'
    binary = p.suffix.lower() in {'.dll','.exe','.lib','.mod','.pyd','.jar','.msi','.zip'}
    form = 'binary' if binary else 'generated' if generated else 'authored'
    return dict(component=component,origin=origin,role=role,form=form,attribution_basis=reason, attribution_method=('unmatched-distribution-placement' if component=='project-distribution' else 'explicit-component-rule'), authorship_status='not-adjudicated', own_solver_count_eligible=(role in {'solver-library','solver-driver'} and component=='xbeach'))
def main():
    inventory=json.loads((AUDIT/'xb-inventory.json').read_text()); assert len(inventory)==456
    files=[]; by_path={}
    for row in sorted(inventory,key=lambda r:r['path']):
        source=SOURCE/row['path'];assert sha(source)==row['sha256'],row['path']
        item={'path':row['path'],'source_sha256':row['sha256'],**classify(row['path'])}
        component=item['component']
        refs={
          'mpich':('trunk/lib/x64/mpich/include/mpi.h',1,45),
          'netcdf':('trunk/lib/win32/netcdff90/netcdf.f90',1,30),
          'ftnunit':('trunk/lib/fortran/ftnunit/packages/ftnunit/src/ftnunit.f90',1,32),
          'texinfo':('trunk/config/texinfo.tex',1,40),
          'arl-autogen':('trunk/autogen.sh',1,30),
          'pkg-config':('trunk/m4/pkg.m4',1,24),
          'libtool':(row['path'],1,25),
          'external-fortran-mpi-macros':(row['path'],1,40),
          'autotools-aggregate':('trunk/aclocal.m4',1,35),
          'bundled-python-runtime':('trunk/scripts/dist/Include/pyconfig.h',1,20),
        }
        evidence={'kind':'hashed-file-and-project-placement','path':row['path'],'source_sha256':row['sha256'],'basis':item['attribution_basis']}
        if component in refs:
            rp,a,b=refs[component];rf=SOURCE/rp;body=rf.read_text(errors='replace').split('\n')
            evidence.update(kind='component-header-and-distribution-path',header_path=rp,header_source_sha256=sha(rf),header_lines=f'{a}-{b}',header_quote='\n'.join(body[a-1:b]))
        item['class_evidence']=evidence
        files.append(item);by_path[item['path']]=item
    dispositions=[]
    for f in sorted((AUDIT/'cw/crosswalk').glob('*/*.crosswalk.json')):
        j=json.loads(f.read_text());assert j['source_path'] in by_path
        for index,d in enumerate(j['dispositions']):
            dispositions.append({'id':f"{j['shard']}:{j['source_path']}:{index}",'crosswalk_path':str(f.relative_to(ROOT)),'crosswalk_sha256':sha(f),'disposition_index':index,'source_path':j['source_path'],'source_sha256':j['source_sha256'],'base_ids':d.get('base_ids',[]),'audit_ids':d.get('audit_ids',[]),'historical_disposition':d['disposition'],'historical_adversarial_verdict':d.get('adversarial',{}).get('verdict'),**classify(j['source_path']),'class_evidence_file':j['source_path']})
    assert len(dispositions)==1472
    counts=lambda rows,key:dict(sorted(collections.Counter(r[key] for r in rows).items()))
    groups=collections.defaultdict(list)
    for r in files:groups[r['source_sha256']].append(r['path'])
    for r in files:r['byte_identical_mirrors']=[p for p in groups[r['source_sha256']] if p!=r['path']]
    data={'schema':'xbeach-attribution/v1','note':'Separate sidecar over immutable audit evidence. Counts are file/record counts, never unique defect counts. File-based operational attribution; no shard-based ownership. Text and binary/metadata inventory are distinguished in original P0 scope. Mixed aggregations are excluded from own-solver defect totals.','inventory_sha256':sha(AUDIT/'xb-inventory.json'),'file_count':len(files),'disposition_count':len(dispositions),'file_origins':counts(files,'origin'),'disposition_origins':counts(dispositions,'origin'),'disposition_by_component':counts(dispositions,'component'),'historical_adversarial_attachments':counts([d for d in dispositions if d['historical_adversarial_verdict'] is not None],'historical_adversarial_verdict'),'byte_identical_file_groups':[{'source_sha256':h,'paths':ps} for h,ps in groups.items() if len(ps)>1],'generated_source_pairs':[{'source':'trunk/lib/win32/netcdff90/Makefile.am','generated':'trunk/lib/win32/netcdff90/Makefile.in','note':'Same rules represented in source and generated form; two records do not imply two independent defects.'}],'files':files,'dispositions':dispositions}
    (OUT/'attribution.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k in ['file_count','disposition_count','file_origins','disposition_origins','historical_adversarial_attachments']},ensure_ascii=False))
if __name__=='__main__':main()
