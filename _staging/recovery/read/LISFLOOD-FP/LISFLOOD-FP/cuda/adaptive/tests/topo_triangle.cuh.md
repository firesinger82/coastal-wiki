---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo_triangle.cuh
lines: 28
sha256: 18027511b3cc04d392c0e4da8eedef0b2a5eafe089dbf3924320e2f6293413a6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo_triangle.cuh — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 원문 출처 주석은 `// from https://www.sciencedirect.com/science/article/pii/S0309170815002237` (7)다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 8–17 | CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (8)가 붙은 `topo_triangle`을 정의한다(9–13). 방향 좌표 `x_or_y_int`를 상수 참조로 받는다(11). 경사(slope) 식은 `real slope = C(0.4) / C(3.0);` (14)다. 지반고 초기값은 `real z_int = C(0.0);` (16)다. 빈 줄도 포함된다(15·17). |
| 18–28 | 시작 시 9–13행 `topo_triangle` 본문 안. `if ( x_or_y_int > C(25.5) && x_or_y_int <= C(28.5) )` (18)이면 `z_int = ( x_or_y_int - C(25.5) ) * slope;` (20)다. `else if ( x_or_y_int > C(28.5) && x_or_y_int <= C(31.5) )` (22)이면 `z_int = C(0.4) - ( x_or_y_int - C(28.5) ) * slope;` (24)다. 두 구간은 상승면과 하강면을 만들고 마지막 `else`는 없다. 두 조건 밖 좌표는 16행 초기값을 유지한다. `return z_int;` (27), 빈 줄, 함수 종료를 포함한다(26·28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
