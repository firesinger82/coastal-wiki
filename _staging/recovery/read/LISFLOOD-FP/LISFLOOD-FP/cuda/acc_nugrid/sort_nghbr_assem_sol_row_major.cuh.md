---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/sort_nghbr_assem_sol_row_major.cuh
lines: 35
sha256: 10c95565a7d2772cf5c602318b51599289b44210402369950a4d48be258d7893
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sort_nghbr_assem_sol_row_major.cuh — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | `#pragma once` (1). CUDA 실행·표준 입출력·메모리·문자열, BLOCK_VAR_MACROS·CHECK_CUDA_ERROR·cuda_utils·AssembledSolution·get_lvl_idx·get_num_blocks·read_raster_file·write_raster_maps·MortonCode 헤더를 포함한다(3–15). lis::cuda::acc_nugrid 이름공간(namespace)을 연다(17–22). 전처리 조건 분기는 없다. |
| 24–35 | `__host__ void sort_nghbr_assem_sol_row_major` (24)는 호스트(host) 함수 원형이다. MortonCode* d_reverse_z_order·d_indices, AssembledSolution& d_buf_assem_sol·d_nghbr_assem_sol 및 int array_length를 받는다(25–31). 기본 인수와 실행 본문은 없다. 빈 줄과 이름공간 닫기(32–35). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
