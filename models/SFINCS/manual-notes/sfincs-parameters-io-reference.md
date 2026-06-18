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

SFINCS 는 staggered equidistant recti-linear 격자, cartesian 좌표(UTM)에서만 사용 가능 (`docs/input.rst §Grid characteristics`). `epsg` 코드도 지정 가능 (예제 `epsg = 32633`, `docs/input.rst §Grid characteristics`).

### 1.2 수치·물리 (momentum/continuity)

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `advection` | 1 | - | 이류항: 0=off (SFINCS-LIE), 1=on (default, SFINCS-SSWE). Cauberg release 이후 구 1D/2D 구분 대체 |
| `advection_scheme` | `upw1` | - | 신규 scheme `upw1`(default) / `original`(Leijnse et al. 2021, 하위호환). 2024.01 release 이후 |
| `advlim` | 1.0 | m/s² | 이류항 가속도 한계 (v2.2.0 이후 default 1.0, limiter on) |
| `alpha` | 0.5 | - | CFL 조건 시간스텝 감소계수 (0.1~0.75 권장) |
| `friction2d` | true | - | 마찰항 2D 성분 포함 여부 (`false`=Leijnse 2021 구현). 2024.01 이후 |
| `huthresh` | 0.05 | m | 최소 flow depth limiter (셀 wet 판정, 0.001~0.1 권장) |
| `theta` | 1.0 | - | momentum 평활화계수 (1.0=무평활, 0.8~1.0) |
| `hmin_cfl` | 0.1 | m | CFL 최대 timestep 결정용 최소 수심 (v2.2.0 이후) |
| `baro` | 1 | - | 기압항 on(1)/off(0). 0이면 ampfile·spwfile 등 기압입력 무시 |
| `viscosity` | 1 | - | 점성항 on(1). `theta=1.0` 과 병용 권장 |
| `nuvisc` | 0.01 | - | 점성계수 'per meter of grid cell length', 내부적으로 격자크기 곱함 |
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
| `ampr_block` | 1 | - | 2D 강우 시간보간: 1=block(구간일정,default), 0=선형보간 |

infiltration 은 **강우가 forcing 될 때만** 켜지며, 방법 간 stack(중첩) 비설계 (`docs/input.rst §Infiltration`). CN 방법은 inch 단위 식 사용:

$$S = \frac{1000}{CN} - 10, \qquad Q = \frac{P^2}{P + S_{max}}$$

(`docs/input.rst §The Curve Number method:`). Green-Ampt:

$$f(t) = K\left(1 + \frac{\Delta\theta\,(\sigma + h_0)}{F(t)}\right)$$

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
| `huvmin` | 0.0 | - | 유속계산 최소수심 `uv=q/max(hu,huvmin)` (v2.3.1 이후) |
| `dtmax` | 60 | s | 최대 내부 timestep |
| `dtmin` | 1.0e-3 | s | 최소 내부 timestep |
| `tspinup` | 0 | s | tstart 후 spinup 기간 (경계수위 댐핑) |
| `spinup_meteo` | 0 | - | meteo forcing 에도 spinup 적용 여부 |
| `utmzone` | nil | - | spiderweb lat&lon→UTM 변환 (예 `16N`/`36S`) |
| `h73table` | 0 | logical | h^(7/3) lookup table (~0-30% 가속) |
| `structure_relax` | 10 | s | 구조물 신/구 방류 비율 완화계수 |

`stopdepth` 는 v2.1.1 Dollerup 이후 제거되어 `uvmax` 로 대체됨.

**Drag coefficients (풍속 의존, Delft3D 방식·Vatvani et al. 2012 기반):**

| 키워드 | 기본값 | 설명 |
|---|---|---|
| `cdnrb` | 3 | break point 개수 |
| `cdwnd` | `0 28 50` | 풍속 break point (m/s, 0 포함) |
| `cdval` | `0.001 0.0025 0.0015` | drag coefficient break point |

(`docs/parameters.rst §More parameters for model input (only for advanced users)`). `docs/input.rst §Drag Coefficients:` 에서는 키워드명을 `cd_nr`/`cd_wnd`/`cd_val` 로 표기 — 본문 간 표기 차이 주의.

### 1.5 출력 제어 (`§Parameters for model output`)

| 키워드 | 기본값 | 단위 | 설명 |
|---|---|---|---|
| `tref` | `20000101 000000` | - | 기준일 `yyyymmdd HHMMSS` |
| `tstart` | `20000101 000000` | - | 시작일 |
| `tstop` | `20000101 000000` | - | 종료일 |
| `dtout` | 0 | s | spatial map 출력 간격 |
| `dthisout` | 600 | s | 관측점 출력 간격 |
| `dtmaxout` | 9999999 | s | 최대값 map 출력 간격 (0=출력안함) |
| `dtrstout` | 0 | s | restart 파일 출력 간격 |
| `trstout` | -999.0 | s | tref 이후 특정 시각 restart 출력 |
| `dtwnd` | 1800 | s | 공간변동 meteo 갱신 간격 (spw·강우·기압·바람) |
| `outputformat` | net | - | bin/asc/net (map=`sfincs_map.nc`, point=`sfincs_his.nc`) |
| `outputformat_map` | net | - | map 전용 출력형식 |
| `outputformat_his` | net | - | his 전용 출력형식 |
| `nc_deflate_level` | 2 | - | netcdf deflate level |
| `percentage_done` | 5 | integer | 진행률 표시 빈도(%) |

**store* 플래그 (전부 default 0, 1=활성):** `storetwet`(wet 지속시간; `twet_threshold` 기본 0.01 m), `storevel`(dtout 유속), `storevelmax`/`storefluxmax`(dtmaxout 최대 유속·flux), `storecumprcp`(누적강우), `storehsubgrid`(subgrid hmax = zsmax−z_zmin; HydroMT downscaling 권장), `storehmean`(subgrid 평균수심 hmax; storehsubgrid=1 일 때만), `storeqdrain`(배수방류), `storezvolume`/`storestoragevolume`(subgrid 부피), `storemeteo`(meteo 입력), `storemaxwind`(최대풍속), `storetzsmax`(zsmax 발생시각; dtmaxout>0 일 때만), `debug`(매 timestep), `timestep_analysis`(timestep 제한 셀 진단).

`timestep_analysis = 1` 시 `sfincs_map.nc` 에 `average_required_timestep`(셀별 시간평균 CFL timestep, 미침수 셀 = -1)·`percentage_limiting_timestep`(전체 timestep 중 해당 셀이 global 최소였던 비율 %) 기록 (`docs/input.rst §Timestep analysis`).

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
| `ksfile / sigmafile / psifile` | no | bin | Green-Ampt: Ks(mm/hr) / wetting front 흡입수두(mm) / 토양수분결핍(-) |
| `f0file / fcfile / kdfile` | no | bin | Horton: 초기침투능(mm/hr) / 최소침투율(mm/hr) / 감쇠상수(hr⁻¹) |
| `sbgfile = sfincs.sbg` | subgrid 시만 | net(신)/bin(구) | subgrid table (Van Ormondt et al. 2024, netcdf 권장 2024.01 이후) |
| `obsfile = sfincs.obs` | no | asc | 관측점 (point 출력) |
| `crsfile = sfincs.crs` | no | tekal | cross-section (방류 출력) |
| `volfile = sfincs.vol` | no | bin | green infra 셀별 저장부피 (m³, subgrid mode 한정) |
| `inifile = sfincs.ini` | no | bin | 셀별 초기수위 (v2.0.0 이후 binary, 구버전 ascii) |
| `rstfile = sfincs.rst` | no | bin | restart (type1: zs,qx,qy,umean,vmean / type2: zs,qx,qy / type3: zs) |

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

**restart 워크플로** (`docs/input.rst §Restart file`): 1차 run 에서 `dtrstout`/`trstout` 지정 → 2차 run 에서 `rstfile` 지정. 현재 type 1(zs,qx,qy,umean,vmean).

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
| `spwfile = sfincs.spw` | asc | m/s, deg, Pa(, mm/hr) | spiderweb (풍속·방향·기압[, 강우]) |
| `netspwfile = spiderweb.nc` | net | 동일 | spiderweb netcdf |
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
- type=1 pump: source→sink 로 `par1` 방류율로 이송 (source 에 물 있을 때만)
- type=2 culvert: `par1`=방류용량, 실제 flow 는 상·하류 수두차 의존
- type=3 check valve: culvert 와 동일 par1, 단방향만 (point1 수위 > point2 시 flow, 역류 방지)

culvert 방류용량:

$$par1 = \mu \cdot A \cdot \sqrt{2g}$$

($\mu$=손실계수 0~1, $A$=개구면적 m², $g$=9.81 m/s²; Bernoulli 유도, `docs/input_structures.rst §Drainage Pumps and Culverts`). par2~par5 는 향후용 placeholder. 향후 Darcy–Weisbach 도입 예정. `storeqdrain=1`(v2.0.2 이후)로 방류량 출력.

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

### 5.3 화면 메시지 (`§Output messages`)

초기화 완료 = `Starting computation ...`, 계산시작 = `0% complete`, 정상종료 = `---Simulation is finished---` (총 runtime·구간별 시간·평균 timestep·최대수심 출력). OpenMP 로 가용 코어 사용 → 병렬 다중 run 비권장, 직렬 권장. 불안정 종료: `Maximum depth of 100.0 m reached!!! Simulation stopped.` — 해결: `alpha` 낮춤·`hmin_cfl` 상향·`dtmax` 하향·`advlim` 등. forcing 인식 메시지 예: `Turning on process: Precipitation` (키워드/인자 사이 **공백만** 사용, tab 혼용 금지).

---

## 6. 파랑 (SnapWave) (`docs/waves.rst`)

`docs/waves.rst §Introduction` 기준 — 경계조건으로서의 파랑 입력은 **work in progress** 이며, 다음 파일들은 **사용하지 말 것**으로 명시: `bwvfile`, `bhsfile`, `btpfile`, `cstfile` (모두 빈 값).

> 주의: 공식 docs RST 에는 SnapWave 설정 키워드 reference 가 정리되어 있지 않다. 단파/IG 파랑 forcing 의 현행 경로는 §3.1 의 `bzifile`(입사파 빠른 수위성분). SnapWave 커널 자체의 설정·구현은 docs 가 아닌 소스 분석 [[../source-analysis/sfincs_snapwave]] 에서 다룬다.

---

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
