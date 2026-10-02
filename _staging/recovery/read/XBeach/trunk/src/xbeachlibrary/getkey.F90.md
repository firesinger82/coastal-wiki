---
file: models/XBeach/raw/source_code/trunk/src/xbeachlibrary/getkey.F90
lines: 134
sha256: bb61b4f99eb19be9231ee7ba7ec1c102a0ed47fc834e53aeffefefac19f89f1e
reader: codex gpt-6.1-sol
read_date: 2026-10-02
---

# getkey.F90 — 판독 구간 기록

구간은 1행부터 134행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `getkey_module`은 파라미터 이름·값을 reflection 방식으로 제공한다는 설명(2–5). `slen`, `maxrank`를 가져오고 기본 private·save, `parameter`, `getkey`, `getkeys`, `getkey_indextype`, `getnkeys` 공개(6–11). `parameter` 형은 type·rank·name·units·description·dimensions 및 문자/실수/정수의 scalar·1차원 pointer를 선언(13–29); rank 주석은 0–4(15). |
| 32–66 | `getkey_indextype`: `getkey.inc` 포함(41), 못 찾을 때 index=-1·type 빈 문자 초기화(42–43). 정수→실수→문자 key 배열을 순서대로 순회하며 `if (integerkeys(i) == key) then`(45), `if (realkeys(i) == key) then`(52), `if (characterkeys(i) == key) then`(59)일 때 각각 해당 index와 'i'/'r'/'c'를 설정하고 즉시 return(46–48·53–55·60–62). 현재 rank 0만 지원한다는 주석(32). |
| 67–103 | `getkey`: 문자·정수·실수 값을 `target, save` 지역변수에 보관(78–80), `getkey.inc` 포함 후 `getkey_indextype` 호출(83–85). 반환값 -1 초기화 후 `if (index .eq. -1 ) return`(87); 통과하면 name·rank=0·type 설정(88–90). `if (type == 'c') then`(91), `elseif (type == 'i') then`(94), `elseif (type == 'r') then`(97)에 따라 각 value 배열의 index 항목을 save 변수에 복사하고 `value%c0/i0/r0` pointer 연결(92–99). 분기 밖에서 반환값 0 설정(101). 같은 형의 후속 호출이 이전 pointer가 참조하는 값을 바꾼다는 주석(76–77). |
| 104–112 | `getnkeys`: `getkey.inc` 포함(109), `n = ncharacterkeys+nintegerkeys+nrealkeys`(110)로 전체 key 수 계산. |
| 113–134 | `getkeys`: allocatable 문자 배열 출력(118), `getkey.inc` 포함(120). `allocate(keys(ncharacterkeys+nintegerkeys+nrealkeys))`(121), 문자→정수→실수 key 순으로 각 구간 복사: `keys(1:ncharacterkeys) = characterkeys(1:ncharacterkeys)` (122), `keys(ncharacterkeys+1:ncharacterkeys+nintegerkeys) = integerkeys(1:nintegerkeys)` (123), `keys(ncharacterkeys+nintegerkeys+1:ncharacterkeys+nintegerkeys+nrealkeys) = realkeys(1:nrealkeys)` (124). 빈 줄을 거쳐 모듈 종료(133–134). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 76–80·92–99: 반환 pointer는 형별 단일 `save` 변수에 연결된다. 같은 형의 다음 호출은 이전 반환 pointer가 참조하는 저장소에 값을 다시 쓴다.
- 13–28·88–99: 형에는 units·description·dimensions와 1차원 pointer가 있으나 이 파일의 `getkey`는 name·rank·type 및 선택된 scalar pointer만 설정한다. 나머지 pointer를 nullify하는 문장은 없다.
