---
slug: efdc_vertical
title: EFDC+ Vertical Coordinate (sigma, IGRIDV / SGZ, KC, KSZ)
model: efdc
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/efdc/source_code/EFDCPlus_Stable/EFDC
---

## Scope

How EFDC+ sets up vertical layers (sigma stretch vs Sigma-Zed/SGZ), where layer thicknesses come from, how vertical velocity W is built, vertical advection in tracers and momentum, the sigma-slope pressure-gradient option (`IINTPG`), and how the SGZ option masks bottom layers per cell. Use this when designing bathymetry-conforming layers for steep bathymetry, debugging vertical advection blow-up, or interpreting layer counts in output.

## Source basis

- `mod_var_global.f90:221, 236` — `KC`, `IGRIDV` definitions.
- `input.f90:145, 264, 516, 531` — input reads for `KC`, `IGRIDV`, `IINTPG`, sigma fractions.
- `aaefdc.f90:1294, 1308, 1323, 1332, 1341, 1435, 1443, 1448, 1492, 1497, 2382, 2592, 2610, 2820, 2944` — layer setup, SGZ allocation, face metrics.
- `varalloc.f90:1276, 1319` — SGZ array allocation, `DZC/DZG/DZIG` allocation.
- `caluvw.f90:16, 686-872, 1238` — vertical velocity W and `HPK`.
- `calexp.f90:243-406, 1152, 1169-1265` — vertical advection and PGF branches.
- `Transport/caltran.f90:49, 152-228` — vertical tracer advection and SGZ skip.
- `calpuv9c.f90:1221, 1268, 1585` — face depths, SGZ face handling.

## A. Sigma layers

- `KC` = water-column layer count (`mod_var_global.f90:221`); read from card C9A (`input.f90:516`).
- Global sigma fractions `DZCK(K)` from card C10 (`input.f90:531`); normalized to sum 1 (`aaefdc.f90:1294`).
- Cell layer fractions: `DZC(L,K)` allocated alongside `DZG/DZIG` (`varalloc.f90:1319`).
- Sigma stretch: inactive layers below `KSZ` zeroed; `DZC = DZCK / DZPC` (`aaefdc.f90:1435, 1443`).
- `DZIC/DZG/DZIG` set up in `aaefdc.f90:1492, 1497`.

## B. IGRIDV (Sigma-Zed / SGZ)

- `IGRIDV = 0` → standard sigma stretch (`mod_var_global.f90:236`, `aaefdc.f90:1323` sets `KSZ=1`).
- `IGRIDV > 0` → Sigma-Zed: variable bottom-active layer per cell.
- Read alongside `KMINV, SGZHPDELTA` at `input.f90:145`.
- SGZ arrays allocated when `IGRIDV > 0` (`varalloc.f90:1276`).
- Input: reads `sgzlayer.inp` (`aaefdc.f90:1332`):
  - `IGRIDV == 1`: per-cell `KSZ` (bottom-active layer index only).
  - `IGRIDV > 1`: per-cell `KSZ` and full `DZC(:)` array.
- Effect: layers `K < KSZ` are inactive (`DZC = 0`); face masks set by max neighbor `KSZ` (`aaefdc.f90:1448`).
- Face metrics `SGZU/SGZV` and inverses `FSGZU/FSGZV` at `aaefdc.f90:2382, 2592`.

This lets you keep coarse layering in deep water while resolving thin near-bed layers in shallow areas — classic motivation for SGZ.

## C. Vertical velocity W

Built in `CALUVW` (`caluvw.f90:16`):
- Main W block at `:686`.
- Continuity form: `W` accumulated from previous-interface `W`, horizontal flux divergences `UHDY/VHDX`, and sources `(QSUM − DZC*QSUME)` (`:697, 715, 733`).
- Time-centered `W2` for advection use (`:852, 872`).

W is **diagnostic** — solved from continuity, not prognostic. Errors in `UHDY/VHDX` propagate directly to W.

## D. Vertical advection

| Equation | File | Lines |
|---|---|---|
| Tracer flux `FWUU = W2 * CON1(KUPW)` | `Transport/caltran.f90` | `:152` |
| Tracer update `(FWUU(K-1) − FWUU(K))` | `Transport/caltran.f90` | `:169, 183` |
| Momentum vertical fluxes `FWU/FWV` from `W/W2` | `calexp.f90` | `:243, 304, 348, 406` |
| Momentum update `(FWU(K) − FWU(K-1))*DZIC` | `calexp.f90` | `:1152` |

Both use upwind (`KUPW = K − sign(W)/2`) for stability.

## E. Sigma-slope pressure-gradient (IINTPG)

- `IINTPG` read at `input.f90:264`.
- SGZ branches override first (used when `IGRIDV>0`):
  - `IGRIDV == 1` → `calexp.f90:1169`.
  - `IGRIDV > 1` → `calexp.f90:1187`.
- Sigma branches (used when `IGRIDV == 0`):

| `IINTPG` | Branch | File:Line |
|---|---|---|
| `0` | Standard density Jacobian | `calexp.f90:1207` |
| `1` | Improved sigma-slope correction | `calexp.f90:1225` |
| `2` | Finite-volume formulation | `calexp.f90:1265` |

There is **no single named "sigma-slope error correction" symbol**; the alternative formulations are selected by `IINTPG`. For steep bathymetry, use `IINTPG=1` or `2`.

## F. Free-surface layer thickness

- Current layer thickness: `HPK = HP * DZC`; inverse `HPKI` (`caluvw.f90:1238`).
- Initial: `HPK = HP * DZC` (`aaefdc.f90:2610`).
- Prior `H1PK/H2PK` for time-history (`aaefdc.f90:2944`); wet/dry update at `calpuv9c.f90:1221`.
- Sigma face depths `HU/HV` from free-surface depths (`calpuv9c.f90:1268`).
- SGZ face depths handle unequal bottom layers via `HPK/DZC` (`calpuv9c.f90:1585`).

Note: there is **no `HUVH` symbol** in this tree (sometimes referenced in older docs).

## G. Boundary handling for SGZ

- Inactive layers zeroed for tracers early (`Transport/caltran.f90:49`).
- Open-BC tracer logic skips inactive `LKSZ` (`Transport/caltran.f90:228`).
- Face masks `SUB3D/SVB3D` for SGZ (`aaefdc.f90:1448, 1458`).
- MPI subdomain boundary zeros face factors (`aaefdc.f90:2820`).

## Decision Guide

| Domain type | `IGRIDV` | `IINTPG` | Notes |
|---|---|---|---|
| Flat / mild bathymetry | `0` (sigma) | `0` | Default behavior |
| Steep slope / canyon | `0` | `1` or `2` | Reduces sigma-coordinate PGF error |
| Deep ocean + shallow shelf combined | `1` (per-cell `KSZ`) | `0` | Coarse deep, thin shallow |
| Highly variable bathymetry, per-cell layer control | `>1` (full `DZC` per cell) | `0` | Most flexible, requires `sgzlayer.inp` |
| Idealized box | `0` | `0` | Default |

## Working Rules

- For SGZ runs, ensure `KSZ` neighbors differ by no more than 1 — large jumps cause numerical noise at face transitions.
- `KMINV` (minimum active layer) prevents single-layer cells; default 1, raise to 2 for stability in very shallow cells.
- `SGZHPDELTA` controls the SGZ blending; typical values 0.1–0.3 of `HDRY`.
- If `KC >= 8` and bathymetry is steep, plot a vertical section of T/S — sigma-coordinate spurious diapycnal mixing shows as artificial stratification near slopes; cure with `IINTPG=2`.
- `HPK` should always be >= `DZC * HDRY` for active layers; if not, drying logic missed it.
- Vertical velocity W is diagnostic; large W spikes (>0.1 m/s in coastal) almost always mean horizontal flux imbalance, not a real physical signal.

## Common Pitfalls

- ▢ Setting `IGRIDV>0` without providing `sgzlayer.inp` — model crashes on read.
- ▢ Mixing sigma and SGZ between cold-start and hot-start — `KSZ` inconsistency corrupts vertical structure.
- ▢ Using `IINTPG=2` (finite-volume) with very thin layers near surface — can introduce small mass-balance errors; check with shorter timestep first.
- ▢ Confusing `HPK` (layer thickness × depth) with `DZC` (sigma fraction) — many output diagnostics need one or the other.
- ▢ Relying on `HUVH` from older documentation — symbol does not exist in this code; use `HU/HV` and `DZC` instead.

## Next expansion

- Per-cell SGZ tooling (how to generate `sgzlayer.inp` from bathymetry).
- IINTPG option benchmark on canyon cases.
- Vertical viscosity coupling note (cross-link to `efdc_turbulence.md`).

## References

- Hamrick 1992 (sigma coordinate base formulation).
- Craig 2014 (SGZ Sigma-Zed implementation in EFDC+).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
