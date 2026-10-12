---
file: models/SWAN/raw/source_code/swan/src/SwanReadGrid.ftn90
lines: 131
sha256: adba920f26e32f738a79298d7a41538b5209a1793ab3e8cd86389fd8b3ff1389
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanReadGrid.ftn90 — 판독 구간 기록

구간은 1행부터 131행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–54 | SwanReadGrid 루틴을 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 신규 이력을 적는다(3–36). 비정형 격자(unstructured grid)를 ADCIRC·Triangle·Easymesh에서 읽는다는 목적·방법과 모듈 사용을 포함한다(40–53). |
| 55–70 | 시작 시 1행 SwanReadGrid 루틴 안. 파일명 길이 lenfnm·기본 이름(base name) basenm, 루프 변수와 추적 변수를 선언한다(57–63). 구조·소스 구분 주석을 포함한다(65–70). 원문(행 순서): `integer, save :: ient = 0 ! number of entries in this subroutine` (63). |
| 71–97 | 시작 시 1행 SwanReadGrid 루틴 안. grid_generator에 따라 SwanReadADCGrid·SwanReadTriangleGrid·SwanReadEasymeshGrid를 호출한다(73–89). ADCIRC 호출에는 파일명 인수가 없고 다른 두 호출은 basenm·lenfnm을 받는다(77·83·89). 그 밖의 생성기는 msgerr 수준 4와 반환으로 처리한다(91–96). 원문(행 순서): `if (ltrace) call strace (ient,'SwanReadGrid')` (71); `if ( grid_generator == meth_adcirc ) then` (73); `call SwanReadADCGrid` (77); `elseif ( grid_generator == meth_triangle ) then` (79); `call SwanReadTriangleGrid ( basenm, lenfnm )` (83); `elseif ( grid_generator == meth_easy ) then` (85); `call SwanReadEasymeshGrid ( basenm, lenfnm )` (89); `else` (91); `call msgerr ( 4, 'Unknown grid generator' )` (93). |
| 98–112 | 시작 시 1행 SwanReadGrid 루틴 안. 정점 루프에서 LXOFFS가 거짓이면 현재 정점 좌표를 XOFFS·YOFFS로 보관하고 그 정점 좌표를 0으로 둔다(100–106). else는 기존 오프셋(offset)을 dble로 변환해 뺀 값을 real로 저장한다(107–110). 루프 종료를 포함한다(111). 원문(행 순서): `do i = 1, nverts` (100); `if ( .not.LXOFFS ) then` (101); `XOFFS = xcugrd(i)` (102); `YOFFS = ycugrd(i)` (103); `LXOFFS = .true.` (104); `xcugrd(i) = 0.` (105); `ycugrd(i) = 0.` (106); `else` (107); `xcugrd(i) = real(xcugrd(i) - dble(XOFFS))` (108); `ycugrd(i) = real(ycugrd(i) - dble(YOFFS))` (109). |
| 113–131 | 시작 시 1행 SwanReadGrid 루틴 안. XCGMIN·YCGMIN=1.e9, XCGMAX·YCGMAX=-1.e9로 시작한다(115–118). 모든 정점 좌표를 비교해 각 축 극값을 갱신한다(119–124). 최대-최소로 영역 포위 사각형(enclosing rectangle) 길이 XCLEN·YCLEN을 구하고 루틴을 끝낸다(128–131). 원문(행 순서): `XCGMIN =  1.e9` (115); `YCGMIN =  1.e9` (116); `XCGMAX = -1.e9` (117); `YCGMAX = -1.e9` (118); `do i = 1, nverts` (119); `if ( xcugrd(i) < XCGMIN ) XCGMIN = xcugrd(i)` (120); `if ( ycugrd(i) < YCGMIN ) YCGMIN = ycugrd(i)` (121); `if ( xcugrd(i) > XCGMAX ) XCGMAX = xcugrd(i)` (122); `if ( ycugrd(i) > YCGMAX ) YCGMAX = ycugrd(i)` (123); `XCLEN = XCGMAX - XCGMIN` (128); `YCLEN = YCGMAX - YCGMIN` (129). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 77–96·100–111: 세 격자 판독 루틴 호출 뒤에는 STPNOW 검사 문장이 없다. 인식된 생성기 분기 종료 후 좌표 처리 루프를 계속한다.
- 101–110: 오프셋 선택은 LXOFFS가 거짓인 첫 처리 정점에서 수행하며 LXOFFS를 참으로 바꾼다. LXOFFS가 이미 참이면 새 격자의 첫 정점에도 기존 XOFFS·YOFFS를 뺀다.
- 115–129: 좌표 극값은 ±1.e9로 초기화한다. 정점 수가 0인 경우를 따로 처리하는 조건은 이 루틴에 없다.

