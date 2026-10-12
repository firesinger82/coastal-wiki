---
file: models/SWAN/raw/source_code/swan/src/SwanReadADCGrid.ftn90
lines: 189
sha256: d084ba33da3dd3f7b4b3bd51fcdf51fe3157d5a56827f3b09fadee1f5ecde9ea
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanReadADCGrid.ftn90 — 판독 구간 기록

구간은 1행부터 189행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–61 | SwanReadADCGrid 루틴을 시작한다(1). 저작권·GPL 3 이상·무보증·신규 및 ADCIRC 경계/매핑(mapping) 갱신 이력을 적는다(3–40). fort.14에서 정점 좌표·삼각형 정점·바닥 지형(bottom topography)을 읽는다는 목적과 모듈 사용을 포함한다(44–60). |
| 62–88 | 시작 시 1행 SwanReadADCGrid 루틴 안. 파일명·추적·입출력 상태·할당 상태·ADCIRC 경계 유형(boundary type)·정점/루프/경계 수·경계 표지(boundary marker)·중단 변수를 선언한다(64–81). 구조·소스 구분 주석을 포함한다(83–88). 원문(행 순서): `integer, save           :: ient = 0 ! number of entries in this subroutine` (65). |
| 89–118 | 시작 시 1행 SwanReadADCGrid 루틴 안. strace를 조건부 호출한다(89). fort.14를 FOR로 열고 중단이면 레이블 900으로 이동한다(93–97). 첫 제목 줄을 a80으로 읽고 ncells·nverts를 자유 형식(list-directed input)으로 읽는다(101·105). 좌표·DEPTH 배열을 미할당일 때만 순차 할당하고 실패 시 msgerr 수준 4를 호출한다(106–117). 두 read의 파일 끝은 레이블 950으로 이동한다(101·105). 두 read의 판독 오류는 레이블 910으로 이동한다(101·105). 할당 실패 메시지 뒤에 `goto 900`을 실행한다(116). 원문(행 순서): `if (ltrace) call strace (ient,'SwanReadADCGrid')` (89); `ndsd   = 0` (93); `iostat = 0` (94); `grdfil = 'fort.14'` (95); `call for (ndsd, grdfil, 'OF', iostat)` (96); `if (stpnow()) goto 900` (97); `istat = 0` (106); `if(.not.allocated(xcugrd)) allocate (xcugrd(nverts), stat = istat)` (107); `if ( istat == 0 ) then` (108); `if(.not.allocated(ycugrd)) allocate (ycugrd(nverts), stat = istat)` (109); `if ( istat == 0 ) then` (111); `if(.not.allocated(DEPTH)) allocate (DEPTH(nverts), stat = istat)` (112); `if ( istat /= 0 ) then` (114); `call msgerr ( 4, 'Allocation problem in SwanReadADCGrid: array xcugrd, ycugrd or depth ' )` (115). [10-13 전수 검증 보완] |
| 119–145 | 시작 시 1행 SwanReadADCGrid 루틴 안. 정점 번호 ii와 xcugrd(ii)·ycugrd(ii)·DEPTH(ii)를 읽고 ii/=j이면 번호 순서 경고를 낸다(121–124). kvertc(3,ncells)를 할당하고 삼각형 번호·더미 정수(dummy integer)·세 정점 번호를 읽는다(126–137). 삼각형 번호 불일치도 경고한다(136). vmark를 할당하고 0으로 초기화한다(139–144). 각 할당 실패 메시지 뒤에 `goto 900`을 실행한다(129·142). 두 read는 파일 끝에서 950으로 이동한다(122·135). 두 read는 판독 오류에서 910으로 이동한다(122·135). 원문(행 순서): `do j = 1, nverts` (121); `if ( ii/=j ) call msgerr ( 1, 'numbering of vertices is not sequential in grid file fort.14 ' )` (123); `if(.not.allocated(kvertc)) allocate (kvertc(3,ncells), stat = istat)` (126); `if ( istat /= 0 ) then` (127); `call msgerr ( 4, 'Allocation problem in SwanReadADCGrid: array kvertc ' )` (128); `do j = 1, ncells` (134); `if ( ii/=j ) call msgerr ( 1, 'numbering of triangles is not sequential in grid file fort.14 ' )` (136); `if(.not.allocated(vmark)) allocate (vmark(nverts), stat = istat)` (139); `if ( istat /= 0 ) then` (140); `call msgerr ( 4, 'Allocation problem in SwanReadADCGrid: array vmark ' )` (141); `vmark = 0` (144). [10-13 전수 검증 보완] |
| 146–177 | 시작 시 1행 SwanReadADCGrid 루틴 안. 열린 경계(open boundary) 수 nopbc와 더미 정수 idum를 읽고 경계별 점 수와 정점 번호에 vm=j를 저장한다(148–157). 이어 다른 경계 수 n1과 더미 정수 idum를 읽고 vm=nopbc+j로 표지를 부여한다(159–163). itype가 4·24가 아니면 단일 정점, else는 정점 쌍을 읽고 두 점 모두 표지한다(164–175). 루프 종료를 포함한다(176). 원문(행 순서): `do j = 1, nopbc` (150); `vm = j` (151); `do k = 1, n2` (153); `vmark(ivert) = vm` (155); `do j = 1, n1` (161); `vm = nopbc + j` (162); `if ( itype /= 4 .and. itype /= 24 ) then` (164); `do k = 1, n2` (165); `vmark(ivert) = vm` (167); `else` (169); `do k = 1, n2` (170); `vmark(ivert ) = vm` (172); `vmark(ivert1) = vm` (173). [10-13 전수 검증 정정] |
| 178–189 | 시작 시 1행 SwanReadADCGrid 루틴 안. 정상 경로는 close(ndsd) 후 레이블 900에서 반환한다(180–182). 레이블 910은 판독 오류, 950은 예상 밖 파일 끝 메시지를 msgerr 수준 4로 내고 900으로 이동한다(184–187). 루틴 종료를 포함한다(189). 원문(행 순서): `910 call msgerr (4, 'error reading data from grid file fort.14' )` (184); `950 call msgerr (4, 'unexpected end of file in grid file fort.14' )` (186). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 122–123·135–136: 정점/삼각형 번호 ii를 배열 인덱스로 사용하는 read가 ii/=j 경고보다 먼저 나온다. 이 블록에는 ii의 상하한 검사나 중복 번호 검사가 없다.
- 135: 삼각형 자료 read의 두 번째 정수 항목은 idum이다. 이 루틴에는 idum=3 확인 조건이 없다. [10-13 전수 검증 정정]
- 97·114–117·127–130·140–143·180–187: close(ndsd)는 정상 판독 경로에 있다. 중단·할당 실패·판독 오류·예상 밖 파일 끝 경로는 close를 거치지 않고 레이블 900으로 이동한다.
