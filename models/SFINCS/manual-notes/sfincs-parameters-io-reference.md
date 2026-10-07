---
title: SFINCS 파라미터·입출력 reference (sfincs.inp 키워드 / 입력파일 / forcing / 구조물 / output)
model: SFINCS
doc: parameters.rst, input.rst, output.rst, input_forcing.rst, input_structures.rst, waves.rst
canonical_source: manual
citation_status: verified
verification_method: SFINCS 공식 docs RST 원문 직접 인용 (raw/source_code/sfincs/docs/)
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[../source-analysis/sfincs_io_data]]"
  - "[[../source-analysis/sfincs_boundaries_forcing]]"
  - "[[../source-analysis/sfincs_structures_physics]]"
  - "[[../source-analysis/sfincs_snapwave]]"
last_source_check: 2026-10-07 (recovery 재판독 대조)
---

# SFINCS 파라미터·입출력 reference

SFINCS 의 모든 모델 설정·도메인·forcing·구조물은 keyword/value 형식의 메인 입력파일 `sfincs.inp` 로 연결된다 (`docs/input.rst §Overview`). 본 노트는 공식 docs 의 파라미터·입출력 reference 를 발췌·정리한다. 입력파일 포맷 표기: bin=binary, asc=ascii, net=netcdf.

---

## 1. sfincs.inp 키워드 (`docs/parameters.rst`)

### 1.1 도메인·격자 (`§Parameters for model input`)

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `mmax` | 0 | - | x-방향 격자 셀 수 (활성셀 최대 ~3M 권장) |
| `nmax` | 0 | - | y-방향 격자 셀 수 |
| `dx` | 0 | m | x-방향 격자 크기 (max 1000 m 권장) |
| `dy` | 0 | m | y-방향 격자 크기 |
| `x0` | 0 | m (UTM) | 첫 격자 셀 코너 (1,1) X-좌표 (셀 중심 아님) |
| `y0` | 0 | m (UTM) | 첫 격자 셀 코너 (1,1) Y-좌표 |
| `rotation` | 0 | deg | x-축(동)에서 반시계 방향 격자 회전 (0~359.999) |

기존 입력은 투영좌표의 정규격자를 정의한다. `sfincs_input.f90:96` `call read_int_input(500,'epsg',epsg,0)`; `sfincs_input.f90:104` `call read_int_input(500,'crsgeo',igeo,0)`; `sfincs_input.f90:399` `if (igeo == 0) then`
현재 코드가 quadtree 격자 입력을 지원한다. `sfincs_domain.f90:193` `if (use_quadtree) then`; `sfincs_domain.f90:197` `call quadtree_read_file(qtrfile, snapwave, nonhydrostatic)`
현재 코드가 crsgeo를 통한 구면좌표 분기를 지원한다. `sfincs_input.f90:104` `call read_int_input(500,'crsgeo',igeo,0)`; `sfincs_input.f90:399` `if (igeo == 0) then`; `sfincs_input.f90:419` `crsgeo = .true.`; `sfincs_domain.f90:1403` `if (crsgeo) then`
구면좌표의 격자 길이는 코드에서 도 단위로 해석한 뒤 m로 변환한다. `sfincs_domain.f90:1403` `if (crsgeo) then`; `sfincs_domain.f90:1405` `! dxr and dyr are now in degrees. Must convert to metres.`
epsg 입력은 좌표계 메타데이터를 제공한다. `sfincs_input.f90:96` `call read_int_input(500,'epsg',epsg,0)`

### 1.2 수치·물리 (momentum/continuity)

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `advection` | 1 | - | 이류항: 0=off (SFINCS-LIE), 1=on (default, SFINCS-SSWE). Cauberg release 이후 구 1D/2D 구분 대체 |
| `advection_scheme` | `upw1` | - | 신규 scheme `upw1`(default) / `original`(Leijnse et al. 2021, 하위호환). 2024.01 release 이후 |
| `advlim` | 1.0 | m/s² | 이류항 가속도 한계 (v2.2.0 이후 default 1.0, limiter on) |
| `alpha` | 0.5 | - | CFL 조건 시간스텝 감소계수 (0.1~0.75 권장) |
| `friction2d` | true | - | 마찰항 2D 성분 포함 여부 (`false`=Leijnse 2021 구현). 2024.01 이후 |
| `huthresh` | 읽기 0.05; NetCDF subgrid 0.0 | m | huthresh의 읽기 기본값은 0.05 m이다. `sfincs_input.f90:80` `call read_real_input(500,'huthresh',huthresh,0.05)`<br>NetCDF subgrid 입력 분기는 huthresh를 0.0으로 재설정한다. `sfincs_subgrid.F90:34` `if (net_file_sbg%ncid > 0) then`; `sfincs_subgrid.F90:40` `huthresh = 0.0`; `sfincs_subgrid.F90:42` `call read_subgrid_file_netcdf()`<br>이 분기의 젖음 조건은 subgrid 표에 들어 있는 지형·수심 관계도 사용한다. `sfincs_subgrid.F90:34` `if (net_file_sbg%ncid > 0) then`; `sfincs_subgrid.F90:40` `huthresh = 0.0`; `sfincs_subgrid.F90:42` `call read_subgrid_file_netcdf()` |
| `theta` | 1.0 | - | momentum 평활화계수 (1.0=무평활, 0.8~1.0) |
| `hmin_cfl` | 0.1 | m | CFL 최대 timestep 결정용 최소 수심 (v2.2.0 이후) |
| `baro` | 1 | - | 기압항 on(1)/off(0). 0이면 ampfile·spwfile 등 기압입력 무시 |
| `viscosity` | false (0) | - | viscosity의 읽기 기본값은 false이다. `sfincs_input.f90:111` `call read_logical_input(500,'viscosity',iviscosity,.false.)`<br>viscosity=1을 입력하면 점성항을 켠다. `sfincs_input.f90:590` `viscosity = .false.`; `sfincs_input.f90:591` `if (iviscosity) then`; `sfincs_input.f90:592` `viscosity = .true.`<br>theta=1.0과 점성을 함께 사용하는 문서의 권고는 읽기 기본값과 구분한다. `docs/developments.rst:222` `* New recommended default combination that with new advection scheme: alpha=0.50, theta=1.0, advection=1 (is now always 2D), viscosity=1.` |
| `nuvisc` | 0.01 | m/s (입력, 해석) | 현재 입력 nuvisc의 기본값은 0.01이다. `sfincs_input.f90:110` `call read_real_input(500,'nuvisc',nuviscdim,0.01)`<br>현재 코드는 이 값을 셀 길이에 곱한다. `sfincs_domain.f90:1565` `nuvisc(iref) = max(nuviscdim * dxyr(iref), 0.0) ! take min of dx and dy, don't allow to be negative`<br>현재 리더는 nuviscdim이라는 입력 키워드를 읽지 않는다. `sfincs_input.f90:110` `call read_real_input(500,'nuvisc',nuviscdim,0.01)`<br>nuviscdim은 현재 코드의 내부 변수 이름이다. `sfincs_input.f90:110` `call read_real_input(500,'nuvisc',nuviscdim,0.01)`; `sfincs_domain.f90:1565` `nuvisc(iref) = max(nuviscdim * dxyr(iref), 0.0) ! take min of dx and dy, don't allow to be negative`<br>해석: 현재 입력 nuvisc의 차원은 m/s이다. `sfincs_input.f90:110` `call read_real_input(500,'nuvisc',nuviscdim,0.01)`; `sfincs_domain.f90:1565` `nuvisc(iref) = max(nuviscdim * dxyr(iref), 0.0) ! take min of dx and dy, don't allow to be negative`; `sfincs_momentum.f90:519` `frc = frc + nuvisc(iref) * hu * ( (uu_nmu - 2*uu_nm + uu_nmd ) * dxuv2inv + (uu_num - 2*uu_nm + uu_ndm ) * dyuv2inv )`; `sfincs_momentum.f90:677` `q(ip) = (qsm + frc * dt) / (1.0 + gnavg2 * dt * qfr / hu73)`; `docs/parameters.rst:116` `:units:		-`<br>해석: 셀 길이를 곱한 내부 nuvisc의 차원은 m^2/s이다. `sfincs_domain.f90:1565` `nuvisc(iref) = max(nuviscdim * dxyr(iref), 0.0) ! take min of dx and dy, don't allow to be negative`; `sfincs_momentum.f90:519` `frc = frc + nuvisc(iref) * hu * ( (uu_nmu - 2*uu_nm + uu_nmd ) * dxuv2inv + (uu_num - 2*uu_nm + uu_ndm ) * dyuv2inv )`; `sfincs_momentum.f90:677` `q(ip) = (qsm + frc * dt) / (1.0 + gnavg2 * dt * qfr / hu73)` |
| `coriolis` | True | logical | Coriolis 항. 투영좌표계에서 latitude 미지정(0.0)이면 off |
| `nuviscdim` | - | - | Cauberg release 이후 deprecated |

이류·점성·평활 상호배제 권고: viscosity=1 **또는** theta<1.0 중 하나만 사용 (둘 다 X) (`docs/input.rst §Numerical parameters`).

### 1.3 초기조건·infiltration·마찰

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `zsini` | 0 | m above ref | 도메인 전체 초기 수위 (bed level 위) |
| `qinf` | 0 | mm/hr | 공간균일·시간일정 infiltration rate (0~100) |
| `qinf_zmin` | 0 | m above ref | `qinf` 적용 최소 표고 (해역 제외용) |
| `sfacinf` | 0.2 | - | Curve Number 초기손실(initial abstraction) 계수 |
| `manning` | 0.04 | s/m^(1/3) | 균일 manning 조도 (0~0.1 권장) |
| `rgh_lev_land` | 0 | m above ref | land/sea 조도 구분 표고 |
| `manning_land` | -999(미사용) | s/m^(1/3) | `rgh_lev_land` 위 land 조도 |
| `manning_sea` | -999(미사용) | s/m^(1/3) | `rgh_lev_land` 아래 sea 조도 |
| `amprblock` | 1 | - | sfincs.inp의 강수 보간 입력 이름은 amprblock이다. `sfincs_input.f90:106` `call read_int_input(500,'amprblock',iamprblock,1)`<br>읽기 기본값은 1이다. `sfincs_input.f90:106` `call read_int_input(500,'amprblock',iamprblock,1)`<br>코드는 이 값을 내부 논리 변수 ampr_block로 바꾼다. `sfincs_input.f90:537` `ampr_block = .true. ! Default use data in ampr file as block rather than linear interpolation`; `sfincs_input.f90:538` `if (iamprblock==0) then`; `sfincs_input.f90:539` `ampr_block = .false.`<br>1은 구간 일정 보간을 뜻한다. `sfincs_meteo.f90:1142` `if (ampr_block) then`; `sfincs_meteo.f90:1146` `twfac  = 0.0`<br>0은 시간 선형 보간을 뜻한다. `sfincs_input.f90:538` `if (iamprblock==0) then`; `sfincs_input.f90:539` `ampr_block = .false.`; `sfincs_meteo.f90:1142` `if (ampr_block) then`; `sfincs_meteo.f90:1146` `twfac  = 0.0` |

infiltration 은 **강우가 forcing 될 때만** 켜지며, 방법 간 stack(중첩) 비설계 (`docs/input.rst §Infiltration`).

CN→S의 전처리 식은 S=1000/CN-10이다. `docs/input.rst:420` `**S = (1000./CN - 10)**`; `docs/input.rst:429` `For spatially varying infiltration values per cell using the Curve Number method without recovery use the scsfile option, with the same grid based input as the depfile using a binary file. Note here that in pre-processing the wanted CN values should be converted to S values following:`
scsfile의 S 입력 단위는 inch이다. `docs/input.rst:430` `* scsfile: maximum soil moisture storage capacity in inches`
kernel은 S를 m로 바꾼다. `sfincs_infiltration.f90:290` `qinffield = qinffield * 0.0254   ! to m`

CN A는 P>sfacinf·S에서 Q=(P-sfacinf·S)^2/(P+(1-sfacinf)·S)를 계산한다. `sfincs_input.f90:102` `call read_real_input(500,'sfacinf',sfacinf,0.2)`; `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`
P가 이 문턱을 넘지 않으면 코드가 강수를 전량 침투로 처리한다. `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:701` `qinfmap(nm) = prcp(nm)`
해석: Q=P^2/(P+S)는 sfacinf=0인 특수 경우로 표시한다. `sfincs_input.f90:102` `call read_real_input(500,'sfacinf',sfacinf,0.2)`; `sfincs_infiltration.f90:689` `if (cumprcp(nm) > sfacinf * qinffield(nm)) then ! qinffield is S`; `sfincs_infiltration.f90:693` `Qq  = (cumprcp(nm) - sfacinf * qinffield(nm))**2 / (cumprcp(nm) + (1.0 - sfacinf) * qinffield(nm))  ! cumulative runoff in m`

(`docs/input.rst §The Curve Number method:`). Green-Ampt:

$$f(t) = K\left(1 + \frac{\Delta\theta\,(\sigma + h_0)}{F(t)}\right)$$

공식 문서의 Green-Ampt 기본식은 표면 수심 h0를 포함한다. `docs/input.rst:496` `**f(t) = K(1+ delta_theta (sigma + h0) / F(t) )**`; `docs/input.rst:501` `Within SFINCS, the Green-Ampt method can be used as follows. The user needs to provide the following variables. For a range of typical values see Table 1. For all variables, one needs to specify these values per cell with the same grid based input as the depfile using a binary file:`
현재 코드의 고강수 분기 식은 ksfield(nm)·(1+GA_head(np)·GA_sigma(np)/GA_F(nm))이다. `sfincs_infiltration.f90:838` `do nm = 1, np`; `sfincs_infiltration.f90:842` `if (prcp(nm) > 0.0) then`; `sfincs_infiltration.f90:846` `if (prcp(nm) < ksfield(nm)) then`; `sfincs_infiltration.f90:850` `qinfmap(nm) = prcp(nm)                       ! infiltration is same as rainfall`; `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`; `sfincs_infiltration.f90:857` `qinfmap(nm) = max(min(qinfmap(nm), prcp(nm)), 0.0)     ! never more than rainfall and and never negative`
이 식은 명시적인 h0 항을 포함하지 않는다. `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`
이 분기의 셀은 마지막 셀의 흡입수두와 수분 부족량을 참조한다. `sfincs_infiltration.f90:838` `do nm = 1, np`; `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`
포화 수리전도도와 누적 침투 상태는 각 셀의 값을 사용한다. `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`; `sfincs_infiltration.f90:863` `GA_sigma(nm) = max(GA_sigma(nm) - (qinfmap(nm) * dt / GA_Lu(nm)), 0.0)`; `sfincs_infiltration.f90:867` `GA_F(nm)    = GA_F(nm) + qinfmap(nm) * dt   ! internal cumulative rainfall from Green-Ampt`
전체 침투율이 공간적으로 균일해진다고 단정할 수 없다. `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`; `sfincs_infiltration.f90:863` `GA_sigma(nm) = max(GA_sigma(nm) - (qinfmap(nm) * dt / GA_Lu(nm)), 0.0)`; `sfincs_infiltration.f90:867` `GA_F(nm)    = GA_F(nm) + qinfmap(nm) * dt   ! internal cumulative rainfall from Green-Ampt`
np를 nm로 바꾸는 작성 의도는 확인하지 않았다. `sfincs_infiltration.f90:838` `do nm = 1, np`; `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`
원문 식과 결함 해석을 구분한다. `docs/input.rst:496` `**f(t) = K(1+ delta_theta (sigma + h0) / F(t) )**`; `sfincs_infiltration.f90:838` `do nm = 1, np`; `sfincs_infiltration.f90:856` `qinfmap(nm) = (ksfield(nm) * (1.0 + (GA_head(np) * GA_sigma(np)) / GA_F(nm)))`


(`docs/input.rst §The Green-Ampt method:`). Horton:

$$f_t = f_c + (f_0 - f_c)\,e^{-kt}$$

(`docs/input.rst §The Horton method:`). Horton 회복: `horton_kr_kd` default 10.0 (회복이 감쇠의 1/10 속도).

### 1.4 고급 키워드 (`§More parameters for model input (only for advanced users)`)

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `bndtype` | 1 | - | `sfincs.bzs` 해석: 1=수위 (구 type 2&3 은 v2.0.2 이후 제거) |
| `rhoa` | 1.25 | kg/m³ | 공기 밀도 |
| `rhow` | 1024 | kg/m³ | 물 밀도 |
| `wiggle_suppression` | True | logical | flux limiter (subgrid mode 한정, v2.2.0 이후 default True) |
| `uvlim` | 10 | m/s | flux 유속 한계 (v2.2.0 이후) |
| `uvmax` | 1000 | m/s | 최대 flux 유속; 미만 timestep시 불안정 판정·정지 (v2.2.0, `stopdepth` 대체) |
| `slopelim` | 9999.9 | - | dzdx slope limiter (default off=9999.9, v2.2.0 이후) |
| `huvmin` | 0.0 | m (해석) | huvmin은 유속 계산에 사용하는 최소 수심이다. `sfincs_input.f90:81` `call read_real_input(500,'huvmin', huvmin, 0.0)                   ! Minimum depth for calculating velocity (uv = q / max(hu, huvmin) used for output and advection)`<br>해석: 읽기 기본값 0.0의 수심 단위는 m이다. `sfincs_input.f90:81` `call read_real_input(500,'huvmin', huvmin, 0.0)                   ! Minimum depth for calculating velocity (uv = q / max(hu, huvmin) used for output and advection)`; `sfincs_momentum.f90:724` `uv(ip) = q(ip) / max(hu, huvmin)`<br>코드는 uv=q/max(hu,huvmin)을 사용한다. `sfincs_momentum.f90:724` `uv(ip) = q(ip) / max(hu, huvmin)` |
| `dtmax` | 60 | s | 최대 내부 timestep |
| `dtmin` | 입력 기본값 없음; 내부 계산값 | s | 현재 코드가 dtmin을 입력 키워드로 읽지 않는다. `sfincs_domain.f90:1530` `! dtmin = alfa * dxymin / (sqrt(9.81 * stopdepth))`; `sfincs_domain.f90:1539` `dtmin = alfa * dxymin / (1.25 * abs(uvmax))`<br>현재 내부 dtmin은 alpha·최소 셀 길이·uvmax로 계산한다. `sfincs_domain.f90:1539` `dtmin = alfa * dxymin / (1.25 * abs(uvmax))` |
| `tspinup` | 0 | s | tstart 후 spinup 기간 (경계수위 댐핑) |
| `spinup_meteo` | 0 | - | meteo forcing 에도 spinup 적용 여부 |
| `utmzone` | nil | - | spiderweb lat&lon→UTM 변환 (예 `16N`/`36S`) |
| `h73table` | 0 | logical | h^(7/3) lookup table (~0-30% 가속) |
| `structure_relax` | 10 | s | 구조물 신/구 방류 비율 완화계수 |

stopdepth의 제거 판은 두 공식 문서의 설명이 상충한다. `docs/parameters.rst:202` `stopdepth - removed from SFINCS v2.1.1 Dollerup onwards, replaced by 'uvmax'`; `docs/developments.rst:173` `* stopdepth - REMOVED in SFINCS v2.2.0, replaced by 'uvmax' to determine possible instabilities based on flow velocities rather than maximum water depth!`
제거 시점을 확인하려면 이전 판의 원문이 필요하다. `docs/parameters.rst:202` `stopdepth - removed from SFINCS v2.1.1 Dollerup onwards, replaced by 'uvmax'`; `docs/developments.rst:173` `* stopdepth - REMOVED in SFINCS v2.2.0, replaced by 'uvmax' to determine possible instabilities based on flow velocities rather than maximum water depth!`

**Drag coefficients (풍속 의존, Delft3D 방식·Vatvani et al. 2012 기반):**

| 키워드 | 기본값 | 설명 |
|---|---|---|
| `cdnrb` | 3 | break point 개수 |
| `cdwnd` | `0 28 50` | 풍속 break point (m/s, 0 포함) |
| `cdval` | `0.001 0.0025 0.0015` | drag coefficient break point |

(`docs/parameters.rst §More parameters for model input (only for advanced users)`). `docs/input.rst §Drag Coefficients:` 에서는 키워드명을 `cd_nr`/`cd_wnd`/`cd_val` 로 표기 — 본문 간 표기 차이 주의.

sfincs.inp의 활성 항력 입력 이름은 cdnrb·cdwnd·cdval이다. `sfincs_input.f90:312` `call read_int_input(500,'cdnrb',cd_nr,0)`; `sfincs_input.f90:334` `call read_real_array_input(500,'cdwnd',cd_wnd,0.0,cd_nr)`; `sfincs_input.f90:335` `call read_real_array_input(500,'cdval',cd_val,0.0,cd_nr)`
cd_nr·cd_wnd·cd_val은 내부 변수 이름이다. `sfincs_input.f90:312` `call read_int_input(500,'cdnrb',cd_nr,0)`; `sfincs_input.f90:334` `call read_real_array_input(500,'cdwnd',cd_wnd,0.0,cd_nr)`; `sfincs_input.f90:335` `call read_real_array_input(500,'cdval',cd_val,0.0,cd_nr)`
리더는 밑줄이 들어간 예시 이름을 입력 별칭으로 지원하지 않는다. `sfincs_read.f90:28` `if (trim(keystr)==trim(keyword)) then`; `sfincs_read.f90:139` `if (trim(keystr)==trim(keyword)) then`
cdnrb를 생략하면 코드는 기본 절점 세 개를 구성한다. `sfincs_input.f90:312` `call read_int_input(500,'cdnrb',cd_nr,0)`; `sfincs_input.f90:318` `cd_nr = 3`; `sfincs_input.f90:323` `cd_wnd(1) =   0.0`; `sfincs_input.f90:324` `cd_wnd(2) =  28.0`; `sfincs_input.f90:325` `cd_wnd(3) =  50.0`; `sfincs_input.f90:326` `cd_val(1) = 0.0010`; `sfincs_input.f90:327` `cd_val(2) = 0.0025`; `sfincs_input.f90:328` `cd_val(3) = 0.0015`
cdnrb를 직접 지정하면 cdwnd·cdval도 함께 지정해야 문서의 기본 곡선을 재현할 수 있다. `sfincs_input.f90:334` `call read_real_array_input(500,'cdwnd',cd_wnd,0.0,cd_nr)`; `sfincs_input.f90:335` `call read_real_array_input(500,'cdval',cd_val,0.0,cd_nr)`


### 1.5 출력 제어 (`§Parameters for model output`)

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `tref` | 읽기 `none`; 생략 시 `tstart` | - | SFINCS의 tref를 생략하면 코드는 tstart를 기준 날짜로 사용한다. `sfincs_input.f90:57` `call read_char_input(500,'tref',trefstr,'none')`; `sfincs_input.f90:354` `if (trefstr(1:4) == 'none') then`; `sfincs_input.f90:356` `trefstr = tstartstr`<br>tstart의 읽기 기본값은 20000101 000000이다. `sfincs_input.f90:58` `call read_char_input(500,'tstart',tstartstr,'20000101 000000')`<br>통합 SnapWave의 별도 시간 변수 리더는 같은 이름에 고정 날짜 기본값을 사용한다. `sfincs_snapwave.f90:684` `call read_char_input(500, 'tref', trefstr, '20000101 000000')   ! Read again > needed in sfincs_ncinput.F90`<br>두 시간 변수의 입력 문맥을 구분한다. `sfincs_input.f90:57` `call read_char_input(500,'tref',trefstr,'none')`; `sfincs_snapwave.f90:684` `call read_char_input(500, 'tref', trefstr, '20000101 000000')   ! Read again > needed in sfincs_ncinput.F90` |
| `tstart` | `20000101 000000` | - | 시작일 |
| `tstop` | `20000101 000000` | - | 종료일 |
| `dtout` | 0 | s | spatial map 출력 간격 |
| `dthisout` | 600 | s | 관측점 출력 간격 |
| `dtmaxout` | 9999999 | s | 최대값 map 출력 간격 (0=출력안함) |
| `dtrstout` | 0 | s | restart 파일 출력 간격 |
| `trstout` | -999.0 | s | tref 이후 특정 시각 restart 출력 |
| `dtwnd` | 1800 | s | 공간변동 meteo 갱신 간격 (spw·강우·기압·바람) |
| `outputformat` | net | - | bin/asc/net (map=`sfincs_map.nc`, point=`sfincs_his.nc`) |
| `outputtype_map` | 읽기 `nil`; 조건부 `outputformat` | - | map 전용 입력 이름은 outputtype_map이다. `sfincs_input.f90:86` `call read_char_input(500,'outputtype_map',outputtype_map,'nil')`<br>두 리더의 기본값은 nil이다. `sfincs_input.f90:86` `call read_char_input(500,'outputtype_map',outputtype_map,'nil')`; `sfincs_input.f90:87` `call read_char_input(500,'outputtype_his',outputtype_his,'nil')`<br>둘 중 하나라도 nil이면 코드가 두 값을 모두 outputformat으로 설정한다. `sfincs_input.f90:532` `if ((outputtype_map == 'nil') .OR. (outputtype_his == 'nil')) then`; `sfincs_input.f90:533` `outputtype_map = outputtype`; `sfincs_input.f90:534` `outputtype_his = outputtype`<br>개별 출력 형식을 지정하려면 두 입력 이름을 함께 확인해야 한다. `sfincs_input.f90:86` `call read_char_input(500,'outputtype_map',outputtype_map,'nil')`; `sfincs_input.f90:87` `call read_char_input(500,'outputtype_his',outputtype_his,'nil')`; `sfincs_input.f90:532` `if ((outputtype_map == 'nil') .OR. (outputtype_his == 'nil')) then` |
| `outputtype_his` | 읽기 `nil`; 조건부 `outputformat` | - | his 전용 입력 이름은 outputtype_his이다. `sfincs_input.f90:87` `call read_char_input(500,'outputtype_his',outputtype_his,'nil')`<br>두 리더의 기본값은 nil이다. `sfincs_input.f90:86` `call read_char_input(500,'outputtype_map',outputtype_map,'nil')`; `sfincs_input.f90:87` `call read_char_input(500,'outputtype_his',outputtype_his,'nil')`<br>둘 중 하나라도 nil이면 코드가 두 값을 모두 outputformat으로 설정한다. `sfincs_input.f90:532` `if ((outputtype_map == 'nil') .OR. (outputtype_his == 'nil')) then`; `sfincs_input.f90:533` `outputtype_map = outputtype`; `sfincs_input.f90:534` `outputtype_his = outputtype`<br>개별 출력 형식을 지정하려면 두 입력 이름을 함께 확인해야 한다. `sfincs_input.f90:86` `call read_char_input(500,'outputtype_map',outputtype_map,'nil')`; `sfincs_input.f90:87` `call read_char_input(500,'outputtype_his',outputtype_his,'nil')`; `sfincs_input.f90:532` `if ((outputtype_map == 'nil') .OR. (outputtype_his == 'nil')) then` |
| `nc_deflate_level` | 2 | - | netcdf deflate level |
| `percentage_done` | 5 | integer | percentage_done의 읽기 기본값은 5이다. `sfincs_input.f90:301` `call read_int_input(500,'percentage_done',percdoneval,5)`<br>코드는 입력값을 0..100으로 제한한다. `sfincs_input.f90:303` `percdoneval = max(min(percdoneval,100), 0)`<br>문서 parameters.rst의 최소값 1과 코드의 하한 0이 다르다. `sfincs_input.f90:303` `percdoneval = max(min(percdoneval,100), 0)`; `docs/parameters.rst:432` `:min:			1`; `docs/parameters.rst:433` `:max:			100` |

**저장 플래그 (1=활성):** `storetwet`(wet 지속시간; `twet_threshold` 기본 0.01 m), `storevel`(dtout 유속), `storevelmax`/`storefluxmax`(dtmaxout 최대 유속·flux), `storecumprcp`(누적강우), `storehsubgrid`(subgrid hmax = zsmax−z_zmin; HydroMT downscaling 권장), `storehmean`(subgrid 평균수심 hmax; storehsubgrid=1 일 때만), `storeqdrain`(배수방류), `storezvolume`/`storestoragevolume`(subgrid 부피), `storemeteo`(meteo 입력), `storemaxwind`(최대풍속), `storetzsmax`(zsmax 발생시각; dtmaxout>0 일 때만), `debug`(매 timestep), `timestep_analysis`(timestep 제한 셀 진단).

열거한 저장 플래그 중 storeqdrain의 읽기 기본값은 1이다. `sfincs_input.f90:289` `call read_int_input(500,'storeqdrain',storeqdrain,1)`
다른 열거 플래그의 읽기 기본값은 0 또는 false이다. `sfincs_input.f90:281` `call read_int_input(500,'storetwet',storetwet,0)`<br>`sfincs_continuity.f90:696` `if (store_twet) then`<br>`sfincs_continuity.f90:699` `if ( (zs(nm) - subgrid_z_zmin(nm)) > twet_threshold) then`<br>`sfincs_continuity.f90:700` `twet(nm) = twet(nm) + dt`<br>`sfincs_continuity.f90:705` `if ( (zs(nm) - zb(nm)) > twet_threshold) then`<br>`sfincs_continuity.f90:707` `twet(nm) = twet(nm) + dt`; `sfincs_input.f90:279` `call read_int_input(500,'storevel',storevel,0)`<br>`sfincs_input.f90:464` `store_velocity = .false.`<br>`sfincs_input.f90:465` `if (storevel==1) then`<br>`sfincs_input.f90:466` `store_velocity = .true.`; `sfincs_input.f90:277` `call read_int_input(500,'storevelmax',storevelmax,0)`<br>`sfincs_input.f90:454` `store_maximum_velocity = .false.`<br>`sfincs_input.f90:455` `if (storevelmax==1 .and. dtmaxout>0.0) then`<br>`sfincs_input.f90:456` `store_maximum_velocity = .true.`; `sfincs_input.f90:278` `call read_int_input(500,'storefluxmax',storefluxmax,0)`<br>`sfincs_continuity.f90:689` `if (store_maximum_flux) then`<br>`sfincs_continuity.f90:691` `qmax(nm) = max(qmax(nm), qz)`; `sfincs_input.f90:280` `call read_int_input(500,'storecumprcp',storecumprcp,0)`<br>`sfincs_input.f90:511` `store_cumulative_precipitation = .false.`<br>`sfincs_input.f90:512` `if (storecumprcp==1) then`<br>`sfincs_input.f90:513` `store_cumulative_precipitation = .true.`; `sfincs_input.f90:283` `call read_int_input(500,'storehsubgrid',storehsubgrid,0)`<br>`sfincs_ncoutput.F90:3537` `if (subgrid .eqv. .false. .or. store_hsubgrid .eqv. .true.) then`<br>`sfincs_ncoutput.F90:3541` `if (store_hmean .and. subgrid .eqv. .true.) then`<br>`sfincs_ncoutput.F90:3547` `call compute_subgrid_mean_depth(zsmax, hmean)`<br>`sfincs_ncoutput.F90:3559` `if (store_hmean) then`<br>`sfincs_ncoutput.F90:3563` `zstmp(m, n) = hmean(nm)`; `sfincs_input.f90:284` `call read_logical_input(500, 'storehmean', store_hmean, .false.)`<br>`sfincs_ncoutput.F90:3537` `if (subgrid .eqv. .false. .or. store_hsubgrid .eqv. .true.) then`<br>`sfincs_ncoutput.F90:3541` `if (store_hmean .and. subgrid .eqv. .true.) then`<br>`sfincs_ncoutput.F90:3547` `call compute_subgrid_mean_depth(zsmax, hmean)`<br>`sfincs_ncoutput.F90:3559` `if (store_hmean) then`<br>`sfincs_ncoutput.F90:3563` `zstmp(m, n) = hmean(nm)`; `sfincs_input.f90:290` `call read_int_input(500,'storezvolume',storezvolume,0)`<br>`sfincs_input.f90:579` `if (subgrid) then`<br>`sfincs_input.f90:580` `if (storezvolume==1) then`<br>`sfincs_input.f90:581` `store_zvolume = .true.`; `sfincs_input.f90:291` `call read_int_input(500,'storestoragevolume',storestoragevolume,0)`<br>`sfincs_input.f90:655` `if (volfile(1:4) /= 'none') then`<br>`sfincs_input.f90:656` `if (subgrid) then`<br>`sfincs_input.f90:657` `use_storage_volume = .true.`<br>`sfincs_input.f90:659` `if (storestoragevolume==1) then`<br>`sfincs_input.f90:660` `store_storagevolume = .true.`<br>`sfincs_input.f90:664` `call write_log('Warning : storage volume only supported for subgrid topographies!', 1)`; `sfincs_input.f90:294` `call read_int_input(500,'storemeteo',storemeteo,0)`<br>`sfincs_input.f90:472` `if (storemeteo==1) then`<br>`sfincs_input.f90:473` `store_meteo = .true.`<br>`sfincs_input.f90:475` `if (iwindmax==1) then`<br>`sfincs_input.f90:476` `store_wind_max = .true.`; `sfincs_input.f90:295` `call read_int_input(500,'storemaxwind',iwindmax,0)`<br>`sfincs_input.f90:472` `if (storemeteo==1) then`<br>`sfincs_input.f90:473` `store_meteo = .true.`<br>`sfincs_input.f90:475` `if (iwindmax==1) then`<br>`sfincs_input.f90:476` `store_wind_max = .true.`; `sfincs_input.f90:282` `call read_int_input(500,'storetzsmax',storetzsmax,0)`<br>`sfincs_input.f90:506` `store_t_zsmax = .false.`<br>`sfincs_input.f90:507` `if (storetzsmax==1) then`<br>`sfincs_input.f90:508` `store_t_zsmax = .true.`<br>`sfincs_continuity.f90:600` `if (store_maximum_waterlevel) then`<br>`sfincs_continuity.f90:604` `if (store_t_zsmax) then`<br>`sfincs_continuity.f90:607` `t_zsmax(nm) = t`; `sfincs_input.f90:288` `call read_logical_input(500,'timestep_analysis',timestep_analysis,.false.)`<br>`sfincs_lib.f90:586` `if (timestep_analysis) then`<br>`sfincs_lib.f90:588` `call timestep_analysis_update(min_dt)`<br>`sfincs_lib.f90:696` `if (timestep_analysis) then`<br>`sfincs_lib.f90:698` `call timestep_analysis_finalize(nt)`; `sfincs_input.f90:293` `call read_logical_input(500,'debug',debug,.false.)`<br>`sfincs_lib.f90:479` `if (debug .and. t >= t0out) then`<br>`sfincs_lib.f90:483` `tout = t`
qdrain.txt 출력은 store_qdrain을 검사한다. `sfincs_output.f90:660` `if (ndrn>0 .and. store_qdrain) then`; `sfincs_output.f90:663` `write(970,'(f12.1,10000f9.3)')t,(qtsrc(iobs), iobs = nsrc + 1, nsrcdrn, 2)`
NetCDF 배수 이력 출력은 ndrn>0만 검사한다. `sfincs_ncoutput.F90:2206` `if (ndrn>0) then`; `sfincs_ncoutput.F90:2208` `NF90(nf90_def_var(his_file%ncid, 'drainage_discharge', NF90_FLOAT, (/his_file%drain_dimid, his_file%time_dimid/), his_file%drain_varid)) ! time-varying discharge through drainage structure`
storemaxwind=1은 storemeteo=1일 때 최대 풍속 저장을 켠다. `sfincs_input.f90:472` `if (storemeteo==1) then`; `sfincs_input.f90:475` `if (iwindmax==1) then`; `sfincs_input.f90:476` `store_wind_max = .true.`

`timestep_analysis=1`의 출력 변수는 `sfincs_map.nc`의 `average_required_timestep`과 `percentage_limiting_timestep`이다 (`docs/input.rst §Timestep analysis`).

average_required_timestep은 각 면의 젖은 단계 요구 시간 간격을 산술평균한다. `sfincs_timestep_analysis.f90:51` `timestep_analysis_average_required_timestep(ip) = timestep_analysis_average_required_timestep(ip) + timestep_analysis_required_timestep(ip)`; `sfincs_timestep_analysis.f90:55` `timestep_analysis_times_wet(ip) = timestep_analysis_times_wet(ip) + 1`
코드는 주변 유효 면 평균의 최솟값에 alpha를 곱한다. `sfincs_timestep_analysis.f90:124` `dtm = min(dtm, timestep_analysis_average_required_timestep(nmd1) / max(timestep_analysis_times_wet(nmd1), 1))`; `sfincs_timestep_analysis.f90:182` `timestep_analysis_average_required_timestep_per_cell(nm) = min(dtm * alfa, dtmax)`
코드는 이 값을 dtmax 이하로 제한한다. `sfincs_timestep_analysis.f90:182` `timestep_analysis_average_required_timestep_per_cell(nm) = min(dtm * alfa, dtmax)`
해석: 유효한 건조 면의 0/max(0,1) 경로는 값 0을 만들 수 있다. `sfincs_timestep_analysis.f90:124` `dtm = min(dtm, timestep_analysis_average_required_timestep(nmd1) / max(timestep_analysis_times_wet(nmd1), 1))`
-1은 유효 주변 면이 없어 큰 초기 dtm이 남는 경우에 기록한다. `sfincs_timestep_analysis.f90:188` `timestep_analysis_average_required_timestep_per_cell(nm) = -1.0`
percentage_limiting_timestep은 주변 면별 제한 횟수의 최댓값에 100/nt를 곱한다. `sfincs_timestep_analysis.f90:59` `if (timestep_analysis_required_timestep(ip) <= min_dt + 1.0e-6) then`; `sfincs_timestep_analysis.f90:125` `tmsl = max(tmsl, timestep_analysis_times_limiting(nmd1))`; `sfincs_timestep_analysis.f90:192` `timestep_analysis_percentage_limiting_per_cell(nm) = 100.0 * tmsl / nt`
해석: 이 비율은 주변 면의 제한 단계 집합을 합친 비율과 일반적으로 같지 않다. `sfincs_timestep_analysis.f90:125` `tmsl = max(tmsl, timestep_analysis_times_limiting(nmd1))`; `sfincs_timestep_analysis.f90:192` `timestep_analysis_percentage_limiting_per_cell(nm) = 100.0 * tmsl / nt`

> cross-link: 키워드→코드 매핑은 [[../source-analysis/sfincs_io_data]] 참조.

---

## 2. 도메인 입력파일 (`docs/parameters.rst §Input files / Domain`, `docs/input.rst §Domain`)

| 파일 (키워드=기본명) | 필수 | 포맷 | 설명 |
|---|---|---|---|
| `sfincs.inp` | yes | asc | 메인 입력파일 (설정·도메인·forcing·구조물) |
| `depfile = sfincs.dep` | regular=yes / subgrid=no | bin/asc | 셀중심 표고 (지형+, 수심−, m above ref) |
| `mskfile = sfincs.msk` | yes | bin/asc | 마스크: 0=비활성, 1=활성, 2=수위경계, 3=outflow 경계 |
| `indexfile = sfincs.ind` | `inputformat=bin` 시만 | bin | 활성 격자 인덱스 (ascii 입력시 미사용) |
| `manningfile = sfincs.man` | no (subgrid 무시) | bin | 셀별 manning 조도 |
| `qinffile = sfincs.qinf` | no | bin | 셀별 시간일정 infiltration |
| `scsfile = sfincs.scs` | no | bin | Curve Number 방법 A (회복없음) max 토양수분저장 (inch) |
| `smaxfile / sefffile / ksfile` | no | bin | CN 방법 B (회복): max 저장(m) / 시작저장(m) / 포화수리전도도(mm/hr) |
| `ksfile / sigmafile / psifile` | no | bin | ksfile은 포화 수리전도도를 mm/hr로 담는다. `sfincs_input.f90:256` `call read_char_input(500,'ksfile',ksfile,'none')             ! saturated hydraulic conductivity [mm/hr]`; `docs/input.rst:503` `* ksfile: saturated hydraulic conductivity in mm/hr`; `sfincs_infiltration.f90:494` `ksfield    = ksfield / 1000 / 3600           ! from mm/hr to m/s`<br>sigmafile은 최대 수분 부족량을 무차원 값으로 담는다. `sfincs_input.f90:255` `call read_char_input(500,'sigmafile',sigmafile,'none')       ! maximum moisture deficit θdmax [-]`; `docs/input.rst:504` `* sigmafile: soil moisture deficit in [-]`; `sfincs_infiltration.f90:440` `read(501)GA_sigma_max`<br>psifile은 습윤 전선의 흡입수두를 mm로 담는다. `sfincs_input.f90:254` `call read_char_input(500,'psifile',psifile,'none')           ! suction head [mm]`; `docs/input.rst:505` `* psifile: suction head at the wetting front in mm`; `sfincs_infiltration.f90:416` `read(500)GA_head`; `sfincs_infiltration.f90:492` `GA_head    = GA_head / 1000                  ! from mm to m`<br>parameters.rst의 sigmafile·psifile 설명은 서로 바뀌었다. `sfincs_input.f90:254` `call read_char_input(500,'psifile',psifile,'none')           ! suction head [mm]`; `sfincs_input.f90:255` `call read_char_input(500,'sigmafile',sigmafile,'none')       ! maximum moisture deficit θdmax [-]`; `docs/input.rst:504` `* sigmafile: soil moisture deficit in [-]`; `docs/input.rst:505` `* psifile: suction head at the wetting front in mm` |
| `f0file / fcfile / kdfile` | no | bin | Horton: 초기침투능(mm/hr) / 최소침투율(mm/hr) / 감쇠상수(hr⁻¹) |
| `sbgfile = sfincs.sbg` | subgrid 시만 | net(신)/bin(구) | subgrid table (Van Ormondt et al. 2024, netcdf 권장 2024.01 이후) |
| `obsfile = sfincs.obs` | no | asc | 관측점 (point 출력) |
| `crsfile = sfincs.crs` | no | tekal | cross-section (방류 출력) |
| `volfile = sfincs.vol` | no | bin | 저장용량 옵션은 subgrid에서 사용한다. `sfincs_input.f90:655` `if (volfile(1:4) /= 'none') then`; `sfincs_input.f90:656` `if (subgrid) then`; `sfincs_input.f90:657` `use_storage_volume = .true.`<br>순강수·면 유량의 양의 유입은 남은 저장용량을 먼저 채운다. `sfincs_continuity.f90:503` `if (storage_volume(nm) > 1.0e-6 .and. dvol > 0.0) then`; `sfincs_continuity.f90:513` `storage_volume(nm) = max(dv, 0.0)`; `sfincs_continuity.f90:525` `dvol = 0.0`; `sfincs_continuity.f90:535` `z_volume(nm) = z_volume(nm) + dvol`<br>점 유량은 계산 셀의 z_volume에 직접 들어간다. `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt`<br>점 유량은 저장용량의 우선 저장 분기를 우회한다. `sfincs_continuity.f90:319` `z_volume(nm) = z_volume(nm) + qtsrc(isrc) * dt`; `sfincs_continuity.f90:501` `! If water enters the cell through a point discharge, it will NOT end up in storage volume !`; `sfincs_continuity.f90:503` `if (storage_volume(nm) > 1.0e-6 .and. dvol > 0.0) then` |
| `inifile = sfincs.ini` | no | bin | 셀별 초기수위 (v2.0.0 이후 binary, 구버전 ascii) |
| `rstfile = sfincs.rst` | no | bin | 현재 restart 파일의 유량 배열 이름은 통합 q이다. `sfincs_initial_conditions.F90:195` `! 1: zs, q, uvmean`; `sfincs_initial_conditions.F90:229` `read(500)iniq`<br>현재 restart 파일의 경계 평균 유량 배열 이름은 uvmean이다. `sfincs_initial_conditions.F90:195` `! 1: zs, q, uvmean`; `sfincs_initial_conditions.F90:233` `read(500)uvmean`<br>현재 리더는 type 1·2·4·5·6에서 iniq와 uvmean을 읽는다. `sfincs_initial_conditions.F90:227` `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`; `sfincs_initial_conditions.F90:229` `read(500)iniq`; `sfincs_initial_conditions.F90:233` `read(500)uvmean`<br>type 2의 문서·코드 헤더는 uvmean을 적지 않는다. `sfincs_initial_conditions.F90:196` `! 2: zs, q`; `sfincs_initial_conditions.F90:227` `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`; `sfincs_initial_conditions.F90:233` `read(500)uvmean`<br>type 2 파일의 실제 호환성은 이 코드 대조만으로 확정할 수 없다. `sfincs_initial_conditions.F90:196` `! 2: zs, q`; `sfincs_initial_conditions.F90:227` `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`; `sfincs_initial_conditions.F90:229` `read(500)iniq`; `sfincs_initial_conditions.F90:233` `read(500)uvmean`<br>type 4·5·6은 각각 CN 회복·Green-Ampt·Horton 상태를 추가로 읽는다. `sfincs_initial_conditions.F90:198` `! 4: zs, q, uvmean and cnb infiltration (writing scs_Se)`; `sfincs_initial_conditions.F90:199` `! 5: zs, q, uvmean and gai infiltration (writing GA_sigma & GA_F)`; `sfincs_initial_conditions.F90:200` `! 6: zs, q, uvmean and hor infiltration (writing rain_T1)`; `sfincs_initial_conditions.F90:240` `read(500)scs_Se`; `sfincs_initial_conditions.F90:246` `read(500)GA_sigma`; `sfincs_initial_conditions.F90:248` `read(500)GA_F`; `sfincs_initial_conditions.F90:255` `read(500)rain_T1`<br>코드의 실제 읽기 동작과 주석의 형식 설명을 구분한다. `sfincs_initial_conditions.F90:195` `! 1: zs, q, uvmean`; `sfincs_initial_conditions.F90:196` `! 2: zs, q`; `sfincs_initial_conditions.F90:227` `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`; `sfincs_initial_conditions.F90:229` `read(500)iniq`; `sfincs_initial_conditions.F90:233` `read(500)uvmean` |

**파일 grid 포맷** (depfile 동일 구조, `docs/input.rst §Depth file`):
```
<zb x0,y0> <zb x1,y0>
<zb x0,y1> <zb x1,y1>
```

**msk 값 의미** (`docs/input.rst §Mask file`): 0=비활성(flux 없음), 1=활성(수위·flux 계산), 2=경계(수위 forcing), 3=outflow(수위 비forcing, 수심 인위적 0 유지).

**obsfile** 좌표+이름(작은따옴표, 최대 256자, `docs/input.rst §Observation points`):
```
592727.98 2969420.51 'NOAA_8722548_PGABoulevardBridge,PalmBeach'
```

**crsfile** tekal: 이름 / 점개수 / x y 좌표 (셀당 2점 초과 가능, `docs/input.rst §Cross-sections for discharge output`).

**restart 워크플로** (`docs/input.rst §Restart file`): 1차 run 에서 `dtrstout`/`trstout` 지정 → 2차 run 에서 `rstfile` 지정. 현재 type 1의 배열은 `zs`, 통합 `q`, `uvmean`이다. `sfincs_initial_conditions.F90:195` `! 1: zs, q, uvmean`; `sfincs_initial_conditions.F90:227` `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`; `sfincs_initial_conditions.F90:229` `read(500)iniq`; `sfincs_initial_conditions.F90:233` `read(500)uvmean`

> cross-link: 입력파일 read 루틴은 [[../source-analysis/sfincs_io_data]] 참조.

---

## 3. Forcing (`docs/parameters.rst §Forcing-*`, `docs/input_forcing.rst`)

### 3.1 수위·파랑 경계 (`§Water levels`, `§Waves`)

| 파일 | 필수 | 포맷 | 설명 |
|---|---|---|---|
| `bndfile = sfincs.bnd` | 수위·파랑 시만 | asc | 경계 입력위치 (msk=2 셀에 forcing); 2개 최근접 위치 가중평균 보간 |
| `bzsfile = sfincs.bzs` | 수위 시만 | asc | 위치별 (느린) 수위 시계열, time(s) since `tref` |
| `bzifile = sfincs.bzi` | 파랑 시만 | asc | 입사파 빠른 수위성분 (bzs 평균수위 기준, IG/단파); **bzs 와 시간스텝 동일** |
| `netbndbzsbzifile = sfincs_netbndbzsbzifile.nc` | netcdf 시만 | net | bnd+bzs(+bzi) 통합 FEWS netcdf |

파랑 forcing 시 입사 성분만 prescribe (반사는 SFINCS 내부 계산), 신호는 0 주변, 보통 초 단위 고빈도 (`docs/input_forcing.rst §Waves`). netcdf 변수: `x,y,time,zs,zi,stations`, time UNIT `"minutes since 1970-01-01 00:00:00.0 +0000"`.

**bzsfile 포맷:**
```
<time1> <zs1 bnd1> <zs1 bnd2>
0    0.50  0.75
3600 0.60  0.80
```

### 3.2 방류 (`§Discharges`)

| 파일 | 포맷 | 설명 |
|---|---|---|
| `srcfile = sfincs.src` | asc | 방류 입력위치 |
| `disfile = sfincs.dis` | asc | 위치별 방류 시계열 (m³/s), time(s) since tref |
| `netsrcdisfile = sfincs_netsrcdisfile.nc` | net | src+dis 통합 FEWS netcdf (변수 `x,y,time,discharge,stations`) |

### 3.3 Meteo (`§Forcing - Meteo`, `docs/input_forcing.rst §Meteo`)

Meteo 입력 5방식 (`docs/input_forcing.rst §Meteo`): (1) spiderweb 극좌표(열대저기압 바람·기압, 강우도 가능), (2) Delft3D gridded(amu/amv/ampr/amp), (3) FEWS netcdf gridded, (4) 공간균일, (5) 혼합.

| 파일 | 포맷 | 단위 | 설명 |
|---|---|---|---|
| `spwfile = sfincs.spw` | asc | m/s, deg, Pa(, mm/hr) | ASCII spwfile은 풍속·풍향·기압 저하량을 입력한다. `sfincs_meteo.f90:63` `call read_spw_file(spwfile,spw_nt,spw_nrows,spw_ncols,spw_radius,spw_times,spw_xe,spw_ye,spw_vmag,spw_vdir,spw_pdrp,spw_prcp,spw_nquant,trefstr)`<br>코드는 ASCII 기압 저하량을 기준 기압에서 빼서 절대기압으로 바꾼다. `sfincs_meteo.f90:67` `spw_pabs = gapres - spw_pdrp` |
| `netspwfile = spiderweb.nc` | net | m/s (바람 성분), Pa (절대기압), mm/hr (강수) | NetCDF netspwfile은 wind_x·wind_y 성분과 절대기압 pressure를 입력한다. `sfincs_ncinput.F90:966` `NF90(nf90_inq_varid(net_file_spw%ncid, "wind_x",            net_file_spw%wind_x_varid) )`; `sfincs_ncinput.F90:967` `NF90(nf90_inq_varid(net_file_spw%ncid, "wind_y",            net_file_spw%wind_y_varid) )`; `sfincs_ncinput.F90:968` `NF90(nf90_inq_varid(net_file_spw%ncid, "pressure",          net_file_spw%pressure_varid) )   ! Note: absolute pressure, not pressure drop`; `sfincs_ncinput.F90:1046` `spw_pabs(it,:,:) = ampr_prtmp(1,:,:)`<br>NetCDF precipitation은 별도 강수 변수이다. `sfincs_ncinput.F90:972` `status = NF90_INQ_VARID(net_file_spw%ncid, "precipitation", net_file_spw%precip_varid)`<br>developments.rst:229의 precipitation 표기는 pressure 대상의 오자로 해석한다. `sfincs_ncinput.F90:968` `NF90(nf90_inq_varid(net_file_spw%ncid, "pressure",          net_file_spw%pressure_varid) )   ! Note: absolute pressure, not pressure drop`; `sfincs_ncinput.F90:972` `status = NF90_INQ_VARID(net_file_spw%ncid, "precipitation", net_file_spw%precip_varid)`; `docs/developments.rst:229` `* netspwfile input for precipitation should be absolute atmospheric pressure, not the pressure drop.` |
| `amufile = sfincs.amu` | asc | m/s | Delft3D x-방향 풍속 (`quantity1=x_wind`) |
| `amvfile = sfincs.amv` | asc | m/s | Delft3D y-방향 풍속 (`quantity1=y_wind`) |
| `ampfile = sfincs.amp` | asc | Pa | Delft3D 기압 (`quantity1=air_pressure`) |
| `amprfile = sfincs.ampr` | asc | mm/hr | Delft3D 강우강도 (`quantity1=precipitation`) |
| `wndfile = sfincs.wnd` | asc | m/s, deg | 공간균일 바람 (vmag, vdir 항해방위=바람불어오는 방향) |
| `precipfile = sfincs.prcp` | asc | mm/hr | 공간균일 강우 |
| `netamuamvfile = sfincs_netamuamvfile.nc` | net | m/s | FEWS 바람 x&y |
| `netampfile = sfincs_netampfile.nc` | net | Pa | FEWS 기압 |
| `netamprfile = sfincs_netamprfile.nc` | net | mm/hr | FEWS 강우 |

Delft3D-meteo ascii 는 **13줄 헤더** 필수 (`FileVersion`~`NODATA_value`, 파일당 1 quantity, `docs/input_forcing.rst §Spatially varying gridded`). spiderweb lat&lon 은 `utmzone` 로 SFINCS 내부 변환. WES 도구로 spiderweb 생성.

> cross-link: 경계·forcing read 및 적용은 [[../source-analysis/sfincs_boundaries_forcing]] 참조.

---

## 4. 구조물 (`docs/parameters.rst §Structures`, `docs/input_structures.rst`)

| 파일 | 포맷 | 설명 |
|---|---|---|
| `thdfile = sfincs.thd` | asc | thin dam: 셀 flow 완전차단 (무한벽); polyline, 최대 5000점 |
| `weirfile = sfincs.weir` | asc | weir: 높이(levee) 있는 thin dam, 월류 flux 계산. x y z cd (cd≈0.6 권장) |
| `drnfile = sfincs.drn` | asc | drainage pump/culvert/check valve (type 1/2/3) |

**thin dam** polyline 은 격자에 snap (`docs/input_structures.rst §Thin dam`). **weir** snapped 좌표는 v2.0.2 이후 `sfincs_his.nc` 에 `structure_x/y/height`, snap 후 셀당 최대 2 uv점 (`docs/input_structures.rst §Weirs`).

**drnfile 포맷** (`docs/input_structures.rst §Drainage Pumps and Culverts`):
```
<xsnk> <ysnk> <xsrc> <ysrc> <type> <par1> par2 par3 par4 par5
```
- type 1의 par1은 목표 유량이며 단위는 m^3/s이다. `sfincs_discharges.f90:390` `qq = drainage_params(idrn, 1)`
- type 2·3의 par1은 수두차 제곱근에 곱하는 계수이다. `sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `sfincs_discharges.f90:412` `qq = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`
  해석: type 2·3의 par1 단위는 m^(5/2)/s이다. `sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `sfincs_discharges.f90:412` `qq = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `docs/input_structures.rst:207` ``` ``par1 = \(\mu \cdot A \cdot \sqrt{2g}\)`` ```
- type 3은 취수점 수위가 배출점 수위보다 높을 때 같은 계수로 단방향 유량을 계산한다. `sfincs_discharges.f90:412` `qq = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `sfincs_discharges.f90:267` `nmq = find_quadtree_cell(xsnk(idrn), ysnk(idrn))`; `sfincs_discharges.f90:279` `nmq = find_quadtree_cell(xsrc(idrn), ysrc(idrn))`; `sfincs_discharges.f90:647` `qtsrc(jin)  = -qq`; `sfincs_discharges.f90:648` `qtsrc(jout) = qq`

입력의 첫 좌표 쌍은 취수점이다. `sfincs_discharges.f90:238` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1)`; `sfincs_discharges.f90:267` `nmq = find_quadtree_cell(xsnk(idrn), ysnk(idrn))`; `sfincs_discharges.f90:647` `qtsrc(jin)  = -qq`
입력의 두 번째 좌표 쌍은 배출점이다. `sfincs_discharges.f90:238` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1)`; `sfincs_discharges.f90:279` `nmq = find_quadtree_cell(xsrc(idrn), ysrc(idrn))`; `sfincs_discharges.f90:648` `qtsrc(jout) = qq`
type 1..3은 par1만 읽는다. `sfincs_discharges.f90:238` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1)`
type 4..5는 움직이는 수문의 par1..par6을 읽는다. `sfincs_discharges.f90:244` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1), drainage_params(idrn,2), drainage_params(idrn,3), drainage_params(idrn,4), drainage_params(idrn,5), drainage_params(idrn,6)`; `sfincs_discharges.f90:428` `wdt   = drainage_params(idrn, 1)                        ! width`; `sfincs_discharges.f90:433` `tcls  = drainage_params(idrn, 6)                        ! closing time (seconds)`; `sfincs_discharges.f90:531` `tclose = drainage_params(idrn, 4)                       ! time wrt tref for closing gate`; `sfincs_discharges.f90:533` `tcls  = drainage_params(idrn, 6)                        ! closing time (seconds)`


culvert 방류용량:

$$par1 = \mu \cdot A \cdot \sqrt{2g}$$

해석: type 2·3의 `par1` 단위는 m^(5/2)/s이다. `sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `sfincs_discharges.f90:412` `qq = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`; `docs/input_structures.rst:207` ``` ``par1 = \(\mu \cdot A \cdot \sqrt{2g}\)`` ```


($\mu$=손실계수 0~1, $A$=개구면적 m², $g$=9.81 m/s²; Bernoulli 유도, `docs/input_structures.rst §Drainage Pumps and Culverts`).

par2..par5의 자리표시자 설명은 type 1..3에만 적용한다. `sfincs_discharges.f90:238` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1)`; `sfincs_discharges.f90:244` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1), drainage_params(idrn,2), drainage_params(idrn,3), drainage_params(idrn,4), drainage_params(idrn,5), drainage_params(idrn,6)`
Darcy–Weisbach 계산은 문서가 적은 미래 계획이다. `docs/input_structures.rst:222` `Future updates will incorporate the Darcy–Weisbach equation for more accurate discharge estimates by considering frictional and minor losses along the culvert length, which is particularly useful for longer or rougher conduits.`
qdrain.txt 출력은 store_qdrain을 검사한다. `sfincs_output.f90:660` `if (ndrn>0 .and. store_qdrain) then`; `sfincs_output.f90:663` `write(970,'(f12.1,10000f9.3)')t,(qtsrc(iobs), iobs = nsrc + 1, nsrcdrn, 2)`
NetCDF 배수 이력 출력은 ndrn>0만 검사한다. `sfincs_ncoutput.F90:2206` `if (ndrn>0) then`; `sfincs_ncoutput.F90:2208` `NF90(nf90_def_var(his_file%ncid, 'drainage_discharge', NF90_FLOAT, (/his_file%drain_dimid, his_file%time_dimid/), his_file%drain_varid)) ! time-varying discharge through drainage structure`
배수 이력은 출력 시각의 qtsrc를 기록한다. `sfincs_ncoutput.F90:3467` `q_drain(idrn) = qtsrc(iobs)`; `sfincs_ncoutput.F90:3470` `NF90(nf90_put_var(his_file%ncid, his_file%drain_varid, q_drain, (/1, nthisout/))) ! write discharge of sink point`
배수 이력은 dthisout 구간의 최대 유량을 모으지 않는다. `sfincs_ncoutput.F90:3467` `q_drain(idrn) = qtsrc(iobs)`; `sfincs_ncoutput.F90:3470` `NF90(nf90_put_var(his_file%ncid, his_file%drain_varid, q_drain, (/1, nthisout/))) ! write discharge of sink point`

> cross-link: 구조물 물리 구현은 [[../source-analysis/sfincs_structures_physics]] 참조.

---

## 5. Output (`docs/output.rst`)

### 5.1 global map `sfincs_map.nc` (`§Parameters netcdf file global (sfincs_map.nc)`)

| 변수 | standard_name | 단위 | 설명 |
|---|---|---|---|
| `x`,`y` | projection_x/y_coordinate | m | 셀중심 좌표 |
| `zb` | altitude | m above ref | bed level (subgrid 시 미사용, sbgfile 사용) |
| `msk` | land_binary_mask | - | 마스크 |
| `time`/`timemax` | time | s since tref | dtout / dtmaxout 출력시각 |
| `zs` | sea_surface_height_above_mean_sea_level | m above ref | 순간 수위 (dtout) |
| `h` | depth | m | 순간 수심 (dtout) |
| `u`,`v` | sea_water_x/y_velocity | m/s | 순간 유속 (dtout) |
| `subgrid_volume` | subgrid_volume_in_cell | m³ | subgrid 부피 |
| `storage_volume` | storage_volume_in_cell | m³ | storage 부피 |
| `zsmax` | max sea_surface_height... | m above ref | 최대수위 (dtmaxout>0 시) |
| `t_zsmax` | (동) | m above ref | 셀별 최대수위 발생시각 (dtmaxout>0) |
| `vmax` | maximum_flow_velocity | m/s | 최대유속 proxy (dtmaxout>0) |
| `qmax` | maximum_flux | m²/s | 최대 flux proxy (dtmaxout>0) |
| `cuminf` | - | m | 전체 누적 침투깊이 |
| `cumprcp` | - | m | 전체 누적 강우깊이 |
| `inp` | - | - | sfincs.inp 입력 전체 복사본 |
| `total_runtime` | - | s | 총 runtime |
| `average_dt` | - | s | 평균 timestep |

### 5.2 관측점 `sfincs_his.nc` (`§Parameters netcdf file observation points (sfincs_his.nc)`)

obsfile 지정 시 또는 weir/cross-section 지정 시만 생성. 주요 변수: `point_x/y`(보간 위치), `station_x/y`(지정 위치), `point_zb`, `point_zs`(수위), `point_h`(수심), `point_u/v`, `point_uvmag`(절대유속), `point_uvdir`(방향, deg wrt north), `point_prcp`, `point_qinf`, `crosssection_discharge`(m³/s), `drainage_discharge`(m³/s). weir/thin dam snap 좌표: `structure_x/y/height`, `thindam_x/y`. 시계열 간격 = `dthisout`.

배수 이력은 출력 시각의 qtsrc를 기록한다. `sfincs_ncoutput.F90:3467` `q_drain(idrn) = qtsrc(iobs)`; `sfincs_ncoutput.F90:3470` `NF90(nf90_put_var(his_file%ncid, his_file%drain_varid, q_drain, (/1, nthisout/))) ! write discharge of sink point`
배수 이력은 dthisout 구간의 최대 유량을 모으지 않는다. `sfincs_ncoutput.F90:3467` `q_drain(idrn) = qtsrc(iobs)`; `sfincs_ncoutput.F90:3470` `NF90(nf90_put_var(his_file%ncid, his_file%drain_varid, q_drain, (/1, nthisout/))) ! write discharge of sink point`


### 5.3 화면 메시지 (`§Output messages`)

초기화 완료 = `Starting computation ...`, 계산시작 = `0% complete`, 정상종료 = `---Simulation is finished---` (총 runtime·구간별 시간·평균 timestep·최대수심 출력). OpenMP 로 가용 코어 사용 → 병렬 다중 run 비권장, 직렬 권장.

현재 중단 조건은 dtchk<dtmin이며 nt>1이다. `sfincs_lib.f90:634` `if (dtchk < dtmin .and. nt > 1) then`
현재 중단 메시지는 최소 시간 간격과 uvmax 초과를 적는다. `sfincs_lib.f90:638` `write(error_message,'(a,f0.4,a,f0.1,a)')'Error! Minimum time step of ', dtmin, ' s reached ! Current velocity exceeded uvmax ', uvmax, ' m/s. Simulation stopped.'`

해결: `alpha` 낮춤·`hmin_cfl` 상향·`dtmax` 하향·`advlim` 등. forcing 인식 메시지 예: `Turning on process: Precipitation` (키워드/인자 사이 **공백만** 사용, tab 혼용 금지).

---

## 6. 파랑 (SnapWave) (`docs/waves.rst`)

`docs/waves.rst §Introduction` 기준 — 경계조건으로서의 파랑 입력은 **work in progress** 이며, 다음 파일들은 **사용하지 말 것**으로 명시: `bwvfile`, `bhsfile`, `btpfile`, `cstfile` (모두 빈 값).

> 주의: 공식 docs RST 에는 SnapWave 설정 키워드 reference 가 정리되어 있지 않다. 단파/IG 파랑 forcing 의 현행 경로는 §3.1 의 `bzifile`(입사파 빠른 수위성분). SnapWave 커널 자체의 설정·구현은 docs 가 아닌 소스 분석 [[../source-analysis/sfincs_snapwave]] 에서 다룬다.

---

## 문서와 코드가 다른 매개변수

| 키워드 | 문서 docs/파일:줄과 원문 | 코드 파일:줄과 원문 | 차이 |
|---|---|---|---|
| A013<br>`huthresh` | `docs/parameters.rst:81` `huthresh`<br>`docs/parameters.rst:82` `:description:		Minimum flow depth limiter.`<br>`docs/parameters.rst:83` `:units:		m`<br>`docs/parameters.rst:84` `:default:		0.05`<br>`docs/parameters.rst:85` `:min:			0.001 (recommended)`<br>`docs/parameters.rst:86` `:max:			0.1 (recommended)` | `sfincs_input.f90:80` `call read_real_input(500,'huthresh',huthresh,0.05)`<br>`sfincs_subgrid.F90:34` `if (net_file_sbg%ncid > 0) then`<br>`sfincs_subgrid.F90:40` `huthresh = 0.0`<br>`sfincs_subgrid.F90:42` `call read_subgrid_file_netcdf()` | 확인: 읽기 기본값은 0.05 m이다. 확인: NetCDF subgrid 분기는 실효 huthresh를 0.0으로 덮어쓴다. 문서는 이 예외를 적지 않는다. |
| A017<br>`viscosity` | `docs/parameters.rst:105` `viscosity`<br>`docs/parameters.rst:106` `:description:		Turns on the viscosity term in the momentum equation (viscosity = 1), advised to combine with theta = 1.0.`<br>`docs/parameters.rst:107` `:units:		-`<br>`docs/parameters.rst:108` `:default:		1`<br>`docs/parameters.rst:109` `:min:			0`<br>`docs/parameters.rst:110` `:max:			1`<br>`docs/input.rst:838` `'viscosity' turns on the viscosity term in the momentum equation (viscosity = 1).`<br>`docs/input.rst:848` `viscosity 	= 1` | `sfincs_input.f90:111` `call read_logical_input(500,'viscosity',iviscosity,.false.)`<br>`sfincs_input.f90:590` `viscosity = .false.`<br>`sfincs_input.f90:591` `if (iviscosity) then`<br>`sfincs_input.f90:592` `viscosity = .true.` | 확인: 문서 기본값은 1이다. 확인: 리더 기본값은 .false.이다. 확인: 후처리도 점성을 자동으로 켜지 않는다. |
| A019<br>`nuvisc` | `docs/parameters.rst:114` `nuvisc`<br>`docs/parameters.rst:115` `:description:		Viscosity coefficient 'per meter of grid cell length', used if 'viscosity=1' and multiplied internally with the grid cell size (per quadtree level in quadtree mesh mode).`<br>`docs/parameters.rst:116` `:units:		-`<br>`docs/parameters.rst:117` `:default:		0.01`<br>`docs/parameters.rst:118` `:min:			0.0`<br>`docs/parameters.rst:119` `:max:			Inf` | `sfincs_input.f90:110` `call read_real_input(500,'nuvisc',nuviscdim,0.01)`<br>`sfincs_domain.f90:1565` `nuvisc(iref) = max(nuviscdim * dxyr(iref), 0.0) ! take min of dx and dy, don't allow to be negative`<br>`sfincs_momentum.f90:519` `frc = frc + nuvisc(iref) * hu * ( (uu_nmu - 2*uu_nm + uu_nmd ) * dxuv2inv + (uu_num - 2*uu_nm + uu_ndm ) * dyuv2inv )`<br>`sfincs_momentum.f90:677` `q(ip) = (qsm + frc * dt) / (1.0 + gnavg2 * dt * qfr / hu73)` | 확인: 읽기 기본값 0.01은 대응한다. 확인: 코드는 입력값을 셀 길이에 곱해서 내부 nuvisc를 만든다. 확인: 내부 nuvisc는 속도의 공간 2차 차분에 곱한다. 해석: 내부 nuvisc의 차원은 m^2/s이다. 해석: 입력 nuvisc의 차원은 m/s이다. 문서의 단위 '-'가 이 식의 차원과 맞지 않는다. |
| A029<br>`ampr_block` | `docs/parameters.rst:174` `ampr_block`<br>`docs/parameters.rst:175` `:description:		Keyword controlling whether the input precipitation rate for 2D precipitation input fields is kept constant for the duration of the input time interval (block interpolation, ampr_block = 1, default), or whether it is interpolated linearly in time (ampr_block = 0).`<br>`docs/parameters.rst:176` `:units:		-`<br>`docs/parameters.rst:177` `:default:		1`<br>`docs/parameters.rst:178` `:min:			0`<br>`docs/parameters.rst:179` `:max:			1`<br>`docs/input_forcing.rst:224` `**NOTE - ampr_block - keyword controlling whether the input precipitation rate is kept constant for the duration of the input time interval (block interpolation, ampr_block = 1, default), or whether it is interpolated linearly in time (ampr_block = 0).**` | `sfincs_input.f90:106` `call read_int_input(500,'amprblock',iamprblock,1)`<br>`sfincs_input.f90:537` `ampr_block = .true. ! Default use data in ampr file as block rather than linear interpolation`<br>`sfincs_input.f90:538` `if (iamprblock==0) then`<br>`sfincs_input.f90:539` `ampr_block = .false.`<br>`sfincs_meteo.f90:1142` `if (ampr_block) then`<br>`sfincs_meteo.f90:1146` `twfac  = 0.0` | 확인: 활성 입력 이름은 amprblock이다. 확인: ampr_block은 내부 논리 변수 이름이다. 확인: 기본값과 블록 보간 의미는 대응한다. |
| A038<br>`huvmin` | `docs/parameters.rst:233` `huvmin - added from SFINCS v2.3.1 onwards`<br>`docs/parameters.rst:234` `:description:		Minimum depth for calculating velocity (uv = q / max(hu, huvmin), used for output and advection`<br>`docs/parameters.rst:235` `:units:		-`<br>`docs/parameters.rst:236` `:default:		0.0`<br>`docs/parameters.rst:237` `:min:			0.0`<br>`docs/parameters.rst:238` `:max:			9999.9`<br>`docs/developments.rst:53` `* Added input variable 'huvmin', minimum depth for calculating velocity (uv = q / max(hu, huvmin)), used for output and advection.` | `sfincs_input.f90:81` `call read_real_input(500,'huvmin', huvmin, 0.0)                   ! Minimum depth for calculating velocity (uv = q / max(hu, huvmin) used for output and advection)`<br>`sfincs_momentum.f90:719` `q(ip) = min(max(q(ip), - hu * uvlim), hu * uvlim)`<br>`sfincs_momentum.f90:724` `uv(ip) = q(ip) / max(hu, huvmin)` | 확인: 기본값 0.0은 대응한다. 해석: max(hu, huvmin)의 두 인자는 같은 수심 단위를 가져야 한다. 해석: huvmin 단위는 m이다. 문서의 단위 '-'가 계산식과 맞지 않는다. |
| A042<br>`spinup_meteo` | `docs/parameters.rst:257` `spinup_meteo`<br>`docs/parameters.rst:258` `:description:		Option to also apply spinup to the meteo forcing, default is off (0)`<br>`docs/parameters.rst:259` `:units:		0`<br>`docs/parameters.rst:260` `:default:		0`<br>`docs/parameters.rst:261` `:min:			0`<br>`docs/parameters.rst:262` `:max:			1` | `sfincs_input.f90:112` `call read_int_input(500,'spinup_meteo', ispinupmeteo, 0)`<br>`sfincs_input.f90:596` `spinup_meteo = .true.`<br>`sfincs_input.f90:597` `if (ispinupmeteo==0) then`<br>`sfincs_input.f90:598` `spinup_meteo = .false.` | 확인: 기본값 0과 켜기 값 1은 대응한다. 확인: 리더가 정수 플래그를 읽는다. 해석: 문서의 :units: 0은 단위 표기의 오자이다. |
| A047<br>`cdwnd` | `docs/parameters.rst:290` `cdwnd`<br>`docs/parameters.rst:291` `:description:		Wind speed break points (including 0)`<br>`docs/parameters.rst:292` `:units:		-`<br>`docs/parameters.rst:293` `:default:		0  28  50`<br>`docs/parameters.rst:294` `:min:			2 values`<br>`docs/parameters.rst:295` `:max:			-` | `sfincs_input.f90:334` `call read_real_array_input(500,'cdwnd',cd_wnd,0.0,cd_nr)`<br>`sfincs_input.f90:323` `cd_wnd(1) =   0.0`<br>`sfincs_input.f90:324` `cd_wnd(2) =  28.0`<br>`sfincs_input.f90:325` `cd_wnd(3) =  50.0`<br>`sfincs_meteo.f90:303` `do iw = 1, 1000`<br>`sfincs_meteo.f90:304` `wnd = iw*0.1`<br>`sfincs_meteo.f90:307` `if (wnd>=cd_wnd(icd) .and. wnd<cd_wnd(icd + 1)) then`<br>`sfincs_meteo.f90:308` `cdval(iw) = cd_val(icd) + (wnd - cd_wnd(icd))*(cd_val(icd + 1) - cd_val(icd))/(cd_wnd(icd + 1) - cd_wnd(icd))` | 확인: 기본 절점 0·28·50은 cdnrb를 생략할 때 대응한다. 해석: 문서의 단위 '-'는 풍속 절점의 m/s와 맞지 않는다. 확인: cdnrb를 직접 지정하면 배열 리더의 누락 기본값은 0.0이다. |
| A049<br>`tref` | `docs/parameters.rst:308` `tref`<br>`docs/parameters.rst:309` `:description:		Reference date in 'yyyymmdd HHMMSS'`<br>`docs/parameters.rst:310` `:units:		-`<br>`docs/parameters.rst:311` `:default:		20000101 000000` | `sfincs_input.f90:57` `call read_char_input(500,'tref',trefstr,'none')`<br>`sfincs_input.f90:354` `if (trefstr(1:4) == 'none') then`<br>`sfincs_input.f90:356` `trefstr = tstartstr`<br>`sfincs_snapwave.f90:684` `call read_char_input(500, 'tref', trefstr, '20000101 000000')   ! Read again > needed in sfincs_ncinput.F90` | 확인: SFINCS 리더 기본값은 none이다. 확인: SFINCS 후처리는 tref를 tstart로 설정한다. 고정 날짜를 일반 기본값으로 적은 문서가 이 조건을 누락한다. 확인: SnapWave 시간 변수의 별도 리더는 고정 날짜를 사용한다. |
| A051<br>`tstop` | `docs/parameters.rst:316` `tstop`<br>`docs/parameters.rst:317` `:description:		Stop date in 'yyyymmdd HHMMSS'`<br>`docs/parameters.rst:318` `:units:		m`<br>`docs/parameters.rst:319` `:default:		20000101 000000` | `sfincs_input.f90:59` `call read_char_input(500,'tstop',tstopstr,'20000101 000000')`<br>`sfincs_input.f90:365` `call time_difference(trefstr,tstartstr,dtsec)  ! time difference in seconds between tstart and tref`<br>`sfincs_input.f90:367` `call time_difference(trefstr,tstopstr,dtsec)`<br>`sfincs_input.f90:368` `t1 = dtsec*1.0 ! time difference in seconds between tstop and tstart` | 확인: 리더가 종료 날짜 문자열을 읽는다. 확인: 기본 날짜는 대응한다. 문서의 단위 m이 날짜 문자열과 맞지 않는다. |
| A059<br>`outputformat_map` | `docs/parameters.rst:350` `outputformat_map`<br>`docs/parameters.rst:351` `:description:		Choice whether the SFINCS model map output is given in binary 'bin', ascii 'asc' or netcdf files 'net' (default is the setting of 'outputformat', which is 'net').`<br>`docs/parameters.rst:352` `:units:		-`<br>`docs/parameters.rst:353` `:default:		net` | `sfincs_input.f90:86` `call read_char_input(500,'outputtype_map',outputtype_map,'nil')`<br>`sfincs_input.f90:532` `if ((outputtype_map == 'nil') .OR. (outputtype_his == 'nil')) then`<br>`sfincs_input.f90:533` `outputtype_map = outputtype`<br>`sfincs_input.f90:534` `outputtype_his = outputtype` | 확인: 활성 키워드는 outputtype_map이다. 확인: 읽기 기본값은 nil이다. 확인: map 또는 his 중 하나라도 nil이면 코드가 둘 다 outputformat으로 덮어쓴다. |
| A060<br>`outputformat_his` | `docs/parameters.rst:354` `outputformat_his`<br>`docs/parameters.rst:355` `:description:		Choice whether the SFINCS model his output is given in binary 'bin', ascii 'asc' or netcdf files 'net' (default is the setting of 'outputformat', which is 'net').`<br>`docs/parameters.rst:356` `:units:		-`<br>`docs/parameters.rst:357` `:default:		net` | `sfincs_input.f90:87` `call read_char_input(500,'outputtype_his',outputtype_his,'nil')`<br>`sfincs_input.f90:532` `if ((outputtype_map == 'nil') .OR. (outputtype_his == 'nil')) then`<br>`sfincs_input.f90:533` `outputtype_map = outputtype`<br>`sfincs_input.f90:534` `outputtype_his = outputtype` | 확인: 활성 키워드는 outputtype_his이다. 확인: 읽기 기본값은 nil이다. 확인: map 또는 his 중 하나라도 nil이면 코드가 둘 다 outputformat으로 덮어쓴다. |
| A070<br>`storeqdrain` | `docs/parameters.rst:396` `storeqdrain`<br>`docs/parameters.rst:397` `:description:		Flag to turn on writing away drainage discharge during simulation (storeqdrain = 1)`<br>`docs/parameters.rst:398` `:units:		-`<br>`docs/parameters.rst:399` `:default:		0` | `sfincs_input.f90:289` `call read_int_input(500,'storeqdrain',storeqdrain,1)`<br>`sfincs_input.f90:516` `if (storeqdrain==0) then`<br>`sfincs_input.f90:517` `store_qdrain = .false.`<br>`sfincs_input.f90:519` `store_qdrain = .true.`<br>`sfincs_output.f90:660` `if (ndrn>0 .and. store_qdrain) then`<br>`sfincs_output.f90:663` `write(970,'(f12.1,10000f9.3)')t,(qtsrc(iobs), iobs = nsrc + 1, nsrcdrn, 2)`<br>`sfincs_ncoutput.F90:2206` `if (ndrn>0) then`<br>`sfincs_ncoutput.F90:2208` `NF90(nf90_def_var(his_file%ncid, 'drainage_discharge', NF90_FLOAT, (/his_file%drain_dimid, his_file%time_dimid/), his_file%drain_varid)) ! time-varying discharge through drainage structure`<br>`sfincs_ncoutput.F90:3459` `if (ndrn>0) then`<br>`sfincs_ncoutput.F90:3467` `q_drain(idrn) = qtsrc(iobs)`<br>`sfincs_ncoutput.F90:3470` `NF90(nf90_put_var(his_file%ncid, his_file%drain_varid, q_drain, (/1, nthisout/))) ! write discharge of sink point` | 확인: 문서 기본값은 0이다. 확인: 리더 기본값은 1이다. 확인: ASCII 이력 출력은 store_qdrain을 검사한다. 확인: NetCDF 이력 출력은 ndrn>0만 검사한다. |
| A074<br>`storemaxwind` | `docs/parameters.rst:412` `storemaxwind`<br>`docs/parameters.rst:413` `:description:		Flag to turn on writing away maximum wind speed during simulation (storemaxwind = 1)`<br>`docs/parameters.rst:414` `:units:		-`<br>`docs/parameters.rst:415` `:default:		0` | `sfincs_input.f90:295` `call read_int_input(500,'storemaxwind',iwindmax,0)`<br>`sfincs_input.f90:472` `if (storemeteo==1) then`<br>`sfincs_input.f90:473` `store_meteo = .true.`<br>`sfincs_input.f90:475` `if (iwindmax==1) then`<br>`sfincs_input.f90:476` `store_wind_max = .true.` | 확인: 읽기 기본값 0은 대응한다. 확인: 코드가 storemeteo=1 분기 안에서만 최대 풍속 저장을 켠다. 문서는 이 의존 조건을 적지 않는다. |
| A078<br>`percentage_done` | `docs/parameters.rst:428` `percentage_done`<br>`docs/parameters.rst:429` `:description:		Setting of how frequent to show progress of SFINCS in terms of % and time remaining, default = 5%`<br>`docs/parameters.rst:430` `:units:		integer`<br>`docs/parameters.rst:431` `:default:		5`<br>`docs/parameters.rst:432` `:min:			1`<br>`docs/parameters.rst:433` `:max:			100` | `sfincs_input.f90:301` `call read_int_input(500,'percentage_done',percdoneval,5)`<br>`sfincs_input.f90:303` `percdoneval = max(min(percdoneval,100), 0)` | 확인: 기본값 5는 대응한다. 확인: 코드는 입력을 0..100으로 제한한다. 문서 최소값 1과 코드의 하한 0이 다르다. |
| A086<br>`scsfile` | `docs/parameters.rst:483` `scsfile = sfincs.scs`<br>`docs/parameters.rst:484` `:description:		For spatially varying infiltration values per cell using the Curve Number method A (without recovery) use the scsfile option, with the same grid based input as the depfile using a binary file.`<br>`docs/parameters.rst:485` `:units:		-`<br>`docs/parameters.rst:486` `:required:		no`<br>`docs/parameters.rst:487` `:format:		bin`<br>`docs/input.rst:429` `For spatially varying infiltration values per cell using the Curve Number method without recovery use the scsfile option, with the same grid based input as the depfile using a binary file. Note here that in pre-processing the wanted CN values should be converted to S values following:`<br>`docs/input.rst:430` `* scsfile: maximum soil moisture storage capacity in inches` | `sfincs_input.f90:250` `call read_char_input(500,'scsfile',scsfile,'none')`<br>`sfincs_infiltration.f90:283` `read(500)qinffield`<br>`sfincs_infiltration.f90:290` `qinffield = qinffield * 0.0254   ! to m` | 확인: 파일은 CN 번호 대신 저장용량 S를 담는다. 확인: 코드는 inch 값에 0.0254를 곱한다. 문서의 단위 '-'가 맞지 않는다. 확인: input.rst는 inch를 올바르게 적는다. |
| A090<br>`sigmafile` | `docs/parameters.rst:504` `sigmafile = sfincs.sigma`<br>`docs/parameters.rst:505` `:description:		For spatially varying infiltration values per cell using the Green & Ampt method (with recovery) provide the sigmafile (as well as the psifile and ksfile) as suction head at the wetting front in mm, with the same grid based input as the depfile using a binary file.`<br>`docs/parameters.rst:506` `:units:		mm`<br>`docs/parameters.rst:507` `:required:		no`<br>`docs/parameters.rst:508` `:format:		bin`<br>`docs/input.rst:504` `* sigmafile: soil moisture deficit in [-]` | `sfincs_input.f90:255` `call read_char_input(500,'sigmafile',sigmafile,'none')       ! maximum moisture deficit θdmax [-]`<br>`sfincs_infiltration.f90:429` `varname = 'sigma'`<br>`sfincs_infiltration.f90:440` `read(501)GA_sigma_max` | 확인: 코드가 수분 부족량 GA_sigma_max를 읽는다. 문서 parameters.rst의 흡입수두 mm 설명이 psifile 설명과 바뀌었다. 확인: input.rst:504는 코드와 대응한다. |
| A091<br>`psifile` | `docs/parameters.rst:509` `psifile = sfincs.psi`<br>`docs/parameters.rst:510` `:description:		For spatially varying infiltration values per cell using the Green & Ampt method (with recovery) provide the psifile (as well as the sigmafile and ksfile) as soil moisture deficit in [-], with the same grid based input as the depfile using a binary file.`<br>`docs/parameters.rst:511` `:units:		-`<br>`docs/parameters.rst:512` `:required:		no`<br>`docs/parameters.rst:513` `:format:		bin`<br>`docs/input.rst:505` `* psifile: suction head at the wetting front in mm` | `sfincs_input.f90:254` `call read_char_input(500,'psifile',psifile,'none')           ! suction head [mm]`<br>`sfincs_infiltration.f90:416` `read(500)GA_head`<br>`sfincs_infiltration.f90:492` `GA_head    = GA_head / 1000                  ! from mm to m` | 확인: 코드가 흡입수두 GA_head를 읽는다. 확인: 코드는 mm를 m로 환산한다. 문서 parameters.rst의 수분 부족량 설명이 sigmafile 설명과 바뀌었다. 확인: input.rst:505는 코드와 대응한다. |
| A100<br>`rstfile` | `docs/parameters.rst:554` `rstfile = sfincs.rst`<br>`docs/parameters.rst:555` `:description:		More advanced restartfile that can also contain fluxes and velocities. As produced by SFINCS if dtrstout > 0 OR trstout > 0. Type of restart - 1: zs, qx, qy, umean and vmean  - 2: zs, qx, qy - 3: zs`<br>`docs/parameters.rst:556` `:units:		-`<br>`docs/parameters.rst:557` `:required:		no`<br>`docs/parameters.rst:558` `:format:		bin` | `sfincs_input.f90:214` `call read_char_input(500,'rstfile',rstfile,'none')`<br>`sfincs_initial_conditions.F90:195` `! 1: zs, q, uvmean`<br>`sfincs_initial_conditions.F90:196` `! 2: zs, q`<br>`sfincs_initial_conditions.F90:198` `! 4: zs, q, uvmean and cnb infiltration (writing scs_Se)`<br>`sfincs_initial_conditions.F90:199` `! 5: zs, q, uvmean and gai infiltration (writing GA_sigma & GA_F)`<br>`sfincs_initial_conditions.F90:200` `! 6: zs, q, uvmean and hor infiltration (writing rain_T1)`<br>`sfincs_initial_conditions.F90:227` `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`<br>`sfincs_initial_conditions.F90:229` `read(500)iniq`<br>`sfincs_initial_conditions.F90:233` `read(500)uvmean` | 확인: 현재 파일은 통합 q·uvmean 배열을 읽는다. 확인: type 2도 코드에서 uvmean을 읽는다. 문서는 type 2에 속도 배열을 적지 않는다. 확인: 현재 코드가 침투 상태를 담는 type 4..6도 지원한다. |
| A109<br>`netspwfile` | `docs/parameters.rst:611` `netspwfile = spiderweb.nc`<br>`docs/parameters.rst:612` `:description:		Spiderweb file including wind speed, direction, pressure (and possibly rainfall).`<br>`docs/parameters.rst:613` `:units:		coordinates: m in projected UTM zone, data: m/s, wind_from_direction in degrees, p_drop in Pa (and precipitation in mm/hr).`<br>`docs/parameters.rst:614` `:required:		no`<br>`docs/parameters.rst:615` `:format:		netcdf`<br>`docs/developments.rst:229` `* netspwfile input for precipitation should be absolute atmospheric pressure, not the pressure drop.` | `sfincs_input.f90:268` `call read_char_input(500,'netspwfile',netspwfile,'none')`<br>`sfincs_ncinput.F90:968` `NF90(nf90_inq_varid(net_file_spw%ncid, "pressure",          net_file_spw%pressure_varid) )   ! Note: absolute pressure, not pressure drop`<br>`sfincs_ncinput.F90:1044` `NF90(nf90_get_var(net_file_spw%ncid, net_file_spw%pressure_varid, prtmp, start = (/ 1, 1, it /), count = (/ spw_ncols, spw_nrows, 1 /))) ! be aware of start indices`<br>`sfincs_ncinput.F90:1046` `spw_pabs(it,:,:) = ampr_prtmp(1,:,:)`<br>`sfincs_ncinput.F90:966` `NF90(nf90_inq_varid(net_file_spw%ncid, "wind_x",            net_file_spw%wind_x_varid) )`<br>`sfincs_ncinput.F90:967` `NF90(nf90_inq_varid(net_file_spw%ncid, "wind_y",            net_file_spw%wind_y_varid) )` | 확인: NetCDF pressure는 절대기압이다. 문서의 p_drop 설명이 ASCII spwfile 설명을 반복한다. 확인: NetCDF 바람은 wind_x·wind_y 성분을 읽는다. 문서는 이 파일에 풍향 입력을 적는다. |
| A121<br>`drnfile` | `docs/parameters.rst:675` `drnfile = sfincs.drn`<br>`docs/parameters.rst:676` `:description:		Drainage pumps, culverts and check valves are both specified using the same format file, put with a different indication of the type (type=1 is drainage pump, type=2 is culvert and type=3 is check valve).`<br>`docs/parameters.rst:677` `:units:		coordinates: m in projected UTM zone, discharges in m^3/s.`<br>`docs/parameters.rst:678` `:required:		no`<br>`docs/parameters.rst:679` `:format:		asc`<br>`docs/input_structures.rst:145` `A drainage pump moves water from a retraction point (source location) to an outflow point (sink location) at a specified discharge rate, as long as there is enough water available at the retraction point. The discharge rate is defined using the par1 parameter.`<br>`docs/input_structures.rst:147` `For culverts, par1 represents the discharge capacity. The actual flow through the culvert depends on the water level difference (head difference) between the upstream and downstream ends. This gradient determines how much water flows through the culvert based on the capacity defined in par1.`<br>`docs/input_structures.rst:207` ``` ``par1 = \(\mu \cdot A \cdot \sqrt{2g}\)`` ``` | `sfincs_input.f90:222` `call read_char_input(500,'drnfile',drnfile,'none')`<br>`sfincs_discharges.f90:238` `read(drainage_line,*,iostat=stat)xsnk(idrn), ysnk(idrn), xsrc(idrn), ysrc(idrn), drainage_type(idrn), drainage_params(idrn,1)`<br>`sfincs_discharges.f90:390` `qq = drainage_params(idrn, 1)`<br>`sfincs_discharges.f90:398` `qq  = drainage_params(idrn, 1) * sqrt(zs(nmin) - zs(nmout))`<br>`sfincs_discharges.f90:422` `qq = max(qq, 0.0)` | 확인: 펌프의 par1은 유량이다. 확인: 암거와 역류방지 밸브의 par1은 수두차 제곱근에 곱하는 계수이다. 해석: 후자의 단위는 m^(5/2)/s이다. 문서의 단위 m^3/s는 모든 유형의 par1에 적용되지 않는다. |
| E003<br>`latitude` | `docs/parameters.rst:121` `:description: Turns on the Coriolis term in the momentum equation, by default turned on (coriolis = True). For projected coordinate system, if latitude is not provided (default, latitude = 0.0), coriolis is still turned off.`<br>`docs/developments.rst:179` `* coriolis - clarification of use in model and logfile: for projected coordinate systems only turned on if a latitude is provided other than 0 (default, latitude = 0.0, means no coriolis terms used in momentum equation). For large scale applications on spherical grid, the coriolis term is turned on by default.` | `sfincs_input.f90:91` `call read_real_input(500,'latitude',latitude,0.0)`<br>`sfincs_input.f90:404` `fcorio = 2 * 7.2921e-05 * sin(latitude * pi / 180)`<br>`sfincs_input.f90:406` `if (latitude < 0.01 .and. latitude > -0.01) then`<br>`sfincs_input.f90:410` `coriolis = .false.` | 확인: 기본값 0.0은 대응한다. 확인: 코드는 -0.01 < latitude < 0.01에서 Coriolis를 끈다. 문서는 조건을 latitude=0으로만 적는다. 해석: 이 변수의 단위는 도이다. |
| E014<br>`snapwave_waveforces_factor` | `docs/developments.rst:54` `* Added input variable 'snapwave_waveforces_factor' which you can set to 0 to turn off wave forces and thus incident wave setup.` | `sfincs_input.f90:308` `call read_real_input(500,'snapwave_waveforces_ratio',waveforces_ratio,1.0)`<br>`sfincs_snapwave.f90:502` `fwuv(ip) = waveforces_ratio * (0.5 * (cosrot * fwx0(nm) + sinrot * fwy0(nm)) + 0.5 * ( cosrot * fwx0(nmu) + sinrot * fwy0(nmu))) / rhow`<br>`sfincs_snapwave.f90:508` `fwuv(ip) = waveforces_ratio * (0.5 * (-sinrot * fwx0(nm) + cosrot * fwy0(nm)) + 0.5 * (-sinrot * fwx0(nmu) + cosrot * fwy0(nmu))) / rhow` | 확인: 활성 입력 이름은 snapwave_waveforces_ratio이다. 문서의 factor 이름을 읽는 호출이 없다. 확인: 대응 계수의 기본값은 1.0이다. 확인: 0을 설정하면 파력을 0으로 만든다. |
| E016<br>`cd_nr` | `docs/input.rst:857` `There is specified for how many points 'cd_nr' a velocity 'cd_wnd' and a drag coefficient 'cd_val' is specified, the following are the default values:`<br>`docs/input.rst:861` `cd_nr 		= 3` | `sfincs_input.f90:312` `call read_int_input(500,'cdnrb',cd_nr,0)`<br>`sfincs_input.f90:318` `cd_nr = 3`<br>`sfincs_input.f90:323` `cd_wnd(1) =   0.0`<br>`sfincs_input.f90:324` `cd_wnd(2) =  28.0`<br>`sfincs_input.f90:325` `cd_wnd(3) =  50.0`<br>`sfincs_input.f90:326` `cd_val(1) = 0.0010`<br>`sfincs_input.f90:327` `cd_val(2) = 0.0025`<br>`sfincs_input.f90:328` `cd_val(3) = 0.0015`<br>`sfincs_read.f90:28` `if (trim(keystr)==trim(keyword)) then`<br>`sfincs_read.f90:139` `if (trim(keystr)==trim(keyword)) then` | 확인: 활성 입력 이름은 cdnrb이다. 확인: 리더가 키워드를 문자 그대로 비교한다. 문서 예시의 이름은 리더에 대응하지 않는다. 기본 절점 값은 A046–A048에서 대조한다. |
| E017<br>`cd_wnd` | `docs/input.rst:857` `There is specified for how many points 'cd_nr' a velocity 'cd_wnd' and a drag coefficient 'cd_val' is specified, the following are the default values:`<br>`docs/input.rst:863` `cd_wnd 		= 0 28 50` | `sfincs_input.f90:334` `call read_real_array_input(500,'cdwnd',cd_wnd,0.0,cd_nr)`<br>`sfincs_input.f90:318` `cd_nr = 3`<br>`sfincs_input.f90:323` `cd_wnd(1) =   0.0`<br>`sfincs_input.f90:324` `cd_wnd(2) =  28.0`<br>`sfincs_input.f90:325` `cd_wnd(3) =  50.0`<br>`sfincs_input.f90:326` `cd_val(1) = 0.0010`<br>`sfincs_input.f90:327` `cd_val(2) = 0.0025`<br>`sfincs_input.f90:328` `cd_val(3) = 0.0015`<br>`sfincs_read.f90:28` `if (trim(keystr)==trim(keyword)) then`<br>`sfincs_read.f90:139` `if (trim(keystr)==trim(keyword)) then` | 확인: 활성 입력 이름은 cdwnd이다. 확인: 리더가 키워드를 문자 그대로 비교한다. 문서 예시의 이름은 리더에 대응하지 않는다. 기본 절점 값은 A046–A048에서 대조한다. |
| E018<br>`cd_val` | `docs/input.rst:857` `There is specified for how many points 'cd_nr' a velocity 'cd_wnd' and a drag coefficient 'cd_val' is specified, the following are the default values:`<br>`docs/input.rst:865` `cd_val 		= 0.0010 0.0025 0.0015` | `sfincs_input.f90:335` `call read_real_array_input(500,'cdval',cd_val,0.0,cd_nr)`<br>`sfincs_input.f90:318` `cd_nr = 3`<br>`sfincs_input.f90:323` `cd_wnd(1) =   0.0`<br>`sfincs_input.f90:324` `cd_wnd(2) =  28.0`<br>`sfincs_input.f90:325` `cd_wnd(3) =  50.0`<br>`sfincs_input.f90:326` `cd_val(1) = 0.0010`<br>`sfincs_input.f90:327` `cd_val(2) = 0.0025`<br>`sfincs_input.f90:328` `cd_val(3) = 0.0015`<br>`sfincs_read.f90:28` `if (trim(keystr)==trim(keyword)) then`<br>`sfincs_read.f90:139` `if (trim(keystr)==trim(keyword)) then` | 확인: 활성 입력 이름은 cdval이다. 확인: 리더가 키워드를 문자 그대로 비교한다. 문서 예시의 이름은 리더에 대응하지 않는다. 기본 절점 값은 A046–A048에서 대조한다. |
| E019<br>`rgh_level_land` | `docs/parameters.rst:163` `:description:		Varying manning roughness based on elevation (above 'rgh_level_land', overules uniform 'manning', specify in s/m^(1/3).`<br>`docs/parameters.rst:169` `:description:		Varying manning roughness based on elevation (below 'rgh_level_land', overules uniform 'manning', specify in s/m^(1/3).` | `sfincs_input.f90:76` `call read_real_input(500,'rgh_lev_land',rghlevland,0.0)` | 확인: 설명에 적힌 입력 이름이 표제의 rgh_lev_land와 다르다. 확인: 코드는 rgh_lev_land만 읽는다. |
| E020<br>`manning_Sea` | `docs/input.rst:317` `manning_Sea = 0.02` | `sfincs_input.f90:75` `call read_real_input(500,'manning_sea',manning_sea,-999.0)`<br>`sfincs_read.f90:28` `if (trim(keystr)==trim(keyword)) then` | 확인: 활성 이름은 소문자 manning_sea이다. 확인: 키워드 비교가 대소문자를 구분한다. |

### 문서에만 있는 항목

- A018 `nuviscdim`: 확인: 문서는 이 이름을 폐기된 키워드로 표시한다. 확인: 활성 리더는 nuvisc를 내부 nuviscdim 변수에 읽는다. 해석: developments.rst:286은 과거 판의 설명이다. `docs/parameters.rst:111` `nuviscdim`<br>`docs/parameters.rst:112` `:description:		Depricated after Cauberg release of SFINCS.`<br>`docs/parameters.rst:113` `:units:		-`<br>`docs/input.rst:851` `nuviscdim 	= Deprecated after Cauberg release of SFINCS.`<br>`docs/developments.rst:286` `* Option to include viscosity, enabling running on theta=1.0,  with viscosity = 1. The values 'nuvisc' will be automatically determined based on your grid resolution, and written to the log screen. Value can still be overruled by specifying 'nuvisc = value' directly, or increased with e.g. a factor 2 using 'nuviscdim = 2'.`; `sfincs_input.f90:110` `call read_real_input(500,'nuvisc',nuviscdim,0.01)`
- A033 `stopdepth`: 확인: 현재 입력 리더가 이 이름을 읽지 않는다. 확인: 현재 dtmin 계산은 uvmax를 사용한다. 확인: parameters.rst는 제거 판을 v2.1.1로 적는다. 확인: developments.rst는 제거 판을 v2.2.0으로 적는다. 제거 시점은 이전 판의 원문이 있어야 판정할 수 있다. `docs/parameters.rst:202` `stopdepth - removed from SFINCS v2.1.1 Dollerup onwards, replaced by 'uvmax'`<br>`docs/parameters.rst:203` `:description:		Water depth based on which the minimal time step is determined below which the simulation is classified as unstable and stopped.`<br>`docs/parameters.rst:204` `:units:		m`<br>`docs/parameters.rst:205` `:default:		100`<br>`docs/parameters.rst:206` `:min:			0`<br>`docs/parameters.rst:207` `:max:			Inf`<br>`docs/developments.rst:173` `* stopdepth - REMOVED in SFINCS v2.2.0, replaced by 'uvmax' to determine possible instabilities based on flow velocities rather than maximum water depth!`; `sfincs_domain.f90:1530` `! dtmin = alfa * dxymin / (sqrt(9.81 * stopdepth))`<br>`sfincs_domain.f90:1539` `dtmin = alfa * dxymin / (1.25 * abs(uvmax))`
- A040 `dtmin`: 확인: 현재 코드가 dtmin을 입력 키워드로 읽지 않는다. 확인: 코드는 alpha·최소 셀 길이·uvmax로 내부 dtmin을 계산한다. 문서의 고정 입력 기본값 1.0e-3을 적용하지 않는다. `docs/parameters.rst:245` `dtmin`<br>`docs/parameters.rst:246` `:description:		Minimum allowed internal timestep.`<br>`docs/parameters.rst:247` `:units:		s`<br>`docs/parameters.rst:248` `:default:		1.0e-3`<br>`docs/parameters.rst:249` `:min:			1.0e-3`<br>`docs/parameters.rst:250` `:max:			Inf`; `sfincs_domain.f90:1539` `dtmin = alfa * dxymin / (1.25 * abs(uvmax))`<br>`sfincs_lib.f90:634` `if (dtchk < dtmin .and. nt > 1) then`
- E015 `spw_merge_frac`: 확인: 변경 기록은 내부 변수 이름 spw_merge_frac를 적는다. 확인: 활성 입력 이름은 spwmergefrac이다. 확인: 기본값 0.5는 대응한다. 이 이름을 sfincs.inp에 그대로 쓰는 별칭은 없다. 수정 이력은 이전 판이 있어야 판정할 수 있다. `docs/developments.rst:123` `* Fixed bug when spw_merge_frac is different from default 0.5.`; `sfincs_input.f90:107` `call read_real_input(500,'spwmergefrac',spw_merge_frac,0.5)`<br>`sfincs_meteo.f90:701` `if (dstspw > spw_merge_frac * spw_radius) then`<br>`sfincs_meteo.f90:702` `merge_frac = (1.0 / (1.0 - min(spw_merge_frac, 0.999))) * (spw_radius - dstspw) / spw_radius`
- E023 `bwvfile`: 확인: SFINCS 리더에 정확한 이름 bwvfile이 없다. 확인: 통합 SnapWave는 경계 위치를 snapwave_bndfile로 읽는다. 문서는 이 목록을 사용하지 말라고 적는다. `docs/waves.rst:7` `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:`<br>`docs/waves.rst:9` `bwvfile = ''`; `sfincs_snapwave.f90:672` `call read_char_input(500, 'snapwave_bndfile', snapwave_bndfile, 'none')`
- E024 `bhsfile`: 확인: SFINCS 리더에 정확한 이름이 없다. 확인: 독립 snapwave.inp 리더에는 같은 이름이 있다. 문서의 사용 금지 안내는 SFINCS 입력 문맥에서 대응한다. `docs/waves.rst:7` `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:`<br>`docs/waves.rst:11` `bhsfile = ''`; `snapwave/snapwave_input.f90:56` `call read_char_input(500,'bhsfile',bhsfile,'')`
- E025 `btpfile`: 확인: SFINCS 리더에 정확한 이름이 없다. 확인: 독립 snapwave.inp 리더에는 같은 이름이 있다. 문서의 사용 금지 안내는 SFINCS 입력 문맥에서 대응한다. `docs/waves.rst:7` `The input of waves as boundary conditions is still work in progress. Right now the following files should not be used:`<br>`docs/waves.rst:13` `btpfile = ''`; `snapwave/snapwave_input.f90:57` `call read_char_input(500,'btpfile',btpfile,'')`
- 기상 파일 헤더 H001 `FileVersion`, H002 `filetype`, H003 `grid_unit`, H004 `quantity1`, H005 `unit1`, H006 `NODATA_value`: 리더는 헤더 줄 수를 찾은 뒤 이 필드들을 건너뛴다. `docs/input_forcing.rst:312` `FileVersion      = 1.03`; `docs/input_forcing.rst:313` `filetype         = meteo_on_equidistant_grid`; `docs/input_forcing.rst:316` `grid_unit        = m`; `docs/input_forcing.rst:322` `quantity1        = x_wind`; `docs/input_forcing.rst:323` `unit1            = m s-1`; `docs/input_forcing.rst:324` `NODATA_value     = -999`; `sfincs_spiderweb.f90:173` `id=index(line,'TIME')`<br>`sfincs_spiderweb.f90:176` `nheader = ip - 1 !-2 as in Hurrywave?`<br>`sfincs_spiderweb.f90:192` `do ip = 1, nheader`<br>`sfincs_spiderweb.f90:193` `read(888,*)cdummy`
  이 대조는 해당 필드의 값이나 단위를 검사하는 활성 `read_*_input` 호출을 찾지 못했다. `sfincs_spiderweb.f90:173` `id=index(line,'TIME')`<br>`sfincs_spiderweb.f90:176` `nheader = ip - 1 !-2 as in Hurrywave?`<br>`sfincs_spiderweb.f90:192` `do ip = 1, nheader`<br>`sfincs_spiderweb.f90:193` `read(888,*)cdummy`

## 인용 출처 요약

- `docs/parameters.rst` — §Parameters for model input / §More parameters for model input (only for advanced users) / §Parameters for model output / §Input files / §Domain / §Forcing - Water levels and waves / §Forcing - Discharges / §Forcing - Meteo / §Structures
- `docs/input.rst` — §Overview / §Grid characteristics / §Depth file / §Mask file / §Index file / §Subgrid tables / §Friction / §Infiltration (§The Curve Number method: / §The Green-Ampt method: / §The Horton method:) / §Storage volume / §Observation points / §Cross-sections for discharge output / §Initial water level / §Restart file / §Time management / §Timestep analysis / §Input format / §Output format / §Numerical parameters / §Drag Coefficients:
- `docs/output.rst` — §Output messages / §Parameters netcdf file global (sfincs_map.nc) / §Parameters netcdf file observation points (sfincs_his.nc)
- `docs/input_forcing.rst` — §Water levels / §Waves / §Discharges / §Meteo / §Spatially varying gridded / §Spatially uniform
- `docs/input_structures.rst` — §Thin dam / §Weirs / §Drainage Pumps and Culverts
- `docs/waves.rst` — §Introduction

## readthedocs 라이브 사이트

본 RST 소스는 공식 readthedocs 를 빌드 — `docs/<name>.rst` → `https://sfincs.readthedocs.io/en/latest/<name>.html`:
<https://sfincs.readthedocs.io/en/latest/parameters.html> · <https://sfincs.readthedocs.io/en/latest/input.html> · <https://sfincs.readthedocs.io/en/latest/input_forcing.html> · <https://sfincs.readthedocs.io/en/latest/input_structures.html> · <https://sfincs.readthedocs.io/en/latest/output.html> · <https://sfincs.readthedocs.io/en/latest/waves.html>. 로컬 RST(버전 고정) 1차 + 라이브 URL 병기.
