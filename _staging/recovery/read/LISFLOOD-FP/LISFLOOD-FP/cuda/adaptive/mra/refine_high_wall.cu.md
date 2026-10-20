---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/refine_high_wall.cu
lines: 57
sha256: 996c3a20e4c4d10af38a85a403554b06aa0d14f1d266aea1f91eb5543389ac40
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# refine_high_wall.cu — 판독 구간 기록

구간은 1행부터 57행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | refine_high_wall.cuh 포함과 빈 줄(1–2). `__host__` (3)인 refine_high_wall은 SimulationParams와 SolverParams의 const 참조, const int max_ref_lvl, bool 포인터 h_preflagged_details를 받는다(4–11). refinement_thickness에 solver_params.ref_thickness를 복사한다(12). `const int num_refined_cells_x = refinement_thickness * sim_params.xsz;` (14), `const int num_refined_cells_y = refinement_thickness * sim_params.ysz;` (15), `const int num_refined_cells   = num_refined_cells_x + num_refined_cells_y;` (16)로 처리할 셀 수를 계산한다. num_refined_cells 길이의 MortonCode 배열을 new[]로 할당한다(18). `Coordinate x_max = sim_params.xsz - 1;` (20), `Coordinate y_max = sim_params.ysz - 1;` (21)로 최대 좌표 인덱스를 구한다. 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 23–34 | 시작 시 4–11행 refine_high_wall 함수 안. 북쪽 벽 세분화(refinement) 주석(23). `for (int j = 0; j < refinement_thickness; j++)` (24)와 그 안의 `for (int i = 0; i < sim_params.xsz; i++)` (26)를 돈다. x에 i를 복사한다(28). `Coordinate y = y_max - j;` (29)로 북쪽에서 안쪽으로 이동한다. `refined_high_wall_codes[j * sim_params.xsz + i] = generate_morton_code(x, y);` (31)로 모턴 코드(Morton code)를 생성해 배열 앞부분에 저장한다. 루프 닫기와 빈 줄도 포함한다(25·27·30·32–34). |
| 35–46 | 시작 시 4–11행 refine_high_wall 함수 안이며 24행 북쪽 루프 밖. 동쪽 벽 세분화 주석(35). `for (int j = 0; j < refinement_thickness; j++)` (36)와 그 안의 `for (int i = 0; i < sim_params.ysz; i++)` (38)를 돈다. `Coordinate x = x_max - j;` (40)로 동쪽에서 안쪽으로 이동하고 y에 i를 복사한다(41). `refined_high_wall_codes[num_refined_cells_x + j * sim_params.ysz + i] = generate_morton_code(x, y);` (43)로 북쪽 코드들 뒤에 동쪽 코드를 저장한다. 루프 닫기와 빈 줄도 포함한다(37·39·42·44–46). |
| 47–57 | 시작 시 4–11행 refine_high_wall 함수 안이며 북쪽·동쪽 루프 밖. `HierarchyIndex starting_idx = get_lvl_idx(max_ref_lvl - 1);` (47)로 표시할 수준(level)의 시작 인덱스를 계산한다. `for (int i = 0; i < num_refined_cells; i++)` (49)에서 `MortonCode child_idx = refined_high_wall_codes[i] / 4; // to get Morton code one level below` (51)로 한 수준 아래 코드를 얻고 `h_preflagged_details[starting_idx + child_idx] = true;` (53)로 표시한다. delete[]로 임시 코드 배열을 해제한다(56). 루프와 함수 닫기, 빈 줄도 포함한다(48·50·52·54–55·57). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–45: 벽 코드 생성 루프는 북쪽과 동쪽에 대해서만 존재한다. 이 함수에는 남쪽·서쪽 벽 코드 생성 루프가 없다.
- 12·24–43: refinement_thickness는 solver_params.ref_thickness를 그대로 사용한다. 이 값을 sim_params.xsz 또는 sim_params.ysz와 비교하여 제한하는 조건문은 이 함수에 없다.
