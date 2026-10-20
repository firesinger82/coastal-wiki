---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_int_to_file.cuh
lines: 16
sha256: 6b609b85b342160fc8d43f87345e4ffff39046550a0f06a3344bd0063ad7c848
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_int_to_file.cuh — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_utils.cuh` (3), `<cstdio>`·`<cstring>` (5–6)을 포함한다. 2·4·7–8행의 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 9–16 | CUDA 호스트(host) 지시 `__host__` (9)와 `void write_int_to_file` 원형을 선언한다(10–16). 상수 문자 포인터 `filename`·`dirroot`, 정수 포인터 `d_results`, 상수 정수 값 `array_length`를 받는다(12–15). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
