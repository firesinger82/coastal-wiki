---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/dg2/cuda_dg2_dem.cu
lines: 290
sha256: 28b1a2c2930774e90a989036eb77cc43c346d917252c9842c1b82e4af57f2dd4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dg2_dem.cu — 판독 구간 기록

구간은 1행부터 290행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | DG2 DEM·공통 DEM·기하·solver·util·입출력 헤더를 포함한다(1–6). lis::cuda::dg2 이름공간(namespace)을 연다(8–13). 파일 내부에 전처리 조건 분기는 없다. DEM은 지형고(digital elevation model)이다. |
| 15–36 | `__global__ void initialise_Zstar_x` (15)는 x 방향 면 지형을 초기화한다. `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (21), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (22), `for (int j=global_j+1; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (24), `for (int i=global_i; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (26)이다. `NUMERIC_TYPE Z_neg = DEM.neg_x(j*cuda::pitch + i);` (28), `NUMERIC_TYPE Z_pos = DEM.pos_x(j*cuda::pitch + i+1);` (30), `Zstar_x[j*cuda::pitch + i] = FMAX(Z_neg, Z_pos);` (32)로 양측 재구성값(reconstructed value)의 최대값을 쓴다. |
| 37–62 | `__global__ void initialise_Zstar_y` (37)의 위치는 `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (43), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (44)이다. `for (int j=global_j; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (46), `for (int i=global_i+1; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (48)에서 `NUMERIC_TYPE Z_neg = DEM.neg_y((j+1)*cuda::pitch + i);` (50), `NUMERIC_TYPE Z_pos = DEM.pos_y(j*cuda::pitch + i);` (52), `Zstar_y[j*cuda::pitch + i] = FMAX(Z_neg, Z_pos);` (54)를 계산한다. 커널과 이름공간을 닫는다(55–61). |
| 63–82 | 호스트(host) Topography 생성자는 cuda::Topography::load로 평균 지형 _0을 읽고(74–75), load_slope로 파일명 뒤에 "1x"·"1y"를 붙인 두 기울기(slope)를 읽는다(76–77). zero_perimeter_slopes와 clamp_boundary_values를 호출한다(79–80). |
| 83–110 | load_slope는 `char dem_slope[256];` (93)에 strcpy·strcat으로 이름을 만든다(94–95). lis::GhostRaster::allocate 후 fopen_or_die로 열고 AsciiRaster::read_header·match_cell_dimensions_or_die·read를 호출한다(97–105). 파일을 닫고 배열을 반환한다(106–109). |
| 111–151 | zero_perimeter_slopes의 `for (int j=1; j<geometry.ysz+1; j++)` (117)는 서쪽 i=0·동쪽 `const int i=geometry.xsz+1;` (128)의 내부 인접 셀에서 _1x·_1y를 C(0.0)으로 만든다(122–123·129–130). `for (int i=1; i<geometry.xsz+1; i++)` (134)는 북쪽 j=0·남쪽 `const int j=geometry.ysz+1;` (145)의 내부 인접 셀에서 두 기울기를 C(0.0)으로 만든다(139–140·146–147). |
| 152–192 | clamp_boundary_values의 `for (int j=1; j<geometry.ysz+1; j++)` (158)는 서쪽 가상 셀(ghost cell)에 오른쪽 _0(163), 동쪽 `const int i=geometry.xsz+1;` (169)에 왼쪽 _0을 복사한다(170). `for (int i=1; i<geometry.xsz+1; i++)` (175)는 북쪽에 아래쪽 _0(180), 남쪽 `const int j=geometry.ysz+1;` (186)에 위쪽 _0을 복사한다(187). SQRT(C(3.0)) 기울기를 더하거나 빼는 후속 줄은 주석이다(164·171·181·188). |
| 193–218 | Topography 소멸자는 _0·_1x·_1y를 delete[]로 해제한다(193–198). DeviceTopography::initialise는 cuda::GhostRaster::allocate_device로 세 배열을 할당하고 copy로 호스트 값을 옮긴다(200–211). Zstar_x·Zstar_y도 할당한 뒤 initialise_Zstar_x/y를 호출한다(213–216). |
| 219–228 | DeviceTopography::initialise_Zstar는 initialise_Zstar_x와 initialise_Zstar_y를 호출한다(225–226). |
| 229–274 | `__device__` (229·238·247·256·265) 함수 neg_x·pos_x·neg_y·pos_y·Zdagger이다. 각각 `return _0[idx] + SQRT(C(3.0))*_1x[idx];` (235), `return _0[idx] - SQRT(C(3.0))*_1x[idx];` (244), `return _0[idx] + SQRT(C(3.0))*_1y[idx];` (253), `return _0[idx] - SQRT(C(3.0))*_1y[idx];` (262), `return Zstar - FMAX(C(0.0), -(ETA - Zstar));` (272)를 반환한다. |
| 275–290 | Zstar 초기화 래퍼(wrapper)는 `lis::cuda::dg2::initialise_Zstar_x<<<1, cuda::block_size>>>(Zstar_x, *this);` (277), `lis::cuda::dg2::initialise_Zstar_y<<<1, cuda::block_size>>>(Zstar_y, *this);` (282)를 실행한다. free_device는 cuda::free_device로 _0·_1x·_1y를 해제한다(285–290). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 93–95: 파일명 버퍼 크기는 256이다. strcpy·strcat 앞에는 길이 검사 조건이 없다.
- 100–105: load_slope는 헤더의 no_data_value를 읽는다. 해당 함수는 그 값을 이후 문장에서 참조하지 않는다.
- 213–214·285–290: initialise는 Zstar_x와 Zstar_y를 할당한다. 이 파일의 DeviceTopography::free_device는 두 배열을 해제하지 않는다.
