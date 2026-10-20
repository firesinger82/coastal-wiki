---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/types/real.h
lines: 17
sha256: 40aee7de57d9d488e7e335ac03a3bc86c0fdbd3559946733d11be813f7a937d2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# real.h — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–2 | `#pragma once` (1)와 빈 줄(2)이다. |
| 3–9 | `#if _NUMERIC_MODE == 1` (3)의 참 분기이다. 빈 줄(4) 뒤 `typedef double real;` (5)로 배정밀도(double precision) 자료형을 선택한다. 매크로 원문은 `#define C(x) x` (6), `#define NUM_FRMT "lf"` (7), `#define NUM_FIG  ".15"` (8)이다. `C(x)`는 인수를 그대로 치환한다. 마지막은 빈 줄(9)이다. |
| 10–17 | 시작 시 3행 `#if _NUMERIC_MODE == 1`의 불성립 분기로 들어간다. `#else` (10)와 빈 줄(11) 뒤 `typedef float real;` (12)로 단정밀도(single precision) 자료형을 선택한다. 매크로 원문은 `#define C(x) x##f` (13), `#define NUM_FRMT "f"` (14), `#define NUM_FIG  ".8"` (15)이다. `C(x)`는 토큰 결합(token pasting)으로 `f` 접미사를 붙인다. 빈 줄(16) 뒤 `#endif` (17)로 두 분기를 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 3: `_NUMERIC_MODE`의 정의와 기본값은 이 파일에 없다. 빌드 설정에서 선택하는 실제 값은 이 대상 파일의 원문만으로 확인할 수 없다.
