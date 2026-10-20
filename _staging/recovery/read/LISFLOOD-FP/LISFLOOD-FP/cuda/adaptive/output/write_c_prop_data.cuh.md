---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_c_prop_data.cuh
lines: 25
sha256: 4ab043927e2d2cdefa1aed0ab1a68414da3de2bc5f95e9f8964f9bf09032bb40
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_c_prop_data.cuh — 판독 구간 기록

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1)로 중복 포함을 막는다. `SolverParams.h`·`PlottingParams.h`·`AssembledSolution.h`를 포함한다(3–5). `write_cumulative_data.h` (7)와 `append_reals_to_file.cuh` (9)를 포함한다. 빈 줄도 이 구간에 포함된다. 조건부 전처리 분기는 없다. |
| 11–25 | CUDA 호스트(host) 지시 `__host__` (11)와 `void write_c_prop_data` 원형을 선언한다(12–25). `PlottingParams`, `clock_t`, `SolverParams`, `SimulationParams`, `AssembledSolution`과 실수 인수 네 개, 정수 셀 수, 불리언 첫 단계 여부를 모두 상수 참조로 받는다(14–24). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
