---
file: models/SWASH/raw/source_code/swash/src/SwanReadADCGrid.ftn90
lines: 187
sha256: f32cc276600af3962a5d640f12e739f5e87fa034c80e2e7c5ebea0a4939962b0
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanReadADCGrid.ftn90 — 판독 구간 기록

구간은 1행부터 187행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–59 | SwanReadADCGrid 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29). 2007년 신설·2009년 ADCIRC 경계 자료로 모든 경계 꼭짓점(vertex) 표시 이력(30–38). fort.14에서 좌표·삼각형 꼭짓점·바닥 지형(bottom topography)을 읽는다는 목적·방법(40–49). ocpcomm2·ocpcomm4·m_genarr·SwanGriddata 사용(53–56), implicit none(58). |
| 60–86 | 시작 시 1행 SwanReadADCGrid 루틴 안. 파일명 grdfil, `integer, save           :: ient = 0`(63), 읽기·할당 상태, 경계 유형·꼭짓점·카운터·파일 장치 번호(unit number)·경계 수·마커(marker), line·stpnow를 선언한다(62–79). 구조·실행부 표제(81–86). [10-15 전수 검증 보완] |
| 87–115 | 시작 시 1행 SwanReadADCGrid 루틴 안. `if (ltrace) call strace (ient,'SwanReadADCGrid')` (87). `ndsd   = 0`(91), `iostat = 0`(92), `grdfil = 'fort.14'`(93), `call for (ndsd, grdfil, 'OF', iostat)` (94), `if (stpnow()) goto 900` (95). 첫 제목 줄을 건너뛰고 셀(cell)·꼭짓점 수를 읽는다(99·103). `istat = 0`(104), `if(.not.allocated(xcugrd)) allocate (xcugrd(nverts), stat = istat)` (105). `if ( istat == 0 ) then` (106)의 `if(.not.allocated(ycugrd)) allocate (ycugrd(nverts), stat = istat)` (107), `if ( istat == 0 ) then` (109)의 `if(.not.allocated(DEPTH)) allocate (DEPTH(nverts), stat = istat)` (110). `if ( istat /= 0 ) then` (112)은 msgerr 등급 4와 goto 900(113–114)이다. read는 end=950·err=910을 사용한다. 106행 조건은 108행 `endif`에서 닫힌다. 109행 조건은 111행 `endif`에서 닫힌다. 112행 조건은 115행 `endif`에서 닫힌다. [10-15 전수 검증 보완] |
| 116–142 | 시작 시 1행 SwanReadADCGrid 루틴 안. `do j = 1, nverts` (119)에서 ii·좌표·DEPTH를 ii 인덱스로 읽는다(120). `if ( ii/=j ) call msgerr ( 1, 'numbering of vertices is not sequential in grid file fort.14 ' )` (121). `if(.not.allocated(kvertc)) allocate (kvertc(3,ncells), stat = istat)` (124), `if ( istat /= 0 ) then` (125)은 msgerr 등급 4·goto 900(126–127). `do j = 1, ncells` (132)은 ii·idum·세 꼭짓점을 ii 셀 인덱스로 읽는다(133). `if ( ii/=j ) call msgerr ( 1, 'numbering of triangles is not sequential in grid file fort.14 ' )` (134). `if(.not.allocated(vmark)) allocate (vmark(nverts), stat = istat)` (137), `if ( istat /= 0 ) then` (138)은 msgerr 등급 4·goto 900(139–140), `vmark = 0`(142)이다. [10-15 전수 검증 보완] |
| 143–155 | 시작 시 1행 SwanReadADCGrid 루틴 안. 개방 경계(open boundary) 수 nopbc와 idum을 읽는다(146–147). `do j = 1, nopbc` (148)은 `vm = j`(149), 경계점 수 n2 판독(150), `do k = 1, n2` (151)에서 ivert를 읽고 `vmark(ivert) = vm`(152–153)이다. 두 루프 종료(154–155). [10-15 전수 검증 정정] [10-15 전수 검증 보완] |
| 156–175 | 시작 시 1행 SwanReadADCGrid 루틴 안. 나머지 경계 수 n1와 idum을 읽는다(157–158). `do j = 1, n1` (159)은 `vm = nopbc + j` (160), n2·itype 판독(161). `if ( itype /= 4 .and. itype /= 24 ) then` (162)은 `do k = 1, n2` (163)에서 꼭짓점 1개 판독·표시(164–165). `else` (167)는 `do k = 1, n2` (168)에서 ivert·ivert1 두 개 판독·동일 마커 저장(169–171)이다. 조건·루프 종료(173–174). 162행 참 분기의 대입식은 `vmark(ivert) = vm`(165)이다. 167행 `else`의 대입식은 `vmark(ivert ) = vm`(170), `vmark(ivert1) = vm`(171)이다. 두 내부 루프는 각각 166행과 172행 `enddo`에서 닫힌다. [10-15 전수 검증 보완] |
| 176–187 | 시작 시 1행 SwanReadADCGrid 루틴 안. 정상 경로 close(ndsd)(178), 900 return(180). 910은 읽기 오류 msgerr 등급 4와 goto 900(182–183), 950은 예상 밖 파일 끝 msgerr 등급 4와 goto 900(184–185). 마지막 주석·루틴 종료(186–187). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 120–121·133–134: 입력 ii를 배열 인덱스로 사용한 뒤 순차 번호 여부를 경고한다. 이 read 앞에 ii 범위 검사 조건은 없다.
- 133: 삼각형당 꼭짓점 수 위치를 idum으로 읽는다. idum이 3인지 검사하는 조건은 없다.
- 95·114·127·140·180–185: 오류 경로는 900 return으로 이동한다. 해당 경로는 정상 close(ndsd)를 건너뛴다.
