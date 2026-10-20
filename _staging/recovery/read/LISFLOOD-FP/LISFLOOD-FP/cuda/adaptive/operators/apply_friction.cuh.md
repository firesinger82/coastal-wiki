---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/apply_friction.cuh
lines: 53
sha256: 7e1bf69facdb843405bdd757840419b965310a9a3ac5cfe778f62abcd044641d
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# apply_friction.cuh — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | `#pragma once` (1), CUDA 실행 및 real 형식 헤더 포함(3·5). 조건부 전처리 분기는 없다. `__device__ __forceinline__` (7) 지정의 장치(device) 인라인(inline) 함수 apply_friction을 정의한다(8–19). 깊이 h·깊이 허용값 tol_h·속도 허용값 tol_s·조도 n·중력 g·시간 간격 dt는 const real 참조로 받고 qx·qy는 갱신할 real 참조로 받는다(10–17). 기본 인수는 없다. |
| 20–40 | 시작 시 7–19행 apply_friction 함수 안. `bool below_depth = (h < tol_h);` (20) 뒤 `if (below_depth)` (22)이면 qx·qy를 C(0.0)으로 설정하고 반환한다(24–27). `real ux = qx / h;`<br>`real uy = qy / h;` (30–31)로 두 속도를 계산한다. `if (abs(ux) < tol_s && abs(uy) < tol_s)` (33)이면 qx·qy를 C(0.0)으로 설정하고 반환한다(35–38). |
| 41–53 | 시작 시 7–19행 apply_friction 함수 안이며 두 조기 반환 조건 밖. `real Cf = g * n * n / pow( h, C(1.0) / C(3.0) );` (41)로 마찰 계수(friction coefficient)를 계산한다. `real speed = sqrt(ux * ux + uy * uy);` (43)으로 속력, `real Sf_x = -Cf * ux * speed;`<br>`real Sf_y = -Cf * uy * speed;` (45–46)으로 두 마찰 항을 구한다. `real D_x = C(1.0) + dt * Cf / h * (C(2.0) * ux * ux + uy * uy) / speed;`<br>`real D_y = C(1.0) + dt * Cf / h * (C(2.0) * uy * uy + ux * ux) / speed;` (48–49)로 두 분모를 계산하고 `qx += dt * Sf_x / D_x;`<br>`qy += dt * Sf_y / D_y;` (51–52)로 qx·qy를 갱신한다. 함수 종료(53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33·43·48–49: 속도에 의한 조기 반환 조건은 두 성분의 abs 값이 모두 tol_s보다 작은 경우다. 이후 분모로 쓰는 speed에 대한 별도 speed == 0 검사는 없다. tol_s의 설정 범위는 이 파일에 없다.
