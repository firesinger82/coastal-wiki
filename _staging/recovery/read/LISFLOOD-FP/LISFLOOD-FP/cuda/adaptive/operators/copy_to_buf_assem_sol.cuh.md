---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/copy_to_buf_assem_sol.cuh
lines: 12
sha256: ed60772acb93c993233495bc8b730d4a906996b8b101565a9aa0d786b3e9073a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# copy_to_buf_assem_sol.cuh — 판독 구간 기록

구간은 1행부터 12행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1) 뒤 CUDA 유틸리티와 AssembledSolution 헤더를 포함한다(3·5). 조건부 전처리 분기는 없다. |
| 7–12 | `__host__` (7) 지정의 copy_to_buf_assem_sol 호스트(host) 함수를 선언한다(8–12). 입력은 const AssembledSolution&이며 출력은 AssembledSolution&다(10–11). 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
