---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/modal_projections.cuh
lines: 22
sha256: 7d609c089ce01d2e66dce8fca965c1603da76a8f15fc05b861127691904291e3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# modal_projections.cuh — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1). cuda_runtime.h, device_launch_parameters.h, BLOCK_VAR_MACROS.cuh, NodalValues.h, HierarchyIndex.h, Coordinate.h, AssembledSolution.h, SolverParams.h를 포함한다(3–12). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 14–22 | `__global__` (14)인 CUDA 커널(kernel) modal_projections를 선언한다(15–22). NodalValues, AssembledSolution, SolverParams, int mesh_dim과 int interface_dim을 값으로 받는다(17–21). 기본 인수와 커널 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
