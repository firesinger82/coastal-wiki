---
file: models/SWASH/raw/source_code/swash/src/CMakeLists.txt
lines: 88
sha256: b3ab0328991da786f457164cb36288c5f63a05ecaefc726d4f104d2d69cf44d6
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# CMakeLists.txt — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 스위치(switch) 정의 주석(1). `if( WIN32 )` (2)은 `set( SWITCHES -dos -cvis )` (3), `elseif( UNIX )` (4)은 `set( SWITCHES -unix )` (5)이다. 이 플랫폼 분기에는 `else()`가 없다. 플랫폼 분기는 `endif()` (6)로 닫힌다. 사용자 스위치 주석(8) 뒤 `if( MPI )` (9) 안에서 `if( CMAKE_Fortran_COMPILER_ID MATCHES "GNU" )` (10)은 `list( APPEND SWITCHES -mpi )` (11), `else()` (12)는 `list( APPEND SWITCHES -impi -mpi )` (13)이다. 10행 컴파일러 조건은 `endif()` (14)로 닫힌다. 9행 MPI 조건은 `endif()` (15)로 닫힌다. 16행은 빈 줄이다. [10-15 전수 검증 보완] |
| 17–23 | `if( PERL_FOUND )` (18)이면 `execute_process( COMMAND ${PERL_EXECUTABLE} ${CMAKE_SOURCE_DIR}/switch.pl ${SWITCHES} ${SRC}/*.ftn ${SRC}/*.ftn90 )` (19)로 Fortran 원문을 전처리한다. `else()` (20)는 `message( FATAL_ERROR "-- Cannot build ${CMAKE_PROJECT_NAME} without Perl" )` (21)이다. switch.pl 57–66행은 선택한 스위치에 대응하는 행 첫머리 표시만 지운다. |
| 24–33 | `if( CMAKE_Fortran_COMPILER_ID MATCHES "GNU" )` (25)은 `set( CMAKE_Fortran_FLAGS "-O -w -fno-second-underscore -ffree-line-length-none" CACHE STRING "" FORCE )` (27)이다. 이 분기에서 `if( ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 10 )` (28)이면 `set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fallow-argument-mismatch" )` (29)을 추가한다. `if( WIN32 AND ${CMAKE_Fortran_COMPILER_VERSION} VERSION_GREATER_EQUAL 7 )` (31)이면 `set( CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fdec" )` (32)을 추가한다. |
| 34–53 | 이 구간은 `if( CMAKE_Fortran_COMPILER_ID MATCHES "GNU" )` (25)로 시작한 분기 사슬의 후속 분기부터 이어진다. 이 분기 사슬은 `endif()` (52)로 닫힌다. `elseif( CMAKE_Fortran_COMPILER_ID MATCHES "Intel" )` (34)의 `if( UNIX )` (36)은 `set( CMAKE_Fortran_FLAGS "-O2 -W0 -assume byterecl -traceback -diag-disable 8290 -diag-disable 8291 -diag-disable 8293" CACHE STRING "" FORCE )` (37), `elseif( WIN32 )` (38)은 `set( CMAKE_Fortran_FLAGS "/O2 /assume:byterecl /traceback /nowarn /nologo /Qdiag-disable:8290 /Qdiag-disable:8291 /Qdiag-disable:8293" CACHE STRING "" FORCE )` (39)이다. 36–40행의 Intel 플랫폼 분기에는 `else()`가 없다. Intel 플랫폼 분기는 `endif()` (40)로 닫힌다. `elseif( CMAKE_Fortran_COMPILER_ID MATCHES "PGI" )` (41)은 `set( CMAKE_Fortran_FLAGS "-fast" CACHE STRING "" FORCE )` (43), `elseif( CMAKE_Fortran_COMPILER_ID MATCHES "Fujitsu" )` (44)은 `set( CMAKE_Fortran_FLAGS "-O1 -staticlink -nwo" CACHE STRING "" FORCE )` (46), `elseif( CMAKE_Fortran_COMPILER_ID MATCHES "XL" )` (47)은 `set( CMAKE_Fortran_FLAGS "-O3 -qstrict -qarch=auto -qtune=auto -qcache=auto -qalign=4k -w" CACHE STRING "" FORCE )` (49)이다. `else()` (50)는 `message( FATAL_ERROR "-- Current Fortran compiler ${CMAKE_Fortran_COMPILER} not supported" )` (51)이다. [10-15 전수 검증 보완] |
| 54–70 | `if( MPI )` (55)은 `find_package( MPI REQUIRED COMPONENTS Fortran )` (56)이다. `else()` (57)는 `unset( MPI_Fortran_FOUND CACHE )` (59), `unset( MPI_Fortran_COMPILER CACHE )` (60), `unset( MPI_Fortran_LIBRARIES CACHE )` (61)이다. 라이브러리(library) 생성 주석(64) 뒤 `if( NOT TARGET swash${VERSION} )` (65)은 `include( ${SRC}/srclist.cmake )` (66), `add_library( swash${VERSION} STATIC ${swash_src} )` (67), `set_target_properties( swash${VERSION} PROPERTIES LINKER_LANGUAGE Fortran )` (68)이다. |
| 71–88 | `if( NOT TARGET ${EXE} )` (72)은 `set( swashmain ${SRC}/Swash.f90 )` (73), `add_executable( ${EXE} ${swashmain} )` (74), `target_link_libraries( ${EXE} swash${VERSION} ${MPI_Fortran_LIBRARIES} )` (75)이다. 72행 조건은 `endif()` (76)로 닫힌다. 79–83행 설치 명령은 이 조건 밖에 있다. 설치 명령은 `install( TARGETS ${EXE} swash${VERSION} RUNTIME DESTINATION bin LIBRARY DESTINATION lib ARCHIVE DESTINATION lib )` (79), `install( DIRECTORY ${CMAKE_BINARY_DIR}/mod/ DESTINATION mod )` (80), `install( DIRECTORY ${CMAKE_SOURCE_DIR}/doc/ DESTINATION doc )` (81), `install( DIRECTORY ${CMAKE_SOURCE_DIR}/misc/ DESTINATION misc )` (82), `install( DIRECTORY ${CMAKE_SOURCE_DIR}/tools/ DESTINATION tools )` (83)이다. `if( WIN32 )` (84)은 `install( PROGRAMS ${CMAKE_SOURCE_DIR}/bin/swashrun.bat DESTINATION bin )` (85), `elseif( UNIX )` (86)은 `install( PROGRAMS ${CMAKE_SOURCE_DIR}/bin/swashrun DESTINATION bin )` (87)이다. 84–88행 플랫폼 분기에는 `else()`가 없다. 이 분기는 `endif()` (88)로 닫힌다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–22: execute_process 호출에는 RESULT_VARIABLE을 받는 인수가 없다. 이 파일에는 switch.pl 실행 결과를 검사하는 조건이 없다.
- 27·37·39·43·46·49: 기본 컴파일러 플래그 설정은 CACHE STRING에 FORCE를 사용한다.
