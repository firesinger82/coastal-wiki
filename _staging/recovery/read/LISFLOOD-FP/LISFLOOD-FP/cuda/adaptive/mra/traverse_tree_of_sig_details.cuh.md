---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/traverse_tree_of_sig_details.cuh
lines: 26
sha256: a2aa235ec516f55799bc600a262d72c31278c444391881467ffa39121d702e30
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# traverse_tree_of_sig_details.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1), CUDA 실행·CUB 블록 저장·BLOCK_VAR_MACROS·HierarchyIndex·AssembledSolution·MortonCode·SolverParams·ScaleCoefficients·get_lvl_idx 헤더를 포함한다(3–16). 조건부 전처리 분기는 없다. |
| 18–26 | `__global__` (18) 지정의 traverse_tree_of_sig_details 커널(kernel)을 선언한다(19–26). 인수는 유의 상세 bool 포인터, 스케일 계수(scale coefficient), 조립 해(assembled solution) 버퍼(buffer), num_threads, SolverParams다(21–25). 기본 인수나 실행 설정은 이 선언에 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
