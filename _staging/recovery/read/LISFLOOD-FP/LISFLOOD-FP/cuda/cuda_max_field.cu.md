---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_max_field.cu
lines: 136
sha256: a315096845f7a3bc946c0be43707ad71014eccad15604216419162f508180d63
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_max_field.cu — 판독 구간 기록

구간은 1행부터 136행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | max_field·solver·io 헤더(1–3), lis::cuda 이름 공간(namespace)(5–8). `__global__ void` (10), `__launch_bounds__(CUDA_BLOCK_SIZE)` (11)의 update_max_field(12–16). `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (18), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (19). `for (int j=global_j+1; j<cuda::geometry.ysz+1; j+=blockDim.y*gridDim.y)` (21), `for (int i=global_i+1; i<cuda::geometry.xsz+1; i+=blockDim.x*gridDim.x)` (23)에서 maxH 참조(25), `maxHvalue = FMAX(maxHvalue, H[j*cuda::pitch+i]);` (26). 빈 줄(30–32). 전처리 조건 분기는 없다. |
| 33–76 | 시작 시 5–8행 lis::cuda 이름 공간 안. `__global__ void` (33), `__launch_bounds__(CUDA_BLOCK_SIZE)` (34)의 update_max_field_ACC(35–39). `int global_i = blockIdx.x*blockDim.x + threadIdx.x;` (41), `int global_j = blockIdx.y*blockDim.y + threadIdx.y;` (42). `for (int j=global_j; j<cuda::geometry.ysz; j+=blockDim.y*gridDim.y)` (44), `for (int i=global_i; i<cuda::geometry.xsz; i+=blockDim.x*gridDim.x)` (46)에서 `maxHvalue = FMAX(maxHvalue, H[j*cuda::pitch+i]);` (49). 51–67행은 모두 주석이며 침수 시작·누적 시간·최대 수심 시각의 미실행 코드다. 주석 조건은 `////if (U.H[ptr] > cuda::solver_params.DepthThresh)` (52), `////	if (initHtm[ptr] == NULLVAL /*&& (Arrptr->H[ptr]>C(0.01)*/)` (57), `////	//if (Arrptr->H[ptr]>C(0.01))` (59), `////	if (U.H[ptr] > maxH[ptr])` (62). 주석 시간식은 `////		initHtm[ptr] = cuda::solver_params.t / C(3600.0); //// solver is accessible?` (58), `////	totalHtm[ptr] += cuda::dt / C(3600.0);` (60), `////		maxHtm[ptr] = cuda::solver_params.t / C(3600.0); //// ad t to solver_params` (65). 루프·함수·이름 공간 종료(69–75), 빈 줄(76). |
| 77–100 | MaxField 생성자(constructor)는 resrootname·Geometry·pitch·offset·grid_size·acceleration·precision을 받는다(77–87). 멤버 초기화 목록은 acceleration을 제외한 여섯 인수를 저장한다(88–94). GhostRaster::allocate_device(geometry)로 maxH 장치 메모리를 할당(97), `cudaMemset(maxH, 0, lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE));` (98)로 전체 0 초기화. |
| 101–116 | MaxField::update는 `lis::cuda::update_max_field<<<grid_size, CUDA_BLOCK_SIZE>>>(maxH, H);` (106)를 호출한다. MaxField::updateACC는 `lis::cuda::update_max_field_ACC << <grid_size, CUDA_BLOCK_SIZE >> > (maxH, H);` (114)를 호출한다. 두 함수 선언·종료·빈 줄(101–116). |
| 117–136 | MaxField::write는 800자 filename 버퍼(119)에 resrootname과 .max를 snprintf로 결합(120), fopen_or_die의 wb 모드로 연다(122). GhostRaster::allocate_pinned(124), cuda::copy로 전체 elements(geometry)*sizeof(NUMERIC_TYPE) 바이트를 호스트로 복사(125), AsciiRaster::write에 geometry·pitch·offset·NULLVAL·0·precision 전달(126–127). fclose·free_pinned(129–130). 소멸자(destructor)는 free_device(maxH)(133–136). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 77–98: 생성자의 acceleration 인수는 본문과 멤버 초기화 목록에서 사용하지 않는다. maxH는 allocate_device로 할당한다.
- 51–67: 침수 시작 시각·누적 시간·최대 수심 시각 계산은 주석으로만 남아 있다.
- 98: cudaMemset 호출의 반환값을 검사하는 문장은 없다.
