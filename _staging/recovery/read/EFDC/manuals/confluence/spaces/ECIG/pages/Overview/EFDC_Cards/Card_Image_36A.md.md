---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36A.md
lines: 67
sha256: 930760380d089f7a01c1326f6a88e3d136c9ff77cdc3aa8c1aa3ec91a9a33b83
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_36A.md — 판독 구간 기록

구간은 1행부터 67행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | C36A — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 퇴적물(sediment) 초기화와 수주(water column)·하상(bed) 표현 옵션 제목을 제시한다(10). ISTRAN(6)과 ISTRAN(7)이 모두 0일 때도 자료가 필요하다고 적는다(12). 빈 줄과 주석 표식도 포함한다(11–15). 원문: ` C36A SEDIMENT INITIALIZATION AND WATER COLUMN/BED REPRESENTATION OPTIONS ` (10); ` \* DATA REQUIRED EVEN IF ISTRAN(6) AND ISTRAN(7) ARE 0 ` (12). |
| 16–33 | 퇴적물 수송 응력(stress) — 유체역학 모델(hydrodynamic model) 응력 사용, 전체 응력에서 입자 응력(grain stress) 분리, 독립 로그 법칙(log law) 조도 높이(roughness height), 점착성·비점착성 가중 조도와 로그·멱 법칙(power law) 저항 옵션을 제시한다(16–32). 외부 파일명과 구현 날짜도 원문대로 옮긴다(24·28·32). 원문: ` \* ISBEDSTR: 0 USE HYDRODYNAMIC MODEL STRESS FOR SEDIMENT TRANSPORT ` (16); ` \*                    1 SEPARATE GRAIN STRESS FROM TOTAL IN COHESIVE AND NON-COHESIVE COMPONENTS ` (18); ` \*                    2 SEPARATE GRAIN STRESS FROM TOTAL APPLY TO COHESIVE AND NON-COHESIVE SEDS ` (20); ` \*                    3 USE INDEPENDENT LOG LAW ROUGHNESS HEIGHT FOR SEDIMENT TRANSPORT ` (22); ` \*                      READ FROM FILE SEDROUGH.INP ` (24); ` \*                   4 SEPARATE GRAIN STRESS FROM TOTAL USING COHESIVE/NON-COHESIVE WEIGHTED ` (26); ` \*                      ROUGHNESS AND LOG LAW RESISTANCE (IMPLEMENTED 5/31/05) ` (28); ` \*                   5 SEPARATE GRAIN STRESS FROM TOTAL USING COHESIVE/NON-COHESIVE WEIGHTED ` (30); ` \*                      ROUGHNESS AND POWER LAW RESISTANCE (IMPLEMENTED 5/31/05) ` (32). |
| 34–45 | 조도 입경과 비균일 유동(non-uniform flow) — 비점착성 조도에 D50, 2*D50, D90, 2*D90을 사용하는 옵션을 구분한다(34–40). 비균일 유동 효과의 입자 응력 분배(grain stress partitioning) 보정 조건과 ISBEDSTR=4·5에서 사용하지 말라는 지시를 적는다(42–44). 원문: ` \* ISBSDIAM: 0 USE D50 DIAMETER FOR NON-COHESIVE ROUGHNESS ` (34); ` \*                   1 USE 2\*D50 FOR NON-COHESIVE ROUGHNESS ` (36); ` \*                   2 USE D90 FOR NON-COHESIVE ROUGHNESS ` (38); ` \*                   3 USE 2\*D90 FOR NON-COHESIVE ROUGHNESS ` (40); ` \* ISBSDFUF: 1 CORRECT GRAIN STRESS PARTITIONING FOR NON-UNIFORM FLOW EFFECTS ` (42); ` \* DO NOT USE FOR ISBEDSTR = 4 AND 5 ` (44). |
| 46–63 | 경계층 계수·점성·제방 침식 — 점착성 하상 위 난류 경계층(turbulent boundary layer)의 매끄러움 계수와 완전 매끄러움·완전 거침 값을 제시한다(46–52). ISBEDSTR=4·5일 때 계수를 사용하지 않는다고 적는다(54). 동점성(kinematic viscosity), 외부 시계열에 따른 제방 침식(bank erosion), 안정성 분석(stability analysis)으로 계산하는 비활성 옵션을 설명한다(56–60). 원문: ` \* COEFTSBL: COEFFICIENT SPECIFYING THE HYDRODYNAMIC SMOOTHNESS OF ` (46); ` \* TURBULENT BOUNDARY LAYER OVER COHESIVE BED IN TERMS OF ` (48); ` \* EQUIVALENT GRAIN SIZE FOR COHESIVE GRAIN STRESS ` (50); ` \* CALCULATION, FULLY SMOOTH = 4, FULLY ROUGH = 100. ` (52); ` \* NOT USED FOR ISBEDSTR = 4 AND 5 ` (54); ` \* VISMUDST: KINEMATIC VISCOSITY TO USE IN DETERMINING COHESIVE GRAIN STRESS ` (56); ` \* ISBKERO: 1 FOR BANK EROSION SPECIFIED BY EXTERNAL TIME SERIES ` (58); ` \*                  2 FOR BANK EROSION INTERNALLY CALCULATED BY STABILITY ANALYSIS (Not Active) ` (60). |
| 64–67 | C36A 입력 예시 — Markdown의 빈 표 머리글과 구분선(64–65), 열 이름(66), 입력 값(67)을 제시한다. 한 셀에 합쳐진 두 이름과 두 값을 분리하거나 고치지 않고 그대로 옮긴다. 원문: ` \| C36A \| ISBEDSTR \| ISBSDIAM \| ISBSDFUF \| COEFTSBL VISMUDST \| ISBKERO \| ` (66); ` \|  \| 1 \| 0 \| 0 \| 4 .000001 \| 0 \| ` (67). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 66–67행: 입력 표의 한 열 이름 셀에는 `COEFTSBL VISMUDST`가 함께 있다(66). 그 열의 값 셀에는 `4 .000001`이 함께 있다(67).
