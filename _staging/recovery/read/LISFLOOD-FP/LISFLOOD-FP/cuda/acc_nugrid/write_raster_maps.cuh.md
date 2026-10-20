---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_raster_maps.cuh
lines: 28
sha256: f711780222b20c95b0d159a547327fec43de995964d98be2fceccb44214d66e6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_raster_maps.cuh — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1)로 중복 포함을 막는다. stdio.h·string.h·BLOCK_VAR_MACROS.cuh·cuda_utils.cuh·AssembledSolution.h를 포함한다(3–7). 전처리 조건 분기는 없다. |
| 9–28 | lis::cuda::acc_nugrid 이름공간(namespace)(9–14)에서 `__host__ void write_raster_maps` (16)를 선언한다. respath, d_assem_sol, mesh_dim, pars, call_gzip 및 precision을 받는다(18–23). 기본 인수는 `const int& precision = DEFAULT_PRECISION` (23). DEFAULT_PRECISION의 정의·값은 이 파일에 없다. 선언·이름공간 종료(24–28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
