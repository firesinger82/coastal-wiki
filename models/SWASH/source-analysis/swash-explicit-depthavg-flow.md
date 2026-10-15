---
title: "SWASH 명시적 수심평균 flow solver — ExpDep 1DH/2DH/Uflow 시간적분"
model: SWASH
component: src (explicit depth-averaged flow)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashExpDep1DHflow.ftn90 (Purpose/Method 헤더 :45-67, 시간적분·연속·CFL :199-1666), SwashExpDep2DHflow.ftn90 (헤더 :46-67, 곡선좌표 metric·SIP Poisson·CFL :1271-4977), SwashExpDepUflow.ftn90 (헤더 :42-61, 삼각망 face/cell·Euler explicit advection·BiCGSTAB :228-1807) 의 file:line 인용. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 명시적 수심평균 flow solver — ExpDep 1DH/2DH/Uflow

> 비정수압 수심평균(1-layer) 천수 방정식의 명시적(explicit) 시간적분 커널. 직교 1DH·곡선 2DH·삼각망 U 세 변종. (경로: raw/source_code/swash/src/SwashExpDep{1DH,2DH,U}flow.ftn90)

## 1. 세 파일의 정체와 공통 골격

| 파일 | subroutine | 격자 | advection 시간스킴 | Poisson solver |
|---|---|---|---|---|
| `SwashExpDep1DHflow.ftn90` | `SwashExpDep1DHflow` | 1DH 직교 (rectilinear) | MacCormack 예측-수정 | `tridiag` (삼중대각) |
| `SwashExpDep2DHflow.ftn90` | `SwashExpDep2DHflow` | 2DH 곡선좌표 (curvilinear) | MacCormack 예측-수정 | `sip` (Strongly Implicit Procedure) |
| `SwashExpDepUflow.ftn90` | `SwashExpDepUflow` | 비정형 삼각망 (unstructured) | Euler explicit + Lax-Wendroff | `bicgstabu` (BiCGSTAB) |

세 파일 모두 "non-hydrostatic, depth-averaged shallow water equations"의 시간적분을 수행한다 (1DH `SwashExpDep1DHflow.ftn90:47`, 2DH `SwashExpDep2DHflow.ftn90:48`, U `SwashExpDepUflow.ftn90:44`). 즉 **연직 1-layer**(depth-averaged) 분기로, 다층(multi-layer) 변종은 별도 `SwashExpLay*` 파일. 비정수압 압력 projection을 옵션(`ihydro == 1`)으로 포함하므로, `SwashImpDep2DHflow`(완전 암시적)와 달리 **운동량의 명시적 적분 + 압력만 암시적**인 semi-implicit 구조다.

### 공통 Method (헤더 verbatim, 1DH `:49-67`)

> The time integration with respect to the continuity equation and the water level gradient of the u-momentum equation is based on the leap-frog technique (or the Hansen scheme).
>
> The time integration with respect to the advective term is based on the predictor-corrector scheme of MacCormack, while that for the bottom friction is based on Euler implicit and for the non-hydrostatic pressure gradient a semi-implicit approach is employed (theta-scheme).
>
> The space discretization of the advective term is momentum conservative (or energy head conservative in case of flow contraction) and is approximated by either first order upwind or higher order (flux-limited) scheme (CDS, Fromm, BDF, QUICK, MUSCL, Koren, etc.). The higher order scheme is treated by defect correction consistent with the MacCormack scheme.
>
> The w-momentum equation only contains the z-gradient of the non-hydrostatic pressure and is discretized by means of the Keller-box scheme.
>
> The non-hydrostatic pressure is obtained by means of the second order accurate pressure correction technique.

2DH 헤더(`SwashExpDep2DHflow.ftn90:52-67`)는 이와 동일(단 "momentum equations" 복수). Uflow는 advection 시간스킴이 다르다(아래 §6).

각 time step 내 연산 순서는 세 파일 공통:
1. mass flux 계산
2. advection·압력경사·점성·바닥마찰·바람·식생·baroclinic 등 운동량 기여항 계산
3. 중간(intermediate) 수평속도 `u1`(2DH는 `v1`도) 명시적 갱신
4. (옵션) 고차 advection defect correction
5. 중간 연직속도 `w` 갱신 (Keller-box)
6. (`ihydro==1`) Poisson 방정식 구성·해석 → 비정수압 압력보정 `dq`
7. 압력 갱신 + 속도 보정(projection)
8. global 연속방정식으로 수위 `s1` 갱신 (예측-수정)
9. CFL 수 계산

## 2. 시간적분 스킴 (theta·leap-frog·MacCormack·Hancock)

### 2.1 implicitness 파라미터

`theta = pnums(5)` — 비정수압 압력경사 implicitness (1DH `:174`). `thetamb = pnums(71)` — global 연속식 내 ambient current implicitness (1DH `:175`).

### 2.2 운동량 명시적 갱신 + Euler-implicit 마찰

중간 속도는 모든 source항을 모은 `contrib`을 명시적으로 적분하되, 바닥마찰·식생·다공질·바람 임피던스는 분모 `denom`에 넣어 Euler implicit 처리한다 (1DH `:717-725`):

```
contrib = advec(nm) + zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm)) - visc(nm)
denom   = 1. + cvegu(nm,1,2) + cpomu(nm,1) + dt * ( cbot(nm) + cporfr + cveg + wndimp(nm) )
u1(nm)  = ( (1.+cvegu(nm,1,2)+cpomu(nm,1)) * u0(nm) - dt * contrib ) / denom
```

`cbot`(바닥마찰)·`cporfr`(다공질)·`cveg`(식생)·`wndimp`(바람)이 `dt`와 함께 분모에 들어가 implicit — 헤더의 "bottom friction is based on Euler implicit"과 일치. 2DH도 동일 구조에 Coriolis `corf(nm)`와 velocity magnitude `utot`가 추가된다 (`SwashExpDep2DHflow.ftn90:1354-1360`).

### 2.3 수위경사 (leap-frog/Hansen)

운동량의 수위경사는 직전 시각 수위 `s0`로 계산되고(1DH `:707` `zgrad = grav * rdx * (s0(nmu) - s0(nm))`), 연속식의 수위 갱신은 새 속도 `u1`로부터 나온 mass flux로 이뤄져(§4) 시차(staggered) leap-frog/Hansen 구조를 이룬다.

### 2.4 Hancock/RK3 예측-수정 (global 연속식)

`jhk` 값으로 연속식 시간정확도 선택 (1DH `:1342`, 2DH `:4332`, U `:1545`, 세 파일 verbatim 동일):

```
! (jhk = 1: RK3, jhk = 2: Hancock, jhk = 3: first order Euler)
do j = jhk, 3
```

`jhk`는 `SwashReadInput.ftn90:1887-1891`에서 입력 키워드에 따라 설정(`jhk=3` Euler / `jhk=2` Hancock / `jhk=1` RK3) — 본 flow 파일들에는 정의 없음(외부 module). 루프 내 `fh = 0.5`(예측단계 j≤2)·`fh = 1.`(수정단계 j=3)로 부분 시간전진을 한다 (1DH `:1346-1358`). 헤더 update 주석 "8.01, October 2021: Hancock scheme for global continuity equation"(`:42`)이 이 도입 시점.

초기값은 RK3이다 (`src/SwashInit.ftn90:393` `jhk        =  1     ! RK3`). [10-15 대조 정정]
선형 모드에서는 `if ( linswe ) then`에서 `jhk      = 3`을 대입한다 (`src/SwashCheckPrep.ftn90:1457–1459`). [10-15 대조 정정]
실제 연속식 단계는 최종 `jhk`를 따른다 (`src/SwashExpDep2DHflow.ftn90:4334` `do j = jhk, 3`; [theory-framework:ST1-324](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]

## 3. 공간차분 — advection (1DH/2DH MacCormack 계열)

### 3.1 1차 upwind 예측 + 고차 defect correction

advective velocity는 1차 upwind로 먼저 결정한다 (1DH `:222-251`): wl-point에서 부호로 upwind 쪽 속도 선택.

```
if ( fac > 1.0e-5 ) then
   ua(nm) = u0(nmd)        ! 흐름 +방향 → 좌측 upwind
else if ( fac < -1.0e-5 ) then
   ua(nm) = u0(nm )        ! 흐름 -방향 → 우측 upwind
```

momentum/energy-head conservative 선택은 `stricthead`(energy head)·`strictmom`(momentum) 논리로 분기 (1DH `:231`, `:272`). `linswe`(선형 SWE)일 때 advection 가중치를 0으로 두어 advection을 끈다 (1DH `:267-270`). 예측단계 advection은:

```
advec(nm) = rdx * ( fac1 * (ua(nmu) - u0(nm)) - fac2 * (ua(nm) - u0(nm)) )   ! 1DH :291
```

고차 스킴은 `propsc = nint(pnums(6))` 가 1이 아닐 때 defect correction으로 추가된다 (1DH `:742-744`). limiter 파라미터 `kappa=pnums(7)`·`mbound=pnums(8)`·`phieby=pnums(9)` (1DH `:746-748`), flux limiter는 함수 `fluxlim`. 중간속도 갱신 후 고차 보정을 빼는 방식으로 MacCormack 수정단계를 구현 (1DH `:795-833`):

```
u1(nm) = u1(nm) - dt * rdx * ( fac1 * ua(nmu)  - fac2 * ua(nm) )   ! :833
```

헤더의 "higher order scheme is treated by defect correction consistent with the MacCormack scheme"(`:60-61`)과 일치. 사용 가능 고차 스킴: CDS, Fromm, BDF, QUICK, MUSCL, Koren 등 (`:60`).

### 3.2 2DH 곡선좌표 metric

2DH는 곡선좌표 Jacobian/metric을 명시적으로 사용. `guu, guv, gvu, gvv, gsqs, gsqsu, gsqsv` 를 `m_genarr`에서 import (`SwashExpDep2DHflow.ftn90:74`). advection의 곡률(curvature) 보정항이 metric 미분으로 들어간다 (예: u-momentum `:578-580`):

```
if ( advecx(nm) /= 0. ) advecx(nm) = advecx(nm) + 0.5 * u0(nm) * v * ( gvv(nm) + gvv(nmu) - gvv(ndm) - gvv(ndmu) ) / gsqsu(nm)
if ( advecy(nm) /= 0. ) advecy(nm) = advecy(nm) - 0.5 * v * v * ( guu(nmu) - guu(nmd) ) / gsqsu(nm)
```

`gsqs`는 cell-center Jacobian, `gsqsu`/`gsqsv`는 u/v-point Jacobian. 수위경사도 곡선거리로 나눈다: `zgrad = grav * (s0(nmu) - s0(nm)) / gvu(nm)` (`:1342`). u·v 두 운동량을 각각 풀며(u: `:1271-1370`, v: `:2911-`), repeating(주기) 격자 동기화 `periodic`/`SWEXCHG` 호출이 곳곳에 삽입(`:264`, `:283`, `:4434` 등 — "extension repeating grid" `:41`).

## 4. global 연속방정식 (수위 갱신)

### 4.1 1DH

mass flux `qx = hu*u1`(비선형) 또는 `dpu*u1`(linswe) 후, 수위를 발산으로 갱신 (1DH `:1368-1393`):

```
qx(nm) = hu(nm)*u1(nm)                                   ! :1368
s1(nm) = s0(nm) - fh * dt * rdx * ( qx(nm) - qx(nmd) )   ! :1393
```

경계 가상셀 복사·Riemann/water-level opening 예외(`:1404-1410`), 예측단계마다 `SwashUpdDepu(u1)`로 수심 갱신(`:1414`). 내부파 생성 시 mass source `s1 += dt*srcm` (`:1418-1426`).

### 4.2 2DH (2차원 발산, Jacobian)

x·y mass flux를 metric 폭으로 곱한 뒤 셀 Jacobian으로 나눠 발산 (`SwashExpDep2DHflow.ftn90:4359`, `:4387`, `:4418`):

```
qx(nm) = hu(nm)*guu(nm)*u1(nm)
qy(nm) = hv(nm)*gvv(nm)*v1(nm)
s1(nm) = s0(nm) - fh * dt * ( qx(nm) - qx(nmd) + qy(nm) - qy(ndm) ) / gsqs(nm)
```

`gsqs`(Jacobian)로 나눠 곡선좌표 면적 정규화. 영구 dry점 `s1(1)=0` (`:4425`).

### 4.3 Uflow (유한체적, face flux 합)

셀별로 모든 face의 mass flux를 부호 `rsgn`(face 방향) 가중 합산해 셀 면적으로 나눔 (`SwashExpDepUflow.ftn90:1596-1610`):

```
qn(iface) = lf * hu(iface) * u1(iface)        ! lf = face length, :1598
qf = qf + rsgn * qn(iface)                      ! :1600
area = cell(icell)%attr(CELLAREA)               ! :1606
s1(icell) = s0(icell) - fh * dt * qf / area     ! :1610
```

이는 삼각셀에 대한 명시적 유한체적 연속식. `rsgn`은 face가 셀의 left/right 중 어느 쪽인지로 ±1 결정 (`:1590-1594`).

## 5. 비정수압 압력 projection (depth-avg 1-layer 형태)

`ihydro == 1`일 때만 활성. 운동량의 압력경사항 `qgrad`는 theta로 가중되며 `iproj==2`(non-conservative)일 때 `(1.-theta)`배 (1DH `:387`). 압력경사 매트릭스 `gmat`은 u-point에서 구성 (1DH `:325-356`).

### 5.1 Poisson 방정식 구성·해석 — 격자별 solver 차이

핵심 차이점: **세 변종이 서로 다른 선형 solver를 사용**.

- **1DH** — 삼중대각 직접해(`tridiag`). 계수 `a,b,c`·우변 `d` 구성 후 (1DH `:1244-1257`):
  ```
  b(nm) = fac1 * gmat(nm,1) + fac2 * gmat(nmd,2) - 2./hs(nm)   ! :1248
  d(nm) = ( fac1*u1(nm) + fac2*u1(nmd) + w1top(nm) + w1bot(nm) )/(dt*theta)   ! :1250
  call tridiag ( a, b, c, d, dq, kgrpnt )   ! :1265
  ```
- **2DH** — 5-대각(`amat(nm,1..5)`) → SIP. `amat(nm,1)`은 대각, 2/3은 x-이웃, 4/5는 y-이웃 (`SwashExpDep2DHflow.ftn90:4054-4072`):
  ```
  amat(nm,1) = amat(nm,1) - 2.*gsqs(nm) / hs(nm)   ! :4071
  rhs(nm)    = rhs(nm)/(dt*theta)                    ! :4074
  call sip( amat, rhs, dq )                          ! :4092
  ```
- **Uflow** — 셀당 대각 `amat(icell,0)` + 인접 face 3개 `amat(icell,1:3)` → BiCGSTAB (`SwashExpDepUflow.ftn90:1365-1432`):
  ```
  amat(icell,0) = -2.*area / (hs(icell)*hs(icell))   ! :1365
  rhs (icell  ) = area * ( w1top(icell) + w1bot(icell) ) / hs(icell)   ! :1366
  call bicgstabu ( amat, rhs, dq )                    ! :1440
  ```

우변의 `-2./hs`(1DH) / `-2.*gsqs/hs`(2DH) / `-2.*area/hs²`(U) 항은 1-layer Keller-box 압력 닫힘에서 오는 연직 항으로, 다층 변종과 구분되는 depth-averaged 특유의 형태.

### 5.2 압력 갱신·속도 projection

`iproj==1`이면 압력 증분(`q=q+dq`), `iproj==2`이면 치환(`q=dq`) (1DH `:1278-1282`, 2DH `:4105-4109`). projection으로 속도를 보정 (1DH `:1300`):

```
u1(nm) = u1(nm) - dt*theta*( gmat(nm,1) * dq(nm) + gmat(nm,2) * dq(nmu) )
```

w-velocity는 Keller-box 관계로 갱신 (1DH `:1317-1319`): `w1top(nm) = w1top(nm) + w1bot(nm) + 2.*dt*theta*dq(nm)/hs(nm)`.

## 6. Uflow의 차별점 — 삼각망 유한체적

Uflow는 구조화 두 파일과 알고리즘이 상당히 다르다.

### 6.1 advection 시간스킴 = Euler explicit (MacCormack 아님)

헤더 verbatim (`SwashExpDepUflow.ftn90:51-56`):

> The time integration with respect to the advective term is based on Euler explicit, while that for the bottom friction is based on Euler implicit.
>
> The space discretization of the advective term is momentum conservative and is approximated by first order upwind or higher order (flux-limited) scheme (CDS, Fromm, BDF, QUICK, MUSCL, Koren, etc.). The r-ratio formulation based on most upwave vertex is employed.

즉 1DH/2DH가 MacCormack 예측-수정인 데 비해 Uflow advection은 단순 Euler explicit. 고차는 **Lax-Wendroff** 2차 보정으로 추가된다("add second order approximation based on Lax-Wendroff method" `:366`, `lwfac` Lax-Wendroff factor `:144`/`:415`). r-ratio는 most upwave vertex 기반 (`:56`, `vu` upwind vertex `:115`).

### 6.2 face-normal 속도 + circumcenter 재구성

미지수는 **face 법선속도** `u1(nfaces)` (`:91`).
이류용 `perot(u0)`는 면 법선 속도 `u0`로 셀 중심 속도 벡터를 재구성한다 (`src/SwashExpDepUflow.ftn90:226`; `src/SwashUServ.ftn90:148–157`). [10-15 대조 정정] [10-15 전수 검증 정정]
코리올리 계산은 `hu`를 곱한 면 플럭스를 따로 재구성한다 (`src/SwashExpDepUflow.ftn90:948–949`; [theory-unstructured:ST2-146](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]
1차 upwind advection은 면을 공유하는 좌/우 셀의 face flux를 upwind 셀 기준으로 합산 (`:228-346`):

```
if ( u0(ifacel) > 0. ) then
   icellu = icelll
else
   icellu = icellr
endif      ! :280-284
```

### 6.3 운동량 갱신 (face 단위, depth로 정규화)

경계 face(prescribed water level, `wlimp`)와 내부 face를 분리해 푼다 (`:969-1054`). 내부 face (`:1034-1044`):

```
zgrad   = grav * rdx * hf * ( s0(icellr) - s0(icelll) )       ! :1034
contrib = advec(iface) / humn(iface) + ( zgrad + pgrad(iface) + qgrad(iface) - windu(iface) - visc(iface) + corf(iface) ) / hum(iface)   ! :1038
denom   = 1. + dt * ( cbot(iface) + wndimp(iface) )           ! :1040
u1(iface) = ( u0(iface) - dt * contrib ) / denom               ! :1044
```

운동량 경사는 `FACEDISTC`를 사용한다 (`src/SwashExpDepUflow.ftn90:1021`). [10-15 대조 정정]
`FACEDISTC`는 계산 중심에서 면 중점까지의 두 거리 합의 역수다 (`src/SwanGridFace.ftn90:384–411`; [theory-unstructured:ST2-150](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]

## 7. CFL 수 (안정성 진단)

세 파일 모두 step 말미에 최대 CFL를 계산·MPI reduce(`SWREDUCE ... SWMAX`). 정의는 격자에 맞게 다르다:

| 변종 | CFL 식 | 인용 |
|---|---|---|
| 1DH | $\text{CFL} = \frac{\Delta t}{\Delta x}\left(\sqrt{g\,h} + |u|\right)$ | `SwashExpDep1DHflow.ftn90:1663` |
| 2DH | $\text{CFL} = \Delta t\,(\sqrt{g\,h}+|\vec u|)\sqrt{\Delta x^{-2}+\Delta y^{-2}}$ | `SwashExpDep2DHflow.ftn90:4967` |
| U | $\text{CFL} = \text{rdx}\cdot\Delta t\,(\sqrt{g\,h}+|u|)$, rdx=FACEDISTG | `SwashExpDepUflow.ftn90:1800` |

```
! 1DH :1661-1664
dep = 0.5 * ( s1(nm) + dps(nm) + s1(nmu) + dps(nmu) )
cfl = rdx * dt * ( sqrt(grav*dep) + abs(u1(nm)) )

! 2DH :4964-4967  (dxl,dyl = 곡선 metric 평균)
dxl = 0.5 * ( gvv(nm) + gvv(ndm) )
dyl = 0.5 * ( guu(nm) + guu(nmd) )
cfl = dt * ( sqrt(grav*dep) + utot ) * sqrt(1./(dxl*dxl) + 1./(dyl*dyl))
```

세 식 모두 $\sqrt{gh}$(천수파속) + 유속의 advective 부분 합 — 명시적 운동량 적분의 CFL 안정조건 진단. 2DH는 2차원 대각 셀에 맞춰 $\sqrt{\Delta x^{-2}+\Delta y^{-2}}$.
`cflmax`는 `SwashCommdata3`의 모듈 변수다 (`src/SwashModule1.ftn90:250` `module SwashCommdata3`). [10-15 대조 정정]
선언 위치는 `src/SwashModule1.ftn90:651`이다 ([callflow:RF-022](../../../_staging/recovery/flow/SWASH-callflow.md#6-기존-노트-대조와-수정안)). [10-15 대조 정정]

구조 2DH의 CFL 순회는 영구 제외점 이외의 점을 평가한다 (`src/SwashExpDep2DHflow.ftn90:4956` `if ( nm > 1 ) then`). [10-15 대조 정정]
구조 1DH의 CFL 순회는 젖음 마스크로 제한하지 않는다 (`src/SwashExpDep1DHflow.ftn90:1654–1664`). [10-15 대조 정정]
비구조 수심평균 경로는 젖은 내부 면만 평가한다 (`src/SwashExpDepUflow.ftn90:1796,1798` `if ( wetu(iface) == 1 ) then`, `if ( face(iface)%atti(FMARKER) == 0 ) then`; [callflow:RF-021](../../../_staging/recovery/flow/SWASH-callflow.md#8-차이-결론)). [10-15 대조 정정]

CFL 진단은 `FACEDISTG`를 사용한다 (`src/SwashExpDepUflow.ftn90:1773` `rdx  = face(iface)%attr(FACEDISTG)`). [10-15 대조 정정]
`FACEDISTG`는 셀 무게중심 간 거리의 역수다 (`src/SwanGridFace.ftn90:408–411`). [10-15 대조 정정]
기술문서의 CFL 수심은 상류 수심이다 (`swashtech PDF p.98`(인쇄 p.90); [theory-unstructured:ST2-150](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]
실제 CFL 진단은 길이 가중 수심 `dep`를 사용한다 (`src/SwashExpDepUflow.ftn90:1784` `dep = finp * ( s1(icelll) + dps(icelll) ) + (1.-finp) * ( s1(icellr) + dps(icellr) )`). [10-15 대조 정정]

## 8. 추가 물리항 (세 파일 공통, 위치만)

| 항 | 1DH | 비고 |
|---|---|---|
| 점성(viscosity) | `:395-` | 2DH는 곡선 metric 응력 텐서 `:814` |
| 바람응력 implicit | `:463-` | `wndimp` |
| 바닥마찰 | `:485-` | `cbot` Euler implicit |
| baroclinic forcing | `:525-` | 밀도경사 |
| 대기압경사 | `:550-` | |
| Coriolis | (1DH 없음) | 2DH `corf` `:1354`, U `:863` |
| 식생(vegetation) | `:713-715` | `cvegu`, 수평실린더 dissipation `:1201-` |
| 다공질(porous media) | `:709-711` | `apomu/bpomu/cpomu`, update "1.10 March 2012" `:40` |
| 내부파 생성 | `:1418-` | `srcm`, "6.01 June 2019" `:41` |
| sponge layer 흡수 | `:1684-` | `spwidl` |

## 9. 진단·검증 코드

`ITEST >= 30`일 때 (1DH `:1583-1648`):
- net mass outflow `moutf` (local 연속식 잔차, `:1596`)
- `vol`은 면적·길이를 곱하지 않은 수위 합을 출력한다 (`src/SwashExpDep1DHflow.ftn90:1626`; `src/SwashExpDep2DHflow.ftn90:4905`; [theory-framework:ST1-310](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론)). [10-15 대조 정정]
- total energy `ener`(potential `:1629` + kinetic `:1634-1636`)

reflective 경계 닫힌 영역에서의 보존성 점검용 (주석 `:1609`).

비구조 유동 네 경로의 ITEST 체적 진단은 셀 면적 없이 수위를 합한다 (`src/SwashExpDepUflow.ftn90:1741`; `src/SwashImpDepUflow.ftn90:1923`; `src/SwashExpLayUflow.ftn90:2865`; `src/SwashImpLayUflow.ftn90:3036`). [10-15 대조 정정]
이 출력은 일반 삼각망의 변위 체적과 다르다 ([theory-unstructured:ST2-039](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]
이 출력의 결함 후보는 E·강함이다 ([theory-unstructured:ST2-039](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론)). [10-15 대조 정정]
이 판정은 연속식의 물리 갱신과 구분한다 ([theory-unstructured:ST2-039](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]

## 10. 요약 — 핵심 메커닉

1. **반-명시(semi-implicit)**: 운동량 advection·수위경사는 명시적(leap-frog/MacCormack), 바닥마찰·식생·다공질·바람은 Euler implicit(분모), 비정수압 압력만 theta-scheme 암시적 projection.
2. **세 변종의 본질적 차이는 (a) 격자 metric (직교/곡선 Jacobian/삼각 face-cell), (b) advection 시간스킴 (1DH·2DH=MacCormack vs U=Euler+Lax-Wendroff), (c) Poisson solver (tridiag / SIP / BiCGSTAB)** 세 가지.
3. **연속식은 jhk로 RK3/Hancock/Euler 선택**하는 예측-수정 구조 (8.01에서 Hancock 도입).
4. **압력은 2차 정확도 pressure-correction**(projection)으로 풀며 1-layer depth-averaged Keller-box 닫힘 항(`-2/hs` 류)을 동반.
5. CFL은 step 말미 진단만 — 자동 dt 조정 로직은 이 파일들에 없음(외부).

`cflmax`의 선언은 `src/SwashModule1.ftn90:651`에 있다. [10-15 대조 정정]
`jhk`의 초기값·입력 선택·선형 모드 보정은 §2.4에 있다. [10-15 대조 정정]
선형 솔버의 구현은 [선형 솔버 노트](swash-linear-solvers.md)에 정리했다. [10-15 대조 정정]

## 문서와 코드 차이 (10-15 대조)

대조 근거: [callflow](../../../_staging/recovery/flow/SWASH-callflow.md#8-차이-결론), [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#5-차이-결론), [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론), [outputs](../../../_staging/recovery/compare/swash-outputs-vs-code.md#5-차이-결론), [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론).
문서 쪽은 PDF 쪽이다.
인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

문서 판은 SWASH 12.01 매뉴얼 swashuse·swashtech다(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경). 코드 판은 `VERNUM 12.01`이다(공개 저장소 main `a486d5f`, 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-015 | 수위 부분 단계 RK3·Hancock·Euler 선택 | `swashuse PDF p.98`(인쇄 p.90) 도식은 `EXPL [cfllow] [cflhig]`를 적는다. p.161과<br>`misc/swash.edt:273`은 `(HANCock\|EULer)`를 적는다. | `src/SwashReadInput.ftn90:1886–1891`은 `if ( KEYWIS ('EUL') ) then`, `jhk = 3`; `else if ( KEYWIS ('HANC') ) then`, `jhk = 2`; `else if ( KEYWIS ('RK3') ) then`, `jhk = 1`이다.<br>`src/SwashInit.ftn90:393` `jhk        =  1     ! RK3`.<br>`src/SwashExpDep2DHflow.ftn90:4334` `do j = jhk, 3`.<br>`src/SwashReadInput.ftn90:431–432`의 LIN 선택은 `linswe = .true.`로 설정한다.<br>`src/SwashCheckPrep.ftn90:1457–1459` `if ( linswe ) then`, `jhk      = 3`. `608ffd7`·`9554c98`은 이 구간을 바꾸지 않았다. | C 문서 누락 | TIMEI EXPL은 수위 부분 단계의 RK3·Hancock·Euler를 선택한다. 초기 jhk는 RK3에 해당한다. 선형화 천수방정식 선택 시 준비 단계가 jhk를 Euler로 바꾼다. C는 주 설명 p.98–101의 부분 단계 설명과 부록 p.161에도 없는 RK3·초기값·선형화 보정 설명에 한정한다. Hancock·Euler 키워드는 부록에 존재한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| callflow:RF-017 | 2DH CFL 수식의 변수명 | `swashuse PDF p.136`(인쇄 p.128): `\mathrm{Cr}=\Delta t\left(\sqrt{gd}+\sqrt{u^2+v^2}\right)\sqrt{\frac{1}{\Delta x^2}+\frac{1}{\Delta y^2}}\leq1` | `src/SwashExpDep2DHflow.ftn90:4962` `utot = sqrt( u*u + v*v )`; `src/SwashExpDep2DHflow.ftn90:4967` `cfl = dt * ( sqrt(grav*dep) + utot ) * sqrt(1./(dxl*dxl) + 1./(dyl*dyl))`. | F 표기 차이 | 국소 격자 폭·중심 속도를 대입하면 설명서 2DH CFL 식과 코드 식이 일치한다. |
| callflow:RF-021 | CFL 최댓값을 구하는 점의 집합 | `swashuse PDF p.99,136`(인쇄 p.91,128)의 `over all wet grid points`. | 구조 2DH `src/SwashExpDep2DHflow.ftn90:4956`은 `if ( nm > 1 ) then`이다. 구조 1DH<br>`src/SwashExpDep1DHflow.ftn90:1654–1664`도 젖음 마스크를 검사하지 않는다. 비구조 깊이 평균 경로<br>`src/SwashExpDepUflow.ftn90:1796,1798`은 `if ( wetu(iface) == 1 ) then`과 `if ( face(iface)%atti(FMARKER) == 0 ) then`을 함께 요구한다. 최초 소스 `8756667 2022-09-03 initial release`의 `8756667:src/SwashExpDep2DHflow.ftn90:3126`에도 `if ( nm > 1 ) then`이 있다. 같은 커밋의 사용자 설명서 p.86과 문서 기준 `7949227`의 p.99는 같은 젖은 점 문장을 쓴다. `git log --all -G`의 해당 조건 이력에는 최초 도입과 소스 삭제·재등록만 있다. | B 문서 오기 | 구조 2DH의 이 순회는 영구 제외점 이외의 점을 평가한다. 구조 1DH의 이 순회도 젖음 마스크로 제한하지 않는다. 비구조 깊이 평균 경로는 젖은 내부 면만 평가한다. 문서의 평가 집합 설명을 이 경로별 조건으로 구별한다. 구조 2DH 조건은 최초 공개 소스부터 같으므로 B를 판 차이 A로 바꾸지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| callflow:RF-022 | 명시적 깊이 평균 노트의 cflmax 선언 모듈 추정 | `source-analysis/swash-explicit-depthavg-flow.md:262` `` `cflmax`는 module 변수로 노출(파일 내 정의 없음, `SwashTimecomm` 추정 — ⚠ 미확인, 본 파일에서는 대입만 함). `` | `src/SwashModule1.ftn90:250` `module SwashCommdata3`; `src/SwashModule1.ftn90:651` `real                                       :: cflmax      ! maximum CFL value found in flow computation`. 최초 소스 `8756667 2022-09-03 initial release`의 같은 파일 `8756667:src/SwashModule1.ftn90:248,613`에도 같은 모듈·선언이 있다. `git log --all -Gcflmax -- src/SwashModule1.ftn90`에는 최초 도입과 소스 삭제·재등록 이력만 있다. | B 문서 오기 | cflmax는 SwashCommdata3의 모듈 변수다. 현재 선언 위치는 `src/SwashModule1.ftn90:651`이다. 최초 공개 소스부터 같은 모듈에 있으므로 SwashTimecomm 추정은 판 차이로 설명할 수 없는 기존 노트의 오기다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| guide-syntax-build:SG1-102 | 식 (5.1) 1DH CFL | `swashuse PDF p.135`(인쇄 p.127) 식 (5.1): `\mathrm{Cr}=\dfrac{\Delta t\left(\sqrt{gd}+\lvert u\rvert\right)}{\Delta x}\leq1`. | `src/SwashExpDep1DHflow.ftn90:1661–1664` `dep = 0.5 * ( s1(nm) + dps(nm) + s1(nmu) + dps(nmu) )` / `!` / `cfl = rdx * dt * ( sqrt(grav*dep) + abs(u1(nm)) )` / `if ( cfl > cflmax ) cflmax = cfl` | C 문서 누락 | 계수·부호는 같지만 p.135의 식은 수심의 공간 위치와 평가 시각을 적지 않는다. 인용한 1DH 경로는 두 점의 현재 총수심 s1+dps를 평균한다. C는 p.135의 이 구현 조건 누락에 한정한다. SG1-103의 2DH 경로는 단일 셀 총수심을 사용하므로 수심 평균으로 묶지 않는다. [10-15 결론 검증 보완] |
| guide-syntax-build:SG1-103 | 번호 없는 2DH CFL 식 | `swashuse PDF p.136`(인쇄 p.128) 번호 없는 식: `\mathrm{Cr}=\Delta t\left(\sqrt{gd}+\sqrt{u^2+v^2}\right)\sqrt{\dfrac1{\Delta x^2}+\dfrac1{\Delta y^2}}\leq1`. | `src/SwashExpDep2DHflow.ftn90:4960–4962` `u    = 0.5 * ( u1(nm) + u1(nmd) )` / `v    = 0.5 * ( v1(nm) + v1(ndm) )` / `utot = sqrt( u*u + v*v )`; `src/SwashExpDep2DHflow.ftn90:4967` `cfl = dt * ( sqrt(grav*dep) + utot ) * sqrt(1./(dxl*dxl) + 1./(dyl*dyl))`<br>`src/SwashExpDep2DHflow.ftn90:4958` `dep = s1(nm) + dps(nm)`; `src/SwashExpDep2DHflow.ftn90:4964–4965`은 두 방향의 국소 격자폭을 평균한다. | C 문서 누락 | 2차원 CFL은 해당 셀의 현재 총수심 `dep = s1(nm) + dps(nm)`을 사용한다. 수심을 이웃과 평균하지 않는다. 속도와 국소 격자폭에는 평균을 사용한다. `swashuse PDF p.136`(인쇄 p.128)은 이 평가 위치와 시각을 생략한다. SG1-102의 1차원 수심 평균과 구분한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| inputs-physics-numerics:SI2-244 | 자동 수두 전환의 실제 조건 | `swashuse PDF p.96`(인쇄 p.88): “energy head conservation ... only in strong flow contractions” | `src/SwashExpDep1DHflow.ftn90:272`: `else if ( ( u0(nm) > u0(nmd) .or. stricthead ) .and. .not.strictmom ) then`; `src/SwashExpDep1DHflow.ftn90:274–275` `fac1 = 0.5 * ( ua(nmu) + ua(nm) )` / `fac2 = fac1`; `src/SwashExpDep1DHflow.ftn90:279–280` `fac1 = qm(nmu) / humn(nm)` / `fac2 = qm(nm ) / humn(nm)`<br>`src/SwashReadInput.ftn90:1984–1988`에서 UMOM MOMENTUM은 `strictmom = .true.`로, HEAD는 `stricthead = .true.`와 `strictmom  = .false.`로 설정한다. | C 문서 누락 | 명시적 수심평균 1DH의 자동 수두 조건은 `u0(nm)>u0(nmd)`이다. HEAD는 stricthead로 이 분기를 강제하며 MOMENTUM은 strictmom으로 배제한다. 선형화 linswe 분기가 먼저 적용된다. `swashuse PDF p.96`(인쇄 p.88)의 strong에 대응하는 별도 크기 임계값은 이 조건에 없다. [10-15 결론 검증 보완] |
| inputs-physics-numerics:SI2-277 | explicit 추가 적분 선택의 본문 설명 누락 | `swashuse PDF p.98–101`(인쇄 p.90–93) 본문에는 EULER·HANCOCK·RK3의 동작과 기본값 설명이 없다. p.161 부록과<br>`misc/swash.edt:273`에는 HANCock·EULer 이름이 있다. | `src/SwashReadInput.ftn90:1886–1891`: `if ( KEYWIS ('EUL') ) then` / `jhk = 3` / `else if ( KEYWIS ('HANC') ) then` / `jhk = 2` / `else if ( KEYWIS ('RK3') ) then` / `jhk = 1`<br>`src/SwashInit.ftn90:393`: `jhk        =  1     ! RK3`<br>`src/SwashExpDep1DHflow.ftn90:1342–1344`와<br>`src/SwashExpDepUflow.ftn90:1545–1547`은 `do j = jhk, 3`으로 전역 연속방정식을 적분한다.<br>`src/SwashCheckPrep.ftn90:1457–1459`는 linswe이면 `jhk      = 3`으로 바꾼다. | C 문서 누락 | EULER·HANCOCK 이름은 부록 p.161에 있다. C는 본문의 선택 의미·기본값 설명과 RK3 이름 누락으로 한정한다. 파서는 `EULER=3`·`HANCOCK=2`·`RK3=1`로 jhk를 정한다. 초기값은 RK3이며 선형화 모드는 EULER로 바꾼다. 구조 격자 수심평균 1DH와 비정형 수심평균 계산 모두 이 값을 전역 연속방정식의 단계 반복에 사용한다. [10-15 결론 검증 정정] |
| outputs:SO1-223 | Courant 식·기호 | `swashuse PDF p.146`(인쇄 p.138): `\mathrm{Cr}=\Delta t\left(\sqrt{gd}+\sqrt{u^2+v^2}\right)\sqrt{\frac1{\Delta x^2}+\frac1{\Delta y^2}}`; `∆t the time step`; `∆x and ∆y the grid sizes`; `u and v the velocity components` | `src/SwashExpDep2DHflow.ftn90:4958` `dep = s1(nm) + dps(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4962` `utot = sqrt( u*u + v*v )`<br>`src/SwashExpDep2DHflow.ftn90:4967` `cfl = dt * ( sqrt(grav*dep) + utot ) * sqrt(1./(dxl*dxl) + 1./(dyl*dyl))`<br>`src/SwashExpDep2DHflow.ftn90:4960–4965`는 인접 속도 성분과 격자 길이의 평균으로 u·v·dxl·dyl을 정한다. | F 표기 차이 | `dt=∆t`, `grav=g`, `dep=d`, `utot=√(u²+v²)`, `dxl=∆x`, `dyl=∆y`를 대응시키면 해당 2차원 Courant 식은 같다. §5의 F는 변수 표기 차이만 뜻한다. [10-15 결론 검증 정정] |
| theory-framework:ST1-041 | 식 (2.2) 운동량 방정식 | `swashtech PDF p.19`(인쇄 p.11): `\frac{\partial h\mathbf u}{\partial t}+\nabla\cdot(\mathbf q\otimes\mathbf u)=-gh\nabla\zeta` | `src/SwashExpDep1DHflow.ftn90:279–280` `fac1 = qm(nmu) / humn(nm)`<br>`fac2 = qm(nm ) / humn(nm)`<br>`src/SwashExpDep1DHflow.ftn90:291` `advec(nm) = rdx * ( fac1 * (ua(nmu) - u0(nm)) - fac2 * (ua(nm) - u0(nm)) )`<br>`src/SwashExpDep1DHflow.ftn90:707` `zgrad = grav * rdx * (s0(nmu) - s0(nm))`<br>`src/SwashExpDep1DHflow.ftn90:277` `else if ( humn(nm) > 0. ) then`<br>`src/SwashExpDep1DHflow.ftn90:289` `if ( wetu(nm) == 1 ) then` | F 표기 차이 | 해석: 코드는 유속의 이류형을 계산한다. `\partial_t(h\mathbf u)=h\partial_t\mathbf u+\mathbf u\partial_t h`와 식 (2.1)을 대입하면 식 (2.4)가 된다. 충격·건습·수두 선택 조건은 이 대수적 변형만으로 동일하다고 단정하지 않는다. 인용한 플럭스 계수의 대응은 ST1-022의 운동량형·양의 수심·젖은 면 분기에 한정한다. [10-15 결론 검증 보완] |
| theory-framework:ST1-046 | 식 (2.3) 곱 규칙 | `swashtech PDF p.19`(인쇄 p.11): `\nabla\cdot(\mathbf q\otimes\mathbf u)=(\mathbf q\cdot\nabla)\mathbf u+(\nabla\cdot\mathbf q)\mathbf u` | `src/SwashExpDep1DHflow.ftn90:291` `advec(nm) = rdx * ( fac1 * (ua(nmu) - u0(nm)) - fac2 * (ua(nm) - u0(nm)) )`<br>`src/SwashExpDep1DHflow.ftn90:279–280` `fac1 = qm(nmu) / humn(nm)`<br>`fac2 = qm(nm ) / humn(nm)` | F 표기 차이 | 해석: ST1-022의 운동량형·양의 수심·젖은 면 분기에서 코드 우변은 `[Q_+u_+-Q_-u_- - u_i(Q_+-Q_-)]/(h_i\Delta x)`이다. 여기서 `h_i`는 코드의 `humn(nm)`이다. 이 식은 플럭스형 이류에서 유속과 질량 플럭스 발산의 곱을 뺀 뒤 수심으로 나눈 형태이다. 문서의 식 (2.3) 전체와 코드의 유속 이류항을 그대로 같은 식으로 놓지 않는다. 수두형 분기에는 이 플럭스 계수 전개를 적용하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-050 | 번호 없는 해밀토니안 적분 | `swashtech PDF p.20`(인쇄 p.12): `\int_\Omega d\mathbf x\int_{z=-d}^{z=\zeta}dz\left[\frac12\mathbf u\cdot\mathbf u+gz\right]` | `src/SwashExpDep1DHflow.ftn90:1629` `ener = ener + 0.5 * grav * dx * s1(nm) * s1(nm)`<br>`src/SwashExpDep1DHflow.ftn90:1632` `fac1 = ( s1(nm ) + dps(nm ) ) * dx`<br>`src/SwashExpDep1DHflow.ftn90:1634` `ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nmd) * u1(nmd)`<br>`src/SwashExpDep1DHflow.ftn90:1611` `if ( ITEST >= 30 ) then`<br>`src/SwashReadInput.ftn90:2780–2781` `if ( KEYWIS ('TEST') ) then`<br>`call ININTG ('ITEST',ITEST,'STA',30)` | F 표기 차이 | 해석: 연직 적분은 `\frac12h\mathbf u^2+\frac12g(\zeta^2-d^2)`이다. 코드는 정지 바닥의 상수 `-\frac12g\int d^2`를 제외한 에너지 영점을 사용한다. 이 상수 차이는 시간 변화량에 영향을 주지 않는다. 공간 구적과 시간적분의 오차가 사라진다는 뜻은 아니다. 인용한 1D 진단은 `ITEST >= 30`에서 계산한다. 원문 주석 `src/SwashExpDep1DHflow.ftn90:1609`는 반사 경계를 가진 닫힌 영역에 적합한 진단이라고 명시한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-051 | 식 (2.5) 스칼라 내적 | `swashtech PDF p.21`(인쇄 p.13): `\langle f,g\rangle=\int_\Omega fg\,d\mathbf x` | `src/SwashExpDep2DHflow.ftn90:4908` `ener = ener + 0.5 * grav * gsqs(nm) * s1(nm) * s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then` | F 표기 차이 | 해석: 같은 위치의 두 수위 값에 셀 면적 `gsqs`를 곱한 합이 이산 내적이다. 코드가 연속 Hilbert 공간 자체를 구성하는 것은 아니다. 해석: 이산 내적은 `\langle f,g\rangle_A=\sum_c A_cf_cg_c`이다. 이 값은 ST1-050의 TEST 입력으로 활성화하는 에너지 진단에 포함된다. [10-15 결론 검증 보완] |
| theory-framework:ST1-052 | 식 (2.6) 벡터 내적 | `swashtech PDF p.21`(인쇄 p.13): `\langle\mathbf v,\mathbf w\rangle=\int_\Omega\mathbf v\cdot\mathbf w\,d\mathbf x` | `src/SwashExpDep2DHflow.ftn90:4913` `ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nmd) * u1(nmd)`<br>`src/SwashExpDep2DHflow.ftn90:4918` `ener = ener + 0.125 * ( fac1 + fac2 ) * v1(ndm) * v1(ndm)`<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then`<br>`src/SwashExpDep2DHflow.ftn90:4912` `fac2 = ( s1(nmd) + dps(nmd) ) * gsqs(nmd)` | F 표기 차이 | 해석: 법선 성분의 면 가중합이 벡터 내적을 근사한다. 수위 위치로 유속을 단순 이동시킨 값과 같은 식으로 취급하지 않는다. 균일 격자의 수심 평균 비교에 한정한 공유 면 계수는 ST1-073이다. 비균일 격자의 진단 가중치는 ST1-344에서 구별한다. 이 비교의 코드 값은 TEST 에너지 진단이다. [10-15 결론 검증 보완] |
| theory-framework:ST1-064 | 번호 없는 에너지 범함수 | `swashtech PDF p.22`(인쇄 p.14): `\mathcal H(h,m_x,m_y)=\frac12\int_\Omega\left[\frac{m_x^2+m_y^2}{h}+g\zeta^2\right]\,dx\,dy` | `src/SwashExpDep2DHflow.ftn90:4908` `ener = ener + 0.5 * grav * gsqs(nm) * s1(nm) * s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4911` `fac1 = ( s1(nm ) + dps(nm ) ) * gsqs(nm )`<br>`src/SwashExpDep2DHflow.ftn90:4913` `ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nmd) * u1(nmd)`<br>`src/SwashExpDep2DHflow.ftn90:4912` `fac2 = ( s1(nmd) + dps(nmd) ) * gsqs(nmd)`<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then` | F 표기 차이 | 해석: `(m_x^2+m_y^2)/h=h(u^2+v^2)`이다. TEST 진단은 공유 면의 운동에너지 기여를 양쪽 셀에 나누어 더한다. 내부 공유 면의 합은 `\frac14(A_Lh_L+A_Rh_R)u_f^2`이다. 균일 직교 격자에서는 ST1-073의 수심 평균식과 같다. 비균일 격자에서 문서의 Hodge 가중치와 자동으로 같아지는 것은 아니며, 그 차이는 ST1-344에 구별한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-073 | 번호 없는 운동에너지 | `swashtech PDF p.24`(인쇄 p.16): `\mathcal H_{\mathrm{kin}}=\frac12\int_\Omega h\mathbf u\cdot\mathbf u\,d\mathbf x=\frac12\langle\mathbf u,h\mathbf u\rangle` | `src/SwashExpDep1DHflow.ftn90:1632–1634` `fac1 = ( s1(nm ) + dps(nm ) ) * dx`<br>`fac2 = ( s1(nmd) + dps(nmd) ) * dx`<br>`ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nmd) * u1(nmd)`<br>`src/SwashExpDep1DHflow.ftn90:1635–1636` `fac2 = ( s1(nmu) + dps(nmu) ) * dx`<br>`ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nm ) * u1(nm )`<br>`src/SwashExpDep1DHflow.ftn90:1611` `if ( ITEST >= 30 ) then` | F 표기 차이 | 해석: 균일 1D 격자의 내부 공유 면에서는 두 셀의 진단 기여가 함께 합산된다. 그 합은 `\frac12\bar h_e\Delta x\,u_e^2`이다. 문서의 수심 가중치를 유지한다. 이 식의 코드 대응은 TEST 에너지 진단이며, 경계 면의 기여는 내부 면의 두 번 합산과 구별한다. [10-15 결론 검증 보완] |
| theory-framework:ST1-079 | 번호 없는 총에너지 합 | `swashtech PDF p.24`(인쇄 p.16): `\mathcal H=\frac12\langle\mathbf u,h\mathbf u\rangle+\frac12g\langle\zeta,\zeta\rangle` | `src/SwashExpDep2DHflow.ftn90:4908` `ener = ener + 0.5 * grav * gsqs(nm) * s1(nm) * s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4915` `ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nm ) * u1(nm )`<br>`src/SwashExpDep2DHflow.ftn90:4920` `ener = ener + 0.125 * ( fac1 + fac2 ) * v1(nm ) * v1(nm )`<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then` | F 표기 차이 | TEST 진단은 수위 위치의 위치에너지와 면 유속의 운동에너지를 합한다. ST1-073의 공유 면 계수 변형은 균일 격자의 내부 면에 적용한다. 비균일 격자의 면적·수심 가중치는 ST1-064·344와 같이 구별한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-082 | 번호 없는 이류 연산자 정의 | `swashtech PDF p.25`(인쇄 p.17): `A\mathbf u:=\nabla\cdot(\mathbf q\otimes\mathbf u)`; `A=\mathbf q\cdot\nabla+(\nabla\cdot\mathbf q)I` | `src/SwashExpDep1DHflow.ftn90:291` `advec(nm) = rdx * ( fac1 * (ua(nmu) - u0(nm)) - fac2 * (ua(nm) - u0(nm)) )` | F 표기 차이 | 해석: 문서의 `A\mathbf u`는 운동량 플럭스의 발산이다. 인용한 코드는 유속 방정식의 이류항이다. ST1-046의 운동량형 분기에서 플럭스 발산과 질량 변화항을 분리한 뒤 수심으로 나누어 연결한다. 따라서 코드의 `advec` 자체를 문서의 `A\mathbf u`로 동일시하지 않는다. 문서의 `I`는 항등 텐서이다. [10-15 결론 검증 정정] |
| theory-framework:ST1-091 | 번호 없는 면 플럭스 적분 | `swashtech PDF p.26`(인쇄 p.18): `\int_S\mathbf q\cdot d\mathbf S`; `\mathbf q\cdot d\mathbf S` | `src/SwashExpDep2DHflow.ftn90:4387` `qy(nm) = hv(nm)*gvv(nm)*v1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4380` `if ( .not.linswe ) then` | F 표기 차이 | 해석: 수심 적분 후 법선 유속에 수심과 면 길이를 곱한 체적 플럭스가 대응한다. 일반 질량 적분에는 밀도가 추가된다. 인용한 수심 플럭스는 비선형 분기에서 계산한다. 일정 밀도로 나눈 수심 적분량과 일반 3차원 질량 플럭스를 구별한다. [10-15 결론 검증 보완] |
| theory-framework:ST1-092 | 번호 없는 Gauss 발산정리 | `swashtech PDF p.26`(인쇄 p.18): `\int_V\nabla\cdot\mathbf q\,dV=\oint_{\partial V}\mathbf q\cdot d\mathbf S` | `src/SwashExpDep2DHflow.ftn90:4418` `s1(nm) = s0(nm) - fh * dt * ( qx(nm) - qx(nmd) + qy(nm) - qy(ndm) ) / gsqs(nm)` | F 표기 차이 | 해석: 셀 면 유량의 부호합이 적분 발산이다. 점 값의 발산을 얻을 때만 셀 면적으로 나눈다. |
| theory-framework:ST1-166 | 번호 없는 주 격자 가중 내적 | `swashtech PDF p.44`(인쇄 p.36): `\langle\alpha^{(k)},\beta^{(k)}\rangle_{\mathbb H^k}:=(\alpha^{(k)})^{\mathsf T}\mathbb H^k\beta^{(k)}` | `src/SwashExpDep2DHflow.ftn90:4908` `ener = ener + 0.5 * grav * gsqs(nm) * s1(nm) * s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then` | F 표기 차이 | 가중 내적의 특수값인 수위 에너지 합이 대응한다. 대각 면적 가중치는 행렬 없이 곱한다. 인용한 합은 ST1-050의 TEST 입력으로 활성화하는 에너지 진단이다. [10-15 결론 검증 보완] |
| theory-framework:ST1-184 | 번호 없는 벡터 Laplacian 구성 | `swashtech PDF p.47`(인쇄 p.39): `\mathbb D^0\tilde{\mathbb H}^n\tilde{\mathbb D}^{n-1}\mathbb H^1\upsilon^{(1)}+\tilde{\mathbb H}^{n-1}\tilde{\mathbb D}^{n-2}\mathbb H^2\mathbb D^1\upsilon^{(1)}` | `src/SwashExpDep1DHflow.ftn90:413` `visc(nm) = hvisc * rdx * rdx * ( hs(nmu)*(u0(nmu) - u0(nm)) - hs(nm)*(u0(nm) - u0(nmd)) ) / hum(nm)` | F 표기 차이 | 해석: 일정 수심의 1D에서 인용한 점성식은 유속의 2차 중앙차분으로 환원된다. F의 범위는 이 조건의 Laplacian이다. 다차원 curl·div 두 경로를 별도로 조립하는 구현과 같다고 확대하지 않는다. [10-15 결론 검증 정정] |
| theory-framework:ST1-197 | 번호 없는 압력 기울기 예제 | `swashtech PDF p.49`(인쇄 p.41): `\pi_i=p(v_i)`; `\begin{bmatrix}-1&+1&0&0\\0&-1&0&+1\\0&0&-1&+1\\-1&0&+1&0\end{bmatrix}\begin{bmatrix}\pi_1\\\pi_2\\\pi_3\\\pi_4\end{bmatrix}=\begin{bmatrix}\pi_2-\pi_1\\\pi_4-\pi_2\\\pi_4-\pi_3\\\pi_3-\pi_1\end{bmatrix}` | `src/SwashExpDep1DHflow.ftn90:338–341` `fac = 0.5 * rdx / hum(nm)`<br>`gmat(nm,1) = -fac * ( s0(nm ) + dps(nmu) )`<br>`gmat(nm,2) =  fac * ( s0(nmu) + dps(nm ) )`; `src/SwashExpDep1DHflow.ftn90:381` `qgrad(nm) = gmat(nm,1) * q(nm) + gmat(nm,2) * q(nmu)` | F 표기 차이 | 해석: 일정 수심·평탄 바닥의 내부 젖은 점에서는 두 압력 계수가 반대 부호가 된다. 이 조건에서 `qgrad=(q_R-q_L)/(2\Delta x)`이다. 계수 `1/2`는 바닥 압력 `q`를 수심 평균 압력으로 바꾸는 연직 폐쇄에 따른다. 그 조건은 ST1-273과 같다. ST1-188·221과 같은 차분 대응이다. 문서의 꼭짓점 배치와 코드 수위점 배치는 구별한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-220 | 식 (2.22) 반이산 연속방정식 | `swashtech PDF p.55`(인쇄 p.47): `\frac{d\nu^{(n)}}{dt}+\mathbb D^{n-1}\phi^{(n-1)}=0` | `src/SwashExpDep2DHflow.ftn90:4418` `s1(nm) = s0(nm) - fh * dt * ( qx(nm) - qx(nmd) + qy(nm) - qy(ndm) ) / gsqs(nm)` | F 표기 차이 | 해석: 양변에 셀 면적을 곱하면 `\Delta\nu=-fh\,\Delta t\sum_f s_f\phi_f`이다. 문서의 반이산식에 시간적분을 적용한 형태이다. |
| theory-framework:ST1-240 | 식 (2.26) 수심방정식 | `swashtech PDF p.59`(인쇄 p.51): `\frac{d\tilde\eta^{(0)}}{dt}+\mathbb H^n\mathbb D^{n-1}\phi^{(n-1)}=0` | `src/SwashExpDep2DHflow.ftn90:4418` `s1(nm) = s0(nm) - fh * dt * ( qx(nm) - qx(nmd) + qy(nm) - qy(ndm) ) / gsqs(nm)` | F 표기 차이 | 체적방정식에 역 면적을 적용한 점 수위식이다. 바닥이 고정이면 점 수심 증가와 수위 증가가 같다. |
| theory-framework:ST1-243 | 번호 없는 이산 총에너지 | `swashtech PDF p.59`(인쇄 p.51): `\mathcal H=\mathcal H_{\mathrm{kin}}+\mathcal H_{\mathrm{pot}}=\frac12\langle\upsilon^{(n-1)},\phi^{(n-1)}\rangle_{\mathbb H^{n-1}}+\frac12g\langle\tilde\zeta^{(0)},\tilde\zeta^{(0)}\rangle_{\tilde{\mathbb H}^0}` | `src/SwashExpDep2DHflow.ftn90:4908` `ener = ener + 0.5 * grav * gsqs(nm) * s1(nm) * s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4911–4913` `fac1 = ( s1(nm ) + dps(nm ) ) * gsqs(nm )`<br>`fac2 = ( s1(nmd) + dps(nmd) ) * gsqs(nmd)`<br>`ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nmd) * u1(nmd)` | F 표기 차이 | 균일 직교 격자에서 공유 면의 두 셀 기여는 `2\times\frac18A(h_L+h_R)u_f^2=\frac12A\bar h_fu_f^2`이다. 위치에너지는 `\frac12\sum_c gA_c\zeta_c^2`이다. 비균일 격자의 진단 가중치는 ST1-344에서 별도로 판정한다. |
| theory-framework:ST1-257 | 식 (3.2) 전체 운동량식 | `swashtech PDF p.63`(인쇄 p.55): `\frac{\partial h\mathbf u}{\partial t}+\nabla\cdot(\mathbf q\otimes\mathbf u)+gh\nabla\zeta=-\int_{-d}^{\zeta}\nabla p\,dz+\nabla\cdot(\nu_hh\nabla\mathbf u)-c_f\lVert\mathbf u\rVert\mathbf u+\boldsymbol\tau_w-f\hat{\mathbf z}\times h\mathbf u` | `src/SwashExpDep2DHflow.ftn90:1354` `contrib = advecx(nm) + advecy(nm) + zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm)) - visc(nm) + corf(nm)`<br>`src/SwashExpDep2DHflow.ftn90:1356` `denom = 1. + cvegu(nm,1,2) + cpomu(nm,1) + dt * ( cbot(nm) + cporfr + cveg + wndimp(nm) )`<br>`src/SwashExpDep2DHflow.ftn90:1360` `u1(nm) = ( (1.+cvegu(nm,1,2)+cpomu(nm,1)) * u0(nm) - dt * contrib ) / denom` | F 표기 차이 | 해석: 문서는 수심 적분 운동량식이다. 코드는 연속방정식을 사용해 유속식으로 만들고 마찰을 분모에 넣는다. 아래 각 항의 계수·부호를 개별 대조했다. 다공체·식생·밀도·기압 추가항은 [theory-framework 보고서 §3](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#3-코드에만-있는-처리)에 정리되어 있다. [10-15 전수 검증 정정] |
| theory-framework:ST1-258 | 식 (3.2) 이류 항 | `swashtech PDF p.63`(인쇄 p.55): `\nabla\cdot(\mathbf q\otimes\mathbf u)` | `src/SwashExpDep1DHflow.ftn90:291` `advec(nm) = rdx * ( fac1 * (ua(nmu) - u0(nm)) - fac2 * (ua(nm) - u0(nm)) )`<br>`src/SwashImpDepM1DHflow.ftn90:490–491` `a(nm) = -fac2`<br>`c(nm) =  fac1` | F 표기 차이 | 식 (2.3)·(2.4)의 곱 규칙과 질량 변화항을 적용한다. 상류 경로와 중앙 mimetic 경로는 다른 소산 성질을 가진다. |
| theory-framework:ST1-259 | 식 (3.2) 정수압 기울기 | `swashtech PDF p.63`(인쇄 p.55): `gh\nabla\zeta` | `src/SwashExpDep2DHflow.ftn90:1342` `zgrad = grav * (s0(nmu) - s0(nm)) / gvu(nm)`<br>`src/SwashExpDep2DHflow.ftn90:2982` `zgrad = grav * (s0(num) - s0(nm)) / guv(nm)` | F 표기 차이 | 수심 적분식의 `h`를 유속식에서 나눈다. 코드는 두 격자 좌표 방향의 수위 차를 각각 유속 방향 길이로 나눈다. 문서의 동·북 성분과의 대응에는 격자의 방향을 함께 적용한다. 좌표 변환은 ST1-265이다. 해석: `(gh\nabla\zeta)/h=g\nabla\zeta`이다. [10-15 결론 검증 정정] |
| theory-framework:ST1-260 | 식 (3.2) 비정수압 기울기 | `swashtech PDF p.63`(인쇄 p.55): `-\int_{-d}^{\zeta}\nabla p\,dz` | `src/SwashExpDep1DHflow.ftn90:338–341` `fac = 0.5 * rdx / hum(nm)`<br>`!`<br>`gmat(nm,1) = -fac * ( s0(nm ) + dps(nmu) )`<br>`gmat(nm,2) =  fac * ( s0(nmu) + dps(nm ) )`<br>`src/SwashExpDep1DHflow.ftn90:381` `qgrad(nm) = gmat(nm,1) * q(nm) + gmat(nm,2) * q(nmu)` | F 표기 차이 | 압력의 바닥값은 코드의 `q`이다. 구동력에 양의 `qgrad`를 더하고 유속 갱신에서 전체 구동력을 뺀다. 식 (3.4)의 보존형 변형은 ST1-273에서 보인다. |
| theory-framework:ST1-261 | 식 (3.2) 점성 항 | `swashtech PDF p.63`(인쇄 p.55): `\nabla\cdot(\nu_hh\nabla\mathbf u)` | `src/SwashExpDep1DHflow.ftn90:413` `visc(nm) = hvisc * rdx * rdx * ( hs(nmu)*(u0(nmu) - u0(nm)) - hs(nm)*(u0(nm) - u0(nmd)) ) / hum(nm)`<br>`src/SwashExpDep2DHflow.ftn90:719` `visc(nm) = hvisc * ( fac1/gvu(nm) + fac2/guu(nm) ) / hum(nm)` | F 표기 차이 | 점성 플럭스의 차분을 면 수심으로 나눈다. 전체 구동력에서는 `-visc`이므로 최종 유속에는 양의 점성 항을 더한다. 상수 `hvisc` 경로의 활성 조건은 `ihvisc == 1 .and. hvisc > 0.`이다. |
| theory-framework:ST1-264 | 식 (3.2) Coriolis 부호 | `swashtech PDF p.63`(인쇄 p.55): `-f\hat{\mathbf z}\times h\mathbf u` | `src/SwashExpDep2DHflow.ftn90:1000` `cfu(nm,1) = -fcor(nm,1) * v`<br>`src/SwashExpDep2DHflow.ftn90:2641` `cfv(nm,1) = fcor(nm,2) * u`<br>`src/SwashExpDep2DHflow.ftn90:1360` `u1(nm) = ( (1.+cvegu(nm,1,2)+cpomu(nm,1)) * u0(nm) - dt * contrib ) / denom`<br>`src/SwashExpDep2DHflow.ftn90:3000` `v1(nm) = ( (1.+cvegv(nm,1,2)+cpomv(nm,1)) * v0(nm) - dt * contrib ) / denom` | F 표기 차이 | `\hat{\mathbf z}\times(u,v)=(-v,u)`이다. 구동력에 포함한 `corf`를 갱신에서 빼므로 가속도는 `(+fv,-fu)`이다. 이전 시간 가중치와 격자 보간은 이 표의 ST1-296에 정리되어 있다. [10-15 전수 검증 정정] |
| theory-framework:ST1-267 | 번호 없는 유속·플럭스와 압력 정의 | `swashtech PDF p.63`(인쇄 p.55): `\mathbf u=(u,v)`; `\mathbf q=h\mathbf u`; `p` `normalised by the water density`; `difference between the mass flux q and the mass circulation level hu`. | `src/SwashExpDep1DHflow.ftn90:205` `qx(nm) = hu(nm)*u0(nm)`<br>`src/SwashExpDep1DHflow.ftn90:1005` `w1top(nm) = w0top(nm) + w0bot(nm) - w1bot(nm) + 2.*dt*fac*q(nm)/hs(nm)` | F 표기 차이 | 코드의 `qx`는 플럭스이다. 코드의 `q`는 바닥 비정수압이다. 압력의 유속 가속도 적용에 밀도를 다시 나누지 않는다. 따라서 문서의 정규화 압력에 대응한다. |
| theory-framework:ST1-271 | 정수압 조건·약해 | `swashtech PDF p.64`(인쇄 p.56): `p\equiv0`; `nonlinear hyperbolic equations`; `may thus generate discontinuous solutions featuring shock waves`; `weak solutions in the variational context.` | `src/SwashExpDep2DHflow.ftn90:641` `if ( ihydro == 1 ) then`; `src/SwashExpDep2DHflow.ftn90:662–664` `else`<br>`!`<br>`qgrad = 0.` | F 표기 차이 | 비정수압 모드가 아닌 분기는 비정수압 가속도를 0으로 둔다. 이 대응은 문서의 `p\equiv0`를 코드의 가속도 항으로 표현한 F이다. 쌍곡성·불연속·약해의 존재에 관한 문장은 수학적 설명이며 이 분기의 보증 성질로 확대하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-273 | 식 (3.4) 비정수압 보존형 | `swashtech PDF p.64`(인쇄 p.56): `\int_{-d}^{\zeta}\nabla p\,dz=\frac12\nabla(hp_b)-p_b\nabla d` | `src/SwashExpDep1DHflow.ftn90:338–341` `fac = 0.5 * rdx / hum(nm)`<br>`!`<br>`gmat(nm,1) = -fac * ( s0(nm ) + dps(nmu) )`<br>`gmat(nm,2) =  fac * ( s0(nmu) + dps(nm ) )` | F 표기 차이 | 해석: `\frac12(h_Rp_R-h_Lp_L)-\frac12(p_R+p_L)(d_R-d_L)=\frac12[(\zeta_R+d_L)p_R-(\zeta_L+d_R)p_L]`이다. 이를 `\Delta x\,\bar h`로 나누면 코드의 두 계수와 같다. `p_b`의 평균을 지형 경사에 곱한 형태이다. |
| theory-framework:ST1-274 | 번호 없는 Keller-box 연직 식 | `swashtech PDF p.64`(인쇄 p.56): `\frac{\partial w_s}{\partial t}=\frac{2p_b}{h}-\frac{\partial w_b}{\partial t}` | `src/SwashExpDep1DHflow.ftn90:1005` `w1top(nm) = w0top(nm) + w0bot(nm) - w1bot(nm) + 2.*dt*fac*q(nm)/hs(nm)`<br>`src/SwashExpDep1DHflow.ftn90:1317–1319` `w1top(nm) = w1top(nm) + w1bot(nm) + 2.*dt*theta*dq(nm)/hs(nm)`<br>`w1bot(nm) = -0.5 * rdx * ( u1(nm) + u1(nmd) ) * ( dpu(nm) - dpu(nmd) )`<br>`w1top(nm) = w1top(nm) - w1bot(nm)` | F 표기 차이 | 예측 단계는 이전 위·아래 경계 유속의 합을 유지하고 새 바닥 유속을 뺀다. 압력 보정 단계는 `2\Delta t\,\theta\,\delta p/h`를 더한다. 계수 2와 바닥 시간변화의 부호가 같다. 해석: `(w_s^*-w_s^n)+(w_b^*-w_b^n)=2\Delta t\,fac\,p_b/h`이다. |
| theory-framework:ST1-277 | 식 (3.5) 국소 연속방정식 | `swashtech PDF p.64`(인쇄 p.56): `\nabla\cdot\mathbf u+\frac{w_s-w_b}{h}=0` | `src/SwashExpDep1DHflow.ftn90:1596` `moutf = moutf + qx(nm) - qx(nmd) - 0.5 * ( u1(nm) + u1(nmd) ) * ( hu(nm) - hu(nmd) ) + dx * ( w1top(nm) - w1bot(nm) )`; 같은 파일 `src/SwashExpDep1DHflow.ftn90:1585` `if ( ITEST >= 30 .and. ihydro == 1 ) then`. | F 표기 차이 | 해석: 수평 잔차는 `h_Ru_R-h_Lu_L-\frac12(u_R+u_L)(h_R-h_L)=\frac12(h_R+h_L)(u_R-u_L)`이다. 전체 잔차를 `\Delta x\,\frac12(h_R+h_L)`로 나누면 식의 차분형이다. 코드의 면 수심과 셀 수심은 각 이산 위치에서 평가한다. 이 식은 비정수압 모드의 테스트 수준 30 이상에서 계산하는 연속식 잔차이다. [10-15 결론 검증 보완] |
| theory-framework:ST1-285 | 수두·운동량·선형 분기 | `swashtech PDF p.25·59`(인쇄 p.17·51)은 상류 소산의 동기만 적는다. 구체 분기 없음.<br>`swashuse PDF p.96`(인쇄 p.88)은 `MOMENTUM`과 `HEAD`를 설명한다. | `src/SwashExpDep1DHflow.ftn90:267–280` `if ( linswe ) then`<br>`!`<br>`fac1 = 0.`<br>`fac2 = 0.`<br>`!`<br>`else if ( ( u0(nm) > u0(nmd) .or. stricthead ) .and. .not.strictmom ) then`<br>`!`<br>`fac1 = 0.5 * ( ua(nmu) + ua(nm) )`<br>`fac2 = fac1`<br>`!`<br>`else if ( humn(nm) > 0. ) then`<br>`!`<br>`fac1 = qm(nmu) / humn(nm)`<br>`fac2 = qm(nm ) / humn(nm)`<br>`src/SwashReadInput.ftn90:431–432` `if ( KEYWIS ('LIN') ) then`<br>`linswe = .true.`; `src/SwashReadInput.ftn90:1984–1988`은 `MOM`에서 `strictmom = .true.`, `HEAD`에서 `stricthead = .true.`와 `strictmom = .false.`를 대입한다. | C 문서 누락 | C의 범위는 `swashtech PDF p.25·59`(인쇄 p.17·51)의 실제 분기 설명이다. HEAD·MOMENTUM 선택은 사용자 설명서에 있다. 선형 모드는 비선형 이류 계수를 0으로 둔다. 인용한 수두 조건을 만족하면 수두 보존형을 선택한다. 그다음 `humn(nm) > 0.` 분기는 플럭스 기반 운동량 보존형을 사용한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-286 | 수위 적분의 단계·기본값 | `swashtech PDF p.55·59·63`(인쇄 p.47·51·55)의 반이산식에는 시간적분 단계 없음.<br>`swashuse PDF p.161`(인쇄 p.153)과<br>`misc/swash.edt:273`은 `HANCock`·`EULer` 선택을 적는다. | `src/SwashInit.ftn90:393` `jhk        =  1     ! RK3`<br>`src/SwashExpDep2DHflow.ftn90:4332` `! (jhk = 1: RK3, jhk = 2: Hancock, jhk = 3: first order Euler)`<br>`src/SwashExpDep2DHflow.ftn90:4334` `do j = jhk, 3`<br>`src/SwashExpDep2DHflow.ftn90:4340` `fh = 0.5`<br>`src/SwashExpDep2DHflow.ftn90:4346` `fh = 1.`<br>`src/SwashReadInput.ftn90:1886–1892`의 `EUL`·`HANC`·`RK3` 입력은 각각 `jhk = 3`·`2`·`1`을 선택한다.<br>`src/SwashCheckPrep.ftn90:1457–1461`은 `if ( linswe ) then`에서 `jhk = 3`을 대입한다. | C 문서 누락 | C는 `swashtech PDF p.55·59·63`(인쇄 p.47·51·55)의 시간 단계 설명에 한정한다. 기본 초기값은 RK3이지만 입력 선택과 선형 모드의 Euler 강제가 있다. 실제 `do j = jhk, 3` 반복 횟수는 최종 `jhk`에 따른다. 수위·유속의 시간 배치와 연속식 적분 선택을 구별한다. 같은 선택은 ST1-324에도 적용한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-288 | 연직 유속의 수평 이류 선택 | `swashtech PDF p.64`(인쇄 p.56)의 번호 없는 연직식에는 수평 이류 항 없음.<br>`swashuse PDF p.138–139`(인쇄 p.130–131)는 `DISCRET UPW WMOM H`와 수평 이류의 생략·자동 포함을 설명한다. | `src/SwashExpDep1DHflow.ftn90:1016` `if ( horwinc ) then`<br>`src/SwashExpDep1DHflow.ftn90:1051` `w1top(nm) = w1top(nm) - 0.5 * ( fac1 * (w0top(nm) - w0top(nmd)) + fac2 * (w0top(nmu) - w0top(nm)) )`<br>`src/SwashInit.ftn90:399` `horwinc    = .false.`<br>`src/SwashExpDep1DHflow.ftn90:1047` `if ( propsc == 3 .and. kappa == 1. ) then`이 인용한 중앙차분식의 추가 조건이다.<br>`src/SwashReadInput.ftn90:1969–1972`의 `WMOM`은 `horwinc = .true.`를 대입하며 `src/SwashReadInput.ftn90:909–920`의 `BRE`도 이를 켠다.<br>`src/SwashCheckPrep.ftn90:762–765,862–864,872–880`에는 자동 활성화가 있고 `src/SwashCheckPrep.ftn90:1113–1115,1457–1463`에는 부유체·선형 모드의 해제가 있다. | C 문서 누락 | C는 `swashtech PDF p.64`(인쇄 p.56)의 연직식에 한정한다. 기능 선택과 자동 포함은 사용자 설명서에 있다. 실제 계산은 최종 `horwinc`가 참일 때 수행한다. 인용한 1051행은 그 안의 중앙차분 조건에서만 사용한다. 초기값 거짓을 전체 실행의 비활성으로 해석하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-296 | Coriolis 시간 가중치·격자 보간 | `swashtech PDF p.63`(인쇄 p.55)은 연속 Coriolis 항만 적는다. 시간·격자 계수 없음.<br>`swashuse PDF p.159`(인쇄 p.151)와<br>`misc/swash.edt:186`은 `[epsab2]` 입력을 명령 도식에 표시한다. | `src/SwashInit.ftn90:309` `pcor(2) = 0.1`<br>`src/SwashExpDep2DHflow.ftn90:972` `epsab2 = pcor(2)`<br>`src/SwashExpDep2DHflow.ftn90:991` `corf(nm) = -(0.5+epsab2) * cfu(nm,1)`<br>`src/SwashExpDep2DHflow.ftn90:997–998` `v = sqrt(abs(fcor(nm,2))*dpv(nm))*v0(nm) + sqrt(abs(fcor(nmu,2))*dpv(nmu))*v0(nmu) + sqrt(abs(fcor(ndm,2))*dpv(ndm))*v0(ndm) + sqrt(abs(fcor(ndmu,2))*dpv(ndmu))*v0(ndmu)`<br>`v = v / (4.*sqrt(abs(fcor(nm,1))*dpu(nm)))`<br>`src/SwashExpDep2DHflow.ftn90:1002` `corf(nm) = corf(nm) + (1.5+epsab2) * cfu(nm,1)`<br>`src/SwashReadInput.ftn90:1382–1385`의 `CORI`는 `coriolis = .true.`와 `call INREAL ('EPSAB2', pcor(2), 'STA', 0.1)`을 실행한다.<br>`src/SwashExpDep2DHflow.ftn90:970,985`의 조건은 `if ( coriolis ) then`과 `if ( wetu(nm) == 1 .and. fcor(nm,1) /= 0. ) then`이다. | C 문서 누락 | C는 기술문서 p.63에 없는 구조 격자의 시간·공간 가중식이다. 이전·현재 Coriolis 값에 수정 Adams–Bashforth 가중치를 적용한다. 네 v점의 보간에는 `\sqrt{\lvert f\rvert d}`를 쓴다. 최종 Coriolis 활성값과 젖은 점·비영 f 조건 아래에서만 인용식을 계산한다. [10-15 결론 검증 보완] |
| theory-framework:ST1-298 | 밀도 경사와 대기압 경사 | `swashtech PDF p.19`(인쇄 p.11)의 실제 문장은 `barotropic flow of an incompressible fluid`이다. 기존 인용 `Fluid is assumed to be of constant density.`는 이 쪽에 없다. p.63 식 (3.2)는 밀도 경사·대기압 경사를 별도로 적지 않는다.<br>`swashuse PDF p.42·83`(인쇄 p.34·75)은 대기압 입력장과 밀도에 관련된 수송을 설명한다. | `src/SwashExpDep2DHflow.ftn90:920` `if ( idens /= 0 ) then`<br>`src/SwashExpDep2DHflow.ftn90:932` `pgrad(nm) = 0.5 * grav * hum(nm) * (rho(nmu) - rho(nm)) / ( rhow*gvu(nm) )`<br>`src/SwashExpDep2DHflow.ftn90:947` `if ( svwp ) then`<br>`src/SwashExpDep2DHflow.ftn90:959` `pgrad(nm) = pgrad(nm) + (patm(nmu) - patm(nm)) / ( rhow*gvu(nm) )`<br>`src/SwashInputField.ftn90:145–160`의 `PR` 입력은 `svwp = .true.`를 대입하며 `SAL`·`TEMP`는 수송 인덱스를 설정한다.<br>`src/SwashCheckPrep.ftn90:889`는 해당 수송 조건에서 `idens = 1`을 대입한다. | C 문서 누락 | C는 기술문서 p.19·63의 제한된 방정식 설명에 한정한다. p.19의 원문은 `barotropic flow of an incompressible fluid`이다. 사용자 설명서와 원본 README 26–28행은 밀도 구동 흐름을 포함한다. 활성 밀도·대기압 모드의 추가 가속도는 인용한 코드와 같다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] [10-15 전수 검증 정정] |
| theory-framework:ST1-309 | 보존 진단의 활성·경계·전역 합 | `swashtech PDF p.60–61`(인쇄 p.52–53)은 반이산 에너지 증명을 적는다. 이 출력 절차 없음.<br>`swashuse PDF p.122`(인쇄 p.114)는 `[itest] = 30`에서 질량·에너지 보존을 점검할 수 있다고 명시한다. | `src/SwashExpDep2DHflow.ftn90:4881` `! Note: this testing is appropriate for a closed domain with reflective boundaries`<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then`<br>`src/SwashExpDep2DHflow.ftn90:4929–4933` `call SWREDUCE ( vol, 1, SWREAL, SWSUM )`<br>`call SWREDUCE (ener, 1, SWREAL, SWSUM )`<br>`!`<br>`write(PRINTF,102) vol`<br>`write(PRINTF,103) ener`<br>`src/SwashReadInput.ftn90:2780–2781` `if ( KEYWIS ('TEST') ) then`<br>`call ININTG ('ITEST',ITEST,'STA',30)`. | C 문서 누락 | C는 `swashtech PDF p.60–61`(인쇄 p.52–53)에 없는 진단 적용 경계와 전역 합의 구현 설명이다. TEST 30 기능 자체는 사용자 설명서에 있다. 테스트 수준이 30 이상이면 부분 영역의 진단 합을 모아 출력한다. 닫힌 영역·반사 경계는 주석의 적용 권고이며 이를 검사하는 조건문은 이 출력 블록에 없다. 출력 정의의 문제는 ST1-310·344에서 구별한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-310 | 체적 진단의 면적 누락 | `swashtech PDF p.55`(인쇄 p.47): `by mass we refer to the area-integrated height`; p.58: `\nu^{(n)}=\tilde{\mathbb H}^0\tilde\eta^{(0)}`. | `src/SwashExpDep2DHflow.ftn90:4880` `! calculate total displaced volume of water (reference is at z = 0) and energy`<br>`src/SwashExpDep2DHflow.ftn90:4905` `vol = vol + s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4908` `ener = ener + 0.5 * grav * gsqs(nm) * s1(nm) * s1(nm)`<br>`src/SwashExpDep2DHflow.ftn90:4932` `write(PRINTF,102) vol`<br>`src/SwashExpDep1DHflow.ftn90:1626` `vol = vol + s1(nm)`<br>`src/SwashFloatObjects.ftn90:415–416` `area = dxl * dyl`<br>`vol  = flos(nm) * area`<br>`src/SwashReadInput.ftn90:2780–2781`은 TEST 수준을 읽는다.<br>`src/SwashComputFlow.ftn90:134–146`은 2D의 `kmax == 1`, `mtimei == 1`에서 이 루틴을 호출한다.<br>`src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then`; `src/SwashExpDep2DHflow.ftn90:4929` `call SWREDUCE ( vol, 1, SWREAL, SWSUM )`. | E 코드 결함 후보 | 근거 강도: 중간. 해석: 2D 체적은 `\sum_c A_c\zeta_c`여야 한다. 진단은 `\sum_c\zeta_c`를 출력한다. 자체 주석의 체적, 같은 판 문서의 면적 적분, 다른 체적 계산 경로와 충돌한다. 균일 격자에서는 누락한 공통 면적이 상수이므로 상대 보존 변화 감시가 가능하다. 비균일 격자에서는 같은 결론을 낼 수 없다. 유동 갱신식의 질량 보존 결함을 뜻하지 않는다. TEST 30에서 도달하며 진단문에 비활성 전처리 접두어가 없다. 전역 합부터 출력까지 면적을 보정하지 않는다. `8756667:src/SwashExpDep2DHflow.ftn90:3075`, `25c79e7:src/SwashExpDep2DHflow.ftn90:4805`(11.01), 문서 배포 시점 `7949227:src/SwashExpDep2DHflow.ftn90:4905`가 모두 같다. 1D도 `8756667:src/SwashExpDep1DHflow.ftn90:1133`, 11.01의 `25c79e7:src/SwashExpDep1DHflow.ftn90:1625`에서 같은 수위 합이다. main blame의 `f7ebbca`는 삭제 후 재등록이며 식의 도입 시점이 아니다. 문서 뒤 코드 변경 `608ffd7`·`9554c98`은 이 유동 파일을 수정하지 않았다. [git 판정 E2](../../../_staging/recovery/compare/SWASH-git-verify-E2.md)의 E·근거 중간을 유지한다. ST1-333도 같은 판정이다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| theory-framework:ST1-324 | 수위 적분 선택의 기본값 | `source-analysis/swash-explicit-depthavg-flow.md:74` `시차(staggered) leap-frog/Hansen 구조를 이룬다.`; `source-analysis/swash-explicit-depthavg-flow.md:85` `루프 내` | `src/SwashInit.ftn90:393` `jhk        =  1     ! RK3`<br>`src/SwashExpDep2DHflow.ftn90:4334` `do j = jhk, 3`<br>`src/SwashReadInput.ftn90:1886–1892`은 Euler·Hancock·RK3를 각각 `jhk = 3`·`2`·`1`로 선택한다.<br>`src/SwashCheckPrep.ftn90:1457–1459`은 `if ( linswe ) then`에서 `jhk      = 3`을 대입한다. | C 문서 누락 | 기존 노트 78–85행은 이미 RK3·Hancock·Euler와 입력 선택을 설명한다. C는 초기 기본값과 선형 모드 강제 선택을 보충하는 범위이다. 초기값은 RK3이지만 선형 모드에서는 Euler로 바뀐다. 실제 연속식 단계는 최종 `jhk`를 따르며 ST1-286과 같다. 수위·유속의 시간 배치와 이 선택을 구별한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-framework:ST1-344 | 셀별 운동에너지 진단의 가중치 | `swashtech PDF p.59`(인쇄 p.51): `\mathcal H_{\mathrm{kin}}=\frac12\langle\upsilon^{(n-1)},\phi^{(n-1)}\rangle_{\mathbb H^{n-1}}`; p.58: 식 (2.24). 셀별 출력 분배식은 적지 않는다.<br>`swashuse PDF p.122`(인쇄 p.114)는 TEST 30의 에너지 점검을 설명하지만 이 셀별 분배식은 적지 않는다. | `src/SwashExpDep2DHflow.ftn90:4911–4915` `fac1 = ( s1(nm ) + dps(nm ) ) * gsqs(nm )`<br>`fac2 = ( s1(nmd) + dps(nmd) ) * gsqs(nmd)`<br>`ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nmd) * u1(nmd)`<br>`fac2 = ( s1(nmu) + dps(nmu) ) * gsqs(nmu)`<br>`ener = ener + 0.125 * ( fac1 + fac2 ) * u1(nm ) * u1(nm )`; 같은 파일 `src/SwashExpDep2DHflow.ftn90:4883` `if ( ITEST >= 30 ) then`; `src/SwashExpDep2DHflow.ftn90:4902` `if ( nm > 1 ) then`. 출력 적용 경계와 전역 합은 ST1-309이다. | C 문서 누락 | 해석: 내부 공유 면의 출력 기여는 `E_f^{\mathrm{code}}=\frac14(A_Lh_L+A_Rh_R)u_f^2`이다. 문서의 운동에너지는 `E_f^{\mathrm{doc}}=\frac12\bar h_fl_fd_fu_f^2`이다. 균일 직교 격자에서는 두 식이 같다. 면 길이 `l_f`가 같은 비균일 직교 사각 셀에서 `l_fd_f=(A_L+A_R)/2`이면 차이는 `\frac18(A_L-A_R)(h_L-h_R)u_f^2`이다. 이 경우에는 두 식이 일반적으로 같지 않다. 코드 진단의 다른 공간 가중치는 문서에 없는 처리이다. 이 진단값에 문서의 반이산 에너지 보존 증명을 자동 적용하지 않는다. 이 비교는 두 유효 셀에 공유된 내부 면의 진단 가중치에 한정한다. C는 반이산 에너지 정의와 다른 출력 분배식을 기술문서에 설명하지 않은 점이며 유동 갱신의 보존 결함으로 분류하지 않는다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-022 | (5.7) 정확 운동량식 | `swashtech PDF p.71`(인쇄 p.63): `\frac{d\gamma_{\tilde e}^{(1)}(t)}{dt}+\tilde\alpha_{\tilde e}^{(1)}(t)+g\overline{\tilde\eta^{(0)}}_{\tilde e}\bigl(\tilde\zeta_{\tilde v_r}^{(0)}(t)-\tilde\zeta_{\tilde v_l}^{(0)}(t)\bigr)=0`<br>`swashuse PDF p.96`(인쇄 p.88): `a robust and efficient upwind-biased scheme for the horizontal advection terms in the momentum equation has been implemented`<br>`swashtech PDF p.103`(인쇄 p.95) 식 (7.5)의 이류형 항등식 | `src/SwashExpDepUflow.ftn90:1034` `zgrad = grav * rdx * hf * ( s0(icellr) - s0(icelll) )`; `src/SwashExpDepUflow.ftn90:1038` `contrib = advec(iface) / humn(iface) + ( zgrad + pgrad(iface) + qgrad(iface) - windu(iface) - visc(iface) + corf(iface) ) / hum(iface)` | C 문서 누락 | 해석: 압력 경사 항의 구조는 같다. 실제 비구조 이류는 상류 속도차와 고차 보정을 사용한다(ST2-045·048). 상류법 자체는 `swashuse PDF p.96`(인쇄 p.88)에 설명되어 있다. C는 swashtech §5.4의 정확 운동량식에서 실제 이류형 구현으로 이어지는 설명 누락으로 한정한다. 정확 적분식 자체의 수학적 오류를 뜻하지 않는다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-039 | 전체 부피 — 번호 없음 | `swashtech PDF p.75`(인쇄 p.67): `\sum_{c\in\Omega}A_ch_c`<br>`swashuse PDF p.122`(인쇄 p.114): `with [itest] = 30, one may check mass and energy conservation, if appropriate.` | `src/SwashExpDepUflow.ftn90:1741` `vol = vol + s1(icell)`; `src/SwashExpDepUflow.ftn90:1730` `! calculate total displaced volume of water (reference is at z = 0) and energy`<br>`src/SwashReadInput.ftn90:2780` `if ( KEYWIS ('TEST') ) then`; `src/SwashReadInput.ftn90:2781` `call ININTG ('ITEST',ITEST,'STA',30)`<br>`src/SwashCompUnstruc.ftn90:67` `if ( .not.momskip ) call SwashCompUFlow`<br>`src/SwashCompUFlow.ftn90:70–102`의 층 수·시간 방법별 네 유동 호출<br>`src/SwashExpDepUflow.ftn90:1733` `if ( ITEST >= 30 ) then`; `src/SwashExpDepUflow.ftn90:1762` `write(PRINTF,102) vol`<br>`src/SwashImpDepUflow.ftn90:1923`,<br>`src/SwashExpLayUflow.ftn90:2865`,<br>`src/SwashImpLayUflow.ftn90:3036`도 `vol = vol + s1(icell)`. 최초 공개 소스 `8756667 2022-09-03`의 같은 네 파일 `8756667:src/SwashExpDepUflow.ftn90:1048`, `8756667:src/SwashImpDepUflow.ftn90:1110`, `8756667:src/SwashExpLayUflow.ftn90:2062`, `8756667:src/SwashImpLayUflow.ftn90:2127`에도 같은 대입이 있다. main blame의 `f7ebbca 2024-08-02`는 소스 재등록 시점이다. `7949227` 이후 `608ffd7`·`9554c98`은 이 네 파일을 바꾸지 않았다. [git 판정 근거](../../../_staging/recovery/compare/SWASH-git-verify-E2.md) | E 코드 결함 후보 | 해석: 비구조 유동 네 경로의 ITEST 체적 진단은 셀 면적 없이 수위를 합한다. `z=0` 기준 변위 체적은 `\sum A_c\zeta_c`이므로 출력값은 일반 삼각망의 변위 체적과 다르다. `TEST 30`과 실제 유동 호출로 도달하는 진단이다. 이 대입에는 비활성 전처리 접두어가 없다. 물리 갱신식과 구분한 출력 결함 후보이며 E·강함을 유지한다. 최초 공개 소스에도 같은 식이 있고 12.01 뒤 두 코드 커밋에도 그대로 남는다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| theory-unstructured:ST2-045 | (5.21) 운동량 발산 | `swashtech PDF p.77`(인쇄 p.69): `\mathbf a_c=\frac1{A_c}\sum_{f\in\partial c}s_{c,f}\phi_f^{(n-1)}\mathbf u_f`<br>`swashuse PDF p.96`(인쇄 p.88): `a robust and efficient upwind-biased scheme for the horizontal advection terms in the momentum equation has been implemented`<br>`swashtech PDF p.103`(인쇄 p.95) 식 (7.5)의 이류형 항등식 | `src/SwashExpDepUflow.ftn90:288` `if ( quf(icell,jf) < 0. ) cadv = cadv + quf(icell,jf) * ( nx * uvc(icellu,1) + ny * uvc(icellu,2) - u0(iface) )`<br>`src/SwashExpDepUflow.ftn90:230` `if ( .not.linswe ) then`; `src/SwashExpDepUflow.ftn90:234` `if ( face(iface)%atti(FMARKER) == 0 .and. wetu(iface) == 1 ) then`; `src/SwashExpDepUflow.ftn90:370` `if ( propsc /= 1 ) then`; `src/SwashExpDepUflow.ftn90:482–485`의 `hox = 0.5 * max(0.,lwfac) * fluxlim(grad1x,grad2x)`, `hoy = 0.5 * max(0.,lwfac) * fluxlim(grad1y,grad2y)`, `cadv = cadv + quf(icell,jf) * ( nx * hox + ny * hoy )` | C 문서 누락 | 해석: 비선형 내부 젖은 면의 기본 이류항은 유입 플럭스에 상류 재구성 속도와 대상 면 속도의 차를 곱한다. 선택한 공간 기법에 따른 고차 보정도 더한다. `swashuse PDF p.96`(인쇄 p.88)은 비구조 상류 기법을 설명한다. C는 swashtech §5.5.4의 운동량 발산식과 실제 이류형 구현의 연결 설명 누락으로 한정한다. 항별 차이만으로 운동량 비보존을 단정하지 않는다. ST2-022·047·048·060·061은 같은 구현을 가리킨다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-046 | (5.22) 이류의 양쪽 길이 가중 | `swashtech PDF p.77`(인쇄 p.69): `\tilde\alpha_{\tilde e}^{(1)}=\int_{\tilde e}\mathbf a\cdot\mathbf t_{\tilde e}\,dl\approx\mathbf a_l\cdot\mathbf r_{fl}-\mathbf a_r\cdot\mathbf r_{fr}=(l_{fl}\mathbf a_l+l_{fr}\mathbf a_r)\cdot\mathbf t_{\tilde e}` | `src/SwashExpDepUflow.ftn90:250` `faca  = finp`; `src/SwashExpDepUflow.ftn90:257` `faca  = 1. - finp`; `src/SwashExpDepUflow.ftn90:296` `advec(iface) = advec(iface) + faca * cadv / area` | F 표기 차이 | 해석: 코드가 저장하는 양은 선적분을 `l_{\tilde e}`로 나눈 값이다. `\mathrm{finp}=l_{fl}/l_{\tilde e}`와 `1-\mathrm{finp}=l_{fr}/l_{\tilde e}`를 대입하면 가중 연산은 같다. `\mathbf a_c` 자체의 차이는 ST2-045다. |
| theory-unstructured:ST2-047 | 운반 속도의 산술 평균·반대칭 조건 — 번호 없음 | `swashtech PDF p.77`(인쇄 p.69): `\bar{\mathbf u}_f=\frac12(\mathbf u_l+\mathbf u_r)`; `we must use the following interpolation`<br>`swashuse PDF p.96`(인쇄 p.88): `a robust and efficient upwind-biased scheme for the horizontal advection terms in the momentum equation has been implemented`<br>`swashtech PDF p.103`(인쇄 p.95) 식 (7.5)의 이류형 항등식 | `src/SwashExpDepUflow.ftn90:280–284` `if ( u0(ifacel) > 0. ) then`, `icellu = icelll`, `else`, `icellu = icellr`, `endif`; `src/SwashExpDepUflow.ftn90:288` `if ( quf(icell,jf) < 0. ) cadv = cadv + quf(icell,jf) * ( nx * uvc(icellu,1) + ny * uvc(icellu,2) - u0(iface) )` | C 문서 누락 | 해석: 문서는 에너지 보존형 반대칭 이류 연산자의 산술 운반 속도를 설명한다. 비구조 코드는 상류 셀을 선택한 기본항에 선택 기법의 고차 보정을 더한다(ST2-045). 상류 기법은 `swashuse PDF p.96`(인쇄 p.88)에 명시되어 있다. C는 swashtech §5.5.4의 산술 평균 조건과 실제 옵션의 관계 설명 누락으로 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-060 | (5.31) 쌍대 운동량식 | `swashtech PDF p.80`(인쇄 p.72): `l_{\tilde e}\frac{d\tilde h_fu_{\tilde e}}{dt}+(l_{fl}\mathbf a_l+l_{fr}\mathbf a_r)\cdot\mathbf t_{\tilde e}+g\bar h_{\tilde e}(\zeta_r-\zeta_l)=0`<br>`swashuse PDF p.96`(인쇄 p.88): `a robust and efficient upwind-biased scheme for the horizontal advection terms in the momentum equation has been implemented`<br>`swashtech PDF p.103`(인쇄 p.95) 식 (7.5)의 이류형 항등식 | `src/SwashExpDepUflow.ftn90:1038` `contrib = advec(iface) / humn(iface) + ( zgrad + pgrad(iface) + qgrad(iface) - windu(iface) - visc(iface) + corf(iface) ) / hum(iface)`<br>`src/SwashUpdateUDepths.ftn90:198` `humn = 1.5*hum - 0.5*humo` | C 문서 누락 | 해석: 수위 경사와 양쪽 길이 가중의 구조는 같다. 실제 시간 갱신은 `humn` 외삽을 사용한다. 실제 이류형 구현은 ST2-045와 같다. 상류법 자체는 `swashuse PDF p.96`(인쇄 p.88)에 있다. C는 swashtech §5.6의 반이산 운동량식과 이 시간 갱신·이류 구현을 연결하는 설명 누락으로 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-061 | (5.32) 면 운동량식 | `swashtech PDF p.81`(인쇄 p.73): `\Delta s_f\frac{d\tilde h_fu_f}{dt}+(\Delta s_{fl}\mathbf a_l+\Delta s_{fr}\mathbf a_r)\cdot\mathbf n_f+g\bar h_f(\zeta_r-\zeta_l)=0`; `\mathbf t_{\tilde e}\cdot\mathbf n_f=1`<br>`swashuse PDF p.96`(인쇄 p.88): `a robust and efficient upwind-biased scheme for the horizontal advection terms in the momentum equation has been implemented`<br>`swashtech PDF p.103`(인쇄 p.95) 식 (7.5)의 이류형 항등식 | `src/SwashExpDepUflow.ftn90:1034` `zgrad = grav * rdx * hf * ( s0(icellr) - s0(icelll) )`; `src/SwashExpDepUflow.ftn90:1044` `u1(iface) = ( u0(iface) - dt * contrib ) / denom` | C 문서 누락 | 해석: 문서 식 (5.31)을 직교 메트릭으로 표현한 식이다. 압력 경사의 길이는 코드에서 역수 `rdx`로 들어간다. 실제 이류형 구현과 시간 외삽은 ST2-045·048·060과 같다. C는 swashtech §5.6의 식과 그 구현을 연결하는 설명 누락으로 한정한다. 상류법 자체의 누락은 아니다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-108 | 전체 외력 — 번호 없음 | `swashtech PDF p.91`(인쇄 p.83): `\frac{\partial h\mathbf u}{\partial t}+\cdots=-\frac12\nabla(hp_b)+p_b\nabla d+\nabla\cdot(\nu_hh\nabla\mathbf u)-c_f\lVert\mathbf u\rVert\mathbf u+\boldsymbol\tau_w-f\hat{\mathbf z}\times h\mathbf u` | `src/SwashExpDepUflow.ftn90:1038` `contrib = advec(iface) / humn(iface) + ( zgrad + pgrad(iface) + qgrad(iface) - windu(iface) - visc(iface) + corf(iface) ) / hum(iface)`; `src/SwashExpDepUflow.ftn90:1040` `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )` | F 표기 차이 | 해석: 음의 우변 힘은 `contrib`에 양으로 들어간다. 바람·점성은 빼서 우변의 양의 힘을 구현한다. 바닥 마찰은 분모에 넣는다. 문서 밖의 기압·밀도 강제도 코드에 있다. |
| theory-unstructured:ST2-111 | (5.42) 압력 경사·점성 | `swashtech PDF p.92`(인쇄 p.84): `l_{\tilde e}\frac{d\tilde h_fu_{\tilde e}}{dt}+\cdots=-\frac12(h_rp_r-h_lp_l)+(l_{fl}\mathbf d_l+l_{fr}\mathbf d_r)\cdot\mathbf t_{\tilde e}` | `src/SwashExpDepUflow.ftn90:520` `gmat(iface,1) = -rdx * ( (0.5-finp)*dps(icelll) + 0.5*s0(icelll) +      finp * dps(icellr) )`; `src/SwashExpDepUflow.ftn90:521` `gmat(iface,2) =  rdx * ( (finp-0.5)*dps(icellr) + 0.5*s0(icellr) + (1.-finp) * dps(icelll) )`; `src/SwashExpDepUflow.ftn90:651` `visc(iface) = visc(iface) + faca * cvisc / area` | F 표기 차이 | 해석: 코드는 압력 경사와 바닥 반력을 합친 `gmat`를 만든다. 이 결합식의 압력 경사 계수는 `1/2`다. 점성의 길이 가중은 (5.22)와 같다. [10-15 전수 검증 정정] |
| theory-unstructured:ST2-117 | (5.44) 바닥 반력과 다른 외력 선적분 | `swashtech PDF p.93`(인쇄 p.85): `l_{\tilde e}\frac{d\tilde h_fu_{\tilde e}}{dt}+\cdots=\bar p_{\tilde e}(d_r-d_l)+\int_{\tilde e}[-c_f\lVert\mathbf u\rVert\mathbf u+\boldsymbol\tau_w-f\hat{\mathbf z}\times h\mathbf u]\cdot\mathbf t_{\tilde e}\,dl` | `src/SwashExpDepUflow.ftn90:556` `qgrad(iface) = gmat(iface,1) * q(icelll) + gmat(iface,2) * q(icellr)` | F 표기 차이 | 해석: 실제 채택 평균은 (5.46)이다. `gmat`는 그 바닥 반력을 압력 경사와 합쳐 저장한다. |
| theory-unstructured:ST2-119 | (5.46) 채택한 압력 가중 평균 | `swashtech PDF p.93`(인쇄 p.85): `\tilde p_f=\frac{\Delta s_{fl}}{\Delta s_f}p_l+\frac{\Delta s_{fr}}{\Delta s_f}p_r`; `The latter was chosen` | `src/SwashExpDepUflow.ftn90:520` `gmat(iface,1) = -rdx * ( (0.5-finp)*dps(icelll) + 0.5*s0(icelll) +      finp * dps(icellr) )`; `src/SwashExpDepUflow.ftn90:521` `gmat(iface,2) =  rdx * ( (finp-0.5)*dps(icellr) + 0.5*s0(icellr) + (1.-finp) * dps(icelll) )` | F 표기 차이 | 해석: 압력 경사를 전개하면 바닥 경사 항의 왼쪽 압력 가중치는 `finp`다. 오른쪽 압력 가중치는 `1.-finp`다. |
| theory-unstructured:ST2-122 | 외력의 길이 가중 — 번호 없음 | `swashtech PDF p.93`(인쇄 p.85): `\int_{\tilde e}[-c_f\lVert\mathbf u\rVert\mathbf u+\boldsymbol\tau_w-f\hat{\mathbf z}\times h\mathbf u]\cdot\mathbf t_{\tilde e}\,dl\approx\mathbf S_l\cdot\mathbf r_{fl}-\mathbf S_r\cdot\mathbf r_{fr}=(l_{fl}\mathbf S_l+l_{fr}\mathbf S_r)\cdot\mathbf t_{\tilde e}` | `src/SwashExpDepUflow.ftn90:758` `cbot(iface) = cbot(iface) + faca * cfricu(icell) * utot / hum(iface)`; `src/SwashExpDepUflow.ftn90:953` `cfu(iface,1) = cfu(iface,1) + faca * fcor(icell,1) * ( ny * ux - nx * uy ) / area` | F 표기 차이 | 해석: 코드의 `faca`는 부분 길이 비율이다. 선적분을 전체 길이로 나눈 같은 가중이다. |
| theory-unstructured:ST2-128 | (5.47) 코리올리 선적분 | `swashtech PDF p.94`(인쇄 p.86): `\int_{\tilde e}(f\hat{\mathbf z}\times h\mathbf u)\cdot\mathbf t_{\tilde e}\,dl\approx(\Delta s_{fl}\mathbf c_l+\Delta s_{fr}\mathbf c_r)\cdot\mathbf n_f` | `src/SwashExpDepUflow.ftn90:953` `cfu(iface,1) = cfu(iface,1) + faca * fcor(icell,1) * ( ny * ux - nx * uy ) / area` | F 표기 차이 | 해석: `ny*ux-nx*uy`는 `\mathbf n_f\cdot(\hat{\mathbf z}\times\mathbf q_c)`다. `faca`는 각 부분 길이를 전체 길이로 나눈 값이다. |
| theory-unstructured:ST2-130 | 회전 벡터 전개 — 번호 없음 | `swashtech PDF p.94`(인쇄 p.86): `\hat{\mathbf z}\times h_c\mathbf u_c=\frac1{A_c}\sum_{f\in\partial c}s_{c,f}h_fu_fS_f\hat{\mathbf z}\times\mathbf r_{fc}=\frac1{A_c}\sum_{f\in\partial c}s_{c,f}h_fu_fS_f\mathbf t_{fc}` | `src/SwashExpDepUflow.ftn90:953` `cfu(iface,1) = cfu(iface,1) + faca * fcor(icell,1) * ( ny * ux - nx * uy ) / area` | F 표기 차이 | 해석: 코드가 먼저 두 플럭스 성분을 합한 뒤 회전·투영한다. 회전·투영은 선형이므로 합 안에서 수행한 식과 같다. |
| theory-unstructured:ST2-136 | (5.49) 전체 면 운동량식 | `swashtech PDF p.95`(인쇄 p.87): `\begin{aligned}\Delta s_f\frac{d\tilde h_fu_f}{dt}+(\Delta s_{fl}\mathbf a_l+\Delta s_{fr}\mathbf a_r)\cdot\mathbf n_f+g\bar h_f(\zeta_r-\zeta_l)={}&-1/2(h_rp_r-h_lp_l)+\tilde p_f(d_r-d_l)\\&+(\Delta s_{fl}\mathbf d_l+\Delta s_{fr}\mathbf d_r)\cdot\mathbf n_f\\&-(\Delta s_{fl}c_{f,l}\lVert\mathbf u_l\rVert+\Delta s_{fr}c_{f,r}\lVert\mathbf u_r\rVert)u_f\\&+\Delta s_f\boldsymbol\tau_{w,f}\cdot\mathbf n_f\\&-(\Delta s_{fl}\mathbf c_l+\Delta s_{fr}\mathbf c_r)\cdot\mathbf n_f\end{aligned}` | `src/SwashExpDepUflow.ftn90:1038` `contrib = advec(iface) / humn(iface) + ( zgrad + pgrad(iface) + qgrad(iface) - windu(iface) - visc(iface) + corf(iface) ) / hum(iface)`; `src/SwashExpDepUflow.ftn90:1040` `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )` | C 문서 누락 | 해석: 압력·점성·마찰·바람·Coriolis의 공간 계수는 ST2-108·111·117·119·122·124·126·128·130에서 대조했다. 실제 이류형 구현과 시간 외삽은 ST2-045·060·135와 같다. C는 `swashtech PDF p.95`(인쇄 p.87) 식 (5.49)와 이 완전 이산 갱신의 연결 설명 누락으로 한정한다. 이 식에 기압·밀도 강제·상대 바람의 음해 처리가 모두 적혀 있지 않다는 사실을 두 매뉴얼 전체의 기능 누락으로 확대하지 않는다. [10-15 결론 검증 정정] |
| theory-unstructured:ST2-144 | (6.2) 양의 유속 운동량 업데이트 | `swashtech PDF p.98`(인쇄 p.90): `l_{\tilde e}\frac{\tilde h_f^nu_f^{n+1/2}-\tilde h_f^{n-1}u_f^{n-1/2}}{\Delta t}+\frac1{A_{c_l}}(\mathbf x_f-\mathbf x_{c_l})\cdot\sum_{k\in\partial c_l}s_k\hat h_k^nu_k^{n-1/2}S_k\mathbf u_{c_l,k}+g\bar h_f^n(\zeta_{c_r}^n-\zeta_{c_l}^n)=0`; `assume uf > 0`<br>`swashuse PDF p.96`(인쇄 p.88)의 비구조 상류 이류 설명(ST2-045) | `src/SwashExpDepUflow.ftn90:243` `do l = 1, 2`; `src/SwashExpDepUflow.ftn90:288` `if ( quf(icell,jf) < 0. ) cadv = cadv + quf(icell,jf) * ( nx * uvc(icellu,1) + ny * uvc(icellu,2) - u0(iface) )`<br>`src/SwashUpdateUDepths.ftn90:198` `humn = 1.5*hum - 0.5*humo`<br>`src/SwashExpDepUflow.ftn90:296` `advec(iface) = advec(iface) + faca * cadv / area`; `src/SwashExpDepUflow.ftn90:1038`의 `advec(iface) / humn(iface)` | C 문서 누락 | 해석: 문서는 양의 면 유속에서 상류 셀 하나의 운동량 합을 사용한다. 코드는 양쪽 셀의 유입 속도차 기여를 길이로 가중한다(ST2-045). 시간 갱신에서는 두 수심·속도 곱의 차 대신 `humn` 외삽을 사용한다. C는 `swashtech PDF p.98`(인쇄 p.90) 식 (6.2)와 이 실제 갱신의 연결 설명 누락이다. 상류법 자체는 `swashuse PDF p.96`(인쇄 p.88)에 설명되어 있다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-146 | 시간 이류의 셀 벡터 — 번호 없음 | `swashtech PDF p.98`(인쇄 p.90): `\mathbf u_c=\frac1{A_ch_c}\sum_f s_f\hat h_f^nu_f^{n-1/2}S_f(\mathbf x_f-\mathbf x_c)` | `src/SwashExpDepUflow.ftn90:226` `call perot ( u0, 1, 1 )`<br>`src/SwashUServ.ftn90:148` `uvc(icell,k,1) = uvc(icell,k,1) + rsgn * lf * ( xf - xc ) * u(iface,k)` | C 문서 누락 | 해석: `swashtech PDF p.98`(인쇄 p.90)의 식은 면 수심을 곱한 플럭스를 재구성한 뒤 셀 수심으로 나눈다. 이류용 `perot(u0)`는 면 수심을 곱하지 않은 면 속도로 셀 중심 속도 벡터를 재구성한다. C는 제6장의 이 재구성식과 실제 이류용 벡터의 차이를 설명하지 않은 부분이다. 코리올리용 플럭스 재구성은 ST2-129와 구분한다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| theory-unstructured:ST2-147 | (6.3) 수위 업데이트 | `swashtech PDF p.98`(인쇄 p.90): `A_c\frac{\zeta_c^{n+1}-\zeta_c^n}{\Delta t}+\sum_f s_f\hat h_f^nu_f^{n+1/2}S_f=0`<br>`swashuse PDF p.161`(인쇄 p.153) 및<br>`misc/swash.edt:273`의 `EXPL [cfllow] [cflhig]` 뒤 `HANCock`·`EULer` 선택 구문 | `src/SwashExpDepUflow.ftn90:1544–1547` `! solve global continuity equation by means of a second order predictor-corrector scheme`, `! (jhk = 1: RK3, jhk = 2: Hancock, jhk = 3: first order Euler)`, `!`, `do j = jhk, 3`; `src/SwashExpDepUflow.ftn90:1598` `qn(iface) = lf * hu(iface) * u1(iface)`<br>`src/SwashInit.ftn90:393` `jhk        =  1     ! RK3`<br>`src/SwashReadInput.ftn90:1886–1891` `if ( KEYWIS ('EUL') ) then`, `jhk = 3`, `else if ( KEYWIS ('HANC') ) then`, `jhk = 2`, `else if ( KEYWIS ('RK3') ) then`, `jhk = 1`<br>`src/SwashExpDepUflow.ftn90:1667` `if ( j <= 2 ) call SwashUpdUDepu ( u1 )` | C 문서 누락 | 해석: 명시적 경로의 `jhk=3`은 한 번 전진한다. 기본 `jhk=1`은 예측·보정 단계에서 면 수심과 플럭스를 다시 계산한다. 입력의 `EUL`·`HANC`·`RK3`가 단계 선택을 바꾼다. Hancock·Euler 구문은 swashuse 부록 p.161에도 있다. C는 swashtech 제6장에 없는 단계별 수심 갱신과 RK3 기본 선택의 설명으로 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-150 | CFL — 번호 없음 | `swashtech PDF p.98`(인쇄 p.90): `C_f=\frac{\Delta t(\sqrt{g\hat h_f^{n+1}}+\lvert u_f^{n+1/2}\rvert)}{l_{\tilde e}}<1` | `src/SwashExpDepUflow.ftn90:1773` `rdx  = face(iface)%attr(FACEDISTG)`; `src/SwashExpDepUflow.ftn90:1784` `dep = finp * ( s1(icelll) + dps(icelll) ) + (1.-finp) * ( s1(icellr) + dps(icellr) )`<br>`src/SwashExpDepUflow.ftn90:1796` `if ( wetu(iface) == 1 ) then`; `src/SwashExpDepUflow.ftn90:1798` `if ( face(iface)%atti(FMARKER) == 0 ) then`; `src/SwashExpDepUflow.ftn90:1800` `cfl = rdx * dt * ( sqrt(grav*dep) + abs(u1(iface)) )`<br>`src/SwanGridFace.ftn90:408–411`의 무게중심 간 거리와 `FACEDISTG` | C 문서 누락 | 해석: 원문 쪽 이미지의 수심 기호는 `\hat h_f^{n+1}`이다. 이 수심은 같은 쪽의 상류 수위 정의를 따른다. 코드는 내부 젖은 면에서 길이 가중 수심 `dep`를 사용한다. 따라서 파속과 유속을 더하는 구조 및 시간층은 같지만 수심 정의는 다르다. 코드의 분모는 무게중심 간 거리다. 문서의 `l_{\tilde e}`는 계산 중심에서 면 중점까지의 거리 합이다. 정삼각 격자에서는 거리들이 같아도 일반 수위장에서 상류 수심과 가중 수심까지 같아지는 것은 아니다. C는 tech p.98 CFL식과 실제 진단의 수심·거리 정의 차이에 한정한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-357 | 수평 이류의 제한자·Lax–Wendroff 보정 | `swashuse PDF p.95–97`(인쇄 p.87–89)은 비구조 r-ratio와 고차·제한자 선택을 설명한다.<br>`swashtech PDF p.108`(인쇄 p.100)은 1차 상류법도 사용한다고 적는다. | `src/SwashExpDepUflow.ftn90:368–374` `propsc = nint(pnums(6))`, `!`, `if ( propsc /= 1 ) then`, `!`, `kappa  = pnums(7)`, `mbound = pnums(8)`, `phieby = pnums(9)`; `src/SwashExpDepUflow.ftn90:418` `lwfac = 1. - rdx * dt * abs(u0(ifacel))`; `src/SwashExpDepUflow.ftn90:450–478`은 상류 꼭짓점의 면적 가중 속도와 `grad1x`·`grad2x`·`grad1y`·`grad2y`를 계산한다; `src/SwashExpDepUflow.ftn90:482–485` `hox = 0.5 * max(0.,lwfac) * fluxlim(grad1x,grad2x)`, `hoy = 0.5 * max(0.,lwfac) * fluxlim(grad1y,grad2y)`, `!`, `cadv = cadv + quf(icell,jf) * ( nx * hox + ny * hoy )` | C 문서 누락 | 코드는 상류 꼭짓점의 면적 가중 속도로 두 경사를 만든다. `propsc=1`에서만 이 고차 보정을 생략한다. C는 이 면적 가중 경사와 Lax–Wendroff 시간 보정 계수에 한정한다. [10-15 결론 검증 보완] [10-15 전수 검증 보완] |
| theory-unstructured:ST2-376 | 밀도와 기압의 수평 힘 | `swashtech PDF p.91`(인쇄 p.83)의 힘 목록에는 밀도·기압 항이 없다.<br>`swashuse PDF p.22–23`(인쇄 p.14–15)은 기압 입력과 경압 압력경사를 설명한다. | `src/SwashExpDepUflow.ftn90:803` `if ( idens /= 0 ) then`; `src/SwashExpDepUflow.ftn90:818` `pgrad(iface) = 0.5 * grav * rdx * hum(iface) * hum(iface) * (rho(icellr) - rho(icelll)) / rhow`; `src/SwashExpDepUflow.ftn90:838` `if ( svwp ) then`; `src/SwashExpDepUflow.ftn90:853` `pgrad(iface) = pgrad(iface) + rdx * hum(iface) * (patm(icellr) - patm(icelll)) / rhow` | C 문서 누락 | 밀도 힘에는 수심 제곱과 `g/2`가 들어간다. 기압 힘에는 수심과 물 밀도의 역수가 들어간다. 운동량 업데이트는 두 경사를 뺀다. C는 두 기능의 존재가 아니라 비구조 면의 수심·밀도·기압을 결합하는 이산식에 한정한다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-380 | 연속식 예측·수정의 실제 절차 | `swashtech PDF p.98`(인쇄 p.90)의 (6.3)은 수위 갱신식 하나를 적는다.<br>`swashuse PDF p.99–101`(인쇄 p.91–93)은 시간 적분을 설명하며 p.161의 구문에는 EULER·HANCOCK이 있다. | `src/SwashInit.ftn90:393` `jhk        =  1     ! RK3`<br>`src/SwashExpDepUflow.ftn90:1547` `do j = jhk, 3`; `src/SwashExpDepUflow.ftn90:1553` `fh = 0.5`; `src/SwashExpDepUflow.ftn90:1559` `fh = 1.`; `src/SwashExpDepUflow.ftn90:1667` `if ( j <= 2 ) call SwashUpdUDepu ( u1 )`; 다층 대응<br>`src/SwashExpLayUflow.ftn90:2604` `do j = jhk, 3`<br>`src/SwashReadInput.ftn90:1858–1892`의 TIMEI EXPLICIT 분기는 EULER·HANCOCK·RK3를 각각 jhk=3·2·1로 읽는다. | C 문서 누락 | `jhk=1`은 두 예측 단계와 한 수정 단계를 수행한다. `jhk=2`는 예측 한 단계와 수정 한 단계를 수행한다. `jhk=3`은 수정 한 단계만 수행한다. 앞선 예측 단계의 수심을 다음 플럭스에 사용한다. C는 세 내부 단계의 실제 반복·수심 재계산에 한정한다. [10-15 결론 검증 보완] |
