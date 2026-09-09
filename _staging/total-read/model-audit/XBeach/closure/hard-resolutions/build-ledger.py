"""Rebuild the five-item superseding ledger from immutable local inputs."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent
SCRATCH = Path('/tmp/xbeach-closure-hard')
RAW = 'models/XBeach/raw/source_code/'
LIB = RAW + 'trunk/src/xbeachlibrary/'
MPI = RAW + 'trunk/lib/x64/mpich/'
CW = '_staging/total-read/model-audit/XBeach/cw/crosswalk/'
sha = lambda b: hashlib.sha256(b).hexdigest()
DEFERRED = '_staging/total-read/model-audit/XBeach/closure/deferred-inputs.json'
deferred_data = (ROOT / DEFERRED).read_bytes()
deferred = json.loads(deferred_data)

def evidence(path, a, b=None):
    data = (ROOT / path).read_bytes()
    lines = data.split(b'\n')
    b = a if b is None else b
    assert 1 <= a <= b <= len(lines)
    return {'path': path, 'sha256': sha(data), 'line_start': a, 'line_end': b,
            'line_numbering': 'physical LF-delimited; CR retained in quote',
            'quote_exact_utf8': b'\n'.join(lines[a-1:b]).decode()}

def artifact(name):
    p = OUT / name
    return {'path': str(p.relative_to(ROOT)), 'sha256': sha(p.read_bytes())}

def disasm_quote(name, needle, before=0, after=0):
    p = OUT / name
    lines = p.read_bytes().split(b'\n')
    line = next(i for i, text in enumerate(lines, 1) if needle.encode() in text)
    return evidence(str(p.relative_to(ROOT)), line-before, line+after)

def item(key, shard, filename, index):
    path = CW + shard + '/' + filename + '.crosswalk.json'
    data = (ROOT / path).read_bytes()
    cw = json.loads(data)
    source = ROOT / RAW / cw['source_path']
    assert sha(source.read_bytes()) == cw['source_sha256']
    row = cw['dispositions'][index]
    frozen = next(r for r in deferred['items'] if r['crosswalk_path'] == path and r['index'] == index)
    assert frozen['crosswalk_sha256'] == sha(data) and frozen['original_disposition'] == row
    return {'id': key, 'closure_status': 'CLOSED_WITH_SCOPED_DISPOSITION',
            'deferred_input_id': frozen['id'], 'deferred_input_path': DEFERRED,
            'deferred_input_sha256': sha(deferred_data),
            'original_crosswalk_path': path, 'original_crosswalk_sha256': sha(data),
            'disposition_index_zero_based': index, 'base_ids': row['base_ids'],
            'audit_ids': row['audit_ids'], 'original_disposition': row,
            'source_path': RAW + cw['source_path'], 'source_sha256': cw['source_sha256'],
            'supersedes': 'Only this row interpretation; original crosswalk, source and receipts remain immutable.'}

# Reproducible disassembly: outputs contain actual bytes and relocation symbols.
dll = SCRATCH / 'mpich2mpi.extracted.dll'
cmd = ['objdump', '-d', '--start-address=0x18006fb20', '--stop-address=0x1800700c8', str(dll)]
dis = subprocess.check_output(cmd, cwd=ROOT, text=True)
(OUT / 'runtime-comm-dup.disassembly.txt').write_text(dis)
exports = subprocess.check_output(['objdump', '-p', str(dll)], cwd=ROOT, text=True)
(OUT / 'runtime-export-map.txt').write_text('\n'.join(l for l in exports.splitlines() if 'ImageBase' in l or '[  58]' in l or '[ 356]' in l or 'MPI_Comm_dup' in l) + '\n')
cxx = subprocess.check_output(['objdump', '-dr', MPI + 'lib/cxx.lib'], cwd=ROOT, text=True)
cxx = '\n\n'.join(c for c in cxx.split('Disassembly of section ') if '<?Create_keyval@' in c)
(OUT / 'cxx-create-keyval.disassembly.txt').write_text(cxx)
assert '4c 8b e2' in dis and 'mov    %rdx,%r12' in dis
assert '18006fee0:' in dis and 'movl   $0x4000000,(%r12)' in dis
assert '18006fe5a:' in dis and 'mov    %ecx,(%r12)' in dis
assert cxx.count('cmove  %r9,%rcx') == 3
for cls, cfunc in [('Comm','Comm'),('Datatype','Type'),('Win','Win')]:
    assert '?NULL_COPY_FN@' + cls + '@MPI' in cxx
    assert 'MPI_' + cfunc + '_create_keyval' in cxx

# Enumerate the checked build manifests rather than extrapolate to every possible build.
builds = [ROOT / LIB / 'Makefile.am', *sorted((ROOT / LIB).glob('*.vfproj'))]
inventory = []
for p in builds:
    data = p.read_bytes()
    inventory.append({'path': str(p.relative_to(ROOT)), 'sha256': sha(data),
                      'wave_boundary_main_occurrences': data.lower().count(b'wave_boundary_main'),
                      'wave_boundary_datastore_occurrences': data.lower().count(b'wave_boundary_datastore')})
assert all(x['wave_boundary_main_occurrences'] == x['wave_boundary_datastore_occurrences'] == 0 for x in inventory)
(OUT / 'checked-build-manifests.json').write_text(json.dumps(inventory, indent=2) + '\n')

rows = []
r = item('XB-HARD-01', 'XBeach-001', 'trunk__src__xbeachlibrary__wave_boundary_main.f90', 8)
r.update(final_disposition='NARROWED', conflict_resolution='BASE_CORRECT_AUDIT_REFUTED',
    base_truth='TRUE: the component is a scalar INTEGER without ALLOCATABLE or POINTER; ALLOCATED and DEALLOCATE are invalid.',
    audit_truth='FALSE: neither the component nor input randomseed is an allocatable vector. The comment about 40 integers is stale, not a declaration.',
    severity='HIGH if this prototype is compiled; no failure claimed for the seven checked build manifests',
    reasoning='waveBoundaryParameters has waveBoundaryParametersType from the directly USE-associated datastore. Its scalar component declaration contradicts the vector hypothesis. An isolated compile using the complete original datastore and the exact original failing statement emits both required-ALLOCATABLE diagnostics. Makefile.am and six vfproj manifests omit main/datastore; therefore this is an integration-time defect in an excluded prototype, not an observed shipped-build failure.',
    canonical_ready_ko='`wave_boundary_main`의 seed 처리에는 잠재적 컴파일 결함이 있다. 저장소 타입의 `randomseed`는 비할당 정수 스칼라인데 `ALLOCATED`와 `DEALLOCATE`에 전달된다. 따라서 “미할당 seed 벡터 대입” 해석은 기각한다. 확인한 Makefile.am과 6개 vfproj에는 이 모듈이 없으므로 해당 빌드의 실행 결함으로 확대하지 않는다. (`'+LIB+'wave_boundary_datastore.f90:16-30`; `'+LIB+'wave_boundary_main.f90:121-135,221-224`; `'+LIB+'Makefile.am:4-60`.)',
    evidence=[evidence(LIB+'wave_boundary_datastore.f90',16,30),evidence(LIB+'wave_boundary_datastore.f90',73,77),evidence(LIB+'wave_boundary_main.f90',121,135),evidence(LIB+'wave_boundary_main.f90',221,224),evidence(LIB+'Makefile.am',4,60)],
    experiment_artifacts=[artifact('randomseed-probe.f90'),artifact('randomseed-probe-results.json'),artifact('checked-build-manifests.json')])
rows.append(r)

r = item('XB-HARD-02','XBeach-002','trunk__src__xbeachlibrary__morphevolution.F90',24)
r.update(final_disposition='NARROWED', conflict_resolution='BASE_CORRECT_AUDIT_STALE_STATE_REFUTED',
    base_truth='TRUE for finite vv==0: kturbv is cleared on every call; forward j iteration reads the current and next not-yet-written row, both zero.',
    audit_truth='PARTLY TRUE: the wrong work array is read; FALSE that values survive from a previous call or previous processing of this cell.',
    severity='MED/scoped zero-velocity interpolation defect; HIGH effect not established',
    reasoning='The SAVE attribute does not preserve nonzero values across the unconditional whole-array zero assignment. For increasing j, kturbv(i,j) has not been assigned yet and kturbv(i,j+1) is a future row; the last boundary row is only overwritten after the loop. Thus the branch computes exactly zero, independently of nonzero neighboring s%kturb. Sturbv multiplies this by vv in Lagrangian mode: when vv is exactly zero, replacing interpolation would not change that flux. Eulerian mode multiplies by vev instead, so the defect can affect flux when vv==0 and vev!=0; no case-specific effect size is asserted.',
    canonical_ready_ko='`waveturb`의 `vv==0` 분기는 `s%kturb` 대신 작업배열 `kturbv`를 평균한다. 배열은 호출마다 0으로 초기화되고 j가 증가하는 순서로 갱신되므로 두 피연산자는 모두 0이다. “이전 호출의 잔존값 사용” 해석은 기각한다. Lagrangian 이류에서는 같은 0의 `vv`를 곱해 이 면의 flux 차이가 없지만, Eulerian 이류는 `vev`를 곱하므로 `vv==0`, `vev!=0` 조건에서 잘못된 0이 영향을 줄 수 있다. (`'+LIB+'morphevolution.F90:2863-2874,2918-2938`.)',
    evidence=[evidence(LIB+'morphevolution.F90',2858,2874),evidence(LIB+'morphevolution.F90',2903,2938),evidence(LIB+'morphevolution.F90',2952,2955)])
rows.append(r)

r = item('XB-HARD-03','XBeach-D00','trunk__lib__README.txt.txt',0)
r.update(final_disposition='STANDS',conflict_resolution='AUDIT_CORRECT_BASE_REFUTED',
    base_truth='FALSE: the file has two nonblank physical LF-delimited lines, not one blank line.',
    audit_truth='TRUE: its architecture inventory names only win32; the local x64 distribution exists.',
    severity='LOW/documentation coverage',
    reasoning='Exact bytes start with the library introduction and name the win32 folder. They contain one LF separator and no final LF. The x64 header and supplied x64 archive are independently hashed local evidence of the additional distribution.',
    canonical_ready_ko='`trunk/lib/README.txt.txt`는 빈 파일이 아니다. 2개 비어 있지 않은 줄에서 win32 사전 빌드 라이브러리만 안내하며, 함께 제공되는 x64 MPICH를 안내하지 않는다. 이는 아키텍처 목록의 누락이다. (`'+RAW+'trunk/lib/README.txt.txt:1-2`; `'+MPI+'include/mpi.h:1-15`.)',
    evidence=[evidence(RAW+'trunk/lib/README.txt.txt',1,2),evidence(MPI+'include/mpi.h',1,15)],
    binary_sources=[{'path':MPI+'lib/cxx.lib','sha256':sha((ROOT/MPI/'lib/cxx.lib').read_bytes())}])
rows.append(r)

r = item('XB-HARD-04','XBeach-V01','trunk__lib__x64__mpich__include__mpicxx.h',3)
r.update(final_disposition='NARROWED',conflict_resolution='UNINITIALIZED_OUTPUT_REFUTED_FOR_BUNDLED_RUNTIME_UNCHECKED_STATUS_RETAINED',
    base_truth='PARTLY TRUE: all four Clone implementations and both return-type branches discard MPI_Comm_dup status; FALSE that bundled runtime returned-error paths leave ncomm uninitialized.',
    audit_truth='PARTLY TRUE for the same reason. Automatic local ncomm has no initializer in the header, but the supplied C runtime writes the pointed-to object before return.',
    severity='LOW/unchecked status in bundled runtime; no indeterminate-handle claim',
    reasoning='MSI decompression independently yields a PE whose MPI_Comm_dup and PMPI_Comm_dup exports both map to RVA 0x6fb20. Windows x64 entry RDX (MPI_Comm* output) is preserved in R12 at RVA 0x6fb4b. Every visible ordinary error path joins RVA 0x6fe94, then at 0x6fee0 stores literal 0x04000000 through R12 before the call at 0x6fee8 and shared return at 0x700c7. The supplied mpi.h defines that literal as MPI_COMM_NULL. Success stores the allocated handle through R12 at 0x6fe5a. Therefore the original uninitialized-handle allegation is disproven for this binary and a valid output pointer as supplied by Clone. Status is still discarded and a null-handle wrapper can be returned. The DLL was inspected statically, not installed or executed; behavior of replacement runtimes is outside this refutation. The earlier unverifiable external source quotation is not used.',
    canonical_ready_ko='제공된 x64 MPICH의 `Clone`은 `MPI_Comm_dup` 반환 코드를 확인하지 않아, 오류 핸들러가 복귀하면 null communicator wrapper를 반환할 수 있다. 다만 “초기화되지 않은 ncomm 사용”은 이 배포본에는 해당하지 않는다. MSI에 포함된 DLL의 `MPI_Comm_dup` 오류 경로가 출력 포인터에 `MPI_COMM_NULL`을 쓴 뒤 복귀한다. (`'+MPI+'include/mpicxx.h:1567-1580,1658-1671,2328-2341,2443-2456`; `'+MPI+'include/mpi.h:189`; 제공 MSI의 MPI_Comm_dup RVA 0x6fb20, 출력 대입 RVA 0x6fee0.)',
    evidence=[evidence(MPI+'include/mpicxx.h',1567,1580),evidence(MPI+'include/mpicxx.h',1658,1671),evidence(MPI+'include/mpicxx.h',2328,2341),evidence(MPI+'include/mpicxx.h',2443,2456),evidence(MPI+'include/mpi.h',189)],
    binary_validation={'runtime_provenance':artifact('runtime-provenance.json'),'extracted_binary':{'location':'scratch only; regenerate with extract-runtime.py; excluded from git','sha256':sha(dll.read_bytes())}, 'export_map':artifact('runtime-export-map.txt'),'disassembly':artifact('runtime-comm-dup.disassembly.txt'), 'claim_refuted':'returned-error use of indeterminate ncomm with the supplied runtime', 'all_return_paths_checked':'single RET at VA 0x1800700c7; success output store at VA 0x18006fe5a or error output store at VA 0x18006fee0 precedes shared epilogue'})
rows.append(r)

r = item('XB-HARD-05','XBeach-V01','trunk__lib__x64__mpich__include__mpicxx.h',8)
r.update(final_disposition='NARROWED',conflict_resolution='ORDINARY_REGISTRATION_FAILURE_REFUTED_DIRECT_HELPER_DEFECT_RETAINED',
    base_truth='PARTLY TRUE: every helper sets flag=1 and leaves attr_out untouched; ordinary Create_keyval registration does not invoke that body.',
    audit_truth='PARTLY TRUE: body observation is correct; the stated ordinary duplication installation path is defeated by callback pointer-identity guards in supplied cxx.lib.',
    severity='LOW/direct helper or forwarding callback only',
    reasoning='Each of Comm/Datatype/Win Create_keyval has the matching NULL_COPY_FN relocation at offset 0x0a, compares it with RCX at 0x0e, zeroes R9D at 0x04 and conditionally moves R9 to RCX at 0x18 before calling its C create_keyval at offset 0x2b. Thus the exact helper pointer is converted to the C null callback, matching the zero-valued macros in mpi.h. This directly validates the neutralizer for the supplied x64 archive. It does not correct the inline helper body: direct calls, or registration of a distinct function which forwards to that body, bypass the identity check. Retain only this explicit scope; no XBeach call site or observed model failure is claimed. No external quote is needed.',
    canonical_ready_ko='x64 `mpicxx.h`의 `NULL_COPY_FN` 본문은 `attr_out`을 대입하지 않고 `flag=1`로 만든다. 그러나 함께 제공된 `cxx.lib`의 Comm/Datatype/Win `Create_keyval`은 이 함수 포인터를 C null callback(0)으로 치환하므로 일반 등록 뒤 복제에서 미정의 포인터가 설치된다는 주장은 기각한다. 본문 직접 호출이나 별도 전달 callback은 이 치환을 거치지 않으므로 낮은 우선순위의 결함으로 남긴다. (`'+MPI+'include/mpicxx.h:409,1471,1904`; `'+MPI+'include/mpi.h:265-271`; `'+MPI+'lib/cxx.lib`, 각 Create_keyval 함수 +0x04–+0x2c의 relocation 포함 역어셈블리.)',
    evidence=[evidence(MPI+'include/mpicxx.h',409),evidence(MPI+'include/mpicxx.h',1471),evidence(MPI+'include/mpicxx.h',1904),evidence(MPI+'include/mpi.h',265,271)],
    binary_validation={'source_path':MPI+'lib/cxx.lib','source_sha256':sha((ROOT/MPI/'lib/cxx.lib').read_bytes()),'disassembly':artifact('cxx-create-keyval.disassembly.txt'),'claim_refuted':'indeterminate attribute installation following ordinary exact-pointer Create_keyval registration with supplied cxx.lib'})
rows.append(r)

rows[3]['evidence'] += [
    evidence(str((OUT/'runtime-export-map.txt').relative_to(ROOT)),1,7),
    disasm_quote('runtime-comm-dup.disassembly.txt','18006fb4b:',after=1),
    disasm_quote('runtime-comm-dup.disassembly.txt','18006fe5a:',after=1),
    disasm_quote('runtime-comm-dup.disassembly.txt','18006fee0:',before=3,after=3),
    disasm_quote('runtime-comm-dup.disassembly.txt','1800700b8:',after=4),
]
for cls in ['Comm','Datatype','Win']:
    rows[4]['evidence'].append(disasm_quote('cxx-create-keyval.disassembly.txt','<?Create_keyval@'+cls+'@',after=20))

ledger={'schema':'xbeach-hard-resolution/v1','date':'2026-09-09','author':'Codex (gpt-6-astra)',
        'scope':'Exactly three disposition conflicts plus two XBeach-V01 REFUTED_UNVERIFIED rows.',
        'status':'Five evidence-backed scoped dispositions; external governance completion remains parent responsibility.',
        'line_numbering':'Physical LF separators in raw bytes; no splitlines() conversion; quote_exact_utf8 retains CR.',
        'items':rows}
(OUT/'hard-resolutions.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')

md=['---','title: "XBeach 잔여 고난도 5건의 근거 기반 재판정"','canonical_source: self','citation_status: verified','has_source_needed: false','note_author: "Codex (gpt-6-astra)"','note_date: 2026-09-09','verification_by: "Codex local source cross-reference and binary inspection"','verification_date: 2026-09-09','---','',
    'AI 재판정 기록이다. 원본 crosswalk·소스·receipt는 수정하지 않았으며, 이 원장이 지정한 0-based 행의 해석만 대체한다. 원래 두 주장과 과거 adversarial verdict는 JSON에 그대로 보존했다. 이 기록은 사용자 또는 외부 거버넌스 게이트의 완료 판정을 대신하지 않는다.','',
    '정확한 원문 인용, 물리적 LF 줄 번호, 원본·증거 SHA-256은 [hard-resolutions.json](hard-resolutions.json)에 있다.','']
for r in rows:
    md += ['## '+r['id']+' — '+r['final_disposition'],'',r['canonical_ready_ko'],'',
           '- 원래 행: `'+r['original_crosswalk_path']+'` / index '+str(r['disposition_index_zero_based'])+' / '+','.join(r['base_ids'])+' ↔ '+','.join(r['audit_ids']),
           '- crosswalk SHA-256: `'+r['original_crosswalk_sha256']+'`',
           '- 재판정: '+r['conflict_resolution'], '']
md += ['## 재현 범위','',
       '`python3 extract-runtime.py`는 원본 MSI의 OLE cabinet stream을 읽고 대상 DLL만 `/tmp/xbeach-closure-hard`에 추출한다. 설치·실행은 하지 않으며 DLL·컴파일 산출물은 git에 포함하지 않는다. `python3 build-ledger.py`는 추출된 DLL과 원본 cxx.lib를 objdump로 읽어 relocation 포함 증거와 원장을 재생성한다. Python olefile, 시스템 libarchive 및 GNU objdump가 필요하다.','',
       '[runtime-provenance.json](runtime-provenance.json)은 MSI→cabinet→DLL의 SHA-256 연결을, [runtime-export-map.txt](runtime-export-map.txt)는 MPI_Comm_dup 이름과 RVA 연결을, [runtime-comm-dup.disassembly.txt](runtime-comm-dup.disassembly.txt)는 출력 포인터 저장·공통 복귀 경로를 보존한다. [cxx-create-keyval.disassembly.txt](cxx-create-keyval.disassembly.txt)는 세 Create_keyval의 함수 포인터 치환을 보존한다.','',
       'Fortran 검사는 원본 datastore 모듈과 원본의 문제가 되는 한 문장을 분리해 컴파일한 것이다. 전체 XBeach 빌드 실행을 뜻하지 않는다. [randomseed-probe-results.json](randomseed-probe-results.json)에 명령과 진단을 기록했다. 난류의 결과 범위는 소스의 대입 순서와 두 flux 식에 대한 정적 분석이며 별도 유동 실행 결과를 주장하지 않는다.','']
(OUT/'README.md').write_text('\n'.join(md))
print(json.dumps({'items':len(rows),'dispositions':{r['id']:r['final_disposition'] for r in rows}},indent=2))
