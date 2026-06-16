---
title: "SWASH 암시적 다층 flow solver — SwashImpLay{1D,2D,M1D,P1D,U}flow 반정수압 projection 구조"
model: SWASH
component: src (implicit layered flow / non-hydrostatic projection)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashImpLay1DHflow.ftn90(Purpose/Method :44-79, 반복루프 :1458·:2829, 수위 tridiag :1467-1597, divergence/Poisson 빌드 :2570-2702, qlay 축소 :2706-2722, Poisson 풀이 :2742-2780, 압력·속도 보정 :2833-2908), SwashImpLayM1DHflow.ftn90(skew-symmetric 주석 :42-84, qm/중심차분 advection :301-321), SwashImpLayP1DHflow.ftn90(subgrid Purpose :84-87, npu/kup use :94, u1p 적분 :1693-1713, dq0 tridiag :2738, coarse→fine 보간 :2752-2816), SwashImpLayUflow.ftn90(triangular Purpose :41-75, perot :295-299·1954·2881, pcgu/newtonU :1683·1784, bicgstab3 :2785), SwashComputFlow.ftn90 dispatch :106-188, SwashCheckPrep.ftn90 iproj/qmax 기본값 :585-655, SwashReadInput.ftn90 PROJ ITER :1566-1574 직접 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/README.md
---

# SWASH 암시적 다층 flow solver — 반정수압 위상해상 projection 구조

> 연직 layer 다수(kmax>1)일 때 반정수압(non-hydrostatic) 층평균 천수방정식을 semi-implicit 시간적분 + 압력-correction projection으로 푸는 `SwashImpLay*` 군. (경로: raw/source_code/swash/src/)

본 노트는 티어 C 배정 5파일을 다룬다. `SwashImpLayP2DHflow`(2D subgrid)는 기존 노트가 다루므로 제외.

## 1. 5개 변종의 정체와 dispatch

`SwashComputFlow.ftn90`이 mode(1D/2D), `kmax`(층 수), `mtimei`(시간적분), `mimetic`/`lsubg`(스킴 옵션) 조합으로 호출 대상을 분기한다 (`SwashComputFlow.ftn90:106-188`). 본 군은 모두 **`mtimei == 2` (semi-implicit approach)** 경로다 (`:117`, `:177`).

| 파일 | 호출 조건 (1D, kmax>1) | 수평 advection 시간적분 | 특징 |
|---|---|---|---|
| `SwashImpLay1DHflow` | `mtimei==2 .and. .not.mimetic .and. .not.lsubg` (`:126`) | MacCormack predictor-corrector | 표준 1D 다층 |
| `SwashImpLayM1DHflow` | `mtimei==2 .and. mimetic` (`:122`) | Crank-Nicolson, 중심차분 | mimetic / skew-symmetric |
| `SwashImpLayP1DHflow` | `mtimei==2 .and. lsubg` (`:124`) | MacCormack | subgrid(연직 이중격자) |
| `SwashImpLay2DHflow` | 2D `mtimei==2 .and. .not.lsubg` (`:182`) | MacCormack | 표준 2D 다층 |
| `SwashImpLayUflow` | unstructured(triangular) mesh | Euler explicit / 고차 | Perot 재구성, 삼각망 |

세 파일(1D, P1D, 2D)의 Purpose/Method 헤더는 사실상 동일한 문장 — verbatim:

> "Performs the time integration for the non-hydrostatic, layer-averaged 1D shallow water equations" (`SwashImpLay1DHflow.ftn90:46`)
> "The non-hydrostatic pressure is obtained by means of the second order accurate pressure correction technique." (`SwashImpLay1DHflow.ftn90:79`; 동일 `SwashImpLay2DHflow.ftn90:77`, `SwashImpLayP1DHflow.ftn90:82`)

## 2. 공통 시간적분 스킴 (theta-scheme + 항별 처리)

`SwashImpLay1DHflow.ftn90:50-57` Method 블록 verbatim:

> "The time integration with respect to the continuity equation and the water level gradient of the u-momentum equation is based on a theta-scheme. Only a value of 0.5 <= theta <= 1 will be taken."
> "The time integration with respect to the horizontal advective term is based on the predictor-corrector scheme of MacCormack, while that for the bottom friction is based on Euler implicit and for the non-hydrostatic pressure gradient a semi-implicit approach is employed (theta-scheme). Both vertical advective and viscosity terms are treated semi-implicit as well. This results in a tri-diagonal system."

항별 처리 정리:

| 항 | 처리 | implicitness factor |
|---|---|---|
| 연속방정식·수위경사 | $\theta$-scheme, $0.5\le\theta\le1$ | `theta = pnums(...)`, `theta3 = pnums(5)` (`:199`) |
| 수평 advection | MacCormack predictor-corrector (1D/2D/P), CN(M), Euler explicit(U) | — |
| 바닥마찰 | Euler implicit | — |
| 비정수압 압력경사 | semi-implicit $\theta$-scheme | `theta3 = pnums(5)` (`:199`) |
| 연직 advection/viscosity (u-mom) | semi-implicit → tri-diagonal | `thetau = pnums(31)` (`:200`) |
| w-momentum 연직항 | semi-implicit | `thetaw = pnums(32)` (`:201`) |

연직항이 semi-implicit이므로 연직으로 tridiagonal 계가 형성된다 — u-momentum 풀이가 `call tridiag` (`SwashImpLay1DHflow.ftn90:1597`)로 귀결.

## 3. 반정수압 압력 위치: Keller-box vs 중앙 차분 (ihydro)

`ihydro` 분기로 비정수압 압력 $q$의 연직 배치가 결정된다.

- **`ihydro == 1`** — Keller-box. 주석 verbatim: "Keller-box scheme, so non-hydrostatic pressure is located at the centers of layer interfaces" (`SwashImpLay1DHflow.ftn90:548`). gradient matrix `gmatu`/`gmatw` 구성 (`:546-737`).
- **`ihydro == 2`** — 압력이 cell center(layer 중앙)에 위치, 별도 gradient 빌드 (`:738-`).

`ihydro==1` & `kpmax<5` & `qlay==0`이면 수치 분산관계 보정(`numdisp=.true.`) 활성 (`SwashCheckPrep.ftn90:591-595`). w-momentum의 z-gradient 압력은 명시적 중심차분 또는 implicit Keller-box로 이산 (`SwashImpLay1DHflow.ftn90:73-77` Method).

## 4. projection: pressure-correction(iproj=1) vs pressure-projection(iproj=2)

핵심 분기 `iproj` (압력 갱신 방식):

```
update the non-hydrostatic pressure
if ( iproj == 1 ) then
   q = q + dq            ! pressure correction (증분)
else if ( iproj == 2 ) then
   q = dq                ! pressure projection (전량 재계산)
```
(`SwashImpLay1DHflow.ftn90:2837-2841`)

기본값 결정: floating object 없으면 `iproj = 1`, 있으면 `iproj = 2` (`SwashCheckPrep.ftn90:630-636`). 사용자가 `NONHYDROSTATIC ... PROJECTION` 키워드 주면 `iproj = 2` 강제 + `ITER` 부키워드로 `lpproj = .true.` (`SwashReadInput.ftn90:1566-1570`).

`lpproj`(non-hydrostatic pressure part를 연속방정식에 포함하는 반복 projection)는 2차 정확도를 위한 outer iteration을 켠다. `lpproj .and. mtimei /= 2`이면 무의미하다며 끈다 (`SwashCheckPrep.ftn90:651-653`). `lpproj` 아니면 `pnums(59)`(maxiter)=1 (`:656`).

## 5. outer iteration loop (2차 정확도 pressure projection)

수위 보정 + 압력 보정을 감싸는 반복문. 진입·종료 조건:

```
maxit = nint(pnums(59))      ! 최대 반복 (PROJ ITER MAXITER, 기본 50)
reps  = pnums(58)            ! 허용오차 (PROJ TOL, 기본 1e-4)
epslin = max(reps, reps*s0mx)
10 if ( resm > epslin .and. jj < maxit ) then    ! ← label 10 진입
   jj = jj + 1
   ... 수위 tridiag, 모멘텀, divergence/Poisson, 보정 ...
   goto 10                                         ← 반복
endif
```
(setup `SwashImpLay1DHflow.ftn90:1446-1454`; 루프 헤드 `:1458`; `goto 10` `:2829`)

주석 verbatim: "start iteration process to obtain 2nd order accuracy in pressure projection method" (`SwashImpLay1DHflow.ftn90:1456`).

## 6. 수위 보정 방정식 (tridiagonal 연속방정식)

outer loop 안에서 수위 correction `ds`를 푼다. theta-scheme 연속방정식이 1D에서 삼중대각계로 환원:

- $\mathrm{fac} = g\,\Delta t^2 / \Delta x^2$ (`:1467`)
- 대각 빌드: `a(nm) = -fac*teta(nmd)*hu(nmd)`, `c(nm) = -fac*teta(nm)*hu(nm)`, `b(nm) = fac1 - teta2(nm)*(a+c)` (`:1494-1512`)
- RHS: 좌우 면의 층적분 질량플럭스 차 $d=\Delta t\,/\Delta x\,(\sum_k hku\cdot u - \dots)$ (`:1519-1526`)
- `lpproj`일 때 비정수압 압력경사 기여 추가: `d(nm) = d(nm) + dt*dt*rdx*theta3*(teta(nm)*fac2 - teta(nmd)*fac1)` (`:1571`)
- 풀이: `call tridiag ( a, b, c, d, ds, kgrpnt )` (`:1597`)
- `inewt /= 0`이면 Newton-type(wet/dry 양positivity 보존) 경로 `call newton1D` (`:1731`)

`inewt` 기본값: structured(`optg /= 5`)면 0, unstructured면 1 (`SwashCheckPrep.ftn90:618-624`), 단 `mtimei /= 2`면 강제 0 (`:626`).

## 7. 비정수압 압력: divergence matrix → Poisson 방정식 → 보정

projection의 심장부 (`SwashImpLay1DHflow.ftn90:2566-2908`).

### (a) divergence matrix `dmat`
각 (m,k)에서 face 두께·$\Delta\sigma$로 6-stencil divergence 연산자 구성 (`:2570-2609`). 표면(k==kmax)·표면압력층(presp==1)에서 경계조정 `fac2=0`/`fac1=0` (`:2591-2592`). 표층(k==1)에서 stencil 절곡 보정 (`:2611-2622`).

### (b) Poisson 방정식 빌드
$A_p = D\,G$ (divergence∘gradient). amatp의 각 대각밴드를 `dmat`와 `gmatu`의 곱으로 명시 조립 (`:2644-2661`). w-momentum의 `gmatw` 기여를 `ihydro==1`(Keller-box, full band) vs else 두 갈래로 추가 (`:2663-2689`). RHS는 예측 속도장의 발산:

```
rhsp(nm,k) = ( dmat·u1(좌우·상하) + kwd*w1(nm,k-1) - kwu*w1(nm,k) ) / (dt*theta3)
```
(`:2691-2694`). rigid body motion(floating) 기여 `+ skc(nm)/(dt*theta3)` (top layer) (`:2698`).

### (c) reduced Poisson (qlay)
표층 일부 layer의 압력을 top face 값에 묶어 미지수 축소: "to reduce the pressure Poisson equation set pressure of bottom face to that of top face for a number of layers" (`:721`, `:2283`). `qmax = kpmax - qlay`개 미지수로 amatp/rhsp를 가중합 축소 (`:2706-2722`). `qmax` 정의: `SwashCheckPrep.ftn90:585`.

### (d) Poisson 풀이 (linear solver 분기)
```
if ( qmax == 1 ) then
   call tridiag ( amatp(:,:,2), amatp(:,:,1), amatp(:,:,3), rhsp, dq, kgrpnt )   ! 1압력층 → 삼중대각
else
   if ( lprecon ) call iluds/iludr/ilu ( amatp )    ! icond=1/2/3 전처리
   call bicgstab ( amatp, rhsp, dq )                ! 일반: BiCGSTAB
endif
```
(`SwashImpLay1DHflow.ftn90:2742-2780`). 전처리 선택 `icond` 기본값: floating 없으면 2(ILUD), 있으면 3(ILU) (`SwashCheckPrep.ftn90:640-646`); 키워드 `ILUDS/ILUD/ILU/NONE` (`SwashReadInput.ftn90:1553-1561`). 풀이 후 subdomain 간 `SWEXCHG(dq)` (`:2784`), 축소층 복원 `dq(:,k)=dq(:,qmax)` (`:2787-2791`).

### (e) 속도·압력 보정 (projection step)
- 압력 갱신: §4 (`:2835-2843`)
- u 보정: `u1 = u1 - dt*theta3*( gmatu · dq )` (6-stencil) (`:2865-2866`)
- w 보정: `ihydro==1`(Keller-box, 누적 stencil) vs else `w1 = w1 - dt*theta3*( gmatw(1)*dq(kd) + gmatw(2)*dq(k+1) )` (`:2876-2908`)
- `lpproj` 시 다음 반복용 압력경사 `dqgrd` 갱신 (`:2797-2827`) → §6의 수위식 RHS로 환류

## 8. 변종별 차이점

### 8.1 M1D — mimetic / skew-symmetric (energy-conservative)
헤더가 보존성을 명시 — verbatim: "strictly mass and momentum conservative at the discrete level, and strictly energy conservative in discrete space ... The discrete advective operator is skew-symmetric" (`SwashImpLayM1DHflow.ftn90:42-46`). theta는 0.5만: "Only a value of theta = 0.5 is taken." (`:53`). 수평 advection을 Crank-Nicolson + 중심차분으로:

```
qm(nm,k) = 0.5 * ( qx(nm,k) + qx(nmd,k) )          ! face→center 질량플럭스 평균
fac1 = 0.5 * rdx * qm(nmu,k) / hkumn(nm,k)         ! 중심차분 skew-symmetric
fac2 = 0.5 * rdx * qm(nm ,k) / hkumn(nm,k)
```
(`:301`, `:320-321`). 점성도 대칭(symmetric)으로 이산 (`:64`). 경계조건은 skew-symmetry 보존 위해 속도만 규정: "only velocity is prescribed at the boundary" (`:84`). MacCormack 예측-수정 부재 → `resm/maxit` 1D advection sub-iteration이 다르고 module use에 `wrk` 추가 (`:91`).

### 8.2 P1D — subgrid (연직 이중격자)
헤더 verbatim: "the horizontal and vertical momentum equations are solved on separate grids in the vertical. The vertical momentum equation and the pressure Poisson equation are solved on a coarse vertical grid, whereas the horizontal momentum equation is solved on a subgrid with a high vertical resolution. Non-hydrostatic pressure on subgrid is obtained by means of linear interpolation." (`SwashImpLayP1DHflow.ftn90:84-87`). `npu`(pressure layer당 velocity layer 수), `kup`(매핑) 사용 (`:94`).

- coarse 압력층 속도 적분: `u1p(nm,kp) = Σ_j hku(nm,k)*u1(nm,k) / hkuc(nm,kp)` (`:1705-1713`)
- coarse grid에서 w-momentum·Poisson 빌드 (`:1745-`, RHS `:2606-2608`은 `u1p` 사용)
- 1압력층(`qmax==1`)이면 압력 보정도 별도 `dq0` tridiag: `call tridiag ( a, b, c, d, dq0, kgrpnt )` (`:2738`)
- coarse→fine 선형보간: `ihydro==1`은 interface 중심 `dqv(nm,k) = dq(nm,kp)*(1-fac) + dq(nm,kp-1)*fac` (`:2782`); `ihydro==2`는 cell center 보간 + 바닥 외삽 (`:2792-2816`)

### 8.3 2D — 표준 2층축 다층
인자 없는 subroutine, `m_genarr`에서 격자 metric(guu,gvv,gsqs,...)·`msta/mend/nsta/nend`(루프 범위) import (`SwashImpLay2DHflow.ftn90:84`). 알고리즘 골격은 1D와 동일(MacCormack + theta + divergence/Poisson + bicgstab `:2776`)하되 두 수평방향(u,v) 모멘텀·gradient를 각각 빌드. 7003줄로 가장 큼.

### 8.4 Uflow — unstructured(triangular) mesh
헤더 verbatim: "Performs the time integration for the non-hydrostatic, layer-averaged shallow water equations on triangular mesh" (`SwashImpLayUflow.ftn90:43`). advection은 Euler explicit + cell→vertex/face의 r-ratio 고차 limiter: "The time integration with respect to the advective term is based on Euler explicit" (`:50`), "The r-ratio formulation based on most upwave vertex is employed." (`:57`).

- **Perot 재구성**: face normal 속도 → cell 중심 벡터. `call perot ( u0, 1, kmax )` (`:299`), `call perot ( u1, 1, kmax )` (`:1954`, `:2881`). 적분속도도 Perot's formula로 (`:1349`).
- **수위 보정 solver**: 비대칭 그래프라 tridiag 불가 → `call pcgu( amat, rhs, ds )` (PCG, `:1683`); Newton-type면 `call newtonU ( amatn, rhsn, ds )` (`:1784`). sum(rhs)>0 사전 검사 (`:1759`).
- **Poisson solver**: `call bicgstab3 ( amatp(1:ncells,1:qmax,0:nconct), rhsp, dq )` (`:2785`) — 셀 단위(`ncells`) 가변 stencil(`0:nconct`) BiCGSTAB.
- `epswom = 0.005` (다른 파일은 0.001, `:91` vs `SwashImpLay1DHflow.ftn90:105`).

## 9. 공통 후처리: 상대 연직속도 wom

projection 완료 후 모든 변종이 layer interface 기준 상대 연직속도 `wom`을 계산 (`SwashImpLay1DHflow.ftn90:3095-`). Method verbatim: "This relative velocity, stored in array wom, is defined as the difference between the vertical velocity along the streamline and the vertical velocity along the interface." (`:66-68`). 표면 wom이 0이어야 함을 `epswom` 허용오차로 점검 (`:3129`); 정수압 흐름이면 층평균 연속식에서 유도 (`:69-70`). 파봉 전면에서는 정수압 가정 → 국부 연속식으로 유도 (`:3173`). 종료부에서 CFL 위반 검사 + `sigmacoor` 격자갱신 (`:3087`, `:3314-3321`).

## 10. 알고리즘 요약 (한 outer-step)

1. u-momentum 빌드 (advection·마찰·점성·압력경사 explicit/semi-implicit) → 연직 tridiag로 예측속도 `u1`
2. (lpproj) outer loop label 10 진입 (`:1458`)
3. 수위 보정 tridiag (`call tridiag`/`pcgu`/`newton1D`) → `ds`, 수위·속도 갱신
4. w-momentum 빌드 → 연직 tridiag로 예측 `w1`
5. divergence matrix `dmat` + Poisson `amatp = D·G` 빌드, RHS = 예측장 발산
6. (qlay) Poisson 축소 → `tridiag`(qmax==1) 또는 `bicgstab`/`bicgstab3`(else)로 `dq`
7. 압력 갱신(`q=q+dq` 또는 `q=dq`) + u·w projection 보정
8. (lpproj) `dqgrd` 갱신 후 `goto 10`; 수렴 시 wom·CFL 후처리

## 11. 미확인 / source-needed

- `tridiag`, `bicgstab`, `bicgstab3`, `pcgu`, `iluds/iludr/ilu`, `perot`, `newton1D/newtonU`, `sigmacoor`의 내부 구현은 본 5파일 밖(별도 솔버 모듈)이라 본 노트 범위 밖 — **source-needed** (호출 시그니처만 인용).
- `gmatu`/`gmatw`/`dmat` band 인덱스(1~6, ishif 등)의 기하학적 의미 상세는 gradient-matrix 빌드부(`:546-862`) 추가 정독 필요 — 본 노트는 호출·조립 구조만 확인.
- 2D 파일의 v-방향 모멘텀 세부(7003줄)는 1D 대칭 추론에 의존; v-specific file:line 미인용 부분은 **source-needed**.
