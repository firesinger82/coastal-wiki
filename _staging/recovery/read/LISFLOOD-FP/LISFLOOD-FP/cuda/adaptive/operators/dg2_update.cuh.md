---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/dg2_update.cuh
lines: 34
sha256: 01cd9329a9fb20d099a0b6f1ecf2f365db874edc688b1372a2080c03c70efacb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# dg2_update.cuh — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#pragma once` (1) 뒤 CUDA 실행·CUB 블록 스캔(block scan)·BLOCK_VAR_MACROS·MortonCode·Neighbours·FlowCoeffs·SolverParams·SimulationParams·FlowVector 및 get_leg_basis·get_bed_src·flux_HLL 헤더를 포함한다(3–18). 조건부 전처리 분기는 없다. |
| 20–34 | `__global__` (20) 지정의 dg2_update 커널(kernel)을 선언한다(21–34). 이웃(neighbour), 읽을 조립 해(assembled solution)와 저장할 조립 해, 솔버(solver)·모의 매개변수, real dx_finest·dy_finest·dt, int test_case, real* d_dt_CFL, bool rkdg2를 받는다(23–33). 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
