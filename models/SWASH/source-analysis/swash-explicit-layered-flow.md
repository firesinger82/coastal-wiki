---
title: "SWASH 명시적 다층 flow solver — SwashExpLay*flow 5종 (layer-averaged + 비정수압 압력)"
model: SWASH
component: src (explicit multi-layer flow solver)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashExpLay1DHflow.ftn90 Purpose/Method(:46-91)·gmat build(:512-635)·Poisson 조립(:2246-2335)·Poisson solve(:2407-2447)·압력 update(:2462-2472)·속도 correction(:2476-2535)·wom 계산(:2978-3068), SwashExpLayP1DHflow.ftn90 subgrid Purpose(:50-91)·coarse gmat(:609-668), SwashExpLayUflow.ftn90 Purpose(:42-76), SwashModule1.ftn90 ihydro/iproj/qlay/qmax/kpmax 정의(:363,:614-649) 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 명시적 다층 flow solver — SwashExpLay*flow 5종

> 명시적(explicit) 다층(layer-averaged) 천수 파-흐름 solver. 연직 layer 구조 + 비정수압 압력(non-hydrostatic pressure)을 pressure-correction(projection)으로 푼다. (경로: raw/source_code/swash/src/)

## 1. 5개 파일의 역할 분담

`Lay` = 다층(multi-layer, layer-averaged), `P` 접미사 = **subgrid 압력 layer** 변종(velocity layer ≠ pressure layer). 모두 명시적(explicit) 시간적분 루틴이다.

| 파일 | 차원/격자 | 압력-속도 layer | 라인수 | Purpose 인용 |
|---|---|---|---|---|
| `SwashExpLay1DHflow.ftn90` | 1DH 직교 | 동일 (velocity=pressure) | 3200 | "non-hydrostatic, layer-averaged 1D shallow water equations" `SwashExpLay1DHflow.ftn90:48` |
| `SwashExpLay2DHflow.ftn90` | 2DH 직교 | 동일 | 7746 | "...2D shallow water equations" `SwashExpLay2DHflow.ftn90:50` |
| `SwashExpLayUflow.ftn90` | 비정렬 삼각망(triangular) | 동일 | 3173 | "...shallow water equations on triangular mesh" `SwashExpLayUflow.ftn90:44` |
| `SwashExpLayP1DHflow.ftn90` | 1DH 직교 + subgrid | **coarse pressure / fine velocity** | 4068 | "...1D shallow water equations solved with a subgrid approach" `SwashExpLayP1DHflow.ftn90:52-53` |
| `SwashExpLayP2DHflow.ftn90` | 2DH 직교 + subgrid | coarse / fine | 9383 | "...2D shallow water equations" `SwashExpLayP2DHflow.ftn90:56` |

`P`-변종의 핵심(subgrid approach) verbatim:
> "A subgrid approach is applied in which the horizontal and vertical momentum equations are solved on separate grids in the vertical. The vertical momentum equation and the pressure Poisson equation are solved on a coarse vertical grid, whereas the horizontal momentum equation is solved on a subgrid with a high vertical resolution. Non-hydrostatic pressure on subgrid is obtained by means of linear interpolation." — `SwashExpLayP1DHflow.ftn90:88-91`

`ihydro==3`(subgrid)과 `kpmax`(coarse pressure layer 수)는 P-변종에만 등장한다 (비-P 3개 파일에서 grep count = 0; P1DH 11/90회, P2DH 14/121회 출현 — 직접 grep 확인).

## 2. 공통 Method (5개 파일 동일 헤더)

`SwashExpLay1DHflow.ftn90:50-81` Method 블록 verbatim 요약 (5개 파일 거의 동일):

| 항 | 시간적분 | 비고 |
|---|---|---|
| 연속방정식 + 수위경사(∂ζ/∂x) | leap-frog (Hansen scheme) | `:52-53` |
| 수평 advection | predictor-corrector MacCormack (1DH/2DH); Euler explicit (Uflow `:51`) | `:55-56` |
| 바닥마찰 | Euler implicit | `:56` |
| 비정수압 압력경사 | semi-implicit θ-scheme | `:57` |
| 연직 advection·viscosity | semi-implicit → tri-diagonal 시스템 | `:57-58` |

- 수평 advection 공간이산: momentum conservative (flow contraction 시 energy-head conservative), 1차 upwind 또는 고차 flux-limited (CDS/Fromm/BDF/QUICK/MUSCL/Koren), 고차는 defect correction `:60-63`.
- 연직 advection·viscosity: finite-volume 중심차분 `:65-66`.
- 비정수압 압력: "second order accurate pressure correction technique" `:81`.

θ(implicitness factor)는 `theta` (비정수압 압력경사), `thetau`(u-momentum 연직항), `thetaw`(w-momentum 연직항)로 분리 — `SwashExpLay1DHflow.ftn90:156-159`.

## 3. 연직 layer 구조와 핵심 배열

layer 인덱스 `k=1`(표층)…`k=kmax`(저층). loop counter `k`, 이웃 layer `kd=k-1`, `ku=k+1`, `kdd=k-2`, `kuu=k+2` — `SwashExpLay1DHflow.ftn90:113-117`. 거의 모든 연산이 `do k = 1, kmax` layer loop 안에서 수행 (1DH 파일에서만 30+회 출현).

| 배열 | 의미 | 출처 |
|---|---|---|
| `hks(nm,k)` | layer k 두께 (수위점) | `:534` 등 사용 |
| `hkum(nm,k)` | layer k 두께 (u-velocity점) | `:529` |
| `zks(nm,k)` | layer interface k의 z-좌표 (수위점) | `:531-532` |
| `wom(nm,k)` | **layer interface 상대 연직속도** (streamline 연직속도 − interface 연직속도) | `:69-70`, `:2995` |
| `w1(nm,k)` | z-방향 연직속도 (w-momentum 해) | `:74-75`, `:2217` |
| `q(nm,k)` / `dq(nm,k)` | 비정수압 압력 / 압력보정 | `:2467`, `:2494` |

`wom`의 정의(verbatim): "This relative velocity, stored in array wom, is defined as the difference between the vertical velocity along the streamline and the vertical velocity along the interface." — `SwashExpLay1DHflow.ftn90:69-70`. 표면 상대속도 허용오차 `epswom=0.001`(1DH/2DH) / `0.005`(Uflow) — `SwashExpLay1DHflow.ftn90:107`, `SwashExpLayUflow.ftn90:92`.

## 4. 비정수압 압력 모드 (ihydro)

`SwashModule1.ftn90:614-618` 정의 verbatim:
> `ihydro` indicates (non-)hydrostatic flow computation
> `=0` hydrostatic
> `=1` non-hydrostatic using box scheme for vertical pressure gradient
> `=2` non-hydrostatic using standard discretization for vertical pressure gradient
> `=3` box scheme applied for a pressure layer containing a number of velocity layers

| ihydro | 압력 위치 | gradient matrix 계수 수 | 인용 |
|---|---|---|---|
| 1 (Keller-box) | layer interface 중심 | 4 (`gmatu(nm,k,1..4)`) | `SwashExpLay1DHflow.ftn90:516,534-537` |
| 2 (central diff) | cell center | 6 (`gmatu(nm,k,1..6)`) | `:598,617-622` |
| 3 (subgrid box) | coarse pressure layer | `gmatu0`(단일층) 또는 `gmatu(nm,kp,..)` | `SwashExpLayP1DHflow.ftn90:611-668` |

### 4.1 gradient matrix 조립 (`gmatu`)
Keller-box (`ihydro==1`), `SwashExpLay1DHflow.ftn90:529-537`:
```
fac  = 0.5 * rdx / hkum(nm,k)
fac1 = zks(nmu,k-1) - zks(nm,k-1)
fac2 = zks(nmu,k  ) - zks(nm,k  )
gmatu(nm,k,1) = (-hks(nm ,k) - fac1) * fac
gmatu(nm,k,2) = (-hks(nm ,k) + fac2) * fac
gmatu(nm,k,3) = ( hks(nmu,k) - fac1) * fac
gmatu(nm,k,4) = ( hks(nmu,k) + fac2) * fac
```
= u-velocity점에서 비정수압 압력 q의 수평경사를 layer interface 기하(`zks`)와 두께(`hks`,`hkum`)로 표현. central(`ihydro==2`)는 6계수 + 연직 인접 layer(`kd`,`ku`) 기여 포함 `:614-622`.

경계 처리: 좌(`LMXF`)/우(`LMXL`) Neumann 반사 — interface 계수를 인접으로 접어 넣고 0으로 — `:550-566`. 표층(`k=1`) bottom-face 계수 제거 `:574-576`.

### 4.2 P-변종 coarse-grid gradient (`gmatu0`, kup)
`SwashExpLayP1DHflow.ftn90:611-625` — `ihydro==3`(단일 압력층)일 때 depth-averaged 형태:
```
fac = 0.5 * rdx / hum(nm)
gmatu0(nm,1) = -fac * ( s0(nm ) + dps(nmu) )
gmatu0(nm,2) =  fac * ( s0(nmu) + dps(nm ) )
```
다중 coarse 층(`kp=1,kpmax`)은 `kup(kp)`로 velocity layer 인덱스 매핑, `hkumc`(coarse 두께) 사용 `:652-668`. `kpv(k)`는 velocity layer→pressure layer 역매핑 (advection 등에서 background current 참조 시) `:1213-1240`.

`kpmax` = "number of vertical pressure layers" `SwashModule1.ftn90:363`.

## 5. Pressure Poisson 방정식 (projection)

비정수압 압력 보정 = $A_p\,\delta q = \mathrm{rhs}$, where $A_p = D\,G$ (divergence × gradient).

### 5.1 divergence matrix (`dmat`)
`SwashExpLay1DHflow.ftn90:2261-2276` — layer 별 6계수:
```
dmat(nm,k,2) =  rdx * hku(nm ,k) - fac1 * hks(nm,kd) + fac2 * hks(nm,ku)
dmat(nm,k,4) = -rdx * hku(nmd,k) - fac1 * hks(nm,kd) + fac2 * hks(nm,ku)
dmat(nm,k,5) =  fac2 * hks(nm ,k)   ! 상부 layer 기여
```
저층(`k==kmax`)은 `fac2=0`(바닥 무유속) `:2269`. 표층 free-surface BC 반영 `:2292-2298`.

### 5.2 Poisson matrix (`amatp = dmat·gmat`)
`SwashExpLay1DHflow.ftn90:2318-2335` — divergence와 gradient를 곱해 19-band(`amatp(nm,k,1..24)`) 행렬 조립. 대각 + w-momentum gradient(`gmatw`) 기여 `:2322-2323`. 이것이 $D G$ 구조의 명시적 구현.

### 5.3 Poisson solve
`SwashExpLay1DHflow.ftn90:2409-2447`:
- `qmax==1` (depth-averaged 1압력층): `tridiag` 직접 해 `:2411`.
- 그 외: BiCGSTAB `:2443`, 선택적 ILU 전처리 `icond=1/2/3` → `iluds`/`iludr`/`ilu` `:2419-2435`. (선형 solver 상세는 `swash-source-analysis-nonhydrostatic`/Poisson 노트 참조 — source-needed in this note.)
- subdomain 교환 `SWEXCHG` `:2451`.

`qlay`/`qmax`(reduced Poisson): qlay = "number of layers for which pressure is constant to be used in reduced pressure equation method", qmax = "total number of layers for reduced pressure Poisson equation (=kmax-qlay)" — `SwashModule1.ftn90:647-649`. 상위 `qlay`개 layer 압력을 동일 처리해 Poisson 차수를 줄임 `SwashExpLay1DHflow.ftn90:581-592`, 해 후 `dq(:,qmax+1:kmax)=dq(:,qmax)`로 복제 `:2454-2458`.

## 6. 압력 update와 속도 correction (projection 마무리)

### 6.1 압력 update — iproj
`SwashExpLay1DHflow.ftn90:2466-2470`:
```
if ( iproj == 1 ) then   ! pressure correction method
   q = q + dq
else if ( iproj == 2 ) then   ! classical projection method
   q = dq
endif
```
`iproj=1` pressure-correction (증분), `iproj=2` classical projection — `SwashModule1.ftn90:622-624`.

### 6.2 속도 보정
u-velocity `:2494-2495`:
```
u1(nm,k) = u1(nm,k) - dt*theta*( gmatu(nm,k,1)*dq(nm,kd) + ... + gmatu(nm,k,6)*dq(nmu,ku) )
```
w-velocity `:2515-2531` — Keller-box(`ihydro==1`)는 전 layer 합산(`do j=0,kmax-1`, `gmatw`) `:2517-2525`, central(`ihydro==2`)는 인접 2층만 `:2529`. 모두 $\mathbf{u}^{n+1} = \mathbf{u}^* - \Delta t\,\theta\,G\,\delta q$ 형태의 명시적 projection 보정.

## 7. 상대 연직속도 wom 재계산 (2 분기)

`SwashExpLay1DHflow.ftn90:2978-3068` — Method `:68-72`에 명시된 두 경로:

분기 A — **hydrostatic (ihydro==0)**: 층별 연속방정식에서 표면→바닥으로 적분 복원 `:2982-3008`:
```
wom(nm,k) = wom(nm,k+1) - rdx*( hku(nm,k+1)*u1(nm,k+1) - hku(nmd,k+1)*u1(nmd,k+1) ) - ( hksnew(nm,k+1) - hks(nm,k+1) )/dt
```
표면(`k=0`) 상대속도가 `epswom` 초과 시 경고 후 0 설정 `:3016-3023`.

분기 B — **non-hydrostatic**: w-momentum 해 `w1`에서 직접 `:3038-3047`:
```
fac = ( fac2*hks(nm,k) + fac1*hks(nm,k+1) ) / ( hks(nm,k) + hks(nm,k+1) )
wom(nm,k) = w1(nm,k) - ( zksnew(nm,k) - zks(nm,k) )/dt - fac*rdx*( zkuo(nm,k) - zkuo(nmd,k) )
```
즉 wom = (z-방향 연직속도 w1) − (interface 이동속도 ∂z/∂t) − (수평이류에 의한 interface 경사 기여). 표면·바닥 `wom=0` `:3049-3050`.

분기 B-예외 — **breaking wave 전면**: `brks(nm)==1`이면 정수압 가정, 국소 연속방정식으로 wom 복원(분기 A 식 재사용) `:3052-3062`. verbatim: "hydrostatic pressure is assumed at steep front of breaking wave, so relative vertical velocity is derived from local continuity equation" `:3054`.

## 8. 전체 시간스텝 흐름 (1DH 대표, 명시적 순서)

`SwashExpLay1DHflow.ftn90` 섹션 주석 순서:
1. 시간미분·질량flux 계산 `:254,:275`
2. gradient matrix `gmatu` 조립 `:512`, 압력경사 `:681`
3. u-momentum 우변 조립(advection/마찰/바람/viscosity) `:746-971`, tri-diagonal 해 `:1197`
4. 고차 advection defect correction `:1311,:1414`
5. w-momentum 조립·해 `:1518,:2192-2234` (thetaw 복원 `:2234`)
6. 비정수압 압력보정: dmat·Poisson 조립·해 `:2246-2447`
7. 압력 update `:2462`, 속도 correction `:2474`
8. global continuity (predictor-corrector / Heun) → 수위 `:2578-2651`
9. wom 재계산 `:2978`, CFL `:3086`

global continuity 시간적분 분기는 `jhk` (1=RK3, 2=Hancock, 3=Euler) — `SwashModule1.ftn90:625-628`; 8.01 업데이트 "Hancock scheme for global continuity equation" `SwashExpLay1DHflow.ftn90:43`.

## 9. Uflow(삼각망) 차이

`SwashExpLayUflow.ftn90` — 직교격자 `m`/`mu` 인덱싱 대신 cell face loop("loop over faces of the cell") 기반 `:255,:334,:482` 등 다수. advection은 Euler explicit + "r-ratio formulation based on most upwave vertex" `:51,:58`. gmat/Poisson 구조는 동일(Keller-box `:649` / central `:726`), 단 2단계 블록(`:645`, `:1989`)으로 분리 — 1차 build와 후속 build. 나머지 비정수압 메커닉(pressure correction, wom 2분기)은 직교 버전과 동일 패턴.

## 10. 미확인 / source-needed
- 선형 solver(`bicgstab`/`tridiag`/ILU `iluds`/`iludr`/`ilu`) 내부는 본 노트 범위 밖 — 별도 Poisson/solver 노트 참조 필요 (source-needed).
- `gmatw`(w-momentum gradient matrix) 상세 조립부는 5절에서 amatp 기여로만 언급 — 전체 build 라인(`:1957` 부근) 미전사 (분량 비례 생략).
- P2DH(9383줄)는 P1DH와 동일 메커닉의 2DH 확장으로 간주, 개별 라인 미전사 (Purpose `:56`만 인용).
