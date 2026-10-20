---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/sharc-intel-cpu
lines: 3
sha256: ee0af2aafd568f273deeac37255f26286f3617fa251bbbd0bf26644b439f991c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sharc-intel-cpu — 판독 구간 기록

구간은 1행부터 3행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–3 | 옵션 원문은 `CXXFLAGS := -std=c++14 -Wall -O3 -parallel -qopenmp -static -qopt-report=2 -qopt-report-phase=vec -xhost -ipo -I$(HOME)/include -D_NUMERIC_MODE=1 -D_NETCDF=0 -D_ONLY_RECT=0` (1), `LDFLAGS := -w -O3 -parallel -qopenmp -static-intel -lnuma -L$(HOME)/lib` (2)이다. 3행은 빈 줄이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
