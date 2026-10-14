---
file: models/SWASH/raw/source_code/swash/src/SwanReadTriangleGrid.ftn90
lines: 178
sha256: 1fad88c6417e7f164062ea3ade95a3e70c5cb08e2c979ae5d5ff1f40cd441783
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanReadTriangleGrid.ftn90 — 판독 구간 기록

구간은 1행부터 178행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–58 | SwanReadTriangleGrid 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). `<name>.node`에서 꼭짓점(vertex) 좌표, `<name>.ele`에서 삼각형 꼭짓점을 읽는다는 목적·방법(38–45). ocpcomm4·SwanGriddata 사용(49–50), implicit none(52). lenfnm·basenm은 intent(in)(56–57). |
| 59–92 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. 파일명·`integer, save     :: ient = 0`(62)·읽기 및 할당 상태·인덱스·속성 수 nattr·경계 마커(marker) 수 nbmark·차원 ndim·요소당 점 수 nnodes·더미(dummy)값·line·stpnow 선언(61–75). nbmark는 0 또는 1, ndim은 2여야 한다는 선언 주석(69–70). 구조·실행부 표제(77–82), `if (ltrace) call strace (ient,'SwanReadTriangleGrid')` (83). `filenm = trim(basenm)//'.node'` (87), `ndsd   = 0`(88), `iostat = 0`(89), `call for (ndsd, filenm, 'OF', iostat)` (90), `if (stpnow()) goto 900` (91). [10-15 전수 검증 보완] |
| 93–115 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. nverts·ndim·nattr·nbmark 판독(95), `istat = 0`(96). `if(.not.allocated(xcugrd)) allocate (xcugrd(nverts), stat = istat)` (97), `if ( istat == 0 ) then` (98)의 `if(.not.allocated(ycugrd)) allocate (ycugrd(nverts), stat = istat)` (99), `if ( istat == 0 ) then` (101)의 `if(.not.allocated(vmark)) allocate (vmark(nverts), stat = istat)` (102). `if ( istat /= 0 ) then` (104)은 msgerr 등급 4·goto 900(105–106). `if ( nbmark == 0 ) then` (111)은 경계 마커 필수 오류와 goto 900(112–113)이다. [10-15 전수 검증 보완] |
| 116–133 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. `if ( nattr == 0 ) then` (118)의 `do j = 1, nverts` (119)은 ii·좌표·vmark를 읽는다(120). `if ( ii/=j ) call msgerr ( 1, 'numbering of vertices is not sequential in Triangle file '//filenm )` (121). `else` (123)의 `do j = 1, nverts` (124)은 ii·좌표·rdum·vmark를 읽는다(125). `if ( ii/=j ) call msgerr ( 1, 'numbering of vertices is not sequential in Triangle file '//filenm )` (126). 분기 종료(128), close(ndsd)(132). |
| 134–150 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. `filenm = trim(basenm)//'.ele'` (136), `ndsd   = 0`(137), `iostat = 0`(138), `call for (ndsd, filenm, 'OF', iostat)` (139), `if (stpnow()) goto 900` (140). ncells·nnodes·nattr 판독(144), `if(.not.allocated(kvertc)) allocate (kvertc(3,ncells), stat = istat)` (145). `if ( istat /= 0 ) then` (146)은 msgerr 등급 4·goto 900(147–148). [10-15 전수 검증 보완] |
| 151–178 | 시작 시 1행 SwanReadTriangleGrid 루틴 안. `if ( nnodes == 3 .and. nattr == 0 ) then` (153)의 `do j = 1, ncells` (154)은 ii와 세 꼭짓점을 읽는다(155). `if ( ii/=j ) call msgerr ( 1, 'numbering of triangles is not sequential in Triangle file '//filenm )` (156). `else` (158)의 `do j = 1, ncells` (159)은 같은 세 꼭짓점 뒤 line을 읽는다(160). `if ( ii/=j ) call msgerr ( 1, 'numbering of triangles is not sequential in Triangle file '//filenm )` (161). close(ndsd)(167), 900 return(169), 910·950은 inquire와 읽기 오류·예상 밖 파일 끝 msgerr 등급 4·goto 900(171–176). read는 end=950·err=910을 사용한다(95·120·125·144·155·160). 마지막 주석·루틴 종료(177–178). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70·95–128: ndim을 입력으로 읽지만 ndim==2 검사 조건은 없다. nattr가 비영이면 rdum 한 개만 읽는다.
- 120–126·155–161: 입력 ii를 배열 인덱스로 사용한 뒤 순차 번호 여부를 경고한다. read 앞의 인덱스 범위 검사는 없다.
- 144–163: nnodes·nattr가 기본 조건과 다르면 else에서 세 꼭짓점과 문자열 line을 읽는다. nnodes가 3인지 강제하는 오류 분기는 없다.
- 91·106·113·140·148·169–176: 오류 경로는 900 return으로 이동한다. 오류 레이블에는 close가 없다.
