---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_reg_tree.cu
lines: 43
sha256: 77664aad8a04f8b88c3aca4b0e8a52442cb023027560e330e89d690d35e0377f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_reg_tree.cu — 판독 구간 기록

구간은 1행부터 43행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | `#include "get_reg_tree.cuh"` (1) 뒤 호스트 함수 `__host__ void lis::cuda::acc_nugrid::get_reg_tree` (3)를 정의한다. 인수는 `bool* d_sig_details`와 `int lev`이다(5–6). 반복 조건은 `for (int level = lev - 1; level > LVL_SINGLE_BLOCK; level--)` (9)이다. 반복 안의 수준 시작 인덱스 식은 `index_1D prev_lvl_idx = get_lvl_idx(level - 1);` (11), `index_1D curr_lvl_idx = get_lvl_idx(level);` (12), `index_1D next_lvl_idx = get_lvl_idx(level + 1);` (13)이다. 스레드(thread) 수는 `int      num_threads  = 1 << (2 * level);` (14)이다. 블록(block) 수는 `int num_blocks = get_num_blocks(num_threads, THREADS_PER_BLOCK_MRA);` (16)이다. 템플릿 인자 false인 CUDA 커널 호출은 `reg_new<false><<<num_blocks, THREADS_PER_BLOCK_MRA>>>` (18)이며 인수 순서는 `d_sig_details`, `level`, `prev_lvl_idx`, `curr_lvl_idx`, `next_lvl_idx`, `num_threads`이다(19–26). 반복을 닫고 빈 줄을 둔다(27–28). 이 파일에는 전처리 조건 분기가 없고 두 매크로의 수치 정의도 없다. |
| 29–43 | 시작 시 3–8행의 `get_reg_tree` 함수 안이며 9행 반복 밖. 인덱스 식은 `index_1D prev_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK - 1);` (29), `index_1D curr_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK);` (30), `index_1D next_lvl_idx = get_lvl_idx(LVL_SINGLE_BLOCK + 1);` (31)이다. 스레드 수는 `int      num_threads  = 1 << (2 * LVL_SINGLE_BLOCK);` (32)이다. CUDA 호출은 `reg_new<true><<<1, THREADS_PER_BLOCK_MRA>>>` (34)이다. 인수는 `d_sig_details`, `LVL_SINGLE_BLOCK`, 이전·현재·다음 수준 인덱스, `num_threads` 순서이다(35–42). 함수를 닫는다(43). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9·29–42: `lev`는 첫 반복문의 시작 수준에 쓰인다. 반복문 밖의 `reg_new<true>` 호출은 `lev`에 대한 별도 조건 없이 실행된다.
- 18–26·34–42: 두 CUDA 커널 실행문은 이 함수에서 오류 검사 매크로나 명시적 장치 동기화 호출로 감싸지 않는다.
