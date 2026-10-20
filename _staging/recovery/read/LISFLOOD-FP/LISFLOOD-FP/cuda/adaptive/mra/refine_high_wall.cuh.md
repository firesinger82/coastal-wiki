---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/refine_high_wall.cuh
lines: 18
sha256: c0bb1e72e49af61c1f9ab0d06ec466f227741ff5342dea3bfff27c842e02846c
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# refine_high_wall.cuh — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1)로 중복 포함을 막는다. CUDA 유틸리티(utilities), SimulationParams·SolverParams, 모턴 코드(Morton code) 생성 및 get_lvl_idx 헤더를 포함한다(3–9). 조건부 전처리 분기는 없다. |
| 11–18 | `__host__` (11) 지정의 호스트(host) 함수 refine_high_wall을 선언한다(12–18). 입력은 const 참조 sim_params·solver_params, const int max_ref_lvl이며 h_preflagged_details는 bool 포인터다(14–17). 구현·조건·기본값은 이 선언에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
