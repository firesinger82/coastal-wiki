---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/limit_slopes.cu
lines: 238
sha256: d5191e6caedae2ab90dd1a18c3ebcc43dfecfbfdb9ddd22891a4814bf5336736
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# limit_slopes.cu — 판독 구간 기록

구간은 1행부터 238행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–34 | 헤더 포함과 CUDA 커널(kernel) `limit_slopes` 정의이다(1–14). 해·이웃·모의/해석기 매개변수·최세 간격·최대 수심을 받는다(6–12). 인덱스 범위와 최세 레벨 조건을 확인한다(16–24). 지역 간격·계층 인덱스(hierarchy index)·중심 좌표를 계산하고 x 또는 y가 해당 상한 이상이면 반환한다(25–33). 전처리 조건 분기는 없다. 원문: `__global__` (3); `int idx   = blockIdx.x * blockDim.x + t_idx;` (17); `if (idx < d_assem_sol.length)` (19); `if (level == solver_params.L)` (23); `real dx_loc = dx_finest * ( 1 << (solver_params.L - level) );`<br>`real dy_loc = dy_finest * ( 1 << (solver_params.L - level) );` (25–26); `real x = get_x_coord(h_idx, level, solver_params.L, dx_finest);`<br>`real y = get_y_coord(h_idx, level, solver_params.L, dy_finest);` (30–31); `if ((x >= sim_params.xsz * dx_finest) \|\| (y >= sim_params.ysz * dy_finest)) return;` (33). |
| 35–94 | 시작 시 3–14행 커널·19행 유효 인덱스 분기·23행 최세 레벨 분기 안. STEP 2 주석과 중심·북·동 이웃의 흐름 계수(FlowCoeffs) 조립이다(35–93). 각각 수심·x유량·y유량의 평균과 x/y 모드(mode)를 해당 배열에서 읽는다(38–55·57–74·76–93). |
| 95–160 | 시작 시 3–14행 커널·19행 유효 인덱스 분기·23행 최세 레벨 분기 안. 남·서 이웃 흐름 계수를 조립한다(95–131). 중심과 네 이웃 지형의 평면 계수(PlanarCoefficients)를 읽는다(133–137). 지형과 수심 계수를 더해 수면고 계수를 구성한다(139–143). 이웃 레벨·인덱스를 읽고 면별 단위 좌표 주석과 STEP 3a 머리 주석을 포함한다(145–160). 원문: `const PlanarCoefficients eta   = z   + coeffs.h;`<br>`const PlanarCoefficients eta_n = z_n + coeffs_n.h;`<br>`const PlanarCoefficients eta_e = z_e + coeffs_e.h;`<br>`const PlanarCoefficients eta_s = z_s + coeffs_s.h;`<br>`const PlanarCoefficients eta_w = z_w + coeffs_w.h;` (139–143). |
| 161–215 | 시작 시 3–14행 커널·19행 유효 인덱스 분기·23행 최세 레벨 분기 안. `get_leg_basis`로 네 이웃 면의 Legendre 기저(Legendre basis)를 계산한다(163–166). 수면고·x유량·y유량 각각에 `get_limited_slopes`를 호출한다(168–182·184–198·200–214). 중심·네 이웃 계수, 네 면 기저, 최세 간격, `solver_params.tol_Krivo`를 전달한다. 원문: `LegendreBasis basis_n = get_leg_basis(h_idx, h_idx_n, level_n, solver_params.L, x, y, dx_loc, dy_loc, dx_finest, dy_finest, NORTH);`<br>`LegendreBasis basis_e = get_leg_basis(h_idx, h_idx_e, level_e, solver_params.L, x, y, dx_loc, dy_loc, dx_finest, dy_finest, EAST);`<br>`LegendreBasis basis_s = get_leg_basis(h_idx, h_idx_s, level_s, solver_params.L, x, y, dx_loc, dy_loc, dx_finest, dy_finest, SOUTH);`<br>`LegendreBasis basis_w = get_leg_basis(h_idx, h_idx_w, level_w, solver_params.L, x, y, dx_loc, dy_loc, dx_finest, dy_finest, WEST);` (163–166); `Slopes eta_limited = get_limited_slopes`<br>`(`<br>`eta,`<br>`eta_n,`<br>`eta_e,`<br>`eta_s,`<br>`eta_w,`<br>`basis_n,`<br>`basis_e,`<br>`basis_s,`<br>`basis_w,`<br>`dx_finest,`<br>`dy_finest,`<br>`solver_params.tol_Krivo`<br>`);` (168–182); `Slopes qx_limited = get_limited_slopes`<br>`(`<br>`coeffs.qx,`<br>`coeffs_n.qx,`<br>`coeffs_e.qx,`<br>`coeffs_s.qx,`<br>`coeffs_w.qx,`<br>`basis_n,`<br>`basis_e,`<br>`basis_s,`<br>`basis_w,`<br>`dx_finest,`<br>`dy_finest,`<br>`solver_params.tol_Krivo`<br>`);` (184–198); `Slopes qy_limited = get_limited_slopes`<br>`(`<br>`coeffs.qy,`<br>`coeffs_n.qy,`<br>`coeffs_e.qy,`<br>`coeffs_s.qy,`<br>`coeffs_w.qy,`<br>`basis_n,`<br>`basis_e,`<br>`basis_s,`<br>`basis_w,`<br>`dx_finest,`<br>`dy_finest,`<br>`solver_params.tol_Krivo`<br>`);` (200–214). |
| 216–238 | 시작 시 3–14행 커널·19행 유효 인덱스 분기·23행 최세 레벨 분기 안. 방향별 중심·양쪽 이웃 수심 최솟값이 최대 수심의 0.05배를 초과하는지 계산한다(216–217). 저장할 모드들을 참조로 연결한다(219–226). 조건 참이면 수면고 제한 모드에서 지형 모드를 뺀 수심 모드와 제한 유량 모드를 저장하고, 거짓이면 기존 모드를 유지한다(228–235). 두 조건과 커널을 닫는다(236–238). 원문: `const bool above_h_min_limiter_x = ( C(0.05) * max_h < min( coeffs.h._0, min(coeffs_e.h._0, coeffs_w.h._0) ) );`<br>`const bool above_h_min_limiter_y = ( C(0.05) * max_h < min( coeffs.h._0, min(coeffs_n.h._0, coeffs_s.h._0) ) );` (216–217); `h1x = (above_h_min_limiter_x) ? eta_limited._1x - z._1x : h1x;`<br>`h1y = (above_h_min_limiter_y) ? eta_limited._1y - z._1y : h1y;` (228–229); `qx1x = (above_h_min_limiter_x) ? qx_limited._1x : qx1x;`<br>`qx1y = (above_h_min_limiter_y) ? qx_limited._1y : qx1y;` (231–232); `qy1x = (above_h_min_limiter_x) ? qy_limited._1x : qy1x;`<br>`qy1y = (above_h_min_limiter_y) ? qy_limited._1y : qy1y;` (234–235). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·216–235: 모드 갱신은 최세 레벨 조건 안에서만 실행한다. 각 방향의 수심 하한 조건이 거짓이면 해당 방향의 기존 수심·유량 모드를 유지한다.
- 216–217: 제한기(limiter) 적용 수심의 계수 `C(0.05)`는 두 방향 모두 코드에 고정되어 있다.
