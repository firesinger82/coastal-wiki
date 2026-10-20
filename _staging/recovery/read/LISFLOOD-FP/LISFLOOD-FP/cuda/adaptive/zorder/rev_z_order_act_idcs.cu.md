---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/rev_z_order_act_idcs.cu
lines: 20
sha256: dc5854d99785541cb2d62ed52dd09b55ddfbfa9388ff8db7e9974de16047ec65
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rev_z_order_act_idcs.cu — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `rev_z_order_act_idcs.cuh`를 포함한다(1). 빈 줄(2) 뒤 `__global__` (3) 커널(kernel) `rev_z_order_act_idcs`를 정의한다(4–11). 인수는 역 행 우선 순서(reverse row-major order) 배열 `MortonCode* d_rev_row_major`, 임시 해 `AssembledSolution d_buf_assem_sol`, 출력 해 `AssembledSolution d_assem_sol`, 가장 세밀한 수준(finest level)의 원소 수 `const int num_finest_elems`이다(6–9). 전처리 조건 분기는 없다. |
| 12–20 | 시작 시 4행 커널 본문 안이다. 스레드 인덱스(thread index) 식은 `const int idx = blockDim.x * blockIdx.x + threadIdx.x;` (12)이다. 빈 줄(13) 뒤 `if (idx >= num_finest_elems) return;` (14)로 원소 수 밖 스레드를 종료한다. 빈 줄(15) 뒤 `const int sorted_idx = d_rev_row_major[idx];` (16)로 원본의 위치를 얻는다. 빈 줄(17) 뒤 `d_assem_sol.act_idcs[idx] = d_buf_assem_sol.act_idcs[sorted_idx];` (18), `d_assem_sol.levels[idx]   = d_buf_assem_sol.levels[sorted_idx];` (19)로 활성 인덱스(active index)와 세분화 수준(refinement level)을 원래 순서로 복사한다. 커널 종료(20)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14·16–19: 스레드 범위 조건은 `idx >= num_finest_elems`이다. 배열에서 읽은 `sorted_idx`가 임시 해의 배열 범위 안인지 검사하는 별도 조건은 이 커널에 없다.
