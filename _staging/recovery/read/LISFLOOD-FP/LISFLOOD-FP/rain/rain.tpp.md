---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/rain/rain.tpp
lines: 245
sha256: 2a3c1051513079423393446af2078260108f417ad08dc4b0dab275cbff5bbc61
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rain.tpp — 판독 구간 기록

구간은 1행부터 245행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | rain.h·file_tool.h·utility.h를 포함한다(1–3). 허용오차는 `static const NUMERIC_TYPE epsilon = C(1e-12);` (5)이다. 템플릿 생성자는 allocator_를 인수로 초기화한다(7–16). `enabled_ = (strlen(filename) > 0);` (17)로 사용 여부를 계산하며 `if (!enabled_) return;` (18)이면 반환한다. read_file_netCDF_start로 rainfall_depth를 열고 `netcdf_.data = allocator_.allocate(netcdf_.xlen * netcdf_.ylen);` (21)로 자료 공간을 확보한다. xsz·ysz를 차원에서 복사하고 `geometry_.dx = netcdf_.xs[1] - netcdf_.xs[0];` (25), `geometry_.dy = netcdf_.ys[0] - netcdf_.ys[1];` (26), `geometry_.blx = netcdf_.xs[0] - geometry_.dx/C(2.0);` (27), `geometry_.tly = netcdf_.ys[0] + geometry_.dy/C(2.0);` (28), `geometry_.bly = geometry_.tly - geometry_.ysz*geometry_.dy;` (29)로 격자 간격과 원점을 계산한다. update_time(C(0.0))을 호출한다(31). 이 파일 자체의 1–163행에는 전처리 조건이 없다. 포함 여부는 rain.cpp의 _NETCDF 분기에 달린다. |
| 34–56 | has_same_origin의 반환식은 `return FABS(Parptr->blx - geometry_.blx) < epsilon &&` (40), `FABS(Parptr->bly - geometry_.bly) < epsilon;` (41)이다. is_tile_size_multiple_of_grid는 `NUMERIC_TYPE dx_ratio = geometry_.dx / Parptr->dx;` (50), `NUMERIC_TYPE dy_ratio = geometry_.dy / Parptr->dy;` (51)로 간격비를 구하고 `return FABS(round(dx_ratio) - dx_ratio) <= epsilon &&` (53), `FABS(round(dy_ratio) - dy_ratio) <= epsilon;` (54)로 반올림 값과의 차이를 epsilon 이하로 검사한다. 두 함수는 NUMERIC_TYPE 및 C 매크로를 그대로 사용한다. |
| 57–77 | update_time에서 `if (!enabled_) return;` (63)이면 반환한다. `if (read_file_netCDF(&netcdf_, t / C(3600.0) /* s to hr */))` (65)가 참일 때 `netcdf_.dt *= C(3600.0); // hr to s` (67)로 시간 간격을 시간 단위에서 초로 바꾼다. `for (int i=0; i<geometry_.xsz*geometry_.ysz; i++)` (70)에서 `netcdf_.data[i] /= netcdf_.dt;` (72), `netcdf_.data[i] /= C(1000.0); // mm to m` (73)으로 누적 강우 mm를 m/s 강우율로 바꾼다. 루프·분기·함수를 닫는다(74–76). |
| 78–102 | update_time_SGC는 `if (!enabled_) return (false);` (84)이면 false를 반환한다. `time_updated = read_file_netCDF(&netcdf_, t / C(3600.0) /* s to hr */);` (87)로 netCDF 판독 결과를 얻고 `if (time_updated)` (88)에서 `netcdf_.dt *= C(3600.0); // hr to s` (90)으로 시간 간격을 변환한다. `for (int i=0; i<geometry_.xsz*geometry_.ysz; i++)` (93)에서 `netcdf_.data[i] /= netcdf_.dt;` (95), `netcdf_.data[i] /= C(1000.0); // mm to m` (96)으로 강우율을 변환한다. 분기 밖에서 time_updated를 반환한다(99–100). |
| 103–128 | rate_at_cell은 `if (!enabled_) return C(0.0);` (111)이면 0을 반환한다. `int tile_i = i * Parptr->dx / geometry_.dx;` (113), `NUMERIC_TYPE top_gap = Parptr->tly - geometry_.tly;` (115), `int tile_j = (j - top_gap/Parptr->dy) * Parptr->dy / geometry_.dy;` (116)으로 타일 정수 인덱스를 계산한다. `if (tile_i < geometry_.xsz && tile_j >= 0)` (118)이면 `return netcdf_.data[tile_j*geometry_.xsz + tile_i];` (120)을 반환하고 `else` (122)에서는 C(0.0)을 반환한다(124). |
| 129–155 | rate_at_cell_SGC는 `if (!enabled_) return C(0.0);` (139)이면 0을 반환한다. `int tile_i = i * dx_col / geometry_.dx;` (141), `NUMERIC_TYPE top_gap = tly - geometry_.tly;` (143), `int tile_j = (j - top_gap/dy_col) * dy_col / geometry_.dy;` (144)로 전달된 행 간격과 tly를 사용해 타일 인덱스를 계산한다. `if (tile_i < geometry_.xsz && tile_j >= 0)` (146)이면 `return netcdf_.data[tile_j*geometry_.xsz + tile_i];` (148)을 반환하고 `else` (150)에서는 C(0.0)을 반환한다(152). |
| 156–186 | update_H의 계산 블록은 `#if _NETCDF == 1` (164)인 경우 컴파일된다. 그 안에서 `if (!enabled_) return;` (165)이면 반환하고 update_time(Solverptr->t)을 호출한다(167). 합산값을 0으로 초기화한다(168). OpenMP 지시는 `#pragma omp parallel for reduction (+:total_rain_mass)` (169)이며 `for (int j=0; j<Parptr->ysz; j++)` (170)과 `for(int i=0; i<Parptr->xsz; i++)` (172)의 두 루프에서 DEM과 H를 참조한다(174·177). `if (FABS(Z - Parptr->nodata_elevation) < 1e-6) continue;` (175)로 무자료 셀을 건너뛰고 `NUMERIC_TYPE inc = rate_at_cell(Parptr, i, j) * Solverptr->Tstep;` (178), `H += inc;` (179), `total_rain_mass += inc*Parptr->dA;` (180)으로 수심·강우 체적을 누적한다. `#endif` (183) 뒤의 `Parptr->RainTotalLoss += total_rain_mass;` (184)는 _NETCDF 조건 밖에 있다. |
| 187–215 | update_rain_grid_SGM의 인수는 188–200행이다. `#if _NETCDF == 1` (202)인 경우 본문을 컴파일하고 `if (!enabled_) return;` (203)이면 반환한다. update_time 호출은 주석 처리되어 있다(205). `if (update_time_SGC(curr_time)); // if the file had to be read update rain_grid` (206) 뒤 207행의 별도 블록에서 `for (int j = 0; j < grid_rows; j++)` (208)을 수행한다. fp_vol에 dem_data의 범위를 복사하고 시작·끝을 가져온다(211–213). 행 오프셋은 `int grid_row_index = j * grid_cols_padded;` (214)이다. |
| 216–234 | 시작 시 188행 update_rain_grid_SGM·202행 _NETCDF == 1 분기·207행 별도 블록·208행 j 루프 안. `#ifdef __INTEL_COMPILER` (216)일 때 `__assume_aligned(rain_grid, 64);` (217)을 적용하고 `#endif` (218)로 닫는다. __INTEL_COMPILER가 정의되지 않은 경우 이 정렬 가정만 제외된다. `#pragma ivdep` (219) 뒤 `for (int i = row_start; i < row_end; i++)` (220)에서 `int grid_cell_index = grid_row_index + i;` (222)로 셀 오프셋을 구한다. 행별 dx_col·dy_col을 복사한다(223–224). `if (dem_grid[grid_cell_index] != DEM_NO_DATA)` (225)일 때 `rain_grid[grid_cell_index] = rate_at_cell_SGC(i, j,row_dx, row_dy, tly)*cell_area_col[j];` (227)로 강우율과 셀 면적을 곱한다. 루프·별도 블록을 닫고 `#endif` (232) 뒤 함수를 닫는다(233–234). |
| 235–245 | 소멸자는 별도의 _NETCDF 조건 없이 정의된다(236–238). `if (!enabled_) return;` (239)이면 반환한다. free로 xs·ys·times를 해제하고(240–242), `allocator_.deallocate(netcdf_.data, netcdf_.xlen * netcdf_.ylen);` (243)으로 자료를 할당자에 반환한 뒤 CloseNetCDF를 호출한다(244). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–26: x·y 좌표의 [1]을 참조한다. 이 생성자 안에는 차원 길이가 2 이상인지 검사하는 분기가 없다.
- 113–124·141–152: 두 셀 강우율 함수의 조건은 tile_i < geometry_.xsz && tile_j >= 0이다. 같은 조건에 tile_i >= 0과 tile_j < geometry_.ysz 검사는 없다.
- 164–184: total_rain_mass 선언은 #if _NETCDF == 1 안에 있고 해당 변수의 RainTotalLoss 누적은 #endif 뒤에 있다. 이 파일을 포함하는 rain.cpp는 _NETCDF == 1일 때 rain.tpp를 선택한다.
- 206–231: `if (update_time_SGC(curr_time)); // if the file had to be read update rain_grid` (206)은 끝에 세미콜론이 있다. 뒤 207–231행은 if의 참 분기 본문이 아닌 별도 블록이다.
- 225–228: DEM_NO_DATA인 셀에는 rain_grid 대입이 없다. 이 함수에는 그 셀의 이전 rain_grid 값을 지우는 문장도 없다.
- 243: 자료 해제 개수는 netcdf_.xlen * netcdf_.ylen이다. 생성자의 할당 크기도 같은 곱이다(21).
