---
title: "SFINCS SnapWave 연안 파솔버 — 정상상태 wave/action 전파 + IG·wind·radiation stress 결합"
model: SFINCS
component: snapwave (coastal phase-averaged wave solver, coupled)
canonical_source: self
citation_status: verified
verification_method: "직접 Read — sfincs_snapwave.f90 (전 739줄), snapwave/snapwave_solver.f90 (2005줄), snapwave_domain.f90 (2097줄), snapwave_boundaries.f90 (972줄), snapwave_infragravity.f90 (699줄), snapwave_windsource.f90 (232줄), snapwave_RFtable.f90 (3990줄). 인용 라인 모두 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
---

# SFINCS SnapWave 연안 파솔버

SnapWave는 Deltares가 SFINCS와 한 바이너리로 통합한 **정상상태(stationary) 방향분해(directional) 파에너지 평형** 솔버다. 비정상 분광모델(SWAN 등)과 달리 시간미분을 가성(pseudo) under-relaxation 으로만 쓰고 sweep 반복으로 정상해를 찾는 reduced-complexity 모델이다. 입사파(incident)와 인프라그래비티(IG) 파를 동시에 풀고, 파 라디에이션 응력으로 SFINCS 흐름에 setup/wave force 를 되돌려준다. 결합·매핑은 `sfincs_snapwave.f90`, 물리 솔버는 `snapwave/` 서브모듈 군.

본체 시간루프와의 위치는 [[sfincs-architecture-source-map]] §3 (파/처오름 행) 참조.

## 1. 자료구조 & 결합 진입점 (`sfincs_snapwave.f90`)

모듈은 SnapWave 격자(`snapwave_no_nodes` 노드)와 SFINCS 격자(`np` 점) 사이 양방향 인덱스를 들고, 노드별 파라미터 배열을 보유한다 (`sfincs_snapwave.f90:8-40`). 대표 배열: `snapwave_H`(입사 Hrms), `snapwave_H_ig`(IG), `snapwave_Tp`/`snapwave_Tp_ig`, `snapwave_Fx`/`snapwave_Fy`(파 force), `snapwave_Dw`/`snapwave_Df`(breaking/friction 소산), `snapwave_srcig`/`snapwave_alphaig`/`snapwave_beta`(IG source 진단).

### 결합 초기화 `couple_snapwave` (`:44`)
순서: `read_snapwave_input`(inp 읽기) → `initialize_snapwave_domain`(메쉬·upwind) → `read_boundary_data` → 배열 할당 → `find_matching_cells`. spherical/cartesian 은 SFINCS `crsgeo` 로 `sferic` 결정 (`:97-101`).

### 격자 매핑 `find_matching_cells` (`:173`)
quadtree 인덱스를 매개로 SnapWave↔SFINCS 노드를 연결한다 (`index_sfincs_in_snapwave`, `index_snapwave_in_sfincs`). SFINCS 가 비활성인 SnapWave 노드는, `snapwave_use_nearest` 시 1000km 이내 최근접 SFINCS 점을 OpenMP 거리탐색으로 찾고(`:231-252`), 아니면 수위 0 처리.

### 매 타임스텝 갱신 `update_wave_field(t, tloop)` (`:289`)
1. SnapWave 수심을 SFINCS 수위에서 산정: `snapwave_depth = max(zs(ip) - snapwave_z, 1e-5)` (wavemaker 면 `zsm`) (`:354-368`).
2. 바람 입력 시 SFINCS `windu/windv` → 크기·방향 변환, **nautical-coming-from(deg) → cartesian-going-to(rad)** (`:390-398`).
3. `compute_snapwave(t)` 호출 (실제 솔버).
4. 결과를 SFINCS 배열로 역매핑 (`:417-485`): `hm0`, `hm0_ig`, `sw_tp`, force 등.
5. **Hrms→Hm0 변환**: `hm0 = hm0 * sqrt(2.0)` (`:487-488`).
6. 파 force 를 UV 점으로 보간·회전, `rhow` 로 나눠 가속도화: U점 `fwuv = waveforces_ratio*(... cosrot*fwx + sinrot*fwy ...)/rhow` (`:502`), V점은 회전 부호 반전 (`:508`). `waveforces_ratio` 기본 1.0, wavemaker_hinc 시 incident setup 이중계산 방지용 0 설정 가능 (`:503` 주석).

### `compute_snapwave(t)` (`:525`)
SnapWave 작업배열에 depth/zb/u10 복사 → `update_boundary_conditions(t)` → `compute_wave_field()` → 결과를 모듈 배열로 복사. 핵심 단위변환:
- 평균방향: `snapwave_mean_direction = modulo(270 - thetam*180/pi + 360, 360)` (cartesian rad → nautical deg) (`:551`).
- **파 force 단위변환**: `snapwave_Fx = Fx * rho * depth` (솔버 `F`=Dw·k/σ/ρ/h 를 SFINCS 기대 단위로 환산) (`:563-564`).
- force limiter: `snapwave_fwmaxfac = 0.25*sqrt(g)*rho*gammax**2/tpmean_bwv` (`:567`).
- H≤0 셀은 Tp·방향·cg 를 0 으로 청소(초기 Tpini 잔존 방지) (`:573-584`).

### 입력 파라미터 `read_snapwave_input` (`:602`)
`sfincs.inp` 에서 `snapwave_*` 키를 읽는다. 주요 기본값 (모두 `read_*_input` 호출 라인):
`snapwave_gamma`=0.7, `snapwave_gammax`=999, `snapwave_alpha`=1.0, `snapwave_fw`=0.01, `snapwave_fwig`=0.015, `snapwave_niter`=10, `snapwave_dtheta`=10°, `snapwave_sector`=180°, `snapwave_baldock_ratio`=0.2, `snapwave_baldock_exponent`=2, `relax_factor_DoverA/DoverE`=0.25 (`:615-641`). IG: `snapwave_igwaves`=1, `snapwave_gammaig`=0.7, `snapwave_gamma_fac_br`=0.45, `snapwave_shinc2ig`=1.0, `snapwave_ig_opt`=1, `snapwave_iterative_srcig`=0 (`:644-652`). IG bc: `snapwave_use_herbers`=1, `snapwave_tpig_opt`=1(Tm01), `snapwave_jonswapgamma`=3.3 (`:655-657`). 플래그 후처리: `igwaves`/`igherbers`/`iterative_srcig`/`wind`/`vegetation` 설정 (`:688-724`), `nr_sweeps` 는 1 또는 4 만 허용(아니면 4) (`:726-731`), `coupled_to_sfincs=.true.` (`:734`).

## 2. 핵심 솔버 (`snapwave/snapwave_solver.f90`)

### `compute_wave_field()` (`:9`)
celerity·refraction 사전계산 후 `solve_energy_balance2Dstat` 호출. 분산관계는 근사식:
$$ k = \frac{\sigma^2}{g}\,(1 - e^{-(\sigma\sqrt{h/g})^{2.5}})^{-0.4},\quad C=\sigma/k,\quad n=0.5+\frac{kh}{\sinh(2kh)},\quad C_g=nC $$
(`solver:74-78`). IG 파수 `kwav_ig` 는 동일 형태로 `sigm_ig` 사용, `cg_ig = Cg` 동기화 (`:80-90`). Hmax: 입사파는 `Hmx = gamma*depth`(`:100`), IG 는 `Hmx_ig = 0.88/k_ig*tanh(gamma_ig*k_ig*h/0.88)` (`:106`). 굴절속도:
$$ c_\theta(\theta,k)=\frac{\sigma}{\sinh(2kh)}\,(\partial_x h\,\sin\theta-\partial_y h\,\cos\theta) $$
파주기당 1/4 라디안으로 제한 `min(|cθ|, σ/4)` (`:116-137`). 솔버 후 `Fx=F*cos(thetam)`, `Fy=F*sin(thetam)` (`:176-177`).

### `solve_energy_balance2Dstat` (`:183`) — 메인 반복
비정형 격자에서 방향분해 에너지평형을 풀이. 노드별 ee(θ), IG 면 ee_ig(θ), 바람 면 action aa(θ).

**Sweep & 정렬**: 4 sweep 방향으로 좌표를 회전투영(`ra = x cos(θm+kπ/2)+y sin(...)`) 후 heapsort 로 정렬 (`:490-497`). 반복은 `niter*4` 회, sweep=mod(iter,4) (`:526-532`). grid edge·upwind 없는 점은 `inner=.false.` 처리 (`:501-522`).

**upwind 보간**: 두 upwind 점 `prev(1:2,θ,k)` 와 weight `w` 로 에너지·cg 보간 (`:666-685`). 풍파는 action `aa` 도 보간하며 `[ee/sigmax, ee/sigmin]` 으로 clip.

**source/sink (Step 3)**:
- 바닥마찰: `uorbi = 0.5*σ*Hk/sinh(kh)`, `Dfk = 0.28*rho*fw*uorbi^3` (`:710-711`).
- breaking: `Hk > baldock_ratio*Hmx` 일 때만 `baldock(...)` 호출 (`:716-726`).
- 식생: `vegatt` (`:730-733`).
- 소산비 under-relax: `DoverE = (1-r)*DoverE + r*(Dwk+Dfk+Dvegk)/Ek` (`:743-744`).

**에너지 평형 행렬 (Step 4)**: θ에 대한 삼중대각계. 우변 `R = ee/dt + cgprev*eeprev/ds - srcig_local*shinc2ig`(IG sink) (`:778`), 대각 `B = 1/dt + cg/ds + DoverE`, 비대각은 굴절항 `±cθ/(2dθ)` (cyclic θ경계) (`:783-797`). 바람 source `WsorE` 가산 후 `solve_tridiag` (`:799-801`).

**action 평형 (Step 5, 풍파)**: A·C 동일, `B_aa` 에 DoverA, θ 끝단은 upwind BC (`:809-838`).

**depth-limit (Step 6)**: `depthlimfac = max(1, (sqrt(Ek/rhog8)/(gammax*h))^2)`, `ee /= depthlimfac` (`:842-844`).

**IG 평형 (Step 7)**: IG 마찰 `Dfk_ig = fw_ig*0.0361*(g/h)^1.5*Hk*Ek_ig` (`:866`), IG breaking 도 Baldock(gamma_ig). 우변에 IG source `+srcig_local` (`:885-889`), θ경계는 cθ_ig 부호별 한쪽 차분 (`:893-917`).

**수렴**: sweep=4 마다 `diff/eemax < crit` 로 노드별 `ok` 마킹, `error<crit .or. %ok>99` 시 종료. IG 수렴은 로그만 출력하고 종료조건엔 입사파만 사용(주석처리됨, `:986`).

**후처리**: H, thetam(`atan2(Σee·sinθ, Σee·cosθ)`), IG H, 방향평균 beta/alphaig/srcig (`:1026-1063`). 식생 시 `swvegnonlin`(비선형 궤도속도) 후 `F = Dw*k/σ/ρ/h (+ Dveg항 + Fvw)` (`:1078-1116`).

### `solve_tridiag` (`:1123`) — Thomas 알고리즘 (전방소거·후방대입).

### `baldock` (`:1166`) — 파 breaking 소산
$$ D_w = 0.28\,\alpha\,\frac{\rho g}{T}\,e^{-(H_{max}/H_{loc})^2}\,(H_{max}^2+H_{loc}^2)\cdot f $$
여기서 `f=(Hloc/Hmax)^iexp` (Hloc>Hmax 일 때만, 가파른 해안 보강용) (`:1183-1200`).

## 3. Infragravity (IG) source/sink (`snapwave_solver.f90:1209` + `snapwave_infragravity.f90`)

### `determine_infragravity_source_sink_term` (`solver:1209`)
Leijnse et al. 2024 기반 IG source. node별 라디에이션 응력 `Sxx = (2·n - 0.5)·E` 사전계산(n은 [0,1] clip) (`:1305`). 각 방향 upwind:
- 국부 slope `beta_local = max((Σw·(zb(k)-zb(prev)))/ds, 0)` (`:1336`).
- 상대수심 `gam = 0.5*(Hprev/depthprev + H/depth)` (`:1358`).
- 쇼올링 파라미터 `alphaig` 추정 (`estimate_shoaling_parameter_alphaig`, `:1366`).
- ig_opt=1: 보존 쇼올링 `Sxx_cons = Eprev·cgprev/cg_ig·(2n-0.5)`, `dSxx = Sxx_cons - Sxxprev` (`:1383-1387`); ig_opt=2 는 실제 차분 (`:1391`). `dSxx = max(dSxx,0)`.
- IG source:
$$ \text{srcig} = \alpha_{igfac}\cdot\alpha_{ig}\cdot\sqrt{E^{ig}_{prev}}\cdot\frac{cg_{prev}}{h_{prev}}\cdot\frac{dS_{xx}}{ds}\cdot\frac{ee(\theta,k)}{E_{local}} $$
(`:1399`).
- breaking 후(gam > gamma_fac_br·gamma) Fermi-Dirac 형 transition_factor 로 srcig 를 0 으로 부드럽게 소거 (`:1407-1411`).

### `estimate_shoaling_parameter_alphaig` (`solver:1434`)
Leijnse 2024 피팅상수(beta1=0.016993 … beta7=0.34037). beta≤0 면 alphaig=0, 아니면 gam 영역별 지수식, 최종 [0,1] clip (`:1446-1479`).

### IG 경계조건 — Herbers 1994 (`snapwave_infragravity.f90`)
오프쇼어 입력점에서 IG Hm0·Tp 를 입사 스펙트럼으로부터 산정. XBeach `waveparams.f90` 3단계(build_jonswap/build_etdir/build_boundw)를 한 서브루틴 `compute_herbers` 로 포팅 (`:119`).
- Part1: JONSWAP 1D→2D 방향분포 스펙트럼 빌드 (`jonswapgk`, `:160-239`).
- Part2: 피크 주변 K=400 성분 선택, 랜덤위상/방향 할당 (`:242-388`).
- Part3: Herbers eq.1/A5 difference-interaction 계수 D 로 bound long wave 에너지 `Ebnd` 계산 (`:390-478`).
- 최종 `hsig = 4*sqrt(Σ Ebnd·df)` (`:483`), 주기 `tpDcalc` 로 Tm01/Tm-1,0/Tp/Tpsmooth (`:495`).
진입점 `determine_ig_bc` (`:11`): Hs/depth>0.5 면 depth 를 `2*hsinc` 로 강제, depth>200m 면 200 으로 제한(NaN 방지) (`:48-65`). tpig_opt 로 주기 선택(1=Tm01 기본) (`:88-104`). 분산관계는 Klopman 근사 `bc_disper` (`:582`).

## 4. 도메인 & upwind (`snapwave_domain.f90`)

`initialize_snapwave_domain` (`:7`): 상수 설정(`rho=1025`, `np=22`) → quadtree/ASCII/SFINCS 메쉬 읽기(기본 quadtree) → 방향격자 `ntheta360=360/dtheta`, `ntheta=sector/dtheta` (`:100-101`) → 대규모 배열 할당(`:105-170`). 바닥마찰은 공간균일이되 `zb > rghlevland` 육지면 `fw*fwratio` 적용 (`:177-182`).

**upwind 이웃**: `snapwave.upw` 캐시가 있으면 읽고(prev360/w360/ds360/dhdx/dhdy), 없으면 `fm_surrounding_points`(주변점·bed slope 최소제곱) + `find_upwind_neighbours` 로 생성 후 저장 (`:223-279`).
- `find_upwind_neighbours` (`:356`): 각 노드·방향마다 주변 edge 와 광선(θ+π)의 교차점을 `intersect_angle` 로 찾아 2개 upwind 점·weight·거리 ds 산정. 교차 실패 시 prev=1, w=0 (`:405-410`).
- `fm_surrounding_points` (`:457`): face_nodes 로 cell-노드 연결관계 구성, 정렬된 surr_pts 로 bed slope `dhdx=-Σ(dx·dz)/Σdx²` 최소제곱 추정 (sferic 보정 포함) (`:566-594`).

**경계 마스크**: msk=2(파 경계), msk=3(Neumann). msk=2 없으면 구버전 encfile polygon 으로 보충 (`:286-304`). Neumann 은 `neuboundaries_light` 로 각 msk=3 점의 최근접 msk=1 점을 `neumannconnected` 에 저장 (`:308-321`, `:791`). msk=1 이 inner (`:340-348`).

**quadtree 메쉬** `read_snapwave_quadtree_mesh` (`:1039`): quadtree 점에서 refinement 레벨별(mu/nu/mnu) 10여 종 cell 타입(Type 1~10+)을 분기 생성 — fine↔coarse 전이 처리 (`:1331` 이하 장대 분기).

## 5. 경계 데이터 & 스펙트럼 (`snapwave_boundaries.f90`)

`read_boundary_data` (`:8`): jonswap(단일점)/netcdf/timeseries 분기 → `find_boundary_indices`. 입력 방향은 cartesian going-to rad 로 변환 `wd_bwv=(270-wd_bwv)*pi/180`, 분산은 deg→rad (`:85-88`).

`update_boundary_conditions(t)` (`:471`): 경계점 갱신 → 바람장 → theta grid 를 평균 파/바람 방향 중심으로 회전 → `update_boundaries`.

`update_boundary_points` (`:521`): 시계열을 시간보간(`tbfac`). 입력 클램프 — Hs∈[0,25]m, ds∈[3,90]°, Tp∈[0.1,25]s (`:586-609`). IG bc 는 igherbers 면 `find_nearest_depth_for_boundary_points` 후 `determine_ig_bc` 호출(`:671-692`), 아니면 `tpmean_bwv_ig = tpmean_bwv * Tinc2ig` (`:696`).

**경계 스펙트럼 빌드** (`:716-725`): cos^ms 방향분포로 JONSWAP 에너지를 분배.
$$ E_0 = 0.0625\,\rho g\,H_{s}^2,\quad ms = 1/ds^2 - 1,\quad ee_{bwv}(\theta)=\frac{\text{dist}(\theta)}{\Sigma\text{dist}}\cdot\frac{E_0}{d\theta} $$
±π/2 밖은 0. IG 스펙트럼도 동일형, `E0_ig = 0.0625 rho g Hs_ig^2` (`:732`).

`make_theta_grid` (`:778`): 360° 테이블에서 중심방향 주변 ntheta 빈을 인덱스 `i360` 로 슬라이스해 w/prev/ds/windspreadfac 채움. 바람 시 `windspreadfac = cos(θ-u10dir)^mwind` 정규화 (`:818-826`).

`update_boundaries` (`:854`): 격자 경계점(nmindbnd)에 두 가장 가까운 입력점의 ee 를 가중보간 (`:870-880`). IG 는 herbers 면 eet_bwv_ig 보간, 아니면 `ee_ig = eeinc2ig*ee` (`:897-905`).

## 6. 풍파 성장 (`snapwave_windsource.f90`)

`windinput` (`:96`): 무차원 wave state 기반 wind source (Kahma & Calkoen 성장곡선, Breugem-Holthuijsen 완전발달 상한). 깊이제한 완전발달치 `Emaxddmlss=min(aa3²/16·d^(2bb3), Eful)`, `Eful=0.0036`, `Tful=7.69`(Pierson-Moskowitz) (`:125-158`). source 항 `dE = cgdmlss/fE`, `dT = cgdmlss/fT`, dcg/dx 보정 후 방향분포 `windspreadfac` 적용, 차원화 `wsorE = max(u10³·rho·..., 0)`, `wsorA = max(u10⁴·rho/g·..., 0)` (`:168-207`).

`compute_celerities` (`:67`): 노드별 분산관계(`disper_approx_1`)·refraction(`:67-94`). `disper_approx_1` (`:213`): 위 §2 동일 근사식의 단일노드판.

## 7. 식생 & RF table (`snapwave_solver.f90` + `snapwave_RFtable.f90`)

`vegatt` (`solver:1631`) → `swvegatt` (`:1687`): Suzuki et al. 2012 식 단파 식생소산.
$$ D_{vg} = \frac{1}{2\sqrt\pi}\rho\,C_d\,b\,N\,\Big(\tfrac12 k\,g/\sigma\Big)^3\,(h_{term}-h_{term,old})\,H^3 $$
(`:1738`). Cd 미지정 시 에러(M.Bendoni bulkdrag 는 주석처리) (`:1663-1670`).

`swvegnonlin` (`:1879`): Rienecker & Fenton (1981) 비선형 파형으로 skewness 유발 net drag 산정 (XBeach SurfBeat 포팅). `load_RFtable` 로 (11,18,20) RF 테이블 적재 (`:1925`), Ursell 수 기반 Ruessink 위상 `phi=π/2·(1-tanh(0.815/Urs^0.672))` 로 cos/sin 가중 w1/w2 (`:1960-1966`), h0/t0 격자에서 4점 양선형보간 (`:1972-1985`), 50점 시계열 `unl = urf2·sqrt(g·h)` 출력 (`:1999-2000`).

`snapwave_RFtable.f90`: 단일 서브루틴 `load_RFtable` (`:7`). 본문 99% 가 하드코딩 RF 계수 1D 배열(`RFvegtmp`, `:20-3981`)이며 마지막에 `RFveg = reshape(RFvegtmp, (/11,18,20/))` (`:3983`). XBeach `RFveg.inc` 를 컴파일 불필요하게 인라인한 것 (`:16-19` 주석). 차원: 11(=3 메타+8 Fourier 성분)×18(H/depth)×20(T√(g/h)).

## 8. 결합 데이터 흐름 요약

| 단계 | 함수 | 결과 |
|---|---|---|
| 초기화 | `couple_snapwave` → `initialize_snapwave_domain` | 메쉬·upwind·경계 |
| 매스텝 입력 | `update_wave_field` | depth(=SFINCS zs-zb), u10 |
| 경계 | `update_boundary_conditions` | ee/ee_ig 경계 스펙트럼, theta grid |
| 솔버 | `compute_wave_field` → `solve_energy_balance2Dstat` | H, H_ig, Tp, Dw, F, thetam |
| IG | `determine_infragravity_source_sink_term` + Herbers bc | srcig, alphaig, H_ig |
| 출력 매핑 | `update_wave_field` 후반 | hm0(×√2), hm0_ig, fwuv(force/rhow) |

SnapWave→SFINCS 의 물리적 되먹임은 **UV 점 파 force `fwuv`** (radiation stress divergence/ρ → 운동량 가속도, `sfincs_snapwave.f90:502-508`)로, 이것이 SFINCS 흐름에 wave setup·wave-driven current 를 만든다.
