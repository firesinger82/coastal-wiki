---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-16__ISTAT.md
lines: 21
sha256: 99e3bcbb0230127d22fd17db860f52bf093d1302c2d136a8c001bf0b5e18b6e0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-16__ISTAT.md — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–15 | ISTAT.INP 적용 조건과 필드 — 얼음 덮임(ice cover)에 따른 켜짐·꺼짐 상태의 시계열(time series)을 정의한다(11–12). 첫 데이터 줄의 필드, 단일 계열 조건, 이후 데이터 줄의 반복 범위와 상태 값은 다음 원문과 같다(13–15). 원문: `**Data Format B-16  ISTAT.INP for ISICE = 2**   ` (10); `C \*\* ISTAT FILE  ` (11); `C \*\* TIME SERIES ON THE STATUS OF ICE ON/OFF VIA ICE COVER  ` (12); `C \*\* FIRST DATA LINE: MISER(N),TCISER(N),TAISER(N),N=1(only one)  ` (13); `C \*\* NEXT DATA LINES: TISER(M,N),RICECOVS(M,N), M=1:MISER  ` (14); `C \*\* TISER: TIME, RICECOVS = 1: ON/0:OFF  ` (15). |
| 16–21 | ISTAT.INP 예시 — 첫 데이터 줄과 이어지는 다섯 시각의 상태 값을 제시한다(16–21). 원문: `5     86400     0  ` (16); `0.000     0.0000  ` (17); `240.000 1.0000  ` (18); `242.000 0.0000  ` (19); `243.000 1.0000  ` (20); `300.000 0.0000` (21). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 13–15: `TCISER(N)`과 `TAISER(N)`은 첫 데이터 줄의 필드로 나오지만 이 파일에는 뜻과 단위가 없다. `TISER`의 시간 단위도 이 파일에는 없다.
