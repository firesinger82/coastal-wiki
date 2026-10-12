---
file: models/SWAN/raw/manuals/website/settings/basin.swn
lines: 9
sha256: 9a0b013a381e7852e9a3d70ea400f5bbded2268a700d73f67f3d8528d1cacae9
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# basin.swn — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | 적용 대상 — 주석은 하구(estuary), 조석 입구(tidal inlet), 호수(lake)에 적합한 설정이라고 적는다(1). 이 문구는 설정 파일의 설명이다. 원문: `$ settings suitable for estuaries, tidal inlets and lakes` (1). |
| 2–6 | 물리 설정 명령 — GEN3 WESTH의 WU 항력(drag)을 지정한다(2). WCAP AB는 CDS2·BR·CDS3 설정값을 명시하고 흐름에 의한 소산(current-induced dissipation)이 포함된다는 주석을 단다(3). BREAK BKD, FRICT JONSWAP, TRIADS DCTA와 BIPHASE DEWIT를 지정한다(4–6). 수치와 대소문자 및 인라인 주석(inline comment)을 원문 그대로 옮긴다. 이 파일은 단위나 별도의 기본값 표를 제시하지 않는다. 원문: `GEN3 WESTH DRAG WU` (2); `WCAP AB CDS2 5.0E-05 BR 0.00175 CURRENT CDS3 0.8 ! note: current-induced dissipation included` (3); `BREAK BKD` (4); `FRICT JONSWAP CFJON 0.038` (5); `TRIADS DCTA TRFAC 4.4 P 1.3333333 BIPHASE DEWIT` (6). |
| 7–9 | 수치 설정 권고 — 구분용 `$` 주석을 포함한다(7). 계산을 적절히 종료하기 위해 아래 수치 설정을 사용하라고 권고한다(8). STOPC의 위치 인수와 MXITST·ALFA 설정값을 그대로 제시한다(9). 원문: `$` (7); `$ to terminate the SWAN computation properly, using the numerical settings below is recommended` (8); `NUM STOPC 0.005 0.01 0.005 99.5 STAT MXITST 50 ALFA 0.` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
