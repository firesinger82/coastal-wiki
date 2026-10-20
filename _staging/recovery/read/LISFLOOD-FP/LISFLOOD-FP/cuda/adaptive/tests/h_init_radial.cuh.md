---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/h_init_radial.cuh
lines: 17
sha256: e4286a6f5a80107faf4c2774b63a622a1ce829320f12f14d374a13e019fc6fde
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# h_init_radial.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 7–17 | CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (7)가 붙은 `h_init_radial`을 정의한다(8–13). x·y 좌표를 상수 참조로 받는다(10–11). 반경 식은 `const real r = sqrt(x_int * x_int + y_int * y_int);` (14)다. 원문 삼항 반환식은 `return ( r < C(2.5) ) ? C(2.5) : C(0.5);` (16)다. 반경이 2.5보다 작을 때 수심 2.5, 그 밖에는 0.5를 반환한다. 빈 줄과 함수 종료를 포함한다(15·17). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·16: 반경 계산의 중심은 좌표 원점이다. 반경 경계 2.5와 두 수심 2.5·0.5는 함수 내부의 숫자 상수다.
