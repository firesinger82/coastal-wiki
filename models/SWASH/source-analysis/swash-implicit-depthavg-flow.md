---
title: "SWASH 암시적 수심평균 flow solver — 1DH/M1DH/M2DH/Uflow (theta-스킴·tridiag·pressure correction)"
model: SWASH
component: src (implicit depth-averaged flow / time integration)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashImpDep1DHflow.ftn90(Purpose/Method 헤더 :41-63, theta 설정 :182-184, 명시적 momentum predictor :667-704, continuity tridiag 시스템 build :851-955, Poisson build/solve :1377-1426, 속도/압력 보정 :1467-1531), SwashImpDepM1DHflow.ftn90(Method 헤더 :42-68, teta=0.5 :179, Crank-Nicolson 암시 momentum tridiag :447-602), SwashImpDepM2DHflow.ftn90(Method :42-68, amat 5점 sip u/v :655-744·1105-1194, continuity amat build :1240-1318, newton2D :1523, Poisson sip :1991), SwashImpDepUflow.ftn90(Purpose/Method :41-60, theta :188-190, 명시 face momentum :996-1045, pcgu/newtonU :1140·1233, bicgstabu Poisson :1749, 속도보정 :1779) file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 암시적 수심평균 flow solver — 1DH / M1DH / M2DH / Uflow

> 비정수압·수심평균(2D 수직적분) 천수방정식의 시간적분 커널 4종. theta-스킴(연속·수위경사) + pressure correction(비정수압)으로 구성. 경로: raw/source_code/swash/src/ — SwashImpDep1DHflow.ftn90, SwashImpDepM1DHflow.ftn90, SwashImpDepM2DHflow.ftn90, SwashImpDepUflow.ftn90.

> **범위 주의**: 본 노트는 *수심평균(depth-averaged)* 암시적 flow에 한정. `SwashImpDep2DHflow`(구조격자 2DH, 비-M)는 기존 pressure-solver 노트가 다루므로 제외. 다층(multi-layer) `SwashImpLay*`도 별도.

---

## 1. 공통 정체성과 4 변종의 분류

| 파일 | 차원/격자 | momentum 시간적분 | M(=momentum-conservative) | 선형 solver |
|---|---|---|---|---|
| `SwashImpDep1DHflow` | 1DH 구조격자 | predictor-corrector(MacCormack), 명시 | 비-M(flux-limited, 에너지/모멘텀 선택) | `tridiag` |
| `SwashImpDepM1DHflow` | 1DH 구조격자 | Crank-Nicolson, **암시** | M(엄밀 모멘텀/에너지 보존, skew-symmetric) | `tridiag` |
| `SwashImpDepM2DHflow` | 2DH 곡선격자 | Crank-Nicolson, **암시** | M | `sip`(5점), `newton2D` |
| `SwashImpDepUflow` | 비구조 삼각망 | Euler implicit(friction만), advec 명시 | momentum-conservative | `pcgu`, `newtonU`, `bicgstabu` |

네 파일 모두 동일한 큰 흐름을 따른다: ① mass flux/advection velocity 계산 → ② 비정수압 압력 gradient matrix `gmat` build → ③ 중간(intermediate) 수평속도 → ④ theta-스킴 연속방정식으로 수위보정 `ds` 선형계 풀이 → ⑤ 수위경사로 속도보정 → ⑥ Keller-box w-momentum → ⑦ Poisson eq → pressure correction `dq` → ⑧ 속도/압력 최종 보정 → mass flux 갱신.

**M 접미사 확인됨**: M-변종 헤더는 "strictly mass and momentum conservative at the discrete level, and strictly energy conservative in discrete space ... The discrete advective operator is skew-symmetric" 라고 명시(`SwashImpDepM1DHflow.ftn90:42-48`, 동일 문구 `SwashImpDepM2DHflow.ftn90:42-48`). 즉 M = momentum/energy-conservative skew-symmetric 변종이 맞다.

---

## 2. theta-스킴(반암시) 기본 구조 — pnums 매핑

세 변종 공통으로 시간적분 implicitness factor를 `pnums`에서 읽음.

| 변수 | 의미 | 출처 |
|---|---|---|
| `teta`/`theta` = `pnums(1)` | 연속방정식·mass flux 시간가중 | `SwashImpDep1DHflow.ftn90:182`; `SwashImpDepUflow.ftn90:188` |
| `teta2`/`theta2` = `pnums(4)` | 수위경사(surface gradient) 시간가중 | `SwashImpDep1DHflow.ftn90:183`; `:189` |
| `theta3` = `pnums(5)` | 비정수압 압력경사 implicitness | `SwashImpDep1DHflow.ftn90:184`; `:190` |

**theta 허용범위 차이**(M 여부의 핵심):
- 비-M 1DH/Uflow: `0.5 <= theta <= 1` (`SwashImpDep1DHflow.ftn90:48`; `SwashImpDepUflow.ftn90:48`).
- M-1DH/M-2DH: **theta = 0.5 고정** — 코드에서 직접 `teta = 0.5` 강제(`SwashImpDepM1DHflow.ftn90:179`; M2DH 헤더 `:53` "Only a value of theta = 0.5 is taken"). 엄밀 에너지보존을 위해 Crank-Nicolson(중심·2차)에 고정.

부유체(floating object) 하부에서는 `teta`/`teta2`를 `pship(2)`로 국소 치환(`SwashImpDep1DHflow.ftn90:188-211`).

---

## 3. SwashImpDep1DHflow — 명시 predictor-corrector + 압력보정

### 3.1 Method 헤더 (verbatim)
`SwashImpDep1DHflow.ftn90:47-62`:
> "The time integration with respect to the continuity equation and the water level gradient of the u-momentum equation is based on a theta-scheme. Only a value of 0.5 <= theta <= 1 will be taken."
> "The time integration with respect to the advective term is based on the predictor-corrector scheme of MacCormack, while that for the bottom friction is based on Euler implicit and for the non-hydrostatic pressure gradient a semi-implicit approach is employed (theta-scheme)."
> "The space discretization of the advective term is momentum conservative (or energy head conservative in case of flow contraction) and is approximated by either first order upwind or higher order (flux-limited) scheme (CDS, Fromm, BDF, QUICK, MUSCL, Koren, etc.)."
> "The w-momentum equation only contains the z-gradient of the non-hydrostatic pressure and is discretized by means of the Keller-box scheme."

### 3.2 advection: 모멘텀 vs 에너지헤드 보존 선택
upwind advective velocity 결정(`SwashImpDep1DHflow.ftn90:260-287`): 분기 조건
`( u0(nm) > u0(nmd) .or. stricthead ) .and. .not.strictmom` 가 참이면 에너지헤드 보존형(`fac = 0.5*(u0(nm)+u0(nmd))`), 거짓이면 모멘텀 보존형(`fac = qm(nm)`). 즉 **유속 수축(flow contraction)** 시 에너지헤드, 일반 시 모멘텀 보존 — 헤더의 "or energy head conservative in case of flow contraction" 구현(`:267-275`, predictor `:303-326`).

advection term(predictor):
$$\text{advec}(nm) = \frac{1}{\Delta x}\big[ \text{fac1}\,(u_a^{mu}-u_0^{nm}) - \text{fac2}\,(u_a^{nm}-u_0^{nm}) \big]$$
(`SwashImpDep1DHflow.ftn90:322`).

고차(flux-limited) 보정은 defect correction으로 corrector 단계에서 추가(`:715-810`, `fluxlim(grad1,grad2)` 호출 `:750`, `:758`). `propsc = nint(pnums(6))`로 스킴 선택(`:713`).

### 3.3 중간 u-속도 (명시 갱신)
비-M 1DH의 결정적 특징: momentum predictor를 **명시적으로** 계산.
`SwashImpDep1DHflow.ftn90:690-696`:
```
contrib = advec(nm) + zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm)) - visc(nm)
denom   = 1. + cvegu(nm,1,2) + cpomu(nm,1) + dt*( cbot(nm) + cporfr + cveg + wndimp(nm) )
u1(nm)  = ( (1.+cvegu(nm,1,2)+cpomu(nm,1))*u0(nm) - dt*contrib ) / denom
```
즉 advection/수위경사/압력경사/점성은 명시(u0 기반), bottom friction·porous·vegetation·wind drag만 분모(`denom`)로 Euler-implicit 처리. **여기에는 tridiagonal 계가 없다**(M-변종과의 대비점).

수위경사 `zgrad = grav*rdx*(s0(nmu)-s0(nm))` (`:678`).

### 3.4 연속방정식 → 수위보정 tridiag 계
`fac = grav*dt*dt*rdx*rdx`(`:847`)를 계수로, 삼중대각 계수 a/b/c/d build(`:851-901`):
```
a(nm) = -fac * teta(nmd) * hu(nmd)            ! 하위 대각
c(nm) = -fac * teta(nm ) * hu(nm )            ! 상위 대각
b(nm) = fac1 - teta2(nm)*( a(nm)+c(nm) )       ! 주대각 (fac1=1 또는 pship(1))
a(nm) = teta2(nmd)*a(nm);  c(nm) = teta2(nmu)*c(nm)
d(nm) = dt*rdx*( hu(nmd)*(teta(nmd)*ui(nmd)+(1-teta(nmd))*u0(nmd))
               - hu(nm )*(teta(nm )*ui(nm )+(1-teta(nm ))*u0(nm )) )
```
(`SwashImpDep1DHflow.ftn90:874-895`). 우변 `d`는 theta-가중 mass flux divergence. 내부파 생성 mass source(`srcm`)·강체운동(`skc`)·pressure projection 항(`dqgrd`, `lpproj`)도 d에 가산(`:899-934`). 수위 경계조건(slimp/srimp)으로 단부 행 처리 후 `call tridiag( a, b, c, d, ds, kgrpnt )`(`:954`).

**Newton 변종**: `inewt /= 0` 이면 동일 계를 wetting/drying 한계(`lon`/`upn`) 포함 `call newton1D( an, bn, cn, dn, lon, upn, ds, kgrpnt )`로 풀이(`:957-1065`).

### 3.5 속도보정·Poisson·pressure correction
수위보정 후 u 보정:
$$u_1 = u_i - g\,\Delta t\,\frac{1}{\Delta x}\big(\text{teta2}^{mu}\,ds^{mu} - \text{teta2}^{nm}\,ds^{nm}\big)$$
(`SwashImpDep1DHflow.ftn90:1129`). 이를 pressure-projection 반복(`10 if(resm>epslin .and. j<maxit)`, `:838`, `goto 10` `:1461`) 안에서 2차정확도까지 수렴시킴. 수렴기준 `epslin = max(reps,reps*s0mx)`, `reps=pnums(58)`, `maxit=pnums(59)` (`:826-832`).

Keller-box w-momentum(`w1bot`/`w1top`)는 `:1228-1256`. free surface는 `w1top(nm)=w0top+w0bot-w1bot+2*dt*fac*q(nm)/hs(nm)`(`:1236`).

Poisson eq(비정수압 압력보정 `dq`) — 삼중대각:
`SwashImpDep1DHflow.ftn90:1390-1396`:
```
fac1 = rdx*( dpu(nm)-dpu(nmd) + 0.5*(hu(nm)+hu(nmd)) )
fac2 = rdx*( dpu(nm)-dpu(nmd) - 0.5*(hu(nm)+hu(nmd)) )
a(nm)= fac2*gmat(nmd,1)
b(nm)= fac1*gmat(nm,1)+fac2*gmat(nmd,2) - 2./hs(nm)
c(nm)= fac1*gmat(nm,2)
d(nm)= ( fac1*u1(nm)+fac2*u1(nmd)+w1top(nm)+w1bot(nm) )/(dt*theta3)
```
`call tridiag( a, b, c, d, dq, kgrpnt )`(`:1425`). 압력 갱신 `q=q+dq`(iproj==1) 또는 `q=dq`(iproj==2)(`:1467-1473`), 최종 u/w 보정(`:1477-1521`), mass flux `qx(nm)=hu(nm)*(teta(nm)*u1(nm)+(1-teta(nm))*u0(nm))`(`:1529`).

**gmat(비정수압 압력 gradient matrix)**: free surface(`presu==0`)는
`gmat(nm,1)=-fac*(s0(nm)+dps(nmu))`, `gmat(nm,2)=fac*(s0(nmu)+dps(nm))`, `fac=0.5*rdx/hum(nm)` (`:369-376`). pressurized flow는 `hs` 기반(`:382-401`). `iproj==2`면 `qgrad=(1-theta3)*qgrad`(`:449`).

---

## 4. SwashImpDepM1DHflow — Crank-Nicolson 암시 momentum tridiag

### 4.1 핵심 차이: momentum 자체가 암시 tridiagonal
비-M 1DH가 u1을 명시 갱신(§3.3)하는 반면, M-1DH는 **advection·viscosity를 Crank-Nicolson으로 암시 처리하여 momentum tridiag 계를 직접 푼다**. 헤더(`SwashImpDepM1DHflow.ftn90:55-61`):
> "The time integration with respect to the advective and viscosity terms is based on the Crank-Nicolson scheme ... The space discretization of the horizontal advective and viscosity terms is strictly momentum conservative and are approximated with central differences, so that the advection term is skew-symmetric and the viscosity term is symmetric."

### 4.2 momentum 계 build
advective 가중 `fac1/fac2 = 0.25*dt*rdx*qm/humn` (1/4 = 중심차분 + CN 절반)(`SwashImpDepM1DHflow.ftn90:458-459`). 시스템:
`SwashImpDepM1DHflow.ftn90:490-493`:
```
a(nm) = -fac2
c(nm) =  fac1
b(nm) =  denom - a(nm) - c(nm)
d(nm) = (1.+cvegu(nm,1,2)+cpomu(nm,1)+a(nm)+c(nm))*u0(nm) - a(nm)*u0(nmd) - c(nm)*u0(nmu) - dt*contrib
```
여기서 `contrib = zgrad + pgrad + qgrad - windu/...` 로 **advection은 contrib에 없음**(좌변 a/c로 들어감 = 암시). `a=-fac2, c=+fac1` 의 반대부호 = skew-symmetric 이산 연산자 구현.

점성항도 동일 시스템에 가산(symmetric): `fac1/fac2 = 0.5*dt*rdx*rdx*hvisc*hs/hum`, `a-=fac2; c-=fac1; b+=fac1+fac2` (`:521-538`, `ihvisc>1` 분기 vnu2d `:557-574`). 양쪽 부호 동일(`a-=fac2, c-=fac1`) = symmetric.

경계조건 적용 후 `call tridiag( a, b, c, d, u1, kgrpnt )`(`:602`) — **u1을 직접 푸는 점이 비-M과 결정적 대비**. 헤더 주: "only velocity is prescribed at the boundary"(`:68`)로 skew-symmetry 보존(`:584-598`에서 좌단 Dirichlet u, 우단 u1(nml) 고정).

### 4.3 나머지(연속·Poisson)는 1DH와 동형
수위보정 tridiag(`:634-727`), Newton 변종 `newton2D`... 아니 `newton1D`(`:822`), Poisson tridiag(`:1050-1096`), mass flux/에너지 진단(`:1194-`)은 비-M 1DH와 구조 동일. teta=0.5 고정만 다름.

---

## 5. SwashImpDepM2DHflow — 곡선격자 2D, 5점 SIP

### 5.1 차원 확장
M-1DH의 2D 곡선격자(curvilinear) 버전. metric 항 `guu, guv, gvu, gvv, gsqs, gsqsu, gsqsv`를 `m_genarr`에서 사용(`SwashImpDepM2DHflow.ftn90:75`). u-momentum과 v-momentum 각각 별도 계. 헤더 Method는 M-1DH와 동일(strictly conservative, CN, skew-symmetric central, theta=0.5)(`:42-68`).

### 5.2 u/v-momentum: 5점 행렬 + SIP
1D의 tridiag(3점) 대신 5점 stencil `amat(nm,1..5)`(중앙·서·동·남·북). u-momentum:
`SwashImpDepM2DHflow.ftn90:655-660`:
```
amat(nm,2) = -fac2; amat(nm,3) = fac1     ! x-방향(서/동) advection, skew
amat(nm,4) = -fac4; amat(nm,5) = fac3     ! y-방향(남/북) cross-advection
amat(nm,1) =  denom - sum(2..5)
rhs (nm)   = (1.+cvegu+cpomu+sum(2..5))*u0(nm) - amat2*u0(nmd) - ... - dt*contrib
```
y-방향 cross-advective 가중 `fac3/fac4 = 0.25*dt*qym/(guu*humn)` (`:607-608`). 해: `call sip( amat, rhs, u1 )`(`:744`). v-momentum 대칭 구조: `fac3/fac4 = 0.25*dt*qxm/(gvv*hvmn)`(`:1057-1058`), `amat` build(`:1105-1110`), `call sip( amat, rhs, v1 )`(`:1194`).

`sip` = Strongly Implicit Procedure(불완전 LU 기반 반복 solver) — 비대칭 5점 계 처리.

### 5.3 연속방정식(수위보정) 5점 계
`fac = grav*dt*dt`(`:1234`), metric 포함 계수(`:1264-1308`):
```
amat(nm,2) = -fac*tetau(nmd)*guu(nmd)*hu(nmd)/gvu(nmd)   ! 서
amat(nm,3) = -fac*tetau(nm )*guu(nm )*hu(nm )/gvu(nm )   ! 동
amat(nm,4) = -fac*tetav(ndm)*gvv(ndm)*hv(ndm)/guv(ndm)   ! 남
amat(nm,5) = -fac*tetav(nm )*gvv(nm )*hv(nm )/guv(nm )   ! 북
amat(nm,1) = fac1*gsqs(nm) - teta2(nm)*(sum 2..5)
```
우변은 u·v 양방향 theta-가중 mass flux divergence(`gsqs`=셀 면적 metric)(`:1309-1310`). 해: 표준 `inewt==0` 분기는 `sip`(노트 §5.2 동일 solver, 본문 build 후 풀이), Newton 변종은 `call newton2D( amatn, rhsn, lon, upn, ds )`(`:1523`).

### 5.4 Poisson·보정
비정수압 압력보정: `build the Poisson equation`(`:1898-`) 후 `call sip( amat, rhs, dq )`(`:1991`). 압력 갱신(`:2055-`), 속도 최종 보정(`:2065-`). u-point/v-point 각각 gmat(`gmatu`/`gmatv`) build(`:335`, `:797`).

---

## 6. SwashImpDepUflow — 비구조 삼각망 face-based

### 6.1 정체성
삼각형 비구조격자(unstructured triangular mesh)용 수심평균 solver(`SwashImpDepUflow.ftn90:43` "on triangular mesh"). 변수는 면(face)·셀(cell) 기반: `nfaces`/`ncells`, 속도는 face의 법선성분 `u1(nfaces)`, 압력보정 `dq(ncells)`, 셀 circumcenter 속도성분 `uvc(ncells,2)`(`:83-91`). `SwanGriddata`/`SwanGridobjects` 모듈 사용(`:76-77`) — SWAN 비구조 인프라 공유.

### 6.2 시간적분
헤더 Method(`SwashImpDepUflow.ftn90:47-55`):
> "The time integration with respect to the continuity equation and the water level gradient ... theta-scheme. Only a value of 0.5 <= theta <= 1 ..."
> "The time integration with respect to the advective and viscous terms and bottom friction is based on Euler implicit."
> "The space discretization of the advective term is momentum conservative and is approximated by first order upwind or higher order (flux-limited) scheme ... The r-ratio formulation based on most upwave vertex is employed."

⚠ **헤더 주석과 코드의 불일치(주의)**: 헤더는 advective/viscous 항이 "Euler implicit"라고 하나, intermediate face velocity 갱신부에서는 advection·viscosity가 `advec(iface)`/`visc(iface)`로 **u0(이전 시각)에서 명시적으로** 계산되어 `contrib`로 들어가고, `denom = 1.+dt*(cbot+wndimp)` 에는 bottom friction·wind drag만 암시 처리된다(`SwashImpDepUflow.ftn90:1039-1045`; `advec`가 u0 기반임은 `:474·482·490·1039`). 즉 수심평균 경로의 advection은 명시. (`advec` 계산이 모두 `u0` 사용: `:474,482,490`.) bottom friction만 Euler-implicit이 코드상 정확.

intermediate u(내부 면):
`SwashImpDepUflow.ftn90:1039-1045`:
```
contrib = advec(iface)/humn(iface) + (zgrad+pgrad+qgrad-windu-visc+corf)/hum(iface)
denom   = 1. + dt*( cbot(iface) + wndimp(iface) )
u1(iface) = ( u0(iface) - dt*contrib ) / denom
```
`corf` = Coriolis 항. 경계 면은 friction만(`denom=1.+dt*cbot`)(`:998-1002`).

### 6.3 수위보정 — PCG / Newton
연속방정식 계는 셀 단위. `fac = grav*theta*theta2*dt*dt`(`:1059`). 셀마다 인접 face 순회하며 `amat(icell,0)`(대각, 초기 셀면적)·`amat(icell,jf)`(off-diag) build, 우변은 theta-가중 face mass flux `-dt*rsgn*lf*hu(iface)*(theta*u1+(1-theta)*u0)`(`:1067-1118`). 표준 경로: `call pcgu( amat, rhs, ds )`(`:1140`) — preconditioned CG(대칭 SPD 계). Newton 변종(`inewt/=0`): 동일 계에 wetting/drying 항 추가, 수렴 보증 위해 `sum(rhsn)>0` 체크(`:1208-1210`) 후 `call newtonU( amatn, rhsn, ds )`(`:1233`).

속도보정(내부 면): `u1(iface) = u1(iface) - grav*theta2*dt*rdx*hf*(ds(icellr)-ds(icelll))/hum(iface)`(`:1285`); 경계 면은 `dbs-ds(icellb)` 기반(`:1260`).

### 6.4 Poisson — BiCGSTAB
비정수압 압력보정 `dq`: Poisson build(`:1622-`) 후 **`call bicgstabu( amat, rhs, dq )`**(`:1749`) — 비대칭 계용 BiCGSTAB. (수위보정의 SPD 계는 PCG, Poisson은 BiCGSTAB로 solver가 다름.) 압력 갱신 q=q+dq / q=dq(`:1756-1762`), face 속도 최종 보정 `u1(iface) -= dt*theta3*(gmat(iface,1)*dq(icelll)+gmat(iface,2)*dq(icellr))/hum(iface)`(`:1779`), 경계 면은 단일 셀(`:1787`).

gmat(face 압력 gradient): 내부 면·수위 경계 면 분기(`:229-296`), `iproj==2`면 `qgrad=(1-theta3)*qgrad`(`:296`).

---

## 7. 4 변종 비교 요약 (메커닉 표)

| 항목 | 1DH(비-M) | M1DH | M2DH | Uflow |
|---|---|---|---|---|
| momentum advection 시간처리 | 명시 MacCormack predictor-corrector (`:50-52`) | 암시 Crank-Nicolson (`:55-56`) | 암시 CN (`:55-56`) | 명시(코드, advec=u0) — 헤더는 "Euler implicit" ⚠ (`:50-51` vs `:1039`) |
| advection 공간이산 | upwind/flux-limited, mom 또는 energy-head (`:54-57`) | 중심차분 skew-symmetric (`:59-61`) | 중심차분 skew-symmetric (`:59-61`) | upwind/flux-limited, r-ratio most-upwave vertex (`:53-55`) |
| theta 범위 | 0.5–1 (`:48`) | 0.5 고정 (`:179`) | 0.5 고정 (`:53`) | 0.5–1 (`:48`) |
| momentum solver | 없음(명시 갱신 `:696`) | tridiag (`:602`) | sip 5점 (`:744,1194`) | 명시 갱신 `:1045` |
| 수위보정 solver | tridiag / newton1D (`:954,1065`) | tridiag / newton1D (`:727,822`) | sip / newton2D (`:1523`) | pcgu / newtonU (`:1140,1233`) |
| Poisson(dq) solver | tridiag (`:1425`) | tridiag (`:1096`) | sip (`:1991`) | bicgstabu (`:1749`) |
| 격자 | 1D 구조 | 1D 구조 | 2D 곡선(metric guu/gvv/gsqs) | 비구조 삼각 |
| friction 시간처리 | Euler implicit(denom) (`:692`) | Euler implicit(denom) (`:486`) | Euler implicit(denom) | Euler implicit(denom) (`:1041`) |

공통 비정수압 처리: Keller-box w-momentum + 2차정확 pressure correction(theta3 semi-implicit), `iproj==1`이면 incremental(q=q+dq), `iproj==2`이면 non-incremental(q=dq). 4파일 모두 동일 패턴(`SwashImpDep1DHflow.ftn90:1467-1473` 등).

---

## 8. 미확인·후속

- `tridiag`, `newton1D`, `newton2D`, `newtonU`, `sip`, `pcgu`, `bicgstabu` 의 내부 구현(전처리·수렴조건)은 본 노트 범위 밖(별도 solver 노트 후보). 호출부 시그니처만 인용함.
- §6.2의 헤더-코드 불일치(Uflow advection이 헤더상 "Euler implicit"이나 코드는 u0 기반 명시)는 다층(`SwashImpLayUflow`)에서는 다를 수 있음 — 본 노트는 수심평균 경로만 확인. source-needed: 다층 경로의 advection 시간처리.
- M2DH의 cross-advection(`fac3/fac4`) skew-symmetry 정확 검증은 수치해석적 증명 영역 — 코드 부호 구조(`amat,4=-fac4; amat,5=+fac3`)만 인용.
