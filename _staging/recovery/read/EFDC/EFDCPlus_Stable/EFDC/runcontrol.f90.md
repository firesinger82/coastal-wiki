---
file: models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/runcontrol.f90
lines: 71
sha256: e46f7887f894cf0ec71c5eccffb61eea7f5e2f64fc6cc4777d9ea978a5cda4ed
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# runcontrol.f90 — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 저작권・GNU GPLv2・배포처 머리말(1–8). C 라이브러리 KBHIT/ATEXIT 대체 및 32/64비트 키보드 실행 제어(keyboard run control)를 위한 함수라는 주석(9–11). 2011-03 Paul M. Craig의 64비트 비호환 제거 변경 기록과 빈 줄(12–17). |
| 18–28 | 전처리기(preprocessor) `#ifdef _WIN` (18)이 파일 끝까지 Windows 조건을 연다. `LOGICAL FUNCTION KEY_PRESSED()` (20)는 IFCORE를 사용(23)하고 `KEY_PRESSED = PEEKCHARQQ ( )` (25)의 결과를 반환. 키 입력 여부를 판단한다는 주석(21), 함수 종료・빈 줄(27–28). |
| 29–56 | 시작 시 18행 _WIN 전처리기 참 분기 안. `LOGICAL FUNCTION ISEXIT()` (30), 재개/종료 비교 목적 주석(31), IFCORE와 GLOBAL의 IK4를 사용하고 I1/I2・한 글자 KEY 선언(33–37). `KEY = GETCHARQQ()` (39)로 첫 입력, `I1 = ICHAR(KEY)` (40)로 문자 코드(character code) 저장. 일시 정지・같은 키 종료・다른 키 재개 안내를 출력(42–44). `KEY = GETCHARQQ()` (46), `I2 = ICHAR(KEY)` (47)로 다음 문자 코드 저장. `if( I1 /= I2 )then` (49)이면 ISEXIT=.FALSE.(50), `else` (51)이면 ISEXIT=.TRUE.(52). 조건・함수 종료・빈 줄(53–56). |
| 57–71 | 시작 시 18행 _WIN 전처리기 참 분기 안. `SUBROUTINE QUIT` (58)는 IFCORE를 사용하고 한 글자 KEY 선언(60–61). 장치 6에 TAP ANY KEY TO EXIT EFDC_DSI를 출력(63), `KEY = GETCHARQQ()` (65)로 문자 하나를 받은 뒤 return(67). 루틴 종료(69), `#endif` (70)로 _WIN 조건 종료, 마지막 빈 줄(71). 이 파일에서 QUIT 안에 STOP/ERROR STOP 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–70: KEY_PRESSED・ISEXIT・QUIT 정의는 모두 _WIN 조건 안에 있다. 이 전처리기 분기에는 #else가 없다. 다른 플랫폼 구현은 판독하지 않았다.
- 58–69: QUIT는 종료 안내 후 GETCHARQQ 입력을 받고 return한다. 입력 KEY는 이후 참조하지 않는다. QUIT 자체에는 프로그램 종료문이 없다.
- 20–69: 세 실행 단위는 모두 IFCORE를 사용한다. 세 실행 단위에는 implicit none 문장이 없다.
