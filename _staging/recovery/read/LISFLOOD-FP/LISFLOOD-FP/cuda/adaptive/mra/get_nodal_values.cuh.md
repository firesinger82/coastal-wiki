---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/get_nodal_values.cuh
lines: 22
sha256: 12855bce88f7838e398750fbebccd4b430e68663611213dce1937f16dbe392f1
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_nodal_values.cuh — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | `#pragma once` (1). CUDA 실행 환경, cuda_utils.cuh, BLOCK_VAR_MACROS.cuh, SimulationParams.h, get_num_blocks.h, init_nodal_values.cuh를 포함한다(3–11). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 13–22 | `__host__ void get_nodal_values` (13)를 선언한다. NodalValues 참조, real의 const 참조 dx_finest와 dy_finest, Depths1D와 SimulationParams의 const 참조 bcs와 sim_params, const int 참조 interface_dim과 test_case를 받는다(15–21). 기본 인수와 함수 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
