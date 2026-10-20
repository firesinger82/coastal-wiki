---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_soln_vtk.cuh
lines: 28
sha256: 3ed231eaffc07c4e6c655aa8acea72b71a5785a7b12c4193fecfde3dab5ccb0d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_soln_vtk.cuh — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1)로 중복 포함을 막는다. `<cstdio>`·`<cstdlib>` (3–4), `cuda_utils.cuh` (6), `Points.h`·`AssembledSolution.h`·`SimulationParams.h`·`SolverParams.h`·`PlottingParams.h`·`SaveInterval.h` (8–13), `compact.cuh`·`get_lvl_idx.cuh` (15–16)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 18–28 | CUDA 호스트(host) 지시가 붙은 `__host__ void write_soln_vtk` (18) 원형을 선언한다(19–28). 출력 설정, 조립 해(assembled solution), 실수 포인터 `d_dt_CFL`, 최세 격자의 x·y 간격, 모의 설정, 해석기 설정, 저장 간격을 받는다(20–27). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
