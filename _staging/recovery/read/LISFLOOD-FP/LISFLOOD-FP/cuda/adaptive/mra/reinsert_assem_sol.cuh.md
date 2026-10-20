---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/reinsert_assem_sol.cuh
lines: 17
sha256: 97cb007514866461de088ffc1e65cf20f9c954ad42a81bb62ca37b23695cefd6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# reinsert_assem_sol.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)와 빈 줄. CUDA 실행 헤더 2개와 ScaleCoefficients·AssembledSolution·SolverParams 형식 헤더를 포함한다(3–8). 조건부 전처리 분기는 없다. |
| 10–17 | `__global__` (10)로 reinsert_assem_sol 커널(kernel)을 선언한다. AssembledSolution, HierarchyIndex 포인터 act_idcs, ScaleCoefficients, SolverParams를 값 또는 포인터로 받으며 기본 인수는 없다(11–17). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
