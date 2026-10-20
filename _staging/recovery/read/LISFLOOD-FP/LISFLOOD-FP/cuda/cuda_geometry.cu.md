---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_geometry.cu
lines: 96
sha256: aba81545bbfff1c4a84f270ff5f056b7862d9e2af668c2bf8796fee55bf8a1c3
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_geometry.cu — 판독 구간 기록

구간은 1행부터 96행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | ghostraster·cuda_geometry·cuda_util 헤더(1–3). 고정 호스트 메모리(pinned host memory) allocate_pinned(5–8)의 반환식은 `return static_cast<NUMERIC_TYPE*>(malloc_pinned(` (10), `lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE)));` (11). allocate_device(14–17)는 `return static_cast<NUMERIC_TYPE*>(malloc_device(` (19), `lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE)));` (20). copy(23–28)는 `checkCudaErrors(cudaMemcpy(dst, src,` (30), `lis::GhostRaster::elements(geometry)*sizeof(NUMERIC_TYPE),` (31), `cudaMemcpyDefault));` (32). 함수 종료·빈 줄(33–36). 전처리 조건 분기는 없다. |
| 37–67 | allocate_pinned_H(37–40)는 `return static_cast<NUMERIC_TYPE*>(malloc_pinned(` (42), `lis::GhostRaster::elements_H(geometry)*sizeof(NUMERIC_TYPE)));` (43). allocate_device_H(46–49)는 `return static_cast<NUMERIC_TYPE*>(malloc_device(` (51), `lis::GhostRaster::elements_H(geometry)*sizeof(NUMERIC_TYPE)));` (52). copy_H(55–60)는 `checkCudaErrors(cudaMemcpy(dst, src,` (62), `lis::GhostRaster::elements_H(geometry)*sizeof(NUMERIC_TYPE),` (63), `cudaMemcpyDefault));` (64). 함수 종료·빈 줄(65–67). |
| 68–96 | allocate_pinned_Q(68–71)는 `return static_cast<NUMERIC_TYPE*>(malloc_pinned(` (73), `lis::GhostRaster::elements_Q(geometry)*sizeof(NUMERIC_TYPE)));` (74). allocate_device_Q(77–80)는 `return static_cast<NUMERIC_TYPE*>(malloc_device(` (82), `lis::GhostRaster::elements_Q(geometry)*sizeof(NUMERIC_TYPE)));` (83). copy_Q(86–91)는 `checkCudaErrors(cudaMemcpy(dst, src,` (93), `lis::GhostRaster::elements_Q(geometry)*sizeof(NUMERIC_TYPE),` (94), `cudaMemcpyDefault));` (95). 함수 종료(96). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
