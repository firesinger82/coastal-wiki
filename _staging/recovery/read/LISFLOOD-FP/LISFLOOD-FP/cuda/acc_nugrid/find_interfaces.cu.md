---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/find_interfaces.cu
lines: 166
sha256: f3ea51da139e04dad0b1eacb3640eaff6d748a0388b650a477cafd66d1a280d7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# find_interfaces.cu — 판독 구간 기록

구간은 1행부터 166행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 헤더 포함(1–2)。CUDA 커널(kernel) `__global__ void lis::cuda::acc_nugrid::find_interfaces` (4) 정의와 인수(5–10). 전처리 조건 분기는 없다. `int idx = blockIdx.x * blockDim.x + threadIdx.x;` (11), `if (idx >= d_non_uniform_nghbrs.length) return;` (13)으로 스레드 인덱스와 범위를 정한다. 누적 접면(interface) 시작 위치와 이웃 방향을 읽고(15·17), dx_sum·dx는 `C(0.0)`, count는 0으로 시작한다(19–22). 소유 요소 인덱스를 읽는다(26). 수준·모턴 코드(Morton code)·좌표 계산 블록은 주석이다(28–33). |
| 35–74 | 시작 시 4행 `find_interfaces` 커널 안. `for (int i = 0; i < d_assem_sol.nghbr_counts[owner_elem_idx]; i++)` (35)에서 소유 요소 접면을 순회한다. `int owner_itrfaces_idx = d_assem_sol.cumu_nghbr_counts[owner_elem_idx] + i;` (37)로 접면 인덱스를 구하고 방향을 읽는다(39). 직교 방향 선택식은 `bool vertical =`<br>`(`<br>`(`<br>`nghbr_dir == I_EAST`<br>`\|\|`<br>`nghbr_dir == I_WEST`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_NORTH`<br>`\|\|`<br>`interface_dir == I_SOUTH`<br>`)`<br>`);` (41–54), `bool horizontal =`<br>`(`<br>`(`<br>`nghbr_dir == I_NORTH`<br>`\|\|`<br>`nghbr_dir == I_SOUTH`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_EAST`<br>`\|\|`<br>`interface_dir == I_WEST`<br>`)`<br>`);` (56–69). 이웃 활성 인덱스를 읽는다(73). 루프는 다음 구간으로 이어진다. |
| 75–98 | 시작 시 4행 커널·35행 소유 요소 접면 루프 안. 고스트 접면 처리 TODO 주석(75). `if (nghbr_act_idx < 0)` (76)이면 이웃 요소 인덱스를 0으로 설정하고 return한다(79–80). `if (vertical \|\| horizontal)` (85)이면 소유 접면의 dx를 읽고(87), `dx_sum += dx;` (89)로 폭을 누적한다. dx와 적재 인덱스를 접면 배열에 저장하고 누적 위치·개수를 증가시킨다(91–94). 조건과 소유 요소 루프 종료(95–96), 다음 부분 주석(98). |
| 99–136 | 시작 시 4행 커널 안이며 소유 요소 루프 밖. 이웃 요소 인덱스를 읽고(99), `for (int i = 0; i < d_assem_sol.nghbr_counts[nghbr_elem_idx]; i++)` (101)에서 그 요소의 접면을 순회한다. `int nghbr_itrfaces_idx = d_assem_sol.cumu_nghbr_counts[nghbr_elem_idx] + i;` (103), 방향 읽기(105), 직교 방향 식 `bool vertical =`<br>`(`<br>`(`<br>`nghbr_dir == I_EAST`<br>`\|\|`<br>`nghbr_dir == I_WEST`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_NORTH`<br>`\|\|`<br>`interface_dir == I_SOUTH`<br>`)`<br>`);` (107–120), `bool horizontal =`<br>`(`<br>`(`<br>`nghbr_dir == I_NORTH`<br>`\|\|`<br>`nghbr_dir == I_SOUTH`<br>`)`<br>`&&`<br>`(`<br>`interface_dir == I_EAST`<br>`\|\|`<br>`interface_dir == I_WEST`<br>`)`<br>`);` (122–135). 이 루프는 다음 구간으로 이어진다. |
| 137–153 | 시작 시 4행 커널·101행 이웃 요소 접면 루프 안. `if (vertical \|\| horizontal)` (137)이면 이웃 접면 dx를 읽고(139), `dx_sum += dx;` (141)로 폭을 더한다. dx와 적재 인덱스를 접면 배열에 저장하고 누적 위치·개수를 증가시킨다(143–146). 조건·루프 종료(147–148). 두 요소에서 모은 dx_sum을 이웃 배열에 저장한다(152). |
| 154–166 | 시작 시 4행 커널 안이며 두 접면 루프 밖. 원래 idx를 nghbr에 보존하고 예정 접면 수를 읽은 뒤 idx를 누적 접면 시작 위치로 바꾼다(154–158). `for (int i = 0; i < interface_count; i++)` (160)에서 접면 유량을 `C(0.0)`으로 초기화하고 이웃 번호와 실제 count를 저장한다(162–164). 루프·커널 종료(165–166). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 75–80·152–164: 고스트 접면 처리 TODO가 남아 있다. 고스트 이웃은 이웃 요소 인덱스만 0으로 설정한 뒤 반환하므로 뒤의 dx_sum·접면 유량 초기화에 도달하지 않는다.
- 22·93–94·145–146·156–164: 실제 채운 접면 수 count와 예정 접면 수 interface_count를 각각 사용한다. 두 수가 같은지 검사하는 조건문은 이 커널에 없다.
