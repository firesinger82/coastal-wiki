---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/preflag_topo.cuh
lines: 21
sha256: e0f7661de3a7beb5b9d14c9ac7abf133d7344696d66e106b34f4ba015fb0ef8a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# preflag_topo.cuh — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1). cuda_utils.cuh, SolverParams.h, get_num_blocks.h, HierarchyIndex.h, encode_and_thresh_topo.cuh를 포함한다(3–9). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 11–21 | `__host__` (11)인 void preflag_topo 선언이다(12–21). ScaleCoefficients와 Details 참조, bool 포인터 d_preflagged_details, Maxes와 SolverParams 및 SimulationParams 참조, int first_time_step을 받는다(14–20). 기본 인수와 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
