---
title: "efdc vertical"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_vertical.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How EFDC+ sets up vertical layers (sigma stretch vs Sigma-Zed/SGZ), where layer thicknesses come from, how vertical velocity W is built, vertical advection in tracers and momentum, the sigma-slope pressure-gradient option (`IINTPG`), and how the SGZ option masks bottom layers per cell. Use this when designing bathymetry-conforming layers for steep bathymetry, debugging vertical advection blow-up, or interpreting layer counts in output.

## Source basis

- `mod_var_global.f90:221, 236` — `KC`, `IGRIDV` definitions.
- `input.f90:150, 269, 538, 553` — input reads for `KC`, `IGRIDV`, `IINTPG`, sigma fractions.
- `aaefdc.f90:1295, 1310, 1325, 1334, 1343, 1437, 1445, 1450, 1494, 1499, 2384, 2594, 2612, 2822, 2946` — layer setup, SGZ allocation, face metrics.
- `varalloc.f90:1276, 1319` — SGZ array allocation, `DZC/DZG/DZIG` allocation.
- `caluvw.f90:16, 686-872, 1238` — vertical velocity W and `HPK`.
- `calexp.f90:243-406, 1152, 1169-1222` — vertical advection and PGF branches.
- `Transport/caltran.f90:49, 152-228` — vertical tracer advection and SGZ skip.
- `calpuv9c.f90:1221, 1268, 1585` — face depths, SGZ face handling.

## A. Sigma layers

- `KC` = water-column layer count (`mod_var_global.f90:221`); read from card C9A (`input.f90:538`).
- Global sigma fractions `DZCK(K)` from card C10 (`input.f90:553`); normalized to sum 1 (`aaefdc.f90:1295`).
- Cell layer fractions: `DZC(L,K)` allocated alongside `DZG/DZIG` (`varalloc.f90:1319`).
- Sigma stretch: inactive layers below `KSZ` zeroed; `DZC = DZCK / DZPC` (`aaefdc.f90:1437, 1445`).
- `DZIC/DZG/DZIG` set up in `aaefdc.f90:1494, 1499`.

## B. IGRIDV (Sigma-Zed / SGZ)

- `IGRIDV = 0` → standard sigma stretch (`mod_var_global.f90:236`, `aaefdc.f90:1325` sets `KSZ=1`).
- `IGRIDV > 0` → Sigma-Zed: variable bottom-active layer per cell.
- Read alongside `KMINV, SGZHPDELTA` at `input.f90:150`.
- SGZ arrays allocated when `IGRIDV > 0` (`varalloc.f90:1276`).
- Input: reads `sgzlayer.inp` (`aaefdc.f90:1334`):
  - `IGRIDV == 1`: per-cell `KSZ` (bottom-active layer index only).
  - `IGRIDV > 1`: per-cell `KSZ` and full `DZC(:)` array.
- Effect: layers `K < KSZ` are inactive (`DZC = 0`); face masks set by max neighbor `KSZ` (`aaefdc.f90:1450`).
- Face metrics `SGZU/SGZV` and inverses `FSGZU/FSGZV` at `aaefdc.f90:2384, 2594`.

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

## E. Sigma-slope pressure-gradient (IGRIDV; IINTPG legacy input)

- `IINTPG` is still read at `input.f90:269`, but EFDC+ Stable 12.5 no longer uses it to select buoyancy shear. Its only remaining behavioral consumer is `setbcs.f90:449`: `IINTPG /= 0` disables the external density-gradient cell-face flag treatment for 2-cell-wide channels. In `calexp2t.f90` (2TL), the four `IINTPG` occurrences were also removed (`calexp2t.f90:1246-1305`).
- Buoyancy shear branches use `IGRIDV`; SGZ branches apply when `IGRIDV>0`:
  - `IGRIDV == 1` → `calexp.f90:1169`.
  - `IGRIDV > 1` → `calexp.f90:1187`.
- v12.5 branches:

| `IGRIDV` | Branch | File:Line |
|---|---|---|
| `== 1` | Sigma-Zed buoyancy shears | `calexp.f90:1169` |
| `> 1` | Sigma-Zed buoyancy shears | `calexp.f90:1187` |
| else | STANDARD-SIGMA buoyancy shears | `calexp.f90:1206-1207` |

There is **no single named "sigma-slope error correction" symbol**; for EFDC+ Stable 12.5, the `IINTPG` buoyancy-shear branches were removed; use `IGRIDV>0` (SGZ) for steep bathymetry. `IINTPG /= 0` disables the 2-cell-wide channel external density-gradient cell-face flag treatment at `setbcs.f90:449`.

## F. Free-surface layer thickness

- Current layer thickness: `HPK = HP * DZC`; inverse `HPKI` (`caluvw.f90:1238`).
- Initial: `HPK = HP * DZC` (`aaefdc.f90:2612`).
- Prior `H1PK/H2PK` for time-history (`aaefdc.f90:2946`); wet/dry update at `calpuv9c.f90:1221`.
- Sigma face depths `HU/HV` from free-surface depths (`calpuv9c.f90:1268`).
- SGZ face depths handle unequal bottom layers via `HPK/DZC` (`calpuv9c.f90:1585`).

Note: there is **no `HUVH` symbol** in this tree (sometimes referenced in older docs).

## G. Boundary handling for SGZ

- Inactive layers zeroed for tracers early (`Transport/caltran.f90:49`).
- Open-BC tracer logic skips inactive `LKSZ` (`Transport/caltran.f90:228`).
- Face masks `SUB3D/SVB3D` for SGZ (`aaefdc.f90:1450, 1460`).
- MPI subdomain boundary zeros face factors (`aaefdc.f90:2822`).

## Decision Guide

| Domain type | `IGRIDV` | `IINTPG` | Notes |
|---|---|---|---|
| Flat / mild bathymetry | `0` (sigma) | `0` | Default behavior |
| Steep slope / canyon | `>0` (SGZ) | `0` | EFDC+ Stable 12.5 removed the `IINTPG` buoyancy-shear branches; `IINTPG /= 0` disables the 2-cell-wide channel external density-gradient cell-face flag treatment at `setbcs.f90:449` |
| Deep ocean + shallow shelf combined | `1` (per-cell `KSZ`) | `0` | Coarse deep, thin shallow |
| Highly variable bathymetry, per-cell layer control | `>1` (full `DZC` per cell) | `0` | Most flexible, requires `sgzlayer.inp` |
| Idealized box | `0` | `0` | Default |

## Working Rules

- For SGZ runs, ensure `KSZ` neighbors differ by no more than 1 — large jumps cause numerical noise at face transitions.
- `KMINV` (minimum active layer) prevents single-layer cells; default 1, raise to 2 for stability in very shallow cells.
- `SGZHPDELTA` controls the SGZ blending; typical values 0.1–0.3 of `HDRY`.
- If `KC >= 8` and bathymetry is steep, plot a vertical section of T/S — sigma-coordinate spurious diapycnal mixing shows as artificial stratification near slopes; for EFDC+ Stable 12.5, the `IINTPG` buoyancy-shear branches were removed; use `IGRIDV>0` (SGZ) for steep bathymetry. `IINTPG /= 0` disables the 2-cell-wide channel external density-gradient cell-face flag treatment at `setbcs.f90:449`.
- `HPK` should always be >= `DZC * HDRY` for active layers; if not, drying logic missed it.
- Vertical velocity W is diagnostic; large W spikes (>0.1 m/s in coastal) almost always mean horizontal flux imbalance, not a real physical signal.

## Common Pitfalls

- ▢ Setting `IGRIDV>0` without providing `sgzlayer.inp` — model crashes on read.
- ▢ Mixing sigma and SGZ between cold-start and hot-start — `KSZ` inconsistency corrupts vertical structure.
- ▢ For EFDC+ Stable 12.5, the `IINTPG` buoyancy-shear branches were removed; use `IGRIDV>0` (SGZ) for steep bathymetry. `IINTPG /= 0` disables the 2-cell-wide channel external density-gradient cell-face flag treatment at `setbcs.f90:449`.
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

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
