---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/zorder/get_i_index.cuh
lines: 9
sha256: 4ca2e24faf5375d45a051648e5ead72404014ec2c1504a906f811cd2e0641cf4
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_i_index.cuh — 판독 구간 기록

구간은 1행부터 9행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–4 | `#pragma once` (1)와 빈 줄(2) 뒤 `../zorder/compact.cuh`를 포함한다(3). 마지막은 빈 줄(4)이다. 전처리 조건 분기는 없다. |
| 5–9 | `__host__ __device__ __forceinline__` (5) 함수 `Coordinate get_i_index(MortonCode code)`를 정의한다(6–7). 반환식은 `return compact(code);` (8)이다. 모턴 코드(Morton code)를 `compact`에 그대로 전달한 좌표를 반환한다. 함수 종료(9)이다. |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
