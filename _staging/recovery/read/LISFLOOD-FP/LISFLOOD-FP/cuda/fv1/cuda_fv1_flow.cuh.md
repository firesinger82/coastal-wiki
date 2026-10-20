---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv1/cuda_fv1_flow.cuh
lines: 63
sha256: ad00f0b8f6d114630a4bf90f786cd8a4e121ef5626e2a391432ebc0ad95da185
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv1_flow.cuh — 판독 구간 기록

구간은 1행부터 63행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | `#pragma once` (1), `#include "../geometry.h"` (2), `#include "cuda_flow.cuh"` (3)와 lis::cuda::fv1 이름공간(namespace)(5–10)이다. 전처리 조건 분기는 없다. Flow 구조체(struct)의 포인터는 `NUMERIC_TYPE* __restrict__ H;` (14), `NUMERIC_TYPE* __restrict__ HU;` (15), `NUMERIC_TYPE* __restrict__ HV;` (16), `NUMERIC_TYPE* __restrict__ maxH;` (18), `NUMERIC_TYPE* __restrict__ totalHtm;` (19), `NUMERIC_TYPE* __restrict__ maxHtm;` (20), `NUMERIC_TYPE* __restrict__ initHtm;` (21)이다. |
| 23–30 | 시작 시 12행 Flow 구조체 안이다. `__host__ __device__ FlowVector operator[]` (23)는 idx를 받아 `return { H[idx], HU[idx], HV[idx] };` (28)로 값을 반환한다. |
| 31–63 | 시작 시 12행 Flow 구조체 안이다. Flow·Geometry를 받는 정적 allocate_pinned·allocate_device(31–41), dst·src·Geometry를 받는 copy(43–48), Flow를 받는 free_pinned·free_device를 선언한다(50–58). 구조체와 세 이름공간을 닫는다(59–63). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
