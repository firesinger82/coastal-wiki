---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/flux.h
lines: 35
sha256: d8646b5febd22d0858e1ad17ae3f7656e507ac31a3c41c996bdb8a7ac9e9f955
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# flux.h — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | `#pragma once`(1), lisflood 헤더 포함(2), 물리 플럭스(physical flux) x형 원형(4–13)과 y형 원형(15–24)이다. Solver·H·HU·HV를 입력으로 받고 NUMERIC_TYPE 참조 세 개로 결과를 내보낸다. 조건부 전처리 분기·기본 인수값·실행문은 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2). |
| 26–35 | 공통 `physical_flux`의 원형이다. x·y형과 같은 입력·출력 자료형을 사용한다. 분기나 계산식은 선언에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
