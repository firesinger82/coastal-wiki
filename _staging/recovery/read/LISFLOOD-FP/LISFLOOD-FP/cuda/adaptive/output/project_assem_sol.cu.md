---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/project_assem_sol.cu
lines: 77
sha256: 5043c4ce5029338750e691c3d38b918c5f9620411b37eae7cbf3b3c4e0209278
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# project_assem_sol.cu — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–30 | 헤더 포함과 CUDA 호스트 함수(host function) `project_assem_sol` 정의이다(1–16). 격자 크기·유의 상세 표시(significant detail)·척도 계수(scale coefficients)·작업 해·해석기 매개변수·Morton 코드(Morton code) 배열·현재 해·출력 해를 받는다(6–14). 해 길이에 맞는 블록 수를 계산하고 `reinsert_assem_sol` 커널(kernel)을 실행한다(17–25). 최세 원소 수·트리 순회(tree traversal) 스레드 수·블록 수를 계산한다(27–29). 전처리 조건 분기는 없다. `THREADS_PER_BLOCK`의 값은 이 파일에서 정의하지 않는다. 원문: `__host__` (3); `int num_blocks_sol = get_num_blocks(d_assem_sol.length, THREADS_PER_BLOCK);` (17); `reinsert_assem_sol<<<num_blocks_sol, THREADS_PER_BLOCK>>>`<br>`(`<br>`d_assem_sol,`<br>`d_assem_sol.act_idcs,`<br>`d_scale_coeffs,`<br>`solver_params`<br>`);` (19–25); `int num_finest_elems      = mesh_dim * mesh_dim;`<br>`int num_threads_traversal = num_finest_elems / 4;`<br>`int num_blocks_traversal  = get_num_blocks(num_threads_traversal, THREADS_PER_BLOCK);` (27–29). |
| 31–58 | 시작 시 3–16행 `project_assem_sol` 안. 출력 해 길이를 최세 원소 수로 설정한다(31). `traverse_tree_of_sig_details`와 `load_soln_coeffs` 커널을 실행한다(33–47). `rev_z_order_assem_sol`에 역순서 배열·인덱스·작업 해·출력 해·최세 원소 수를 전달하여 정렬 순서를 되돌린다(49–56). 함수 종료와 빈 줄을 포함한다(57–58). 원문: `traverse_tree_of_sig_details<<<num_blocks_traversal, THREADS_PER_BLOCK>>>`<br>`(`<br>`d_sig_details,`<br>`d_scale_coeffs,`<br>`d_buf_assem_sol,`<br>`num_threads_traversal,`<br>`solver_params`<br>`);` (33–40); `load_soln_coeffs<<<get_num_blocks(num_finest_elems, THREADS_PER_BLOCK), THREADS_PER_BLOCK>>>`<br>`(`<br>`d_buf_assem_sol,`<br>`d_scale_coeffs,`<br>`num_finest_elems`<br>`);` (42–47). |
| 59–77 | CUDA 커널 `load_soln_coeffs` 정의이다(59–66). 전체 인덱스를 계산하고 최세 원소 수 이상이면 반환한다(67–69). 활성 계층 인덱스(hierarchy index)를 읽는다(71). 척도 계수의 수면고에서 지형을 빼 수심 평균을 만들고 두 유량·지형 평균을 복사한다(73–77). 원문: `__global__` (59); `int idx = blockDim.x * blockIdx.x + threadIdx.x;` (67); `if (idx >= num_finest_elems) return;` (69); `d_assem_sol.h0[idx]  = d_scale_coeffs.eta0[act_idx] - d_scale_coeffs.z0[act_idx];` (73). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–28: 최세 원소 수는 `mesh_dim * mesh_dim`이다. 트리 순회 스레드 수는 이를 정수 4로 나눈 값이다.
- 13–14·31: 출력 해 객체는 값으로 전달한다. 함수 본문은 전달받은 객체의 length 필드를 대입한다.
- 73–76: `load_soln_coeffs` 본문은 수심·두 유량·지형의 평균 계수만 대입한다. x/y 모드 계수 대입문은 없다.
