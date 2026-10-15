---
title: "SWASH scalar transport — 염분·온도·sediment 이류-확산 transport (ComputTrans dispatch + Exp*trans 커널)"
model: SWASH
component: src (scalar transport / constituents)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashComputTrans.ftn90 / SwashCompUTrans.ftn90 dispatch, SwashExpDep1DHtrans.ftn90 전문(:1-534), SwashExpDep2DHtrans/DepUtrans/Lay1DHtrans/Lay2DHtrans/LayUtrans Purpose·Method 블록 및 핵심 스킴부, SwashInitBCtrans.ftn90·SwashInitBCUtrans.ftn90 전문, SwashServices.ftn90 fluxlim(:307-452) file:line 인용. 2026-10-15 SWASH recovery 대조 보고서 반영" # [10-15 전수 검증 정정]
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH scalar transport — 염분·온도·sediment 이류-확산 transport

> SWASH의 constituent(염분 lsal·온도 ltemp·부유사 lsed) 이류-확산 transport 방정식 시간적분 커널. dispatch는 `SwashComputTrans`(구조격자)·`SwashCompUTrans`(비정형 삼각격자), 실제 솔버는 격자차원(1D/2D)×연직(depth-averaged/layer-averaged)×격자형태(구조/비정형) 조합 6개 `Swash{Exp}{Dep|Lay}{1DH|2DH|U}trans`. 경로: raw/source_code/swash/src/

## 1. dispatch 구조 (ComputTrans / CompUTrans)

`SwashComputTrans`의 Purpose: `"Computes constituents by means of solving the transport equations"` (`SwashComputTrans.ftn90:40`). 분기는 `oned`(1D/2D)와 `kmax`(연직 층수)에 따라:

| 모드 | 조건 | 호출 솔버 | 인용 |
|---|---|---|---|
| 구조 1D depth-avg | `oned .and. kmax==1` | `SwashExpDep1DHtrans` | `SwashComputTrans.ftn90:71-75` |
| 구조 1D layer-avg | `oned .and. kmax/=1` | `SwashExpLay1DHtrans` | `SwashComputTrans.ftn90:78-82` |
| 구조 2D depth-avg | `.not.oned .and. kmax==1` | `SwashExpDep2DHtrans` | `SwashComputTrans.ftn90:91-95` |
| 구조 2D layer-avg | `.not.oned .and. kmax/=1` | `SwashExpLay2DHtrans` | `SwashComputTrans.ftn90:98-102` |

비정형(삼각) 격자 dispatch는 `SwashCompUTrans` — Purpose `"... solving the transport equations on triangular mesh"` (`SwashCompUTrans.ftn90:40`). `kmax==1`이면 `SwashExpDepUtrans`, 아니면 `SwashExpLayUtrans` 호출 (`SwashCompUTrans.ftn90:66-78`).

두 dispatch 모두 마지막에 출력용 평균 농도 갱신: `if ( ltraoutp ) call SwashAverOutp ( 2 )` (`SwashComputTrans.ftn90:111`, `SwashCompUTrans.ftn90:84`). 솔버가 푸는 변수는 `rp(mcgrd,ltrans)` (current time level 농도), 이전 시각은 `rpo` (`SwashComputTrans.ftn90:75`, `SwashExpDep1DHtrans.ftn90:90-91`).

`ltrans`개 constituent를 루프하며, constituent 인덱스는 `lsal`(염분)·`ltemp`(온도)·`lsed`(부유사) (`SwashExpDep1DHtrans.ftn90:153,157-161`).

## 2. 지배 스킴 — depth-averaged 1DH (대표 구현, 전문 read)

`SwashExpDep1DHtrans`의 Method 블록(verbatim, `SwashExpDep1DHtrans.ftn90:42-61`):

```
!   The time integration is fully explicit.
!   The time integration with respect to the advective term is based on the predictor-corrector scheme
!   of MacCormack, while that for the diffusive term is based on Euler explicit.
!   The space discretization is based on the finite volume approach. The discretization is such that
!   it is consistent with the discretization of the global continuity equation.
!   The advective term is approximated by either first order upwind or higher order (flux-limited) scheme
!   (CDS, Fromm, BDF, QUICK, MUSCL, Koren, etc.). The higher order scheme is treated by defect correction
!   consistent with the MacCormack scheme.
!   The Thatcher-Harleman boundary condition is imposed at sea side for unsteady salt intrusion.
```

이류 스킴 핵심: MacCormack predictor-corrector = **(predictor) 1차 upwind으로 농도 갱신 → (corrector) flux-limited 고차 보정을 defect correction으로 추가**.

### 2.1 Prandtl-Schmidt 수 (확산계수 스케일링)

수심평균 1DH에서 염분·수온의 `psm`은 0.7이다. 같은 경로에서 부유사의 `psm`은 1.0이다. (`src/SwashExpDep1DHtrans.ftn90:157–161`) 다층 1DH의 부유사는 입력값 `snum`인 `psed(3)`을 사용한다. (`src/SwashExpLay1DHtrans.ftn90:159–162`; `src/SwashReadInput.ftn90:1442`) 두 경로의 수평 와점성계수 평균은 각각의 `psm`으로 나눠 확산계수에 적용한다. (`src/SwashExpDep1DHtrans.ftn90:303–305`; `src/SwashExpLay1DHtrans.ftn90:362–364`) [10-15 전수 검증 정정]

### 2.2 finite-volume 이류 flux — predictor (1차 upwind)

내부 cell-face 루프에서 mass flux `qx` 부호로 upwind 셀의 이전 농도를 취함 (`SwashExpDep1DHtrans.ftn90:285-293`):

```fortran
if ( qx(nm) > 0. ) then
   flux(nm) = qx(nm) * rpo(nm)     ! 좌측 셀에서 유입
else
   flux(nm) = qx(nm) * rpo(nmu)    ! 우측 셀에서 유입
endif
```

`momskip`(운동량 방정식 skip 시)일 때 mass flux를 `qx = hu * u1`로 재계산 (`SwashExpDep1DHtrans.ftn90:149`).

### 2.3 수평 확산 flux

유효 수평 확산계수 `dif2d` 결정 (`SwashExpDep1DHtrans.ftn90:297-313`):
- 사용자 상수 `hdiff > 0` → `dif2d = hdiff`
- 아니면 `ihvisc == 2 또는 3`(난류 모델) → `dif2d = 0.5*(vnu2d(nm)+vnu2d(nmu))/psm` (face 평균을 psm으로 나눔)
- 그 외 → `dif2d = 0.` (확산 없음)

안정성: 확산 stability 상한 `stabmx = 0.5*dx*dx/dt` (`SwashExpDep1DHtrans.ftn90:145`). `dif2d >= stabmx`면 clamp하고 불안정점 카운트 `icistb` 증가 (`SwashExpDep1DHtrans.ftn90:317-320`). 확산 flux는 face에서의 water depth 평균 가중:
```fortran
flux(nm) = flux(nm) - 0.5*(hso(nm)+hso(nmu))*dif2d*rdx*(rpo(nmu)-rpo(nm))
```
(`SwashExpDep1DHtrans.ftn90:324`).

### 2.4 농도 update (finite-volume, mass-conservative)

총 flux로 셀 농도 갱신 — 우측 face flux를 빼고(`-dt*rdx*flux(nm)`, `:343`) 좌측 face flux를 더한 뒤(`+dt*rdx*flux(nmd)`, `:360`) water depth `hs(nm)`로 나눠 depth-averaged 농도 산출 (`SwashExpDep1DHtrans.ftn90:343,360,364`). 건조점은 `hs(nm) > epsdry` 조건으로 skip (`:339,356`).

### 2.5 corrector — 고차 flux-limited 보정 (defect correction)

스킴 선택 파라미터 `propsc = nint(pnums(46))`; `propsc /= 1`이면 고차 보정 활성 (`SwashExpDep1DHtrans.ftn90:377-379`). 파라미터 `kappa=pnums(47)`, `mbound=pnums(48)`, `phieby=pnums(49)` (`:381-383`). upwind 방향에 따라 consecutive gradient 두 개(`grad1`,`grad2`)를 잡아 `dc = 0.5*fluxlim(grad1,grad2)` 보정 flux 계산 (`:406-422`), 그 후 §2.4와 동일한 방식으로 농도 재보정 (`:445,462,466`).

### 2.6 flux limiter (SwashServices::fluxlim)

`fluxlim(a,b)` Purpose `"Computes the flux limiter for higher order correction"` (`SwashServices.ftn90:346`). 입력은 numerator/denominator gradient, gradient 비 `r = a/b` (`:387-395`). `propsc` 값별 limiter (`SwashServices.ftn90:397-450`):

| propsc | limiter 클래스 | 식 핵심 | 인용 |
|---|---|---|---|
| 3 | 선형 kappa-scheme (BDF/CDS/QUICK/Fromm) | $0.5(1+\kappa)a + 0.5(1-\kappa)b$ | `:397-401` |
| 4 | Sweby Phi-limiter (minmod/superbee) | $\max(\max(0,\min(\phi r,1)),\min(r,\phi))\cdot b$ | `:403-407` |
| 5 | R-kappa limiter (Van Leer) | $r<0$이면 0, 그 외 kappa·r 다항식 ×b | `:409-435` |
| 6 | PL-kappa limiter (MUSCL/Koren/SMART) | $\max(0,\min(m_b r, \min(m_b, 0.5(1+\kappa)r+0.5(1-\kappa))))\cdot b$ | `:437-443` |

unknown propsc는 `msgerr(4,...)` fatal (`:447`). Method 주석: limiter는 solution gradient(=denominator)와 곱해진 값 (`SwashServices.ftn90:359`). 상세는 Zijlema 박사 논문 인용 (`:357`).

## 3. 경계조건 — Thatcher-Harleman (염분 침입)

Method 블록 인용: `"The Thatcher-Harleman boundary condition is imposed at sea side for unsteady salt intrusion. The constituent return time is given by the user."` + 출처 Thatcher & Harleman (1972) MIT Tech Report 144 (`SwashExpDep1DHtrans.ftn90:56-61`).

좌측 경계 처리(`SwashExpDep1DHtrans.ftn90:171-217`):
- open + inflow(`qx(nmf)>0`): 염분이면 return-time 가중으로 cosine 완화
  ```fortran
  fac = max(icretl(1,1),0.) / max(tcret,dt)
  rp(nmf,l) = coutl(1,1) + 0.5*( cbndl(1,1,l) - coutl(1,1) )*( 1. + cos(fac*pi) )
  ```
  (`:186-188`). 비염분 constituent는 단순 Dirichlet `rp=cbndl` (`:190`). return time counter `icretl`는 매 step `dt`씩 감소 (`:188`).
- open + outflow: upwind으로 flux 잡고 outflow 농도를 1차 이류 advection으로 update, 염분이면 `coutl`(유출 농도) 저장 + `icretl=tcret` 리셋 (`:197-204`).
- closed(`ibl==1`): flux=0, mirror `rp(nmf)=rp(nmfu)` (`:212-213`).

우측 경계는 대칭 구조 (`SwashExpDep1DHtrans.ftn90:219-265`); inflow/outflow 부호가 좌측과 반대(`qx(nml)>0`이 outflow).

`tcret`(constituent return time)는 사용자 지정. `coutl/coutr`(좌·우 유출 농도), `icretl/icretr`(잔여 return time), `cbndl/cbndr`(경계 입력 농도)가 상태 변수.

## 4. 초기화 & Dirichlet 경계값 저장 (InitBCtrans / InitBCUtrans)

`SwashInitBCtrans` Purpose: `"Initializes transport constituents based on input fields and stores boundary values as Dirichlet type condition"` (`SwashInitBCtrans.ftn90:40`). 세 constituent를 각각 처리 (`lsal>0`, `ltemp>0`, `lsed>0` 블록; `:85,234,383`).

입력 필드 → wl-point 농도 보간:
- 1D: face 입력 필드 두 점 평균 `rp(nm,:,lsal) = 0.5*(salf(nm,:)+salf(nmd,:))` (`SwashInitBCtrans.ftn90:100`).
- 2D: 4점 평균 `rp = 0.25*(salf(nm)+salf(nmd)+salf(ndm)+salf(ndmd))` (`:146`). 영구 건조 이웃은 mirror 처리 (`:142-144`).
- **부유사는 질량농도 → 부피농도 변환**: 입력을 `/rhos`(입자 밀도)로 나눔 (`SwashInitBCtrans.ftn90:398,444`). 온도/염분은 변환 없음.

병렬: subdomain 간 `SWEXCHG` 교환 (`:106,157`), 주기경계는 `periodic` 호출 (`:192,226`). 경계값은 `cbndl/cbndr`(좌우, x), `cbndb/cbndt`(아래/위, y)에 Dirichlet로 저장 (`:116,121,176,183,210,217`).

비정형(삼각) 버전 `SwashInitBCUtrans` Purpose: `"... in case of unstructured grid"` (`SwashInitBCUtrans.ftn90:40`). centroid 농도 = 셀 3 vertex 입력 평균 `rp(icell,:,lsal) = (salf(v1)+salf(v2)+salf(v3))/3.` (`:88-92`). 경계 face는 2 vertex 평균을 `cbndu`·`bcrp`에 저장 (`:98-110`). 부유사 동일하게 `/rhos` (`:160,175`).

## 5. layer-averaged transport — 연직 항의 semi-implicit (Lay1DH 대표)

`SwashExpLay1DHtrans` Method(verbatim 발췌, `SwashExpLay1DHtrans.ftn90:45-60`):
```
!   The time integration is fully explicit, except for the vertical terms (see below).
!   The horizontal advective term ... predictor-corrector scheme of MacCormack ...
!   The space discretization of the vertical advective and diffusivity terms is based on higher order
!   (flux-limited) schemes and central differences, respectively, in a finite volume fashion.
!   These vertical terms are treated semi-implicit. This results in a tri-diagonal system.
```

수평 항은 depth-averaged와 동일(MacCormack + flux-limiter). **연직 항만 semi-implicit** — implicitness factor `theta = pnums(33)` (`SwashExpLay1DHtrans.ftn90:151`).

### 5.1 tri-diagonal 시스템

연직 이산화로 3중대각 matrix `amatc(nm,k,1:3)` (1=main diag, 2=하위, 3=상위) 와 우변 `rhsc` 구성. 대각 초기화 `amatc(nm,k,1) = hks(nm,k)/dt` (셀 두께/dt) (`SwashExpLay1DHtrans.ftn90:203`).

연직 이류(implicit part): vertical velocity `w = wom(nm,k-1)`, 셀 두께 합 `fac = hks(k-1)+hks(k)` 기준으로 `theta` 가중 계수를 대각에 누적 (`:507-549`). 고차 스킴 분기는 별도 `propsc=nint(pnums(51))`, `kappa=pnums(52)` 등 (`:488-491`) — 수평과 다른 파라미터 슬롯.

연직 확산(central): `fac1 = 2.*theta*vnu3d(nm,k-1)/psm/fac`를 대각/비대각에 대칭 누적 (`:583-588`).

명시적 part(`theta /= 1.`)는 우변 `rhsc`에 `(1-theta)` 가중 항 추가 (`:607-665`).

### 5.2 Thomas 알고리즘 (tri-diagonal 풀이)

전방소거 + 후방대입으로 풀이 (`SwashExpLay1DHtrans.ftn90:685-703`):
```fortran
bi = 1./amatc(nm,1,1); amatc(nm,1,1)=bi; amatc(nm,1,3)=amatc(nm,1,3)*bi; rhsc(nm,1)=rhsc(nm,1)*bi
do k=2,kmax
   bi = 1./(amatc(nm,k,1)-amatc(nm,k,2)*amatc(nm,k-1,3))
   ...
enddo
rp(nm,kmax,l)=rhsc(nm,kmax)
do k=kmax-1,1,-1
   rp(nm,k,l)=rhsc(nm,k)-amatc(nm,k,3)*rp(nm,k+1,l)
enddo
```

### 5.3 anti-creep 보정

sigma 좌표 인공 확산(creep) 억제: `if ( icreep == 1 ) call SwashAntiCreep1DH(amatc,rhsc,rpo,kgrpnt,psm)` (`src/SwashExpLay1DHtrans.ftn90:677`). 2D 대응은 `SwashAntiCreep2DH`다. (`src/SwashExpLay2DHtrans.ftn90:951`) [10-15 대조 정정]
STANDARD는 층 경사와 연직 농도 구배의 곱을 더한다. SVK 확산의 보간은 MUSCL이다. (`src/SwashAntiCreep1DH.ftn90:170–182`; `src/SwashHDiffZplane1DH.ftn90:285–294`; `src/SwashHDiffZplane2DH.ftn90:315`) [10-15 대조 정정]
원문 식은 아래 차이 표의 `inputs-physics-numerics:SI2-283`과 `inputs-physics-numerics:SI2-284`에 있다. [10-15 대조 정정]

### 5.4 sediment 침식/퇴적 (bed 경계 mass exchange)

부유사(`l==lsed`)일 때 bed 셀(`k=kmax`)에 erosion/deposition flux를 추가한다. (`src/SwashExpLay1DHtrans.ftn90:421–484`) `src/SwashModule1.ftn90:539–552`가 psed의 정의를 제공한다. [10-15 대조 정정]

- **noncohesive sand**(`psed(9)>0`): bed 마찰속도 `fac = (0.3+psed(7))*rtur(nm,kmax,1)`(난류운동에너지 기반, 파괴 난류 포함 가능). erosion = pickup function `rhsc += psed(9)*((fac-psed(5))/psed(5))**1.5` (임계 `psed(5)` 초과 시), deposition = fall velocity `amatc(nm,kmax,1) += psed(1)` (`:439-447`).
- **cohesive mud**(`psed(10)>0`): bed 전단응력은 `fac = 0.3*rhow*rtur(nm,kmax,1)`이다. 침식은 `if( fac > psed(10) ) rhsc(nm,kmax) = rhsc(nm,kmax) + psed(12) * ( fac/psed(10) - 1. )`이다. (`src/SwashExpLay1DHtrans.ftn90:468–472`) 퇴적 항은 `psed(1)*(1.-fac/psed(11))`이다. 조건은 `fac<psed(11)`이다. (`src/SwashExpLay1DHtrans.ftn90:476`) [10-15 대조 정정]
- erate는 문서에서 질량 flux 단위이다. 수송 상태는 체적 농도이다. 활성 침식 대입에는 rhos 환산이 없다. 이 차이는 E 강함의 코드 결함 후보이다. (swashuse PDF p.87: “entrainment rate for erosion (in kg/m2/s).”; swashuse PDF p.85: “cb is the (volumetric) sediment concentration”; `src/SwashDensity.ftn90:66`; `src/SwashInitBCtrans.ftn90:398`; `src/SwashExpLay1DHtrans.ftn90:472`) [10-15 대조 정정]

`psed(1)`이 fall(settling) velocity 계수임이 deposition 양쪽에 공통 등장으로 확인됨 (`:447,476`).

## 6. 차원·격자 변형별 구현 요약

| 솔버 파일 | 차원 | 연직 | 격자 | 비고 | 인용 |
|---|---|---|---|---|---|
| `SwashExpDep1DHtrans` | 1D | depth-avg | 구조 | 대표 구현, 전문 분석 | `:40-61` |
| `SwashExpDep2DHtrans` | 2D | depth-avg | 구조 | x·y 양방향 1차 upwind(`qx`,`qy` 부호) | `:40-61,429,509` |
| `SwashExpDepUtrans` | 2D | depth-avg | 삼각 | cell-centered FV, **local time stepping**, centroid 농도 | `SwashExpDepUtrans.ftn90:40-54` |
| `SwashExpLay1DHtrans` | 1D | layer-avg | 구조 | 연직 semi-implicit tri-diag | `:41-60` |
| `SwashExpLay2DHtrans` | 2D | layer-avg | 구조 | 위 + y방향, AntiCreep2DH | `SwashExpLay2DHtrans.ftn90:951` |
| `SwashExpLayUtrans` | 2D | layer-avg | 삼각 | 삼각 FV + 연직 semi-implicit | `SwashExpLayUtrans.ftn90:38-60` |

비정형(U) 솔버의 추가 특징(verbatim, `SwashExpDepUtrans.ftn90:44-54`):
```
!   The time integration is fully explicit. Local time stepping is employed.
!   The space discretization is a cell-centered finite volume discretization ...
!   The concentration is located at the centroid of the triangular cell.
!   The discretization is mass conservative and complies with the discrete maximum principle.
!   ... For the r-ratio the most upwave vertex of upwind cell is used.
```
즉 비정형 격자는 **local time stepping**(셀별 substep) 채택 — 인자에 `rp0/rp1/rpi`(substep·time-step level 농도)가 등장 (`SwashExpDepUtrans.ftn90:87-90`). 구조격자(`Dep1DH/2DH`)는 global explicit이라 이 인자 없음.

## 7. 핵심 데이터 흐름 / 상태 변수

| 변수 | 의미 | 출처 |
|---|---|---|
| `rp(mcgrd,ltrans)` | 현재 시각 농도 (출력 변수) | `SwashExpDep1DHtrans.ftn90:90` |
| `rpo` | 이전 시각 농도 (upwind flux 입력) | `:91,167` |
| `flux` | cell-face 총 flux (이류+확산) | `:88` |
| `qx`/`qy`/`qn` | mass flux (x/y/face-normal) | `:89`, `SwashExpLay1DHtrans` qy, `SwashExpDepUtrans.ftn90:85` |
| `hs`/`hso` | water depth (현재/이전) | `:324,339,364` |
| `psm` | Prandtl-Schmidt 수 | `:121,157-161` |
| `cbndl/r/b/t`, `cbndu` | Dirichlet 경계 농도(x좌/우, y하/상, 비정형 face) | `SwashInitBCtrans.ftn90:116,176,210,217`; `SwashInitBCUtrans.ftn90:107` |
| `coutl/r`,`icretl/r`,`tcret` | Thatcher-Harleman 유출농도·잔여 return time·return time | `SwashExpDep1DHtrans.ftn90:186,202-203` |
| `psed()` | sediment의 수송·바닥교환 매개변수 | `src/SwashModule1.ftn90:539–552` [10-15 대조 정정] |

## 8. 수송 매개변수와 층 순서 [10-15 대조 정정]

- STANDARD는 층 경사와 연직 농도 구배의 곱을 더한다. SVK 확산의 보간은 MUSCL이다. (`src/SwashAntiCreep1DH.ftn90:170–182`; `src/SwashHDiffZplane1DH.ftn90:285–294`; `src/SwashHDiffZplane2DH.ftn90:315`) [10-15 대조 정정]
- `src/SwashModule1.ftn90:539–552`가 psed의 정의를 제공한다. psed(5)는 입력 때 무차원 임계 Shields 수이다. `src/SwashCheckPrep.ftn90:926`이 이를 임계 마찰속도 제곱으로 변환한다. psed(10)·psed(11)는 N/m² 응력이다. psed(12)는 침식률이다. ALFA와 AK는 각각 psed(4)와 psed(13)이다. [10-15 대조 정정] (단위: swashuse PDF p.87. 입력 이름: `src/SwashReadInput.ftn90:1444,1458`.) [10-15 전수 검증 보완]
- k−1은 위층이다. k는 그 아래층이다. 수층 침강은 위층의 손실과 아래층의 유입으로 연결된다. 바닥 퇴적은 최하층 kmax에서 처리한다. (`src/SwashExpLay1DHtrans.ftn90:447,594–595`) [10-15 대조 정정]

## 문서와 코드 차이 (10-15 대조)

행 ID의 약칭은 [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md)와 [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md)를 가리킨다.
문서 인용은 PDF 쪽 번호를 쓴다.
swashuse의 인쇄 쪽 번호는 PDF 쪽 번호에서 8을 뺀다.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227` 2026-05-06 "release v12.01"에서 마지막 변경. 코드 판: VERNUM 12.01, 공개 저장소 main `a486d5f` 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| guide-syntax-build:SG1-887 | 침전물 입력 단위와 거칠기 | swashuse PDF p.87은 FALL의 mm/s와 SIZE의 µm를 명시한다. p.86은 입경에 따른 거칠기 5.5d50을 설명한다. | `src/SwashCheckPrep.ftn90:824–838` `if ( lsed > 0 ) then` / `if ( psed(1) < 0. ) then` / `call msgerr (1, 'incorrect sediment settling velocity')` / `psed(1) = 0.` / `else` / `! fall velocity is given by user in millimeter per second` / `psed(1) = psed(1) * 1.e-3` / `endif` / `if ( psed(2) < 0. ) then` / `call msgerr (1, 'incorrect median sediment diameter')` / `psed(2) = 0.` / `else` / `! grain size is given by user in micrometer` / `psed(2) = psed(2) * 1.e-6` / `endif`; `src/SwashCheckPrep.ftn90:843–856` `if ( lsed > 0 .and. (psed(2) /= 0. .or. psed(10) /= 0. .or. lsal > 0 .or. ltemp > 0) .and. kmax > 1 .and. lmixt ) then` / `if ( iturb /= 1 ) then` / `call msgerr (3, 'vertical mixing (k-epsilon model) must be employed in case of sediment transport')` / `endif` / `if ( irough /= 4 ) then` / `call msgerr (3, 'logarithmic wall-law must be applied in case of sediment transport')` / `endif` / `if ( instead ) then` / `call msgerr (1, 'no steady flow condition in case of sediment transport')` / `instead = .false.` / `endif` / `! calculate the Nikuradse roughness height in case of sand transport, if appropriate` / `if ( .not.varfr .and. .not. pbot(2) /= 0. .and. psed(2) /= 0. ) then` / `pbot(2) = psed(4) * psed(2)` `src/SwashInit.ftn90:378` `psed(4) = 5.5`; swashuse PDF p.86–87. | C 문서 누락 | FALL·SIZE의 SI 단위 변환과 입경에 비례하는 거칠기 식은 문서에 대응한다. C는 음수 입력의 0 보정과 거칠기 자동 대입의 정확한 조건에 한정한다. 거칠기는 843행의 침전물·다층·혼합밀도 조건 안에서 `if ( .not.varfr .and. .not. pbot(2) /= 0. .and. psed(2) /= 0. ) then`일 때만 `pbot(2) = psed(4) * psed(2)`로 대입한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| inputs-physics-numerics:SI2-141 | erate 단위 | swashuse PDF p.87: “entrainment rate for erosion (in kg/m2/s).”;<br>swashuse PDF p.85: “cb is the (volumetric) sediment concentration” / | `src/SwashReadInput.ftn90:1424`: `call INREAL( 'ERATE', psed(12), 'REQ', 0.)`;<br>`src/SwashExpLay1DHtrans.ftn90:472`: `if( fac > psed(10) ) rhsc(nm,kmax) = rhsc(nm,kmax) + psed(12) * ( fac/psed(10) - 1. )`;<br>`src/SwashInitBCtrans.ftn90:398`: `rp(nm,:,lsed) = 0.5 * ( sedf(nm,:) + sedf(nmd,:) ) / rhos`;<br>`src/SwashDensity.ftn90:66`: `real*8        :: c        ! local sediment volume concentration`;<br>`src/SwashExpLay1DHtrans.ftn90:423`: `if ( l == lsed ) then`; 455행: `if ( psed(10) > 0. ) then`; 464행: `if ( hs(nm) > epsdry ) then`; 700행: `rp(nm,kmax,l) = rhsc(nm,kmax)`.<br>`src/SwashCheckPrep.ftn90:804–818`은 단일층·DENSITY NO에서 침식을 끈다. 843–848행은 활성 다층 혼합에 연직 k–epsilon과 LOGLAW를 요구한다. | E 코드 결함 후보 | 해석: erate는 문서에서 질량 flux 단위이다. 수송 상태는 체적 농도이다. 활성 침식 대입에는 rhos 환산이 없다. 이 차이는 E 강함의 코드 결함 후보이다. 구조 침식식은 `8756667:src/SwashExpLay1DHtrans.ftn90:472`부터, 비구조 식은 `9b8a012:src/SwashExpLayUtrans.ftn90:662`부터 같다. `9554c98`은 수송 초기화 위치만 옮겼으며 침식률의 단위를 변환하지 않는다. 활성 다층 경로에서 kg/m²/s의 erate를 체적 농도식에 직접 더하므로 E 강함을 유지한다. [10-15 결론 검증 보완] [10-15 git 이력 판정] |
| inputs-physics-numerics:SI2-146 | TRANSPORT 본문의 ALFA·CRSN·CP·EK 설명 누락 | swashuse PDF p.83–87 본문에는 ALFA·CRSN·CP·EK 입력 설명이 없다. p.159 부록은 `[alfa] [crsn] [cp] [ek]`를 표시한다. | `src/SwashReadInput.ftn90:1400–1402`: `!           [alfa] [crsn] [cp] [ek]   (not documented)                          &` / `!` / `!           ANTICreep  STAndard \| SVK \| None`; `src/SwashReadInput.ftn90:1458–1461`: `call INREAL( 'ALFA', psed(4), 'STA', 5.5    )` / `call INREAL( 'CRSN', psed(5), 'STA', 0.05   )` / `call INREAL( 'CP'  , psed(6), 'STA', 0.00033)` / `call INREAL( 'EK'  , psed(7), 'UNC', 0.     )`;<br>`misc/swash.edt:194`의 `[alfa] [crsn] [cp] [ek]`. | C 문서 누락 | 네 값은 거칠기 배율·임계 Shields 수·pickup 계수·쇄파 난류 추가 계수이다. ALFA와 AK는 서로 다른 대상이다. C는 p.83–87 본문의 입력 의미·기본값 설명 누락으로 한정한다. 부록에는 네 매개변수 이름이 있다. [10-15 결론 검증 정정] [10-15 전수 검증 정정] |
| inputs-physics-numerics:SI2-147 | 별칭·추가 입력 검사 | — | `src/SwashReadInput.ftn90:1406`: `if ( KEYWIS ('TRANSP') .or. KEYWIS('CONST') ) then`; `src/SwashReadInput.ftn90:1447`: `if ( KEYWIS ('DENS') .or. KEYWIS('MIXT') ) then`; `src/SwashReadInput.ftn90:1468`: `else if ( KEYWIS ('STA') .or. KEYWIS ('Y') ) then`;<br>`src/SwashCheckPrep.ftn90:789–791`: `if ( tcret < 0. ) then` / `call msgerr (1, 'incorrect return time for salt intrusion')` / `tcret = 0.`;<br>`src/SwashCheckPrep.ftn90:825–834`는 음수 침강속도와 음수 입경을 각각 0으로 복구한다. | C 문서 누락 | 음수 복귀시간은 0으로 복구한다. 음수 침강속도와 입경도 0으로 복구한다. [10-15 결론 검증 보완] |
| inputs-physics-numerics:SI2-148 | 수평 확산의 실제 계수·안정성 | — | `src/SwashExpLay1DHtrans.ftn90:159–162`: `if ( l == lsal .or. l == ltemp ) then` / `psm = 0.7` / `else if ( l == lsed ) then` / `psm = psed(3)`; `src/SwashExpLay1DHtrans.ftn90:364`: `dif2d = 0.5 * ( vnu2d(nm) + vnu2d(nmu) ) / psm`; `src/SwashExpLay1DHtrans.ftn90:376–377`: `if ( .not. dif2d < stabmx ) then` / `dif2d  = stabmx` | C 문서 누락 | 염분·수온의 비율은 고정 0.7이다. 부유사는 snum을 사용한다. 코드가 실제 확산계수를 안정성 상한으로 자른다. |
| inputs-physics-numerics:SI2-149 | ANTICREEP 추가 조건 | — | `src/SwashCheckPrep.ftn90:797`: `if ( itrans == 0 .or. kmax == 1 ) icreep = 0`; `src/SwashCheckPrep.ftn90:799`: `if ( icreep == 2 .and. ( lreptx .or. lrepty ) ) call msgerr (3,'repeating grid not allowed in case of Stelling and Van Kester method')` | C 문서 누락 | 수송이 없거나 단일층이면 anti-creep를 해제한다. SVK는 반복 격자를 허용하지 않는다. |
| inputs-physics-numerics:SI2-150 | 바닥교환 해제와 매개변수 초기화 | swashuse PDF p.23: “In the depth-averaged mode, there is no mass exchange of suspended sediment between the bed and the flow.”; p.86: “Also, there is no sedimentation and erosion near the bed.” | `src/SwashCheckPrep.ftn90:804–810`: `if ( kmax == 1 ) then` / `call msgerr (1, 'no mass exchange of sediment in depth-averaged mode')` / `psed( 1) = 0.` / `psed( 2) = 0.` / `psed(10) = 0.` / `psed(11) = 0.` / `psed(12) = 0.`; `src/SwashCheckPrep.ftn90:812–818`: `if ( .not.lmixt ) then` / `call msgerr (1, 'no mass exchange of sediment for tracer')` / `psed( 1) = 0.` / `psed( 2) = 0.` / `psed(10) = 0.` / `psed(11) = 0.` / `psed(12) = 0.`; | C 문서 누락 | 단일층과 DENSITY NO의 바닥교환 해제는 각각 swashuse PDF p.23과 p.86의 설명과 일치한다. C는 이때 침강속도·입경·임계응력·침식률을 모두 0으로 덮어쓰는 매개변수 처리의 설명 누락으로 한정한다. [10-15 결론 검증 정정] |
| inputs-physics-numerics:SI2-151 | Eckart 상태방정식·밀도 기준 | — | `src/SwashDensity.ftn90:105–108`: `p0        =  5890d0  + (  38d0  - 375d-3*t)*t +              3d0*s` / `lambda    = 17795d-1 + (1125d-2 - 745d-4*t)*t - (38d-1 + 1d-2*t)*s` / `!` / `rho(n,k) = p0/(lambda+0.698*p0)`; `src/SwashDensity.ftn90:163`: `if ( lsal > 0 .or. ltemp > 0 ) rho = 1000.*rho - rhow` | C 문서 누락 | 코드는 Eckart 밀도를 계산한 뒤 기준 밀도를 뺀 편차를 저장한다. `rho`를 절대 밀도로 설명하면 다르다. |
| inputs-physics-numerics:SI2-152 | 침강 방향·최하층 | — | `src/SwashExpLay1DHtrans.ftn90:590`: `! include fall velocity in case of sediment transport`; `src/SwashExpLay1DHtrans.ftn90:594–595`: `amatc(nm,k-1,1) = amatc(nm,k-1,1) +     psed(1)` / `amatc(nm,k  ,2) = amatc(nm,k  ,2) - kwu*psed(1)`; `src/SwashExpLay1DHtrans.ftn90:445`: `! include downward sediment flux (deposition) by means of fall velocity`; `src/SwashExpLay1DHtrans.ftn90:447`: `amatc(nm,kmax,1) = amatc(nm,kmax,1) + psed(1)` | C 문서 누락 | k−1은 위층이다. k는 그 아래층이다. 수층 침강은 위층의 손실과 아래층의 유입으로 연결된다. 바닥 퇴적은 최하층 kmax에서 처리한다. |
| inputs-physics-numerics:SI2-243 | limiter 실제 식·보호값 | — | `src/SwashServices.ftn90:387`: `if ( abs(b) > 1.e-10 ) then`; `src/SwashServices.ftn90:389`: `r = a / b`; `src/SwashServices.ftn90:393`: `r = 0.`; `src/SwashServices.ftn90:421`: `fluxlim = 2.*r * ( -r*r + (3.+kappa)*r - kappa )/((1.+r)**2)`; `src/SwashServices.ftn90:425`: `fluxlim = ( (2.+kappa)*r - kappa )/( 1.+r )`; `src/SwashServices.ftn90:443`: `fluxlim = max( 0., min( mbound*r, fac ) ) * b` | C 문서 누락 | 구배 b의 크기가 1e−10 이하이면 `r=0`이다. R-kappa의 kappa<0 분기는 `r≤1`과 `r>1`의 식이 다르다. Sweby·PL-kappa의 식은 SI2-228/230에 적었다. |
| inputs-physics-numerics:SI2-283 | STANDARD anti-creep 실제 곱 | — | `src/SwashAntiCreep1DH.ftn90:170–182`: `flux(nm,k,1) = 0.5 * ( hkso(nm,k) + hkso(nmu,k) ) * dif2d * rdx *                    &` / `!         --- compute d z(k) / dx` / `0.5 * ( zkso(nmu,k-1) - zkso(nm,k-1) + zkso(nmu,k) - zkso(nm,k) ) *   &` / `!         --- compute d c(k-1/2) / dz` / `( rpo(nmu,kd) + rpo(nm,kd) - rpo(nmu,ku) - rpo(nm,ku) ) * 2. /        &` / `( (ku-k) * (zkso(nmu,k -1) - zkso(nmu,ku)) +                          &` / `(k-kd) * (zkso(nmu,kd-1) - zkso(nmu,k )) +                          &` / `(ku-k) * (zkso(nm ,k -1) - zkso(nm ,ku)) +                          &` / `(k-kd) * (zkso(nm ,kd-1) - zkso(nm ,k )) )` | C 문서 누락 | 코드는 수평 확산 flux에 수평 층 경사와 연직 농도 구배의 곱을 더한다. k−1은 위층이다. 변수명 kd/ku만 보고 층 순서를 바꾸지 않는다. |
| inputs-physics-numerics:SI2-284 | SVK z-plane 실제 limiter·flux | — | `src/SwashHDiffZplane1DH.ftn90:285–290`: `! MUSCL limiter` / `if ( grmax < 0. .or. grmin > 0. ) then` / `grad = min( grmin, 0.25 * grsum )` / `if (grad1 < 0.) grad = max( grmax, 0.25 * grsum )` / `endif` / `grad = 2. * grad`; `src/SwashHDiffZplane1DH.ftn90:294`: `flux = dif2d * rdx * rdx * ( point(kf-1) - point(kf) ) * grad`;<br>`src/SwashHDiffZplane2DH.ftn90:315`: `flux = dif2d * ( point(kf-1) - point(kf) ) * grad * guu(nm) / gvu(nm)` | C 문서 누락 | z-plane 확산은 MUSCL 보간을 사용한다. DISCRETIZATION TRANSPORT의 이류 limiter 선택과 다른 내부 선택이다. Van Leer 대안 줄은 일반 주석으로 남아 있다. |
