---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_37.md
lines: 75
sha256: 6cbaca543b6747c9feb9691ae3d626cb2f98585813904c5f2b4182532bef7c84
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_37.md — 판독 구간 기록

구간은 1행부터 75행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C37 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 하상 역학 특성(bed mechanical properties) 매개변수 집합 1 제목을 제시한다(10). NSED>0이면 ISTRAN(6)=0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C37 BED MECHANICAL PROPERTIES PARAMETER SET 1 ` (10); ` \* DATA REQUIRED IF NSED>0, EVEN IF ISTRAN(6) = 0 ` (12). |
| 16–39 | 시간과 압밀(consolidation) — 하상 상호작용 시간 간격은 초, 하상·수주(water column) 상호작용 시작 시각은 일 단위다(16–18). 일정 하상 특성, 일정·가변 계수의 단순 압밀, 가변 계수의 복잡한 압밀, 셀별 압밀 옵션을 제시한다(20–38). IBMECH>0의 설정 효과와 요구 파일, 셀별 지도 파일을 원문대로 옮긴다(30–38). 원문: ` \* SEDSTEP: SEDIMENT BED INTERACTION TIME STEP (SECONDS) ` (16); ` \*SETSTART: START TIME FOR BED/WATER COLUMN INTERACTION (DAYS) ` (18); ` \* IBMECH: 0 TIME INVARIANT CONSTANT BED MECHANICAL PROPERITES (UNIFORM BED ONLY) ` (20); ` \*                1 SIMPLE CONSOLIDATION CALCULATION WITH CONSTANT COEFFICIENTS ` (22); ` \*                2 SIMPLE CONSOLIDATION WITH VARIABLE COEFFICIENTS DETERMINED ` (24); ` \*                   EFDC FUNCTIONS CSEDCON1,2,3(IBMECH) ` (26); ` \*                3 COMPLEX CONSOLIDATION WITH VARIABLE COEFFICIENTS DETERMINED ` (28); ` \*                   EFDC FUNCTIONS CSEDCON1,2,3(IBMECH). IBMECH > 0 SETS THE ` (30); ` \*                   C38 PARAMETER ISEDBINT=1 AND REQUIRES INITIAL CONDITIONS ` (32); ` \*                   FILES BEDLAY.INP, BEDBDN.INP AND BEDDDN.IN ` (34); ` \*               9 TYPE OF CONSOLIDATION VARIES BY CELL WITH IBMECH FOR EACH ` (36); ` \*                   DEFINED IN INPUT FILE CONSOLMAP.INP ` (38). |
| 40–53 | 하상 형태와 공극률 — 일정 하상 형태(bed morphology)의 적용 조건과 물의 연행·배출(entrainment/expulsion) 효과를 제외하거나 포함하는 활성 옵션을 구분한다(40–44). 새 층을 추가하는 최상층 두께 조건과 최하부 두 층 결합 조건을 적는다(46–48). 일정 공극률(porosity)의 적용 조건과 퇴적되는 비점착성 퇴적물(non-cohesive sediment)에도 사용하는 설명을 제시한다(50–52). 원문: ` \* IMORPH: 0 CONSTANT BED MORPHOLOGY (IBMECH=0, ONLY) ` (40); ` \*                1 ACTIVE BED MORPHOLOGY: NO WATER ENTRAIN/EXPULSION EFFECTS ` (42); ` \*                2 ACTIVE BED MORPHOLOGY: WITH WATER ENTRAIN/EXPULSION EFFECTS ` (44); ` \* HBEDMAX: TOP BED LAYER THICKNESS (m) AT WHICH NEW LAYER IS ADDED OR IF ` (46); ` \*                    KBT(I,J)=KB, NEW LAYER ADDED AND LOWEST TWO LAYERS COMBINED ` (48); ` \* BEDPORC: CONSTANT BED POROSITY (IBMECH=0, OR NSED=0) ` (50); ` \*                    ALSO USED AS POROSITY OF DEPOSITIN NON-COHESIVE SEDIMENT ` (52). |
| 54–71 | 유동성 이토와 간극비(void ratio) — 유동성 이토(fluid mud)의 최대·최소 점착성 퇴적물(cohesive sediment) 농도 및 단위를 정의한다(54–56). 퇴적되는 물질의 간극비, 최소 하상 간극비, 압밀률 상수(consolidation rate constant)와 계산식을 제시한다(58–62). 상수의 양·영·음 값에 따른 압밀 대상을 구분하며 영 값 설명의 부등식을 그대로 옮긴다(64–68). 원문: ` \* SEDMDMX: MAXIMUM FLUID MUD COHESIVE SEDIMENT CONCENTRATION (MG/L) ` (54); ` \* SEDMDMN: MINIMUM FLUID MUD COHESIVE SEDIMENT CONCENTRATION (MG/L) ` (56); ` \* SEDVDRD: VOID RATIO OF DEPOSITING COHESIVE SEDIMENT ` (58); ` \* SEDVDRM: MINIMUM COHESIVE SEDIMENT BED VOID RATIO (IBMECH > 0) ` (60); ` \* SEDVDRT: BED CONSOLIDATION RATE CONSTANT (sec) (IBMECH = 1,2), EXP(-DELT/SEDVDRT) ` (62); ` \*                  > 0 CONSOLIDATE OVER TIME TO SEDVDRM ` (64); ` \*                  = 0 CONSOLIDATE INSTANTANEOUSLY TO SEDVDRM (0.0>=SEDVDRT<=0.0001) ` (66); ` \*                  < 0 CONSOLIDATE TO INITIAL VOID RATIOS ` (68). |
| 72–75 | C37 입력 예시 — Markdown의 빈 표 머리글과 구분선(72–73), 열 이름(74), 입력 값(75)을 제시한다. 원문: ` \| C37 \| SEDSTEP \| SEDSTART \| IBMECH \| IMORPH \| HBEDMAX \| BEDPORC \| SEDMDMX \| SEDMDMN \| SEDVDRD \| SEDVDRM \| SEDVRDT \| ` (74); ` \|  \| 5 \| 220 \| 1 \| 1 \| 2 \| 0.4 \| 50000 \| 10000 \| 0.666667 \| 0.5 \| -1 \| ` (75). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18·74행: 시작 시각 설명의 이름은 `SETSTART`다(18). 입력 열 이름은 `SEDSTART`다(74).
- 62·74행: 압밀률 상수 설명의 이름은 `SEDVDRT`다(62). 입력 열 이름은 `SEDVRDT`다(74).
- 66행: 이 줄은 `= 0 CONSOLIDATE INSTANTANEOUSLY`와 `(0.0>=SEDVDRT<=0.0001)`을 함께 적는다. 부등식의 두 비교 연산자는 각각 `>=`와 `<=`다.
- 48·62행: 층 추가 조건의 `KBT`와 압밀 계산식의 `DELT`는 이 파일에 기호 정의가 없다.
- 32행: 원문은 `C38 PARAMETER ISEDBINT=1`이라고 적는다. 이번에 직접 읽은 `Card_Image_38.md`의 16–34·40행에는 `ISEDBINT`가 없다. 이번에 직접 읽은 `Card_Image_36.md`의 28–34·94행에는 `ISEDBINT`가 있다.
