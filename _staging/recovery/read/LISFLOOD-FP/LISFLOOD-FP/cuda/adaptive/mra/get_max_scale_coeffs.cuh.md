---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/get_max_scale_coeffs.cuh
lines: 18
sha256: ed943663c0f8537d095b37565038808c5b83cdabd6a9c397edd86dfabff8c9a2
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_max_scale_coeffs.cuh — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1). BLOCK_VAR_MACROS.cuh, AssembledSolution.h, Maxes.h, get_num_blocks.h, init_eta_temp.cuh, get_max_from_array.cuh를 포함한다(3–11). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 13–18 | `__host__` (13)인 get_max_scale_coeffs를 선언한다(14–18). 반환 형식은 Maxes이다. 인수는 AssembledSolution 참조 d_assem_sol과 real 포인터 참조 d_eta_temp이다(16–17). 기본 인수와 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
