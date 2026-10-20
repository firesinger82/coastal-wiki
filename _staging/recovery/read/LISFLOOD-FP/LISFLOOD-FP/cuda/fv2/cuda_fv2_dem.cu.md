---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/fv2/cuda_fv2_dem.cu
lines: 162
sha256: 66f208465ff61b0e9d82508a0de9869f164f929070a94057a055873701f81fd7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_fv2_dem.cu — 판독 구간 기록

구간은 1행부터 162행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–35 | 헤더와 lis::cuda::fv2 이름 공간(namespace)(1–13). `__global__ void initialise_Zstar_x` (15). `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (21), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (22), `for (int j=global_j+1; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (24), `for (int i=global_i; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (26). 인접 DEM._0 값을 읽어 계면 지형(interface topography)을 `Zstar_x[j*cuda::pitch + i] = FMAX(Z_neg, Z_pos);` (31)로 정한다. 조건부 전처리 지시는 없다. CMakeLists.txt의 CUDA 조건(73) 아래 소스 목록(102)에 이 파일이 있다. |
| 36–60 | `__global__ void initialise_Zstar_y` (36). `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (42), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (43), `for (int j=global_j; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (45), `for (int i=global_i+1; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (47). j+1과 j의 지형으로 `Zstar_y[j*cuda::pitch + i] = FMAX(Z_neg, Z_pos);` (52). 이름 공간 종료와 빈 줄(57–60). |
| 61–80 | 호스트 지형 생성자(61–76)는 `cuda::Topography::load(filename, geometry, pitch, offset, nodata_elevation, acceleration, verbose)` (72–73)를 호출해 _0를 받는다. acceleration 추가·수정 주석이 있다(68·73). 이어 `clamp_boundary_values(geometry, pitch)` (75)를 호출한다. 빈 줄(77–80). |
| 81–117 | 경계 고정은 `for (int j=1; j<geometry.ysz+1; j++)` (87)에서 서쪽 i=0·동쪽 `const int i=geometry.xsz+1;` (97)에 인접 내부 지형을 복사한다(92·98). `for (int i=1; i<geometry.xsz+1; i++)` (102)에서는 북쪽 j=0·남쪽 `const int j=geometry.ysz+1;` (112)에 j+1·j−1 지형을 복사한다(107·113). |
| 118–138 | Topography 소멸자는 `delete[] _0;` (120). DeviceTopography::initialise는 `cuda::GhostRaster::allocate_device(geometry)`로 _0·Zstar_x·Zstar_y를 할당하고(129·132–133), `cuda::GhostRaster::copy(_0, DEM._0, geometry)` (130), initialise_Zstar_x·initialise_Zstar_y(134–135)를 호출한다. |
| 139–148 | `__device__` (139) `NUMERIC_TYPE lis::cuda::fv2::DeviceTopography::Zdagger` (140)의 반환식은 `return Zstar - FMAX(C(0.0), -(ETA - Zstar));` (146). |
| 149–162 | 초기화 래퍼(wrapper)는 `lis::cuda::fv2::initialise_Zstar_x<<<1, cuda::block_size>>>(Zstar_x, *this);` (151), `lis::cuda::fv2::initialise_Zstar_y<<<1, cuda::block_size>>>(Zstar_y, *this);` (156)를 실행한다. free_device는 `cuda::free_device(_0);` (161)를 호출한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 129–135·159–162: initialise는 _0·Zstar_x·Zstar_y를 할당한다. 이 파일의 free_device는 _0만 해제한다.
- 87–115: 경계 복사 루프는 j=1..ysz와 i=1..xsz를 순회한다. 네 모서리 고스트 셀에 대입하는 문장은 이 루틴에 없다.
