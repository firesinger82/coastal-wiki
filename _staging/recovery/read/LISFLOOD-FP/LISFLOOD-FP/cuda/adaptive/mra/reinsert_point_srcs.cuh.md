---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/reinsert_point_srcs.cuh
lines: 19
sha256: 5d686d7e648e1f9754593d31f4d2e43e5d4e6fca70ab989534520abeaad27066
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# reinsert_point_srcs.cuh — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | `#pragma once` (1) 뒤 CUDA 실행·장치 실행 인수, ScaleCoefficients·PointSources 및 get_lvl_idx 헤더를 포함한다(3–9). 조건부 전처리 분기는 없다. |
| 11–19 | `__global__` (11) 지정의 reinsert_point_srcs 커널(kernel) 선언이다(12–19). 인수는 ScaleCoefficients·PointSources와 real dt·dx_finest, int max_ref_lvl이다(14–18). 기본값은 선언하지 않는다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
