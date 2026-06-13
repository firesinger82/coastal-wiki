---
title: "FUNWAVE-GPU 전수분석 — CUDA Fortran 커널·cuSPARSE·MGPU"
model: FUNWAVE
citation_status: verified
verification_method: "models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/{mod_cuda,init_gpu,etauv_solver_gpu,exchange_gpu,breaker_gpu,masks_gpu,mixing_gpu,sponge_gpu}.F 전수 read (서브에이전트, 2026-06-13). file:line GPU src 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-13
---

# FUNWAVE-GPU (CUDA Fortran 판) 전수분석

> FUNWAVE-TVD v3.3의 multi-GPU 이식 (dryuanye/FUNWAVE-GPU, Yuan 2020 JAMES). 비-gpu 파일은 CPU판 공유 ([`funwave-flux-tvd`](funwave-flux-tvd.md) 등); 본 노트는 **GPU 전용 *_gpu.F + mod_cuda.F**. 빌드·Blackwell 포팅은 [`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md).

## 1. mod_cuda.F (451) — GPU 전역 제어
`use cudafor` + `use cusparse`. device 상태·핸들·stream.
- 변수: `TriSolver`(0=Thomas/1=cuSPARSE 스위치) · `streamID(8)`+`stream_d2h`(비동기 stream) · `cusparseh`(핸들) · `gtsv_buf`+`gtsv_bufsize`(cuSPARSE workspace) · `BlockDim*_2D=16`/`_Inner_2D=14`(타일+halo 2) · **constant memory** `Beta_ref_d·alpha_d(3)·beta_d(3)`(RK계수)·`n_left/right/bottom/top_d`(경계법선) · ~100개 `_d` device 배열(전 상태 사본)
- subr: `var_d2h_output`(:171 암묵 cudaMemcpy) · `ESTIMATE_DT_GPU`(:225 `!$cuf kernel do(2)`+MPI_ALLREDUCE) · `cusparse_init`(:348 cusparseCreate)/`cusparse_destroy`(:358) · `cudadeviceQuery`(:301)

## 2. init_gpu.F (596) — GPU 초기화
- `AssignDevice`(:25 MGPU): `cudaSetDevice`, 노드내 rank→GPU(MPI_COMM_SPLIT_TYPE SHARED)
- `CudaMemUse`(:55): `cudaMemGetInfo` 80%↑ 경고
- `stream_init`(:92): `cudaStreamCreate` ×8+d2h
- `ALLOCATE_VARIABLES_GPU`(:112): ~80 `_d` 배열 device allocate
- `INITIALIZATION_GPU`(:267): host→device 복사(`Eta_d=Eta` 암묵 cudaMemcpy) + **WaveMaker 문자열→정수 WaveMakerCode**(GPU 커널 char 불가) + TriSolver==1이면 cusparse_init

## 3. etauv_solver_gpu.F (2019) — ★시간적분+분산 tridiagonal (핵심)
`ESTIMATE_HUV_GPU(ISTEP)`(:86): ① `HUV_BAR_KERNEL`(eta·Ubar·Vbar RK 업데이트) ② TriSolver별 tridiagonal ③ `post_tridiagonal_kernel`(Froude cap·HU/HV).

**커널(attributes(global))**:
- `HUV_BAR_KERNEL`(:1204): MUSCL-Hancock flux 발산 RK 1단계. CPU `ESTIMATE_HUV` 이중루프 → 2D 커널 완전병렬, `alpha_d/beta_d(ISTEP)` constant
- `triDx_init_kernel`(:1427)/`triDy_init_kernel`(:1589): tridiagonal 계수 2D 병렬 구성(`Γ₁·MASK9_d·dep²·DX²`)
- `triDx_cusparse_init_kernel`(:1502)/`triDy_cusparse_init_kernel`(:1683): cuSPARSE용 1D 평면화(strided batch 패킹 `RowIndex=(i−NGhost)+(j−NGhost−1)(Mloc−2NGhost)`)
- `transpose_kernel`(:1955): x방향 Thomas용 행렬전치(coalesced access)
- `post_tridiagonal_kernel`(:1975): 건조셀·HU/HV·Froude

**솔버 2경로**:
- **TriSolver==0 Thomas**: `triDx_triDy_cuda`(:565) — transpose→`triDx_cuda_kernel`(streamID2)+`triDy_cuda_kernel`(streamID3, 각 행/열=1스레드 직렬 Thomas)→deviceSync→역transpose
- **TriSolver==1 cuSPARSE**: `triDx_cusparse`(:897)/`triDy_cusparse`(:933) — `cusparseSgtsv2StridedBatch_bufferSizeExt`→`cusparseSgtsv2StridedBatch(m=Mloc−2NGhost, batchCount=Nloc−2NGhost, batchStride=Mloc−2NGhost, gtsv_buf)`. **CPU TRIDx(J루프 직렬 Thomas) → 전 행 batch 동시**. (x/y는 m↔batchCount 교환)
- **MGPU**: `triDxDy_mgpu_cuda_v1`(:183 비주기, X/Y streamID2/3 병렬+MPI 경계교환)·`_v2`(:321 주기 Y1/Y2 분리)·`periodic_triDx_triDy_cuda`(:597 Sherman-Morrison)·`triD{x,y}_mgpu_cuda`(`cudaMemcpy2dAsync` D2H→MPI→H2D)

★ Blackwell 포팅: `cusparseSgtsvStridedBatch`(CUDA12 제거)→`cusparseSgtsv2StridedBatch`(+bufferSizeExt+gtsv_buf) — [`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md).

## 4. exchange_gpu.F (1853) — 경계·halo (module boundary_condition_module)
- `BOUNDARY_CONDITION_FLUXES_GPU`(:152): 경계 flux 0, `boundary_condition_X/Y_kernel` streamID2/3 비동기
- `EXCHANGE_GPU`(:800): 주변수 ghost → `PHI_COLL_GPU`+`!$cuf` U_d*=MASK_d
- `PHI_COLL_GPU`(:967): 6 VTYPE ghost, `!$cuf kernel do(2) <<<*,(4,64)>>>`(NGhost=3 얇은 x에 최적 block), MGPU `cudaMemcpy2D`+`MPI_SENDRECV`, `phi_exch_cuda`
- `EXCHANGE_DISPERSION_GPU`(:340): 분산 ~20 미분필드 ghost, 다물리량 단일커널(launch 오버헤드 절감)+streamID 비동기
- `periodic_NSexchange_gpu`(:1597): 남북주기 `cudaMemcpy2D`(단일 D2D / MGPU D2H+MPI+H2D)

## 5. 물리 커널 (CPU판 GPU화)
- **breaker_gpu.F**(309) `breaking_kernel`(:128): Kennedy eddy viscosity. ★**shared memory** `Age_sh`(:140) — AGE_BREAKING0_d(이전스텝) 로드+`syncthreads()`로 4분면 전파 race 제거(CPU는 직접덮어 순서의존). Inner 14×14
- **masks_gpu.F**(179) `update_mask9_kernel`(:98): MASK9 9점곱 **shared `MASK_sh`**로 global access 최소화. `update_mask_kernel`(:21) flood/dry. `UPDATE_MASK_GPU`(:127) MGPU phi_int_exch_cuda+deviceSync
- **mixing_gpu.F**(153) `calc_sum_kernel`(:61)/`calc_mean_kernel`(:33): 시간평균 누적·정규화(Eta0_d zero-upcrossing 파고). `MIXING_STUFF_GPU`(:143) STEADY_TIME 후
- **sponge_gpu.F**(44) `sponge_damping_kernel`(:18): LD `Eta_d/SPONGE_d`(MASK_d>0만), in-place

## 6. CPU판 vs GPU판 핵심 차이

| 항목 | CPU (FUNWAVE-TVD) | GPU (FUNWAVE-GPU) |
|---|---|---|
| tridiagonal | TRIDx/y J루프 직렬 Thomas | TriSolver0 행별 병렬 Thomas(+transpose) / TriSolver1 **cuSPARSE batched** |
| halo 교환 | 배열복사 | `!$cuf kernel do`/cudaMemcpy2D + MPI(MGPU) |
| 쇄파 AGE | 직접덮어(순서의존) | AGE0_d **shared** race 제거 |
| DT | 단일루프 min | `!$cuf` reduction + MPI_ALLREDUCE |
| WaveMaker 분기 | character 비교 | 정수 WaveMakerCode(커널 char 불가) |
| x-Thomas | — | transpose_kernel(coalesced) |

CUDA 요소: `attributes(global)` 물리커널 / `!$cuf kernel do` 단순루프 / `shared`(Age·MASK·U/V/Eta) / `constant`(Beta_ref·alpha/beta·법선) / `streamID(8)` 비동기 / `cusparseSgtsv2StridedBatch`.

## 7. 연결
- [`funwave-build-and-blackwell-port.md`](funwave-build-and-blackwell-port.md)(빌드·cusparse v2) · [`funwave-dispersion-solver.md`](funwave-dispersion-solver.md)(CPU TRID 원형) · [`funwave-code-graph.md`](funwave-code-graph.md)
