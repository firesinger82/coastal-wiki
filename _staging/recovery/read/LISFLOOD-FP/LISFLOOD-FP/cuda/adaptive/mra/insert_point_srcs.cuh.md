---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/insert_point_srcs.cuh
lines: 18
sha256: 3e40cda9dccfdbf0e66d39d59f7d62972a0de2b945150d1ba5a928809439c622
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# insert_point_srcs.cuh — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1). cuda_runtime.h, device_launch_parameters.h, AssembledSolution.h, PointSources.h, get_lvl_idx.cuh를 포함한다(3–9). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 11–18 | `__global__` (11)인 CUDA 커널(kernel) insert_point_srcs를 선언한다(12–18). AssembledSolution, PointSources, real dt, real dx_finest를 값으로 받는다(14–17). 기본 인수와 커널 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
