---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/get_x_coord.cuh
lines: 25
sha256: c9a90f5cbaaa8bdff84b0b19bd38b0ae288a577abf5a912748deb8b61228f3cb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_x_coord.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`를 포함한다(3). 빈 줄(4) 뒤 `get_lvl_idx.cuh`, `get_i_index.cuh`, `get_spatial_coord.cuh`를 포함한다(5–7). 마지막은 빈 줄(8)이다. 이 파일 자체에는 전처리 조건 분기가 없다. |
| 9–17 | `__device__ __forceinline__` (9) 함수 `real get_x_coord`를 정의한다(10–17). 상수 참조(const reference) 인수는 계층 인덱스(hierarchy index) `h_idx`, 현재 세분화 수준(refinement level) `level`, 최대 수준 `max_ref_lvl`, 가장 세밀한 x 방향 셀 크기 `dx_finest`이다(12–15). |
| 18–25 | 시작 시 10행 함수 본문 안이다. 지역 셀 크기(cell size) 식은 `real dx_loc = dx_finest * ( 1 << (max_ref_lvl - level) );` (18)이다. 빈 줄(19) 뒤 `MortonCode code = h_idx - get_lvl_idx(level);` (20)로 해당 수준의 시작 인덱스를 빼 모턴 코드(Morton code)를 구한다. 빈 줄(21) 뒤 `Coordinate i = get_i_index(code);` (22)로 x 방향 격자 인덱스를 구한다. 빈 줄(23) 뒤 `return get_spatial_coord(i, dx_loc);` (24)로 셀 중심 좌표(cell-centre coordinate)를 반환한다. 함수 종료(25)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 12–20: 셀 크기 계산은 `1 << (max_ref_lvl - level)`을 사용한다. 이 함수에는 수준 차이의 부호·시프트 범위 또는 `h_idx`의 해당 수준 범위를 확인하는 조건이 없다.
