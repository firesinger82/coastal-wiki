---
title: "FUNWAVE-GPU CUDA 포팅 디테일 — kernel launch·device memory·stream·MGPU halo exchange"
model: FUNWAVE
component: gpu-cuda-port
canonical_source: self
citation_status: verified
verification_method: "소스 직접 read (서브에이전트, 2026-06-16). models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/{mod_cuda,init_gpu,mgpu_utilities,etauv_solver_gpu,exchange_gpu,breaker_gpu}.F + Makefile_cuda/Makefile_mgpu/Makefile_cuda.orig 의 file:line 인용. 경로는 해당 GPU src 기준 상대."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/FUNWAVE/README.md
  - models/FUNWAVE/source-analysis/funwave-gpu-source.md
  - models/FUNWAVE/source-analysis/funwave-build-and-blackwell-port.md
---

# FUNWAVE-GPU CUDA 포팅 디테일 — kernel launch · device memory · stream · MGPU halo exchange

> CUDA Fortran(`cudafor`) 이식의 **구현 메커닉** — kernel launch geometry(`dim3`·tile/inner-tile), device 메모리 모델(`_d` 사본·`constant`·`shared`), stream 동시성, MGPU halo 교환(MPI 파생형·`cudaMemcpy2D` 스테이징). 경로는 `models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/` 기준.
> 알고리즘·서브루틴 맵·CPU↔GPU 차이 표는 [[funwave-gpu-source]] 가 canonical. 본 노트는 **중복을 피하고 CUDA 구현 디테일(launch·exchange·memory)** 에 집중. 빌드·Blackwell 플래그는 [[funwave-build-and-blackwell-port]].

---

## 1. 컴파일 모델: CPP 분기 + nvfortran CUDA Fortran

`.F.o` 규칙은 `cpp`로 전처리(`.f90` 생성) 후 `$(FC) -c`로 컴파일 (`Makefile_cuda:71-74`). GPU는 표준 CUDA C가 아닌 **CUDA Fortran** — kernel은 `attributes(global) subroutine`, device 배열은 `device` 속성으로 직접 선언. 별도 `.cu` 파일 없음.

세 빌드 변종:

| Makefile | 핵심 플래그 | FC | 대상 |
|---|---|---|---|
| `Makefile_cuda` | `-DUSE_CUDA -DPGI -DCARTESIAN`, `OPT=-cuda -gpu=cc120 -cudalib=cusparse` (`:27-28,:38`) | `nvfortran` (`:36`) | 단일 GPU, Blackwell(cc120) |
| `Makefile_cuda.orig` | `OPT=-Mcuda=cuda10.1 -Mcudalib=cusparse`, `FC=pgf90` | pgf90 | 원본(구 PGI/CUDA10.1) |
| `Makefile_mgpu` | `-DUSE_CUDA -DPGI -DMGPU`, `OPT=-Mcuda=cuda10.1 -Mcudalib=cusparse`, `FC=mpif90` (`:27-29,:37,:39`) | mpif90 | multi-GPU + MPI |

- `-DMGPU` 가 multi-GPU(+MPI) 경로 전부를 토글. `Makefile_mgpu:78` 만 `MODS`에 **`mgpu_utilities.F`** 를 포함(단일 GPU 빌드는 제외).
- `cusparse` 링크는 세 빌드 모두 공통(`-cudalib=cusparse`/`-Mcudalib=cusparse`).
- ★ Blackwell 포팅의 핵심 변경은 `FC: pgf90→nvfortran`, `OPT: -Mcuda=cuda10.1 → -cuda -gpu=cc120` 두 줄 (`diff Makefile_cuda.orig Makefile_cuda`). 상세 [[funwave-build-and-blackwell-port]].

---

## 2. Device 메모리 모델 (mod_cuda.F)

`module mod_cuda` 가 `use cudafor` + `use cusparse` (`mod_cuda.F:10-11`)로 전 device 상태를 SAVE 보유.

### 2.1 세 종류 device 메모리

| 종류 | 선언 | 예 | 비고 |
|---|---|---|---|
| **global (device)** | `allocatable, device` | `~100개 _d` 필드 (`mod_cuda.F:51-165`) | CPU 전 상태배열의 device 사본 |
| **constant** | `constant` | `Beta_ref_d`·`alpha_d(3)`·`beta_d(3)`(MUSCL RK 계수)·`n_left/right/bottom/top_d`(경계 법선) (`mod_cuda.F:38-42`) | 읽기전용, 브로드캐스트 캐시 |
| **shared** | 커널 내 `shared` | `Age_sh`(breaker)·`MASK_sh`(masks) | 타일 로컬, [[funwave-gpu-source]] |

- device 배열은 host 배열과 **동명+`_d` suffix** 규약 (`Eta_d`↔`Eta`, `MASK_d`↔`MASK` 등).
- host↔device 전송은 CUDA Fortran의 **암묵 cudaMemcpy** (배열 대입). `INITIALIZATION_GPU`의 `ETA_d = ETA`·`H_d = H`·`MASK_d = MASK` (`init_gpu.F:370,371,378`)가 곧 H2D 복사. 역방향 D2H는 `var_d2h_output`의 `Eta = Eta_d` 등(출력 직전, `mod_cuda.F:190-194`).

### 2.2 출력 D2H 정책 (var_d2h_output)
`var_d2h_output`(`mod_cuda.F:171-220`)은 **출력 플래그가 켜진 변수만** D2H 다운로드. `Eta/U/V/H/MASK`는 무조건(`:190-194`), `MASK9`·`P`·`Q`·`VorticityMax`·`AGE_BREAKING`·`nu_break` 등은 `OUT_*` 가드(`:195-219`). 주석: max값을 host에서 `MAXVAL`로 구하려면 먼저 다운로드해야 함(아니면 parallel reduction 필요) (`:173-174`). 비동기 `cudaMemcpy2dAsync(stream=stream_d2h)` 변종이 주석으로 남아있음(`:185-189`) — 현재는 동기 대입 사용.

### 2.3 블록 차원 상수
```
BlockDimX_2D = 16, BlockDimY_2D = 16          (mod_cuda.F:29)
BlockDimX_Inner_2D = 14, BlockDimY_Inner_2D = 14   (mod_cuda.F:30)
```
- **2D 일반 커널**: 16×16 타일.
- **Inner 14×14**: stencil(±1 이웃) 커널이 타일 경계에서 halo 한 겹씩 손실 → 유효 출력은 14×14, 블록은 16×16 로드. → grid 인덱싱이 `Inner` 보폭을 씀(§4 breaker 참조).
- 주석에 8×8/6×6 대안이 남아있음(`:31-32`).

---

## 3. Kernel launch geometry (etauv_solver_gpu.F)

CUDA Fortran chevron `call kernel<<<grid, tBlock [,shmem, stream]>>>(args)`.

### 3.1 2D 물리 커널 — 전 격자 타일
`ESTIMATE_HUV_GPU`(`etauv_solver_gpu.F:86~`)의 메인 RK 커널:
```fortran
tBlock = dim3 (BlockDimX_2D, BlockDimY_2D ,1)                          ! 16×16
grid   = dim3 ( ceiling(real(Mloc)/BlockDimX_2D), ceiling(real(Nloc)/BlockDimY_2D), 1 )
call HUV_BAR_KERNEL <<<grid ,tBlock>>> (...)
```
(`etauv_solver_gpu.F:90-94`). 동일 패턴으로 `triDx_init_kernel`/`triDx_cusparse_init_kernel`(`:124-131`), `triDy_*`(`:135-142`), `post_tridiagonal_kernel`(`:173-176`). 각 커널 내부 인덱스:
```fortran
i = threadIdx%x + (BlockIdx%x-1)*BlockDim%x
j = threadIdx%y + (BlockIdx%y-1)*BlockDim%y
if (i>=Ibeg .AND. i<=Iend .AND. j>=Jbeg .AND. j<=Jend) then ...
```
(`post_tridiagonal_kernel`, `etauv_solver_gpu.F:1985-1987`) — 경계 가드로 over-launch 잉여 스레드 제거.

### 3.2 1D Thomas 커널 — 행/열 = 1 스레드
`tBlock = dim3(32,1,1)` (`etauv_solver_gpu.F:191,332,578`). forward/back sweep 은 각 행(또는 열)을 한 스레드가 직렬 처리:
```fortran
call triDx_forwardsweep_cuda_kernel
     <<<dim3(ceiling(real(Nloc)/tBlock%x),1,1), tBlock, 0, streamID(2)>>>(...)
call triDy_forwardsweep_cuda_kernel
     <<<dim3(ceiling(real(Mloc)/tBlock%x),1,1), tBlock, 0, streamID(3)>>>(...)
```
(`etauv_solver_gpu.F:225-230`). X-sweep은 `Nloc`개 행(streamID 2), Y-sweep은 `Mloc`개 열(streamID 3)을 **서로 다른 stream에 동시 발행**.

### 3.3 Transpose (coalesced X-Thomas)
X 방향 Thomas는 메모리 stride가 비효율 → `transpose_kernel`로 행렬 전치 후 풀고 역전치:
```fortran
grid_tran      = dim3(ceiling(real(Nloc)/tBlock_tran%x), ceiling(real(Mloc)/tBlock_tran%y), 1)
grid_tran_back = dim3(ceiling(real(Mloc)/tBlock_tran%x), ceiling(real(Nloc)/tBlock_tran%y), 1)
call transpose_kernel<<<grid_tran,tBlock_tran>>>(myAx_d, myAx_T, Nloc, Mloc)   ! ×3 계수
...
call transpose_kernel<<<grid_tran_back, tBlock_tran>>>(myFx_T, U_d, Mloc, Nloc) ! 역전치 → U_d
```
(`etauv_solver_gpu.F:568-591`). 커널 본체는 단순 element swap `odata(i,j)=idata(j,i)` (`etauv_solver_gpu.F:1955-1966`) — shared-memory 타일 전치가 아닌 naive 전치(coalesced write/strided read).

### 3.4 `!$cuf kernel do` — 단순 루프 자동 커널화
2중 do 루프에 `!$cuf kernel do(2) <<<*,*>>>` directive를 붙이면 컴파일러가 커널 생성. 예:
- `ESTIMATE_DT_GPU`: CFL 시간스텝, `!$cuf kernel do(2)` x/y 두 루프 + `min` reduction (`mod_cuda.F:238-262`). MGPU면 `MPI_ALLREDUCE(...,MPI_MIN,...)` 로 전역 최소 (`mod_cuda.F:265-267`).
- cusparse 결과 unpack: `!$cuf kernel do(2) <<<*,*>>>` 로 `Drow(1D 평면) → U_d/V_d` (`etauv_solver_gpu.F:919-924, 948-953`).
- 명시 블록형도 존재: `PHI_COLL_GPU` periodic ghost가 `!$cuf kernel do(2) <<<*,(64,4)>>>` — NGhost=3 두께의 얇은 방향에 맞춘 비대칭 블록(64×4) (`exchange_gpu.F:1039`).

---

## 4. Inner-tile + shared memory (breaker_gpu.F)

stencil 커널의 inner-tile 인덱싱 실증 — `breaking_kernel`:
```fortran
real(SP),dimension(BlockDimX_2D,BlockDimY_2D),shared :: Age_sh   ! 16×16 shared
tx = threadIdx%x ; ty = threadIdx%y
i = tx + (blockIdx%x-1)*BlockDimX_Inner_2D    ! ★ Inner(14) 보폭 — 블록은 16 로드
j = ty + (blockIdx%y-1)*BlockDimY_Inner_2D
if (...) Age_sh(tx,ty) = AGE_BREAKING0_d(i,j)  ! 이전스텝 값 shared 로드
call syncthreads()
if (... .and. tx>1 .and. ty>1 .and. tx<blockDim%x .and. ty<blockDim%y) then  ! 내부 14×14만 출력
```
(`breaker_gpu.F:140-157`). 핵심:
1. **grid 보폭 = Inner(14)** 이므로 인접 블록이 한 겹씩 겹쳐 halo를 공유 — 16 로드 / 14 계산.
2. **`AGE_BREAKING0_d`(이전스텝 사본)** 을 shared 로드 + `syncthreads()` → CPU판이 AGE를 in-place 덮어쓰던 순서의존을 제거(병렬 race 방지). 주석: "CPU version rewrite the age_breaking directly, which make parallel impossible" (`breaker_gpu.F:149-150`).
3. 출력 가드 `tx>1 .and. tx<blockDim%x`로 타일 테두리(halo) 스레드는 쓰기 제외.

같은 shared 패턴이 `masks_gpu.F`의 `MASK_sh`(MASK9 9점곱)에 적용 — [[funwave-gpu-source]] §5.

---

## 5. Stream 동시성 모델

`streamID(8)` + `stream_d2h` 를 `init_gpu.F:92-100`(`stream_init`)에서 `cudaStreamCreate` ×9 생성, `stream_destroy`에서 파기(`:102-109`). 선언은 `mod_cuda.F:20-21`.

용법:
- **X/Y 방향 독립 작업 동시화**: X-sweep → `streamID(2)`, Y-sweep → `streamID(3)` (서로 데이터 비의존이므로 GPU에서 겹침). `triDxDy_mgpu_cuda_v1` 전체가 이 구조(`etauv_solver_gpu.F:225-229`).
- **주기 BC v2 추가 stream**: Y를 둘로 쪼개 `streamID(3)`+`streamID(4)` (`etauv_solver_gpu.F:379,406-407,456`).
- **동기화 2종**: 작업 분리 후 `cudaStreamSynchronize(streamID(n))`(개별 stream, `etauv_solver_gpu.F:240,252,299,309`), transpose↔sweep 경계는 `cudaDeviceSynchronize()`(전역, `:589`).
- **비동기 D2H 출력용** `stream_d2h` 는 현재 코드상 주석 처리된 `cudaMemcpy2dAsync`용으로 예약(`mod_cuda.F:185-189`).

---

## 6. Multi-GPU: device 할당 · 메모리 가드

### 6.1 rank → GPU 매핑 (init_gpu.F AssignDevice)
`# if defined (MGPU)` 가드(`init_gpu.F:24`). 노드 내 로컬 rank로 device 선택:
```fortran
call MPI_COMM_SPLIT_TYPE(MPI_COMM_WORLD, MPI_COMM_TYPE_SHARED, 0, MPI_INFO_NULL, newComm, ier)
call MPI_COMM_RANK(newComm, newRank, ier)   ! 노드 내 로컬 랭크
dev = newRank
istat = cudaSetDevice(dev)                   ! 로컬 랭크 → GPU 번호
```
(`init_gpu.F:36-41`). `MPI_COMM_TYPE_SHARED` 로 동일 노드 프로세스를 묶어 노드-로컬 인덱스를 GPU id로 사용 → 1 노드 N-GPU 시 rank가 GPU에 1:1 핀. 주석: OpenMPI ≥3.1.3 필요(`init_gpu.F:35`). `GPULOG.txt`에 rank/GPU/hostname 기록(`:43-50`).

### 6.2 메모리 가드 (CudaMemUse)
`cudaMemGetInfo(freeMem,totalMem)` (`init_gpu.F:60`). 사용률 80% 초과 시 경고+STOP (`init_gpu.F:72-76` MGPU / `:83-87` 단일). MGPU는 `MPI_ALLREDUCE(MPI_MAX)`/`(MPI_MIN)` 로 전 rank 최대사용/최소여유 집계(`:65-66`).

---

## 7. MGPU halo exchange — `cudaMemcpy2D` 스테이징 + MPI 파생형

`# if defined (MGPU) module mgpu_utilities`(`mgpu_utilities.F:1-2`). device 데이터를 직접 MPI 송신하지 않고 **device→host 스테이징 버퍼 복사 후 MPI, 다시 host→device** 하는 3-step 패턴 (CUDA-aware MPI 미가정).

### 7.1 MPI 파생 데이터형 (mpi_datatype)
```fortran
call MPI_TYPE_VECTOR(Nloc, Nghost, Mloc, MPI_SP, HaloWE, ier)   ! 동서 ghost 열
call MPI_TYPE_VECTOR(Nghost, Mloc, Mloc, MPI_SP, HaloSN, ier)   ! 남북 ghost 행
... HaloWE_int, HaloSN_int (MPI_INTEGER 판) ...
call MPI_TYPE_VECTOR(1, Mloc, Mloc, MPI_SP, YType, ier)
```
(`mgpu_utilities.F:14-26`). strided ghost 영역을 한 묶음으로 다루는 vector type을 정의·commit. real/integer 양쪽 준비.

### 7.2 phi_exch_cuda — 주변수 ghost 교환
실제 사용 경로(`mgpu_utilities.F:104-154`). 위쪽에 `MPI_SENDRECV(PHI(...),1,HaloWE,...)` 직접 device 송신 버전이 **주석으로** 남아있고(`:28-100`), 현재 활성판은 `cudaMemcpy2D` 스테이징:
```fortran
! 동서(EW), len = Nloc*Nghost
istat = cudaMemcpy2D(sWmsg(1,1),Nghost, PHI(Ibeg,1),Mloc, Nghost,Nloc)        ! D2H pack
call MPI_SENDRECV(sWmsg,len,MPI_SP,n_west,1, rWmsg,len,MPI_SP,n_west,0,comm2d,status,ier)
istat = cudaMemcpy2D(PHI(Ibeg-Nghost,1),Mloc, rWmsg(1,1),Nghost, Nghost,Nloc) ! H2D unpack
```
(`mgpu_utilities.F:117-122`, east 대칭 `:124-129`). 남북(SN)은 `len=Mloc*Nghost`, `cudaMemcpy2D(...,Mloc,Mloc,Nghost)` (`:134-152`). `cudaMemcpy2D(dst,dpitch,src,spitch,width,height)` 의 pitch 인자로 `Mloc`(전체 행 stride)↔`Nghost`/`Mloc`(packed buffer stride)를 맞춰 strided ghost를 연속 버퍼로 모음.

- 정수 변종 `phi_int_exch_cuda`(MASK 류) 동일 구조, `MPI_INTEGER`/`HaloWE_int` (`mgpu_utilities.F:165-207`).
- 두 루틴은 `interface phi_exch_cuda` 로 generic 묶음 (`mgpu_utilities.F:8-11`) → 호출측은 real/int 구분 없이 `phi_exch_cuda` 호출.
- `n_west/east/suth/nrth .ne. MPI_PROC_NULL` 가드로 도메인 경계 rank는 해당 방향 skip (`:117,124,134,144`).

### 7.3 EXCHANGE 호출측 (exchange_gpu.F)
`PHI_COLL_GPU`(`exchange_gpu.F:968~`)가 VTYPE별 ghost 처리. MGPU periodic 남북은 `cudaMemcpy2D`+`MPI_SENDRECV`로 master(bottom)↔top rank 교환(`exchange_gpu.F:1001-1011`), 단일 GPU/PY=1 이면 device-to-device `cudaMemcpy2D`(`:1030-1033`) 또는 `!$cuf kernel do(2) <<<*,(64,4)>>>` 직접 복사(`:1039-1045`). 다물리량 통합 dispersion 교환·다른 VTYPE 상세는 [[funwave-gpu-source]] §4.

### 7.4 MGPU tridiagonal 경계 교환 (etauv_solver_gpu.F)
Thomas sweep이 도메인 경계를 가로지를 때 forward/back-substitution 계수를 rank 간 전달. `triDxDy_mgpu_cuda_v1`(`etauv_solver_gpu.F:183~`):
```fortran
call MPI_IRECV(rmsgx, 2*Nloc, MPI_SP, n_west, 0, comm2d, req, ier); call MPI_WAIT(...)
istat = cudaMemcpy2dAsync(myDx_T(1,Ibeg-1),Nloc, rmsgx(1,1),Nloc, Nloc,1, cudaMemcpyHostToDevice, streamID(2))  ! H2D 받은 계수
...
call triDx_forwardsweep_cuda_kernel<<<...,streamID(2)>>>(...)
istat = cudaMemcpy2DAsync(smsgx(1,1),Nloc, myDx_T(1,Iend),Nloc, Nloc,1, cudaMemcpyDeviceToHost, streamID(2))    ! D2H 보낼 계수
istat = cudaStreamSynchronize(streamID(2)); call MPI_ISEND(smsgx, 2*Nloc, MPI_SP, n_east, 0, comm2d, req, ier)
```
(`etauv_solver_gpu.F:200-242` 발췌). 특징:
- **비동기 stream 사용**: `cudaMemcpy2dAsync(..., streamID(2/3))` 로 X(streamID2)/Y(streamID3) 교환을 겹침.
- **send 전 `cudaStreamSynchronize`** 로 D2H 완료 보장 후 `MPI_ISEND` (`:240-241`).
- 경계 rank(`MPI_PROC_NULL`)면 sweep 시작 인덱스를 `Ibeg+1`/`Jbeg+1` 로 당김(교환 생략) (`:206-208, 219-221`).
- 변종: `_v2`(주기 Y 분할, `etauv_solver_gpu.F:321~`), `periodic_triDx_triDy_cuda`(Sherman-Morrison, `:597~`) — 알고리즘은 [[funwave-gpu-source]] §3.

---

## 8. cuSPARSE batched tridiagonal — 호출 디테일

`TriSolver` 파라미터(`mod_cuda.F:17`, `0=Thomas / 1=cuSPARSE`)가 솔버 분기. `cusparse_init`이 `TriSolver==1` 일 때만 `cusparseCreate(cusparseh)` (`mod_cuda.F:348-356`).

`triDx_cusparse`(`etauv_solver_gpu.F:897-931`):
```fortran
istat = cusparseSgtsv2StridedBatch_bufferSizeExt(cusparseh, Mloc-2*NGhost, Arow,Brow,Crow,Drow, Nloc-2*NGhost, Mloc-2*NGhost, gtsv_bufsize)
if(.not.allocated(gtsv_buf)) allocate(gtsv_buf(gtsv_bufsize))
if(size(gtsv_buf,kind=8) < gtsv_bufsize) then; deallocate(gtsv_buf); allocate(gtsv_buf(gtsv_bufsize)); endif
istat = cusparseSgtsv2StridedBatch(cusparseh, Mloc-2*NGhost, Arow,Brow,Crow,Drow, Nloc-2*NGhost, Mloc-2*NGhost, gtsv_buf)
```
(`etauv_solver_gpu.F:910-913`). 인자 의미: `m = Mloc-2*NGhost`(시스템 크기), `batchCount = Nloc-2*NGhost`(행 수), `batchStride = Mloc-2*NGhost`. → CPU의 J-루프 직렬 Thomas가 **전 행을 단일 batch 호출**로 동시 처리.

- ★ **Blackwell/CUDA12 포팅 핵심**: 구판 `cusparseSgtsvStridedBatch`(CUDA12에서 제거)를 **v2 API** `cusparseSgtsv2StridedBatch` + 별도 `bufferSizeExt` 질의 + `gtsv_buf`(`mod_cuda.F:27-28`) 워크스페이스로 교체. `etauv_solver_gpu.F:907-909` 주석에는 v2 API 의 **이전 workspace 처리 변종**(수동 `c_loc(buf)`/`c_char` 방식)이 보존됨(제거된 v1 심볼 자체는 아님). 상세 [[funwave-build-and-blackwell-port]].
- `triDy_cusparse`(`:933~`)는 `m↔batchCount` 교환(`Nloc-2*NGhost` ↔ `Mloc-2*NGhost`, `:939,942`).
- 결과 1D `Drow` → 2D `U_d/V_d` unpack은 `!$cuf kernel do(2)` (인덱스 `(i-NGhost)+(j-NGhost-1)*(Mloc-2*NGhost)`, `:919-924`).

---

## 9. 연결
- [[funwave-gpu-source]] — GPU 서브루틴/커널 맵·알고리즘·CPU↔GPU 차이표 (canonical)
- [[funwave-build-and-blackwell-port]] — 빌드 플래그·nvfortran·cusparse v2 포팅
- [[funwave-dispersion-solver]] — CPU TRIDx/y 직렬 Thomas 원형
- [[funwave-code-graph]] — 전체 호출 그래프
