---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/sharc-gcc-cpu
lines: 4
sha256: eafcbe75c867c64dd8e6cfa7d8a6693892ca5b1356d874511eed9ee7b302b748
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sharc-gcc-cpu — 판독 구간 기록

구간은 1행부터 4행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–4 | 옵션 원문은 `CXXFLAGS := -std=c++14 -Wall -O3 -fopenmp -static -I$(HOME)/include -D_NUMERIC_MODE=1 -D_NETCDF=0` (1), `LDFLAGS := -O3 -L$(HOME)/lib` (2), `LDLIBS := -lgomp -lnuma` (3)이다. 4행은 빈 줄이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
