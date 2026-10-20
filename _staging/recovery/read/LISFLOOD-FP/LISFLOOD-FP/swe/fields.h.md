---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/fields.h
lines: 10
sha256: 7680d40582fb796b21f56b4102cb45a269935fcdd1d35c7b094c0f716d34bfdc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# fields.h — 판독 구간 기록

구간은 1행부터 10행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once`(1)와 lisflood 헤더 포함(2) 뒤 천수방정식(shallow water equations) 배열 할당 함수(4–8)와 해제 함수(10)를 선언한다. 할당 함수는 Pars·Arrays 포인터를 받고 해제 함수는 Arrays 포인터만 받는다. 실행문·기본 인수값·조건부 전처리 분기는 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
