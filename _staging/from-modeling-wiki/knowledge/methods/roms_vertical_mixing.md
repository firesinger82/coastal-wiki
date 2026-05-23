---
slug: roms_vertical_mixing
title: ROMS Vertical Mixing (GLS / MY2.5 / KPP)
model: roms
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/roms/source_code/roms
---

## Scope

How ROMS dispatches between the three vertical mixing closures, what state they carry, where stability functions live, how the bottom boundary layer is treated, and how `Akv`/`Akt` are exposed to history output. Use this when picking a closure, debugging surface/bottom mixed-layer depth, or extracting mixing coefficients for analysis.

## Source basis

- `ROMS/Include/cppdefs.h:233-253` — mutually exclusive closure macros and stability-function selectors.
- `ROMS/Nonlinear/main3d.F:75-100, 535-1030` — closure dispatch into the main nonlinear loop.
- `ROMS/Modules/mod_mixing.F` — state arrays (`tke`, `gls`, `Lscale`, `Akk`, `Akp`, `Akv`, `Akt`).
- `ROMS/Nonlinear/gls_*.F`, `my25_*.F`, `lmd_*.F` — solver kernels.
- `ROMS/Nonlinear/set_vbc.F:576-693` — bottom-stress drag laws.
- `ROMS/Utility/def_his.F`, `wrt_his.F` — history-file output paths.

## A. Mixing scheme dispatch

- The closures `GLS_MIXING`, `MY25_MIXING`, `LMD_MIXING` are **mutually exclusive** at compile time (`cppdefs.h:233-240`).
- `main3d.F:75-100` conditionally imports `gls_*`, `my25_*`, or `lmd_vmix` modules into the nonlinear loop.
- Dispatch points:
  - `main3d.F:535-537` — KPP coefficient update before 3D RHS/steps.
  - `main3d.F:642-645` — predictor turbulence step (`my25_prestep` / `gls_prestep`) right after `rhs3d`.
  - `main3d.F:1027-1030` — corrector turbulence step in vertical-mixing/turbulence phase.

## B. GLS (Generic Length Scale)

State arrays (`mod_mixing.F:237-257`):
- `tke` (turbulent kinetic energy).
- `gls` (length-scale-related variable; psi-equation).
- `Lscale` (turbulent length).
- `Akk` (TKE diffusivity), `Akp` (psi diffusivity), `Akv`, `Akt` (the mixing outputs you actually want).

Workflow:
1. `gls_prestep.F:52-70` — predictor advection of `tke` / `gls`.
2. `gls_corstep.F:76-120` — corrector applies shear/buoyancy production, dissipation, and updates all five fields.
3. Stability functions (`gls_corstep.F:1084-1126`) selected by CPP path: `CANUTO_A`, `CANUTO_B`, `KANTHA_CLAYSON_KCQE`, `KANTHA_CLAYSON`, else Galperin-type.
4. Top/bottom Dirichlet BCs (`gls_corstep.F:885-928`); top includes optional `CHARNOK`, `CRAIG_BANNER`, or wave-dissipation forcing.
5. Surface/bottom `Akv/Akk/Akp` set; tracer `Akt` reset to background (`:1168-1181`).

GLS lets you emulate `k-ε`, `k-ω`, `k-kl`, generic-length-scale by picking `gls_p, gls_m, gls_n, gls_cmu0` in input — single solver, multiple closures.

## C. MY2.5 (Mellor-Yamada 2.5)

- Operationally uses `tke` (~ `q²`) and `gls` repurposed as `q² L` length-scale-like prognostic (`mod_mixing.F:95-99`).
- Predictor: advection-only step for `tke/gls` (`my25_prestep.F:52-67`).
- Corrector: production/dissipation + implicit vertical diffusion solver (`my25_corstep.F:59-87`).
- Wall scaling for dissipation uses parabolic wall function `Wscale = my_E2/(kappa²)` with surface and bottom distance factors (`my25_corstep.F:628-633`).
- Stability functions: Galperin or Kantha-Clayson (`#ifdef KANTHA_CLAYSON`) form `Sm/Sh` from `Gh` (`:716-730`).

MY2.5 is the legacy closure — keep for backward comparison, but new applications generally choose GLS k-ε or k-ω.

## D. KPP (LMD/KPP)

`lmd_vmix.F:33-90` is the top-level driver:

1. Interior mixing (`lmd_vmix_tile`) — shear instability via gradient Richardson `Rig = bvf / (shear² + eps)` (`lmd_vmix.F:181-241, 326-337`); double-diffusion add-ons via `lmd_finish`.
2. Surface BL (`lmd_skpp`) — bulk-Richardson criterion `Rib(hsbl) = Ric` defines BL depth (`lmd_skpp.F:332-334, 482-547`); shape-function-based `Akv/Akt` inside BL (`:884-898`).
3. Optional bottom BL (`lmd_bkpp`) — analogous treatment producing `hbbl`/`kbbl` and BBL `Akv/Akt`.
4. Finishing pass (`lmd_finish`) — combines, applies background.

KPP is **non-local**: it computes a mixed-layer depth and applies a profile inside it, rather than solving a prognostic TKE equation. Cheap, robust, but less responsive to transient turbulence events than GLS.

## E. Bottom boundary layer

Two paths:

| Configuration | Code path | Behavior |
|---|---|---|
| `BBL_MODEL` off, `LMD_BKPP` off | `set_vbc.F:576-693` | Direct stress law (log/quadratic/linear) |
| `BBL_MODEL` off, `LMD_BKPP` on | `lmd_bkpp.F` | KPP-style BBL with `hbbl/kbbl` |
| `BBL_MODEL = SG/MB/SSW` | separate sediment-coupled BBL | Full wave-current interaction |

Stress-law branches in `set_vbc.F`:
- Logarithmic: `Cd = κ²/log((z1-z0)/z0)²`, clipped by `Cdb_min/max` (`:597-600`).
- Quadratic: `τ = ρ * rdrag2 * |u|·u` (`:647-665`).
- Linear: `τ = ρ * rdrag * u` (`:680-693`).

`Ustar` (friction velocity) for KPP-BBL is built from `bustr/bvstr` (`lmd_bkpp.F:248-255`).

## F. Stability functions

- GLS: switch block at `gls_corstep.F:1084-1126` (Canuto A/B, KC-QE, KC, Galperin fallback).
- MY2.5: Galperin or Kantha-Clayson at `my25_corstep.F:716-730`.
- Compile-time selection via `cppdefs.h:249-253` (`CANUTO_A`, `CANUTO_B`, `KANTHA_CLAYSON`).
- KPP includes anisotropy-like directional smoothing for Richardson diagnostics (`RI_HORAVG`, `RI_VERAVG`, spline/non-spline via `RI_SPLINES`) (`lmd_vmix.F:245-307`) — affects how instability-driven mixing is *diagnosed*, not the closure itself.

## G. Output of mixing coefficients

History-file variables (`def_his.F:1595-1649`, `wrt_his.F:1653-1713`):
- `idVvis` ⇒ `MIXING(ng)%Akv` — vertical viscosity (m²/s).
- `idTdif` ⇒ `MIXING(ng)%Akt(:,:,:,itemp)` — temperature diffusivity.
- `idSdif` ⇒ `MIXING(ng)%Akt(:,:,:,isalt)` — salinity diffusivity.

PIO path mirrors at `wrt_his.F:4132-4208`. Note: `mod_mixing.F` is the state container; **there is no `ROMS/Nonlinear/mixing.F`** in this tree.

## Decision Guide

| Application | Closure |
|---|---|
| Open-ocean mixed-layer dynamics, transient events | GLS k-ε (`Vstretching=4`, `theta_s≥6`) |
| Shallow shelf with strong tides | GLS k-ω or MY2.5 |
| Quick configuration, no TKE budget needed | KPP |
| Sediment / wave-current BBL | `BBL_MODEL = SSW` (Sherwood-Signell-Warner) |
| Reproducing legacy ROMS results | MY2.5 |
| Idealized stratified tests | KPP (lowest setup overhead) |

## Working Rules

- For GLS, set `gls_cmu0=0.5544`, `gls_p`, `gls_m`, `gls_n` according to chosen subform (k-ε: `p=3, m=1.5, n=-1`; k-ω: `p=-1, m=0.5, n=-1`). Don't mix-and-match without checking.
- Always output `Akv` and `Akt(itemp)` to history when calibrating — looking at `T/S` profiles alone hides whether mixing is doing the right thing.
- `Charnok` boundary at the surface is required when forcing with strong winds; otherwise GLS underpredicts surface TKE production by 30–50%.
- KPP `Ric` defaults to 0.45–0.50 (deep ML) or 0.30 (shallow ML); test sensitivity if MLD is your target metric.
- Bottom drag: log-law gives a physical `Cd`, but `z0` choice dominates. Use sediment-derived `z0` for shelves; constant `Cd` (quadratic) is acceptable for idealized runs.

## Common Pitfalls

- ▢ Activating two closures simultaneously — compile fails or worse, silently uses wrong one.
- ▢ Output `Akt` shows zero at surface — that is intentional (surface BC is Dirichlet on tracers; surface tracer flux enters via `stflux`, not `Akt`).
- ▢ KPP `hsbl` looks unrealistically deep — usually due to weak stratification ICs, not a code bug. Check `bvf` near surface.
- ▢ GLS blow-up after restart — `tke/gls` are prognostic and must be in the restart file. Cold-starting `tke=0` causes a singular dissipation term.
- ▢ Confusing `Akv` (viscosity) with `Akt` (diffusivity) when comparing with observations — `Pr_t` is not 1 in stratified flows.

## Next expansion

- Per-stability-function comparison (Canuto A vs KC-QE for shelf seas).
- Sediment-BBL detailed note (`BBL_MODEL=SSW` wave-current closure).

## References

- Umlauf & Burchard 2003 (GLS unification).
- Mellor & Yamada 1982 (MY2.5).
- Large, McWilliams, Doney 1994 (KPP).
- Warner et al. 2005 (ROMS GLS implementation).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
