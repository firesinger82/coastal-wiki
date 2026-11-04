---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass3_NLSW_Spherical_wgsl.md
lines: 35
sha256: e1a1c07a4406bb13403d05b810c97e68c6392d2044ee52954a55135543da685d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass3_NLSW_Spherical_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass3_NLSW_Spherical.wgsl`

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 원문 링크·설명이다(1–3). 조건 `grid_type == 2`의 NLSW 적분으로 `Pass3_NLSW.wgsl` 계약을 유지하며 `dx`·`dy`는 경도·위도 도 간격이다(1–7). 바인딩 `19`는 `txDissipationFlux` 대신 `txSphericalMetrics`다. `r/g/b/a`는 `1 / (R * cos(phi_center))`, `cos(phi_north_face)`, `cos(phi_south_face)`, `tan(phi_center) / R`다(11–16). `main.js`는 `1 / R`을 Pass3 uniform 끝에 쓴다(18). `lat_LL`은 좌하단 모서리로 중심 `lat_LL + (j + 0.5) * dy`, 면 `lat_LL + j * dy`·`lat_LL + (j + 1) * dy`다(20). 공유 계약은 state·flux·history·output이다(7). uniform 끝의 `1 / R`은 위도 방향 압력 경사 항용이다(18). [11-04 전수 검증 보완] |
| 22–35 | 유량 발산은 `1 / (R cos(phi)) * [dF/dlambda + d(cos(phi) G)/dphi]` (26)이다. P 발생항은 `-gH / (R cos(phi)) * eta_lambda + (PQ / H) * tan(phi) / R` (30), Q 발생항은 `-gH / R * eta_phi - (P^2 / H) * tan(phi) / R` (31)다. 범위는 NLSW뿐이며 JavaScript가 표준 `second-order` 재구성·Boussinesq/COULWAVE 비활성·퇴적물 비활성·Cartesian 쇄파 비활성을 강제한다(35). 운동량 source term은 구면 압력 경사와 곡률 항을 더한다(28). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
