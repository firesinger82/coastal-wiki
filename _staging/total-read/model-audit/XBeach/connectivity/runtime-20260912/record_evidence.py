"""Bind reviewed source spans and classify interfaces without claiming reachability."""
import collections
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SRC = ROOT/'models/XBeach/raw/source_code/trunk/src/xbeachlibrary'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(name): return json.loads((HERE/name).read_text())
def dump(name, data): (HERE/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
def binding(p): return {'path': str(p.relative_to(ROOT)), 'sha256': sha(p)}

specs = {
    'variables.def': [(256,256)],
    'params.F90': [(70,79),(98,109)],
    'libxbeach.F90': [(171,184),(280,312)],
    'ship.F90': [(287,337),(365,373),(403,410)],
    'flow_timestep.F90': [(74,122),(131,149),(176,177),(563,580),(597,616),
                          (635,658),(706,719),(724,759)],
    'flow_secondorder.F90': [(686,824)],
    'nonh.F90': [(42,43),(201,247),(683,697),(1234,1262),(1411,1422),
                 (1446,1449),(1844,1883),(2162,2176),(2237,2241),(2858,2935)],
    'vegetation.F90': [(318,345),(400,400),(563,564)],
    'wave_instationary.F90': [(294,295)],
    'wave_stationary_directions.F90': [(442,444)],
    'wave_timestep.F90': [(75,114)],
    'rainfall.F90': [(22,70),(86,100)],
    'bedroughness.F90': [(220,249),(275,300)],
    'output.F90': [(5,8),(51,80),(158,170)],
    'ncoutput.F90': [(1118,1164)],
    'logging.F90': [(17,37),(53,75),(332,386)],
    'libxbeach_dynamic.F90': [(12,63)],
    'xmpi.F90': [(199,224),(1710,1728)],
    'introspection.F90': [(1,111)],
}
spans = []
for name, ranges in specs.items():
    p = SRC/name
    lines = p.read_bytes().split(b'\n')
    for a,b in ranges:
        spans.append({'id': f'{name}:{a}-{b}', **binding(p), 'line_start': a, 'line_end': b,
                      'quote_exact_utf8': b'\n'.join(lines[a-1:b]).decode()})

reuse = ['remaining-20260912/remaining.json', 'remaining-20260912/source-reuse.json',
         'build-mode-20260912/build-map.json', 'build-mode-20260912/contracts.json',
         'build-mode-20260912/generation-probe.json', 'lifecycle/edges.json',
         'lifecycle/resolution-20260912/adjudication.json', 'lifecycle/resolution-20260912/review-response.json',
         'physics/connectivity.json', 'physics/resolution-20260912/adjudication.json',
         'physics/resolution-20260912/review-response.json']
contracts = [
    {'id':'R1-RT01','state':'ph', 'conclusion':'Ship pressure head in metres; shipwave maps it before the flow gradient consumes zs+ph. It is independent of nonh pres/dp.',
     'guard':'executestep xcompute AND error==0; ships==1 for producer; (flow==1 OR wavemodel==WAVEMODEL_NONH) for downstream flow consumption; ship compute_force and firstship branches remain distinct',
     'evidence':['variables.def:256-256','ship.F90:287-337','ship.F90:365-373','ship.F90:403-410','libxbeach.F90:280-312','flow_timestep.F90:131-149']},
    {'id':'R1-RT02','state':'pres/dp and uu/vv/Wm', 'conclusion':'nonh predictor/UV correction/corrector ordering; integer nonhq3d dispatcher; correctors update pres, not ph; model contains MPI guarded exchanges.',
     'guard':'flow wavemodel==NONH; nonhq3d case1 versus default; case1 ny==0 versus else; explicit pressure/advW and UV correction secorder==1',
     'evidence':['params.F90:70-79','flow_timestep.F90:635-658','nonh.F90:42-43','nonh.F90:201-247','nonh.F90:683-697','nonh.F90:1234-1262','nonh.F90:1411-1422','nonh.F90:1446-1449','nonh.F90:1844-1883','nonh.F90:2162-2176','nonh.F90:2237-2241','nonh.F90:2858-2935'],
     'reuses':'build-mode-20260912/build-map.json'},
    {'id':'R1-RT03','state':'momentum residual and continuity', 'conclusion':'dudt/dvdt are subtracted; u/v Coriolis residual signs are -fc*vu/+fc*uv. advUV/huhv are active secorder calls; flow_secondorder_con caller is commented.',
     'guard':'wetu/wetv==1 for momentum, secorder==1 for actual corrections; no activation inferred from a definition or comment',
     'evidence':['flow_timestep.F90:563-580','flow_timestep.F90:597-616','flow_timestep.F90:635-658','flow_timestep.F90:706-719','flow_timestep.F90:724-759','flow_secondorder.F90:686-824','params.F90:98-109']},
    {'id':'R1-RT04','state':'Dveg and Fvegu/Fvegv', 'conclusion':'Active stationary/direction and surfbeat consumers include Dveg. Wave precedes vegatt (last update); flow follows it (same-step drag).',
     'guard':'vegetation==1; porcanflow branch separate; wave stationary interval/surfbeat/single_dir guards reused rather than all branches assumed every step',
     'evidence':['libxbeach.F90:280-312','vegetation.F90:318-345','vegetation.F90:400-400','vegetation.F90:563-564','wave_timestep.F90:75-114','wave_instationary.F90:294-295','wave_stationary_directions.F90:442-444','flow_timestep.F90:563-580','flow_timestep.F90:597-616'],
     'reuses':'build-mode-20260912/contracts.json'},
    {'id':'R1-RT05','state':'rainfallrate and infil', 'conclusion':'Initializer converts mm/hr to m/s. Current rainfall interpolation feeds the following continuity update; gwflow ran before that flow call.',
     'guard':'init xmaster; rainfall==1 for update; not constantRainfall for time interpolation; USEMPI broadcast constantRainfall only t<=dt',
     'evidence':['libxbeach.F90:171-184','libxbeach.F90:280-312','rainfall.F90:22-70','rainfall.F90:86-100','flow_timestep.F90:724-759']},
    {'id':'R1-RT06','state':'D90top to cfu/cfv', 'conclusion':'flow first-call setup invokes bedroughness_init; each flow calls bedroughness_update before momentum. Later morphology changes feed subsequent flow calls.',
     'guard':'White-Colebrook grain-size and ngd>1 for D90top; other coefficient/extra-friction options are separate; existing grain overwrite finding unchanged',
     'evidence':['flow_timestep.F90:74-122','flow_timestep.F90:176-177','bedroughness.F90:220-249','bedroughness.F90:275-300','libxbeach.F90:280-312'],
     'reuses':'physics/resolution-20260912/adjudication.json#XB-PHY-U01'},
    {'id':'R1-RT07','state':'output provider and writer rank', 'conclusion':'Active output uses ncoutput_module for NetCDF and Fortran output. Non-xomaster return precedes both write branches. Legacy var_output_init calls are commented.',
     'guard':'output format; USENETCDF for NetCDF support; xomaster before writing; dooutputglobal then donetcdf/dofortran',
     'evidence':['output.F90:5-8','output.F90:51-80','output.F90:158-170','ncoutput.F90:1118-1164']},
    {'id':'R1-RT08','state':'logging callbacks and generated writelog', 'conclusion':'Generated writelog specifics call writelog_a/distribute. set_logger binds logging_callback; logmsg checks association. assignlogdelegate binds a separate distributelog pointer. Exported writetolog calls that pointer without an association guard; caller must provide it before use.',
     'guard':'xmaster for writelog_distribute; associated(logging_callback) in logmsg; c_associated(fPtr) in delegate setup; no association guard in writetolog',
     'evidence':['logging.F90:17-37','logging.F90:53-75','logging.F90:332-386','libxbeach_dynamic.F90:12-63'],
     'generated':'generated-links.json (writelog.inc and writeloginterface.inc); generated output line numbers are not raw-source lines'},
    {'id':'R1-RT09','state':'MPI error callback registration', 'conclusion':'xmpi_initialize passes model comm_errhandler to MPI_Comm_create_errhandler and sets it on the world communicator. Its body calls halt_program. It is not dead code merely because no direct CALL exists.',
     'guard':'USEMPI; actual error callback invocation belongs to the external MPI runtime and is not simulated',
     'evidence':['xmpi.F90:199-224','xmpi.F90:1710-1728']},
]
dump('evidence.json', {'schema':'xbeach-runtime-source-contracts/v1','base_commit':'9f438b9',
     'scope':'Fixed R1 inputs; source-bound contracts and bounded R3 corrections',
     'evidence':spans, 'reused_evidence':[binding(HERE.parent/x) for x in reuse],
     'contracts':contracts,'R1_complete':False,'whole_model_complete':False,'human_approval_issued':False})

procedures = [json.loads(x) for x in (HERE/'procedures.jsonl').read_text().splitlines()]
calls = [json.loads(x) for x in (HERE/'call-candidates.jsonl').read_text().splitlines()]
byid = {x['id']:x for x in procedures}
interfaces = read('interfaces.json')
generated = read('generated-links.json')
runtime = {'c_associated','c_f_pointer','c_f_procpointer','c_loc','cpu_time','date_and_time','flush',
           'get_command_argument','getcwd','random_seed','sleep','sleepqq','system_clock','tracebackqq','usleep'}
symbols = collections.defaultdict(list)
for c in calls:
    if c['direct_definition_candidates'] or c['generic_specific_candidates']: continue
    symbols[c['symbol']].append(c['id'])
boundaries = []
for name, ids in sorted(symbols.items()):
    if name=='writelog':
        kind, contract = 'model_generated_generic', 'R1-RT08'
    elif name in {'logging_callback','distributelog'}:
        kind, contract = 'host_procedure_pointer', 'R1-RT08'
    elif name.startswith(('mpi_','mpe_')):
        kind, contract = 'external_mpi_or_mpe_interface', 'Model-side call/CPP locations only; implementation excluded'
    elif name.startswith(('nf90_','nf_')):
        kind, contract = 'external_netcdf_interface', 'Model-side call/CPP locations only; implementation excluded'
    elif name in runtime:
        kind, contract = 'language_c_or_os_runtime_interface', 'Model-side interface only; implementation excluded'
    else:
        raise AssertionError(('unclassified symbol',name))
    boundaries.append({'symbol':name,'classification':kind,'contract':contract,'call_candidate_ids':ids,
                       'scope_limit':'Symbol boundary classification does not prove branch feasibility, argument types or runtime behavior'})
dump('interface-boundaries.json', {'symbols':boundaries, 'generated_outputs':binding(HERE/'generated-links.json'),
      'callback_contracts':['R1-RT08','R1-RT09'], 'library_internals_inspected':False})

orphans = []
for x in read('no-incoming-candidates.json'):
    p = byid[x['id']]
    generic = [g for g in interfaces if g['module']==p['module'] and p['name'] in g['specific_names']]
    targets = []
    if p['kind']=='program':
        status, proof = 'program_entry', 'Source program declaration and source-bindings build targets'
    elif p['bind_c_names']:
        status, proof = 'declared_C_interface', 'Source bind(C,name) declaration; host invocation not required to be present in model source'
    elif p['module']=='introspection_module' and generic:
        status, proof = 'declared_Fortran_generic_interface', 'introspection module interface declarations; no claim that every host uses every API'
        targets = [{'name':g['name'],'path':g['path'],'line':g['line_start']} for g in generic]
    elif p['name']=='writelog_distribute':
        status, proof = 'model_generated_incoming', 'R1-RT08 and generated-links.json:writelog.inc'
    elif p['name']=='comm_errhandler':
        status, proof = 'registered_callback', 'R1-RT09'
    elif p['name']=='flow_secondorder_con':
        status, proof = 'commented_current_caller', 'R1-RT03; no active call in selected lexical index; external uses not excluded'
    elif p['name'] in {'var_output_init','var_output'}:
        status, proof = 'legacy_output_no_active_dispatch', 'R1-RT07; current provider is ncoutput_module'
    else:
        status, proof = 'open_no_indexed_incoming', 'Definition exists but no candidate incoming; requires source/import/generated/helper disposition, not dead-code proof'
    orphans.append({'id':x['id'],'classification':status,'evidence':proof,'generic_interfaces':targets,
                    'source':{'path':p['path'],'sha256':p['sha256'],'line_start':p['line_start'],'line_end':p['line_end']}})
dump('entry-dispositions.json', {'scope':'Only routines lacking indexed incoming; endpoint candidates elsewhere remain unproven',
      'records':orphans,'open_ids':[x['id'] for x in orphans if x['classification'].startswith('open_')],
      'R1_complete':False,'human_approval_issued':False})

# Literal Python exports link by C symbol and build family, not Fortran spelling.
exports = collections.defaultdict(list)
for p in procedures:
    for x in p['bind_c_names']: exports[x['name']].append(p['id'])
python_links = []
for p in read('python-wrapper.json'):
    for c in p['literal_foreign_calls']:
        python_links.append({'python_path':p['path'],'python_method':p['name'],**c,
                             'C_export_candidates':exports[c['symbol']],
                             'limit':'Select the matching build family; same exported name in different libraries is not a shared implementation'})
dump('python-export-links.json', {'literal_links':python_links,
      'dynamic_selection_methods':[x for x in read('python-wrapper.json') if x['dynamic_selection_requires_review']],
      'known_lifecycle_contract_reuse':'lifecycle/resolution-20260912/adjudication.json#XB-SC-012',
      'limit':'Dynamic getter/setter type/rank choices require explicit adjudication; literal export resolution alone does not close R1'})

dump('remaining-gaps.json', {'scope':'Residuals within frozen R1, not new task scope',
      'gaps':[
          {'id':'R1-G1','task':'Adjudicate candidate edges against imported visibility, generic type/rank and jointly feasible build/CPP/execution guards; reuse existing lifecycle/physics/mode contracts.',
           'artifact':'call-candidates.jsonl','status':'open'},
          {'id':'R1-G2','task':'Resolve these no-incoming definitions as interface/helper/inactive/generated or identify a missing edge.',
           'procedure_ids':[x['id'] for x in orphans if x['classification'].startswith('open_')],'status':'open'},
          {'id':'R1-G3','task':'Bind Python dynamic getter/setter choices and remaining generated include expansion to specific model interfaces and build families.',
           'artifacts':['python-export-links.json','generated-links.json'],'status':'open'}],
      'completed_here':['R1-RT01','R1-RT02','R1-RT03','R1-RT04','R1-RT05','R1-RT06','R1-RT07','R1-RT08','R1-RT09'],
      'R1_complete':False,'R2':'unchanged_open','R3':'seven_document_candidates','R4':'not_final_packet',
      'count_policy':'Index and gap counts are inventory identifiers, not defect counts or completion percentages'})
print('Bound',len(spans),'source spans;',len(contracts),'runtime contracts;',len(orphans),'no-incoming dispositions;',sum(x['classification'].startswith('open_') for x in orphans),'still open')
