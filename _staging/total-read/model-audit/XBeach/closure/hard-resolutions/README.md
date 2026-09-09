---

> **후속 교정:** 아래 초기 XB-HARD-04의 DLL 식별과 배포본 전체 기각은 철회됐다. MSI File 테이블을 확인한 [최종 식별·판정 override](../local-refutations/mpich-identity/identity-ledger.json)가 우선한다. 기존 JSON과 초기 역어셈블리는 검토 이력으로 보존하며 최신 canonical에는 교정 결과를 반영한다. XB-HARD-05는 archive 동일성을 추가 확인했다.

title: "XBeach 잔여 고난도 5건의 근거 기반 재판정"
canonical_source: self
citation_status: verified
has_source_needed: false
note_author: "Codex (gpt-6-astra)"
note_date: 2026-09-09
verification_by: "Codex local source cross-reference and binary inspection"
verification_date: 2026-09-09
---

AI 재판정 기록이다. 원본 crosswalk·소스·receipt는 수정하지 않았으며, 이 원장이 지정한 0-based 행의 해석만 대체한다. 원래 두 주장과 과거 adversarial verdict는 JSON에 그대로 보존했다. 이 기록은 사용자 또는 외부 거버넌스 게이트의 완료 판정을 대신하지 않는다.

정확한 원문 인용, 물리적 LF 줄 번호, 원본·증거 SHA-256은 [hard-resolutions.json](hard-resolutions.json)에 있다.

## XB-HARD-01 — NARROWED

`wave_boundary_main`의 seed 처리에는 잠재적 컴파일 결함이 있다. 저장소 타입의 `randomseed`는 비할당 정수 스칼라인데 `ALLOCATED`와 `DEALLOCATE`에 전달된다. 따라서 “미할당 seed 벡터 대입” 해석은 기각한다. 확인한 Makefile.am과 6개 vfproj에는 이 모듈이 없으므로 해당 빌드의 실행 결함으로 확대하지 않는다. (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_datastore.f90:16-30`; `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_boundary_main.f90:121-135,221-224`; `models/XBeach/raw/source_code/trunk/src/xbeachlibrary/Makefile.am:4-60`.)

- 원래 행: `_staging/total-read/model-audit/XBeach/cw/crosswalk/XBeach-001/trunk__src__xbeachlibrary__wave_boundary_main.f90.crosswalk.json` / index 8 / A2 ↔ B3
- crosswalk SHA-256: `6983672a072bbb64cad0977f66baa59ed8fe65fce0cb833ad67080e292f39693`
- 재판정: BASE_CORRECT_AUDIT_REFUTED

## XB-HARD-02 — NARROWED

`waveturb`의 `vv==0` 분기는 `s%kturb` 대신 작업배열 `kturbv`를 평균한다. 배열은 호출마다 0으로 초기화되고 j가 증가하는 순서로 갱신되므로 두 피연산자는 모두 0이다. “이전 호출의 잔존값 사용” 해석은 기각한다. Lagrangian 이류에서는 같은 0의 `vv`를 곱해 이 면의 flux 차이가 없지만, Eulerian 이류는 `vev`를 곱하므로 `vv==0`, `vev!=0` 조건에서 잘못된 0이 영향을 줄 수 있다. (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/morphevolution.F90:2863-2874,2918-2938`.)

- 원래 행: `_staging/total-read/model-audit/XBeach/cw/crosswalk/XBeach-002/trunk__src__xbeachlibrary__morphevolution.F90.crosswalk.json` / index 24 / A12 ↔ B25
- crosswalk SHA-256: `50c963c451b342572c346a1184fb748acb94d84e013b27ba7ea376167b966e6c`
- 재판정: BASE_CORRECT_AUDIT_STALE_STATE_REFUTED

## XB-HARD-03 — STANDS

`trunk/lib/README.txt.txt`는 빈 파일이 아니다. 2개 비어 있지 않은 줄에서 win32 사전 빌드 라이브러리만 안내하며, 함께 제공되는 x64 MPICH를 안내하지 않는다. 이는 아키텍처 목록의 누락이다. (`models/XBeach/raw/source_code/trunk/lib/README.txt.txt:1-2`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpi.h:1-15`.)

- 원래 행: `_staging/total-read/model-audit/XBeach/cw/crosswalk/XBeach-D00/trunk__lib__README.txt.txt.crosswalk.json` / index 0 / A0 ↔ B0
- crosswalk SHA-256: `bbcd0b1bd1c578ea2c1f6aa313e2dfe0a4286f5f38691e782c20393752d17522`
- 재판정: AUDIT_CORRECT_BASE_REFUTED

## XB-HARD-04 — NARROWED

제공된 x64 MPICH의 `Clone`은 `MPI_Comm_dup` 반환 코드를 확인하지 않아, 오류 핸들러가 복귀하면 null communicator wrapper를 반환할 수 있다. 다만 “초기화되지 않은 ncomm 사용”은 이 배포본에는 해당하지 않는다. MSI에 포함된 DLL의 `MPI_Comm_dup` 오류 경로가 출력 포인터에 `MPI_COMM_NULL`을 쓴 뒤 복귀한다. (`models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpicxx.h:1567-1580,1658-1671,2328-2341,2443-2456`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpi.h:189`; 제공 MSI의 MPI_Comm_dup RVA 0x6fb20, 출력 대입 RVA 0x6fee0.)

- 원래 행: `_staging/total-read/model-audit/XBeach/cw/crosswalk/XBeach-V01/trunk__lib__x64__mpich__include__mpicxx.h.crosswalk.json` / index 3 / A10 ↔ B10
- crosswalk SHA-256: `b43d49e46fd591d0e04142e34e8903dfeab1e7e7d793164b4c7b209bba1b9760`
- 재판정: UNINITIALIZED_OUTPUT_REFUTED_FOR_BUNDLED_RUNTIME_UNCHECKED_STATUS_RETAINED

## XB-HARD-05 — NARROWED

x64 `mpicxx.h`의 `NULL_COPY_FN` 본문은 `attr_out`을 대입하지 않고 `flag=1`로 만든다. 그러나 함께 제공된 `cxx.lib`의 Comm/Datatype/Win `Create_keyval`은 이 함수 포인터를 C null callback(0)으로 치환하므로 일반 등록 뒤 복제에서 미정의 포인터가 설치된다는 주장은 기각한다. 본문 직접 호출이나 별도 전달 callback은 이 치환을 거치지 않으므로 낮은 우선순위의 결함으로 남긴다. (`models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpicxx.h:409,1471,1904`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/include/mpi.h:265-271`; `models/XBeach/raw/source_code/trunk/lib/x64/mpich/lib/cxx.lib`, 각 Create_keyval 함수 +0x04–+0x2c의 relocation 포함 역어셈블리.)

- 원래 행: `_staging/total-read/model-audit/XBeach/cw/crosswalk/XBeach-V01/trunk__lib__x64__mpich__include__mpicxx.h.crosswalk.json` / index 8 / A0 ↔ B0
- crosswalk SHA-256: `b43d49e46fd591d0e04142e34e8903dfeab1e7e7d793164b4c7b209bba1b9760`
- 재판정: ORDINARY_REGISTRATION_FAILURE_REFUTED_DIRECT_HELPER_DEFECT_RETAINED

## 재현 범위

`python3 extract-runtime.py`는 원본 MSI의 OLE cabinet stream을 읽고 대상 DLL만 `/tmp/xbeach-closure-hard`에 추출한다. 설치·실행은 하지 않으며 DLL·컴파일 산출물은 git에 포함하지 않는다. `python3 build-ledger.py`는 추출된 DLL과 원본 cxx.lib를 objdump로 읽어 relocation 포함 증거와 원장을 재생성한다. Python olefile, 시스템 libarchive 및 GNU objdump가 필요하다.

[runtime-provenance.json](runtime-provenance.json)은 MSI→cabinet→DLL의 SHA-256 연결을, [runtime-export-map.txt](runtime-export-map.txt)는 MPI_Comm_dup 이름과 RVA 연결을, [runtime-comm-dup.disassembly.txt](runtime-comm-dup.disassembly.txt)는 출력 포인터 저장·공통 복귀 경로를 보존한다. [cxx-create-keyval.disassembly.txt](cxx-create-keyval.disassembly.txt)는 세 Create_keyval의 함수 포인터 치환을 보존한다.

Fortran 검사는 원본 datastore 모듈과 원본의 문제가 되는 한 문장을 분리해 컴파일한 것이다. 전체 XBeach 빌드 실행을 뜻하지 않는다. [randomseed-probe-results.json](randomseed-probe-results.json)에 명령과 진단을 기록했다. 난류의 결과 범위는 소스의 대입 순서와 두 flux 식에 대한 정적 분석이며 별도 유동 실행 결과를 주장하지 않는다.
