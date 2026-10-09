---
file: models/ADCIRC/raw/source_code/adcirc/src/hashtable.F90
lines: 166
sha256: a4979b2aefc434a90af4783c953b8d285a40fdd388e61efff4a1f87904a7c06d
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# hashtable.F90 — 판독 구간 기록

구간은 1행부터 166행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | ADCIRC 저작권과 LGPL 3 이상·무보증 머리말(1–19). 정수 키를 정수 값에 대응시키는 해시 테이블(hash table)의 목적을 적는다(21–26). 주석은 나머지 연산(modulus)으로 해시 값을 계산하고 연결 리스트(linked list)로 충돌(collision)을 처리한다고 적는다(27–28). 작성자·소속·2017년 표기와 구분 주석(30–34). |
| 35–55 | hashtable 모듈 시작과 implicit none(35–36). 기본 private이며 ipair·dict·close_dict·add_ipair·find를 공개한다(38–43). ipair 형식은 정수 key/value, 논리 empty, 다음 ipair를 가리키는 포인터(pointer) next를 선언한다(45–52). 이 형식 선언에는 필드 기본값이 없다. 빈 줄·contains(53–55). |
| 56–74 | dict(ipair_array, num_ipairs)의 목적 주석·인수와 i 선언(56–63). num_ipairs 크기의 배열을 할당한다(65). `do i = 1, num_ipairs` (66)에서 key/value를 0, empty를 .true.로 초기화하고 next를 nullify한다(67–70). 루프·루틴 종료와 빈 줄(71–74). 이 루틴에는 num_ipairs의 범위 검사문이 없다. |
| 75–113 | add_ipair(d, key, value)의 목적 주석·인수·index와 current_ipair 선언(75–85). 버킷(bucket) 인덱스 식은 `index = 1 + modulo(key - 1, size(d))` (88). `if (d(index)%empty) then` (91)의 참 분기는 key/value를 복사하고 empty를 .false.로 바꾼다(92–94). `else` (95)에서는 current_ipair를 d(index)에 연결한다(96). `do` (97) 안의 `if (.not. associated(current_ipair%next)) then` (98)이 참이면 다음 노드를 할당·연결하고 key/value·empty·next를 설정한 뒤 exit한다(99–105). `else` (106)이면 다음 노드로 이동한다(107). 조건·루프·루틴 종료와 빈 줄(108–113). |
| 114–144 | find(d, key)의 목적 주석·정수 반환형·인수·포인터·index 선언(114–122). 인덱스 식은 `index = 1 + modulo(key - 1, size(d))` (125). current_ipair를 d(index)에 연결한다(128). `do` (129)에서 `if (key == current_ipair%key) then` (130)이면 해당 value를 반환하고 exit한다(131–132). `else` (133)의 `if (associated(current_ipair%next)) then` (134)이 참이면 next로 이동한다(135). `else` (136)이면 반환 기본값 `find = 0` (137)을 설정하고 exit한다(138). 조건·루프·함수 종료와 빈 줄(139–144). |
| 145–157 | close_dict(d)의 해제 목적 주석·인수·i 선언(145–151). `do i = 1, size(d)` (152)에서 `if (associated(d(i)%next)) call remove_ipair(d(i)%next)` (153)으로 연결 노드를 먼저 해제한다. d 자체를 deallocate하고 루틴을 끝낸다(155–156). 빈 줄(157). |
| 158–166 | 비공개 재귀 루틴(recursive subroutine) remove_ipair(i)의 주석·선언과 포인터 인수(158–161). `if (associated(i%next)) call remove_ipair(i%next)` (162)으로 다음 노드부터 재귀 해제한다. 현재 i를 deallocate한다(163). 루틴 종료·빈 줄·모듈 종료(164–166). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 47–52·65–70·99–104: ipair 형식 선언에는 기본값이 없다. dict는 배열 요소의 모든 필드를 초기화한다. add_ipair는 새 연결 노드의 모든 필드를 설정한다.
- 59–71·88·125·152–155: dict에는 num_ipairs>0 검사나 기존 할당 상태 검사가 없다. add_ipair·find는 size(d)를 modulo의 두 번째 인수로 사용한다. add_ipair·find·close_dict에는 allocated(d) 검사문이 없다.
- 91–109·130–132: add_ipair의 충돌 경로에는 기존 key와 새 key를 비교하는 문장이 없다. 새 쌍은 연결 리스트 끝에 추가된다. find는 순회 중 처음 일치한 key의 value를 반환한다.
- 67–69·128–140: dict는 빈 버킷의 key를 0으로 설정한다. find는 empty를 검사하지 않고 key를 먼저 비교한다. 빈 버킷에서 key=0이 일치하면 초기 value=0을 반환한다.
- 83·93·102·131·137: value 인수에는 0을 제외하는 검사문이 없다. find는 일치한 value를 그대로 반환한다. 찾지 못한 경우에도 0을 반환한다. 별도 발견 여부 반환값은 없다.

