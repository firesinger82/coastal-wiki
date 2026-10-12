---
file: models/SWAN/raw/manuals/website/settings/tud.swn
lines: 9
sha256: 3bba0589a835f98158606b2ae3c67059c3fcd364cce659b80b187e82b67b831b
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# tud.swn — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | 도입 버전 — 주석은 버전 41.01에서 도입한 설정이라고 적는다(1). 원문: `$ settings introduced in version 41.01` (1). |
| 2–6 | 물리 설정 명령 — GEN3 KOM과 DRAG FIT를 지정한다(2). WCAP KOMEN의 DELTA 설정과 Rogers 등의 2003년 문헌에 따른다는 주석을 함께 옮긴다(3). BREAK CON과 FRICT JONSWAP의 설정값을 제시한다(4–5). TRIADS의 ITRIAD·TRFAC·CUTFR·DINT·URCRIT·URSLIM과 CCA를 사용한다는 Salmon 등의 2016년 문헌 주석을 제시한다(6). 이 파일은 단위나 별도의 기본값 표를 제시하지 않는다. 원문: `GEN3 KOM DRAG FIT` (2); `WCAP KOMEN CDS2 2.36E-05 POWST 2. DELTA 1. POWK 1. ! note: delta is set to 1 according to Rogers et al. (2003)` (3); `BREAK CON 1. 0.73` (4); `FRICT JONSWAP CFJON 0.038` (5); `TRIADS ITRIAD 1 TRFAC 0.8 CUTFR 2.5 DINT 360. URCRIT 0.2 URSLIM 0.01 ! note: CCA is employed (Salmon et al., 2016)` (6). |
| 7–9 | 수치 설정 권고 — 구분용 `$` 주석을 포함한다(7). 계산을 적절히 종료하기 위해 아래 수치 설정을 사용하라고 권고한다(8). STOPC의 위치 인수와 STAT MXITST·ALFA를 그대로 옮긴다(9). 원문: `$` (7); `$ to terminate the SWAN computation properly, using the numerical settings below is recommended` (8); `NUM STOPC 0.005 0.01 0.005 99.5 STAT MXITST 50 ALFA 0.` (9). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
