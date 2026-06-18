---
title: LISFLOOD-FP CUDA GPU 솔버 (cuda/ — entry·HLL flux·flow·boundary·ghost raster)
model: LISFLOOD-FP
component: cuda-gpu
canonical_source: self
citation_status: verified
verification_method: "cuda/{cuda_simulate.cu, cuda_solver.cu, cuda_hll.cu, cuda_flow.cu, cuda_boundary.cu, ghostraster.cpp} 및 fv1/cuda_fv1_{flow,solver,simulate}.cu, cuda_solver.cuh, cuda_solver.templates.cu, params.h, cuda_atomic.cuh 직접 read 후 file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[lisflood-fp-architecture-source-map]]"
---

# LISFLOOD-FP CUDA GPU 솔버

LISFLOOD-FP 의 GPU 경로(`cuda/`)는 천수방정식(SWE)을 **FV1(1차 유한체적 HLL Godunov)** 으로 푸는 정식 2D 솔버다. CPU 의 ACC(국소 관성) 솔버와 달리, GPU 경로는 보존형 SWE 를 HLL Riemann flux 로 직접 적분한다. 솔버 패밀리는 4종으로 분기한다:

| 서브디렉토리 | 수치 스킴 | 비고 |
|---|---|---|
| `cuda/fv1/` | 1차 FV Godunov + HLL | 정식 GPU SWE 솔버 (본 노트의 주 대상) |
| `cuda/dg2/` | 2차 불연속 Galerkin (slope-limited) | `cuda_dg2_slope_limit.cu` 등 |
| `cuda/acc/` | ACC(관성 근사) GPU 포팅 | `cuda_acc_flow.cu`, `Rainfall_uniform.h` |
| `cuda/acc_nugrid/` | **동적 비균일 격자(non-uniform grid)** ACC | Morton-code 트리·wavelet detail thresholding 기반 적응 해상도 |

> 공통 코어 커널·HLL flux·경계조건·ghost raster 는 `cuda/` 최상위에 있고 fv1/dg2 가 공유한다. 아키텍처 전반은 [[lisflood-fp-architecture-source-map]] 참조.

---

## 1. 자료구조와 메모리 모델

### 1.1 보존변수 벡터 `FlowVector`
3성분 구조체 $U=(H, HU, HV)$ — 수심·x운동량·y운동량 (`cuda/cuda_flow.cuh:9-13`). `__host__ __device__` 산술 연산자(+, −, *, /, 단항−)가 인라인 정의되어 커널 안에서 벡터 연산처럼 쓴다 (`cuda_flow.cuh:46-84`).

핵심 멤버 함수(`cuda/cuda_flow.cu`):
- `star(Z, Zstar)` — 정수압 재구성(hydrostatic reconstruction). $H^\star=\max(0,\,\eta-Z^\star)$ where $\eta=H+Z$ (`cuda_flow.cu:41-49`), 운동량은 속도 유지 $U^\star=(H^\star,\,H^\star u,\,H^\star v)$ (`cuda_flow.cu:4-13`).
- `physical_flux_x/y()` — 물리 flux $F_x=(HU,\,HU^2/H+\tfrac12 gH^2,\,HUHV/H)$ (`cuda_flow.cu:15-39`). 단, `DepthThresh` 이하 dry cell 은 0 벡터 반환.
- `speed(discharge)` — $H\ge$ `DepthThresh` 일 때만 $q/H$, 아니면 0 (dry-cell 0/0 회피, `cuda_flow.cu:51-64`).

### 1.2 `Flow` SoA (Structure-of-Arrays)
fv1 의 `Flow` 는 `H`, `HU`, `HV` 세 개의 분리된 디바이스 배열을 들고 다닌다 (`fv1/cuda_fv1_flow.cu:6-26`). SoA 배치는 coalesced 메모리 접근을 위한 것. pinned(host)·device 버전 둘 다 할당 (`allocate_pinned`/`allocate_device`).

### 1.3 GPU 상수·관리 메모리
`cuda/cuda_solver.cu:4-12` 에서 디바이스 전역 심볼 정의:
- `__constant__` : `geometry`, `rain_geometry`, `pitch`, `physical_params`, `solver_params`, `boundaries`, `sample_points` — 시뮬레이션 내내 불변, 상수 캐시 경유 broadcast.
- `__managed__ NUMERIC_TYPE dt` — Unified Memory. host/device 모두 `cuda::dt` 로 접근(타임스텝 동기화 매개) (`cuda_solver.cu:11`).
- `__managed__ int sample_buf_idx` (`cuda_solver.cu:12`).

`Geometry` 는 `xsz, ysz, blx, bly, tly, dx, dy` (geometry.h). `SolverParams`/`PhysicalParams` 는 `cuda/params.h` 에서 CPU 측 `Pars/Solver/States` 로부터 생성 — `cfl`, `max_dt(=InitTstep)`, `DepthThresh`, `SpeedThresh`, `g`, `manning(=FPn)` 등 (`params.h:5-60`).

### 1.4 블록 크기
$16\times16=256$ 스레드 블록 (`cuda_solver.cuh:2-4`: `CUDA_BLOCK_SIZE_X/Y=16`, `CUDA_BLOCK_SIZE=256`). `block_size` dim3 정의 `cuda_solver.cu:14`. 그리드는 `dim3(128,128)` 고정 grid-stride 패턴 (`fv1/cuda_fv1_simulate.cu:28`).

---

## 2. Ghost cell raster 레이아웃 (`ghostraster.cpp`)

FV1 은 도메인 사방에 1셀 두께 ghost 띠를 둔다. 두 가지 인덱싱 규약이 공존:

| 함수 | 값 | 의미 |
|---|---|---|
| `elements` | $(xsz+2)(ysz+2)$ | ghost 포함 전체 (`ghostraster.cpp:4-7`) |
| `pitch` | $xsz+2$ | 행 stride (`ghostraster.cpp:19-22`) |
| `offset` | $xsz+3$ | 첫 내부셀 선형 인덱스 = $1\cdot pitch+1$ (`ghostraster.cpp:24-27`) |
| `elements_H` | $xsz\cdot ysz$ | ghost 없는 H 격자(ACC용) (`ghostraster.cpp:9-12`) |
| `elements_Q` | $(xsz+1)(ysz+1)$ | 셀 경계 flux 격자 (`ghostraster.cpp:14-17`) |
| `pitch_ACC` | $xsz$ | ACC 경로는 ghost 없음 (`ghostraster.cpp:29-32`) |
| `offset_ACC` | $0$ (`ghostraster.cpp:34-37`) |

즉 **FV1 은 pitch=xsz+2(ghost 1셀)**, **ACC 는 pitch=xsz(ghost 없음)** 로 동일 raster API 가 두 솔버를 모두 서비스한다. `allocate()` 는 값 초기화 `new[...]()` 로 0 초기화 (`ghostraster.cpp:39-42`).

내부셀 선형 인덱스는 커널에서 `j*pitch + i` 로 계산 (예: `fv1/cuda_fv1_solver.cu:25`).

---

## 3. HLL Riemann 근사 flux (`cuda_hll.cu`)

코어 솔버. x-방향 `HLL::x(U_neg, U_pos)` 가 본체이고 y-방향은 회전 트릭으로 재사용한다.

**Dry-dry 단락**: 양쪽 다 `DepthThresh` 이하면 0 flux (`cuda_hll.cu:24-28`).

**속도 복원**: wet 쪽만 $U=HU/H$ (`cuda_hll.cu:30-44`).

**파속(wave speed) 추정** — Toro 의 two-rarefaction / 정적 추정:
$$A=\sqrt{gH},\quad H^\star=\frac{\left[\tfrac12(A_-+A_+)+\tfrac14(U_--U_+)\right]^2}{g}$$
(`cuda_hll.cu:46-52`).

좌/우 신호속도 $S_-,S_+$ — dry 쪽이면 건식 전선(dry front) 식 $U_\pm\mp 2A_\pm$, 아니면 $\min/\max$ 취함 (`cuda_hll.cu:54-72`):
$$S_-=\min(U_--A_-,\;U^\star-A^\star),\quad S_+=\max(U_++A_+,\;U^\star+A^\star)$$

**flux 분기** (`cuda_hll.cu:86-122`):
- $S_-\ge0$ → $F=F_-$ (`:86-89`)
- $S_-<0\le S_+$ → HLL 중간상태 식으로 $F.H, F.HU$ 계산, **횡 운동량 $F.HV$ 는 접촉파 속도 $S_{mid}$ 의 부호로 upwind** ($S_{mid}\ge0$ 이면 $V_-$, 아니면 $V_+$) (`:90-118`)
- else → $F=F_+$ (`:119-122`)

**y-방향 회전 재사용**: $U=(H,HV,-HU)$ 로 회전→`HLL::x`→역회전 (`cuda_hll.cu:4-16`). 코드 중복 제거.

---

## 4. FV1 솔버 커널 (`fv1/cuda_fv1_solver.cu`)

### 4.1 차원분리(dimensional splitting) 업데이트
`update_flow_variables` (`cuda_fv1_solver.cu:526-546`) 가 한 타임스텝을 구성:
1. (friction on 이면) `apply_friction` + ghost 갱신
2. `update_flow_variables_x` : $U^{old}\to U^x$ (중간상태)
3. `update_flow_variables_y` : $U^x\to U^{new}$
4. `std::swap(Uold, U)` 로 더블버퍼 핑퐁

**x 갱신 커널** (`cuda_fv1_solver.cu:293-384`): 블록당 shared memory 에 셀경계 flux `F` 와 `Hstar` 캐시 (`:304-305`). 블록은 x로 **1셀 겹치게**(halo) 배치 — `blockIdx.x*(blockDim.x-1)` (`:307`), 우단 블록 시작 스킵 (`:319`). 각 인터페이스서 `star()` 재구성 → `HLL::x` → shared 저장, `__syncthreads()` 후 좌/우 flux 차분으로 갱신:
$$H=H^0-\frac{\Delta t}{\Delta x}(F_e.H-F_w.H)$$
$$HU=HU^0-\frac{\Delta t}{\Delta x}\big[(F_e.HU-F_w.HU)-S_{bed,x}\big]$$
(`cuda_fv1_solver.cu:376-379`). 경계셀($i=0$ 또는 $xsz$)은 `Boundary::inside_x` 적용 (`:340-349`).

**y 갱신 커널** (`:386-479`): 동일 구조, y로 halo, $U^x$ 를 입력으로 $\Delta y$ 차분.

### 4.2 정수압 재구성 bed source (well-balanced)
`bed_source_x/y` (`cuda_fv1_solver.cu:261-291`) — $Z^\dagger=Z^\star-\max(0,-(\eta-Z^\star))$ 로 보정한 well-balanced 바닥경사항:
$$S_{bed,x}=-g\cdot\tfrac12(H^\star_w+H^\star_e)\frac{Z^\dagger_e-Z^\dagger_w}{\Delta x}$$
정지수면(lake-at-rest) 보존을 위한 표준 처리.

### 4.3 마찰 (semi-implicit Manning)
`apply_friction` (`cuda_fv1_solver.cu:205-259`): $C_f=gn^2/H^{1/3}$, $S_f=-C_f\,u\,|\mathbf{u}|$ 를 점-내재(point-implicit) 분모 $D$ 로 안정화:
$$D_x=1+\frac{\Delta t\,C_f}{H}\frac{2u^2+v^2}{|\mathbf u|},\qquad HU\mathrel{+}=\frac{\Delta t\,S_{f,x}}{D_x}$$
(`:250-256`). `DepthThresh`/`SpeedThresh` 이하면 운동량 0 처리 (`:224-238`). Manning $n$ 은 공간변동 raster(`manning[...]`) 또는 전역 상수(`physical_params.manning`) (`:240-242`).

### 4.4 적응 타임스텝 per-element CFL
`update_dt_per_element` (`cuda_fv1_solver.cu:64-99`): 셀별
$$\Delta t=\min\!\left(\frac{\mathrm{cfl}\cdot\Delta x}{|u|+\sqrt{gH}},\;\frac{\mathrm{cfl}\cdot\Delta y}{|v|+\sqrt{gH}}\right)$$
dry cell 은 `max_dt` (`:95`). 결과 `dt_field` 는 §5 에서 전역 min reduction.

### 4.5 Solver 객체 메모리
생성자에서 3개 디바이스 `Flow`(`U1,U2,Ux`) 할당 — 핑퐁 2개 + x중간상태 1개 (`cuda_fv1_solver.cu:505-507`), `Uold=U1, U=U2` (`:497-498`). 소멸자에서 해제 (`:594-599`).

---

## 5. 동적 타임스텝 reduction (`cuda_solver.templates.cu`)

`DynamicTimestep<F>` (`cuda_solver.cuh:80-106`)는 NVIDIA **CUB `DeviceReduce::Min`** 으로 셀별 dt 의 전역 최소를 구한다.
- 생성자: 첫 호출로 워크스페이스 바이트 수 질의 → `d_temp` 할당, `dt_field` 할당 (`cuda_solver.templates.cu:23-35`). 비적응(`adaptive_ts != ON`)이면 `dt=max_dt` 고정 (`:36-39`).
- `update_dt()`: 솔버가 `dt_field` 채움 → CUB Min → `cuda::dt`(managed) 에 기록 → `cuda::sync()` (`:73-85`).

`DynamicTimestepACC` 는 ghost 없는 `elements_H` 크기로 동일 동작(ACC 경로, `:42-71`, `:87-97`).

---

## 6. 경계조건 & 점소스 (`cuda_boundary.cu`)

### 6.1 호스트측 디바이스 초기화
`Boundary::initialise` (`cuda_boundary.cu:496-511`): 시계열·BC·점소스(PS)를 디바이스에 복사 후 `boundaries` 상수심볼로 업로드. `BoundaryConditions` 구조체(`cuda_boundary.cuh:19-36`)는 `BC_type/value/time_series`, `PS_type/value/time_series/idx`, `all_time_series` 를 `__restrict__` 포인터로 보유.

`initialise_BC/PS` 는 시계열 포인터를 host vector 내 주소 매칭으로 디바이스 인덱스로 변환(`cuda_boundary.cu:564-582`, `:611-628`). PS 셀 위치는 `ypi*pitch+xpi+offset` 선형화 (`:636-639`).

### 6.2 시간변동 갱신 커널
- `linear_interpolate` (`cuda_boundary.cu:11-36`) — 시계열 선형보간(범위밖이면 끝값 클램프).
- `update_time_series<<<1,1>>>` (`:38-48`) 모든 시계열 `current_value` 갱신.
- `update_time_varying_boundary_conditions<<<64,256>>>` / `..._point_sources` (`:50-78`): `HVAR3`/`QVAR5` 타입만 현재값 반영.
- 호스트 런처 `update_time_series` 가 셋을 순차 호출 (`:646-654`).

### 6.3 점소스 적용
`update_point_sources` (`cuda_boundary.cu:96-136`):
- `HFIX2/HVAR3`(수위지정): $H_{new}=\min(0, \text{val}-Z)$, 변화량을 discharge 로 질량통계 누적.
- `QFIX4/QVAR5`(유량지정): $H\mathrel{+}=q\,\Delta t/\Delta x$.

분리 버전 `update_point_sources_Q`/`_H` (`:138-216`)는 ACC 경로용(Q 먼저·H 나중). 질량 in/out 은 `accumulate_point_source_stats` 가 atomicAdd 누적 (`:80-94`).

### 6.4 외부/내부 상태 (ghost 채우기)
`outside_x` (`cuda_boundary.cu:331-367`)는 BC 타입별 ghost 상태:
- `FREE1` 그대로, `HFIX2/HVAR3` $H=\max(0,\text{val}-Z^\star)$, `QFIX4/QVAR5` $HU=\pm\text{val}$, default(`NONE0`) 반사벽 $HU=-HU$ (`:362`).
- `outside_y`/`inside_y` 는 $(H,HV,HU)$ 회전으로 x 버전 재사용 (`:369-384`, `:410-423`).

방위별 ghost 1D 인덱스 매핑 `index_w/e/n/s` (FV1, `:425-459`)와 `_ACC` 변형(off-by-one 차이, `:461-495`)이 둘레를 따라 BC 배열에 사상.

### 6.5 H 갱신·드레인
`update_H` 커널 (`cuda_boundary.cu:219-265`, ACC 경로): flux 발산으로 $\Delta V=\Delta t(q_{x0}-q_{x1}+q_{y0}-q_{y1})$, 음수 깊이 방지 `WDweight` 부분 flux 스케일링(`drycheck`) (`:247-257`) 후 $H\mathrel{+}=\Delta V/\Delta x^2$, 음수는 0 클램프 (`:259-261`).
`drain_nodata_water`/`...ACC` (`:266-327`): nodata 고도($\approx$`nodata_elevation`) 셀의 물을 배출하고 질량통계에 반영. `__launch_bounds__(256)` 로 레지스터 압박 제한.

---

## 7. 질량보존 통계 (`cuda_solver.cu`)

`update_mass_stats_x/y` (`cuda_solver.cu:16-80`)는 도메인 가장자리($i=0$ 또는 $xsz$ 등)에서 flux $F.H$ 부호에 따라 유입/유출을 `atomicAdd` 누적 ($\times\Delta y$ 또는 $\times\Delta x$). flux 커널에서 매 인터페이스 호출됨 (예: `cuda_fv1_solver.cu:355`, `:451`). atomicAdd double 폴리필은 `cuda_atomic.cuh:5-22` (compute capability < 6.0 대비 CAS 루프).

---

## 8. 메인 시뮬레이션 루프 (`fv1/cuda_fv1_simulate.cu`)

`Simulation::run` (`cuda_fv1_simulate.cu:18-209`) 전체 흐름:

**셋업** (`:34-138`):
- DEM 로드 + 경계 클램프(`:34-36`), geometry/pitch 상수심볼 업로드(`:39-40`).
- `d_DEM`, `Zstar_x/y`(정수압 재구성 바닥) 디바이스 할당·초기화(`:42-49`).
- 동적 강우 `DynamicRain`(Unified allocator)(`:53-55`), `Flow U` pinned 할당+초기수위/유량 로드(`:57-62`).
- Manning raster(옵션, `:64-73`), `PhysicalParams`/`SolverParams` 상수 업로드(`:75-81`).
- 경계조건 디바이스 초기화(`:85-87`), `Solver`(=fv1 솔버) 생성(`:89-91`), `DynamicTimestep` 생성(`:93-94`).
- 통계/최대수심장/스냅샷/스테이지 샘플러 객체(`:97-133`).

**시간 루프** `while (t < Sim_Time)` (`:140-190`):
1. 동적/균일 강우 적용(`:142-153`)
2. 순간질량 0클리어·BC 시계열 갱신·점소스 적용·질량누적(`:155-160`)
3. `update_ghost_cells()`(`:161`)
4. `dynamic_dt.update_dt()` + `MinTstep` 추적(`:162-163`)
5. `t += dt` (`:166`)
6. `update_flow_variables(...)` ← **핵심 SWE 적분**(`:169-170`)
7. nodata 드레인(옵션)·질량누적·최대수심 갱신(`:171-177`)
8. 출력 필요시 샘플링·통계·스냅샷 기록(`:179-189`)

**정리**: 루프시간 출력, 샘플/스냅샷/최대장 flush, 디바이스/pinned 메모리 해제(`:192-208`).

---

## 9. acc_nugrid — 동적 비균일 격자 (개요)

`cuda/acc_nugrid/` 는 ACC 솔버를 **Haar wavelet 기반 적응 격자**로 확장한 별도 파이프라인이다 (`cuda_acc_nugrid_simulate.cu`). 일반 FV1 의 균일 raster 와 달리:
- **Morton(Z-order) 코드** 로 셀 선형화 (`generate_all_morton_codes.cuh`, `MortonCode.h`).
- **scale/detail 계수** wavelet 분해 후 `preflag_topo`/`encode_and_thresh_topo` 로 유의(detail) 임계화하여 활성 셀만 유지 — 동적 해상도 (`get_max_scale_coefficients.cuh`, `traverse_tree_of_sig_details.cu`).
- **비균일 이웃·인터페이스** 탐색(`find_nonuniform_neighbours.cu`, `find_interfaces.cu`, `count_interfaces_per_neighbours.cu`) 후 `compute_q`→`update_h` 로 ACC 유량/수위 갱신.
- CFL dt 는 `get_dt_CFL.cu`/`calculate_dt.cu`.
- 입출력은 VTK(`write_soln_vtk.cu`)·체크포인트 별도 구현.

(이 트리는 60+ 커널 파일의 독립 서브시스템 — 상세 분석은 별도 노트 권장. 본 노트는 존재·역할만 명시.)

---

## 핵심 요약

- GPU 정식 경로(`fv1`)는 **HLL Godunov + 정수압 재구성(well-balanced bed source) + semi-implicit Manning 마찰 + 차원분리 + CUB Min 적응 dt** 의 완전한 1차 SWE 솔버.
- 메모리: `FlowVector(H,HU,HV)` SoA, FV1 은 ghost 1셀(`pitch=xsz+2`)·ACC 는 ghost 없음(`pitch=xsz`), 솔버상수는 `__constant__`, dt 는 `__managed__`.
- HLL 커널이 코어이며 y방향은 회전 재사용으로 코드 중복 제거.
- 4개 솔버 패밀리(fv1/dg2/acc/acc_nugrid)가 동일 HLL/boundary/ghostraster 인프라 공유, acc_nugrid 는 Morton+wavelet 동적해상도 별도 파이프라인.
