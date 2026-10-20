---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/ScaleChildren.h
lines: 22
sha256: 91533b2b610bb98b492706fc8f1c46815cfea8b39f5ac0d4e2a47edd2ef63f5c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# ScaleChildren.h — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1) 뒤 CUDA 실행시간(runtime) 헤더와 `real.h`를 포함한다(3–5). 전처리 조건 분기는 없다. |
| 7–15 | `ScaleChildrenHW` 구조체(struct)는 `real`형 `child_0`·`child_1`·`child_2`·`child_3`을 선언한다(7–14). 필드 기본값과 메서드는 없다. |
| 16–22 | `ScaleChildrenMW` 구조체는 `ScaleChildrenHW`형 `_0`·`_1x`·`_1y`를 보유한다(16–22). 필드 기본값과 메서드는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
