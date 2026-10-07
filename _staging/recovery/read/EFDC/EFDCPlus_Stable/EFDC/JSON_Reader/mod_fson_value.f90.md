---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/JSON_Reader/mod_fson_value.f90
lines: 319
sha256: 626cc62621b7b212059f8046b616f044a1c9900407252806477202770d145bfc
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_fson_value.f90 — 판독 구간 기록

구간은 1행부터 319행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | EFDC+·DSI 2021–2024·GPLv2 머리말(1–8). Joseph A. Levin의 2012년 저작권·사용 허가·무보증 조항(9–25). 원래 파일명 value_m.f95·작성자 josephalevin·2012-03-07 생성 주석·빈 줄(26–33). |
| 34–85 | `mod_fson_value` 모듈·문자열(string) 모듈 사용·implicit none·기본 private·공개 값(value) 형식 및 생성/소멸/추가/조회/개수/출력 선언(34–42). 형식 상수는 `integer, public, parameter :: TYPE_UNKNOWN = -1` (45), `integer, public, parameter :: TYPE_NULL = 0` (46), `integer, public, parameter :: TYPE_OBJECT = 1` (47), `integer, public, parameter :: TYPE_ARRAY = 2` (48), `integer, public, parameter :: TYPE_STRING = 3` (49), `integer, public, parameter :: TYPE_INTEGER = 4` (50), `integer, public, parameter :: TYPE_REAL = 5` (51), `integer, public, parameter :: TYPE_LOGICAL = 6` (52). fson_value는 name, `integer :: value_type = TYPE_UNKNOWN` (60), logical·integer·8바이트 integer·real·배정밀도(double precision) 필드(61–65), `integer, private :: count = 0` (66), value_string·next·parent·children·tail의 null 포인터(59·67–71)를 보유한다. 1부터 시작하는 인덱스 또는 이름 조회 주석(77). fson_value_get 일반 인터페이스(generic interface)는 get_by_index·get_by_name_chars·get_by_name_string을 등록한다(78–82). contains·빈 줄(84–85). |
| 86–96 | `fson_value_create() result(new)` 선언·결과 포인터(86–90). new를 nullify한 뒤 allocate한다(92–93). 함수 종료·빈 줄(95–96). |
| 97–152 | 재귀(recursive) `fson_value_destroy(this, destroy_next)` 선언·선택 destroy_next·지역변수(97–107). `if( present(destroy_next) )then` (109)은 donext에 인수를 복사(110), else(111)는 `donext = .true.` (112)이다. `if( associated(this) )then` (115) 안에서 `if(associated(this.name) )then` (117)은 fson_string_destroy·nullify(name)(118–119), `if(associated(this.value_string) )then` (122)은 fson_string_destroy·nullify(value_string)(123–124)이다. `if(associated(this.children) )then` (127)은 `do while (this.count > 0)` (128)로 p에 첫 자식을 연결하고 children을 next로 이동한다(129–130). `this.count = this.count - 1` (131), `fson_value_destroy(p, .false.)` 호출(132), 루프 뒤 children nullify(134)이다. `if( (associated(this.next)) .and. (donext) )then` (137)은 next의 재귀 소멸·nullify(138–139)이다. `if(associated(this.tail) )then` (142)은 tail nullify(143)이다. 현재 this deallocate·nullify(146–147). 바깥 조건·루틴 종료·빈 줄(149–152). |
| 153–177 | 연결 리스트(linked list)에 멤버를 추가하는 `fson_value_add(this, member)` 선언·implicit none·인수(153–161). member.parent를 this에 연결한다(164). `if( associated(this.children) )then` (167)은 this.tail.next를 member에 연결(168), else(169)는 this.children을 member에 연결(170)한다. tail을 member에 연결(173)하고 `this.count = this.count + 1` (174)을 수행한다. 루틴 종료·빈 줄(176–177). |
| 178–187 | 정수 함수 `fson_value_count(this) result(count)` 선언·포인터(178–182). count에 this.count를 복사한다(184). 함수 종료·빈 줄(186–187). |
| 188–203 | `get_by_index(this, index) result(p)` 선언·인수·i(188–194). p를 this.children에 연결(196)한다. `do i = 1, index - 1` (198)에서 p를 p.next로 이동한다(199). 루프·함수 종료·빈 줄(200–203). |
| 204–221 | `get_by_name_chars(this, name) result(p)` 선언·문자 name·임시 string 포인터(204–211). `fson_string_create(name)`으로 이름을 변환(214)한다. `get_by_name_string(this, string)` 결과를 p에 연결(216)한다. 임시 string을 `fson_string_destroy`로 해제한다(218). 함수 종료·빈 줄(220–221). |
| 222–248 | `get_by_name_string` 선언·값/이름 포인터·정수(222–228). `if(this.value_type .ne. TYPE_OBJECT )then` (230)은 p nullify·return(231–232)이다. `count = fson_value_count(this)` (235), p=this%children(236). `do i = 1, count` (237)의 `if( fson_string_equals(p%name, name) )then` (238)은 일치 시 return(239)이다. 검사 뒤 p%next로 이동한다(241). 루프 종료 뒤 p nullify(245). 함수 종료·빈 줄(247–248). |
| 249–285 | 재귀 `fson_value_print(this, indent)` 선언·선택 indent·길이 1024 tmp_chars·정수(249–256). `if( present(indent) )then` (258)은 tab에 indent를 복사(259), else(260)는 `tab = 0` (261)이다. `spaces = tab * 2` (264). `select case (this.value_type)` (266)의 `case(TYPE_OBJECT)` (267)는 여는 중괄호를 출력(268)하고 `count = fson_value_count(this)` (269), element=this%children(270)을 설정한다. `do i = 1, count` (271)에서 fson_string_copy로 이름을 복사(273)하고 trim한 이름·따옴표·콜론을 출력한다(275). `fson_value_print(element, tab + 1)` 호출(277), `if( i < count )then` (279)이면 쉼표 출력(280), next 이동(282)이다. 루프 뒤 닫는 중괄호 출력(285). |
| 286–319 | 시작 시 252행 fson_value_print 루틴·266행 select 안. 병렬 `case (TYPE_ARRAY)` (286)는 여는 대괄호 출력(287), `count = fson_value_count(this)` (288), element=this%children(289)이다. `do i = 1, count` (290)에서 `fson_value_print(element, tab + 1)`(292), `if( i < count )then` (294)이면 쉼표 출력(295), next 이동(297)을 수행한다. 루프 뒤 닫는 대괄호 출력(299). `case (TYPE_NULL)` (300)는 null 출력(301)이다. `case (TYPE_STRING)` (302)는 fson_string_copy(303) 뒤 trim한 문자열을 따옴표로 감싸 출력한다(304). `case (TYPE_LOGICAL)` (305)의 `if( this.value_logical )then` (306)은 true 출력(307), else(308)는 false 출력(309)이다. `case (TYPE_INTEGER)` (311)는 value_long_integer 출력(312), `case (TYPE_REAL)` (313)는 value_double 출력(314)이다. select·루틴·모듈 종료·빈 줄(315–319). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 59–71·89–95: name·value_string·값 연결 포인터·value_type·count에는 선언 시 기본값이 있다. value_logical·value_integer·value_long_integer·value_real·value_double에는 선언 시 초기값이 없다. 생성 함수는 nullify와 allocate만 실행한다.
- 109–113·137–147: destroy_next의 기본값은 true이다. 다음 형제의 소멸은 재귀 호출로 수행한다. 부모의 children·tail·count를 갱신하는 문장은 이 루틴에 없다.
- 164–174: 추가 루틴은 member.parent를 설정한다. 이 루틴에는 member.next 초기화, 중복 이름 검사, this/member 연결 여부 검사, this의 형식 검사가 없다.
- 191–200: 인덱스 조회는 children에서 index−1번 next를 따라간다. index 하한·count 상한·중간 포인터 연결 여부 검사가 없다.
- 255·273–275·303–304: 출력용 문자 버퍼(buffer)의 길이는 1024이다. 이름과 문자열 출력은 trim(tmp_chars)를 사용한다. 따옴표·역슬래시·제어문자를 이스케이프(escape)하는 분기는 출력 루틴에 없다.
- 266–315: 출력 select는 object·array·null·string·logical·integer·real을 처리한다. TYPE_UNKNOWN case와 case default는 없다.
