---
file: models/SWAN/raw/manuals/website/settings/tud2.swn
lines: 9
sha256: 28a9dde6f5fcea606c81f81e88213838575e8fba5c5a23dfbe295489aa9947be
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# tud2.swn — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | 도입 버전 — 주석은 버전 41.45에서 도입한 설정이라고 적는다(1). 원문: `$ settings introduced in version 41.45` (1). |
| 2–6 | 물리 설정 명령 — GEN3 WESTH와 DRAG WU를 지정한다(2). WCAP AB의 CDS2·BR과 BREAK CON, FRICT JONSWAP의 CFJON을 제시한다(3–5). TRIADS DCTA의 TRFAC·P와 BIPHASE ELD를 제시한다(6). 임계 Ursell 수(critical Ursell number)를 0.63으로 설정한다는 Doering·Bowen의 1995년 문헌 주석도 그대로 옮긴다(6). 이 파일에는 단위나 별도의 기본값 표가 없다. 원문: `GEN3 WESTH DRAG WU` (2); `WCAP AB CDS2 5.0E-05 BR 0.00175` (3); `BREAK CON 1. 0.73` (4); `FRICT JONSWAP CFJON 0.038` (5); `TRIADS DCTA TRFAC 4.4 P 1.3333333 BIPHASE ELD 0.63 ! note: critical Ursell number set to 0.63 (Doering and Bowen, 1995)` (6). |
| 7–9 | 수치 설정 권고 — 구분용 `$` 주석을 포함한다(7). 계산을 적절히 종료하기 위해 아래 수치 설정을 사용하라고 권고한다(8). STOPC의 위치 인수와 STAT MXITST·ALFA를 그대로 옮긴다(9). 원문: `$` (7); `$ to terminate the SWAN computation properly, using the numerical settings below is recommended` (8); `NUM STOPC 0.005 0.01 0.005 99.5 STAT MXITST 50 ALFA 0.` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
