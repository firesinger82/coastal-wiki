---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_boundary.cuh
lines: 197
sha256: a44a377707147e6b265a730498e6138de9f09f38c843c39cdf187a7968844713
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_boundary.cuh — 판독 구간 기록

구간은 1행부터 197행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | `#pragma once` (1), stats·cuda_flow·lisflood 헤더(2–4), lis::cuda 이름 공간(namespace)(6–9). 시계열(time series) TimeSeries는 count, `NUMERIC_TYPE* __restrict__ time;` (14), `NUMERIC_TYPE* __restrict__ value;` (15), current_value를 가진다(11–17). 이 파일에는 전처리 조건 분기가 없다. |
| 19–37 | BoundaryConditions 형식. 경계는 BC_count·BC_type·BC_value·BC_time_series(21–25), 점원(point source)은 PS_count·PS_type·PS_value·PS_time_series·PS_idx(27–32), 공유 시계열은 all_time_series·time_series_count(34–35)를 가진다. 모든 배열 포인터에 __restrict__를 붙인다(23–25·29–34). |
| 38–91 | Boundary 구조체 시작(38–39). initialise는 BoundaryConditions·BoundCs 참조 및 pitch·offset(40–46), update_time_series는 t(48–51), update_point_sources는 H·DEM·MassStats 포인터(53–58), update_H는 H·DEM·Qx·Qy·MassStats·dim3 grid_size·drycheck(60–69)를 받는 static 함수다. drain_nodata_water(71–77)·drain_nodata_waterACC(79–85)는 H·DEM·MassStats·grid_size를 받는다. free_device는 BoundaryConditions 참조를 받는다(87–90). |
| 92–125 | 시작 시 38행 Boundary 구조체 안. `__device__ static FlowVector outside_x` (92), `__device__ static FlowVector outside_y` (101)는 U_const·U_inside·bc_i·HU_sign·Zstar를 받는다(93–108). `__device__ static FlowVector inside_x` (110), `__device__ static FlowVector inside_y` (118)는 U_outside·U_const·U_inside·bc_i를 받는다(111–124). |
| 126–173 | 시작 시 38행 Boundary 구조체 안. `__device__ static int index_w` (126), `__device__ static int index_e` (132), `__device__ static int index_n` (138), `__device__ static int index_s` (144), `__device__ static int index_w_ACC` (150), `__device__ static int index_e_ACC` (156), `__device__ static int index_n_ACC` (162), `__device__ static int index_s_ACC` (168)의 원형. 각 함수는 const int i·j를 받는다(127–172). |
| 174–197 | 시작 시 38행 Boundary 구조체 안. private(174) 아래 initialise_all_time_series(175–179)·initialise_BC(181–185)는 BoundaryConditions·BoundCs 참조를 받는다. initialise_PS(187–193)는 두 참조와 pitch·offset을 받는다. 구조체·이름 공간 종료(194–197). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11–36: TimeSeries와 BoundaryConditions의 필드에는 기본값 초기화가 없다.
