---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/get_spatial_coord.cuh
lines: 15
sha256: 996600dba80e4c2ed5abc58802c0b054bf131eba425de8a0e36a045dc1dc0671
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_spatial_coord.cuh — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`를 포함한다(3). 빈 줄(4) 뒤 `../types/real.h`를 포함한다(5). 마지막은 빈 줄(6)이다. 이 파일 자체에는 전처리 조건 분기가 없다. |
| 7–15 | `__device__ __forceinline__` (7) 함수 `real get_spatial_coord`를 정의한다(8–13). 입력은 상수 참조(const reference) `const int& idx` (10), `const real& cellsize` (11)이다. 반환식 원문은 `return idx * cellsize + cellsize / C(2.0);` (14)이다. 격자 인덱스에 셀 크기(cell size)를 곱하고 반 셀을 더하여 셀 중심 좌표(cell-centre coordinate)를 반환한다. 형식 매크로 `C(2.0)`를 식에 그대로 사용한다. 함수 종료(15)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–14: 함수 인수는 인덱스와 셀 크기뿐이다. 반환식에는 별도의 좌표 원점 이동항이 없다.
