---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/utilities/cuda_utils.cuh
lines: 56
sha256: fd369e4052b2a8a3b8a8cbb5d5d1c6dbd4f5cbbdd89ed963257781600cca8d62
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_utils.cuh — 판독 구간 기록

구간은 1행부터 56행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`를 포함한다(3). 빈 줄(4) 뒤 `../utilities/CHECK_CUDA_ERROR.cuh`를 포함한다(5). 빈 줄(6) 뒤 `cstdio`를 포함한다(7). 마지막은 빈 줄(8)이다. 전처리 조건 분기는 없다. |
| 9–17 | 호스트(host) 함수 선언은 `__host__` (9), `cudaError_t sync_device();` (10), 빈 줄(11), `__host__` (12), `cudaError_t peek();` (13), 빈 줄(14), `__host__` (15), `cudaError_t reset();` (16)이다. 마지막은 빈 줄(17)이다. 이 구간에는 함수 본문과 실제 호출이 없다. |
| 18–33 | `__host__` (18) 아래 `copy_cuda`를 선언한다(19–24). 빈 줄(25) 뒤 `__host__` (26) 아래 `copy_cuda_async`를 선언한다(27–32). 두 선언은 `void* dst`, `void* src`, `size_t bytes`를 받고 `cudaError_t`를 반환한다. 마지막은 빈 줄(33)이다. 기본 인수와 조건 분기는 없다. |
| 34–45 | `__host__` (34) 아래 `void* malloc_device(size_t bytes)`를 선언한다(35–38). 빈 줄(39) 뒤 `__host__` (40) 아래 `cudaError_t free_device(void* ptr)`를 선언한다(41–44). 마지막은 빈 줄(45)이다. 이 구간은 할당·해제의 원형만 제공한다. |
| 46–56 | `__host__` (46) 아래 `void* malloc_pinned(size_t bytes)`를 선언한다(47–50). 빈 줄(51) 뒤 `__host__` (52) 아래 `cudaError_t free_pinned(void* ptr)`를 선언한다(53–56). 고정 호스트 메모리(pinned host memory) 함수의 원형만 있으며 실제 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
