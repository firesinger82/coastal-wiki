---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/checkerror.F
lines: 77
sha256: 175e95ec802ad8f9bf778a728ab5d5c64b2c9bb9d43fbbced47df78d8c837d86
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# checkerror.F — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 시작 시 열린 전처리 조건 없음. `#include "cppdefs.h"` (1)은 cppdefs.h를 포함한다. `CheckError(ErrorFlag, source, routine, message)` 함수 시작(2). 저작권·MIT/X 라이선스와 원천 코드가 반환한 오류 플래그(error flag)를 검사하고 메시지를 출력한다는 주석(4–14). `#ifdef ESMF_LIB` (16) 안에서 ESMF를 사용한다(17). `#endif` (18). mod_param·mod_parallel·mod_iounits·mod_scalars 사용(19–22), implicit none(24), 정수 ErrorFlag와 길이 가정 문자열 source/routine/message의 intent(in) 선언(28–32). 결과 CheckError는 logical이다(36). 빈 줄·선언 주석도 포함한다. |
| 38–63 | 시작 시 2행 CheckError 함수 안. 시작 시 열린 전처리 조건 없음. 오류 검사 주석(38–47), 기본값 `CheckError=.FALSE.` (44). `SELECT CASE (TRIM(ADJUSTL(source)))` (48)은 source의 앞 공백을 옮기고 뒤 공백을 제거해 선택한다. `CASE ('ROMS')` (50)의 `IF (ErrorFLAG.ne.NoError) THEN` (51)이면 CheckError를 참으로 설정한다(52). `#ifdef ESMF_LIB` (54) 안의 `CASE ('ESMF')` (55)는 `IF (ErrorFlag.ne.ESMF_SUCCESS) THEN` (56)이면 참을 설정한다(57). `#endif` (59). `CASE DEFAULT` (60)는 CheckError를 거짓으로 설정한다(61). END SELECT(63). |
| 64–77 | 시작 시 2행 CheckError 함수 안. 열린 전처리 조건 없음. 오류 보고 주석(64–66). `IF (CheckError) THEN` (67) 안의 `IF (Master) THEN` (68)은 ADJUSTL/TRIM한 routine/source/message를 stdout에 출력한다(69–71). 내부 IF 종료(72), FORMAT 10은 루틴명과 원천명, Error while 메시지를 구성한다(73). 외부 IF 종료·빈 줄·RETURN·함수 종료(74–77). 다른 루틴 호출은 이 구간에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 48–61: source 선택에는 ROMS와 ESMF_LIB 조건 안의 ESMF만 있다. CASE DEFAULT는 ErrorFlag 값과 무관하게 CheckError=.FALSE.를 반환한다. ESMF_LIB가 정의되지 않으면 ESMF라는 source도 CASE DEFAULT로 처리한다.
