---
title: "SWAN swanuse §4.4-4.5.3 command reference — start-up(PROJECT/SET/MODE/COORD) + grid(CGRID/READGRID) + input(INPGRID/READINP/WIND) + BC/IC(BOUND/INITIAL) verbatim"
topic: swan
canonical_source: external
external_source: "swanuse.pdf (User Manual, SWAN Cycle III version 41.51) §4.4 Start-up + §4.5.1 grid + §4.5.2 input + §4.5.3 BC/IC (p.26-56) + node23/25/26/27.md. command 구문·파라미터·default."
citation_status: verified
verification_method: "swanuse website_markdown node23(Start-up 278줄)/node25(CGRID 275)/node26(input 599)/node27(BC/IC 609) 직접 read: PROJECT/SET/MODE/COORDINATES/CGRID/READGRID/INPGRID/READINP/WIND/ICE/BOUND/BOUNDSPEC/INITIAL 구문+default verbatim. 2026-10-13 recovery 대조 보고서 R1–R8 반영."
last_source_check: 2026-10-13 (recovery 대조 반영)
note_author: "Claude Opus 4.8 (1M context) raw markdown direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — command 구문·default 값 verbatim"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/manual-notes/swan-command-physics-reference.md
  - models/SWAN/manual-notes/swan-command-numerics-output-reference.md
  - models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md
---

# SWAN swanuse §4.4-4.5.3 setup/grid/input/BC command reference — verified

> swanuse.pdf (User Manual v41.51) §4.4-4.5.3 직접 read. SWAN 입력파일의 **설정·격자·입력데이터·경계/초기조건** command 구문·default. Physics command 는 [swan-command-physics-reference](swan-command-physics-reference.md), numerics/output 은 [swan-command-numerics-output-reference](swan-command-numerics-output-reference.md).

## 1. §4.4 Start-up

### 1.1 PROJECT
```
PROJECT 'name' 'nr'
'title1'
'title2'
'title3'
```
첫 줄에 PROJECT·name·nr를 쓴다. title1·title2·title3는 각각 다음 줄에 쓴다. `src/swanpre1.ftn:526` `CALL NWLINE`.

NAME 생략은 최초 SWAN 값을 유지한다. `src/swanmain.ftn:986` `PROJID = 'SWAN'`; `src/swanpre1.ftn:524` `CALL INCSTR ('NAME', PROJID, 'UNC', BLANK)`.

### 1.2 SET — general parameters
```
SET [level] [nor] [depmin] [maxmes] [maxerr] [grav] [rho] [cdcap] [uscap] [inrhog] [hsrerr] <NAUTical|CARTesian> [pwtail] [froudmax] [icewind] [excmark]
```
| param | default | 의미 |
|---|---|---|
| `[level]` | 0 | 공간·시간 일정 수위 상승 (m) |
| `[nor]` | 90° | 북쪽 방향 (x축 기준 반시계). spherical 시 변경 불가 |
| `[depmin]` | **0.05 m** | 임계값 이하의 활성점에서는 파 작용밀도를 0으로 만든다. `src/swanmain.ftn:1139` `DEPMIN = 0.05`; `src/swancom1.ftn:3289` `IF (KCGRD(1).LE.1 .OR. COMPDA(KCGRD(1),JDP2).LE.DEPMIN) THEN`; `src/swancom1.ftn:3292` `AC2(ID,IS,KCGRD(1)) = 0.`. |
| `[maxmes]` | 200 | MAXMES는 200으로 초기화하고 입력을 읽지만 중단 검사에 쓰지 않는다. `src/swanmain.ftn:1625` `MAXMES = 200`; `src/swanpre1.ftn:2173` `CALL ININTG ('MAXMES', MAXMES, 'UNC', 0)`; `src/swmod1.ftn:2842` `! MAXMES [   200] not used`. |
| `[maxerr]` | 1 | 계산 시작을 막는 조건은 `IF (LEVERR.GT.MAXERR) THEN`이다. MAXERR와 같은 수준은 이 검사에서 허용한다. swanuse PDF 36쪽 / 인쇄 28쪽: “at the level indicated the computations will continue”. `src/swanmain.ftn:521` `IF (LEVERR.GT.MAXERR) THEN`. |
| `[grav]` | 9.81 | 중력가속도 |
| `[rho]` | **1025** | 물 밀도 kg/m³ |
| `[cdcap]` | 99999 | CDCAP은 모든 항력 분기에 공통인 최종 상한이 아니다. `src/swanmain.ftn:1009` `CDCAP  = 99999.`; `src/swancom3.ftn:920` `CDRAG = MIN ( CDCAP, CDRAG )`; `src/swancom3.ftn:922` `CDRAG = 0.0012875`. |
| `[uscap]` | 99999 | USCAP으로 제한한 뒤 CDFAC의 제곱근을 곱한다. `src/swanmain.ftn:1010` `USCAP  = 99999.`; `src/swancom3.ftn:1074` `UFRIC = MIN(USCAP,UFRIC) * SQRT(CDFAC)`. |
| `[inrhog]` | 0 | 출력 0=variance / 1=true energy |
| `[hsrerr]` | 0.10 | Hs 부합 경고 임계 (structured only) |
| NAUTICAL / **CARTESIAN** | CARTESIAN | wind/wave 방향 convention |
| `[pwtail]` | GEN3 KOMEN/WESTH **4**, GEN1/2/JANSSEN 5 | 에너지 꼬리는 주파수 비의 음의 PWTAIL 거듭제곱이다. GEN1·GEN2·JANSSEN의 해당 초기화는 PWTAIL이 4일 때 5로 바꾼다. 원하는 값을 보장하려면 GEN 뒤에서 SET PWTAIL을 지정한다. `src/swancom1.ftn:7600` `FACHFR = 1. / XIS ** PWTAIL(1)`; `src/swanpre1.ftn:2826` `IF (EQREAL(PWTAIL(1),4.)) THEN`; `src/swanpre1.ftn:2827` `PWTAIL(1) = 5.`. |
| `[froudmax]` | 0.8 | FROUDMAX는 유속 크기의 상한을 정한다. `IF (VTOT .GT. CGMAX) THEN`에서 유속 성분을 같은 비율로 줄인다. `src/swanmain.ftn:4917` `CGMAX = PNUMS(18)*SQRT(GRAV*DEPW)`; `src/swanmain.ftn:4918` `IF (VTOT .GT. CGMAX) THEN`; `src/swanmain.ftn:4919` `CGFACT = CGMAX / VTOT`; `src/swanmain.ftn:4920` `UU = UU * CGFACT`; `src/swanmain.ftn:4921` `VV = VV * CGFACT`. |
| `[icewind]` | 0 | 0=wind input × open water fraction / 1=ice 무영향 |
| `[excmark]` | 999 | unstructured boundary vertex 제외 marker |

### 1.3 MODE
```
MODE <-> STATionary | NONSTationary> <-> TWODimensional | ONEDimensional>
```
**default STATIONARY TWODIMENSIONAL**. Nonstationary = (a)단일 nonstat (b)연속 stationary 시퀀스 (c)혼합 (COMPUTE).

### 1.4 COORDINATES
```
COORDINATES <-> CARTesian | SPHErical <-> CCM | QC>> REPeating
```
- **CARTESIAN default** (m). **SPHERICAL** (degrees, x=longitude Greenwich, y=latitude N; CCM=central conformal Mercator / QC=quasi-cartesian)
- nested run = coarse grid 와 동일 좌표계. spherical regular grid 는 E-W/N-S 정렬(alpc=alpinp=alpfr=0)
- REPEATING (academic, x방향 주기경계; SETUP 불가, regular only)

## 2. §4.5.1 Computational grid

### 2.1 CGRID (required)
```
CGRID <-> REGular [xpc][ypc][alpc][xlenc][ylenc][mxc][myc] | CURVilinear [mxc][myc] (EXCeption [xexc][yexc]) | UNSTRUCtured> <-> CIRcle | SECtor [dir1][dir2]> [mdc][flow][fhigh][msc]
```
- **REGULAR**(uniform rect, xpc/ypc origin, alpc=0 방향, xlenc/ylenc 길이, mxc/myc mesh 수=격자점−1) / **CURVILINEAR**(READGRID COOR, EXCEPTION xexc 무시점) / **UNSTRUCTURED**(READGRID UNSTRUC, [swan-tech-ch8-unstructured-grid-scheme](swan-tech-ch8-unstructured-grid-scheme.md))
- **spectral**: **CIRCLE default**(전원, Δθ=360/mdc) / SECTOR `[dir1][dir2]` (Δθ=(dir2−dir1)/mdc). ⚠ **quadruplet(GEN3) 시 SECTOR는 spectrum sector보다 양쪽 30° 넓게** (아니면 부정확)
- `mdc` = θ mesh 수 (**최소 3/quadrant**), `flow`/`fhigh` = 최저/최고 주파수(Hz), `msc` = 주파수 수−1 (**logarithmic** $f_{i+1}=\gamma f_i$, $\Delta f/f = \gamma−1$, msc=log(fhigh/flow)/log(1+Δf/f))
- 문서의 최소 4는 주파수 개수이다. msc는 주파수 개수보다 1 작다. swanuse PDF 40–41쪽 / 인쇄 32–33쪽: “minimum number of frequencies is 4”. `src/swanpre1.ftn:1768` `MSC  = MSS+1`.
- 중첩 경계의 지리적 위치는 맞아야 한다. 스펙트럼 격자는 다를 수 있다. 파일 최고 주파수 위에는 PWTAIL의 진단 꼬리를 붙일 수 있다. `src/swanmain.ftn:8485` `IF (IS.LE.ISIGTA) THEN`; `src/swanmain.ftn:8495` `(SPCSIG(ISIGTA)/SPCSIG(IS))**(PWTAIL(1)+1)`.

### 2.2 READGRID
```
READGRID COORdinates [fac] 'fname' [idla] [nhedf] [nhedvec] <FREE|FORMAT|UNFORMAT>
READGRID UNSTRUCtured <TRIAngle 'fname' | EASYmesh 'fname' | -> ADCirc>
```
curvilinear 좌표 / unstructured mesh (Triangle·Easymesh·ADCIRC fort.14, [swan-grid-readers](../source-analysis/swan-grid-readers.md)).

ADCIRC는 fort.14를 읽는다. fname은 Triangle·Easymesh의 확장자 없는 이름이다. swanuse PDF 43쪽 / 인쇄 35쪽: 기본 `ADCirc`; “‘fname’ basename … without extension.” `src/swanpre1.ftn:1478` `CALL INKEYW ('STA', 'ADC')`; `src/SwanReadADCGrid.ftn90:95` `grdfil = 'fort.14'`.

## 3. §4.5.2 Input grids and data

### 3.1 INPGRID
```
INPgrid <BOTtom|WLEVel|CURrent|FRiction|WInd|AICE|HICE|...> <-> REGular [xpinp][ypinp][alpinp][mxinp][myinp][dxinp][dyinp] | CURVilinear [stagrx][stagry][mxinp][myinp] | UNSTRUCtured> (EXCeption [excval]) (NONSTATionary [tbeginp][deltinp]<SEC|MIN|HR|DAY>[tendinp])
```
입력 데이터(수심 BOTTOM, 수위, 유속, friction, wind, ice 등)별 격자 정의. REGULAR(xpinp origin, alpinp 방향, mxinp/myinp/dxinp/dyinp) / CURVILINEAR(stagrx/y stagger) / UNSTRUCTURED. NONSTATIONARY (시간 tbeginp~tendinp, deltinp 간격).

### 3.2 READINP
```
READinp <BOTtom|WLEVel|CURrent|FRiction|WInd|AICE|HICE|...> [fac] 'fname' [idla] [nhedf] [nhedt] [nhedvec] <FREE|FORMAT|UNFORMAT>
```
`fac` = 곱 factor, `idla` = layout(1-6 격자 방향/순서), `nhedf/nhedt` = header 줄 수.

### 3.3 WIND / ICE (constant)
```
WIND [vel] [dir]        ! 10m 풍속(m/s) + 방향(deg, NAUTICAL/CARTESIAN)
ICE  [aice] [hice]      ! ice fraction + thickness
```
공간 얼음 입력은 INPGRID AICE·HICE와 READINP AICE·HICE를 사용한다. ICE는 aice·hice 상수를 받는 별도 명령이다. `src/swanpre1.ftn:1404` `ELSE IF (KEYWIS ('AICE')) THEN`; `src/swanpre1.ftn:1408` `ELSE IF (KEYWIS ('HICE')) THEN`. [swan-tech-ch2-sources-sinks](swan-tech-ch2-sources-sinks.md) wind input.

## 4. §4.5.3 Boundary and initial conditions

### 4.1 BOUND SHAPESPEC (스펙트럼 형상)
```
BOUnd SHAPespec <-> JONswap [gamma] | TMA [gamma] [d] | PM | GAUSs [sigfr] | BIN> <-> PEAK | MEAN> <-> DSPR POWer | DEGRees>
```
경계 parametric spectrum 형상: **JONSWAP**(default gamma=3.3)/TMA/Pierson-Moskowitz/Gaussian/BIN, peak vs mean frequency, directional spread (power vs degrees).

TMA [gamma] [d]를 추가한다. swanuse PDF 55쪽 / 인쇄 47쪽: `TMA`. `src/swanpre2.ftn:2816` `FSHAPE = 5`. GAUSS의 기본값은 0.01 Hz이다. `src/swanpre2.ftn:2812` `CALL INREAL ('SIGFR', SIGMAG, 'STA', 0.01)`.

### 4.2 BOUNDSPEC (경계 스펙트럼 지정)
```
BOUNDSPEC <SIDE <N|NW|...>|SEGMENT ...> <CONSTANT|VARIABLE> <PAR [hs][per][dir][dd]|FILE 'fname'>
```
- side/segment 별 parametric(PAR: Hs/period/dir/directional spread dd) 또는 file 스펙트럼. 여러 BOUNDSPEC 로 다측 경계 (한 command = 한 side/segment)

### 4.3 BOUNDNEST1/2/3 (nesting)
```
BOUNDNEST1 NEST 'fname' <CLOSED|OPEN>       ! SWAN coarse → nested
BOUNDNEST2 WAMNEST 'fname' ...               ! WAM
BOUNDNEST3 WWIII 'fname' ...                 ! WAVEWATCH III
```
대모델(SWAN/WAM/WW3) 경계 스펙트럼을 nested run 에 (CGRID 먼저). 1D 불가.

### 4.4 INITIAL
```
INITial <-> DEFAULT | ZERO | PAR [hs][per][dir][dd] | HOTStart <MULTiple|SINGle> 'fname' <FREE|UNFormatted>>
```
- **DEFAULT** = 2nd-gen first guess (stationary) / Kahma-Calkoen growth (nonstat, [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) §A.4) / **ZERO**(무파) / **PAR**(균일 parametric) / **HOTSTART**(이전 run hotfile, MPI MULTIPLE/SINGLE)

## 5. command 순서 (§4.2)

`PROJECT → SET → MODE → COORDINATES → CGRID → (READGRID) → INPGRID/READINP (각 입력) → WIND/ICE → BOUND/BOUNDSPEC/BOUNDNEST → INITIAL → [physics] → [numerics] → output locations → output quantities → COMPUTE → STOP`

## 6. 입력 옵션 대조

- IDLA 5·6은 각 열을 아래에서 위로 읽는다. `src/ocpmix.ftn:985` `&               ((ARR(IX,IY), IY=1,MYA), IX=1,MXA)`.
- TENDINP를 생략하면 내부 종료 시각은 1.D20이다. `src/swanpre1.ftn:4015` `CALL INCTIM (ITMOPT,'TENDINP',IFLEND(IGRID1),'STA',1.D20)`.
- COMPUTE/HOTFILE/STOP + NUMERIC/PROP + output(FRAME/BLOCK/TABLE/QUANTITY) → [swan-command-numerics-output-reference](swan-command-numerics-output-reference.md).

## 7. 연결

- [swan-command-physics-reference](swan-command-physics-reference.md) — §4.5.4 physics (GEN/WCAPPING/...)
- [swan-command-numerics-output-reference](swan-command-numerics-output-reference.md) — §4.5.5-4.7 numerics/output/lock-up
- [swan-documentation-stack](swan-documentation-stack.md) — 4 docs + 57 command 목록
- [swan-grid-readers](../source-analysis/swan-grid-readers.md) — READGRID UNSTRUCTURED (ADCIRC/Triangle/Easymesh)
- [swan-tech-ch4-5-bc-2d-setup](swan-tech-ch4-5-bc-2d-setup.md) — BC/IC 이론 (Ch 4)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

빈 인용 칸은 `—`로 표시한다. 표의 절 번호는 각 행이 링크한 대조 보고서의 절 번호다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R4:T1-024 | 시간 가변 BOTTOM | swanuse PDF 18–19쪽 / 인쇄 10–11쪽: “bathymetry … may be time varying”. | `src/swanpre1.ftn:4011` `IF (IGRID1.EQ.1 .OR. IGRID1.EQ.8) CALL MSGERR (2,`; `src/swanpre1.ftn:4012` `&        'nonstationary input field not allowed in this case')` | B 문서 오기 | 시간 가변 수위와 시간 가변 BOTTOM 입력을 구분한다. 후자는 이 명령 경로에서 금지한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-050 | PROJECT 이름 기본값 | swanuse PDF 35쪽 / 인쇄 27쪽: “‘name’ is the name of the project, at most 16 characters long. Default: blanks.” | `src/swanpre1.ftn:524` `CALL INCSTR ('NAME', PROJID, 'UNC', BLANK)`; `src/swanmain.ftn:986` `PROJID = 'SWAN'`; `src/swmod1.ftn:261` `CHARACTER (LEN=16)     :: PROJID`; `src/ocpcre.ftn:1004` `IF (KONT.EQ.'UNC') GOTO 80` | B 문서 오기 | NAME 생략은 최초 SWAN 값을 유지한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-054 | DEPMIN 설명 | swanuse PDF 35쪽 / 인쇄 27쪽: “In the computation any positive depth smaller than [depmin] is made equal to [depmin].” “Default: [depmin] = 0.05.” | `src/swanpre1.ftn:2172` `CALL INREAL ('DEPMIN', DEPMIN, 'UNC', 0.)`; `src/swanmain.ftn:1139` `DEPMIN = 0.05`; `src/swancom1.ftn:3289` `IF (KCGRD(1).LE.1 .OR. COMPDA(KCGRD(1),JDP2).LE.DEPMIN) THEN`; `src/swancom1.ftn:3292` `AC2(ID,IS,KCGRD(1)) = 0.`; `src/swancom1.ftn:3296` `RETURN` | B 문서 오기 | DEPMIN은 건조점의 파 작용밀도 제거 조건에 사용된다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-055 | MAXMES 중단 | swanuse PDF 35–36쪽 / 인쇄 27–28쪽: “maximum number of error messages … at which the computation is terminated.” “Default: [maxmes] = 200.” | `src/swanpre1.ftn:2173` `CALL ININTG ('MAXMES', MAXMES, 'UNC', 0)`; `src/swanmain.ftn:1625` `MAXMES = 200`; `src/swmod1.ftn:2842` `! MAXMES [   200] not used`; `src/ocpmix.ftn:1358` `IF (LEV.GT.LEVERR) LEVERR=LEV`; `src/ocpmix.ftn:1372` `IF (LEV.GT.MAXERR) THEN` | D 문서에만 있음 | MAXMES 입력값은 저장되지만 메시지 개수에 따른 중단에는 쓰이지 않는다. MAXERR와 LEVERR는 오류 심각도를 비교하므로 MAXMES의 다른 이름이 아니다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-058 | CDCAP 적용 범위 | swanuse PDF 36쪽 / 인쇄 28쪽: “the maximum value for the wind drag coefficient”; “Default: [cdcap] = 99999.” | `src/swanpre1.ftn:2177` `CALL INREAL ('CDCAP',  CDCAP,  'UNC', 0.)`; `src/swanmain.ftn:1009` `CDCAP  = 99999.`; `src/swancom3.ftn:920` `CDRAG = MIN ( CDCAP, CDRAG )`; `src/swancom3.ftn:918` `IF ( WIND10 .GT. 7.5 ) THEN`; `src/swancom3.ftn:922` `CDRAG = 0.0012875`; `src/swancom3.ftn:1074` `UFRIC = MIN(USCAP,UFRIC) * SQRT(CDFAC)`; `src/swancom3.ftn:916` `IF ( IDRAG.EQ.1 ) THEN`; `src/swancom3.ftn:1059` `ELSE IF (IDRAG.EQ.4) THEN` | C 문서 누락 | CDCAP은 모든 항력 분기에 공통인 최종 상한이 아니다. `swancom3.ftn`의 1·2세대 풍파·predictor 경로에서는 Wu의 낮은 풍속 분기에 고정 항력계수를 쓴다. Hwang 경로에서는 마찰속도에 USCAP을 적용한 뒤 CDFAC을 반영한다. C 판정은 U의 SET CDCAP 설명에 빠진 적용 조건에 한정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-060 | SET의 위치 입력 | swanuse PDF 35쪽 / 인쇄 27쪽: `SET [level] [nor] [depmin] [maxmes] [maxerr] [grav] [rho] [cdcap] [inrhog]`; swanuse PDF 133쪽 / 인쇄 125쪽: “in the same order as they appear in the command scheme.” 반면 swanuse PDF 135쪽 / 인쇄 127쪽 및 웹 `swanuse/node49.html:63`은 `[cdcap] [uscap] [inrhog]`이다. | `src/swanpre1.ftn:2178` `CALL INREAL ('USCAP',  USCAP,  'UNC', 0.)`; `src/swanpre1.ftn:2179` `CALL ININTG ('INRHOG', INRHOG, 'UNC', 0)`; `misc/swan.edt:7` `!        [maxerr]  [grav]  [rho]  [cdcap]  [uscap]  [inrhog]                &` | C 문서 누락 | SET §4.4 본문의 문법표는 CDCAP과 INRHOG 사이의 USCAP을 빠뜨렸다. Appendix C와 소스 편집 템플릿에는 USCAP이 있다. 본문 표대로 위치 수치를 쓰면 INRHOG로 의도한 값이 USCAP에 들어간다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-061 | PWTAIL 부호 | swanuse PDF 36–37쪽 / 인쇄 28–29쪽: “The energy density is assumed to be proportional to frequency to the power [pwtail].” 기본값은 GEN1·GEN2·JANSSEN에서 5이고 KOMEN·WESTH에서 4이다. | `src/swanpre1.ftn:2192` `CALL INREAL ('PWTAIL', PWTAIL(1), 'UNC', 0.)`; `src/swanpre1.ftn:2194` `IF (PWTAIL(1).LE.1.) CALL MSGERR (3, 'Incorrect PWTAIL')`; `src/swanmain.ftn:1019` `PWTAIL(1) = 4.`; `src/swancom1.ftn:7600` `FACHFR = 1. / XIS ** PWTAIL(1)` | B 문서 오기 | 양수 PWTAIL은 주파수에 대한 감소 지수의 크기이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-062 | GEN의 PWTAIL 덮어쓰기 | swanuse PDF 37쪽 / 인쇄 29쪽 및 웹 `swanuse/node23.html:440–448`: “this SET command should be located in the command file after the GEN1, GEN 2 or GEN3 command (these will override the SET command with respect to [pwtail])”. | `src/swanpre1.ftn:2825` `!       if [pwtail] is not changed, make it 5`; `src/swanpre1.ftn:2827` `PWTAIL(1) = 5.`; `src/swanpre1.ftn:2826` `IF (EQREAL(PWTAIL(1),4.)) THEN` | C 문서 누락 | GEN1·GEN2·GEN3 JANSSEN은 앞선 SET의 PWTAIL이 정확히 4일 때만 5로 바꾼다. 4가 아닌 값은 유지한다. 문서의 'override'는 이 조건을 적지 않는다. SET을 GEN 뒤에 두라는 지침은 유효하다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-084 | XEXC 필수·기본값 | swanuse PDF 40쪽 / 인쇄 32쪽: `[xexc]` “Required if the option EXCEPTION is used. Default: [xexc] = 0.0.” `[yexc]`에도 “Required if the option EXCEPTION is used.”와 “Default: [yexc] = [xexc].”가 함께 있다. | `src/swanpre1.ftn:1714` `IF (OPTG.EQ.3) THEN`; `src/swanpre1.ftn:1717` `CALL INREAL ('EXCVAL', EXCFLD(8), 'REQ', 0.)`; `src/swanpre1.ftn:1718` `CALL INREAL ('EXCVAL', EXCFLD(9), 'STA', EXCFLD(8))` | B 문서 오기 | EXCEPTION의 첫 값은 필수이다. 누락 오류 뒤의 0을 생략 기본값으로 안내하지 않는다. 두 번째 값은 생략할 수 있으며 첫 값으로 대체된다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-085 | XEXC·YEXC 이름 | swanuse PDF 39–40쪽 / 인쇄 31–32쪽: `EXCeption [xexc] [yexc]`; swanuse PDF 132쪽 / 인쇄 124쪽: “Copy the name of the variable … literally followed by an = sign”. | `src/swanpre1.ftn:1717` `CALL INREAL ('EXCVAL', EXCFLD(8), 'REQ', 0.)`; `src/swanpre1.ftn:1718` `CALL INREAL ('EXCVAL', EXCFLD(9), 'STA', EXCFLD(8))`; `misc/swan.edt:19` `!         <  CURVilinear [mxc] [myc]  (EXC [xexc] [yexc]) [alpc]     >      &`; `src/ocpcre.ftn:609` `IF (NAAM.NE.ELTEXT(1:LENNM)) GOTO 20` | B 문서 오기 | 이름 지정 입력 XEXC·YEXC는 현재 리더 이름 EXCVAL과 다르다. 위치 입력은 수용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-088 | γ=1.1의 반올림 | swanuse PDF 41쪽 / 인쇄 33쪽: `[flow] and [msc]`, `[fhigh] and [msc]`, `[flow] and [fhigh]`; “such that γ = 1.1”. | `src/swanpre1.ftn:1754` `MSS = NINT(ALOG(FRHIG/FRLOW)/ALOG(1.1))`; `src/swanpre1.ftn:1758` `FRLOW = FRHIG/EXP(ALOG(1.1)*REAL(MSS))`; `src/swanpre1.ftn:1762` `FRHIG = FRLOW*EXP(ALOG(1.1)*REAL(MSS))`; `src/swanpre1.ftn:1746` `&                 'At least, FLOW and FHIGH or MSC must be given!')`; `src/swanpre1.ftn:4685` `FRINTF = ALOG(SHIG/SLOW) / FLOAT(MSC-1)`; `src/swanpre1.ftn:4686` `SFAC   = EXP(FRINTF)`; `src/swanpre1.ftn:4691` `SPCSIG(IS) = SPCSIG(IS-1) * SFAC` | C 문서 누락 | 문서의 로그 주파수 격자 관계식은 코드와 부합한다. 빠진 내용은 메시 수의 정수 반올림이다. 양끝 주파수만 지정하면 MSS를 반올림한 뒤 양끝으로 비를 다시 정하므로 실제 주파수 비는 정확히 1.1이 아닐 수 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-089 | 최소 분해능·SECTOR 여유 | swanuse PDF 40–41쪽 / 인쇄 32–33쪽: “SECTOR should be 30° wider on each side”; “minimum number of directional bins is 3 per directional quadrant”; “minimum number of frequencies is 4”; “[flow] = 0.03 Hz is recommended”. | `src/swanpre1.ftn:1730` `CALL ININTG('MDC',MDC,'RQI',0)`; `src/swanmain.ftn:6617` `CALL MSGERR(1,'It is not recommended to use quadruplets'     )`; `src/swanmain.ftn:6618` `CALL MSGERR(1,'in combination with calculations on a sector.')` | H 코드 대조 대상 아님 | 수치·정확도 요구와 권고를 명령 읽기의 자동 검사와 구분한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-095 | 비정규 격자 경고 조건 | swanuse PDF 43쪽 / 인쇄 35쪽: “should not be smaller than 4 or larger than 10”; “angles … should not be higher than 143°”; “SWAN will print an error message.” swantech PDF 144 / 인쇄 136 §8.1.3에도 셀 수·각도 조건이 있다. ITEST의 출력 조건은 적지 않는다. | `src/SwanCheckGrid.ftn90:106` `if ( noc > 0 .and. noc < 4 .and. vmark(i) == 0 ) then`; `src/SwanCheckGrid.ftn90:111` `if ( noc > 10 ) then`; `src/SwanCheckGrid.ftn90:118` `if ( badvertex ) call msgerr (1, 'number of cells around vertex is smaller than 4 or larger than 10')`; `src/SwanCheckGrid.ftn90:151` `if ( .not. cosphi1 > -0.8 .and. ITEST >= 100 ) then`; `src/SwanCheckGrid.ftn90:154` `call msgerr (1, trim(msgstr) )`; `src/SwanCheckGrid.ftn90:157` `if ( .not. cosphi2 > -0.8 .and. ITEST >= 100 ) then`; `src/SwanCheckGrid.ftn90:163` `if ( .not. cosphi3 > -0.8 .and. ITEST >= 100 ) then` | C 문서 누락 | 삼각형 각도 경고는 ITEST≥100일 때 출력한다. 경고 수준은 1이다. C는 품질 기준 자체가 아니라 진단을 출력하는 조건의 누락이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-096 | 45°–135° 권고 | swanuse PDF 42쪽 / 인쇄 34쪽: “It is recommended to use grids with angles between 45 and 135 degrees.” | — | H 코드 대조 대상 아님 | 권고 각도 범위는 CVCHEK의 오류 조건과 다르다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-097 | SECTOR 30° 메시지 | swanuse PDF 40쪽 / 인쇄 32쪽: “30° wider on each side”. 직접 비교할 코드 내부 경고는 “sector of less than 30 degrees”이다. | `src/swanmain.ftn:6610` `IF ((SPDIR2-SPDIR1) .LT. (PI/12.)) THEN`; `src/swanmain.ftn:6612` `CALL MSGERR(2,'sector of less than 30 degrees should be'     )`; `src/swanpre1.ftn:1786` `SPDIR1 = SPDIR1 * PI / 180.`; `src/swanpre1.ftn:1787` `SPDIR2 = SPDIR2 * PI / 180.`; `src/swanmain.ftn:6607` `IF (IQUAD .GE. 1) THEN`; `src/swanmain.ftn:6609` `IF (.NOT. FULCIR) THEN` | E 코드 결함 후보·중간 | 4파 상호작용과 SECTOR를 함께 쓸 때 구체적인 경고 문장은 30°를 말한다. 실제 분기 문턱은 15°이다. 각도 검사와 진단문이 불일치하는 중간 강도 결함 후보이다. 15° 이상에는 일반 SECTOR 경고가 남는다. 문서의 양쪽 30° 여유 조건은 별개이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-136 | TENDINP 생략 | swanuse PDF 48–49쪽 / 인쇄 40–41쪽: `[tbeginp]`, `[deltinp]`, `SEC / MIN / HR / DAY`, `[tendinp]`; “Default is ISO-notation.” 종료 생략 기본값은 적지 않는다. | `src/swanpre1.ftn:4013` `CALL INCTIM (ITMOPT,'TBEGINP',IFLBEG(IGRID1),'REQ',0D0)`; `src/swanpre1.ftn:4014` `CALL INITVD ('DELTINP', IFLINT(IGRID1), 'REQ', 0D0)`; `src/swanpre1.ftn:4015` `CALL INCTIM (ITMOPT,'TENDINP',IFLEND(IGRID1),'STA',1.D20)`; `src/ocpcre.ftn:1494` `CALL INKEYW ('STA', 'S')`; `src/ocpcre.ftn:1496` `FAC = 24.*3600.`; `src/ocpcre.ftn:1498` `FAC = 3600.`; `src/ocpcre.ftn:1500` `FAC = 60.`; `src/ocpcre.ftn:1503` `FAC = 1.`; `src/ocpcre.ftn:1508` `RVAR = FAC * RI` | C 문서 누락 | TENDINP를 생략하면 내부 종료 시각은 1.D20이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-137 | 1D 입력 제한 | swanuse PDF 48쪽 / 인쇄 40쪽: EXCEPTION과 NONSTATION 항목에 각각 “NOT FOR 1D-MODE.” | `src/swanpre1.ftn:3995` `IF (KEYWIS ('EXC')) THEN`; `src/swanpre1.ftn:4007` `IF (KEYWIS ('NONSTAT')) THEN`; `src/swanpre1.ftn:4010` `NSTATM = 1`; `src/swanmain.ftn:5598` `!       evaluate SVALQI (1D-mode):`; `src/swanmain.ftn:5606` `SVALQI = EXCFLD(IGRID)` | B 문서 오기 | 정규 1D 입력의 EXCEPTION·NONSTATIONARY를 일괄 금지한다고 쓰지 않는다. 곡선·비정규 격자의 1D 제한은 별개이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-144 | IDLA 5·6 방향 | swanuse PDF 52–53쪽 / 인쇄 44–45쪽: `=5` “from top to bottom starting in the lower-left-hand corner”; 배열 예시는 `1,1 1,2 ... 1,myc+1`; `=6`은 같은 배치에서 열별 새 레코드를 요구하지 않는다. | `src/ocpmix.ftn:979` `DO IX=1, MXA`; `src/ocpmix.ftn:981` `&               (ARR(IX,IY), IY=1,MYA)`; `src/ocpmix.ftn:985` `&               ((ARR(IX,IY), IY=1,MYA), IX=1,MXA)` | B 문서 오기 | IDLA 5·6은 각 열을 아래에서 위로 읽는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-147 | 자료 echo 조건 | swanuse PDF 54쪽 / 인쇄 46쪽 및 웹 `swanuse/node26.html:1584–1593`: “If the file does not contain a sufficient number of data”; 이어서 “if [itest]>0 … reproduce the data”. 별도로 `TEST 120`·`READINP`·`TEST 0` 예시를 제시한다. | `src/ocpmix.ftn:1097` `CALL MSGERR (2, 'Unexpected end of file while reading '//`; `src/ocpmix.ftn:1100` `IDLA = -1`; `src/ocpmix.ftn:1124` `WRITE (PRINTF, 994) (ARR(IX,IY), IX=1,MXA)` | C 문서 누락 | 자료 부족 오류에 관한 문서의 `if [itest]>0`는 충분조건이므로 코드와 충돌하지 않는다. 실제 echo 조건은 `ITEST.GE.100 .OR. IDLA.LT.0`이다. 정상 읽기의 100 문턱과 오류 때 ITEST와 무관하게 echo하는 처리가 문서에서 빠졌다. TEST 120 예시는 유효하다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-191 | 정상 INITIAL 제한 | swanuse PDF 64쪽 / 인쇄 56쪽: “stationary (INITIAL HOTSTART only)”. | `src/swanpre1.ftn:6168` `!     error message removed because MODE is not required any more,`; `src/swanpre1.ftn:6169` `!     and INIT can be useful also in stationary mode`; `src/swanpre1.ftn:6220` `CALL SSHAPE (AC2(1,1,1), SPCSIG, SPCDIR, FSHAPE, DSHAPE)`; `src/swancom1.ftn:3460` `IF (ICOND.NE.4 .AND. ITER.EQ.1 .AND. NSTATC.EQ.0) THEN`; `src/swancom1.ftn:3466` `CALL SPREDT (SWPDIR           ,AC2               ,CAX       ,` | B 문서 오기 | 정상 계산에서도 PAR·ZERO를 읽는다. HOTSTART 이외에는 첫 추정 경로가 다시 작동한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-194 | INITIAL HS 이름 | swanuse PDF 64쪽 / 인쇄 56쪽: `PAR [hs] [per] [dir] [dd]`; Appendix B의 이름 지정 규칙은 T1-085와 같다. | `src/swanpre1.ftn:6184` `CALL INREAL ('HSIG', SPPARM(1), 'REQ', 0.)`; `src/swanpre2.ftn:3621` `CALL INREAL ('HS',  SPPARM(1), 'REQ', 0.)`; `src/ocpcre.ftn:476` `CALL INDBLE (NAAM, RDBL, KONT, DRSTA)`; `src/ocpcre.ftn:608` `LENNM = LEN(NAAM)`; `src/ocpcre.ftn:609` `IF (NAAM.NE.ELTEXT(1:LENNM)) GOTO 20` | E 코드 결함 후보·강함 | INITIAL PAR의 이름 입력은 문서의 HS와 달리 HSIG를 요구한다. HS=는 INDBLE의 이름 비교를 통과하지 못한다. 위치 숫자 입력은 수용한다. 코드 자체 문법 주석의 HS와 구현의 HSIG도 불일치한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-225 | MODE NOUPDATE | — | `src/swanpre1.ftn:771` `IF (KEYWIS ('NOUPDAT')) THEN`; `src/swanpre1.ftn:772` `ACUPDA = .FALSE.`; `src/swanmain.ftn:1170` `ACUPDA = .TRUE.`; `src/swancom1.ftn:3636` `IF (.NOT.ACUPDA) THEN`; `src/swancom1.ftn:3638` `GOTO 700`; `src/SwanCompUnstruc.ftn90:1191` `if ( ACUPDA ) then` | C 문서 누락 | NOUPDATE는 수송 계산의 작용밀도 갱신을 건너뛰게 한다. 구조·비정규 격자 모두 ACUPDA로 이 갱신을 제어한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-226 | SPHERICAL REARTH | — | `src/swanpre1.ftn:827` `CALL INREAL ('REARTH', REARTH, 'UNC', 0.)`; `src/swanpre1.ftn:828` `LENDEG = REARTH * PI / 180.`; `src/swanmain.ftn:1187` `REARTH = 2.E7/PI` | C 문서 누락 | SPHERICAL 뒤에서 지구 반지름을 m 단위로 지정할 수 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-229 | ASTD 입력장 | — | `src/swanpre1.ftn:1388` `ELSE IF (KEYWIS ('ASTD')) THEN`; `src/swanpre1.ftn:1390` `IGRD = 10`; `src/swanpre1.ftn:4334` `IGR1   = 10`; `src/swanpre1.ftn:4335` `VARAST = .TRUE.`; `src/swanpre1.ftn:4502` `CALL SWCOPR( TARR, ASTDF, MXG(IGR1)*MYG(IGR1) )`; `src/swanmain.ftn:4973` `COMPDA(INDX,JASTD2) = ASTD`; `src/swanout1.ftn:2714` `CALL SWIPOL(COMPDA(1,JASTD2),OVEXCV(46),XC,YC, MIP, CROSS,` | C 문서 누락 | ASTD 입력값은 공간 보간 뒤 COMPDA의 JASTD2 열에 저장한다. 출력 요청에서는 이 열을 보간한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-230 | WIND ASTD 상수 | — | `src/swanpre1.ftn:2780` `CALL INREAL('ASTD',CASTD,'STA',0.)`; `src/swanmain.ftn:1008` `CASTD  = 0.               ! const. air-sea temp diff` | C 문서 누락 | WIND는 세 번째 수치 ASTD를 읽는다. CASTD의 물리항 사용 경로는 없다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-231 | IGHS·IGTM·IGDIR | — | `src/swanpre1.ftn:1412` `ELSE IF (KEYWIS ('HSS').OR.KEYWIS ('IGHS')) THEN`; `src/swanpre1.ftn:1416` `ELSE IF (KEYWIS ('TSS').OR.KEYWIS ('IGTM')) THEN`; `src/swanpre1.ftn:1420` `ELSE IF (KEYWIS ('DSS').OR.KEYWIS ('IGDIR')) THEN` | C 문서 누락 | IGHS·IGTM·IGDIR는 HSS·TSS·DSS와 같은 입력장 별칭이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-235 | GAUSS 기본 폭 | swanuse PDF 55쪽 / 인쇄 47쪽: “width of the Gaussian frequency spectrum expressed as a standard deviation in Hz” | `src/swanpre2.ftn:2812` `CALL INREAL ('SIGFR', SIGMAG, 'STA', 0.01)`; `src/swanpre2.ftn:2814` `PSHAPE(2) = PI2 * SIGMAG` | C 문서 누락 | GAUSS의 SIGFR를 생략하면 0.01 Hz를 사용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-236 | INITIAL 사각형 선택 | — | `src/swanpre1.ftn:6213` `IF (OPTG.NE.5) THEN`; `src/swanpre1.ftn:6214` `CALL ININTG ('IX1', IX1, 'STA', 0)`; `src/swanpre1.ftn:6215` `CALL ININTG ('IX2', IX2, 'STA', MXC-1)`; `src/swanpre1.ftn:6216` `CALL ININTG ('IY1', IY1, 'STA', 0)`; `src/swanpre1.ftn:6217` `CALL ININTG ('IY2', IY2, 'STA', MYC-1)`; `src/swanpre1.ftn:6224` `DO IX = IX1+1, IX2+1`; `src/swanpre1.ftn:6225` `DO IY = IY1+1, IY2+1` | C 문서 누락 | 구조 격자 INITIAL PAR 뒤의 IX1·IX2·IY1·IY2로 대입 영역을 지정할 수 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-237 | INITIAL의 직접 MEAN·PEAK | — | `src/swanpre1.ftn:6186` `IF (KEYWIS('MEAN')) THEN`; `src/swanpre1.ftn:6187` `IF (FSHAPE.GT.0) FSHAPE=-FSHAPE`; `src/swanpre1.ftn:6188` `ELSE IF (KEYWIS('PEAK')) THEN`; `src/swanpre1.ftn:6189` `IF (FSHAPE.LT.0) FSHAPE=-FSHAPE` | C 문서 누락 | INITIAL PAR의 파고 뒤에서 MEAN·PEAK을 직접 지정할 수 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-250 | USCAP 본문 설명 | swanuse PDF 135쪽 / 인쇄 127쪽: `[cdcap] [uscap] [inrhog]`. | `src/swanpre1.ftn:2178` `CALL INREAL ('USCAP',  USCAP,  'UNC', 0.)`; `src/swanmain.ftn:1010` `USCAP  = 99999.`; `src/swancom3.ftn:1074` `UFRIC = MIN(USCAP,UFRIC) * SQRT(CDFAC)` | C 문서 누락 | USCAP은 Appendix C에 있다. SET 본문에는 기본값 99999와 Hwang 경로의 적용식을 보충한다. USCAP으로 제한한 뒤 CDFAC의 제곱근을 곱한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-251 | SORT·NSWEEP 설명 | swanuse PDF 135쪽 / 인쇄 127쪽: `[sort] [nsweep] CURV`. | `src/swanpre1.ftn:2200` `CALL INREAL ('SORT'    , usort    , 'UNC', 0.)`; `src/swanpre1.ftn:2201` `CALL ININTG ('NSWEEP'  , nsweep   , 'UNC', 0 )`; `src/swanpre1.ftn:2210` `usort = PI2 * (ALTMP - NINT(ALTMP))`; `src/swanmain.ftn:3762` `nsweep = 3`; `src/SwanVertlist.ftn90:187` `sdir = sdir + PI2/real(nsweep)` | C 문서 누락 | SORT·NSWEEP는 비정규 격자의 정점 정렬 방향과 스윕 수를 설정한다. C는 SET 본문의 인수 설명 누락이다. 알고리즘 자체는 기술 매뉴얼에 설명되어 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-252 | SET CURV 설명 | swanuse PDF 135쪽 / 인쇄 127쪽: `CURV`. | `src/swanpre1.ftn:2202` `IF (KEYWIS ('CURV')) CCURV = .TRUE.`; `src/swanmain.ftn:1083` `CCURV  = .FALSE.`; `src/swancom5.ftn:4508` `IF ( OPTG.EQ.3 .AND. CCURV ) THEN`; `src/swancom5.ftn:4512` `!            so that all bins will be filled` | C 문서 누락 | SET CURV는 곡선 격자의 predictor 보정 분기를 켠다. Appendix C에는 문법이 있다. SET 본문에 이 용도 설명이 빠졌다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-253 | PRINTF·PRTEST 설명 | swanuse PDF 135쪽 / 인쇄 127쪽: `[printf] [prtest]`. | `src/swanpre1.ftn:2203` `!        the unit numbers PRINTF and PRTEST should be set in swaninit,`; `src/swanpre1.ftn:2205` `CALL ININTG ('PRINTF'  , PRINTF   , 'UNC', 0 )`; `src/swanpre1.ftn:2206` `CALL ININTG ('PRTEST'  , PRTEST   , 'UNC', 0 )`; `src/ocpids.ftn:183` `PRINTF = 4` | C 문서 누락 | PRINTF·PRTEST는 파일 이름이 아니라 unit 번호이다. C는 SET 본문의 인수 설명 누락이다. swaninit에서 설정하는 방법은 구현 매뉴얼에 있다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-254 | 곡선 격자의 ALPC | swanuse PDF 135쪽 / 인쇄 127쪽: `CURVilinear [mxc] [myc] (EXC [xexc] [yexc]) [alpc]`. | `src/swanpre1.ftn:1720` `CALL INREAL ('ALPC',ALPC,'STA',0.)`; `src/swanpre1.ftn:1722` `ALPC = PI2 * (ALTMP - NINT(ALTMP))`; `src/swanpre1.ftn:1772` `IF (FULCIR) THEN`; `src/swanpre1.ftn:1778` `SPDIR1 = ALPC + 0.5 * DDIR`; `src/swanpre1.ftn:1728` `CALL INREAL ('DIR1', SPDIR1, 'REQ', 0.)`; `src/swanpre1.ftn:1729` `CALL INREAL ('DIR2', SPDIR2, 'REQ', 0.)` | C 문서 누락 | CGRID CURVILINEAR의 ALPC는 CIRCLE일 때 스펙트럼 방향 격자의 기준각에 사용한다. SECTOR는 DIR1·DIR2를 직접 읽는다. 좌표 파일을 회전시키는 선택으로 설명하지 않는다. Appendix C에는 문법이 있고 §4.5.1 본문에는 이 용도 설명이 빠졌다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-306 | 중첩 범위 밖은 전부 0 | `manual-notes/swan-command-setup-grid-reference.md:76`의 `(밖은 0)` | `src/swanmain.ftn:8495` `(SPCSIG(ISIGTA)/SPCSIG(IS))**(PWTAIL(1)+1)`; `src/swanmain.ftn:8485` `IF (IS.LE.ISIGTA) THEN` | B 문서 오기 | 스펙트럼 격자는 다를 수 있다. 파일 최고 주파수 위에는 진단 꼬리를 붙일 수 있다. 노트와 사용자 매뉴얼의 “밖은 0”을 모든 주파수에 적용하지 않는다. 중첩 경계의 지리적 위치는 별도 조건이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-307 | PROJECT 제목의 줄 배치 | `manual-notes/swan-command-setup-grid-reference.md:27`은 제목 세 개를 같은 줄에 쓴다. | `src/swanpre1.ftn:526` `CALL NWLINE` | B 문서 오기 | PROJECT의 name·nr 다음에는 제목마다 새 줄을 사용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-308 | INPGRID ICE 표기 | `manual-notes/swan-command-setup-grid-reference.md:104`의 `INPGRID WIND/ICE` | `src/swanpre1.ftn:1404` `ELSE IF (KEYWIS ('AICE')) THEN`; `src/swanpre1.ftn:1408` `ELSE IF (KEYWIS ('HICE')) THEN` | B 문서 오기 | 얼음 입력장은 AICE·HICE로 나눈다. ICE는 상수 입력 명령이다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-309 | MSC의 최소값 해석 | `manual-notes/swan-command-setup-grid-reference.md:75`의 `주파수 수−1 (**최소 4**` | `src/swanpre1.ftn:1768` `MSC  = MSS+1` | B 문서 오기 | 문서의 최소 4는 주파수 개수이다. 메시 수 msc와 구분한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-310 | MAXERR 중단 경계 | `manual-notes/swan-command-setup-grid-reference.md:41`의 `계산중단 error level`. swanuse PDF 36쪽 / 인쇄 28쪽 및 웹 `swanuse/node23.html:246–250`: “at the level indicated the computations will continue”. | `src/swanmain.ftn:521` `IF (LEVERR.GT.MAXERR) THEN` | C 문서 누락 | 노트의 “계산중단 error level”에는 초과 조건이 빠져 있다. 사용자 매뉴얼은 지정한 수준에서는 계산을 계속한다고 적는다. 계산 시작을 막는 조건은 `IF (LEVERR.GT.MAXERR) THEN`이다. MAXERR와 같은 수준은 이 검사에서 허용한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-311 | FROUDMAX의 유속 변경 | `manual-notes/swan-command-setup-grid-reference.md:49`의 `최대 Froude (current/√gd, 초과시 maximize)`는 swanuse PDF 37쪽 / 인쇄 29쪽의 상한 설명을 옮겼다. | `src/swanmain.ftn:4917` `CGMAX = PNUMS(18)*SQRT(GRAV*DEPW)`; `src/swanmain.ftn:4918` `IF (VTOT .GT. CGMAX) THEN`; `src/swanmain.ftn:4919` `CGFACT = CGMAX / VTOT` | F 표기 차이 | FROUDMAX는 유속 크기의 상한을 정한다. `IF (VTOT .GT. CGMAX) THEN`에서 유속 성분을 같은 비율로 줄인다. 문서와 노트의 “maximize”는 상한 적용을 느슨하게 표현한 말이다. 유속을 증가시킨다는 오기로 판정하지 않는다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R4:T1-313 | 노트의 TMA 누락 | `manual-notes/swan-command-setup-grid-reference.md:110`의 모양 목록에는 TMA가 없다. swanuse PDF 55쪽 / 인쇄 47쪽은 `TMA`를 설명한다. | `src/swanpre2.ftn:2816` `FSHAPE = 5` | C 문서 누락 | 노트의 BOUND SHAPE 목록에 TMA [gamma] [d]를 추가한다. 사용자 매뉴얼에는 이미 있으므로 C 판정은 해당 노트에 한정한다. [R4](../../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#5-차이-결론) |
| R5:PN-145 | ICE | — | `src/swanpre1.ftn:2624` `IF (KEYWIS ('ICE')) THEN`; `src/swanpre1.ftn:2625` `CALL INREAL('AICE',PICE(1),'REQ',0.)`; `src/swanpre1.ftn:2626` `CALL INREAL('HICE',PICE(2),'REQ',0.)` | C 문서 누락 | ICE는 균일 농도와 두께를 필수로 읽는다. SICE 활성화는 별도다. [R5](../../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론) |
| R7:ED-051 | READINP 괄호 | `misc/swan.edt:47` `!               \ SERIES 'fname2' /  [idla] [nhedf] ([nhedt]) (nhedvec])    &`; swanuse PDF 50쪽, 인쇄 42쪽 및 `website/online_doc/swanuse/node26.html:842`는 `([nhedvec])`로 적는다. | `src/swanpre1.ftn:4430` `CALL INREAL ('FAC', IFLFAC(IGR1), 'STA', 1.)`; `src/ocpmix.ftn:712–713` `IF (LOGC) THEN`; `misc/swan.edt:47` `!               \ SERIES 'fname2' /  [idla] [nhedf] ([nhedt]) (nhedvec])    &` | B 문서 오기 | 로컬 swan.edt:47과 웹 부록 node49:103의 `(nhedvec])`는 여는 대괄호가 없는 오기이다. swanuse READINP 본문의 `([nhedvec])`와 맞추어 고친다. NHEDVEC는 벡터 입력 조건에서 읽는다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:H-291 | 주파수 개수 자동 계산 | `website/modifications/modifications.htm:291` `The lowest and the highest frequencies can be specified. The number of frequencies will be computed by SWAN such that the ratio of frequency resolution is 10%. This is required by the DIA method.`; swanuse PDF 41쪽, 인쇄 33쪽 및 `website/online_doc/swanuse/node25.html:509–524`: `The actual resolution in the computations should therefore not deviate too much from this.` | `src/swanpre1.ftn:1754` `MSS = NINT(ALOG(FRHIG/FRLOW)/ALOG(1.1))                        40.31`; `src/swanpre1.ftn:1753` `ELSE IF (MSS.EQ.-999) THEN`; `src/swanpre1.ftn:1768` `MSC  = MSS+1` | F 표기 차이 | FLOW와 FHIGH를 주고 MSC 입력을 생략하면 NINT가 주파수 구간 수 MSS를 정한다. 10%는 목표 간격이다. swanuse는 실제 해상도가 이 값에서 너무 많이 벗어나지 않아야 한다고 설명한다. 수정 이력의 10%를 항상 정확한 비율이라는 보장으로 읽은 B 판정을 느슨한 표기의 F로 낮춘다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
