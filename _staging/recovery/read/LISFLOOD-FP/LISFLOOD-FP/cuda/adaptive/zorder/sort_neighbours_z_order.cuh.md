---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/sort_neighbours_z_order.cuh
lines: 22
sha256: 2fd503cd612c8625d25730bfd0a85b98ae1907457728266343864fb53d562a59
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# sort_neighbours_z_order.cuh — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | `#pragma once` (1). CUDA 런타임(runtime)·CUB 정렬·CHECK_CUDA_ERROR·cuda_utils·Neighbours·MortonCode·SolverParams 헤더 포함(3–12)과 빈 줄. 별도 전처리 조건 분기는 없다. |
| 14–22 | `__global__` (14) 커널(kernel) sort_neighbours_z_order 원형. 두 const Neighbours 값, MortonCode 포인터, const int num_finest_elems, const SolverParams를 받는다(15–22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
