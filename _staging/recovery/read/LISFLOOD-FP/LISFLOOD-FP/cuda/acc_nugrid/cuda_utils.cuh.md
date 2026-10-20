---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/acc_nugrid/cuda_utils.cuh
lines: 53
sha256: dcb0e06f5f472f2d05fdcbdd7934630500015f13d6f7ac79388d1e79a7aa91f9
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_utils.cuh — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1), CUDA 실행 환경과 `CHECK_CUDA_ERROR.cuh` 포함(3·5). `lis::cuda::acc_nugrid` 이름 공간(namespace)을 연다(7–12). 전처리 조건 분기는 없다. |
| 14–26 | `cudaError_t`를 반환하는 `sync`, `peek`, `reset` 선언(14–18). `copy_cuda`는 목적지·원본 void 포인터와 size_t 바이트 수를 받는다(20–25). 인수 기본값은 없다. |
| 27–53 | `__host__ __device__` (27·33·39·45) 지정을 각 함수 앞에 둔다. `malloc_device`, `malloc_unified`는 바이트 수를 받아 void 포인터를 반환한다(28–37). `free_device`, `free_unified`는 void 포인터를 받아 `cudaError_t`를 반환한다(40–49). 이름 공간 종료(51–53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
