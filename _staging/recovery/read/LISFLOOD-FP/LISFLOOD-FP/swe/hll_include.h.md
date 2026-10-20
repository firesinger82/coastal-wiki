---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/swe/hll_include.h
lines: 109
sha256: 2833cfc20f6c6b0379c2fb5af560cf07065615739d34f633b8beee2db11ab6d0
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# hll_include.h — 판독 구간 기록

구간은 1행부터 109행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–32 | HLL 리만 해법(Harten–Lax–van Leer Riemann solver)의 포함용 계산 본문이다. 포함 위치는 `swe/hll.cpp` 43행 HLL 함수 안의 60행이다. 두 수심이 모두 DepthThresh 이하이면 세 플럭스를 0으로 설정하고 반환한다. 이후 좌·우 각각 건조 조건이면 속도를 0으로, else면 유량을 수심으로 나누어 계산한다. 파일 자체에 함수 선언·조건부 전처리 분기·include guard는 없다. 원문: `if (H_neg <= DepthThresh && H_pos <= DepthThresh)` (1); `{` (2); `H_flux = C(0.0);` (3); `HU_flux = C(0.0);` (4); `HV_flux = C(0.0);` (5); `return;` (6); `}` (7); `NUMERIC_TYPE U_neg, V_neg;` (9); `if (H_neg <= DepthThresh)` (10); `{` (11); `U_neg = C(0.0);` (12); `V_neg = C(0.0);` (13); `}` (14); `else` (15); `{` (16); `U_neg = HU_neg / H_neg;` (17); `V_neg = HV_neg / H_neg;` (18); `}` (19); `NUMERIC_TYPE U_pos, V_pos;` (21); `if (H_pos <= DepthThresh)` (22); `{` (23); `U_pos = C(0.0);` (24); `V_pos = C(0.0);` (25); `}` (26); `else` (27); `{` (28); `U_pos = HU_pos / H_pos;` (29); `V_pos = HV_pos / H_pos;` (30); `}` (31). |
| 33–60 | 좌·우 중력파 속도(gravity wave speed)와 별 상태(star state)를 계산한다. S_neg·S_pos는 건조측 조건에서 한쪽 물리 상태의 파속을 사용하고, else에서 원래 상태·별 상태의 파속 중 min 또는 max를 선택한다. 두 분기는 서로 독립이다. 원문: `NUMERIC_TYPE A_neg = SQRT(g * H_neg);` (33); `NUMERIC_TYPE A_pos = SQRT(g * H_pos);` (34); `NUMERIC_TYPE H_star = pow(C(0.5)*(A_neg+A_pos) + C(0.25)*(U_neg - U_pos),` (36); `C(2.0))	/ g;` (37); `NUMERIC_TYPE U_star = C(0.5)*(U_neg + U_pos) + A_neg - A_pos;` (38); `NUMERIC_TYPE A_star = SQRT(g*H_star);` (39); `NUMERIC_TYPE S_neg;` (41); `if (H_neg <= DepthThresh)` (42); `{` (43); `S_neg = U_pos - C(2.0)*A_pos;` (44); `}` (45); `else` (46); `{` (47); `S_neg = min(U_neg - A_neg, U_star - A_star);` (48); `}` (49); `NUMERIC_TYPE S_pos;` (51); `if (H_pos <= DepthThresh)` (52); `{` (53); `S_pos = U_neg + C(2.0)*A_neg;` (54); `}` (55); `else` (56); `{` (57); `S_pos = max(U_pos + A_pos, U_star + A_star);` (58); `}` (59). |
| 61–88 | 좌·우의 질량·법선 운동량·접선 운동량 플럭스를 만든다. S_neg가 0 이상이면 왼쪽 플럭스를 복사한다. S_neg가 음수이고 S_pos가 0 이상인 else if에서는 중간 질량·법선 운동량 플럭스를 계산하여 저장한다. 해당 else if는 다음 구간까지 열린다. 원문: `NUMERIC_TYPE H_flux_neg = HU_neg;` (61); `NUMERIC_TYPE HU_flux_neg = U_neg*HU_neg + C(0.5)*g*H_neg*H_neg;` (62); `NUMERIC_TYPE HV_flux_neg = HV_neg*U_neg;` (63); `NUMERIC_TYPE H_flux_pos = HU_pos;` (65); `NUMERIC_TYPE HU_flux_pos = U_pos*HU_pos + C(0.5)*g*H_pos*H_pos;` (66); `NUMERIC_TYPE HV_flux_pos = HV_pos*U_pos;` (67); `if (S_neg >= C(0.0))` (69); `{` (70); `H_flux = H_flux_neg;` (71); `HU_flux = HU_flux_neg;` (72); `HV_flux = HV_flux_neg;` (73); `}` (74); `else if (S_neg < C(0.0) && S_pos >= C(0.0))` (75); `{` (76); `NUMERIC_TYPE H_flux_mid =` (77); `(S_pos*H_flux_neg - S_neg*H_flux_pos + S_neg*S_pos*(H_pos-H_neg))` (78); `/` (79); `(S_pos - S_neg);` (80); `NUMERIC_TYPE HU_flux_mid =` (81); `(S_pos*HU_flux_neg - S_neg*HU_flux_pos + S_neg*S_pos*(HU_pos-HU_neg))` (82); `/` (83); `(S_pos - S_neg);` (84); `H_flux = H_flux_mid;` (86); `HU_flux = HU_flux_mid;` (87). |
| 89–109 | 시작 시 75행 중간 파속 else if 안이다. S_mid를 계산하고 S_neg·S_mid 부호 조건으로 접선 속도의 좌·우 값을 선택하여 HV_flux를 만든다. 103행 else는 69·75행 조건이 모두 성립하지 않는 경우이며 오른쪽 세 플럭스를 복사한다. 마지막 빈 줄도 포함한다. 원문: `NUMERIC_TYPE S_mid =` (89); `(S_neg*H_pos*(U_pos - S_pos) - S_pos*H_neg*(U_neg - S_neg))` (90); `/` (91); `(H_pos*(U_pos-S_pos) - H_neg*(U_neg - S_neg));` (92); `if (S_neg < C(0.0) && S_mid >= C(0.0))` (94); `{` (95); `HV_flux = H_flux_mid * V_neg;` (96); `}` (97); `else` (98); `{` (99); `HV_flux = H_flux_mid * V_pos;` (100); `}` (101); `}` (102); `else` (103); `{` (104); `H_flux = H_flux_pos;` (105); `HU_flux = HU_flux_pos;` (106); `HV_flux = HV_flux_pos;` (107); `}` (108). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 33–34: 한쪽만 건조한 경로에서도 양쪽 `SQRT(g * H_neg)`와 `SQRT(g * H_pos)`를 계산한다. 이 두 식 앞에는 수심의 0 하한 대입이 없다.
- 77–84·89–92: 중간 플럭스는 S_pos−S_neg로 나누고 S_mid는 수심·속도 조합으로 나눈다. 해당 나눗셈 바로 앞에 별도의 영 분모 검사는 없다.
