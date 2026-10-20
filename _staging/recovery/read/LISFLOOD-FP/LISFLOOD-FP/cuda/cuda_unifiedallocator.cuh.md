---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_unifiedallocator.cuh
lines: 17
sha256: 36bbb309065b25d2ee5f26d6f0be5186f9be9e50b7856cbd16db475fd952b8a5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_unifiedallocator.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1)와 빈 줄, lis::cuda 이름공간(namespace)(3–6)이다. 전처리 조건 분기는 없다. `template<typename T>` (8)의 UnifiedAllocator는 `T* allocate(std::size_t n);` (12), `void deallocate(T* ptr, std::size_t unused);` (13)를 공개한다. 클래스·이름공간을 닫는다(14–17). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1–17: std::size_t를 사용하지만 이 헤더 안에는 다른 헤더를 포함하는 지시가 없다.
