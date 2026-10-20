---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/find_neighbours.cuh
lines: 21
sha256: 350f0f7e2cdb1da6941fbe716469b034815adae3a706464bf39d88e1cd770f86
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# find_neighbours.cuh — 판독 구간 기록

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1) 뒤 CUDA 실행·Neighbours·Coordinate·Directions·MortonCode·SimulationParams·get_lvl_idx 헤더를 포함한다(3–12). 조건부 전처리 분기는 없다. |
| 14–21 | `__global__` (14) 지정의 find_neighbours 커널(kernel)을 선언한다(15–21). AssembledSolution d_assem_ol, Neighbours d_neighbours, SimulationParams sim_params, int mesh_dim을 받는다(17–20). 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
