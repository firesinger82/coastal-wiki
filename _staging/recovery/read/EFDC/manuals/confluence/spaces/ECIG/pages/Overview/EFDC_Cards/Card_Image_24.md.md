---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_24.md
lines: 72
sha256: 2643e1613f0e877a8951484337fd6a866aa85652557140c65a1c30c4057fb6d1
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_24.md — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C24 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 체적 공급원·흡수원(volume source/sink)의 위치·크기·농도 시계열(concentration series) 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C24 VOLUMETRIC SOURCE/SINK LOCATIONS, MAGNITUDES, AND CONCENTRATION SERIES ` (10). |
| 14–29 | 위치·유량·승수 — 셀 인덱스(cell index)와 일정 유입·유출률(constant inflow/outflow rate)의 단위를 정의한다(14–18). 상수 및 시계열 공급원·흡수원에 곱하는 값은 정상 유입·유출, U면·V면·두 면의 측방 유입·유출(lateral inflow/outflow)에 따라 다르다(20–28). 원문: ` \* IQS: I CELL INDEX OF VOLUME SOURCE/SINK ` (14); ` \* JQS: J CELL INDEX OF VOLUME SOURCE/SINK ` (16); ` \* QSSE: CONSTANT INFLOW/OUTFLOW RATE IN M\*m\*m/s ` (18); ` \* NQSMUL: MULTIPLIER SWITCH FOR CONSTANT AND TIME SERIES VOL S/S ` (20); ` \*                 = 0 MULT BY 1. FOR NORMAL IN/OUTFLOW (L\*L\*L/T) ` (22); ` \*                 = 1 MULT BY DY FOR LATERAL IN/OUTFLOW (L\*L/T) ON U FACE ` (24); ` \*                 = 2 MULT BY DX FOR LATERAL IN/OUTFLOW (L\*L/T) ON V FACE ` (26); ` \*                 = 3 MULT BY DX+DY FOR LATERAL IN/OUTFLOW (L\*L/T) ON U&V FACES ` (28). |
| 30–39 | 운동량 플럭스(momentum flux) — NQSMFF가 0이 아닐 때 체적 공급원·흡수원의 운동량 플럭스를 고려한다고 적는다(30). 네 옵션은 음·양의 U면과 V면을 구분한다(32–38). 원문: ` \* NQSMFF: IF NON ZERO ACCOUNT FOR VOL S/S MOMENTUM FLUX ` (30); ` \*                = 1 MOMENTUM FLUX ON NEG U FACE ` (32); ` \*                = 2 MOMENTUM FLUX ON NEG V FACE ` (34); ` \*                = 3 MOMENTUM FLUX ON POS U FACE ` (36); ` \*                = 4 MOMENTUM FLUX ON POS V FACE ` (38). |
| 40–59 | 시계열 연결 — 체적 유량과 염분(salinity)·온도(temperature)·염료(dye)·패류 유생(shellfish larvae)·독성 오염물질(toxic contaminants)·점착성 퇴적물(cohesive sediment)·비점착성 퇴적물(non-cohesive sediment)의 시계열 식별자를 정의한다(40–54). 셀에 할당하는 시계열 유량 비율을 설명한다(56). 원문: ` \* IQSERQ: ID NUMBER OF ASSOCIATED VOLUMN FLOW TIME SERIES ` (40); ` \* ICSER1: ID NUMBER OF ASSOCIATED SALINITY TIME SERIES ` (42); ` \* ICSER2: ID NUMBER OF ASSOCIATED TEMPERATURE TIME SERIES ` (44); ` \* ICSER3: ID NUMBER OF ASSOCIATED DYE CONC TIME SERIES ` (46); ` \* ICSER4: ID NUMBER OF ASSOCIATED SHELL FISH LARVAE RELEASE TIME SERIES ` (48); ` \* ICSER5: ID NUMBER OF ASSOCIATED TOXIC CONTAMINANT CONC TIME SERIES ` (50); ` \* ICSER6: ID NUMBER OF ASSOCIATED COHESIVE SEDIMENT CONC TIME SERIES ` (52); ` \* ICSER7: ID NUMBER OF ASSOCIATED NON-COHESIVE SED CONC TIME SERIES ` (54); ` \* QSFACTOR: FRACTION OF TIME SERIES FLOW NQSERQ ASSIGNED TO THIS CELL ` (56). |
| 60–72 | C24 입력 예시 — Markdown의 빈 표 머리글과 구분선(60–61), 열 이름(62), 지점 주석과 입력 값이 붙은 모든 자료 행(63–72)을 제시한다. 각 행의 수치와 지점명을 그대로 옮긴다. 원문: ` \| C24 \| IQS \| JQS \| QSSE \| NQSMUL \| NQSMFF \| IQSERQ \| ICSER1 \| ICSER2 \| ICSER3 \| ICSER4 \| ICSER5 \| ICSER6 \| ICSER7 \| QSFACTOR \| ! ID \| ` (62); ` \|  \| 50 \| 79 \| 0.00E+00 \| 0 \| 0 \| 3 \| 0 \| 3 \| 0 \| 0 \| 0 \| 0 \| 0 \| 5.00E-01 \| ! Sammamish River \| ` (63); ` \|  \| 50 \| 80 \| 0.00E+00 \| 0 \| 0 \| 3 \| 0 \| 3 \| 0 \| 0 \| 0 \| 0 \| 0 \| 5.00E-01 \| ! Sammamish River \| ` (64); ` \|  \| 43 \| 76 \| 0.00E+00 \| 0 \| 0 \| 4 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 1.00E+00 \| ! KingCo34a \| ` (65); ` \|  \| 43 \| 75 \| 0.00E+00 \| 0 \| 0 \| 5 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 1.00E+00 \| ! KingCo35C \| ` (66); ` \|  \| 64 \| 23 \| 0.00E+00 \| 0 \| 0 \| 7 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 1.00E+00 \| ! 12120000 \| ` (67); ` \|  \| 54 \| 7 \| 0.00E+00 \| 0 \| 0 \| 2 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 1.00E+00 \| ! KingCo37A \| ` (68); ` \|  \| 45 \| 3 \| 0.00E+00 \| 0 \| 0 \| 1 \| 0 \| 2 \| 0 \| 0 \| 0 \| 0 \| 0 \| 3.33E-01 \| ! Cedar River \| ` (69); ` \|  \| 46 \| 3 \| 0.00E+00 \| 0 \| 0 \| 1 \| 0 \| 2 \| 0 \| 0 \| 0 \| 0 \| 0 \| 3.33E-01 \| ! Cedar River \| ` (70); ` \|  \| 44 \| 3 \| 0.00E+00 \| 0 \| 0 \| 1 \| 0 \| 2 \| 0 \| 0 \| 0 \| 0 \| 0 \| 3.33E-01 \| ! Cedar River \| ` (71); ` \|  \| 3 \| 42 \| 0.00E+00 \| 0 \| 0 \| 6 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 0 \| 9.80E-01 \| ! Clock \| ` (72). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 40·56·62행: 연결 체적 유량 시계열 식별자는 설명과 입력 표에서 `IQSERQ`라고 적는다(40·62). `QSFACTOR` 설명은 시계열 유량 이름을 `NQSERQ`라고 적는다(56).
