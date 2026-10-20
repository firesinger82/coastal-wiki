---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/config/bluecrystal3-intel
lines: 15
sha256: d71b0acef1fd69e33c3b47c3a93fa895629aa50609cfe0e33f121a8a3342c2c7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# bluecrystal3-intel — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–9 | 다음은 모두 주석이며 실행 설정이 아니다. `# Compiling on Bristol Bluecrystal Phase 3 server with intel compiler (with netcdf)` (1), `# module load languages/intel-compiler-16-u2` (2), `# module load tools/cmake-3.17.5` (3), `` # export CXX=`which icpc` `` (4), `` # export CC=`which icc` `` (5), `# cmake -S . -B build -D_CONFIG=config/bluepebble-intel-netcdf` (6), `# cmake --build build` (7), `#` (8), `# CMAKE config:` (9)이다. |
| 10–15 | 실제 CMake 설정은 `set(_NETCDF 1)` (10), `add_compile_definitions(_NUMERIC_MODE=1)` (11), `add_compile_definitions(_ONLY_RECT=1)` (12), `set(CMAKE_CXX_FLAGS "-Wall -qopt-report=2 -qopt-report-phase=vec -xhost -ipo -parallel")` (13), `set(NetCDF_LIBRARY "/cm/shared/libraries/intel_builds/netcdf-4.7.0-intel-16.par/lib/libnetcdf.so")` (14), `set(NetCDF_INCLUDE_DIR "/cm/shared/libraries/intel_builds/netcdf-4.7.0-intel-16.par/include")` (15)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1·6·14–15: 주석은 `Bluecrystal Phase 3`를 적지만 주석의 CMake 예시는 `config/bluepebble-intel-netcdf`를 지정한다. 실제 NetCDF 경로는 `/cm/shared/libraries/intel_builds/netcdf-4.7.0-intel-16.par` 아래로 고정되어 있다.
