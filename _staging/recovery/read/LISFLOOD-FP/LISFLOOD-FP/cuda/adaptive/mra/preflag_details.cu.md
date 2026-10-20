---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/preflag_details.cu
lines: 94
sha256: 493d98786bf154fdb88be40e2eaf8b7387db89715ce40badb400b75e7125231f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# preflag_details.cu — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | preflag_details.cuh 포함과 빈 줄(1–2). `__host__` (3)인 preflag_details는 Boundaries, PointSources, StagePoints, SimulationParams, SolverParams, num_details, max_ref_lvl, test_case를 const 참조로 받고 bool 포인터를 반환한다(4–15). `size_t bytes = num_details * sizeof(bool);` (16)로 저장 크기를 계산한다. `bool* h_preflagged_details = new bool[num_details]();` (18)는 호스트(host) 표시 배열을 값 초기화하여 false로 채운다. `bool* d_preflagged_details = (bool*)malloc_device(bytes);` (20)로 장치(device) 배열을 할당한다. `HierarchyIndex starting_idx = get_lvl_idx(max_ref_lvl - 1);` (22)로 표시할 수준(level)의 시작 인덱스를 얻는다. 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 23–40 | 시작 시 4–15행 preflag_details 함수 안. `for (int i = 0; i < stage_points.num_points; i++)` (24)에서 `MortonCode child_idx = stage_points.codes[i] / 4; // to get Morton code one level below` (26)로 모턴 코드(Morton code)를 한 수준 아래로 바꾼다. `h_preflagged_details[starting_idx + child_idx] = true;` (28)로 관측점의 표시를 설정한다. 별도의 `if (nullptr != boundaries.north.codes)` (31) 안에서 `for (int i = 0; i < boundaries.north.num_cells(); i++)` (33)를 돈다. `MortonCode child_idx = boundaries.north.codes[i] / 4;` (35), `h_preflagged_details[starting_idx + child_idx] = true;` (37)로 북쪽 경계 셀을 표시한다. 두 루프·조건 끝과 빈 줄도 포함한다(29·38–40). |
| 41–60 | 시작 시 4–15행 preflag_details 함수 안이며 31행 북쪽 조건 밖. `if (nullptr != boundaries.east.codes)` (41) 안의 `for (int i = 0; i < boundaries.east.num_cells(); i++)` (43)에서 `MortonCode child_idx = boundaries.east.codes[i] / 4;` (45), `h_preflagged_details[starting_idx + child_idx] = true;` (47)로 동쪽 경계 셀을 표시한다. 별도의 `if (nullptr != boundaries.south.codes)` (51) 안의 `for (int i = 0; i < boundaries.south.num_cells(); i++)` (53)에서 `MortonCode child_idx = boundaries.south.codes[i] / 4;` (55), `h_preflagged_details[starting_idx + child_idx] = true;` (57)로 남쪽 경계 셀을 표시한다. 각 조건·루프 끝과 빈 줄도 포함한다. |
| 61–77 | 시작 시 4–15행 preflag_details 함수 안이며 51행 남쪽 조건 밖. `if (nullptr != boundaries.west.codes)` (61) 안의 `for (int i = 0; i < boundaries.west.num_cells(); i++)` (63)에서 `MortonCode child_idx = boundaries.west.codes[i] / 4;` (65), `h_preflagged_details[starting_idx + child_idx] = true;` (67)로 서쪽 경계 셀을 표시한다. 이 조건 밖의 `for (int i = 0; i < point_sources.num_srcs; i++)` (71)에서 `MortonCode child_idx = point_sources.h_codes[i] / 4;` (73), `h_preflagged_details[starting_idx + child_idx] = true;` (75)로 점 공급원(point source)을 표시한다. 각 조건·루프 끝과 빈 줄도 포함한다. |
| 78–94 | 시작 시 4–15행 preflag_details 함수 안이며 앞의 모든 루프 밖. `if (test_case == 0 && solver_params.refine_wall)` (78)이면 refine_high_wall에 sim_params, solver_params, max_ref_lvl, h_preflagged_details를 전달한다(80–86). 이 조건을 닫은 뒤 `copy_cuda(d_preflagged_details, h_preflagged_details, bytes);` (89)로 전체 표시를 장치 배열에 복사한다. delete[]로 호스트 배열을 해제하고 장치 배열 포인터를 반환한다(91·93). 빈 줄과 함수 끝도 포함한다(87–88·90·92·94). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·22–75: 호스트 표시 배열의 길이는 num_details이다. 관측점·경계·점 공급원 표시에 사용하는 starting_idx + child_idx와 num_details를 비교하는 조건문은 이 함수에 없다.
