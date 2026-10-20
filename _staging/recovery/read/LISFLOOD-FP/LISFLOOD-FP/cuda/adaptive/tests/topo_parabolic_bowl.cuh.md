---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo_parabolic_bowl.cuh
lines: 14
sha256: a01c6fd5aa60270b27a492bcb1d532f0a65f5dfb6dd9fe8c160dbeceab5d5e4c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo_parabolic_bowl.cuh — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 7–14 | CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (7)가 붙은 `topo_parabolic_bowl`을 정의한다(8–12). 방향 좌표 `x_or_y_int`를 상수 참조로 받는다(10). 원문 반환식은 `return C(0.01) * x_or_y_int * x_or_y_int;` (13)다. 계수 0.01인 포물선(parabola) 지반고를 반환한다. 함수를 닫는다(14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
