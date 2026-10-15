---
title: "SWASH 명시적 다층 flow solver — SwashExpLay*flow 5종 (layer-averaged + 비정수압 압력)"
model: SWASH
component: src (explicit multi-layer flow solver)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashExpLay1DHflow.ftn90 Purpose/Method(:46-91)·gmat build(:512-635)·Poisson 조립(:2246-2335)·Poisson solve(:2407-2447)·압력 update(:2462-2472)·속도 correction(:2476-2535)·wom 계산(:2978-3068), SwashExpLayP1DHflow.ftn90 subgrid Purpose(:50-91)·coarse gmat(:609-668), SwashExpLayUflow.ftn90 Purpose(:42-76), SwashModule1.ftn90 ihydro/iproj/qlay/qmax/kpmax 정의(:363,:614-649) 인용 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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

경계 처리: 좌(`LMXF`)/우(`LMXL`) 경계에서 제거할 압력 계수를 남길 계수에서 뺀다. 제거할 계수는 0으로 만든다 (`src/SwashExpLay1DHflow.ftn90:550–566`). [10-15 전수 검증 정정]
최상층 1에서 위쪽 자유수면 경계면의 압력 계수 1·3을 0으로 만든다. (`src/SwashExpLay1DHflow.ftn90:574–575` `gmatu(nm,1,1) = 0.`·`gmatu(nm,1,3) = 0.`). [10-15 대조 정정]
아래쪽 경계면 계수 2·4를 없애는 처리가 아니다. (`src/SwashExpLay1DHflow.ftn90:531–537`). [10-15 대조 정정]

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
- `qmax`가 1이 아니면 BiCGSTAB으로 푼다 (`src/SwashExpLay1DHflow.ftn90:2409–2447`). `lprecon`이 참이면 `icond`에 따라 `iluds`·`iludr`·`ilu` 전처리를 선택한다 (`src/SwashExpLay1DHflow.ftn90:2416–2437`). 구현은 [선형 솔버 노트](swash-linear-solvers.md)에 정리되어 있다. [10-15 전수 검증 정정]
- subdomain 교환 `SWEXCHG` `:2451`.

`qlay`/`qmax`(reduced Poisson): qlay = "number of layers for which pressure is constant to be used in reduced pressure equation method", qmax = "total number of layers for reduced pressure Poisson equation (=kmax-qlay)" — `SwashModule1.ftn90:647-649`. [10-15 대조 정정]
축소 압력계는 아래쪽 qlay개 층의 압력 자유도를 줄인다. (`swashuse PDF p.93`; `src/SwashExpLay1DHflow.ftn90:2454–2458`). [10-15 대조 정정]
풀이 뒤 코드는 `k=qmax+1`부터 kmax까지의 압력 보정을 `k=qmax`의 값으로 채운다. (`src/SwashExpLay1DHflow.ftn90:2454–2458` `dq(:,k) = dq(:,qmax)`). [10-15 대조 정정]

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

분기 A — **hydrostatic (`ihydro==0`)**: 정수압 경로는 바닥 계면 `k=kmax`의 상대 연직속도를 0으로 둔다. (`src/SwashExpLay1DHflow.ftn90:2982` `wom(:,kmax) = 0.`). [10-15 대조 정정]
코드는 k를 감소시키며 바닥에서 자유수면으로 상대 연직속도를 복원한다. (`src/SwashExpLay1DHflow.ftn90:2984` `do k = kmax-1, 0, -1`). [10-15 대조 정정]
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

## 10. 관련 구현 [10-15 전수 검증 정정]
- `bicgstab`·`tridiag`·`iluds`·`iludr`·`ilu`는 `SwashSolvers.ftn90`에 구현되어 있다 (`src/SwashSolvers.ftn90:3312,4297,3050,2694,2258`). [선형 솔버 노트](swash-linear-solvers.md)는 각 구현을 설명한다. [10-15 전수 검증 정정]
- Keller-box는 층 아래쪽으로 교대 부호 계수를 확장한다. (`src/SwashExpLayUflow.ftn90:1999–2000,2010–2011`). [10-15 대조 정정]
- 표준 배치는 인접 층 두께 합을 사용한다. (`src/SwashExpLayUflow.ftn90:2059–2060`). [10-15 대조 정정]
- 두 배치 모두 최상층 압력 계수를 별도 수정한다. (`src/SwashExpLayUflow.ftn90:2023,2071–2072`). [10-15 대조 정정]
- P2DH는 2DH subgrid 유동을 계산한다 (`src/SwashExpLayP2DHflow.ftn90:56–57,92–95`). 단일 압력층의 수평 압력경사는 `gmatu0`와 `gmatv0`에 조립한다 (`src/SwashExpLayP2DHflow.ftn90:928,944–947,3488–3491`). [10-15 전수 검증 정정]

## 문서와 코드 차이 (10-15 대조)

결론과 원문 인용은 [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론), [outputs](../../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론)의 최종본에서 옮겼다.
swashuse의 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경). 코드 판: VERNUM 12.01(공개 저장소 main `a486d5f`, 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| inputs-physics-numerics:SI2-280 | 층 CFL·증가 지연과 연직 기본값 대조 | `swashuse PDF p.99`는 격자점별 Courant 수의 최대값을 사용한다고 설명한다. `swashuse PDF p.101`은 thetau·thetaw·thetat의 기본값을 모두 0.5로 명시한다. | `src/SwashExpLay1DHflow.ftn90:3097–3100`: `dep = 0.5 * ( s1(nm) + dps(nm) + s1(nmu) + dps(nmu) )` / `!` / `cfl = rdx * dt * ( sqrt(grav*dep) + maxval(abs(u1(nm,:))) )` / `if ( cfl > cflmax ) cflmax = cfl`; `src/SwashInit.ftn90:416–418`: `pnums(31) = 0.5` / `pnums(32) = 0.5` / `pnums(33) = 0.5`; `swashuse PDF p.101`: `Default: [thetau] = 0.5`, `Default: [thetaw] = 0.5`, `Default: [thetat] = 0.5`. 시간 간격 증가 지연의 원문은 SI2-261의 `src/SwashMain.ftn90:285–291`이다. | C 문서 누락 | 세 연직 theta의 기본값 0.5는 p.101과 코드가 일치한다. C는 p.99에 없는 다층 유속의 maxval 계산과 SI2-261의 20단계 증가 지연으로 한정한다. 기본값 설명이 없는 것으로 분류하지 않는다. [10-15 결론 검증 정정] |
| outputs:SO1-300 | 층별 압력의 정의 위치 | `swashuse PDF p.116`은 PRESSK·NHPRSK를 per layer로 적는다. `swashuse PDF p.136–137`과 Figure 5.2는 STANDARD의 셀 중심·BOX의 층 경계 배치를 구분한다.; `src/SwashReadInput.ftn90:1502–1508`에서 BOX는 ihydro=1, STANDARD는 ihydro=2이다. `src/SwashExpLay1DHflow.ftn90:514–516·596–598`은 두 위치를 명시한다. `src/SwashQuanOutp.ftn90:931–937`은 q 또는 qv를 출력 슬롯에 복사한다. `src/SwashQuanOutp.ftn90:2234–2243·2281`의 PRESSK 정수압항은 층 경계 z_k를 사용한다. | `src/SwashHydroLoads.ftn90:305` `! note: q is defined at layer interface`; `src/SwashHydroLoads.ftn90:306–309` `if ( k == 1 ) then` / `qd = 0.` / `else` / `qd = q(nm,k-1)`; `src/SwashQuanOutp.ftn90:2281` `oparrk(:,k,14) = 0.01 * rhow * ( grav * ( oparr(:,2) - oparrk(:,k,2) ) + oparrk(:,k,13) )` | C 문서 누락 | 압력 슬롯 k를 항상 층 k의 아래 경계라고 단정한 결론을 철회한다. BOX의 q는 층 아래 경계에 있지만 STANDARD의 q는 셀 중심에 있다. `lsubg`가 거짓이면 NHPRSK는 이 q를 사용한다. PRESSK의 정수압항은 층 경계 z_k로 계산한다. C는 p.116의 출력 정의가 이 배치·합성 관계를 구체적으로 설명하지 않는 데 한정한다. `k=1`은 최상층이다. [10-15 결론 검증 정정] |
| theory-framework:ST1-301 | 층별 바람 응력의 위치 | `swashtech PDF p.63–64`는 수심 적분 바람 항을 적는다. 층 인덱스 없음. | `src/SwashExpLay1DHflow.ftn90:890` `! compute explicit part of wind stress term at internal u-point (top layer only), if appropriate`; `src/SwashExpLay1DHflow.ftn90:900` `rhsu(nm,1) = rhsu(nm,1) + windu(nm)/max(1.e-3,hkum(nm,1))`; `src/SwashImpLay1DHflow.ftn90:1071` `! compute explicit part of wind stress term at internal u-point (top layer only), if appropriate`; `src/SwashImpLay1DHflow.ftn90:1081` `rhsu(nm,1) = rhsu(nm,1) + windu(nm)/max(1.e-3,hkum(nm,1))`; `src/SwashExpLay2DHflow.ftn90:1366` `! compute explicit part of wind stress term at internal u-point (top layer only), if appropriate`; `src/SwashExpLay2DHflow.ftn90:1377` `rhsu(nm,1) = rhsu(nm,1) + windu(nm)/max(1.e-3,hkum(nm,1))`; `src/SwashImpLay2DHflow.ftn90:1562` `! compute explicit part of wind stress term at internal u-point (top layer only), if appropriate`; `src/SwashImpLay2DHflow.ftn90:1573` `rhsu(nm,1) = rhsu(nm,1) + windu(nm)/max(1.e-3,hkum(nm,1))`; 각 파일 `src/SwashExpLay1DHflow.ftn90:892`·`src/SwashImpLay1DHflow.ftn90:1073`·`src/SwashExpLay2DHflow.ftn90:1368`·`src/SwashImpLay2DHflow.ftn90:1564`의 바깥 조건은 `if ( iwind /= 0 ) then`이다. 안쪽 젖은 점 검사는 각각 `wetu(nm) == 1` 또는 `uwetp(nm) == 1`이다. WIND 입력과 실제 응력 호출은 ST1-295·293에 연결한다. | C 문서 누락 | C는 `swashtech PDF p.63–64`에 없는 층 인덱스와 가속도 분모이다. 네 층별 경로 모두 인덱스 1을 최상층으로 사용한다. 바람이 활성이고 해당 유속점이 젖었을 때 최상층에만 응력을 더한다. 분모는 최상층 두께에 `1.e-3` 하한을 적용한 값이다. [10-15 결론 검증 보완] |
| theory-framework:ST1-302 | 최하층 바닥 마찰 | `swashtech PDF p.63` 식 (3.2)는 수심 적분 마찰만 적는다. 층별 벽법칙 없음. `swashuse PDF p.76–77`은 다층 계산의 LOGLAW 선택을 설명한다. | `src/SwashExpLay1DHflow.ftn90:926–930` `! compute bottom friction (bottom layer only), if appropriate`<br>`!`<br>`if ( irough == 4 ) then`<br>`!`<br>`! logarithmic wall-law`; `src/SwashExpLay1DHflow.ftn90:941` `amatu(nm,kmax,1) = amatu(nm,kmax,1) + 0.5 * ( logfrc(nm,1) + logfrc(nmu,1) ) / hkum(nm,kmax)`; `src/SwashReadInput.ftn90:789–790` `else if ( KEYWIS('LOG') ) then`<br>`irough = 4`; `src/SwashExpLay1DHflow.ftn90:939` `if ( wetu(nm) == 1 ) then`. | C 문서 누락 | C는 `swashtech PDF p.63`에 없는 최하층 인덱스와 행렬 적용식이다. LOGLAW 선택 자체는 사용자 설명서에 있다. 선택된 로그 벽법칙은 젖은 점에서 최하층 `kmax`의 대각항에 인용 계수를 더한다. [10-15 결론 검증 보완] |
| theory-framework:ST1-303 | 층별 플럭스 합과 수심 평균 유속 | `swashtech PDF p.63`은 `\mathbf q=h\mathbf u`를 적는다. 층별 합 절차 없음. | `src/SwashExpLay1DHflow.ftn90:2621–2625` `do k = 1, kmax`<br>`!`<br>`work(nm,1) = work(nm,1) + qx(nm,k)`<br>`!`<br>`enddo`; `src/SwashExpLay1DHflow.ftn90:2631` `! compute the depth-averaged u-velocity`; `src/SwashExpLay1DHflow.ftn90:2643` `udep(nm) = work(nm,1) / hu(nm)`; 같은 파일 `src/SwashExpLay1DHflow.ftn90:2619,2641` `if ( wetu(nm) == 1 ) then`; `src/SwashExpLay1DHflow.ftn90:2633` `if ( j == jhk ) then`. | C 문서 누락 | 젖은 면의 층별 체적 플럭스를 최상층 1부터 최하층 kmax까지 합한다. `j == jhk`인 단계에서 전체 플럭스를 면 수심으로 나눠 수심 평균 유속을 저장한다. C는 `swashtech PDF p.63`에 없는 층 합과 저장 단계이다. [10-15 결론 검증 보완] |
| theory-framework:ST1-334 | 최상층 압력 경계면의 방향 | `source-analysis/swash-explicit-layered-flow.md:97` `표층`과 `bottom-face 계수 제거`. | `src/SwashExpLay1DHflow.ftn90:531–537` `fac1 = zks(nmu,k-1) - zks(nm,k-1)`<br>`fac2 = zks(nmu,k  ) - zks(nm,k  )`<br>`!`<br>`gmatu(nm,k,1) = (-hks(nm ,k) - fac1) * fac`<br>`gmatu(nm,k,2) = (-hks(nm ,k) + fac2) * fac`<br>`gmatu(nm,k,3) = ( hks(nmu,k) - fac1) * fac`<br>`gmatu(nm,k,4) = ( hks(nmu,k) + fac2) * fac`; `src/SwashExpLay1DHflow.ftn90:574–575` `gmatu(nm,1,1) = 0.`<br>`gmatu(nm,1,3) = 0.` | B 문서 오기 | 최상층 1에서 위쪽 자유수면 경계면의 압력 계수 1·3을 0으로 만든다. 아래쪽 경계면 계수 2·4를 없애는 처리가 아니다. `8756667:src/SwashExpLay1DHflow.ftn90:519–525,562–563`에도 위쪽 `k-1`과 계수 1·3의 영 대입이 있다. 현재 531–537·574–575행까지 같은 방향을 유지한다. [git 판정 AD §3](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)대로 판 차이가 아니라 현재 노트의 B이다. 층 정의는 ST1-328과 같다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| theory-unstructured:ST2-208 | 제8장 3차원 천수식 본문 | `swashtech PDF p.109`: `This chapter is yet empty.`; `swashuse PDF p.40`: `With this optional command the user indicates that the run will be in multi-layered mode and controls the distribution of vertical layers.` | `src/SwashCompUFlow.ftn90:90` `! solve (non-hydrostatic) layer-averaged shallow water equations with a fix number of layers`; `src/SwashCompUFlow.ftn90:96` `call SwashExpLayUflow`; `src/SwashCompUFlow.ftn90:102` `call SwashImpLayUflow` | C 문서 누락 | 해석: C는 swashtech 제8장 p.109의 빈 본문에 한정한다. `swashuse PDF p.40`에는 다층 모드와 수직 층 분포 명령이 있다. `SwashCompUFlow`에는 층 수와 시간 방법에 따른 다층 유동 호출이 있다. 제8장의 빈 본문을 다층 구현 부재로 해석하지 않는다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-384 | 층별 질량 플럭스·수위 경사 | `swashuse PDF p.40`은 다층 배치를 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 아래 비구조 층 플럭스·수위 경사식이 없다. | `src/SwashExpLayUflow.ftn90:280` `quf(icell,k,jf) = rsgn * lf * hku(iface,k) * u0(iface,k)`; `src/SwashExpLayUflow.ftn90:601` `hf = 0.5 * ( hks(icelll,k) + hks(icellr,k) )`; `src/SwashExpLayUflow.ftn90:605` `rhsu(iface,k) = rhsu(iface,k) - grav * rdx * hf * ( s0(icellr) - s0(icelll) ) / hkum(iface,k)` | C 문서 누락 | 질량 플럭스는 hku를 사용한다. hku는 기본 상류 수심과 선택한 보정에서 만든다. 중심 수심 선택도 있으므로 항상 순수 상류 두께라고 부르지 않는다(ST2-353·354·382). 수위 경사는 양쪽 셀 층 두께의 산술 평균을 사용한다. 운동량 분모는 가중 면 두께다. [10-15 결론 검증 정정] |
| theory-unstructured:ST2-385 | 바람은 최상층·마찰은 최하층 | `swashuse PDF p.74`는 다층의 표면 유속을 바람 응력에 쓴다고 설명한다. `swashuse PDF p.76–78`은 바닥 마찰을 설명한다. `swashtech PDF p.109`에는 아래 층별 행렬 대입식이 없다. | `src/SwashExpLayUflow.ftn90:1060` `! compute explicit part of wind stress term (top layer only), if appropriate`; `src/SwashExpLayUflow.ftn90:1068` `rhsu(iface,1) = rhsu(iface,1) + windu(iface) / hkum(iface,1)`; `src/SwashExpLayUflow.ftn90:1084` `amatu(iface,1,1) = amatu(iface,1,1) + cwndu(iface) / hkum(iface,1)`; `src/SwashExpLayUflow.ftn90:1092` `! compute bottom friction term (bottom layer only), if appropriate`; `src/SwashExpLayUflow.ftn90:1125` `amatu(iface,kmax,1) = amatu(iface,kmax,1) + fac / hkum(iface,kmax)`; 반음해 대응 `src/SwashImpLayUflow.ftn90:1060,1068,1084,1092,1125`의 원문도 같다. | C 문서 누락 | 명시적 다층 파일과 반음해 다층 파일 모두 주석과 첨자가 같은 층 방향을 가리킨다. 바닥 마찰의 층을 `k=1`로 바꾸어 쓰지 않는다. C는 바람·마찰을 적용하는 층별 우변·대각 계수의 식에 한정한다. [10-15 결론 검증 보완] [10-15 전수 검증 정정] |
| theory-unstructured:ST2-387 | 연직 이류의 중심·상류·제한자 선택 | `swashuse PDF p.94–97`은 연직 이류의 중심·상류·제한자 선택을 설명한다. `swashuse PDF p.100–101`은 연직 항의 음해 처리를 설명한다. `swashtech PDF p.109`에는 층별 행렬식이 없다. | `src/SwashExpLayUflow.ftn90:1386–1387` `if ( k == 1    ) kwd = 0.`, `if ( k == kmax ) kwu = 0.`; `src/SwashExpLayUflow.ftn90:1404` `if ( propsc == 3 .and. kappa == 1. ) then`; `src/SwashExpLayUflow.ftn90:1425–1430` `ctrkt = kwd * ctrkt / ( hkum(iface,kd) + hkum(iface,k ) )`, `ctrkb = kwu * ctrkb / ( hkum(iface,k ) + hkum(iface,ku) )`, `!`, `amatu(iface,k,1) = amatu(iface,k,1) - ctrkt + ctrkb`, `amatu(iface,k,2) =  ctrkt`, `amatu(iface,k,3) = -ctrkb`; `src/SwashExpLayUflow.ftn90:1456–1458` `amatu(iface,k,1) = amatu(iface,k,1) - ctrkt + ctrkb + max(ctrkt,0.) - min(ctrkb,0.)`, `amatu(iface,k,2) =  min(ctrkt,0.)`, `amatu(iface,k,3) = -max(ctrkb,0.)`; `src/SwashExpLayUflow.ftn90:1469` `rhsu(iface,k) = rhsu(iface,k) - 0.5 * ctrkt * fluxlim(grad1,grad2)`; `src/SwashReadInput.ftn90:2087–2091`은 연직 UMOM 선택을 pnums(36:39)에 저장한다. `src/SwashExpLayUflow.ftn90:1372–1375`는 이를 propsc·kappa·mbound·phieby로 읽는다. | C 문서 누락 | 코드는 계면 상대 연직속도를 양쪽 셀에서 길이로 가중한다. 중심 선택은 양쪽 층 두께 합으로 나눈다. 상류 선택은 자기 층 두께로 나눈다. 상류 선택의 고차 부분은 우변 제한자 보정으로 더한다. C는 비구조 층 두께와 상대 연직속도를 결합하는 행렬·우변 계수에 한정한다. [10-15 결론 검증 보완] [10-15 전수 검증 정정] |
| theory-unstructured:ST2-388 | 연직 점성의 삼중대각 계수 | `swashuse PDF p.78–80·100–101`은 연직 난류 점성과 음해 적분을 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 아래 층 경계의 삼중대각 계수식이 없다. | `src/SwashExpLayUflow.ftn90:1502` `if ( iturb < 2 ) then`; `src/SwashExpLayUflow.ftn90:1521–1526` `ctrkt = 2.* ctrkt / ( hkum(iface,k)*( hkum(iface,kd) + hkum(iface,k ) ) )`, `ctrkb = 2.* ctrkb / ( hkum(iface,k)*( hkum(iface,k ) + hkum(iface,ku) ) )`, `!`, `amatu(iface,k,1) = amatu(iface,k,1) + kwd*ctrkt + (2.*kwu-1.)*ctrkb`, `amatu(iface,k,2) = amatu(iface,k,2) - kwd*ctrkt +    (1.-kwu)*ctrkb`, `amatu(iface,k,3) = amatu(iface,k,3) -                     kwu*ctrkb` | C 문서 누락 | 점성 입력은 계면 점성의 셀 간 가중 평균이다. 최상층과 최하층의 계수는 `kwd,kwu`로 바뀐다. 계수의 부호를 연직 첨자 이름만으로 해석하지 않는다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-389 | 층별 수평속도의 직접 삼중대각 풀이 | `swashuse PDF p.100–101`은 연직 운동량의 theta 방법을 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 아래 소거·후진 대입·시간 가중값 환산 절차가 없다. | `src/SwashExpLayUflow.ftn90:1552–1555` `bi = 1./(amatu(iface,k,1) - amatu(iface,k,2)*amatu(iface,k-1,3))`, `amatu(iface,k,1) = bi`, `amatu(iface,k,3) = amatu(iface,k,3)*bi`, `rhsu (iface,k  ) = (rhsu(iface,k) - amatu(iface,k,2)*rhsu(iface,k-1))*bi`; `src/SwashExpLayUflow.ftn90:1559–1562` `u1(iface,kmax) = rhsu(iface,kmax)`, `do k = kmax-1, 1, -1`, `u1(iface,k) = rhsu(iface,k) - amatu(iface,k,3)*u1(iface,k+1)`, `enddo`; `src/SwashExpLayUflow.ftn90:1580` `u1(iface,k) = ( u1(iface,k) - (1.-thetau) * u0(iface,k) ) / thetau` | C 문서 누락 | 전진 소거는 위층에서 아래층으로 진행한다. 후진 대입은 최하층에서 위층으로 진행한다. `thetau`가 1이 아니면 시간 가중값을 실제 새 속도로 환산한다. 이 루프는 전역 SIP 호출이 아니다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-390 | Keller-box의 수평 압력·계면 경사 | `swashuse PDF p.90`은 Keller-box 기법을 설명한다. `swashuse PDF p.136–137`은 BOX의 계면 압력 배치를 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 아래 삼각 격자의 수평 압력 계수식이 없다. | `src/SwashExpLayUflow.ftn90:649` `! Keller-box scheme, so non-hydrostatic pressure is located at the centers of layer interfaces`; `src/SwashExpLayUflow.ftn90:666–674` `fac = rdx / hkum(iface,k)`, `!`, `fac1 = zks(icellr,k-1) - zks(icelll,k-1)`, `fac2 = zks(icellr,k  ) - zks(icelll,k  )`, `!`, `gmatu(iface,k,1) = (-0.5 * hks(icelll,k) -     finp  * fac1) * fac`, `gmatu(iface,k,2) = (-0.5 * hks(icelll,k) +     finp  * fac2) * fac`, `gmatu(iface,k,3) = ( 0.5 * hks(icellr,k) - (1.-finp) * fac1) * fac`, `gmatu(iface,k,4) = ( 0.5 * hks(icellr,k) + (1.-finp) * fac2) * fac`; `src/SwashReadInput.ftn90:1499–1504`의 NONHYDROSTATIC BOX·KELLER 선택은 ihydro=1을 설정한다. | C 문서 누락 | 층 두께를 곱한 압력 차와 계면 경사의 반력을 한 계수 배열에 합친다. 이 식의 `k-1` 계면은 위쪽이다. `k` 계면은 아래쪽이다. C는 압력 배치 자체가 아니라 두 셀의 층 두께·계면 경사를 결합하는 gmatu 계수에 한정한다. [10-15 결론 검증 보완] [10-15 전수 검증 보완] |
| theory-unstructured:ST2-391 | 표준 압력 배치의 수평 계수 | `swashuse PDF p.90`은 STANDARD의 중앙차분을 설명한다. `swashuse PDF p.136–137`은 STANDARD의 셀 중심 압력 배치를 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 아래 비구조 수평 압력 계수식이 없다. | `src/SwashExpLayUflow.ftn90:726` `! central differences, so non-hydrostatic pressure is located at the cell centers`; `src/SwashExpLayUflow.ftn90:746–754` `fac1 = rdx * ( zks(icellr,k-1) - zks(icelll,k-1) ) / ( hkum(iface,kd) + hkum(iface,k ) )`, `fac2 = rdx * ( zks(icellr,k  ) - zks(icelll,k  ) ) / ( hkum(iface,k ) + hkum(iface,ku) )`, `!`, `gmatu(iface,k,1) = -    finp  * fac1`, `gmatu(iface,k,3) = -(1.-finp) * fac1`, `gmatu(iface,k,2) = ( -rdx*hks(icelll,k) -     finp  * hkum(iface,kd)*fac1 +     finp  * hkum(iface,ku)*fac2 ) / hkum(iface,k)`, `gmatu(iface,k,4) = (  rdx*hks(icellr,k) - (1.-finp) * hkum(iface,kd)*fac1 + (1.-finp) * hkum(iface,ku)*fac2 ) / hkum(iface,k)`, `gmatu(iface,k,5) =      finp  * fac2`, `gmatu(iface,k,6) =  (1.-finp) * fac2`; `src/SwashReadInput.ftn90:1506–1508`의 STANDARD 선택은 ihydro=2를 설정한다. | C 문서 누락 | 표준 배치는 자기 층과 위·아래층 압력을 결합한다. 표면·바닥의 계수 접기는 `src/SwashExpLayUflow.ftn90:788–798`에서 별도로 수행한다. C는 gmatu의 층 결합과 경계 계수 접기에 한정한다. [10-15 결론 검증 보완] [10-15 전수 검증 보완] |
| theory-unstructured:ST2-392 | 연직 압력 경사·표면 압력 처리 | `swashuse PDF p.90`은 두 연직 압력경사 이산화 방법을 설명한다. `swashuse PDF p.136–137`은 두 압력 배치를 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 아래 교대 부호 계수와 자유수면 계수 접기가 없다. | `src/SwashExpLayUflow.ftn90:1999–2000` `gmatw(icell,:,1) =  2./hks(icell,:)`, `gmatw(icell,:,2) = -gmatw(icell,:,1)`; `src/SwashExpLayUflow.ftn90:2010–2011` `gmatw(icell,k-1,2*j+1) =  2.*fac/hks(icell,j+k-1)`, `gmatw(icell,k-1,2*j+2) = -gmatw(icell,k-1,2*j+1)`; `src/SwashExpLayUflow.ftn90:2023` `gmatw(icell,1,1) = 0.`; 표준 배치 `src/SwashExpLayUflow.ftn90:2059–2060` `gmatw(icell,k,1) =  2./(hks(icell,kd) + hks(icell,k))`, `gmatw(icell,k,2) = -gmatw(icell,k,1)`; `src/SwashExpLayUflow.ftn90:2071–2072` `gmatw(icell,1,2) = gmatw(icell,1,2) - gmatw(icell,1,1)`, `gmatw(icell,1,1) = 0.` | C 문서 누락 | Keller-box는 층 아래쪽으로 교대 부호 계수를 확장한다. 표준 배치는 인접 층 두께 합을 사용한다. 두 배치 모두 최상층 압력 계수를 별도 수정한다. [10-15 결론 검증 보완] [10-15 전수 검증 보완] |
| theory-unstructured:ST2-393 | 압력 보정 풀이·수평속도 보정 | `swashuse PDF p.91–93`은 BiCGSTAB와 압력 보정·PROJECTION 선택을 설명한다. `swashtech PDF p.111`은 준비 중이다. | `src/SwashExpLayUflow.ftn90:2450` `call bicgstab3 ( amatp(1:ncells,1:qmax,0:nconct), rhsp(1:ncells,1:qmax), dq(1:ncells,1:qmax) )`; `src/SwashExpLayUflow.ftn90:2465–2469` `if ( iproj == 1 ) then`, `q = q + dq`, `else if ( iproj == 2 ) then`, `q = dq`, `endif`; `src/SwashExpLayUflow.ftn90:2493–2494` `u1(iface,k) = u1(iface,k) - dt*theta * ( gmatu(iface,k,1)*dq(icelll,kd) + gmatu(iface,k,2)*dq(icelll,k ) + gmatu(iface,k,3)*dq(icellr,kd)  &`<br>`+ gmatu(iface,k,4)*dq(icellr,k ) + gmatu(iface,k,5)*dq(icelll,ku) + gmatu(iface,k,6)*dq(icellr,ku) )`; 반음해 `src/SwashImpLayUflow.ftn90:2785` `call bicgstab3 ( amatp(1:ncells,1:qmax,0:nconct), rhsp(1:ncells,1:qmax), dq(1:ncells,1:qmax) )`; `src/SwashReadInput.ftn90:1566–1567`의 PROJECTION은 iproj=2를 설정한다. `src/SwashCheckPrep.ftn90:630–635`의 자동 선택은 부유체가 없으면 iproj=1, 있으면 iproj=2다. | C 문서 누락 | 두 시간 방법의 다층 압력은 `bicgstab3`를 사용한다. `iproj=1`은 보정을 기존 압력에 더한다. `iproj=2`는 보정값으로 압력을 대체한다. C는 압력 갱신의 내부 대입과 비구조 수평속도 보정 계수에 한정한다. 해법·PROJECTION 선택 자체의 문서 누락으로 분류하지 않는다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-394 | 바닥 연직속도·연직 운동량 풀이 | `swashtech PDF p.109`에는 바닥 운동학 조건의 다층 구현이 없다. `swashuse PDF p.40·90·100–101`은 다층·비정수압·음해 연직 적분을 설명한다. | `src/SwashExpLayUflow.ftn90:1659–1660` `w1(icell,kmax) = w1(icell,kmax) + rsgn * lf * zku(iface,kmax) * ( nx * (2.*uvc(icell,kmax,1)-uvc(icell,kmax-1,1)) + &`<br>`ny * (2.*uvc(icell,kmax,2)-uvc(icell,kmax-1,2)) )`; `src/SwashExpLayUflow.ftn90:1666` `w1(icell,kmax) = w1(icell,kmax) / area`; `src/SwashExpLayUflow.ftn90:2144–2147` `bi = 1./(amatw(icell,k,1) - amatw(icell,k,2)*amatw(icell,k-1,3))`, `amatw(icell,k,1) = bi`, `amatw(icell,k,3) = amatw(icell,k,3)*bi`, `rhsw (icell,k  ) = (rhsw(icell,k) - amatw(icell,k,2)*rhsw(icell,k-1))*bi`; `src/SwashExpLayUflow.ftn90:2153` `w1(icell,k) = rhsw(icell,k) - amatw(icell,k,3)*w1(icell,k+1)`; `src/SwashExpLayUflow.ftn90:2168` `w1(icell,k) = ( w1(icell,k) - (1.-thetaw) * w0(icell,k) ) / thetaw` | C 문서 누락 | 바닥 계면은 `kmax`다. 바닥 연직속도는 최하층과 그 위층의 수평속도를 외삽하여 만든다. 코드는 계면 연직속도의 삼중대각계를 직접 푼다. C는 최하층과 그 위층 속도의 외삽 및 삼중대각 풀이 계수에 한정한다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-395 | 정수압·비정수압의 상대 연직속도 | `swashtech PDF p.109`에는 움직이는 계면에 대한 상대 연직속도식이 없다. `swashuse PDF p.40·90·100–101`의 다층 설명에도 아래 복원과 잔차 처리식은 없다. | `src/SwashExpLayUflow.ftn90:2909` `wom(:,kmax) = 0.`; `src/SwashExpLayUflow.ftn90:2950` `wom(icell,k) = wom(icell,k+1) - qf / area - ( hksnew(icell,k+1) - hks(icell,k+1) ) / dt`; `src/SwashExpLayUflow.ftn90:2966` `if ( abs(wom(icell,0)) > epswom ) then`; `src/SwashExpLayUflow.ftn90:2971` `wom(icell,0) = 0.`; `src/SwashExpLayUflow.ftn90:3024` `wom(icell,k) = w1(icell,k) - qf / area - ( zksnew(icell,k) - zks(icell,k) ) / dt`; `src/SwashExpLayUflow.ftn90:3028–3029` `wom(icell,0   ) = 0.`, `wom(icell,kmax) = 0.`; `src/SwashExpLayUflow.ftn90:2907–2911,2966–2974,2977–2983,3024–3029`의 정수압·비정수압 분기. | C 문서 누락 | 정수압 경로는 바닥 상대속도를 0으로 두고 바닥에서 위쪽으로 복원한다. 표면 상대속도는 `if ( abs(wom(icell,0)) > epswom ) then` 안에서만 0으로 다시 설정한다. 따라서 그 문턱 이하 잔차까지 무조건 0으로 만든다는 결론은 틀리다. 비정수압의 젖은 셀 경로는 실제 연직속도에서 계면 경사 이송과 계면 이동속도를 뺀다. 그 경로는 표면·바닥 값을 0으로 둔다. 정수압 복원 방향의 노트 오기는 ST2-428이다. [10-15 결론 검증 정정] |
| theory-unstructured:ST2-396 | 층 플럭스 합과 수심 평균 속도 | `swashuse PDF p.40·100`은 다층과 시간 가중 적분을 설명한다. `swashtech PDF p.109` 및 사용설명서의 해당 설명에는 비구조 면의 층 플럭스 합과 평균 속도의 아래 대입식이 없다. | `src/SwashExpLayUflow.ftn90:2628` `qn(iface,k) = lf * hku(iface,k) * u1(iface,k)`; `src/SwashExpLayUflow.ftn90:2644` `uwrk(iface) = uwrk(iface) + qn(iface,k)`; `src/SwashExpLayUflow.ftn90:2664` `udep(iface) = uwrk(iface) / ( lf * hu(iface) )`; `src/SwashExpLayUflow.ftn90:2713` `s1(icell) = s0(icell) - fh * dt * qf / area`; `src/SwashImpLayUflow.ftn90:2940–2942` `u = theta*u1(iface,k) + (1.-theta)*u0(iface,k)`, `!`, `qn(iface,k) = lf * hku(iface,k) * u`; `src/SwashImpLayUflow.ftn90:2958` `udep(iface) = udep(iface) + hku(iface,k) * u1(iface,k)`; `src/SwashImpLayUflow.ftn90:2962` `udep(iface) = udep(iface) / hu(iface)` | C 문서 누락 | 명시적 수위식은 층 플럭스를 합한다. 반음해 플럭스는 이전·새 층 속도의 시간 가중값을 사용한다. 출력·다음 처리용 수심 평균 속도는 새 층 속도로 계산한다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-428 | 정수압 상대속도 복원 방향 | models/SWASH/source-analysis/swash-explicit-layered-flow.md:158 ``분기 A — **hydrostatic (ihydro==0)**: 층별 연속방정식에서 표면→바닥으로 적분 복원 `:2982-3008`:`` | `src/SwashExpLay1DHflow.ftn90:2982` `wom(:,kmax) = 0.`; `src/SwashExpLay1DHflow.ftn90:2984` `do k = kmax-1, 0, -1`; 비구조 대응 `src/SwashExpLayUflow.ftn90:2909` `wom(:,kmax) = 0.`; `src/SwashExpLayUflow.ftn90:2911` `do k = kmax-1, 0, -1` | B 문서 오기 | 정수압 경로는 바닥 계면 `k=kmax`의 상대 연직속도를 0으로 둔다. 코드는 k를 감소시키며 바닥에서 자유수면으로 상대 연직속도를 복원한다. 같은 방향의 비구조 상대속도 계산은 ST2-395와 같다. [SWASH-git-verify-AD.md §3 ST2-428](../../../_staging/recovery/compare/SWASH-git-verify-AD.md). `8756667 2022-09-03 initial release`의 `src/SwashExpLay1DHflow.ftn90:2422,2424`에 같은 바닥값과 감소 반복문이 있다. `7949227`과 main에도 같다. 표면에서 바닥으로 복원하던 과거 구현의 변경이 아니므로 B를 유지한다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| theory-unstructured:ST2-429 | 축소 압력계의 위층·아래층 | models/SWASH/source-analysis/swash-explicit-layered-flow.md:132 ``상위 `qlay`개 layer 압력을 동일 처리해 Poisson 차수를 줄임`` | `src/SwashExpLay1DHflow.ftn90:2454–2458` `do k = qmax+1, kmax`, `!`, `dq(:,k) = dq(:,qmax)`, `!`, `enddo`; `src/SwashExpLayUflow.ftn90:2027` `! to reduce the pressure Poisson equation set pressure of bottom face to that of top face for a number of layers` | B 문서 오기 | 축소 압력계는 아래쪽 qlay개 층의 압력 자유도를 줄인다. 풀이 뒤 코드는 `k=qmax+1`부터 kmax까지의 압력 보정을 `k=qmax`의 값으로 채운다. `swashuse PDF p.93`의 아래층 정의와도 일치한다. 매뉴얼과 코드의 일치 판정은 ST2-397이다. [SWASH-git-verify-AD.md §3 ST2-429](../../../_staging/recovery/compare/SWASH-git-verify-AD.md). `8756667 2022-09-03 initial release`의 `src/SwashExpLay1DHflow.ftn90:2078–2080`에 같은 아래층 복사가 있다. `7949227`과 main에도 같다. 위층을 묶던 구현의 변경이 아니므로 노트 오기 B를 유지한다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
