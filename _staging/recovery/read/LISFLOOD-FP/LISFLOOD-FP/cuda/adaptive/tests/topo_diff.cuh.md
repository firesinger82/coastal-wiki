---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo_diff.cuh
lines: 26
sha256: 73a0ec36eeae8e77e76ec264612c806aa6edfff5f7952392150feff659cb9927
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo_diff.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_runtime.h` (3)와 `real.h` (5)를 포함한다. 원문 출처 주석은 `// from https://www.sciencedirect.com/science/article/pii/S004578251830389X` (7)다. CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (8)가 붙은 `topo_diff`를 정의하며 x·y 좌표를 상수 참조로 받는다(9–14). 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 15–26 | 시작 시 9–14행 `topo_diff` 본문 안. `real z_int = 0;` (15)으로 초기화한다. 원문 식은 `real cone1 = C(1.0) - C(0.2) * sqrt( ( x_int - C(20.0) ) * ( x_int - C(20.0) ) + ( y_int - C(15.0) ) * ( y_int - C(15.0) ) );` (17), `real cone2 = C(2.0) - C(0.5) * sqrt( ( x_int - C(40.0) ) * ( x_int - C(40.0) ) + ( y_int - C(15.0) ) * ( y_int - C(15.0) ) );` (18), `real cone3 = C(3.0) - C(0.3) * sqrt( ( x_int - C(60.0) ) * ( x_int - C(60.0) ) + ( y_int - C(15.0) ) * ( y_int - C(15.0) ) );` (19)다. 중심이 각각 (20,15), (40,15), (60,15)인 원뿔(cone) 높이를 계산한다. `z_int = max(z_int, cone1);` (21), `z_int = max(z_int, cone2);` (22), `z_int = max(z_int, cone3);` (23)로 0과 세 높이의 최댓값을 남긴다. `return z_int;` (25), 빈 줄, 함수 종료를 포함한다(16·20·24·26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
