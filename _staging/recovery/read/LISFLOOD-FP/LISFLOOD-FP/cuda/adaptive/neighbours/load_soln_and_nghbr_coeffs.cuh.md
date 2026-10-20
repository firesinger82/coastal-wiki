---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/load_soln_and_nghbr_coeffs.cuh
lines: 19
sha256: b6e8bc44aa064c7033aae9bb5616239d5cde81f7ad9877edd4d70b63358fdc81
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# load_soln_and_nghbr_coeffs.cuh — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1) 뒤 장치 실행 인수·CUB 블록 기수 정렬(block radix sort)·Neighbours·ScaleCoefficients·AssembledSolution·SolverParams 헤더를 포함한다(3–10). 조건부 전처리 분기는 없다. |
| 12–19 | `__global__` (12) 지정의 load_soln_and_nghbr_coeffs 커널(kernel)을 선언한다(13–19). Neighbours·ScaleCoefficients·AssembledSolution·SolverParams를 받으며 기본 인수는 없다(15–18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
