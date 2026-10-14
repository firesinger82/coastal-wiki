---
file: models/SWASH/raw/source_code/swash/clobber.cmake
lines: 18
sha256: f803a8f2eea4c5ccefc43f187a0eaeca1be5ec4ca67712064e0951005ef6c4cd
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# clobber.cmake — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 머리말은 빌드 파일과 디렉터리 제거용이라고 적는다(1). 재귀 검색 명령은 `file( GLOB_RECURSE F90FILES "${CMAKE_SOURCE_DIR}/src/*.f" "${CMAKE_SOURCE_DIR}/src/*.for" "${CMAKE_SOURCE_DIR}/src/*.f90" )` (4)이다(3). 검색 패턴은 소스 디렉터리 아래 `src/*.f`, `src/*.for`, `src/*.f90`이다(4). 제거 목록 초기 설정식은 `set( DEL ${F90FILES} )` (7)이다(6). 빈 줄을 포함한다(2·5). |
| 8–12 | 제거 목록에 빌드 폴더를 넣는다는 주석이 있다(9). 검색 명령은 `file( GLOB BUILD "${CMAKE_SOURCE_DIR}/build" )` (10)이다. 목록 추가 설정식은 `set( DEL ${DEL} ${BUILD} )` (11)이다. 빈 줄을 포함한다(8·12). |
| 13–18 | 주석은 목록 항목을 순회하며 각각 삭제한다고 적는다(13). 반복 시작 명령은 `foreach( D ${DEL} )` (14)이다. 반복 내부 조건은 `  if( EXISTS ${D} )` (15)이다. 존재하는 항목의 제거 명령은 `    file( REMOVE_RECURSE ${D} )` (16)이다. `endif()`와 `endforeach()`로 조건과 반복을 닫는다(17–18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·7·10–16: 제거 목록에는 `build`와 소스 디렉터리 아래 `*.f`, `*.for`, `*.f90` 검색 결과가 함께 들어간다. 존재 조건을 통과한 모든 목록 항목에 `REMOVE_RECURSE`를 적용한다.
