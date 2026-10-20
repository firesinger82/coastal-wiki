---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/get_modal_values.cuh
lines: 21
sha256: 15a44af412a1732bc81f07f0f700084f0c2f9b25c9a29b45e46028823692bc3b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_modal_values.cuh — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1). BLOCK_VAR_MACROS.cuh, cuda_utils.cuh, get_lvl_idx.cuh, read_and_project_modes_fv1.cuh, read_and_project_modes_dg2.cuh를 포함한다(3–8). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 10–21 | `__host__` (10)인 void get_modal_values 선언이다(11–21). NodalValues, AssembledSolution, SolverParams, SimulationParams를 참조로 받는다(13–16). mesh_dim, interface_dim, test_case는 const int 참조이고 input_filename은 const char 포인터이다(17–20). 기본 인수와 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
