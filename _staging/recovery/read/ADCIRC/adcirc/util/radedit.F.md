---
file: models/ADCIRC/raw/source_code/adcirc/util/radedit.F
lines: 75
sha256: 0c7a53e0c2a4ce7c21d4936ef1f8c0b498b0adad700b6080fc37b5247bbdb3a2
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# radedit.F — 판독 구간 기록

구간은 1행부터 75행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | ADCIRC 명칭·저작권·LGPL 3 이상·무보증 머리말과 구분 주석이다. |
| 20–44 | radedit 프로그램과 implicit none(20–22). 격자(grid) 크기·입출력 장치·단계 수·I/O 상태와 카운터를 선언한다(23–25). `character(80) :: fnameIn, fnameOut, buf` (26), `character(40) :: buf` (27)로 문자열을 선언한다. real(8) allocatable rs와 x/y를 선언한다(29–31). `if (COMMAND_ARGUMENT_COUNT() < 2) then` (33)이면 사용법 출력 후 stop이다. GET_COMMAND_ARGUMENT로 입력 파일명과 단계 수 문자열을 받는다(39–40). buf를 i10 형식으로 nsteps에 읽고 안내를 출력한다(42–44). |
| 45–62 | 시작 시 20행 radedit 프로그램 안. 입력 장치 10과 출력 장치 11을 연다(46–52). 출력 이름은 입력 이름 뒤에 ".new"를 붙인다(49). ni·nj·x·y와 문자열 buf를 list-directed 형식으로 읽어 같은 값들을 출력한다(55–59). rs를 (2,ni,nj)로 할당한다(61). 빈 줄을 포함한다. |
| 63–75 | 시작 시 20행 radedit 프로그램 안. `do istep = 1, nsteps` (63)의 `do j = nj, 1, -1` (65)에서 `read(in,*, iostat=ios) ((rs(k,i,j), k= 1,2), i = 1,ni)` (66)로 두 성분을 읽는다. 별도 `do j = nj, 1, -1` (69)에서 `write(out,1000) ((rs(k,i,j), k= 1,2), i = 1,ni)` (70)로 같은 역순 j 자료를 쓴다. 단계 루프 종료(73). 출력 형식은 `1000 format(1x,1p5e15.7)` (74)이다. 프로그램 종료(75). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 26–27: buf를 character(80) 선언과 character(40) 선언에 모두 적고 있다.
- 66–73: 자료 read는 iostat=ios를 받는다. 이후 ios를 검사하는 조건문은 없다.
- 42·55–63: nsteps·ni·nj를 입력에서 받는다. 단계 루프 및 rs 할당 전에 양수 여부나 입력 자료 개수를 확인하는 문장은 없다.
