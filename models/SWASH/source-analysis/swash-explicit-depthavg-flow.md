---
title: "SWASH 명시적 수심평균 flow solver — ExpDep 1DH/2DH/Uflow 시간적분"
model: SWASH
component: src (explicit depth-averaged flow)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashExpDep1DHflow.ftn90 (Purpose/Method 헤더 :45-67, 시간적분·연속·CFL :199-1666), SwashExpDep2DHflow.ftn90 (헤더 :46-67, 곡선좌표 metric·SIP Poisson·CFL :1271-4977), SwashExpDepUflow.ftn90 (헤더 :42-61, 삼각망 face/cell·Euler explicit advection·BiCGSTAB :228-1807) 의 file:line 인용."
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

미지수는 **face 법선속도** `u1(nfaces)` (`:91`). 셀 중심속도 벡터는 **Perot's formula**로 face flux로부터 재구성 (`:946` "compute the depth-integrated velocity vector at current cell using Perot's formula", `uvc(ncells,2)` circumcenter 속도 `:92`). 1차 upwind advection은 면을 공유하는 좌/우 셀의 face flux를 upwind 셀 기준으로 합산 (`:228-346`):

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

`rdx = face(iface)%attr(FACEDISTC)` — 인접 circumcenter 간 거리 역수 (`:1021`).

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

세 식 모두 $\sqrt{gh}$(천수파속) + 유속의 advective 부분 합 — 명시적 운동량 적분의 CFL 안정조건 진단. 2DH는 2차원 대각 셀에 맞춰 $\sqrt{\Delta x^{-2}+\Delta y^{-2}}$. 계산된 `cflmax`는 module 변수로 노출(파일 내 정의 없음, `SwashTimecomm` 추정 — ⚠ 미확인, 본 파일에서는 대입만 함).

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
- 닫힌 영역 total displaced volume `vol` + total energy `ener`(potential `:1629` + kinetic `:1634-1636`)

reflective 경계 닫힌 영역에서의 보존성 점검용 (주석 `:1609`).

## 10. 요약 — 핵심 메커닉

1. **반-명시(semi-implicit)**: 운동량 advection·수위경사는 명시적(leap-frog/MacCormack), 바닥마찰·식생·다공질·바람은 Euler implicit(분모), 비정수압 압력만 theta-scheme 암시적 projection.
2. **세 변종의 본질적 차이는 (a) 격자 metric (직교/곡선 Jacobian/삼각 face-cell), (b) advection 시간스킴 (1DH·2DH=MacCormack vs U=Euler+Lax-Wendroff), (c) Poisson solver (tridiag / SIP / BiCGSTAB)** 세 가지.
3. **연속식은 jhk로 RK3/Hancock/Euler 선택**하는 예측-수정 구조 (8.01에서 Hancock 도입).
4. **압력은 2차 정확도 pressure-correction**(projection)으로 풀며 1-layer depth-averaged Keller-box 닫힘 항(`-2/hs` 류)을 동반.
5. CFL은 step 말미 진단만 — 자동 dt 조정 로직은 이 파일들에 없음(외부).

source-needed: `cflmax`·`jhk`·`iproj`·`ihydro` 등 module 변수의 실제 선언·자동 dt 제어 로직은 본 세 파일 밖(SwashTimecomm/SwashCommdata3/SwashReadInput)이므로 본 노트 범위에서는 대입·사용 지점만 인용. `tridiag`/`sip`/`bicgstabu` 내부 알고리즘은 별도 파일(미검수).
