---
file: models/SWASH/raw/source_code/swash/src/SwanReadEasymeshGrid.ftn90
lines: 155
sha256: 17fa41af20a23577b52acc9992448c57273d349dc81511586d1d93ea402e420c
reader: codex gpt-6.1-sol
read_date: 2026-10-15
---

# SwanReadEasymeshGrid.ftn90 — 판독 구간 기록

구간은 1행부터 155행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–58 | SwanReadEasymeshGrid 입구(1), 기관·작성자·GPL 3 이상·무보증 머리말(2–29), 2007년 신설 이력(30–36). `<name>.n`에서 꼭짓점(vertex) 좌표, `<name>.e`에서 삼각형 꼭짓점을 읽는다는 목적·방법(38–45). ocpcomm4·SwanGriddata 사용(49–50), implicit none(52). lenfnm·basenm은 intent(in)(56–57). |
| 59–85 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. 파일명·`integer, save     :: ient = 0`(62)·읽기 및 할당 상태·반복 인덱스·파일 장치 번호(unit number)·line·stpnow 선언(61–68), 구조·실행부 표제(70–75). `if (ltrace) call strace (ient,'SwanReadEasymeshGrid')` (76). `filenm = trim(basenm)//'.n'` (80), `ndsd   = 0`(81), `iostat = 0`(82), `call for (ndsd, filenm, 'OF', iostat)` (83), `if (stpnow()) goto 900` (84). [10-15 전수 검증 보완] |
| 86–111 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. nverts 판독(88), `istat = 0`(89), `if(.not.allocated(xcugrd)) allocate (xcugrd(nverts), stat = istat)` (90). `if ( istat == 0 ) then` (91)의 `if(.not.allocated(ycugrd)) allocate (ycugrd(nverts), stat = istat)` (92), `if ( istat == 0 ) then` (94)의 `if(.not.allocated(vmark)) allocate (vmark(nverts), stat = istat)` (95). `if ( istat /= 0 ) then` (97)은 msgerr 등급 4·goto 900(98–99). `do j = 1, nverts` (104)에서 형식 100으로 좌표와 경계 마커(marker)를 판독한다(105). close(ndsd)(110). [10-15 전수 검증 보완] |
| 112–138 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. `filenm = trim(basenm)//'.e'` (114), `ndsd   = 0`(115), `iostat = 0`(116), `call for (ndsd, filenm, 'OF', iostat)` (117), `if (stpnow()) goto 900` (118). ncells 판독(122), `if(.not.allocated(kvertc)) allocate (kvertc(3,ncells), stat = istat)` (123). `if ( istat /= 0 ) then` (124)은 msgerr 등급 4·goto 900(125–126). `do j = 1, ncells` (131)은 형식 200으로 꼭짓점 3개와 남은 문자열 line을 읽는다(132). close(ndsd)(137). [10-15 전수 검증 보완] |
| 139–155 | 시작 시 1행 SwanReadEasymeshGrid 루틴 안. 0부터 세는 꼭짓점 번호를 보정한다는 주석(139), `kvertc = kvertc + 1` (141). 900 return(143), 910·950은 inquire로 파일명을 얻고 읽기 오류 또는 예상 밖 파일 끝 msgerr 등급 4를 호출한 뒤 goto 900(145–150). `100 format((6x,2e22.15,i3))` (152)는 좌표·마커, `200 format((5x,3i5,a))` (153)는 연결성과 나머지 문자열 판독 형식이다. read의 end=950·err=910 처리(88·105·122·132). 루틴 종료(155). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 105·132·141·152–153: 점 번호와 요소 번호 위치는 고정폭으로 건너뛴다. 연결성 배열에는 모든 값을 1 증가시키는 보정을 적용한다.
- 84·99·118·126·143–150: 오류 경로는 900 return으로 이동한다. 이미 열린 파일을 오류 레이블에서 닫는 문장은 없다.
