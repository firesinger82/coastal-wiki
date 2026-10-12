---
file: models/SWAN/raw/manuals/website/settings/booij99.swn
lines: 7
sha256: e11c64fb630a2442b5cf0787216d8e0b5de52f3bcd35fce6b1c3bfb79f6c70c6
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# booij99.swn — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | 설정의 출처 — 주석은 Booij 등의 1999년 문헌이 초기 SWAN 버전 중 하나에서 도입한 설정이라고 적는다(1). 원문: `$ settings introduced by Booij et al (1999) in one of the earliest SWAN versions` (1). |
| 2–6 | 물리 설정 명령 — GEN3 KOM과 DRAG WU를 지정한다(2). WCAP KOMEN의 CDS2·POWST·DELTA·POWK를 명시한다(3). BREAK CON의 위치 인수와 FRICT JONSWAP의 CFJON을 제시한다(4–5). TRIADS는 ITRIAD·TRFAC·CUTFR·URCRIT·URSLIM을 명시한다(6). 설정값을 기본값으로 단정하지 않고 원문 그대로 옮긴다. 이 파일에는 단위 설명이 없다. 원문: `GEN3 KOM DRAG WU` (2); `WCAP KOMEN CDS2 2.36E-05 POWST 2. DELTA 0. POWK 1.` (3); `BREAK CON 1. 0.73` (4); `FRICT JONSWAP CFJON 0.067` (5); `TRIADS ITRIAD 11 TRFAC 0.1 CUTFR 2.5 URCRIT 0.2 URSLIM 0.01` (6). |
| 7–7 | 수치 설정 명령 — NUM ACCUR의 위치 인수와 STAT MXITST·ALFA를 제시한다(7). 원문의 정수·소수·지수 표기를 그대로 옮긴다. 원문: `NUM ACCUR 0.02 0.02 0.02 98. STAT MXITST 15 ALFA 0.` (7). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
