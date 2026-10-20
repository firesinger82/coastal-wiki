---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/rev_z_order_act_idcs.cuh
lines: 17
sha256: ecb8967547f747fea3ada04d4c12579ae93f0fd729569aa662289a824677efc5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rev_z_order_act_idcs.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_utils.cuh`를 포함한다(3). 빈 줄(4) 뒤 `cub/cub.cuh`를 포함한다(5). 빈 줄(6) 뒤 `AssembledSolution.h`와 `MortonCode.h`를 포함한다(7–8). 마지막은 빈 줄(9)이다. 전처리 조건 분기는 없다. |
| 10–17 | `__global__` (10) 커널(kernel) `void rev_z_order_act_idcs`의 원형을 선언한다(11–17). 인수는 `MortonCode* d_rev_row_major` (13), `AssembledSolution d_buf_assem_sol` (14), `AssembledSolution d_assem_sol` (15), `const int num_finest_elems` (16)이다. 함수 본문과 커널 실행 구문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
