---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_util.cu
lines: 105
sha256: 8cf4f1645bb1cc9fb998de421d0a31a3f394a21498bb841eae5a7d1e334acc81
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_util.cu — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | util·helper_cuda 헤더를 포함한다(1–2). 전처리 조건 분기는 없다. sync는 `checkCudaErrors(cudaDeviceSynchronize());` (6), peek는 `checkCudaErrors(cudaPeekAtLastError());` (12)를 호출한다. CUDA 오류 코드를 직접 반환하는 디버그(debug)용 대체 구현은 전부 주석이다(16–24). 빈 줄을 포함한다. |
| 27–36 | copy는 dst·src·count를 받아 `checkCudaErrors(cudaMemcpy(dst, src, count, cudaMemcpyDefault));` (34)를 호출한다. 복사 방향은 cudaMemcpyDefault로 전달한다. |
| 37–66 | malloc_unified는 `checkCudaErrors(cudaMallocManaged(&ptr, size));` (43), malloc_pinned는 `checkCudaErrors(cudaMallocHost(&ptr, size));` (53), malloc_device는 `checkCudaErrors(cudaMalloc(&ptr, size));` (63)를 호출하고 각각 ptr를 반환한다. 순서대로 통합 메모리(unified memory)·고정 호스트 메모리(pinned host memory)·장치 메모리(device memory) 할당 함수이다. |
| 67–90 | free_unified는 `checkCudaErrors(cudaFree(ptr));` (72), free_pinned는 `checkCudaErrors(cudaFreeHost(ptr));` (80), free_device는 `checkCudaErrors(cudaFree(ptr));` (88)를 호출한다. |
| 91–105 | get_device는 `checkCudaErrors(cudaGetDevice(&device));` (94) 후 장치 번호를 반환한다(95). get_device_properties는 `checkCudaErrors(cudaGetDeviceProperties(&properties, device));` (104)로 주어진 장치의 속성을 채운다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
