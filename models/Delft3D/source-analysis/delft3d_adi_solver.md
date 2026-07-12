---
title: "Delft3D-FLOW ADI hydrodynamic solver — adi.f90(2 stage 교번) + SUD(연속+운동량 implicit 결합→수위, double sweep) + UZD(운동량 implicit advection+연직 diffusion, MOMSOL) + cucnp/taubot/difu"
topic: delft3d
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute/ 직접 read — adi.f90(ADI 1 step, stage1/2 SUD+UZD 282-326) + sud.f90(implicitly coupled momentum+continuity) + uzd.f90(implicit advection+vertical diffusion, MOMSOL options) + cucnp/taubot/difu file:line 인용. Delft3D-FLOW structured."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — ADI 2-stage·SUD·UZD verbatim"
verification_date: 2026-06-03
related:
  - models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher.md
  - models/Delft3D/source-analysis/delft3d_turbulence.md
  - models/Delft3D/source-analysis/delft3d_sigma_z.md
  - models/Delft3D/source-analysis/delft3d_drying_flooding.md
---

# Delft3D-FLOW ADI hydrodynamic solver

> `flow2d3d_kernel/src/compute/` 직접 read. **Delft3D-FLOW(structured curvilinear)의 핵심 수리 solver** — Alternating Direction Implicit(ADI, Leendertse) 로 운동량+연속방정식을 푼다. [[delft3d_flow2d3d_dispatcher]] 가 호출하는 compute kernel. D-Flow FM(unstructured)와 별개의 구조격자 엔진.

## 1. ADI method — adi.f90 (2 stage 교번) ★

한 time step 을 **2 half-step(stage)** 으로 분할, 방향을 번갈아 implicit:
```fortran
! adi.f90: ADI performs one time step of Alternating Direction Implicit
stage1: CALL SUD(...)  → CALL UZD(...)      ! 첫 half-step (한 방향 implicit)
stage2: (방향 swap, SUD+UZD)                ! 둘째 half-step
```
- **stage1**: ξ(u) 방향 운동량+연속 implicit + η(v) 방향 explicit → SUD 가 수위·u 갱신, UZD 가 v 갱신.
- **stage2**: 방향 교환(η implicit) — 매 step 두 방향을 대칭 처리(2차 정확도, 무조건 안정).
- `hv`(v-point 수심)는 SUD 에서 wet point(kfv=1) 계산(:285). `dischy`/`solver`/`icreep` 옵션.
- **advection explicit 성분의 정량 CFL(2026-07-12 보강)**: `chkadv.f90` 이 TRISOL 에서 **반스텝마다 U-점·V-점 각각**(총 4회/step, trisol.f90:2245,2255; Z-모델 z_trisol:3331,3341 z_chkadv) advection Courant 를 점검 — `CFL = hdt·|u0|/gvu`(U, chkadv.f90:157) / `hdt·|v̄|/guu`(V-4점 평균, :162-167), 정의는 헤더 명시 "following definitions G.S. Stelling, 1984"(:35-37). **CFL>1 이면 G051 경고 + 권장 dt = 2·Δx/|u|max 출력(:192-199)이고 하드 스톱은 아님** — ADI 파속(barotropic)은 무조건 안정이나 explicit advection 은 Courant≤1 이 정확도·안정 권고라는 이원 구조가 소스로 확정.

## 2. SUD — implicit 연속+운동량 결합 (sud.f90) ★

> "SUD evaluates/solves the **implicitly coupled momentum and continuity equation**"
- 해당 방향의 운동량(barotropic) 과 연속방정식을 **동시 implicit** 으로 풀어 **수위(ζ=s1)** 산출. continuity 의 flux divergence + 운동량의 pressure gradient `g·∂ζ` 를 결합 → tridiagonal(double-sweep) 또는 conjugate-gradient solver(`solver`).
- water-level-continuity coupling 이 ADI 의 핵심(반-implicit barotropic → 큰 dt 안정). drying/flooding mask(kfu/kfv, [[delft3d_drying_flooding]]) 반영.

## 3. UZD — 운동량 implicit advection+diffusion (uzd.f90)

> "step the momentum equation with **implicit advection** approximation, and **implicit diffusion in the vertical**"
- cross-direction 운동량: horizontal advection(`MOMSOL` 옵션 — implicit central WAQUA scheme 등) + **연직 diffusion implicit**(vertical mixing [[delft3d_turbulence]] AV) + Coriolis + viscosity.
- MOMSOL: 운동량 이송 스킴 선택(implicit central / 기타). 연직 implicit → 얕은층 안정.

## 4. 보조 kernel

- **cucnp.f90**: 운동량 방정식 계수(coefficient) 조립(advection·Coriolis·viscosity matrix 항).
- **taubot.f90**: bed shear stress(bottom friction, Chézy/Manning/White-Colebrook) → 운동량 bottom drag.
- **difu.f90**: **transport(advection-diffusion)** — 염분·온도·sediment·tracer 의 수송(ADI 와 같은 방향 분할). [[delft3d_sediment]]·[[delft3d_heat]] 가 사용.

## 5. 위치 — structured vs unstructured

| 엔진 | solver |
|---|---|
| **Delft3D-FLOW**(flow2d3d, structured curvilinear) | **본 노트 ADI**(adi/sud/uzd) |
| **D-Flow FM**(dflowfm, unstructured) | implicit FV solver([[delft3d_dflowfm_overview]]) |

→ ADI 는 구조격자 전용(σ/Z-layer [[delft3d_sigma_z]]). 비정형은 dflowfm.

## 6. 연결

- [[delft3d_flow2d3d_dispatcher]] — adi/sud/uzd 호출 dispatcher
- [[delft3d_turbulence]] — UZD 연직 diffusion AV(eddy viscosity)
- [[delft3d_sigma_z]] — σ/Z layer 연직격자(ADI 가 푸는 격자)
- [[delft3d_drying_flooding]] — kfu/kfv wet/dry mask
- [[sediment/delft3d_sediment]] / [[delft3d_heat]] — difu transport
- Leendertse / Stelling ADI (Delft3D-FLOW 수치)
