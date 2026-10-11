---
title: "adcirc met forcing implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-met-forcing-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-11 (recovery 재판독 대조)
---

# ADCIRC met forcing — NWS dispatch, OWI readers, wind drag

## Scope

Where ADCIRC reads wind/pressure forcing, how `NWS` selects format, exact reader paths for NWS=2/12/13/14/15, wind-drag computation, and inverse-barometer pressure handling. Critical for the upcoming JMA-MSM → NWS=13 workflow.

## A. NWS dispatch

- NWS가 0이 아니면 코드는 NCICE를 먼저 분리한다. (`[file=src/read_input.F line=1775]` `NCICE = INT(ABS(NWS)/1000)`; `[file=src/read_input.F line=1776]` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`)
- 코드는 `i=0,5` 반복에서 `allowable_nws + i*100`과 그 음수를 검사한다. (`[file=src/read_input.F line=1782]` `do i=0,5`; `[file=src/read_input.F line=1783]` `if ( any(nws.eq.(allowable_nws + i*100)).or.`; `[file=src/read_input.F line=1784]` `&        any(nws.eq.(-1*(allowable_nws + i*100))) ) then`)
- 코드는 허용 검사 뒤에 NRS를 분리한다. (`[file=src/read_input.F line=1829]` `NRS=ABS(NWS/100)`; `[file=src/read_input.F line=1830]` `NWS=(ABS(NWS)-NRS*100)*(NWS/ABS(NWS))`)
- Cold-start init: `coldStartMeteorologicalForcing` at `[file=src/wind.F line=1811-2057]` (`IF(NWS...)` blocks for 1, ±2, 3, ±4, ±5, 6, ±7, ±8, 10, 11, ±12, ±13, ±14, ±15, 16, 19, 20, 29, 30)
- `hotstartMeteorologicalForcing`은 HOTSTART의 기상 초기화 루틴이다. (`[file=src/hstart.F line=1447]` `call hotstartMeteorologicalForcing(nws, wsx2, wsy2, pr2,`; `[file=src/wind.F line=2087]` `subroutine hotstartMeteorologicalForcing(nws, wsx2, wsy2, pr2,`)
- TIMESTEP은 단계별 기상 갱신에 `getMeteorologicalForcing`을 호출한다. (`[file=src/timestep.F line=655]` `call getMeteorologicalForcing(nws, wsx2, wsy2, pr2,`; `[file=src/wind.F line=860]` `subroutine getMeteorologicalForcing(nws, wsx2, wsy2, pr2,`)
- Per-NWS print banner at `[file=src/read_input.F line=1825-2070]`

### Per-value dispatch line map

| NWS | Cold-start init | Hot-start 초기화 | Print banner |
|-----|-----------------|-------------------|--------------|
| 0 | (skip) | `wind.F:2135-2146` | `read_input.F:1833-1838` |
| +1 | -- | `wind.F:2149-2164` | `read_input.F:1839-1846` |
| ±2 | -- | `wind.F:2170-2201` (NWS=2), `wind.F:2203-2217` (NWS=-2) | `read_input.F:1847-1866` |
| +3 | -- | `wind.F:2223-2291` | `read_input.F:1867-1878` |
| ±4 | -- | `wind.F:2298-2346, 2348-2381` | `read_input.F:1879-1904` |
| ±5 | -- | `wind.F:2387-2436, 2438-2472` | `read_input.F:1905-1930` |
| +6 | -- | `wind.F:2481-2526` | `read_input.F:1931-1943` |
| ±7 | -- | `wind.F:2535-2558, 2560-2585` | `read_input.F:1947-1966` |
| +10 | -- | `wind.F:2693-2741` | `read_input.F:1990-2003` |
| +11 | -- | `wind.F:2751-2796` | `read_input.F:2004-2016` |
| ±12 | -- | `wind.F:2800-2848` | `read_input.F:2018-2045` |
| ±13 | -- | `wind.F:2852-2885, 3032-3067` | `read_input.F:2672-2672, 4671` |
| ±14 | -- | `wind.F:2937-3027` | `read_input.F:2047-2072` |
| ±15 | -- | `wind.F:3071-3096` | `read_input.F:2073-2083, 2767-2774` |

## A2. NWS=8 (parametric vortex, mod_nws08) — verified 2026-06-04

- `nws08.F90`(1600, module `mod_nws08`): **parametric 태풍 vortex** wind — best-track(중심위치·중심기압·Rmax)으로 wind/pressure 격자장 합성. `&nws08Control` namelist.
- **2 vortex 모델**: `vortexModel="Holland"`(Holland 1980 gradient wind) 또는 **`"CLE15"`**(Chavas-Lin-Emanuel 2015, outer-region radial structure). `backgroundWindModel`: `radialVelocityWeighted` 또는 `LC12`(Lin-Chavas 2012 이동 비대칭). `windspeed_averaging_minute`(1/10), `WindMultiplier`.
- NWS=8 트랙 reader는 W 문자일 때 경도 부호를 바꾼다. (`[file=src/nws08.F90 line=1049]` `if (ew(i) == 'W') then`; `[file=src/nws08.F90 line=1050]` `Lon(i) = -1.d0*Lon(i) ! negative b/c WEST longitude`)
- NWS=8 트랙 reader는 S 문자일 때 위도 부호를 바꾼다. (`[file=src/nws08.F90 line=1052]` `if (ns(i) == 'S') then`; `[file=src/nws08.F90 line=1053]` `Lat(i) = -1.d0*Lat(i) ! negative b/c SOUTH latitude`)
- 현행 fort22.rst는 NWS=8이 E/W 문자를 무시한다고 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=353]` `* The symmetric vortex model (NWS=8) in ADCIRC assumes that the longitudes in the fort.22 are west longitude, so it multiplies the longitude values by -1. It ignores the 'E' or 'W' in the longitude column of the fort.22.`)
- 이 판의 NWS=8 해당 호출은 `HollandGet`이다. (`[file=src/nws08.F90 line=531]` `call HollandGet(WVNX, WVNY, PRESS, TIMELOC, FoundEye, EyeLon, EyeLat)`)
- fort22.rst의 NWS=8 본문은 Generalized asymmetric Holland를 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=330]` `NWS = 8 or 108: Dynamic Symmetric Holland Vortex Model`; `[file=docs/technical_reference/input_files/fort22.rst line=333]` `In this format, a single tropical cyclone model using the Generalized asymmetric Holland formulation with a moving reference frame and a background wind field is used.`)
- NWS=20은 별도의 `NWS20GET` 경로를 사용한다. (`[file=src/wind.F line=1502]` `IF(NWS.EQ.20) THEN`; `[file=src/wind.F line=1503]` `CALL NWS20GET(wvnx2, wvny2, prn2, timeloc)`)
- NWS=±29는 OWI 제어 파일을 NWS=12 reader로 읽는다. (`[file=src/wind.F line=1928]` `IF ((ABS(NWS).EQ.12).OR.(ABS(NWS).EQ.29).OR.(ABS(NWS).EQ.30)) THEN`; `[file=src/wind.F line=1929]` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`; `[file=src/wind.F line=1930]` `CALL NWS12GET(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`)
- NWS=±29는 GBLINPUTDIR의 `NWS_19_fort.22`를 추가로 읽는다. (`[file=src/wind.F line=1948]` `if (abs(nws).eq.29) then`; `[file=src/wind.F line=1949]` `OPEN(22,FILE=TRIM(GBLINPUTDIR)//'/'//'NWS_19_fort.22',`; `[file=src/wind.F line=1951]` `CALL NWS19GET(vortexWVNX2,vortexWVNY2,vortexPRN2,STATIM*86400.D0)`; `[file=src/wind.F line=2897]` `if (abs(nws).eq.29) then`; `[file=src/wind.F line=2898]` `OPEN(22,FILE=TRIM(GBLINPUTDIR)//'/'//'NWS_19_fort.22',`; `[file=src/wind.F line=2900]` `CALL NWS19GET(vortexWVNX2,vortexWVNY2,vortexPRN2,TimeLoc)`)
- EFDC [[efdc_cyclone_wind]](Holland/Hubbert/McConochie/Willoughby)와 같은 계열 — ADCIRC 측 symmetric parametric TC. GAHM/AHM(asymmetric, 별도)과 구분. storm-surge 직결.

## B. NWS=2 (절점별 응력·기압 파일)

- Reader inline in `hotStartMeteorologicalForcing`: `wind.F:2170-2201` (NWS=2), `wind.F:2203-2217` (NWS=-2)
- NWS=2의 두 바람 관련 입력은 풍속이 아니라 응력이다. (`[file=src/wind.F line=2193]` `WSX2(I) = RampMete2*WINDX`; `[file=src/wind.F line=2194]` `WSY2(I) = RampMete2*WINDY`)
- 코드는 fort.22에서 절점 번호와 두 응력 성분 및 기압을 직접 읽는다. (`[file=src/wind.F line=1817]` `READ(22,*) (NHG,WVNX1(I),WVNY1(I),PRN1(I),I=1,NP)`; `[file=src/wind.F line=1818]` `READ(22,*) (NHG,WVNX2(I),WVNY2(I),PRN2(I),I=1,NP)`)
- fort.22에는 WTIMINC 헤더를 넣지 않는다. (`[file=src/wind.F line=1817]` `READ(22,*) (NHG,WVNX1(I),WVNY1(I),PRN1(I),I=1,NP)`; `[file=src/wind.F line=1818]` `READ(22,*) (NHG,WVNX2(I),WVNY2(I),PRN2(I),I=1,NP)`)
- 문서 설명은 WTIMINC를 fort.15에 지정하도록 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=133]` `* Additional sets of met. data must be provided every WTIMINC, where WTIMINC is the met. data time interval and is specified in the Model Parameter and Periodic Boundary Condition File.`)
- NWS=3 reader는 `ICS.EQ.1`에서 Cartesian X·Y를 사용하는 보간 경로도 갖는다. (`[file=src/wind.F line=3330]` `IF(ICS.EQ.1) THEN`; `[file=src/wind.F line=3331]` `YCOOR=Y(I)`; `[file=src/wind.F line=3332]` `XCOOR=X(I)`)
- NWS=3 문서는 ADCIRC 격자가 lon·lat이어야 한다고 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=170]` `* Meteorological data is input to a longitude, latitude grid and interpolated in space onto the ADCIRC grid. The ADCIRC grid must be in lon, lat coordinates.`)
- NWS=±4 reader는 기압 입력에 100을 곱한 뒤 RHOWATG로 나눈다. (`[file=src/wind.F line=3411]` `PRN2(NHG)=100.d0*PRN2(NHG)/RHOWATG !CONVERT MILLIBARS TO M OF WATER`)
- NWS=±4 문서는 기압 입력을 hundredths of a millibar로 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=217]` `* Wind velocity (assumed to be 10m 10 minute averaged value) must be input in knots and surface atmospheric pressure must be input in hundredths of a millibar.`)
- 해석: NWS=±4의 코드 변환이 요구하는 기압 입력 단위는 mbar다(정적 판독, 실행 미확인). (`[file=src/wind.F line=3411]` `PRN2(NHG)=100.d0*PRN2(NHG)/RHOWATG !CONVERT MILLIBARS TO M OF WATER`)
- NWS=6 reader는 U·V·P를 첫 레코드부터 읽는다. (`[file=src/wind.F line=3522]` `READ(22,*) WVXFN(I,J),WVYFN(I,J),PRN(I,J)`)
- NWS=6 reader는 문서의 날짜·시각 여섯 필드를 읽지 않는다. (`[file=docs/technical_reference/input_files/fort22.rst line=274]` `IMDAY, IMMONTH, IMYEAR, IMHOUR, IMMIN, IMSEC`; `[file=src/wind.F line=3520]` `DO I=1,NWLAT`; `[file=src/wind.F line=3522]` `READ(22,*) WVXFN(I,J),WVYFN(I,J),PRN(I,J)`; `[file=src/wind.F line=3524]` `END DO`)
- NWS=±7은 두 성분을 응력으로 직접 사용한다. (`[file=src/wind.F line=1157]` `WSX2(I) = RampMete*WindX !apply ramp`; `[file=src/wind.F line=1158]` `WSY2(I) = RampMete*WindY`)
- 해석: NWS=±7의 두 성분은 물 기준 밀도로 나눈 응력 단위를 요구한다(정적 판독, 실행 미확인). (`[file=src/wind.F line=1155]` `WindX = WVNX1(I) + WTRatio*(WVNX2(I)-WVNX1(I))`; `[file=src/wind.F line=1157]` `WSX2(I) = RampMete*WindX !apply ramp`; `[file=src/wind.F line=1158]` `WSY2(I) = RampMete*WindY`)
- 공통 매개변수 문서는 NWS=±7의 두 성분을 m/s 풍속으로 적는다. (`[file=docs/technical_reference/parameter_definitions/index.rst line=2002]` `(If NWS = 6, 106, 7, -7) applied horizontal wind velocity in the x,y directions. An oceanographic convention is used where velocity is positive when it is blowing toward positive coordinate directions. Units are assumed to be m/s`)
- NWS=±4 모델 reader는 고정 형식으로 읽는다. (`[file=src/wind.F line=3400]` `171     READ(PBLJAGF,'(I8,5E13.5)') NHG,WVNX2(NHG),WVNY2(NHG),`; `[file=src/wind.F line=3401]` `&                               PRN2(NHG)`)
- NWS=±4 prep reader는 같은 문자열을 list-directed로 읽는다. (`[file=prep/prep.F line=3406]` `READ(22,'(A80)',END=9999) PBLJAGF`; `[file=prep/prep.F line=3416]` `READ(PBLJAGF,*,END=9999) NHG,U,V,PR`)
- 이 두 읽기 형식의 실행 결과는 확인하지 않음. (`[file=src/wind.F line=3400]` `171     READ(PBLJAGF,'(I8,5E13.5)') NHG,WVNX2(NHG),WVNY2(NHG),`; `[file=prep/prep.F line=3416]` `READ(PBLJAGF,*,END=9999) NHG,U,V,PR`)
- Linear interpolation: `WTRATIO = (TimeLoc - WTIME1) / WTIMINC`, then `WVNX/WVNY/PRN` interpolated at `[file=src/wind.F line=2189-2199]`

## C. NWS=12 (OWI legacy ASCII)

- Module: `OWIWIND`
- NWS=12 cold-start 초기화는 `NWS12INIT`과 `NWS12GET`을 호출한다. (`[file=src/wind.F line=1928]` `IF ((ABS(NWS).EQ.12).OR.(ABS(NWS).EQ.29).OR.(ABS(NWS).EQ.30)) THEN`; `[file=src/wind.F line=1929]` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`; `[file=src/wind.F line=1930]` `CALL NWS12GET(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`)
- HOTSTART의 기상 초기화는 `hotstartMeteorologicalForcing`을 호출한다. (`[file=src/hstart.F line=1447]` `call hotstartMeteorologicalForcing(nws, wsx2, wsy2, pr2,`)
- NWS=12의 단계별 자료 갱신은 `IF (TimeLoc.GT.WTIME2) THEN` 조건에서 `NWS12GET`을 호출한다. (`[file=src/wind.F line=1313]` `IF (ABS(NWS).EQ.12.or.ABS(NWS).eq.14) THEN`; `[file=src/wind.F line=1314]` `IF (TimeLoc.GT.WTIME2) THEN`; `[file=src/wind.F line=1324]` `CALL NWS12GET(WVNX2,WVNY2,PRN2,NP,PRBCKGRND)`)
- Implementation: `NWS12INIT` at `[file=src/owiwind.F line=168-255]`, `NWS12GET` at `[file=src/owiwind.F line=269-369]`
- File expectations: pressure/wind file pairs, defaults `fort.221/222`, optional `fort.223/224`, `fort.217/218`, or dynamic file list from `fort.22` when `numSets<0` at `[file=src/owiwind.F line=798-807, 830-836, 888-903]`

### Header / time block

- Per-snap grid/date header read with format `11` at `[file=src/owiwind.F line=489-490, 508-509, 579-580]`
- Pressure field + u/v wind arrays with format `22` at `[file=src/owiwind.F line=554-569]`
- File header start/end dates parsed from columns `56:65` and `71:80` at `[file=src/owiwind.F line=1085-1099]`
- 각 기압·바람 파일 쌍의 시작·끝 날짜는 서로 같아야 한다. (`[file=src/owiwind.F line=931]` `IF(date1pressure.NE.date1wind.OR.date2pressure.NE.date2wind)THEN`; `[file=src/owiwind.F line=934]` `CALL check_owi_err(1,errorVar,this(i)%wind_file,this(i)%iounit_wind)`)
- 중첩 격자의 시작 날짜는 첫 격자의 시작 날짜와 같아야 한다. (`[file=src/owiwind.F line=940]` `IF(this(i)%startDate.NE.this(1)%startdate)THEN`; `[file=src/owiwind.F line=943]` `CALL check_owi_err(1,errorVar,this(i)%wind_file,this(i)%iounit_wind)`)
- 이 검사 구간은 중첩 격자의 끝 날짜까지 같도록 요구하지 않는다. (`[file=src/owiwind.F line=940]` `IF(this(i)%startDate.NE.this(1)%startdate)THEN`; `[file=src/owiwind.F line=943]` `CALL check_owi_err(1,errorVar,this(i)%wind_file,this(i)%iounit_wind)`)
- 현행 nws12.rst는 중첩 격자의 시작·끝 날짜가 다를 수 있다고 적는다. (`[file=docs/user_guide/model_configuration/meteorological_forcing/nws12.rst line=112]` `of the input files, although the start and end times of the nested input overlay`; `[file=docs/user_guide/model_configuration/meteorological_forcing/nws12.rst line=113]` `sets may differ.`)
- 격자 불일치 분기는 성공한 READ의 errorIO를 `check_owi_err`에 그대로 넘긴다. (`[file=src/owiwind.F line=508]` `read (owi(idx)%iounit_wind,11,end=10000,err=9999,iostat=errorIO)`; `[file=src/owiwind.F line=513]` `if(iLatp.ne.iLatw.or.iLongp.ne.iLongw.or.dxp.ne.dxw.or.`; `[file=src/owiwind.F line=515]` `&       iCYMDHp.ne.iCYMDHw.or.iMinp.ne.iMinw) then`; `[file=src/owiwind.F line=519]` `call check_owi_err(errorIO,errorVar,filename,iounit)`)
- 해석: 성공한 READ의 ERRORIO=0은 격자 비교만으로 비영 값이 되지 않는다(정적 판독, 실행 미확인). (`[file=src/owiwind.F line=519]` `call check_owi_err(errorIO,errorVar,filename,iounit)`; `[file=src/owiwind.F line=1134]` `if (iret.ne.0) then`)
- 이 오류 처리 호출의 실제 종료 결과는 확인하지 않음. (`[file=src/owiwind.F line=519]` `call check_owi_err(errorIO,errorVar,filename,iounit)`; `[file=src/owiwind.F line=1144]` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`)

## D. NWS=13 (OWI NetCDF) — relevant for JMA-MSM workflow

- Module: `OWIWIND_NETCDF` (separate from NWS=12)
- `USE OWIWIND_NETCDF`, calls `NWS13INIT`/`NWS13GET` at `[file=src/wind.F line=1780, 2045-2049, 2857-2860, 3035-3037]`
- NWS=13 reader는 `src/owiwind_netcdf.F`이다. (`[file=src/owiwind_netcdf.F line=262]` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)
- namelist의 네 멤버는 NWS13File·NWS13ColdStartString·NWS13WindMultiplier·NWS13GroupForPowell이다. (`[file=src/read_input.F line=530]` `NWS13ColdStartString = "99999999.999999"`; `[file=src/read_input.F line=531]` `NWS13File = "fort.22.nc"`; `[file=src/read_input.F line=532]` `NWS13GroupForPowell = "0"`; `[file=src/read_input.F line=533]` `NWS13WindMultiplier = "1.0"`)
- NWS=13은 전역 속성 `group_order`로 그룹 순서를 읽는다. (`[file=src/owiwind_netcdf.F line=265]` `call check_err(NF90_GET_ATT(NC_ID,NF90_GLOBAL,"group_order",GroupOrder))`)
- 각 그룹의 차원은 `time`, `yi`, `xi`이다. (`[file=src/owiwind_netcdf.F line=346]` `call check_err(NF90_INQ_DIMID(NC_IDG,"time",NC_DIM))`; `[file=src/owiwind_netcdf.F line=367]` `call check_err(NF90_INQ_DIMID(NC_IDG,"xi",NC_DIM))`; `[file=src/owiwind_netcdf.F line=369]` `call check_err(NF90_INQ_DIMID(NC_IDG,"yi",NC_DIM))`)
- 그룹은 `U10`, `V10`, `PSFC`, `lon`, `lat` 변수를 사용한다. (`[file=docs/user_guide/model_configuration/meteorological_forcing/nws13.rst line=68]` `-  Variables – U10/V10, PSFC`; `[file=src/owiwind_netcdf.F line=381]` `call check_err(NF90_INQ_VARID(NC_IDG,"lon",NC_VAR))`; `[file=src/owiwind_netcdf.F line=384]` `call check_err(NF90_INQ_VARID(NC_IDG,"lat",NC_VAR))`; `[file=src/owiwind_netcdf.F line=683]` `call check_err(NF90_INQ_VARID(NC_IDG,"U10",NC_VAR))`; `[file=src/owiwind_netcdf.F line=702]` `call check_err(NF90_INQ_VARID(NC_IDG,"V10",NC_VAR))`; `[file=src/owiwind_netcdf.F line=721]` `call check_err(NF90_INQ_VARID(NC_IDG,"PSFC",NC_VAR))`)
- 날짜 파서는 time units 문자열의 앞 14자를 건너뛴다. (`[file=src/owiwind_netcdf.F line=321]` `READ(UNIT=TimeUnits,FMT='(14X,I4,1X,I2,1X,I2,1X,I2,1X,I2,1X,I2)')`; `[file=src/owiwind_netcdf.F line=322]` `&    Year,Month,Day,Hour,Minute,Second`)
- 문서 설명의 `minutes from`과 예제의 `minutes since`는 다르다. (`[file=docs/user_guide/model_configuration/meteorological_forcing/nws13.rst line=97]` `-  *time* (time), Datetime-number with units of “minutes from YYYY-mm-dd`; `[file=docs/user_guide/model_configuration/meteorological_forcing/nws13.rst line=129]` `|              time:units = "minutes since 1990-01-01T01:00:00" ;`)
- 코드는 NWS13File에 입력 디렉터리 접두사를 붙이지 않는다. (`[file=src/owiwind_netcdf.F line=262]` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)
- Time matching: model seconds (`TIMELOC`, `WTIME1/WTIME2`) passed to `NWS13GET` at `[file=src/wind.F line=2046-2049, 2858-2861]`
- No `TIMCO` symbol in these files

## E. NWS=14, 15 (newer)

- **NWS=14**: GRIB2/NetCDF meteorological reader family at `[file=src/read_input.F line=2032-2058]`
  - `NWS14INIT`, `NWS14GET` at `[file=src/wind.F line=2947, 2953-2955, 2968-2970]`
  - Cold start: `[file=src/wind.F line=2002-2010, 2022-2024]`
- **NWS=-14**: hybrid path combining NWS14 background + OWI overlay at `[file=src/wind.F line=2958-2964, 2973-2980]`
  - Hot start: `[file=src/wind.F line=2014-2019, 2028-2030]`
- v56.2.1의 NWS=14는 GRIB2 또는 netCDF 입력을 읽는다. (`[file=src/wind.F line=8021]` `Pfile = 'fort.221.grb2'`; `[file=src/wind.F line=8030]` `Pfile = 'fort.221.nc'`)
- NWS=-14는 NWS14 배경에 OWI 입력을 추가한다. (`[file=src/wind.F line=2014]` `if (NWS.eq.-14) then`; `[file=src/wind.F line=2015]` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`; `[file=src/wind.F line=2016]` `CALL NWS12GET(WVNX1,WVNY1,PRN1,NP,PRBCKGRND,HasData)`)
- 코드는 NWS=-14의 netCDF 입력에서 종료한다. (`[file=src/wind.F line=8235]` `IF (NWS.EQ.-14) THEN`; `[file=src/wind.F line=8238]` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`; `[file=src/wind.F line=8239]` `&      message="NWS = -14 has not yet been set up to use netcdf "//`; `[file=src/wind.F line=8240]` `&              "files. Try again with grib2 background wind files.")`)
- 현행 nws_parameters.rst의 -14 hot-start 시간 기준 설명은 이 OWI 추가 경로를 설명하지 않는다. (`[file=docs/user_guide/model_configuration/meteorological_forcing/nws_parameters.rst line=312]` `Wind velocity and atmospheric pressure are read in from NetCDF or GRIB2 format files. This option allows ADCIRC to directly read standardized meteorological formats. If NWS = 14, ADCIRC assumes data from the cold start time; if NWS = -14, ADCIRC assumes data from the hot start time. The files must include wind velocity components and sea level pressure on a regular grid with proper metadata.`; `[file=src/wind.F line=2014]` `if (NWS.eq.-14) then`; `[file=src/wind.F line=2015]` `CALL NWS12INIT(WVNX1,WVNY1,PRN1,NP,PRBCKGRND)`)
- netCDF 제어 파일의 추가 얼음 변수 필드는 `if (NCICE.eq.14) then`에서만 읽는다. (`[file=src/wind.F line=8259]` `if (NCICE.eq.14) then`; `[file=src/wind.F line=8260]` `read(22,*) Cvar ! Ice var name`)
- `Tvar.eq.'refdate'` 경로는 `%Y-%m-%dT%H:%M:%S` 형식의 기준 날짜를 읽는다. (`[file=src/wind.F line=9262]` `ELSEIF (Tvar.eq.'refdate') THEN`; `[file=src/wind.F line=9270]` `refdate = strptime(trim(Tformat),`; `[file=src/wind.F line=9271]` `&                         "%Y-%m-%dT%H:%M:%S")`)
- 이 경로는 기준 날짜와 초 배열로 시작 snapshot을 찾는다. (`[file=src/wind.F line=9273]` `call Check_err(NF90_GET_VAR(NC_ID,Temp_ID,NCTIMES))`; `[file=src/wind.F line=9275]` `stepdate = refdate +`; `[file=src/wind.F line=9276]` `&                    timedelta(seconds=INT(NCTIMES(NT_OUT)))`; `[file=src/wind.F line=9277]` `IF (stepdate.EQ.curDT) THEN`)
- 코드는 NWS=14의 기상 파일명과 fort.22에 입력 디렉터리를 붙이지 않는다. (`[file=src/wind.F line=8021]` `Pfile = 'fort.221.grb2'`; `[file=src/wind.F line=8022]` `INQUIRE(file=Pfile,exist=Fexists)`; `[file=src/wind.F line=8030]` `Pfile = 'fort.221.nc'`; `[file=src/wind.F line=8031]` `INQUIRE(file=Pfile,exist=Fexists)`; `[file=src/wind.F line=8243]` `OPEN(22,file='fort.22',ACTION='READ',IOSTAT=ierr)`)
- **NWS=15**: HWind forcing at `[file=src/read_input.F line=2059-2069]`
  - `NWS15INIT`, `NWS15GET` at `[file=src/wind.F line=2055-2057, 3071-3074]`
- NWS=15·16 초기화 루틴은 GLOBALDIR의 fort.22를 연다. (`[file=src/wind.F line=6258]` `call openFileForRead(22,trim(globaldir)//"/fort.22",errorio)`; `[file=src/wind.F line=6971]` `call openFileForRead(22,trim(globaldir)//"/fort.22",errorio)`)
- NWS=15 reader는 격자 간격을 km로 읽고 1000을 곱한다. (`[file=src/wind.F line=6723]` `read(220,'(7X,F8.5,A)',end=246,err=248,iostat=errorio)`; `[file=src/wind.F line=6724]` `&   hWindFiles(cn)%dh`; `[file=src/wind.F line=6725]` `write(scratchMessage,'("Mercator grid spacing is ",F8.5," km.")')`; `[file=src/wind.F line=6787]` `hWindFiles(cn)%dh = hWindFiles(cn)%dh * 1000.d0`)
- 현행 NWS=15 문서는 격자 간격을 m로 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=496]` `* the mercator grid spacing is in meters and is uniform in x and y (dx=dy)`)
- NWS=16 제어 레코드는 시간·ramp·파일명 세 필드다. (`[file=src/wind.F line=7009]` `read(22,*,end=246,err=248,iostat=errorio)`; `[file=src/wind.F line=7010]` `&     GFDL_Files(i)%cycleTime,`; `[file=src/wind.F line=7011]` `&     GFDL_Files(i)%rampVal,`; `[file=src/wind.F line=7012]` `&     GFDL_Files(i)%file_name`)
- 문서 예제의 Pc 열은 NWS=16 제어 reader에 없다. (`[file=docs/technical_reference/input_files/fort22.rst line=569]` `0.0 -1 0.0 "/home/jason/hwind/al092011_0828_1330" ! time (hours), Pc (mb), ramp mult, filename`; `[file=src/wind.F line=7010]` `&     GFDL_Files(i)%cycleTime,`; `[file=src/wind.F line=7011]` `&     GFDL_Files(i)%rampVal,`; `[file=src/wind.F line=7012]` `&     GFDL_Files(i)%file_name`)
- NWS=16 reader는 NCELLS를 I10으로 읽는다. (`[file=src/wind.F line=7253]` `read(LUN,'(I10)') NPTS_GFDL`)
- F10.4 형식의 옛 READ는 주석이다. (`[file=src/wind.F line=7251]` `!       READ(LUN,'(F10.4)') RPTS_GFDL`; `[file=src/wind.F line=7252]` `!       NPTS_GFDL = INT(RPTS_GFDL)`)
- NWS=16 데이터 reader는 선택적인 nest 열을 읽지 않는다. (`[file=docs/technical_reference/input_files/fort22.rst line=556]` `* column 10: nest number (this is not always present)`; `[file=src/wind.F line=7264]` `!          READ(LUN,'(10F10.4)') UTMP,VTMP,TTMP,MTMP,SPTMP,PTMP,`; `[file=src/wind.F line=7265]` `!     &                      LONGTMP,LATTMP,HTMP,NTMP`; `[file=src/wind.F line=7266]` `READ(LUN,'(9F10.4)') UTMP,VTMP,TTMP,MTMP,SPTMP,PTMP,`; `[file=src/wind.F line=7267]` `&                      LONGTMP,LATTMP,HTMP`)

## F. Wind drag

- Stress form: `WSX/WSY = Ramp * airwaterdensityrat * WDragCo * WindComponent * WindMag`
  i.e., proportional to `Cd * (rho_air/rho_water) * U10²`
- Examples: `[file=src/wind.F line=2288-2289, 3014-3015]`
- Garratt formula: `Cd = 0.001 * (0.75 + 0.067 * WindSpeed)` at `[file=src/wind.F line=514-521]`
- Cap: `WindDrag = MIN(GarrattWindDrag(...), WindDragLimit)` at `[file=src/wind.F line=531-539]`
- Default cap: `WindDragLimit = 0.0035` at `[file=src/wind.F line=122]`
- Configurable via `/metControl/ WindDragLimit` namelist at `[file=src/read_input.F line=238, 484-487]`
- 현행 입력 문서는 일부 NWS의 응력 계수 상한을 0.003으로 적는다. (`[file=docs/technical_reference/input_files/fort22.rst line=222]` `* if(DRAG_COEFF.gt.0.003) DRAG_COEFF=0.003`; `[file=docs/technical_reference/input_files/fort22.rst line=258]` `* if(DRAG_COEFF.gt.0.003) DRAG_COEFF=0.003`; `[file=docs/technical_reference/input_files/fort200.rst line=93]` `If (DRAG_COEFF.gt.0.003) DRAG_COEFF=0.003`)
- 코드의 기본 WindDragLimit은 0.0035다. (`[file=src/wind.F line=122]` `REAL(8) :: WindDragLimit = 0.0035d0   ! maximum wind drag value`)
- 실제 계산은 선택한 DragLaw와 WindDragLimit에 따른다. (`[file=src/wind.F line=537]` `WindDrag = MIN(GarrattWindDrag(WindSpeed,NodeNumber),WindDragLimit)`)
- **Legacy `CDCAP` token NOT present in these files** — modern code uses `WindDragLimit`

## G. Pressure-only effect (inverse barometer)

- Atmospheric pressure stored as water-surface equivalent (`PR2`) relative to `PRBCKGRND_MH2O`:
  ```
  PRDIFF = Ramp * (PR_forcing - PRBCKGRND_MH2O)
  PR2 = PRBCKGRND_MH2O + PRDIFF
  ```
  at `[file=src/wind.F line=2197-2200, 3016-3022]`
- `PRBCKGRND_MH2O` converted from mb to meters of water at `[file=src/wind.F line=352-355]`
- `NOIVB`: forces `PR2 = PRBCKGRND_MH2O` (disables IB contribution) at `[file=src/wind.F line=3018-3021, 1415-1418]`

## H. fort.71-74 met output

- Output **control** is in `read_input.F` (not the actual write):
  - Station met (NOUTM, units 71/72): `[file=src/read_input.F line=3988-3993, 4003-4014, 4051]`
  - Global met (NOUTGW, units 73/74): `[file=src/read_input.F line=4345-4353, 4360-4371]`
- **No `WRITE(71/72/73/74,...)`** in `wind.F`/`owiwind.F`/`owi_ice.F`/`read_input.F` — actual write loop is elsewhere (in `write_output.F`, see ADCIRC outputs note)

## Decision Guide — JMA-MSM workflow

| Step | Tool | Result |
|------|------|--------|
| Download JMA-MSM | external (already in WORK_LOG) | NetCDF files per day |
| Convert to OWI NetCDF | `tools/scripts/jma_to_fort22.py` | NWS=13 compatible NetCDF |
| Set NWS=13 in fort.15 | text edit | format declaration |
| Set NWS13 namelist | `NWS13File`, `NWS13ColdStartString` | reader configuration |
| Run | adcprep + padcirc | hourly wind/pressure forcing |

## Working Rules

1. fort.15의 namelist 이름은 `owiWindNetcdf`이다. (`[file=src/read_input.F line=529]` `namelistSpecifier = 'owiWindNetcdf'`; `[file=src/read_input.F line=534]` `read(unit=15,nml=owiWindNetcdf,iostat=ios,iomsg=ios_nml_error_msg)`)
   - 네 멤버는 문자열 입력이다. (`[file=docs/user_guide/model_configuration/meteorological_forcing/nws13.rst line=208]` `*&owiWindNetcdf* fort.15 namelist with all inputs quoted as strings`)
   - NWS13ColdStartString은 `YYYYMMDD.HHMMSS` 형식의 cold-start 날짜 문자열이다. (`[file=docs/user_guide/model_configuration/meteorological_forcing/nws13.rst line=210]` `-  *NWS13ColdStartString*: required cold start time of simulation formatted as`; `[file=docs/user_guide/model_configuration/meteorological_forcing/nws13.rst line=211]` `'YYYYMMDD.HHMMSS'`)
   - NWS13File의 기본값은 `fort.22.nc`다. (`[file=src/read_input.F line=531]` `NWS13File = "fort.22.nc"`)
   - NWS13ColdStartString sentinel 검사는 `IF(NWS.EQ.13)THEN`에서 실행한다. (`[file=src/read_input.F line=1796]` `IF(NWS.EQ.13)THEN`; `[file=src/read_input.F line=1797]` `IF(INDEX(NWS13ColdStartString,"99999999.999999").GT.0)THEN`; `[file=src/read_input.F line=1799]` `&                  message="NWS13ColdStartString must be set in the owiWindNetcdf namelist in the fort.15 file.")`)
   - 코드는 이 검사 뒤에 NRS를 분리한다. (`[file=src/read_input.F line=1829]` `NRS=ABS(NWS/100)`)
2. NWS의 기본 값은 외력 종류를 선택한다. (`[file=src/wind.F line=2170]` `IF(NWS.EQ.2) THEN`; `[file=src/wind.F line=2203]` `IF(NWS.EQ.-2) THEN`)
   - 일부 NWS의 부호는 자료 시간 기준을 바꾼다. (`[file=src/wind.F line=2172]` `WTIME1 = STATIM*86400.D0`; `[file=src/wind.F line=2205]` `WTIME1 = TimeLoc`)
   - NWS=2와 NWS=-2는 모두 입력 응력을 WSX2·WSY2에 직접 대입한다. (`[file=src/wind.F line=2193]` `WSX2(I) = RampMete2*WINDX`; `[file=src/wind.F line=2194]` `WSY2(I) = RampMete2*WINDY`; `[file=src/wind.F line=2210]` `WSX2(I) = RampMete2*WVNX1(I)`; `[file=src/wind.F line=2211]` `WSY2(I) = RampMete2*WVNY1(I)`)
   - NWS=-2의 부호 자체가 풍속을 Cd로 곱하게 만들지 않는다. (`[file=src/wind.F line=2203]` `IF(NWS.EQ.-2) THEN`; `[file=src/wind.F line=2210]` `WSX2(I) = RampMete2*WVNX1(I)`; `[file=src/wind.F line=2211]` `WSY2(I) = RampMete2*WVNY1(I)`)
3. **CDCAP** is renamed to `WindDragLimit` in v55+; legacy fort.15 `CDCAP` lines may be ignored.
4. **NOIVB=1** to disable inverse barometer when only wind matters; default behavior includes IB pressure effect on water level.
5. NWS=2의 fort.22에는 WTIMINC 헤더를 넣지 않는다. (`[file=src/wind.F line=1817]` `READ(22,*) (NHG,WVNX1(I),WVNY1(I),PRN1(I),I=1,NP)`; `[file=src/wind.F line=1818]` `READ(22,*) (NHG,WVNX2(I),WVNY2(I),PRN2(I),I=1,NP)`)

## Common Pitfalls

- **NWS=13 with wrong NetCDF variable names** — fails silently or wrong forcing; use the canonical OWI converter tool.
- NWS=14는 GRIB2 또는 NetCDF 입력을 읽는다. (`[file=src/wind.F line=8021]` `Pfile = 'fort.221.grb2'`; `[file=src/wind.F line=8030]` `Pfile = 'fort.221.nc'`)
- NWS=-14는 같은 입력과 OWI 입력을 결합한다. (`[file=src/wind.F line=2973]` `if (NWS.eq.-14) then`; `[file=src/wind.F line=2974]` `CALL NWS12GET(WVNX2,WVNY2,PRN2,NP,PRBCKGRND,HasData)`)
- NWS=-14의 fort.15 보충 줄에는 WTIMINC_12가 추가된다. (`[file=src/read_input.F line=2674]` `IF (NWS.eq.-14) THEN`; `[file=src/read_input.F line=2675]` `IF((NCICE.EQ.0).AND.(NRS.EQ.0)) READ(15,*) WTIMINC,`; `[file=src/read_input.F line=2676]` `&                                                 WTIMINC_12`; `[file=docs/user_guide/model_configuration/meteorological_forcing/wtiminc.rst line=19]` `````NWS=-14``, a second parameter, WTIMINC_12```; `[file=docs/user_guide/model_configuration/meteorological_forcing/wtiminc.rst line=20]` `defines the time increment for meteorological data for the OWI-formatted files.`)
- **Wind multiplier scaling** — `NWS13WindMultiplier` for unit conversion. Default 1.0; check if your NetCDF is in m/s or knots.
- **NOIVB** with hurricane storm-surge — disabling IB underestimates surge by 1-3 cm per mb pressure drop.

## References

- `src/wind.F` — main NWS dispatch + per-NWS readers.
- `src/owiwind.F` — OWI legacy reader (NWS=12).
- `src/owi_ice.F` — ice forcing.
- `src/read_input.F` — namelist parsing, NWS validation.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 50+ file:line citations |
| Coverage | NWS dispatch table, NWS=2/12/13/14/15 readers, wind drag, IB, output control |
| Review status | `review_required: true` |
