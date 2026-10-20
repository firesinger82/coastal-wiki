---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/bluepebble-intel-netcdf
lines: 16
sha256: b61f8301b18e3188b899e64251c92fdee612e5a684bd66e3587038e650a7d1b2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# bluepebble-intel-netcdf — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–10 | 다음은 모두 주석이다. `# Compiling on Bristol Bluepebble server with intel compiler (with netcdf)` (1), `# module load lang/gcc/9.1.0` (2), `# module load tools/cmake/3.14.2` (3), `# module load lang/intel-parallel-studio-xe/2020` (4), `` # export CXX=`which icpc` `` (5), `` # export CC=`which icc` `` (6), `# cmake -S . -B build -D_CONFIG=config/bluepebble-intel-netcdf` (7), `# cmake --build build` (8), `#` (9), `# CMAKE config:` (10)이다. |
| 11–16 | 실제 설정은 `set(_NETCDF 1)` (11), `add_compile_definitions(_NUMERIC_MODE=1)` (12), `add_compile_definitions(_ONLY_RECT=1)` (13), `set(CMAKE_CXX_FLAGS "-Wall -qopt-report=2 -qopt-report-phase=vec -xhost -ipo")` (14), `set(NetCDF_LIBRARY "/sw/lib/netcdf-c-4.7.0/lib/libnetcdf.so")` (15), `set(NetCDF_INCLUDE_DIR "/sw/lib/netcdf-c-4.7.0/include")` (16)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–16: NetCDF 라이브러리와 포함 경로는 `/sw/lib/netcdf-c-4.7.0` 아래로 고정되어 있다.
