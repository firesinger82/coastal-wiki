---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/regularisation.cu
lines: 105
sha256: ac612891f8ec692c296e96414da7ae5c714647f34fd003cc5227f9ad5656423e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# regularisation.cu — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | regularisation.cuh 포함(1), `template <bool SINGLE_BLOCK>` (3), `__global__` (4)로 유의 상세(significant detail) 규칙화 커널(kernel)을 정의한다. 조건부 전처리 분기는 없다. `__shared__ bool shared_sig_details[THREADS_PER_BLOCK];` (12)는 공유 메모리(shared memory) 배열이다. DetailChildren 지역값을 선언한다(14). 스레드(thread) 인덱스(index)는 `HierarchyIndex t_idx = threadIdx.x;`<br>`HierarchyIndex idx   = blockIdx.x * blockDim.x + t_idx;` (16–17)다. `if (idx >= num_threads) return;` (19)로 범위 밖 스레드가 반환한다. 계층 레벨(level) 시작 인덱스를 `HierarchyIndex prev_lvl_idx = get_lvl_idx(level - 1);`<br>`HierarchyIndex curr_lvl_idx = get_lvl_idx(level);`<br>`HierarchyIndex next_lvl_idx = get_lvl_idx(level + 1);` (21–23)으로 구한다. |
| 25–61 | 시작 시 3–11행 regularisation 템플릿(template) 함수 안. `if (SINGLE_BLOCK)` (25) 참 분기는 단일 블록(block) 경로다. parent_idx 선언(27), `HierarchyIndex child_idx = curr_lvl_idx + t_idx;` (28) 뒤 상세 플래그를 공유 배열에 복사한다(30). `__syncthreads();` (32)로 동기화한다. `for (int lvl = LVL_SINGLE_BLOCK - 1; lvl >= 0; lvl--)` (34)에서 `HierarchyIndex curr_lvl_idx_block = get_lvl_idx(lvl);`<br>`int            num_threads        = 1 << (2 * lvl);`<br>`parent_idx = curr_lvl_idx_block + t_idx;` (36–39)로 부모 위치와 참여 스레드 수를 계산한다. `if (t_idx < num_threads)` (41) 참일 때 `child_details = get_child_details`<br>`(`<br>`shared_sig_details,`<br>`4 * t_idx`<br>`);` (43–47)로 네 자식 상세를 읽는다. `__syncthreads();` (50) 뒤 `if (t_idx < num_threads)` (52)에서 `if (child_details.has_sig_detail()) d_sig_details[parent_idx] = SIGNIFICANT;` (54)로 유의 부모를 설정하고 `shared_sig_details[t_idx] = child_details.has_sig_detail();` (56)로 결과를 공유 배열에 복사한다. `__syncthreads();` (59) 후 반복하며 루프·분기를 닫는다(60–61). |
| 62–83 | 시작 시 3–11행 regularisation 함수 안이며 25행 if의 `else` (62) 경로다. `HierarchyIndex h_idx = curr_lvl_idx + idx;` (64)로 현재 계층 위치를 계산하고 공유 배열에 상세를 복사한다(66). `__syncthreads();` (68) 뒤 `if ( t_idx >= (THREADS_PER_BLOCK / 4) ) return;` (70)로 블록의 뒤쪽 스레드가 반환한다. `HierarchyIndex t_idx_shifted = 4 * t_idx;`<br>`h_idx         = prev_lvl_idx + t_idx + blockIdx.x * (THREADS_PER_BLOCK / 4);` (72–73)으로 네 자식 묶음과 부모 위치를 구한다. `child_details = get_child_details`<br>`(`<br>`shared_sig_details,`<br>`t_idx_shifted`<br>`);` (75–79) 호출 뒤 `if ( child_details.has_sig_detail() ) d_sig_details[h_idx] = SIGNIFICANT;` (81)로 유의 부모를 설정한다. 분기와 커널을 닫는다(82–83). |
| 84–105 | 빈 줄(84) 뒤 inline dummy_template_instantiator를 정의한다(85–91). bool 포인터와 level·num_threads를 받아 `regularisation<true><<<1, 1>>>`<br>`(`<br>`d_sig_details,`<br>`level,`<br>`num_threads`<br>`);` (92–97) 및 `regularisation<false><<<1, 1>>>`<br>`(`<br>`d_sig_details,`<br>`level,`<br>`num_threads`<br>`);` (99–104)로 두 템플릿을 각각 1블록·1스레드로 실행하는 호출문을 갖는다. 함수 종료(105). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·32·50·59·68: idx 범위 검사의 조기 반환은 공유 메모리 동기화보다 앞에 있다. 이 파일에는 num_threads가 블록 크기의 배수인지 검사하는 문장이 없다.
- 23: next_lvl_idx는 계산한 뒤 이 함수에서 참조하지 않는다.
- 54·81: 전역 d_sig_details에는 자식이 유의할 때 SIGNIFICANT를 대입한다. 자식이 유의하지 않을 때 전역 부모 값을 지우는 대입은 없다.
- 92–104: dummy_template_instantiator 안의 두 커널 실행 설정은 모두 <<<1, 1>>>로 고정되어 있다.
