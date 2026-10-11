---
title: "ADCIRC ICE 커버리지 — v49.64+ 자료와 v56.2.1 코드 대조"
model: ADCIRC
component: manual-notes
canonical_source: self
citation_status: verified
verification_method: "공식 자료 `raw/manuals/pdfs/adcirc_modifications_for_ice.pdf`(10쪽, Chris Massey·Ray Chapman, ERDC-CHL, 'Modifications to ADCIRC v49.64+ for ICE Coverage') pdftotext -layout 전수 추출 후 직접 read. 모든 단언을 snapshot `e8b62a70` 소스와 대조 — wind.F:120-139(항력 상한·DragLawString 기본값)·:507(Garratt 식)·:728-792(WindIceDrag 4분기)·:984 외(호출부), couple2swan.F:966,1033,1055,1185(SWAN 전달), global.F:673(CICE_TIMINC). 자료는 v49.64+ 기준이라 현 스냅샷과 어긋나는 지점을 §4에 분리 기록."
note_author: "Claude Opus 5"
note_date: 2026-09-22
related:
  - models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md
  - models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md
  - models/ADCIRC/source-analysis/adcirc-swan-coupling.md
last_source_check: 2026-10-11 (recovery 재판독 대조)
---

# ADCIRC ICE 커버리지

> 출처: `raw/manuals/pdfs/adcirc_modifications_for_ice.pdf` — "Modifications to ADCIRC v49.64+ for ICE Coverage",
> Chris Massey·Ray Chapman (ERDC-CHL), 10쪽 발표자료. **버전 기준이 v49.64+ 로 현 스냅샷(`e8b62a70`)보다 앞선다.**

## 1. 적용 범위 — 풍응력 항력과 SWAN 결합

> "Ice coverage in ADCIRC was added as a way to **modify the wind drag values**.
> In no other way is ice coverage considered during ADCIRC's computational process." (p.2)

ADCIRC 단독 운동량 경로에서 확인한 얼음 처리는 풍응력 항력 수정이다. (`src/wind.F:984` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/wind.F:1457` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`)

ADCIRC+SWAN은 SWAN_IICE=2에서 dry forcing을 수행한다. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`)

ADCIRC+SWAN은 SWAN_IICE=3에서 얼음 농도를 전달한다. (`src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

허용 경로에서 별도 유빙 응력·열역학 진화식은 확인하지 않음. (`src/wind.F:984` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/wind.F:1457` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`; `src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

⚠ **단, ADCIRC+SWAN 결합에서는 예외다** (§4-③).

## 2. 구판 자료의 fort.15 활성화 안내

> "These are the only changes required in the fort.15 file in order to use ice coverage." (p.6)

| 항목 | 값 |
|---|---|
| `NWS` | v49.64+ PDF는 `1000+평소 바람 옵션`과 OWI 얼음의 12000을 안내한다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 6 / 인쇄 쪽 6` `Ice coverage is indicated by setting NWS = 1000+ your normal wind type option. OWI formatted Ice is 12000.`) v56.2.1은 NCICE를 0·10·12·14·17로 제한한다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`) PDF 예시 NWS=12012는 NCICE=12와 NWS=12를 선택한다. (`src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`) |
| `WTIMINC` 줄 | `3600.0 86400.0  ! WTIMINC, CICE_TIMINC` — 바람 증분 뒤에 **얼음 증분**을 잇는다. 둘 다 초 단위 |

코드는 `NCICE = INT(ABS(NWS)/1000)`으로 얼음 flag를 추출한다. (`src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`)

구판의 단순 +1000 안내는 v56.2.1의 공통 허용 규칙으로 사용할 수 없다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`)

단순 +1000의 NCICE=1은 허용 목록에서 거부한다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`)
`CICE_TIMINC`·`CICE_TIME1`·`CICE_TIME2` 는 `global.F:673` 에 선언돼 있다.
현행 fort25.rst 제목의 fort.255·277은 본문·코드의 fort.225·227과 다르다. (`docs/technical_reference/input_files/fort25.rst:3` `Fort.25, 255/277: Ice Coverage Input Files`; `src/owi_ice.F:132` `OPEN(225,FILE=TRIM(GBLINPUTDIR)//'/'//'fort.225', STATUS='OLD')`; `src/owi_ice.F:158` `OPEN(227,FILE=TRIM(GBLINPUTDIR)//'/'//'fort.227',STATUS='OLD')`)

현행 fort25.rst는 -1.0%를 0.0%로 처리한다고 적는다. (`docs/technical_reference/input_files/fort25.rst:21` `If numIceFields in the fort.25 file is set to 1, only the fort.225 file will be read; if numIceFields in the fort.25 file is set to 2 then both the fort.225 and fort.227 files will be read. The fort.225 (the basin scale, i.e., large scale coarse grid) and optional fort.227 (the region scale, i.e., smaller scale finer grid) files contain the actual ice percentage values (0.0 to 100.0%) and a value of -1.0 which means land or no data available. A value of -1.0% is treated as 0.0% ice in ADCIRC.`)

코드는 보간 셀의 음수 모서리 값을 비음수 모서리들의 평균으로 바꾼다. (`src/owi_ice.F:374` `if(CV(k) .ge. 0.d0) then`; `src/owi_ice.F:375` `CVbar = CVbar + CV(k)`; `src/owi_ice.F:376` `ibar = ibar + 1`; `src/owi_ice.F:379` `if (ibar.gt.0) CVbar = CVbar/real(ibar,8)`; `src/owi_ice.F:381` `if (CV(k).lt.0.d0) CV(k) = CVbar`)

모든 모서리가 음수이면 평균의 초기값 0이 남는다. (`src/owi_ice.F:374` `if(CV(k) .ge. 0.d0) then`; `src/owi_ice.F:379` `if (ibar.gt.0) CVbar = CVbar/real(ibar,8)`; `src/owi_ice.F:381` `if (CV(k).lt.0.d0) CV(k) = CVbar`)

## 3. 항력 공식

### 3.1 기저 — Garratt (1977)

ADCIRC 기본 풍응력 항력은 Garratt 형이며 상한 **0.0035** 를 건다 (p.2).
현행 입력 문서는 일부 NWS의 응력 계수 상한을 0.003으로 적는다. (`docs/technical_reference/input_files/fort22.rst:222` `* if(DRAG_COEFF.gt.0.003) DRAG_COEFF=0.003`; `docs/technical_reference/input_files/fort22.rst:258` `* if(DRAG_COEFF.gt.0.003) DRAG_COEFF=0.003`)

코드의 기본 WindDragLimit은 0.0035다. (`src/wind.F:122` `REAL(8) :: WindDragLimit = 0.0035d0   ! maximum wind drag value`)

실제 계산은 선택한 DragLaw와 WindDragLimit에 따른다. (`src/wind.F:537` `WindDrag = MIN(GarrattWindDrag(WindSpeed,NodeNumber),WindDragLimit)`)

$$C_D = \frac{0.75 + 0.067\,|\vec{w}|}{1000}$$

코드: `wind.F:507`(식), `wind.F:122` `WindDragLimit = 0.0035d0`.
**따라서 Garratt 최솟값(무풍)은 $0.75\times10^{-3} = 0.00075$ 다.** 이 값이 §4-① 의 쟁점이다.

### 3.2 ICE CUBE — 얼음 비율의 3차 다항식

현재 fort25.rst는 ICE CUBE 다항식의 계수를 명시한다. (`docs/technical_reference/input_files/fort25.rst:47` `\mathrm{CDF} = [0.075 + 0.75 \mathrm{IC} – 0.9 \mathrm{IC}^2 + 0.2 \mathrm{IC}^3 ] 10^{-2} \text{ (IceCube formulation, this is the default)}`)

adcirc_modifications_for_ice.pdf 3쪽은 세 설계 조건을 서술한다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3`)

코드의 pic는 PercentIce에 0.01을 곱한 0–1 비율이다. (`src/wind.F:761` `pic = PercentIce*0.01d0`)

PDF 문장의 pic=50·100은 백분율이다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3` `When pic = 50 it has a value of 0.0025 and a zero gradient`; `raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3` `When pic = 100 it has a value of 0.00125.`)

$$C_{D,\text{ice}} = \left(0.075 + 0.75\,p_{ic} - 0.9\,p_{ic}^2 + 0.2\,p_{ic}^3\right)\times 10^{-2}$$
위 다항식은 현재 rst와 코드의 식에 대응한다. (`docs/technical_reference/input_files/fort25.rst:47` `\mathrm{CDF} = [0.075 + 0.75 \mathrm{IC} – 0.9 \mathrm{IC}^2 + 0.2 \mathrm{IC}^3 ] 10^{-2} \text{ (IceCube formulation, this is the default)}`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`)

코드 다항식의 0% 값은 0.00075다. (`src/wind.F:761` `pic = PercentIce*0.01d0`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`)

PDF는 0% 설명에 0.000075를 적었다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3` `When pic = 0 the drag coefficient is equal to the minimum value for Garratt (.000075)`)

해석: PDF의 자릿수 오류 가능성이 있다(정적 판독, 실행 미확인). (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`)

아래 표는 코드 다항식의 계산값을 적는다.

| 조건 | 계산 | 결과 |
|---|---|---|
| `pic`=0인 코드 다항식 | $0.075\times10^{-2}$ | **0.00075**. (`src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`) |
| `pic`=0.5 → 0.0025, 기울기 0 | $(0.075+0.375-0.225+0.025)\times10^{-2}$ ; $\frac{d}{dp}=0.75-1.8p+0.6p^2 \to 0$ | **0.0025**, 기울기 **0** ✓ |
| `pic`=1 → 0.00125 | $(0.075+0.75-0.9+0.2)\times10^{-2}$ | **0.00125** ✓ |

IceCube 분기는 `PercentIce`가 0 이상이면 얼음 항력과 바람 항력 중 큰 값을 사용한다. `PercentIce`가 음수이면 바람 항력을 사용한다 [10-11 검증 보완]. (`src/wind.F:749` `CASE("IceCube")`; `src/wind.F:758` `IF (PercentIce.lt.0.d0) then`; `src/wind.F:759` `WindIceDrag = WindDrag`; `src/wind.F:764` `WindIceDrag = max(IceDrag,WindDrag)`)

Lupkes 계열 분기는 얼음 면적 비율로 바람 항력과 얼음 항력을 결합한다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`; `src/wind.F:776` `pic = min(PercentIce*0.01d0,1d0)`; `src/wind.F:778` `WindIceDrag = WindDrag*(1d0 - pic) + (Cskin + Cform)*pic`)

## 4. 자료와 현 스냅샷의 차이

### ① PDF·소스 주석의 0.000075와 코드 식의 0.00075

PDF·코드 주석은 Garratt의 최솟값을 0.000075로 적는다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3` `When pic = 0 the drag coefficient is equal to the minimum value for Garratt (.000075)`; `src/wind.F:751` `C....... When pic = 0 the drag coefficient is equal to`; `src/wind.F:752` `C....... the minimum value for Garratt (.000075), when pic = 50`)

Garratt 코드 식의 무풍 값은 0.00075다. (`src/wind.F:520` `Drag = 0.001d0*(0.75d0+0.067d0*WindSpeed)`)

IceCube 코드 식의 0% 값은 0.00075다. (`src/wind.F:761` `pic = PercentIce*0.01d0`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`)

해석: 자릿수 오류 가능성이 있다(정적 판독, 실행 미확인). (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3`; `src/wind.F:752` `C....... the minimum value for Garratt (.000075), when pic = 50`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`)

어느 문서가 어느 주석을 복사했는지는 확인하지 않음.

### ② WindIceDrag의 세 항력법과 오류 분기

WindIceDrag는 RaysIce·IceCube·Lupkes 계열의 세 항력법을 선택한다. (`src/wind.F:738` `CASE("RaysIce")`; `src/wind.F:749` `CASE("IceCube")`; `src/wind.F:767` `CASE("Lupkes","default","Powell")`)

default와 Powell은 Lupkes 계열의 별칭이다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`)

CASE DEFAULT는 오류로 종료한다. (`src/wind.F:781` `CASE DEFAULT`; `src/wind.F:784` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`)

NWS가 0이 아닐 때 초기 WindInit의 문자열 검사는 IceCube·RaysIce·Lupkes를 허용하지 않는다. (`src/wind.F:367` `if (NWS.eq.0) return`; `src/wind.F:371` `SELECT CASE(TRIM(DragLawString))`; `src/wind.F:372` `CASE("Garratt","GARRATT","garratt","default")`; `src/wind.F:376` `CASE("Swell","SWELL","swell")`; `src/wind.F:380` `CASE("Powell","POWELL","powell")`; `src/wind.F:391` `CASE DEFAULT`; `src/wind.F:394` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`)

`wind.F:736-787` 의 `SELECT CASE(TRIM(DragLawString))`:

| `DragLawString` | 식 | 근거 |
|---|---|---|
| `RaysIce` | $(0.125 + 0.5\,p_{ic}(1-p_{ic}))\times10^{-2}$; `if (PercentIce .lt. 1.d0) then`이면 바람 항력을 유지한다. 그 밖에는 `WindIceDrag = max(IceDrag,WindDrag)`를 쓴다 [10-11 검증 보완]. | `src/wind.F:738` `CASE("RaysIce")`; `src/wind.F:741` `if (PercentIce .lt. 1.d0) then`; `src/wind.F:742` `WindIceDrag = WindDrag`; `src/wind.F:744` `pic = PercentIce*0.01d0`; `src/wind.F:745` `IceDrag = (0.125d0 + 0.5d0*pic*(1.0d0-pic))*0.01d0`; `src/wind.F:746` `WindIceDrag = max(IceDrag,WindDrag)` |
| `IceCube` | §3.2 | `wind.F:749-765` |
| `Lupkes` / `default` / `Powell` | $C_D(1-p_{ic}) + (C_{skin}+C_{form})p_{ic}$, $C_{form}=C_{form,max}(1-p_{ic})^\beta$ | `wind.F:767-779`. Lüpkes et al. (2012) doi:10.1029/2012JD017630 · Joyce et al. (2019) doi:10.1016/j.ocemod.2019.101421 |
| 그 외 | `terminate(ADCIRC_EXIT_FAILURE)` — 조용히 넘어가지 않는다 | `wind.F:781-786` |

POWELL 빌드 조건이 없으면 DragLawString의 기본값은 default다. (`src/wind.F:131` `#ifndef POWELL`; `src/wind.F:132` `CHARACTER(len=10) :: DragLawString = 'default' ! controls wind drag formulation`)

POWELL 빌드 조건이 있으면 DragLawString의 기본값은 Powell이다. (`src/wind.F:134` `#else`; `src/wind.F:139` `CHARACTER(len=10) :: DragLawString = 'Powell'`)

WindIceDrag에서 두 문자열은 Lupkes 계열 분기를 선택한다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`)

NWS가 0이 아닐 때 초기 WindInit의 문자열 검사도 입력 선택을 제한한다. (`src/wind.F:367` `if (NWS.eq.0) return`; `src/wind.F:371` `SELECT CASE(TRIM(DragLawString))`; `src/wind.F:391` `CASE DEFAULT`; `src/wind.F:394` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`)

현행 fort25.rst는 미지정 또는 default에서 IceCube를 사용한다고 적는다. (`docs/technical_reference/input_files/fort25.rst:43` `The IceCube formulation is used if the DragLawString is not specified in the fort.15, or is specified as “IceCube” or “default”. IceCube is a cubic function that represents a smoother transition between Garratt and the RaysIce formulation for low ice cover percentages and low wind speeds. This function is as follows:”`)

이 문서의 기본 선택 설명은 코드의 Lupkes 분기와 다르다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`)

현행 fort25.rst는 IC를 0–1로 정의한 뒤 IC=50·100을 함께 사용한다. (`docs/technical_reference/input_files/fort25.rst:39` `in which IC is the ice concentration varying from 0.0 to 1.0 for open water and complete ice cover conditions, respectively. To specify this quadratic formulation for the wind drag, set the DragLawString parameter in the fort.15 file to “RaysIce”.`; `docs/technical_reference/input_files/fort25.rst:49` `When IC = 0 the drag coefficient is equal to the minimum value for Garratt (.000075), when IC = 50 it has a value of 0.0025 and a zero gradient, and when IC = 100 it has a value of 0.00125.`)

OWI ASCII 얼음 입력은 percent다. (`docs/technical_reference/input_files/fort25.rst:21` `If numIceFields in the fort.25 file is set to 1, only the fort.225 file will be read; if numIceFields in the fort.25 file is set to 2 then both the fort.225 and fort.227 files will be read. The fort.225 (the basin scale, i.e., large scale coarse grid) and optional fort.227 (the region scale, i.e., smaller scale finer grid) files contain the actual ice percentage values (0.0 to 100.0%) and a value of -1.0 which means land or no data available. A value of -1.0% is treated as 0.0% ice in ADCIRC.`)

GRIB2·netCDF 면적 비율은 caller가 100배로 바꾼다. (`src/wind.F:1240` `IF (NCICE.eq.10) then`; `src/wind.F:1241` `Cicenow = 100d0*( CICE1(I) +`; `src/wind.F:1242` `&                           WTRatio*( CICE2(I)-CICE1(I) ) )`; `src/wind.F:2998` `if (NCICE.eq.14) then`; `src/wind.F:2999` `Cicenow = 100d0*(CICE1(I) +`; `src/wind.F:3000` `&                             CTRATIO*(CICE2(I)-CICE1(I)))`)

### ③ ★SWAN 결합에서는 "항력 전용" 이 아니다

PDF는 In no other way를 무조건 적었다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 2 / 인쇄 쪽 2` `In no other way is ice coverage considered during ADCIRC's computational process.`)

현재 SWAN 결합 분기에는 추가 얼음 처리가 있다. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`; `src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

해석: 구판 PDF를 단독 ADCIRC 설명으로 제한해 읽을 수 있지만 이 제한은 원문 인용이 아니다(정적 판독, 실행 미확인). (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 2 / 인쇄 쪽 2`)

PDF의 v49.64+와 현재 코드의 v56.2.1은 판이 다르다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 1 / 인쇄 쪽 1`; `CMakeLists.txt:92` `set(ADCIRC_VERSION_STRING "v56.2.1")`)
`couple2swan.F` 는 `NCICE≠0` 일 때 얼음장을 SWAN 으로 넘긴다:

- `SWAN_IICE => IICE` 로 SWAN 쪽 플래그를 받고(`:966`), `SWAN_IICE` 값에 따라 분기(`:1033`·`:1055`)
- `ICETIMEFRAC = ((STATIM*86400+ITIME*DT)-CICE_TIME1)/CICE_TIMINC` 로 시간 보간(`:1185`·`:1213`)

ADCIRC 인터페이스는 SWAN에 얼음 농도를 전달하거나 총수심을 0으로 만든다. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`; `src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

이번 대조는 SWAN 내부의 파랑 감쇠 알고리즘을 확인하지 않음. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`; `src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

해석: 전달 자료의 SWAN 물리 사용은 별도 검증 사항이다(정적 판독, 실행 미확인). (`src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)
상세는 [adcirc-swan-coupling](../source-analysis/adcirc-swan-coupling.md).

## 5. 정리

| 축 | 내용 |
|---|---|
| 물리 범위 | 단독 운동량 경로의 풍응력 항력 수정이다. (`src/wind.F:984` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/wind.F:1457` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`) 별도 열역학·유빙 응력 진화식은 확인하지 않음. |
| 입력 | 현재 허용 NCICE는 0·10·12·14·17이다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`) OWI 예시 NWS=12012는 NCICE=12와 NWS=12를 선택한다. (`src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`) `CICE_TIMINC`를 지정한다. |
| 항력 선택 | default·Powell의 WindIceDrag 선택은 Lupkes 계열이다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`) 초기 WindInit은 문자열을 검사한다. (`src/wind.F:371` `SELECT CASE(TRIM(DragLawString))`; `src/wind.F:391` `CASE DEFAULT`; `src/wind.F:394` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`) |
| 결합 | SWAN_IICE=2는 dry forcing을 수행한다. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`) SWAN_IICE=3은 얼음 농도를 전달한다. (`src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`) SWAN 내부 파랑 감쇠는 확인하지 않음. |
| 주의 | PDF·코드 주석의 0.000075와 코드 식의 0.00075가 다르다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3`; `src/wind.F:752` `C....... the minimum value for Garratt (.000075), when pic = 50`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`) 해석: 자릿수 오류 가능성이 있다(정적 판독, 실행 미확인). |
