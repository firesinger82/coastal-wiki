---
title: "LISFLOOD-FP 8.3(8.2 + 공식 패치) 소스 아키텍처 맵 — CPU·CUDA·Metal"
model: LISFLOOD-FP
component: source (top-level + swe/ + cuda/ + metal/)
canonical_source: self
citation_status: verified
verification_method: "2026-06-18 v8.2 Zenodo 아카이브(doi:10.5281/zenodo.13121102) 소스 직접 read 이력 보존. v8.2:lisflood.cpp:20-27 솔버 include·:34 main·:53-169 Solver struct 기본값과 swe/·root *.cpp 직접 확인. 2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - ../README.md
  - ../web-refs/lisflood-fp-official-resources.md
source_scope: LISFLOOD-FP/*
---

# LISFLOOD-FP 8.3(8.2 + 공식 패치) 소스 아키텍처 맵 [10-21 대조 정정]

> 현재 원자료는 Zenodo 8.2에 공식 8.3 패치를 적용한 코드이다 (`../LISFLOOD-FP-8.3-package/README.md:19–24`). [10-21 대조 정정]

2026-06-18의 v8.2 원분석 기준일은 `note_date`에 보존한다. [10-21 대조 정정]
현재 코드 인용의 기준은 `../raw/source_code/LISFLOOD-FP/`이다. [10-21 대조 정정]
`../LISFLOOD-FP-8.3-package/` 인용은 코드 기준 경로의 형제 패키지를 뜻한다.
`v8.0:`·`v8.1:`·`v8.2:`는 해당 이전 배포본을 뜻한다.
`bf804e23:models/LISFLOOD-FP/`는 반영 전 노트의 커밋과 경로를 뜻한다.

## 1. main과 솔버 선택 [10-21 대조 정정]

main의 선언은 `lisflood.cpp:37`의 `int main(int argc, char *argv[])`이다. [10-21 대조 정정]
v8.2의 같은 선언은 `v8.2:lisflood.cpp:34`에 있다. [10-21 대조 정정]
일반 해법은 공통 Solver 설정을 쓴다 (`lisflood.cpp:773–793`). [10-21 대조 정정]
HWFV1·MWDG2는 같은 `.par`를 별도 구조체로 다시 읽는다 (`cuda/adaptive/cuda_adaptive_simulate.cu:162–167`). [10-21 대조 정정]

CUDA 분기는 FV1, FV2, DG2, ACC, acc_nugrid, adaptive 순서로 플래그를 검사한다 (`lisflood.cpp:422–450`). [10-21 대조 정정]
CUDA 분기의 `return 0;`은 CPU 초기화 전에 실행된다 (`lisflood.cpp:457`). [10-21 대조 정정]
SGC는 `Fast_MainStart`를 호출한다 (`lisflood.cpp:775`). [10-21 대조 정정]
FV1 분기는 `METAL_ENABLED` 빌드에서 `if (Statesptr->cuda == ON && metal_is_available())`일 때 Metal FV1을 호출한다 (`lisflood.cpp:778–788`). [10-21 대조 정정]
그 조건을 충족하지 못하면 CPU FV1을 호출한다 (`lisflood.cpp:787–788`). [10-21 대조 정정]
CPU DG2 호출은 `lisflood.cpp:792–793`에 있다. [10-21 대조 정정]
Mac에서 CUDA 전용 해법까지 같은 해법의 CPU 구현으로 실행된다고 쓰면 안 된다 (`lisflood.cpp:419–459,773–805`). [10-21 대조 정정]

전체 실행 순서는 [callflow의 실행 흐름도](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md#4-실행-흐름도)에 연결한다.
흐름도의 Metal 시작 분기는 `lisflood.cpp:778,782,783`이다 ([Claude 렌더 확인(10-21)](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md#4-실행-흐름도)). [10-21 대조 정정]

## 2. 솔버 계열 (2 family)

### 2.1 Classic "FP" 솔버 (root `*.cpp`) — 원조 Bristol reduced-physics

| 파일 | 솔버 |
|---|---|
| `fp_acc.cpp` | **ACC** — local inertia(acceleration) 근사 SWE. LISFLOOD-FP 대표 reduced-physics(Bates et al. 2010). advection 무시·관성항 유지 → 고속 |
| `fp_flow.cpp` | diffusive wave(관성 무시) 흐름 |
| `fp_trent.cpp` | 고전 공간 1차 Roe 근사 리만 해법 (`fp_trent.cpp:3`, `fp_flow.cpp:50`). [10-21 대조 정정] |
| `iterateq.cpp` | 반복 solver |
| `sgc.cpp` | **sub-grid channel**(SGC) — 격자보다 작은 하도를 sub-grid 처리(Neal et al.) |
| `por_flow.cpp` | porosity 흐름 |
| `weir_flow.cpp`·`ch_flow.cpp` | 위어·채널 |
| `boundary.cpp`·`input.cpp`·`output.cpp` | 경계·입출력 |

### 2.2 신규 "swe/" 솔버 — SEAMLESS-WAVE(Kesserwani) 완전 2D shallow-water

| 파일 | 솔버 |
|---|---|
| `swe/fv1.cpp` | **FV1** — 1차 Godunov 유한체적 (full 2D SWE, shock-capturing) |
| `swe/dg2.cpp` | **DG2** — 활성 CPU DG2 구현 (`lisflood.cpp:790–793`). [10-21 대조 정정] |
| `swe/dg2new.cpp` | 호출이 주석 처리된 CPU DG2 리팩터 (`lisflood.cpp:794–796`). [10-21 대조 정정] |
| `swe/hll.cpp` | **HLL** Riemann flux (FV1/DG2 공용 numerical flux) |
| `swe/flux.cpp`·`fields.cpp` | flux·필드 자료구조 |
| `swe/boundary/input/output/stats` | swe 전용 경계·IO·통계 |

### 2.3 CUDA (`cuda/`)

CUDA 목록은 FV1·FV2·DG2·ACC·acc_nugrid·adaptive를 포함한다 (`lisflood.cpp:422–450`). [10-21 대조 정정]
균일 ACC와 비균일 ACC는 국소 관성 유량식을 사용한다 (`cuda/acc/cuda_acc_solver.cu:723–729`, `cuda/acc_nugrid/compute_q.cu:235–237`). [10-21 대조 정정]
acc_nugrid는 시간 반복 전에 구성한 비균일 격자를 사용한다 (`cuda/acc_nugrid/cuda_acc_nugrid_simulate.cu:154,231–282,541–715`). [10-21 대조 정정]
adaptive의 HWFV1·MWDG2는 `if (solver_params.epsilon > C(0.0) || first_t_step)`에서 유동 detail로 격자를 갱신한다 (`cuda/adaptive/cuda_adaptive_simulate.cu:422–523`). [10-21 대조 정정]
수준별 임계값과 정규화 detail 판정은 단일 DG2 격자의 slope limiter와 다르다 (`cuda/adaptive/mra/encode_and_thresh_topo.cu:29–54`; user manual.docx p.24(변환본)의 `limitslopes`). [10-21 대조 정정] [10-21 전수 검증 보완]

### 2.4 Metal FV1 [10-21 대조 정정]

Metal FV1은 v8.3에서 추가되었다 (`VersionHistory.h:31–32`). [10-21 대조 정정]
`cuda`와 `metal`은 같은 GPU 플래그를 켠다 (`pars.cpp:965–968`). [10-21 대조 정정]
Metal 실행 조건과 구현 차이는 [Metal FV1 노트](lisflood-fp-metal-fv1.md)에 정리한다.

### 2.5 dg2new의 빌드와 호출 [10-21 대조 정정]

legacy Make는 dg2new를 컴파일 목록에 넣는다 (`makefile:29–34`). [10-21 대조 정정]
현재 CMake는 dg2new를 목록에 넣지 않는다 (`CMakeLists.txt:51–64`). [10-21 대조 정정]
주 실행기는 dg2new를 호출하지 않는다 (`lisflood.cpp:794–796`). [10-21 대조 정정]

## 3. 솔버의 물리·수치해법 [10-21 전수 검증 정정]

확산파 해법은 국소 가속도와 이류 가속도를 생략한다 (user manual.pdf p.10–11). [10-21 전수 검증 정정]
ACC는 이류 가속도를 생략한 국소 관성 해법이다 (user manual.pdf p.10–11). [10-21 전수 검증 정정]
FV1은 완전 천수방정식의 1차 Godunov형 유한체적 해법이다 (user manual.docx p.5·14(변환본)). [10-21 전수 검증 정정]
DG2는 완전 천수방정식의 2차 불연속 Galerkin 해법이다 (user manual.docx p.5·15(변환본)). [10-21 전수 검증 정정]

DG2와 adaptive의 HWFV1·MWDG2는 실행 경로가 다르다 (`lisflood.cpp:447–450,790–796`). [10-21 대조 정정]

- reduced-physics 측(ACC)은 [SFINCS 아키텍처 맵](../../SFINCS/source-analysis/sfincs-architecture-source-map.md)의 SFINCS reduced SWE와 같은 계열.
- full SWE 측(FV1/DG2)은 [SWASH 아키텍처 맵](../../SWASH/source-analysis/swash-architecture-source-map.md)·Godunov 계열과 유사하나 LISFLOOD-FP는 raster DEM 범람 특화.

## 4. 관련 분석 [10-21 대조 정정]

- [고전 ACC·유동](lisflood-fp-classic-acc-flow.md): `fp_acc.cpp`의 국소 관성 이산화.
- [CPU FV1·DG2](lisflood-fp-swe-fv1-dg2.md): 활성 SWE와 비활성 dg2new의 구분. [10-21 대조 정정]
- [하도·SGC](lisflood-fp-channel-sgc.md): sub-grid channel 처리.
- [CUDA](lisflood-fp-cuda-gpu.md): CUDA 실행 계열.
- [적응 MRA](lisflood-fp-mwdg2-adaptive-mra.md): `cuda/adaptive/`의 HWFV1·MWDG2. [10-21 대조 정정]
- [CPU·CUDA·Metal 차이](lisflood-fp-cpu-gpu-differences.md): 시간 간격·수치 형식 대조.

## 문서와 코드 차이 (10-21 대조)

이 절은 최종 대조 기록의 결론을 옮긴 AI 정리이다.
표의 원문 인용은 결론 문장과 구분한다.
CPU·GPU 보고서 행은 구현 사이의 대조이다.

2013 PDF 매뉴얼 표지는 Code release 6.1.1을 적는다 (user manual.pdf p.1). [10-21 전수 검증 보완]
PDF 표지 날짜는 2013-11-25이다 (user manual.pdf p.1). [10-21 전수 검증 보완]
user manual.docx 표지는 변경 추적으로 6.1.1 삭제와 8.0.0 삽입을 표시한다 (변환본 p.1). [10-21 전수 검증 정정]
DOCX 판 이력 맨 위에는 8.0(2020-07-20)이 삽입되어 있다 (변환본 p.5). [10-21 전수 검증 정정]
user manual +bridge.docx 표지는 Code release 4.3.6을 적는다 (변환본 p.1). [10-21 전수 검증 보완]
bridge 표지 날짜는 2008-04-25이다 (변환본 p.1). [10-21 전수 검증 보완]
현재 코드는 Zenodo 8.2(10.5281/zenodo.13121102)에 공식 8.3 변경을 적용한 판이다 (`../LISFLOOD-FP-8.3-package/README.md:19–24`; [최종 근거 LB1-408](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)). [10-21 전수 검증 정정]
체크포인트에 쓰는 내부 숫자 판은 8.1.0이다 (`VersionHistory.h:16–22`). [10-21 전수 검증 보완]
릴리스 이름은 8.3이다 (`VersionHistory.h:23`). [10-21 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| bridge-docx:LB1-382 | 아키텍처 노트의 적용 판 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:16` `# LISFLOOD-FP v8.2 소스 아키텍처 맵` | `lisflood.cpp:780` `#ifdef METAL_ENABLED`; 782행 `if (Statesptr->cuda == ON && metal_is_available())`; `VersionHistory.h:23`의 배포판 표시는 `#define LF_Release "8.3"`이다.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:9,16`; `VersionHistory.h:21–23`; `lisflood.cpp:778–788`; `../LISFLOOD-FP-8.3-package/README.md:35,39` | A 판 차이 | 8.2 원분석의 기준일은 남긴다. 현재 원자료의 8.3 적용 사실을 별도로 적는다. Metal FV1 분기와 현재 행 번호를 추가한다. 내부 체크포인트 번호 8.1.0을 배포판 번호로 쓰지 않는다. [10-21 전수 검증 정정] |
| build-83:LN1-136 | Mac의 CPU 실행 범위 | `../LISFLOOD-FP-8.3-package/README.md:135–137` `On a Mac, FV1 runs on the Apple GPU and the other solvers on the CPU.` | `lisflood.cpp:773–805`의 CPU 선택은 SGC·fv1·dg2·그 밖의 IterateQ다. `pars.cpp:590–628`은 fv2·acc_nugrid·mwdg2·hwfv1 상태를 각각 켠다.<br>확인한 원문: `../LISFLOOD-FP-8.3-package/README.md:135–137`; `lisflood.cpp:419–459,773–805`; `pars.cpp:582–628` | B 문서 오기 | Mac에서 CUDA 전용 해법까지 같은 해법의 CPU 구현으로 실행된다고 쓰면 안 된다. |
| build-83:LN1-237 | dg2new의 해법 연결 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61` `**dg2new = multiwavelet 적응**`·`bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:83` ``- `swe/dg2new.cpp` — DG2 multiwavelet 적응 격자(v8.2 핵심, Kesserwani)`` | `v8.2:CMakeLists.txt:26–65`에는 dg2new가 없다. `v8.2:makefile:31`은 파일을 컴파일한다. `lisflood.cpp:794–796`의 실행 호출은 주석이다. 실제 adaptive는 `CMakeLists.txt:178`의 별도 디렉터리다.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61,83`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:29–38`; `swe/dg2new.cpp:11–38`; `cuda/adaptive/types/SolverTypes.h:3–7`; `lisflood.cpp:447–450,794–796`; `CMakeLists.txt:26–65,178`; `v8.2:makefile:31` | B 문서 오기 | dg2new를 MWDG2 구현이라고 쓰지 않는다. |
| callflow:RF-001 | 후대 솔버 추가 | user manual.pdf p.1 `Code release 6.1.1`, `25th November 2013`; user manual +bridge.docx p.1(변환본) `Code release 4.3.6`, `25th April 2008`; user manual +bridge.docx p.5(변환본)에는 2009년 이력도 있다. user manual.docx p.5(변환본) `8.0 Jul 20 2020 New first-order finite volume (FV1) and second-order discontinuous Galerkin (DG2) solvers for multi-core CPUs and Nvidia GPUs` | `VersionHistory.h:34` `8.0  Jul 24 2020  FV1 and DG2 Solvers added (JS)`; `v8.0:lisflood.cpp:409,413`의 실제 simulation.run 호출. Metal은 `VersionHistory.h:32` `the mass counter, flux kernels synchronised; Metal FV1 back end (HR)`와 `lisflood.cpp:783–784`의 실제 호출.<br>확인한 원문: user manual.pdf p.1·10–12; user manual +bridge.docx p.1·5(변환본); user manual.docx p.1·5(변환본) 쪽 이미지; `VersionHistory.h:31–34`; `v8.0:lisflood.cpp:403–418`; `lisflood.cpp:778–788` | A 판 차이 | PDF·bridge의 해법 목록은 현행 8.3의 전체 목록이 아니다. 8.0 이전 판(PDF 6.1.1·bridge 4.3.6) 기준, 그 판 코드는 배포본이 없다. FV1·DG2는 8.0 계열에서 추가되었다. Metal FV1은 8.3에서 추가되었다. |
| callflow:RF-015 | dg2new와 MWDG2 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61` `dg2new = multiwavelet 적응`. | `lisflood.cpp:794–796`의 주석 처리된 dg2new 호출.<br>`lisflood.cpp:447–450`의 `simulation.run(argc, argv);`.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61,83`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:29–31`; `v8.2:swe/dg2new.cpp:11–21,90–104`; `swe/dg2new.cpp:11–44,90–104`; `lisflood.cpp:447–450,790–801` | B 문서 오기 | dg2new는 CPU DG2 리팩터링 코드다. 활성 MWDG2 해법의 위치는 cuda/adaptive다. |
| callflow:RF-017 | 원분석·현재 코드 위치 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:7,29`의 `:34 main`. | `v8.2:lisflood.cpp:34` `int main(int argc, char *argv[])`;<br>`lisflood.cpp:37` `int main(int argc, char *argv[])`;<br>`v8.2:lisflood.cpp:772`와 `lisflood.cpp:775`의 Fast_MainStart 호출;<br>`VersionHistory.h:23` `#define LF_Release "8.3"`.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:7,29`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-lisflood2-driver.md:20–24`; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:26–27`; `v8.2:lisflood.cpp:34,770–783`; `lisflood.cpp:37,773–793`; `VersionHistory.h:16–23,31–32` | A 판 차이 | 노트의 8.2 분석 이력은 유지한다. 현재 raw 코드의 인용 위치와 표시 판 8.3을 별도로 갱신한다. main은 `lisflood.cpp:37`에 있다. Fast_MainStart 호출은 `lisflood.cpp:775`에 있다. |
| cpu-gpu-acc-adaptive:LG2-092 | CUDA entry와 adaptive 파서 | 구현 대조의 빌드 조건: `CMakeLists.txt:73` `if (CMAKE_CUDA_COMPILER)`<br>`CMakeLists.txt:77` `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)`<br>`CMakeLists.txt:178` `add_subdirectory(cuda/adaptive)` | `lisflood.cpp:437` `else if (Statesptr->acceleration == ON)`<br>`lisflood.cpp:442` `else if (Statesptr->acc_nugrid == ON)`<br>`lisflood.cpp:447` `else if (Statesptr->mwdg2 == ON \|\| Statesptr->hwfv1 == ON)`<br>확인한 원문: `CMakeLists.txt:72–77,178`; `lisflood.cpp:437–459`; `cuda/adaptive/cuda_adaptive_simulate.cu:151–175`; `VersionHistory.h:16–23`; `../LISFLOOD-FP-8.3-package/README.md:59–60` | C 문서 누락 | CUDA 해법별 entry와 별도 adaptive 파서를 기준으로 옵션 적용 범위를 정한다. |
| cpu-gpu-swe:LG1-001 | dg2new의 선택·빌드 | 구현 대조의 CPU 원문: `lisflood.cpp:792` `dg2::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`; `lisflood.cpp:796` `//solver.solve();` | CUDA: `CMakeLists.txt:108-113`에 `cuda/dg2/cuda_dg2_solver.cu`를 포함한다.<br>Metal: FV1만 구현한다. `metal/metal_integrate.cpp:7–13`의 `run_metal_fv1`은 `lis::metal::fv1::simulate`를 호출한다.<br>확인한 원문: `lisflood.cpp:778–796`; `makefile:29–34`; `CMakeLists.txt:51–64·108–113` | C 문서 누락 | dg2new는 별도 비활성 CPU 구현이다. 현재 실행 경로에서 호출되지 않음은 `lisflood.cpp:794–796`의 주석 처리로 확인된다. legacy Make는 이 파일을 컴파일 목록에 넣는다. 현재 CMake는 이 파일을 목록에 넣지 않는다. [10-21 전수 검증 정정] |
| docx-manual:LV1-253 | 매뉴얼에 없는 GPU 해법 | `fv2`·`acc_nugrid`·`mwdg2`·`hwfv1`. 두 매뉴얼에 없음. | `pars.cpp:590–628`은 각각 플래그를 ON으로 설정한다. 순서대로 CFL=`C(0.33)`·`C(0.7)`·`C(0.3)`·`C(0.5)`다. 네 분기의 `Solverptr->DepthThresh`는 모두 `C(1e-3)`다. `lisflood.cpp:429–459`의 CUDA 분기에서 각 simulator를 호출하고 반환한다.<br>확인한 원문: user manual.docx p.14–15·19–26(변환본); user manual.pdf p.11–12·15–21; `pars.cpp:590–628`; `lisflood.cpp:419–459·773–805` | C 문서 누락 | FV2·비균일 ACC·적응 MWDG2·HWFV1을 문서가 생략했다. 이 플래그만 켜고 GPU 경로에 들어가지 않으면 CPU FV1·DG2 호출로 자동 변환하지 않는다. |
| docx-manual:LV1-283 | adaptive 다중해상도 임계 식 | adaptive 다중해상도 임계 식. | `cuda/adaptive/mra/encode_and_thresh_topo.cu:29` `real epsilon_local = solver_params.epsilon / ( 1 << (solver_params.L - level) );`; 같은 파일:54 `if ( (z_details.get_max() / maxes.z) >= epsilon_local ) d_preflagged_details[parent_idx] = SIGNIFICANT;`; `cuda/adaptive/mra/reinsert_assem_sol.cu:18–20`의 수면·x/y 유량 재삽입.<br>확인한 원문: user manual.docx p.14–15·23–24(변환본); user manual.pdf p.11–12·18; `cuda/adaptive/mra/encode_and_thresh_topo.cu:29–54`; `cuda/adaptive/mra/reinsert_assem_sol.cu:18–20` | C 문서 누락 | 수준별 임계값과 정규화 detail 판정은 두 매뉴얼에 없다. 단일 DG2 격자의 slope limiter와 다르다. [10-21 전수 검증 보완] |
| docx-manual:LV1-294 | dg2new의 호출 여부 | `dg2new`의 실제 실행 여부. 매뉴얼에 없음. | `lisflood.cpp:790–796`에서 활성 호출은 `dg2::solve(...)`다. `//dg2new::DG2Solver solver(Fnameptr, &Fps, Statesptr, Parptr, Solverptr,` / `//        BCptr, Stageptr, Arrptr, verbosemode);`·`//solver.solve();`는 주석이다. `swe/dg2new.cpp:300` `// FIXME: BC treatment`; `CMakeLists.txt:50–64`의 SWE 목록에는 dg2new.cpp가 없다.<br>확인한 원문: user manual.docx p.14–15·23(변환본); user manual.pdf p.11–12·18; `lisflood.cpp:790–796`; `swe/dg2new.cpp:300`; `CMakeLists.txt:50–64`; `makefile:31`; `lisflood.cpp:447–450` | C 문서 누락 | dg2new는 적응 multiwavelet 구현이 아니다. `makefile:31`에 컴파일 대상으로 있어도 주 실행기에서 호출하지 않는다. 실제 적응 GPU는 LV1-279–283의 cuda/adaptive 경로다. |
| files-output:LI2-342 | metal 별칭·마른 NoData | 8.3 GPU 선택 별칭과 dry NoData 최적화 | `pars.cpp:965–968` `if (read_empty_param(param_name, line_number, param_value_ptr, "cuda", verbose, mode) \|\|`<br>`read_empty_param(param_name, line_number, param_value_ptr, "metal", verbose, mode))`<br>`{`<br>`Statesptr->cuda = ON;`; 패치 `2958–2965`의 metal 추가; 패치 `79`, `87` `+ if (Hold == C(0.0)) continue; // dry: nothing to add to the mass balance`<br>확인한 원문: `../LISFLOOD-FP-8.3-package/README.md:33·35`; `v8.3:lisflood-8.2-to-8.3.patch:75–89`; `pars.cpp:965–968` | A 판 차이 | metal은 공통 GPU 선택 상태를 켠다. v8.3의 마른 NoData 변경은 `if (Hold == C(0.0)) continue;`로 0인 질량수지 덧셈을 건너뛴다. |
| par:LI1-291 | 명령 줄 전용 분기 | user manual.pdf p.15–22의 `.par` 입력 표. | `lisflood.cpp:289` `for (i = 1; i < argc; i++) if (!strcmp(argv[i], "-version")) return(0);`<br>`lisflood.cpp:290` (빈 줄)<br>`lisflood.cpp:291` `for (i = 1; i < argc; i++) if (!strcmp(argv[i], "-compare_results"))`<br>`lisflood.cpp:309` `for (i = 1; i < argc - 1; i++) if (!strcmp(argv[i], "-resroot"))`<br>`lisflood.cpp:310` `{`<br>`lisflood.cpp:311` `sscanf(argv[i + 1], "%s", ParFp.res_prefix);`<br>`lisflood.cpp:312` `if (verbosemode == ON) printf("Results root name reset by command line: %s\n", ParFp.res_prefix);`<br>`lisflood.cpp:313` `}`<br>`lisflood.cpp:314` (빈 줄)<br>`lisflood.cpp:315` `compare_grids(compare_results_dir1, compare_results_dir2, ParFp.res_prefix, compare_results_ext);`<br>확인한 원문: user manual.pdf p.15–22; `lisflood.cpp:289–291,309–315` | C 문서 누락 | -version·-compare_results는 .par 키워드가 아니다. |
| par:LI1-367 | 공통 설정·별도 adaptive 파서 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:39` ``→ **단일 entry, 다중 솔버**: include 가 곧 솔버 카탈로그 — ACC·FV1·DG2 각각 **CPU + CUDA** 버전, 추가로 **acc_nugrid**(비균일격자=v8.x dynamic resolution adaptivity). 런타임 입력(parfile)으로 솔버 선택, `Solver` 구조체(:53)에 전역 설정.`` | `lisflood.cpp:447` `else if (Statesptr->mwdg2 == ON \|\| Statesptr->hwfv1 == ON)`<br>`lisflood.cpp:448` `{`<br>`lisflood.cpp:449` `lis::cuda::adaptive::Simulation simulation;`<br>`lisflood.cpp:450` `simulation.run(argc, argv);`<br>`cuda/adaptive/cuda_adaptive_simulate.cu:162` `SolverParams     solver_params(input_filename);`<br>`cuda/adaptive/cuda_adaptive_simulate.cu:163` `SimulationParams sim_params   (test_case, input_filename, solver_params.L);`<br>`cuda/adaptive/cuda_adaptive_simulate.cu:164` `PlottingParams   plot_params  (input_filename);`<br>`cuda/adaptive/cuda_adaptive_simulate.cu:165` `Depths1D         bcs          (test_case);`<br>`cuda/adaptive/cuda_adaptive_simulate.cu:166` `SaveInterval     saveint      (input_filename, "saveint");`<br>`cuda/adaptive/cuda_adaptive_simulate.cu:167` `SaveInterval     massint      (input_filename, "massint");`<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:39`; `lisflood.cpp:447–450`; `cuda/adaptive/cuda_adaptive_simulate.cu:162–167`; `lisflood.cpp:773–793` | C 문서 누락 | 일반 해법은 공통 Solver 설정을 쓴다. HWFV1·MWDG2는 같은 .par를 별도 구조체로 다시 읽는다. Apple Metal FV1 경로를 현행 판의 추가 분기로 적는다. |
| par:LI1-373 | dg2·mwdg2 매핑 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61` ``\| `swe/dg2.cpp`·`dg2new.cpp` \| **DG2** — 2차 Discontinuous Galerkin. **dg2new = multiwavelet 적응**(v8.2 headline: dynamic resolution adaptivity) \|``<br>`bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:83` ``- `swe/dg2new.cpp` — DG2 multiwavelet 적응 격자(v8.2 핵심, Kesserwani)`` | `lisflood.cpp:790` `else if (Statesptr->dg2 == ON)`<br>`lisflood.cpp:791` `{`<br>`lisflood.cpp:792` `dg2::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`<br>`lisflood.cpp:793` `Stageptr, Arrptr, verbosemode);`<br>`lisflood.cpp:794` `//dg2new::DG2Solver solver(Fnameptr, &Fps, Statesptr, Parptr, Solverptr,`<br>`lisflood.cpp:795` `//        BCptr, Stageptr, Arrptr, verbosemode);`<br>`lisflood.cpp:796` `//solver.solve();`<br>`lisflood.cpp:447` `else if (Statesptr->mwdg2 == ON \|\| Statesptr->hwfv1 == ON)`<br>`lisflood.cpp:448` `{`<br>`lisflood.cpp:449` `lis::cuda::adaptive::Simulation simulation;`<br>`lisflood.cpp:450` `simulation.run(argc, argv);`<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61,83`; `lisflood.cpp:447–450,790–796`; `v8.2:lisflood.cpp:444–450,780–786`; `lisflood.cpp:419–450` | B 문서 오기 | dg2는 CPU·CUDA DG2를 선택한다. dg2new는 주석 처리된 CPU 리팩터이다. 적응 multiwavelet 해법은 mwdg2이며 cuda/adaptive를 실행한다. |
| theory:LT1-300 | 후대 해법·GPU·Metal | user manual.pdf p.5 이력은 5.9에서 끝난다. p.10–11 표 1은 FV1·DG2·GPU·Metal을 적지 않는다. | `VersionHistory.h:31–40`은 8.3 CUDA·Metal, 8.1 병합, 8.0 FV1·DG2, 7.1 D8, 7.0 super-grid, 6.3 Froude 제한, 6.2 reservoir, 6.1 distributed rainfall, 6.0 최적화·NetCDF를 열거한다. 원문 예: `8.0  Jul 24 2020  FV1 and DG2 Solvers added (JS)`(`VersionHistory.h:34`). `lisflood.cpp:422–449`의 CUDA 분기는 FV1·FV2·DG2·ACC·ACC 비균일 격자·MWDG2/HWFV1을 선택한다.<br>확인한 원문: user manual.pdf p.5·10–11; `VersionHistory.h:31–40`; `lisflood.cpp:419–449·778–805`; `../LISFLOOD-FP-8.3-package/README.md:1–20`; `../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:19–24` | A 판 차이 | FV1·DG2는 v8.0의 추가 기능이다. v8.1 이후 CUDA 해법 목록이 확장되었다. v8.3 패치는 Metal 지원을 추가한다. 2013년 문서의 해법 목록을 현행 전체 목록으로 사용하지 않는다. |
| theory:LT1-413 | Trent의 해법 이름 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:49` “Trent — 추가 dynamic 처리” | `fp_trent.cpp:3` `FLOODPLAIN FLOW WITH ROE APPROXIMATE RIEMANN SOLVER 1st ORDER SCHEME`; `fp_flow.cpp:50`은 `CalcFPQxRoe`를 호출한다.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:49`; user manual.pdf p.11; `fp_trent.cpp:3`; `fp_flow.cpp:50` | B 문서 오기 | `fp_trent.cpp`는 고전 공간 1차 Roe 근사 리만 해법이다. |
| theory:LT1-414 | dg2new와 적응 해법 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61` “**dg2new = multiwavelet 적응**”; `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:83` “DG2 multiwavelet 적응 격자” | `lisflood.cpp:794–796` `//dg2new::DG2Solver solver(Fnameptr, &Fps, Statesptr, Parptr, Solverptr,` / `//        BCptr, Stageptr, Arrptr, verbosemode);` / `//solver.solve();`; `lisflood.cpp:447–450`은 `mwdg2`·`hwfv1`에 `lis::cuda::adaptive::Simulation`을 선택한다.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-architecture-source-map.md:61·83`; `swe/dg2new.cpp:1–38`; `lisflood.cpp:447–450·790–796` | B 문서 오기 | `dg2new`는 호출이 주석 처리된 CPU DG2 리팩터이다. 적응 해법 MWDG2·HWFV1은 `cuda/adaptive` 경로이다. |

## 대조 근거

- theory: [보고서](../../../_staging/recovery/compare/lisflood-theory-vs-code.md), [최종 근거 LT1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md).
- par: [보고서](../../../_staging/recovery/compare/lisflood-par-vs-code.md), [최종 근거 LI1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md).
- files-output: [보고서](../../../_staging/recovery/compare/lisflood-files-output-vs-code.md), [최종 근거 LI2](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md).
- docx-manual: [보고서](../../../_staging/recovery/compare/lisflood-docx-manual-vs-code.md), [최종 근거 LV1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md).
- bridge-docx: [보고서](../../../_staging/recovery/compare/lisflood-bridge-docx-vs-code.md), [최종 근거 LB1b](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md).
- build-83: [보고서](../../../_staging/recovery/compare/lisflood-build-83-vs-code.md), [최종 근거 LN1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LN1.md).
- cpu-gpu-swe: [보고서](../../../_staging/recovery/compare/lisflood-cpu-gpu-swe.md), [최종 근거 LG1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md).
- cpu-gpu-acc-adaptive: [보고서](../../../_staging/recovery/compare/lisflood-cpu-gpu-acc-adaptive.md), [최종 근거 LG2](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG2.md).
- callflow: [보고서](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md), [최종 근거 RF](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md).
