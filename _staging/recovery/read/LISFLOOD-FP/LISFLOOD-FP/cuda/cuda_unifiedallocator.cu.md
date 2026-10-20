---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_unifiedallocator.cu
lines: 5
sha256: 3dfa158151443e67bfaea821fc9bb6802c4275a910868cd616b69d7187219f53
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_unifiedallocator.cu — 판독 구간 기록

구간은 1행부터 5행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | `#include "../lisflood.h"` (1), `#include "cuda_unifiedallocator.cuh"` (2), `#include "cuda_unifiedallocator.templates.cu"` (3)를 포함한다. 전처리 조건 분기는 없다. 빈 줄 뒤 `template class lis::cuda::UnifiedAllocator<NUMERIC_TYPE>;` (5)로 수치형에 대한 명시적 인스턴스화(explicit instantiation)를 수행한다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
