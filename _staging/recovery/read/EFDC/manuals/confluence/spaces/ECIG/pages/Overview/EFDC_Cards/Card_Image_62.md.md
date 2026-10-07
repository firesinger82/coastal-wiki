---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_62.md
lines: 38
sha256: 8fc9fd0afc462ecf474e77f832384716720fbb99ff7455d0c47e1eda2c54d95d
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_62.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 108199941(2), 제목 Card Image 62(3), space ECIG(4), 원문 URL(5), 버전 2(6), 수정 시각 2018-04-04T04:43:13.067Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–20 | C62 경계 위치 — 북쪽 농도 경계 조건(concentration boundary conditions)의 위치를 다룬다(10). I·J 셀 첨자(cell index)와 유출(outflow)에서 유입(inflow)으로 바뀔 때 지정값을 회복하는 시간 단계 개수를 정의한다(14–20). 이름·적용 조건 원문: `\* ICBN:          I CELL INDEX` (14); `\* JCBN:         J CELL INDEX` (16); `\* NTSCRN:   NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE` (18); `\*                   TO INFLOW FROM OUTFLOW` (20). |
| 21–34 | 북쪽 경계의 시계열 식별자 — 염분(salinity), 온도(temperature), 염료 농도(dye concentration), 패류 유생(shellfish larvae), 독성 오염물질(toxic contaminant), 점착성 퇴적물(cohesive sediment), 비점착성 퇴적물(non-cohesive sediment)의 시계열(time series) 번호를 각각 정의한다(22–34). 원문: `\* NSSERN:   NORTH BOUNDARY CELL SALINITY TIME SERIES ID NUMBER` (22); `\* NTSERN:   NORTH BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER` (24); `\* NDSERN:   NORTH BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER` (26); `\* NSFSERN: NORTH BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER` (28); `\* NTXSERN: NORTH BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.` (30); `\* NSDSERN: NORTH BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER` (32); `\* NSNSERN: NORTH BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER` (34). |
| 35–38 | C62 입력 형식 — 빈 줄·주석 표시와 열 이름 줄을 포함한다(35–38). 수치 데이터 행과 기본값은 이 파일에 없다. 열 이름 원문: `C62 IBBN JBBN NTSCRN NSSERN NTSERN NDSERN NSFSERN NTXSERN NSDSERN NSNSERN` (38). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·16·38: 본문 셀 첨자 이름은 `ICBN`와 `JCBN`이다(14·16). 입력 열 이름은 `IBBN`와 `JBBN`이다(38). 두 표기의 대응 설명은 이 파일에 없다.

