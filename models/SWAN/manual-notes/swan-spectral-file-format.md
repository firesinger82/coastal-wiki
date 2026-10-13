---
title: "SWAN spectral file format (swanuse Appendix D) — BOUNDSPEC/SPECOUT/NESTOUT 파일구조: SWAN version·TIME·LOCATIONS/LONLAT·RFREQ/AFREQ·CDIR/NDIR·QUANT·FACTOR/ZERO/NODATA + 1D 3-quantity/2D 1-quantity verbatim"
topic: swan
canonical_source: external
external_source: "swanuse (User Manual, SWAN Cycle III version 41.51) Appendix D 'Spectrum files, input and output' (node50.md). spectral input(BOUNDSPEC) + output(SPECOUT/NESTOUT) 파일 표준 포맷 version 1. 1D nonstat spherical + 2D stat Cartesian 예제 + formal description."
citation_status: verified
verification_method: "models/SWAN/raw/manuals/website_markdown/online_doc/swanuse/node50.md 직접 read. 파일 키워드(SWAN/TIME/LOCATIONS/LONLAT/RFREQ/AFREQ/CDIR/NDIR/QUANT/FACTOR/ZERO/NODATA/LOCATION) 구조 + 1D 3-quantity/2D 1-quantity 규칙 + exception value + FACTOR scaling verbatim. source-analysis output-formats(dispatch)와 cross-check. 2026-10-13 recovery 대조 보고서 R1–R8 반영"
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 파일 포맷 키워드·구조 verbatim, BOUNDSPEC/SPECOUT/NESTOUT·nesting 정합"
verification_date: 2026-06-03
last_source_check: "2026-10-13 (recovery 대조 반영)"
related:
  - models/SWAN/source-analysis/swan-output-formats.md
  - models/SWAN/manual-notes/swan-command-numerics-output-reference.md
  - models/SWAN/source-analysis/swan-nesting-io-implementation.md
  - models/SWAN/manual-notes/swan-output-variable-definitions.md
---

# SWAN spectral file format (swanuse Appendix D) — verified

> swanuse Appendix D (User Manual 41.51 / node50) 직접 read. SWAN **spectral 파일의 표준 포맷**(version 1) — `BOUNDSPEC`(입력) + `SPECOUT`/`NESTOUT`(출력) + nesting 이 공유. 본 노트 = **파일 구조/키워드**(format spec), [swan-output-formats](../source-analysis/swan-output-formats.md) = output **dispatch 메커닉**(source-code), [swan-output-variable-definitions](swan-output-variable-definitions.md) = quantity **의미**. writer는 SWAN 1을 쓴다. reader는 SWAN 표식 뒤의 판 번호를 검사하지 않는다. (`src/swanout2.ftn:1866` `INTEGER, SAVE :: IVERF = 1`; `src/swanout2.ftn:1907` `WRITE (NREF, 101) IVERF`; `src/swanpre2.ftn:4095` `ELSE IF (EQCSTR(HEDLIN,'SWAN')) THEN`.) [10-13 전수 검증 보완]

## 1. 파일 식별 + 포함 정보

- writer는 SWAN 1을 쓴다. reader는 SWAN 표식 뒤의 판 번호를 검사하지 않는다. (`src/swanout2.ftn:1866` `INTEGER, SAVE :: IVERF = 1`; `src/swanout2.ftn:1907` `WRITE (NREF, 101) IVERF`; `src/swanpre2.ftn:4095` `ELSE IF (EQCSTR(HEDLIN,'SWAN')) THEN`; swanuse PDF 145쪽 / 인쇄 137쪽.) [10-13 전수 검증 보완]
- 포함: locations 좌표 / frequencies / directions(2D) / time(time-dependent) / spectral energy·variance density (+ 1D 는 average direction·directional spreading).

## 2. Free format 규약 ★

- **free format**(FORTRAN convention), 단 **모든 키워드·quantity 이름은 line 1번째 위치에서 시작**(Appendix B syntax).
- 2D 밀도 표는 전체 배열을 한 READ로 읽는다. 표의 각 주파수 행 뒤에 임의의 설명을 붙일 수 있다고 일반화하지 않는다. (`src/swanmain.ftn:8425` `READ (NDSD,*,END=930,ERR=920)`; `src/swanmain.ftn:8426` `&             ((BAUX1(IANG,IFRE),IANG=1,NANG),IFRE=1,NFRE)`; swanuse PDF 150쪽 / 인쇄 142쪽.)
- `$` = comment line (예: `$ Data produced by SWAN version 41.51`).
- 정상 TEST 파일은 ITER와 coding 0을 사용한다. (`src/swanpre2.ftn:6307` `WRITE (IFPAR, 102) 'ITER', 'iteration-dependent data'`; `src/swanpre2.ftn:6308` `WRITE (IFPAR, 103) 0`.)
- PAR은 HSIGN·RTM01과 원천항 12개를 기록한다. IWCAP=8이면 Sswell이 추가된다. (`src/swanpre2.ftn:6334` `ICHECK1=14`; swanuse PDF 119–120쪽 / 인쇄 111–112쪽.)
- Appendix D의 TIME 구조만으로 TEST 파일 전체를 설명하지 않는다. (swanuse PDF 150쪽 / 인쇄 142쪽.)

## 3. 파일 구조 (formal description verbatim 순서)

| 순서 | 내용 |
|---|---|
| 1 | `SWAN` + version number |
| 2 | **nonstat 만**: 키워드 `TIME` |
| 3 | **nonstat 만**: time coding option (ISO `=1` 권장). stationary 면 2-3 부재 |
| 4 | locations: `LOCATIONS`(Cartesian, x-y m problem coord) 또는 `LONLAT`(spherical, lon-lat) + 개수 + 각 location 좌표 |
| 5 | frequency (1D·2D 공통): `AFREQ`(절대) 또는 `RFREQ`(상대) + 개수 + Hz column(줄당 1개) |
| 6 | direction (**2D 만**): `NDIR`(nautical) 또는 `CDIR`(Cartesian) + 개수 + degree column |
| 7 | `QUANT` + quantity 개수 + 각 quantity {name / unit / **exception value**(undefined 시 기록값)} |
| 8 (VVV) | data table: {date-time(nonstat 만)} + location별 spectrum. nonstat 은 VVV 부터 반복 |

## 4. 1D vs 2D quantity 규칙 ★★

### 1D spectrum — 항상 **3 quantity**
순서: ① energy/variance density ② average direction(`CDIR` Cartesian / `NDIR` nautical) ③ directional spreading.
- spreading 키워드: SWAN **write** = `DSPRDEGR`(degrees); SWAN **read** = `DSPRD`/`DEGR`(option DEGREES) 또는 `DSPRP`/`POWER`(option POWER, BOUND SHAPE).
- 각 location: `LOCATION` + index(같은 줄). spectrum undefined(land 등) 시 `NODATA`(이후 숫자 없음).
- table = frequency 당 3열(density / CDIR·NDIR / DSPR).

### 2D spectrum — 항상 **1 quantity**
energy 또는 variance density. 이름: **`EnDens`**(true energy density) / **`VaDens`**(variance density).
- 각 location: 키워드 **`FACTOR`** + 곱할 factor + scaled density table.
  - **true density = table 값 × FACTOR** (예: factor `0.675611E-06`).
  - 밀도 표는 NINT로 반올림한다. (`src/swanser.ftn:5575` `WRITE (NREF, FIX_SPEC) (NINT(ACLOC(ID,IS)/EFAC), ID=1,MDC)`; swanuse PDF 151쪽 / 인쇄 143쪽.)
  - ZERO는 내부 최대 척도가 1E−10 이하일 때도 기록한다. 정확한 0만을 표시하는 조건은 아니다. (`src/swanser.ftn:5564` `IF (EFAC .LE. 1.E-10) THEN`.)
  - 건조점과 보간 실패는 NODATA를 쓴다. (`src/swanout2.ftn:2033` `IF (DEP.LE.0. .OR. EQREAL(DEP,OVEXCV(4))) THEN`; `src/swanout2.ftn:2054–2055` `IF (IERR.GT.0) THEN`, `WRITE (NREF, 220) 'NODATA'`; swanuse PDF 151쪽 / 인쇄 143쪽.) [10-13 전수 검증 보완]

## 5. Exception value 예 (예제 verbatim)

| quantity | unit | exception |
|---|---|---|
| VaDens (1D) | m²/Hz | `-0.9900E+02` (-99) |
| VaDens (2D) | m²/Hz/degr | `-0.9900E+02` |
| CDIR | degr | `-0.9990E+03` (-999) |
| DSPRDEGR | degr | `-0.9000E+01` (-9) |

→ 1D 예제: 25 frequency(0.0418-1.0 Hz), 2 location(LONLAT), VaDens+CDIR+DSPRDEGR. 2D 예제: 25 freq × 12 dir(30-360°), VaDens m²/Hz/degr + FACTOR.

## 6. 연결

- [swan-output-formats](../source-analysis/swan-output-formats.md) — SPEC1D/SPEC2D dispatch + 파일 naming·unit (source-code; 본 노트는 그 파일의 내부 포맷)
- [swan-command-numerics-output-reference](swan-command-numerics-output-reference.md) — `SPECOUT`/`NESTOUT` command 구문 + `BOUNDSPEC`(setup-grid ref)
- [swan-nesting-io-implementation](../source-analysis/swan-nesting-io-implementation.md) — NESTOUT→BOUNDNEST nesting 이 이 spectral 파일로 parent→child 전달
- [swan-output-variable-definitions](swan-output-variable-definitions.md) — EnDens/VaDens/CDIR·NDIR/DSPR quantity 의 적분 정의 (Appendix A)
- [swan-documentation-stack](swan-documentation-stack.md) §7 한계의 swanuse Appendix 잔여(D) 충족
- XBeach는 `read_swan_file`로 SWAN 2D 스펙트럼을 읽는다. (`models/XBeach/raw/source_code/trunk/src/xbeachlibrary/waveparamsnew.F90:936,1048–1094`; [SWAN 파일 입력](../../XBeach/source-analysis/xbeach_swan_handoff.md); [파랑 경계 생성](../../XBeach/source-analysis/xbeach_wave_boundary_generation.md).) EFDC의 GETSWAN_GRP는 `HS PDIR RTP WLEN DEPTH DISSIP`의 SWAN TABLE 출력을 읽는다. (`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Waves/mod_getswan.f90:32–37`; [EFDC 파랑 입력](../../EFDC/source-analysis/efdc_waves.md).) [10-13 전수 검증 정정]

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD `43e9bbb` (2026-07-13 patch B). (`src/swanmain.ftn:965` `VERNUM = 41.51`.)

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R6:O-031 | TEST의 원천항 수 | swanuse PDF 119쪽 / 인쇄 111쪽: `variance densities and 6 source terms`; swanuse PDF 120쪽 / 인쇄 112쪽는 wind, whitecapping, bottom friction, breaking, triads, quadruplets를 나열한다. | `src/swanpre2.ftn:6333–6336` `IF(IWCAP.NE.8)THEN`, `ICHECK1=14`, `ELSE`, `ICHECK1=15`. `src/swanpre2.ftn:6366` `'Svege'`. `src/swanpre2.ftn:6370` `'Sturb'`. `src/swanpre2.ftn:6374` `'Smud'`. `src/swanpre2.ftn:6378` `'Sice'`. `src/swanpre2.ftn:6394` `'Sbragg'`. `src/swanpre2.ftn:6398` `'Sqc'`. `src/swanpre2.ftn:6357` `'Sswell'`. | B 문서 오기 | TEST PAR은 HSIGN·RTM01과 원천항 12개를 쓴다. S1D·S2D는 VaDens와 원천항 12개를 쓴다. IWCAP=8이면 각 파일에 Sswell이 추가된다. |
| R6:O-032 | TEST의 정상 계산 파일 머리말 | swanuse PDF 119쪽 / 인쇄 111쪽: `after every iteration in the case of MODE STATIONARY`. Appendix D, swanuse PDF 150쪽 / 인쇄 142쪽: `The description of the file to write or read source terms is identical to this description except that the quantities obviously differ.`. | `src/swanpre2.ftn:6307` `WRITE (IFPAR, 102) 'ITER', 'iteration-dependent data'`. `src/swanpre2.ftn:6308` `WRITE (IFPAR, 103) 0`. S1D는 6427–6428행에도 같은 ITER·0을 쓴다. `src/swancom2.ftn:3647` `WRITE (IFS1D, 80) 'Test point ', IPTST`. | C 문서 누락 | 정상 TEST 파일은 TIME 대신 ITER와 coding 0을 쓴다. Appendix D의 정식 키워드 설명에는 ITER가 없다. S1D의 점 표식도 일반 SPEC1D의 LOCATION 대신 Test point이다. |
| R6:O-104 | 2D 정수화·FACTOR | swanuse PDF 151쪽 / 인쇄 143쪽: `truncated by SWAN to integer values for compact writing`. 읽는 쪽은 real도 받아야 한다. | `src/swanser.ftn:5568` `EFAC = 1.01 * EFAC * 10.**(-DEC_SPEC)`. `src/swanser.ftn:5575` `WRITE (NREF, FIX_SPEC) (NINT(ACLOC(ID,IS)/EFAC), ID=1,MDC)`. `src/swanmain.ftn:8425–8426` `READ (NDSD,*,END=930,ERR=920)`와 `&             ((BAUX1(IANG,IFRE),IANG=1,NANG),IFRE=1,NFRE)`. | B 문서 오기 | 2D 스펙트럼의 축척 밀도는 절삭하지 않고 NINT로 반올림한다. |
| R6:O-105 | ZERO 임계값·음수 스펙트럼 배율 | swanuse PDF 151쪽 / 인쇄 143쪽: `if the spectrum is identical 0`. | `src/swanser.ftn:5560` `EFAC = MAX (EFAC, 10.*ABS(ACLOC(ID,IS)))`. `src/swanser.ftn:5564` `IF (EFAC .LE. 1.E-10) THEN`. `src/swanser.ftn:5565` `WRITE (NREF, 12) 'ZERO'`. | C 문서 누락 | 정확한 0만 ZERO가 되는 것은 아니다. 양의 최대값과 음의 절댓값 10배 중 최대가 1E−10 이하여도 ZERO이다. 음수 원천항의 부호 자리를 확보하는 배율 처리도 문서에 없다. |
| R6:O-106 | NODATA·1D의 작은 밀도·입력 0 처리 | swanuse PDF 151쪽 / 인쇄 143쪽: `NODATA if the spectrum is undefined`, 예외값은 계산값이 undefined일 때 쓴다. | `src/swanout2.ftn:2033` `IF (DEP.LE.0. .OR. EQREAL(DEP,OVEXCV(4))) THEN`. `src/swanout2.ftn:2035` `&       WRITE (NREF, 220) 'NODATA'`. `src/swanout2.ftn:2054–2055` `IF (IERR.GT.0) THEN`, `WRITE (NREF, 220) 'NODATA'`. `src/swanout2.ftn:2388` `IF (ACLOC(IOM).GT.1.E-12.OR.IQCM.NE.0) THEN`. `src/swanout2.ftn:2401` `ACLOC(IOM)       = OVEXCV(22)`. `src/swanmain.ftn:7905` `IF (HEDLIN(1:6).EQ.'NODATA' .OR. HEDLIN(1:4).EQ.'ZERO')`. `src/swanmain.ftn:7909` `BSPECS(ID,IS,IBSPEC,2) = 0.`. `src/swanout2.ftn:2388–2404`의 정상 분기는 2397행에서 ACLOC에 PI2를 곱한다. `src/swanmain.ftn:7903–7913`은 SWN 형식의 두 표식을 같은 0 대입으로 처리한다. | C 문서 누락 | 건조점과 보간 실패는 NODATA를 쓴다. 1D에서는 `IF (ACLOC(IOM).GT.1.E-12.OR.IQCM.NE.0) THEN`의 ELSE에서 밀도·방향·방향 퍼짐을 모두 예외값으로 쓴다. 따라서 1E−12 임계값에 의한 예외 처리는 IQCM=0일 때 적용된다. 이 임계값은 Hz 단위 변환 전 ACLOC의 값이다. SWN 경계 입력은 ZERO와 NODATA를 모두 0 에너지로 바꾼다. C는 Appendix D에 없는 수치 임계값·입력 변환 규칙에 한정한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 전수 검증 보완] |
| R6:O-107 | 입력의 판 번호·AFREQ/RFREQ | swanuse PDF 150쪽 / 인쇄 142쪽: `the keyword AFREQ or RFREQ (to distinguish between absolute and relative frequencies)`. | `src/swanpre2.ftn:4095` `ELSE IF (EQCSTR(HEDLIN,'SWAN')) THEN`. 4097행은 바로 다음 행을 읽는다. `src/swanpre2.ftn:4185` `IF (EQCSTR(HEDLIN(2:5),'FREQ')) THEN`. | C 문서 누락 | 스펙트럼 reader는 SWAN 표식 뒤 판 번호를 검사하지 않는다. AFREQ와 RFREQ의 첫 글자로 읽기 경로를 구별하지 않는다. |
| R6:O-108 | 입력 예외값·단위·방향 퍼짐 복원 | swanuse PDF 151쪽 / 인쇄 143쪽: 물리량마다 `unit of the quantity`, `exception value of the quantity`가 있다. | `src/swanpre2.ftn:4321` `BSPFIL%BFILED(11) = NINT(EXCV)`. `src/swanpre2.ftn:4323` `READ (NDSD, '(A)') HEDLIN`. `src/swanmain.ftn:8316` `IF (EQREAL(ETOT,REAL(BFILED(11)))) THEN`. `src/swanmain.ftn:8342` `MS = MAX (FAC*DSPR**(-2) - 2., 1.)`. | C 문서 누락 | 밀도 예외값만 정수로 반올림해 저장한다. 방향·방향 퍼짐의 예외값 행은 읽고 버린다. 밀도 단위 문자열 대신 EnDens/VaDens 이름으로 ρg 변환을 선택한다. degree 입력의 cos 지수 복원은 구간별 FAC=1.2/1.096/1.01 근사식이다. POWER 입력은 지수를 그대로 쓴다. |
| R6:O-111 | 자유 형식과 행 뒤 설명 | swanuse PDF 150쪽 / 인쇄 142쪽: `all information on each line after the required input for SWAN is ignored by SWAN.` | `src/swanmain.ftn:8425` `READ (NDSD,*,END=930,ERR=920)`. `src/swanmain.ftn:8426` `&             ((BAUX1(IANG,IFRE),IANG=1,NANG),IFRE=1,NFRE)`. | B 문서 오기 | 2D 밀도 표 전체를 하나의 list-directed READ로 읽는다. 각 주파수 행 뒤에 임의의 설명을 붙여도 무시된다고 보장할 수 없다. 머리말의 단일 행 READ와 전체 표 READ를 구분해야 한다. |
| R6:O-140 | TEST S2D의 건조점 블록 수 | swanuse PDF 120쪽 / 인쇄 112쪽: `The format of this file is defined in Appendix D.`. Appendix D swanuse PDF 151쪽 / 인쇄 143쪽의 `NODATA`는 미정의 스펙트럼을 나타낸다. | `src/swancom2.ftn:3732` `IF (DEP2(INDX).LE.0.) THEN`. `src/swancom2.ftn:3733` `DO LOOP = 1, 10`. `src/swancom2.ftn:3734` `WRITE (IFS2D, 80) 'NODATA'`. `src/swanpre2.ftn:6592` `ICHECK1=13`. `src/swanpre2.ftn:6594` `ICHECK1=14`. `src/swanpre2.ftn:6235–6238`은 비구조 격자의 범위 안 시험점 번호를 수심 검사 없이 등록한다. `src/swancom1.ftn:2232–2248,2429–2446`은 시험점이 있는 정상·비정상 경로에서 PLTSRC를 호출한다. `src/swancom2.ftn:3525–3531`은 등록 시험점을 순회한다. git 원문 `b2ae30e:src/swancom2.ftn:3643`의 10회 반복은 `7ee8981:src/swancom2.ftn:3733`과 `43e9bbb:src/swancom2.ftn:3733`에도 유지된다. [SWAN-git-verify-E](../../../_staging/recovery/compare/SWAN-git-verify-E.md)의 확정 판정은 E 유지(강함)이다. | E 코드 결함 후보 (강함) | TEST S2D는 `IF (DEP2(INDX).LE.0.) THEN`에서 NODATA를 10개 기록한다. 머리말은 13개 물리량을 선언하며 IWCAP=8이면 14개를 선언한다. 등록된 건조 시험점이 PLTSRC에 도달하는 경로가 있다. 이 건조점 분기에는 전처리 표식이 없다. 뒤따르는 지점·시간의 블록 해석을 어긋나게 할 수 있는 강한 정적 결함 후보이다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R6:N-018 | 정수화·ZERO | `models/SWAN/manual-notes/swan-spectral-file-format.md:60`: `정수로 truncate`. 61행: `identical 0`.<br>swanuse PDF 151쪽 / 인쇄 143쪽: `truncated by SWAN to integer values for compact writing`. 읽는 쪽은 real도 받아야 한다.<br>swanuse PDF 151쪽 / 인쇄 143쪽: `if the spectrum is identical 0`. | O-104·O-105. `src/swanser.ftn:5575` `WRITE (NREF, FIX_SPEC) (NINT(ACLOC(ID,IS)/EFAC), ID=1,MDC)`. `src/swanser.ftn:5564` `IF (EFAC .LE. 1.E-10) THEN`. | B 문서 오기 | 밀도 표는 NINT로 반올림한다. ZERO는 내부 최대 척도가 1E−10 이하일 때도 기록한다. 정확한 0만을 표시하는 조건은 아니다. |
| R6:N-019 | 파일 인식·행 뒤 주석 | `models/SWAN/manual-notes/swan-spectral-file-format.md:21`: `first line 의 SWAN+version 으로 인식`. 31행: `line 의 필수 입력 이후 정보는 무시`.<br>swanuse PDF 150쪽 / 인쇄 142쪽: `all information on each line after the required input for SWAN is ignored by SWAN.` | O-107·O-111. `src/swanout2.ftn:1866` `INTEGER, SAVE :: IVERF = 1`; `src/swanout2.ftn:1907` `WRITE (NREF, 101) IVERF`; `src/swanpre2.ftn:4095` `ELSE IF (EQCSTR(HEDLIN,'SWAN')) THEN`. `src/swanmain.ftn:8426` `&             ((BAUX1(IANG,IFRE),IANG=1,NANG),IFRE=1,NFRE)`. | B 문서 오기 | writer는 SWAN 1을 쓰지만 reader는 SWAN 표식 뒤의 판 번호를 검사하지 않는다. 2D 밀도 표는 전체 배열을 한 READ로 읽는다. 표의 각 주파수 행 뒤에 임의의 설명을 붙일 수 있다고 일반화하지 않는다. [10-13 전수 검증 보완] |
| R6:N-020 | TEST 파일 예외 | `models/SWAN/manual-notes/swan-spectral-file-format.md:33`: `source term 파일도 동일 포맷(quantity 만 다름)`.<br>swanuse PDF 119쪽 / 인쇄 111쪽: `after every iteration in the case of MODE STATIONARY`. Appendix D, swanuse PDF 150쪽 / 인쇄 142쪽: `The description of the file to write or read source terms is identical to this description except that the quantities obviously differ.`. | O-031·O-032. `src/swanpre2.ftn:6307` `WRITE (IFPAR, 102) 'ITER', 'iteration-dependent data'`. `src/swanpre2.ftn:6334` `ICHECK1=14`. | C 문서 누락 | 정상 TEST 파일은 ITER와 coding 0을 사용한다. PAR은 HSIGN·RTM01과 원천항 12개를 기록한다. IWCAP=8이면 Sswell이 추가된다. Appendix D의 TIME 구조만으로 TEST 파일 전체를 설명하지 않는다. |
