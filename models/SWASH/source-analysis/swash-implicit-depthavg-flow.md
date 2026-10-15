---
title: "SWASH 암시적 수심평균 flow solver — 1DH/M1DH/M2DH/Uflow (theta-스킴·tridiag·pressure correction)"
model: SWASH
component: src (implicit depth-averaged flow / time integration)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashImpDep1DHflow.ftn90(Purpose/Method 헤더 :41-63, theta 설정 :182-184, 명시적 momentum predictor :667-704, continuity tridiag 시스템 build :851-955, Poisson build/solve :1377-1426, 속도/압력 보정 :1467-1531), SwashImpDepM1DHflow.ftn90(Method 헤더 :42-68, teta=0.5 :179, Crank-Nicolson 암시 momentum tridiag :447-602), SwashImpDepM2DHflow.ftn90(Method :42-68, amat 5점 sip u/v :655-744·1105-1194, continuity amat build :1240-1318, newton2D :1523, Poisson sip :1991), SwashImpDepUflow.ftn90(Purpose/Method :41-60, theta :188-190, 명시 face momentum :996-1045, pcgu/newtonU :1140·1233, bicgstabu Poisson :1749, 속도보정 :1779) file:line 인용. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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
| `SwashImpDepM1DHflow` | 1DH 구조격자 | Crank-Nicolson, **암시** | 공간의 운동량·에너지 보존 (theory-framework:ST1-323) | `tridiag` [10-15 대조 정정] |
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
여기서 `contrib = zgrad + pgrad(nm) + qgrad(nm) - windu(nm)/max(1.e-3,hum(nm))`에는 이류항과 점성항이 없다 (`src/SwashImpDepM1DHflow.ftn90:482–484`). [10-15 전수 검증 정정]
해석: 균일 1D 격자의 양의 수심을 가진 젖은 내부 면에서 `M_i=humn_i\Delta x`를 곱하면 `M_i c_i=-M_{i+1}a_{i+1}`이다 (`src/SwashImpDepM1DHflow.ftn90:456–459,468,490–492`; theory-framework:ST1-056·322). [10-15 전수 검증 정정]
질량 변화 대각항도 에너지 조건에 포함한다 (theory-framework:ST1-322). [10-15 대조 정정]
이 비대각 관계만으로 유속 연산자 전체가 반대칭이라고 결론 내릴 수 없다 (theory-framework:ST1-056). [10-15 대조 정정]

해석: 균일 1D의 내부 젖은 점에서 점성 연산자의 이웃 계수에 `hum`을 곱하면 공유 수심을 가진 같은 부호의 계수가 된다 (`src/SwashImpDepM1DHflow.ftn90:508,521–522,535–537`; theory-framework:ST1-175). [10-15 대조 정정]
이 점성 계수는 `hum` 가중 내적에서 자기수반 관계에 대응한다 (theory-framework:ST1-176). [10-15 대조 정정]
점성의 가중 대칭과 음의 소산은 구별한다 (theory-framework:ST1-322). [10-15 대조 정정]

경계조건 적용 후 `call tridiag( a, b, c, d, u1, kgrpnt )`(`:602`) — **u1을 직접 푸는 점이 비-M과 결정적 대비**. 헤더 주: "only velocity is prescribed at the boundary"(`:68`)로 skew-symmetry 보존(`:584-598`에서 좌단 Dirichlet u, 우단 u1(nml) 고정).

### 4.3 나머지(연속·Poisson)는 1DH와 동형
수위보정 tridiag(`:634-727`), Newton 변종 `newton2D`... 아니 `newton1D`(`:822`), Poisson tridiag(`:1050-1096`), mass flux/에너지 진단(`:1194-`)은 비-M 1DH와 구조 동일. teta=0.5 고정만 다름.

구조 격자의 ITEST 체적 진단은 면적·길이를 곱하지 않은 수위 합을 출력한다 (`src/SwashExpDep1DHflow.ftn90:1626`; `src/SwashExpDep2DHflow.ftn90:4905`; M1DH의 자유수면 점은 `src/SwashImpDepM1DHflow.ftn90:1261`; theory-framework:ST1-333). [10-15 전수 검증 보완]
균일 격자에서는 체적에 비례하지만 비균일 격자의 물리 체적으로 해석하면 결함 후보이다 (theory-framework:ST1-333, E 중간). [10-15 대조 정정]
이 진단은 유동의 질량 갱신식과 구별한다 (theory-framework:ST1-333). [10-15 대조 정정]

---

## 5. SwashImpDepM2DHflow — 곡선격자 2D, 5점 SIP

### 5.1 차원 확장
M-1DH의 2D 곡선격자(curvilinear) 버전. metric 항 `guu, guv, gvu, gvv, gsqs, gsqsu, gsqsv`를 `m_genarr`에서 사용(`SwashImpDepM2DHflow.ftn90:75`). u-momentum과 v-momentum 각각 별도 계. 헤더 Method는 M-1DH와 동일(strictly conservative, CN, skew-symmetric central, theta=0.5)(`:42-68`).

공간의 질량·운동량 보존과 공간의 에너지 보존은 구별한다 (theory-framework:ST1-323). [10-15 대조 정정]
시간 분할 때문에 시간 에너지는 엄밀 보존이 아니라 근사 보존이다 (`src/SwashImpDepM1DHflow.ftn90:46–47`; theory-framework:ST1-323). [10-15 대조 정정]
식 (2.23)의 보존 대응은 외력·점성·마찰을 제외한 부분계에 해당한다 (swashtech PDF p.57; `src/SwashImpDepM1DHflow.ftn90:476–486,508`; theory-framework:ST1-229·323). [10-15 전수 검증 보완]
점성의 가중 대칭과 음의 소산은 별도로 다룬다 (theory-framework:ST1-322). [10-15 대조 정정]

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

헤더는 이류·점성 항의 시간적분을 Euler implicit이라고 설명한다 (`src/SwashImpDepUflow.ftn90:50–51`). 실제 이류·점성 항은 `u0`와 그 셀 속도 보간값으로 계산되어 `contrib`에 명시적으로 들어간다 (`src/SwashImpDepUflow.ftn90:306,474–490,760–768,1039`). 바닥 마찰과 상대풍속의 유속 의존 항은 `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )`에 들어간다 (`src/SwashImpDepUflow.ftn90:1041–1045`; theory-unstructured:ST2-365). [10-15 전수 검증 정정]

intermediate u(내부 면):
`SwashImpDepUflow.ftn90:1039-1045`:
```
contrib = advec(iface)/humn(iface) + (zgrad+pgrad+qgrad-windu-visc+corf)/hum(iface)
denom   = 1. + dt*( cbot(iface) + wndimp(iface) )
u1(iface) = ( u0(iface) - dt*contrib ) / denom
```
`corf` = Coriolis 항. 경계 면은 friction만(`denom=1.+dt*cbot`)(`:998-1002`).

마른 면에서 전체 `cbot`를 지우는 대입은 앞서 계산한 젖은 면의 마찰을 지울 수 있다 (`src/SwashImpDepUflow.ftn90:341,412`; theory-unstructured:ST2-365, E 강함). [10-15 대조 정정]
`835452f`(2025-07-11, additional changes)가 두 수심 평균 파일의 마른 면 ELSE에 전체 대입을 추가했다 (theory-unstructured:ST2-365). [10-15 대조 정정]

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

## 8. 해석 조건과 경로

- 구조 격자의 `tridiag`, `newton1D`, `newton2D`, `sip` 구현은 [선형 솔버 노트](swash-linear-solvers.md)에 정리되어 있다 (`src/SwashSolvers.ftn90:4297,5283,5491,1811`). 비구조 격자의 `newtonU`, `pcgu`, `bicgstabu` 구현은 [비구조 솔버 노트](swash-unstructured-solvers.md)에 정리되어 있다 (`src/SwashUServ.ftn90:2324,299,1211`). [10-15 전수 검증 정정]
- 수심 평균 `SwashImpDepUflow`의 바닥 마찰은 `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )`에 들어간다 (`src/SwashImpDepUflow.ftn90:1041`; theory-unstructured:ST2-365). [10-15 대조 정정]
- M2DH의 cross-advection 계수는 `amat(nm,4) = -fac4`와 `amat(nm,5) =  fac3`이다 (`src/SwashImpDepM2DHflow.ftn90:607–608,657–658`). 이 두 부호만으로 전체 유속 행렬의 무가중 반대칭을 뜻하지 않는다 (theory-framework:ST1-322). [10-15 전수 검증 정정]

## 문서와 코드 차이 (10-15 대조)

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경); 코드 판: `VERNUM 12.01`, 공개 저장소 main `a486d5f`(2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

문서 인용의 인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

근거 보고서: [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md#5-차이-결론), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| theory-framework:ST1-056 | 식 (2.9) 반대칭 정의 | swashtech PDF p.21: `\langle\mathbf u,A\mathbf v\rangle=-\langle A\mathbf u,\mathbf v\rangle,\quad\forall\mathbf u,\mathbf v\in\mathcal V` | `src/SwashImpDepM1DHflow.ftn90:458–459` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)`<br>`fac2 = 0.25 * dt * rdx * qm(nm ) / humn(nm)`; `src/SwashImpDepM1DHflow.ftn90:490–491` `a(nm) = -fac2`<br>`c(nm) =  fac1`; `src/SwashImpDepM1DHflow.ftn90:492` `b(nm) =  denom - a(nm) - c(nm)`; `src/SwashImpDepM1DHflow.ftn90:456` `if ( humn(nm) > 0. ) then`; `src/SwashImpDepM1DHflow.ftn90:468` `if ( wetu(nm) == 1 ) then`; `src/SwashReadInput.ftn90:2010–2011` `else if ( KEYWIS ('MIME') ) then`<br>`mimetic = .true.`; `src/SwashComputFlow.ftn90:89` `else if ( mtimei == 2 ) then`; 같은 파일 93–96행은 `mimetic`의 참 분기에서 `SwashImpDepM1DHflow`를 호출한다. | F 표기 차이 | 해석: 양의 수심을 가진 젖은 내부 면에서 `M_i=humn_i\Delta x`를 곱하면 비대각 계수는 `M_i c_i=-M_{i+1}a_{i+1}`를 만족한다. 그러나 이류 대각 성분 `-a(nm)-c(nm)`은 일반적으로 0이 아니다. 따라서 이 비대각 관계만으로 유속 연산자 전체가 반대칭이라고 결론 내릴 수 없다. 문서의 반대칭 조건과 연결하려면 ST1-083처럼 질량 변화항까지 포함해 운동량형으로 변환해야 한다. 인용 경로는 1D·단층·반암시적 시간적분의 `DISCRET MIMETIC` 선택에 해당한다. |
| theory-framework:ST1-081 | 번호 없는 이류 보존 조건 | swashtech PDF p.24: `\left\langle\mathbf u,\frac12\frac{\partial h}{\partial t}\mathbf u+\nabla\cdot(\mathbf q\otimes\mathbf u)\right\rangle=0` | `src/SwashImpDepM1DHflow.ftn90:490–493` `a(nm) = -fac2`<br>`c(nm) =  fac1`<br>`b(nm) =  denom - a(nm) - c(nm)`<br>`d(nm) = (1.+cvegu(nm,1,2)+cpomu(nm,1)+a(nm)+c(nm)) * u0(nm) - a(nm) * u0(nmd) - c(nm) * u0(nmu) - dt * contrib`; `src/SwashImpDepM1DHflow.ftn90:456` `if ( humn(nm) > 0. ) then`; `src/SwashImpDepM1DHflow.ftn90:468` `if ( wetu(nm) == 1 ) then` | F 표기 차이 | 해석: 질량 변화의 대각 기여와 공유 플럭스의 양쪽 반대 부호가 대응한다. 외력·분할 시간적분을 포함한 전체 시스템의 정확 보존 조건으로 확대하지 않는다. 코드 대응은 ST1-056의 M1D 선택 및 양의 수심·젖은 내부 면 조건을 따른다. 반대칭 대상은 ST1-083의 질량 변화항을 포함한 운동량 연산자이다. |
| theory-framework:ST1-083 | 번호 없는 반대칭 조건·연산자 | swashtech PDF p.25: `\langle\mathbf u,[A+\frac12\frac{\partial h}{\partial t}I]\mathbf u\rangle=0`; `A+\frac12\frac{\partial h}{\partial t}I` `must be skew-symmetric.` | `src/SwashImpDepM1DHflow.ftn90:490–492` `a(nm) = -fac2`<br>`c(nm) =  fac1`<br>`b(nm) =  denom - a(nm) - c(nm)` | F 표기 차이 | 해석: 공유 플럭스의 반대 부호 비대각항과 질량 변화의 대각항을 구별한다. `A` 단독의 무가중 반대칭을 요구하는 식이 아니다. 해석: 문서의 운동량 이류는 `A+A^{\mathsf T}=-\dot h I`를 만족해야 한다. 코드 유속식과 비교할 때 `A_{\mathrm{mom}}=hA_{\mathrm{vel}}-\dot h I`라는 곱 규칙 변환을 적용한다. 이 대응은 ST1-056의 양의 수심을 가진 젖은 내부 면에서 시간 계수를 분리한 공간 연산자에 대한 해석이다. 코드의 유속 이류 대각항은 일반적으로 0이 아니다. |
| theory-framework:ST1-084 | 식 (2.13) | swashtech PDF p.25: `A=\frac12C-\frac12C^{\mathsf T}-\frac12\frac{\partial h}{\partial t}I` | `src/SwashImpDepM1DHflow.ftn90:458–459` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)`<br>`fac2 = 0.25 * dt * rdx * qm(nm ) / humn(nm)`; `src/SwashImpDepM1DHflow.ftn90:490–492` `a(nm) = -fac2`<br>`c(nm) =  fac1`<br>`b(nm) =  denom - a(nm) - c(nm)` | F 표기 차이 | 해석: 중앙 이류의 반대 부호 연결은 ST1-056이다. 연속방정식의 `\partial_t h=-\nabla\cdot\mathbf q`를 넣으면 식 (2.14)가 된다. 코드는 `C`라는 연산자 객체 대신 계수를 조립한다. ST1-056의 호출·수심·젖은 면 조건과 ST1-083의 질량 변화항 변환을 함께 적용한다. |
| theory-framework:ST1-085 | 식 (2.14) | swashtech PDF p.25: `A=\frac12C-\frac12C^{\mathsf T}+\frac12(\nabla\cdot\mathbf q)I` | `src/SwashImpDepM1DHflow.ftn90:492–493` `b(nm) =  denom - a(nm) - c(nm)`<br>`d(nm) = (1.+cvegu(nm,1,2)+cpomu(nm,1)+a(nm)+c(nm)) * u0(nm) - a(nm) * u0(nmd) - c(nm) * u0(nmu) - dt * contrib` | F 표기 차이 | 해석: 질량 변화가 이류 대각항에 남는다. 이류의 시간 평균 계수가 포함되므로 코드의 0.25를 문서의 0.5와 직접 비교하지 않는다. 이 대응은 ST1-056의 호출·수심·젖은 면 조건을 따르는 공간 계수의 비교이다. 운동량형과 유속형 사이의 변환은 ST1-083이다. |
| theory-framework:ST1-175 | 번호 없는 자기수반 조건 | swashtech PDF p.45: `\langle\mathbb C^k\alpha^{(k)},\beta^{(k)}\rangle_{\mathbb H^k}=\langle\alpha^{(k)},\mathbb C^k\beta^{(k)}\rangle_{\mathbb H^k},\quad\forall\alpha^{(k)},\beta^{(k)}\in V^k` | `src/SwashImpDepM1DHflow.ftn90:508` `if ( ihvisc == 1 .and. hvisc > 0. ) then`; `src/SwashImpDepM1DHflow.ftn90:521–522` `fac1 = 0.5 * dt * rdx * rdx * hvisc * hs(nmu) / hum(nm)`<br>`fac2 = 0.5 * dt * rdx * rdx * hvisc * hs(nm ) / hum(nm)`; `src/SwashImpDepM1DHflow.ftn90:535–537` `a(nm) = a(nm) - fac2`<br>`c(nm) = c(nm) - fac1`<br>`b(nm) = b(nm) + fac1 + fac2` | F 표기 차이 | 해석: 균일 1D의 내부 젖은 점에서 점성 연산자의 이웃 계수에 `hum`을 곱하면 공유 수심을 가진 같은 부호의 계수가 된다. 이는 가중 자기수반 관계의 코드 대응이다. 전체 운동량 행렬의 자기수반성으로 확대하지 않는다. ST1-176과 같은 판정이다. |
| theory-framework:ST1-176 | 번호 없는 자기수반 표기 | swashtech PDF p.45: `(\mathbb C^k)^{\mathsf T}=\mathbb C^k` | `src/SwashImpDepM1DHflow.ftn90:508` `if ( ihvisc == 1 .and. hvisc > 0. ) then`; `src/SwashImpDepM1DHflow.ftn90:521–522` `fac1 = 0.5 * dt * rdx * rdx * hvisc * hs(nmu) / hum(nm)`<br>`fac2 = 0.5 * dt * rdx * rdx * hvisc * hs(nm ) / hum(nm)`; `src/SwashImpDepM1DHflow.ftn90:535–537` `a(nm) = a(nm) - fac2`<br>`c(nm) = c(nm) - fac1`<br>`b(nm) = b(nm) + fac1 + fac2` | F 표기 차이 | 해석: ST1-175의 점성 계수는 `hum` 가중 내적에서 자기수반 관계에 대응한다. T를 점 유속 배열의 무가중 전치로 해석하지 않는다. |
| theory-framework:ST1-177 | 번호 없는 반수반 조건 | swashtech PDF p.45: `\langle\mathbb C^k\alpha^{(k)},\beta^{(k)}\rangle_{\mathbb H^k}=-\langle\alpha^{(k)},\mathbb C^k\beta^{(k)}\rangle_{\mathbb H^k},\quad\forall\alpha^{(k)},\beta^{(k)}\in V^k` | `src/SwashImpDepM1DHflow.ftn90:458–459` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)`<br>`fac2 = 0.25 * dt * rdx * qm(nm ) / humn(nm)`; `src/SwashImpDepM1DHflow.ftn90:490–492` `a(nm) = -fac2`<br>`c(nm) =  fac1`<br>`b(nm) =  denom - a(nm) - c(nm)` | F 표기 차이 | 해석: `humn`을 곱한 두 이웃 이류 계수는 같은 공유 플럭스의 반대 부호가 된다. ST1-056·177·178은 이 대응을 가리킨다. 대각 성분과 시간 수심 변화를 포함하는 전체 행렬이 반대칭이라는 주장은 아니다. |
| theory-framework:ST1-178 | 번호 없는 반수반 표기 | swashtech PDF p.45: `(\mathbb C^k)^{\mathsf T}=-\mathbb C^k` | `src/SwashImpDepM1DHflow.ftn90:458–459` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)`<br>`fac2 = 0.25 * dt * rdx * qm(nm ) / humn(nm)`; `src/SwashImpDepM1DHflow.ftn90:490–492` `a(nm) = -fac2`<br>`c(nm) =  fac1`<br>`b(nm) =  denom - a(nm) - c(nm)` | F 표기 차이 | 해석: `humn`을 곱한 두 이웃 이류 계수는 같은 공유 플럭스의 반대 부호가 된다. ST1-056·177·178은 이 대응을 가리킨다. 대각 성분과 시간 수심 변화를 포함하는 전체 행렬이 반대칭이라는 주장은 아니다. |
| theory-framework:ST1-227 | 번호 없는 정수압 구동력 | swashtech PDF p.56: `g\overline{\tilde\eta^{(0)}}\odot\tilde{\mathbb D}^0\tilde\zeta^{(0)}`; `\odot`는 같은 길이의 성분별 곱. | `src/SwashImpDepM2DHflow.ftn90:637` `zgrad = grav * (s0(nmu) - s0(nm)) / gvu(nm)`; `src/SwashUpdateDepths.ftn90:201` `hum(nm) = 0.5 * ( hs(nm) + hs(nmu) )` | F 표기 차이 | 해석: 유속식의 `zgrad`에 면 수심과 쌍대 변 길이를 곱하면 문서의 선적분 운동량 구동력이 된다. |
| theory-framework:ST1-228 | 번호 없는 이류와 비대각 조건 | swashtech PDF p.56–57: `A\mathbf u=\nabla\cdot(\mathbf q\otimes\mathbf u)`; `\mathbb A\tilde\upsilon^{(1)}`; `N_e\times N_e`; `skew-symmetric off-diagonal part`; `not a topological operator`. | `src/SwashImpDepM1DHflow.ftn90:458–459` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)`<br>`fac2 = 0.25 * dt * rdx * qm(nm ) / humn(nm)`; `src/SwashImpDepM1DHflow.ftn90:490–491` `a(nm) = -fac2`<br>`c(nm) =  fac1` | F 표기 차이 | 거리와 수심 계수를 포함하는 질량 가중 반대칭 비대각항이다. 임의 상류차분의 계수가 같은 성질을 가진다고 쓰지 않는다. |
| theory-framework:ST1-229 | 식 (2.23) 흐름방정식 | swashtech PDF p.57: `\frac{d\tilde\gamma^{(1)}}{dt}+\mathbb A\tilde\upsilon^{(1)}=-g\overline{\tilde\eta^{(0)}}\odot\tilde{\mathbb D}^0\tilde\zeta^{(0)}` | `src/SwashImpDepM1DHflow.ftn90:493` `d(nm) = (1.+cvegu(nm,1,2)+cpomu(nm,1)+a(nm)+c(nm)) * u0(nm) - a(nm) * u0(nmd) - c(nm) * u0(nmu) - dt * contrib`; `src/SwashImpDepM1DHflow.ftn90:472` `zgrad = grav * rdx * (s0(nmu) - s0(nm))` | F 표기 차이 | 문서의 선적분 흐름을 점 유속·질량 가중 이류 계수로 표현한다. 외력을 끈 부분계에 대응한다. 시간적분은 분할 단계이므로 문서의 반이산 보존을 시간까지 확장하지 않는다. |
| theory-framework:ST1-239 | 식 (2.25) 순환 폐쇄 | swashtech PDF p.59: `\tilde\gamma^{(1)}=\widetilde{\tilde\eta^{(0)}}\odot\tilde\upsilon^{(1)}` | `src/SwashUpdateDepths.ftn90:212` `humn = 1.5*hum - 0.5*humo`; `src/SwashImpDepM1DHflow.ftn90:458` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)` | F 표기 차이 | 해석: 코드는 면의 질량 가중치와 점 유속을 분리한다. 문서의 선적분 순환에는 쌍대 변 길이가 추가된다. 코드의 시간 외삽은 문서의 공간 보간 정의와 별도로 다룬다. 해석: 점 유속식의 질량 가중량에 쌍대 변 길이 `d_f`를 곱한 값은 `\gamma_f=d_fh_fu_f`이다. |
| theory-framework:ST1-241 | 식 (2.27) 순환방정식 | swashtech PDF p.59: `\frac{d\left(\widetilde{\tilde\eta^{(0)}}\odot\tilde\upsilon^{(1)}\right)}{dt}+\mathbb A\tilde\upsilon^{(1)}=-g\overline{\tilde\eta^{(0)}}\odot\tilde{\mathbb D}^0\tilde\zeta^{(0)}` | `src/SwashImpDepM1DHflow.ftn90:493` `d(nm) = (1.+cvegu(nm,1,2)+cpomu(nm,1)+a(nm)+c(nm)) * u0(nm) - a(nm) * u0(nmd) - c(nm) * u0(nmu) - dt * contrib` | F 표기 차이 | ST1-229에 순환 폐쇄를 대입한 식이다. 코드는 유속 방정식의 질량 가중 계수로 계산한다. |
| theory-framework:ST1-290 | 유출 Courant 수와 수심 경고 | swashtech PDF p.1–66에 이 경고 조건 없음. swashuse PDF p.99는 흐름 Courant 수 제한을 설명한다. | `src/SwashImpDep1DHflow.ftn90:1179` `cfl = sumqf * dt * rdx / hs(nm)`; `src/SwashImpDep1DHflow.ftn90:1192–1195` `if ( .not. cflmax < 1. .and. INODE == MASTER ) then`<br>`!`<br>`call msgerr ( 1, 'positivity of the water depth cannot be guaranteed')`<br>`call msgerr ( 0, 'It is advised to reduce the time step' )`; 같은 파일 `src/SwashImpDep1DHflow.ftn90:1152` `if ( inewt == 0 ) then`; `src/SwashImpDep1DHflow.ftn90:1177` `if ( hs(nm) > epsdry ) then`; `src/SwashImpDep1DHflow.ftn90:1188` `call SWREDUCE ( cflmax, 1, SWREAL, SWMAX )`. | C 문서 누락 | C는 기술문서 p.1–66에 없는 경고의 구현 조건이다. 비Newton 경로에서 건조 한계보다 깊은 점의 유출 플럭스로 Courant 수를 구한다. 전역 최댓값이 1 이상이면 MASTER가 인용한 경고를 낸다. 이 경고문 자체는 시간간격을 바꾸지 않는다. |
| theory-framework:ST1-322 | 이류·점성의 가중 대칭 | `source-analysis/swash-implicit-depthavg-flow.md:140` `의 반대부호 = skew-symmetric 이산 연산자 구현.`; `source-analysis/swash-implicit-depthavg-flow.md:142` `양쪽 부호 동일` | `src/SwashImpDepM1DHflow.ftn90:458–459` `fac1 = 0.25 * dt * rdx * qm(nmu) / humn(nm)`<br>`fac2 = 0.25 * dt * rdx * qm(nm ) / humn(nm)`; `src/SwashImpDepM1DHflow.ftn90:490–492` `a(nm) = -fac2`<br>`c(nm) =  fac1`<br>`b(nm) =  denom - a(nm) - c(nm)` | C 문서 누락 (현재 노트) | 계수의 부호만으로 점 유속 행렬 전체의 보통 반대칭을 주장하지 않는다. 해석: 균일 1D 격자에서 `M_i=humn_i\Delta x`이면 `M_i c_i=-M_{i+1}a_{i+1}`이다. 질량 변화 대각항도 에너지 조건에 포함한다. 점성은 같은 방식의 가중 대칭과 음의 소산을 구별한다. 이류의 가중 반대칭은 ST1-177·178과 같다. 점성의 가중 대칭은 ST1-175·176과 같다. C는 이 조건을 생략한 기존 노트의 설명에 한정한다. |
| theory-framework:ST1-323 | M 경로의 시간 보존 한계 | `source-analysis/swash-implicit-depthavg-flow.md:154` `헤더 Method는 M-1DH와 동일(strictly conservative, CN, skew-symmetric central, theta=0.5)` | `src/SwashImpDepM1DHflow.ftn90:46–47` `!         to the divergence operator. However, due to the time splitting between the surface gradient and other`<br>`!         terms of the momentum equation, the energy is not strictly conservative in time. Nevertheless, the` | C 문서 누락 (현재 노트) | 공간의 질량·운동량 보존과 공간의 에너지 보존을 구별해 적는다. 시간 분할 때문에 시간 에너지는 엄밀 보존이 아니라 근사 보존이다. 외력·점성·마찰 활성 조건을 별도로 적는다. |
| theory-framework:ST1-333 | 보존 진단 설명의 보충 | `source-analysis/swash-implicit-depthavg-flow.md:147` `mass flux/에너지 진단`; 같은 줄 `비-M 1DH와 구조 동일.` | `src/SwashExpDep1DHflow.ftn90:1626` `vol = vol + s1(nm)`; `src/SwashExpDep2DHflow.ftn90:4905` `vol = vol + s1(nm)`; ST1-310의 반대 근거 검색과 면적 가중 비교를 적용한다. | E 코드 결함 후보(근거 중간) | 근거 강도: 중간. ST1-310과 같은 체적 진단 정의를 다룬다. 구조 격자의 ITEST 체적 진단은 면적·길이를 곱하지 않은 수위 합을 출력한다. 균일 격자에서는 체적에 비례하지만 비균일 격자의 물리 체적으로 해석하면 결함 후보이다. 유동의 질량 갱신식과 구별한다. `8756667`·11.01의 `25c79e7`·문서 시점 `7949227`에서 식이 유지된 근거와 실제 호출·전처리 검사는 ST1-310에 연결한다. 같은 사실을 C와 E로 나눴던 분류를 E로 맞춘다. |
| theory-unstructured:ST2-365 | 마른 면에서 전체 마찰 배열 삭제 | swashtech PDF p.94의 마찰식은 젖은 다른 면의 힘을 지우지 않는다. 코드의 면별 계산과 전체 배열 대입을 대조했다. | `src/SwashExpDepUflow.ftn90:718` `cbot = 0.`; `src/SwashExpDepUflow.ftn90:789` `cbot = 0.`; `src/SwashImpDepUflow.ftn90:341` `cbot = 0.`; `src/SwashImpDepUflow.ftn90:412` `cbot = 0.`; 비교: `src/SwashExpDepUflow.ftn90:734` `cbot(iface) = 0.`; `src/SwashCompUFlow.ftn90:70–84`는 `kmax=1`에서 `mtimei=1`·2에 따라 두 경로를 호출한다. `src/SwashExpDepUflow.ftn90:698–718`의 젖은 내부면·젖은 경계면 다음 ELSE가 마른 면 대입에 도달한다. :1040과 `src/SwashImpDepUflow.ftn90:1041`의 `denom = 1. + dt * ( cbot(iface) + wndimp(iface) )`이 값을 소비한다. 문제 대입에는 비활성 전처리 접두어가 없다. | E 코드 결함 후보(강함) | 비구조 수심 평균의 명시적·반음해 유동은 마른 면에서 cbot 배열 전체를 0으로 만든다. 이 대입은 앞서 계산한 젖은 면의 바닥 마찰을 지울 수 있다. E 강함을 유지한다. 마찰을 끈 분기의 전체 초기화와 구별한다. [SWASH-git-verify-E2.md §2 ST2-365](../../../_staging/recovery/compare/SWASH-git-verify-E2.md). `835452f 2025-07-11 additional changes`가 두 파일의 마른 면 ELSE에 전체 대입을 추가했다. `7949227 2026-05-06 release v12.01`과 main에도 남는다. `608ffd7`·`9554c98`은 두 파일을 수정하지 않았다. 같은 판의 결함 후보이므로 A로 바꾸지 않는다. |
| theory-unstructured:ST2-398 | 반음해 수위의 행렬·속도 보정 | swashuse PDF p.99–100은 반음해 수위의 대칭 양의 정부호 선형계와 PCG를 설명한다. swashtech PDF p.97–98·111에는 아래 비구조 행렬 대입식이 없다. | `src/SwashImpDepUflow.ftn90:1059` `fac = grav * theta * theta2 * dt * dt`; `src/SwashImpDepUflow.ftn90:1067` `amat(icell,0) = cell(icell)%attr(CELLAREA)`; `src/SwashImpDepUflow.ftn90:1091–1093` `hf             = 0.5 * ( hs(icelll) + hs(icellr) )`, `ctrs           = -fac * lf * hu(iface) * rdx * hf / hum(iface)`, `amat(icell,jf) = ctrs`; `src/SwashImpDepUflow.ftn90:1108` `amat(icell,0) = amat(icell,0) - ctrs`; `src/SwashImpDepUflow.ftn90:1118` `rhs(icell) = rhs(icell) - dt * rsgn * lf * hu(iface) * ( theta*u1(iface) + (1.-theta)*u0(iface) )`; `src/SwashImpDepUflow.ftn90:1140` `call pcgu( amat, rhs, ds )`; `src/SwashImpDepUflow.ftn90:1285` `u1(iface) = u1(iface) - grav * theta2 * dt * rdx * hf * ( ds(icellr) - ds(icelll) ) / hum(iface)`; `src/SwashImpDepUflow.ftn90:1295` `s1 = s0 + ds` | C 문서 누락 | 대각은 셀 면적에서 시작한다. 면 계수는 두 시간 가중치와 `g\Delta t^2`를 포함한다. 수위 보정 뒤에 속도도 보정한다. 다층 대응은 `src/SwashImpLayUflow.ftn90:1683,1842,1854`에 있다. C는 행렬의 구체적인 면 계수와 수위·속도 보정식에 한정한다. |
| theory-unstructured:ST2-400 | 비음수 수심의 유출 합 검사 | swashtech PDF p.98은 면별 충분조건을 적는다. swashuse PDF p.140은 한 셀에서 모든 유속이 유출 방향일 때 더 엄격한 제한이 생길 수 있다고 설명한다. | `src/SwashImpDepUflow.ftn90:1299` `if ( inewt == 0 ) then`; `src/SwashImpDepUflow.ftn90:1334–1337` `uf = theta*u1(iface) + (1.-theta)*u0(iface)`, `qf = rsgn * lf * hu(iface) * uf`, `!`, `if ( qf > 0. ) sumqf = sumqf + qf`; `src/SwashImpDepUflow.ftn90:1347` `cfl = sumqf * dt / hs(icell) / area`; `src/SwashImpDepUflow.ftn90:1356–1359` `if ( .not. cflmax < 1. ) then`, `!`, `call msgerr ( 1, 'positivity of the water depth cannot be guaranteed')`, `call msgerr ( 0, 'It is advised to reduce the time step' )` | C 문서 누락 | 코드는 셀의 양의 유출 플럭스들을 합한다. 이 검사는 Newton을 끈 경로에서만 수행한다. 이 합 조건은 ST2-149의 면별 조건과 다르다. C는 그 경우의 비구조 유출 합 계산과 Newton 비활성 조건에 한정한다. |
