---
file: models/ADCIRC/raw/manuals/wiki/markdown/YYYY_MM_DD_HH24_StormNumber_BLAdj.md
lines: 35
sha256: c2971d1b96752fa7dd06b0a96a3422cb505d6af09e321092dd820c855fba1d64
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# YYYY_MM_DD_HH24_StormNumber_BLAdj.md — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | YYYY MM DD HH24 StormNumber BLAdj — 제목과 판본 표기를 포함한다(1–3). 아래 입력 항목 묶음이 `fort.15 file`의 매개변수형 와류 기상 강제력(parametric vortex meteorological forcing) 유형에 연결된다고 설명한다(5). 적용 조건과 항목 순서는 원문 그대로 옮긴다. 원문: `` `YYYY MM DD HH24 StormNumber BLAdj` is an input in the [fort.15 file](/Fort.15_file) associated with the parametric vortex meteorological forcing input type (`[NWS](/NWS)` = 8).  `` (5). |
| 7–35 | Parameter Summary — `Entry`와 `Description` 머리글 아래에서 초기 시작(cold-start) 날짜·시각의 연, 월, 일과 24시간 시각을 설명한다(9–27). 예보 앙상블(forecast ensemble)의 폭풍 번호와 경계층 보정계수(boundary layer adjustment factor)를 설명한다(29–35). 폭풍 번호의 통상 설정과 보정계수의 합리적 범위, 풍속 사이의 관계를 원문 그대로 옮긴다. 원문: `YYYY` (13); `4 integer year of the cold-start datetime` (15); `MM` (17); `2 integer month of the cold-start datetime` (19); `DD` (21); `2 integer day of the cold-start datetime` (23); `HH24` (25); `2 integer 24-hour time of the cold-start datetime` (27); `StormNumber` (29); `Storm number of forecast ensemble. Usually just set equal to 1.` (31); `BLAdj` (33); `Boundary layer adjustment factor between wind speed at 10-m and the wind speed at the top of the atmospheric boundary layer (winds at top of atm. b.l.) = (winds at 10-m)/BLAdj. A reasonable range is 0.7 to 0.9.` (35). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
