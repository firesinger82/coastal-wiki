---
title: "LISFLOOD-FP GPU 적응격자 솔버 — cuda/adaptive (HWFV1/MWDG2 멀티웨이블릿 MRA)"
model: LISFLOOD-FP
component: adaptive-solver
canonical_source: self
citation_status: verified
verification_method: "raw v8.2 cuda/adaptive/ 직접 read: cuda_adaptive_simulate.cu(962) 전체 + mra/{Filters.h,encode_and_thresh_{flow,topo},regularisation,extra_significance,decoding_all,traverse_tree_of_sig_details,preflag_details,get_max_scale_coeffs,get_max_from_array}.cu + classes/{SolverParams,SimulationParams,Detail,Maxes}.h + operators/{fv1,dg2}_update.cu + input/read_command_line_params.cpp — file:line 전수 (2026-07-07). dispatch lisflood.cpp:444-448 직접 확인."
note_author: "Claude Fable 5"
note_date: 2026-07-07
related:
  - "[[lisflood-fp-architecture-source-map]]"
  - "[[lisflood-fp-swe-fv1-dg2]]"
  - "[[lisflood-fp-cuda-gpu]]"
---

# LISFLOOD-FP 멀티웨이블릿 적응격자 — `cuda/adaptive/` (HWFV1 · MWDG2)

> 소스: `models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/` (250 파일). 이하 file:line 은 이 디렉토리 기준.
> **정체**: v8.x headline "dynamic resolution adaptivity"의 실체. parfile `hwfv1`/`mwdg2` 키워드 → `lis::cuda::adaptive::Simulation`(`lisflood.cpp:444-448`, CUDA 빌드 전용). [[lisflood-fp-swe-fv1-dg2]]의 정정(★`swe/dg2new.cpp`≠멀티웨이블릿)이 예고한 **실제 MW 솔버 노트**. 코드 내 인용: "Fig 2 of Kesserwani and Sharifian et al. (2020)"(`cuda_adaptive_simulate.cu:104`).

## 0. 자료구조 — 격자 계층 + Z-order
- 정방 2^L×2^L finest 격자 위 **grid hierarchy**: 레벨 n 에 4^n 요소, 전체 (4^(L+1)−1)/3 을 1D 배열에 적층, 각 레벨은 Morton code Z-order (`cuda_adaptive_simulate.cu:117-132` 주석 + `zorder/`). L=`max_ref_lvl` parfile 키워드(`classes/SolverParams.h:33`).
- 자식 번호는 논문 Fig 2 대비 **상하 flip**(원점 top-left, `:101-114`).
- 도메인 크기·xll/yll 은 표준 `DEMfile` ASCII 헤더에서, `sim_time`·`fpfric` 은 parfile 에서 (`classes/SimulationParams.h:37-57`).

## 1. 두 솔버 (`types/SolverTypes.h`)
| 키워드 | 웨이블릿 | 셀 당 DOF | CFL(하드코딩) |
|---|---|---|---|
| `hwfv1` | **Haar**(HW) — H0,H1,G0,G1=±1/√2 (`mra/Filters.h:5-8`) | 변수당 스칼라 1 (η,qx,qy,z) | 0.5 (`SolverParams.h:38-42`) |
| `mwdg2` | **multiwavelet**(MW, Alpert 계열) — 3×3 필터행렬 HH0-3(저역)+GA/GB/GC0-3(고역) (`Filters.h:10-56,58-`) | 변수당 Legendre 모드 3 (0·1x·1y 평면계수) | 0.3 (`SolverParams.h:43-47`) |

부모↔자식 변환: HW `encode_scale`=평균(`mra/encode_scale.cuh:10-13`)·detail α/β/γ(`mra/encode_details.cuh:60-75`); MW 는 모드 3개를 4 자식에 대해 행렬 축약(`encode_scale.cuh` `encode_scale_0/1x/1y`), detail 도 모드별 α/β/γ 9개. CLI 오버라이드: `-epsilon`·`-solver`·`-dirroot`(`input/read_command_line_params.cpp:17-45`).

## 2. 스텝 당 MRA 사이클 (`cuda_adaptive_simulate.cu:422-924`)
1. **인코딩**(bottom-up, L−1→0): 자식 4개→부모 scale + detail, 임계 `‖detail‖/maxes ≥ ε_local` 로 significant 판정 — `ε_local = ε/2^(L−n)` (`mra/encode_and_thresh_flow.cu:46,215-217`; 래퍼 `encoding_all.cu`).
2. **정규화**(regularisation): 자식 significant → 부모 강제 significant (트리 완결, `mra/regularisation.cu:54,81`; `get_reg_tree.cu`).
3. **예측**(extra significance): `‖detail‖ ≥ ε_local·2^(M_BAR+1)` 이면 자식 4개 선-refine — **`M_BAR=1.5` 하드코딩**(`mra/extra_significance.cuh:4`, `.cu:36,60`).
4. **디코딩**(top-down): significant 부모의 자식 계수 재구성(`mra/decoding.cu`; `decoding_all.cu` 가 3.과 4.를 묶음).
5. **리프 추출**: 트리 하강, 첫 insignificant 노드가 활성 셀(`mra/traverse_tree_of_sig_details.cu:41-87`) → z-order 역변환·compaction 으로 **비균일 활성 셀 목록** `d_assem_sol` 조립(`:528-584`).
6. 이웃 탐색은 **finest 격자 전점**에서 활성 조상 인덱스를 찾는 방식(`neighbours/find_neighbours.cu`) → 이웃 간 레벨 차 무제한 허용(2:1 강제 없음, §4 grading 참조).
7. 솔버 업데이트: HWFV1 = 1단 FV1(`operators/fv1_update.cu`); MWDG2 = **RK2 2단**(stage1 `:681`, 2단 평균 `dg2_update.cu:326-334`), 단간에 `for_nghbrs` 재인코딩(detail 미갱신, 이웃용 부모계수만 동기화, `:710-725`; `encode_and_thresh_flow.cu:251`). `limitslopes` 시 Krivodonova 계열 슬로프 리미터(`operators/limit_slopes.cu`, finest 레벨 한정 `:23`).
8. Δt = wet 셀 `CFL·Δx_loc/(|u|+√(gh))` 의 전역 min-reduce(`fv1_update.cu:234-237`, `dg2_update.cu:354-357`, `operators/get_dt_CFL.cu`); dry 셀은 `initial_tstep` 기록(`fv1_update.cu:51`, `dg2_update.cu:61`).

경계·point source·stage 셀 및 (`refine_wall` 시) 벽 인접대는 **영구 preflag** — 항상 finest 유지(`mra/preflag_details.cu:24-88`, `refine_high_wall.cu`).

## 3. ★주요 findings (code-only 사실)
- **★`maxes.qy` copy-paste 버그**: detail 정규화 분모 qy 최대값을 **`qx0` 배열로 계산**(`mra/get_max_scale_coeffs.cu:23` — `maxes.qy = get_max_from_array(d_assem_sol.qx0, …)`). max|qx|≫max|qy| 인 흐름에서 qy detail 이 과소 정규화 → y-방향 특징 **과소-refine** 가능. v8.2 Zenodo 정본 기준 미수정.
- **정규화 분모 하한 1.0 클램프**: `max(*h_max_out, C(1.0))`(`mra/get_max_from_array.cu:56`) — max|q|<1, max|z|<1 인 **실험실 스케일에서 상대 임계가 사실상 절대 임계로 전환**(스케일 비불변). 소규모 벤치마크에서 ε 재보정 필요.
- **ε=0 ⇒ 균일격자 모드**: regrid 블록은 `epsilon>0 || first_t_step` 에서만 실행(`cuda_adaptive_simulate.cu:479`) — ε=0 이면 첫 스텝 후 finest 균일격자 고정(= 비적응 GPU FV1/DG2).
- **`grading`(이웃 균형) 은 MWDG2 지형 preflag 에서만**: topo 인코딩 MW 분기에서 significant 셀의 동레벨 이웃 4개 flag(`mra/encode_and_thresh_topo.cu:89-118`) — HWFV1 분기·flow 인코딩에는 부재. 일반적으로 **2:1 balance 는 강제되지 않음**(§2-6).
- **`tol_q` 데드 파라미터**: 0 하드코딩(`SolverParams.h:16`), parfile·CLI 미노출 → q-임계 절사(`encode_and_thresh_flow.cu:52` 외 다수, `fv1_update.cu:219`)는 전부 무동작.
- **첫 Δt=0.001 s 하드코딩**(`cuda_adaptive_simulate.cu:184`); CFL 값도 솔버별 고정(§1) — parfile `initial_tstep` 은 dry-cell Δt 후보로만 쓰임(§2-8).
- **별도 미니앱 성격**: `simulation.run(argc, argv)` 가 parfile 을 **자체 키워드로 재파싱**(`max_ref_lvl`·`epsilon`·`hwfv1/mwdg2`·`grading`·`limitslopes`·`tol_Krivo`·`refine_wall`·`ref_thickness`·`startq2d`, `SolverParams.h:33-72`) — 본체 파서(input.cpp)의 State 를 사실상 무시. 합성 테스트 22종 내장(`cuda_adaptive_simulate.cu:59-87`), `monai.dem`·`oregon-seaside-0p02m.dem` 파일명 하드코딩 특례(`SimulationParams.h:58-59`).

## 4. Primary sources
- **Kesserwani & Sharifian (2020)** — 코드 내 직접 인용(`cuda_adaptive_simulate.cu:104`); (Multi)wavelet 적응 Godunov/DG2 정식화(*Adv. Water Resour.* 계열).
- **Sharifian, Kesserwani et al.** — LISFLOOD-FP 8.x GPU 솔버 논문(*GMD*; `hwfv1`/`mwdg2` 명칭 출처) → [[lisflood-fp-official-resources]].
- 정본 소스: Zenodo doi:10.5281/zenodo.13121102 (v8.2).

## 5. 관련
- [[lisflood-fp-swe-fv1-dg2]] — CPU FV1/DG2(균일격자)·dg2new 정정의 본편
- [[lisflood-fp-cuda-gpu]] — GPU 공통 인프라·acc_nugrid(Haar 적응 ACC, 본 노트와 별개 파이프라인)
- [[lisflood-fp-architecture-source-map]] — 솔버 카탈로그·디스패치
