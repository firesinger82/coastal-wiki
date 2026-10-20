---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/calculate_dt.cuh
lines: 26
sha256: b77027aeaa62c75b057f1396d0cb26d35f958d9b9d04a3c710cc86fe1bd4b45f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# calculate_dt.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | `#pragma once` (1), cuda_runtime·device_launch_parameters·stdio·AssembledSolution 포함(3–6), `lis::cuda::acc_nugrid` 이름공간(namespace)(8–13). 나머지는 빈 줄. 이 파일의 모든 구간에는 `#if` 계열 전처리 조건 분기가 없다. |
| 15–26 | `__global__ void` (15)의 calculate_dt 커널(kernel) 선언(16–22). AssembledSolution d_assem_sol·Pars pars·Solver solver는 값 인수(18–20), d_dt_CFL은 NUMERIC_TYPE* 출력 배열 인수(21). 본문·계산식·기본 인수값은 없다. 빈 줄·이름공간 종료(23–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
