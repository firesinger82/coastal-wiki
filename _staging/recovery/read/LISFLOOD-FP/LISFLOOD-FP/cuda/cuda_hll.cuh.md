---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_hll.cuh
lines: 26
sha256: 04d61504da242cd32c91a1c124a7414c8852be64741a8db8524def04fbdea52f
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_hll.cuh — 판독 구간 기록

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), lisflood·cuda_flow 헤더(2–3), lis::cuda 이름 공간(namespace)(5–8), HLL 구조체(10–11). 별도 전처리 조건 분기는 없다. |
| 12–26 | 시작 시 10행 구조체 안. `__device__ static FlowVector x` (12), `__device__ static FlowVector y` (18)의 원형은 const FlowVector& U_neg·U_pos를 받아 FlowVector를 반환한다(13–16·19–22). 구조체·이름 공간 종료(23–26). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
