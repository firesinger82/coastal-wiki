---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/extra_significance.cu
lines: 89
sha256: 7fd639790e7a9233f8c35a331b3bae929e5f90c84b1e58786fec47d9c166aa70
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# extra_significance.cu — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 헤더를 포함하고 SINGLE_BLOCK 템플릿의 CUDA extra_significance 커널을 정의한다(1–13). 전역 인덱스를 계산하고 num_threads 이상이면 반환한다(14–16). 조건부 전처리 분기는 없다. LVL_SINGLE_BLOCK·M_BAR·SIGNIFICANT의 값은 이 파일에서 정의하지 않으며 원문 기호로 유지한다. 원문: `template<bool SINGLE_BLOCK>` (3); `__global__` (4); `HierarchyIndex idx = blockIdx.x * blockDim.x + threadIdx.x;` (14); `if (idx >= num_threads) return;` (16). |
| 18–39 | 시작 시 5행 extra_significance 커널 안. SINGLE_BLOCK 참 분기는 lvl=0부터 LVL_SINGLE_BLOCK 미만까지 반복한다(18–20). 현재/다음 수준 시작 인덱스와 스레드 수를 계산한다(22–24). 해당 수준의 활성 스레드는 부모·자식 주소, 기존 유의성과 정규화 상세를 읽는다(26–33). 수준별 epsilon에 pow(C(2.0), M_BAR + 1)을 곱하여 추가 유의성 임계값을 계산한다(35–36). norm_detail과 비교하여 is_extra_sig를 설정한다(38). 원문: `if (SINGLE_BLOCK)` (18); `for (int lvl = 0; lvl < LVL_SINGLE_BLOCK; lvl++)` (20); `HierarchyIndex curr_lvl_idx_block = get_lvl_idx(lvl);` (22); `HierarchyIndex next_lvl_idx_block = get_lvl_idx(lvl + 1);` (23); `int            num_threads_block  = 1 << (2 * lvl);` (24); `if (idx < num_threads_block)` (26); `HierarchyIndex parent_idx = curr_lvl_idx_block + idx;` (28); `HierarchyIndex child_idx  = next_lvl_idx_block + 4 * idx;` (29); `real eps_local_block     = solver_params.epsilon / ( 1 << (solver_params.L - lvl) );` (35); `real eps_extra_sig_block = eps_local_block * pow(C(2.0), M_BAR + 1);` (36); `bool is_extra_sig = (norm_detail >= eps_extra_sig_block);` (38). |
| 40–51 | 시작 시 5행 커널·18행 SINGLE_BLOCK 참 분기·20행 lvl 루프·26행 활성 스레드 분기 안. 기존 유의성과 추가 유의성 조건이 모두 참이면 자식 네 개를 SIGNIFICANT로 둔다(40–45). 유의성·활성 스레드 조건 밖에서 매 수준 __syncthreads()를 실행한다(47–49). 루프와 참 분기를 닫는다(50–51). 원문: `if (is_sig && is_extra_sig)` (40); `d_sig_details[child_idx + 0] = SIGNIFICANT;` (42); `d_sig_details[child_idx + 1] = SIGNIFICANT;` (43); `d_sig_details[child_idx + 2] = SIGNIFICANT;` (44); `d_sig_details[child_idx + 3] = SIGNIFICANT;` (45); `__syncthreads();` (49). |
| 52–76 | 시작 시 5행 커널 안. 18행 SINGLE_BLOCK의 else 경로이다(52). 전달된 level의 현재/다음 시작 인덱스와 부모 주소를 계산한다(54–57). epsilon을 1 << (L-level)로 나눈 뒤 pow(C(2.0), M_BAR + 1)을 곱한다(59–60). 기존 유의성과 정규화 상세를 읽고 추가 조건을 비교한다(62–65). 둘을 동시에 만족하지 않으면 반환한다(67). 나머지는 자식 주소를 계산하고 자식 네 개를 SIGNIFICANT로 둔다(69–74). 원문: `else` (52); `HierarchyIndex curr_lvl_idx = get_lvl_idx(level);` (54); `HierarchyIndex next_lvl_idx = get_lvl_idx(level + 1);` (55); `HierarchyIndex parent_idx = curr_lvl_idx + idx;` (57); `real eps_local     = solver_params.epsilon / (1 << (solver_params.L - level));` (59); `real eps_extra_sig = eps_local * pow(C(2.0), M_BAR + 1);` (60); `bool sig_detail  = d_sig_details[parent_idx];` (62); `real norm_detail = d_norm_details[parent_idx];` (63); `bool is_extra_sig = (norm_detail >= eps_extra_sig);` (65); `if ( !(sig_detail && is_extra_sig) ) return;` (67); `HierarchyIndex child_idx = next_lvl_idx + 4 * idx;` (69); `d_sig_details[child_idx + 0] = SIGNIFICANT;` (71); `d_sig_details[child_idx + 1] = SIGNIFICANT;` (72); `d_sig_details[child_idx + 2] = SIGNIFICANT;` (73); `d_sig_details[child_idx + 3] = SIGNIFICANT;` (74). |
| 77–89 | 커널 밖 inline dummy_template_instantiator 정의이다(78–86). extra_significance<false>와 <true>를 각각 <<<1,1>>> 실행 구성으로 호출한다(87–88). 원문: `extra_significance<false><<<1,1>>>(d_sig_details, d_norm_details, solver_params, level, num_threads);` (87); `extra_significance<true> <<<1,1>>>(d_sig_details, d_norm_details, solver_params, level, num_threads);` (88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20·49: 단일 블록 수준 반복은 solver_params.L 대신 LVL_SINGLE_BLOCK을 상한으로 사용한다.
- 42–45·71–74: 두 경로는 자식 유의성에 SIGNIFICANT만 쓴다. 자식의 d_norm_details를 갱신하거나 유의성을 지우는 문장은 없다.
- 16·49: 커널 입구의 idx>=num_threads 조기 반환 뒤 단일 블록 경로에는 __syncthreads()가 있다.
- 87–88: 템플릿 인스턴스화용 함수의 두 커널 실행 구성은 모두 <<<1,1>>>로 고정된다.
