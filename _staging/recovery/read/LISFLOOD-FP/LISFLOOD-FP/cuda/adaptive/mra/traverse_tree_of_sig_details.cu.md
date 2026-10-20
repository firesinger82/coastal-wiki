---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/traverse_tree_of_sig_details.cu
lines: 101
sha256: a4acf5e6301af9793b67b7c69565bdd036ea5b0d8687dcd9b22d410d9ead3909
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# traverse_tree_of_sig_details.cu — 판독 구간 기록

구간은 1행부터 101행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | 헤더 포함(1), `__global__` (3) 커널(kernel) traverse_tree_of_sig_details 입구와 인수 선언(4–12). 조건부 전처리 분기는 없다. `__shared__ union`<br>`{`<br>`int            levels [4 * THREADS_PER_BLOCK];`<br>`HierarchyIndex indices[4 * THREADS_PER_BLOCK];`<br>`} shared;` (13–18)은 levels와 indices가 메모리를 공유하는 유니온(union)이다. 스레드(thread)별 levels[4]·indices[4]를 선언한다(20–21). `HierarchyIndex t_idx = threadIdx.x;`<br>`HierarchyIndex idx   = blockIdx.x * blockDim.x + t_idx;`<br>`int block_store_step = 3 * blockIdx.x * THREADS_PER_BLOCK;` (23–26)으로 스레드·블록 저장 위치를 구하며 `if (idx >= num_threads) return;` (28)로 범위를 검사한다. h_idx·curr_code·level은 0, keep_on_traversing은 true로 초기화한다(30·32·35·39). `MortonCode fine_code = 4 * idx;` (33)과 `HierarchyIndex curr_lvl_idx = get_lvl_idx(level);` (37)로 세밀 모턴 코드와 레벨 위치를 구한다. |
| 41–61 | 시작 시 3–12행 traverse_tree_of_sig_details 커널 안. `while (keep_on_traversing)` (41)에서 `MortonCode curr_code = ( fine_code >> ( 2 * (solver_params.L - level) ) );` (43)으로 현재 모턴 코드를 구한다. `curr_lvl_idx = get_lvl_idx(level);`<br>`h_idx = curr_lvl_idx + curr_code;` (45–47)로 계층 위치를 정하고 유의 플래그 is_sig를 읽는다(49). `if (!is_sig)` (51) 참이면 `for (int i = 0; i < 4; i++)` (54)에서 네 indices에 같은 h_idx, 네 levels에 같은 level을 복사한다(56–57). keep_on_traversing=false로 순회를 끝내도록 설정한다(60). 분기 참 부분 종료(61). |
| 62–87 | 시작 시 3–12행 커널·41행 while 안이며 51행 if의 `else` (62) 경로다. `level++;` (64)로 레벨을 올리고 `bool penultimate_level = (level == solver_params.L);` (66)으로 최세 레벨 도달 여부를 구한다. `if (!penultimate_level)` (68)이면 순회 플래그를 true로 유지한다(70). `else` (72) 경로에서는 `HierarchyIndex next_lvl_idx = get_lvl_idx(level);`<br>`HierarchyIndex child_idx    = next_lvl_idx + 4 * curr_code;` (74–75)로 네 자식 시작 위치를 구한다. `for (int i = 0; i < 4; i++)` (78)에서 `indices[i] = child_idx + i;` (80)으로 네 자식 인덱스(index)를 계산하고 level을 각 levels[i]에 복사한다(81). 순회 플래그를 false로 설정한 뒤 분기·while을 닫는다(84–87). |
| 88–101 | 시작 시 3–12행 커널 안이며 41행 while 밖. 활성 인덱스 저장 주석(89) 뒤 `for (int i = 0; i < 4; i++) shared.indices[4 * t_idx + i] = indices[i];` (90), `__syncthreads();` (91), `for (int i = 0; i < 4; i++) d_buf_assem_sol.act_idcs[idx + i * THREADS_PER_BLOCK + block_store_step] = shared.indices[t_idx + i * THREADS_PER_BLOCK];` (93), `__syncthreads();` (94)로 공유 배열과 전역 act_idcs를 채운다. 레벨 저장 주석(96) 뒤 `for (int i = 0; i < 4; i++) shared.levels[4 * t_idx + i] = levels[i];` (97), `__syncthreads();` (98), `for (int i = 0; i < 4; i++) d_buf_assem_sol.levels[idx + i * THREADS_PER_BLOCK + block_store_step] = shared.levels[t_idx + i * THREADS_PER_BLOCK];` (100)으로 같은 재배열을 levels에 적용한다. 커널 종료(101). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7: d_scale_coeffs 인수는 이 커널 본문에서 사용하지 않는다.
- 32·43: 바깥 curr_code는 0으로 선언한다. while 안에서 같은 이름의 curr_code를 다시 선언하며 실제 순회식과 child_idx 계산은 내부 변수를 사용한다.
- 28·91·94·98: idx 조기 반환은 모든 __syncthreads()보다 앞에 있다. 출력 인덱스 식은 THREADS_PER_BLOCK을 사용하며 blockDim.x와 같다는 검사는 이 파일에 없다.
- 35·41–87: level 초기값은 0이다. level 증가는 유의 상세 분기에만 있고 최세 레벨 판단은 증가 뒤 level == solver_params.L 비교로 수행한다. 별도의 최대 반복 횟수 검사는 없다.
