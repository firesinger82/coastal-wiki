---
title: "XBeach non-hydrostatic mode (nonh.F90) — wave-resolving 동압력 보정: projection(5-diagonal Poisson → solver_solvemat) + 1-layer/reduced 2-layer(Keller-box) + predictor-corrector → ph 압력 → flow"
topic: xbeach
canonical_source: self
citation_status: verified
verification_method: "models/XBeach/raw/source_code/trunk/src/xbeachlibrary/nonh.F90 (3471) 직접 read — nonh_cor(146 entry, 2회/step), nonhq3d 분기(1-layer nonh_1lay_pred/cor vs reduced 2-layer nonh_2lay_pred/cor_2dV/3d, 174-249), 5-diagonal pressure matrix mat+rhs+dp, solver_solvemat(686/1412/2164) file:line 인용. Pieter Bart Smit 2009/2014."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — projection 압력보정·2-layer·predictor-corrector verbatim"
verification_date: 2026-06-03
related:
  - models/XBeach/source-analysis/xbeach_flow_solver.md
  - models/XBeach/source-analysis/xbeach_mode_dispatch.md
  - models/XBeach/source-analysis/xbeach_wave_action_balance.md
---

# XBeach non-hydrostatic mode (nonh.F90) — XBeach-NH

> `nonh.F90`(3471, Pieter Bart Smit 2009/2014) 직접 read. XBeach 의 **wave-resolving 비정수압 모드**(`wavemodel=nonhydrostatic`). 파작용 평형([[xbeach_wave_action_balance]])으로 wave-averaged 하는 surfbeat 와 달리, **개별 단주기파를 직접 해상**(Boussinesq류 frequency dispersion). NLSWE 흐름([[xbeach_flow_solver]])에 **동압력(dynamic pressure) `ph`** 를 더해 비정수압 효과 포함. MPI 시 미포함(`#ifdef CMPI` 제외, :42).

## 1. 역할 — projection method (pressure correction)

비정수압 = 정수압(`g·∂zs`)만으로 부족한 **수직가속도(분산)** 를 동압력으로 보정. **projection(예측-보정)**:
1. flow 가 동압력 무시하고 예측 유속 산출(`uu0`).
2. 연속방정식(divergence-free) 만족하도록 **동압력 `dp` 의 Poisson 방정식** 구성·해.
3. `dp` 경사로 u,v,w 보정 → `ph` 누적 → [[xbeach_flow_solver]] §1 의 `g·∂(zs+ph)/∂x` 운동량 항.

## 2. nonh_cor — 진입 (nonh.F90:146-249) ★

flow 모듈이 **timestep 당 2회** 호출(`ipredcor`):
```fortran
select case(par%nonhq3d)
  case(.true.)   ! 새 reduced 2-layer
     predictor: nonh_2lay_pred_2dV(2DV) / nonh_2lay_pred_3d(3D)
     corrector: nonh_2lay_cor_2dV     / nonh_2lay_cor_3d
  case(.false.)  ! old 1-layer
     predictor: nonh_1lay_pred ; corrector: nonh_1lay_cor
```
- **predictor**(path=0): 알려진 압력으로 explicit 예측. **corrector**(path=1): 새 압력 implicit 보정.
- **2DV**(cross-shore 수직단면) vs **3D** 코드패스.

## 3. 두 vertical 정식 (nonhq3d)

| nonhq3d | 정식 | dispersion |
|---|---|---|
| `.false.` | **old 1-layer** (Draft report) — 단층 depth-averaged + 동압력 (Keller-box 표면) | kh ≲ 일정 한계 |
| `.true.` | **reduced 2-layer**(Smit 2014) — 연직 2층(`wcoef`=하층 상대두께) | 더 깊은 상대수심까지 정확(kh↑) |

- **Keller-box** compact scheme(표면 추적) — 적은 층수로 정확한 선형 분산(Boussinesq 대안). 2-layer 는 1-layer 보다 deep-water dispersion 개선(외해 경계 더 깊이 배치 가능).
- `wcoef` = reduced 2-layer 하층 상대두께(분산 최적화 파라미터).

## 4. Pressure Poisson 풀이 (5-diagonal matrix)

```fortran
! mat(5-diagonal) · dp = rhs   →
call solver_solvemat( mat, rhs, dp, s%nx, s%ny, par )    ! :686/1412/2164
```
- **`mat`** = 5-diagonal 압력행렬(중앙+동서남북 이웃 계수, 압력계수 `au/av/adu/adv` 로 조립). **`rhs`** = 예측 유속의 divergence(연속 위배량). **`dp`** = 동압력 보정.
- `solver_solvemat`(solver_module) — elliptic 선형solver(SIP/iterative). dp 로 u/v/w 보정해 divergence-free.
- `aws/awb` = 수직속도 ws(surface)/wb(bottom) 압력계수(old model; 2-layer 는 obsolete).

## 5. surfbeat vs nonh 비교

| | surfbeat | nonh |
|---|---|---|
| 단주기파 | wave-averaged(파작용 N=E/σ) | **직접 해상**(phase-resolving) |
| 분산 | wave model dispersion | **동압력 Keller-box**(1/2-layer) |
| infragravity | bound long wave(파군 변조) | 직접 해상 |
| 압력 | hydrostatic(ph=0) | **+동압력 ph** |
| 비용 | 저렴(파작용) | 비쌈(파 해상 + Poisson solve) |
| 용도 | dissipative beach·storm | reef·steep·runup·harbor(분산 중요) |

→ [[xbeach_flow_solver]] §6 의 모드 분기에서 nonh 가 `ph`≠0 + `Fx` 없음(파 직접) 경로.

## 6. 연결

- [[xbeach_flow_solver]] — 동압력 `ph` → `g·∂(zs+ph)` 운동량(§1) + W advection 2nd-order(flow_secondorder_advW)
- [[xbeach_mode_dispatch]] — surfbeat/stationary/nonh 모드 선택(`wavemodel`)
- [[xbeach_wave_action_balance]] — surfbeat 대안(nonh 는 미사용)
- solver_module `solver_solvemat` — 압력 Poisson elliptic solver
- Smit, Stelling, Roelvink et al. 2010/2014 (XBeach-NH non-hydrostatic) / Keller-box scheme
