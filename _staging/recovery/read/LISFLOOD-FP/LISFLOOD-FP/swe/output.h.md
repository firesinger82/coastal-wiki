---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/output.h
lines: 55
sha256: 66e1683e1b4fc4419fa6b3913f752337a85d16ea892cb96bf8100105e43aea2e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# output.h — 판독 구간 기록

구간은 1행부터 55행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | `#pragma once`(1), lisflood 헤더 포함(2) 뒤 질량 수지(mass balance) 출력(4–10), 수심 표본 출력(12–19), 속력(speed) 표본 출력(21–28)의 원형을 선언한다. 표본형은 Stage·Arrays 포인터까지 받는다. 기본 인수값·조건부 전처리 분기·실행문은 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2). |
| 30–55 | 해 출력 `write_solution`(30–37), 최대 수심장 출력 `write_max_field`(39–45), 일반장 출력 `write_field`(47–55)의 원형이다. 일반장 출력은 자료 포인터와 ASCII·이진 파일명 접미사, Fnames·States·Pars 포인터를 받는다. 계산식과 조건은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
