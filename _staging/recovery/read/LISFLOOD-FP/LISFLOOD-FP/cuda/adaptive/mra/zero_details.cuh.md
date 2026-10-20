---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/zero_details.cuh
lines: 17
sha256: da5287909b562d323e6afa4ec05169c8b29f4edcd7379b80e7d03d33b9f8bd24
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# zero_details.cuh — 판독 구간 기록

구간은 1행부터 17행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1) 뒤 CUDA 실행·장치 실행 인수·Details·HierarchyIndex·SolverParams 헤더를 포함한다(3–8). 조건부 전처리 분기는 없다. |
| 10–17 | `__global__` (10) 지정의 zero_details 커널(kernel)을 선언한다(11–17). 인수는 Details, real 포인터 d_norm_details, int num_details, SolverParams이며 기본값은 없다(13–16). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
