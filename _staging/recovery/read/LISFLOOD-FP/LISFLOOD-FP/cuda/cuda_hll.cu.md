---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/cuda_hll.cu
lines: 123
sha256: 6454d39abda80bf3e8e0613eee13560554038cdcfe10544cfc076b03249057fa
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# cuda_hll.cu — 판독 구간 기록

구간은 1행부터 123행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | hll·solver 헤더(1–2). `__device__ lis::cuda::FlowVector lis::cuda::HLL::y` (4)는 x방향 리만 해법(Riemann solver) 호출을 위해 `FlowVector u_neg_rotated = { u_neg.H, u_neg.HV, -u_neg.HU };` (10), `FlowVector u_pos_rotated = { u_pos.H, u_pos.HV, -u_pos.HU };` (11). `FlowVector F_rotated = HLL::x(u_neg_rotated, u_pos_rotated);` (13), `return { F_rotated.H, -F_rotated.HV, F_rotated.HU };` (15). 전처리 조건 분기는 없다. |
| 18–53 | `__device__ lis::cuda::FlowVector lis::cuda::HLL::x` (18). 연속 조건 `if (u_neg.H <= cuda::solver_params.DepthThresh &&` (24), `u_pos.H <= cuda::solver_params.DepthThresh)` (25)는 FlowVector() 반환(27). U_neg·V_neg=0(30–31), `if (u_neg.H > cuda::solver_params.DepthThresh)` (32)는 `U_neg = u_neg.HU / u_neg.H;` (34), `V_neg = u_neg.HV / u_neg.H;` (35). U_pos·V_pos=0(38–39), `if (u_pos.H > cuda::solver_params.DepthThresh)` (40)는 `U_pos = u_pos.HU / u_pos.H;` (42), `V_pos = u_pos.HV / u_pos.H;` (43). `NUMERIC_TYPE A_neg = SQRT(cuda::physical_params.g * u_neg.H);` (46), `NUMERIC_TYPE A_pos = SQRT(cuda::physical_params.g * u_pos.H);` (47). `NUMERIC_TYPE H_star = POW(C(0.5)*(A_neg+A_pos) + C(0.25)*(U_neg - U_pos),` (49), `C(2.0))	/ cuda::physical_params.g;` (50). `NUMERIC_TYPE U_star = C(0.5)*(U_neg + U_pos) + A_neg - A_pos;` (51), `NUMERIC_TYPE A_star = SQRT(cuda::physical_params.g*H_star);` (52). |
| 54–85 | 시작 시 18행 HLL::x 안. `if (u_neg.H <= cuda::solver_params.DepthThresh)` (55)는 `S_neg = U_pos - C(2.0)*A_pos;` (57), `else` (59)는 `S_neg = FMIN(U_neg - A_neg, U_star - A_star);` (61). `if (u_pos.H <= cuda::solver_params.DepthThresh)` (65)는 `S_pos = U_neg + C(2.0)*A_neg;` (67), `else` (69)는 `S_pos = FMAX(U_pos + A_pos, U_star + A_star);` (71). 음측 플럭스(negative-side flux)의 전체 초기화는 `FlowVector F_neg = {` (74), `u_neg.HU,` (75), `U_neg * u_neg.HU + C(0.5) * cuda::physical_params.g * u_neg.H * u_neg.H,` (76), `u_neg.HV*U_neg` (77), `};` (78). 양측 플럭스(positive-side flux)는 `FlowVector F_pos = {` (80), `u_pos.HU,` (81), `U_pos * u_pos.HU + C(0.5) * cuda::physical_params.g * u_pos.H * u_pos.H,` (82), `u_pos.HV*U_pos` (83), `};` (84). |
| 86–123 | 시작 시 18행 HLL::x 안. `if (S_neg >= C(0.0))` (86)는 F_neg 반환(88). `else if (S_neg < C(0.0) && S_pos >= C(0.0))` (90)의 연속 식은 `F.H =` (94), `(S_pos*F_neg.H - S_neg*F_pos.H + S_neg*S_pos*(u_pos.H-u_neg.H))` (95), `/` (96), `(S_pos - S_neg);` (97). `F.HU =` (98), `(S_pos*F_neg.HU - S_neg*F_pos.HU + S_neg*S_pos*(u_pos.HU-u_neg.HU))` (99), `/` (100), `(S_pos - S_neg);` (101). `NUMERIC_TYPE S_mid =` (103), `(S_neg*u_pos.H*(U_pos - S_pos) - S_pos*u_neg.H*(U_neg - S_neg))` (104), `/` (105), `(u_pos.H*(U_pos-S_pos) - u_neg.H*(U_neg - S_neg));` (106). `if (S_neg < C(0.0) && S_mid >= C(0.0))` (108)는 `F.HV = F.H * V_neg;` (110), `else` (112)는 `F.HV = F.H * V_pos;` (114). F 반환(117). 바깥 `else` (119)는 F_pos 반환(121). 함수 종료(123). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 24–27·46–47: 두 수심이 모두 DepthThresh 이하이면 조기 반환한다. 그 조건 밖에서는 각 수심의 추가 하한 보정 없이 SQRT(g*H)를 계산한다.
- 94–106: HLL 중간 플럭스와 S_mid 계산의 분모를 0과 비교하는 별도 조건은 없다.
