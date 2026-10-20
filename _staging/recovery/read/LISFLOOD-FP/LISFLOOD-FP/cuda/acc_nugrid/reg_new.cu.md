---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/reg_new.cu
lines: 111
sha256: ed0a078f4cf1392818031110571880725a9fa69325ad37c7ef983f0ecf14e755
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# reg_new.cu — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | reg_new.cuh 포함(1), `template <bool SINGLE_BLOCK>` (3)<br>`__global__ void lis::cuda::acc_nugrid::reg_new` (4)로 단일 블록 여부를 템플릿(template) 인자로 받는 CUDA 커널(kernel)을 정의한다. 인수는 유의 상세계수 플래그, level, 이전·현재·다음 레벨 시작 인덱스, 스레드 수이다(5–12). `__shared__ bool shared_sig_details[THREADS_PER_BLOCK_MRA];` (14)와 DetailChildren 선언(16). 스레드 인덱스는 `index_1D t_idx = threadIdx.x;` (18)<br>`index_1D idx   = blockIdx.x * blockDim.x + t_idx;` (19). 경계 조건 `if (idx >= num_threads) return;` (21). `if (SINGLE_BLOCK)` (23) 참 분기는 `index_1D child_idx = curr_lvl_idx + t_idx;` (26)로 자식 위치를 계산하고 공유 메모리(shared memory)에 플래그를 복사한다(28). `__syncthreads();` (30). 전처리 조건 분기는 없다. |
| 31–59 | 시작 시 4행 reg_new 커널·23행 SINGLE_BLOCK 참 분기 안. 상위 레벨로 거슬러 가는 반복은 `for (int lvl = LVL_SINGLE_BLOCK - 1; lvl >= 0; lvl--)` (32). 레벨 시작 위치와 스레드 수는 `index_1D curr_lvl_idx_block = get_lvl_idx(lvl);` (34)<br>`int      num_threads        = 1 << (2 * lvl);` (35), 부모 위치는 `parent_idx = curr_lvl_idx_block + t_idx;` (37). `if (t_idx < num_threads)` (39)이면 get_child_details 호출에 shared_sig_details와 `4 * t_idx` (44)를 전달한다(41–45). `__syncthreads();` (48) 뒤 `if (t_idx < num_threads)` (50)에서 `if (child_details.has_sig_detail()) d_sig_details[parent_idx] = SIGNIFICANT;` (52), `shared_sig_details[t_idx] = child_details.has_sig_detail();` (54)로 전역·공유 플래그를 갱신한다. `__syncthreads();` (57) 후 반복·참 분기를 닫는다(58–59). |
| 60–81 | 시작 시 4행 reg_new 커널 안. `else` (60)는 23행 SINGLE_BLOCK 거짓 분기이다. `index_1D g_idx = curr_lvl_idx + idx;` (62)로 전역 위치를 구하고 공유 배열에 복사한다(64). `__syncthreads();` (66) 뒤 `if ( t_idx >= (THREADS_PER_BLOCK_MRA / 4) ) return;` (68)로 담당 스레드를 제한한다. `index_1D t_idx_shifted = 4 * t_idx;` (70)<br>`g_idx         = prev_lvl_idx + t_idx + blockIdx.x * (THREADS_PER_BLOCK_MRA / 4);` (71)로 자식 묶음과 부모 위치를 계산한다. get_child_details(shared_sig_details, t_idx_shifted)를 호출한다(73–77). `if ( child_details.has_sig_detail() ) d_sig_details[g_idx] = SIGNIFICANT;` (79)로 유의 플래그를 설정하고 분기·커널을 닫는다(80–81). |
| 82–111 | dummy_template_instantiator는 커널과 동일한 인수를 받는 inline 함수이다(83–91). true 특수화 호출 전체는 `lis::cuda::acc_nugrid::reg_new<true><<<1, 1>>>` (92)<br>`(` (93)<br>`d_sig_details,` (94)<br>`level,` (95)<br>`prev_lvl_idx,` (96)<br>`curr_lvl_idx,` (97)<br>`next_lvl_idx,` (98)<br>`num_threads` (99)<br>`);` (100). false 특수화 호출 전체는 `lis::cuda::acc_nugrid::reg_new<false><<<1, 1>>>` (102)<br>`(` (103)<br>`d_sig_details,` (104)<br>`level,` (105)<br>`prev_lvl_idx,` (106)<br>`curr_lvl_idx,` (107)<br>`next_lvl_idx,` (108)<br>`num_threads` (109)<br>`);` (110). 두 호출의 실행 구성은 각각 블록 1개·스레드 1개로 원문에 고정되어 있다. 함수 끝(111). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·10·83–110: 커널 인수 level과 next_lvl_idx는 커널 본문의 계산에 사용되지 않는다. dummy_template_instantiator는 두 인수를 그대로 전달한다.
- 21·30·48·57·66: idx 경계의 조기 반환은 첫 __syncthreads()보다 앞에 있다. 이 파일에는 해당 경계에 맞추는 실제 호출부의 실행 구성 검사가 없다.
- 52·79: 부모 플래그의 전역 대입은 has_sig_detail() 참일 때 SIGNIFICANT를 쓰는 문장뿐이다. 거짓일 때 전역 부모 플래그를 해제하는 문장은 없다.
