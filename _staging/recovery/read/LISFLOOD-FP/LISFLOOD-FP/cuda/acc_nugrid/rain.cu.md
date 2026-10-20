---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/rain.cu
lines: 111
sha256: 9e202f2af471c070275ab829b3e2eadfb75aff015162f2c40ad5557e8e917325
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rain.cu — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | rain.cuh·rain.h·통합 할당자(unified allocator)·블록 변수 매크로 헤더를 포함한다(1–4). 조건부 포함 원문은 `#if _NETCDF == 1` (6); `#include "../../rain/rain.tpp"` (7); `#else` (8); `#include "../../rain/rain_stub.tpp"` (9); `#endif` (10)이다. _NETCDF가 1인 분기는 rain.tpp, 1이 아닌 #else 분기는 rain_stub.tpp를 포함한다. `template class DynamicRain<UnifiedAllocator<NUMERIC_TYPE>>;` (12)로 템플릿(template)을 명시적으로 인스턴스화한다. _NETCDF의 값 정의는 이 파일에 없으며 실제 빌드 설정은 이 기록의 판독 대상에 포함하지 않았다. 빈 줄도 포함한다. |
| 14–42 | 6–10행 전처리 분기 밖의 장치 함수(device function) 지정과 반환형·이름은 `__device__` (14); `NUMERIC_TYPE lis::cuda::acc_nugrid::rate_at_cell` (15)이다. 강우 배열, 셀 i·j, dx, Pars, 강우 격자의 가로 수·상단 y·dx·dy를 받는다(16–26). 강우 타일(tile) 위치는 `int tile_i = (i) * dx / dx_rain;` (28) 및 `NUMERIC_TYPE top_gap = pars.tly - tly_rain;` (30); `int tile_j = (j - top_gap/ dx) * dx / dy_rain;` (31)이다. `if (tile_i < xsz_rain && tile_j >= 0)` (33)일 때 `return rain_data[tile_j*xsz_rain + tile_i];` (35)를 반환한다. `else` (37)에서는 `return C(0.0);` (39)를 반환한다. 함수 닫기와 빈 줄을 포함한다(40–42). |
| 43–70 | 6–10행 전처리 분기 밖에서 CUDA 커널(kernel) `__global__` (43); `void lis::cuda::acc_nugrid::update_rain` (44)를 정의한다. 조립 해(assembled solution)·강우 배열·강우 격자 정보·Pars·Solver를 받는다(45–54). `#if _NETCDF == 1` (56) 아래 본문은 _NETCDF == 1에서만 컴파일된다. t_idx에 threadIdx.x를 복사한다(57). `index_1D idx = blockIdx.x * blockDim.x + t_idx;` (58) 및 `if (idx >= d_assem_sol.length) return;` (60)으로 유효 스레드(thread)를 정한다. 격자 크기는 `NUMERIC_TYPE dx = pars.dx * (1 << (solver.L - d_assem_sol.levels[idx]));` (62)이다. level을 읽고(64), `MortonCode code = d_assem_sol.act_idcs[idx] - get_lvl_idx(level); // MKS: code in level` (66) 및 `int i = compact(code);` (68); `int j = compact(code >> 1);` (69)로 Morton 코드(Morton code)와 위치를 구한다. 이 전처리 분기는 다음 구간으로 이어진다. |
| 71–80 | 시작 시 43–55행 update_rain 커널·`#if _NETCDF == 1` (56) 분기 안. Z를 z0에서 읽는다(71). `if (FABS(Z - pars.nodata_elevation) < C(1e-6)) {` (72)의 참 분기는 주석만 둔다(73–74). `else {` (75)에서 `d_assem_sol.h[idx] += rate_at_cell(rain_data, i, j, dx, pars, xsz_rain, tly_rain, dx_rain, dy_rain) * solver.Tstep;` (76)으로 강우율과 시간 간격의 곱을 수심에 더한다. `#endif` (78)로 전처리 분기를 닫는다. 이 분기에는 #else가 없으므로 _NETCDF가 1이 아니면 update_rain 본문의 실행문이 없다. 함수 닫기와 빈 줄을 포함한다(79–80). |
| 81–111 | 전처리 조건 없이 CUDA 커널 `__global__` (81); `void lis::cuda::acc_nugrid::drain_nodata_water` (82)를 정의한다. 조립 해·Pars·Solver를 받는다(83–87). t_idx 복사(90), `index_1D idx = blockIdx.x * blockDim.x + t_idx;` (91) 및 `if (idx >= d_assem_sol.length) return;` (93)으로 인덱스를 제한한다. `NUMERIC_TYPE dx = pars.dx * (1 << (solver.L - d_assem_sol.levels[idx]));` (95)로 dx를 계산한다. level 복사(97)와 `MortonCode code = d_assem_sol.act_idcs[idx] - get_lvl_idx(level); // MKS: code in level` (99)·`int i = compact(code);` (101); `int j = compact(code >> 1);` (102)로 위치를 계산한다. Z를 읽고(104), `if (FABS(Z - pars.nodata_elevation) < C(1e-6)) {` (105)일 때 `d_assem_sol.h[idx] = C(0.0);` (107)로 수심을 0으로 만든다. 닫는 괄호와 빈 줄을 포함한다(108–111). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–39: rate_at_cell의 배열 접근 조건은 tile_i < xsz_rain 및 tile_j >= 0이다. 이 함수에는 tile_i의 하한 또는 tile_j의 상한 검사가 없으며 강우 격자의 세로 크기 인수도 없다.
- 56–78: update_rain의 실행문 전체는 _NETCDF == 1 전처리 분기 안에 있다. 이 분기의 #else는 없다.
- 95–107: drain_nodata_water에서 계산한 dx·i·j는 이후 실행문에서 참조하지 않는다. level과 code는 i·j를 구하는 데 사용한다.
