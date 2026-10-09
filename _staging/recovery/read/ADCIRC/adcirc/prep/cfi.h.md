---
file: models/ADCIRC/raw/source_code/adcirc/prep/cfi.h
lines: 47
sha256: 91ded5da7773d27c5c4061ea28ffa0c1bce3570bcbecb21f29797db042655a68
reader: codex gpt-6.1-sol
read_date: 2026-10-09
---

# cfi.h — 판독 구간 기록

구간은 1행부터 47행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 헤더 가드(header guard) `#ifndef CFI_H` (1) 안에서 `#define CFI_H` (2). `#if (defined(_CRAYMPP))` (4)는 `#  include <fortran.h>` (5). 그 안의 `#  ifndef CRAY_FOR_TYPE` (6)은 기본 선택 `#    define CRAY_FOR_TYPE 1` (7). 바깥 `#else` (9)는 `#  define BSD_FOR_TYPE 1` (10). 플랫폼 분기 종료·빈 줄(11–12). |
| 13–17 | 시작 시 1행 CFI_H 헤더 가드(header guard) 안. `#ifndef PASTE2` (13)이면 `#  define PASTE2(a,b) gEnErIcPaste2(a,b)` (14), `#  define gEnErIcPaste2(a,b) a##b` (15)로 전처리기 토큰 연결(token pasting)을 정의한다. 조건 종료·빈 줄(16–17). |
| 18–25 | 시작 시 1행 헤더 가드 안. `#if (defined(BSD_FOR_TYPE))` (18)은 C 문자 포인터와 별도 길이를 쓰는 Fortran 문자열 인터페이스를 정의한다. 포인터·길이 대입 매크로는 `#  define CP2FCD(cp,len,fcd) do{fcd = cp; PASTE2(fcd,_len)=len;}while(0)` (19). 포인터 변환 `#  define FCD2CP(s) s` (20), 길이 `#  define FCDLEN(s) PASTE2(s,_len)` (21). 선언은 `#  define FDESC(s) char * s; static size_t PASTE2(s,_len)` (22). 인수·프로토타입(prototype)은 `#  define FSTRING(a,comma) comma char * a` (23), `#  define protoFSTRING(a)  char * a` (24), `#  define protoLenFSTRING(a) , size_t PASTE2(a,_len)` (25). 19행 while(0)은 do 블록을 한 번 수행하는 매크로 구성이다. |
| 26–32 | 시작 시 1행 헤더 가드·18행 BSD_FOR_TYPE 분기 안. `#  if (defined(NO_TRAILING_UNDERSCORE) \|\| defined(_IBMR2))` (26)이면 `#    define FORTRAN_NAME(UN,ln) ln` (27). `#  else` (28)는 `#    define FORTRAN_NAME(UN,ln) PASTE2(ln,_)` (29)로 소문자 이름 뒤에 밑줄을 연결한다. 이름 조건·BSD 조건 종료·빈 줄(30–32). |
| 33–42 | 시작 시 1행 헤더 가드 안이며 BSD 조건은 종료됨. 독립 조건 `#if (defined(CRAY_FOR_TYPE))` (33). 문자 기술자(character descriptor) 변환은 `#  define CP2FCD(cp,len,fcd) fcd = _cptofcd(cp,len)` (34), `#  define FCD2CP(s) _fcdtocp(s)` (35). 선언 `#  define FDESC(s) _fcd s` (36), 길이 `#  define FCDLEN(s) _fcdlen(s)` (37). 인수 `#  define FSTRING(a,comma) comma _fcd a` (38), 프로토타입 `#  define protoFSTRING(a) _fcd a` (39), 추가 길이 인수가 없는 `#  define protoLenFSTRING(a)` (40). 외부 이름은 `#  define FORTRAN_NAME(UN,ln) UN` (41). CRAY 조건 종료(42). |
| 43–47 | 시작 시 1행 헤더 가드 안. 빈 줄(43–46), `#endif /* CFI_H */` (47)로 헤더 가드를 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4–11 및 18–42: BSD_FOR_TYPE·CRAY_FOR_TYPE 처리 블록은 독립된 #if이다. _CRAYMPP가 없으면 BSD_FOR_TYPE을 정의하며, 외부에서 CRAY_FOR_TYPE도 정의한 경우를 배제하는 조건은 이 헤더에 없다. 두 블록은 CP2FCD 등 같은 매크로 이름을 정의한다.
- 5 및 22·25: BSD 선언 매크로는 size_t를 사용한다. 이 헤더의 include는 _CRAYMPP 분기의 fortran.h뿐이며 BSD 분기에 size_t용 include는 없다.
- 19 및 34: BSD의 CP2FCD는 do...while(0)으로 포인터·길이를 함께 대입한다. CRAY의 CP2FCD는 _cptofcd 호출 결과를 대입하는 문장으로 정의되며 do 블록 래퍼는 없다.
