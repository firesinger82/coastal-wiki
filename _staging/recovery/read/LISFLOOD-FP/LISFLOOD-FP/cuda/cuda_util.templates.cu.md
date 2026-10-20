---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_util.templates.cu
lines: 13
sha256: f064fa7b4c83ae448de84f6ad523d25c5aef6d9f7b317fa227a3d2b59d777392
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_util.templates.cu — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#include <helper_cuda.h>` (1)와 빈 줄이다. 전처리 조건 분기는 없다. `template<typename T>` (3)의 copy_to_symbol은 const T& symbol·const void* src·size_t count를 받는다(4–9). `checkCudaErrors(cudaMemcpyToSymbol(symbol, src, count));` (11)로 심볼(symbol)에 복사한다. 함수 끝과 마지막 빈 줄을 포함한다(12–13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
