---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/topo.cuh
lines: 72
sha256: 6d802f1e0ceed126832390464ce59bd867946c6a4790999a3c9eaf7cf9f3e6d6
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# topo.cuh — 판독 구간 기록

구간은 1행부터 72행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | `#pragma once` (1)로 중복 포함을 막는다. `topo_c_prop_1D.cuh`·`topo_three_cones.cuh`·`topo_diff.cuh`·`topo_non_diff.cuh`·`topo_triangle.cuh`·`topo_parabolic_bowl.cuh`를 포함한다(3–8). x·y 절점(nodal point) 값에 따른 이론 지형 생성이라는 주석(10) 뒤 CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (11)를 사용한다. `topo`는 x·y 좌표와 시험 번호를 상수 참조로 받는다(12–18). 기본 지반고는 `real z_int = C(0.0);` (19)다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 21–40 | 시작 시 12–18행 `topo` 본문 안. 원문 분기는 `switch (test_case)` (21)다. `case 1:` (23)·`case 3:` (24)은 x 방향 주석과 `z_int = topo_c_prop_1D(x_int);` (26)을 갖는다. `case 2:` (28)·`case 4:` (29)는 y 방향 주석과 `z_int = topo_c_prop_1D(y_int);` (31)을 갖는다. `case 11:` (33)·`case 13:` (34)은 x 방향 건물 월류(overtopping) 주석과 `z_int = topo_c_prop_1D(x_int);` (35)을 갖는다. `case 12:` (37)·`case 14:` (38)는 y 방향 건물 월류 주석과 `z_int = topo_c_prop_1D(y_int);` (39)를 갖는다. 각 묶음은 `break;`로 끝난다(27·32·36·40). |
| 41–60 | 시작 시 12–18행 `topo` 본문·21행 `switch (test_case)` 안. `case 15:` (41)는 `z_int = topo_triangle(x_int);` (42), `case 16:` (44)은 `z_int = topo_triangle(y_int);` (45)를 실행한다. `case 17:` (47)은 x 방향 포물선 그릇(parabolic bowl)과 `y = ax^2` 주석(48–49), `z_int = topo_parabolic_bowl(x_int);` (50)을 갖는다. `case 18:` (52)은 y 방향 주석(53)과 `z_int = topo_parabolic_bowl(y_int);` (54)를 갖는다. `case 19:` (56)·`case 20:` (57)은 세 원뿔(three cones)의 c-property·댐 붕괴(dam break) 주석(58)과 `z_int = topo_three_cones(x_int, y_int);` (59)를 갖는다. 각 실행 묶음은 `break;`로 끝난다(43·46·51·55·60). |
| 61–72 | 시작 시 12–18행 `topo` 본문·21행 `switch (test_case)` 안. `case 21:` (61)은 `z_int = topo_diff(x_int, y_int);` (62), `case 22:` (64)는 `z_int = topo_non_diff(x_int, y_int);` (65)를 실행하며 각각 `break;`가 있다(63·66). `default:` (67)는 값 변경 없이 `break;`만 실행한다(68). switch 종료·빈 줄 뒤 `return z_int;`로 반환하고 함수를 닫는다(69–72). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19·21–69: case 5–10과 case 23의 개별 분기는 없다. 이 시험 번호들은 default에서 지반고를 변경하지 않으므로 초기값 `C(0.0)`이 반환된다.
