---
title: "ADCIRC Storm Surge — NWS family 비교 (NWS=3/4/13/14/20)"
topic: storm-surge
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "2026-07-10 재승격: 공식 docs 직접 대조 — nws_parameters.rst(NWS=3 :248 / =4 :251 / =13 :308-310 / =14 :311-312 / =19 discouraged :32 verbatim). NWS=13 실기능은 코드 정본(read_input.F:1796-1796 owiWindNetcdf namelist·:4721 'OWI Netcdf (NWS13) format') — rst :308-310 'ramping' 서술은 stale(code≠docs, [[adcirc-storm-surge-foundation]] 판정 공유). 2026-07-10 L4 감사 후속: 개인 워크플로 서술은 _staging/from-canonical/adcirc-nws13-jma-msm-local-workflow.md 로 추출(절대규칙 #2·#8), 객관 단언은 [[adcirc-met-forcing-implementation]] (file:line 인용 보유) 로 소급."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23 → L4 레이어 정리 2026-07-10"
note_date: 2026-04 (original) / 2026-05-23 (promote) / 2026-07-10 (layer cleanup)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md
  - models/ADCIRC/raw/source_code/adcirc/src/
last_source_check: 2026-10-11 (recovery 재판독 대조)
---

# ADCIRC Storm Surge NWS Families

Date: 2026-04-12 (2026-07-10 레이어 정리)

Purpose:
- compare the main meteorological forcing families relevant to storm-surge work

리더 인덱스 성격의 비교 노트. 각 포맷의 reader 경로·file:line 은
[[adcirc-met-forcing-implementation]] (NWS=2/12/13/14/15 reader, wind drag, inverse barometer) 및
[[adcirc-storm-surge]] §D(NWS family 표) 가 canonical.

## Scope

This is still a foundation note.

It compares forcing families and data requirements.
It does not choose final project parameter values.

## Main Families Relevant To Storm Surge

(포맷 서술 출처: `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst`)

### `NWS=3`

- type: US Navy Fleet Numeric 포맷 wind file — lon/lat 격자에서 ADCIRC grid 로 공간보간, Garret 식 wind stress (rst:248-249)
- useful for: simpler wind-run style examples
- official example: APES Wind Run (`examples/index.rst:26`)

### `NWS=4`

- type: PBL/JAG 포맷 wind/pressure at selected ADCIRC grid nodes (rst:251-252)
- useful for: older storm event examples such as Hurricane Isabel (`examples/index.rst:28`)
- limitation: legacy/example-oriented

### `NWS=13`

- NWS=13 상세 문서는 OWI NetCDF 입력을 정의한다. (`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:65` `**NetCDF4 File** contents:`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:67` `-  Group(s) – 1 group per grid or overlay`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:68` `-  Variables – U10/V10, PSFC`)
- fort.15 namelist 이름은 `owiWindNetcdf`이다. (`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:208` `*&owiWindNetcdf* fort.15 namelist with all inputs quoted as strings`; `src/read_input.F:534` `read(unit=15,nml=owiWindNetcdf,iostat=ios,iomsg=ios_nml_error_msg)`)
- NWS13ColdStartString sentinel 검사는 `IF(NWS.EQ.13)THEN`에서만 실행한다. (`src/read_input.F:1796` `IF(NWS.EQ.13)THEN`; `src/read_input.F:1797` `IF(INDEX(NWS13ColdStartString,"99999999.999999").GT.0)THEN`; `src/read_input.F:1799` `&                  message="NWS13ColdStartString must be set in the owiWindNetcdf namelist in the fort.15 file.")`)
- 이 시점에는 NCICE만 분리했다. (`src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`; `src/read_input.F:1796` `IF(NWS.EQ.13)THEN`)
- 코드는 이 검사 뒤에 NRS를 분리한다. (`src/read_input.F:1829` `NRS=ABS(NWS/100)`; `src/read_input.F:1830` `NWS=(ABS(NWS)-NRS*100)*(NWS/ABS(NWS))`)
- useful for: high-quality gridded forcing with overlays, curvilinear grids, and irregular timesteps
- reader 경로·namelist 요건: [[adcirc-met-forcing-implementation]] §D (owiwind_netcdf.F file:line 인용)
- nws_parameters.rst의 NWS=13 개요는 NWS=5 계열의 ramp와 WRAMP를 설명한다. (`docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:308` `**NWS = 13, -13**`; `docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:309` `Similar to NWS = 5/-5, but applies a ramping function to the meteorological inputs. Wind velocity and atmospheric pressure are read in at all grid nodes from the Single File Meteorological Forcing Input File. The positive/negative convention for time reference is the same as with NWS = 5/-5. The meteorological forcing is ramped up over a user-specified time period using the WRAMP parameter.`)
- 이 개요는 v56.2.1의 OWI NetCDF reader와 다르다. (`src/wind.F:2045` `CALL NWS13INIT(0.D0,W)`; `src/wind.F:2046` `CALL NWS13GET(WTIME1,WVNX1,WVNY1,PRN1,`)
- 같은 현행 문서의 nws13.rst는 OWI NetCDF와 owiWindNetcdf를 정의한다. (`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:65` `**NetCDF4 File** contents:`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:208` `*&owiWindNetcdf* fort.15 namelist with all inputs quoted as strings`)
- 이 상세 정의는 코드의 reader와 일치한다. (`src/read_input.F:534` `read(unit=15,nml=owiWindNetcdf,iostat=ios,iomsg=ios_nml_error_msg)`; `src/owiwind_netcdf.F:262` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)
- NWS=13 reader는 `src/owiwind_netcdf.F`이다. (`src/owiwind_netcdf.F:262` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)
- NWS=13은 전역 속성 `group_order`로 그룹 순서를 읽는다. (`src/owiwind_netcdf.F:265` `call check_err(NF90_GET_ATT(NC_ID,NF90_GLOBAL,"group_order",GroupOrder))`)
- 각 그룹의 차원은 `time`, `yi`, `xi`이다. (`src/owiwind_netcdf.F:346` `call check_err(NF90_INQ_DIMID(NC_IDG,"time",NC_DIM))`; `src/owiwind_netcdf.F:367` `call check_err(NF90_INQ_DIMID(NC_IDG,"xi",NC_DIM))`; `src/owiwind_netcdf.F:369` `call check_err(NF90_INQ_DIMID(NC_IDG,"yi",NC_DIM))`)
- 각 그룹은 `U10`, `V10`, `PSFC`, `lon`, `lat` 변수를 사용한다. (`src/owiwind_netcdf.F:381` `call check_err(NF90_INQ_VARID(NC_IDG,"lon",NC_VAR))`; `src/owiwind_netcdf.F:384` `call check_err(NF90_INQ_VARID(NC_IDG,"lat",NC_VAR))`; `src/owiwind_netcdf.F:683` `call check_err(NF90_INQ_VARID(NC_IDG,"U10",NC_VAR))`; `src/owiwind_netcdf.F:702` `call check_err(NF90_INQ_VARID(NC_IDG,"V10",NC_VAR))`; `src/owiwind_netcdf.F:721` `call check_err(NF90_INQ_VARID(NC_IDG,"PSFC",NC_VAR))`)
- 날짜 파서는 time units 문자열의 앞 14자를 건너뛴다. (`src/owiwind_netcdf.F:321` `READ(UNIT=TimeUnits,FMT='(14X,I4,1X,I2,1X,I2,1X,I2,1X,I2,1X,I2)')`; `src/owiwind_netcdf.F:322` `&    Year,Month,Day,Hour,Minute,Second`)
- 문서 설명의 `minutes from`과 예제의 `minutes since`는 다르다. (`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:97` `-  *time* (time), Datetime-number with units of “minutes from YYYY-mm-dd`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:129` `|              time:units = "minutes since 1990-01-01T01:00:00" ;`)
- 코드는 NWS13File에 입력 디렉터리 접두사를 붙이지 않는다. (`src/owiwind_netcdf.F:262` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)

### `NWS=20`

- type: Generalized Asymmetric Holland Model
- 이 판의 NWS=8 해당 호출은 `HollandGet`이다. (`src/nws08.F90:531` `call HollandGet(WVNX, WVNY, PRESS, TIMELOC, FoundEye, EyeLon, EyeLat)`)
- fort22.rst의 NWS=8 Generalized asymmetric Holland 설명은 NWS=20 GAHM 경로와 구분한다. (`docs/technical_reference/input_files/fort22.rst:333` `In this format, a single tropical cyclone model using the Generalized asymmetric Holland formulation with a moving reference frame and a background wind field is used.`; `src/wind.F:1502` `IF(NWS.EQ.20) THEN`; `src/wind.F:1503` `CALL NWS20GET(wvnx2, wvny2, prn2, timeloc)`)
- NWS=±29는 OWI 제어 파일과 GBLINPUTDIR의 `NWS_19_fort.22`를 함께 읽는다. (`src/wind.F:1928` `IF ((ABS(NWS).EQ.12).OR.(ABS(NWS).EQ.29).OR.(ABS(NWS).EQ.30)) THEN`; `src/wind.F:1929` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`; `src/wind.F:1948` `if (abs(nws).eq.29) then`; `src/wind.F:1949` `OPEN(22,FILE=TRIM(GBLINPUTDIR)//'/'//'NWS_19_fort.22',`; `src/wind.F:1951` `CALL NWS19GET(vortexWVNX2,vortexWVNY2,vortexPRN2,STATIM*86400.D0)`)
- NWS=19는 고정 폭 레코드를 읽는다. (`docs/technical_reference/input_files/fort22.rst:624` `* The format of the file is fixed and users will want to use the aswip program to be sure that the input fort.22 file is properly formatted.`; `src/wind.F:5216` `26       FORMAT(3x, i3, 2x, i4, 3i2, 6x, a4, 2(2x,i3),a1, 2x, i4,a1, 2x,`; `src/wind.F:5217` `&         i3,2x, i4, 6x, i3, 7x, 4(i4,2x), i4, 8x, i3,`; `src/wind.F:5218` `&          27x, 2(i3,2x), a10, 2x, i4, 2x, i4,`; `src/wind.F:5219` `&         2x, 4(i1,2x),2x, 4(f6.1,2x), 2x, f8.4) !,2(2x,f10.4))`)
- NWS=19 reader는 날짜·TECH·TAU·좌표·풍속·기압·등풍속선·네 반경·배경 기압·RMW·이동 방향·이동 속도·이름·cycle 번호·등풍속선 수·네 선택 값·네 Rmax·Holland B 순서로 읽는다. (`src/wind.F:5223` `READ(22,26) advr1(ient), iyear1(ient),imth1(ient),iday1(ient),`; `src/wind.F:5224` `&    ihr1(ient), type1(ient),iFcstInc1(ient), ilat1(ient),ns,`; `src/wind.F:5225` `&    ilon1(ient),ew, ispd1(ient), icpress1(ient), ivr1(ient),`; `src/wind.F:5226` `&    (ir1(ient,i),i=1,4), ipn1(ient), atcfRMW1(ient),`; `src/wind.F:5227` `&    dir1(ient),speed1(ient), name1(ient),`; `src/wind.F:5228` `&    cycle_num1(ient),isotachs_per_cycle1(ient),`; `src/wind.F:5229` `&    (quadflag1(ient,i),i=1,4),(rmaxw1(ient,i),i=1,4),HollB1(ient)`)
- NWS=20 reader는 NWS=19 필드 뒤에서 사분면 Holland B 네 값과 경계층 Vmax 네 값을 추가로 읽는다. (`docs/technical_reference/input_files/fort22.rst:638` `The file format is similar to the NWS = 19 format with 8 additional columns of data, see notes below for more information.`; `docs/technical_reference/input_files/fort22.rst:660` `* Columns 40-43: Quadrant-varying Holland B parameter`; `docs/technical_reference/input_files/fort22.rst:661` `* Columns 44-47: Quadrant-varying Vmax calculated at the top of the planetary boundary (a wind reduction factor is applied to reduce the wind speed at the boundary to the 10-m surface)`; `src/wind.F:5811` `&    (quadflag1(ient,i),i=1,4),(rmaxw1(ient,i),i=1,4),HollB1(ient),`; `src/wind.F:5812` `&    (HollBs1(ient,i),i=1,4),(VmaxesBL1(ient,i),i=1,4)`)
- 코드는 TAU의 시간 단위 값을 초로 바꾼다. (`src/wind.F:5258` `CycleTime(icyc) =  iFcstInc1(ient) * 3600.d0 + timeOffset`)
- 코드는 위도·경도의 0.1도 정수와 N/S·E/W 필드에서 좌표 부호를 반영한다. (`src/wind.F:5262` `IF(ew.EQ.'E')THEN`; `src/wind.F:5263` `ilon(icyc)=(-1)*ilon(icyc)`; `src/wind.F:5265` `IF(ns.EQ.'S')THEN`; `src/wind.F:5266` `ilat(icyc)=(-1)*ilat(icyc)`; `src/wind.F:5268` `lon(icyc) = (-1.0d0) * ilon(icyc) * 0.1d0`; `src/wind.F:5269` `lat(icyc)=ilat(icyc) * 0.1d0`)
- 문서는 최대 풍속을 knots로 적는다. (`docs/technical_reference/input_files/fort22.rst:612` `* Column 9: Maximum sustained wind speed in knots`)
- 문서는 중심 기압과 배경 기압을 MB로 적는다. (`docs/technical_reference/input_files/fort22.rst:613` `* Column 10: Minimum sea level pressure in MB`; `docs/technical_reference/input_files/fort22.rst:616` `* Column 18: Background pressure in MB; a standard value of 1013 can be used`)
- 문서는 등풍속선 풍속을 knots로 적는다. (`docs/technical_reference/input_files/fort22.rst:614` `* Column 12: Wind intensity in knots of the radii defined in the record (34, 50, 64 or 100 knots)`)
- 문서는 등풍속선의 네 반경을 NM로 적는다. (`docs/technical_reference/input_files/fort22.rst:615` `* Columns 14, 15, 16, 17: Radius of specified wind intensity for quadrants 1, 2, 3, 4 in NM; ≥ 0`)
- 코드는 이동 방향을 deg2rad로 바꿔 이동 속도의 두 성분을 만든다. (`src/wind.F:5255` `uTrans(icyc) = sin(dir1(ient)*deg2rad)*speed1(ient)`; `src/wind.F:5256` `vTrans(icyc) = cos(dir1(ient)*deg2rad)*speed1(ient)`)
- 코드는 quadflag가 1인 사분면의 Rmax를 채택한다. (`src/wind.F:5273` `if (quadflag1(ient,i)==1) then`; `src/wind.F:5274` `rmaxw(icyc,i) = rmaxw1(ient,i)`; `src/wind.F:5275` `quadflag(icyc,i) = quadflag1(ient,i)`)
- NWS=20은 선택한 사분면의 Holland B와 경계층 Vmax를 저장한다. (`src/wind.F:5936` `if (quadflag1(ient,i)==1) then`; `src/wind.F:5940` `HollBs(icyc,i,isot) = HollBs1(ient,i)`; `src/wind.F:5941` `VmaxesBL(icyc,i,isot) = VmaxesBL1(ient,i)`)
- NWS=20은 풍속에 kt2ms를 적용한다. (`src/wind.F:6120` `&                       (cHollBs(i)*((cVmwBL(i)*kt2ms)**2+`)
- NWS=20은 반경에 nm2m을 적용한다. (`src/wind.F:6119` `&                       cVmwBL(i)*kt2ms*crmaxw(i)*nm2m*corio/`)
- NWS=20은 계산한 Pa 기압을 RhoWatG로 나눈다. (`src/wind.F:6216` `press(i) = press(i) / RhoWatG`)
- useful for: parametric tropical cyclone forcing — 공식 문서가 NWS=19 를 명시적으로 비권장: `nws_parameters.rst:32` verbatim "Use of the Dynamic Asymmetric Holland Model (NWS=19) is discouraged. The Generalized Asymmetric Holland Model (NWS=20) provides improved functionality."
- strength: compact forcing representation for hurricane workflows
- 상세: [[adcirc_gahm_vortex_model]]

### `NWS=-14` / `NWS=14`

- v56.2.1의 NWS=14는 GRIB2 또는 netCDF 입력을 읽는다. (`src/wind.F:8021` `Pfile = 'fort.221.grb2'`; `src/wind.F:8030` `Pfile = 'fort.221.nc'`)
- NWS=-14는 NWS14 배경에 OWI 입력을 추가한다. (`src/wind.F:2014` `if (NWS.eq.-14) then`; `src/wind.F:2015` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`; `src/wind.F:2016` `CALL NWS12GET(WVNX1,WVNY1,PRN1,NP,PRBCKGRND,HasData)`)
- 코드는 NWS=-14의 netCDF 입력에서 종료한다. (`src/wind.F:8235` `IF (NWS.EQ.-14) THEN`; `src/wind.F:8238` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`; `src/wind.F:8239` `&      message="NWS = -14 has not yet been set up to use netcdf "//`; `src/wind.F:8240` `&              "files. Try again with grib2 background wind files.")`)
- 현행 nws_parameters.rst의 -14 hot-start 시간 기준 설명은 이 OWI 추가 경로를 설명하지 않는다. (`docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst:312` `Wind velocity and atmospheric pressure are read in from NetCDF or GRIB2 format files. This option allows ADCIRC to directly read standardized meteorological formats. If NWS = 14, ADCIRC assumes data from the cold start time; if NWS = -14, ADCIRC assumes data from the hot start time. The files must include wind velocity components and sea level pressure on a regular grid with proper metadata.`; `src/wind.F:2014` `if (NWS.eq.-14) then`; `src/wind.F:2015` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`)
- netCDF 제어 파일의 추가 얼음 변수 필드는 `if (NCICE.eq.14) then`에서만 읽는다. (`src/wind.F:8259` `if (NCICE.eq.14) then`; `src/wind.F:8260` `read(22,*) Cvar ! Ice var name`)
- `Tvar.eq.'refdate'` 경로는 `%Y-%m-%dT%H:%M:%S` 형식의 기준 날짜를 읽는다. (`src/wind.F:9262` `ELSEIF (Tvar.eq.'refdate') THEN`; `src/wind.F:9270` `refdate = strptime(trim(Tformat),`; `src/wind.F:9271` `&                         "%Y-%m-%dT%H:%M:%S")`)
- 이 경로는 기준 날짜와 초 배열로 시작 snapshot을 찾는다. (`src/wind.F:9273` `call Check_err(NF90_GET_VAR(NC_ID,Temp_ID,NCTIMES))`; `src/wind.F:9275` `stepdate = refdate +`; `src/wind.F:9276` `&                    timedelta(seconds=INT(NCTIMES(NT_OUT)))`; `src/wind.F:9277` `IF (stepdate.EQ.curDT) THEN`)
- NWS=14 reader는 `wind.F`의 `NWS14INIT`·`NWS14GET`이다. (`src/wind.F:1333` `CALL NWS14GET(WVNX2,WVNY2,PRN2,CICE2)`)
- 코드는 기상 파일명과 fort.22에 입력 디렉터리를 붙이지 않는다. (`src/wind.F:8021` `Pfile = 'fort.221.grb2'`; `src/wind.F:8022` `INQUIRE(file=Pfile,exist=Fexists)`; `src/wind.F:8030` `Pfile = 'fort.221.nc'`; `src/wind.F:8031` `INQUIRE(file=Pfile,exist=Fexists)`; `src/wind.F:8243` `OPEN(22,file='fort.22',ACTION='READ',IOSTAT=ierr)`)
- useful for: more generic gridded forcing workflows
- strength: broad compatibility with gridded products
- limitation: different configuration path from the OWI-NWS13 convention

## `NWS=13` Facts (docs 귀속 — 인용 소급)

아래 사실은 [[adcirc-met-forcing-implementation]] §D 가 소스 file:line 로 커버:
- `NWS=13` is the OWI NetCDF format for gridded wind and pressure
- it supports moving storm-centered grids, overlays, arbitrary and irregular timesteps, and curvilinear grids
- ADCIRC expects an OWI-NWS13-style NetCDF structure and a matching `&owiWindNetcdf` namelist in `fort.15`

## Layered Separation (구조 원칙)

storm surge forcing 은 세 레이어로 분리해 다루는 것이 유지보수에 유리:
- forcing source layer — 기상 자료 원천 (예: 재분석·수치예보 격자장)
- ADCIRC forcing interface layer — `NWS` 포맷 계약 (예: `NWS=13`)
- conversion layer — 원천 자료를 ADCIRC-readable 포맷으로 매핑하는 전처리

This separation is important because:
- source availability problems belong to the forcing source layer
- NetCDF schema problems belong to the conversion layer
- ADCIRC run interpretation belongs to the interface and model layers

## Official `NWS=13` Requirements

([[adcirc-met-forcing-implementation]] §D 소급)
- OWI-NWS13 conventions in the NetCDF file
- wind fields `U10`, `V10`
- pressure field `PSFC`
- time dimension with valid units
- `lat` and `lon` variables
- group ordering and ranking if overlays are used
- `fort.15` namelist `&owiWindNetcdf`

## Next Step

- ~~`[source-needed]` 잔여 인용(NWS=19 deprecation 문서 identity) 보강 후 verified 재승격 검토~~ — **완료(2026-07-10)**: nws_parameters.rst 인용 보강 + verified 재승격
- 개인 워크플로(JMA-MSM 경로)는 `_staging/from-canonical/adcirc-nws13-jma-msm-local-workflow.md` 에서 experience 게이트 대기
