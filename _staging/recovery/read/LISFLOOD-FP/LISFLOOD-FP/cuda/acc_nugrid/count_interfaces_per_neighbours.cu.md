---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/count_interfaces_per_neighbours.cu
lines: 150
sha256: cb158e032aabd653e8446be617dbd4440b97c889e38386d5bf749629275698ec
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# count_interfaces_per_neighbours.cu — 판독 구간 기록

구간은 1행부터 150행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 헤더 포함(1), CUDA 커널(kernel) `__global__ void lis::cuda::acc_nugrid::count_interfaces_per_neighbours` (3) 정의(4–8). 전처리 조건 분기는 없다. 스레드 인덱스는 `int idx = blockIdx.x * blockDim.x + threadIdx.x;` (9), 범위 검사는 `if (idx >= d_non_uniform_nghbrs.length) return;` (11). 접면(interface) 수는 0에서 시작하며 이웃 방향과 소유 요소 인덱스를 읽는다(13–19). |
| 21–64 | 시작 시 3행 커널 안. `for (int i = 0; i < d_assem_sol.nghbr_counts[owner_elem_idx]; i++)` (21)로 소유 요소의 모든 이웃 접면을 순회한다. `int owner_itrfaces_idx = d_assem_sol.cumu_nghbr_counts[owner_elem_idx] + i;` (23)로 접면 인덱스를 구하고 방향을 읽는다(25). 수직 접면 선택식은 `bool vertical =`<br>`(`<br>`(`<br>`nghbr_dir == I_EAST`<br>`\|\|`<br>`nghbr_dir == I_WEST`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_NORTH`<br>`\|\|`<br>`interface_dir == I_SOUTH`<br>`)`<br>`);` (27–40). 수평 접면 선택식은 `bool horizontal =`<br>`(`<br>`(`<br>`nghbr_dir == I_NORTH`<br>`\|\|`<br>`nghbr_dir == I_SOUTH`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_EAST`<br>`\|\|`<br>`interface_dir == I_WEST`<br>`)`<br>`);` (42–55). `if (vertical \|\| horizontal) interface_count++;` (57)로 현재 이웃 방향에 직교하는 접면을 센다. 루프 종료·구분 주석·빈 줄(58–64). |
| 65–92 | 시작 시 3행 커널 안. 이웃 활성 인덱스를 읽는다(65). 고스트 셀(ghost cell)은 같은 해상도에서 접면 둘을 더한다는 주석(69–70)이 있지만 `if (nghbr_act_idx < 0)` (71) 안의 개수 저장문은 주석이고 곧바로 return한다(73–74). 내부 이웃은 요소 인덱스를 0으로 시작하고 `for (int i = 0; i < d_assem_sol.length; i++)` (81)에서 현재 i를 저장하고 활성 인덱스를 읽는다(83–85). `if (nghbr_act_idx == soln_act_idx) break;` (87)로 일치 시 탐색을 끝낸다. 찾은 인덱스를 `nghbr_elem_idcs[idx]`에 저장한다(90–91). |
| 93–132 | 시작 시 3행 커널 안. `for (int i = 0; i < d_assem_sol.nghbr_counts[nghbr_elem_idx]; i++)` (93)로 이웃 요소의 접면을 순회한다. `int nghbr_itrfaces_idx = d_assem_sol.cumu_nghbr_counts[nghbr_elem_idx] + i;` (95)와 방향 읽기(97)를 수행한다. 수직 선택식은 `bool vertical =`<br>`(`<br>`(`<br>`nghbr_dir == I_EAST`<br>`\|\|`<br>`nghbr_dir == I_WEST`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_NORTH`<br>`\|\|`<br>`interface_dir == I_SOUTH`<br>`)`<br>`);` (99–112). 수평 선택식은 `bool horizontal =`<br>`(`<br>`(`<br>`nghbr_dir == I_NORTH`<br>`\|\|`<br>`nghbr_dir == I_SOUTH`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_EAST`<br>`\|\|`<br>`interface_dir == I_WEST`<br>`)`<br>`);` (114–127). `if (vertical \|\| horizontal) interface_count++;` (129)로 소유 요소에서 센 수에 직교 접면 수를 더한다. 루프 종료와 구분 주석(130–132). |
| 133–150 | 시작 시 3행 커널 안. 접면 개수를 `itrface_counts[idx]`에 저장한다(134). 수심·지형 값의 부호 플래그 설정 주석(136). `if (nghbr_dir == I_EAST \|\| nghbr_dir ==  I_SOUTH)` (138)는 owner=1, neighbour=-1을 설정한다(140–141). `else if (nghbr_dir == I_WEST \|\| nghbr_dir == I_NORTH)` (143)는 owner=-1, neighbour=1을 설정한다(145–146). 분기·커널 종료와 구분 주석(147–150). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 69–75·134–146: 고스트 이웃 분기는 접면 수 저장문이 주석이며 곧바로 반환한다. 이 분기는 뒤의 접면 수와 부호 플래그 저장에 도달하지 않는다.
- 79–91: 이웃 활성 인덱스 탐색에는 찾지 못한 경우를 구분하는 변수가 없다. 해 길이가 양수이고 일치 항목이 없으면 마지막 순회 인덱스를 저장한다.
