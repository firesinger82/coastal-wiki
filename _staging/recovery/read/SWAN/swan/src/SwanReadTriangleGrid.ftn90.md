---
file: models/SWAN/raw/source_code/swan/src/SwanReadTriangleGrid.ftn90
lines: 178
sha256: 2e5cfc392b5584aa263896a488495afe9d96c06b0d191761330d2a4ad3f173ae
reader: codex gpt-6.1-sol
read_date: 2026-10-12
---

# SwanReadTriangleGrid.ftn90 — 판독 구간 기록

구간은 1행부터 178행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–53 | SwanReadTriangleGrid를 시작한다(1). 저작권·GPL 3 이상·무보증·2007년 신규 이력을 적는다(3–36). `<name>.node`의 정점 좌표와 `<name>.ele`의 삼각형 정점을 읽는다는 목적·방법과 모듈 사용을 포함한다(40–52). |
| 54–82 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. 파일명 길이와 기본 이름(base name) 입력, 파일명·추적·입출력/할당 상태·식별 번호·속성(attribute) 수·경계 표지(boundary marker) 여부·차원·셀당 정점 수·더미 실수(dummy real)·문자열·중단 변수를 선언한다(56–75). nbmark 주석 범위는 0 또는 1, ndim 주석 요구값은 2이다(69–70). 원문(행 순서): `integer, save     :: ient = 0 ! number of entries in this subroutine` (62). |
| 83–115 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. 기본 이름에 '.node'를 붙여 FOR로 열고 중단을 확인한다(87–91). nverts·ndim·nattr·nbmark를 자유 형식(list-directed input)으로 읽는다(95). 좌표와 vmark를 미할당일 때 순차 할당하고 실패하면 수준 4 메시지를 낸 뒤 `goto 900`으로 이동한다(96–107). nbmark=0이면 경계 표지 필수 메시지를 내고 레이블 900으로 이동한다(111–114). 원문(행 순서): `if (ltrace) call strace (ient,'SwanReadTriangleGrid')` (83); `filenm = trim(basenm)//'.node'` (87); `ndsd   = 0` (88); `iostat = 0` (89); `call for (ndsd, filenm, 'OF', iostat)` (90); `if (stpnow()) goto 900` (91); `istat = 0` (96); `if(.not.allocated(xcugrd)) allocate (xcugrd(nverts), stat = istat)` (97); `if ( istat == 0 ) then` (98); `if(.not.allocated(ycugrd)) allocate (ycugrd(nverts), stat = istat)` (99); `if ( istat == 0 ) then` (101); `if(.not.allocated(vmark)) allocate (vmark(nverts), stat = istat)` (102); `if ( istat /= 0 ) then` (104); `call msgerr ( 4, 'Allocation problem in SwanReadTriangleGrid: array xcugrd, ycugrd or vmark ' )` (105); `if ( nbmark == 0 ) then` (111); `call msgerr ( 4, 'boundary marker for vertices/faces must be specified ' )` (112). 입력문은 `read(ndsd, *, end=950, err=910) nverts, ndim, nattr, nbmark`이다(95). 입력문은 파일 끝에서 950으로 이동한다. 입력문은 판독 오류에서 910으로 이동한다. [10-13 전수 검증 보완] |
| 116–133 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. nattr=0이면 번호·좌표·표지를 읽는다(118–122). else는 좌표와 표지 사이에 더미 실수 rdum 한 개를 더 읽는다(123–127). 두 경로 모두 ii를 배열 인덱스로 쓰고 ii/=j이면 번호 순서 경고를 낸다(120–126). 분기 종료 후 .node를 닫는다(128–132). 원문(행 순서): `if ( nattr == 0 ) then` (118); `do j = 1, nverts` (119); `if ( ii/=j ) call msgerr ( 1, 'numbering of vertices is not sequential in Triangle file '//filenm )` (121); `else` (123); `do j = 1, nverts` (124); `if ( ii/=j ) call msgerr ( 1, 'numbering of vertices is not sequential in Triangle file '//filenm )` (126). 두 `read`는 파일 끝에서 `end=950`으로 이동한다(120·125). 두 `read`는 판독 오류에서 `err=910`으로 이동한다(120·125). [10-13 전수 검증 보완] |
| 134–168 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. 기본 이름에 '.ele'를 붙여 FOR로 열고 중단을 확인한다(136–140). ncells·nnodes·nattr를 읽고 kvertc(3,ncells)를 미할당일 때 할당하며 실패하면 수준 4 메시지를 낸 뒤 `goto 900`으로 이동한다(144–149). nnodes=3·nattr=0이면 번호·세 정점을 읽고 else는 뒤에 문자 line 한 개를 더 읽는다(153–163). 두 경로 모두 ii/=j 순서 경고를 내며 정상 경로는 .ele를 닫는다(156·161·167). 원문(행 순서): `filenm = trim(basenm)//'.ele'` (136); `ndsd   = 0` (137); `iostat = 0` (138); `call for (ndsd, filenm, 'OF', iostat)` (139); `if (stpnow()) goto 900` (140); `if(.not.allocated(kvertc)) allocate (kvertc(3,ncells), stat = istat)` (145); `if ( istat /= 0 ) then` (146); `call msgerr ( 4, 'Allocation problem in SwanReadTriangleGrid: array kvertc ' )` (147); `if ( nnodes == 3 .and. nattr == 0 ) then` (153); `do j = 1, ncells` (154); `if ( ii/=j ) call msgerr ( 1, 'numbering of triangles is not sequential in Triangle file '//filenm )` (156); `else` (158); `do j = 1, ncells` (159); `if ( ii/=j ) call msgerr ( 1, 'numbering of triangles is not sequential in Triangle file '//filenm )` (161). 세 `read`는 파일 끝에서 `end=950`으로 이동한다(144·155·160). 세 `read`는 판독 오류에서 `err=910`으로 이동한다(144·155·160). [10-13 전수 검증 보완] |
| 169–178 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. 레이블 900에서 반환한다(169). 판독 오류 910과 예상 밖 파일 끝 950은 inquire로 파일명을 얻고 msgerr 수준 4를 호출한 뒤 900으로 이동한다(171–176). 루틴 종료를 포함한다(178). 원문(행 순서): `call msgerr (4, 'error reading data from Triangle file '//filenm )` (172); `call msgerr (4, 'unexpected end of file in Triangle file '//filenm )` (175). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·95·144–163: ndim의 주석 요구값은 2이며 이 루틴에는 ndim을 검사하는 조건이 없다. nnodes가 3이 아닌 경우도 else에서 세 정점만 kvertc에 읽는다.
- 95·118–128: nattr가 0이 아닌 정점 입력 분기는 속성 수와 관계없이 rdum 한 개를 읽는다. nattr개의 속성을 반복해서 건너뛰는 루프는 없다.
- 120–121·125–126·155–156·160–161: 입력 번호 ii를 배열 인덱스로 쓰는 read가 ii/=j 경고보다 먼저 나온다. 이 블록에는 ii의 상하한 검사가 없다.
- 95–167: 정점 번호는 입력 ii로 직접 좌표·표지를 저장하고 삼각형 정점 번호도 직접 저장한다. 이 루틴에는 0부터 시작하는 번호를 1로 이동하는 대입이 없다.
- 91·104–114·140·146–149·169–176: close는 두 정상 판독 경로에 있다. 중단·할당 실패·표지 누락·판독 오류·예상 밖 파일 끝 경로는 레이블 900에서 반환하며 별도 close 문장이 없다.
- 63: idum은 선언 이후 사용되지 않는다.
