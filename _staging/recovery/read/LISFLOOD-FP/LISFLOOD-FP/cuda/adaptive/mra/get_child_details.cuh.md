---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/mra/get_child_details.cuh
lines: 23
sha256: f49871d0106931c8c8ceb6ff699b9c896a2c019e1ed98d765539b7228da13dc5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_child_details.cuh — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | `#pragma once` (1). CUDA 실행 환경과 DetailChildren 형식 헤더를 포함하고 빈 줄을 둔다(2–6). 이 파일에는 전처리 조건 분기가 없다. |
| 7–23 | `__device__ __forceinline__` (7)인 get_child_details 장치 함수(device function)는 bool 배열 shared_child_details와 t_idx를 받는다(8–13). 집합 초기화(aggregate initialization)의 원문은 `DetailChildren child_details =` (14), `{` (15), `shared_child_details[t_idx + 0], // detail_0` (16), `shared_child_details[t_idx + 1], // detail_1` (17), `shared_child_details[t_idx + 2], // detail_2` (18), `shared_child_details[t_idx + 3]  // detail_3` (19), `};` (20)이다. 연속 네 원소를 detail_0부터 detail_3까지 배치하고 child_details를 반환한다(22). 닫는 중괄호까지 포함한다(23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–20: 함수는 배열 길이를 인수로 받지 않는다. t_idx부터 t_idx + 3까지 접근하기 전에 경계를 검사하는 조건문은 이 함수에 없다.
