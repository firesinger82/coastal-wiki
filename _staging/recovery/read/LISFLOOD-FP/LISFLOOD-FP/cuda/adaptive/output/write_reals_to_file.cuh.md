---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_reals_to_file.cuh
lines: 17
sha256: b01cdbf2a9407821f58e60fde5116b50743e8443e8bdcc6f2898942fa5023af5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_reals_to_file.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_utils.cuh` (3), `<cstdio>`·`<cstring>` (5–6), `real.h` (8)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 10–17 | CUDA 호스트(host) 지시 `__host__` (10)와 `void write_reals_to_file` 원형을 선언한다(11–17). 상수 문자 포인터 `filename`·`dirroot`, 실수 포인터 `d_results`, 상수 정수 참조 `array_length`를 받는다(13–16). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
