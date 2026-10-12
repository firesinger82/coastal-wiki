---
title: "SFINCS IO·전역 데이터 모듈 (data / input / read / ncinput / ncoutput / output / bmi)"
model: SFINCS
component: io-and-global-data
canonical_source: self
citation_status: verified
verification_method: "원본 Fortran 직접 read — source/src/sfincs_data.f90 (1151줄 전수), sfincs_input.f90 (749줄), sfincs_read.f90 (303줄 전수), sfincs_ncinput.F90 (1088줄 header+subroutine 인덱스), sfincs_ncoutput.F90 (4414줄 type 정의+subroutine 인덱스+dispatch), sfincs_output.f90 (747줄 전수에 가까움), sfincs_bmi.f90 (436줄 전수). 모든 단언 file:line 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - "[[sfincs-architecture-source-map]]"
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# SFINCS IO·전역 데이터 (S-tier)

SFINCS 의 IO·전역 상태 레이어. `sfincs_data` 가 `compute_water_levels` 등이 `use` 하는 전역 변수 저장소(common-block 대체, `sfincs_continuity.f90:5-7`; `sfincs_read.f90:1-38`·`sfincs_spiderweb.f90:1-10`의 입력 루틴은 예외), 나머지 6개가 ASCII/binary/netCDF 입출력 + BMI 결합 API 를 담당.

상대경로 기준: `models/SFINCS/raw/source_code/sfincs/source/src/`.

---

## 1. `sfincs_data.f90` — 전역 변수 module (single global state)

`module sfincs_data` 는 `contains` 까지 단순 변수 선언 블록(`sfincs_data.f90:1`~`:868`). 파생 type 없이 module-level allocatable 배열·스칼라로 공유 상태를 보유 — 사실상 Fortran 의 전역 common block 역할. `compute_water_levels`는 `use sfincs_data` 로 직접 접근한다(`sfincs_continuity.f90:5-7`); `sfincs_read.f90:1-38`·`sfincs_spiderweb.f90:1-10`의 입력 루틴에는 해당 use가 없다.

### 1.1 주요 자료구조 군

| 군 | 대표 변수 (file:line) | 의미 |
|---|---|---|
| 시간 | `tstart_all, tfinish_all` (`:7`), `dtavg` (`:8`), `min_dt` (`:9`) | wallclock·평균 dt |
| 에러 | `error` (`:12`), `error_message` (`:13`) | 에러 코드/메시지 |
| BMI 플래그 | `bmi` (`:17`), `use_qext` (`:18`) | BMI 모드·외부 flux 사용 |
| 상수 | `g` (`:22`), `pi` (`:23`) | 중력·π (값은 `read` 시 세팅, §2.4) |
| 그리드 | `mmax, nmax` (`:111-112`), `dx, dy` (`:39-40`), `x0, y0` (`:58-59`), `rotation` (`:60`) | 정규격자 정의 |
| 수치 | `alfa` (courant, `:27`), `theta` (`:53`), `huthresh` (`:61`), `dtmax/dtmin` (`:55-56`) | 시간적분 파라미터 |

### 1.2 인덱스 배열 (quadtree 비구조 격자 연결)

SFINCS 는 압축 1D 인덱싱(z-점=셀 중심, uv-점=면)을 사용. 핵심:

- z→z 좌표: `z_index_z_n`, `z_index_z_m` (`sfincs_data.f90:297-298`, `target` 속성 — BMI 노출용)
- z→uv 이웃: `z_index_uv_md1/md2/mu1/mu2/nd1/...` (`:299-310`) — 각 셀의 4방향 면 인덱스
- uv→z: `uv_index_z_nm`, `uv_index_z_nmu` (`:312-313`) — 면의 양쪽 셀
- uv→uv stencil: `uv_index_u_nmu/nmd/num/ndm`, `uv_index_v_*` (`:314-321`) — advection stencil
- quadtree 매핑: `index_sfincs_in_quadtree`, `index_quadtree_in_sfincs` (`:344-345`) — BMI 셀 조회에 사용 (§7)

플래그: `z_flags_iref` (refinement level per cell, `:328`), `uv_flags_iref/type/dir` (`:330-332`), 마스크 `kcs/kcuv/kfuv` (`:334-336`).

크기 카운터: `np` (활성 z-점 수, `:280`), `npuv` (uv-점 수, `:281`), `ncuv` (`:282`) — `integer*4`.

### 1.3 동적 상태 배열 (계산 핵심)

핵심 주석 verbatim (`sfincs_data.f90:581`):
> `! The only double precision arrays are zs and z_volume.`

- `zs` (수위, **real*8**, `target`, `:586`), `z_volume` (셀 체적, **real*8**, `:593`) — 정밀도 손실 방지로 유일하게 배정밀도
- `q` / `q0` (flux, `:589-590`), `uv` / `uv0` (속도, `:591-592`) — real*4
- 최대값: `zsmax, vmax, qmax` (`:583-585`)
- `qext` (외부 flux, `target`, BMI 노출, `:599`), `uorb` (orbital velocity, `target`, `:600`)

### 1.4 서브그리드·침투·기상

- 서브그리드 테이블: `subgrid_nlevels` (`:562`), `subgrid_z_zmin` (`target`, `:564`), `subgrid_z_volmax` (`:566`), `subgrid_z_dep(:,:)` (`:567`), uv-점 `subgrid_uv_havg/nrep/pwet` (`:573-575`)
- 침투 5법 변수: SCS-CN (`scs_Se/P1/F1/S1`, `:390-393`), Green-Ampt (`GA_head/sigma_max/sigma/F/Lu`, `:394-398`), Horton (`horton_fc/f0/kd`, `:399-401`)
- 기상 격자: spiderweb `spw_*` (`:704-724`), wind `amuv_*` (`:726-738`), pressure `amp_*` (`:740-750`), rain `ampr_*` (`:752-762`)

### 1.5 룩업 테이블 (모듈 내 하드코딩)

- `cdlgx(50,20)` — LGX 풍압 항력계수 테이블, `reshape` 로 초기화 (`sfincs_data.f90:844-863`)
- `x73(1000,10)` — $h^{7/3}$ 룩업, `subroutine fill_h73_tables()` 에서 채움 (`:867`, `:872`). 식: `x73(j,k) = hh**2 * hh**(1.0/3.0)` 즉 $h^2 \cdot h^{1/3}=h^{7/3}$ (`:889`), `h73table` 켜질 때만 allocate (`:882-884`)

### 1.6 모듈 내 procedure

`contains` (`:869`) 이후 3개:
- `fill_h73_tables()` (`:872`) — §1.5
- `initialize_parameters()` (`:897`) — `t=t0`, `dt=1.0e-6` (첫 스텝 극소, `:919`), 카운터 0 초기화. 주석 `! First time step very small` (`:919`)
- `finalize_parameters()` (`:941`) — allocatable 해제. 대부분 주석처리됨. 개발자 주석 verbatim (`:945`): `! MvO says: "I really do not think this deallocation nonsense is necessary!!!"`. `z_volume` 해제는 에러 유발해 비활성 (`:1028`: `> this one seems to cause an error, not sure why`)

---

## 2. `sfincs_input.f90` — sfincs.inp 파서

`subroutine read_sfincs_input()` (`sfincs_input.f90:5`) 단일 루틴. `sfincs.inp` 를 unit 500 으로 열고(`:48`), keyword 단위로 전역 변수 채움.

### 2.1 파싱 흐름

1. `check_file_exists('sfincs.inp', ...)` (`:46`) — 존재 강제
2. 수십 개 `read_*_input(500, 'keyword', var, default)` 호출 — 각 호출이 파일을 rewind 후 keyword 스캔(§3)
3. `close(500)` (`:345`)
4. 파생값 계산·플래그 변환 (`:347` 이후)

### 2.2 keyword 예시 (default 포함)

| keyword | 변수 | default | line | 결론 |
|---|---|---|--- | --- |
| `alpha` | `alfa` | 0.50 | `:70` | — |
| `theta` | `theta` | 1.0 | `:71` | — |
| `huthresh` | `huthresh` | 0.05 | `:80` | C 문서 누락. 이 판은 NetCDF subgrid 입력을 사용할 때 huthresh의 읽기 기본값 0.05 m를 0으로 덮어쓴다. [대조 보고서 §5 A013·C001](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:943)<br>근거: `docs/parameters.rst:84` `:default:		0.05`<br>`sfincs_input.f90:80` `call read_real_input(500,'huthresh',huthresh,0.05)`<br>`sfincs_subgrid.F90:34` `if (net_file_sbg%ncid > 0) then`<br>`sfincs_subgrid.F90:40` `huthresh = 0.0`<br>`sfincs_momentum.f90:177` `if (zsu>zmin + huthresh) then ! In the 'new' subgrid formulations, zmin is lowest pixel + huthresh. Huthresh was already applied when building the subgrid tables. In sfincs_domain, huthresh is set to 0.0 to acount for this.`<br>확인: 코드 주석은 표 생성 때 이미 huthresh를 적용했다고 설명한다.<br>해석: 기본값 표는 NetCDF subgrid의 덮어쓰기 조건을 누락했다. |
| `manning` | `manning` | 0.04 | `:73` | — |
| `dtmax` | `dtmax` | 60.0 | `:79` | — |
| `inputformat` | `inputtype` | `bin` | `:84` | — |
| `outputformat` | `outputtype` | `net` | `:85` | — |
| `nc_deflate_level` | `nc_deflate_level` | 2 | `:88` | — |

#### 문서에 빠진 주 입력

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| K056·K057·K058 | 출력 시각과 파랑 갱신 간격 | K056: `sfincs_input.f90:61` `call read_real_input(500,'t0out',t0out,-999.0)`<br>K057: `sfincs_input.f90:62` `call read_real_input(500,'t1out',t1out,-999.0)`<br>K058: `sfincs_input.f90:68` `call read_real_input(500,'dtwave',dtwave,3600.0)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 t0out·t1out·dtwave의 읽기 기본값으로 각각 -999·-999·3600을 사용한다. [대조 보고서 §5 K056·K057·K058](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:987) |
| K061·K062·K063·K064·K065 | 기압·필터·복사응력·좌표 입력 | K061: `sfincs_input.f90:92` `call read_real_input(500,'pavbnd',pavbnd,0.0)`<br>K062: `sfincs_input.f90:93` `call read_real_input(500,'gapres',gapres,101200.0)`<br>K063: `sfincs_input.f90:101` `call read_real_input(500,'btfilter',btfilter,60.0)`<br>K064: `sfincs_input.f90:103` `call read_int_input(500,'radstr',iradstr,0)`<br>K065: `sfincs_input.f90:104` `call read_int_input(500,'crsgeo',igeo,0)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 pavbnd·gapres·btfilter·radstr·crsgeo 입력을 읽는다. [대조 보고서 §5 K061·K062·K063·K064·K065](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:988) |
| K068·K069·K070·K071 | 전역·파령·SnapWave·고정 출력 간격 입력 | K068: `sfincs_input.f90:109` `call read_int_input(500,'global',iglobal,0)`<br>K069: `sfincs_input.f90:113` `call read_real_input(500,'waveage',waveage,-999.0)`<br>K070: `sfincs_input.f90:114` `call read_int_input(500,'snapwave', isnapwave, 0)`<br>K071: `sfincs_input.f90:115` `call read_int_input(500,'dtoutfixed', ioutfixed, 1)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>확인: global·vegetation·timestep·restart의 일반 명사 용례는 동명 입력 필드의 설명이 아니다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 global·waveage·snapwave·dtoutfixed 입력을 읽는다. [대조 보고서 §5 K068·K069·K070·K071](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:989) |
| K109·K110·K111·K112·K113·K114·K115·K116·K117·K118·K119·K120 | 유동·조도·조석·기상 계수 입력 | K109: `sfincs_input.f90:179` `call read_real_input(500,'btrelax',btrelax,3600.0)`<br>K110: `sfincs_input.f90:182` `call read_real_input(500,'wiggle_factor',wiggle_factor,0.1)`<br>K111: `sfincs_input.f90:183` `call read_real_input(500,'wiggle_threshold',wiggle_threshold,0.1)`<br>K112: `sfincs_input.f90:187` `call read_logical_input(500,'advection_mask',advection_mask,.true.)`<br>K113: `sfincs_input.f90:190` `call read_real_input(500, 'nuviscfac', nuviscfac, 100.0)`<br>K114: `sfincs_input.f90:197` `call read_real_input(500, 'rugdepth', runup_gauge_depth, 0.05)`<br>K115: `sfincs_input.f90:198` `call read_logical_input(500, 'wave_enhanced_roughness', wave_enhanced_roughness, .false.)`<br>K116: `sfincs_input.f90:199` `call read_logical_input(500, 'use_bcafile', use_bcafile, .true.)`<br>K117: `sfincs_input.f90:200` `call read_real_input(500, 'factor_wind', factor_wind, 1.0)`<br>K118: `sfincs_input.f90:201` `call read_real_input(500, 'factor_pres', factor_pres, 1.0)`<br>K119: `sfincs_input.f90:202` `call read_real_input(500, 'factor_prcp', factor_prcp, 1.0)`<br>K120: `sfincs_input.f90:203` `call read_real_input(500, 'factor_spw_size', factor_spw_size, 1.0)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 열거한 유동·조도·조석·기상 계수 입력을 읽는다. [대조 보고서 §5 K109·K110·K111·K112·K113·K114·K115·K116·K117·K118·K119·K120](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:993) |
| K121·K122·K123·K124·K125·K126·K127·K128·K129·K130·K131·K132 | bathtub·식생·격자·침투 파일 입력 | K121: `sfincs_input.f90:205` `call read_real_input(500, 'bathtub_fachs', bathtub_fac_hs, 0.2)`<br>K122: `sfincs_input.f90:206` `call read_real_input(500, 'bathtub_dt', bathtub_dt, -999.0)`<br>K123: `sfincs_input.f90:207` `call read_logical_input(500,'vegetation',vegetation,.false.)`<br>K124: `sfincs_input.f90:211` `call read_char_input(500,'qtrfile',qtrfile,'none')`<br>K125: `sfincs_input.f90:224` `call read_char_input(500,'vegetationfile',veggiefile,'none')`<br>K126: `sfincs_input.f90:225` `call read_char_input(500,'vegetationtype_toml',veggietype_toml,'none')   ! companion TOML lookup table; if set, veggiefile holds only vegetation_type integers`<br>K127: `sfincs_input.f90:233` `call read_char_input(500, 'bdrfile', bdrfile, 'none')`<br>K128: `sfincs_input.f90:238` `call read_char_input(500,'prcfile',prcpfile,'none')`<br>K129: `sfincs_input.f90:247` `call read_char_input(500,'z0lfile',z0lfile,'none')`<br>K130: `sfincs_input.f90:270` `call read_char_input(500,'infiltration_file',infiltrationfile,'none')`<br>K131: `sfincs_input.f90:271` `call read_char_input(500,'infiltration_type',inftype,'none')`<br>K132: `sfincs_input.f90:276` `call read_char_input(500, 'rugfile', rugfile, 'none')`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>확인: global·vegetation·timestep·restart의 일반 명사 용례는 동명 입력 필드의 설명이 아니다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 열거한 bathtub·식생·격자·침투 관련 입력을 읽는다. [대조 보고서 §5 K121·K122·K123·K124·K125·K126·K127·K128·K129·K130·K131·K132](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:994) |
| K133·K134·K135·K136·K137·K138·K139 | 쓰나미·파력·파향·하상·보간 출력 입력 | K133: `sfincs_input.f90:286` `call read_int_input(500,'store_tsunami_arrival_time',itsunamitime,0)`<br>K134: `sfincs_input.f90:287` `call read_real_input(500,'tsunami_arrival_threshold',tsunami_arrival_threshold,0.01)`<br>K135: `sfincs_input.f90:292` `call read_int_input(500,'writeruntime',wrttimeoutput,0)`<br>K136: `sfincs_input.f90:296` `call read_int_input(500,'storefw', istorefw, 0)`<br>K137: `sfincs_input.f90:297` `call read_int_input(500,'storewavdir', istorewavdir, 0)`<br>K138: `sfincs_input.f90:299` `call read_logical_input(500, 'store_dynamic_bed_level', store_dynamic_bed_level, .false.)`<br>K139: `sfincs_input.f90:300` `call read_logical_input(500,'snapwave_use_nearest',snapwave_use_nearest,.true.)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다. | C 문서 누락. 이 판은 열거한 진단·출력 플래그와 snapwave_use_nearest 입력을 읽는다. [대조 보고서 §5 K133·K134·K135·K136·K137·K138·K139](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:995) |
| K141 | dtmapout 입력 | K141: `sfincs_input.f90:342` `call read_real_input(500,'dtmapout',dtmapout,0.0)`<br>검색: docs/*.rst·docs/*.txt에서 위 호출의 정확한 입력 이름을 검색했다.<br>확인: 해당 문서는 이 이름들을 입력 필드로 설명하지 않는다.<br>해석: 코드에 존재하는 입력 읽기의 문서 누락이다.<br>`sfincs_input.f90:63`이 dtout을 먼저 dtmapout에 읽는다. `:341`의 `if (dtmapout==0.0) then`을 통과해야 `:342`가 dtmapout 이름을 읽는다. | C 문서 누락. dtout을 읽은 값이 0.0일 때만 dtmapout 입력을 읽는다. dtmapout 리더의 기본값은 0.0이다. [대조 보고서 §5 K141](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:996) [10-12 결론 검증 보완] |



### 2.3 backward-compat 키워드

신·구 키워드 이중 지원 패턴: 신 키워드를 default='none' 으로 읽고, 'none' 이면 구 키워드 재시도. 예: wavemaker `wavemaker_wvmfile` ← `wvmfile` (`:121-122`), precip `prcfile` ← `precipfile` (`:238-242`).

### 2.4 파생값·플래그 변환 (`:347` 이후)

- 시간: `time_difference(trefstr,tstartstr,dtsec)` → `t0`, 동일하게 `t1` (`:365-368`)
- 상수: `g=9.81`, `pi=3.14159`, `gn2=9.81*0.02*0.02` (subgrid 전용, `:372-374`)
- 단위변환: `qinf = qinf/(3600*1000)` (mm/hr → m/s, `:376`); `rotation = rotation*pi/180`, `cosrot/sinrot` (`:378-380`)
- CRS: `crsgeo` 결정 (`igeo==0` → projected, else geographic, `:399-421`)
- Coriolis: `fcorio = 2*7.2921e-05*sin(latitude*pi/180)` (`:404`); latitude≈0 이면 off (`:406-412`) 근거: `docs/developments.rst:179` `* coriolis - clarification of use in model and logfile: for projected coordinate systems only turned on if a latitude is provided other than 0 (default, latitude = 0.0, means no coriolis terms used in momentum equation). For large scale applications on spherical grid, the coriolis term is turned on by default.`<br>`sfincs_input.f90:399` `if (igeo == 0) then`<br>`sfincs_input.f90:404` `fcorio = 2 * 7.2921e-05 * sin(latitude * pi / 180)`<br>`sfincs_input.f90:406` `if (latitude < 0.01 .and. latitude > -0.01) then`<br>`sfincs_input.f90:410` `coriolis = .false.` [대조 보고서 §5 E003·B082·C017](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:964) 결론: 문서 누락. 이 판은 투영격자의 위도가 -0.01도보다 크고 0.01도보다 작으면 Coriolis 항을 끈다.
- `store_*` 논리 플래그를 `storevel`/`storemeteo` 등 integer 입력에서 도출 (`:449`~`:650`). 예: `subgrid` 는 `sbgfile/='none'` 일 때 true (`:547`)
- bathtub 모드는 다수 프로세스 강제 off (`:707-743`)

---

## 3. `sfincs_read.f90` — 저수준 keyword 파싱 유틸

`module sfincs_read` (`sfincs_read.f90:1`). 5개 typed reader + 2 헬퍼.

- `read_real_input` (`:5`), `read_real_array_input` (`:40`), `read_int_input` (`:79`), `read_char_input` (`:115`), `read_logical_input` (`:152`)
- 공통 패턴: `value = default` → `rewind(fileid)` → 줄단위 read → `read_line` 으로 key/val 분리 → keyword 일치 시 파싱 후 `exit` (예: `:16-36`). **keyword 마다 파일 전체 rewind+스캔** — O(N×M) 이지만 inp 작아 문제없음.
- `read_logical_input` 은 값 첫 글자가 `1/y/Y/t/T` 이면 true (`:178`)
- `read_line(line0, keystr, valstr)` (`:192`): tab→space (`notabs`, `:207`), `\r` 제거(윈도 줄끝, `:211-219`), `#`/`!`/`@` 시작줄 무시(`:225`), `=` 분리(`:229-235`), `#` 인라인 코멘트 제거(`:239-245`)
- `notabs` (`:252`) — John S. Urban 의 tab→space 확장 유틸 (8칸 탭스톱). 헤더 주석 보존됨.

---

## 4. `sfincs_ncinput.F90` — netCDF 입력 (FEWS 호환)

`module sfincs_ncinput` (`.F90` 대문자=전처리 사용). 첫 줄 매크로 (`:1`):
> `#define NF90(nf90call) call handle_err(nf90call,__FILE__,__LINE__)`

→ 필수 x·y·time·zs 변수 ID 조회를(`sfincs_ncinput.F90:120-123`) `NF90(...)` 로 감싸 에러 시 파일·줄번호 보고 (`handle_err` `:1077`). 선택적 zi 변수 조회는 매크로 없이 status를 검사한다(`sfincs_ncinput.F90:125-137`).

### 4.1 파생 type (netCDF 파일 핸들)

각 입력 종류별 ncid + dimid + varid 묶음 type:
- `net_type_bndbzsbzi` (경계 수위/IG, `:10`), `net_type_srcdis` (소스 방류, `:17`), `net_type_amuv` (바람 격자, `:24`), `net_type_amp` (기압, `:32`), `net_type_ampr` (강수, `:40`), `net_type_spw` (spiderweb, `:48`), `net_type_vol` (storage volume, `:57`), `net_type_generic` (`:62`)
- 모듈 전역 인스턴스 `net_file_*` (`:68-75`)

### 4.2 reader 루틴

| 루틴 | line | 역할 |
|---|---|---|
| `read_netcdf_boundary_data` | `:79` | bnd/bzs/bzi 시계열. `zi`(IG)는 optional — NF90 매크로 없이 query 후 `bziwaves` 세팅 (`:125-129`) |
| `read_netcdf_discharge_data` | `:173` | src/dis 방류 |
| `read_netcdf_storage_volume` | `:242` | volfile |
| `read_netcdf_quadtree_*` | `:254-478` | quadtree↔sfincs 인덱스 매핑하며 변수 read (real/real8/integer) |
| `read_netcdf_flag_meanings` | `:481` | CF flag_values/flag_meanings 파싱 |
| `read_netcdf_amuv/amp/ampr/spw_data` | `:571 / :697 / :811 / :926` | 기상 격자. 주석 verbatim (`:573`): `! Output is made exactly the same as original read_amuv_dimensions & read_amuv_file subroutines but then with data given by netcdf file` |

표준 netCDF 흐름: `nf90_open` → `nf90_inq_dimid` → `nf90_inquire_dimension`(크기를 전역 `ntbnd`/`nbnd` 등에 직접 대입, `:116-117`) → `nf90_inq_varid` → (이후) `nf90_get_var`. 입력 좌표는 SFINCS 격자와 동일 UTM zone 요구 (주석 `:120`).

---

## 5. `sfincs_ncoutput.F90` — netCDF 출력 (map/his/max)

`module sfincs_ncoutput`. 동일 `NF90` 매크로 (`:1`), `handle_err` (`:4379`). `FILL_VALUE = -99999.0` (`:70`).

### 5.1 파생 type

- `map_type` (`:8`) — sfincs_map.nc 핸들. 차원(`n/m/time/timemax/runtime`), 변수 varid 다수: `zs_varid, zsmax_varid, h_varid, u/v_varid, hm0_varid`(파, `:22`), `fwx/fwy_varid`(파력, `:23`), vegetation `veg_*` (`:30-31`), UGRID mesh2d `mesh2d_*` (`:33-39`)
- `his_type` (`:43`) — sfincs_his.nc. 관측점·단면·구조물·드레인·runup gauge 차원·varid. 파 변수 `dw/df/dwig/cg/beta/srcig/alphaig` (`:62`)
- 전역 인스턴스 `map_file`, `his_file` (`:67-68`)

### 5.2 출력 루틴 (init / update / finalize)

| 루틴 | line | 비고 |
|---|---|---|
| `ncoutput_regular_map_init` | `:74` | 정규격자 map 파일 정의 (가장 큼, ~788줄) |
| `ncoutput_quadtree_map_init` | `:865` | quadtree map (UGRID mesh2d) |
| `ncoutput_his_init` | `:1768` | his 파일 |
| `ncoutput_update_regular_map` | `:2317` | 매 출력시각 map append |
| `ncoutput_update_quadtree_map` | `:2758` | |
| `ncoutput_update_his` | `:3159` | |
| `ncoutput_update_max` / `_quadtree_max` | `:3489 / :3686` | 최대값 map |
| `ncoutput_write_timestep_analysis` | `:3926` | timestep 진단 출력 |
| `ncoutput_write_tsunami_arrival_time` | `:4002` | |
| `ncoutput_add_params` | `:4071` | sfincs.inp 전 키워드를 NC attribute 로 기록 (재현성) |
| `compute_subgrid_mean_depth` | `:4312` | 주석(`:4313`): `! This subroutine cannot sit in sfincs_subgrid.f90 because that uses the same netcdf module` — netCDF module 충돌 회피로 여기 배치 |
| `logical2int` | `:4399` | function |

---

### 문서와 코드 차이 (외부 원문 판정)

| 보고서 행 ID | 항목 | 근거 | 결론 |
|---|---|---|---|
| <a id="cv-s-b042"></a>B042 | quadtree NetCDF를 QGIS에서 표시 | MDAL, [UGRID driver 문서](https://raw.githubusercontent.com/lutraconsulting/MDAL/master/docs/source/drivers/ugrid.rst). MDAL, [`mdal_ugrid.cpp`](https://raw.githubusercontent.com/lutraconsulting/MDAL/master/mdal/frmts/mdal_ugrid.cpp):41, 137, 148, 203, 350, 354–356, 400, 496, 644. MDAL, [`mdal_cf.cpp`](https://raw.githubusercontent.com/lutraconsulting/MDAL/master/mdal/frmts/mdal_cf.cpp):512–515. MDAL 판은 2026-10-12에 받은 master이다. Deltares/SFINCS, [v2.4.0 릴리스 노트](https://api.github.com/repos/Deltares/SFINCS/releases/tags/v2.4.0_Galibier_release). Deltares/SFINCS, [PR #335](https://github.com/Deltares/SFINCS/pull/335) 설명.<br>`sfincs_ncoutput.F90:979–987, 998, 1007, 1033–1038, 1044, 1085`의 속성을 MDAL 리더와 정적으로 대조했다.<br>MDAL은 `EPSG_code`가 비어 있으면 정수 `epsg`로 대체한다. `long_name`의 `direction` 때문에 메시를 거부한다는 설명은 PR #335의 주장이다. 이 설명은 직접 재현하지 않았다. | H 코드 대조 대상 아님. 이 주장은 도구 호환성 주장이다. 코드가 쓰는 UGRID 속성(`cf_role`, `topology_dimension`, `node_coordinates`, `face_coordinates`, `face_node_connectivity`, `start_index`, `grid_mapping`, `epsg`)은 MDAL 소스가 읽는 속성과 겹친다. QGIS 표시는 실행해 확인하지 않았다. [대조 보고서 §5 B042](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:1024) [10-12 외부 원문 판정] [10-12 결론 검증 보완] |

## 6. `sfincs_output.f90` — 출력 디스패처 + ASCII/binary 출력 + 재시작

`module sfincs_output` (`use sfincs_ncoutput`, `:3`). netCDF/binary 분기 + restart 작성.

### 6.1 디스패처

- `initialize_output(tmapout,tmaxout,thisout,trstout)` (`:8`) — 출력 시각 초기화. `outputtype_map=='net'` 이면 use_quadtree 분기로 `ncoutput_*_map_init`, 아니면 `open_map_output` (`:21-29`). his 파일은 관측점/단면/구조물/드레인/runup gauge 중 하나라도 있을 때만 생성 (`:65`)
- `write_output(t, write_map, write_his, write_max, write_rst, ...)` (`:84`) — 매 출력 트리거. GPU 모드 `!$acc update host(zs)` 등으로 디바이스→호스트 복사 후(`:115`~`:142`) net/binary 분기 (`:146-265`). max 출력 후 `zsmax=-999.0` 등 리셋 + 디바이스 재전송 (`:211-239`)
- `finalize_output` (`:272`)

### 6.2 비-netCDF 출력

- `open_map_output` (`:326`), `open_max_output` (`:351`), `write_map_output` (`:388`), `write_max_output` (`:469`), `close_*` (`:534/:552`)
- his: `open_his_output` (`:579`), `write_his_output` (`:605`)

### 6.3 재시작 파일 `write_rst_file(t)` (`:669`)

- `zs`(real*8)→`zs4`(real*4) 다운캐스트 (`:683-686`)
- 파일명: `sfincs.<tstring>.rst`, `form='unformatted'` (`:690-692`)
- 6 flavour (주석 `:694-700`): 1=zs,q,uvmean / 2=zs,q / 3=zs / 4-6=+침투상태(cnb→scs_Se, gai→GA_sigma+GA_F, hor→rain_T1)
<a id="cv-s-a100"></a>**A100·C014 — E 코드 결함 후보(정본).** `sfincs_initial_conditions.F90:196`의 헤더는 type 2를 `! 2: zs, q`로 적는다. `docs/parameters.rst:555`도 type 2에 평균 유량을 열거하지 않는다. 그러나 `sfincs_initial_conditions.F90:227`의 `if (rsttype==1 .or. rsttype==2 .or. rsttype==4 .or. rsttype==5 .or. rsttype==6) then`은 type 2도 포함한다. 이 분기는 `:229`에서 iniq를 읽은 뒤 `:233`에서 `read(500)uvmean`을 실행한다.<br>반대 경로인 `sfincs_output.f90:704–738`을 확인했다. CN B·Green-Ampt·Horton 쓰기는 각각 type 4·5·6이다. 나머지 쓰기는 `:735–738`에서 type 1과 zs4·q·uvmean을 기록한다. 이 쓰기 경로는 type 2를 만들지 않는다. 따라서 후보는 평균 유량이 없는 외부 type 2 파일을 읽는 경우에 한정한다. type 1의 현재 배열 이름은 통합 q와 uvmean이다. 실제 읽기 오류는 실행하지 않았다. [대조 보고서 §5 A100·C014](../../../_staging/recovery/compare/SFINCS-docs-vs-code.md:961) [10-12 결론 검증 보완]
- 중요 주석 verbatim (`:737`): `! Note: q is actually larger than npuv! It has size npuv + ncuv + 1`

---

## 7. `sfincs_bmi.f90` — Basic Model Interface (C-binding)

`module sfincs_bmi` (`sfincs_bmi.f90:1`, `private` + 명시 `public`). C 호환 진입점으로 외부 결합(예: Python BMI, coupler) 노출. 각 함수 `bind(C, name="...")` + `!DEC$/!DIR$ ATTRIBUTES DLLEXPORT`.

### 7.1 BMI 상수 (C 노출, `bind(C)`)

`BMI_LENVARADDRESS=64` (`:41`), `BMI_LENVARTYPE=64` (`:43`), `BMI_LENGRIDTYPE=64` (`:45`), `BMI_LENCOMPONENTNAME=64` (`:47`), `BMI_LENVERSION=256` (`:49`), `BMI_LENERRMESSAGE=1024` (`:51`).

### 7.2 생애주기 API

| C 함수 | line | 내부 |
|---|---|---|
| `initialize` | `:56` | `bmi=.true.`, `use_qext=.true.` 세팅 후 `sfincs_initialize()` (`:59-61`) |
| `update` | `:65` | 단일 스텝: `sfincs_update(unused_t)` (`unused_t=-1.0`, `:70-71`) |
| `update_until(t_target)` | `:75` | `delta_t = t_target - t` 계산 후 `sfincs_update(delta_t)` (`:82-83`) |
| `finalize` | `:87` | `sfincs_finalize()` |

### 7.3 변수 노출 API (get_value_ptr 등)

`get_value_ptr(c_var_name, c_data)` (`:95`) — 이름→포인터 매핑(`select case`, `:109`). 노출 변수: `z_xz`, `z_yz`, `zs`, `zb`, `subgrid_z_zmin`, `qext`, `uorb` (`:110-123`). `c_loc(...)` 로 전역 배열의 C 포인터 반환 → 외부에서 zero-copy 읽기/쓰기. default 시 `c_null_ptr`+`ierr=-1` (`:124-126`).

- `get_var_shape` (`:131`) — 대부분 `size(zs)` 반환 (`:146`), `z_index_z_*` 는 `size(z_index_z_n)` (`:150`)
- `get_var_type` (`:159`) — `zs`→`"double"`, 인덱스→`"integer"`, 나머지→`"float"` (`:172-181`). `zs` 만 배정밀도임이 BMI 에도 일관 노출
- `get_var_rank` (`:187`) — 노출 변수 모두 rank 1 (`:200-205`)
- `set_logical(c_flag_name, ival)` (`:209`) — `"qext"` 플래그로 `use_qext` 토글 (`:227-230`)

### 7.4 시간 조회 API

`get_start_time→t0` (`:237-242`), `get_end_time→t1` (`:247-252`), `get_time_step→dt` (`:257-262`), `get_current_time→t` (`:267-272`). 모두 `real(c_double)` out.

### 7.5 도메인 보조 API (coupling 전용)

- `update_zbuv` (`:277`) — `compute_zbuvmx()` 호출, uv-점 bed level 갱신 (형태학적 결합용)
- `update_apparent_roughness` (`:286`) — `update_wave_enhanced_roughness()` 호출 (`uorb` 갱신 후 호출 전제, 주석 `:291`)
- `get_sfincs_cell_index(x,y,indx)` (`:299`) — `find_quadtree_cell(x,y)` → `index_sfincs_in_quadtree(nmq)` 로 1-based SFINCS 셀 인덱스 반환 (`:311-312`)
- `get_sfincs_cell_indices(x,y,indx,n)` (`:318`) — 벡터판. 격자 밖이면 0 (`:339-341`)
- `get_sfincs_cell_area(indx,area)` (`:351`) — `crsgeo` 면 `cell_area_m2(indx)`, 아니면 `cell_area(z_flags_iref(indx))` (`:359-365`)

### 7.6 C 문자열 헬퍼 (pure)

`strlen` (null 종료 길이, `:391`), `char_array_to_string` (`:409`), `string_to_char_array` (null 추가, `:423`), `get_last_bmi_error` (`:378`, 미구현 — `"error handling not implemented"` 반환 `:384`).

---

## 8. 데이터·IO 흐름 요약

1. **읽기**: `read_sfincs_input` (§2) → 전역 `sfincs_data` 채움 → forcing 은 ASCII/binary(`inputtype`) 또는 netCDF(`net*file` 지정 시 §4 루틴) 으로 별도 로드.
2. **상태**: 전 계산이 `sfincs_data` 전역 배열을 직접 mutate (파생 type 없음). `zs`/`z_volume` 만 real*8.
3. **쓰기**: `write_output` (§6.1) 가 net/binary 분기 → map/his/max + binary restart. netCDF 는 §5.
4. **결합**: BMI (§7) 가 동일 전역 배열을 C 포인터로 노출 — 외부 coupler 가 zero-copy 로 `zs`/`qext`/`zb` 등을 읽고 씀.

전체 컴포넌트 맵은 [[sfincs-architecture-source-map]] 참조.

## 문서 참고 링크 오류

v2.0.2 릴리스 링크의 정정은 [변경 이력 노트의 정본](../manual-notes/sfincs-v2.4.0-galibier-changelog-known-issues.md#문서-참고-링크-오류)을 따른다. [10-12 결론 검증 보완]
