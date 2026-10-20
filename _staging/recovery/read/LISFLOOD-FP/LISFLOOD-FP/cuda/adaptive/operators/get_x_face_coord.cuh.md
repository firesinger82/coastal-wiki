---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_x_face_coord.cuh
lines: 35
sha256: 6f7576cd25f09de184ae57cc7d5e33da2889fdd5e3e36a43eae0da99788eff23
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_x_face_coord.cuh — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–17 | `#pragma once`와 CUDA 런타임·실수·방향 형식 헤더를 포함한다(1–6). CUDA 장치 함수(device function) `get_x_face_coord`는 중심 x좌표·지역 x간격·방향을 받는다(8–15). 반환용 면 좌표(face coordinate)를 `C(0.0)`으로 초기화한다(16). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (8). |
| 18–35 | 시작 시 8–15행 `get_x_face_coord` 안. 방향 switch로 북·남 면의 x중앙, 동 면의 오른쪽 끝, 서 면의 왼쪽 끝 좌표를 구한다(18–29). default는 갱신 없이 break한다(30–31). 면 좌표를 반환하고 함수를 닫는다(34–35). 원문: `switch (direction)` (18); `case NORTH:`<br>`case SOUTH:`<br>`x_face = x - dx_loc / C(2.0) + C(0.5) * dx_loc;` (20–22); `case EAST:`<br>`x_face = x - dx_loc / C(2.0) + C(1.0) * dx_loc;` (24–25); `case WEST:`<br>`x_face = x - dx_loc / C(2.0) + C(0.0) * dx_loc;` (27–28); `default:` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 16·30–34: 나열한 방향 이외의 입력은 초기값 `C(0.0)`을 그대로 반환한다.
