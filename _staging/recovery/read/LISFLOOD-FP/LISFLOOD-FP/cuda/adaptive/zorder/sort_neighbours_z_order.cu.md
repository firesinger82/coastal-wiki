---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/sort_neighbours_z_order.cu
lines: 31
sha256: c86789be0120d8ceab3bc32a2b057526690d69379d8d35e6cb769a89fd3f6e5d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sort_neighbours_z_order.cu — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | 대응 헤더(1), `__global__` (3) 커널(kernel) sort_neighbours_z_order의 Neighbours 두 개·Morton 코드(Morton code) 포인터·최세밀 요소 수·SolverParams 인수(4–11). `const int idx = blockDim.x * blockIdx.x + threadIdx.x;` (13), `if (idx >= num_finest_elems) return;` (15). sorted_idx는 d_rev_z_order[idx](17). 네 방향 act_idcs를 d_neighbours의 sorted_idx에서 d_buf_neighbours의 idx로 복사한다(19–22). 전처리 조건 분기는 없다. |
| 24–31 | 시작 시 4–12행 커널 안. `if (solver_params.solver_type == MWDG2)` (24)일 때만 north·east·south·west의 levels를 같은 인덱스 대응으로 복사한다(26–29). 조건과 커널 종료(30–31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–7·19–29: 두 Neighbours 인수는 const 값으로 선언되지만 d_buf_neighbours의 포인터가 가리키는 배열에는 값을 쓴다.
