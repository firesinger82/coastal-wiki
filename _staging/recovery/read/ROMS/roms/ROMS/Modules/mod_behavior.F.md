---
file: models/ROMS/raw/source_code/roms/ROMS/Modules/mod_behavior.F
lines: 35
sha256: d0c48946d0297e46fe11e9c33de1e8601d4af42ecb16381ff605bcea489f7494
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# mod_behavior.F — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | `cppdefs.h`를 끼워 넣는다(1). 저작권·MIT/X 형식 라이선스 안내(2–8). 주석은 라그랑주 표류체(Lagrangian drifters)의 생물 행동(biological behavior) 매개변수를 선언하고 대개 입력 스크립트에서 읽는다고 설명한다(10–15). *.h 파일은 ROMS/Nonlinear/Biology에 있으며 프로젝트에서 사용자 정의 파일을 선택할 수 있도록 꺾쇠 포함을 사용한다는 주석이다(17–20). 머리말 종료와 빈 줄을 포함한다(21–24). 전처리 원문: `#include "cppdefs.h"` (1). |
| 25–31 | FLOATS와 FLOAT_BIOLOGY가 모두 정의되고 FLOAT_OYSTER가 정의되면 `oyster_floats_mod.h`를 끼워 넣는다(25–27). 내부 else는 내용 없는 mod_behavior 모듈을 선언하고 종료한다(28–30). 내부 전처리 조건을 닫는다(31). 포함 파일 내부의 매개변수·기본값·루틴은 이 원문에 나타나지 않는다. 전처리 원문: `#if defined FLOATS && defined FLOAT_BIOLOGY` (25); `# if defined FLOAT_OYSTER` (26); `#  include <oyster_floats_mod.h>` (27); `#  else` (28); `# endif` (31). |
| 32–35 | 시작 시 `#if defined FLOATS && defined FLOAT_BIOLOGY` (25) 안. FLOATS와 FLOAT_BIOLOGY의 바깥 조건이 불성립하는 else에서 내용 없는 mod_behavior 모듈을 선언하고 종료한다(32–34). 바깥 조건을 닫는다(35). 전처리 원문: `#else` (32); `#endif` (35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
