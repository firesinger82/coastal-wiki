---
title: "XBeach wave 수치 toolkit(wave_functions.F90) — dispersion(Newton) + advection scheme(advecxho/yho/thetaho upwind/higher-order) + compute_wave_direction_velocities(cgx/cgy/ctheta) + compute_wave_forces(Fx/Fy radiation stress) + Stokes drift + breakerdelay"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/wave_functions.F90 (1360) 직접 read — public: dispersion/iteratedispersion/slope2D/breakerdelay/advecxho·yho·thetaho/advecqx·qy/advecwx·wy/compute_wave_direction_velocities/compute_stokes_drift/compute_wave_forces/update_means_wave_flow. advection upwind cgxu>0 분기(157-199) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 파 수치 kernel verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_nonh.md
---

# XBeach wave 수치 toolkit (wave_functions.F90)

> `wave_functions.F90`(1360) 직접 read. [[xbeach_wave_action_balance]]·wave_directions·wave_stationary 가 공유하는 **파 수치 kernel 모음**(module `wave_functions_module`). 분산관계·advection 스킴·group/refraction 속도·**radiation stress force**·Stokes drift.

## 1. Dispersion (dispersion / iteratedispersion / wave_dispersion)

선형 분산관계 `σ² = g·k·tanh(k·h)` 에서 **파수 k 를 Newton 반복**으로 해(ω·h 주어짐). `iteratedispersion` = 흐름(Doppler) 포함 반복. 파장 L=2π/k, 위상속도 c=σ/k, group velocity cg = c·(½ + kh/sinh(2kh)).

## 2. Advection 스킴 (advecxho / advecyho / advecthetaho) ★

파작용/roller 를 x·y·θ 공간에서 전파(flux form). `scheme`(par%scheme) 선택:
```fortran
cgxu = 0.5*(cgx(i+1)+cgx(i))               ! face group velocity
if (cgxu>0) fluxx = ee(i)*cgxu*dnu          ! upwind: 상류 셀
else        fluxx = ee(i+1)*cgxu*dnu
! higher-order(2차): eupw = ee + slope-limited 보정
```
- **upwind**(1차, 안정·확산) / **higher-order**(2차 Lax-Wendroff류, eupw slope 보정). `advecthetaho` = θ-space refraction advection.
- `advecqx/qy` = roller flux(Qb), `advecwx/wy` = 기타. stationary solver 는 nx=3 작은 stencil 호출.

## 3. compute_wave_direction_velocities (cgx/cgy/ctheta)

파작용 advection 속도 산출: `cgx = cg·cos θ + u`(group + 흐름), `cgy = cg·sin θ + v`, **`ctheta`**(refraction 속도, θ-space) = 수심·흐름 경사로부터(Snell). wci(wave-current) 시 Doppler 포함.

## 4. compute_wave_forces (Fx / Fy) ★

radiation stress tensor → **wave force**(흐름 구동): `Sxx/Sxy/Syy`(파+roller 에너지 ee+rr, n=cg/c) 의 공간경사 → `Fx = −∂Sxx/∂x − ∂Sxy/∂y`, `Fy = ...`. [[xbeach_flow_solver]] §1 의 `lwave·Fx` 항 공급원. surfbeat 의 wave→current.

## 5. 기타 kernel

- **compute_stokes_drift**: Stokes 표류속도(파 질량수송) → GLM 흐름 보정([[xbeach_flow_solver]] ue=u+us).
- **breakerdelay**: 쇄파 roller 의 공간 지연(Qb advection, surfzone 안쪽 운동량 전달).
- **slope2D**: 2D 경사(dhdx/dhdy) 계산(wete mask). **update_means_wave_flow**: wave-averaged 평균량 갱신.

## 6. 연결

- [[xbeach_wave_action_balance]] — advecxho/yho/thetaho·dispersion·cgx/cgy/ctheta·compute_wave_forces 호출
- [[xbeach_flow_solver]] — Fx/Fy(compute_wave_forces)·Stokes drift(GLM)
- [[xbeach_nonh]] — advecwx/wy(W advection)
- Holthuijsen action balance / Longuet-Higgins-Stewart(radiation stress)
