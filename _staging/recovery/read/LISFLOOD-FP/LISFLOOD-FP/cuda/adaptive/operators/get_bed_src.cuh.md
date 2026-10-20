---
file: models/LISFLOOD-FP/raw/source_code/LISFLOOD-FP/cuda/adaptive/operators/get_bed_src.cuh
lines: 99
sha256: 0a550dd3a9962e639282424eb382cb2c3b8bf363221ead8e92fd2fd76e423d4a
reader: codex gpt-6.1-sol
read_date: 2026-10-20
---

# get_bed_src.cuh — 판독 구간 기록

구간은 1행부터 99행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|

| 1–26 | `#pragma once`와 CUDA 런타임·흐름 계수(FlowCoeffs) 헤더를 포함한다(1–5). CUDA 장치 함수(device function) `get_bed_src_x`의 실수 반환 오버로드(overload)이다(7–20). 서·동 중간 지형·재구성 수심·수면고·중력·지역 x간격·idx를 받는다(10–18). 지형을 수면고로 보정하고 평균 재구성 수심과 지형 차를 사용한 하상 생성항(bed source term)을 반환한다(21–25). 전처리 조건 분기는 없다. 원문: `#pragma once` (1); `__device__ __forceinline__` (7); `real z_star_w = z_w_intermediate - max( C(0.0), -(eta_w_pos - z_w_intermediate) );`<br>`real z_star_e = z_e_intermediate - max( C(0.0), -(eta_e_neg - z_e_intermediate) );` (21–22); `return g * C(0.5) * (h_star_w_pos + h_star_e_neg) * (z_star_e - z_star_w) / dx_loc;` (24). |
| 27–45 | CUDA 장치 함수 `get_bed_src_y`의 실수 반환 오버로드이다(27–39). 남·북 중간 지형·재구성 수심·수면고·중력·지역 y간격을 받는다(30–37). 보정 지형과 y방향 하상 생성항을 계산하여 반환한다(40–44). 원문: `__device__ __forceinline__` (27); `real z_star_s = z_s_intermediate - max( C(0.0), -(eta_s_pos - z_s_intermediate) );`<br>`real z_star_n = z_n_intermediate - max( C(0.0), -(eta_n_neg - z_n_intermediate) );` (40–41); `return g * C(0.5) * (h_star_s_pos + h_star_n_neg) * (z_star_n - z_star_s) / dy_loc;` (43). |
| 46–73 | CUDA 장치 함수 `get_bed_src_x`의 흐름 계수 반환 오버로드이다(46–60). 수면고·중간 지형·수심 평균 및 x모드·중력·지역 x간격·coeffs·idx를 받는다(49–58). 보정 지형과 지형 x모드(mode)를 계산한다(61–64). 결과 계수를 빈 초기화한 뒤 x운동량의 평균·x모드 생성항을 채워 반환한다(66–72). 원문: `__device__ __forceinline__` (46); `real z_star_e = z_inter_e - max( C(0.0), -(eta_e_neg - z_inter_e) );`<br>`real z_star_w = z_inter_w - max( C(0.0), -(eta_w_pos - z_inter_w) );`<br>`real z1x_star = (z_star_e - z_star_w) / (C(2.0) * sqrt(C(3.0)));` (61–64); `Sbx.qx._0  = -C(2.0) * sqrt(C(3.0)) * g * h0x_star * z1x_star / dx_loc;`<br>`Sbx.qx._1x = -C(2.0) * sqrt(C(3.0)) * g * h1x_star * z1x_star / dx_loc;` (68–69). |
| 74–99 | CUDA 장치 함수 `get_bed_src_y`의 흐름 계수 반환 오버로드이다(74–87). 수면고·중간 지형·수심 평균 및 y모드·중력·지역 y간격·coeffs를 받는다(77–85). 보정 지형과 지형 y모드를 계산한다(88–91). 결과 계수를 빈 초기화한 뒤 y운동량의 평균·y모드 생성항을 채워 반환한다(93–99). 원문: `__device__ __forceinline__` (74); `real z_star_n = z_inter_n - max( C(0.0), -(eta_n_neg - z_inter_n) );`<br>`real z_star_s = z_inter_s - max( C(0.0), -(eta_s_pos - z_inter_s) );`<br>`real z1y_star = (z_star_n - z_star_s) / ( C(2.0) * sqrt( C(3.0) ) );` (88–91); `Sby.qy._0  = -C(2.0) * sqrt( C(3.0) ) * g * h0y_star * z1y_star / dy_loc;`<br>`Sby.qy._1y = -C(2.0) * sqrt( C(3.0) ) * g * h1y_star * z1y_star / dy_loc;` (95–96). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·58: 두 x방향 오버로드가 받는 `idx`는 각 함수 본문에서 참조하지 않는다.
- 57·85: 흐름 계수를 반환하는 두 오버로드가 받는 `coeffs`는 각 함수 본문에서 참조하지 않는다.
- 24·43 및 68–69·95–96: 실수 반환식은 양의 부호로 시작한다. 흐름 계수 반환식은 음의 부호로 시작한다.
