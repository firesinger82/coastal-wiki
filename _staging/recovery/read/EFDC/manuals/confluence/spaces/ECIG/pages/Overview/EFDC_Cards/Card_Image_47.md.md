---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_47.md
lines: 38
sha256: 2ac8145c862938bab8e38c8c281061ed67b75ff949143514da76ec625b1dc283
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_47.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 32473089(2), 제목 Card Image 47(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-12T07:21:28.504Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–20 | C47 경계 위치 — 남쪽 농도 경계 조건(concentration boundary conditions)의 위치를 다룬다(10). I·J 셀 첨자(cell index)와 유출(outflow)에서 유입(inflow)으로 바뀔 때 지정값을 회복하는 시간 단계 개수를 정의한다(14–20). 이름·적용 조건 원문: `\* ICBS: I CELL INDEX` (14); `\* JCBS: J CELL INDEX` (16); `\* NTSCRS: NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE` (18); `\* TO INFLOW FROM OUTFLOW` (20). |
| 21–34 | 남쪽 경계의 시계열 식별자 — 염분(salinity), 온도(temperature), 염료 농도(dye concentration), 패류 유생(shellfish larvae), 독성 오염물질(toxic contaminant), 점착성 퇴적물(cohesive sediment), 비점착성 퇴적물(non-cohesive sediment)의 시계열(time series) 번호를 각각 정의한다(22–34). 원문: `\* NSSERS: SOUTH BOUNDARY CELL SALINITY TIME SERIES ID NUMBER` (22); `\* NTSERS: SOUTH BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER` (24); `\* NDSERS: SOUTH BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER` (26); `\* NSFSERS: SOUTH BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER` (28); `\* NTXSERS: SOUTH BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.` (30); `\* NSDSERS: SOUTH BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER` (32); `\* NSNSERS: SOUTH BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER` (34). |
| 35–38 | C47 입력 형식 — 빈 줄·주석 표시와 열 이름 줄을 포함한다(35–38). 수치 데이터 행과 기본값은 이 파일에 없다. 열 이름 원문: `C47 IBBS JBBS NTSCRS NSSERS NTSERS NDSERS NSFSERS NTXSERS NSDSERS NSNSERS` (38). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·16·38: 본문 셀 첨자 이름은 `ICBS`와 `JCBS`이다(14·16). 입력 열 이름은 `IBBS`와 `JBBS`이다(38). 두 표기의 대응 설명은 이 파일에 없다.

