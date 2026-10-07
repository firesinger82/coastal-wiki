---
file: models/SFINCS/raw/source_code/sfincs/source/src/sfincs_read.f90
lines: 303
sha256: fbf8407c9bf6d7d5f3a36ef6b9d83c6fbd1fd835a802b8c58e7a22600751cee0
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# sfincs_read.f90 — 판독 구간 기록

구간은 1행부터 303행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–39 | sfincs_read 모듈·contains·빈 줄(1–4). `read_real_input(fileid,keyword,value,default)`은 키워드·파일 ID, real*4 출력·기본값, 길이 256 문자열·지역 정수를 선언한다(5–14). `value = default` (16), rewind(fileid)(18) 뒤 `do while(.true.)` (20)에서 문자열 한 줄을 iostat=stat로 읽는다(22). `if (stat==-1) exit` (24)로 종료한다. `call read_line(line, keystr, valstr)` (26), `if (trim(keystr)==trim(keyword)) then` (28)이면 valstr을 내부 read로 value에 읽고 exit한다(30–32). 루프·루틴 종료·빈 줄을 포함한다(36–39). |
| 40–78 | `read_real_array_input(fileid,keyword,value,default,nr)`은 길이 256 문자열, nr와 allocatable real*4 출력 배열을 선언한다(40–50). value(nr)를 할당하고 `value = default` (54)로 채운다(52–54). rewind(56) 뒤 `do while(.true.)` (58)에서 iostat로 한 줄을 읽는다(60). `if (stat==-1) exit` (62), `call read_line(line, keystr, valstr)` (64) 뒤 `if (trim(keystr)==trim(keyword)) then` (66)이면 `read(valstr,*)(value(m), m = 1, nr)` (68)로 nr개 값을 읽고 exit한다(70). 루프·루틴 종료·빈 줄을 포함한다(74–78). |
| 79–114 | `read_int_input(fileid,keyword,value,default)`은 정수 출력·기본값과 길이 256 문자열을 선언한다(79–88). `value = default` (90), rewind(92) 뒤 `do while(.true.)` (94)에서 한 줄을 읽는다(96). `if (stat==-1) exit` (98), `call read_line(line, keystr, valstr)` (100), `if (trim(keystr)==trim(keyword)) then` (102)이면 valstr에서 정수 value를 읽고 exit한다(104–106). 루프·루틴 종료·빈 줄을 포함한다(110–114). |
| 115–151 | `read_char_input(fileid,keyword,value,default)`은 문자 출력·기본값과 길이 256 keystr0/keystr/valstr/line을 선언한다(115–125). `value = default` (127), rewind(129) 뒤 `do while(.true.)` (131)에서 한 줄을 읽는다(133). `if (stat==-1) exit` (135), `call read_line(line, keystr, valstr)` (137), `if (trim(keystr)==trim(keyword)) then` (139)이면 value=valstr(141)로 복사하고 exit한다(143). 루프·루틴 종료·빈 줄을 포함한다(147–151). |
| 152–191 | `read_logical_input(fileid,keyword,value,default)`은 logical 출력·기본값과 길이 256 문자열을 선언한다(152–162). `value = default` (164), rewind(166) 뒤 `do while(.true.)` (168)에서 한 줄을 읽는다(170). `if (stat==-1) exit` (172), `call read_line(line, keystr, valstr)` (174), `if (trim(keystr)==trim(keyword)) then` (176)일 때 내부 `if (valstr(1:1) == '1' .or. valstr(1:1) == 'y' .or. valstr(1:1) == 'Y' .or. valstr(1:1) == 't' .or. valstr(1:1) == 'T') then` (178)은 value=.true.(179), `else` (180)는 value=.false.(181)로 설정한다. 일치 키 처리 뒤 exit한다(184). 조건·루프·루틴 종료·빈 줄을 포함한다(186–191). |
| 192–250 | `read_line(line0, keystr, valstr)`은 키·값 문자열을 반환한다는 주석과 선언을 포함한다(192–200). keystr/valstr를 빈 문자열로 초기화하고 `call notabs(line0, line, ilen)` (207)으로 탭을 처리한다(202–207). `jn = index(line, '\r')` (211), `if (jn > 0) then` (213)이면 `line = line(1 : jn - 1)` (217)로 뒤를 제거한다. `line = trim(line)` (223) 뒤 `if (line(1:1) == '#' .or. line(1:1) == '!' .or. line(1:1) == '@') return` (225)이면 반환한다. `j  = index(line, '=')` (229), `if (j == 0) return` (231) 뒤 `keystr = trim(line(1:j-1))` (233), `valstr = trim(line(j+1:))` (235)로 나눈다. `jn = index(valstr, '#')` (239), `if (jn > 0) then` (241)이면 `valstr = trim(valstr(1 : jn - 1))` (243)로 값의 주석을 제거한다. 조건 밖에서 `valstr = adjustl(trim(valstr))` (247)을 수행한다. 루틴 종료·빈 줄을 포함한다(249–250). |
| 251–275 | 빈 줄 뒤 `notabs(INSTR,OUTSTR,ILEN)` 시작(252). 주석은 열을 유지하는 탭 확장, 8문자 간격, 용도, John S. Urban 저자, expand/unexpand 관련 명령을 적는다(253–262). ISO_FORTRAN_ENV의 ERROR_UNIT을 가져오고 입력·출력 문자열 및 ILEN, 문자·위치·길이·루프 정수를 선언한다(264–274). 원문 상수는 `integer,parameter             :: TABSIZE=8 ! assume a tab stop is set every 8th column` (269)이다. |
| 276–303 | 시작 시 252행 notabs 루틴 안. IPOS=1·OUTSTR 공백 초기화(276·280), `lenin=len(INSTR)` (277), `lenin=len_trim(INSTR(1:lenin))` (278), `lenout=len(OUTSTR)` (279)로 길이를 구한다. `do i10=1,lenin` (282)에서 문자를 얻는다(283). `if(ichar(c) == 9)then` (284)은 `IPOS = IPOS + (TABSIZE - (mod(IPOS-1,TABSIZE)))` (285)로 다음 탭 위치로 이동한다. `else` (286) 안의 `if(IPOS > lenout)then` (287)이면 ERROR_UNIT에 overflow를 쓰고 exit한다(288–289). 내부 `else` (290)는 OUTSTR(IPOS:IPOS)에 문자를 복사하고 `IPOS=IPOS+1` (292)을 수행한다. 조건·루프 종료 뒤 `ILEN=len_trim(OUTSTR(:IPOS))  ! trim trailing spaces` (297), return(298)을 수행한다. 루틴·모듈 종료·빈 줄을 포함한다(300–303). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–24·60–62·96–98·133–135·170–172: 다섯 키 판독 루프의 파일 read 종료 검사는 stat==-1이다. 다른 iostat 값에 대한 조건은 이 루프들에 없다. 수치 value 내부 read에는 iostat 인수가 없다(30·68·104).
- 28–32·66–70·102–106·139–143·176–184: 각 키 판독 루틴은 첫 일치 키를 처리한 뒤 exit한다. 이 파일에는 같은 키의 뒤쪽 값을 다시 선택하는 처리가 없다.
- 178–181: logical 판독은 값 문자열 첫 문자만 검사한다. 열거한 다섯 문자 이외의 첫 문자는 모두 .false.로 처리한다.
- 221–225·233·247: 주석은 앞뒤 공백 제거라고 적는다. line과 keystr에는 trim만 적용한다. adjustl은 마지막 valstr 처리에 적용한다.
- 225·239–245: 줄 시작 주석 검사는 #/!/@를 포함한다. 값 문자열의 인라인 주석 제거는 #만 검색한다. 인용부호 여부를 검사하는 분기는 없다.
- 285·287·292·297: 탭 경로는 IPOS를 늘릴 때 lenout을 검사하지 않는다. 일반 문자 경로는 복사 전에 IPOS>lenout을 검사한다. 최종 OUTSTR(:IPOS) 슬라이스에는 min(IPOS,lenout) 제한이 없다.
- 14·50·88·118·125·155·162·200·207: 키 판독 루틴의 j/ilen, 문자 판독의 keystr0/jn, logical 판독의 keystr0, read_line의 ilen 등은 선언 또는 반환값 수신 이후 실행식에서 사용되지 않는다.
