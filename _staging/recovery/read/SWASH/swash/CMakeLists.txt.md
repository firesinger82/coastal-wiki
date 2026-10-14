---
file: models/SWASH/raw/source_code/swash/CMakeLists.txt
lines: 63
sha256: 3fbdeb86fcc7ee645dd489015684128fe3a8f3cde620f0a821846f39353da9c9
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 머리말은 SWASH 빌드용 CMake 스크립트라고 적는다(1–2). 저작권은 `Copyright (C) 2026  Delft University of Technology`이다(3). 최소 버전 주석은 `3.20 or greater`이다(5). 버전 요구 명령은 `cmake_minimum_required( VERSION 3.20 )` (6)이다. 빈 줄을 포함한다(4·7). |
| 8–15 | 기본 설치 위치 주석은 사용자 로컬 또는 홈 디렉터리라고 적는다(8). 플랫폼 조건은 `if( WIN32 )` (9)이다. Windows 분기 명령은 `  cmake_path( SET LOCALSWASH $ENV{LOCALAPPDATA}/Programs/wavemodels/swash )` (10)과 `  set( CMAKE_INSTALL_PREFIX "${LOCALSWASH}" CACHE STRING "" )` (11)이다. 반대 분기 시작은 `else()` (12)이며 명령은 `  set( CMAKE_INSTALL_PREFIX "$ENV{HOME}/wavemodels/swash" CACHE STRING "" )` (13)이다. `endif()`로 조건을 닫는다(14). 두 설치 경로는 캐시(cache) 문자열 `CMAKE_INSTALL_PREFIX`로 설정된다(11·13). 빈 줄을 포함한다(15). |
| 16–24 | Fortran 프로젝트 선언은 `project( SWASH Fortran )` (17)이다(16). 버전 설정식은 `set( VERSION 12.01 )` (20)이다(19). 빌드 형식 설정식은 `set( CMAKE_BUILD_TYPE None CACHE STRING "" FORCE )` (23)이다(22). 이 설정식은 `CMAKE_BUILD_TYPE` 캐시 문자열을 `None`으로 강제한다(23). 주석·빈 줄을 포함한다(16·18–19·21–22·24). |
| 25–37 | 실행 파일 이름의 플랫폼 조건은 `if( WIN32 )` (26)이다(25). 참 분기는 `   set( EXE swash )` (27)이다. 반대 분기 `else()` (28)는 `   set( EXE swash.exe )` (29)를 실행한다. 실행 파일 이름 조건을 `endif()`로 닫는다(30). Fortran77 확장자 조건은 `if( WIN32 )` (33)이다(32). 참 분기는 `   set( EXTF for )` (34)이다. 반대 분기 `else()` (35)는 `   set( EXTF f   )` (36)을 실행한다. 확장자 조건을 `endif()`로 닫는다(37). 빈 줄을 포함한다(31). |
| 38–46 | 사용자 MPI 옵션 선언은 `option( MPI "" OFF )` (40)이다(39). 기본값은 `OFF`이다(40). 디렉터리 설정식은 `set( BIN ${CMAKE_BINARY_DIR}/bin )` (43), `set( LIB ${CMAKE_BINARY_DIR}/lib )` (44), `set( MOD ${CMAKE_BINARY_DIR}/mod )` (45), `set( SRC ${CMAKE_SOURCE_DIR}/src )` (46)이다. `BIN`, `LIB`, `MOD`는 빌드 디렉터리 기준이며 `SRC`는 소스 디렉터리 기준이다(43–46). 주석의 디렉터리 나열은 `bin/lib//mod/src`이다(42). 빈 줄을 포함한다(38·41). |
| 47–55 | 실행 파일 출력 디렉터리 명령은 `set( CMAKE_RUNTIME_OUTPUT_DIRECTORY ${BIN} )` (49)이다(48). 정적 아카이브 출력 디렉터리 명령은 `set( CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${LIB} )` (50)이다. 라이브러리 출력 디렉터리 명령은 `set( CMAKE_LIBRARY_OUTPUT_DIRECTORY ${LIB} )` (51)이다. Fortran 모듈 출력 디렉터리 명령은 `set( CMAKE_Fortran_MODULE_DIRECTORY ${MOD} )` (54)이다(53). 빈 줄을 포함한다(47·52·55). |
| 56–63 | 주석은 소스 코드의 스위치(switch) 설정에 Perl이 필요하다고 적는다(56). 패키지 검색 명령은 `find_package( Perl REQUIRED )` (57)이다. 라이브러리용 하위 디렉터리 추가 명령은 `add_subdirectory( ${SRC} ${LIB} )` (60)이다(59). 실행 파일용 하위 디렉터리 추가 명령은 `add_subdirectory( ${SRC} ${BIN} )` (63)이다(62). 두 명령의 소스 경로는 `${SRC}`로 같고 빌드 경로는 각각 `${LIB}`와 `${BIN}`이다(60·63). 빈 줄을 포함한다(58·61). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23: `set( CMAKE_BUILD_TYPE None CACHE STRING "" FORCE )`는 `FORCE`를 명시한다.
- 26–30: Windows 분기의 실행 파일 이름은 `swash`이다. 반대 분기의 실행 파일 이름은 `swash.exe`이다.
- 60·63: 같은 `${SRC}`에 대해 `add_subdirectory`를 두 번 호출한다. 두 호출은 서로 다른 빌드 경로 `${LIB}`와 `${BIN}`을 사용한다. 하위 `src/CMakeLists.txt` 내부는 이 판독 대상에 없다.
