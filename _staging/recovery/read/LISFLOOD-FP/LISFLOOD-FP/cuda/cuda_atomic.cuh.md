---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_atomic.cuh
lines: 23
sha256: 2ab82bc78a8b53d3dc7ca10ba8f84b135798213309de7441945ee601497f692d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_atomic.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | `#pragma once` (1), 출처 URL 주석(3)과 빈 줄. `#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ < 600` (5)에서만 아래 대체 원자 덧셈(atomic addition)을 컴파일한다. |
| 6–23 | 시작 시 5행 아키텍처 조건 안. `static __inline__ __device__ double atomicAdd(double* address, double val)` (6). 포인터 변환은 `unsigned long long int* address_as_ull =` (8), `(unsigned long long int*)address;` (9). 기존 비트를 old로 읽는다(10). `do {` (12)에서 assumed=old(13), 연속 대입식 `old = atomicCAS(address_as_ull, assumed,` (14), `__double_as_longlong(val +` (15), `__longlong_as_double(assumed)));` (16). `} while (assumed != old);` (18)로 비교 교환(compare-and-swap)을 반복한다. `return __longlong_as_double(old);` (20), 함수 종료(21), `#endif` (22), 빈 줄(23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
