---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/add_ghost_cells.cuh
lines: 27
sha256: 97849c1747503679d76b3aa0c25f19b19bccf21ac43ac99d3f952003407502ba
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# add_ghost_cells.cuh — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1)와 CUDA 실행·Neighbours·SolverParams·SimulationParams·Boundaries·get_lvl_idx·compact·non_reflective_wave 헤더를 포함한다(3–13). 조건부 전처리 분기는 없다. |
| 15–27 | `__global__` (15) 지정의 add_ghost_cells 커널(kernel)을 선언한다(16–27). 조립 해(assembled solution), 이웃(neighbour), 솔버(solver)·모의 매개변수, 경계, real current_time·dt·dx_finest 및 int test_case를 받는다(18–26). 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
