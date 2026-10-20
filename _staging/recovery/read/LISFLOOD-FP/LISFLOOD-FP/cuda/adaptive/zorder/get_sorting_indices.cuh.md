---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/get_sorting_indices.cuh
lines: 24
sha256: 8c3e684879e61f5c8bd39032c8b7945c4c775b75b50fda3e3cad008f1e2a660a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_sorting_indices.cuh — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_utils.cuh`를 포함한다(3). 빈 줄(4) 뒤 `cub/cub.cuh`를 포함한다(5). 빈 줄(6) 뒤 `CHECK_CUDA_ERROR.cuh`를 포함한다(7). 빈 줄(8) 뒤 `AssembledSolution.h`, `SolverParams.h`, `MortonCode.h`를 포함한다(9–11). 마지막은 빈 줄(12)이다. 전처리 조건 분기는 없다. |
| 13–24 | `__host__` (13) 함수 `void get_sorting_indices`의 원형을 선언한다(14–24). 모턴 코드(Morton code) 원본·출력 배열은 `d_morton_codes`와 `d_sorted_morton_codes`이다(16–17). 두 해 객체 `d_assem_sol`·`d_buf_assem_sol`은 참조(reference) 인수이다(18–19). `d_indices`, `d_rev_z_order`, `d_rev_row_major`는 모두 `MortonCode*`이다(20–22). `solver_params`는 `SolverParams&` 인수이다(23). 함수 본문과 실제 호출은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
