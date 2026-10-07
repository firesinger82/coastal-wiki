---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_52.md
lines: 38
sha256: 5ef48380f55d1be7609cfb2fcfc5abbb0b453d5bf49212c19785ed540fe9066e
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_52.md — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(frontmatter) — 페이지 ID 33751053(2), 제목 Card Image 52(3), space ECIG(4), 원문 URL(5), 버전 1(6), 수정 시각 2018-01-16T02:28:51.208Z(7), 문서 경로(8)와 구분선(1·9)을 포함한다. |
| 10–20 | C52 경계 위치 — 서쪽 농도 경계 조건(concentration boundary conditions)의 위치를 다룬다(10). I·J 셀 첨자(cell index)와 유출(outflow)에서 유입(inflow)으로 바뀔 때 지정값을 회복하는 시간 단계 개수를 정의한다(14–20). 이름·적용 조건 원문: `\* ICBW: I CELL INDEX` (14); `\* JCBW: J CELL INDEX` (16); `\* NTSCRW: NUMBER OF TIME STEPS TO RECOVER SPECIFIED VALUES ON CHANGE` (18); `\*                  TO INFLOW FROM OUTFLOW` (20). |
| 21–34 | 서쪽 경계의 시계열 식별자 — 염분(salinity), 온도(temperature), 염료 농도(dye concentration), 패류 유생(shellfish larvae), 독성 오염물질(toxic contaminant), 점착성 퇴적물(cohesive sediment), 비점착성 퇴적물(non-cohesive sediment)의 시계열(time series) 번호를 각각 정의한다(22–34). 원문: `\* NSSERW: WEST BOUNDARY CELL SALINITY TIME SERIES ID NUMBER` (22); `\* NTSERW: WEST BOUNDARY CELL TEMPERATURE TIME SERIES ID NUMBER` (24); `\* NDSERW: WEST BOUNDARY CELL DYE CONC TIME SERIES ID NUMBER` (26); `\* NSFSERW: WEST BOUNDARY CELL SHELLFISH LARVAE TIME SERIES ID NUMBER` (28); `\* NTXSERW: WEST BOUNDARY CELL TOXIC CONTAMINANT CONC TIME SERIES ID NUM.` (30); `\* NSDSERW: WEST BOUNDARY CELL COHESIVE SED CONC TIME SERIES ID NUMBER` (32); `\* NSNSERW: WEST BOUNDARY CELL NON-COHESIVE SED CONC TIME SERIES ID NUMBER` (34). |
| 35–38 | C52 입력 형식 — 빈 줄·주석 표시와 열 이름 줄을 포함한다(35–38). 수치 데이터 행과 기본값은 이 파일에 없다. 열 이름 원문: `C52      IBBW      JBBW        NTSCRW       NSSERW      NTSERW     NDSERW       NSFSERW       NTXSERW      NSDSERW      NSNSERW` (38). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 14·16·38: 본문 셀 첨자 이름은 `ICBW`와 `JCBW`이다(14·16). 입력 열 이름은 `IBBW`와 `JBBW`이다(38). 두 표기의 대응 설명은 이 파일에 없다.

