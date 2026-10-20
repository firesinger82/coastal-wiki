---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/preflag_details.cu
lines: 79
sha256: ba81a38035c85db9c5136bd7879c37f307736caea1ae2606477b2785ba900575
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# preflag_details.cu — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 대응 헤더 포함과 preflag_details 정의(1–11). 경계(boundary)·점 유입원(point source)·관측점(gauge point), 상세 계수(detail coefficient) 수 및 최대 세분 레벨을 상수 참조로 받는다(5–9). `size_t bytes = num_details * sizeof(bool);` (12)로 바이트 수를 구한다. `bool* h_preflagged_details = new bool[num_details]();` (14)로 호스트(host) 불리언 배열을 값 초기화한다. `bool* d_sig_details = (bool*)malloc_device(bytes);` (16)으로 장치(device) 배열을 할당한다. `index_1D starting_idx = get_lvl_idx(max_ref_lvl - 1); //hierarchyindex` (18)로 최대 레벨 직전의 계층 시작 인덱스를 구한다. 이 파일 전체에는 조건부 전처리 분기가 없다. |
| 20–36 | 시작 시 3–11행 preflag_details 함수 안. 관측점 반복 조건은 `for (int i = 0; i < gauge_points.num_points; i++)` (20)이다. `MortonCode child_idx = gauge_points.codes[i] / 4; // to get Morton code one level below` (22)로 Morton 코드(Morton code)를 4로 나누고 `h_preflagged_details[starting_idx + child_idx] = true;` (24)로 해당 상세 계수를 사전 표시한다. 이어 `if ( !(NULL == boundaries.north.codes) )` (27)일 때 `for (int i = 0; i < boundaries.north.num_cells(); i++)` (29)에서 `MortonCode child_idx = boundaries.north.codes[i] / 4;` (31)와 `h_preflagged_details[starting_idx + child_idx] = true;` (33)으로 북쪽 경계를 표시한다. 각 반복·조건의 닫기와 빈 줄을 포함한다(25–26·34–36). |
| 37–66 | 시작 시 3–11행 preflag_details 함수 안. 동쪽 경계는 `if ( !(NULL == boundaries.east.codes) )` (37)·`for (int i = 0; i < boundaries.east.num_cells(); i++)` (39) 안에서 `MortonCode child_idx = boundaries.east.codes[i] / 4;` (41)와 `h_preflagged_details[starting_idx + child_idx] = true;` (43)으로 표시한다. 남쪽 경계는 `if ( !(NULL == boundaries.south.codes) )` (47)·`for (int i = 0; i < boundaries.south.num_cells(); i++)` (49) 안에서 `MortonCode child_idx = boundaries.south.codes[i] / 4;` (51)와 `h_preflagged_details[starting_idx + child_idx] = true;` (53)으로 표시한다. 서쪽 경계는 `if ( !(NULL == boundaries.west.codes) )` (57)·`for (int i = 0; i < boundaries.west.num_cells(); i++)` (59) 안에서 `MortonCode child_idx = boundaries.west.codes[i] / 4;` (61)와 `h_preflagged_details[starting_idx + child_idx] = true;` (63)으로 표시한다. 각 분기는 서로 독립이며 닫는 괄호와 빈 줄을 포함한다. |
| 67–79 | 시작 시 3–11행 preflag_details 함수 안. `for (int i = 0; i < point_sources.num_srcs; i++)` (67)에서 `MortonCode child_idx = point_sources.h_codes[i] / 4;` (69)로 점 유입원 코드를 변환하고 `h_preflagged_details[starting_idx + child_idx] = true;` (71)로 표시한다. copy_cuda(d_sig_details, h_preflagged_details, bytes)를 호출한다(74). 호스트 배열을 delete[]로 해제하고 장치 포인터를 반환한다(76–79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·20–71: 레벨 인덱스와 Morton 코드의 몫으로 배열 위치를 정한다. 이 함수에는 max_ref_lvl의 하한이나 계산된 위치와 num_details의 범위를 검사하는 분기가 없다.
