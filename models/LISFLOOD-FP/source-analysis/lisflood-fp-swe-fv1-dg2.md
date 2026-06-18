---
title: "LISFLOOD-FP full SWE 솔버 — FV1 / DG2 (Godunov · Discontinuous Galerkin · HLL Riemann)"
model: LISFLOOD-FP
component: swe-solver
canonical_source: self
citation_status: verified
verification_method: "swe/{fv1,dg2,dg2new,hll,flux,fields,boundary}.cpp + hll_include.h + dg2new.h 전수 Read, dispatch는 lisflood.cpp:775-792 직접 확인 (2026-06-18)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[lisflood-fp-architecture-source-map]]"
---

# LISFLOOD-FP full SWE 솔버 (SEAMLESS-WAVE / Kesserwani 계열)

LISFLOOD-FP의 전통 솔버(local-inertial `acceleration`, SGC)와 별개로 `swe/`
디렉토리에는 **완전 천수방정식(full Shallow Water Equations)** 을 푸는 신규
유한체적/DG 솔버가 들어 있다. 두 가지 실가동 경로가 있다.

| 옵션 | 함수 | 정확도 | 자료구조 |
|---|---|---|---|
| `fv1` | `fv1::solve` (`swe/fv1.cpp:10`) | 1차 Godunov 유한체적 (FV1) | cell-centred H,HU,HV |
| `dg2` | `dg2::solve` (`swe/dg2.cpp:14`) | 2차 Discontinuous Galerkin (DG2) + RK2 | cell-mean + x·y slope 계수 |

디스패치는 `lisflood.cpp:775` (`Statesptr->fv1 == ON`) / `:780`
(`Statesptr->dg2 == ON`)에서 분기한다.

> **중요 정정 — `dg2new`는 multiwavelet 적응 솔버가 아니다.**
> `swe/dg2new.cpp`(`dg2new::DG2Solver`, `:11`)는 **균일격자 CPU DG2 리팩터링
> 시제품**이며, `lisflood.cpp:784-786`에서 **주석 처리되어 비가동** 상태다.
> BC 처리가 `// FIXME: BC treatment`(`dg2new.cpp:300, 350`)로 미완이고
> 슬로프 리미터·점원(point source)도 없다. 실제 multiwavelet(MW) 적응 격자
> 솔버는 `swe/`가 아니라 **GPU 측 `cuda/adaptive/mra/`** 에 있다
> (`cuda/adaptive/mra/encode_and_thresh_flow.cu`,
> `cuda/adaptive/types/SolverTypes.h` 등 — 본 노트 범위 밖, grep 확인 2026-06-18).
> 따라서 이 노트는 `dg2new`를 "DG2 자료구조·연산자를 객체지향으로 재정리한
> 참고 구현"으로만 다룬다.

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
(외부 `modifiedvars.h`). 면 $H^\star$ 평균을 쓰는 것이 정수해(lake-at-rest)
보존의 핵심 — well-balanced 이산화.

### 3.4 마찰 (`apply_friction`, `fv1.cpp:104`)

Manning 마찰을 반음해로 처리. $C_f=g n^2/H^{1/3}$(`fv1.cpp:141`),
마찰 소스 $S_{f,x}=-C_f U|\mathbf{u}|$(`:144`), 분모에 Jacobian 항
$D_x=1+\Delta t\,C_f(2U^2+V^2)/(H|\mathbf{u}|)$(`:146-147`)을 두어
$HU \mathrel{+}= \Delta t\,S_{f,x}/D_x$(`:151`). 수심·속도 임계값 미만이면
유량 0(`fv1.cpp:122-136`).

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
순회(`dg2.cpp:1093-1151`). `thin_depth`는 `H≤10·DepthThresh`(`:1066`).

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
| `FREE1` | 자유 유출 | 내부값 복사 (`fv1.cpp:523`) |
| `HFIX2`/`HVAR3` | 고정/시변 수위 | $H_{out}=\max(0,\,\eta_{bc}-z)$ (`fv1.cpp:531`, `dg2.cpp:625`) |
| `QFIX4`/`QVAR5` | 고정/시변 유량 | $HU_{out}=\text{sign}\cdot q$, 미소 수심 보장 (`fv1.cpp:548-551`) |
| `NONE0`(기본) | 폐쇄/반사벽 | $HU_{out}=-HU_{in}$ (`fv1.cpp:577`, `dg2.cpp:658`) |

DG2의 경계는 셀 한쪽 면 재구성값(`limit_pos/neg`, `dg2.cpp:202-206`)을
ghost로 쓰며 결과를 `Arrptr->boundary.{H,HU,HV}`에 저장(`dg2.cpp:213-215`),
다음 CFL 산정에서 재사용한다(`dg2.cpp:1101`).

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

`dg2new::DG2Solver`(`dg2new.cpp:11`)는 동일 DG2 수학을 객체지향+값타입
(`FlowVector`,`Increment`,`dg2new.h:6-32`)으로 재정리한 시제품. 차이/한계:

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
  재구성($\pm\sqrt3$ 가우스점, `:643-657`) — hydrostatic reconstruction.

**이 코드는 `lisflood.cpp:784`에서 주석 처리되어 빌드/실행에 포함되지 않는다.**
실제 적응(multiwavelet) 솔버 분석은 `cuda/adaptive/`(GPU) 별도 노트 대상.

---

## 요약

- 신규 full-SWE 경로는 **FV1(1차 Godunov)** 와 **DG2(2차 DG+SSP-RK2)** 두 가지가
  실가동, 둘 다 **HLL Riemann 플럭스**(`hll_include.h`)와 well-balanced 하상
  소스항을 공유.
- DG2는 셀당 평균+x·y 슬로프, L=L0+L1x+L1y 약형식, 가우스 2점 구적으로 체적적분.
- `dg2new`(질문이 multiwavelet으로 지목)는 **실제로는 비가동 CPU DG2 리팩터**이며,
  MW 적응 격자는 `cuda/adaptive/mra/`에 존재(범위 밖). 이 점이 본 검수의 핵심 정정.
