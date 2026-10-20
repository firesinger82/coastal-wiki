---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/classes/DetailChildren.h
lines: 20
sha256: 14bbe6f50be3bae3dccd1e1f23cacda8439e284aa2a3bb7c6ba0077a4db799f5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# DetailChildren.h — 판독 구간 기록

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | `#pragma once` (1), cuda_runtime.h 포함(3). 전처리 조건 분기는 없다. DetailChildren은 bool detail_0·detail_1·detail_2·detail_3를 보유한다(5–10). 멤버 초기값은 없다. |
| 12–20 | 시작 시 5–6행 DetailChildren 구조체 안. `__device__ __forceinline__` (12)의 has_sig_detail(13–14)에서 논리합 `bool is_sig = (detail_0 \|\| detail_1 \|\| detail_2 \|\| detail_3);` (15)을 계산한다. is_sig 반환 후 메서드·구조체 종료(17–20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
