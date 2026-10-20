---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_x_face_unit.cuh
lines: 50
sha256: 61d277aca0b615b72f99da075180426cc9291acff1ba4bb9ceac092dd8dffa60
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_x_face_unit.cuh — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–21 | `#pragma once`와 CUDA 런타임·실수·계층 인덱스(hierarchy index)·x좌표 계산 헤더를 포함한다(1–8). CUDA 장치 함수(device function) `get_x_face_unit`는 현재·이웃 인덱스, 이웃 레벨·최대 세분 레벨, 면 x좌표·최세 x간격·방향을 받는다(10–21). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (10). |
| 22–43 | 시작 시 10–21행 `get_x_face_unit` 안. 이웃 인덱스가 -1이면 단위 면 좌표(unit face coordinate)를 0으로 초기화한다(22–24). 방향 switch에서 북·남은 0.5, 동은 0, 서는 1로 설정하고 default는 값을 바꾸지 않는다(26–40). 해당 좌표를 즉시 반환하고 이웃 부재 분기를 닫는다(42–43). 원문: `if (h_idx_nghbr == -1)` (22); `switch (direction)` (26); `case NORTH:`<br>`case SOUTH:`<br>`x_face_unit = C(0.5);` (28–30); `case EAST:`<br>`x_face_unit = C(0.0);` (32–33); `case WEST:`<br>`x_face_unit = C(1.0);` (35–36); `default:` (38). |
| 44–50 | 시작 시 10–21행 `get_x_face_unit` 안이며 22행 조건 밖. 이웃 지역 x간격과 `get_x_coord`로 이웃 중심 x좌표를 계산한다(45–47). 이웃 왼쪽 끝에서 면까지의 거리를 이웃 간격으로 나눠 반환한다(49–50). 원문: `real dx_loc_nghbr = dx_finest * ( 1 << (max_ref_lvl - level_nghbr) );` (45); `real x_nghbr = get_x_coord(h_idx_nghbr, level_nghbr, max_ref_lvl, dx_finest);` (47); `return ( x_face - ( x_nghbr - dx_loc_nghbr / C(2.0) ) ) / dx_loc_nghbr;` (49). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13: 현재 인덱스 인수 `h_idx`는 함수 본문에서 참조하지 않는다.
- 24·38–42·49: 이웃 부재 시 알 수 없는 방향은 초기값 0을 반환한다. 이웃 존재 시 계산 결과를 0–1로 제한하는 별도 식은 없다.
