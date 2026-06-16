---
title: "Delft3D D-Flow FM scalar transport + sediment/morphology — explicit FV advection·MUSCL limiter·implicit vertical·bed update divergence"
model: Delft3D
component: dflowfm/compute_transport+compute_sediment
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/). compute_transport: update_constituents.f90(드라이버·서브스텝), comp_fluxhor3d.f90(수평 advection+diffusion FV flux·MUSCL stencil), comp_fluxver.f90(수직 explicit flux), dlimiter.f90(MC limiter), solve_vertical.f90(tridag implicit), solve_2d.f90, make_rhs.f90, get_dtmax.f90(transport CFL), ini_transport.f90(constituent admin·thetavert). compute_sediment: m_fm_bott3d.f90(bed update divergence), fm_upwbed.f90(bedload→link upwind), fm_red_soursin.f90(soursin reduction), fm_erosed.f90(Partheniades-Krone source/sink header), fill_constituents.f90(soursin→const_sour/sink 결선), netnode_based/getequilibriumtransportrates.f90·ucrouse.f90(legacy netnode 평형수송) file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
  - models/Delft3D/source-analysis/delft3d_sediment_morphology.md
  - models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md
  - models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md
---

# Delft3D D-Flow FM scalar transport + sediment/morphology

> 경로: `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/{compute_transport, compute_sediment}/`
> 비구조 격자(unstructured FV)에서 모든 scalar(염분·수온·sediment·tracer·secondary flow)를 하나의 `constituents(NUMCONST, Ndkx)` 배열로 통합 수송. 수평 advection/diffusion 은 **explicit FV flux + MUSCL limiter**, 수직은 **implicit tridiagonal**. Sediment/morphology 는 별도 div-of-bedload 로 bed level 갱신.

기존 노트와의 경계: [[delft3d_sediment_morphology]]·[[delft3d_sediment_transport_formulae]] 는 **수송 공식(Van Rijn·Engelund-Hansen 등)** 중심. 본 노트는 **FM transport solver·advection 스킴·bed-update 이산화** 집중. 시그마/z 레이어는 [[delft3d_sigma_z]], 난류 확산계수는 [[delft3d_turbulence]] 참조.

---

## 1. 통합 수송 드라이버 `update_constituents`

`compute_transport/update_constituents.f90`. 모듈 헤더 주석(verbatim):

> `!> This subroutine transports an array of scalars.`
> `!> updates sedl with`
> `!>     d(h sedl)/dt = -div (q1 sedl) + div (diag(NU) grad sedl) + h ( -sink sedl + source )`
> `!>   solves for each column {k | 1<=k<k=top} an equation of the form`
> `!>     aaj(k) sedj(k-1) + bbj(k) sedj(k) + ccj(k) sedj(k+1) = ddj(k)`
> (`update_constituents.f90:63-70`)

지배방정식 (셀 k, constituent j):
$$\frac{d(h\,c_j)}{dt} = -\nabla\!\cdot(q\,c_j) + \nabla\!\cdot(\nu\,\nabla c_j) + h(-\text{sink}\cdot c_j + \text{source})$$

핵심 호출 순서 (한 flow timestep 내):
1. `fill_constituents(1)` — 모든 scalar 를 통합 배열·source/sink 채움 (`update_constituents.f90:149`).
2. `comp_dxiAu()` — 수평 확산 flux 면적/Dx 사전계산 (`:153`).
3. `get_dtmax()` + `get_ndeltasteps()` — transport CFL 기반 최대 timestep·local substep 수 결정 (`:156-158`).
4. `dts = dts / nsubsteps` — flow dt 를 가장 작은 substep 으로 분할 (`:164`).
5. **substep 루프** `do istep = 0, nsubsteps-1` (`:188`):
   - `comp_fluxhor3D(...)` — 수평 advection+diffusion flux (`:200`).
   - `comp_sumhorflux(...)` — flowlink flux 를 cell 합산 (`:227`).
   - 2D: `solve_2D(...)` / 3D: `comp_fluxver(...)` + `solve_vertical(...)` (`:243-253`).
6. `extract_constituents()` — 통합 배열을 개별 scalar(sa1, tem1, sed, …)로 복원 (`:298`).

limiter type 는 `limtyp = max(limtypsa, limtyptm, limtypsed)` — 염분·수온·sediment 중 최댓값 사용 (`:141`).

### Local time-stepping (substepping)
`nsubsteps>1` 이면 셀별로 다른 substep 빈도 사용. `jaupdatehorflux`/`jaupdate` 로 갱신할 link·cell 선택 (`update_constituents.f90:194-241`). MPI 동기화는 first-order 면 `numlay_cellbased-1`, higher-order 면 `numlay_cellbased/2` substep 마다 (`:168-172`).

---

## 2. 수평 flux: explicit FV advection + MUSCL — `comp_fluxhor3D`

`compute_transport/comp_fluxhor3d.f90`. 모듈 헤더: `!> compute horizontal transport fluxes at flowlink` (`comp_fluxhor3d.f90:33`).

### 2.1 Advection (upwind + slope reconstruction)
flowlink L 의 좌/우 cell `k1=ln(1,L)`, `k2=ln(2,L)` (`:203-204`). Courant 수:
$$cf = \Delta t\,|u_1(L)|\,/\,\Delta x_L \quad(\texttt{dxi})$$
(`comp_fluxhor3d.f90:208`). discharge 를 부호 분리: `QL = max(q1(L),0)`, `QR = min(q1(L),0)` (`:249-250`).

기본 스킴 (limtyp 1~4): 좌측 면값 재구성
```
sedL = sed(j,k1) + acl(LL)*max(0, 1-cf)*dlimiter(ds1L,ds2L,limtyp)*ds2L   (q1(L)>0)
sedR = sed(j,k2) + (1-acl(LL))*max(0, 1-cf)*dlimiter(ds1R,ds2R,limtyp)*ds2R (q1(L)<0)
flux(j,L) = QL*sedL + QR*sedR
```
(`comp_fluxhor3d.f90:288-302`). `ds2L=sed(k2)-sed(k1)`(다운스트림 기울기), `ds1L=(sed(k1)-sedkuL)*sl3L`(업스트림 기울기, `sedkuL` 은 stencil 보간) (`:289-291`). `max(0,1-cf)` 는 Courant 가 클수록 high-order 비중을 줄이는 안정화 항.

upstream stencil 은 `klnup`/`slnup` (cell-link upwind admin) 으로 좌/우 각 2-cell 보간 (`:167-182`). 3D 에서는 layer 정렬 `laydif=L-Lb` + `kmxn`/`kmxL` 로 동일 레이어를 추적 (`:216-235`).

### 2.2 limtyp 변형
- **limtyp 7**: 순수 central `flux = q1*0.5*(sedR+sedL)` ("central only for cursusdemo") (`:260-261`).
- **limtyp 6**: cell-gradient 기반 중앙형(MUSCL central) — 먼저 `dsedx,dsedy` 를 link 차분에서 cell 로 reconstruct(`:124-140`), 면값을 `sed(ku) + half*max(0,1-cf)*dlimitercentral(...)` (`:262-267`).
- **limtyp 9**: 비등간격 격자용 MC — `dlimiter_nonequi` (`:268-285`).

### 2.3 Diffusion
`dicouv>=0 .and. jalimitdiff/=3` 일 때 두 번째 link 루프 (`comp_fluxhor3d.f90:314-410`). 확산계수:
$$\text{difcoeff} = \text{sigdifi}(j)\cdot\nu_{viu}(L) + \text{difsed}(j) + f_{bg}\cdot\text{diuspL}$$
(`:366`) — Smagorinsky 수평점성(`viu`)·분자확산(`difsed`)·사용자 배경확산(`diusp`/`dicouv`). `sigdifi` 는 1/Prandtl(열)·1/Schmidt(질량) (`:80`). flux:
$$\text{flux}(j,L) \mathrel{-}= \text{difcoeff}\cdot \text{dxiAu}(L)\cdot(\text{sed}(j,k2)-\text{sed}(j,k1))$$
(`:381`). `jalimitdiff==1` 이면 monotonicity 판정으로 flux 를 `dfac*(vol/dt - sqi)` 로 제한 ("zie Borsboom sobek note", `:330-377`). `jacreep==1`(anti-creep, sigma) 면 염분·수온은 수평 gradient `dsalL`/`dtemL` 사용 (`:383-396`).

---

## 3. 수평 limiter `dlimiter` (Monotonized Central)

`compute_transport/dlimiter.f90:37-66`. 헤더 `!> limiter function`.

- `limtyp==0` → 0 반환 = **first-order upwind** (`:49-51`).
- `d1*d2 < dtol` (반대부호) → 0 (`:52-54`).
- 비율 `r=d1/d2` 에 대해 **Monotonized Central (MC)**:
$$\psi(r) = \max\!\big(0,\ \min(2r,\ 2,\ \tfrac{1}{2}(1+r))\big)$$
(`dlimiter.f90:63`). Van Leer 분기는 주석처리됨(`:58-62`).

수직용 변형 `dlimitercentral`, 비등간격 `dlimiter_nonequi`, MC 대안 `dlimitercentral.f90`/`dlimiter_nonequi.f90` 존재(역할: 위 §2.2 참조, ⚠ 본문 미상세).

---

## 4. 수직 flux + implicit 풀이

### 4.1 수직 explicit flux `comp_fluxver`
`compute_transport/comp_fluxver.f90`. 헤더 `!> compute vertical fluxes` (`:33`). `thetavert(j)==1` 이면 전부 implicit 처리(여기서는 skip, `:157-159`). layer 두께 `dz` 를 셀 중심 간 간격으로 구성 (`:119-123`).

vertical discharge `qw_loc = qw(k)` 에 **fall velocity** 보정(explicit 모드):
- `jased<4`: `qw_loc = qw(k) - wsf(j)*ba(kk)` (`:137`).
- stm sediment(`jased=4`, `ISED1<=j<=ISEDN`): `kmxsed` 아래에선 settling 0, 위에선 `qw(k) - mtd%ws(k,ll)*ba(kk)` (`:140-143`).

scheme: `thetavert(j)>0` 면 central `qw_loc*0.5*(sedL+sedR)` (`:165`), 완전 explicit 면 MUSCL 재구성 후 upwind (`:168-187`). Courant 억제 `cf = cffacver*dt*|qw|/(ba*dz)` → `max(0,1-cf)` (`:150-152`).

### 4.2 implicit 수직 solve `solve_vertical`
`compute_transport/solve_vertical.f90`. 헤더 `!> solve equations implicitly in vertical direction` (`:33`). `m_tridag` 의 Thomas 알고리즘 사용 (`:35, :244`).

칼럼별 삼중대각계 `a·c(k-1) + b·c(k) + c·c(k+1) = d`:
- 대각에 선형화 sink: `b(n,j) = 1 + dt*sink(j,k)` (`:143`).
- RHS `d` 는 `make_rhs` 결과 (`:148-152`).
- **수직 확산** flux factor (sediment): `(ozmid + seddif/tpsnumber + difsedw)*dtbazi`, 기타 scalar: `(sigdifi*vicwws + difsedw + ozmid)*dtbazi` (`:178-184`). `ozmid` 는 Ozmidov 혼합길이 보정(`xlozmidov`, 안정성층에서 Brunt-Väisälä `bruns`로) (`:167-173`).
- **수직 advection** semi-implicit central(`thetavert>0`): `fluxfac = qw_loc*0.5*thetavert*dt` 를 대각/부대각에 분배 (`:194-211`).
- **implicit fall velocity**(`jaimplicitfallvelocity==1`): settling 을 부호 따라 upwind 으로 대각에 추가 (`:213-232`).

`get_difsedw` (pure fn) = 사용자 배경확산 `dicoww` + constituent별 분자확산 `molecular_diffusion_coeff` (`:256-266`).

### 4.3 2D 풀이 `solve_2D`
수직 없으므로 단순 sink 나눗셈:
$$\text{sed}(j,k) = \text{rhs}(j,k)\,/\,(1 + \Delta t\cdot\text{sink}(j,k))$$
(`solve_2d.f90:101`). `thetavert=0` 으로 `make_rhs` 호출 (`:80-84`).

### 4.4 RHS 구성 `make_rhs`
3D:
$$\text{rhs}(j,k) = \Big[\big(\tfrac{\text{sumhorflux}}{\text{ndeltasteps}} - (1-\theta_v)(\text{fluxver}_k - \text{fluxver}_{k-1})\big)\tfrac{1}{V} + \text{source}\Big]\Delta t + \text{sed}(j,k)$$
(`make_rhs.f90:111`). `sumhorflux` 를 사용 후 0 리셋 (`:112`). 2D 는 vertical 항 제거 (`:133, :156`).

---

## 5. Transport CFL / 최대 timestep — `get_dtmax`

`compute_transport/get_dtmax.f90`. 헤더 `!> get maximum timestep for water columns (see setdtorg)` (`:30`).

2D (`kmx==0`): `dtmax(k) = cflmx*vol1(k)/squ(k)` (outward flux 기준) (`:118-120`). 확산 포함 옵션이면 분모에 `sqi+sumdifflim` (`:123`).
3D: layer별 `vol1(k)/max(squ(k),sqi(k))` 의 최소에 `cflmx` 곱 (`:159-182`). stm sediment + explicit fall velocity 면 settling flux `maxval(mtd%ws)*ba` 까지 분모에 포함 (`:150-156, :166-173`).

`jalimitdtdiff==1`(=`jatransportautotimestepdiff==1`) 이면 확산이 timestep 을 제약, `sumdifflim` 사전계산 (`:80-111`). MPI 면 `reduce_double_min` 으로 전역 최소 (`:203-214`). `jatransportautotimestepdiff` 분기는 `ini_transport.f90:111-131`.

---

## 6. Constituent 관리·thetavert — `ini_transport`

`compute_transport/ini_transport.f90`. constituent 인덱스 할당 순서(누적): salt(`ISALT`) → temperature(`ITEMP`) → sediment(`ISED1..ISEDN`, mxgr fraction) → secondary flow(`ISPIR`) → tracers(`ITRA1..ITRAN`) (`:79-109`).

수직 advection 의 `thetavert` (0=explicit, 1=central implicit):
- salt: `javasal==6` → 0(explicit), else `tetav` (`:148-151`).
- temp: `javatem==6` → 0, else `tetav` (`:157-160`).
- sediment: `javased==6` → 0, else `tetav` (`:166-169`).

source/sink 채움은 `fill_constituents.f90` — heat source(`:188-194`), salt/temp nudging(`:202-208`), secondary flow relaxation `S=(I_eq-I)/Ta`(`:237-239`), lateral load(`:165`).

---

## 7. Sediment source/sink ↔ transport 결선

stm sediment 의 entrainment/deposition 은 `fm_erosed` 가 `sedtra%sourse`/`sinkse` 에 채우고, `fill_constituents.f90:251-252` 에서 transport 의 `const_sour`/`const_sink` 로 합산:
```
const_sour(iconst, kkk) += sedtra%sourse(kk, jsed)
const_sink(iconst, kkk) += sedtra%sinkse(kk, jsed)
```
(`fill_constituents.f90:246-256`). fluff layer 면 `sourf`/`sinkf` 도 추가 (`:255-256`). 즉 sediment 부유사는 다른 scalar 와 **동일한 transport solver** 를 타고, bed exchange 만 source/sink 로 들어간다.

`fm_erosed` 헤더(verbatim):
> `!!    Function: Computes sediment fluxes at the bed using`
> `!!              the Partheniades-Krone formulations.`
> `!!              Arrays SOURSE and SINKSE are filled and added to arrays SOUR and SINK`
> `!!              Computes bed load transport for sand sediment`
> (`fm_erosed.f90:53-58`)
공식 자체(Van Rijn reference height `:830`, Soulsby skin friction `:777`, Rouse profile)는 [[delft3d_sediment_transport_formulae]] 참조.

---

## 8. Bed-load → flowlink upwind — `fm_upwbed`

`compute_sediment/fm_upwbed.f90`. cell 기반 bedload 벡터 `(sx,sy)` 를 flowlink normal 성분 `e_sn` 으로 투영. `upwindbedload = stmpar%morpar%mornum%upwindbedload` (`:69`).

면-법선 총수송 `sutot1,sutot2 = csu*sxtot + snu*sytot` (`:130-131`). upwind 분기 (둘 다 양/음/혼합):
```
sutot1>0 .and. sutot2>0:  e_sn(Lf,l) = csu*sx(k1) + snu*sy(k1)   (k1 upwind)
sutot1<0 .and. sutot2<0:  e_sn(Lf,l) = csu*sx(k2) + snu*sy(k2)   (k2 upwind)
else:                      acl-weighted central
```
(`fm_upwbed.f90:133-146`). central(`upwindbedload=.false.`)이면 항상 acl 가중평균 (`:142-145`). `pure1d_mor` 1D link 는 x-성분 전체벡터 사용 (`:101-127`). 마른 link·비활성 sediment cell 은 0 (`:95-98, :149-153`). 경계처리 `jabndtreatment` 분기 (`:75-79, :157-`).

---

## 9. Bed level 갱신 divergence — `m_fm_bott3d`

`compute_sediment/m_fm_bott3d.f90`. 모듈 헤더 `!> Module with subroutines for bed level update.` (`:33`). drv `fm_bott3d` (`:63`).

### 9.1 호출 흐름 (`fm_bott3d`)
- `dtmor = dts * morfac` — morphological acceleration (`:142`).
- `fm_suspended_sand_correction()` + `fm_total_face_normal_suspended_transport()` (`:148-150`).
- bedload slope/availability 보정: `fm_adjust_bedload(e_sbcn,e_sbct, AVALANCHE_ON, SLOPECOR_ON)` (current), wave-related `e_sbwn`·`e_sswn` (`:166-184`).
- `apply_nodal_point_relation()` (1D 분기점 분배, `:171`), `duneaval()` (`:187-193`).
- 시간 도달 시(`time1 >= tstart_user + tcmp*tfac`): `fm_bed_boundary_conditions` → `fm_change_in_sediment_thickness(dtmor)` → fluff → `fm_dry_bed_erosion` → mormerge (`:206-221`).

### 9.2 수송 divergence → dbodsd (`fm_change_in_sediment_thickness`)
node nm·fraction l 별로 link 합산하여 발산 계산 (`:1014-1170`):
- suspended (neglectentrainment): 수평 부유사 flux `fluxhortot(j,iL)` 합산 → `trndiv += sumflux*bai_mor(nm)` (`:1037-1061`).
- entrainment/deposition 포함: `eroflx = sourse(nm,l)*thick1` (mass conservation, "different from D3D") + 부유사 보정벡터 `e_scrn*wu` (`:1110-1121`).
- bedload: `flux = e_sbn(Lf,l)*wu_mor(Lf)` 합산 → `trndiv += sumflux*bai_mor(nm)` (`:1124-1133`).
- avalanche flux `avalflux` 별도 (`:1135-1144`).
- 최종 변화량:
$$\Delta s_{nm} = (\text{trndiv} + \text{sedflx} - \text{eroflx})\cdot\Delta t_{mor}$$
(`m_fm_bott3d.f90:1146`), `dbodsd(l,nm) += dsdnm` (`:1169`). `link 방향부호`는 helper `fm_sumflux(LL,sumflux,flux)` 가 처리 (`:2017`).

bed change 가 수심의 `dhmax=0.05`(5%) 초과 시 경고(변화 자체는 미제한) (`:1151-1165`).

`dbodsd` 는 이후 `bedcomposition_module` 로 넘어가 layer bookkeeping → `blchg`(bed level change) → `fm_update_bed_level`/`fm_update_bl` (`:1816, :1960`). bed composition 의 layer 알고리즘 자체는 [[delft3d_sediment_morphology]] 참조.

---

## 10. Source/sink 감쇠 — `fm_red_soursin`

`compute_sediment/fm_red_soursin.f90`. 헤더(verbatim):
> `!    Function: Reduces sourse and sink terms to avoid large bed level changes`
> (`fm_red_soursin.f90:46-48`)

mud·bedload 제외(`TRA_COMBINE` 만), 예상 bed change `dz` 가 `h1*dzmax` 초과 시 `reducfac = h1*dzmax/|dz|` 로 sourse·sour_im·sinkse 동시 축소 (`:81-121`). 침식조건(`(sinkse+sour_im)*c < sourse`)이면 `fixfac`(availability) 곱 (`:133-138`). 2D/3D 분기 (3D `kmxsed` layer 두께 `:98-99`, 2D 수심 `:143-146`).

morphological timestep 제약은 `fm_mor_maxtimestep.f90`(`m_fm_mor_maxtimestep`, `:1-8`) 별도(⚠ 본문 미상세, source-needed).

---

## 11. Legacy netnode-based 평형수송 (non-stm)

`compute_sediment/netnode_based/`. **stm 미사용(`jased/=4`)** 시 net node(격자 절점) 기반 평형수송. 진입부:
> `if (stm_included) then; return; end if` (`getequilibriumtransportrates.f90:66-68`)

→ stm 활성 시 이 경로는 작동 안 함. `getequilibriumtransportrates(kk, seq, wse, mx, hsk)` 가 flowcell/ban 별 평형농도 `seq`·유효침강속도 `wse` 반환 (`:40-55`). `jaceneqtr` 로 cell-centered vs net-node 수심 선택 (`:73-117`), `jabanhydrad` 면 hydraulic radius `widarhyr` (`:96-113`).

Rouse 농도 profile (`ucrouse.f90:43-49`, verbatim 식):
$$u_{rouse}(z) = \ln(z/z_0)\cdot\Big(\frac{a}{h-a}\cdot\frac{h-z}{z}\Big)^{rs}$$
($a$=reference height, $rs$=Rouse number). Einstein-Garcia 적분 check 는 `einstein_garcia.f90`·`check_einstein_garcia.f90`, grain size 설정 `setgrainsizes.f90`, 평형 sediment 경계 `setequilibriumsedimentbnds.f90` (역할만, ⚠ 본문 미상세).

---

## 12. 부수 루틴 (역할 요약, 미상세 = source-needed)

| 파일 | 역할 |
|---|---|
| `compute_transport/comp_dxiau.f90` | 수평 확산 flux 면적/Dx 사전계산 |
| `compute_transport/comp_sumhorflux.f90` | link flux → cell 합산 |
| `compute_transport/comp_sinktot.f90` | sediment sink 누적(mass balance) |
| `compute_transport/comp_horfluxtot.f90` | 부유사 총 수평 flux `fluxhortot` |
| `compute_transport/get_jaupdate*.f90` | local timestepping 갱신 마스크 |
| `compute_transport/get_ndeltasteps.f90` | 셀별 substep 수 |
| `compute_transport/diffusionimplicit2d.f90` | 2D implicit 확산(`jalimitdiff==3`) |
| `compute_transport/decaytracers.f90` | tracer 1차 감쇠 |
| `compute_transport/doforester.f90` | Forester 수직 필터(over/undershoot 제거) |
| `compute_transport/{add,droptracer}.f90`·`apply_tracer_bc.f90` | tracer 추가·투하·경계 |
| `compute_sediment/fm_fallve.f90` | 침강속도 계산(모듈 `m_fm_fallve`, `:33`) |
| `compute_sediment/fm_flocculate.f90` | mud 응집 |
| `compute_sediment/fm_adjust_bedload.f90` | bed-slope·avalanche 보정(`compute_ftheta` `:251`) |
| `compute_sediment/fm_bedform.f90` | dune/bedform 예측 |
| `compute_sediment/setucxucy_mor.f90`·`setucxqucyq_mor.f90` | morphology용 cell 유속 재구성 |
| `compute_sediment/m_fm_morstatistics.f90` | morphology 통계(평균 수송 등) |
| `compute_sediment/m_fm_update_crosssections.f90` | 1D 단면 갱신 |
| `compute_sediment/bermslopenudging.f90`·`duneaval.f90` | berm slope·dune avalanche flux |

---

## 핵심 요약

1. **단일 통합 배열** `constituents(NUMCONST,Ndkx)` 로 salt·temp·sediment·tracer·secondary-flow 를 한 번에 수송 — 동일 advection/diffusion/solve 코드 재사용 (`update_constituents.f90:63-70`, `ini_transport.f90:79-109`).
2. **수평 = explicit FV + MUSCL limiter** (`comp_fluxhor3D` `:288-302`, MC limiter `dlimiter.f90:63`), Courant 억제 `max(0,1-cf)`.
3. **수직 = implicit tridiagonal** (`solve_vertical.f90`, Thomas `:244`), advection 은 `thetavert` 로 explicit↔central-implicit 전환.
4. **Transport 전용 CFL** `cflmx*vol/squ` + sediment settling flux 포함, local substepping 으로 안정화 (`get_dtmax.f90`).
5. **Sediment bed exchange 는 source/sink 로만 transport 에 결합** (`fill_constituents.f90:251-252`); bed level 은 별도 transport-divergence (`fm_change_in_sediment_thickness` `:1146`) + bedload upwind (`fm_upwbed.f90`) 으로 갱신, `morfac` 가속.
