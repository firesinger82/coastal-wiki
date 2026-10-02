---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/iso_c_utils.f90
lines: 70
sha256: b63c219fb525ae5463f47044c1b5f8cc05b134cbfee88ae221357952902a424b
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# iso_c_utils.f90 — 판독 구간 기록

구간은 1행부터 70행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | 빈 첫 행, `iso_c_utils` 모듈·ISO C binding 및 pure 유틸리티 안내. C 문자 배열의 고정 최대 길이 `MAXSTRINGLEN = 1024` (7). 원문 조건·식(행 순서): `integer(c_int), parameter :: MAXSTRINGLEN = 1024` (7). |
| 11–22 | `strlen`: 결과 0으로 시작(14); 1부터 배열 크기까지 검사(15). NULL 문자를 만나면 `strlen = i-1` (17) 후 `exit` (18); 끝까지 없으면 초기값 0 유지. 원문 조건·식(행 순서): `strlen = 0` (14); `if (char_array(i) .eq. C_NULL_CHAR) then` (16); `strlen = i-1` (17); `end if` (19). |
| 23–39 | `strcmp`: 두 지역 문자열 길이는 각각 `strlen(char_array1)`·`strlen(char_array2)` (27–28). 문자열 둘 다 첫 배열에서 변환(30–31). 두 독립 사전식 비교로 -1/1, 그 외 0 반환; `char_array_to_string` 호출. 원문 조건·식(행 순서): `string1 = trim(char_array_to_string(char_array1))` (30); `string2 = trim(char_array_to_string(char_array1))` (31); `strcmp = 0` (32); `if (llt(string1,string2)) strcmp = -1` (33); `if (lgt(string1,string2)) strcmp = 1` (34). |
| 40–50 | `strcpy`: 출력 배열을 공백으로 초기화(45), `do i=1,(strlen(str1) + 1)` (46) 범위에서 입력을 복사하여 NULL 위치까지 포함(47). 원문 조건·식(행 순서): `str2 = ' '` (45); `str2(i) = str1(i)` (47). |
| 51–59 | `char_array_to_string`: 입력은 고정 `MAXSTRINGLEN`, 결과 길이는 `strlen(char_array)` (52–53). 1..문자열 길이 루프에서 각 문자를 복사(55–57). 원문 조건·식(행 순서): `string(i:i) = char_array(i)` (56). |
| 60–70 | `string_to_char_array`: 결과는 고정 `MAXSTRINGLEN` (62). 1..`len_trim(string)` 문자 복사(64–66), `char_array(len_trim(string)+1) = C_NULL_CHAR` (67). 뒤쪽 원소를 채우는 문장은 없음. 모듈 끝 포함. 원문 조건·식(행 순서): `char_array(i) = string(i:i)` (65); `char_array(len_trim(string)+1) = C_NULL_CHAR` (67). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–31: `string1`과 `string2` 모두 `char_array1`에서 변환한다. `char_array2`는 28행 길이 지정에 쓰인다.
- 14–20: `strlen`은 NULL을 찾지 못하면 0을 반환한다.
- 12·24–25·41–42·52·62: C 문자 배열 길이가 1024로 고정되어 있다. 64–67행은 입력 길이에 대한 상한 검사 없이 복사와 NULL 기록을 한다.
- 62–67: `string_to_char_array`는 NULL 이후 결과 배열 원소를 명시적으로 초기화하지 않는다.
