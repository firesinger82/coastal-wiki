---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_16.md
lines: 43
sha256: cee85cf35e0ae801b5df0bbe4ad5f22cf84fb433d385f8f348914d3c8dafd035
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Card_Image_16.md — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터(metadata) — 페이지 ID(2), 제목(3), space(4), 원문 URL(5), 버전(6), 갱신 시각(7), 문서 계층 경로(8)를 기록한다. `---` 구분자를 포함한다(1·9). |
| 10–29 | C16 SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITION PARAMETERS / 경계 셀 수 — 수면 높이(surface elevation) 또는 압력(pressure) 경계 조건(boundary condition)의 매개변수 제목을 적는다(10). 남·서·동·북 개방 경계(open boundaries)의 경계 셀 수를 NPBS·NPBW·NPBE·NPBN으로 설명한다(14–28). 방향을 유지했다. 매개변수 원문: `\* NPBS: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS` (14); `\* CELLS ON SOUTH OPEN BOUNDARIES` (16); `\* NPBW: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS` (18); `\* CELLS ON WEST OPEN BOUNDARIES` (20); `\* NPBE: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS` (22); `\* CELLS ON EAST OPEN BOUNDARIES` (24); `\* NPBN: NUMBER OF SURFACE ELEVATION OR PRESSURE BOUNDARY CONDITIONS` (26); `\* CELLS ON NORTH OPEN BOUNDARIES` (28). 주석용 `\*` 줄과 빈 줄을 포함한다. |
| 30–39 | C16 / 강제력·전역 수위 조정 — 조화 강제력(harmonic forcings) 수, 상수·선형·이차 변화의 0·1·2 강제력 형식, 시계열 강제력(time series forcings) 수와 전체 수면 높이에 더하는 상수 조정을 설명한다(30–36). 매개변수·옵션 원문: `\* NPFOR: NUMBER OF HARMONIC FORCINGS` (30); `\* NPFORT: FORCING TYPE, 0=CONSTANT, 1=LINEAR, 2= QUADRATIC VARIATION` (32); `\* NPSER: NUMBER OF TIME SERIES FORCINGS` (34); `\* PDGINIT: ADD THIS CONSTANT ADJUSTMENT GLOBALLY TO THE SURFACE ELEVATION` (36). 주석용 `\*` 줄과 빈 줄을 포함한다(37–39). |
| 40–43 | C16 / 입력 예시 표 — 빈 표 첫 행, 구분 행, 여덟 매개변수 헤더와 입력 예시를 포함한다(40–43). 예시를 기본값으로 표시하지 않았다. 입력 표 원문: `\| C16 \| NPBS \| NPBW \| NPBE \| NPBN \| NPFOR \| NPFORT \| NPSER \| PDGINIT \|` (42); `\|  \| 0 \| 0 \| 34 \| 0 \| 1 \| 0 \| 0 \| 0 \|` (43). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음

