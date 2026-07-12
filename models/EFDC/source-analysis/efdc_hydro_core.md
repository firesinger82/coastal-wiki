---
title: "efdc hydro core"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_hydro_core.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How EFDC+ assembles momentum and continuity, splits external (depth-integrated 2D) from internal (3D shear) modes, switches between 3-time-level (leapfrog + trapezoidal corrector) and 2-time-level paths, applies buoyancy / non-hydrostatic / boundary forcing, and where the depth/free-surface update happens. Use this when debugging mass conservation, switching between IS2TIM modes, or wiring a non-hydrostatic case.

## Source basis

- `aaefdc.f90:3187-3188` — top-level dispatch: `IS2TIM==0 → HDMT` (3TL), `IS2TIM>=1 → HDMT2T` (2TL).
- `calexp.f90`, `calexp2t.f90` — external (depth-integrated) momentum.
- `calpuv9c.f90`, `calpuv2c.f90` — external continuity solver (preconditioned conjugate gradient).
- `caluvw.f90` — internal (3D) momentum, vertical velocity W, barotropic correction.
- `calbuoy.f90`, `calebi.f90` — density and external buoyancy integral.
- `calpnhs.f90` — quasi-non-hydrostatic pressure.
- `setopenbc.f90`, `calpser.f90` — open BC and PSER tide series.

## A. External momentum (CALEXP / CALEXP2T)

- Advection fluxes `FUHU/FVHU/FUHV/FVHV` built per layer, upwind or central (`calexp.f90:218-227`); flux divergence assembled into `FX/FY` (`:685-686`). 2TL mirror in `calexp2t.f90:214-218`.
- Coriolis + curvature: `CAC = FCORC + metric + HP` (`calexp.f90:571`); `FCAX/FCAY` (`:620-621`).
- Vertical sums to depth-integrated `FCAXE/FCAYE`, `FXE/FYE` (`calexp.f90:1133-1136`; `calexp2t.f90:1053-1056`).
- Wind / bottom / pressure enter in **CALPUV**, not CALEXP: `FUHDYE/FVHDXE = old_flow − pressure_grad + DELT*(wind − bottom + Coriolis + buoyancy − advection)` at `calpuv9c.f90:256-257` (3TL), `calpuv2c.f90:224-226` (2TL).
- Horizontal momentum diffusion (`FMDUX/FMDUY/FMDVY/FMDVX`)은 `CALHDMF`(2TL) 또는 `CALHDMF3`(3TL) 에서 계산되어 CALEXP의 viscous flux divergence 항으로 합산 — 상세는 [[efdc_dispersion]] (Smagorinsky + AHO).
- Implicit bottom/vegetation drag coefficients `RCX/RCY` at `calpuv9c.f90:269-270`, applied at `:287-288`.

## B. External continuity (CALPUV9C / CALPUV2C)

- **Solver**: preconditioned conjugate gradient (`calpuv9c.f90:693-707`; 2TL `calpuv2c.f90:656-664`).
- Linear system: RHS `FP` at `calpuv9c.f90:609`; coefficients `CC/CS/CW/CE/CN` at `:623-631`.
- Free-surface / depth update:
  - 3TL: `HP = H2P + DELT * DXYIP * (QSUME − 0.5*div(UHDYE+UHDY2E, VHDXE+VHDX2E))` (`calpuv9c.f90:771-772`).
  - 2TL: `HP = H1P + DELTD2 * DXYIP * (2*QSUME − div(new+old flows))` (`calpuv2c.f90:733-734`).

The PCG operates on **pressure head** `P`, not directly on `HP`. After solve, `HP = GI*P − BELV` is recovered (`calpuv9c.f90:804-807`).

## C. Internal (3D) mode coupling (CALUVW)

전단(DU/DV) 연직 **완전 implicit tridiagonal + Sherman-Morrison** solve 자체는 → **[[efdc_internal_shear_caluvw]]** (2026-07-11 신설; 본 절은 그 이후의 정합 복원만).

Three-step consistency restoration:

1. Shear reconstruction from external unit flows (`caluvw.f90:523-532`).
2. **Barotropic correction**: depth-sum `UHDYF/VHDXF` into `TVARE/TVARN` (`:601-606`), subtract external `UHDYE/VHDXE` (`:610-614`), redistribute via `CERRU/CERRV` (`:617-624`).
3. Mass-flux correction at open boundaries — face-by-face replacement using neighbor-3D − neighbor-external + boundary-external (`:766, 784, 800, 815` for S/N/E/W).

Without step 2, the 3D-integrated transport drifts from the 2D solver result; mass conservation breaks downstream.

## D. Time-stepping (3TL vs 2TL)

| Mode | `IS2TIM` | Driver | `ISTL` | DELT | Use case |
|---|---|---|---|---|---|
| 3TL leapfrog | `0` | `HDMT` | `3` predictor / `2` corrector | `DT2` | Stability, classic EFDC default |
| 3TL trapezoidal corrector | (within `HDMT`) | `HDMT` | `2` (`ROLD=ROLD=0.5`) | `DT2` | Damps leapfrog computational mode every `NTSTBC` steps |
| 2TL | `>=1` | `HDMT2T` | `2` fixed (`IS2TL=1`) | `DT` | Sediment, water quality, dynamic timestep coupling |

- 3TL leapfrog labeled at `hdmt.f90:1344-1349` and `calexp.f90:256` ("THREE TIME LEVEL (LEAP-FROG)").
- Corrector at `hdmt.f90:1335-1342`; `calexp.f90:184` ("THREE TIME LEVEL CORRECTOR STEP").
- 2TL at `hdmt2t.f90:114-115`.

## E. Buoyancy

- `CALBUOY` (`calbuoy.f90:128-179`) computes density from S, T, or both: `B = (ρ/ρ₀) − 1`.
- `CALEBI` (`calebi.f90:106-175`) integrates `B` into external buoyancy integrals `BI1/BI2/BE`.
- External pressure-gradient `FPGXE/FPGYE` assembled in CALPUV (`calpuv9c.f90:217-228`) and added to external momentum (`:256-257`).

## F. Non-hydrostatic (CALPNHS)

Activated when `KC > 1 .and. ISPNHYDS >= 1`:
- CALEXP adds non-hydrostatic pressure-gradient term (`calexp.f90:1010, 1052-1055`).
- CALUVW calls `CALPNHS` (`caluvw.f90:1319`).
- `CALPNHS` computes `PNHYDS` from physical vertical velocity `WZ`: `:50-74` velocity, `:79-103` vertical fluxes, `:162-190` pressure assembly.

This is a **quasi-non-hydrostatic** correction (pressure-projection style), not a fully wave-resolving non-hydrostatic solve.

## G. Boundary forcing into the hydro core

- `CALPSER` (`calpser.f90:45`) interpolates `PSERT(NS)` from time series + offset, called from `HDMT` (`hdmt.f90:676-677`) or `HDMT2T` (`hdmt2t.f90:611-613`) **before** the external solve.
- `SETOPENBC` writes elevation/pressure BC into `FP(L)` from side-specific `PSERT(NPSER*)`:
  - South `setopenbc.f90:252`, West `:357`, East `:460`, North `:566`.
- After PCG, boundary `HP = GI*P − BELV` (`calpuv9c.f90:804-807`).
- `CALPUV` calls `SETOPENBC` before solve (`calpuv9c.f90:638-639`; 2TL `calpuv2c.f90:591-592`).

## Decision Guide

| Situation | Setting |
|---|---|
| Standard tidal/coastal run | 3TL (`IS2TIM=0`); set `NTSTBC` so corrector fires every 24-48 steps |
| Sediment / water quality dominant | 2TL (`IS2TIM>=1`); allows dynamic timestep coupling |
| Density-stratified estuary | 3TL + `ISBAL=2` (S+T); set `IINTPG=1` or `2` for steep bathymetry |
| Wave-resolving short-wave runup | `ISPNHYDS>=1` + `KC>1` (non-hydrostatic) |
| External-mode CFL violation | Reduce `DT` first; PCG itself rarely the bottleneck |
| Mass drift | Verify CALUVW barotropic correction at `:601-624` runs, and `IS2TIM`/timestep are consistent across hot-start |

## Working Rules

- 3TL with overly long `NTSTBC` (>100) lets leapfrog computational mode grow — symptom is checkerboard `HP` field; cure is shorter `NTSTBC`.
- The PCG tolerance (`RPADJ`-related) defaults work for most cases; tighten only if PCG iteration count is large *and* mass-balance closure is poor.
- After hot-start in 3TL, the first step uses corrector (`ISTL=2`); ensure `H1P/H2P` and `UHDY1E/UHDY2E` are valid in the hot-start file.
- Non-hydrostatic mode requires `KC>=4` for meaningful pressure projection; `KC=2` usually under-resolves.
- Open BC `LOPENBCDRY` flag (`setopenbc.f90:295-306, etc.`) auto-disables a BC cell when forced elevation falls below `BELV` — important for tide gauges near dry land.

## Common Pitfalls

- ▢ Setting `IS2TIM` mid-run via hot-start without resetting `H1P/H2P` arrays — mass jump.
- ▢ Forgetting to update `PSER.INP` time origin when changing `TBEGIN` — boundary tide goes out of phase silently.
- ▢ Activating `ISPNHYDS=1` without increasing `KC` — non-hydrostatic correction is negligible.
- ▢ Using `CALPUV2C` (2TL) with stratification + leapfrog-style `NTSTBC` — `NTSTBC` does nothing in 2TL; corrector concept doesn't exist there.
- ▢ Open BC flat-elevation series with steep bathymetry — `LOPENBCDRY` switches it off; check log for "OPEN BC DRY".

## Next expansion

- ~~CALUVW vertical velocity W detailed note~~ — [[efdc_vertical]] (W 연속식 :686-872) + [[efdc_internal_shear_caluvw]] (전단 solve) 로 커버 완료 (2026-07-11).
- PCG preconditioner choice and convergence tuning (separate ops note).
- Curvilinear metric details (CAC term decomposition).

## References

- Hamrick 1992 (EFDC theoretical documentation, GWCE-style external/internal split).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
