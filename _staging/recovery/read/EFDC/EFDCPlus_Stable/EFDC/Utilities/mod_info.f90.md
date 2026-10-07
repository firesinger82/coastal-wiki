---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/mod_info.f90
lines: 108
sha256: 929b4818ee072e4b8f90ba3b4b5676c9732073bcb2ae90d8db479840f96a34bf
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_info.f90 — 판독 구간 기록

구간은 1행부터 108행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | EFDC+·GPLv2 머리말(1–8). INFOMOD·작성자 주석·GLOBAL의 IK4 사용·implicit none·contains·빈 줄(9–15). |
| 16–41 | READSTR는 길이 200의 STR와 입력 UNIT·정수 ISTR/I를 선언한다(16–19). `do while (.TRUE.)` (20)에서 `(A)`로 읽고 err=1000·end=1010을 지정한다(21). `STR = ADJUSTL(STR)` (22), `ISTR = ICHAR(STR(1:1))` (23), I=1 초기화(24). `do while (ISTR == 9)` (25)에서 `I = I+1` (26), `ISTR = ICHAR(STR(I:I))` (27). `SELECT CASE (ISTR)` (29), `CASE (45,46,48:57)  !CHARACTER = -, ., 0:9` (30)은 BACKSPACE UNIT 후 반환한다(31–32). select·루프 종료 및 return(33–35). 오류·파일 끝 레이블은 각각 `call STOPP('READ ERROR!')` (37), `call STOPP('END OF FILE BEFORE EXPECTED!')` (38). 함수 종료·빈 줄(40–41). |
| 42–69 | SKIPCOM은 입력 IUNIT·CC와 선택 인수(optional argument) IUOUT, 길이 250 LINE·COMM 4개를 선언한다(42–47). 기본 주석 문자는 `DATA COMM /'C','c','*','#'/` (48). `do while(.TRUE.)` (50)에서 `(A)`로 읽고 end=999를 지정한다(51). `if( PRESENT(IUOUT)) WRITE(IUOUT,'(A)') LINE` (52). `LINE = ADJUSTL(LINE)` (53), `ISTR = ICHAR(LINE(1:1))` (54), I=1 초기화(55). `do while (ISTR == 9)` (56)에서 `I = I+1` (57), `ISTR = ICHAR(LINE(I:I))` (58). `if( LINE(I:I) == CC .or. ANY(COMM == LINE(I:I)) )then` (60)은 CYCLE(61), `else` (62)는 BACKSPACE 후 exit(63–64). 조건·루프 종료, 999 RETURN, 루틴 종료·빈 줄(65–69). |
| 70–86 | FINDSTR는 STR·SS와 NCOL개의 길이 10 SSN을 선언한다(70–73). 결과 COLM을 0으로 초기화(74), 내부 list-directed read로 SSN(1:NCOL)을 읽고 end=100을 지정한다(75–76). `do M = 1,NCOL` (77)에서 `SSN(M) = ADJUSTL(SSN(M))` (78), `NL = INDEX(SSN(M),SS)` (79). `if( NL > 0 )then` (80)은 COLM에 M을 복사하고 반환한다(81–82). 루프·함수 종료·빈 줄(83–86). |
| 87–108 | NUMCOL은 STR·길이 200 STR1·정수 M/NC/NL을 선언한다(87–90). `STR1 = ADJUSTL(STR)` (92), `NL = LEN_TRIM(STR1)` (93). `if( NL == 0 )then` (94)은 NC=0 후 return(95–96). 조건 밖에서 NC=1(98), `do M = 2,NL` (99). 원문 조건은 `if( STR1(M:M) == '' .and. STR1(M-1:M-1)/='' )then` (100). 참이면 `NC = NC+1` (101). 조건·루프·함수·모듈 종료와 끝 빈 줄(102–108). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·25–28·46·56–59: 두 탭 건너뛰기 루프는 ISTR==9만 검사한다. I가 문자열 길이를 넘는지 확인하는 조건은 이 루프들에 없다.
- 72–84: SSN 선언에는 초기값이 없다. FINDSTR는 내부 read의 end=100 뒤에도 NCOL 전체를 검색한다.
- 99–101: NUMCOL의 구분 조건은 한 문자 슬라이스를 빈 문자 리터럴 ''과 비교한다. 탭을 구분하는 ICHAR==9 조건은 이 함수에 없다.
