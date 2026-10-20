---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/rev_z_order_reals.cuh
lines: 18
sha256: e99d7f9ba4cb3de723e39fac6e1eaaf9c4c224a79ea266e0cacb01c3923cbfeb
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# rev_z_order_reals.cuh — 판독 구간 기록

구간은 1행부터 18행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | `#pragma once` (1). cuda_utils·CUB 기수 정렬(radix sort)·real·MortonCode 헤더 포함(3–8)과 빈 줄. 별도 전처리 조건 분기는 없다. |
| 10–18 | `__host__` (10) rev_z_order_reals 원형. d_rev_z_order·d_indices는 MortonCode 포인터, d_array·d_array_sorted는 real 포인터, array_length는 int다(11–18). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
