---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/cuda_utils.cu
lines: 87
sha256: 7aa679d35f8a7cf5a412a57d5be52519f123c50b4ab40ae3567c95fc22aee442
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_utils.cu — 판독 구간 기록

구간은 1행부터 87행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 헤더 포함(1), `lis::cuda::acc_nugrid`의 `sync`, `peek`, `reset` 정의(3–16). 각각 `return cudaDeviceSynchronize();` (5), `return cudaPeekAtLastError();` (10), `return cudaDeviceReset();` (15)로 CUDA 오류 상태를 반환한다. 전처리 조건 분기는 없다. |
| 18–35 | `copy_cuda`는 목적지·원본 포인터와 바이트 수를 받는다(18–24). `cudaMemcpy`를 `cudaMemcpyDefault`로 호출해 반환값을 error에 저장하고 반환한다(25–33). |
| 36–52 | `__host__ __device__` (36) 지정의 `malloc_device` 정의(37–41). 지역 포인터를 선언하고 `cudaMalloc(&ptr, bytes)`를 호출한 뒤 ptr을 반환한다(42–50). 호출 반환 코드를 받는 변수나 조건 검사는 없다. |
| 53–70 | `__host__ __device__` (53) 지정의 `malloc_unified` 정의(54–58). 지역 포인터와 `cudaMallocManaged(&ptr, bytes)` 호출, ptr 반환(59–67). 통합 메모리(unified memory) 할당 오류를 검사하는 조건문은 이 함수에 없다. |
| 71–87 | `__host__ __device__` (71) 지정의 `free_device` (72–78)는 `return (nullptr != ptr) ? cudaFree(ptr) : cudaSuccess;` (77). `__host__ __device__` (80) 지정의 `free_unified` (81–87)도 `return (nullptr != ptr) ? cudaFree(ptr) : cudaSuccess;` (86). 두 함수 모두 NULL이 아닌 포인터만 `cudaFree`로 해제하고 NULL은 `cudaSuccess`를 반환한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 42–50·59–67: 두 할당 함수의 지역 ptr 선언에는 초기값이 없다. 두 함수는 CUDA 할당 함수의 반환 코드를 검사하지 않고 ptr을 반환한다.
