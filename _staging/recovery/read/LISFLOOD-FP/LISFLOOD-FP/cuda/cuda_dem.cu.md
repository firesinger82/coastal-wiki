---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_dem.cu
lines: 153
sha256: dca0271214f47a6bfaf91ddfbd679eea04fc92f0aff8f01c3552db7fe64c70c3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_dem.cu — 판독 구간 기록

구간은 1행부터 153행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | dem·solver·io 헤더(1–3), lis::cuda::fv1 이름 공간(namespace)(5–10). `__global__ void initialise_Zstar_x` (12)는 DEM의 이웃 두 지반고에서 x면 지반고를 만든다. `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (18), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (19). `for (int j=global_j+1; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (21), `for (int i=global_i; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (23)에서 DEM[j*pitch+i]·DEM[j*pitch+i+1] 복사(25–26), `Zstar_x[j*cuda::pitch + i] = FMAX(Z_neg, Z_pos);` (28). 전처리 조건 분기는 없다. |
| 33–57 | 시작 시 5–10행 lis::cuda::fv1 이름 공간 안. `__global__ void initialise_Zstar_y` (33). `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (39), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (40). `for (int j=global_j; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (42), `for (int i=global_i+1; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (44)에서 DEM[(j+1)*pitch+i]·DEM[j*pitch+i] 복사(46–47), `Zstar_y[j*cuda::pitch + i] = FMAX(Z_neg, Z_pos);` (49). 커널(kernel)·이름 공간 종료·빈 줄(50–57). |
| 58–92 | Topography::load는 파일명·Geometry·pitch/offset 참조·nodata_elevation·acceleration·verbose를 받는다(58–67). fopen_or_die의 rb 모드(69), 원래 결측값 0 초기화(70), AsciiRaster::read_header(71). `if (acceleration == 0){` (74)는 GhostRaster::allocate·pitch·offset(75–77), `} else {` (78)는 allocate_H·pitch_ACC·offset_ACC(79–81). AsciiRaster::read(83), replace_no_data로 입력 결측값을 nodata_elevation으로 치환(84–85), fclose(87), DEM 반환(90). |
| 93–110 | Topography::initialise_Zstar_x(93–97)는 `lis::cuda::fv1::initialise_Zstar_x<<<1, cuda::block_size>>>(Zstar_x, DEM);` (99)를 호출한다. Topography::initialise_Zstar_y(102–106)는 `lis::cuda::fv1::initialise_Zstar_y<<<1, cuda::block_size>>>(Zstar_y, DEM);` (108)를 호출한다. |
| 111–153 | Topography::clamp_boundary_values(111–116). `for (int j=1; j<geometry.ysz+1; j++)` (118)에서 서쪽 i=0(122)은 내부 이웃 DEM 복사(123), 동쪽 `const int i=geometry.xsz+1;` (128)은 내부 이웃 복사(134). `//if (j == 161 \|\| j == 162 \|\| j == 163 \|\| j == 164) {` (129), `//` 뒤의 DEM=-C(20.5) 대입(130)과 else(132)는 모두 주석이다(129–135). `for (int i=1; i<geometry.xsz+1; i++)` (139)에서 북쪽 j=0(143)은 다음 행 복사(144), 남쪽 `const int j=geometry.ysz+1;` (149)은 이전 행 복사(150). 루프·함수 종료(151–153). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 129–135: 동쪽 경계의 특정 j와 -20.5를 사용하는 대체 처리는 주석으로 남아 있다.
- 118–150: 경계 복사 루프는 네 모서리의 바깥 셀을 포함하지 않는다.
