---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/JSON_Reader/mod_fson_string.f90
lines: 273
sha256: aae41f16577ad45fd3f161bda442be809ba45bc58ca6dc7bbf911c1dcb07e136
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_fson_string.f90 — 판독 구간 기록

구간은 1행부터 273행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | EFDC+·DSI 2021–2024·GPLv2 머리말(1–8). Joseph A. Levin의 2012년 저작권·사용 허가·무보증 조항(9–25). 원래 파일명 string.f95·작성자 josephalevin·2012-03-07 생성 주석·빈 줄(26–33). |
| 34–66 | `mod_fson_string` 모듈 시작·기본 private·공개 문자열(string) 형식 및 생성/소멸/길이/추가/비교/복사 선언(34–39). `integer, parameter :: BLOCK_SIZE = 32` (41). fson_string은 길이 BLOCK_SIZE의 chars, `integer :: index = 0` (45), `type(fson_string), pointer :: next => null()` (46)을 보유한다(43–47). append 일반 인터페이스(generic interface)는 append_chars와 append_string(49–51), copy는 copy_chars(53–55), equals는 equals_string(57–59), length는 string_length(61–63)에 연결한다. contains·빈 줄(65–66). |
| 67–83 | `fson_string_create(chars) result(new)` 선언·선택 chars 인수·결과 포인터(67–72). new를 nullify한 뒤 allocate한다(74–75). `if(present(chars) )then` (78)은 `append_chars(new, chars)`를 호출한다(79). 조건·함수 종료·빈 줄(80–83). |
| 84–104 | 재귀(recursive) `fson_string_destroy` 선언·implicit none·인수(84–90). `if( associated(this) )then` (92) 안에서 `if(associated(this.next) )then` (94)이면 `fson_string_destroy(this.next)`를 호출한다(95). 그 내부 조건 뒤 현재 this를 deallocate·nullify한다(98–99). 조건·루틴 종료·빈 줄(101–104). |
| 105–122 | `allocate_block` 선언·implicit none·this/new 포인터(105–112). `if( .not.associated(this.next) )then` (114)은 new nullify·allocate·this.next 연결(115–117)을 수행한다. 조건·루틴 종료·빈 줄(118–122). |
| 123–138 | `append_string(str1, str2)` 선언·포인터·정수(123–128). `length = string_length(str2)` (130). `do i = 1, length` (132)에서 `append_char(str1, get_char_at(str2, i))`를 호출한다(133). 루프·루틴 종료·빈 줄(134–138). |
| 139–155 | `append_chars(str, c)` 선언·문자 입력·정수(139–145). `length = len(c)` (147). `do i = 1, length` (149)에서 `append_char(str, c(i:i))`를 호출한다(150). 루프·루틴 종료·빈 줄(151–155). |
| 156–175 | 재귀 `append_char` 선언·인수(156–161). `if( str.index .GE. BLOCK_SIZE )then` (163)은 `allocate_block(str)`·`append_char(str.next, c)`를 호출한다(165–166). else(168)는 `str.index = str.index + 1` (170)과 해당 chars 위치의 c 복사(171)이다. 조건·루틴 종료·빈 줄(172–175). |
| 176–199 | `copy_chars(this, to)` 선언·문자 intent(inout)·정수(176–182). `length = min(string_length(this), len(to))` (184). `do i = 1, length` (186)에서 `to(i:i) = get_char_at(this, i)` (187)을 수행한다. `do i = length + 1, len(to)` (191)은 `to(i:i) = ""` (192)로 남은 문자를 채운다. 루프·루틴 종료·빈 줄(193–199). |
| 200–215 | 재귀 `string_clear` 선언·포인터(200–204). `if( associated(this.next) )then` (206)은 `string_clear(this.next)`·deallocate(this.next)·nullify(this.next)(207–209)이다. 조건 뒤 this.index=0(212)을 설정한다. 루틴 종료·빈 줄(214–215). |
| 216–230 | 재귀 정수 함수 `string_length(str) result(count)` 선언(216–220). count에 str.index를 복사(222)한다. `if( str.index == BLOCK_SIZE .and. associated(str.next) )then` (224)은 `count = count + string_length(str.next)` (225)이다. 조건·함수 종료·빈 줄(226–230). |
| 231–245 | 재귀 문자 함수 `get_char_at(this, i) result(c)` 선언·인수(231–236). `if( i .LE. this.index )then` (238)은 현재 블록의 chars(i:i)를 복사(239)한다. else(240)는 `c = get_char_at(this.next, i - this.index)` (241)이다. 조건·함수 종료·빈 줄(242–245). |
| 246–273 | `equals_string(this, other) result(equals)` 선언·포인터·i·equals=false 초기화(246–252). `if(fson_string_length(this) .ne. fson_string_length(other) )then` (254)은 false·return(255–256), `elseif(fson_string_length(this) == 0 )then` (257)은 true·return(258–259)이다. `do i = 1, fson_string_length(this)` (262)의 `if(get_char_at(this, i) .ne. get_char_at(other, i) )then` (263)은 false·return(264–265)이다. 루프 뒤 equals=true(269). 함수·모듈 종료·빈 줄(271–273). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 41–46: 문자 저장 블록 크기는 32로 고정되어 있다. index와 next는 선언 시 초기화한다. chars에는 선언 시 초기값이 없다.
- 34–65·70–82·126–154·159–174·179–196·203–271: 모듈과 나열한 루틴에는 implicit none 문장이 없다. destroy와 allocate_block에는 이를 적는다(89·110).
- 36–39·203–214: string_clear는 기본 private인 모듈의 공개 목록에 없다. 이 파일에는 string_clear를 호출하는 외부 루틴이 없고 자기 재귀 호출만 있다(207).
- 147–151: append_chars는 len(c)로 순회한다. 입력의 뒤쪽 공백을 제외하는 len_trim 호출은 없다.
- 184–193: copy_chars는 목적지 길이로 복사량을 제한한다. 남은 목적지 문자는 빈 문자열 대입으로 채운다. 잘린 원문 길이를 보고하는 출력 인수는 없다.
- 222–226: string_length는 현재 index가 BLOCK_SIZE인 경우에만 연결된 다음 블록의 길이를 더한다.
- 234–242: get_char_at는 i<=this.index만 검사한다. 이 함수에는 i의 하한 검사와 this.next 연결 여부 검사가 없다.
