---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cmake/Modules/FindNUMA.cmake
lines: 29
sha256: 62386233995361abf882fbbbcb3585ee31da3deb69a25e7cc628a64472fbfb82
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# FindNUMA.cmake — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–7 | 비균일 메모리 접근(non-uniform memory access, NUMA) 라이브러리 검색 모듈의 주석이다. 원문 주석은 `# - Find NUMA` (1), `# Find the NUMA library and includes` (2), `#` (3), `# NUMA_INCLUDE_DIRS - where to find numa.h, etc.` (4), `# NUMA_LIBRARIES - List of libraries when using NUMA.` (5), `# NUMA_FOUND - True if NUMA found.` (6)이다. 7행은 빈 줄이다. |
| 8–22 | 검색 명령은 `find_path(NUMA_INCLUDE_DIRS` (8), `NAMES numa.h numaif.h` (9), `HINTS ${NUMA_ROOT_DIR}/include)` (10)와 `find_library(NUMA_LIBRARIES` (12), `NAMES numa` (13), `HINTS ${NUMA_ROOT_DIR}/lib)` (14)이다. `include(FindPackageHandleStandardArgs)` (16), `find_package_handle_standard_args(NUMA DEFAULT_MSG NUMA_LIBRARIES NUMA_INCLUDE_DIRS)` (17)로 결과를 판정한다. `mark_as_advanced(` (19)에 `NUMA_LIBRARIES` (20), `NUMA_INCLUDE_DIRS)` (21)를 넘긴다. 빈 줄도 포함한다. |
| 23–29 | `if(NUMA_FOUND AND NOT (TARGET NUMA::NUMA))` (23)에서 `add_library (NUMA::NUMA UNKNOWN IMPORTED)` (24)로 가져온 대상(imported target)을 만든다. `set_target_properties(NUMA::NUMA` (25), `PROPERTIES` (26), `IMPORTED_LOCATION ${NUMA_LIBRARIES}` (27), `INTERFACE_INCLUDE_DIRECTORIES ${NUMA_INCLUDE_DIRS})` (28)로 위치와 인터페이스 포함 경로를 지정한다. `endif()` (29)로 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–14: 비표준 검색 위치의 힌트는 `NUMA_ROOT_DIR`를 사용한다. 이 파일에는 `NUMA_ROOT` 참조가 없다.
