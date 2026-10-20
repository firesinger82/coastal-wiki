---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/tests/h_init.cuh
lines: 78
sha256: 905f68b76075591582816b1042364461dffaa78c5902329195e57af52758a3b5
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# h_init.cuh — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | `#pragma once` (1)로 중복 포함을 막는다. 월류(overtopping)·c-property·방사형(radial)·세 봉우리·세 블록·포물선 그릇(parabolic bowl) 초기화 헤더를 포함한다(3–8). CUDA 장치(device) 지시와 강제 인라인 지시 `__device__ __forceinline__` (10)가 붙은 `h_init`을 정의한다(11–19). `x_int`·`y_int`·`z_int`, `Depths1D` 경계값, 시험 번호를 상수 참조로 받는다(13–17). 초기값은 `real h_int = 0;` (20)다. 빈 줄도 포함된다. 조건부 전처리 분기는 없다. |
| 22–45 | 시작 시 11–19행 `h_init` 본문 안. 원문 분기는 `switch (test_case)` (22)다. `case 1:` (24)과 `case 3:` (25)은 `h_int = h_init_c_property(bcs, z_int, x_int);` (26), `case 2:` (28)와 `case 4:` (29)는 `h_int = h_init_c_property(bcs, z_int, y_int);` (30)을 실행한다. 주석은 각각 x·y 방향의 젖은 상태와 젖음·마름 상태 c-property 시험이다(24–29). `case 5:` (32), `case 7:` (33), `case 9:` (34), `case 11:` (35), `case 13:` (36)은 `h_int = h_init_overtopping(bcs, z_int, x_int);` (37)을 실행한다. `case 6:` (39), `case 8:` (40), `case 10:` (41), `case 12:` (42), `case 14:` (43)는 `h_int = h_init_overtopping(bcs, z_int, y_int);` (44)를 실행한다. 주석은 젖은·마른 댐 붕괴(dam break), 마찰 포함, 건물 월류 시험의 방향을 구분한다(32–43). 각 실행 묶음은 `break;`로 끝난다(27·31·38·45). |
| 46–63 | 시작 시 11–19행 `h_init` 본문·22행 `switch (test_case)` 안. `case 15:` (46)의 원문 삼항식은 `h_int = ( x_int < C(15.5) ) ? C(0.75) : C(0.0);` (47)다. `case 16:` (49)은 `h_int = ( y_int < C(15.5) ) ? C(0.75) : C(0.0);` (50)다. 주석은 x·y 방향 삼각형 댐 붕괴 시험이다(46·49). `case 17:` (52)은 `h_int = h_init_parabolic_bowl(x_int, z_int);` (53), `case 18:` (55)은 `h_int = h_init_parabolic_bowl(y_int, z_int);` (56)다. `case 19:` (58)은 `h_int = C(1.0) - z_int;` (59), `case 20:` (61)은 `h_int = ( x_int < C(16.0) ) ? max( (C(1.875) - z_int), C(0.0) ) : C(0.0);` (62)다. 주석은 세 원뿔과 그 댐 붕괴 시험을 구분한다(58·61). 각 case는 `break;`로 끝난다(48·51·54·57·60·63). |
| 64–78 | 시작 시 11–19행 `h_init` 본문·22행 `switch (test_case)` 안. `case 21:` (64)은 미분 기하(differential geometry) 시험 주석과 `h_int = C(1.95) - z_int;` (65), `case 22:` (67)는 원문 `non-differential geometry` 시험 주석과 `h_int = C(1.78) - z_int;` (68)를 갖는다. `case 23:` (70)은 방사형 댐 붕괴 주석과 `h_int = h_init_radial(x_int, y_int);` (71)을 갖는다. 각 실행 뒤 `break;`가 있다(66·69·72). `default:` (73)는 대입 없이 `break;`만 수행한다(74). switch를 닫고 `return h_int;`로 반환한 뒤 함수를 닫는다(75–78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–7·22–75: `h_init_three_peaks.cuh`와 `h_init_three_blocks.cuh`를 포함하지만 switch 본문에는 두 이름의 함수 호출이 없다. case 21·22는 수심 식을 직접 대입한다(65·68).
- 59·62·65·68: case 19·21·22의 수심 대입에는 0 하한 제한이 없다. case 20의 왼쪽 상태 식에는 `max( (C(1.875) - z_int), C(0.0) )`가 있다.
- 20·73–77: 나열되지 않은 시험 번호의 default는 `h_int`를 변경하지 않는다. 이 경로의 반환값은 초기값 0이다.
