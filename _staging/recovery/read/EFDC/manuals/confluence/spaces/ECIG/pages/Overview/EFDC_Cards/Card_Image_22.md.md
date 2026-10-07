---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_22.md
lines: 47
sha256: e9dc6be1f75515fae7b91b328ca843b3967bc5c2724892768885771e58fee8d8
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_22.md — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | C22 — 원문 frontmatter의 페이지 정보와 분류 경로를 읽었다(1–9). 퇴적물(sediment)·독성 오염물질(toxic contaminants) 수와 농도 시계열(concentration time series) 수를 지정하는 제목을 제시한다(10). 빈 줄과 주석 표식도 포함한다(11–13). 원문: ` C22 SPECIFY NUM OF SEDIMENT AND TOXICS AND NUM OF CONCENTRATION TIME SERIES ` (10). |
| 14–19 | 물질 수 — 독성 오염물질, 점착성 퇴적물(cohesive sediment) 입경 등급(size class), 비점착성 퇴적물(non-cohesive sediment) 입경 등급의 수를 설명한다. 세 항목은 각각 기본값 1을 명시한다(14·16·18). 원문: ` \* NTOX: NUMBER OF TOXIC CONTAMINANTS (DEFAULT = 1) ` (14); ` \* NSED: NUMBER OF COHESIVE SEDIMENT SIZE CLASSES (DEFAULT = 1) ` (16); ` \* NSND: NUMBER OF NON-COHESIVE SEDIMENT SIZE CLASSES (DEFAULT = 1) ` (18). |
| 20–43 | 시계열 수와 퇴적물 질량 수지(sediment mass balance) — 염분(salinity), 온도(temperature), 염료(dye), 패류 유생(shellfish larvae), 독성 오염물질, 점착성 및 비점착성 퇴적물 농도 시계열의 수를 정의한다(20–38). 각 독성·퇴적물 시계열에 해당 물질 수만큼 자료가 있어야 한다는 의무를 적는다(30·34·38). 질량 수지 활성화 값도 제시한다(40). 원문: ` \* NCSER1: NUMBER OF SALINITY TIME SERIES ` (20); ` \* NCSER2: NUMBER OF TEMPERATURE TIME SERIES ` (22); ` \* NCSER3: NUMBER OF DYE CONCENTRATION TIME SERIES ` (24); ` \* NCSER4: NUMBER OF SHELLFISH LARVAE CONCENTRATION TIME SERIES ` (26); ` \* NCSER5: NUMBER OF TOXIC CONTAMINANT CONCENTRATION TIME SERIES ` (28); ` \* EACH TIME SERIES MUST HAVE DATA FOR NTOX TOXICICANTS ` (30); ` \* NCSER6: NUMBER OF COHESIVE SEDIMENT CONCENTRATION TIME SERIES ` (32); ` \* EACH TIME SERIES MUST HAVE DATA FOR NSED COHESIVE SEDIMENTS ` (34); ` \* NCSER7: NUMBER OF NON-COHESIVE SEDIMENT CONCENTRATION TIME SERIES ` (36); ` \* EACH TIME SERIES MUST HAVE DATA FOR NSND NON-COHESIVE SEDIMENTS ` (38); ` \* ISSBAL: SET TO 1 FOR SEDIENT MASS BALANCE ` (40). |
| 44–47 | C22 입력 예시 — Markdown의 빈 표 머리글과 구분선(44–45), 열 이름(46), 입력 값(47)을 제시한다. 예시 값과 14–18행의 기본값을 구분한다. 원문: ` \| C22 \| NTOX \| NSED \| NSND \| NCSER1 \| NCSER2 \| NCSER3 \| NCSER4 \| NCSER5 \| NCSER6 \| NCSER7 \| ISSBAL \| ` (46); ` \|  \| 3 \| 1 \| 2 \| 0 \| 1 \| 1 \| 0 \| 1 \| 1 \| 1 \| 1 \| ` (47). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
