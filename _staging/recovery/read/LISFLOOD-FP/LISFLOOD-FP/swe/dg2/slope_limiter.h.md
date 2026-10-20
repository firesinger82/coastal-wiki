---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/dg2/slope_limiter.h
lines: 68
sha256: 9f1e052aefa14fbe3ad59618a35169d152df4bd5112d2409e11698a5e7045b55
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# slope_limiter.h — 판독 구간 기록

구간은 1행부터 68행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | `#pragma once`(1), lisflood·dg2 헤더 포함(2–3), dg2 이름공간(namespace)(5–6) 뒤 `zero_perimeter_slopes`(7–12), 공통 및 x·y 기울기 제한자(slope limiter)(14–36)를 선언한다. 조건부 전처리 분기·계산식·기본 인수값은 없다. 원문: `#pragma once` (1); `#include "../../lisflood.h"` (2); `#include "../dg2.h"` (3). |
| 38–68 | 시작 시 5행 dg2 이름공간 안이다. `limit_slope`(38–49)는 Solver와 최소 수심·격자 간격·세 셀 상수 및 기울기를 받는다. `minmod`(51)는 NUMERIC_TYPE 세 개를 받는다. `stencil_minH_x`·`stencil_minH_y`(53–67)는 Pars·U·i·j를 받아 최소 수심을 반환하는 함수 원형이다. 실행문은 없으며 68행에서 이름공간을 닫는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
