---
title: "FUNWAVE 빌드 + RTX 5070(Blackwell) GPU 포팅 — 직접 수행 검증"
model: FUNWAVE
citation_status: verified
verification_method: "본 위키 WSL2(Ubuntu 24.04)에서 직접 clone·빌드·실행 (2026-06-12). 소스 = models/FUNWAVE/raw/source_code/{FUNWAVE-TVD, FUNWAVE-GPU}/ (gitignore, 로컬). 컴파일러·실행 로그 직접 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-12
---

# FUNWAVE 빌드 + Blackwell GPU 포팅

> 본 위키 머신(WSL2 Ubuntu 24.04, RTX 5070)에서 **직접 clone→build→run** 검증. 소스는 gitignore(로컬)라 위키 repo엔 미포함; 본 노트가 절차·수정점의 1차 기록.

## 1. 소스 (clone)

| 저장소 | 위치 | 비고 |
|---|---|---|
| `fengyanshi/FUNWAVE-TVD` | `raw/source_code/FUNWAVE-TVD/` (332M) | CPU/MPI Fortran, v3.6 |
| `dryuanye/FUNWAVE-GPU` | `raw/source_code/FUNWAVE-GPU/` (92M) | CUDA Fortran, FUNWAVE-TVD v3.3 기반 |

## 2. FUNWAVE-TVD (CPU/MPI) — ✅ 빌드+런

- 툴체인: **gfortran 13.3 + OpenMPI 4.1.6** (`apt install gfortran libopenmpi-dev openmpi-bin`)
- ⚠️ Makefile 기본 `COMPILER=intel` → **gnu 오버라이드 필수**: `make COMPILER=gnu PARALLEL=true MPI=openmpi`
- 산출: `funwave-work/funwave--mpif90-parallel-single`
- 런 검증: FLAT depth 케이스 → `eta/u/v/mask/BrkSrc/FrcIns` 출력 생성 (PX=PY=1, `mpirun -n 1`)

## 3. FUNWAVE-GPU (CUDA Fortran, 단일 GPU) — ✅ 빌드+런 (RTX 5070 cc120)

- 툴체인: **NVIDIA HPC SDK 26.3 (nvfortran, CUDA 13.1, cuSPARSE)** — apt repo `developer.download.nvidia.com/hpc-sdk/ubuntu`, pkg `nvhpc-26-3`
- 환경: `PATH=$NVROOT/compilers/bin:$NVROOT/comm_libs/mpi/bin`, `LD_LIBRARY_PATH=$NVROOT/compilers/lib:$NVROOT/math_libs/lib64` (NVROOT=`/opt/nvidia/hpc_sdk/Linux_x86_64/26.3`)
- **Makefile_cuda 현대화 수정**(2018년 코드 → 2026 Blackwell):
  - `FC = pgf90` → **`nvfortran`**
  - `OPT = -Mcuda=cuda10.1 -Mcudalib=cusparse` → **`-cuda -gpu=cc120 -cudalib=cusparse`** (cc120 = RTX 5070 Blackwell; `nvaccelinfo` Default Target=cc120 자동인식)

### 3.1 ★ 핵심 수정 — cuSPARSE 옛 API 제거 대응 (CUDA 12+/Blackwell)

논문의 **batched tridiagonal solver**가 `cusparseSgtsvStridedBatch` 호출 → **CUDA 12.0에서 제거**됨(Blackwell은 CUDA 12.8+ 필수 → 옛 API로 회귀 불가). **v2 API로 이식**:

- `cusparseSgtsvStridedBatch(h,m,dl,d,du,x,bc,bs)` → **`cusparseSgtsv2StridedBatch(h,m,dl,d,du,x,bc,bs, pBuffer)`** + 사전 `cusparseSgtsv2StridedBatch_bufferSizeExt(...,bufsize)` 로 work buffer 크기 조회.
- NVHPC `cusparse` 모듈 인터페이스(`compilers/src/cusparse.f90:7380,7328`): `pBuffer = character*1, device :: pBuffer(*)` (`!dir$ ignore_tkr`) → **device 배열 직접 전달**(c_loc 불필요), `pBufferSizeInBytes = integer(8)`.
- 구현: `mod_cuda.F`에 모듈 device buffer 신설 — `character(1),allocatable,device,save :: gtsv_buf` + `integer(8) :: gtsv_bufsize`. `etauv_solver_gpu.F`의 **4개 호출**(triDx/triDy/+periodic 2개, `mod_cuda` `only:` 목록에 `gtsv_buf,gtsv_bufsize` 추가)을 각각 `bufferSizeExt → grow buffer → gtsv2` 3단계로 교체.
- (개발자가 v2 마이그레이션 템플릿을 주석으로 남겨둠: `etauv_solver_gpu.F:59-80,905-909`)

### 3.2 검증 (RTX 5070)

- `funwave_fullcuda` 빌드(nvfortran cc120, link OK).
- 실행 로그: `Device Name: NVIDIA GeForce RTX 5070 / Compute Capability: 12.0 / Multiprocessors: 48`. FLAT+INI_GAU 케이스 시간진행(`TIME/TOTAL 2.02/8.0`) 정상 — **GPU 물리 런 동작**.

## 4. 후속

- 이 Blackwell 포팅(cuSPARSE v2)을 **upstream(dryuanye/FUNWAVE-GPU)에 PR** 가치 — CUDA 12+/Blackwell 사용자 공통 이슈.
- 다중 GPU(`Makefile_mgpu`, MGPU+MPI) 빌드는 별도(NVHPC mpif90). 단일 RTX 5070엔 single-GPU(`Makefile_cuda`)로 충분.
- 소스 확보됨 → physics source-analysis(Boussinesq 항·TVD flux·tridiagonal dispersion·wavemaker·sponge) 작성 가능.

## 5. 연결

- [`../README.md`](../README.md) · [`../web-refs/funwave-official-resources.md`](../web-refs/funwave-official-resources.md)
- 사용 동기(정온도): [`../../../concepts/waves/06-model-application.md`](../../../concepts/waves/06-model-application.md) §1.1
