---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/preflag_details.cuh
lines: 25
sha256: fe8b9572bdc4e5499bb55e5f478cbceb6c92cd74d4ea44988eff8c312a628bd7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# preflag_details.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1). cuda_utils.cuh, Boundaries.h, PointSources.h, StagePoints.h, SimulationParams.h, SolverParams.h, get_lvl_idx.cuh, refine_high_wall.cuh를 포함한다(3–12). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 14–25 | `__host__` (14)인 preflag_details는 bool 포인터를 반환한다(15). 인수는 Boundaries, PointSources, StagePoints, SimulationParams, SolverParams의 const 참조와 num_details, max_ref_lvl, test_case의 const int 참조이다(17–24). 기본 인수와 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
