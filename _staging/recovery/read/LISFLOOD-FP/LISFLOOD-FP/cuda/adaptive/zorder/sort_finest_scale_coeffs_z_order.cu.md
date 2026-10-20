---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/sort_finest_scale_coeffs_z_order.cu
lines: 35
sha256: 3dd612fb22c603721afb46c9da240cac4a8fa4f66b22637ede95679b91e24337
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sort_finest_scale_coeffs_z_order.cu — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | 헤더 포함(1). `__global__` (3) 커널(kernel) sort_finest_scale_coeffs_z_order는 조립 해 두 개·Morton 코드(Morton code) 포인터·SolverParams를 받는다(4–10). `const int idx = blockDim.x * blockIdx.x + threadIdx.x;` (12). `if (idx >= d_assem_sol.length) return;` (14)로 범위 밖 스레드를 종료한다. d_rev_z_order[idx]에서 sorted_idx를 얻는다(16). d_buf_assem_sol의 sorted_idx 위치 h0·qx0·qy0·z0를 d_assem_sol의 idx에 복사한다(18–21). 전처리 조건 분기는 없다. |
| 23–35 | 시작 시 4–11행 커널 안. `if (solver_params.solver_type == MWDG2)` (23)일 때만 h1x·qx1x·qy1x·z1x(25–28)와 h1y·qx1y·qy1y·z1y(30–33)를 같은 인덱스 대응으로 복사한다. 조건과 커널 종료(34–35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–33: 이 커널은 평균 계수와 MWDG2의 1차 계수를 복사한다. levels·act_idcs 대입은 없다.
