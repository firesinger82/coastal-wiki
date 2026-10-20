---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/non_reflective_wave.cuh
lines: 94
sha256: d4f2618e53cc5d3d3ad12e4de15b367070c1f5b1ebfe36ff3b9c81a5969b6037
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# non_reflective_wave.cuh — 판독 구간 기록

구간은 1행부터 94행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–33 | `#pragma once`와 CUDA 런타임·표준 출력·실수 형식 헤더를 포함한다(1–7). 수심 hb와 속도 ub를 담는 `twodoubles` 구조체를 선언한다(9–13). CUDA 장치 함수(device function) `non_reflective_wave`는 입구 수심·dt·dxl·내부/경계 수심과 속도·중력을 받는다(15–27). 반복 횟수·종료 표시·오차 허용값·시작점·잔차를 초기화한다(28–32). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (15); `int k = 0, max_k = 100, cond = 0;` (28); `real Delta = C(1e-6), xa = -dxl / C(2.0), p0 = dxl / C(2.0), p1 = p0 - dxl / C(2.0), dp = C(0.0), relerr = C(0.0), f1 = C(0.0);` (30); `real f0 = (p0 - xa) + dt * ((ub - (p0 - xa) / dxl * (ub - up)) - sqrt(g * (hb - (p0 - xa) / dxl * (hb - hp))));` (32). |
| 34–55 | 시작 시 15–27행 `non_reflective_wave` 안. 반복 한도와 종료 표시를 검사하는 while 루프를 연다(34–35). Newton 방법(Newton method)의 미분값을 계산한다(36). 미분 절댓값이 0 이하이면 경고를 출력하고 cond=1·증분·다음 점을 설정한다(38–45). `else`는 잔차/미분으로 증분과 다음 점을 계산한다(47–50). 루프 안에서 새 잔차와 상대오차를 계산한다(53–54). 원문: `while ( (k <= max_k) && cond == 0 )` (34); `real df = C(1.0) + dt * ( (up - ub) / dxl - C(0.5) * pow((g * (hb - (p0 - xa) / dxl * (hb - hp))), C(-0.5)) * (g * (hp - hb) / dxl));` (36); `if ( abs(df) <= C(0.0) )` (38); `dp = p1 - p0;` (44); `else` (47); `dp = f0 / df;`<br>`p1 = p0 - dp;` (49–50); `f1     = (p1 - xa) + dt * ((ub - (p1 - xa) / dxl * (ub - up)) - sqrt(g * (hb - (p1 - xa) / dxl * (hb - hp))));`<br>`relerr = abs(dp) / ( abs(p1) + C(0.0) );` (53–54). |
| 56–80 | 시작 시 15–27행 함수·34행 while 루프 안. 상대오차, 잔차, 두 조건 동시 충족을 각각 별도 if로 검사하고 cond를 2·3·4로 설정한다(56–75). 각 성공 로그는 주석 처리되어 있다(60·67·74). p0와 f0를 새 값으로 옮기고 반복 횟수를 증가시킨 뒤 루프를 닫는다(77–80). 원문: `if (relerr < Delta)` (56); `if (abs(f1) < Delta)` (63); `if ( (relerr <= Delta) && (abs(f1) < Delta) )` (70); `k++;` (79). |
| 81–94 | 시작 시 15–27행 `non_reflective_wave` 안이며 34행 루프 밖. 추적점에서 수심·속도를 보간(interpolation)하고 파속을 계산한다(82–84). 음의 특성량(characteristic variable)과 고정 수심 상수 `C(0.13535)`를 쓰는 양의 특성량을 계산한다(86–87). 출력 수심·속도를 계산하여 구조체로 반환한다(89–94). 원문: `real hr = hb - (hb - hp) * (p1 - xa) / dxl;`<br>`real ur = ub - (ub - up) * (p1 - xa) / dxl;`<br>`real cr = sqrt(g * hr);` (82–84); `real beta_minus = ur - C(2.0) * cr;`<br>`real beta_plus  = C(2.0) * sqrt(g * (h_inlet + C(0.13535))) + h_inlet * sqrt(g / C(0.13535));` (86–87); `real h_out = C(1.0) / C(16.0) / g * (beta_plus - beta_minus) * (beta_plus - beta_minus);`<br>`real u_out = C(0.5) * (beta_plus + beta_minus);` (90–91). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28·34·79: 반복 한도는 `max_k = 100`이다. 반복 조건은 `k <= max_k`이고 k는 루프 끝에서 증가한다.
- 38–54: 미분값 0 분기에서 cond를 1로 설정한 뒤에도 같은 반복의 잔차와 상대오차 계산을 수행한다. 상대오차의 분모는 `abs(p1) + C(0.0)`이다.
- 56–75: 세 종료 검사는 else if가 아닌 별도 if이다. 뒤의 검사가 참이면 앞서 설정한 cond를 덮어쓴다.
- 87: 양의 특성량 식은 고정 상수 `C(0.13535)`를 두 번 사용한다. 이 상수는 함수 인수로 받지 않는다.
