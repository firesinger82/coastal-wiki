---
file: models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Appendices/Appendix_B_-_Data_Formats/Data_Format_B-19__East_West_Connectors.md
lines: 28
sha256: ecdb498950e9e206f94e4ff6fa048acf4d63ca647dbedaa21dafcdeb5b36b32c
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Data_Format_B-19__East_West_Connectors.md — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 메타데이터 — 페이지 식별자, 제목, space, URL, 버전, 갱신 시각과 문서 계층을 기록한다(2–8). |
| 10–18 | MAPPGEW.INP 정의 — 동서 연결(east-west connection)을 수동으로 만드는 파일이다(11–12). 연결 수와 서쪽 면·동쪽 면에서 연결하는 셀의 좌표 필드 및 반복 조건을 정의한다(14–18). 주석 줄도 포함한다(13,17). 원문: `**Data Format B-19  East West Connectors**   ` (10); `C FILE MAPPGEW.INP PROVIDES INFORMATION FOR MAKING MANUAL GRID CONNECTIONS  ` (11); `C IN THE EAST-WEST (I+1 AND I-1) DIRECTION  ` (12); `C NPEWBP = NUMBER OF EAST-WEST CONNECTIONS  ` (14); `C IWPEW,JWPEW = I,J INDICES OF THE CELL CONNECTED AT THE WEST FACE  ` (15); `C IEPEW,JEPEW = I,J INDICES OF THE CORRESPONDING CELL CONNECTED AT THE EAST FACE  ` (16); `C IWPEW JWPEW IEPEW JEPEW (REPEATED NPEWBP TIMES)  ` (18). |
| 19–28 | MAPPGEW.INP 예시 — 연결 수와 해당 연결 데이터 줄을 제시한다(19–28). 원문: `9  ` (19); `55 77 11 19  ` (20); `55 76 11 20  ` (21); `55 75 11 21  ` (22); `55 74 11 22  ` (23); `55 73 11 23  ` (24); `55 72 11 24  ` (25); `55 71 11 25  ` (26); `55 70 11 26  ` (27); `55 69 11 27` (28). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
