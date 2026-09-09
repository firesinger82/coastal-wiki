# Claude Sonnet 적대적 검토 1

## 검토 결과 (읽기 전용, 승인/완료 발급 안 함)

### 1. 원문 대조 결과 — 5건 모두 인용 정확

- **XB-HARD-01**: `wave_boundary_datastore.f90:16-30`, `wave_boundary_main.f90:195-234`을 직접 읽어 대조. `randomseed`는 실제로 비할당 스칼라 `integer`이고, `wave_boundary_main.f90:223-224`의 `if(allocated(...)) deallocate(...)` 호출과 정확히 일치. `Makefile.am` 전체(1-121줄, 절단 없이 완독)에도 `wave_boundary_main.f90`/`wave_boundary_datastore.f90`가 SOURCES에 없음을 확인. 저장소 전체를 `wave_boundary_main|datastore`로 grep한 결과 4개 파일뿐이며 vfproj·Makefile 계열은 전무. `checked-build-manifests.json`이 확인한 6개는 `xbeachlibrary*.vfproj` 변형(라이브러리 빌드용)이고, 나머지 7개 vfproj(`xbeach.vfproj`, `xbeach_IFX.vfproj` 등 드라이버·테스트·MPICH 예제)까지 직접 grep했으나 역시 0건 — 판정문의 "6개 vfproj" 범위보다 실제 배제 범위가 더 넓다. 즉 스코프 서술이 과소 주장(보수적)이며 반증거리가 되지 않는다. `randomseed-probe-results.json`의 gfortran 오류(exit 1, "must be ALLOCATABLE")도 실제 재현 커맨드·stderr가 기록되어 있어 검증 가능한 1차 증거다. **blocker 없음.**

- **XB-HARD-02**: `morphevolution.F90:2858-2960`을 직접 읽어 루프 순서를 재추적. `kturbv=0.0d0`(2874) 이후 `do j=1,s%ny / do i=1,s%nx+1`(2918-2919) 순행에서 `vv==0` 분기의 `kturbv(i,j)`는 현재 반복에서 아직 대입되지 않았고(0), `kturbv(i,j+1)`은 미래 행이라 역시 미대입(0) — 판정문의 "두 피연산자 모두 0" 주장이 코드와 정확히 일치한다. 경계행 `kturbv(:,s%ny+1)=s%kturb(:,s%ny+1)`(2929)은 루프 밖에서 실행되므로 루프 내부 판단에 영향 없음. Eulerian/Lagrangian 구분(2933-2939)도 원문과 일치. **blocker 없음.**

- **XB-HARD-03**: `README.txt.txt` 실제 파일이 정확히 2줄("prebuild libraries" / "win32 folder"), trailing LF 없음 — 인용과 100% 일치. **blocker 없음.**

- **XB-HARD-04·05**: `mpicxx.h:1567-1580`, `mpi.h:189` 등 소스 인용은 실제 파일과 정확히 일치.

### 2. MPICH 바이너리 반증(04·05) — 검증 한계, blocker 있음

디스어셈블리(`runtime-comm-dup.disassembly.txt`, `cxx-create-keyval.disassembly.txt`)는 텍스트 산출물만 존재하고 추출된 DLL(`extracted_binary`)은 "scratch only, git 제외"로 실제로 부재한다. 나는 objdump를 재실행할 도구가 없으므로 **이 디스어셈블리가 실제 바이너리와 일치하는지 독립 재현하지 못했다** — 같은 파이프라인(codex gpt-6-astra)이 생성하고 같은 파이프라인이 "verified_by"로 재확인한 자기검증이며, 제3자 재현이 아니다. 이는 반증 자체의 신뢰도를 낮추는 방법론적 결함이지 결론이 틀렸다는 뜻은 아니다.

더 구체적인 blocker: `runtime-provenance.json`은 MSI cabinet member `_1BE96E15F472462586C19E8C77FF7927`의 크기(2,089,984B)만 기록하고, **MSI File 테이블에서 이 GUID형 멤버명이 실제로 "mpich2mpi.dll"이라는 파일명과 매핑되는 단계가 없다.** export map의 `MPI_Comm_dup`/`PMPI_Comm_dup` 심볼 존재는 "MPI 런타임 DLL이라는 것"의 방증은 되지만, "XBeach 빌드가 실제로 로드하는 그 DLL"이라는 동일성 주장을 완전히 뒷받침하지는 않는다. 판정문 자체가 "이 배포본에 한정", "설치·실행하지 않음"이라고 스코프를 좁혀 명시했으므로 과잉주장은 아니지만, MSI File 테이블 대조가 빠진 점은 재현 절차에 채워야 할 구멍이다.

### 3. `build_attribution.py` — 소유권 추론 우려 확인됨

`classify()`(10-37행)의 기본값은 `component='xbeach'`, `origin='project-integration'`이며, 어떤 벤더 패턴에도 안 걸리면 이 기본값이 그대로 채택된다(12행). 코드 주석은 "operational, not a copyright/authorship judgment"라고 명시했지만, 실제 `attribution.json` 출력을 보면 217개 파일·1218개 disposition이 `project-integration`으로 분류되어 있고(라인 8-14 확인), **"unknown/미상" 버킷이 존재하지 않는다.** 즉 확장자·경로 패턴에 안 걸리는 파일은 자동으로 "XBeach 프로젝트 소유"로 귀속된다 — 이는 헤더나 저작권 표기를 실제로 열어 확인한 결과가 아니라 매칭 실패에 대한 디폴트다. 43개 항목 문서 자체는 "own-solver defect totals에서 mixed aggregation 제외"라고 방어선을 뒀지만(`attribution.json` note), 하위 소비자가 `project-integration=1218`을 "XBeach 자체 결함 1218건"으로 재해석할 위험은 코드상 실재한다. **이 부분은 "unknown" 카테고리 추가 또는 fallback 근거의 명시적 구분(경로 패턴 매칭 vs 헤더 확인)이 필요하다는 구체적 수정 사항으로 보고한다** — 파일: `build_attribution.py:10-37`.

### 4. 표본 한계

- 이번 검토는 지정된 5건 hard-resolution과 43개 build-vendor 항목의 wrapper/요약만 대상으로 했고, 나머지 문서 207건·소스 60건·로컬반증 8건은 열지 않았다.
- MPICH DLL/`cxx.lib` 이진 반증은 텍스트 디스어셈블리만 재확인했을 뿐 바이너리 자체를 재추출·재역어셈블 하지 않았다.
- `checked-build-manifests.json`이 다루지 않은 7개 vfproj(드라이버·테스트)는 내가 직접 grep으로만 보완 확인했고 공식 원장에는 반영되어 있지 않다.

### 결론

5건 중 4건(XB-HARD-01·02·03, 그리고 04·05의 소스 인용부)은 원문·재현 커맨드와 정확히 일치해 반증 근거가 견고하다. 04·05의 바이너리 반증은 결론 자체를 반박할 증거는 찾지 못했으나, **MSI 멤버→파일명 매핑 누락**과 **비독립적 자기검증**이라는 두 가지 절차적 blocker가 있다. `build_attribution.py`는 소유권 미상 파일을 묵시적으로 `xbeach`/`project-integration`에 귀속시키는 기본값 문제가 있어 수정이 필요하다. 사람 승인이나 전체 완료 판정은 발급하지 않는다.
