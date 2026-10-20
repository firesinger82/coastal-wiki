---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/h_init_parabolic_bowl.cuh
lines: 18
sha256: be8880ab61d6ec6d364a5347707dd0a7e9f5af0129e7932de1fc44e68e549ddf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# h_init_parabolic_bowl.cuh — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 빈 줄도 포함된다. 원문 주석은 `// inspired from https://core.ac.uk/download/pdf/196597598.pdf` (7)다. 조건부 전처리 분기는 없다. |
| 8–18 | CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (8)가 붙은 `h_init_parabolic_bowl`을 정의한다(9–14). 방향 좌표 `x_or_y_int`와 지반고 `z_int`를 상수 참조로 받는다(11–12). 수면 높이 식은 `const real eta = C(0.2) * x_or_y_int + C(10.0);` (15)다. `return max(C(0.0), eta - z_int);` (17)로 수심에 0 하한을 적용한다. 빈 줄과 함수 종료를 포함한다(16·18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
