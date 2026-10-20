---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/init_sig_details.cuh
lines: 11
sha256: 3423ca22c10b5496ec94ca5d25e13b7908c7163645969945e9114623e11fb16e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# init_sig_details.cuh — 판독 구간 기록

구간은 1행부터 11행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | `#pragma once` (1). cuda_runtime.h와 device_launch_parameters.h를 포함하고 빈 줄을 둔다(2–5). 이 파일에는 전처리 조건 분기가 없다. |
| 6–11 | `__global__` (6)인 CUDA 커널(kernel) init_sig_details를 선언한다(7–11). 인수는 bool 포인터 d_sig_details와 int num_details이다(9–10). 기본 인수와 커널 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
