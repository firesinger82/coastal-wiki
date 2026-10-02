---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/mnemoniciso.F90
lines: 105
sha256: 9ffc8b544491ed7e9d2baec29b70c907bb55c66e1f9559ab6f66fdd0b629e0c7
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# mnemoniciso.F90 — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `mnemiso_module`: ISO C binding과 mnemmodule 사용, implicit none·save. bind(c)인 `b_arraytype` (8): type·btype·rank, name(maxnamelen), units(20), description(1024), `character(kind=c_char), dimension(maxrank) :: dimensions(20)`(16, 엔티티의 `(20)`과 `dimension(maxrank)` 속성이 함께 있음) [10-02 검증 정정: 원문 인용], c_ptr array(10–18). |
| 22–31 | bind(c)인 `carraytype`: rank 주석 0..4, type i/r, btype b/d/2, c_ptr array(24–27). contains 포함. |
| 32–49 | `arrayf2c`: 지역 target `a(3)` (34)에 `a = (/ 1.0d0,  2.0d0, 3.0d0 /)` (35); 입력의 type·btype·rank 복사(36–38). 39–43행은 주석 처리된 조건·c_f_pointer·NULL 지정안이며 실행되지 않음. 현재 실행문은 `arrayf2c%array = c_loc(a)` (44). 원문 조건·식(행 순서): `a = (/ 1.0d0,  2.0d0, 3.0d0 /)` (35); `arrayf2c%type = farray%type` (36); `arrayf2c%btype = farray%btype` (37); `arrayf2c%rank = farray%rank` (38); `arrayf2c%array = c_loc(a)` (44). |
| 50–62 | `stringlength`: assumed-shape 문자 배열. 결과 0으로 시작(53), 전체 루프(54)에서 NULL이면 결과=i(55–57)지만 exit 없음. 루프 밖에서 `stringlength = size(char_array)` (59)로 무조건 덮어쓴다. 원문 조건·식(행 순서): `stringlength = 0` (53); `if (char_array(i) .eq. C_NULL_CHAR) then` (55); `stringlength = i` (56); `end if` (57); `stringlength = size(char_array)` (59). |
| 63–82 | 문자 배열↔문자열 변환 두 함수 초안 전체가 주석(63–81); 실행 정의가 아님. 문자 복사와 NULL 추가안이 보인다. |
| 83–105 | `C_F_STRING` 초안과 내부 C strlen 인터페이스는 모두 주석(84–104). C_ASSOCIATED 검사·C_F_POINTER·dummy_string 연결안도 실행되지 않는다. 마지막 모듈 종료(105). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 34–44: arrayf2c는 실제 farray 데이터 포인터 대신 지역 target a(3)의 주소를 결과에 넣는다. 이 루틴에는 a의 SAVE 선언이 없고 모듈에는 SAVE(5)가 있다; 반환 후 수명은 여기서 판정하지 않는다.
- 55–59: NULL 발견 시 stringlength=i를 설정해도 루프를 나가지 않으며, 루프 뒤 전체 배열 크기로 덮어쓴다.
- 14–16: b_arraytype의 units·dimensions 문자열은 20, description은 1024로 고정되어 있다.
