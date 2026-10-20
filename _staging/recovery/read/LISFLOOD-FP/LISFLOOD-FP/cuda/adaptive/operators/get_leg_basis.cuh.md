---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_leg_basis.cuh
lines: 40
sha256: e87026fb54546f81d54e8f50aa60c69b5df6811694b31d23672248eebe8ef165
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_leg_basis.cuh — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–27 | `#pragma once`와 CUDA 런타임·Legendre 기저(Legendre basis)·x/y 면 좌표·단위 좌표 헤더를 포함한다(1–10). CUDA 장치 함수(device function) `get_leg_basis`는 현재·이웃 계층 인덱스(hierarchy index), 이웃 레벨·최대 세분 레벨, 좌표·지역 간격·최세 간격·방향을 받는다(12–27). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (12). |
| 28–40 | 시작 시 12–27행 `get_leg_basis` 안. `get_x_face_coord`와 `get_y_face_coord`로 면 좌표를 계산한다(28–29). `get_x_face_unit`과 `get_y_face_unit`로 이웃 기준 단위 좌표를 계산한다(31–32). 상수 1과 x/y의 일차 정규화 Legendre 기저를 반환한다(34–40). 원문: `real x_face = get_x_face_coord(x, dx_loc, direction);`<br>`real y_face = get_y_face_coord(y, dy_loc, direction);` (28–29); `real x_face_unit = get_x_face_unit(h_idx, h_idx_nghbr, level_nghbr, max_ref_lvl, x_face, dx_finest, direction);`<br>`real y_face_unit = get_y_face_unit(h_idx, h_idx_nghbr, level_nghbr, max_ref_lvl, y_face, dy_finest, direction);` (31–32); `return`<br>`{`<br>`C(1.0),`<br>`sqrt( C(3.0) ) * ( C(2.0) * x_face_unit - C(1.0) ),`<br>`sqrt( C(3.0) ) * ( C(2.0) * y_face_unit - C(1.0) )`<br>`};` (34–39). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
