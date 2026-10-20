---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/hll.h
lines: 44
sha256: 8b85a466efa9b54eee0603719a4fa6bb23125eef517b24cb2c3a9a4c6db9f119
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# hll.h — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | `#pragma once`(1)와 lisflood 헤더 포함(2) 뒤 HLL 리만 해법(Harten–Lax–van Leer Riemann solver)의 x형(4–16), y형(18–30) 원형을 선언한다. 양쪽 상태 여섯 개와 Solver 포인터를 입력으로, 플럭스 참조 세 개를 출력으로 받는다. 조건부 전처리 분기·기본 인수값·실행문은 없다. 원문: `#pragma once` (1); `#include "../lisflood.h"` (2). |
| 32–44 | 공통 `HLL` 원형이다. x·y형과 같은 입력·출력 자료형을 사용한다. 계산식·조건은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
