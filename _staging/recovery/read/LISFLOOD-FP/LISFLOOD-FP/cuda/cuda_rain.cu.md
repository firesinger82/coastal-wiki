---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_rain.cu
lines: 114
sha256: 07b4c37c37665758f6a5b0693fc3549a0b21f37a6fd735684daf4f035930e440
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_rain.cu — 판독 구간 기록

구간은 1행부터 114행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | rain·DynamicRain·UnifiedAllocator 헤더(1–3). `#if _NETCDF == 1` (5)이면 rain.tpp 포함(6), `#else` (7)는 rain_stub.tpp 포함(8), `#endif` (9). `template class DynamicRain<lis::cuda::UnifiedAllocator<NUMERIC_TYPE>>;` (11)로 명시적 인스턴스화(explicit instantiation). 이 파일 안에는 _NETCDF 값 정의가 없다. |
| 13–36 | 전처리 조건 밖의 `__device__` (13) rate_at_cell(14–19). `int tile_i = (i-1) * cuda::geometry.dx / cuda::rain_geometry.dx;` (21), `NUMERIC_TYPE top_gap = cuda::geometry.tly - cuda::rain_geometry.tly;` (23), `int tile_j = (j-1 - top_gap/cuda::geometry.dy) *` (24), `cuda::geometry.dy / cuda::rain_geometry.dy;` (25). `if (tile_i < cuda::rain_geometry.xsz && tile_j >= 0)` (27)는 `return rain_data[tile_j*cuda::rain_geometry.xsz + tile_i];` (29), `else` (31)는 `return C(0.0);` (33). |
| 37–64 | `__global__ void` (37), `__launch_bounds__(CUDA_BLOCK_SIZE)` (38)의 lis::cuda::DynamicRain::update(39–44). 본문은 `#if _NETCDF == 1` (46)에서만 실행 코드를 포함한다. `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (47), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (48). `for (int j=global_j+1; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (50), `for (int i=global_i+1; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (52)에서 DEM[j*cuda::pitch+i] 복사(54). `if (FABS(Z - cuda::solver_params.nodata_elevation) < C(1e-6)) continue;` (55). H[j*cuda::pitch+i] 참조(57), `Hval += rate_at_cell(rain_data, i, j) * cuda::dt;` (58). `#endif` (61), 함수 종료·빈 줄(62–64). _NETCDF==1이 아니면 본문은 비어 있다. |
| 65–88 | 전처리 조건 밖의 `__device__` (65) rate_at_cell_ACC(66–71). `int tile_i = (i) * cuda::geometry.dx / cuda::rain_geometry.dx;` (73), `NUMERIC_TYPE top_gap = cuda::geometry.tly - cuda::rain_geometry.tly;` (75), `int tile_j = (j - top_gap/cuda::geometry.dy) *` (76), `cuda::geometry.dy / cuda::rain_geometry.dy;` (77). `if (tile_i < cuda::rain_geometry.xsz && tile_j >= 0)` (79)는 `return rain_data[tile_j*cuda::rain_geometry.xsz + tile_i];` (81), `else` (83)는 `return C(0.0);` (85). |
| 89–114 | `__global__ void` (89), `__launch_bounds__(CUDA_BLOCK_SIZE)` (90)의 lis::cuda::DynamicRain::updateACC(91–96). `#if _NETCDF == 1` (98) 안에서 `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (99), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (100). `for (int j=global_j; j<cuda::geometry.ysz; j+=blockDim.y*gridDim.y)` (102), `for (int i=global_i; i<cuda::geometry.xsz; i+=blockDim.x*gridDim.x)` (104)에서 DEM[j*cuda::geometry.xsz+i] 복사(106). `if (FABS(Z - cuda::solver_params.nodata_elevation) < C(1e-6)) continue;` (107). H[j*cuda::geometry.xsz+i] 참조(109), `Hval += rate_at_cell_ACC(rain_data, i, j) * cuda::dt;` (110). `#endif` (113), 함수 종료(114). _NETCDF==1이 아니면 본문은 비어 있다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–29·73–81: 강우 셀 접근 조건은 tile_i<xsz와 tile_j>=0만 검사한다. tile_i>=0 및 tile_j<ysz 검사는 두 함수에 없다.
- 21·73: tile_i 계산은 x방향 격자 간격 비를 사용하며 이 파일에는 두 격자의 x원점 차이를 더하는 식이 없다.
- 54–58·106–110: 일반 갱신은 DEM·H 행 간격에 cuda::pitch를 쓴다. ACC 갱신은 두 배열 모두 geometry.xsz를 쓴다.
