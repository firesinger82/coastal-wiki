---
file: models/ROMS/raw/source_code/roms/ROMS/Nonlinear/Biology/biology_floats.F
lines: 21
sha256: 7951e1b95b3bad5ad9f274e9f42f8d4ef84303afc20c8f4b4d5568e6c6e77471
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# biology_floats.F — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 1행은 `cppdefs.h`를 끼워 넣는다. NONLINEAR·FLOATS·FLOAT_BIOLOGY가 모두 정의된 전처리 경로를 연다(2). git 식별자·저작권·MIT/X 라이선스 안내(4–9). 생물학적 부유체(biological float)의 행동을 계산한다는 목적 주석(11). 구분선·빈 주석 포함(3·10·12–14). 전처리 원문: `#include "cppdefs.h"` (1); `#if defined NONLINEAR && defined FLOATS && defined FLOAT_BIOLOGY` (2). |
| 15–17 | 시작 시 2행 `#if defined NONLINEAR && defined FLOATS && defined FLOAT_BIOLOGY` 안. FLOAT_OYSTER 조건을 연다(15). 참 경로는 `oyster_floats.h`를 끼워 넣는다(16). 17행은 내부 조건을 닫는다. 포함 파일 내부는 이 판독 범위에 포함하지 않았다. 전처리 원문: `# ifdef FLOAT_OYSTER` (15); `#  include <oyster_floats.h>` (16); `# endif` (17). |
| 18–21 | 시작 시 2행 `#if defined NONLINEAR && defined FLOATS && defined FLOAT_BIOLOGY` 안. 18행 ELSE는 바깥 조건의 불성립 경로이다. 본문 없는 `MODULE biology_floats_mod`와 `END MODULE biology_floats_mod`를 둔다(19–20). 21행은 바깥 조건을 닫는다. 전처리 원문: `#else` (18); `#endif` (21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–21: FLOAT_OYSTER 조건에는 #else가 없다. 바깥 NONLINEAR·FLOATS·FLOAT_BIOLOGY 조건이 참이고 FLOAT_OYSTER가 정의되지 않으면 헤더를 끼워 넣지 않는다. 빈 biology_floats_mod 모듈은 바깥 조건의 불성립 경로에만 있다.
