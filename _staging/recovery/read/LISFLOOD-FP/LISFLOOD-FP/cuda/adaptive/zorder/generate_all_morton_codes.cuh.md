---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/generate_all_morton_codes.cuh
lines: 17
sha256: 1d512db38b09cf017d6b0d2146be4820e71015f9a5755ebf6d1f4bf98a447c31
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# generate_all_morton_codes.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`·`device_launch_parameters.h`를 포함한다(3–4). 빈 줄(5) 뒤 `MortonCode.h`·`HierarchyIndex.h`를 포함한다(6–7). 빈 줄(8) 뒤 `generate_morton_code.cuh`를 포함한다(9). 마지막은 빈 줄(10)이다. 전처리 조건 분기는 없다. |
| 11–17 | `__global__` (11) 커널(kernel) `void generate_all_morton_codes`의 원형을 선언한다(12–17). 인수는 `MortonCode* d_morton_codes` (14), `int* d_indices` (15), `int mesh_dim` (16)이다. 함수 본문과 커널 실행 구문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
