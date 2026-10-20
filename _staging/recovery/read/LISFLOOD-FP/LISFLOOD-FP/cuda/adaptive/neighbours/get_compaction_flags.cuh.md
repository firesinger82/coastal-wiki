---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/neighbours/get_compaction_flags.cuh
lines: 20
sha256: 6aa593a043e8ca28a41dee8092c3f34d77808b0948cdf69a9c36926becff8619
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_compaction_flags.cuh — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1) 뒤 CUDA 실행·CUB 블록 로드(block load)·BLOCK_VAR_MACROS·HierarchyIndex·CompactionFlags·AssembledSolution 헤더를 포함한다(3–12). 조건부 전처리 분기는 없다. |
| 14–20 | `__global__` (14) 지정의 get_compaction_flags 커널(kernel)을 선언한다(15–20). AssembledSolution·CompactionFlags와 int num_finest_elems를 받는다(17–19). 기본 인수는 없다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
