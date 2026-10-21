---
title: "LISFLOOD-FP full SWE 솔버 — FV1 / DG2 (Godunov · Discontinuous Galerkin · HLL Riemann)"
model: LISFLOOD-FP
component: swe-solver
canonical_source: self
citation_status: verified
verification_method: "swe/{fv1,dg2,dg2new,hll,flux,fields,boundary}.cpp + hll_include.h + dg2new.h 전수 Read, dispatch는 v8.2:lisflood.cpp:775-792 직접 확인 (2026-06-18); 2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "lisflood-fp-architecture-source-map.md"
source_scope: LISFLOOD-FP/swe/*
---

# LISFLOOD-FP full SWE 솔버 (SEAMLESS-WAVE / Kesserwani 계열)

LISFLOOD-FP의 전통 솔버(local-inertial `acceleration`, SGC)와 별개로 `swe/`
디렉토리에는 **완전 천수방정식(full Shallow Water Equations)** 을 푸는 신규
유한체적/DG 솔버가 들어 있다. 두 가지 실가동 경로가 있다.

| 옵션 | 함수 | 정확도 | 자료구조 |
|---|---|---|---|
| `fv1` | `fv1::solve` (`swe/fv1.cpp:10`) | 1차 Godunov 유한체적 (FV1) | cell-centred H,HU,HV |
| `dg2` | `dg2::solve` (`swe/dg2.cpp:14`) | 2차 Discontinuous Galerkin (DG2) + RK2 | cell-mean + x·y slope 계수 |

FV1 분기는 `lisflood.cpp:778–788`이다. [10-21 대조 정정]
8.3은 `#ifdef METAL_ENABLED` 안의 `if (Statesptr->cuda == ON && metal_is_available())`에서 Metal FV1을 호출한다(`lisflood.cpp:780–784`). [10-21 대조 정정]
그 조건이 거짓이면 CPU FV1을 호출한다(`lisflood.cpp:785–788`). [10-21 대조 정정]
CPU DG2 분기는 `lisflood.cpp:790–793`이다. [10-21 대조 정정]

> **중요 정정 — `dg2new`는 multiwavelet 적응 솔버가 아니다.**
> `swe/dg2new.cpp`(`dg2new::DG2Solver`, `:11`)는 **균일격자 CPU DG2 리팩터링
> 시제품**이며, `lisflood.cpp:794–796`에서 **주석 처리되어 비가동** 상태다. [10-21 대조 정정]
> BC 처리가 `// FIXME: BC treatment`(`dg2new.cpp:300, 350`)로 미완이고
> 슬로프 리미터·점원(point source)도 없다. 실제 multiwavelet(MW) 적응 격자
> 솔버는 `swe/`가 아니라 **GPU 측 `cuda/adaptive/mra/`** 에 있다
> (`cuda/adaptive/mra/encode_and_thresh_flow.cu`,
> `cuda/adaptive/types/SolverTypes.h` 등 — 본 노트 범위 밖, grep 확인 2026-06-18).
> 따라서 이 노트는 `dg2new`를 "DG2 자료구조·연산자를 객체지향으로 재정리한
> 참고 구현"으로만 다룬다.

공통 파서는 `dg2depththresh`와 `dg2thindepth_tstep`을 읽는다(`pars.cpp:708–727`). [10-21 대조 정정]
두 입력 필드는 활성 계산에서 사용하지 않는다([par:LI1-233·234 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)). [10-21 대조 정정]

지배방정식은 보존형 2D SWE:

$$
\partial_t \begin{pmatrix}H\\HU\\HV\end{pmatrix}
+ \partial_x \begin{pmatrix}HU\\ HU^2/H + \tfrac12 gH^2\\ HUV\end{pmatrix}
+ \partial_y \begin{pmatrix}HV\\ HUV\\ HV^2/H + \tfrac12 gH^2\end{pmatrix}
= \begin{pmatrix}0\\ -gH\,\partial_x z\\ -gH\,\partial_y z\end{pmatrix} + \text{friction}
$$

여기서 $H$=수심, $HU,HV$=단위폭 유량(discharge), $z$=하상고(DEM).

---

## 1. 자료구조 (`swe/fields.cpp`)

`allocate_swe_fields`(`fields.cpp:4`)가 셀당 보존변수와 면(face) 플럭스 버퍼를
잡는다.

| 배열 | 크기 | 의미 | line |
|---|---|---|---|
| `HU`,`HV` | `xsz*ysz` | 단위폭 유량 ($H$는 기존 acceleration 솔버와 공유) | `fields.cpp:10-11` |
| `FHx,FHUx,FHVx` | `(xsz+1)*(ysz+1)` | x-면 HLL 플럭스 (질량·x운동량·y운동량) | `fields.cpp:12-14` |
| `FHy,FHUy,FHVy` | 〃 | y-면 플럭스 | `fields.cpp:15-17` |
| `Zstar_x,Zstar_y` | 〃 | wetting/drying 보정 하상고 $z^\star$ | `fields.cpp:18-19` |
| `Hstar_*_{x,y}` | `xsz*ysz` | 면 좌/우 재구성 수심 $H^\star$ (neg=cell의 +면, pos=cell의 −면) | `fields.cpp:20-23` |

면 배열이 `xsz+1` 폭을 쓰므로 x-플럭스 인덱싱은 `j*(xsz+1)+i`, 셀 변수는
`j*xsz+i`로 일관되게 다르다(`fv1.cpp:272` vs `:262`).

---

## 2. HLL Riemann 솔버 (`swe/hll.cpp`, `hll_include.h`)

면 플럭스는 **HLL 근사 Riemann 솔버**로 계산한다. `HLL`(`hll.cpp:43`)이 본체이고
실제 식은 인라인 헤더 `hll_include.h`로 분리되어 있다(`hll.cpp:60`에서 `#include`).

방향 처리 (회전 불변성):
- `HLL_x`(`hll.cpp:6`) — 그대로 호출.
- `HLL_y`(`hll.cpp:24`) — 인수를 회전해 호출: `HLL(...,H, HV, -HU, ...)` 뒤
  `HU_flux = -HU_flux`(`hll.cpp:38-40`). 즉 y-방향을 x-문제로 사상.

### 2.1 파속(wave speed) 추정 — two-rarefaction

좌(`neg`)·우(`pos`) 상태로 중간 상태를 추정한다 (`hll_include.h:33-39`):

$$
a_{L,R}=\sqrt{gH_{L,R}},\quad
H^\star=\frac{\big[\tfrac12(a_L+a_R)+\tfrac14(u_L-u_R)\big]^2}{g},\quad
u^\star=\tfrac12(u_L+u_R)+a_L-a_R
$$

파속 (`hll_include.h:41-59`):

$$
S_L=\min(u_L-a_L,\; u^\star-a^\star),\qquad
S_R=\max(u_R+a_R,\; u^\star+a^\star)
$$

**건/습 경계 dry-bed 보정**: 좌가 마르면 $S_L=u_R-2a_R$
(`hll_include.h:42-45`), 우가 마르면 $S_R=u_L+2a_L$
(`hll_include.h:52-55`) — 마른 둑 위 rarefaction front 속도.

### 2.2 HLL 플럭스 선택 (`hll_include.h:69-108`)

$$
\mathbf{F}^{HLL}=
\begin{cases}
\mathbf{F}_L & S_L\ge 0\\[2pt]
\dfrac{S_R\mathbf{F}_L-S_L\mathbf{F}_R+S_LS_R(\mathbf{U}_R-\mathbf{U}_L)}{S_R-S_L} & S_L<0\le S_R\\[6pt]
\mathbf{F}_R & S_R<0
\end{cases}
$$

질량·x운동량은 위 공식 그대로(`hll_include.h:77-87`). **y운동량(횡방향 스칼라)은
접촉파 기준 upwind**: 중간 파속 $S_M$(`:89-92`)의 부호로
$HV_{flux}=H_{flux}\cdot V_L$ (if $S_L<0\le S_M$) 또는 $V_R$
(`hll_include.h:94-101`) — 이류식(advection) 처리로 충격 시 진동 억제.

양면 모두 마르면 즉시 0 플럭스 반환(`hll_include.h:1-7`).

---

## 3. FV1 솔버 (`swe/fv1.cpp`)

### 3.1 시간 루프 (`fv1::solve`, `fv1.cpp:10`)

단계 순서(`fv1.cpp:43-52`):
1. `rain.update_H` / `update_point_sources`(`:187`) — 강우·점원으로 $H$ 갱신.
2. `apply_friction`(`:104`) — 반음해(semi-implicit) 마찰.
3. `update_Hstar` — wetting/drying 재구성 (외부 `fv1/modifiedvars.h`).
4. `update_fluxes`(`:250`) + `update_fluxes_on_boundaries`(`:306`) — 내부·경계 면 HLL.
5. `update_flow_variables`(`:423`) — 보존형 갱신.
6. `drain_nodata_water`(`:157`) — nodata 셀 배수.

적응 시간스텝이면 CFL로 다음 dt 산정(`fv1.cpp:61-64`).

CPU FV1·DG2는 DynamicRain 입력을 사용한다(`swe/fv1.cpp:34–50`; `swe/dg2.cpp:52–76`). [10-21 대조 정정]
공통 파서의 파일 수용과 실제 해법의 외력 지원은 다르다([par:LI1-314 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md)). [10-21 대조 정정]

### 3.2 보존형 갱신 (`update_flow_variables`, `fv1.cpp:423`)

명시적 1차 오일러 + 면 플럭스 발산:

$$
H^{n+1}=H^n-\Delta t\Big[\frac{F^H_e-F^H_w}{\Delta x}+\frac{F^H_n-F^H_s}{\Delta y}\Big]
$$

(`fv1.cpp:441-442`). 운동량은 동일 형태에 **하상 경사 소스항**을 더한다
(`fv1.cpp:450-462`).

### 3.3 well-balanced 하상 소스항 (`bed_source_x/y`, `fv1.cpp:467`)

$$
S^{bed}_x = -g\cdot\tfrac12(H^\star_{neg}+H^\star_{pos})\cdot
\frac{z^\dagger_{neg}-z^\dagger_{pos}}{\Delta x}
$$

(`fv1.cpp:481-482`). $z^\dagger$(`Zdagger_*`)는 wetting/drying 보정 하상고
(외부 `modifiedvars.h`).
CPU FV1의 Hstar는 갱신 전 상태이다(`swe/fv1.cpp:43–48`). [10-21 대조 정정]
현재 CPU 구현은 바닥 원천항의 Zdagger에 갱신 후 수심을 읽는다(`swe/fv1.cpp:441–452`; `swe/fv1/modifiedvars.cpp:329`). [10-21 대조 정정]
CUDA·Metal은 갱신 전 수심을 읽는다(`cuda/fv1/cuda_fv1_solver.cu:372,467`; `metal/fv1/metal_fv1_kernels.metal:501,611`). [10-21 대조 정정]
부분 건조 조건에서 두 시점의 수심을 함께 쓰는 결함 후보 강도는 중간이다([cpu-gpu-swe:LG1-012 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]

### 3.4 마찰 (`apply_friction`, `fv1.cpp:104`)

Manning 마찰을 반음해로 처리. $C_f=g n^2/H^{1/3}$(`fv1.cpp:141`),
마찰 소스 $S_{f,x}=-C_f U|\mathbf{u}|$(`:144`), 분모에 Jacobian 항
$D_x=1+\Delta t\,C_f(2U^2+V^2)/(H|\mathbf{u}|)$(`:146-147`)을 두어
$HU \mathrel{+}= \Delta t\,S_{f,x}/D_x$(`:151`).
CPU FV1은 건조 수심 검사를 통과한 셀에서 `if (FABS(U) <= Solverptr->SpeedThresh && FABS(V) <= Solverptr->SpeedThresh)`이면 HU·HV를 0으로 만든다(`swe/fv1.cpp:122–136`). [10-21 대조 정정]
CPU DG2는 저속 조건에서 운동량을 남기고 마찰 계산을 반환한다(`swe/dg2/friction.cpp:81–94`). [10-21 대조 정정]
CUDA FV1·DG2는 저속 운동량을 0으로 만든다(`cuda/fv1/cuda_fv1_solver.cu:232–237`; `cuda/dg2/cuda_dg2_solver.cu:616–622`; [docx-manual:LV1-096·284 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)). [10-21 대조 정정] [10-21 전수 검증 보완]
내부 `SpeedThresh`의 현재 기본값은 `1e-6`이다(`lisflood.cpp:191`). [10-21 대조 정정]
`speedthresh` 입력 키워드는 v8.0·v8.1·v8.2·현재 파서에 없다([docx-manual:LV1-094 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md)). [10-21 대조 정정]

### 3.5 CFL 시간스텝 (`Tstep_from_cfl`, `fv1.cpp:583`)

$$
\Delta t=\text{cfl}\cdot\min_{i,j}\min\!\Big(\frac{\Delta x}{|U|+\sqrt{gH}},\frac{\Delta y}{|V|+\sqrt{gH}}\Big)
$$

(`fv1.cpp:606-611`), `DepthThresh` 초과 셀만. OpenMP `reduction(min:dt)`
(`:592`, MSVC 제외).

---

## 4. DG2 솔버 (`swe/dg2.cpp`)

DG2는 셀당 **평면 부분(planar)** 표현을 쓴다: 평균($H$)에 더해 x·y 슬로프
계수($H1x,H1y,HU1x,\dots$)를 둔다. 시간적분은 2단계 SSP Runge-Kutta(RK2).

### 4.1 시간 루프 (`dg2::solve`, `dg2.cpp:14`)

기동 시 DEM 슬로프($z_{1x},z_{1y}$)를 읽고(`dg2.cpp:27`) 경계 슬로프를 0으로
(`:28`). 루프(`dg2.cpp:57`)는:
1. 점원·경계값 갱신(`:64-65`).
2. CFL dt(`:69`), 마찰(`:74`).
3. **`rk_stage1`(`:75`) → `rk_stage2`(`:76`)** — SSP-RK2.

CPU DG2는 마찰 후 평균 운동량을 가우스점 마찰에 다시 사용한다(`swe/dg2/friction.cpp:18–67`). [10-21 대조 정정]
CUDA·dg2new와 다른 상태 시점의 결함 후보 강도는 강함이다([cpu-gpu-swe:LG1-045 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]
CPU DG2의 평균 건조 셀은 가우스점 마찰도 건너뛴다([cpu-gpu-swe:LG1-047 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]

### 4.2 SSP-RK2 (`rk_stage1/2`, `dg2.cpp:308, 352`)

각 stage가 동일 파이프라인을 돈다:
슬로프 리미터(`apply_slope_limiter`, `:321`; OFF면 perimeter만 0,`:325`) →
면 재구성 `update_{H,HU,HV}star`(`:327-329`) → 면 HLL `update_fluxes`(`:330`) →
공간연산자 `L`(`:339`) → 계수 갱신.

- stage1: $U^{(1)}=U^n+\Delta t\,L(U^n)$
  (`update_intermediate_coefficient`, `dg2.cpp:704-705`).
- stage2: $U^{n+1}=\tfrac12\big(U^n+U^{(1)}+\Delta t\,L(U^{(1)})\big)$
  (`update_final_coefficient`, `dg2.cpp:749-750`) — 표준 SSP-RK2(Heun).

각 stage 끝에서 `zero_discharge`(`:344, 1184`)로 마른 셀($H<$DepthThresh)
유량 계수 전부 0.

### 4.3 공간연산자 L = L0 + L1x + L1y (`dg2.cpp:787`)

#### L0 — 셀평균 증분 (`dg2.cpp:803`)
FV1과 동형: 면 HLL 플럭스 발산 + 하상 소스(`bed_source_0x/y`)
(`dg2.cpp:819, 826-827`).

#### L1x — x-슬로프 증분 (`dg2.cpp:838`)
DG2 약형식(weak form): 경계항(면 플럭스)에서 **체적적분(가우스 2점 구적)** 을
뺀다. 두 가우스점 값은 `gauss_lower/upper(mean, slope)`로 재구성
(`dg2.cpp:863-865, 874-876`), 각 점에서 해석적 물리플럭스 `physical_flux_x`
(`:871, 882`):

$$
L_{1x}=-\frac{\sqrt3}{\Delta x}\Big(F_w+F_e-F(G_1)-F(G_2)\Big)
$$

(`dg2.cpp:885`). $\sqrt3$ 계수는 Legendre 1차 기저의 정규화에서 나온다.
운동량 슬로프에는 `bed_source_1x`(`:888`)를 더한다. L1y는 y대칭(`dg2.cpp:893`).

### 4.4 DG2 well-balanced 하상 소스 (`dg2.cpp:948`)

평균항(`bed_source_0x`):
$S_0=2\sqrt3\,g\,H^\star_0\,z^\dagger_{1}/\Delta x$ (`dg2.cpp:961`).
슬로프항(`bed_source_1x`): $S_1=2g\,H^\star_1\,z^\dagger_{1}$ (`dg2.cpp:993`).
$z^\dagger_{1}$(`Zdagger1x`)는 보정 하상 슬로프 (외부 `dg2/modifiedvars.h`).

### 4.5 CFL (`dg2::Tstep_from_cfl`, `dg2.cpp:1069`)
FV1과 같은 파속 기반 식(`min_dt`,`:1156`)이되 **내부 셀 + 4 경계 배열**까지
순회(`dg2.cpp:1093-1151`).
`thin_depth`의 활성 식은 `return H <= C(10.0) * Solverptr->DepthThresh;`이다(`swe/dg2.cpp:1066`). [10-21 대조 정정]
이 함수는 단계별 CFL 호출 근거가 아니다([cpu-gpu-swe 수정안 LG1-045–053](../../../_staging/recovery/compare/lisflood-cpu-gpu-swe.md#4-노트-대조와-수정안)). [10-21 대조 정정]
CPU DG2의 y 최소 수심 검사는 `H1x`를 읽는 축 혼동 후보이다(`swe/dg2/slope_limiter.cpp:380–394`). [10-21 대조 정정]
이 결함 후보 강도는 강함이다([cpu-gpu-swe:LG1-050 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]
CUDA의 최소 수심 검사는 다른 스레드가 바꾸는 기울기를 읽을 수 있다(`cuda/dg2/cuda_dg2_solver.cu:802–824`; `cuda/dg2/cuda_dg2_slope_limit.cu:78–111`). [10-21 대조 정정]
이 결함 후보 강도는 중간이다([cpu-gpu-swe:LG1-051 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]

---

## 5. 경계 조건 (`swe/boundary.cpp`, `fv1.cpp:503`, `dg2.cpp:591`)

`boundary.cpp`는 경계 인덱싱과 시계열 보간만 담는다:
- `linear_interpolate`(`boundary.cpp:3`) — 시계열 선형보간, 범위 밖은 끝값 클램프
  (`:12, 27`).
- 경계 1D 인덱스: N=`i`(`:50`), E=`xsz+j`(`:40`), S/W는 둘레 역방향
  (`:60, 30`) — 도메인 둘레를 한 줄로 펼친 순환 인덱스.

BC 종류별 외부상태(ghost) 설정은 솔버별 `set_boundary_values`:

| ID | 의미 | 처리 (fv1.cpp / dg2.cpp) |
|---|---|---|
| `FREE1` | 자유 유출 | CPU FV1은 수심·법선 운동량을 복사한다(`swe/fv1.cpp:523–525`). 접선 식은 `HV_outside = HV_outside;`이다(`swe/fv1.cpp:526`). [10-21 대조 정정] |
| `HFIX2`/`HVAR3` | 고정/시변 수위 | $H_{out}=\max(0,\,\eta_{bc}-z)$ (`fv1.cpp:531`, `dg2.cpp:625`) |
| `QFIX4`/`QVAR5` | 고정/시변 유량 | $HU_{out}=\text{sign}\cdot q$, 미소 수심 보장 (`fv1.cpp:548-551`) |
| `NONE0`(기본) | 폐쇄/반사벽 | $HU_{out}=-HU_{in}$ (`fv1.cpp:577`, `dg2.cpp:658`). CPU FV1 접선 식은 `HV_outside = HV_outside;`이다(`swe/fv1.cpp:578`). [10-21 대조 정정] |

DG2의 경계는 셀 한쪽 면 재구성값(`limit_pos/neg`, `dg2.cpp:202-206`)을
ghost로 쓰며 결과를 `Arrptr->boundary.{H,HU,HV}`에 저장(`dg2.cpp:213-215`),
다음 CFL 산정에서 재사용한다(`dg2.cpp:1101`).

CPU FV1의 FREE·벽 경계는 접선 운동량 복사를 누락한 후보이다([cpu-gpu-swe:LG1-023 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]
이 결함 후보 강도는 강함이다([동일 근거 LG1-023](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]
CUDA 수위 경계는 `U_const.H = U_outside.H;`로 내부 수심도 바꾼다(`cuda/cuda_boundary.cu:400–403`). [10-21 대조 정정]
CUDA 유량 경계는 `U_outside.HV = C(0.0);`로 접선 운동량을 제거한다(`cuda/cuda_boundary.cu:355`). [10-21 대조 정정]
외곽 수위 경계와 별도로 CPU SWE·공통 CUDA의 HFIX·HVAR 점원은 최솟값을 취한다([callflow:RF-022 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md)). [10-21 대조 정정]
이 점원 처리는 하상 위의 양의 지정 수심을 0으로 만드는 강함의 결함 후보이다([동일 근거 RF-022](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md)). [10-21 대조 정정]

---

## 6. `swe/flux.cpp` — 해석적 물리 플럭스

DG2 체적적분에 쓰는 SWE 플럭스 함수의 좌표불변 구현.
`physical_flux`(`flux.cpp:31`):

$$
\mathbf{F}=\big(HU,\; HU^2/H+\tfrac12 gH^2,\; HUV\big),\quad H>\text{DepthThresh}
$$

(`flux.cpp:50-52`), 마른 셀은 0(`:42-46`). `physical_flux_y`는 인수 스왑으로
재사용(`flux.cpp:17-29`).

---

## 7. `swe/dg2new.cpp` — 비가동 DG2 리팩터 (참고)

`dg2new::DG2Solver`는 DG2와 유사한 공간 연산자를 쓰는 비활성 CPU 구현이다(`swe/dg2new.cpp:11,400–555`; `lisflood.cpp:794–796`). [10-21 대조 정정]
자료형은 `Increment`·`LocalFaceValue`·`FlowVector`이다(`swe/dg2new.h:6–32`). [10-21 대조 정정] [10-21 표본 정정]
구현 차이:

- **균일격자 CPU 전용**, 슬로프 리미터·점원 없음, BC `FIXME`
  (`dg2new.cpp:300, 350, 402`); 내부 셀만 순회(`:304, 354`) — 둘레 1셀 고정 0
  (`:38-74`).
- 공간연산자 `space_operator`(`dg2new.cpp:400`)가 4 면을 명시 계산
  → `wetting_drying`(`:661`)로 면별 $z^\star$ 보정($\eta-z_{LR}$, `:702-708`,
  Audusse 류 양수성 보존) → `HLL_x/y`.
- well-balanced 소스는 `dg2_operator`(`:503`)에 `SS0/SS1x/SS1y`로 내장
  ($-gH_0\cdot2\sqrt3\,z_{1x}/\Delta x$ 등, `:528, 541, 555`) — `dg2.cpp`의
  `bed_source_*`와 같은 식을 벡터로 표현.
- `local_face_value`(`:568`)가 **자유수면 $\eta=H+z$** 와 그 슬로프로 면값을
  재구성한다(`swe/dg2new.cpp:643–657`). [10-21 대조 정정]
  면 중심값은 `평균±sqrt(3)×기울기`이다([cpu-gpu-swe의 LG1-081–085 수정안](../../../_staging/recovery/compare/lisflood-cpu-gpu-swe.md#4-노트-대조와-수정안)). [10-21 대조 정정]
  가우스점 값은 `평균±기울기`이다([동일 수정안](../../../_staging/recovery/compare/lisflood-cpu-gpu-swe.md#4-노트-대조와-수정안)). [10-21 대조 정정]

현재 CMake 기본 목록은 dg2new를 컴파일하지 않는다(`CMakeLists.txt:26–65`). [10-21 대조 정정]
옛 makefile 목록은 `swe/dg2new.cpp`를 컴파일한다(`makefile:31`). [10-21 대조 정정]
main의 실행 호출은 `lisflood.cpp:794–796`에서 주석 처리되어 있다. [10-21 대조 정정]
비활성 dg2new의 y 질량 플럭스는 `HU,`를 쓰는 강함의 결함 후보이다([cpu-gpu-swe:LG1-081 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]
fixed 분기는 `if (Statesptr->adaptive_ts == OFF) return;`에서 최종 상태 복사 전에 반환한다(`swe/dg2new.cpp:769,789`). [10-21 대조 정정]
이 비활성 경로의 상태 반영 결함 후보 강도는 강함이다([cpu-gpu-swe:LG1-082 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md)). [10-21 대조 정정]
활성 적응 해법은 [MWDG2·HWFV1 노트](lisflood-fp-mwdg2-adaptive-mra.md)에 정리한다(`lisflood.cpp:447–450`). [10-21 대조 정정]

---

## 8. 입력·출력의 적용 범위

- CPU FV1·DG2의 Qx·Qy는 셀 중심 단위 폭 유량이다(`swe/output.cpp:132–141`; `swe/stats.cpp:131–140`). [10-21 대조 정정]
- DG2는 평균 격자 외에 x·y 기울기 파일을 읽고 쓴다(`swe/dg2.cpp:27–35,107–109`; `swe/dg2/dg2_output.cpp:13–24`). [10-21 대조 정정]
- 두 CPU 반복문은 최대 수심과 관측점 출력을 처리한다([files-output:LI2-332 최종 근거](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)). [10-21 대조 정정]
- 두 CPU 반복문은 고전 IterateQ의 overpass·profile·hazard·중간 checkpoint·gauge 출력 블록을 호출하지 않는다([동일 근거 LI2-332](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md)). [10-21 대조 정정]
- Metal FV1은 공유 SWE writer와 별도 단면 유량 writer를 사용한다([files-output의 LI2-318·331–342 수정안](../../../_staging/recovery/compare/lisflood-files-output-vs-code.md#4-노트-대조와-수정안)). [10-21 대조 정정]

## 요약

- CPU full-SWE 경로는 FV1과 DG2로 나뉜다(`lisflood.cpp:778–793`). [10-21 대조 정정]
- 두 CPU 해법은 HLL Riemann 플럭스를 사용한다(`swe/hll_include.h:77–84`). [10-21 대조 정정]
- 현재 FV1 분기는 8.3의 Metal 조건부 호출도 포함한다(`lisflood.cpp:780–788`). [10-21 대조 정정]
- DG2는 셀당 평균+x·y 슬로프, L=L0+L1x+L1y 약형식, 가우스 2점 구적으로 체적적분.
- `dg2new`(질문이 multiwavelet으로 지목)는 **실제로는 비가동 CPU DG2 리팩터**이며,
  MW 적응 격자는 `cuda/adaptive/mra/`에 존재(범위 밖). 이 점이 본 검수의 핵심 정정.

## 문서와 코드 차이 (10-21 대조)

문서 판: 2013 PDF 매뉴얼의 표지는 Code release 6.1.1·2013-11-25이다(user manual.pdf p.1). user manual.docx의 표지 수정 표시는 Code release 8.0.0·2020-07-20이다(p.1, LibreOffice 변환본). 이 DOCX의 판 이력 맨 위는 8.0이다(p.5, 같은 변환본). user manual +bridge.docx의 표지는 Code release 4.3.6·2008-04-25이다(p.1, LibreOffice 변환본). 코드 판은 Zenodo 8.2(10.5281/zenodo.13121102)에 공식 8.3 패치를 적용한 판이다(`../LISFLOOD-FP-8.3-package/README.md:19–24`). `VersionHistory.h:16–18`의 숫자 판은 8.1.0이다. 릴리스 이름은 8.3이다(`VersionHistory.h:23`). [10-21 전수 검증 정정]

코드 인용의 기준 디렉터리는 [LISFLOOD-FP 원자료](../raw/source_code/LISFLOOD-FP/)이다. `v8.0:`·`v8.1:`·`v8.2:`는 이전 배포본을 가리킨다. `bf804e23:`는 반영 전 노트의 커밋과 줄을 가리킨다.

최종 분류와 결론 문장은 [최종 결론 배정](../../../_staging/recovery/assign/LISFLOOD-FP-final-conclusions.tsv)에 지정된 같은 행 ID의 근거를 따른다. 분류는 A 판 차이, B 문서 오기, C 문서 누락, D 문서에만 있음, E 코드 결함 후보, F 표기 차이이다.

행별 최종 근거: [LB1b](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md), [LN1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LN1.md), [RF](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md), [LG1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md), [LV1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md), [LI2](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md), [LI1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md).

cpu-gpu 행은 CPU·CUDA·Metal 구현을 비교한다. 해당 행의 문서 원문 칸에는 CPU 또는 비교 대상 구현의 원문을 둔다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| bridge-docx:LB1-298 | bridge판에 없는 `fv1` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `fv1` | `pars.cpp:582` `if (read_empty_param(param_name, line_number, param_value_ptr, "fv1", verbose, mode))` / `pars.cpp:584` `Statesptr->fv1 = ON;` / `pars.cpp:585` `Solverptr->cfl = C(0.5);` / `pars.cpp:586` `Solverptr->DepthThresh = C(1e-3);`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:582` `if (read_empty_param(param_name, line_number, param_value_ptr, "fv1", verbose, mode))` / `pars.cpp:584` `Statesptr->fv1 = ON;` / `pars.cpp:585` `Solverptr->cfl = C(0.5);` / `pars.cpp:586` `Solverptr->DepthThresh = C(1e-3);` | C 문서 누락 | 논리 키워드를 읽는다. 솔버 선택 때 CFL·DepthThresh를 다시 대입한다. |
| bridge-docx:LB1-303 | bridge판에 없는 `dg2` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `dg2` | `pars.cpp:630` `else if (read_empty_param(param_name, line_number, param_value_ptr, "dg2", verbose, mode))` / `pars.cpp:632` `Statesptr->dg2 = ON;` / `pars.cpp:633` `Solverptr->cfl = C(0.33);` / `pars.cpp:634` `Solverptr->DepthThresh = C(1e-3);` / `pars.cpp:635` `Solverptr->DG2DepthThresh = C(-1.0);`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:630` `else if (read_empty_param(param_name, line_number, param_value_ptr, "dg2", verbose, mode))` / `pars.cpp:632` `Statesptr->dg2 = ON;` / `pars.cpp:633` `Solverptr->cfl = C(0.33);` / `pars.cpp:634` `Solverptr->DepthThresh = C(1e-3);` / `pars.cpp:635` `Solverptr->DG2DepthThresh = C(-1.0);` | C 문서 누락 | 논리 키워드를 읽는다. 솔버 선택 때 CFL·DepthThresh를 다시 대입한다. |
| bridge-docx:LB1-311 | bridge판에 없는 `dg2depththresh` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `dg2depththresh` | `pars.cpp:708` `if (read_numeric_param(param_name, line_number, param_value_ptr, "dg2depththresh", &Solverptr->DG2DepthThresh, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:708` `if (read_numeric_param(param_name, line_number, param_value_ptr, "dg2depththresh", &Solverptr->DG2DepthThresh, verbose, mode))`; `pars.cpp:710–714` `if (Statesptr->dg2 == OFF)`이면 `exit(1);` | C 문서 누락 | 실수 입력을 읽는다. 읽기 대상은 `Solverptr->DG2DepthThresh`이다. 먼저 선택한 솔버 상태를 검사한다. |
| bridge-docx:LB1-312 | bridge판에 없는 `dg2thindepth_tstep` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `dg2thindepth_tstep` | `pars.cpp:718` `if (read_numeric_param(param_name, line_number, param_value_ptr, "dg2thindepth_tstep", &Solverptr->DG2ThinDepthTstep, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:718` `if (read_numeric_param(param_name, line_number, param_value_ptr, "dg2thindepth_tstep", &Solverptr->DG2ThinDepthTstep, verbose, mode))`; `pars.cpp:720–724` `if (Statesptr->dg2 == OFF)`이면 `exit(1);` | C 문서 누락 | 실수 입력을 읽는다. 읽기 대상은 `Solverptr->DG2ThinDepthTstep`이다. 먼저 선택한 솔버 상태를 검사한다. |
| bridge-docx:LB1-348 | bridge판에 없는 `limitslopes` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `limitslopes` | `pars.cpp:973` `if (read_empty_param(param_name, line_number, param_value_ptr, "limitslopes", verbose, mode))` / `pars.cpp:980` `Parptr->limit_slopes = ON;`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:973` `if (read_empty_param(param_name, line_number, param_value_ptr, "limitslopes", verbose, mode))` / `pars.cpp:980` `Parptr->limit_slopes = ON;`; `pars.cpp:975–978`의 `if (Statesptr->dg2 == OFF && Statesptr->mwdg2 == OFF && Statesptr->fv2 == OFF)` | C 문서 누락 | 논리 키워드를 읽는다. 먼저 선택한 솔버 상태를 검사한다. |
| bridge-docx:LB1-349 | bridge판에 없는 `krivodonovathresh` | user manual +bridge.docx p.21–24(변환본) 표 5·user manual +bridge.docx p.35(변환본) 표 7<br>bridge판에 없는 `krivodonovathresh` | `pars.cpp:984` `if (read_numeric_param(param_name, line_number, param_value_ptr, "krivodonovathresh", &Solverptr->krivodonova_threshold, verbose, mode))`<br>확인한 원문: user manual +bridge.docx p.21–24(변환본) 표 5·p.35 표 7; `pars.cpp:984` `if (read_numeric_param(param_name, line_number, param_value_ptr, "krivodonovathresh", &Solverptr->krivodonova_threshold, verbose, mode))` | C 문서 누락 | 실수 입력을 읽는다. 읽기 대상은 `Solverptr->krivodonova_threshold`이다. |
| bridge-docx:LB1-403 | SWE 분기와 Metal | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:7` `verification_method: "swe/{fv1,dg2,dg2new,hll,flux,fields,boundary}.cpp + hll_include.h + dg2new.h 전수 Read, dispatch는 lisflood.cpp:775-792 직접 확인 (2026-06-18)"` | `lisflood.cpp:778–793`의 FV1·DG2 분기와 Metal 조건은 LB1-380에 있다.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:7`; `lisflood.cpp:778–793`; `../LISFLOOD-FP-8.3-package/README.md:35` | C 문서 누락 | CPU SWE 해법의 구분은 유지한다. 현재 FV1 분기에는 Metal 선택이 추가되었다. 옛 bridge판의 관성 없는 Manning 홍수터 식을 FV1·DG2의 식으로 사용하지 않는다. 행 번호와 8.3 분기만 갱신한다. |
| build-83:LN1-238 | dg2new 빌드·호출 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:291` ``**이 코드는 `lisflood.cpp:784`에서 주석 처리되어 빌드/실행에 포함되지 않는다.**`` | `v8.2:makefile:31`과 현재 `makefile:31`은 `swe/dg2new.cpp \`를 적는다. CMake 목록에는 이 파일이 없다. 현재 `lisflood.cpp:794–796`은 호출을 주석 처리한다.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:291`; `makefile:31`; `CMakeLists.txt:26–65`; `lisflood.cpp:794–796`; `v8.2:makefile:31`; `v8.2:lisflood.cpp:784–786` | B 문서 오기 | dg2new는 CMake 기본 목록에서 제외되지만 옛 make 목록에는 포함된다. 런타임 호출은 주석이다. [10-21 전수 검증 정정] |
| build-83:LN1-239 | FV1 Metal 분기 | `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:26–27` ``디스패치는 `lisflood.cpp:775` (`Statesptr->fv1 == ON`) / `:780` (`Statesptr->dg2 == ON`)에서 분기한다.`` | `v8.2:lisflood.cpp:775–782`의 CPU 호출·현재 `lisflood.cpp:778–793`의 METAL_ENABLED 조건과 CPU 호출·`../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:282–295`<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/source-analysis/lisflood-fp-swe-fv1-dg2.md:26–27`; `v8.2:lisflood.cpp:775–783`; `lisflood.cpp:778–793`; `../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:282–295` | A 판 차이 | 8.3 FV1 분기에는 Metal 조건부 호출을 함께 적는다. `#ifdef METAL_ENABLED` 안의 `if (Statesptr->cuda == ON && metal_is_available())`가 Metal 호출 조건이다. |
| callflow:RF-022 | SWE HFIX·HVAR 점원 수심 | user manual.docx p.30(변환본) 쪽 이미지 | `swe/fv1.cpp:207` `NUMERIC_TYPE H_new = FMIN(C(0.0), BCptr->PS_Val[ps_i] - Z);`; `cuda/cuda_boundary.cu:115–116`도 FMIN이다. 같은 FV1 외곽의 531행은 FMAX다. `lisflood.h:80,91`은 FMIN을 fmin·fminf로 정의한다. 반대 근거와 다른 경로 대조는 §8.1.<br>확인한 원문: user manual.docx p.30(변환본) 쪽 이미지; `swe/fv1.cpp:195–224,528–545`; `swe/dg2.cpp:140–157`; `cuda/cuda_boundary.cu:105–123,190–205`; `lisflood.h:75–96`; `iterateq.cpp:559–571`; `v8.0:swe/fv1.cpp:207`; `v8.1:swe/fv1.cpp:207` | E 코드 결함 후보(강함) | CPU SWE·공통 CUDA의 HFIX·HVAR 점원 처리는 E 코드 결함 후보이며 강도는 강함이다. CPU FV1의 HFIX 식은 `NUMERIC_TYPE H_new = FMIN(C(0.0), BCptr->PS_Val[ps_i] - Z);`이다. CPU FV1의 HVAR 식은 `NUMERIC_TYPE H_new = FMIN(C(0.0), linear_interpolate(BCptr->PS_TimeSeries[ps_i], Solverptr->t) - Z);`이다. CUDA 공통 식은 `NUMERIC_TYPE H_new = FMIN(C(0.0), cuda::boundaries.PS_value[i] - Z);`이다. CPU DG2는 같은 방향의 `min`을 사용한다. 이 처리는 하상 위에 지정한 양의 수심을 0으로 만든다. 같은 판의 외곽 경계와 ACC 점원은 양의 지정 수심을 허용한다. |
| cpu-gpu-swe:LG1-012 | CPU FV1 바닥항의 상태 시점 | CPU: `swe/fv1.cpp:441-442`에서 H를 먼저 바꾼다. `:450-452`의 Q4가 `bed_source_x`를 부른다. `swe/fv1/modifiedvars.cpp:329` `NUMERIC_TYPE H = Arrptr->H[j*Parptr->xsz + i];` | CUDA: `cuda/fv1/cuda_fv1_solver.cu:372` `NUMERIC_TYPE ETA = U_neg.H + Z_neg;`; `:467` `NUMERIC_TYPE ETA = U_pos.H + Z_pos;`<br>Metal: `metal/fv1/metal_fv1_kernels.metal:501` `float ETA = U_c.H + Z_c;`; `:611`도 같은 행이다.<br>확인한 원문: `swe/fv1.cpp:441–452·476–482`; `swe/fv1/modifiedvars.cpp:314–331`; `cuda/fv1/cuda_fv1_solver.cu:372–376·467–472`; `metal/fv1/metal_fv1_kernels.metal:501–503·611–613` | E 코드 결함 후보(중간) | CPU FV1의 바닥항은 갱신 전 Hstar와 갱신 후 수심에서 얻은 Zdagger를 함께 사용한다. 부분 건조 조건의 결함 후보이다. 결함 후보의 강도는 중간이다. |
| cpu-gpu-swe:LG1-023 | CPU FREE·벽 접선 | CPU: `swe/fv1.cpp:526`과 `:578` `HV_outside = HV_outside;` | CUDA: `cuda/cuda_boundary.cu:342` `FlowVector U_outside = { U_const.H, U_const.HU, U_const.HV };`<br>Metal: `metal/fv1/metal_fv1_kernels.metal:81`과 `:85` `out.Qt = in.Qt;`<br>확인한 원문: `swe/fv1.cpp:327–334·523–526·531–534·574–579`; `cuda/cuda_boundary.cu:342–365`; `metal/fv1/metal_fv1_kernels.metal:78–85` | E 코드 결함 후보(강함) | CPU FV1의 FREE·벽 경계는 접선 운동량 복사를 누락한 후보이다. 결함 후보의 강도는 강함이다. |
| cpu-gpu-swe:LG1-029 | CPU 배수 통계의 공유 갱신 | CPU: `swe/fv1.cpp:167` `#pragma omp parallel for`; `:180-181` `accumulate_point_flux_stats(BCptr,` / `-Hold*Parptr->dA/Solverptr->Tstep);`; `swe/stats.cpp:58` `BCptr->Qin += Q;`; `:62` `BCptr->Qout -= Q;` | CUDA: `cuda/cuda_boundary.cu:88` `atomicAdd(&(mass_stats->in), discharge);`; `:92` `atomicAdd(&(mass_stats->out), -discharge);`<br>Metal: `metal/fv1/metal_fv1_kernels.metal:912`은 atomic_add_float를 쓴다.<br>확인한 원문: `swe/fv1.cpp:165–181`; `swe/stats.cpp:48–62·74–83`; `cuda/cuda_boundary.cu:86–92`; `metal/fv1/metal_fv1_kernels.metal:912` | E 코드 결함 후보(강함) | OpenMP CPU FV1 배수는 공유 유입·유출 계수를 동시 갱신할 수 있다. 결함 후보의 강도는 강함이다. |
| cpu-gpu-swe:LG1-043 | DG2 바닥항 부호·계수 | CPU: `swe/dg2.cpp:961` `return C(2.0)*SQRT(C(3.0)) * Solverptr->g * Hstar * Zdagger / Parptr->dx;`; `:993` `return C(2.0) * Solverptr->g * Hstar * Zdagger;` | CUDA: `cuda/dg2/cuda_dg2_solver.cu:165-166`의 Q10<br>확인한 원문: `swe/dg2.cpp:826–835·885–888·958–993`; `swe/dg2/modifiedvars.cpp:401–428`; `cuda/dg2/cuda_dg2_solver.cu:153–166·278–282` | F 표기 차이 | DG2 바닥항은 연산자 바깥 계수를 포함하면 같은 식이다. |
| cpu-gpu-swe:LG1-044 | DG2 방향별 RK2 | CPU: `swe/dg2.cpp:704-705`, `:749-750`의 Q11 | CUDA: `cuda/dg2/cuda_dg2_solver.cu:391-438`의 Q11<br>확인한 원문: `swe/dg2.cpp:704–705·749–750`; `cuda/dg2/cuda_dg2_solver.cu:391–438` | F 표기 차이 | CUDA의 방향별 커널 누적은 CPU와 같은 RK2이다. |
| cpu-gpu-swe:LG1-045 | CPU DG2 가우스점 마찰 상태 | CPU: `swe/dg2/friction.cpp:27` `friction(Solverptr, H, HU, HV, n);` 다음에 `:33-40`의 Q12를 읽는다. | CUDA: `cuda/dg2/cuda_dg2_solver.cu:651` `FlowCoeffs U(Uref);`; `:653-667`에서 가우스점을 먼저 만들고 `:673` `friction(n, U.H, Uref.HU, Uref.HV);`를 부른다.<br>확인한 원문: `swe/dg2/friction.cpp:18–67`; `cuda/dg2/cuda_dg2_solver.cu:650–683`; `swe/dg2new.cpp:238–253` | E 코드 결함 후보(강함) | CPU DG2는 마찰 후 평균 운동량을 가우스점 마찰에 다시 사용한다. CUDA·dg2new와 다른 상태 시점이다. 결함 후보의 강도는 강함이다. |
| cpu-gpu-swe:LG1-046 | DG2 저속 운동량 | CPU: `swe/dg2/friction.cpp:91-94`의 Q12는 운동량을 유지한다. | CUDA: `cuda/dg2/cuda_dg2_solver.cu:616-622`의 Q12는 HU·HV를 0으로 만든다.<br>확인한 원문: `swe/dg2/friction.cpp:81–103`; `swe/fv1.cpp:130–135`; `cuda/dg2/cuda_dg2_solver.cu:616–622`; `metal/fv1/metal_fv1_kernels.metal:319–323`; user manual.docx p.24(변환본) | E 코드 결함 후보(약함) | 저속 DG2의 운동량은 CPU가 유지하고 CUDA가 제거한다. 결함 후보의 강도는 약함이다. |
| cpu-gpu-swe:LG1-047 | 건조 평균 셀의 마찰 | CPU: `swe/dg2/friction.cpp:25` `if (H <= Solverptr->DepthThresh) continue;` | CUDA: `cuda/dg2/cuda_dg2_solver.cu:673-683`은 평균과 네 가우스점에 friction을 적용한다.<br>확인한 원문: `swe/dg2/friction.cpp:25–27·59–67·81–85`; `cuda/dg2/cuda_dg2_solver.cu:606–610·650–683`; `swe/dg2new.cpp:238–246` | E 코드 결함 후보(약함) | CPU DG2의 평균 건조 셀은 가우스점 마찰도 건너뛴다. CUDA는 각 점 수심으로 판단한다. 결함 후보의 강도는 약함이다. |
| cpu-gpu-swe:LG1-049 | DG2 limiter norm 문턱 | CPU: `swe/dg2/slope_limiter.cpp:314` `if (FABS(norm) > C(1e-12))` | CUDA: `cuda/dg2/cuda_dg2_slope_limit.cu:30` `if (FABS(norm) > C(1e-6))`<br>확인한 원문: `swe/dg2/slope_limiter.cpp:298–331`; `cuda/dg2/cuda_dg2_slope_limit.cu:15–47`; `v8.0:cuda/dg2/cuda_dg2_slope_limit.cu:30`; `v8.1:cuda/dg2/cuda_dg2_slope_limit.cu:30`; `v8.2:cuda/dg2/cuda_dg2_slope_limit.cu:30`; user manual.docx p.24(변환본) | C 문서 누락 | CPU DG2의 norm 조건은 `if (FABS(norm) > C(1e-12))`이다. CUDA DG2의 조건은 v8.1부터 `if (FABS(norm) > C(1e-6))`이다. 문서는 이 내부 보호 문턱의 차이를 설명하지 않는다. |
| cpu-gpu-swe:LG1-050 | CPU y 최소 수심의 잘못된 축 | CPU: `swe/dg2/slope_limiter.cpp:381` `NUMERIC_TYPE backward_H1x = U.H1x[(j + 1) * Parptr->xsz + i];`; `:383`, `:385`도 H1x이다. | CUDA: `cuda/dg2/cuda_dg2_slope_limit.cu:101` `NUMERIC_TYPE backward1y = flow.H1y[(j+1)*cuda::pitch + i];`; `:103`, `:105`도 H1y이다.<br>확인한 원문: `swe/dg2/slope_limiter.cpp:215–223·380–394`; `cuda/dg2/cuda_dg2_slope_limit.cu:100–111` | E 코드 결함 후보(강함) | CPU DG2의 y 최소 수심 검사가 x 기울기를 쓰는 축 혼동 후보이다. 결함 후보의 강도는 강함이다. |
| cpu-gpu-swe:LG1-051 | CUDA limiter의 동시 읽기·쓰기 | CPU: CPU는 `swe/dg2/slope_limiter.cpp:121-126`에서 scratch에 결과를 쓴다. `:171-172`에서 별도 루프로 H1x에 반영한다. | CUDA: `cuda/dg2/cuda_dg2_solver.cu:810-812`의 Q14. `cuda/dg2/cuda_dg2_slope_limit.cu:79`은 이웃 `flow.H1x`를 읽는다.<br>확인한 원문: `cuda/dg2/cuda_dg2_solver.cu:802–824·921–926`; `cuda/dg2/cuda_dg2_slope_limit.cu:78–89·100–111`; `swe/dg2/slope_limiter.cpp:121–126·164–172` | E 코드 결함 후보(중간) | CUDA DG2 limiter의 최소 수심 검사는 다른 스레드가 바꾸는 기울기를 읽을 수 있다. 결함 후보의 강도는 중간이다. |
| cpu-gpu-swe:LG1-052 | limiter ON의 둘레 처리 | CPU: `swe/dg2/slope_limiter.cpp:109`은 모든 j의 x 내부 셀을 제한한다. `:211-213`은 y 내부 행의 모든 i를 제한한다. | CUDA: `cuda/dg2/cuda_dg2_solver.cu:926` `zero_perimeter_slopes(DEM, Uold);`; `:734-739`는 북쪽 둘레의 두 방향 기울기를 모두 0으로 만든다.<br>확인한 원문: `swe/dg2.cpp:319–326·363–370`; `swe/dg2/slope_limiter.cpp:107–126·211–223`; `cuda/dg2/cuda_dg2_solver.cu:729–739·915–937` | C 문서 누락 | CUDA DG2는 limiter 사용 여부와 관계없이 둘레의 두 방향 기울기를 제거한다. |
| cpu-gpu-swe:LG1-053 | limiter maxH의 시점·범위 | CPU: `swe/dg2.cpp:62` `if (Parptr->limit_slopes == ON) Solverptr->maxH = maxH(Parptr, Arrptr);`는 강우·점 원천보다 앞선다. | CUDA: `cuda/dg2/cuda_dg2_solver.cu:917` `maxH.update(Uold);`는 강우·점 원천 뒤이다. `cuda/dg2/cuda_dg2_slope_limit.cu:299-300`은 ghost 포함 elements를 reduction한다.<br>확인한 원문: `swe/dg2.cpp:62–64·1023–1031`; `cuda/dg2/cuda_dg2_simulate.cu:140–169`; `cuda/dg2/cuda_dg2_solver.cu:915–920`; `cuda/dg2/cuda_dg2_slope_limit.cu:15·282·299–300`; `cuda/ghostraster.cpp:4–6` | C 문서 누락 | DG2의 0.30×maxH 분기는 CPU·CUDA에서 다른 기준 상태를 사용할 수 있다. |
| cpu-gpu-swe:LG1-057 | FREE 건조 기울기 제거 | CPU: `swe/dg2.cpp:618-621`의 Q14는 H_const와 H_outside만 0으로 만든다. | CUDA: `cuda/dg2/cuda_dg2_solver.cu:518-523`의 Q14는 H1x·H1y도 0으로 만든다.<br>확인한 원문: `swe/dg2.cpp:610–621`; `cuda/dg2/cuda_dg2_solver.cu:512–523` | C 문서 누락 | CUDA DG2는 FREE 건조 경계에서 수심 기울기도 제거한다. |
| cpu-gpu-swe:LG1-059 | CPU DG2 배수 미호출 | CPU: `swe/dg2.cpp:74-85`에는 배수 호출이 없다. | CUDA: `cuda/dg2/cuda_dg2_simulate.cu:170-174`의 Q14는 drain_nodata를 적용한다.<br>확인한 원문: `pars.cpp:1012–1016`; `swe/dg2.cpp:57–111`; `swe/fv1.cpp:50·165–181`; `cuda/dg2/cuda_dg2_simulate.cu:170–174`; user manual.docx p.22(변환본) | E 코드 결함 후보(중간) | drain_nodata는 CPU FV1과 GPU SWE에서 실행되지만 CPU DG2 루프에는 적용되지 않는다. 결함 후보의 강도는 중간이다. |
| cpu-gpu-swe:LG1-080 | dg2new 수정 지형식 | — | `swe/dg2new.cpp:643` `H + SQRT(C(3.0))*H1_hat,`; `:690` `DEM_LR = FMAX(DEM_L, DEM_R);`; `:702` `star_left.H = FMAX(C(0.0), left.ETA - DEM_LR);`; `:710-713`의 Q15<br>`swe/dg2/modifiedvars.cpp:443` `return Zstar - getmax(C(0.0), -(ETA - Zstar));`; 공간 연산자는 LG1-042·043이다.<br>확인한 원문: `swe/dg2new.cpp:410–461·690–713`; `swe/dg2/modifiedvars.cpp:441–443`; `lisflood.cpp:794–796` | F 표기 차이 | dg2new의 방향별 수정 지형은 현재 셀을 기준으로 한 Zdagger의 다른 표현이다. |
| cpu-gpu-swe:LG1-081 | dg2new y 질량 플럭스 | — | `swe/dg2new.cpp:747-752`의 Q15<br>`swe/flux.cpp:28` `physical_flux(Solverptr, H, HV, HU, H_flux, HV_flux, HU_flux);`; `cuda/cuda_flow.cu:37` `return { HV, HU*HV/H, HV*HV/H + C(0.5)*cuda::physical_params.g*H*H };`<br>확인한 원문: `swe/dg2new.cpp:738–756`; `swe/flux.cpp:17–28·50–52`; `cuda/cuda_flow.cu:29–37`; `lisflood.cpp:790–796` | E 코드 결함 후보(강함) | 비활성 dg2new의 flux_y는 y 질량 플럭스에 `HU,`를 쓰는 결함 후보이다. 현재 실행 경로에서 호출되지 않음은 `lisflood.cpp:794–796`의 주석 처리로 확인된다. 결함 후보의 강도는 강함이다. |
| cpu-gpu-swe:LG1-082 | dg2new fixed 상태 반영 | — | `swe/dg2new.cpp:769` `if (Statesptr->adaptive_ts == OFF) return;`; 실제 배열 복사는 `:789` `Arrptr->H[j*Parptr->xsz+i] = H_new[j*Parptr->xsz+i];`부터 시작한다.<br>CPU `swe/dg2.cpp:749-750`은 매번 최종 상태를 쓴다. CUDA `cuda/dg2/cuda_dg2_solver.cu:938-940`도 매번 최종 상태를 쓴다.<br>확인한 원문: `swe/dg2new.cpp:101–109·760–799`; `swe/dg2.cpp:749–750`; `cuda/dg2/cuda_dg2_solver.cu:938–940`; `lisflood.cpp:794–796` | E 코드 결함 후보(강함) | 비활성 dg2new의 fixed 분기는 최종 수심·운동량·기울기를 다음 상태로 복사하지 않는다. 조건문은 `if (Statesptr->adaptive_ts == OFF) return;`이다. 현재 실행 경로에서 호출되지 않음은 `lisflood.cpp:794–796`의 주석 처리로 확인된다. 결함 후보의 강도는 강함이다. |
| cpu-gpu-swe:LG1-083 | dg2new 미완성 경계 | — | `swe/dg2new.cpp:42` `Arrptr->DEM[j*Parptr->xsz+i] = C(0.0);`; `:45` `Arrptr->H[j*Parptr->xsz+i] = C(0.0);`; `:300` `// FIXME: BC treatment`; `:304-306`은 내부 셀만 순회한다.<br>`swe/dg2.cpp:217-220`은 지정 경계를 구성한다. CUDA는 `cuda/dg2/cuda_dg2_solver.cu:515-516`에서 Boundary::outside_x를 부른다.<br>확인한 원문: `swe/dg2new.cpp:38–53·300–308·350–351`; `swe/dg2.cpp:610–629`; `cuda/dg2/cuda_dg2_solver.cu:512–523`; `lisflood.cpp:794–796` | C 문서 누락 | dg2new는 경계 셀의 지형과 수심을 0으로 설정한다. RK 갱신은 둘레를 제외한다. 코드의 `// FIXME: BC treatment`는 경계 처리가 미완성임을 명시한다. 현재 실행 경로는 이 구현을 호출하지 않는다. |
| cpu-gpu-swe:LG1-084 | dg2new의 빠진 주변 처리 | — | `swe/dg2new.cpp:101-109`은 `apply_friction();`, `rk_stage1();`, `rk_stage2();`, `update_Tstep();`, `update_mass_stats();`, `write_solution();`를 호출한다.<br>`swe/dg2.cpp:60-79`에는 강우·점 원천·경계·선택적 limiter·최대 수심·경계 질량 집계가 있다.<br>확인한 원문: `swe/dg2new.cpp:90–110`; `swe/dg2.cpp:60–79`; `lisflood.cpp:794–796` | C 문서 누락 | 비활성 dg2new에는 실제 DG2 solve의 원천항·limiter·질량 주변 처리가 연결되지 않는다. |
| cpu-gpu-swe:LG1-085 | dg2new 첫 dt·건조 등호 | — | `swe/dg2new.cpp:178` `Solverptr->Tstep = 1e-5;`; `:338` `if (Arrptr->H_int[j*Parptr->xsz+i] <= Solverptr->DepthThresh)`<br>`swe/dg2.cpp:43` `Solverptr->Tstep = 1e-6;`; `:1201`의 `<` 분기<br>확인한 원문: `swe/dg2new.cpp:174–184·338–346·801–809`; `swe/dg2.cpp:41–48·1201–1208`; `lisflood.cpp:794–796` | C 문서 누락 | 비활성 dg2new의 adaptive 첫 간격은 `Solverptr->Tstep = 1e-5;`이다. 활성 CPU DG2의 대응 값은 `Solverptr->Tstep = 1e-6;`이다. dg2new는 임계값과 같은 수심의 운동량도 제거한다. |
| cpu-gpu-swe:LG1-086 | dg2new 면 속도의 문턱 | — | `swe/dg2new.cpp:676` `if (left.H > Solverptr->DepthThresh)`<br>`swe/dg2/modifiedvars.cpp:234` `if (H >= Solverptr->DepthThresh)`; CUDA도 `cuda/cuda_flow.cu:56`에서 `>=`를 쓴다.<br>확인한 원문: `swe/dg2new.cpp:674–708`; `swe/dg2/modifiedvars.cpp:234–241`; `cuda/cuda_flow.cu:56–62`; `lisflood.cpp:794–796` | C 문서 누락 | 비활성 dg2new와 기본 DG2는 임계값과 같은 면 수심에서 다르게 운동량을 재구성한다. |
| cpu-gpu-swe:LG1-150 | CPU 계수 생성·downscale | — | `swe/dg2/fields.cpp:47-49`의 Q20; `:77-80`의 Q20<br>확인한 원문: `swe/dg2/fields.cpp:33–49·55–80` | C 문서 누락 | CPU DG2의 계수 생성은 네 꼭짓점 값에서 평균·기울기를 만든다. `dg2::downscale`은 DG2 계수를 2×2 자식 중심 값으로 평가한다. 전후처리의 계수 변환을 GPU 런타임 솔버 동등성의 조건으로 삼지 않는다. |
| docx-manual:LV1-067 | user manual.docx p.22(변환본) <u>`drain_nodata`</u>, `Default: off`. `nodata_elevation`과 함께 NODATA 셀의 물을 제거한다. | user manual.docx p.22(변환본) 표 8; user manual.pdf p.17–18<br>user manual.docx p.22(변환본) <u>`drain_nodata`</u>, `Default: off`. `nodata_elevation`과 함께 NODATA 셀의 물을 제거한다.<br>user manual.pdf p.17–18에 없다. | `pars.cpp:1012–1015`: `if (read_empty_param(param_name, line_number, param_value_ptr, "drain_nodata", verbose, mode))`<br>`{`<br>`Parptr->drain_nodata = ON;`<br>`if (verbose == ON) printf("Water will be removed from DEM NODATA cells\n");`; `lisflood.cpp:151` `Params.drain_nodata = OFF;`<br>확인한 원문: user manual.docx p.22(변환본) 표 8; user manual.pdf p.17–18; `pars.cpp:1012–1015`; `lisflood.cpp:151`; `swe/fv1.cpp:50·165–175`; `swe/dg2.cpp:57–111`; `iterateq.cpp:147–149` | C 문서 누락 | drain_nodata는 기본 OFF이다. CPU FV1은 `if (Parptr->drain_nodata == OFF) return;` 이후 NODATA 표고 셀을 배수한다. CPU DG2 시간 루프에는 이 배수 호출이 없다. 문서에는 해법별 적용 조건이 빠졌다. |
| docx-manual:LV1-081 | user manual.docx p.23(변환본) `depththresh value`, 기본 0.001 m. <u>`FV1: ` `10^{-6}`</u>. | user manual.docx p.23(변환본) 표 10; user manual.pdf p.19 표 10<br>user manual.docx p.23(변환본) `depththresh value`, 기본 0.001 m. <u>`FV1: ` `10^{-6}`</u>.<br>user manual.pdf p.19는 0.001만 적는다. | `pars.cpp:679` `if (read_numeric_param(param_name, line_number, param_value_ptr, "depththresh", &Solverptr->DepthThresh, verbose, mode))`; `pars.cpp:586` `Solverptr->DepthThresh = C(1e-3);`; `v8.0:pars.cpp:575` `Solverptr->DepthThresh = C(1e-6);`<br>확인한 원문: user manual.docx p.23(변환본) 표 10; user manual.pdf p.19 표 10; `pars.cpp:586·679`; `v8.0:pars.cpp:575`; `v8.1:pars.cpp:586` | A 판 차이 | DOCX의 FV1 수심 임계값 10⁻⁶ m는 v8.0 코드와 같다. v8.1과 현재 코드는 FV1 기본값을 10⁻³ m로 설정한다. |
| docx-manual:LV1-094 | user manual.docx p.24(변환본) <u>`speedthresh value`</u>. 마찰을 적용할 속도 임계값을 바꾸는 키워드. | user manual.docx p.24(변환본) 표 10; user manual.pdf p.20 표 10<br>user manual.docx p.24(변환본) <u>`speedthresh value`</u>. 마찰을 적용할 속도 임계값을 바꾸는 키워드.<br>user manual.pdf p.20에 없다. | 현행·v8.0·v8.1 전체의 `rg -i '"speedthresh"'` 결과는 모두 0건이다. 필드 `SpeedThresh`는 `lisflood.cpp:191`에 존재한다.<br>확인한 원문: user manual.docx p.24(변환본) 표 10; user manual.pdf p.20 표 10; `lisflood.cpp:191`; `lisflood.h:755`; 네 소스 트리 rg -i | D 문서에만 있음 | speedthresh 입력 키워드는 v8.0·v8.1·v8.2·현재 파서에 없다. 내부 SpeedThresh 필드의 존재는 입력 키워드 지원을 뜻하지 않는다. 내부 기본값의 판 차이는 LV1-095에서 구분한다. |
| docx-manual:LV1-095 | user manual.docx p.24(변환본) `speedthresh`의 <u>`Default: ` `10^{-9}`</u>. | user manual.docx p.24(변환본) 표 10; user manual.pdf p.20 표 10<br>user manual.docx p.24(변환본) `speedthresh`의 <u>`Default: ` `10^{-9}`</u>.<br>user manual.pdf p.20에 없다. | `v8.0:lisflood.cpp:184` `ParSolver.SpeedThresh = C(1e-9);`; `v8.1:lisflood.cpp:187` `ParSolver.SpeedThresh = C(1e-6);`; 현행 `lisflood.cpp:191` `ParSolver.SpeedThresh = C(1e-6);`<br>확인한 원문: user manual.docx p.24(변환본) 표 10; user manual.pdf p.20 표 10; `v8.0:lisflood.cpp:184`; `v8.1:lisflood.cpp:187`; `v8.2:lisflood.cpp:188`; `lisflood.cpp:191` | A 판 차이 | 8.0의 내부 기본값은 문서와 맞는다. 8.1 이후 값은 `10^{-6}`이다. 키워드 미지원 문제와 구분한다. |
| docx-manual:LV1-096 | user manual.docx p.24(변환본) `friction is not applied when the speed is below this threshold`. FV1·DG2에 적용한다고 적는다. | user manual.docx p.24(변환본) 표 10<br>user manual.docx p.24(변환본) `friction is not applied when the speed is below this threshold`. FV1·DG2에 적용한다고 적는다.<br>user manual.pdf p.20에 없다. | `swe/fv1.cpp:130–136`: `if (FABS(U) <= Solverptr->SpeedThresh`<br>`&& FABS(V) <= Solverptr->SpeedThresh)`<br>`{`<br>`HU = C(0.0);`<br>`HV = C(0.0);`<br>`continue;`<br>`}`<br>`swe/dg2/friction.cpp:91–94`: `if (FABS(U) <= Solverptr->SpeedThresh && FABS(V) <= Solverptr->SpeedThresh)`<br>`{`<br>`return;`<br>`}`<br>확인한 원문: user manual.docx p.24(변환본) 표 10; `swe/fv1.cpp:122–136`; `swe/dg2/friction.cpp:81–94`; `cuda/fv1/cuda_fv1_solver.cu:232–237`; `v8.0:swe/fv1.cpp:130–134`; `v8.1:swe/fv1.cpp:130–134`; `v8.2:swe/fv1.cpp:130–134`; `lisflood.h:755` | C 문서 누락 | FV1은 `if (FABS(U) <= Solverptr->SpeedThresh && FABS(V) <= Solverptr->SpeedThresh)`에서 `HU = C(0.0);`와 `HV = C(0.0);`을 실행한다. 이 조건은 앞선 건조 수심 검사를 통과한 셀에 적용된다. DG2는 같은 저속 조건에서 마찰 계산을 생략한다. 문서에는 FV1의 운동량 절단이 빠졌다. |
| docx-manual:LV1-104 | user manual.docx p.24(변환본) `zero applies the slope limiter globally`. | user manual.docx p.24(변환본) 표 10; user manual.pdf p.20 표 10<br>user manual.docx p.24(변환본) `zero applies the slope limiter globally`.<br>user manual.pdf p.20에 없다. | `swe/dg2/slope_limiter.cpp:298` `if (stencil_minH <= C(0.30) * Solverptr->maxH) return local_slope;`; `v8.0:swe/dg2/slope_limiter.cpp:287` `if (stencil_minH <= C(0.30)*Solverptr->maxH) return local_slope;`<br>확인한 원문: user manual.docx p.24(변환본) 표 10; user manual.pdf p.20 표 10; `swe/dg2/slope_limiter.cpp:298·320`; `v8.0:swe/dg2/slope_limiter.cpp:287` | C 문서 누락 | 임계값 0에서도 얕은 stencil은 먼저 반환한다. `globally`에는 이 예외가 필요하다. |
| docx-manual:LV1-273 | FV1·DG2의 방향별 HLL 호출. | user manual.docx p.14–15(변환본); user manual.pdf p.11–12<br>FV1·DG2의 방향별 HLL 호출. | `swe/hll.cpp:38–40`: `HLL(Solverptr, H_neg, HV_neg, -HU_neg, H_pos, HV_pos, -HU_pos,`<br>`H_flux, HV_flux, HU_flux);`<br>`HU_flux = -HU_flux;`; `swe/hll.cpp:60` `#include "hll_include.h"`; `swe/flux.cpp:50–52`의 질량·운동량 flux.<br>확인한 원문: user manual.docx p.14–15(변환본); user manual.pdf p.11–12; `swe/hll.cpp:38–40·60`; `swe/hll_include.h:1–31·42–58`; `swe/flux.cpp:42–52` | C 문서 누락 | Word는 HLL이라는 이름을 추가했다. y 방향 회전 부호·건습 분기·계산 flux 식은 적지 않는다. |
| docx-manual:LV1-274 | DG2 시간 적분과 제한기 예외. | user manual.docx p.15·23–24(변환본); user manual.pdf p.12·18<br>DG2 시간 적분과 제한기 예외. | `swe/dg2.cpp:74–76`: `apply_friction(Parptr, Solverptr, Arrptr);` / `rk_stage1(Parptr, Solverptr, BCptr, Arrptr);` / `rk_stage2(Parptr, Solverptr, BCptr, Arrptr);`; `swe/dg2/slope_limiter.cpp:298`의 `stencil_minH <= C(0.30)*Solverptr->maxH` 건너뛰기.<br>확인한 원문: user manual.docx p.15·23–24(변환본); user manual.pdf p.12·18; `swe/dg2.cpp:74–76`; `swe/dg2/slope_limiter.cpp:298` | C 문서 누락 | 두 Runge–Kutta 단계와 얕은 stencil의 제한 제외를 문서가 생략했다. krivodonovathresh=0을 전역 무조건 제한으로 읽지 않는다(LV1-104). [10-21 전수 검증 보완] |
| docx-manual:LV1-284 | CPU SWE·CUDA SWE·Metal의 drain·강우 경로. | user manual.docx p.22–24·37(변환본); user manual.pdf p.17–19·31–32<br>CPU SWE·CUDA SWE·Metal의 drain·강우 경로. | `swe/fv1.cpp:49–50`의 flow 갱신·배수 호출; `cuda/fv1/cuda_fv1_simulate.cu:142–175`는 공간 강우·균일 강우·점원·drain을 처리한다. `cuda/dg2/cuda_dg2_simulate.cu:170–174`의 `if (pars.drain_nodata)` 분기도 있다. `metal/fv1/metal_fv1_simulate.mm:1235` `if (pars->drain_nodata == ON && drainNodataPipeline) {`<br>확인한 원문: user manual.docx p.22–24·37(변환본); user manual.pdf p.17–19·31–32; `swe/fv1.cpp:34–50`; `swe/dg2.cpp:52–76`; `cuda/fv1/cuda_fv1_simulate.cu:142–175`; `cuda/dg2/cuda_dg2_simulate.cu:140–174`; `metal/fv1/metal_fv1_simulate.mm:1234–1249` | C 문서 누락 | Word의 새 옵션 설명을 모든 해법에 일괄 적용하면 안 된다. CUDA는 균일 rainfall도 처리한다. CPU SWE는 DynamicRain 경로를 사용한다. [10-21 전수 검증 보완] |
| files-output:LI2-318 | DG2 기울기 시작·출력 파일 | user manual.pdf p.32 | `swe/dg2.cpp:27` `read_dem_slopes(Fnameptr, Parptr, Arrptr, verbose);`; `swe/dg2.cpp:30–35` `if (Statesptr->startfile == ON)`<br>`{`<br>`read_h_slopes(Fnameptr, Parptr, Arrptr, verbose);`<br>`if (Statesptr->startq2d == ON)`<br>`{`<br>`read_discharge_slopes(Fnameptr, Parptr, Arrptr, verbose);`; `swe/dg2.cpp:107` `write_solution_slopes(Fnameptr, Statesptr, Parptr, Solverptr,`<br>확인한 원문: user manual.pdf p.32; `VersionHistory.h:34`; `v8.0:swe/dg2.cpp:27–35`; `swe/dg2.cpp:27–35,107–109`; `swe/dg2/dg2_output.cpp:13–24` | A 판 차이 | v8.0에 추가한 DG2는 수심 평균 격자 외에 x·y 기울기 파일을 읽고 쓴다. |
| files-output:LI2-331 | CPU SWE의 셀 중심 Q·V | user manual.pdf p.38 | `swe/output.cpp:134–141`의 `write_field(Arrptr->HU, ".Qx", ".Qxb", Fnameptr, Statesptr, Parptr);`, `write_field(Arrptr->HV, ".Qy", ".Qyb", Fnameptr, Statesptr, Parptr);`, `write_field(Arrptr->Vx, ".Vx", ".Vxb", Fnameptr, Statesptr, Parptr);`, `write_field(Arrptr->Vy, ".Vy", ".Vyb", Fnameptr, Statesptr, Parptr);`; `swe/output.cpp:189–190`의 outflag `0`; `swe/stats.cpp:139–140` `Vx = HU / H;` / `Vy = HV / H;`<br>확인한 원문: user manual.pdf p.38; `VersionHistory.h:34`; `swe/output.cpp:132–141,178–190`; `swe/stats.cpp:131–140` | A 판 차이 | v8.0에 추가한 CPU FV1·DG2의 Qx·Qy는 셀 중심 단위 폭 유량이다. 셀 경계 체적 유량과 구분한다. |
| files-output:LI2-332 | CPU SWE 출력 지원 범위 | user manual.pdf p.20–21·36–38 | `swe/fv1.cpp:66` `update_max_field(Parptr, Arrptr);`; `swe/fv1.cpp:99` `write_max_field(Fnameptr, Statesptr, Parptr, Arrptr);`; `swe/dg2.cpp:119`의 같은 writer; `swe/output.cpp:148–165`의 `.max/.maxb` 전용 출력<br>확인한 원문: user manual.pdf p.20–21·36–38; `VersionHistory.h:34`; `v8.0:swe/fv1.cpp:66,76–79,99`; `swe/fv1.cpp:39–99`; `swe/dg2.cpp:57–119`; `swe/output.cpp:148–165` | A 판 차이 | v8.0에 추가한 CPU FV1·DG2는 최대 수심과 관측점 출력을 처리한다. 두 반복문은 고전 IterateQ의 overpass·profile·hazard·중간 checkpoint·gauge 출력 블록을 호출하지 않는다. |
| par:LI1-225 | `fv1` 무인자 | user manual.pdf p.15–22 | `fv1` 무인자<br>`pars.cpp:582` `if (read_empty_param(param_name, line_number, param_value_ptr, "fv1", verbose, mode))`<br>`lisflood.cpp:269` `SimStates.fv1 = OFF;`<br>`pars.cpp:584` `Statesptr->fv1 = ON;`<br>`pars.cpp:585` `Solverptr->cfl = C(0.5);`<br>`pars.cpp:586` `Solverptr->DepthThresh = C(1e-3);`<br>`lisflood.cpp:778` `else if (Statesptr->fv1 == ON)`<br>`lisflood.cpp:779` `{`<br>`lisflood.cpp:780` `#ifdef METAL_ENABLED`<br>`lisflood.cpp:781` `// GPU requested (cuda or metal keyword) on an Apple Silicon Mac`<br>`lisflood.cpp:782` `if (Statesptr->cuda == ON && metal_is_available())`<br>`lisflood.cpp:783` `run_metal_fv1(*Fnameptr, &Fps, *Statesptr, *Parptr, *Solverptr, *BCptr,`<br>`lisflood.cpp:784` `*Stageptr, *Arrptr, verbosemode);`<br>`lisflood.cpp:785` `else`<br>`lisflood.cpp:786` `#endif`<br>`lisflood.cpp:787` `fv1::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`<br>`lisflood.cpp:788` `Stageptr, Arrptr, verbosemode);`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:582–586`; `lisflood.cpp:269,778–788`; `VersionHistory.h:34`; `v8.0:pars.cpp:571`; `VersionHistory.h:34`; `v8.0:pars.cpp:571–588`; `v8.1:pars.cpp:582–588`; `lisflood.cpp:419–426` | A 판 차이 | FV1은 v8.0에서 추가됐다. 현재 fv1은 `Solverptr->cfl = C(0.5);`와 `Solverptr->DepthThresh = C(1e-3);`을 대입한다. CUDA 실행에는 CUDA 빌드와 GPU 스위치가 필요하다. Metal 빌드의 FV1 분기는 `if (Statesptr->cuda == ON && metal_is_available())`에서 Metal을 실행한다. 이 조건이 거짓이면 CPU FV1을 실행한다. |
| par:LI1-230 | `dg2` 무인자 | user manual.pdf p.15–22 | `dg2` 무인자<br>`pars.cpp:630` `else if (read_empty_param(param_name, line_number, param_value_ptr, "dg2", verbose, mode))`<br>`lisflood.cpp:274` `SimStates.dg2 = OFF;`<br>`pars.cpp:632` `Statesptr->dg2 = ON;`<br>`pars.cpp:633` `Solverptr->cfl = C(0.33);`<br>`pars.cpp:634` `Solverptr->DepthThresh = C(1e-3);`<br>`pars.cpp:635` `Solverptr->DG2DepthThresh = C(-1.0);`<br>`pars.cpp:636` `Solverptr->DG2ThinDepthTstep = C(0.0);`<br>`lisflood.cpp:790` `else if (Statesptr->dg2 == ON)`<br>`lisflood.cpp:791` `{`<br>`lisflood.cpp:792` `dg2::solve(Fnameptr, &Fps, Statesptr, Parptr, Solverptr, BCptr,`<br>`lisflood.cpp:793` `Stageptr, Arrptr, verbosemode);`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:630–636`; `lisflood.cpp:274,790–793`; `VersionHistory.h:34`; `v8.0:pars.cpp:579`; `VersionHistory.h:34`; `v8.0:pars.cpp:579–588`; `lisflood.cpp:432–435` | A 판 차이 | DG2는 v8.0에서 추가됐다. 현재 dg2는 CPU 또는 CUDA DG2를 선택한다. `Solverptr->cfl = C(0.33);`을 설정한다. `Solverptr->DepthThresh = C(1e-3);`을 설정한다. 뒤에 읽은 옵션은 이 값을 다시 바꿀 수 있다. |
| par:LI1-233 | `dg2depththresh` 실수; m | user manual.pdf p.15–22 | `dg2depththresh` 실수; m<br>`pars.cpp:708` `if (read_numeric_param(param_name, line_number, param_value_ptr, "dg2depththresh", &Solverptr->DG2DepthThresh, verbose, mode))`<br>`pars.cpp:635` `Solverptr->DG2DepthThresh = C(-1.0);`<br>`swe/dg2.cpp:1059` `bool dg2::thin_depth`<br>`swe/dg2.cpp:1060` `(`<br>`swe/dg2.cpp:1061` `Solver *Solverptr,`<br>`swe/dg2.cpp:1062` `NUMERIC_TYPE H`<br>`swe/dg2.cpp:1063` `)`<br>`swe/dg2.cpp:1064` `{`<br>`swe/dg2.cpp:1065` `//    return H > Solverptr->DepthThresh && H <= Solverptr->DG2DepthThresh;`<br>`swe/dg2.cpp:1066` `return H <= C(10.0) * Solverptr->DepthThresh; // thin layer depth is 10*thresh`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:635,708`; `swe/dg2.cpp:1059–1066`; `pars.cpp:708–717` | C 문서 누락 | 공통 파서는 `dg2depththresh`을 읽는다. dg2를 먼저 켜야 한다. 읽은 값의 활성 사용은 없다. thin_depth의 활성 식은 `return H <= C(10.0) * Solverptr->DepthThresh;`이다. 입력 필드를 쓰는 식은 주석이다. |
| par:LI1-234 | `dg2thindepth_tstep` 실수; s | user manual.pdf p.15–22 | `dg2thindepth_tstep` 실수; s<br>`pars.cpp:718` `if (read_numeric_param(param_name, line_number, param_value_ptr, "dg2thindepth_tstep", &Solverptr->DG2ThinDepthTstep, verbose, mode))`<br>`pars.cpp:636` `Solverptr->DG2ThinDepthTstep = C(0.0);`<br>`swe/dg2.cpp:1165` `{`<br>`swe/dg2.cpp:1166` `//if (thin_depth(Solverptr, H) && Solverptr->DG2ThinDepthTstep > C(0.0))`<br>`swe/dg2.cpp:1167` `//{`<br>`swe/dg2.cpp:1168` `//    return (std::min)({dt, Solverptr->DG2ThinDepthTstep});`<br>`swe/dg2.cpp:1169` `//}`<br>`swe/dg2.cpp:1170` `if (H > Solverptr->DepthThresh)`<br>`swe/dg2.cpp:1171` `{`<br>`swe/dg2.cpp:1172` `NUMERIC_TYPE U = HU/H;`<br>`swe/dg2.cpp:1173` `NUMERIC_TYPE V = HV/H;`<br>`swe/dg2.cpp:1174` `NUMERIC_TYPE dt_local_x = Solverptr->cfl*Parptr->dx/(FABS(U)+SQRT(Solverptr->g*H));`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:636,718`; `swe/dg2.cpp:1165–1174`; `pars.cpp:718–727` | C 문서 누락 | 공통 파서는 `dg2thindepth_tstep`을 읽는다. dg2를 먼저 켜야 한다. 읽은 시간 간격 제한 식은 주석이다. 활성 CFL 계산은 이 필드를 쓰지 않는다. |
| par:LI1-256 | `limitslopes` 무인자 | user manual.pdf p.15–22 | `limitslopes` 무인자<br>`pars.cpp:973` `if (read_empty_param(param_name, line_number, param_value_ptr, "limitslopes", verbose, mode))`<br>`lisflood.cpp:148` `Params.limit_slopes = OFF;`<br>`pars.cpp:973` `if (read_empty_param(param_name, line_number, param_value_ptr, "limitslopes", verbose, mode))`<br>`pars.cpp:974` `{`<br>`pars.cpp:975` `if (Statesptr->dg2 == OFF && Statesptr->mwdg2 == OFF && Statesptr->fv2 == OFF)`<br>`pars.cpp:976` `{`<br>`pars.cpp:977` `printf("ERROR Slope limiter only applicable to DG2, MWDG2 and FV2 solvers\n");`<br>`pars.cpp:978` `exit(EXIT_FAILURE);`<br>`pars.cpp:979` `}`<br>`pars.cpp:980` `Parptr->limit_slopes = ON;`<br>`pars.cpp:981` `if (verbose == ON) printf("DG2/FV2 slope limiter enabled\n");`<br>`pars.cpp:982` `return;`<br>`pars.cpp:983` `}`<br>`swe/dg2.cpp:319` `if (Parptr->limit_slopes == ON)`<br>`swe/dg2.cpp:320` `{`<br>`swe/dg2.cpp:321` `apply_slope_limiter(Parptr, Solverptr, Arrptr, U);`<br>`swe/dg2.cpp:322` `}`<br>`swe/dg2.cpp:323` `else`<br>`swe/dg2.cpp:324` `{`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:973–983`; `lisflood.cpp:148`; `swe/dg2.cpp:319–324` | C 문서 누락 | 공통 파서는 `limitslopes`을 읽는다. DG2·MWDG2·FV2를 먼저 선택해야 한다. 이후 CPU DG2의 slope limiter를 켠다. 적응 MWDG2는 같은 이름을 다시 읽는다. |
| par:LI1-257 | `krivodonovathresh` 실수; 무차원 | user manual.pdf p.15–22 | `krivodonovathresh` 실수; 무차원<br>`pars.cpp:984` `if (read_numeric_param(param_name, line_number, param_value_ptr, "krivodonovathresh", &Solverptr->krivodonova_threshold, verbose, mode))`<br>`lisflood.cpp:190` `ParSolver.krivodonova_threshold = C(10.0);`<br>`swe/dg2/slope_limiter.cpp:320` `if (FMAX(DS_backward, DS_forward) >= Solverptr->krivodonova_threshold)`<br>`swe/dg2/slope_limiter.cpp:321` `{`<br>`swe/dg2/slope_limiter.cpp:322` `return minmod`<br>`swe/dg2/slope_limiter.cpp:323` `(`<br>`swe/dg2/slope_limiter.cpp:324` `local_slope,`<br>`swe/dg2/slope_limiter.cpp:325` `(local_const - backward_const) / SQRT(C(3.0)),`<br>확인한 원문: user manual.pdf p.15–22; `pars.cpp:984`; `lisflood.cpp:190`; `swe/dg2/slope_limiter.cpp:320–325`; `cuda/adaptive/classes/SolverParams.h:23,58–61` | C 문서 누락 | 공통 파서는 `krivodonovathresh`을 읽는다. Krivodonova 불연속 검출 문턱이다. 기본값은 10이다. 적응 파서의 tol_Krivo와 별개이다. |
| par:LI1-314 | 위어·강우·진단 옵션의 신규 해법 경로 | user manual.pdf p.15–22 | `swe/fv1.cpp:34` `DynamicRain<> rain(Fnameptr->dynamicrainfilename, verbose);`<br>`swe/fv1.cpp:35` (빈 줄)<br>`swe/fv1.cpp:36` `time_t loop_start;`<br>`swe/fv1.cpp:37` `time(&loop_start);`<br>`swe/fv1.cpp:38` (빈 줄)<br>`swe/fv1.cpp:39` `while (Solverptr->t < Solverptr->Sim_Time)`<br>`swe/fv1.cpp:40` `{`<br>`swe/fv1.cpp:41` `zero_flux_stats(BCptr);`<br>`swe/fv1.cpp:42` (빈 줄)<br>`swe/fv1.cpp:43` `rain.update_H(Parptr, Solverptr, Arrptr);`<br>`swe/fv1.cpp:44` `update_point_sources(Parptr, Solverptr, BCptr, Arrptr);`<br>`swe/fv1.cpp:45` `apply_friction(Parptr, Solverptr, Arrptr);`<br>`swe/fv1.cpp:46` `update_Hstar(Parptr, Arrptr);`<br>`swe/fv1.cpp:47` `update_fluxes(Parptr, Solverptr, Arrptr);`<br>`swe/fv1.cpp:48` `update_fluxes_on_boundaries(Parptr, Solverptr, BCptr, Arrptr);`<br>`swe/fv1.cpp:49` `update_flow_variables(Parptr, Solverptr, Arrptr);`<br>`swe/fv1.cpp:50` `fv1::drain_nodata_water(Parptr, Solverptr, BCptr, Arrptr);`<br>`swe/dg2.cpp:52` `DynamicRain<> rain(Fnameptr->dynamicrainfilename, verbose);`<br>`swe/dg2.cpp:53` (빈 줄)<br>`swe/dg2.cpp:54` `time_t loop_start;`<br>`swe/dg2.cpp:55` `time(&loop_start);`<br>`swe/dg2.cpp:56` (빈 줄)<br>`swe/dg2.cpp:57` `while (Solverptr->t < Solverptr->Sim_Time)`<br>`swe/dg2.cpp:58` `{`<br>`swe/dg2.cpp:59` (빈 줄)<br>`swe/dg2.cpp:60` `zero_flux_stats(BCptr);`<br>`swe/dg2.cpp:61` (빈 줄)<br>`swe/dg2.cpp:62` `if (Parptr->limit_slopes == ON) Solverptr->maxH = maxH(Parptr, Arrptr);`<br>`swe/dg2.cpp:63` `rain.update_H(Parptr, Solverptr, Arrptr);`<br>`swe/dg2.cpp:64` `update_point_sources(Parptr, Solverptr, BCptr, Arrptr);`<br>`swe/dg2.cpp:65` `update_boundary_values(Parptr, Solverptr, BCptr, Arrptr);`<br>`metal/fv1/metal_fv1_simulate.mm:1347` `if (states.rainfallmask == ON \|\| states.routing == ON) {`<br>`metal/fv1/metal_fv1_simulate.mm:1348` `fprintf(stderr, "ERROR: Metal FV1 does not support rainfallmask or rainfallrouting; "`<br>`metal/fv1/metal_fv1_simulate.mm:1349` `"use unmasked rainfall or dynamicrainfile.\n");`<br>`metal/fv1/metal_fv1_simulate.mm:1350` `std::exit(EXIT_FAILURE);`<br>`metal/fv1/metal_fv1_simulate.mm:1351` `}`<br>`metal/fv1/metal_fv1_simulate.mm:1352` `if (states.rainfall == ON && !arrays.rain) {`<br>`metal/fv1/metal_fv1_simulate.mm:1353` `fprintf(stderr, "ERROR: Metal FV1 requires a loaded rainfall time series.\n");`<br>`metal/fv1/metal_fv1_simulate.mm:1354` `std::exit(EXIT_FAILURE);`<br>확인한 원문: user manual.pdf p.15–22; `swe/fv1.cpp:34–50`; `swe/dg2.cpp:52–65`; `metal/fv1/metal_fv1_simulate.mm:1347–1354` | C 문서 누락 | CPU FV1·DG2는 DynamicRain 입력을 쓴다. 고전 Rainfall·Evaporation·FPInfiltration·weir 함수 호출이 같은 모양으로 포함되어 있지 않다. Metal FV1은 rainfallmask 또는 routing을 거부한다. 공통 파서의 수용과 실제 해법의 지원은 다르다. |
