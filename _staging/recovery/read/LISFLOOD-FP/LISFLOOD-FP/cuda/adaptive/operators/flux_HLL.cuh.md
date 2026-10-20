---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/flux_HLL.cuh
lines: 111
sha256: ece876c5876fbd1e73e51ba8bbfc4e688677610dc7cd2d6aa390facacd6a165e
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# flux_HLL.cuh — 판독 구간 기록

구간은 1행부터 111행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–17 | `#pragma once`로 중복 포함을 막고 CUDA 런타임과 흐름 벡터(FlowVector)·해석기·모의 매개변수를 포함한다(1–7). CUDA 장치 함수(device function) `flux_HLL_x`는 양쪽 상태와 매개변수를 참조로 받는다(9–17). 이 파일에는 전처리 조건 분기가 없으므로 매크로 조합별 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (9). |
| 18–41 | 시작 시 9–17행 `flux_HLL_x` 안. 양쪽 수심이 허용오차(tolerance)보다 작으면 기본 생성 흐름 벡터를 반환한다(18). 각 측의 수심·속도를 건조 조건으로 제한한다(20–26). 중력파 속도와 중간 수심·속도·파속을 구하고 HLL(Harten–Lax–van Leer) 파속 경계를 계산한다(28–41). 원문: `if (U_neg.h < solver_params.tol_h && U_pos.h < solver_params.tol_h) return FlowVector();` (18); `const real h_neg = (U_neg.h < solver_params.tol_h) ? C(0.0) : U_neg.h;`<br>`const real u_neg = (U_neg.h < solver_params.tol_h) ? C(0.0) : U_neg.qx / U_neg.h;`<br>`const real v_neg = (U_neg.h < solver_params.tol_h) ? C(0.0) : U_neg.qy / U_neg.h;` (20–22); `const real h_pos = (U_pos.h < solver_params.tol_h) ? C(0.0) : U_pos.h;`<br>`const real u_pos = (U_pos.h < solver_params.tol_h) ? C(0.0) : U_pos.qx / U_pos.h;`<br>`const real v_pos = (U_pos.h < solver_params.tol_h) ? C(0.0) : U_pos.qy / U_pos.h;` (24–26); `const real a_neg = sqrt(sim_params.g * h_neg);`<br>`const real a_pos = sqrt(sim_params.g * h_pos);` (28–29); `const real h_star =`<br>`( C(0.5) * (a_neg + a_pos) + C(0.25) * (u_neg - u_pos) ) * ( C(0.5) * (a_neg + a_pos) + C(0.25) * (u_neg - u_pos) )`<br>`/`<br>`sim_params.g;` (31–34); `const real u_star = C(0.5) * (u_neg + u_pos) + a_neg - a_pos;` (36); `const real a_star = sqrt(sim_params.g * h_star);` (38); `const real s_neg = (h_neg < solver_params.tol_h) ? u_pos - C(2.0) * a_pos : min(u_neg - a_neg, u_star - a_star);`<br>`const real s_pos = (h_pos < solver_params.tol_h) ? u_neg + C(2.0) * a_neg : max(u_pos + a_pos, u_star + a_star);` (40–41). |
| 42–88 | 시작 시 9–17행 `flux_HLL_x` 안. 좌우 물리 플럭스(flux)를 조립한다(43–55). 음측 파속이 0 이상이면 음측 플럭스를 반환한다(57–60). 두 파속 사이에 0이 있으면 수심·x운동량 플럭스와 중간 파속을 계산하고 횡운동량 플럭스를 선택한다(61–82). 나머지 `else`는 양측 플럭스를 반환한다(84–86). 함수 종료와 빈 줄을 포함한다(87–88). 원문: `const FlowVector F_neg =`<br>`{`<br>`U_neg.qx,`<br>`u_neg * U_neg.qx + C(0.5) * sim_params.g * h_neg * h_neg,`<br>`U_neg.qy * u_neg`<br>`};` (43–48); `const FlowVector F_pos =`<br>`{`<br>`U_pos.qx,`<br>`u_pos * U_pos.qx + C(0.5) * sim_params.g * h_pos * h_pos,`<br>`U_pos.qy * u_pos`<br>`};` (50–55); `if ( s_neg >= C(0.0) )` (57); `else if ( s_neg < C(0.0) && s_pos >= C(0.0) )` (61); `F.h =`<br>`( s_pos * F_neg.h - s_neg * F_pos.h + s_neg * s_pos * (h_pos - h_neg) )`<br>`/`<br>`(s_pos - s_neg);` (65–68); `F.qx =`<br>`( s_pos * F_neg.qx - s_neg * F_pos.qx + s_neg * s_pos * (U_pos.qx - U_neg.qx) )`<br>`/`<br>`(s_pos - s_neg);` (70–73); `const real s_mid =`<br>`( s_neg * h_pos * (u_pos - s_pos) - s_pos * h_neg * (u_neg - s_neg) )`<br>`/`<br>`( h_pos * (u_pos - s_pos) - h_neg * (u_neg - s_neg) );` (75–78); `F.qy = ( s_neg < C(0.0) && s_mid >= C(0.0) ) ? F.h * v_neg : F.h * v_pos;` (80); `else` (84). |
| 89–111 | 빈 줄과 CUDA 장치 함수 `flux_HLL_y` 선언이다(89–98). 상태를 회전(rotation)한 뒤 `flux_HLL_x`를 호출한다(99–108). 결과를 역회전하여 반환한다(110–111). 원문: `__device__ __forceinline__` (90); `FlowVector U_neg_rotated = { U_neg.h, U_neg.qy, -U_neg.qx };`<br>`FlowVector U_pos_rotated = { U_pos.h, U_pos.qy, -U_pos.qx };` (99–100); `FlowVector F_rotated = flux_HLL_x`<br>`(`<br>`U_neg_rotated,`<br>`U_pos_rotated,`<br>`solver_params,`<br>`sim_params`<br>`);` (102–108); `return { F_rotated.h, -F_rotated.qy, F_rotated.qx };` (110). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–26·43–55: 건조 측의 수심과 속도는 0으로 제한한다. 질량 플럭스의 첫 성분은 제한하지 않은 `U_neg.qx`와 `U_pos.qx`를 사용한다.
- 65–78: 중간 플럭스와 중간 파속 계산에는 분모가 있다. 해당 분모의 0 여부를 별도로 검사하는 분기는 이 함수에 없다.
