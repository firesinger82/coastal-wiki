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
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# ADCIRC ICE 커버리지

> 출처: `raw/manuals/pdfs/adcirc_modifications_for_ice.pdf` — "Modifications to ADCIRC v49.64+ for ICE Coverage",
> Chris Massey·Ray Chapman (ERDC-CHL), 10쪽 발표자료. **버전 기준이 v49.64+ 로 현 스냅샷(`e8b62a70`)보다 앞선다.**

## 1. 적용 범위 — 풍응력 항력과 SWAN 결합

> "Ice coverage in ADCIRC was added as a way to **modify the wind drag values**.
> In no other way is ice coverage considered during ADCIRC's computational process." (p.2)

ADCIRC 단독 운동량 경로에서 확인한 얼음 처리는 풍응력 항력 수정이다. (`src/wind.F:984` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/wind.F:1457` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`)

<a id="ice-dry"></a>ADCIRC+SWAN의 인용된 초기화 분기는 `NCICE.NE.0`이고 `SWAN_IICE.EQ.2`일 때 얼음 농도가 임계값 이상인 절점만 dry forcing으로 처리한다. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1040` `IF (SWAN_CICE2(IN,1).GE.SWAN_WBICETH) ICY(IN) = 1`; `src/couple2swan.F:1041` `IF(ICY(IN).EQ.1) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`) [10-12 전수 검증 보완] [10-12 결론 검증 보완]

<a id="ice-buffer"></a>ADCIRC+SWAN의 초기화는 `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`에서 결합 버퍼를 채운다. `src/couple2swan.F:1058–1059`의 대입은 `SWAN_CICE2(IN,1) = CICE1(IN)`과 `SWAN_CICE2(IN,2) = CICE2(IN)`이다. 이 대입만으로 SWAN 감쇠 물리에 전달되었다고 판정할 수 없다. 이후 소비 경로는 [C25의 E 후보 정본](#ice-swan-disconnect)을 따른다. [10-12 결론 검증 정정]

허용 경로에서 별도 유빙 응력·열역학 진화식은 확인하지 않음. (`src/wind.F:984` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/wind.F:1457` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`; `src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

⚠ **단, ADCIRC+SWAN 결합에서는 예외다** (§4-③).


([features 보고서 §5 I06 (300줄)<br>K25 (589줄)<br>C24 (673줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 구판 얼음 적용 범위와 SWAN 결합) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:14` (PDF p.2)은 풍응력 외의 얼음 적용이 없다고 설명한다. 현재 코드의 [IICE=2 dry forcing](#ice-dry)과 [IICE=3 결합 버퍼](#ice-buffer)는 이 구판 설명에 없다. 결론: A 판 차이. SWAN 감쇠 물리로의 실제 전달 여부는 [C25의 E 후보](#ice-swan-disconnect)로 구분한다. [10-12 결론 검증 정정]
([features 보고서 §5 C18 (667줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 얼음 농도의 유일 사용처) 결론: B 문서 오기. 얼음 농도의 소비 경로를 WindIceDrag 하나로 한정할 수 없다. 근거는 [IICE=2 dry forcing](#ice-dry)과 [IICE=3 결합 버퍼](#ice-buffer)에 모았다. SWAN 감쇠 입력의 연결은 [C25](#ice-swan-disconnect)를 따른다. [10-12 결론 검증 정정]
<a id="ice-swan-disconnect"></a>([features 보고서 §5 C25 (674줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: ADCIRC 얼음 농도와 SWAN 감쇠 입력의 연결 누락) 근거: features 보고서 §4 C25가 보존한 노트는 ADCIRC의 얼음 농도가 SWAN의 파랑 감쇠 물리로 들어간다고 설명했다.<br>추가 원문: src/couple2swan.F:1153은 `REAL(8)             :: SWAN_PIC`를 지역 스칼라로 선언한다. 1210줄의 주석은 `enable pass ACIRC ice concentration to SWAN`이다.<br>src/couple2swan.F:1211–1218: `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN` / `ICETIMEFRAC = ((STATIM*86400+ITIME*DT)-CICE_TIME1)/CICE_TIMINC` / `DO IN=1,NP` / `SWAN_CICE2(IN,1) = CICE1(IN)` / `SWAN_CICE2(IN,2) = CICE2(IN)` / `SWAN_PIC = ICETIMEFRAC*(SWAN_CICE2(IN,2) - SWAN_CICE2(IN,1))` / `&               + SWAN_CICE2(IN,1)`.<br>같은 파일 1219–1224줄의 후속 처리는 모두 주석이다. SWAN_PIC와 SWAN_CICE2를 raw 전체에서 검색해도 이 모듈 밖의 SWAN 감쇠 입력으로 연결하는 사용처가 없다.<br>추가 원문: thirdparty/swan/swancom1.ftn:7236–7240은 `AICELOC = 0.`에서 시작한다. `IF ( VARAICE ) THEN`에서는 `AICELOC = AICE2(KCGRD(1))`를 쓴다. `ELSEIF ( IICE.GE.3 ) THEN`에서는 `AICELOC = PICE(1)`을 쓴다. 7306–7313줄은 `IF ( IICE.GT.2 ) THEN`에서 AICELOC를 SICE에 전달한다.<br>thirdparty/swan/swancom2.ftn:1542: `if_ice: IF ( AICELOC.GT.0. ) THEN`. 1565줄: `SICEWD = 2. * KI(IS) * CG(IS,1) * AICELOC`. 1573줄: `IMATDA(ID,IS) = IMATDA(ID,IS) + SICEWD`.<br>해석: SWAN에는 얼음 농도에 비례하는 감쇠 항이 있다. ADCIRC에서 보간한 SWAN_PIC는 그 항이 읽는 AICE2·PICE에 전달되지 않는다. 전달을 명시한 코드 주석과 실제 소비 경로의 단절을 E 코드 결함 후보로 분류한다. SWAN 자체의 AICE·PICE 입력을 통한 감쇠와 IICE=2의 dry forcing은 이 결함 후보에 포함하지 않는다.<br>추가 검색: raw와 판독 기록 전체에서 `SWAN_CICE2`, `SWAN_PIC`, `VARAICE`, `AICELOC`, `SICEWD`를 검색했다. couple2swan.F, SWAN의 결합 모듈 사용 목록, swancom1.ftn·swancom2.ftn의 감쇠 경로를 추가로 대조했다. 결론: 코드 결함 후보. SWAN_IICE=3에서 ADCIRC의 보간 얼음 농도를 SWAN 감쇠 입력으로 넘기는 연결이 빠진 코드 결함 후보가 있다. [10-12 G 재판정] [10-12 결론 검증 보완]

## 2. 구판 자료의 fort.15 활성화 안내

> "These are the only changes required in the fort.15 file in order to use ice coverage." (p.6)

| 항목 | 값 |
|---|---|
| `NWS` | v49.64+ PDF는 `1000+평소 바람 옵션`과 OWI 얼음의 12000을 안내한다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 6 / 인쇄 쪽 6` `Ice coverage is indicated by setting NWS = 1000+ your normal wind type option. OWI formatted Ice is 12000.`) v56.2.1은 NCICE를 0·10·12·14·17로 제한한다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`) PDF 예시 NWS=12012는 NCICE=12와 NWS=12를 선택한다. (`src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`) |
| `WTIMINC` 줄 | `3600.0 86400.0  ! WTIMINC, CICE_TIMINC` — 바람 증분 뒤에 **얼음 증분**을 잇는다. 둘 다 초 단위 |

코드는 `IF (NWS.EQ.0) THEN`에서 NCICE를 0으로 설정한다. (`src/read_input.F:1772` `IF (NWS.EQ.0) THEN`; `src/read_input.F:1773` `NCICE = 0`) [10-12 전수 검증 보완] 그 `ELSE` 분기에서 얼음 flag를 추출하고 NWS를 재설정한다. (`src/read_input.F:1774` `ELSE`; `src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`) [10-12 전수 검증 보완]

구판의 단순 +1000 안내는 v56.2.1의 공통 허용 규칙으로 사용할 수 없다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`)

단순 +1000의 NCICE=1은 허용 목록에서 거부한다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`)
`CICE_TIMINC`·`CICE_TIME1`·`CICE_TIME2` 는 `global.F:673` 에 선언돼 있다.
현행 fort25.rst 제목의 fort.255·277은 본문·코드의 fort.225·227과 다르다. (`docs/technical_reference/input_files/fort25.rst:3` `Fort.25, 255/277: Ice Coverage Input Files`; `src/owi_ice.F:132` `OPEN(225,FILE=TRIM(GBLINPUTDIR)//'/'//'fort.225', STATUS='OLD')`; `src/owi_ice.F:158` `OPEN(227,FILE=TRIM(GBLINPUTDIR)//'/'//'fort.227',STATUS='OLD')`)

현행 fort25.rst는 -1.0%를 0.0%로 처리한다고 적는다. (`docs/technical_reference/input_files/fort25.rst:21` `If numIceFields in the fort.25 file is set to 1, only the fort.225 file will be read; if numIceFields in the fort.25 file is set to 2 then both the fort.225 and fort.227 files will be read. The fort.225 (the basin scale, i.e., large scale coarse grid) and optional fort.227 (the region scale, i.e., smaller scale finer grid) files contain the actual ice percentage values (0.0 to 100.0%) and a value of -1.0 which means land or no data available. A value of -1.0% is treated as 0.0% ice in ADCIRC.`)

코드는 보간 셀의 음수 모서리 값을 비음수 모서리들의 평균으로 바꾼다. (`src/owi_ice.F:374` `if(CV(k) .ge. 0.d0) then`; `src/owi_ice.F:375` `CVbar = CVbar + CV(k)`; `src/owi_ice.F:376` `ibar = ibar + 1`; `src/owi_ice.F:379` `if (ibar.gt.0) CVbar = CVbar/real(ibar,8)`; `src/owi_ice.F:381` `if (CV(k).lt.0.d0) CV(k) = CVbar`)

모든 모서리가 음수이면 평균의 초기값 0이 남는다. (`src/owi_ice.F:374` `if(CV(k) .ge. 0.d0) then`; `src/owi_ice.F:379` `if (ibar.gt.0) CVbar = CVbar/real(ibar,8)`; `src/owi_ice.F:381` `if (CV(k).lt.0.d0) CV(k) = CVbar`)


<a id="ice-input-rules"></a>([inputfiles 보고서 §5 ICE-04, ICE-12, ICE-13, ICE-14](../../../_staging/recovery/compare/ADCIRC-inputfiles-vs-code.md#5-차이-결론); 항목: 얼음 입력의 생략된 후속 규칙) 근거: `models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:119` `if(numBlankSnaps.LT.0) then`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:120` `numSkipSnaps = ABS(numBlankSnaps)`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:121` `numBlankSnaps = 0`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:741` `if (PercentIce .lt. 1.d0) then`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:742` `WindIceDrag = WindDrag`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:773` `IF (PercentIce.lt.0.d0) then`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:776` `pic = min(PercentIce*0.01d0,1d0)`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:777` `Cform = Cform_max*(1d0-pic)**beta`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:778` `WindIceDrag = WindDrag*(1d0 - pic) + (Cskin + Cform)*pic`<br>`models/ADCIRC/raw/source_code/adcirc/src/wind.F:788` `IF(WindIceDrag.gt.WindDragLimit) WindIceDrag=WindDragLimit`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:249` `read (225,11,end=10000,err=99999)`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:250` `&      iLatc,iLongc,dxc,dyc,swlatc,swlongc,iCYMDHc,iMinc`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:273` `read(225,22,end=9999,err=99999) ((CiceB(i,j),i=1,iLongB),j=1,iLatB)`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:451` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:452` `&   message='Either unit 225 or 227 could not be read')`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:454` `10000 continue`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:459` `WRITE(screenunit,*) ' EITHER UNIT 225 or 227 RAN OUT'`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:460` `WRITE(screenunit,*) ' EXECUTION WILL CONTINUE'`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:471` `Ciceval(I)=0.d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:427` `if(Cice1.eq.-9999.9D0) then`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:428` `Ciceval(I)=0.d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:430` `if (rampfrac<36) then`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:431` `Cice1=Cice_env-(Cice_env-Cice1)*ramp`<br>`models/ADCIRC/raw/source_code/adcirc/src/owi_ice.F:433` `Ciceval(i) = Cice1`<br>문서는 음수 blank 수·법별 범위 처리·EOF 위치·환경 램프를 모두 설명하지 않는다. 코드는 각각 별도 조건으로 처리한다. 해석: 입력·계산 예외의 문서 누락이다. 결론: 문서 누락. v56.2.1의 얼음 reader는 snapshot 헤더 EOF와 데이터 배열 EOF를 다르게 처리한다. [10-12 결론 검증 보완]
([features 보고서 §5 I09 (303줄)<br>C21 (670줄)<br>C22 (671줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 얼음 문서의 0% 항력 자릿수) 근거: [10-12 결론 정정] I09·C22: 같은 PDF 2쪽의 Garratt 식에 무풍을 대입하면 0.00075다. 3쪽의 0.000075는 문서 내부 모순으로 B 문서 오기로 결론낸다. 판 차이만으로 설명하지 않는다. 오기 판정은 같은 PDF 2쪽 식과 3쪽 수치의 모순으로 확정할 수 있다. 원문의 오기 전파 방향에 관한 추정은 계속 구분한다.<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md` PDF 3쪽 / 인쇄 3쪽: `When pic = 0 the drag coefficient is equal to the minimum value for Garratt (.000075)`<br>src/wind.F:520 `Drag = 0.001d0*(0.75d0+0.067d0*WindSpeed)`<br>src/wind.F:762 `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`<br>src/wind.F:763 `&              + 0.2d0*pic*pic*pic)*0.01d0`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md` PDF 2쪽 `C_DN=10^{-3}(0.75+0.067*V)`; PDF 3쪽 `(.000075)`<br>해석: 같은 PDF 2쪽의 C_DN=10^−3(0.75+0.067*V)에 V=0을 대입하면 0.00075다. 3쪽의 0.000075와 직접 모순된다. 활성 IceCube도 0.075×0.01=0.00075다. 자료와 주석 사이의 오기 전파 방향은 확인하지 않았다. 결론: 문서 오기. 얼음 PDF의 Garratt 최솟값 0.000075는 0.00075의 자릿수 오기다.
([features 보고서 §5 I15 (309줄)<br>C19 (668줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 얼음 유형의 NWS 인코딩) 결론: B 문서 오기. 같은 PDF p.6의 `12000`·`12012` 예제와 `1000+` 설명이 모순된다. 근거와 NCICE 해석은 [NWS 인코딩 정본](#ice-nws-encoding)에 모았다. A 판 차이 분류는 철회한다. [10-12 결론 검증 정정]
([features 보고서 §5 K23 (587줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 얼음·기상 형식 조합 검사) 근거: src/read_input.F:2322 `IF((NCICE.GT.0).AND.`<br>src/read_input.F:2323 `&       ((NWS.EQ.1).OR.(NWS.EQ.2).OR.(NWS.EQ.7))) THEN`<br>src/read_input.F:2327 `&    'NCICE is not allowed for use with abs(NWS)=1,2, or 7.')`<br>src/read_input.F:2328 `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`<br>해석: 문서에 실제 검사 범위가 빠졌다. 메시지의 abs(NWS)와 조건문은 다르다. 서로 다른 종류의 추가 모순 근거를 확보하지 않아 E로 확대하지 않는다. 결론: 문서 누락. v56.2.1의 NCICE 조합 검사는 양의 NWS=1·2·7만 거부한다.
([features 보고서 §5 K24 (588줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: OWI 얼음 초기 스냅샷 생략) 결론: C 문서 누락. 음수 numBlankSnaps의 초기 스냅샷 생략은 [얼음 입력 후속 규칙 정본](#ice-input-rules)을 따른다. [10-12 결론 검증 보완]

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

IceCube 분기는 `IF (PercentIce.lt.0.d0) then`의 `ELSE`에서 `pic = PercentIce*0.01d0`을 계산한다. (`src/wind.F:758` `IF (PercentIce.lt.0.d0) then`; `src/wind.F:760` `ELSE`; `src/wind.F:761` `pic = PercentIce*0.01d0`) [10-12 전수 검증 보완] 해석: 이 식의 pic가 0–1인 범위는 PercentIce가 0–100인 경우다. (`src/wind.F:761` `pic = PercentIce*0.01d0`) [10-12 전수 검증 보완]

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

Lupkes 계열 분기는 `IF (PercentIce.lt.0.d0) then`에서 바람 항력을 사용한다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`; `src/wind.F:773` `IF (PercentIce.lt.0.d0) then`; `src/wind.F:774` `WindIceDrag = WindDrag`) [10-12 전수 검증 보완] 그 `ELSE` 분기는 pic의 상한을 1로 제한한 뒤 바람 항력과 얼음 항력을 결합한다. (`src/wind.F:775` `ELSE`; `src/wind.F:776` `pic = min(PercentIce*0.01d0,1d0)`; `src/wind.F:777` `Cform = Cform_max*(1d0-pic)**beta`; `src/wind.F:778` `WindIceDrag = WindDrag*(1d0 - pic) + (Cskin + Cform)*pic`) [10-12 전수 검증 보완] WindIceDrag는 각 정상 분기 뒤에 WindDragLimit 상한을 적용한다. (`src/wind.F:788` `IF(WindIceDrag.gt.WindDragLimit) WindIceDrag=WindDragLimit`) [10-12 전수 검증 보완]


([fort15 보고서 §5 L493, C22 (L860)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: 얼음 항력 이름과 초기 허용 검사) 근거: 확인한 원문: `docs/technical_reference/parameter_definitions/index.rst:2864` ` the wind drag coefficient formulation can also be set to IceCube (the default) or RaysIce. `<br>`src/wind.F:367` ` if (NWS.eq.0) return `<br>`src/wind.F:371` ` SELECT CASE(TRIM(DragLawString)) `<br>`src/wind.F:372` ` CASE("Garratt","GARRATT","garratt","default") `<br>`src/wind.F:380` ` CASE("Powell","POWELL","powell") `<br>`src/wind.F:391` ` CASE DEFAULT `<br>`src/wind.F:394` ` call terminate(exit_code=ADCIRC_EXIT_FAILURE, `<br>`src/wind.F:738` ` CASE("RaysIce") `<br>`src/wind.F:749` ` CASE("IceCube") `<br>`src/wind.F:767` ` CASE("Lupkes","default","Powell") `<br>해석: initWindModule은 NWS!=0에서 IceCube·RaysIce·Lupkes 문자열을 거부하지만 같은 판 문서와 WindIceDrag는 이 선택을 제시한다. `src/wind.F:364–365`의 선행 항력 검사와 함수 매핑은 이 SELECT CASE의 문자열을 허용값으로 바꾸지 않는다. `checkWindDragType`의 기본 경로도 원래 DragLawString을 다시 대입하지 않는다 (`src/wind.F:408–424`). 따라서 NWS가 0인 우회 경로 외에는 이 충돌을 해소하지 못한다. default와 Powell은 Lupkes 계열 별칭이며 CASE DEFAULT는 네 번째 항력법이 아니다. IceCube 기본이라는 문서 설명도 이 분기와 다르다. 결론: 코드 결함 후보. 얼음 항력의 명시적 문자열 선택은 initWindModule과 WindIceDrag가 충돌하는 결함 후보이다. [10-12 결론 검증 정정]
<a id="ice-nws-encoding"></a>([fort15 보고서 §5 C21 (L859), C25 (L863)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: 얼음 PDF의 NWS=1000+ 문구) 근거: 확인한 원문: `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:13 (PDF p.1)` ` Modifications to ADCIRC v49.64+ for ICE Coverage `<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:18 (PDF p.6)` ` NWS = 1000+ your normal wind type option `<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:18 (PDF p.6)` ` 12000 `<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md:18 (PDF p.6)` ` 12012 `<br>`src/read_input.F:1775` ` NCICE = INT(ABS(NWS)/1000) `<br>`src/read_input.F:1776` ` NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS `<br>`src/read_input.F:2316` ` IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN `<br>해석: [10-12 결론 정정] 단순히 역사적 PDF의 옛 입력 규칙이라고 가를 수 없다. 같은 PDF p.6이 OWI 얼음값 12000 및 NWS=12012 예제를 제시한다. NWS=12에 1000을 더하면 1012이므로 예제와 모순된다. v56.2.1의 천 단위 분리는 12012에서 NCICE=12를 만든다. 따라서 1000+ 문구는 문서 내부 오기이다. 결론: 문서 오기. 얼음 PDF의 NWS=1000+ 문구는 같은 쪽의 OWI 얼음값 12000 및 입력 예제 12012와 모순된다. [10-12 결론 검증 보완]
<a id="ice-default-drag"></a>([fort15 보고서 §5 C23 (L861)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: 기본 DragLawString의 빌드 조건) 근거: 확인한 원문: `src/wind.F:131` ` #ifndef POWELL `<br>`src/wind.F:132` ` CHARACTER(len=10) :: DragLawString = 'default' ! controls wind drag formulation `<br>`src/wind.F:134` ` #else `<br>`src/wind.F:139` ` CHARACTER(len=10) :: DragLawString = 'Powell' `<br>`src/wind.F:767` ` CASE("Lupkes","default","Powell") `<br>해석: C23 노트는 두 초기값이 존재하는 이유인 POWELL 조건을 빠뜨렸다. 두 값이 WindIceDrag에서 Lupkes 계열로 간다는 결론 자체는 맞는다. 결론: 문서 누락. DragLawString의 기본값은 POWELL 빌드 조건에 따라 default 또는 Powell이다. [10-12 결론 검증 보완]
([fort15 보고서 §5 C24 (L862)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: IceCube 최대값 규칙의 적용 범위) 근거: 확인한 원문: `_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md p.3` ` The maximum drag coefficient value, between Garratt (based on wind speed) and ICE CUBE (based on % of ice) is what is used by ADCIRC. `<br>`src/wind.F:749` ` CASE("IceCube") `<br>`src/wind.F:764` ` WindIceDrag = max(IceDrag,WindDrag) `<br>`src/wind.F:767` ` CASE("Lupkes","default","Powell") `<br>`src/wind.F:776` ` pic = min(PercentIce*0.01d0,1d0) `<br>`src/wind.F:778` ` WindIceDrag = WindDrag*(1d0 - pic) + (Cskin + Cform)*pic `<br>해석: C24는 기존 보고서가 이미 오류가 아닌 조건 보완으로 표시한 행이다. PDF의 규칙은 IceCube 분기에 해당한다. 다른 기본 분기는 면적 비율 결합을 사용하므로 노트에 분기 조건을 적어야 한다. C는 조건 설명의 누락이며 PDF 자체의 오기 판정이 아니다. 결론: 문서 누락. 얼음 항력과 바람 항력 중 큰 값을 쓰는 규칙은 IceCube 분기에 적용한다.
([features 보고서 §5 I02 (296·710줄)<br>I04 (298·711줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 별도 얼음 마찰·질량 방정식) 근거: docs/user_guide/special_features/ice_modifications.rst:12 `2. Ice friction effects on water flow`<br>src/wind.F:984 `WDragCo = WindIceDrag(WDragCo,ciceout(i))`<br>src/wind.F:986 `WSX2(I) = RampMete*airwaterdensityrat*WDragCo*WindX*WindMag`<br>src/momentum.F:726 `WSX=DTO2*IFWIND*(WSX1(I)/H1(I)+WSX2(I)/H2(I))`<br>src/momentum.F:727 `WSY=DTO2*IFWIND*(WSY1(I)/H1(I)+WSY2(I)/H2(I))`<br>docs/user_guide/special_features/ice_modifications.rst:14 `4. Modifications to mass conservation equations to account for ice presence`<br>src/timestep.F:637 `if (ncice.ne.0.and.(ncice.ne.14) .and. (ncice.ne.17)) then`<br>src/timestep.F:640 `CICEOUT(I) = CICE1(I) + CICE_TRatio*(CICE2(I)-CICE1(I))`<br>src/gwce.F:2007 `ETA2(I)=NODECODE(I)*(ETAS(I)+dynamicWaterLevelCorrectionDelta(I))+ETA1(I) !COMPUTE NEW ELEVATIONS tgaContOffset`<br>해석: 전체 `models/ADCIRC/raw/`에서 `rg -i`로 `CICE|NCICE|ice.?friction|ice.?mass|WindIceDrag`를 다시 검색했다. 보조 프로그램의 얼음 자료 처리와 SWAN 자체 얼음 감쇠도 검색된다. 이들은 ADCIRC의 유동 운동량·질량 방정식과 구분한다. 농도 보간과 풍응력 계수 수정은 있지만 별도 얼음 항은 없다. ice_modifications.rst가 그 기능을 열거한 근거는 해당 코드에서 확인되지 않는다. 결론: 문서에만 있음. v56.2.1의 ADCIRC 운동량·GWCE 경로에는 별도 얼음 마찰항과 얼음 질량항이 없다. [10-12 결론 검증 보완]
([features 보고서 §5 K20 (584줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: Lupkes 얼음 항력의 계수) 근거: src/wind.F:733 `REAL(8) :: Cskin = 1.5d-3, Cform_max = 3.67d-3, beta = 0.6d0`<br>src/wind.F:767 `CASE("Lupkes","default","Powell")`<br>src/wind.F:776 `pic = min(PercentIce*0.01d0,1d0)`<br>src/wind.F:777 `Cform = Cform_max*(1d0-pic)**beta`<br>src/wind.F:778 `WindIceDrag = WindDrag*(1d0 - pic) + (Cskin + Cform)*pic`<br>해석: 대조한 얼음 문서는 이 분기의 계수와 Cform 식을 적지 않았다. 기본 분기의 판 변화는 I13·I29와 구분한다. 결론: 문서 누락. Lupkes 분기는 Cskin=1.5e-3·Cform_max=3.67e-3·beta=0.6으로 얼음 항력을 계산한다.
([features 보고서 §5 K21 (585줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 얼음 농도 범위 처리) 근거: src/wind.F:758 `IF (PercentIce.lt.0.d0) then`<br>src/wind.F:759 `WindIceDrag = WindDrag`<br>src/wind.F:761 `pic = PercentIce*0.01d0`<br>src/wind.F:773 `IF (PercentIce.lt.0.d0) then`<br>src/wind.F:774 `WindIceDrag = WindDrag`<br>src/wind.F:776 `pic = min(PercentIce*0.01d0,1d0)`<br>해석: 대조 문서는 Lupkes와 IceCube의 입력 범위 처리 차이를 적지 않았다. 음수 입력이면 두 분기 모두 WindDrag를 대입한다. 이후 `src/wind.F:788`의 `IF(WindIceDrag.gt.WindDragLimit) WindIceDrag=WindDragLimit`을 적용한다. 결론: 문서 누락. Lupkes 분기만 얼음 비율의 상한을 1로 제한한다. [10-12 결론 검증 정정]
([features 보고서 §5 K22 (586줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: RaysIce의 저농도 분기) 근거: src/wind.F:741 `if (PercentIce .lt. 1.d0) then`<br>src/wind.F:742 `WindIceDrag = WindDrag`<br>src/wind.F:744 `pic = PercentIce*0.01d0`<br>src/wind.F:745 `IceDrag = (0.125d0 + 0.5d0*pic*(1.0d0-pic))*0.01d0`<br>src/wind.F:746 `WindIceDrag = max(IceDrag,WindDrag)`<br>해석: 대조 문서는 RaysIce의 1퍼센트 미만 입력 분기를 적지 않았다. 결론: C 문서 누락. `PercentIce .lt. 1.d0`이면 WindDrag를 대입한다. 이후 `src/wind.F:788`의 `IF(WindIceDrag.gt.WindDragLimit) WindIceDrag=WindDragLimit`을 적용한다. [10-12 결론 검증 정정]
([features 보고서 §5 C20 (669줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: ICE CUBE 다항식의 출처) 근거: 이 다항식의 직접 원문 근거를 PDF와 구분해야 한다. docs/technical_reference/input_files/fort25.rst:47 `\mathrm{CDF} = [0.075 + 0.75 \mathrm{IC} – 0.9 \mathrm{IC}^2 + 0.2 \mathrm{IC}^3 ] 10^{-2} \text{ (IceCube formulation, this is the default)}`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/adcirc_modifications_for_ice.pdf/p001-010.md` PDF 3쪽: `0.000075`, `pic=50`, `pic=100`의 설계 조건.<br>해석: 보고서의 노트는 PDF 서술과 현행 rst의 계수식을 구분하지 않았다. 같은 식을 인용하더라도 실제 식이 인쇄된 원문에 귀속해야 한다. 결론: 문서 오기. ICE CUBE 다항식의 계수 원문은 fort25.rst이며 얼음 PDF 3쪽은 설계 조건을 서술한다.
([features 보고서 §5 C23 (672줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 얼음 기본 문자열의 빌드 조건) 결론: C 문서 누락. POWELL 조건에 따른 기본 문자열과 Lupkes 분기의 근거는 [기본 항력 정본](#ice-default-drag)에 모았다. [10-12 결론 검증 보완]

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

결합 동작은 [IICE=2 dry forcing](#ice-dry)과 [IICE=3 결합 버퍼](#ice-buffer)를 따른다. SWAN 감쇠 입력에 대한 결론은 [C25의 E 후보](#ice-swan-disconnect)를 따른다. [10-12 결론 검증 정정]

이번 대조는 SWAN 내부의 파랑 감쇠 알고리즘을 확인하지 않음. (`src/couple2swan.F:1033` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.2)) THEN`; `src/couple2swan.F:1045` `SWAN_ETA2(IN,:) = - DP(IN)`; `src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)

해석: 전달 자료의 SWAN 물리 사용은 별도 검증 사항이다(정적 판독, 실행 미확인). (`src/couple2swan.F:1055` `IF((NCICE.NE.0).AND.(SWAN_IICE.EQ.3)) THEN`; `src/couple2swan.F:1058` `SWAN_CICE2(IN,1) = CICE1(IN)`; `src/couple2swan.F:1059` `SWAN_CICE2(IN,2) = CICE2(IN)`)
상세는 [adcirc-swan-coupling](../source-analysis/adcirc-swan-coupling.md).

## 5. 정리

| 축 | 내용 |
|---|---|
| 물리 범위 | 단독 운동량 경로의 풍응력 항력 수정이다. (`src/wind.F:984` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`; `src/wind.F:1457` `WDragCo = WindIceDrag(WDragCo,ciceout(i))`) 별도 열역학·유빙 응력 진화식은 확인하지 않음. |
| 입력 | 현재 허용 NCICE는 0·10·12·14·17이다. (`src/read_input.F:2316` `IF (NCICE.NE.0.AND.NCICE.NE.10.and.NCICE.NE.12.AND.NCICE.ne.14.AND.NCICE.ne.17) THEN`; `src/read_input.F:2317` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`) OWI 예시 NWS=12012는 NCICE=12와 NWS=12를 선택한다. (`src/read_input.F:1775` `NCICE = INT(ABS(NWS)/1000)`; `src/read_input.F:1776` `NWS = INT(ABS(NWS)-NCICE*1000)*INT(NWS/ABS(NWS))  !RESETTING NWS/NRS`) `CICE_TIMINC`를 지정한다. |
| 항력 선택 | default·Powell의 WindIceDrag 선택은 Lupkes 계열이다. (`src/wind.F:767` `CASE("Lupkes","default","Powell")`) 초기 WindInit은 문자열을 검사한다. (`src/wind.F:371` `SELECT CASE(TRIM(DragLawString))`; `src/wind.F:391` `CASE DEFAULT`; `src/wind.F:394` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`) |
| 결합 | [IICE=2 dry forcing](#ice-dry), [IICE=3 결합 버퍼](#ice-buffer), [SWAN 감쇠 입력 연결의 E 후보](#ice-swan-disconnect)를 따른다. [10-12 결론 검증 정정] |
| 주의 | PDF·코드 주석의 0.000075와 코드 식의 0.00075가 다르다. (`raw/manuals/pdfs/adcirc_modifications_for_ice.pdf, PDF 쪽 3 / 인쇄 쪽 3`; `src/wind.F:752` `C....... the minimum value for Garratt (.000075), when pic = 50`; `src/wind.F:762` `IceDrag = (0.075d0 + 0.75d0*pic - 0.9d0*pic*pic`; `src/wind.F:763` `&              + 0.2d0*pic*pic*pic)*0.01d0`) 해석: 자릿수 오류 가능성이 있다(정적 판독, 실행 미확인). |
