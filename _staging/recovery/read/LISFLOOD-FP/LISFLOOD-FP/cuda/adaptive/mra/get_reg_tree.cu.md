---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/get_reg_tree.cu
lines: 35
sha256: 4aaca09795f52e67568093483fd788e4e119cae91caaeb4f22990ca821ff7faf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_reg_tree.cu — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | get_reg_tree.cuh 포함과 빈 줄(1–2). `__host__` (3)인 get_reg_tree는 d_sig_details 포인터와 값으로 받는 SolverParams를 인수로 갖는다(4–9). 이 파일에는 전처리 조건 분기가 없다. |
| 10–21 | 시작 시 4–9행 get_reg_tree 함수 안. `for (int level = solver_params.L - 1; level > LVL_SINGLE_BLOCK; level--)` (10)는 높은 수준(level)부터 LVL_SINGLE_BLOCK보다 큰 수준까지 내림차순으로 처리한다. `int num_threads  = 1 << (2 * level);` (12), `int num_blocks = get_num_blocks(num_threads, THREADS_PER_BLOCK);` (13)로 스레드(thread) 수와 블록(block) 수를 계산한다. `regularisation<false><<<num_blocks, THREADS_PER_BLOCK>>>` (15)에 d_sig_details, level, num_threads를 전달하여 정규화(regularisation)를 실행한다(16–20). 빈 줄과 루프 끝도 포함한다(14·21). |
| 22–35 | 시작 시 4–9행 get_reg_tree 함수 안이며 10행 루프 밖. `HierarchyIndex prev_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK - 1);` (23), `HierarchyIndex curr_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK);` (24), `HierarchyIndex next_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK + 1);` (25)로 세 지역 인덱스를 계산한다. `int num_threads  = 1 << (2 * LVL_SINGLE_BLOCK);` (27)로 스레드 수를 정한다. `regularisation<true><<<1, THREADS_PER_BLOCK>>>` (29)에 d_sig_details, LVL_SINGLE_BLOCK, num_threads를 전달한다(30–34). 이 호출은 한 블록을 사용한다. 빈 줄과 함수 끝도 포함한다(22·26·28·35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–25: prev_lvl_idx, curr_lvl_idx, next_lvl_idx는 계산 후 이 함수의 다른 문장에서 사용되지 않는다.
