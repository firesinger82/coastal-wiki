---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/utilities/cuda_utils.cu
lines: 109
sha256: 5553abdd5278ed1f1a705d2dac16311ff347af6ac513f997e278844d3eac77ef
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_utils.cu — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `../utilities/cuda_utils.cuh`를 포함한다(1). 빈 줄(2) 뒤 `__host__` (3)로 호스트(host) 함수 `sync_device()`를 정의한다(4–5). `return cudaDeviceSynchronize();` (6)로 장치 동기화(device synchronization)의 반환 상태를 그대로 돌려준다. 함수 종료·빈 줄(7–8)이다. 이 파일에는 전처리 조건 분기가 없다. |
| 9–14 | `__host__` (9) 함수 `peek()` (10–11)는 `return cudaPeekAtLastError();` (12)로 마지막 CUDA 오류의 조회 결과를 반환한다. 함수 종료·빈 줄(13–14)이다. |
| 15–20 | `__host__` (15) 함수 `reset()` (16–17)은 `return cudaDeviceReset();` (18)로 장치 초기화 호출의 상태를 반환한다. 함수 종료·빈 줄(19–20)이다. |
| 21–39 | `__host__` (21) 함수 `copy_cuda`는 목적지 `void* dst`, 원본 `void* src`, 바이트 수 `size_t bytes`를 받는다(22–28). `cudaMemcpy`를 `dst`, `src`, `bytes`, `cudaMemcpyDefault` 순서로 호출하여 상태를 지역 `cudaError_t error`에 받는다(29–35). 빈 줄(36) 뒤 `return error;` (37)로 상태를 반환한다. 함수 종료·빈 줄(38–39)이다. |
| 40–58 | `__host__` (40) 함수 `copy_cuda_async`는 목적지·원본·바이트 수를 받는다(41–47). `cudaMemcpyAsync`를 `dst`, `src`, `bytes`, `cudaMemcpyDefault` 순서로 호출하여 상태를 지역 `cudaError_t error`에 받는다(48–54). 스트림(stream) 인수를 이 호출에 명시하지 않는다. 빈 줄(55) 뒤 `return error;` (56)로 상태를 반환한다. 함수 종료·빈 줄(57–58)이다. |
| 59–75 | `__host__` (59) 함수 `malloc_device(size_t bytes)`는 `void*`를 반환한다(60–64). 지역 포인터(pointer) `ptr`를 초기값 없이 선언한다(65). 빈 줄(66) 뒤 `cudaMalloc`에 `&ptr`와 `bytes`를 전달한다(67–71). 빈 줄(72) 뒤 `return ptr;` (73)로 포인터를 반환한다. 함수 종료·빈 줄(74–75)이다. |
| 76–92 | `__host__` (76) 함수 `malloc_pinned(size_t bytes)`는 `void*`를 반환한다(77–81). 지역 `ptr`를 초기값 없이 선언한다(82). 빈 줄(83) 뒤 `cudaMallocHost`에 `&ptr`와 `bytes`를 전달하여 고정 호스트 메모리(pinned host memory)를 요청한다(84–88). 빈 줄(89) 뒤 `return ptr;` (90)로 포인터를 반환한다. 함수 종료·빈 줄(91–92)이다. |
| 93–101 | `__host__` (93) 함수 `free_device(void* ptr)`를 정의한다(94–98). 삼항 연산자(ternary operator) 원문은 `return (nullptr != ptr) ? cudaFree(ptr) : cudaSuccess;` (99)이다. 포인터가 널(null)이 아니면 `cudaFree`를 호출하고 널이면 성공 상태를 반환한다. 함수 종료·빈 줄(100–101)이다. |
| 102–109 | `__host__` (102) 함수 `free_pinned(void* ptr)`를 정의한다(103–107). 삼항 연산자 원문은 `return (nullptr != ptr) ? cudaFreeHost(ptr) : cudaSuccess;` (108)이다. 포인터가 널이 아니면 `cudaFreeHost`를 호출하고 널이면 성공 상태를 반환한다. 함수 종료(109)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 65–73·82–90: 두 메모리 할당 함수는 초기값 없는 지역 포인터를 CUDA 할당 함수의 출력 인수로 넘긴다. 두 함수는 CUDA 할당 함수의 반환 상태를 저장하거나 검사하지 않고 포인터만 반환한다.
