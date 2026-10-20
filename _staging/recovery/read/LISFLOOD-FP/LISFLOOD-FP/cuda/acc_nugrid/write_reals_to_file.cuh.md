---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/write_reals_to_file.cuh
lines: 28
sha256: cd1ecbde57d42dfab9f31bcff61550b4d4a7a35ff2ca4c25788092989b6c3d71
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# write_reals_to_file.cuh — 판독 구간 기록

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1). cuda_runtime.h, stdio.h, string.h, cuda_utils.cuh, ../../lisflood.h를 포함한다(3–9). 전처리 조건 분기는 없다. |
| 11–28 | lis::cuda::acc_nugrid 이름공간(11–16)에서 `__host__ void write_reals_to_file` (18)를 선언한다. 인수는 filename·respath, NUMERIC_TYPE* d_results, const int& array_length(20–23). 기본 인수·실행 본문은 없다. 선언과 이름공간을 닫는다(24–28). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
