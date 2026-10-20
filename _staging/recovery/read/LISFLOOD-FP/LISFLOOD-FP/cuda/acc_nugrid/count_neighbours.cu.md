---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/count_neighbours.cu
lines: 129
sha256: cb5484daa0113f19cfeae1f50d7803282d673f1be904e22b0468c4a61567a29e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# count_neighbours.cu — 판독 구간 기록

구간은 1행부터 129행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–37 | 헤더 포함(1), `__global__ void lis::cuda::acc_nugrid::count_neighbours` (3) CUDA 커널(kernel) 정의와 인수(4–11). 전처리 조건 분기는 없다. `int idx = blockIdx.x * blockDim.x + threadIdx.x;` (12), `if (idx >= d_assem_sol.length) return;` (14)로 스레드 인덱스를 구하고 범위를 제한한다. 수준을 읽고 `MortonCode code = d_assem_sol.act_idcs[idx] - get_lvl_idx(level); // MKS: code in level` (18), `MortonCode code_sw = code << (2 * (solver.L - level));` (19), `MortonCode code_ne = code << (2 * (solver.L - level)) ^ (0xFFFFFFFF >> (32 - 2 * (solver.L - level)));` (20)으로 모턴 코드(Morton code)의 남서·북동 끝을 구한다. `int x_sw = compact(code_sw);` (22), `int y_sw = compact(code_sw >> 1);` (23), `int x_ne = compact(code_ne);` (25), `int y_ne = compact(code_ne >> 1);` (26)으로 좌표를 복원한다. `int mesh_dim = 1 << solver.L;` (28), `int side_len = 1 << (solver.L - level);` (30)으로 전체 격자 폭과 셀 한 변의 최세밀 셀 수를 구한다. 이웃 배열 선언은 주석(32), 이전 이웃은 -5, 누적 수는 0으로 시작한다(34–36). |
| 38–59 | 시작 시 3행 커널 안. 북쪽 탐색 `for (int i = 0; i < side_len; i++)` (39)에서 `bool at_border = (y_ne == (pars.ysz - 1));` (41), `int x = x_ne - i;` (43), `bool bc_bound = boundaries.north.bound(x);` (45)로 경계 위치와 구간 포함 여부를 구한다. `index_1D nghbr = (at_border) ? I_NORTH : (y_ne + 1) * mesh_dim + x; // at_border-> nghbr = -1` (47)로 경계 식별자 또는 행 우선 인덱스를 고르고, `index_1D nghbr_ckeck = (nghbr < 0) ? nghbr : d_nghbr_assem_sol.act_idcs[nghbr];` (49)로 활성 인덱스를 얻는다. `bool already_in_list = (nghbr_ckeck == previous_nghbr);` (51)로 직전 이웃과 비교한 뒤 직전 값을 갱신한다(53). `if (!already_in_list \|\| (bc_bound && at_border)) nghbr_count++;` (55)로 새 이웃 또는 경계 구간의 각 최세밀 접면을 센다. 루프 뒤 이전 이웃을 -5로 되돌린다(58). |
| 60–82 | 시작 시 3행 커널 안. 동쪽 탐색 `for (int i = 0; i < side_len; i++)` (61)에서 `bool at_border = (x_ne == (pars.xsz - 1));` (63), `int y = y_ne - i;` (65), `bool bc_bound = boundaries.east.bound(y);` (67). 이웃 식은 `index_1D nghbr = (at_border) ? I_EAST : y * mesh_dim + (x_ne + 1); // at_border-> nghbr = -2` (69), 활성 인덱스 선택은 `index_1D nghbr_ckeck = (nghbr < 0) ? nghbr : d_nghbr_assem_sol.act_idcs[nghbr];` (71), 중복 검사는 `bool already_in_list = (nghbr_ckeck == previous_nghbr);` (73). 직전 값을 갱신하고(75) `if (!already_in_list \|\| (bc_bound && at_border)) nghbr_count++;` (77)로 개수를 더한다. 루프 종료 뒤 이전 이웃은 -5(81). |
| 83–105 | 시작 시 3행 커널 안. 남쪽 탐색 `for (int i = 0; i < side_len; i++)` (84)에서 `bool at_border = (y_sw == 0);` (86), `int x = x_sw + i;` (88), `bool bc_bound = boundaries.south.bound(x);` (90). 이웃 식은 `index_1D nghbr = (at_border) ? I_SOUTH : (y_sw - 1) * mesh_dim + x; // at_border-> nghbr = -3` (92), 활성 인덱스 선택은 `index_1D nghbr_ckeck = (nghbr < 0) ? nghbr : d_nghbr_assem_sol.act_idcs[nghbr];` (94), 중복 검사는 `bool already_in_list = (nghbr_ckeck == previous_nghbr);` (96). 직전 값을 갱신하고(98) `if (!already_in_list \|\| (bc_bound && at_border)) nghbr_count++;` (100)로 개수를 더한다. 루프 종료 뒤 이전 이웃은 -5(104). |
| 106–129 | 시작 시 3행 커널 안. 서쪽 탐색 `for (int i = 0; i < side_len; i++)` (107)에서 `bool at_border = (x_sw == 0);` (109), `int y = y_sw + i;` (111), `bool bc_bound = boundaries.west.bound(y);` (113). 이웃 식은 `index_1D nghbr = (at_border) ? I_WEST : y * mesh_dim + (x_sw - 1); // at_border-> nghbr = -4` (115), 활성 인덱스 선택은 `index_1D nghbr_ckeck = (nghbr < 0) ? nghbr : d_nghbr_assem_sol.act_idcs[nghbr];` (117), 중복 검사는 `bool already_in_list = (nghbr_ckeck == previous_nghbr);` (119). 직전 값을 갱신하고(121) `if (!already_in_list \|\| (bc_bound && at_border)) nghbr_count++;` (123)로 개수를 더한다. 네 방향의 누적 수를 `d_assem_sol.nghbr_counts[idx]`에 저장하고 커널을 닫는다(127–129). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20: 북동 끝 모턴 코드 식은 `0xFFFFFFFF`와 32를 사용한다. `level == solver.L`이면 원문 우측 시프트 수 `32 - 2 * (solver.L - level)`는 32이다.
- 34·58·81·104: 각 방향의 중복 비교 시작값은 -5로 고정한다.
