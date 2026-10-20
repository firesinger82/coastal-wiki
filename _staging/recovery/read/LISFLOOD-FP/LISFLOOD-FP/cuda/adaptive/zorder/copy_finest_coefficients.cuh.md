---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/copy_finest_coefficients.cuh
lines: 17
sha256: ecbaa4876c61ed5c979f6f76437a00f214a344a6adbd8114040e0181f935dc2d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# copy_finest_coefficients.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1)와 빈 줄(2) 뒤 `cuda_runtime.h`·`device_launch_parameters.h`를 포함한다(3–4). 빈 줄(5) 뒤 `AssembledSolution.h`, `ScaleCoefficients.h`, `SolverParams.h`를 포함한다(6–8). 마지막은 빈 줄(9)이다. 전처리 조건 분기는 없다. |
| 10–17 | `__global__` (10) 커널(kernel) `copy_finest_coefficients`를 선언한다(11–17). 인수는 `AssembledSolution d_assem_sol` (13), `ScaleCoefficients d_scale_coeffs` (14), `SolverParams solver_params` (15), `HierarchyIndex finest_lvl_idx` (16)이다. 반환형은 `void`이다. 함수 본문과 커널 실행 구문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
