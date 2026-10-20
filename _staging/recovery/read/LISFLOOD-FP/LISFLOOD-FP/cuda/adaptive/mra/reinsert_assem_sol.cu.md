---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/reinsert_assem_sol.cu
lines: 32
sha256: 4c04678c1c5680a288a2d5cd024d5581e9bae2fbb7cfc36407e6f6a2fa80da31
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# reinsert_assem_sol.cu — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 관련 헤더 포함(1), `__global__` (3) 커널(kernel) reinsert_assem_sol 정의(4–11). 조건부 전처리 분기는 없다. 조립 해(assembled solution), 활성 인덱스(index), 스케일 계수(scale coefficient), 솔버(solver) 매개변수를 받는다(6–9). `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (12) 뒤 `if (idx >= d_assem_sol.length) return;` (14)로 길이를 검사하고 act_idcs[idx]를 읽는다(16). 수위 계수는 `d_scale_coeffs.eta0[active_idx] = d_assem_sol.h0[idx] + d_assem_sol.z0[idx];` (18)로 계산한다. qx0·qy0 계수는 대응 배열에서 복사한다(19–20). |
| 22–32 | 시작 시 3–11행 reinsert_assem_sol 커널 안. `if (solver_params.solver_type == MWDG2)` (22)일 때 `d_scale_coeffs.eta1x[active_idx] = d_assem_sol.h1x[idx] + d_assem_sol.z1x[idx];` (24) 및 `d_scale_coeffs.eta1y[active_idx] = d_assem_sol.h1y[idx] + d_assem_sol.z1y[idx];` (28)로 x·y 선형 수위 계수를 계산한다. qx1x·qy1x·qx1y·qy1y는 조립 해에서 복사한다(25–26·29–30). 분기·커널 종료(31–32). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
