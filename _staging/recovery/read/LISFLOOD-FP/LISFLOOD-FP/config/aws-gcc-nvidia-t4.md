---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/aws-gcc-nvidia-t4
lines: 8
sha256: 23dde18c0559774473efa9e727525cffca0de9e4d3ebb736334fb8f9263c55cc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# aws-gcc-nvidia-t4 — 판독 구간 기록

구간은 1행부터 8행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–8 | Make 설정은 `CUDA := yes` (1), `NETCDF := yes` (2)이다. 옵션 원문은 `CXXFLAGS := -std=c++14 -Wall -O3 -fopenmp -static -I/usr/local/cuda/include -D_NUMERIC_MODE=1 -D_NETCDF=0 -g` (4), `LDFLAGS := -O3 -L/usr/local/cuda/lib` (5), `LDLIBS := -lgomp -lnuma` (6), `NVCCFLAGS := -rdc=true -gencode=arch=compute_75,code=sm_75 -gencode=arch=compute_75,code=compute_75` (7)이다. 3·8행은 빈 줄이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 2·4·6: `NETCDF := yes`와 컴파일러 옵션 `-D_NETCDF=0`이 함께 있다. `LDLIBS`에는 `-lnetcdf`가 없다.
