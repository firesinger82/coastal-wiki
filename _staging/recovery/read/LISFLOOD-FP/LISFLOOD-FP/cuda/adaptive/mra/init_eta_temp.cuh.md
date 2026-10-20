---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/init_eta_temp.cuh
lines: 13
sha256: 973ea83729a4f84133c04fd64f8e54b4a4bd99d1a32119d10031b9d55e15cb42
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# init_eta_temp.cuh — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–7 | `#pragma once` (1). cuda_runtime.h, device_launch_parameters.h, AssembledSolution.h를 포함한다(3–6). 빈 줄도 포함한다. 이 파일에는 전처리 조건 분기가 없다. |
| 8–13 | `__global__` (8)인 CUDA 커널(kernel) init_eta_temp 선언이다(9–13). AssembledSolution을 값으로 받고 출력 배열로 사용할 real 포인터 d_eta_temp를 받는다(11–12). 기본 인수와 커널 본문은 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
