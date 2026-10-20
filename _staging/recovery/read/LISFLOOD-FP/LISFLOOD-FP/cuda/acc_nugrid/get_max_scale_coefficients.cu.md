---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/get_max_scale_coefficients.cu
lines: 133
sha256: bb5d65736f9469c98828ae06d759a84ada68e7dcb2e5d6980c499c16538e47dd
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_max_scale_coefficients.cu — 판독 구간 기록

구간은 1행부터 133행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | 관련 헤더와 `helper_cuda.h`·`cub/cub.cuh`를 포함한다(1–3). 호스트 함수 지정은 `__host__ lis::cuda::acc_nugrid::Maxes lis::cuda::acc_nugrid::get_max_scale_coefficients` (5)이고 입력은 `AssembledSolution& d_assem_sol`이다(7). 초기화식은 `Maxes maxes = { C(1.0) };` (11)이다. 호스트 출력 한 개를 new로 할당한다(13). 장치 출력 할당식은 `NUMERIC_TYPE* d_max_out = (NUMERIC_TYPE*)malloc_device( sizeof(NUMERIC_TYPE) );` (14)이다. 임시 저장소 포인터는 NULL, 크기는 0으로 초기화한다(20–21). `CHECK_CUDA_ERROR( cub::DeviceReduce::Max` (23)에 `d_temp_storage`, `temp_storage`, `d_assem_sol.z0`, `d_max_out`, `d_assem_sol.length`를 넘긴다(24–30). `d_temp_storage = malloc_device(temp_storage);` (32)로 조회한 크기만큼 저장소를 할당한다. 이 파일에는 전처리 조건 분기가 없다. |
| 35–85 | 시작 시 5–9행의 `get_max_scale_coefficients` 함수 안. 이 구간의 eta·qx 처리문은 모두 주석이다. 블록 수 산출 주석은 `//int num_blocks = get_num_blocks(d_assem_sol.length, THREADS_PER_BLOCK_MRA);` (39)이다. CUDA 커널 호출 주석은 `//init_eta_temp<<<num_blocks, THREADS_PER_BLOCK_MRA>>> /// adds h+z for the finest grid` (41)이며 인수 `d_assem_sol`·`d_eta_temp`도 주석이다(42–45). eta 최대값 축약과 복사는 주석이다(47–61). 저장식 주석은 `//maxes.eta = FMAX( *h_max_out, C(1.0) ); /// FMAX (eta_max, 1.0)` (63)이다. qx의 `cub::DeviceReduce::Reduce`·`abs_max`·`C(0.0)` 인수와 복사도 주석이다(65–82). 저장식 주석은 `//	maxes.qx = FMAX( *h_max_out, C(1.0) );` (84)이다. 이 주석들은 실행되지 않는다. |
| 86–106 | 시작 시 5–9행의 `get_max_scale_coefficients` 함수 안. qy의 `cub::DeviceReduce::Reduce` 호출에서 `d_assem_sol.qy`, `abs_max`, `C(0.0)`을 쓰는 코드와 호스트 복사는 모두 주석이다(86–103). 저장식도 `//maxes.qy = FMAX( *h_max_out, C(1.0) );` (105)로 주석 처리되어 실행되지 않는다. |
| 107–133 | 시작 시 5–9행의 `get_max_scale_coefficients` 함수 안. `CHECK_CUDA_ERROR( cub::DeviceReduce::Max` (108)에 임시 저장소·크기·`d_assem_sol.z0`·`d_max_out`·`d_assem_sol.length`를 전달한다(109–115). `copy_cuda`는 호스트 출력·장치 출력·`sizeof(NUMERIC_TYPE)`을 받는다(117–122). 최대값 저장식은 `maxes.z = FMAX( *h_max_out, C(1.0) );` (124)이다. `free_device`로 장치 출력과 임시 저장소를 해제하고 호스트 출력을 delete한다(128–130). `return maxes;` (132) 뒤 함수를 닫는다(133). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·38–105·124: 초기화 이후 실행되는 `maxes` 필드 대입은 `maxes.z`뿐이다. eta·qx·qy의 계산과 대입은 주석이다.
- 23–32·108–124: 실행되는 최대값 축약의 입력은 두 호출 모두 `d_assem_sol.z0`이다. 최종 저장에는 `C(1.0)`을 두 번째 인수로 사용하는 FMAX가 있다.
- 7·23–30·108–115: 입력 길이는 `d_assem_sol.length`로 그대로 전달된다. 이 함수에는 길이의 유효 범위를 검사하는 조건문이 없다.
