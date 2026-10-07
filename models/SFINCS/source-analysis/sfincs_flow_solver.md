---
title: SFINCS flow solver — reduced-complexity SWE 코어 (momentum·continuity·advection-diffusion·time loop)
model: SFINCS
component: flow-solver
canonical_source: self
citation_status: verified
verification_method: >
  source/src/{sfincs_momentum.f90, sfincs_continuity.f90,
  sfincs_advection_diffusion.f90, sfincs_lib.f90, sfincs_timestep_analysis.f90}
  를 직접 Read. 인용한 모든 file:line 은 본문 작성 전 해당 라인을 직접 확인.
  기본값은 source/src/sfincs_input.f90 read_*_input 호출에서 확인.
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
last_source_check: 2026-10-07 (recovery 재판독 대조)
---

# SFINCS flow solver

SFINCS 의 시간 적분 코어. **staggered grid + explicit** 으로 reduced-complexity 천수방정식(SWE)을 푼다. 한 time step 은 시간루프(`sfincs_lib.f90`)에서

1. `compute_fluxes` (운동량 → U/V 점의 flux `q`, 속도 `uv`)
2. `compute_water_levels` (연속방정식 → 수위 `zs` 또는 부피 `z_volume`)

순서로 실행된다 (`sfincs_lib.f90:584`, `sfincs_lib.f90:618`). [[sfincs-architecture-source-map]] §2 의 호출 순서를 본 노트가 알고리즘 레벨로 보완한다.

## 1. 자료구조 (staggered)

| 변수 | 위치 | 의미 | 인덱싱 |
|---|---|---|---|
| `zs` | z-point (cell center) | 수위 | `nm = 1..np` |
| `z_volume` | z-point | subgrid 모드 셀 부피 | `nm` |
| `q` | uv-point (cell edge) | 단위폭 flux | `ip = 1..npuv` |
| `uv` | uv-point | wet-averaged 속도 = `q / max(hu, huvmin)` | `ip` |
| `q0`, `uv0` | uv-point | `q0`와 `uv0`는 운동량 진입 시점의 사본이다. `sfincs_boundaries.f90:1022` `q(ip) = ub * hnmb + uvmean(ib)`; `sfincs_boundaries.f90:1077` `uv(ip)  = max(min(q(ip) / hnmb, 4.0), -4.0)`; `sfincs_momentum.f90:132` `q0(ip)  = q(ip)`; `sfincs_momentum.f90:133` `uv0(ip) = uv(ip)`<br>경계 유량점의 사본에는 같은 단계에서 갱신한 경계값이 들어간다. `sfincs_boundaries.f90:1022` `q(ip) = ub * hnmb + uvmean(ib)`; `sfincs_boundaries.f90:1077` `uv(ip)  = max(min(q(ip) / hnmb, 4.0), -4.0)`; `sfincs_momentum.f90:132` `q0(ip)  = q(ip)`; `sfincs_momentum.f90:133` `uv0(ip) = uv(ip)`<br>내부 유량점의 사본에는 직전 단계 값이 들어간다. `sfincs_boundaries.f90:1022` `q(ip) = ub * hnmb + uvmean(ib)`; `sfincs_boundaries.f90:1077` `uv(ip)  = max(min(q(ip) / hnmb, 4.0), -4.0)`; `sfincs_momentum.f90:132` `q0(ip)  = q(ip)`; `sfincs_momentum.f90:133` `uv0(ip) = uv(ip)` | `ip` |
| `kcuv` | uv-point | 마스크: 1 정상, 6 연안측방경계 | `sfincs_momentum.f90:159` |
| `kfuv` | uv-point | wet 플래그 (0/1) | `sfincs_momentum.f90:726,747` |

이웃 인덱스는 미리 계산된 매핑 배열로 접근한다: U/V 점에서 좌우 수위점 `uv_index_z_nm`/`uv_index_z_nmu` (`sfincs_momentum.f90:165-166`), 수위점에서 사방 flux 점 `z_index_uv_md/mu/nd/nu` (`sfincs_continuity.f90:130-133`). 즉 격자 위상은 인덱스 배열에 인코딩되어 quadtree 비균일 격자도 동일 루프로 처리된다.

`compute_fluxes`는 이웃 계산 전에 `q`와 `uv`를 복사한다. `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_momentum.f90:132` `q0(ip)  = q(ip)`; `sfincs_momentum.f90:335` `vu      = (uv0(uv_index_v_ndm(ip)) + uv0(uv_index_v_ndmu(ip)) + uv0(uv_index_v_nm(ip)) + uv0(uv_index_v_nmu(ip))) / 4`
`update_boundaries`는 그 복사보다 먼저 경계 유량·속도를 갱신한다. `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_momentum.f90:132` `q0(ip)  = q(ip)`; `sfincs_momentum.f90:335` `vu      = (uv0(uv_index_v_ndm(ip)) + uv0(uv_index_v_ndmu(ip)) + uv0(uv_index_v_nm(ip)) + uv0(uv_index_v_nmu(ip))) / 4`
이류·코리올리·점성은 복사한 배열을 읽는다. `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_momentum.f90:132` `q0(ip)  = q(ip)`; `sfincs_momentum.f90:335` `vu      = (uv0(uv_index_v_ndm(ip)) + uv0(uv_index_v_ndmu(ip)) + uv0(uv_index_v_nm(ip)) + uv0(uv_index_v_nmu(ip))) / 4`

## 2. 운동량 방정식 (`compute_fluxes`)

각 wet U/V 점에서 강제항 `frc` 를 누적한 뒤 Bates et al. (2010) 형식의 semi-implicit friction 갱신으로 새 flux 를 구한다.

### 2.1 wet 판정과 수심 `hu`

- 수위: `zsu = max(zs(nm), zs(nmu))` (`sfincs_momentum.f90:170`).
- subgrid: `zsu > zmin + huthresh` 면 wet (`sfincs_momentum.f90:177-178`). 비-subgrid: `zsu > zbuvmx(ip)` 이며 `zbuvmx = max(zb(nm),zb(nmu)) + huthresh` (`sfincs_momentum.f90:183`, 주석 동일 라인).
- subgrid wet 수심 `hu`: 셀 전체가 잠겼으면(`zsu>zmax`) 테이블 상한 + zsu (`sfincs_momentum.f90:351`), 아니면 subgrid 테이블 `subgrid_uv_havg` 의 선형보간 (`sfincs_momentum.f90:372-378`). 동시에 대표 마찰 `gnavg2`(=$gn^2$)와 wet fraction `phi` 도 같은 보간 (`sfincs_momentum.f90:377-378`).
- 비-subgrid: `hu = max(zsu - zbuvmx(ip), huthresh)`, `gnavg2 = gn2uv(ip)` (`sfincs_momentum.f90:384-385`).

huthresh의 읽기 기본값은 0.05 m이다. `sfincs_input.f90:80` `call read_real_input(500,'huthresh',huthresh,0.05)`
NetCDF subgrid 입력 분기는 huthresh를 0.0으로 재설정한다. `sfincs_subgrid.F90:34` `if (net_file_sbg%ncid > 0) then`; `sfincs_subgrid.F90:40` `huthresh = 0.0`; `sfincs_subgrid.F90:42` `call read_subgrid_file_netcdf()`
이 분기의 젖음 조건은 subgrid 표에 들어 있는 지형·수심 관계도 사용한다. `sfincs_subgrid.F90:34` `if (net_file_sbg%ncid > 0) then`; `sfincs_subgrid.F90:40` `huthresh = 0.0`; `sfincs_subgrid.F90:42` `call read_subgrid_file_netcdf()`

### 2.2 강제항 `frc`

압력(수면경사) 항이 베이스:

$$\text{frc} = -\,g\,h_u\,\frac{\partial z_s}{\partial x}$$

`sfincs_momentum.f90:409`, `dzdx = (zs(nmu)-zs(nm))*dxuvinv` (`:405`). `slopelim` (기본 9999.9, 사실상 off; `sfincs_input.f90:99`) 으로 경사 제한 가능 (`:401`).

이후 옵션 항을 `frc` 에 가산:

| 항 | 조건 | 코드 | file:line |
|---|---|---|---|
| 이류 | `advection` | `adv = -phi*(dqxudx+dqyudy)` 후 `frc+=adv` | `:500,:507` |
| 점성 | `viscosity` | `nuvisc*hu*(라플라시안 uu)` | `:519` (refinement 시 `:525`) |
| 코리올리 | `coriolis` | `frc ± fcoriouv*hu*vu` (U는 +, V는 −) | `:537,:541` |
| 바람 | `wind` | `frc += phi*tauwu(nm)` (얕으면 감쇠) | `:555,:570` |
| 대기압 | `patmos` | `hu*(patm(nm)-patm(nmu))*dxuvinv/rhow` | `:587` |
| 파랑 | `snapwave` | `phi*sign(min(|fwuv|,fwmax),fwuv)` | `:606` |

**이류**는 `mask_adv(ip)==1` (개경계 인근 off) 일 때만 (`:417`). 두 스킴:
- `advection_scheme==0` (original): 단순 upwind, $q>0$/$q<0$ 분기 (`:422-447`).
- `advection_scheme==1` (upw1, **기본** — `sfincs_input.f90:178` `'upw1'`, `:680`): 보존형 1차 upwind 으로 $\partial(qu)/\partial x = q\,\partial u/\partial x + u\,\partial q/\partial x$ 를 면적분값으로 전개 (`:448-498`, 식 주석 `:452-453`).

이류 가속도는 `advlim`(기본 1.0 m/s², `sfincs_input.f90:98`)로 클램프: `adv=min(max(adv,-advlim*hu),advlim*hu)` (`:505`).

코리올리·점성에 쓰는 V-속도는 인접 4점 평균 `vu=(...)/4` (`:335`).

### 2.3 마찰 + Bates 갱신

마찰에 쓰는 flux `qfr`:
- 막 wet 된 점(`kfuv(ip)==0`)은 평형 flux 추정 `qfr=sqrt(|dzdx|/(gnavg2/10))*hu^(5/3)` (`:616`).
- 그 외: `friction2d` 면 $\sqrt{q_x^2+(h_u v_u)^2}$ (`:624`), 아니면 원조 Bates `|q_x|` (`:630`).

새 flux (Bates et al. 2010 의 semi-implicit Manning friction):

$$q^{n+1} = \frac{q_{sm} + \text{frc}\cdot dt}{1 + \dfrac{g\,n^2\,dt\,|q_{fr}|}{h_u^{7/3}}}$$

`sfincs_momentum.f90:677`. 분자 `qsm` 은 보통 `qx_nm`(=`q0`)이며 `thetasmoothing` 시에만 이웃 평균과 혼합 (`:638,:653`, 기본 theta=1.0 → 비활성, `sfincs_input.f90:71`). $h_u^{7/3}$ 은 lookup table `power7over3` (`:667`, 함수 `:787-820`) 또는 직접 `hu**2*hu**(1/3)` (`:673`).

**후처리 한계들**:
- `wiggle_suppression` (subgrid, 기본 on `sfincs_input.f90:180`): 인접 셀 수위 가속 부호가 반대로 클 때 flux 감쇠 (`:683-687`).
- 음의 부피/수심 셀에서 유출 차단: `z_volume(nm)<0` 면 `q=min(q,0)` 등 (`:697-713`).
- flux limiter `uvlim` (기본 10 m/s, `sfincs_input.f90:184`): `q=min(max(q,-hu*uvlim),hu*uvlim)` (`:719`).
- 속도 `uv(ip)=q(ip)/max(hu,huvmin)` (`:724`); `huvmin` 기본 0.0 (`sfincs_input.f90:81`).

dry 점은 `q=uv=0`, `kfuv=0` (`:745-747`).

### 2.4 combined uv 점

quadtree 미세-조대 경계의 결합점 `ncuv` 개는 두 하위 uv 점 평균: `q(cuv)=(q1+q2)/2`, `uv` 동일 (`sfincs_momentum.f90:771-772`). 이 값이 연속방정식·출력에 쓰인다 (주석 `:759-761`).

운동량은 후속 유량 보정 전에 결합점 평균을 만든다. `sfincs_momentum.f90:771` `q(cuv_index_uv(icuv))  = (q(cuv_index_uv1(icuv)) + q(cuv_index_uv2(icuv))) / 2`; `sfincs_momentum.f90:772` `uv(cuv_index_uv(icuv)) = (uv(cuv_index_uv1(icuv)) + uv(cuv_index_uv2(icuv))) / 2`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`
wavemaker·구조물·비정수압 루틴은 이 평균을 다시 만드는 대입을 포함하지 않는다. `sfincs_momentum.f90:771` `q(cuv_index_uv(icuv))  = (q(cuv_index_uv1(icuv)) + q(cuv_index_uv2(icuv))) / 2`; `sfincs_momentum.f90:772` `uv(cuv_index_uv(icuv)) = (uv(cuv_index_uv1(icuv)) + uv(cuv_index_uv2(icuv))) / 2`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`


## 3. 연속방정식 (`compute_water_levels`)

`subgrid` 여부로 분기 (`sfincs_continuity.f90:22-30`): subgrid → `compute_water_levels_subgrid`, 아니면 `compute_water_levels_regular`.

### 3.1 regular

점소스 먼저 (`:87-106`), 이후 각 `kcs(nm)==1` 셀:

$$z_s^{n+1} = z_s^n + \big[(q_{nmd}-q_{nmu})\,dx^{-1} + (q_{ndm}-q_{num})\,dy^{-1}\big]\,dt$$

`sfincs_continuity.f90:151` (projected). 강수 `netprcp*dt` (`:118`), 외부소스 `qext*dt` (`:126`) 선가산. geographic(`crsgeo`)은 위도별 셀폭 `dxm(nm)` 사용 (`:139`).

### 3.2 subgrid (부피 기반)

flux 발산으로 **부피 변화** `dvol` 누적 (`:355` geo / `:376` quadtree / `:380` regular), 강수·qext 를 `dvol += dzsdt*a*dt` 로 가산 (`:495`), storage volume 처리(`:499-531`) 후 `z_volume(nm) += dvol` (`:535`). 수위는 subgrid 테이블에서 역산:

저장용량 옵션은 subgrid에서 사용한다. `sfincs_input.f90:655` `if (volfile(1:4) /= 'none') then`; `sfincs_input.f90:656` `if (subgrid) then`; `sfincs_input.f90:657` `use_storage_volume = .true.`
순강수·면 유량의 양의 유입은 남은 저장용량을 먼저 채운다. `sfincs_continuity.f90:503` `if (storage_volume(nm) > 1.0e-6 .and. dvol > 0.0) then`; `sfincs_continuity.f90:513` `storage_volume(nm) = max(dv, 0.0)`; `sfincs_continuity.f90:525` `dvol = 0.0`; `sfincs_continuity.f90:535` `z_volume(nm) = z_volume(nm) + dvol`
점 유량은 계산 셀의 z_volume에 직접 들어간다. `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt`
점 유량은 저장용량의 우선 저장 분기를 우회한다. `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt`; `sfincs_continuity.f90:501` `! If water enters the cell through a point discharge, it will NOT end up in storage volume !`; `sfincs_continuity.f90:503` `if (storage_volume(nm) > 1.0e-6 .and. dvol > 0.0) then`

- 완전 wet (`z_volume >= subgrid_z_volmax*0.999`): `zs=max(z_zmax,-20)+(vol-volmax)/a` (`:553`).
- 거의 dry (`<=1e-6`): `zs=max(z_zmin,-20)` (`:559`).
- 그 외: 부피→수위 테이블 `subgrid_z_dep` 선형보간 (`:565-568`).

`wiggle_suppression` 용 2차 도함수 `zsderv(nm)=zs - 2*zs11 + zs00` 저장 (`:575`) — 이를 §2.3 의 flux 감쇠가 사용.

subgrid 연속식은 단계 끝에서 `zsderv`를 쓴다. `sfincs_continuity.f90:575` `zsderv(nm) = zs(nm) - 2 * zs11 + zs00`; `sfincs_momentum.f90:683` `mdrv = abs(zsderv(nm) - zsderv(nmu)) - wiggle_threshold`
다음 단계의 운동량은 이 값을 읽는다. `sfincs_continuity.f90:575` `zsderv(nm) = zs(nm) - 2 * zs11 + zs00`; `sfincs_momentum.f90:683` `mdrv = abs(zsderv(nm) - zsderv(nmu)) - wiggle_threshold`
현재 운동량은 직전 단계의 `zsderv`를 사용한다. `sfincs_continuity.f90:575` `zsderv(nm) = zs(nm) - 2 * zs11 + zs00`; `sfincs_momentum.f90:683` `mdrv = abs(zsderv(nm) - zsderv(nmu)) - wiggle_threshold`


### 3.3 부가 저장

`compute_store_variables` (`:626-720`): `vmax`(`:684`), `qmax`(`:691`), `twet`(`:700,707`) 누적. `zsmax`(최대수위)는 메인 루프 내에서 `store_maximum_waterlevel`이 참일 때 갱신한다(`sfincs_continuity.f90:239-255`, subgrid `sfincs_continuity.f90:600-616`).

## 4. 이류-확산 (tracer, 옵션)

현재 `sfincs_update`의 시간 반복은 tracer 계산 루틴을 호출하지 않는다. `sfincs_lib.f90:524` `call update_meteo_fields(t, tloopwnd1)`; `sfincs_lib.f90:530` `call update_meteo_forcing(t, dt, tloopwnd2)`; `sfincs_lib.f90:538` `call update_infiltration_map(dt, tloopinf)`; `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:550` `call update_discharges(t, dt, tloopsrc)`; `sfincs_lib.f90:556` `call update_wave_field(t, tloopsnapwave)`; `sfincs_lib.f90:576` `call bathtub_compute_water_levels(tloopcont)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_lib.f90:588` `call timestep_analysis_update(min_dt)`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_lib.f90:628` `call write_output(tout, write_map, write_his, write_max, write_rst, ntmapout, ntmaxout, nthisout, tloopoutput)`; `sfincs_lib.f90:644` `call write_output(t, .true., .true., .true., .false., ntmapout + 1, ntmaxout, nthisout + 1, tloopoutput)`; `sfincs_meteo.f90:1570` `call update_amuv_data()`; `sfincs_meteo.f90:1576` `call update_amp_data()`; `sfincs_meteo.f90:1582` `call update_ampr_data()`; `sfincs_meteo.f90:1588` `call update_spiderweb_data()`; `sfincs_meteo.f90:1414` `call update_wind_forcing_from_timeseries(t)`; `sfincs_meteo.f90:1422` `call update_precipitation_from_timeseries(t, dt)`; `sfincs_boundaries.f90:1151` `call update_boundary_points(t)`; `sfincs_boundaries.f90:1162` `call update_boundary_conditions(t, dt)`; `sfincs_boundaries.f90:1166` `call update_boundary_fluxes(dt, t)`; `sfincs_snapwave.f90:415` `call compute_snapwave(t)`; `sfincs_momentum.f90:667` `hu73 = power7over3(max(hu, 1.0e-6))`; `sfincs_momentum.f90:787` `function power7over3(hu) result(hu73)`; `sfincs_nonhydrostatic.f90:631` `call bicgstab_solve(nrows, AA, col_idx, row_ptr, QQ, pnh, nh_tol, nh_itermax, iter, relres, .true.)`; `sfincs_continuity.f90:24` `call compute_water_levels_subgrid(dt,t)`; `sfincs_continuity.f90:28` `call compute_water_levels_regular(dt,t)`; `sfincs_continuity.f90:36` `call compute_store_variables(dt)`; `sfincs_output.f90:151` `call ncoutput_update_quadtree_map(t, ntmapout)`; `sfincs_output.f90:153` `call ncoutput_update_regular_map(t, ntmapout)`; `sfincs_output.f90:158` `call write_map_output()`; `sfincs_output.f90:200` `call ncoutput_update_quadtree_max(t, ntmaxout)`; `sfincs_output.f90:202` `call ncoutput_update_max(t, ntmaxout)`; `sfincs_output.f90:207` `call write_max_output()`; `sfincs_output.f90:247` `call write_rst_file(t)`; `sfincs_output.f90:257` `call ncoutput_update_his(t,nthisout)`; `sfincs_output.f90:261` `call write_his_output(t)`; `sfincs_lib.f90:381` `call system_clock(countdt0, count_rate, count_max)`; `sfincs_lib.f90:657` `call system_clock(count1, count_rate, count_max)`; `sfincs_lib.f90:554` `call timer(t3)`; `sfincs_lib.f90:558` `call timer(t4)`; `sfincs_lib.f90:560` `call write_log(logstr, 0)`; `sfincs_lib.f90:664` `call write_log(logstr, 1)`; `sfincs_lib.f90:667` `call write_log(logstr, 1)`; `sfincs_date.f90:369` `call system_clock (count,count_rate,count_max)`; `sfincs_meteo.f90:1566` `call system_clock(count0, count_rate, count_max)`; `sfincs_meteo.f90:1608` `call system_clock(count1, count_rate, count_max)`; `sfincs_meteo.f90:1255` `call system_clock(count0, count_rate, count_max)`; `sfincs_meteo.f90:1426` `call system_clock(count1, count_rate, count_max)`; `sfincs_infiltration.f90:628` `call system_clock(count0, count_rate, count_max)`; `sfincs_infiltration.f90:1034` `call system_clock(count1, count_rate, count_max)`; `sfincs_boundaries.f90:1143` `call system_clock(count0, count_rate, count_max)`; `sfincs_boundaries.f90:1172` `call system_clock(count1, count_rate, count_max)`; `sfincs_discharges.f90:349` `call system_clock(count0, count_rate, count_max)`; `sfincs_discharges.f90:657` `call system_clock(count1, count_rate, count_max)`; `sfincs_snapwave.f90:317` `call system_clock(count0, count_rate, count_max)`; `sfincs_snapwave.f90:519` `call system_clock(count1, count_rate, count_max)`; `sfincs_bathtub.f90:133` `call system_clock(count0, count_rate, count_max)`; `sfincs_bathtub.f90:171` `call system_clock(count1, count_rate, count_max)`; `sfincs_momentum.f90:97` `call system_clock(count0, count_rate, count_max)`; `sfincs_momentum.f90:781` `call system_clock(count1, count_rate, count_max)`; `sfincs_wavemaker.f90:1423` `call system_clock(count0, count_rate, count_max)`; `sfincs_wavemaker.f90:1758` `call system_clock(count1, count_rate, count_max)`; `sfincs_wavemaker.f90:1519` `call write_log(logstr, 0)`; `sfincs_wavemaker.f90:1522` `call write_log(logstr, 0)`; `sfincs_structures.f90:623` `call system_clock(count0, count_rate, count_max)`; `sfincs_structures.f90:694` `call system_clock(count1, count_rate, count_max)`; `sfincs_nonhydrostatic.f90:442` `call system_clock(count0, count_rate, count_max)`; `sfincs_nonhydrostatic.f90:741` `call system_clock(count1, count_rate, count_max)`; `sfincs_continuity.f90:20` `call system_clock(count0, count_rate, count_max)`; `sfincs_continuity.f90:40` `call system_clock(count1, count_rate, count_max)`; `sfincs_output.f90:107` `call system_clock(count0, count_rate, count_max)`; `sfincs_output.f90:267` `call system_clock(count1, count_rate, count_max)`
이 절의 tracer 코드 설명은 활성 시간 단계 흐름과 구분한다. `sfincs_lib.f90:524` `call update_meteo_fields(t, tloopwnd1)`; `sfincs_lib.f90:530` `call update_meteo_forcing(t, dt, tloopwnd2)`; `sfincs_lib.f90:538` `call update_infiltration_map(dt, tloopinf)`; `sfincs_lib.f90:546` `call update_boundaries(t, dt, tloopbnd)`; `sfincs_lib.f90:550` `call update_discharges(t, dt, tloopsrc)`; `sfincs_lib.f90:556` `call update_wave_field(t, tloopsnapwave)`; `sfincs_lib.f90:576` `call bathtub_compute_water_levels(tloopcont)`; `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_lib.f90:588` `call timestep_analysis_update(min_dt)`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_lib.f90:628` `call write_output(tout, write_map, write_his, write_max, write_rst, ntmapout, ntmaxout, nthisout, tloopoutput)`; `sfincs_lib.f90:644` `call write_output(t, .true., .true., .true., .false., ntmapout + 1, ntmaxout, nthisout + 1, tloopoutput)`; `sfincs_meteo.f90:1570` `call update_amuv_data()`; `sfincs_meteo.f90:1576` `call update_amp_data()`; `sfincs_meteo.f90:1582` `call update_ampr_data()`; `sfincs_meteo.f90:1588` `call update_spiderweb_data()`; `sfincs_meteo.f90:1414` `call update_wind_forcing_from_timeseries(t)`; `sfincs_meteo.f90:1422` `call update_precipitation_from_timeseries(t, dt)`; `sfincs_boundaries.f90:1151` `call update_boundary_points(t)`; `sfincs_boundaries.f90:1162` `call update_boundary_conditions(t, dt)`; `sfincs_boundaries.f90:1166` `call update_boundary_fluxes(dt, t)`; `sfincs_snapwave.f90:415` `call compute_snapwave(t)`; `sfincs_momentum.f90:667` `hu73 = power7over3(max(hu, 1.0e-6))`; `sfincs_momentum.f90:787` `function power7over3(hu) result(hu73)`; `sfincs_nonhydrostatic.f90:631` `call bicgstab_solve(nrows, AA, col_idx, row_ptr, QQ, pnh, nh_tol, nh_itermax, iter, relres, .true.)`; `sfincs_continuity.f90:24` `call compute_water_levels_subgrid(dt,t)`; `sfincs_continuity.f90:28` `call compute_water_levels_regular(dt,t)`; `sfincs_continuity.f90:36` `call compute_store_variables(dt)`; `sfincs_output.f90:151` `call ncoutput_update_quadtree_map(t, ntmapout)`; `sfincs_output.f90:153` `call ncoutput_update_regular_map(t, ntmapout)`; `sfincs_output.f90:158` `call write_map_output()`; `sfincs_output.f90:200` `call ncoutput_update_quadtree_max(t, ntmaxout)`; `sfincs_output.f90:202` `call ncoutput_update_max(t, ntmaxout)`; `sfincs_output.f90:207` `call write_max_output()`; `sfincs_output.f90:247` `call write_rst_file(t)`; `sfincs_output.f90:257` `call ncoutput_update_his(t,nthisout)`; `sfincs_output.f90:261` `call write_his_output(t)`; `sfincs_lib.f90:381` `call system_clock(countdt0, count_rate, count_max)`; `sfincs_lib.f90:657` `call system_clock(count1, count_rate, count_max)`; `sfincs_lib.f90:554` `call timer(t3)`; `sfincs_lib.f90:558` `call timer(t4)`; `sfincs_lib.f90:560` `call write_log(logstr, 0)`; `sfincs_lib.f90:664` `call write_log(logstr, 1)`; `sfincs_lib.f90:667` `call write_log(logstr, 1)`; `sfincs_date.f90:369` `call system_clock (count,count_rate,count_max)`; `sfincs_meteo.f90:1566` `call system_clock(count0, count_rate, count_max)`; `sfincs_meteo.f90:1608` `call system_clock(count1, count_rate, count_max)`; `sfincs_meteo.f90:1255` `call system_clock(count0, count_rate, count_max)`; `sfincs_meteo.f90:1426` `call system_clock(count1, count_rate, count_max)`; `sfincs_infiltration.f90:628` `call system_clock(count0, count_rate, count_max)`; `sfincs_infiltration.f90:1034` `call system_clock(count1, count_rate, count_max)`; `sfincs_boundaries.f90:1143` `call system_clock(count0, count_rate, count_max)`; `sfincs_boundaries.f90:1172` `call system_clock(count1, count_rate, count_max)`; `sfincs_discharges.f90:349` `call system_clock(count0, count_rate, count_max)`; `sfincs_discharges.f90:657` `call system_clock(count1, count_rate, count_max)`; `sfincs_snapwave.f90:317` `call system_clock(count0, count_rate, count_max)`; `sfincs_snapwave.f90:519` `call system_clock(count1, count_rate, count_max)`; `sfincs_bathtub.f90:133` `call system_clock(count0, count_rate, count_max)`; `sfincs_bathtub.f90:171` `call system_clock(count1, count_rate, count_max)`; `sfincs_momentum.f90:97` `call system_clock(count0, count_rate, count_max)`; `sfincs_momentum.f90:781` `call system_clock(count1, count_rate, count_max)`; `sfincs_wavemaker.f90:1423` `call system_clock(count0, count_rate, count_max)`; `sfincs_wavemaker.f90:1758` `call system_clock(count1, count_rate, count_max)`; `sfincs_wavemaker.f90:1519` `call write_log(logstr, 0)`; `sfincs_wavemaker.f90:1522` `call write_log(logstr, 0)`; `sfincs_structures.f90:623` `call system_clock(count0, count_rate, count_max)`; `sfincs_structures.f90:694` `call system_clock(count1, count_rate, count_max)`; `sfincs_nonhydrostatic.f90:442` `call system_clock(count0, count_rate, count_max)`; `sfincs_nonhydrostatic.f90:741` `call system_clock(count1, count_rate, count_max)`; `sfincs_continuity.f90:20` `call system_clock(count0, count_rate, count_max)`; `sfincs_continuity.f90:40` `call system_clock(count1, count_rate, count_max)`; `sfincs_output.f90:107` `call system_clock(count0, count_rate, count_max)`; `sfincs_output.f90:267` `call system_clock(count1, count_rate, count_max)`


`compute_tracer_fluxes` (`sfincs_advection_diffusion.f90:5`): wet uv 점마다 tracer flux. upwind 이류 + Fickian 확산:

$$\text{trflux} = q\cdot c_{up} + (c_{nm}-c_{nmu})\cdot \text{dico}$$

$q>0$ 면 상류농도 `trconc(nm)`, 아니면 `trconc(nmu)` (`:49-56`). `dico` 는 확산계수. 결합점 평균도 수행(`:77-85`).

> 주의: `:82` 의 `trflux(itracer, cuv_index_uv(icuv)) = (itracer, trflux(...)+...)/2` 는 인덱싱이 깨진 표현(컴파일 불가 형태)으로 보인다 — tracer 경로가 미완/비활성 가능성. 단언이 아니라 코드 그대로 관찰만 기록.

## 5. 시간 루프와 CFL (`sfincs_lib.f90`)

### 5.1 dt 결정

`compute_fluxes` 가 각 wet 점에서 CFL 후보를 계산:

$$\text{min\_dt\_ip} = \frac{1}{\max\!\big(\sqrt{g h_u},\,|uv|\big)\cdot dx^{-1}}$$

`sfincs_momentum.f90:731`, 전역 최소로 reduction `min_dt=min(min_dt,min_dt_ip)` (`:733`). 즉 dt 는 셀별 파속+이류속도의 CFL 로 매 step 적응.

루프에서 `alfa`(CFL 계수, 기본 0.5 — `sfincs_input.f90:70`)를 곱해 실제 dt:

```
dt = alfa * min_dt   ! min_dt 는 alfa 없이 momentum 에서 계산
dtchk = alfa * min_dt
```

입력 `dtmax`의 기본값은 60초다. `sfincs_input.f90:79` `call read_real_input(500,'dtmax',dtmax,60.0)`; `sfincs_domain.f90:1524` `dtmax = min(dtmax, alfa * dxymin / (sqrt(9.81 * hmin_cfl)))`; `sfincs_momentum.f90:99` `min_dt = dtmax`
투영 좌표의 도메인 초기화는 격자 간격과 `hmin_cfl`로 이 상한을 추가 제한한다. `sfincs_input.f90:79` `call read_real_input(500,'dtmax',dtmax,60.0)`; `sfincs_domain.f90:1524` `dtmax = min(dtmax, alfa * dxymin / (sqrt(9.81 * hmin_cfl)))`; `sfincs_momentum.f90:99` `min_dt = dtmax`
운동량은 최종 상한으로 `min_dt`를 초기화한다. `sfincs_input.f90:79` `call read_real_input(500,'dtmax',dtmax,60.0)`; `sfincs_domain.f90:1524` `dtmax = min(dtmax, alfa * dxymin / (sqrt(9.81 * hmin_cfl)))`; `sfincs_momentum.f90:99` `min_dt = dtmax`

### 5.2 step 순서와 불안정 정지

일반 계산 경로는 운동량 다음에 단계 진단·wavemaker·구조물·비정수압·연속식을 조건에 따라 실행한다. `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_lib.f90:588` `call timestep_analysis_update(min_dt)`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_lib.f90:392` `dtchk = alfa * min_dt`; `sfincs_lib.f90:634` `if (dtchk < dtmin .and. nt > 1) then`
단계 시작의 `dtchk`가 `dtmin`보다 작고 `nt>1`이면 최종 출력을 기록한다. `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_lib.f90:588` `call timestep_analysis_update(min_dt)`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_lib.f90:392` `dtchk = alfa * min_dt`; `sfincs_lib.f90:634` `if (dtchk < dtmin .and. nt > 1) then`
현재 운동량이 새로 만든 `min_dt`는 다음 단계의 간격에 쓰인다. `sfincs_lib.f90:584` `call compute_fluxes(dt, tloopflux)`; `sfincs_lib.f90:588` `call timestep_analysis_update(min_dt)`; `sfincs_lib.f90:594` `call update_wavemaker_fluxes(t, dt, tloopwavemaker)`; `sfincs_lib.f90:600` `call compute_fluxes_over_structures(tloopstruc)`; `sfincs_lib.f90:610` `call compute_nonhydrostatic(dt, tloopnonh)`; `sfincs_lib.f90:618` `call compute_water_levels(t, dt, tloopcont)`; `sfincs_lib.f90:392` `dtchk = alfa * min_dt`; `sfincs_lib.f90:634` `if (dtchk < dtmin .and. nt > 1) then`

현재 중단 메시지는 최소 시간 간격과 uvmax 초과를 적는다. `sfincs_lib.f90:638` `write(error_message,'(a,f0.4,a,f0.1,a)')'Error! Minimum time step of ', dtmin, ' s reached ! Current velocity exceeded uvmax ', uvmax, ' m/s. Simulation stopped.'`


## 6. timestep 진단 (`sfincs_timestep_analysis.f90`, 옵션)

`timestep_analysis` 활성 시 uv 점별 통계로 "어느 셀이 dt 를 제한하는가" 를 추적.

- `compute_fluxes` 진입 시 `timestep_analysis_required_timestep(ip)=dtmax` 로 리셋 (dry 셀은 dtmax 유지) (`sfincs_momentum.f90:112`), wet 점은 `min_dt_ip` 저장 (`:739`).
- `timestep_analysis_update(min_dt)` (`sfincs_lib.f90:588`): wet 점(`kfuv==1`)의 required dt 누적 평균, `times_wet++` (`sfincs_timestep_analysis.f90:51-55`), 전역 `min_dt` 와 거의 같으면(`<= min_dt+1e-6`) `times_limiting++` (`:59-61`).
- `timestep_analysis_finalize(nt)` (`sfincs_lib.f90:698`): 셀의 8개 이웃 U/V 점 평균 required dt 의 최소에 `alfa` 곱해 셀별 dt 맵, 유효 이웃 없으면 −1 (`sfincs_timestep_analysis.f90:178-188`), 제한 비율 `100*tmsl/nt` (`:192`).

  코드는 이 값을 dtmax 이하로 제한한다. `sfincs_timestep_analysis.f90:182` `timestep_analysis_average_required_timestep_per_cell(nm) = min(dtm * alfa, dtmax)`
  해석: 유효한 건조 면의 0/max(0,1) 경로는 값 0을 만들 수 있다. `sfincs_timestep_analysis.f90:124` `dtm = min(dtm, timestep_analysis_average_required_timestep(nmd1) / max(timestep_analysis_times_wet(nmd1), 1))`
  -1은 유효 주변 면이 없어 큰 초기 dtm이 남는 경우에 기록한다. `sfincs_timestep_analysis.f90:188` `timestep_analysis_average_required_timestep_per_cell(nm) = -1.0`
  percentage_limiting_timestep은 주변 면별 제한 횟수의 최댓값에 100/nt를 곱한다. `sfincs_timestep_analysis.f90:59` `if (timestep_analysis_required_timestep(ip) <= min_dt + 1.0e-6) then`; `sfincs_timestep_analysis.f90:125` `tmsl = max(tmsl, timestep_analysis_times_limiting(nmd1))`; `sfincs_timestep_analysis.f90:192` `timestep_analysis_percentage_limiting_per_cell(nm) = 100.0 * tmsl / nt`
  해석: 이 비율은 주변 면의 제한 단계 집합을 합친 비율과 일반적으로 같지 않다. `sfincs_timestep_analysis.f90:125` `tmsl = max(tmsl, timestep_analysis_times_limiting(nmd1))`; `sfincs_timestep_analysis.f90:192` `timestep_analysis_percentage_limiting_per_cell(nm) = 100.0 * tmsl / nt`

- `timestep_analysis_write_log` (`sfincs_lib.f90:781`): 가장 자주 제한한 uv 점의 인덱스·좌표·제한 비율 로그 (`sfincs_timestep_analysis.f90:206-241`).

## 핵심 요약

- explicit, staggered, cell-center 수위 / cell-edge flux. 위상은 인덱스 배열에 인코딩 → quadtree 동일 처리.
- 운동량: 수면경사 압력항 + 옵션(이류 upw1 기본·점성·코리올리·바람·기압·파랑) → Bates(2010) semi-implicit Manning friction 갱신 (`sfincs_momentum.f90:677`).
- 연속: regular 는 수위 직접 갱신, subgrid 는 부피→테이블 역산 (`sfincs_continuity.f90:151` vs `:535,:553-568`).
- dt: 셀별 $1/(\max(\sqrt{gh},|u|)\,dx^{-1})$ 의 전역 최소 × `alfa`(0.5), 상한 `dtmax`(60 s); `dtmin` 미만 시 중단 (`sfincs_lib.f90:391,634`).
