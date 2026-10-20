---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/sharc-gcc-gpu
lines: 5
sha256: 4949d14669312e440b3005884b1c4fac3eb22e2a7db24a6dffad7a38ee186749
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sharc-gcc-gpu — 판독 구간 기록

구간은 1행부터 5행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–5 | 옵션 원문은 `CXXFLAGS := -std=c++14 -Wall -O3 -fopenmp -static -I$(HOME)/include -D_NETCDF=1 -D_NUMERIC_MODE=1` (1), `LDFLAGS := -O3 -L$(HOME)/lib` (2), `LDLIBS := -lgomp -lnuma -lnetcdf` (3)이다. `CUDA := yes` (4)와 `NVCCFLAGS := -rdc=true -gencode=arch=compute_37,code=sm_37 -gencode=arch=compute_37,code=compute_37` (5)로 CUDA 설정과 계산 능력을 적는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
