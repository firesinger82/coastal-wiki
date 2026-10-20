---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_all_raster_maps_fv1.cu
lines: 193
sha256: f6c71bc6bee769328c999c35f4e9fef344b5f0eac368c4f8bf33e083d77ecccc
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_all_raster_maps_fv1.cu — 판독 구간 기록

구간은 1행부터 193행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–44 | 헤더 포함과 FV1 래스터 지도(raster map) 출력 함수 정의이다(1–14). 최세 격자 한 변과 셀 수를 계산한다(15–17). 수심·두 유량·두 속도·지형·수면고의 최세 호스트 배열을 할당한다(19–25). 조립 해의 수심·유량·지형 평균 및 활성 인덱스·레벨 배열을 할당한다(27–32). 바이트 수를 계산하고 `copy_cuda`로 장치 배열을 복사한다(34–43). 전처리 조건 분기는 없다. 원문: `const int mesh_dim = 1 << (solver_params.L);` (15); `const int num_finest_cells = mesh_dim * mesh_dim;` (17); `size_t bytes_flow     = d_assem_sol.length * sizeof(real);`<br>`size_t bytes_act_idcs = d_assem_sol.length * sizeof(HierarchyIndex);`<br>`size_t bytes_levels   = d_assem_sol.length * sizeof(int);` (34–36). |
| 45–68 | 시작 시 3–14행 `write_all_raster_maps_fv1` 안. 요소 루프에서 레벨을 읽고 Morton 코드(Morton code)를 계산하여 최세 위치로 비트를 이동한다(45–51). i·j 좌표와 요소의 하위 셀(subcell) 한 변을 계산한다(53–56). j_loc·i_loc 이중 루프에서 최세 배열 인덱스를 구하고 수심·지형 평균을 반복 저장하며 수면고를 더한다(58–66). 유량·속도 선택 계산 주석을 포함한다(68). 원문: `for (int element = 0; element < d_assem_sol.length; element++)` (45); `MortonCode code = act_idcs[element] - get_lvl_idx(level);` (49); `code <<= 2 * (solver_params.L - level);` (51); `Coordinate i = get_i_index(code);`<br>`Coordinate j = get_j_index(code);` (53–54); `int side_len = 1 << (solver_params.L - level);` (56); `for (int j_loc = 0; j_loc < side_len; j_loc++)` (58); `for (int i_loc = 0; i_loc < side_len; i_loc++)` (60); `int idx = (mesh_dim) * (j + j_loc) + (i + i_loc);` (62); `eta[idx]  = h0[element] + z0 [element];` (66). |
| 69–86 | 시작 시 3–14행 함수·45행 element 루프·58행 j_loc 루프·60행 i_loc 루프 안. 속도 또는 유량 출력을 요청했을 때 선택 분기를 연다(69–70). 유량 출력이면 요소 평균 유량을 두 배열에 저장한다(71–75). 속도 출력이면 수심이 허용오차(tolerance)를 초과할 때 평균 유량/수심, 그 외에는 0을 저장한다(77–81). 선택 분기와 세 루프를 닫고 빈 줄을 포함한다(82–86). 원문: `if (plot_params.voutput \|\| plot_params.qoutput)` (69); `if (plot_params.qoutput)` (71); `if (plot_params.voutput)` (77); `vx[idx] = (h0[element] > solver_params.tol_h) ? qx0[element] / h0[element] : C(0.0);`<br>`vy[idx] = (h0[element] > solver_params.tol_h) ? qy0[element] / h0[element] : C(0.0);` (79–80). |
| 87–139 | 시작 시 3–14행 함수 안이며 45행 요소 루프 밖. 수면고·수심 출력이 꺼지지 않았으면 `write_raster_file`로 각각 `elev`·`wd`를 저장한다(87–113). 유량 출력이면 같은 루틴으로 `qx`·`qy`를 저장한다(115–138). 각 호출에는 출력 설정·해당 배열·모의 매개변수·저장 간격·dx_finest·mesh_dim을 전달한다. 빈 줄도 포함한다(100·114·139). 원문: `if (!plot_params.elevoff)` (87); `if (!plot_params.depthoff)` (101); `if (plot_params.qoutput)` (115). |
| 140–178 | 시작 시 3–14행 함수 안. 속도 출력이면 `write_raster_file`로 `vx`·`vy`를 저장한다(140–163). 첫 시간 단계이면 같은 루틴으로 `dem` 지형을 저장한다(165–177). 각 호출에는 출력 설정·해당 배열·모의 매개변수·저장 간격·dx_finest·mesh_dim을 전달한다. 빈 줄도 포함한다(164·178). 원문: `if (plot_params.voutput)` (140); `if (first_t_step)` (165). |
| 179–193 | 시작 시 3–14행 함수 안. 최세 호스트 배열 일곱 개와 조립 해 평균 배열 네 개, 활성 인덱스·레벨 배열을 해제한다(179–192). 함수를 닫는다(193). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·87–176: `dy_finest` 인수는 함수 본문에서 참조하지 않는다. 모든 `write_raster_file` 호출의 격자 간격 인수에는 `dx_finest`를 전달한다.
- 19–25·45–85: 최세 호스트 배열은 값 초기화 없는 `new real[num_finest_cells]`로 할당한다. 각 요소의 하위 셀 루프에서 배열 값을 채우며 별도의 전체 배열 초기화문은 없다.
- 38–43·69–80: 수심·두 유량·지형 평균은 출력 선택과 무관하게 호스트에 복사한다. 두 유량 최세 배열 저장과 속도 계산은 출력 선택 분기 안에서 수행한다.
