---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/encode_and_thresh_topo.cu
lines: 197
sha256: 95e2a3b1b85ea8a39fa18fc410f4e7429c22dbcb45195fd5ef2d28da5244d5cf
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# encode_and_thresh_topo.cu — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 헤더 포함(1), CUDA 커널(kernel) `__global__ void lis::cuda::acc_nugrid::encode_and_thresh_topo` (3) 정의와 인수(4–14). 전처리 조건 분기는 없다. `index_1D idx = blockIdx.x * blockDim.x + threadIdx.x;` (15), `int num_threads = 1 << (2 * level);` (17), `if (idx >= num_threads) return;` (19)로 해당 수준의 스레드 수와 범위를 정한다. `index_1D prev_lvl_idx = get_lvl_idx(level - 1);` (21), `index_1D curr_lvl_idx = get_lvl_idx(level);` (22), `index_1D next_lvl_idx = get_lvl_idx(level + 1);` (23)로 인접 수준 시작 위치를 얻는다. `index_1D parent_idx = curr_lvl_idx + idx;` (25), `index_1D child_idx  = next_lvl_idx + 4 * idx;` (26)로 부모·자식 위치를 계산한다. |
| 28–81 | 시작 시 3행 `encode_and_thresh_topo` 커널 안. `z0_children`, `z1x_children`, `z1y_children`은 각각 child_idx+0부터 +3까지의 지형 스케일 계수(scale coefficient) 네 개를 읽는다(28–50). 지형 세부 계수(detail coefficient) 계산은 `SubDetail z_details =`<br>`{`<br>`encode_detail_alpha_11(z0_children,z1x_children,z1y_children),`<br>`encode_detail_alpha_21(z0_children,z1x_children,z1y_children),`<br>`encode_detail_alpha_12(z0_children,z1x_children,z1y_children),`<br>`encode_detail_beta_11(z0_children,z1x_children,z1y_children),`<br>`encode_detail_beta_21(z0_children,z1x_children,z1y_children),`<br>`encode_detail_beta_12(z0_children,z1x_children,z1y_children),`<br>`encode_detail_gamma_11(z0_children,z1x_children,z1y_children),`<br>`encode_detail_gamma_21(z0_children,z1x_children,z1y_children),`<br>`encode_detail_gamma_12(z0_children,z1x_children,z1y_children)`<br>`};` (52–63). 결과의 alpha·beta·gamma와 11·21·12 성분을 `d_details.z0`, `.z1x`, `.z1y`의 parent_idx에 복사한다(65–75). 부모 스케일 계수는 `d_scale_coeffs.z0[parent_idx] = encode_scale_11(z0_children, z1x_children, z1y_children);`<br>`d_scale_coeffs.z1x[parent_idx] = encode_scale_21(z0_children, z1x_children, z1y_children);`<br>`d_scale_coeffs.z1y[parent_idx] = encode_scale_12(z0_children, z1x_children, z1y_children);` (77–79). |
| 82–106 | 시작 시 3행 커널 안. `if (non_uniform_n) {` (82)에서 `n0_children`은 조도 자식 네 개를 읽는다(83–89). `n1x_children`, `n1y_children`은 각각 네 성분 모두 `C(0.0)`이다(91–105). 이 분기는 다음 구간으로 이어진다. |
| 107–136 | 시작 시 3행 커널·82행 비균일 조도 참 분기 안. 조도 세부 계수 계산은 `SubDetail n_details =`<br>`{`<br>`encode_detail_alpha_11(n0_children,n1x_children,n1y_children),`<br>`encode_detail_alpha_21(n0_children,n1x_children,n1y_children),`<br>`encode_detail_alpha_12(n0_children,n1x_children,n1y_children),`<br>`encode_detail_beta_11(n0_children,n1x_children,n1y_children),`<br>`encode_detail_beta_21(n0_children,n1x_children,n1y_children),`<br>`encode_detail_beta_12(n0_children,n1x_children,n1y_children),`<br>`encode_detail_gamma_11(n0_children,n1x_children,n1y_children),`<br>`encode_detail_gamma_21(n0_children,n1x_children,n1y_children),`<br>`encode_detail_gamma_12(n0_children,n1x_children,n1y_children)`<br>`};` (107–118). 결과를 `d_details.n0`, `.n1x`, `.n1y`의 alpha·beta·gamma 배열에 복사한다(120–130). 부모 평균 조도는 `d_scale_coeffs.n0[parent_idx] = encode_scale_11(n0_children, n1x_children, n1y_children);` (132). 부모 조도 1차 성분 대입 두 문장은 주석이며 인수는 지형 자식 변수로 적혀 있다(133–134). 비균일 조도 조건 종료(135). |
| 137–161 | 시작 시 3행 커널 안. `if (startfile) {` (137)에서 `h0_children`은 수심 자식 네 개를 읽는다(138–144). `h1x_children`, `h1y_children`은 각각 네 성분 모두 `C(0.0)`이다(146–160). 이 분기는 다음 구간으로 이어진다. |
| 162–192 | 시작 시 3행 커널·137행 시작 파일 참 분기 안. 수심 세부 계수 계산은 `SubDetail h_details =`<br>`{`<br>`encode_detail_alpha_11(h0_children,h1x_children,h1y_children),`<br>`encode_detail_alpha_21(h0_children,h1x_children,h1y_children),`<br>`encode_detail_alpha_12(h0_children,h1x_children,h1y_children),`<br>`encode_detail_beta_11(h0_children,h1x_children,h1y_children),`<br>`encode_detail_beta_21(h0_children,h1x_children,h1y_children),`<br>`encode_detail_beta_12(h0_children,h1x_children,h1y_children),`<br>`encode_detail_gamma_11(h0_children,h1x_children,h1y_children),`<br>`encode_detail_gamma_21(h0_children,h1x_children,h1y_children),`<br>`encode_detail_gamma_12(h0_children,h1x_children,h1y_children)`<br>`};` (162–173). 결과를 `d_details.h0`, `.h1x`, `.h1y`의 alpha·beta·gamma 배열에 복사한다(175–185). 부모 평균 수심은 `d_scale_coeffs.h[parent_idx] = encode_scale_11(h0_children, h1x_children, h1y_children);` (187). 주석 처리된 두 대입문은 `d_scale_coeffs.n1x`, `.n1y`와 지형 자식 변수를 적는다(188–189). 시작 파일 조건 종료(191). |
| 193–197 | 시작 시 3행 커널 안이며 조도·시작 파일 분기 밖. `if ((z_details.get_max() / maxes.z) >= epsilon_local) {` (193)이면 `d_sig_details[parent_idx] = SIGNIFICANT;` (195)로 해당 부모를 유의(significant)하다고 표시한다. 별도 사전 플래그 저장문은 주석(194). 조건과 커널 종료(196–197). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21: `prev_lvl_idx`는 계산 뒤 이 커널에서 참조하지 않는다.
- 82–191·193–195: 조도·수심 세부 계수 계산 분기가 있지만 마지막 유의성 검사는 `z_details.get_max() / maxes.z`만 사용한다. 검사 불성립 때 플래그를 해제하는 else는 없다.
- 193: `maxes.z`를 분모로 사용한다. 이 커널에는 `maxes.z == 0`을 별도로 검사하는 분기가 없다.
