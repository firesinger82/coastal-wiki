---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo_three_cones.cuh
lines: 43
sha256: bd384d8d2dc97381fb6a49ce975f835f60d8043e9d9d34940c1dfc59aa7660eb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo_three_cones.cuh — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3), `<math.h>` (5), `real.h` (7)를 포함한다. CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (9)가 붙은 `topo_three_cones`를 정의한다(10–15). x·y 좌표는 실수 값 인수다(12–13). 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 17–29 | 시작 시 10–15행 `topo_three_cones` 본문 안. `real z_int = 0;` (17)으로 초기화한다. 원뿔(cone) 중심의 원문 초기화는 `real x_1 = 30;` (19), `real y_1 = 6;` (20), `real x_2 = 30;` (21), `real y_2 = 24;` (22), `real x_3 = C(47.5);` (23), `real y_3 = 15;` (24)다. 반경 상수는 `int rm_1 = 8;` (26), `int rm_2 = 8;` (27), `int rm_3 = 10;` (28)이다. 빈 줄도 포함된다(18·25·29). |
| 30–43 | 시작 시 10–15행 `topo_three_cones` 본문 안. 원문 반경 식은 `real r_1 = sqrt( (x_int - x_1) * (x_int - x_1) + (y_int - y_1) * (y_int - y_1) );` (30), `real r_2 = sqrt( (x_int - x_2) * (x_int - x_2) + (y_int - y_2) * (y_int - y_2) );` (31), `real r_3 = sqrt( (x_int - x_3) * (x_int - x_3) + (y_int - y_3) * (y_int - y_3) );` (32)다. 높이 식은 `real zb_1 = (rm_1 - r_1) / 8;` (34), `real zb_2 = (rm_2 - r_2) / 8;` (35), `real zb_3 = C(0.3) * (rm_3 - r_3);` (36)다. `z_int = max(zb_1 , zb_2);` (38), `z_int = max(z_int, zb_3);` (39), `z_int = max(z_int, C(0.0) );` (40)로 세 높이와 0의 최댓값을 선택한다. `return z_int;` (42), 빈 줄, 함수 종료를 포함한다(33·37·41·43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–28·34–36: 세 원뿔의 중심과 반경은 함수 내부에서 고정한다. 첫 두 높이 식의 분모는 반경 변수 대신 숫자 8이다. 세 번째 높이 식의 계수는 `C(0.3)`이다.
