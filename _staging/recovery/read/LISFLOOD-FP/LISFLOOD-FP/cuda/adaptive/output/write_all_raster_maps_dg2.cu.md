---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_all_raster_maps_dg2.cu
lines: 262
sha256: 77e6c055a541027dd53edeb9949c92689596a22a1cd9a8cdacde7a62e0d8e245
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_all_raster_maps_dg2.cu — 판독 구간 기록

구간은 1행부터 262행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–45 | 헤더 포함과 DG2 래스터 지도(raster map) 출력 함수 정의이다(1–14). 최세 한 변과 전체 셀 수를 계산한다(15–17). 수심·두 유량·두 속도·지형·수면고의 최세 호스트 배열을 할당한다(19–25). 조립 해 길이의 평균·x/y 모드(mode) 배열과 활성 인덱스·레벨 배열을 할당한다(27–40). CUDA 복사 바이트 수를 계산한다(42–44). 전처리 조건 분기는 없다. 원문: `const int mesh_dim = 1 << (solver_params.L);` (15); `const int num_finest_cells = mesh_dim * mesh_dim;` (17); `size_t bytes_flow     = d_assem_sol.length * sizeof(real);`<br>`size_t bytes_act_idcs = d_assem_sol.length * sizeof(HierarchyIndex);`<br>`size_t bytes_levels   = d_assem_sol.length * sizeof(int);` (42–44). |
| 46–101 | 시작 시 3–14행 `write_all_raster_maps_dg2` 안. `copy_cuda`로 수심·두 유량·지형의 평균/모드와 활성 인덱스·레벨을 호스트에 복사한다(46–59). 요소 루프에서 레벨과 Morton 코드(Morton code)를 구하고 최세 위치로 비트를 이동한다(61–67). `get_i_index`·`get_j_index`로 격자 좌표를 구하며 하위 셀(subcell) 한 변과 단위 간격을 계산한다(69–74). 요소 흐름 계수(FlowCoeffs)와 지형 평면 계수(PlanarCoefficients)를 구성한다(76–100). 원문: `for (int element = 0; element < d_assem_sol.length; element++)` (61); `MortonCode code = act_idcs[element] - get_lvl_idx(level);` (65); `code <<= 2 * (solver_params.L - level);` (67); `Coordinate i = get_i_index(code);`<br>`Coordinate j = get_j_index(code);` (69–70); `int side_len = 1 << (solver_params.L - level);` (72); `real dx_unit = C(1.0) / side_len;` (74). |
| 102–126 | 시작 시 3–14행 함수·61행 element 루프 안. j_loc·i_loc 이중 루프에서 각 최세 셀 중심의 단위 좌표를 계산한다(102–108). 상수·일차 Legendre 기저(Legendre basis)를 구성하고 `eval_loc_face_val_dg2`로 수심과 지형을 평가한다(110–118). 최세 배열 인덱스를 계산하고 수심·지형을 복사하며 수면고를 더한다(120–124). 유량·속도 선택 계산을 알리는 주석도 포함한다(126). 원문: `for (int j_loc = 0; j_loc < side_len; j_loc++)` (102); `real y_unit = j_loc * dx_unit + dx_unit / C(2.0);` (104); `for (int i_loc = 0; i_loc < side_len; i_loc++)` (106); `real x_unit = i_loc * dx_unit + dx_unit / C(2.0);` (108); `LegendreBasis leg_basis =`<br>`{`<br>`C(1.0),`<br>`sqrt( C(3.0) ) * ( C(2.0) * x_unit - C(1.0) ),`<br>`sqrt( C(3.0) ) * ( C(2.0) * y_unit - C(1.0) )`<br>`};` (110–115); `real h_loc_face_val = eval_loc_face_val_dg2(coeffs.h, leg_basis);`<br>`real z_loc_face_val = eval_loc_face_val_dg2(z_planar, leg_basis);` (117–118); `int idx = (mesh_dim) * (j + j_loc) + (i + i_loc);` (120); `eta[idx] = h_loc_face_val + z_loc_face_val;` (124). |
| 127–147 | 시작 시 3–14행 함수·61행 element 루프·102행 j_loc 루프·106행 i_loc 루프 안. 속도 또는 유량 출력이 켜져 있을 때 두 유량을 평가한다(127–130). 유량 출력이면 평가값을 저장한다(132–136). 속도 출력이면 평가 수심이 허용오차(tolerance)를 초과할 때 유량/수심, 그 외에는 0을 저장한다(138–142). 선택 분기와 세 루프를 닫고 빈 줄을 포함한다(143–147). 원문: `if (plot_params.voutput \|\| plot_params.qoutput)` (127); `real qx_loc_face_val = eval_loc_face_val_dg2(coeffs.qx, leg_basis);`<br>`real qy_loc_face_val = eval_loc_face_val_dg2(coeffs.qy, leg_basis);` (129–130); `if (plot_params.qoutput)` (132); `if (plot_params.voutput)` (138); `vx[idx] = (h_loc_face_val > solver_params.tol_h) ? qx_loc_face_val / h_loc_face_val : C(0.0);`<br>`vy[idx] = (h_loc_face_val > solver_params.tol_h) ? qy_loc_face_val / h_loc_face_val : C(0.0);` (140–141). |
| 148–200 | 시작 시 3–14행 함수 안이며 61행 요소 루프 밖. 수면고 출력이 꺼지지 않았으면 `write_raster_file`에 `elev`와 eta를 전달한다(148–160). 수심 출력이 꺼지지 않았으면 `wd`와 h를 전달한다(162–174). 유량 출력이면 `qx`·`qy`를 각각 해당 배열과 함께 저장한다(176–199). 각 호출에는 출력 설정·모의 매개변수·저장 간격·dx_finest·mesh_dim을 전달한다. 빈 줄을 포함한다(161·175·200). 원문: `if (!plot_params.elevoff)` (148); `if (!plot_params.depthoff)` (162); `if (plot_params.qoutput)` (176). |
| 201–239 | 시작 시 3–14행 함수 안. 속도 출력이면 `write_raster_file`로 `vx`·`vy`를 저장한다(201–224). 첫 시간 단계이면 같은 루틴으로 `dem` 지형을 저장한다(226–238). 각 호출에는 출력 설정·모의 매개변수·저장 간격·dx_finest·mesh_dim을 전달한다. 빈 줄을 포함한다(225·239). 원문: `if (plot_params.voutput)` (201); `if (first_t_step)` (226). |
| 240–262 | 시작 시 3–14행 함수 안. 최세 호스트 배열 일곱 개를 해제한다(240–246). 평균·x/y 모드 배열 열두 개와 활성 인덱스·레벨 배열을 해제한다(248–261). 함수를 닫는다(262). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·148–237: `dy_finest` 인수는 함수 본문에서 참조하지 않는다. 모든 `write_raster_file` 호출의 격자 간격 인수에는 `dx_finest`를 전달한다.
- 19–25·61–146: 최세 호스트 배열은 값 초기화 없는 `new real[num_finest_cells]`로 할당한다. 각 요소의 하위 셀 루프에서 배열 값을 채우며 별도의 전체 배열 초기화문은 없다.
- 117·122·140–141: 평가 수심은 최세 수심 배열에 그대로 저장한다. 수심 허용오차 검사는 속도를 계산하는 삼항식(ternary expression)에 있고 수심 자체를 0으로 제한하는 대입은 없다.
