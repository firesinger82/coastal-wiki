---
file: models/SWAN/raw/source_code/swan/src/SwanPrintGridInfo.ftn90
lines: 177
sha256: bffdfe5a53e3d8ead20704e5fdf385056fa7764e8bdcf5af0b84951a0901fd51
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanPrintGridInfo.ftn90 — 판독 구간 기록

구간은 1행부터 177행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | SwanPrintGridInfo 루틴을 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 추가 이력과 격자 정보 출력 목적을 적는다(3–40). ocpcomm4·SwanGriddata·SwanGridobjects와 implicit none을 포함한다(44–48). [10-13 전수 검증 정정] |
| 49–82 | 시작 시 1행 SwanPrintGridInfo 루틴 안. 경계/내부 셀·면 수, 셀 면적(area), 격자 크기, 삼각형 높이(altitude) h(3), 출력 도움 문자열과 셀·면 객체 포인터(pointer)를 선언한다(52–68). strace를 조건부 호출하고 객체를 연결한다(76–81). 원문(행 순서): `integer, save                         :: ient = 0  ! number of entries in this subroutine` (53); `if (ltrace) call strace (ient,'SwanPrintGridInfo')` (76); `cell => gridobject%cell_grid` (80); `face => gridobject%face_grid` (81). |
| 83–128 | 시작 시 1행 SwanPrintGridInfo 루틴 안. SMS/ADCIRC·Triangle·Easymesh 분기는 셀 형상 설명을 삼각형만으로 설정한다(83–102). 마지막 ELSE는 셀 형상 설명을 삼각형 또는 혼합 셀로 설정한다(104–106). 이 ELSE는 생성기명을 unknown으로 설정한다(107). FMARKER=1·CMARKER=1인 항목을 경계로 세고 전체 수에서 빼 내부 수를 계산한다(113–122). PRINTF에 생성기·정점·셀·면 수를 출력한다(126–127). 원문(행 순서): `if ( grid_generator == meth_adcirc ) then` (83); `write (helptxt(1),'(a)') 'solely triangles'` (87); `write (helptxt(2),'(a)') 'SMS/ADCIRC'` (88); `elseif ( grid_generator == meth_triangle ) then` (90); `write (helptxt(1),'(a)') 'solely triangles'` (94); `write (helptxt(2),'(a)') 'Triangle'` (95); `elseif ( grid_generator == meth_easy ) then` (97); `write (helptxt(1),'(a)') 'solely triangles'` (101); `write (helptxt(2),'(a)') 'Easymesh'` (102); `else` (104); `write (helptxt(1),'(a)') 'triangles or hybrid cells'` (106); `write (helptxt(2),'(a)') 'unknown'` (107); `nfacesb = 0` (113); `do i = 1, nfaces` (114); `if ( face(i)%atti(FMARKER) == 1 ) nfacesb = nfacesb + 1` (115); `nfacesi = nfaces - nfacesb` (117); `ncellsb = 0` (118); `do i = 1, ncells` (119); `if ( cell(i)%atti(CMARKER) == 1 ) ncellsb = ncellsb + 1` (120); `ncellsi = ncells - ncellsb` (122). [10-13 전수 검증 보완] |
| 129–163 | 시작 시 1행 SwanPrintGridInfo 루틴 안. 최소/최대 격자 크기를 1.0e10·0.0으로 시작한다(131–132). 각 높이는 셀 면적의 두 배를 해당 면 길이로 나눈 값이다(138–144). 격자 크기는 세 높이의 역제곱 평균에 제곱근을 취한 값의 역수다(149). 최소 갱신 IF가 거짓일 때만 최대 갱신 ELSEIF를 검사한다(153–156). 이 분기 사슬에는 ELSE가 없다(157). 최솟값과 최댓값을 출력한다(161–162). 원문(행 순서): `mingsiz = 1.0e10` (131); `maxgsiz = 0.0` (132); `do i = 1, ncells` (134); `area = cell(i)%attr(CELLAREA)` (138); `do j = 1, cell(i)%nof` (142); `iface  = cell(i)%face(j)%atti(FACEID)` (143); `h(j) = 2.*area/face(iface)%attr(FACELEN)` (144); `gridsize = 1./sqrt((h(1)**(-2)+h(2)**(-2)+h(3)**(-2))/3.)` (149); `if ( gridsize < mingsiz ) then` (153); `mingsiz = gridsize` (154); `elseif ( gridsize > maxgsiz ) then` (155); `maxgsiz = gridsize` (156). [10-13 전수 검증 정정] |
| 164–177 | 시작 시 1행 SwanPrintGridInfo 루틴 안. 정점·셀·면·내부/경계 개수와 최소·최대 격자 크기 출력 format를 정의한다(166–175). 빈 줄과 루틴 종료를 포함한다(176–177). 원문(행 순서): `' Number of vertices          = ',i7//                         &` (167); `' Number of cells             = ', i7/                         &` (168); `'    Number of internal cells = ', i7/                         &` (169); `'    Number of boundary cells = ',i7//                         &` (170); `' Number of faces             = ',i7/                          &` (171); `'    Number of internal faces = ',i7/                          &` (172); `'    Number of boundary faces = ',i7//)` (173). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 63·104–107·142–149: h는 길이 3이다. 그 밖의 생성기 설명은 'triangles or hybrid cells'이며 높이 저장 루프의 상한은 cell(i)%nof이다. 격자 크기 식은 h(1)·h(2)·h(3)만 사용한다.
- 131–157: mingsiz 초기값은 1.0e10이고 maxgsiz 초기값은 0.0이다. 최대값 갱신은 최소값 갱신 조건의 elseif에 있다.

