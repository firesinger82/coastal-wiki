---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-22__SEDZLJ_Input_Files_ENSIGHT.md
lines: 90
sha256: 7aa92fa7658b6d781c5a236249c53911bc225d982f97492aaf78e16446e96ff4
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-22__SEDZLJ_Input_Files_ENSIGHT.md — 판독 구간 기록

구간은 1행부터 90행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–29 | ENSIGHT.SDF 출력 제어와 퇴적물 변수 — Ensight 출력 파일의 변수별 켜짐·꺼짐 값과 유속(velocity), 활성층 전단응력, 평균 입경(averaged particle size), 소류사 농도(bedload concentration), 부유 퇴적물 농도(suspended sediment concentration) 필드를 제시한다(14–28). 제목, 주석과 빈 줄도 포함한다. 원문: `**Data Format B-22  SEDZLJ Input Files: ENSIGHT.SDF**` (10); `#` (12); `C Input file for Ensight output` (14); `C values of 1 turns on the variable and 0 turns off the variable` (16); `C          1   U  - X velocity` (18); `C          2   V  - Y velocity` (20); `C          3  TAU - Shear Stress on active layer` (22); `C          4  D50 - Averaged particle size` (24); `C          5  CBL - Bedload concentration` (26); `C          6  SED - Suspended sediment concentration` (28). |
| 30–79 | ENSIGHT.SDF 수질과 열 변수 — 조류(algae), 유기 탄소·인·질소(organic carbon/phosphorus/nitrogen), 인산염(phosphate), 암모니아성 질소(ammonia nitrogen), 질산염 질소(nitrate nitrogen), 실리카(silica), 산소 요구량(oxygen demand), 용존산소(dissolved oxygen), 금속(metal), 분변성 대장균(fecal coliform bacteria), 이산화탄소(carbon dioxide), 대형조류(macroalgae), 열 함량(heat content), 온도(temperature)의 필드 이름과 원문 설명을 각 줄 그대로 적는다(30–78). 원문: `C       7  CHC - cyanobacteria` (30); `C       8  CHG - diatom algae` (32); `C       9  CHD - green algae` (34); `C       10  ROC - refractory particulate organic carbon` (36); `C       11  LOC - labile particulate organic carbon` (38); `C       12  DOC - dissolved organic carbon` (40); `C       13  ROP - refractory particulate organic phosphorus` (42); `C       14  LOP - labile particulate organic phosphorus` (44); `C       15  DOP - dissolved organic phosphorus` (46); `C       16  P4D - total phosphate` (48); `C       17  RON - refractory particulate organic nitrogen` (50); `C       18  LON - labile particulate organic nitrogen` (52); `C       19  DON - dissolved organic nitrogen` (54); `C       20  NHX - ammonia nitrogen` (56); `C       21  NOX - nitrate nitrogen` (58); `C       22  SUU - particulate biogenic silica` (60); `C       23  SAA - dissolved available silica` (62); `C       24  COD - chemical oxygen demand` (64); `C       25  DOX - dissolved oxygen` (66); `C       26  TAM - total active metal` (68); `C       27  FCB - fecal coliform bacteria` (70); `C       28  CO2 - Dissolved Carbon Dioxide` (72); `C       29  MAC - macroalgae` (74); `C       30  HEAT- Heat Content` (76); `C          31  TEMP- Temperature (K)` (78). |
| 80–90 | ENSIGHT.SDF 열 순서와 예시 — 세 주석 줄에 열 이름을 적고 세 데이터 줄에 출력 스위치 값을 적는다(80–90). 원문: `C  U     V   TAU  D50  CBL  SED` (80); `C  CHC  CHD  CHG  ROC  LOC  DOC  ROP  LOP  DOP  P4D  RON   LON  DON` (82); `C  NHX  NOX  SUU  SAA  COD  DOX  TAM  FCB  CO2  MAC  HEAT  TEMP` (84); `   1     1    1    1    1    1` (86); `   0     0    0    0    0    0    0    0    0    0    0     0    0` (88); `   0     0    0    0    0    0    0    0    0    0    0     0` (90). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 32–34·82: 변수 목록은 `CHG - diatom algae` 다음에 `CHD - green algae`를 적지만 열 이름 줄은 `CHC CHD CHG` 순서이다.
