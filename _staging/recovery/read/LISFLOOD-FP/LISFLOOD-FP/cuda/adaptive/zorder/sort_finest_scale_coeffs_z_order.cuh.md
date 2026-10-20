---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/sort_finest_scale_coeffs_z_order.cuh
lines: 20
sha256: 64379960512397250699d2114b4353f070480060ed2fc4629c3e1bd137c820ad
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sort_finest_scale_coeffs_z_order.cuh — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1). cuda_utils·CUB·CHECK_CUDA_ERROR·AssembledSolution·SolverParams·MortonCode 헤더 포함(3–11)과 빈 줄. 별도 전처리 조건 분기는 없다. |
| 13–20 | `__global__` (13) 커널(kernel) sort_finest_scale_coeffs_z_order 원형. d_buf_assem_sol·d_assem_sol·d_rev_z_order·solver_params를 받는다(14–20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
