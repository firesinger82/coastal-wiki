---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_y_face_coord.cuh
lines: 35
sha256: 423936f13ef51f9540a1da6d2c408675bebaa28ac835f21c342e3df785434185
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_y_face_coord.cuh — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–17 | `#pragma once`와 CUDA 런타임·실수·방향 형식 헤더를 포함한다(1–6). CUDA 장치 함수(device function) `get_y_face_coord`는 중심 y좌표·지역 y간격·방향을 받는다(8–15). 반환용 면 좌표(face coordinate)를 `C(0.0)`으로 초기화한다(16). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (8). |
| 18–35 | 시작 시 8–15행 `get_y_face_coord` 안. 방향 switch에서 북 면은 위쪽 끝, 동·서 면은 y중앙, 남 면은 아래쪽 끝 좌표를 구한다(18–29). default는 갱신 없이 break한다(30–31). 면 좌표를 반환하고 함수를 닫는다(34–35). 원문: `switch (direction)` (18); `case NORTH:`<br>`y_face = y - dy_loc / C(2.0) + C(1.0) * dy_loc;` (20–21); `case EAST:`<br>`case WEST:`<br>`y_face = y - dy_loc / C(2.0) + C(0.5) * dy_loc;` (23–25); `case SOUTH:`<br>`y_face = y - dy_loc / C(2.0) + C(0.0) * dy_loc;` (27–28); `default:` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·30–34: 나열한 방향 이외의 입력은 초기값 `C(0.0)`을 그대로 반환한다.
