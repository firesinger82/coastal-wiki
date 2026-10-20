---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/output/write_stage_point_data.cuh
lines: 31
sha256: 2d1de32dc6a551777c58ae8a154f7b9fa34ee0a957f74b8bed26a09f07b671f7
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_stage_point_data.cuh — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `#pragma once` (1)로 중복 포함을 막는다. `cuda_utils.cuh` (3), `<cstdio>`·`<cstdlib>` (5–6), `AssembledSolution.h`·`ScaleCoefficients.h`·`SolverParams.h`·`PlottingParams.h`·`StagePoints.h`·`FinestGrid.h` (8–13), `get_i_index.cuh`·`get_j_index.cuh` (15–16)를 포함한다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 18–31 | CUDA 호스트(host) 지시 `__host__` (18)와 `void write_stage_point_data` 원형을 선언한다(19–31). 격자 차원과 해석기·출력 설정은 상수 참조다(21–23). 조립 해(assembled solution), 최세 격자, 출력 지점(stage point)은 값 인수다(24–26). 현재 시간, x·y 격자 간격, 첫 단계 여부는 상수 참조다(27–30). 기본 인수 값이나 실행 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
