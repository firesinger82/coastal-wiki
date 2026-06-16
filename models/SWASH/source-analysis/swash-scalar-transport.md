---
title: "SWASH scalar transport — 염분·온도·sediment 이류-확산 transport (ComputTrans dispatch + Exp*trans 커널)"
model: SWASH
component: src (scalar transport / constituents)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashComputTrans.ftn90 / SwashCompUTrans.ftn90 dispatch, SwashExpDep1DHtrans.ftn90 전문(:1-535), SwashExpDep2DHtrans/DepUtrans/Lay1DHtrans/Lay2DHtrans/LayUtrans Purpose·Method 블록 및 핵심 스킴부, SwashInitBCtrans.ftn90·SwashInitBCUtrans.ftn90 전문, SwashServices.ftn90 fluxlim(:307-452) file:line 인용"
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

constituent별 난류 Prandtl/Schmidt 수 `psm`: 염분·온도 = 0.7, 부유사 = 1.0 (`SwashExpDep1DHtrans.ftn90:157-161`). 수평 eddy 확산계수는 이 `psm`으로 나눠 적용.

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

sigma 좌표 인공 확산(creep) 억제: `if ( icreep == 1 ) call SwashAntiCreep1DH(amatc,rhsc,rpo,kgrpnt,psm)` (`SwashExpLay1DHtrans.ftn90:677`). 2D 대응 `SwashAntiCreep2DH` (`SwashExpLay2DHtrans.ftn90:951`). ⚠ AntiCreep 서브루틴 본체는 본 배정 외 파일이라 미확인.

### 5.4 sediment 침식/퇴적 (bed 경계 mass exchange)

부유사(`l==lsed`)일 때 bed 셀(k=kmax)에 erosion/deposition flux 추가 (`SwashExpLay1DHtrans.ftn90:421-484`). 파라미터는 `psed()` 배열(의미는 SwashCommdata3 모듈, 주석 `:428`):

- **noncohesive sand**(`psed(9)>0`): bed 마찰속도 `fac = (0.3+psed(7))*rtur(nm,kmax,1)`(난류운동에너지 기반, 파괴 난류 포함 가능). erosion = pickup function `rhsc += psed(9)*((fac-psed(5))/psed(5))**1.5` (임계 `psed(5)` 초과 시), deposition = fall velocity `amatc(nm,kmax,1) += psed(1)` (`:439-447`).
- **cohesive mud**(`psed(10)>0`): bed 전단응력 `fac = 0.3*rhow*rtur(nm,kmax,1)`. erosion `rhsc += psed(12)*(fac/psed(10)-1.)` (`fac>psed(10)`), deposition `amatc += psed(1)*(1.-fac/psed(11))` (`fac<psed(11)`) (`:468-476`).

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
| `psed()` | sediment 파라미터(settling/임계전단/pickup) | `SwashExpLay1DHtrans.ftn90:425-476` |

## 8. 출처 미확인 / 후속

- `SwashAntiCreep1DH/2DH` 본체: 호출만 확인(`SwashExpLay1DHtrans.ftn90:677`, `SwashExpLay2DHtrans.ftn90:951`), 알고리즘 내부는 배정 외 파일 — source-needed.
- `psed()` 각 인덱스의 정확한 물리적 의미: 주석이 SwashCommdata3 모듈 참조(`SwashExpLay1DHtrans.ftn90:428`)로 위임 — 본 노트는 코드 사용 맥락에서 `psed(1)`=settling, `psed(5)`/`psed(10)`/`psed(11)`=임계전단, `psed(9)`/`psed(12)`=pickup 계수로 **추정**(⚠ 모듈 정의 직접 미확인).
- `SwashExpLay2DHtrans`(1256줄)·`SwashExpLayUtrans`(1138줄) 전문은 1DH/U 구현의 차원 확장이며 Purpose·Method·AntiCreep 호출만 확인, 라인별 전사 생략(proportional).
