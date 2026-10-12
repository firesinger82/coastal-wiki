---
file: models/SWAN/raw/manuals/website/settings/fort.26.v41.10
lines: 7
sha256: 5f9487b2034bb2f0a67ac258d55957782a9d0388dd5950847ff4eb1028c4bcbc
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# fort.26.v41.10 — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | 적용 조건 — 주석은 버전 41.10 이후의 긴밀 결합(tightly coupled) SWAN+ADCIRC 설정이라고 적고 관련 웹페이지를 연결한다(1). 원문: `$ settings for tightly coupled SWAN+ADCIRC since version 41.10 (see https://ccht.ccee.ncsu.edu/swanadcirc/)` (1). |
| 2–6 | 물리·전파 설정 명령 — GEN3 KOMEN, DRAG WU, AGROW를 함께 지정한다(2). WCAP KOMEN은 이름 없는 위치 인수 다섯 개를 제시한다(3). BREAKING은 추가 인수를 적지 않는다(4). FRICTION MADSEN의 KN과 PROP BSBT를 지정한다(5–6). 수치 표기를 그대로 옮긴다. 이 파일에는 위치 인수의 이름·단위나 KN의 단위 설명이 없다. 원문: `GEN3 KOMEN DRAG WU AGROW` (2); `WCAP KOMEN 2.36E-5 3.02E-3 2.0 1.0 1.0` (3); `BREAKING` (4); `FRICTION MADSEN KN=0.05` (5); `PROP BSBT` (6). |
| 7–7 | 수치 설정 명령 — NUM STOPC의 DABS·DREL·CURVAT·NPNTS와 NONSTAT MXITNS를 이름과 함께 제시한다(7). 등호와 설정값을 그대로 옮긴다. 원문: `NUM STOPC DABS=0.005 DREL=0.01 CURVAT=0.005 NPNTS=95 NONSTAT MXITNS=20` (7). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
