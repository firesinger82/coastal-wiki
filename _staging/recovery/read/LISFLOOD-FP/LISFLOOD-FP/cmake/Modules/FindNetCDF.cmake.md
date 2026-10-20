---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cmake/Modules/FindNetCDF.cmake
lines: 96
sha256: 7137869f3e45c4496d47b4863d782884329699386c58a99512e5c46b565341aa
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# FindNetCDF.cmake — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–10 | 블록 주석은 `#[==[` (1)에서 `#]==]` (9)까지이다. `Provides the following variables:` (2) 아래 `` * `NetCDF_FOUND`: Whether NetCDF was found or not. `` (4), `` * `NetCDF_INCLUDE_DIRS`: Include directories necessary to use NetCDF. `` (5), `` * `NetCDF_LIBRARIES`: Libraries necessary to use NetCDF. `` (6), `` * `NetCDF_VERSION`: The version of NetCDF found. `` (7), `` * `NetCDF::NetCDF`: A target to use with `target_link_libraries`. `` (8)를 설명한다. 3·10행은 빈 줄이다. |
| 11–36 | `# Try to find a CMake-built NetCDF.` (11)은 주석이다. `find_package(netCDF CONFIG QUIET)` (12), `if (netCDF_FOUND)` (13)에서 주석 `# Forward the variables in a consistent way.` (14) 다음 `set(NetCDF_FOUND "${netCDF_FOUND}")` (15), `set(NetCDF_INCLUDE_DIRS "${netCDF_INCLUDE_DIR}")` (16), `set(NetCDF_LIBRARIES "${netCDF_LIBRARIES}")` (17), `set(NetCDF_VERSION "${NetCDFVersion}")` (18)로 변수를 전달한다. `if (NOT TARGET NetCDF::NetCDF)` (19)에서 `add_library(NetCDF::NetCDF INTERFACE IMPORTED)` (20)을 호출한다. 그 안의 `if (TARGET "netCDF::netcdf")` (21)는 주석 `# 4.7.3` (22)과 `set_target_properties(NetCDF::NetCDF PROPERTIES` (23), `INTERFACE_LINK_LIBRARIES "netCDF::netcdf")` (24)를 사용한다. `elseif (TARGET "netcdf")` (25)는 `set_target_properties(NetCDF::NetCDF PROPERTIES` (26), `INTERFACE_LINK_LIBRARIES "netcdf")` (27)를 사용한다. `else ()` (28)는 `set_target_properties(NetCDF::NetCDF PROPERTIES` (29), `INTERFACE_LINK_LIBRARIES "${netCDF_LIBRARIES}")` (30)를 사용한다. 내부 분기 종료(31–32) 뒤 주석 `# Skip the rest of the logic in this file.` (33), `return ()` (34)로 나머지 처리를 건너뛴다. 바깥 분기 종료·빈 줄(35–36)도 포함한다. |
| 37–55 | `find_package(PkgConfig QUIET)` (37), `if (PkgConfig_FOUND)` (38)에서 `pkg_check_modules(_NetCDF QUIET netcdf IMPORTED_TARGET)` (39)을 호출한다. `if (_NetCDF_FOUND)` (40)에서는 주석 `# Forward the variables in a consistent way.` (41) 다음 `set(NetCDF_FOUND "${_NetCDF_FOUND}")` (42), `set(NetCDF_INCLUDE_DIRS "${_NetCDF_INCLUDE_DIRS}")` (43), `set(NetCDF_LIBRARIES "${_NetCDF_LIBRARIES}")` (44), `set(NetCDF_VERSION "${_NetCDF_VERSION}")` (45)를 적용한다. 그 안 `if (NOT TARGET NetCDF::NetCDF)` (46)일 때 `add_library(NetCDF::NetCDF INTERFACE IMPORTED)` (47), `set_target_properties(NetCDF::NetCDF PROPERTIES` (48), `INTERFACE_LINK_LIBRARIES "PkgConfig::_NetCDF")` (49)를 적용한다. 내부 분기 종료(50) 뒤 주석 `# Skip the rest of the logic in this file.` (51)와 `return ()` (52)가 있다. 나머지는 분기 종료·빈 줄(53–55)이다. |
| 56–80 | 앞의 두 검색 경로에서 반환하지 않은 경우이다. `find_path(NetCDF_INCLUDE_DIR` (56), `NAMES netcdf.h` (57), `DOC "netcdf include directories")` (58), `mark_as_advanced(NetCDF_INCLUDE_DIR)` (59)로 헤더 경로를 찾는다. `find_library(NetCDF_LIBRARY` (61), `NAMES netcdf` (62), `DOC "netcdf library")` (63), `mark_as_advanced(NetCDF_LIBRARY)` (64)로 라이브러리를 찾는다. `if (NetCDF_INCLUDE_DIR)` (66)에서 `file(STRINGS "${NetCDF_INCLUDE_DIR}/netcdf.h" _netcdf_version_lines` (67), `REGEX "#define[ \t]+NC_VERSION_(MAJOR\|MINOR\|PATCH\|NOTE)")` (68)로 버전 선언을 읽는다. 추출식은 `string(REGEX REPLACE ".*NC_VERSION_MAJOR *\([0-9]*\).*" "\\1" _netcdf_version_major "${_netcdf_version_lines}")` (69), `string(REGEX REPLACE ".*NC_VERSION_MINOR *\([0-9]*\).*" "\\1" _netcdf_version_minor "${_netcdf_version_lines}")` (70), `string(REGEX REPLACE ".*NC_VERSION_PATCH *\([0-9]*\).*" "\\1" _netcdf_version_patch "${_netcdf_version_lines}")` (71), `string(REGEX REPLACE ".*NC_VERSION_NOTE *\"\([^\"]*\)\".*" "\\1" _netcdf_version_note "${_netcdf_version_lines}")` (72), `set(NetCDF_VERSION "${_netcdf_version_major}.${_netcdf_version_minor}.${_netcdf_version_patch}${_netcdf_version_note}")` (73)이다. 이후 `unset(_netcdf_version_major)` (74), `unset(_netcdf_version_minor)` (75), `unset(_netcdf_version_patch)` (76), `unset(_netcdf_version_note)` (77), `unset(_netcdf_version_lines)` (78)로 임시 변수를 제거한다. 79행에서 분기를 닫으며 빈 줄도 포함한다. |
| 81–96 | `include(FindPackageHandleStandardArgs)` (81), `find_package_handle_standard_args(NetCDF` (82), `REQUIRED_VARS NetCDF_LIBRARY NetCDF_INCLUDE_DIR` (83), `VERSION_VAR NetCDF_VERSION)` (84)로 패키지 결과를 정한다. `if (NetCDF_FOUND)` (86)에서 `set(NetCDF_INCLUDE_DIRS "${NetCDF_INCLUDE_DIR}")` (87), `set(NetCDF_LIBRARIES "${NetCDF_LIBRARY}")` (88)를 적용한다. 그 안 `if (NOT TARGET NetCDF::NetCDF)` (90)에서 `add_library(NetCDF::NetCDF UNKNOWN IMPORTED)` (91), `set_target_properties(NetCDF::NetCDF PROPERTIES` (92), `IMPORTED_LOCATION "${NetCDF_LIBRARY}"` (93), `INTERFACE_INCLUDE_DIRECTORIES "${NetCDF_INCLUDE_DIR}")` (94)를 적용한다. 95–96행에서 두 분기를 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–35·37–54·56–96: CMake 구성 패키지 검색과 PkgConfig 검색은 성공 분기에서 `return ()`을 호출한다. 마지막 표준 인수 처리 블록은 두 경로에서 반환하지 않았을 때 도달한다.
