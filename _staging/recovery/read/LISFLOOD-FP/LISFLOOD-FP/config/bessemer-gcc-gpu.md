---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/bessemer-gcc-gpu
lines: 7
sha256: 27ae871ef53b1c6ce60d66a187d530ca07a0037544e9a885fdd483029e01db53
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# bessemer-gcc-gpu — 판독 구간 기록

구간은 1행부터 7행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–7 | `CUDA := yes` (1)로 CUDA 설정을 적는다. 옵션 원문은 `CXXFLAGS := -std=c++14 -Wall -O3 -fopenmp -static -I$(HOME)/include -D_NUMERIC_MODE=1 -D_NETCDF=1 -g` (3), `LDFLAGS := -O3 -L$(HOME)/lib` (4), `LDLIBS := -lgomp -lnuma -lnetcdf` (5), `NVCCFLAGS := -rdc=true -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_70,code=compute_70` (6)이다. 2·7행은 빈 줄이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
