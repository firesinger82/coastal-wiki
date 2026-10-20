---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/bluepebble-intel
lines: 14
sha256: 18a86b92e180dae8969eb805786347fb21069e997182f662ec3021863b58c51a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# bluepebble-intel — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–10 | 다음은 모두 주석이다. `# Compiling on Bristol Bluepebble server with intel compiler (without netcdf)` (1), `# module load lang/gcc/9.1.0` (2), `# module load tools/cmake/3.14.2` (3), `# module load lang/intel-parallel-studio-xe/2020` (4), `` # export CXX=`which icpc` `` (5), `` # export CC=`which icc` `` (6), `# cmake -S . -B build -D_CONFIG=config/bluepebble-intel` (7), `# cmake --build build` (8), `#` (9), `# CMAKE config:` (10)이다. |
| 11–14 | 실제 설정은 `set(_NETCDF 0)` (11), `add_compile_definitions(_NUMERIC_MODE=1)` (12), `add_compile_definitions(_ONLY_RECT=1)` (13), `set(CMAKE_CXX_FLAGS "-Wall -qopt-report=2 -qopt-report-phase=vec -xhost -ipo -parallel")` (14)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
