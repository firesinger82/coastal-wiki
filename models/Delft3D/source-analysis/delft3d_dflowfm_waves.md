---
title: "Delft3D D-Flow FM 파 결합 — radiation stress·wave force·Stokes drift + surfbeat(XBeach) infragravity"
model: Delft3D
component: dflowfm/compute_waves
canonical_source: self
citation_status: verified
verification_method: "Delft3D 소스 직접 read (src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/compute_waves/). 파 결합 dispatcher(compute_wave_forcing_rhs.f90), 파라미터 계산(compute_wave_parameters.f90), wave force(setwavfu.f90), Stokes 속도(wave_comp_stokes_velocities.f90·wave_uorbrlabda.f90), 파 mass flux 경계(setwavmubnd.f90), 파-흐름 bottom stress(tauwave.f90·setmodind.f90), surfbeat(surfbeat/xbeachwaves.f90: radiation stress·wave action balance·roller·breaker dissipation) 의 식·자료구조·분기를 file:line 인용. 모드 상수는 dflowfm_data/m_waveconst.f90 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/README.md
---

# Delft3D D-Flow FM 파 결합 — radiation stress·wave force·Stokes drift + surfbeat

> D-Flow FM(비구조 격자) 측 파 효과 커널. 경로: `src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/compute_waves/`. flow2d3d(구조격자) 측은 [[wave/delft3d_flow_wave_coupling]] 참조 — **본 노트는 D-Flow FM 전용**.

## 0. 위치·범위 주의

배정 경로가 `packages/dflowfm_kernel/.../compute_waves` 였으나 실제 트리는 한 단계 더 깊음:
`src/engines_gpl/dflowfm/packages/dflowfm_kernel/src/dflowfm_kernel/compute_waves/`.
이 디렉토리는 (a) 루트의 파 결합 파일 25개 + (b) `surfbeat/` 하위(XBeach 유래 13파일, ≈16k 라인)로 구성.

## 1. 파 결합 모드 (jawave) 열거

모든 분기의 기준 상수는 `dflowfm_data/m_waveconst.f90` 에 정의:

| 상수 | 값 | 의미 | 인용 |
|---|---|---|---|
| `NO_WAVES` | 0 | 파 없음 | `m_waveconst.f90:5` |
| `WAVE_FETCH_HURDLE` | 1 | Hurdle-Stive fetch 모델 | `m_waveconst.f90:6` |
| `WAVE_FETCH_YOUNG` | 2 | Young-Verhagen fetch 모델 | `m_waveconst.f90:7` |
| `WAVE_SWAN_ONLINE` | 3 | online SWAN 결합 | `m_waveconst.f90:8` |
| `WAVE_SURFBEAT` | 4 | surfbeat(XBeach) infragravity | `m_waveconst.f90:9` |
| `WAVE_UNIFORM` | 5 | 균일 파장(spatially uniform) | `m_waveconst.f90:10` |
| `WAVE_NC_OFFLINE` | 7 | SWAN NetCDF offline | `m_waveconst.f90:11` |

파력(wave force) 모드 `WAVEFORCING_*`: 0=없음, 1=radiation stress, 2=dissipation total, 3=dissipation 3D (`m_waveconst.f90:18-21`).
Stokes drift 모드 `STOKES_DRIFT_*`: 0=off, 1=depth-uniform, 2=2nd-order, 3=+viscous, 4=+viscous+advection (`m_waveconst.f90:24-28`).

## 2. 시간스텝 dispatcher — compute_wave_forcing_rhs

`compute_wave_forcing_rhs.f90` 의 `compute_wave_forcing_RHS` 가 매 스텝 파 강제력을 모드별로 분기:

- **fetch 모드** (`jawave < WAVE_SWAN_ONLINE`): 2D면 `tauwave()` 호출 (`compute_wave_forcing_rhs.f90:68-72`).
- **SWAN online/offline** (`jawave == WAVE_SWAN_ONLINE .or. == WAVE_NC_OFFLINE`): `tauwave()` → `setwavfu()`(wave force) → `setwavmubnd()`(경계 mass flux) (`compute_wave_forcing_rhs.f90:75-81`).
- **SURFBEAT**: `jajre==1 .and. nwbnd>0` 이고 `swave==1` 일 때 XBeach 체인 `xbeach_wave_bc()` → `xbeach_apply_wave_bc()` → `xbeach_waves()` → `xbeach_wave_compute_flowforcing2D()`, 3D면 추가로 `xbeach_wave_compute_flowforcing3D()` (`compute_wave_forcing_rhs.f90:84-107`).
- **UNIFORM**: 2D면 `tauwave()` (`compute_wave_forcing_rhs.f90:110-114`).

파라미터(uorb·rlabda·Stokes) 계산은 별도로 `compute_wave_parameters.f90` 의 `compute_wave_parameters` 가 담당 (`compute_wave_parameters.f90:48`).

## 3. 파 파라미터 — uorb, 파장(rlabda)

`wave_uorbrlabda.f90` 의 `wave_uorbrlabda`:

- 분산관계로 파수 `rk` 결정: 심해(`k0h > pi`)면 `rk = k0`, 극천해(`k0h < 5e-3`)면 `rk = ω/√(g·hss)`, 중간이면 `getwavenr()` 반복해 (`wave_uorbrlabda.f90:66-72`). 여기서 `k0 = ω²/g` (`wave_uorbrlabda.f90:64`).
- 파장 `rlabda(k) = 2π/rk` (`wave_uorbrlabda.f90:76`).
- 바닥 궤도속도 진폭:
$$u_{orb} = \frac{1}{2} H_{rms}\,\frac{\omega}{\sinh(k\,h)}$$
(`wave_uorbrlabda.f90:82`). `jauorb==0`(구 D3D 관례)이면 `uorb *= √π/2` 보정 (`wave_uorbrlabda.f90:83-85`). SWAN에서 직접 읽은 uorb 사용 옵션은 `jauorbfromswan==1` (`wave_uorbrlabda.f90:79-80`).

`compute_wave_parameters` 에서 `hwav` 는 항상 breaking 한계 `gammax`로 clip: `hwav = min(hwav, gammax*hs)` (`compute_wave_parameters.f90:105`, `:66`, `:149`). NetCDF offline 입력은 `Hsig → Hrms` 변환 `hwav = hwavcom / √2` (`compute_wave_parameters.f90:101`).

## 4. Wave force (radiation stress 구배) — setwavfu

`setwavfu.f90` 의 `setwavfu` 가 셀중심 파 강제력 `sxwav/sywav`(표면력, surface)와 `sbxwav/sbywav`(체적력, body)를 link 법선 방향으로 투영해 `wavfu/wavfv` 생성.

핵심 메커닉:
- **force 한계(limiter)**: `facmax = 0.25·g·ρ·gammaloc²` (`setwavfu.f90:83`), `fmax = facmax·hu^1.5 / max(0.1, twav)` (`setwavfu.f90:108`, 3D는 `:150`).
- **2D** (`kmx==0`): link 양 셀의 force를 `acl` 가중 평균 후 법선·접선 분해, 벡터 norm으로 한계 적용(성분별이 아님 — `:116` 주석 "Should be done on the vector norm, nt separate comps"), 표면력+체적력 합산 (`setwavfu.f90:99-127`). 최종 가속도화: `wavfu *= min(huvli, 1/hminlw)/rhomean`, 단위 [m/s²] (`setwavfu.f90:130-131`).
- **3D** (`kmx>0`): 표면력은 **최상위 층(Lt)에만** 부여 — "as in D3D" (`setwavfu.f90:159`), 체적력은 연직 균일 분배 (`setwavfu.f90:196-199`).
- limiting depth `hminlw`/`gammaloc` 는 SWAN 계열이면 `m_waves` 값, SURFBEAT면 `m_xbeach_data` 의 `hminlw`/`gammaxxb` (`setwavfu.f90:71-81`).

## 5. Stokes drift 와 wave mass flux

### 5.1 셀중심 mass flux → link Stokes 속도
`wave_comp_stokes_velocities.f90` 의 `wave_comp_stokes_velocities` (SWAN online/offline·2D 경로):
- mass flux 한계: `massflux_max = (1/8)·g·hs^1.5·gammax²` (`wave_comp_stokes_velocities.f90:81`).
- 천해 surf zone 보정: `gammal = hwav/h`, `gammal>1` 이면 `hstokes = deltahmin·(gammal-1)·hwav + h` (`wave_comp_stokes_velocities.f90:104-109`, `deltahmin=0.1` `:78`).
- link Stokes 속도: `ustokes(L) = Mu/hstokes` (= mass flux ÷ effective depth) (`wave_comp_stokes_velocities.f90:117-118`). 경계는 Neumann (`:125-154`). MPI ghost 갱신 `update_ghosts(ITYPE_U,…)` (`:156-161`).

### 5.2 fetch/uniform 의 Stokes (shear velocity 기반)
2D fetch·uniform 모드에선 `compute_wave_shear_velocity(hw,tw,hh,…,ustt)` 로 ustt 산출 후 풍향(fetch) 또는 phiwav(uniform)으로 투영 (`compute_wave_parameters.f90:86-88`, `:164-166`).

### 5.3 경계 wave mass flux — setwavmubnd
`setwavmubnd.f90` 의 `setwavmubnd`: 전 mesh 에 정의되나 **open boundary 에서만 비영(非零)** (`setwavmubnd.f90:61-62`). u-bnd(`nbndu`), Riemann z-bnd(`BOUNDARY_VELOCITY_RIEMANN`), normal-velocity bnd(`nbndn`) 각각에 대해 셀중심 `mxwav/mywav` 를 link 법선으로 투영하고 `min(huvli, 1/hminlw)` 로 가중 (`setwavmubnd.f90:76-79`, `:104-116`, `:133-144`). 접선 bnd 는 불필요 (`:148`). 2D/3D(연직 균일, "like D3D" `:81`) 분기.

전역 토글 `jawavestokes==0` 이면 `compute_wave_parameters` 끝에서 ustokes/vstokes 강제 0 (`compute_wave_parameters.f90:176-179`).

## 6. 파-흐름 결합 bottom shear stress — tauwave

`tauwave.f90` 의 `tauwave` (2D; 3D는 `update_verticalprofiles` 에서 호출 — `compute_wave_forcing_rhs.f90:70` 주석). 파+흐름 조합 바닥 마찰 모델.

- **Eulerian 속도 사용**: `uuu = u1(L) - ustokes(L)` (`tauwave.f90:101`), `vvv = v(L) - vstokes(L)` (`:107`) — 즉 Stokes drift 를 제거한 흐름속도로 마찰 계산.
- 흐름 관련 거칠기: Chézy `cz = get_chezy(...)`, `z0 = h/(e·(exp(κ·cz/√g)-1))` (`tauwave.f90:129-133`).
- 파 마찰계수 (modind 1~9): `astar = T·uorb/z0`, `astar>astarc` 이면 `fw = 0.00251·exp(14.1/astar^0.19)`, 아니면 `fw=0.3` (`tauwave.f90:151-157`; `astarc = 30π²` `:75`).
- 파 단독 바닥전단응력: `tauwav = 0.5·ρ·fw·ftauw·uorb²` (`tauwave.f90:162`).
- modind=9(Van Rijn)이면 `cfhi_vanrijn`, 일반은 `cfwavhi` 채움 (`tauwave.f90:115-117`, `:87`).

### wave-current 상호작용 모델 키워드 (modind)
`setmodind.f90` 의 `setmodind(rouwav, modind)` 가 4글자 키워드를 정수 modind 로 매핑 (`setmodind.f90:49-69`):

| 키워드 | modind | 모델 |
|---|---|---|
| FR84 | 1 | Fredsøe (1984) |
| MS90 | 2 | Myrhaug-Slaattelid (1990) |
| HT91 | 3 | Huynh-Thanh & Temperville (1991) |
| GM79 | 4 | Grant-Madsen (1979) |
| DS88 | 5 | Davies-Soulsby (1988) |
| BK67 | 6 | Bijker (1967) |
| CJ85 | 7 | Christoffersen-Jonsson (1985) |
| OY88 | 8 | O'Connor-Yoo (1988) |
| VR04 | 9 | Van Rijn (2004) |
| RU03 | 10 | Ruessink (2003) |

조합 응력 계수 `ymxpar` 는 `getymxpar.f90` 의 `getymxpar` (Soulsby 파라미터화) 호출 (`tauwave.f90:45` use, `compute_wave_parameters`/tauwave 내 사용). 보조 함수: `swart.f90`(Swart 마찰), `soulsby.f90`(Soulsby), `hurdlestive.f90`/`ian_young_pt.f90`(fetch growth).

## 7. Fetch 기반 파 성장 (jawave 1/2)

- **Hurdle-Stive** (`hurdlestive.f90:43`): 무차원 fetch `fs = g·F/ua²`·depth `ds`로 `Hsig`, `Tsig` 직접 산출. 식은 Coastal Stabilisation(Silvester-Shu) 2.35/2.36 & Hurdle-Stive 1989 (`hurdlestive.f90:56-57` 주석). 기준풍속 `ua = 0.71·(rt·U10)^1.23` (`:52`).
- **Young-Verhagen** (`ian_young_pt.f90`).
- fetch 계산 자체: `getfetch.f90`·`tauwavefetch.f90`(620라인, 매 격자점 바람 방향별 fetch·depth 적분). MPI 병렬에선 전용 fetch proc 사용 — `fetch_proc.F90` 의 `fetch_proc_operation_data`/`m_fetch_operation_utils`(`fetch_proc.F90:33-54`)가 mass-gather 로 s1 송신·fetch 값 수신 (`:53-54`).

## 8. surfbeat (XBeach 유래) — infragravity 위상해상

`surfbeat/` 는 XBeach surfbeat 모드를 D-Flow FM 비구조 격자에 이식한 것. 핵심은 `xbeachwaves.f90` (6176라인, module `m_xbeachwaves`, `xbeachwaves.f90:33`). 공개 진입점: `xbeach_waves`, `xbeach_wave_compute_flowforcing2D/3D`, `xbeach_wave_bc`, `xbeach_flow_bc`, `xbeach_wave_init` 등 (`xbeachwaves.f90:41-42`).

### 8.1 메인 흐름 — xbeach_waves
`xbeach_waves(ierr)` (`xbeachwaves.f90:3217`):
1. 파 계산용 수심 `hhw` 설정 (deltaH 옵션 시 `hs + deltaH·H`) (`:3237-3241`), `hstokes` 천해 보정 (`:3243-3254`).
2. `instat` 에 따라 분기: `'stat'/'stat_table'` 이면 `xbeach_wave_dispersion(0)` + `xbeach_wave_stationary(0)` (`:3259-3264`); 그 외 instationary 면 `xbeach_wave_dispersion` + `xbeach_wave_instationary()` (`:3285`, `:3295`). `single_dir>0` 분기로 refraction 만 stationary 풀이 (`:3266-3285`). wave-current interaction `wci>0` 면 dispersion type 2 (`:3280-3282`).
3. `xbeach_compute_stokesdrift()` 매 스텝 (2D) (`:3300-3302`).

### 8.2 파 작용/에너지 균형 — xbeach_wave_instationary
`xbeach_wave_instationary` (`xbeachwaves.f90:876`), 방향분해(θ-grid, `ntheta`) 위상평균 에너지 `ee1(itheta,k)`:
- bulk 에너지 `E = Σ ee1·dtheta`, 파고 `H = √(8E/(ρg))` (`:1042-1047`). `gammaxxb·hs` 초과 영역은 `ee1` 스케일 다운 + `H` clip (`:1050-1069`).
- **breaker dissipation** `D` 는 `xbeach_wave_breaker_dissipation(...)` (`:1073`).
- **bed friction dissipation**: `Df = (2·fw·ρ/(3π))·uorb³`, `uorb = H·σ/2·1/sinh(k·h)` (`:1076-1080`); `h>fwcutoff` 면 `Df=0` (`:1086-1088`).
- dissipation 의 방향 분배: 깨짐 `ddlok`, 깨짐+마찰 `dd` (`:1092-1095`).
- **roller energy balance**: `rr` 의 수평·방향 이류(`advec_horz`/`advec_dir`) (`:1121-1122`), Euler step `rr += dts·(ddlok - drr)`, `drr = 2·g·BR·rr/cwav` (`:1174-1176`). `roller==0` 이면 rr=0 (`:1177-1179`).
- 에너지 갱신: `ee1 -= dts·dd` (`:1173`), 음수 clip (`:1181-1184`). MPI ghost 갱신 (`:1191-1200`).
- `thetamean` = 에너지 가중 평균 파향 (`:1224-1227`), waterline 인접 dry cell 은 이웃 평균으로 채움 (`:1230-1261`).
- roller off 시 대체: `R = 0.9·ρ·g·sin(β)·H²` (Martins 2018) (`:1217`).

### 8.3 breaker dissipation 식 — xbeach_wave_breaker_dissipation
`xbeach_wave_breaker_dissipation` (`xbeachwaves.f90:2222`):
- **Roelvink (1993)** `break=='roelvink1'`: $Q_b = 1 - e^{-(H/(\gamma h))^n}$ (`:2282`, `:2285`), $D = Q_b\cdot 2\alpha\rho g H^2/8 / T_{rep}$ (`:2286`, `:2291`). wci 시 $\gamma\tanh(kh)/k$ 형 (`:2280`).
- **Baldock et al. (1998)** `break=='baldock'` (stationary 전용): `gam = γ` 또는 wci 시 `0.76·kh+0.29` (`:2308-2311`).
- 모드 제약: Roelvink/Roelvink-Daly 는 instationary 만, Baldock/Janssen 은 stationary 만 (`:361-381`).

### 8.4 radiation stress → flow forcing
`xbeach_wave_compute_flowforcing2D` (`xbeachwaves.f90:1306`):
- radiation stress (파 + roller 기여):
$$S_{xx} = \big[n\,\textstyle\sum(1+\cos^2\theta)\,E_\theta - \tfrac12\sum E_\theta\big]d\theta + \sum\cos^2\theta\, r_\theta\,d\theta$$
(`:1331`, `:1335`), 동형 `Syy`(`:1332`,`:1336`), `Sxy = n·Σsinθcosθ·E·dθ + roller`(`:1333`,`:1337`). `nwav = cgwav/cwav` (`:1329`).
- wave force = radiation stress 구배: `Fx_cc = -∂Sxx/∂x - ∂Sxy/∂y`, `Fy_cc = -∂Sxy/∂x - ∂Syy/∂y` (`:1364-1367`). 구배는 link 가중 `wcx1/wcy1·dxi` 합산 (`:1351-1361`). 경계 Neumann (`:1370-1389`), MPI ghost (`:1391-1400`).
- 2D wavfu: `wavfu = (Fx·csu + Fy·snu)/(ρ·max(hu,hminlw))` (`:1412-1413`), dry link 0 (`:1416-1419`).

`xbeach_wave_compute_flowforcing3D` (`xbeachwaves.f90:6040`): dissipation 을 표면력으로 분배 `sxwav = cos(dir)·D·T/L`, body force = `Fx_cc - sxwav` (`:6066-6073`), roller on 시 `DR` 사용 (`:6058-6061`), 이후 `setwavfu()` 호출해 3D wavfu 구성 (`:6094`) — 즉 §4 의 표면/체적력 split 메커닉을 재사용.

### 8.5 경계조건
`xbeach_wave_bc`(`:1670`)·`xbeach_apply_wave_bc`(`:2177`): 파 에너지 경계 스펙트럼; `xbeach_flow_bc`(`:2683`): absorbing-generating(Riemann) 흐름 경계. wave energy boundary 의 edge node 인덱싱 (`:5418-5465`).

### 8.6 surfbeat 지원 모듈
`surfbeat/` 내 보조: `xbeach_readkey.F90`(params.txt 키 파싱), `xbeach_filefunctions.F90`(로깅), `xbeach_math_tools.F90`(수치), `xbeach_interp.F90`(보간), `xbeach_netcdf.f90`(출력, 1724라인), `xbeach_wave_boundary_main.f90`·`xbeach_wave_boundary_update.f90`(스펙트럼 경계 생성, 3005라인), `xbeach_paramsconst.f90`(상수), `xbeach_typesandkinds.F90`, `xbeach_errorhandling.f90`, `xbeach_getcellcentergradients.f90`, `xbeach_wave_boundary_datastore.f90`. 역할만 요약 — 세부는 source-needed.

## 9. 보조 루틴 요약 (역할만)

- `alloc9basicwavearrays.f90` — 기본 파 배열 할당.
- `flow_waveinit.f90`(367라인) — 파 결합 초기화.
- `getwavenr.f90` — 분산관계 반복해 파수 (`getwavenr` `:43`경, `wave_uorbrlabda.f90:71` 호출).
- `reconstruct_cc_stokesdrift.f90` — link Stokes → 셀중심 재구성 (`reconstruct_cc_stokesdrift.f90:43`).
- `wave_fillsurdis.f90`·`wave_statbreakerdis.f90` — surface/breaker dissipation 채우기.
- `wave_shear_velocity.f90` — 파 shear velocity (`compute_wave_parameters.f90:86` 호출).
- `wave_makeplotvars.f90` — GUI 시각화 변수 (`compute_wave_forcing_rhs.f90:117-123`).

## 10. flow2d3d 와의 차이 (요지)

- **격자**: flow2d3d = 구조격자(M,N); D-Flow FM = 비구조 link/셀 (`ln`, `acl`, `csu`, `snu` 기반 투영).
- **공통 D3D 관례 유지**: 3D 표면력 최상위 층 부여(`setwavfu.f90:159`), 경계 mass flux 연직 균일(`setwavmubnd.f90:81`), `jauorb==0` 의 `√π/2` 보정(`wave_uorbrlabda.f90:84`) — 모두 "as in D3D" 명시.
- **surfbeat**: flow2d3d 에는 없는 XBeach 기반 infragravity 위상해상 모듈이 D-Flow FM 측에만 존재.
- SWAN 결합 자체(파↔흐름 양방향)의 일반 메커닉은 [[wave/delft3d_flow_wave_coupling]] 참조; 본 노트는 FM kernel 내부 force 적용·Stokes·tauwave·surfbeat 에 집중.
