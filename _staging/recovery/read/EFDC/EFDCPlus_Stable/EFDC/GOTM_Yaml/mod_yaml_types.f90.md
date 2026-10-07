---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/GOTM_Yaml/mod_yaml_types.f90
lines: 578
sha256: 30cb6b708c6493b98fcdab63e2ef49fec8800e0968a17dfecb85dd222b8c4469
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# mod_yaml_types.f90 — 판독 구간 기록

구간은 1행부터 578행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–47 | Fortran-YAML 파서(parser) 소개·저장소·저작권·GNU GPL·무보증 머리말(1–15). yaml_types 모듈은 implicit none·기본 private·공개 노드/스칼라(scalar)/null/오류/dictionary/list 형식을 지정한다(17–25). 상수 원문은 `integer,parameter :: string_length = 1024` (27), `integer,parameter :: real_kind = kind(1.0d0)` (28)이다. 추상 type_node의 path 기본값은 빈 문자열이다(30–31). `#ifdef USE_YAML` (32) 안의 deferred dump, set_path·finalize를 선언하고 node_dump의 추상 interface를 정의한다(33–46). 빈 줄(47)도 포함한다. |
| 48–94 | 시작 시 17행 모듈 선언부 안. type_scalar의 string은 길이 string_length·초기값 ''이며 USE_YAML 아래 dump·논리/정수/실수 변환을 선언한다(48–57). type_null은 dump를 갖는다(59–64). 키/값 쌍은 빈 key·null value·accessed=.false.·null next를 선언한다(66–71). type_dictionary는 null first와 USE_YAML 아래 get 계열·set 계열·dump·flatten·접근 플래그 초기화·경로 설정·해제 결합 루틴(type-bound procedure)을 선언한다(73–93). |
| 95–131 | 시작 시 17행 모듈 선언부 안. type_list_item의 node/next와 type_list의 first는 null이며 list는 append·dump·set_path·finalize를 갖는다(95–109). type_error는 길이 string_length의 message를 선언하고 기본값을 지정하지 않는다(111–113). `#ifdef USE_YAML` (115)·contains(116) 뒤 node_finalize는 실행문 없이 끝난다(118–120). dictionary_reset_accessed는 `do while (associated(pair))` (126)에서 각 pair의 accessed를 .false.로 설정한다(127). 자식 재귀 호출은 없다. |
| 132–183 | dictionary_get은 반환 포인터를 null로 시작한다(132–140). `do while (associated(pair))` (141)·`if( pair%key==key) exit` (142)로 키를 찾는다. `if( associated(pair) )then` (145)이면 value를 연결하고 accessed=.true.를 설정한다(146–147). dictionary_set의 `if( .not.associated(self%first) )then` (158)은 첫 쌍을 할당한다(160–161). `else` (162)의 `do while (associated(pair%next))` (165)·`if( pair%key==key) exit` (166)로 같은 키 또는 마지막 쌍을 찾는다. `if( .not.pair%key==key )then` (169)이면 다음 쌍을 할당하고 `else` (174)는 기존 pair%value를 deallocate한다(172–175). 키 복사·값 포인터 연결 뒤 루틴을 끝낸다(180–182). |
| 184–240 | dictionary_set_string은 scalar 노드를 할당하고 문자열을 복사한 뒤 self%set을 호출한다(184–195). value_dump는 trim(string)을, null_dump는 'null'을 출력한다(197–207). 재귀 dictionary_dump는 first=.true.·pair=first 뒤 `do while (associated(pair))` (217)를 돈다. `if( first )then` (218)은 first=.false., `else` (220)는 들여쓰기 출력이다(219·221). select type의 dictionary/list 분기는 키·콜론 출력 뒤 각각 dump(unit,indent+2)를 호출한다(224–232). class default는 같은 행 키·값 출력과 dump(unit,indent+len_trim(pair%key)+2) 호출이다(233–235). 루프·루틴·빈 줄까지 포함한다(237–240). |
| 241–298 | dictionary_flatten은 `do while (associated(pair))` (249)의 select type에서 scalar를 target%set_string(prefix//trim(key),string)으로 복사하고 dictionary를 prefix//trim(key)//'/'로 재귀 flatten한다(250–254). scalar_to_logical·scalar_to_integer·scalar_to_real은 각 default를 value에 복사하고 문자열 내부 파일(internal file)을 목록 지향(list-directed) read로 변환한다(260–295). 선택적 성공 반환 원문은 `if( present(success)) success = (ios == 0)` (270), `if( present(success)) success = (ios == 0)` (283), `if( present(success)) success = (ios == 0)` (296)이다. 각 함수는 iostat를 받지만 별도 오류 객체를 만들지 않는다. |
| 299–350 | node_set_path는 경로를 복사한다(299–303). dictionary_set_path는 자신 경로를 복사하고 `do while (associated(pair))` (312)에서 `call pair%value%set_path(trim(self%path)//'/'//trim(pair%key))` (313)을 재귀 호출한다. dictionary_get_scalar는 error·scalar를 null로 하고 self%get을 호출한다(318–329). `if( required.and..not.associated(node) )then` (330)이면 오류 객체·키 부재 메시지이다(331–332). `if( associated(node) )then` (334)의 select type은 scalar를 연결하고 null/dictionary/list이면 오류 객체와 해당 형식 메시지를 만든다(335–346). select·조건·함수 종료·빈 줄(347–350). |
| 351–409 | dictionary_get_dictionary는 error/dictionary=null·self%get 뒤 `if( required.and..not.associated(node) )then` (363)이면 키 부재 오류를 만든다(364–365). `if( associated(node) )then` (367)의 select type에서 null은 새 빈 dictionary 할당·path 복사, dictionary는 기존 노드 연결, class default는 형식 오류이다(368–376). dictionary_get_list도 error/list=null·self%get 뒤 `if( required.and..not.associated(node) )then` (393)은 키 부재 오류이다(394–395). `if( associated(node) )then` (397)의 select type에서 null은 새 빈 list 할당, list는 기존 노드 연결, class default는 형식 오류이다(398–405). null 목록에는 경로 복사 문장이 없다. |
| 410–445 | dictionary_get_string의 기본값·결과 복사는 `if( present(default)) value = default` (419), `if( associated(node)) value = node%string` (421)이다. get_scalar에는 required=.not.present(default)를 넘긴다(420). dictionary_get_logical의 `if( present(default)) value = default` (434) 뒤 같은 required 인수로 get_scalar를 호출한다(435). `if( associated(node) )then` (436)에서 `value = node%to_logical(value,success)` (437), `if( .not.success )then` (438)이면 Boolean 해석 불가 오류 객체·메시지를 만든다(439–441). |
| 446–487 | dictionary_get_integer의 `if( present(default)) value = default` (456) 뒤 get_scalar(key,.not.present(default),error)를 호출한다(457). `if( associated(node) )then` (458)의 식은 `value = node%to_integer(value,success)` (459)이고 `if( .not.success )then` (460)은 정수 해석 불가 오류 객체·메시지이다(461–462). dictionary_get_real은 `if( present(default)) value = default` (477) 뒤 같은 required 규칙으로 get_scalar를 호출한다(478). `if( associated(node) )then` (479)의 식은 `value = node%to_real(value,success)` (480), `if( .not.success )then` (481)은 실수 해석 불가 오류이다(482–483). |
| 488–523 | dictionary_finalize는 `do while (associated(pair))` (493)에서 next를 보존하고 값 finalize·값/쌍 deallocate를 실행한다(494–498). 종료 후 first를 null로 한다(500). list_append의 `if( .not.associated(self%first) )then` (509)은 첫 항목을 할당하고 node를 연결한다(511–512). `else` (513)의 `do while (associated(item%next))` (516)는 마지막 항목을 찾고 다음 항목을 할당·node 연결한다(519–520). 전달된 node를 복제하는 문장은 없다. |
| 524–543 | list_dump는 first=.true.·item=first 뒤 `do while (associated(item))` (532)를 돈다. `if( first )then` (533)은 first=.false., `else` (535)는 들여쓰기를 출력한다(534·536). '- ' 출력 뒤 `call item%node%dump(unit,indent+2)` (539), 다음 항목 이동·루프·루틴 종료(540–542). 빈 줄(543)도 포함한다. |
| 544–561 | list_set_path는 길이 6 strindex와 inode를 선언한다(544–549). 경로 복사·inode=0·item=first 뒤 `do while (associated(item))` (554)에서 i0로 inode를 문자열화한다(555). 경로 호출 원문은 `call item%node%set_path(trim(self%path)//'['//trim(strindex)//']')` (556)이다. `inode = inode + 1` (557) 뒤 다음 항목으로 이동한다(558). 이 경로 인덱스는 0부터 시작한다. |
| 562–578 | list_finalize는 `do while (associated(item))` (567)에서 next를 보존하고 노드 finalize·노드/항목 deallocate·다음 항목 이동을 수행한다(568–572). first를 null로 하고 루틴을 끝낸다(574–575). `#endif` (576)·빈 줄·yaml_types 모듈 종료(578)까지 포함한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27·31·49·67·112: 노드 경로·스칼라 문자열·dictionary 키·오류 메시지는 길이 1024로 고정되어 있다.
- 169–181·488–501: dictionary_set의 기존 키 교체는 pair%value를 직접 deallocate한다. dictionary_finalize의 해제는 먼저 해당 값의 finalize를 호출한다. 교체 분기에는 finalize 호출이 없다.
- 122–130: dictionary_reset_accessed는 현재 dictionary의 쌍 플래그만 초기화한다. 자식 dictionary/list의 플래그를 재귀 초기화하는 호출은 없다.
- 249–255: dictionary_flatten의 select type에는 scalar와 dictionary 분기만 있다. list·null·class default 분기는 없다.
- 369–376·399–405: null에서 새 dictionary를 만들 때는 원본 path를 복사한다. null에서 새 list를 만들 때는 path를 복사하지 않는다.
- 419–421·434–437·456–459·477–480: 기본값이 없는 getter 경로에서는 반환 value를 초기화하는 문장이 변환/반환 전에 없다. 논리·정수·실수 getter는 그 value를 변환 루틴의 default 인수로 넘긴다.
- 549·552–557: list_set_path의 문자열 인덱스 버퍼 길이는 6이다. 인덱스는 0부터 시작하며 문자열을 쓴 뒤에 1을 더한다.
