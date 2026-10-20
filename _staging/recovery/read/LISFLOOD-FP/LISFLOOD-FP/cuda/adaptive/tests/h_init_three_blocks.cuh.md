---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/h_init_three_blocks.cuh
lines: 14
sha256: 8e19dbd1a642c3ec348504a9c710c039156a6b62c89d8def9367445dfd39f127
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# h_init_three_blocks.cuh — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 7–14 | CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (7)가 붙은 `h_init_three_blocks`를 정의한다(8–12). 지반고 `z_int`를 상수 참조로 받는다(10). 반환식은 `return C(1.78) - z_int;` (13)다. 수면 높이 상수는 1.78이다. 함수를 닫는다(14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13: 반환식에는 수심을 0 이상으로 제한하는 연산이나 조건이 없다.
