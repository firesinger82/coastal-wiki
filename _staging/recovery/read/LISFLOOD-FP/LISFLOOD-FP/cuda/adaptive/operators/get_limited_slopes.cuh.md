---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_limited_slopes.cuh
lines: 78
sha256: 49f9c5be68af317281aa4b645f42cbbf15ad4c440f4f2b50715342e18e081a8b
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_limited_slopes.cuh — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–26 | `#pragma once`와 경사(Slopes)·평면 계수(PlanarCoefficients)·해석기 매개변수·DG2 면 값 평가·minmod 헤더를 포함한다(1–8). CUDA 장치 함수(device function) `get_limited_slopes`는 중심·네 이웃 계수와 이웃 면의 Legendre 기저(Legendre basis), 최세 간격, 허용값 tol_Krivo를 받는다(10–26). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (10). |
| 27–53 | 시작 시 10–26행 `get_limited_slopes` 안. STEP 3b 주석 뒤 `eval_loc_face_val_dg2`로 이웃측 면 값 네 개를 계산한다(27–33). 중심측 면 값은 상수·방향별 ±sqrt(3) 기저로 평가한다(35–38). STEP 3c에서 양쪽 면 값의 차의 절댓값을 계산한다(40–46). STEP 4에서 평균과 각 모드(mode)의 합·차로 방향별 노름(norm)을 구한다(48–52). 원문: `const real u_n_pos = eval_loc_face_val_dg2(u_n, basis_n);`<br>`const real u_e_pos = eval_loc_face_val_dg2(u_e, basis_e);`<br>`const real u_s_neg = eval_loc_face_val_dg2(u_s, basis_s);`<br>`const real u_w_neg = eval_loc_face_val_dg2(u_w, basis_w);` (30–33); `const real u_n_neg = eval_loc_face_val_dg2(u, { C(1.0), C(0.0), sqrt( C(3.0) ) } );`<br>`const real u_e_neg = eval_loc_face_val_dg2(u, { C(1.0), sqrt( C(3.0) ), C(0.0) } );`<br>`const real u_s_pos = eval_loc_face_val_dg2(u, { C(1.0), C(0.0), -sqrt( C(3.0) ) });`<br>`const real u_w_pos = eval_loc_face_val_dg2(u, { C(1.0), -sqrt( C(3.0) ), C(0.0) });` (35–38); `const real jump_n = abs(u_n_pos - u_n_neg);`<br>`const real jump_e = abs(u_e_pos - u_e_neg);`<br>`const real jump_s = abs(u_s_pos - u_s_neg);`<br>`const real jump_w = abs(u_w_pos - u_w_neg);` (43–46); `const real norm_x = max( abs(u._0 - u._1x), abs(u._0 + u._1x) );`<br>`const real norm_y = max( abs(u._0 - u._1y), abs(u._0 + u._1y) );` (51–52). |
| 54–78 | 시작 시 10–26행 `get_limited_slopes` 안. STEP 5에서 노름이 `C(1e-12)`보다 클 때 면 점프(jump)를 반 최세 간격과 노름으로 나누고, 그 외에는 0으로 둔다(54–61). 방향별 점프 척도 최댓값이 tol_Krivo보다 작으면 원래 모드를 유지한다. 그 외에는 원래 모드와 양옆 평균 차에 `minmod`를 호출한다(63–75). 제한된 두 경사를 반환하고 함수를 닫는다(77–78). 원문: `const real DS_e = ( norm_x > C(1e-12) ) ? jump_e / (C(0.5) * dx_finest * norm_x) : C(0.0);`<br>`const real DS_w = ( norm_x > C(1e-12) ) ? jump_w / (C(0.5) * dx_finest * norm_x) : C(0.0);` (57–58); `const real DS_n = ( norm_y > C(1e-12) ) ? jump_n / (C(0.5) * dy_finest * norm_y) : C(0.0);`<br>`const real DS_s = ( norm_y > C(1e-12) ) ? jump_s / (C(0.5) * dy_finest * norm_y) : C(0.0);` (60–61); `const real u1x_limited = (max(DS_e, DS_w) < tol_Krivo) ? u._1x : minmod`<br>`(`<br>`u._1x,`<br>`(u._0 - u_w._0),`<br>`(u_e._0 - u._0)`<br>`);` (63–68); `const real u1y_limited = (max(DS_n, DS_s) < tol_Krivo) ? u._1y : minmod`<br>`(`<br>`u._1y,`<br>`(u._0 - u_s._0),`<br>`(u_n._0 - u._0)`<br>`);` (70–75). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–61: 방향별 점프 척도의 길이 인자는 `dx_finest`와 `dy_finest`이다. 이 함수에는 지역 레벨에 따른 길이 재조정 식이 없다.
- 57–75: 노름의 하한 판단은 `C(1e-12)`로 고정되어 있다. 제한기 적용 여부는 별도 인수 `tol_Krivo`와 비교한다.
