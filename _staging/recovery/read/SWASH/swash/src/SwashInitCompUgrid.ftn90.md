---
file: models/SWASH/raw/source_code/swash/src/SwashInitCompUgrid.ftn90
lines: 164
sha256: 3fbb6b7379b75357aec134ce69b26af67c6140b54eabacc763f93a4fe0fd6150
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwashInitCompUgrid.ftn90 — 판독 구간 기록

구간은 1행부터 164행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–78 | `SwashInitCompUgrid ( logcom )` 시작(1). 기관·GPL 3 이상·무보증 머리말(2–28), 저자·2010년 신설(30–36). 비정형 격자(unstructured grid) 설명 배열 초기화 목적(38–40). ocpcomm4·SwashCommdata2/3·m_genarr·m_parall·SwashFlowdata·SwanGriddata 사용(44–50), implicit none(52). `logcom`은 크기 6의 intent(inout) 논리 배열이다(56). 주석상 각 원소의 의미는 1=의미 없음, 2=CGRID 수행, 3=READINP BOTTOM 수행, 4=READ COOR 수행, 5=READ UNSTRUC 수행, 6=s1/u1/v1 할당이다(58–63). i·ient·istat·msgstr 선언(67–71), ient 기본값 `integer, save :: ient = 0 ! number of entries in this subroutine` (68). 구조·원문 안내 주석 포함. [10-15 전수 검증 보완] |
| 79–99 | 시작 시 1행 SwashInitCompUgrid 루틴 안. `call strace (ient,'SwashInitCompUgrid')`(79). i=1..nverts 루프(83), 좌표 이동(offset) 최초 설정 조건 `if ( .not.lxoffs ) then` (84). 최초 꼭짓점 좌표를 xoffs/yoffs에 저장하고 lxoffs를 참으로 설정하며 좌표를 0으로 설정(85–89). `else` (90)에서 이동 식 `xcugrd(i) = real(xcugrd(i) - dble(xoffs))` (91); `ycugrd(i) = real(ycugrd(i) - dble(yoffs))` (92). 루프 종료(94). `call SwashCheckGrid`(98). 대입문·반복문 원문은 `do i = 1, nverts`(83), `xoffs = xcugrd(i)`(85), `yoffs = ycugrd(i)`(86), `lxoffs = .true.`(87), `xcugrd(i) = 0.`(88), `ycugrd(i) = 0.`(89)이다. [10-15 전수 검증 보완] |
| 100–117 | 시작 시 1행 SwashInitCompUgrid 루틴 안. 좌표 범위 초기값 `xcgmin =  1.e9` (102); `ycgmin =  1.e9` (103); `xcgmax = -1.e9` (104); `ycgmax = -1.e9` (105). i=1..nverts 루프(106)에서 최소/최대 갱신 조건 `if ( xcugrd(i) < xcgmin ) xcgmin = xcugrd(i)` (107); `if ( ycugrd(i) < ycgmin ) ycgmin = ycugrd(i)` (108); `if ( xcugrd(i) > xcgmax ) xcgmax = xcugrd(i)` (109); `if ( ycugrd(i) > ycgmax ) ycgmax = ycugrd(i)` (110). 외접 영역(enclosure) 길이 식 `xclen = xcgmax - xcgmin` (115); `yclen = ycgmax - ycgmin` (116). 대입문·반복문 원문은 `do i = 1, nverts`(106)이다. [10-15 전수 검증 보완] |
| 118–144 | 시작 시 1행 SwashInitCompUgrid 루틴 안. istat=0(118). s1 할당 조건 `if ( .not.allocated(s1) ) allocate(s1(ncells), stat = istat)` (119), 성공 조건 `if ( istat == 0 ) then` (120), u1 할당 조건 `if ( .not.allocated(u1) ) allocate (u1(nfaces,kmax), stat = istat)` (121). 오류 조건 `if ( istat /= 0 ) then` (123)이면 메시지·msgerr(4)·return(124–126). s1/u1=0 초기화(128–129), logcom(6)=.true.(130). 다층 조건 `if ( kmax > 1 ) then` (132)에서는 udep 할당 조건 `if ( .not.allocated(udep) ) allocate(udep(nfaces), stat = istat)` (134), 오류 조건 `if ( istat /= 0 ) then` (135)에 메시지·msgerr(4)·return(136–138). udep=0(141). 대입문·반복문 원문은 `istat = 0`(118), `s1 = 0.`(128), `u1 = 0.`(129), `logcom(6) = .true.`(130), `udep = 0.`(141)이다. 첫 오류 경로는 `write (msgstr, '(a,i6)') 'allocation problem: array s1 or u1 and return code is ',istat`(124)로 메시지를 만든다. 이어서 `call msgerr ( 4, trim(msgstr) )`(125)와 `return`(126)을 실행한다. 다층 오류 경로는 `write (msgstr, '(a,i6)') 'allocation problem: array udep and return code is ',istat`(136)로 메시지를 만든다. 이어서 `call msgerr ( 4, trim(msgstr) )`(137)와 `return`(138)을 실행한다. `if ( kmax > 1 ) then`(132)은 ELSE 없이 `endif`(143)에서 닫힌다. [10-15 전수 검증 보완] |
| 145–164 | 시작 시 1행 SwashInitCompUgrid 루틴 안. 직렬 실행(serial run)의 전역 개수 설정이라는 주석(145). 조건 `if ( nvertsg == 0 ) then` (147)이면 nvertsg=nverts·ncellsg=ncells(148–149). 정규 격자(regular grid)용 배열의 빈 배열 할당 조건 `if ( .not.allocated(KGRPGL) ) allocate(KGRPGL(0,0))` (154); `if ( .not.allocated(kgrpnt) ) allocate(kgrpnt(0,0))` (155); `if ( .not.allocated(XGRDGL) ) allocate(XGRDGL(0,0))` (156); `if ( .not.allocated(YGRDGL) ) allocate(YGRDGL(0,0))` (157). 편의상 배열 할당 크기에 쓸 mcgrd=nverts·MCGRDGL=nvertsg(159–162). 루틴 종료(164). 대입문·반복문 원문은 `nvertsg = nverts`(148), `ncellsg = ncells`(149), `mcgrd   = nverts`(161), `MCGRDGL = nvertsg`(162)이다. [10-15 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 56–63·119–130: logcom(6) 설명은 s1·u1·v1 할당 여부라고 적는다. 이 루틴은 s1과 u1을 할당하고 logcom(6)을 참으로 설정한다. 이 파일에는 v1 할당문이 없다.
- 102–105·115–116: 좌표 최솟값은 1.e9, 최댓값은 -1.e9로 초기화한다. 외접 영역 길이는 갱신된 최댓값에서 최솟값을 뺀다.
- 79: strace 호출에는 ltrace 조건이 없다.
