---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc/cuda_acc_max.cu
lines: 37
sha256: 964e6c40f65fa5e8989f64fcf801f05b366561c7a287b2d2e0bd383fc1b74796
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_acc_max.cu — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | 최대값·ACC 해법·CUDA 해법·유틸리티·오류 검사·CUB 헤더를 포함한다(1–6). 이 파일에는 조건부 전처리 블록이 없다. 동일 소스 루트의 CMakeLists.txt에서 `if (CMAKE_CUDA_COMPILER)` (73) 아래 `add_compile_definitions(CUDA THRUST_IGNORE_CUB_VERSION_CHECK)` (77)를 적용하며 cuda/acc 구현 파일은 114–118행에 열거한다. config.default.cmake:2의 수치 모드 정의는 `add_compile_definitions(_NUMERIC_MODE=1)`이다. 실제 구성·컴파일은 실행하지 않았다. 원문(조건·식·호출·선언): `#include "cuda_acc_max.cuh"` (1); `#include "cuda_acc_solver.cuh"` (2); `#include "cuda_solver.cuh"` (3); `#include "cuda_util.cuh"` (4); `#include <helper_cuda.h>` (5); `#include <cub/cub.cuh>` (6). |
| 8–24 | MaxH 생성자는 가상 셀 래스터(ghost raster)의 elements_H로 요소 수를 초기화한다(8–13). temp·입력·출력 포인터를 nullptr로 둔 상태에서 cub::DeviceReduce::Max를 checkCudaErrors로 감싸 호출한다(15–20). 이어 bytes 크기의 장치 메모리를 malloc_device로 할당한다(22). 첫 호출의 bytes 사용은 원문 그대로 남긴다. 원문(조건·식·호출·선언): `lis::cuda::acc::MaxH::MaxH` (8); `(` (9); `Geometry& geometry` (10); `)` (11); `:` (12); `elements(lis::GhostRaster::elements_H(geometry))` (13); `temp = nullptr;` (15); `NUMERIC_TYPE* dummy_in = nullptr;` (16); `NUMERIC_TYPE* dummy_out = nullptr;` (17); `checkCudaErrors(cub::DeviceReduce::Max(temp, bytes,` (19); `dummy_in, dummy_out, elements));` (20); `temp = malloc_device(bytes);` (22). |
| 25–33 | MaxH::update는 Flow의 H를 CUB 최대값 축약(reduction)에 전달하고 결과를 cuda::acc::maxH 주소로 받는다(25–31). checkCudaErrors가 호출을 감싼다. 이 함수에는 자체 루프·조건·직접 커널 실행 구문이 없다. 원문(조건·식·호출·선언): `void lis::cuda::acc::MaxH::update` (25); `(` (26); `const Flow& flow` (27); `)` (28); `checkCudaErrors(cub::DeviceReduce::Max(temp, bytes, flow.H,` (30); `&(cuda::acc::maxH), elements));` (31). |
| 34–37 | 소멸자(destructor)는 free_device(temp)를 호출한다(34–37). 원문(조건·식·호출·선언): `lis::cuda::acc::MaxH::~MaxH()` (34); `free_device(temp);` (36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13·30–31: 축약 요소 수는 GhostRaster::elements_H의 반환값이다. update는 별도의 내부 셀 마스크 없이 flow.H와 이 요소 수를 전달한다.
- 15–22: 첫 DeviceReduce::Max 호출은 temp·dummy_in·dummy_out이 모두 nullptr인 상태에서 bytes를 인수로 전달한다. 이어 bytes 크기로 temp를 할당한다.
