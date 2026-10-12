---
title: "adcirc wetting drying implementation"
topic: general
canonical_source: self
citation_status: verified
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
has_source_needed: true
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-wetting-drying-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC wetting/drying — NOLIFA, H0, NODECODE, transitions

## Scope

Code-level walk-through of the wet/dry algorithm: when nodes flip wet→dry, when dry→wet, what thresholds (`H0`, `HABSMIN`, `HOFF`) control them, and how it interacts with bottom friction and momentum equations.

수심 하한(clamp)을 제거해 천해 노드가 다수 활성화되는 메시에서는 wet/dry 거동이 특히 중요해진다.

## A. NOLIFA flag effect

- `IFNLFA = 0` only when `NOLIFA=0`; for `NOLIFA=1` and `NOLIFA=2`: `IFNLFA=1` at `[file=src/adcirc.F line=286-290]`
  → Both `NOLIFA=1` and `=2` use nonlinear depth `H = DP + IFNLFA*ETA`
- **Wet/dry hard-gated to `NOLIFA=2`**: `computeWettingAndDrying` returns immediately if not 2 at `[file=src/wetdry.F line=204-206]`
- `IFNLFA` used in matrix terms (`DPAvg`, `H00`, `H0N*`): `[file=src/gwce.F line=506-507, 1318-1321, 2474, 2571-2573]`
- `computeWettingAndDrying`은 `nolifa.ne.2`이면 반환한다 (`[file=src/wetdry.F line=204]` `if (nolifa.ne.2) then`). GWCE와 운동량의 조립식은 `NODECODE·NOFF`를 직접 곱한다 (`[file=src/gwce.F line=1010]` `NC1=NODECODE(NM1)`; `[file=src/gwce.F line=1015]` `NCELE=NC1*NC2*NC3*NOFF(IE)`; `[file=src/momentum.F line=309]` `NC1=NODECODE(NM1)`; `[file=src/momentum.F line=312]` `NCELE=NC1*NC2*NC3*NOFF(IE)`). 동적 침수·노출 상태 변경 조건과 마스크 소비 조건은 서로 다르다 (`[file=src/wetdry.F line=204]` `if (nolifa.ne.2) then`; `[file=src/gwce.F line=1015]` `NCELE=NC1*NC2*NC3*NOFF(IE)`; `[file=src/momentum.F line=312]` `NCELE=NC1*NC2*NC3*NOFF(IE)`).

So:
| NOLIFA | Wet/dry? | Nonlinear depth (H = DP + ETA)? |
|--------|----------|--------------------------------|
| 0 | No | No |
| 1 | No | Yes (no node state changes) |
| 2 | Yes | Yes |

## B. H0 thresholds

문서 판: 1995년 후보·요소 구현 보고서와 1999년 v34.XX 보고서. 코드 판: v56.2.1 (`CMakeLists.txt:92` `set(ADCIRC_VERSION_STRING "v56.2.1")`).

- `H0` parsed by `READ_INPUT()` from fort.15 (referenced at `[file=src/adcirc.F line=227, 239]`)
- Computed during `initializeWettingAndDrying` at `[file=src/wetdry.F line=126-127]`:
  - `HABSMIN=0.8*H0`는 수심 하한 조정값이다 (`[file=src/wetdry.F line=126]` `habsmin=0.8d0*h0`; `[file=src/wetdry.F line=244]` `IF(HTOT.LT.HABSMIN)THEN`). D1은 현재 `NODECODE(I).EQ.1`인 절점에서 수심을 검사한다 (`src/wetdry.F:235` `IF(NODECODE(I).EQ.1) THEN`). [10-12 전수 검증 보완] 이 절점의 노출 수심 조건은 `IF(HTOT.LE.H0) THEN`이다 (`[file=src/wetdry.F line=241]` `IF(HTOT.LE.H0) THEN`). [10-12 전수 검증 보완]
  - `HOFF = 1.2 * H0` (re-wetting / element-active threshold)
- D1 (drying) fires when `HTOT <= H0` at `[file=src/wetdry.F line=241-246, 271, 278]`; if `HTOT < HABSMIN`, ETA is clipped upward
- `HOFF` controls element activity (`NOFF`) and re-wetting checks at `[file=src/wetdry.F line=306, 370, 517, 664, 863-864, 1144-1202]`


([features 보고서 §5 W09 (124·703줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 최소 수심의 단계별 증가) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich03.pdf/p001-018.md` PDF 9쪽 / 인쇄 7쪽: `the value of Hmin is ramped up from zero to the value specified in the input file over a specified number of time steps (typically on the order of 10 to 20).`<br>src/wetdry.F:241 `IF(HTOT.LE.H0) THEN`<br>src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>해석: 1995년 원문은 당시 요소 기법의 이력 제어를 설명한다. wetdry.F와 read_input.F에서 Hmin·ramp·H0를 검색했지만 H0의 단계별 증가 상태를 찾지 못했다. 결론: 판 차이. v56.2.1의 기본 노출 검사는 1995년 Hmin 증가 절차 대신 H0와 직접 비교한다.
([features 보고서 §5 W17 (132줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 노출 문턱의 등호) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 7쪽 / 인쇄 6쪽: `H < H0` (LaTeX 전사)<br>src/wetdry.F:241 `IF(HTOT.LE.H0) THEN`<br>해석: v34.XX 원문의 H<H0와 v56.2.1의 HTOT.LE.H0가 다르다. 현재 동작의 기준은 활성 조건문이다. 결론: 판 차이. v56.2.1은 HTOT가 H0와 같은 절점도 노출로 판정한다.
([features 보고서 §5 W18 (133줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 노출 수심 하한) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 7쪽 / 인쇄 6쪽: `H < H0/10;\quad H=H0/10` (LaTeX 전사)<br>src/wetdry.F:126 `habsmin=0.8d0*h0`<br>src/wetdry.F:278 `IF(HTOT.LT.HABSMIN) ETA2(I)=HABSMIN-DP(I)`<br>해석: v34.XX 원문의 수심 하한과 현재 초기화 상수가 다르다. 결론: 판 차이. v56.2.1은 구판 H0/10 대신 0.8*H0를 노출 수심 하한으로 사용한다.
([features 보고서 §5 W30 (145줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 구판 권고값과 현재 입력) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 8쪽 / 인쇄 7쪽: `reasonable values might be H0 = 0.1m, NODEDRYMIN = 300/Dt, NODEWETMIN = 300/Dt, VELMIN = 0.05 m/s`<br>src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>해석: reasonable values might be는 당시 권고다. 현재는 fort.15에서 값을 읽으며 대기 단계의 사용도 바뀌었다. 결론: 판 차이. v34.XX의 H0·대기 단계·VELMIN 예시는 v56.2.1의 기본값이 아니다.
([features 보고서 §5 C01 (650줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: HABSMIN 용도) 근거: 용도 오기. src/wetdry.F:126 `habsmin=0.8d0*h0`<br>src/wetdry.F:241 `IF(HTOT.LE.H0) THEN`<br>src/wetdry.F:244 `IF(HTOT.LT.HABSMIN)THEN`<br>해석: 보고서가 인용한 노트의 drying threshold라는 이름은 실제 비교값 H0와 모순된다. 결론: 문서 오기. HABSMIN=0.8*H0는 수심 하한 보정값이다.
([features 보고서 §5 C06 (655줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: H0·VELMIN의 표준 기본값이라는 설명) 근거: 4절 C06이 보존한 노트는 H0·VELMIN의 값을 표준 기본값으로 설명했다.<br>추가 원문: src/read_input.F:3020–3021: `IF(NOLIFA.EQ.2) THEN` / `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`. 3033–3034줄의 ELSE 경로도 `READ(15,*) H0`이다. 3039–3042줄은 `IF(H0.LE.0D0)THEN`에서 종료한다.<br>docs/technical_reference/parameter_definitions/index.rst:693은 H0를 `typical value 0.01 – 0.1 m`로 설명한다. 703줄은 VELMIN에 `A typical value might be 0.05 m/s.`라고 적는다.<br>추가 원문: `models/ADCIRC/raw/source_code/adcircpy/adcircpy/fort15.py:1747–1751`의 H0 속성은 미설정일 때 `return 0.01`이다. 같은 파일 1780–1784줄의 VELMIN 속성도 `return 0.01`이다.<br>testsuite의 adcirc_alaska_ice-2d/fort.15:31은 H0=0.1과 VELMIN=0.01을 입력한다. adcirc_shinnecock_inlet/fort.15:26은 H0=0.05와 VELMIN=0.02를 입력한다.<br>해석: ADCIRC는 침수·노출 경로에서 두 값을 fort.15의 필수 입력으로 읽는다. 문서는 typical 값으로 설명한다. 외부 생성기와 시험 입력도 서로 다른 값을 사용한다. 이를 ADCIRC 본체의 표준 기본값으로 바꿔 적은 노트 인용을 B로 분류한다.<br>추가 검색: raw와 판독 기록 전체에서 `H0`, `VELMIN`, `default`, `0.001`을 검색했다. adcircpy의 기본 입력 생성 코드와 testsuite 입력을 추가로 대조했다. 결론: 문서 오기. H0와 VELMIN은 fort.15 입력값이며 문서의 typical 값이나 외부 생성기의 초기값을 ADCIRC의 표준 기본값으로 적으면 안 된다. [10-12 G 재판정]
([features 보고서 §5 C08 (657줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: H0=0.1의 필수성) 근거: 현재 코드의 일반 필수값으로 H0=0.1을 강제할 근거 없음. src/wetdry.F:241 `IF(HTOT.LE.H0) THEN`<br>src/wetdry.F:370 `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`<br>입력 기본값의 근거 미확인. src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>src/wetdry.F:127 `hoff=1.2d0*h0`<br>해석: 보고서의 영구 노출 주장은 현재 조건문과 모순된다. H0=0.05이고 두 습윤 이웃 수심이 HOFF=0.06 이상이면 H0=0.1 없이도 보통 W1 검사를 통과할 수 있다. 이는 조건식의 반례이며 특정 격자의 침수를 실행으로 보장한 결과가 아니다. 결론: 문서 오기. v56.2.1의 침수·노출 조건은 입력한 H0를 사용하므로 H0=0.1을 보편 필수값으로 요구하지 않는다.

## C. NODECODE (per-node wet/dry status)

- D1 update per timestep at `[file=src/wetdry.F line=234-285]` — currently wet (`NODECODE=1`) flips to dry when `HTOT <= H0`
- Wet→dry: both `NNODECODE` and `NODECODE` set to 0 immediately at `[file=src/wetdry.F line=274-275, 279-280]`
- Dry→wet (W1) requires:
  - Element has exactly two wet nodes (`NCTOT=2`) at `[file=src/wetdry.F line=354-355]`
  - 보통 W1은 두 wet 노드가 모두 `HOFF` 이상이어야 한다 (`[file=src/wetdry.F line=370]` `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`). 압력차와 유속 계산에는 그중 수위가 높은 한 노드를 쓴다 (`[file=src/wetdry.F line=371]` `NM123=NM1`; `[file=src/wetdry.F line=372]` `IF(ETA2(NM2).GT.ETA2(NM1)) NM123=NM2`; `[file=src/wetdry.F line=375]` `DELETA=ETA2(NM123)-ETA2(NM3)`).
  - Computed velocity exceeds `VELMIN` at `[file=src/wetdry.F line=440-444]` (and symmetric branches at 515+, 662+)
- Final reconciliation: `NODECODE := NNODECODE` at `[file=src/wetdry.F line=1413-1417]` — committed flip point

## D. Velocity reset on dry nodes

- `VELMIN` enforced as activation criterion: `VEL > VELMIN` at `[file=src/wetdry.F line=440, 588, 734]`
- All-nodes-wet branches: `VEL := VELMIN` before `TK` formation at `[file=src/wetdry.F line=881, 946, 1011]` — prevents singularity
- Dry-node zeroing in momentum: `NCI=NODECODE(I)` multiplication at `[file=src/momentum.F line=714, 783-786, 799-803]`. With `NCI=0`, momentum collapses
- Explicit wet/dry-interface zeroing exists only as **commented-out code** at `[file=src/momentum.F line=1134-1137, 1897-1900]`

## E. Dry→wet recovery

- Primary path: 2-wet-node triangle (`NCTOT=2`) at `[file=src/wetdry.F line=354-355]`
- 보통 W1은 두 wet 노드가 모두 `HOFF` 이상이어야 한다 (`[file=src/wetdry.F line=370]` `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`). 압력차와 유속 계산에는 그중 수위가 높은 한 노드를 쓴다 (`[file=src/wetdry.F line=371]` `NM123=NM1`; `[file=src/wetdry.F line=372]` `IF(ETA2(NM2).GT.ETA2(NM1)) NM123=NM2`; `[file=src/wetdry.F line=375]` `DELETA=ETA2(NM123)-ETA2(NM3)`). 이 문장은 장벽·연직 요소 벽·지형 변화의 추가 경로를 포함하지 않는다.
- Final velocity check: hydraulic-gradient-derived `VEL > VELMIN` at `[file=src/wetdry.F line=440-444, 588-591, 734-737]`
- 추가 지형 변화 경로는 `IF ((NDDT.NE.0).AND.(IT.LE.BTIME_END+1) ) THEN`에서 실행한다 (`[file=src/wetdry.F line=845]` `IF ((NDDT.NE.0).AND.(IT.LE.BTIME_END+1) ) THEN`). 이 경로는 앞선 D1·침수 장벽 처리까지 반영한 `NODECODE`의 세 노드가 모두 wet인 상태가 아닌지 검사한다 (`[file=src/wetdry.F line=851]` `IF(NCTOT.lt.3) THEN   !If not wet from previous time step`; `src/wetdry.F:275` `NODECODE(I) = 0`; `src/wetdry.F:280` `NODECODE(I)=0`; `src/wetdry.F:314` `NODECODE(I)=1`; `src/wetdry.F:850` `NCTOT=NODECODE(NM1)+NODECODE(NM2)+NODECODE(NM3)`). [10-12 전수 검증 정정] 이 경로는 현재 `NNODECODE`의 세 노드도 모두 wet인 상태가 아닌지 검사한다 (`[file=src/wetdry.F line=852]` `NCTOT=NNODECODE(NM1)+NNODECODE(NM2)+NNODECODE(NM3)`; `[file=src/wetdry.F line=853]` `if(NCTOT.lt.3) then !if not alreay made wet for this time step`). 세 수심이 모두 `HOFF` 이상이면 dry 노드를 wet으로 바꾼다 (`[file=src/wetdry.F line=863]` `IF( (HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF).AND.`; `[file=src/wetdry.F line=864]` `&                   (HTOTN3.GE.HOFF) ) THEN`).


([features 보고서 §5 W01 (116줄)<br>W02 (117·702줄)<br>W03 (118줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 1995년 DCA·NWA 후보 기법) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich01.pdf/p001-018.md` PDF 5쪽 / 인쇄 3쪽: `Therefore, both wet and dry nodes participate equally in the model computations.`<br>src/wetdry.F:1373 `NCEle=NC1*NC2*NC3*NOFF(IE)`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich01.pdf/p001-018.md` PDF 5쪽 / 인쇄 3쪽: `At present we simply multiply the deep water drag coefficient, C_{f\min}, by a large number (e.g., 100 - 1000) when H < 2H_{\min}.` (본문 기호 LaTeX 전사)<br>src/wetdry.F:213 `IF (directvelWD.AND.useHF) THEN`<br>src/wetdry.F:416 `TKWET = MAX(FRIC(NM123)*(IFLINBF+(VELMIN/H1)*`<br>src/wetdry.F:418 `&                                  (1.D0+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA))),`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich01.pdf/p001-018.md` PDF 6쪽 / 인쇄 4쪽: `If a node is currently dry and ζ at any adjacent wet node rises above ζ at the node being checked, the node is considered to have wetted.`<br>src/wetdry.F:355 `IF((NCTOT.EQ.2) .AND. (IBTYPE64FLOODPLAINCNT.NE.3)) THEN  ! (IBTYPE64FLOODPLAINCNT.NE.3) is added to avoid excessie wetting when all three nodes of an element on a floodplain are on a IBTYPE=64 boundary. 10/16/2023 sb`<br>src/wetdry.F:370 `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`<br>src/wetdry.F:440 `IF(VEL.GT.VELMIN) THEN`<br>판독 기록 `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich01.pdf/p001-018.md` PDF 1쪽의 날짜는 1995년 1월 30일이다.<br>해석: 1995년 보고서는 DCA·NWA·EWA를 비교한다. 후보의 모든 절점 참여와 큰 항력 배율을 현재 요소 기법의 요구사항으로 읽으면 안 된다. 결론: 판 차이. v56.2.1은 1995년 후보 기법 대신 두 습윤 절점의 HOFF와 VELMIN을 검사하는 요소 침수 경로를 사용한다.
([features 보고서 §5 W08 (123줄)<br>W15 (130줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 습윤·건조 인터페이스 no-slip) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich03.pdf/p001-018.md` PDF 9쪽 / 인쇄 7쪽: `Therefore we have chosen to implement a no slip condition in ADCIRC at all interface nodes.`<br>src/momentum.F:1134 `c        IF(MJU(I).NE.NODELE(I)) THEN !uncomment for essential`<br>src/momentum.F:1135 `c           UBAR2(I)=0.D0    !no slip and normal flux`<br>src/momentum.F:1136 `c           VBAR2(I)=0.D0    !on wet/dry interface nodes`<br>src/momentum.F:1137 `c        ENDIF`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 7쪽 / 인쇄 6쪽: `Therefore we have chosen to implement a no slip condition in ADCIRC at all nodes lying along a wet/dry boundary.`<br>src/momentum.F:1134 `c        IF(MJU(I).NE.NODELE(I)) THEN !uncomment for essential`<br>src/momentum.F:1135 `c           UBAR2(I)=0.D0    !no slip and normal flux`<br>src/momentum.F:1136 `c           VBAR2(I)=0.D0    !on wet/dry interface nodes`<br>src/momentum.F:1137 `c        ENDIF`<br>해석: 1995년 구현 보고서와 v34.XX 설명은 당시 선택한 no-slip을 적는다. v56.2.1에서 같은 처리는 uncomment 지시가 붙은 비활성 구문이다. 결론: 판 차이. v56.2.1은 구판 문서의 모든 습윤·건조 인터페이스 유속을 0으로 만드는 구문을 주석으로 남긴다.
([features 보고서 §5 W11 (126줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 수위 경사와 바람 응력의 공동 습윤 조건) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich03.pdf/p001-018.md` PDF 10쪽 / 인쇄 8쪽: `the water level gradient and`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich03.pdf/p001-018.md` PDF 10쪽 / 인쇄 8쪽: `the vector sum of the water level gradient and the wind stress both favor water motion toward all dry nodes that are connected to the interface node.`<br>src/wetdry.F:372 `IF(ETA2(NM2).GT.ETA2(NM1)) NM123=NM2`<br>src/wetdry.F:375 `DELETA=ETA2(NM123)-ETA2(NM3)`<br>src/wetdry.F:420 `VEL=G*(DELETA/DELDIST)/TKWET`<br>src/wetdry.F:440 `IF(VEL.GT.VELMIN) THEN`<br>해석: 1995년 원문은 모든 연결 건조 절점에 대한 수위 경사와 바람 응력 벡터 조건을 적는다. 활성 식 VEL=G*(DELETA/DELDIST)/TKWET에는 그 바람 벡터 검사가 없다. 결론: 판 차이. v56.2.1의 기본 W1은 선택한 습윤 절점과 건조 절점의 수위차로 재침수 유속을 계산한다.
([features 보고서 §5 W21 (136줄)<br>K02 (566줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 재침수 유속의 후보 절점 선택) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 8쪽 / 인쇄 7쪽: `This calculation is then repeated along a line connecting the other wet node on the element with the dry node to determine the corresponding depth-averaged velocity.`<br>src/wetdry.F:371 `NM123=NM1`<br>src/wetdry.F:372 `IF(ETA2(NM2).GT.ETA2(NM1)) NM123=NM2`<br>src/wetdry.F:375 `DELETA=ETA2(NM123)-ETA2(NM3)`<br>src/wetdry.F:420 `VEL=G*(DELETA/DELDIST)/TKWET`<br>해석: v34.XX 문서는 두 습윤 절점에서 각각 유속을 계산한다. 현재 분기는 수위로 먼저 절점을 고른다. 결론: 판 차이. v56.2.1의 기본 W1은 수위가 더 높은 습윤 절점 하나를 선택한다.
([features 보고서 §5 W25 (140·707줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 지정 유량 경계의 일괄 습윤) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 8쪽 / 인쇄 7쪽: `or a specified discharge boundary that is actively discharging flow into the domain at that node, all nodes in this element must be wet.`<br>src/timestep.F:877 `CASE(2,12,22,52)`<br>src/timestep.F:878 `QN2(I)=QN2(I)+rotate_normal_flux(ICS, I, QNAM(J,I)*RFF*COS(ARGJ-QNPH(J,I)))`<br>src/timestep.F:1023 `NIBNODECODE(:) = 0`<br>src/wetdry.F:813 `NBNCTOT=NIBNODECODE(NM1)+NIBNODECODE(NM2)+NIBNODECODE(NM3)`<br>src/wetdry.F:1087 `IF((NIBCNT(I).GT.0).AND.(NNODECODE(I).EQ.0)) THEN`<br>해석: v34.XX 문서는 지정 유량 유입에도 요소 전체 습윤을 적용했다. timestep.F·weir_boundary.F90·wetdry.F에서 NIBNODECODE·CASE(2,12,22,52)를 검색하면 수신 플래그 대입은 장벽·관류 경로에 있다. 결론: 판 차이. v56.2.1의 지정 유량 경계 2·12·22는 장벽 수신 플래그를 통한 요소 강제 습윤을 수행하지 않는다.
([features 보고서 §5 W31 (146줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 경사면 상류 흐름의 적용 한계 주장) 근거: 문서 원문: `1999_Luettich01.pdf` PDF p.7 / 인쇄 p.6: `only wetting and drying due to subcritical flow over sloping inclines can realistically be simulated.`<br>문헌 서지: Richard A. Luettich, Jr.; Joannes J. Westerink (March 11, 1999), *Elemental Wetting and Drying in the ADCIRC Hydrodynamic Model: Upgrades and Documentation for ADCIRC Version 34.XX*, Contractors Report, Contract No. DACW39-95-K-0011. 표지와 적용 한계의 판독 기록은 `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md:13,19`이다.<br>대응 코드: `src/wetdry.F:411` `IF (directvelWD.AND.useHF) THEN`<br>`src/wetdry.F:412` `VEL=sqrt(g*H1*DELETA/DELDIST)`<br>`src/wetdry.F:413` `ELSEIF (directvelWD) THEN`<br>`src/wetdry.F:414` `VEL=sqrt((g*H1/FRIC(NM123))*(DELETA/DELDIST))`<br>해석: 문서는 v34.XX의 경사면 흐름 재현 범위를 주장한다. 이 주장의 정확도는 코드의 조건문만으로 정하지 않는다. H는 이 적용 한계 주장에 부여한다. 결론: 코드 대조 대상 아님. 경사면 상류 흐름에 한정한 재현 가능성은 Luettich·Westerink(1999)의 적용 한계 주장이다. [10-12 G 정리]
([features 보고서 §5 K01 (565줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: subgrid 침수·노출 수심) 근거: src/wetdry.F:236 `IF(level0)THEN`<br>src/wetdry.F:237 `HTOT = gridDepthVertETA2(i)`<br>src/wetdry.F:241 `IF(HTOT.LE.H0) THEN`<br>src/wetdry.F:242 `IF(level0)THEN`<br>src/wetdry.F:244 `IF(HTOT.LT.HABSMIN)THEN`<br>src/wetdry.F:245 `gridDepthVertETA2(i) = HABSMIN`<br>src/wetdry.F:246 `wetDepthVertETA2(i) = HABSMIN`<br>해석: 기존 침수·노출 문서의 DP+ETA 설명에 subgrid 수심 선택 조건이 없다. 결론: 문서 누락. level0의 침수·노출 판정은 lookup 수심 gridDepthVertETA2를 사용한다.
([features 보고서 §5 K03 (567줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 음의 침수 수위차) 근거: src/wetdry.F:375 `DELETA=ETA2(NM123)-ETA2(NM3)`<br>src/wetdry.F:377 `IF (DELETA.lt.0.d0) DELETA = 0.d0`<br>해석: 인용한 후보 유속 설명은 음의 수위차 처리 조건을 생략한다. 결론: 문서 누락. 침수 후보의 수위차 DELETA가 음수이면 v56.2.1은 이를 0으로 제한한다.
([features 보고서 §5 K04 (568줄)<br>C03 (652줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 시변 수심 침수 분기) 근거: src/wetdry.F:845 `IF ((NDDT.NE.0).AND.(IT.LE.BTIME_END+1) ) THEN`<br>src/wetdry.F:851 `IF(NCTOT.lt.3) THEN   !If not wet from previous time step`<br>src/wetdry.F:852 `NCTOT=NNODECODE(NM1)+NNODECODE(NM2)+NNODECODE(NM3)`<br>src/wetdry.F:853 `if(NCTOT.lt.3) then !if not alreay made wet for this time step`<br>src/wetdry.F:863 `IF( (HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF).AND.`<br>src/wetdry.F:864 `&                   (HTOTN3.GE.HOFF) ) THEN`<br>해석: 보고서에 보존한 노트 설명은 변경 후 수심 검사만 적고 분기 진입 조건을 생략했다. 결론: 문서 누락. 시변 수심의 추가 침수 검사는 NDDT가 0이 아니고 IT가 BTIME_END+1 이하일 때 적용된다. 단위 불일치의 별도 E 후보는 바로 아래 `WETDRY-BTIME-UNITS`에 기록한다. [10-12 결론 검증 보완]

<a id="wetdry-btime-units"></a>

E(코드 결함 후보) `WETDRY-BTIME-UNITS`: `src/wetdry.F:172`는 `integer, intent(in) :: it ! time step number`로 IT를 선언한다. `src/wetdry.F:845`는 `IF ((NDDT.NE.0).AND.(IT.LE.BTIME_END+1) ) THEN`으로 진입한다. 반면 `src/hstart.F:1244–1246`은 `bTIME1 = STATIM*86400.D0`, `bTIME2 = bTIME1 + bTIMINC`, `BTIME_END = BTIME1 + BCHGTIMINC`로 종료 시각을 초 단위로 구성한다. 수심 갱신은 `src/timestep.F:494`의 `IF(timeloc.LT.BTIME_END) THEN`을 사용한다. `src/wetdry.F:841–843`의 주석은 수심 변화 기간에만 이 추가 침수 검사를 수행한다고 설명한다. 단계 번호와 초 단위 종료 시각을 직접 비교하는 것은 이 의도 및 다른 갱신 경로와 모순된다. 반대 근거 검색에서 cstart·hstart·timestep의 BTIME_END 대입은 모두 시각 구성 또는 갱신이다 (`src/cstart.F:130`; `src/hstart.F:1246,1262,1296,1326,1346,1380`; `src/timestep.F:473,524`). BTIME_END를 시간 단계 번호로 변환하거나 wetdry의 IT를 초로 변환하는 경로는 찾지 못했다. 같은 timestep의 `.LT.` 변경 주석과 `.EQ.` 종료 처리는 시각 비교이며 이 단위 불일치를 보정하지 않는다 (`src/timestep.F:494,505,545,557`). 영향 범위는 NOLIFA=2에서 NDDT가 0이 아닌 추가 침수 검사이다 (`src/wetdry.F:204–206,845`). IT와 초 시각의 수치 대응이 달라지면 검사 기간도 달라질 수 있다. 근거 강도는 강함이다. 실제 격자의 침수 결과는 실행하지 않았다. 기존 K04·C03의 C는 분기 조건의 문서 누락에 대한 판정으로 유지한다. [10-12 결론 검증 보완]
([features 보고서 §5 K05 (569줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 장벽 수취 절점의 침수) 근거: src/wetdry.F:1087 `IF((NIBCNT(I).GT.0).AND.(NNODECODE(I).EQ.0)) THEN`<br>src/wetdry.F:1088 `NNODECODE(I)=1`<br>해석: 인용한 일반 침수 규칙은 내부 장벽 수취 상태를 반영하는 NIBCNT 조건을 적지 않았다. 결론: 문서 누락. NIBCNT가 양수인 건조 절점은 최종 침수·노출 처리 중 습윤 절점으로 전환된다.
([features 보고서 §5 C02 (651줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 보통 W1의 수위차 절점 선택) 근거: 보통 W1의 두 wet 노드 조건은 일치한다. src/wetdry.F:370 `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`<br>src/wetdry.F:371 `NM123=NM1`<br>src/wetdry.F:372 `IF(ETA2(NM2).GT.ETA2(NM1)) NM123=NM2`<br>src/wetdry.F:375 `DELETA=ETA2(NM123)-ETA2(NM3)`<br>해석: 두 절점 조건 자체는 맞다. 보고서가 인용한 설명은 그 뒤 최대 수위 절점 선택을 생략했다. 결론: 문서 누락. 보통 W1은 두 습윤 절점의 HOFF 조건을 확인한 뒤 수위가 높은 절점으로 수위차를 계산한다.
([features 보고서 §5 C05 (654줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: DELETA의 원문 위치) 근거: 인용 위치 오기. src/wetdry.F:375 `DELETA=ETA2(NM123)-ETA2(NM3)`<br>src/wetdry.F:377 `IF (DELETA.lt.0.d0) DELETA = 0.d0`<br>해석: 보고서가 보존한 1242–1289줄 인용은 해당 조건 위치가 아니다. 같은 판의 실제 조건문 위치로 인용을 고쳐야 한다. 결론: 문서 오기. 음의 DELETA를 0으로 만드는 근거는 wetdry.F:377의 조건문이다.
([features 보고서 §5 C07 (656줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 재침수의 보편 조건) 근거: 보통 W1을 모든 침수 경로로 일반화했다. src/wetdry.F:1087 `IF((NIBCNT(I).GT.0).AND.(NNODECODE(I).EQ.0)) THEN`<br>src/wetdry.F:1088 `NNODECODE(I)=1`<br>src/wetdry.F:845 `IF ((NDDT.NE.0).AND.(IT.LE.BTIME_END+1) ) THEN`<br>src/wetdry.F:863 `IF( (HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF).AND.`<br>src/wetdry.F:864 `&                   (HTOTN3.GE.HOFF) ) THEN`<br>해석: 보고서가 보존한 at least 2 문장은 모든 침수 경로의 필수조건으로 서술했다. NIBCNT 강제 전환과 시변 수심 분기가 그 일반화를 반박한다. 결론: 문서 오기. 두 습윤 이웃 조건은 보통 W1에 적용하며 장벽 수취와 시변 수심의 별도 침수 경로에는 일반화하지 않는다.

## F. Edge effects (front handling)

- `NODEDRYMIN·NODEWETMIN`은 `NOLIFA.EQ.2`일 때 fort.15에서 읽는다 (`[file=src/read_input.F line=3021]` `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`; `src/read_input.F:3020` `IF(NOLIFA.EQ.2) THEN`). [10-12 전수 검증 보완] 로그에는 두 입력값의 지속 시간 안내가 있다 (`[file=src/read_input.F line=3025]` `&          /,5X,'AND NODEREP > NODEWETMIN = ',I6,' TIME STEPS',`; `[file=src/read_input.F line=3032]` `&          /,5X,'AND NODEREP > NODEDRYMIN = ',I6,' TIME STEPS',/)`). 활성 침수·노출 전환에서 두 입력값을 사용하는 줄은 검색되지 않았다. 현행 문서도 값을 무시한다고 명시한다 (`docs/technical_reference/parameter_definitions/index.rst:698`). 상세 근거는 아래 W10·W19·W23·K07 판정을 정본으로 사용한다. 실제 최소 지속시간의 실행 비교는 하지 않았다. [10-12 결론 검증 정정]
- Wet/dry front via `MJU` (active attached elements) at `[file=src/wetdry.F line=1361-1377, 1387-1390]`:
  - Landlocked wet nodes are dried
  - `MJU` forced to ≥ 1 to keep momentum solve numerically safe
- Mass/flux coupling at fronts: `NCELE = NC1*NC2*NC3*NOFF(IE)` at `[file=src/wetdry.F line=1373]`, `[file=src/gwce.F line=477]`, `[file=src/momentum.F line=312]`
- Spurious oscillation guards:
  - Anti-flooding `NOFF` logic at `[file=src/wetdry.F line=1103-1162]`
  - Single-node connectivity suppression at `[file=src/wetdry.F line=1209-1230]`
  - 코드는 `IF (DELETA.lt.0.d0) DELETA = 0.d0`으로 음의 `DELETA`를 0으로 둔다 (`[file=src/wetdry.F line=375]` `DELETA=ETA2(NM123)-ETA2(NM3)`; `[file=src/wetdry.F line=377]` `IF (DELETA.lt.0.d0) DELETA = 0.d0`).
  - Slope-limited gravity (`ALPHAL`) in GWCE at `[file=src/gwce.F line=515-516]`


([features 보고서 §5 W10 (125·704줄)<br>W19 (134·705줄)<br>W23 (138·706줄)<br>K07 (571줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 최소 습윤·건조 대기 단계) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich03.pdf/p001-018.md` PDF 10쪽 / 인쇄 8쪽: `nodes are not allowed to wet for a specified number of time steps (typically 10 - 20) after they have dried.`<br>src/wetdry.F:440 `IF(VEL.GT.VELMIN) THEN`<br>src/read_input.F:3032 `&          /,5X,'AND NODEREP > NODEDRYMIN = ',I6,' TIME STEPS',/)`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 7쪽 / 인쇄 6쪽: `NODEREP < NODEWETMIN` (LaTeX 전사)<br>src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>src/read_input.F:3025 `&          /,5X,'AND NODEREP > NODEWETMIN = ',I6,' TIME STEPS',`<br>src/wetdry.F:241 `IF(HTOT.LE.H0) THEN`<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 8쪽 / 인쇄 7쪽: `NODEREP < NODEDRYMIN` (LaTeX 전사)<br>src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>src/read_input.F:3032 `&          /,5X,'AND NODEREP > NODEDRYMIN = ',I6,' TIME STEPS',/)`<br>src/wetdry.F:440 `IF(VEL.GT.VELMIN) THEN`<br>docs/technical_reference/parameter_definitions/index.rst:698 `In the past, the wetting and drying algorithm required two additional integers as input. These extra parameters are no longer needed by the code, but they are still present to maintain backward compatibility. Their values will be ignored.`<br>해석: 1995년 및 v34.XX 문서는 NODEREP를 사용한 이력 제어를 적는다. src·prep·wind·util에서 NODEDRYMIN·NODEWETMIN·NODEREP를 검색한 결과는 선언·입력·로그·제어정보 재기록이다. `src/control.F:927–930`은 fort.15 값을 다시 기록한다. `src/xdmfio.F:907–912`는 같은 값을 XDMF Information으로 기록한다. 이 저장 경로를 침수·노출 전환 조건으로 세지 않는다. 결론: 판 차이. v56.2.1은 NODEDRYMIN과 NODEWETMIN을 읽지만 활성 상태 전환에는 사용하지 않는다. [10-12 결론 검증 보완]
([features 보고서 §5 W13 (128줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 절점 곱 이외의 요소 마스크) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 7쪽 / 인쇄 6쪽: `An element is wet if the product of the NODECODE values for each node in the element is 1 and dry if the product is 0.`<br>src/wetdry.F:1373 `NCEle=NC1*NC2*NC3*NOFF(IE)`<br>src/wetdry.F:101 `! jgf52.08.08: Enable analyst to remove NOFF from wetting and`<br>해석: v34.XX 원문은 절점 곱만 적는다. 후속 판 주석은 NOFF를 이전 방식과 구별한다. 결론: 판 차이. v56.2.1은 세 절점 상태의 곱에 NOFF를 곱해 요소 기여도를 정한다.
([features 보고서 §5 W26 (141줄)<br>K06 (570줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 장벽 수신 이후의 요소 비활성화) 근거: `_staging/recovery/read/ADCIRC/manuals/pdfs/1999_Luettich01.pdf/p001-009.md` PDF 8쪽 / 인쇄 7쪽: `There is no override for this case.`<br>src/wetdry.F:1114 `NBNCTOT=NIBCNT(NM1)*NIBCNT(NM2)*NIBCNT(NM3)`<br>src/wetdry.F:1115 `IF(NBNCTOT.EQ.0) THEN   !No barrier/pipe receiving nodes in this elem`<br>src/wetdry.F:1373 `NCEle=NC1*NC2*NC3*NOFF(IE)`<br>src/wetdry.F:1114 `NBNCTOT=NIBCNT(NM1)*NIBCNT(NM2)*NIBCNT(NM3)`<br>src/wetdry.F:1115 `IF(NBNCTOT.EQ.0) THEN   !No barrier/pipe receiving nodes in this elem`<br>해석: v34.XX 문서의 no override는 현재의 절점 습윤과 요소 활성 상태 구분을 설명하지 않는다. 결론: 판 차이. v56.2.1은 장벽 수신 절점의 강제 습윤 뒤에도 요소 NOFF를 별도로 판정한다.
([features 보고서 §5 C04 (653줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: NODEDRYMIN·NODEWETMIN 조정 효과) 근거: 현행 source 전체에서 NODEDRYMIN·NODEWETMIN은 입력과 로그 근거를 찾았다. src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>src/read_input.F:3022 `WRITE(16,17) H0,NODEWETMIN,VELMIN,NODEDRYMIN`<br>src/read_input.F:3025 `&          /,5X,'AND NODEREP > NODEWETMIN = ',I6,' TIME STEPS',`<br>src/read_input.F:3032 `&          /,5X,'AND NODEREP > NODEDRYMIN = ',I6,' TIME STEPS',/)`<br>src/read_input.F:3021 `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`<br>src/read_input.F:3022 `WRITE(16,17) H0,NODEWETMIN,VELMIN,NODEDRYMIN`<br>src/read_input.F:3025 `&          /,5X,'AND NODEREP > NODEWETMIN = ',I6,' TIME STEPS',`<br>src/read_input.F:3032 `&          /,5X,'AND NODEREP > NODEDRYMIN = ',I6,' TIME STEPS',/)`<br>docs/technical_reference/parameter_definitions/index.rst:698 `In the past, the wetting and drying algorithm required two additional integers as input. These extra parameters are no longer needed by the code, but they are still present to maintain backward compatibility. Their values will be ignored.`<br>해석: src·prep·wind·util에서 NODEDRYMIN·NODEWETMIN·NODEREP를 검색했다. 입력·로그·전처리 전달 이외의 활성 판정에서 사용하지 않는다. 현재 모델의 tuning 효과를 안내한 보고서 속 노트 문장은 코드와 모순된다. 과거 규칙과의 판 차이는 W10·W19·W23에서 분류했다. 결론: 문서 오기. v56.2.1은 NODEDRYMIN·NODEWETMIN을 읽지만 활성 침수·노출 전환에 사용하지 않는다.

## G. Friction interaction

- Friction terms (`TK0/TK/TK2`) computed at all nodes without explicit `NODECODE` IF guard at `[file=src/gwce.F line=2477-2482]`
- But friction effect is switched off on dry nodes via momentum's `NCI=NODECODE` multiplication at `[file=src/momentum.F line=714, 751-753, 783-786]`
- During wetting checks, `FRIC` is recomputed (Manning→Cd conversion + lower bound) at `[file=src/wetdry.F line=397-408, 543-553, 690-700]`


([features 보고서 §5 W06 (121줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: 혼합 마찰식의 Manning형 매개변수) 근거: [10-12 결론 정정] W06: 문서의 조건부 매개변수 관계는 W05의 활성 IFHYBF 식에 그대로 대입할 수 있다. 별도 LoadManningsN 분기와의 차이를 구현 부재로 읽지 않는다. 5절은 혼합식에 한정하여 F로 분류한다.<br>`_staging/recovery/read/ADCIRC/manuals/pdfs/1995_Luettich01.pdf/p001-018.md` PDF 7–8쪽 / 인쇄 5–6쪽: `We note that if C_{f\min}\equiv gn^2/H_o^\gamma and \gamma=1/3, where g is the gravitational constant and n is the Manning coefficient, Eq. (1) will provide a Manning equation type frictional behavior for H<H_o, Figure 1.` (본문 기호 LaTeX 전사)<br>조건식: `C_{f\min}\equiv gn^2/H_o^\gamma,\quad\gamma=1/3,\quad H<H_o`<br>src/wetdry.F:388 `IF (LoadManningsN) THEN`<br>src/wetdry.F:402 `FRIC(NM123)=g*ManningsN(NM123)**2.d0`<br>src/wetdry.F:403 `&                         /( ( DP(NM123)+IFNLFA*ETA2(NM123) )`<br>src/wetdry.F:404 `&                                                  **(1.d0/3.d0) )`<br>src/wetdry.F:416 `TKWET = MAX(FRIC(NM123)*(IFLINBF+(VELMIN/H1)*`<br>src/wetdry.F:418 `&                                  (1.D0+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA))),`<br>src/wetdry.F:416 `TKWET = MAX(FRIC(NM123)*(IFLINBF+(VELMIN/H1)*`<br>src/wetdry.F:417 `&                                  (IFNLBF+IFHYBF*`<br>src/wetdry.F:418 `&                                  (1.D0+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA))),`<br>해석: W05의 활성 IFHYBF 식에 C_fmin=gn²/H_o^(1/3), γ=1/3을 대입하면 C_f=gn²/H^(1/3)×[1+(H/H_o)^θ]^(1/(3θ))이다. H/H_o가 작아지면 마지막 인수는 1에 접근한다. 이는 직접 LoadManningsN 분기와의 동일성 주장이 아니다. 결론: 표기 차이. 혼합 마찰식은 문서의 매개변수를 대입하면 Manning형 천해 거동을 갖는다.

## Decision Guide — H0 selection (수심 하한별)

| Bathymetry minimum | Recommended H0 | Why |
|-------------------|----------------|-----|
| ~5m (수심 하한 강제 시) | H0=0.5 → 1.0 (or any) | Wet/dry never fires |
| ~0.5-1m (자연 천해) | 표준 `H0` 기본값 확인하지 않음 | `H0`는 fort.15에서 읽는다 (`[file=src/read_input.F line=3021]` `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`). 확인하지 않음: 현재 판의 `H0=0.05–0.1` 표준 기본값 근거. `[source-needed]` |
| 음수 가능 (조간대) | `NODEDRYMIN·NODEWETMIN`은 활성 전환에서 미사용 | 두 입력값은 `NOLIFA.EQ.2`일 때 fort.15에서 읽는다 (`[file=src/read_input.F line=3021]` `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`; `src/read_input.F:3020` `IF(NOLIFA.EQ.2) THEN`). [10-12 전수 검증 보완] 현행 문서의 무시 규약과 [Edge effects 절](#f-edge-effects-front-handling)의 W10·W19·W23·K07 판정을 따른다 (`docs/technical_reference/parameter_definitions/index.rst:698`). [10-12 결론 검증 정정] |

수심 하한(5m clamp)을 제거한 메시:
- **Set `H0=0.1`** in fort.15
- Verify `HOFF=0.12` (auto from `1.2*H0`)
- 다수의 천해 노드가 정상적으로 wet/dry에 참여
- `H0`는 노출 문턱이다 (`[file=src/wetdry.F line=241]` `IF(HTOT.LE.H0) THEN`). `HOFF=1.2*H0`는 보통 W1의 침수 문턱이다 (`[file=src/wetdry.F line=127]` `hoff=1.2d0*h0`; `[file=src/wetdry.F line=370]` `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`). 확인하지 않음: `H0=0.1`을 쓰지 않은 모든 천해 노드가 영구 노출 상태가 된다는 일반화.

## Working Rules

1. **`HABSMIN = 0.8*H0`, `HOFF = 1.2*H0`** are hard-coded ratios. To tighten/loosen wet/dry, change `H0` itself.
2. **`NCELE` masking is multiplicative** — once `NODECODE=0`, that node's contribution to all matrix terms is zero (no special branch).
3. 보통 W1은 `HOFF` 이상인 두 wet 이웃을 요구한다 (`[file=src/wetdry.F line=370]` `IF((HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF)) THEN`). 장벽 수취 노드와 연결된 `NIBCNT>0` 노드는 별도로 wet으로 강제한다 (`[file=src/wetdry.F line=1087]` `IF((NIBCNT(I).GT.0).AND.(NNODECODE(I).EQ.0)) THEN`; `[file=src/wetdry.F line=1088]` `NNODECODE(I)=1`). 지형 변화의 추가 침수 경로도 있다 (`[file=src/wetdry.F line=845]` `IF ((NDDT.NE.0).AND.(IT.LE.BTIME_END+1) ) THEN`; `[file=src/wetdry.F line=863]` `IF( (HTOTN1.GE.HOFF).AND.(HTOTN2.GE.HOFF).AND.`; `[file=src/wetdry.F line=864]` `&                   (HTOTN3.GE.HOFF) ) THEN`).
4. `VELMIN`은 `NOLIFA.EQ.2`일 때 fort.15에서 읽는다 (`[file=src/read_input.F line=3021]` `READ(15,*) H0,NODEDRYMIN,NODEWETMIN,VELMIN`; `src/read_input.F:3020` `IF(NOLIFA.EQ.2) THEN`). [10-12 전수 검증 보완] 확인하지 않음: 현재 판의 `VELMIN=0.001 m/s` 표준 기본값 근거. `[source-needed]`
5. **Friction recomputed during wetting checks** — Manning conversion happens twice (assembly + wet check) — slight inefficiency but correct.

## Common Pitfalls

- **`NOLIFA=1` thinking it has wet/dry** → no, only `NOLIFA=2` activates `computeWettingAndDrying`.
- **H0=5.0 with naturally-shallow bathymetry** → all shallow nodes always dry; tide can't propagate.
- **VELMIN=0.5 m/s** (way too high) → re-wetting never triggers; intertidal flats stuck dry.
- **Hot restart with different H0** → wet/dry state from old H0 frozen; mass artifacts.

## References

- `src/wetdry.F` — full wet/dry algorithm.
- `src/adcirc.F` — `IFNLFA` setup.
- `src/gwce.F` — `NCELE` masking in matrix assembly.
- `src/momentum.F` — `NCI` zeroing of dry-node momentum.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 35+ file:line citations |
| Coverage | NOLIFA dispatch, H0/HABSMIN/HOFF, NODECODE transitions, VELMIN, recovery, friction interaction |
| Review status | `review_required: true` |
