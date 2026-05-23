---
title: "roms advection"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_advection.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

Where each advection scheme lives in the source, how to select per-tracer schemes via runtime `Hadvection/Vadvection` switches, how monotonicity limiters (HSIMT, MPDATA) work, how the open-boundary advective flux is decided per cell, and the relationship between advection choice and pressure-gradient correction. Use this when sediment/biology requires monotonicity, when tracer rings appear, or when checking momentum conservation.

## Source basis

- `ROMS/Nonlinear/step3d_t.F` — all tracer advection branches (centered, upstream, MPDATA, HSIMT, splines, Akima).
- `ROMS/Nonlinear/rhs3d.F` — momentum advection (centered-2, centered-4, 3rd-order upstream-bias).
- `ROMS/Nonlinear/mpdata_adiff.F` — MPDATA antidiffusive correction.
- `ROMS/Nonlinear/t3dbc_im.F`, `u3dbc_im.F` — open-boundary radiation/inflow logic.
- `ROMS/Nonlinear/prsgrd.F` + variants `prsgrd31/32/40/42/44.h` — sigma-coordinate pressure-gradient.
- `ROMS/Include/cppdefs.h` — `TS_MPDATA_LIMIT`, `UV_C2ADVECTION`, `UV_C4ADVECTION`, `UV_VIS2`, `UV_SADVECTION`.

Note on missing files: this tree has no `u3dbc.F`, `t3dbc.F`, `t3drhs.F`, `u3drhs.F`. Use the `_im.F` variants and `step3d_t.F`/`rhs3d.F` instead.

## A. Tracer horizontal advection

Selected at runtime per tracer via `Hadvection(itrc,ng)%<scheme>`:

| Scheme | Code | Properties |
|---|---|---|
| `CENTERED2` | `step3d_t.F:432-434` | 2nd order, dispersive, no monotonicity |
| `CENTERED4` | `:633, 676, 693, 740, 757` | 4th order, less dispersive, still no monotonicity |
| `UPSTREAM3` | `:633, 667, 687, 731, 751` | 3rd-order upstream-biased, hyperdiffusive — smooths but keeps direction |
| `MPDATA` | `:451, 873, 1376` + `mpdata_adiff.F:174` | Multi-pass: upwind base + recursive antidiffusive correction |
| `HSIMT` | `:475-476, 526, 545, 1117, 1132` | TVD limiter, **monotonic** (no over/undershoots) |
| `AKIMA4` | `:633` family | Akima 4th-order spline |

Note: this version's tracer scheme selection is largely **runtime** via `Hadvection/Vadvection` fields, not direct CPP macros like `TS_U3HADVECTION` or `TS_C4HADVECTION` (those are not present in this tree).

## B. Tracer vertical advection

Selected per tracer via `Vadvection(itrc,ng)%<scheme>`:

| Scheme | Code | Properties |
|---|---|---|
| `CENTERED2` | `step3d_t.F:1027-1029` | 2nd order |
| `CENTERED4` / `SPLIT_U3` | `:1144-1145` | 3rd-order upstream/4th-order centered share stencil branch |
| `SPLINES` | `:936-938` | Cubic-spline reconstruction |

Momentum vertical advection variants are at `rhs3d.F:1098-1314` including `UV_SADVECTION` (spline vertical advection, `cppdefs.h:30,38`).

## C. Momentum advection

| Branch | Selector | Code |
|---|---|---|
| Centered-2 | `UV_C2ADVECTION` | `rhs3d.F:752-754, 812-814` |
| Centered-4 | `UV_C4ADVECTION` | `rhs3d.F:831, 951` |
| 3rd-order upstream-biased | else (default) | `rhs3d.F:951+` with velocity-dependent hyperdiffusion |

`UV_VIS2` controls **harmonic momentum mixing** (`uv3dmix2`), not the advection stencil itself — common confusion (`rhs3d.F:54, 195`). To get explicit horizontal viscosity, set `UV_VIS2` and supply `visc2`.

No "Sadourny" or "Arakawa" energy-conserving tags are present in this tree; available named switch is `UV_SADVECTION` (spline vertical advection only) — not horizontal energy conservation.

## D. Limiters / monotonicity

- **HSIMT TVD limiter**: `step3d_t.F:475-476, 526, 545, 1117, 1132`. Implements a flux-corrected transport with explicit slope limiter, guaranteeing monotonicity.
- **MPDATA limiter option**: `cppdefs.h:88`, `mpdata_adiff.F:155`. With `TS_MPDATA_LIMIT`, the corrective flux factor is reduced from `1.0` to `0.25` — softer correction, less shape-preserving.
- **WENO**: not in tracer/momentum advection kernels; appears only in pressure-gradient Jacobian options (`prsgrd42.h`, `prsgrd44.h`) and biology/sediment modules.

For positive-definite tracers (sediment, biology, dye, salinity in some cases), use HSIMT or MPDATA. For temperature/salinity in normal stratified flows, UPSTREAM3 is the typical workhorse.

## E. Pressure-gradient (sigma-coordinate error)

Dispatcher in `prsgrd.F:16-25`:

| CPP option | Implementation file | Notes |
|---|---|---|
| `PJ_GRADPQ4` | `prsgrd44.h` | Quartic with WENO reconciliation |
| `PJ_GRADPQ2` | `prsgrd42.h` | Quartic, simpler |
| `PJ_GRADP` | `prsgrd40.h` | Standard density Jacobian |
| `DJ_GRADPS` | `prsgrd32.h` | Density-Jacobian splines |
| else | `prsgrd31.h` | Standard Jacobian (legacy default) |

`cppdefs.h:90-101` documents that the quartic options are tied to **WENO reconciliation and monotonicity constraints** — these are intended for steep-bathymetry domains where standard density-Jacobian sigma-coordinate error is significant (deep canyons, abrupt shelf breaks).

## F. Boundary handling for advection

- Tracer open/radiation BC (`t3dbc_im.F:96-498`): implicit upstream-radiation form with celerities `Cx, Ce` and optional nudging.
- Closed BC: `:207, 341, 475, 609`.
- Inflow vs outflow: sign test `(dTdt * dTdx) < 0` (or `dTde` on N/S edges) selects inflow nudging coefficient `obc_in` vs outflow `obc_out` (`:127, 261, 395, 529`).
- Momentum analog: `u3dbc_im.F:97, 220, 504, 662`.

This per-cell sign test is what lets boundary nudging be loose at outflow (let interior solution leave) and tight at inflow (lock to climatology) — a key tunable.

## Decision Guide

| Tracer / Application | Choice |
|---|---|
| T, S, normal stratified | `UPSTREAM3` horizontal + `CENTERED4` vertical |
| Sediment, biology, dye | `HSIMT` horizontal + `SPLINES` vertical |
| Coastal high-resolution, sharp fronts | `HSIMT` |
| Idealized accuracy benchmark | `CENTERED4` (no monotonicity, but high order) |
| Mass-conserving, monotonic, tolerable cost | `MPDATA` with `TS_MPDATA_LIMIT` |
| Steep bathymetry (canyons, slopes) | `PJ_GRADPQ4` (PRSGRD) |
| Standard shelf bathymetry | `DJ_GRADPS` |
| Inflow-dominated boundary | `obc_in ≫ obc_out` (e.g., 1 day vs 1 year) |
| Outflow / radiating boundary | `obc_in = obc_out` weak |
| Momentum, normal config | default 3rd-order upstream-bias |
| Momentum with explicit energy budget | `UV_C4ADVECTION` + `UV_VIS2` |

## Working Rules

- Always set `Hadvection` and `Vadvection` per tracer in input — defaults can vary by code version.
- HSIMT cost: ~25% over UPSTREAM3 in typical configs. Worth it for any positive-definite tracer.
- MPDATA without `TS_MPDATA_LIMIT` can produce ringing in fronts; turn the limiter on for production runs.
- For sigma-coordinate steep-bathy domains, `PJ_GRADPQ4` reduces velocity bias near sharp slopes substantially — pair with smoothed bathymetry (`r_max ≤ 0.2`) for best results.
- `obc_in / obc_out` ratio of 100–1000 is normal for nesting boundaries.
- If you see tracer mass drift, check the `Huon/Hvom` correction in `step3d_uv.F:1507-1526` — advection scheme is rarely the cause; barotropic-baroclinic coupling is.

## Common Pitfalls

- ▢ Choosing `CENTERED2/4` for sediment — produces negative concentrations, model crashes downstream.
- ▢ Using `MPDATA` without `TS_MPDATA_LIMIT` then complaining about ringing — turn on the limiter.
- ▢ Setting `UV_VIS2` and assuming it controls advection — it controls *harmonic mixing*, not the advection stencil.
- ▢ Sigma-coordinate model with steep bathymetry on default `PJ_GRADP` — produces spurious velocities along density surfaces; switch to `PJ_GRADPQ4`.
- ▢ `obc_in < obc_out` (inverted ratio) — boundary leaks rather than nudges.
- ▢ Mixing schemes between tracers in restart vs new run — Hadvection setup must be consistent or T/S restart drift appears.

## Next expansion

- Quantitative comparison HSIMT vs MPDATA cost+accuracy on standard test cases.
- Pressure-gradient bias measurement for canyon test (`prsgrd31` vs `prsgrd44`).

## References

- Smolarkiewicz 1984, 2006 (MPDATA).
- Wu & Zhu 2010 (HSIMT TVD).
- Shchepetkin & McWilliams 2003 (sigma-coordinate PGF).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
