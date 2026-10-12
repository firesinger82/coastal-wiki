---
file: models/SWAN/raw/manuals/website/settings/fort.26.v41.31
lines: 7
sha256: 7822986945afe4efedf844d9319dd3c30ee392d1bac5fbeab74fe3162d5e2379
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# fort.26.v41.31 — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–1 | 적용 조건 — 주석은 버전 41.31 이후의 긴밀 결합(tightly coupled) SWAN+ADCIRC 설정이라고 적고 관련 웹페이지를 연결한다(1). 원문: `$ settings for tightly coupled SWAN+ADCIRC since version 41.31 (see https://ccht.ccee.ncsu.edu/swanadcirc/)` (1). |
| 2–6 | 물리·전파 설정 명령 — GEN3 ST6의 위치 인수와 UP·HWANG·VECTAU·U10PROXY·AGROW 구문을 제시한다(2). SSWELL ARDHUIN의 위치 인수를 제시한다(3). BREAKING은 추가 인수를 적지 않는다(4). FRICTION MADSEN의 KN과 PROP BSBT를 지정한다(5–6). 이름 없는 위치 인수에 임의의 이름이나 단위를 붙이지 않고 원문 그대로 옮긴다. 이 파일에는 별도의 단위 설명이 없다. 원문: `GEN3 ST6 4.70E-7 6.6E-6 4 4 UP HWANG VECTAU U10PROXY 28 AGROW` (2); `SSWELL ARDHUIN 1.2` (3); `BREAKING` (4); `FRICTION MADSEN KN=0.05` (5); `PROP BSBT` (6). |
| 7–7 | 수치 설정 명령 — NUM STOPC의 DABS·DREL·CURVAT·NPNTS와 NONSTAT MXITNS를 이름과 함께 제시한다(7). 등호와 설정값을 그대로 옮긴다. 원문: `NUM STOPC DABS=0.005 DREL=0.01 CURVAT=0.005 NPNTS=95 NONSTAT MXITNS=20` (7). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

없음
