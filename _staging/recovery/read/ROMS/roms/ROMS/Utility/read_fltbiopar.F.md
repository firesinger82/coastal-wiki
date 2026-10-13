---
file: models/ROMS/raw/source_code/roms/ROMS/Utility/read_fltbiopar.F
lines: 22
sha256: 88029f421f3a81ca13f1098101016cbe2103c96f5cded1d544b3b1f7efcb51da
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# read_fltbiopar.F — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 시작 시 열린 전처리 조건 없음. `cppdefs.h`를 포함한다(1). FLOATS와 FLOAT_BIOLOGY가 모두 정의된 조건을 연다(2). 저작권·라이선스와 생물 부유체(biological float) 모델 입력 매개변수의 판독·보고 목적을 적은 주석이다(3–15). 이 구간에는 수치 기본값이나 실행식이 없다. 전처리 원문: `#include "cppdefs.h"` (1); `#if defined FLOATS && defined FLOAT_BIOLOGY` (2). |
| 16–18 | 시작 시 전처리 바깥 블록 `#if defined FLOATS && defined FLOAT_BIOLOGY` (2) 안. FLOAT_OYSTER가 정의되면 oyster_floats_inp.h를 끼워 넣는다(16–17). FLOAT_OYSTER 조건을 닫는다(18). 포함 파일 내부는 이 대상 원문에 들어 있지 않다. 전처리 원문: `# if defined FLOAT_OYSTER` (16); `#  include <oyster_floats_inp.h>` (17); `# endif` (18). |
| 19–22 | 시작 시 전처리 바깥 블록 `#if defined FLOATS && defined FLOAT_BIOLOGY` (2) 안. FLOATS·FLOAT_BIOLOGY 결합 조건의 else다(19). 인수와 실행문 없는 `read_FltBioPar` 스텁(stub)을 정의하고 바깥 조건을 닫는다(20–22). 전처리 원문: `#else` (19); `#endif` (22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16–18: FLOAT_OYSTER 조건에는 #else가 없다. 직접 적힌 read_FltBioPar 스텁은 FLOATS·FLOAT_BIOLOGY 결합 조건의 바깥 #else에만 있다(19–21).
