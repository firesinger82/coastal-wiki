---
title: "delft3d sediment"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_sediment.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

Delft3D's sediment-transport architecture in `compute_sediment/`: `erosed` computes suspended source/sink + bedload + diffusivity; `bott3d` updates bed composition + level; cohesive routes through `erosilt` (Krone-Partheniades excess-shear formula `iform=-3`); noncohesive routes through `eqtran` with Van Rijn 1993 (`iform=-1`), Van Rijn 2004/SANTOSS (`iform=-2/-4`), Van Rijn 1984 (`iform=7`); 3D vs 2D source/sink via `soursin_3d`/`soursin_2d`; multi-fraction `lsedtot`; the bed-composition layer model with `compthick` transport-layer thickness; coupling to morphology via `dps = dps - depchg`; calibration parameter web (`tcrero, tcrdep, eropar, factcr, taucr, ws, bed, bedw, sus, susw`). Use this when wiring sediment for coastal/estuarine cases or interpreting `bottomdepth/dps` evolution.

## Source basis

- `compute_sediment/erosed.f90` — main entry, suspended + bedload + diffusivity.
- `compute_sediment/bott3d.f90` — bed composition + level update.
- `compute_sediment/erosilt.f90` — Partheniades-Krone cohesive.
- `compute_sediment/eqtran.f90`, `tram1.f90`, `tram2.f90`, `tranb7.f90` — transport gateways + Van Rijn formulations.
- `compute_sediment/soursin_3d.f90`, `soursin_2d.f90` — source/sink conversion.
- `compute_sediment/red_soursin.f90` — limiter.
- `compute_sediment/compthick.f90` — transport-layer thickness.
- `main/trisol.f90:1968-3279` — call sites.

## A. Directory and entry

`compute_sediment/` files: `erosed.f90, bott3d.f90, red_soursin.f90, compthick.f90, upwbed.f90, adjust_bedload.f90, updwaqflxsed.f90, dwnvel.f90, bndmorlyr.f90, avalan.f90`, dredging/fluff variants, `z_*` Z-layer equivalents.

Runtime from `trisol.f90`:
- `erosed` first computes suspended source/sink, bedload, sediment diffusivity (`:1968, 1974`).
- `bott3d` later computes bed composition + level effects (`:2204, 2205`).
- Second sequence later (`:3041, 3047, 3278, 3279`).

`erosed` fills `SOURSE/SINKSE`, bedload `SBUU/SBVV`, `SEDDIF` (`erosed.f90:46-53`).
`bott3d` updates `BODSED`, mixing-layer thickness, depths (`bott3d.f90:43-52`).

## B. Cohesive mud (Krone-Partheniades)

Mud/cohesive routed through `erosilt` (`erosed.f90:1045-1081`).

`erosilt` documents Partheniades-Krone for cohesive sediment + fluff layers (`:40-43`).

Default formula `iform=-3` parameters: erosion, critical shear deposition, critical shear erosion, fluff critical shear, fluff erosion, deposition efficiency, exponent (`:160-168`).

**Erosion** (excess shear):
```
taum = max(0, taub/tcrero - 1)
sour = eropar · taum^powern
```
(`:183-184`).

**Deposition** (Krone):
```
sink = max(0, 1 - taub/tcrdep)
```
(unless deposition efficiency overrides) (`:195-203`).

Source/sink converted to volumetric model terms using layer thickness (`:262-268`).

Bed slope can reduce cohesive erosion critical shear when slope > `WetSlope` (`:172-180`).

## C. Noncohesive sand (Van Rijn paths)

Sand fractions with bedload/advection-diffusion through `eqtran` (`erosed.f90:1125-1234`).

Van Rijn paths (`eqtran.f90:304-420`):

| `iform` | Formula | Routine |
|---|---|---|
| `-1` | Van Rijn 1993 | `tram1` (`tram1.f90:41-42`) |
| `-2` | Van Rijn 2004 (code says "Van Rijn 2007") | `tram2` (`:58`) |
| `-4` | SANTOSS | `tram2` |
| `7` | Modified Van Rijn 1984 | `tranb7` (`tranb7.f90:31-35`) |

Critical Shields/tau recomputed for spatially varying `D50`:
```
dstar, piecewise tetacr
taucr = factcr · (rho_s - rho_w) · g · d50 · tetacr
```
(`erosed.f90:1135-1162`).

Van Rijn reference height `aks` from roughness/reference, limited to 20% depth (`:923-942`).

## D. Bed/water exchange (suspended-bed)

**Cohesive**: `erosilt` returns `sourse, sinktot`; `erosed` stores in `sourse(nm,l), sinkse(nm,l)` (`erosed.f90:1074-1102`).

**Noncohesive**: `eqtran` computes reference concentration/profile; `erosed` calls `soursin_3d` or `soursin_2d` for explicit + implicit source + sink (`:1218-1335`).

In 3D: if reference concentration > bottom-cell concentration, upward diffusion creates explicit/implicit source + settling sink (`soursin_3d.f90:84-155`); else only settling sink (`:156-165`).

`red_soursin` limiter reduces large sand source/sink — **not applied to mud or pure bedload** (`red_soursin.f90:130-135`).

## E. Bed model (thickness, fractions per layer)

`erosed` gets bed fractions from bed-composition module: top-layer fractions + mud fraction via `getfrac` (`erosed.f90:629-635`).

Multi-fraction non-mud: mean diameters, percentiles, hiding/exposure, optionally active layer + coarse layer (`:697-739`).

`compthick` updates transport-layer thickness:
- Proportional to depth: `thtrlyr = max(ttlalpha · depth, ttlmin)`.
- Or proportional to dune height (`compthick.f90:89-105`).

`bott3d` calls `compthick` when composition or dredging needs current thickness (`bott3d.f90:604-612`).

Bed composition updated through `updmorlyr`, then layer diffusion + boundary composition (`:1079-1094`).

## F. Coupling to morphology (bott3d, dps)

`bott3d` computes `dbodsd(l, nm)` from suspended divergence + deposition + erosion + bedload divergence (`:722-840`).

If composition updating: `updmorlyr` → `depchg` (`:1079-1083`).
If not: `depchg` directly from `dbodsd/cdryb` over fractions (`:1112-1123`).

Bed update: `dps(nm) = dps(nm) - depchg(nm)` (`dps` positive downward) (`:1226-1240`); then water levels + `dpd` (`:1252-1308`).

## G. Multi-fraction (lsedtot)

Code consistently loops `lsedtot` (`erosed.f90:580-619, 1028-1043`):
- Source/sink reset over all fractions.
- Bedload reset over all fractions.
- Transport loop `l = 1, lsedtot`.
- Bed changes per fraction (`bott3d.f90:724-840`).

First `lsed` fractions = suspended/advection-diffusion; comments rely on this mapping with `kmxsed` (`erosed.f90:1117-1119, bott3d.f90:763-769`).

Composition updates can exclude fractions via `cmpupdfrac` (`bott3d.f90:1027-1037`).

## H. Validation pitfalls

Calibrate together:
- Mud: `tcrero, tcrdep, eropar, powern` (`erosilt.f90:160-203`).
- Sand: `factcr, taucr, tetacr, D50` (`erosed.f90:1135-1162`).

Settling velocity `ws`:
- Mud deposition (`erosilt.f90:262`).
- Sand source/sink (`soursin_3d.f90:146-165`, `soursin_2d.f90:80-114`).

Bed roughness affects:
- Shear/velocity construction (`erosed.f90:854-890`).
- Van Rijn reference height (`:923-942`).

Calibration multipliers `bed, bedw, susw, sus` scale transport/concentration after formula evaluation (`eqtran.f90:722-743`).

Large morphology changes warned but not capped in `bott3d` (`:815-840`) — validate timestep, `morfac, cdryb`, layer availability.

## Decision Guide

| Application | Setup |
|---|---|
| Estuarine mud-dominated | Mud fraction(s) with `iform=-3`; calibrate `tcrero, tcrdep` |
| Sandy beach with wave asymmetry | `iform=-2` (Van Rijn 2004) or `-4` (SANTOSS) |
| Coastal mixed mud+sand | Both fraction types; `cmpupdfrac` if needed |
| River bedload dominant | `iform=7` (Van Rijn 1984) |
| Fluff layer | Built-in via `iform=-3` parameters |
| Multi-fraction (sand sizes) | `lsedtot > 1`, per-fraction `D50, ws, tcrero` |
| Long-term morfac | Verify mass conservation; check `wrwaqbal` if WAQ-coupled |
| Q3D-style suspended profile | Not built-in; use Z-model + `kmxsed` |

## Working Rules

- For Korean coastal mud (Yeongsan, Han mouth): mud `iform=-3`, `tcrero=0.1-0.3 Pa`, `eropar=1e-5 to 5e-4 kg/m²/s`.
- Sand `D50` 0.1-0.5 mm typical; `factcr=1.5-2.0` for hiding effect in mixtures.
- Output `dps, sbuu, sbvv, sourse, sinkse` for diagnostics.
- Multi-fraction needs `cdryb` per fraction; check sum consistency.
- `morfac > 1` requires monitoring `bott3d` warnings.
- Hot-start with sediment: bed composition state must be preserved.

## Common Pitfalls

- ▢ Wrong sign on `dps` — positive downward; `dps -= depchg` for accretion is correct.
- ▢ Confusing `iform=-2` with `-4` — both via `tram2` but different physics.
- ▢ Setting `tcrdep > tcrero` — model halts; deposition must be at lower stress than erosion.
- ▢ Multi-fraction without `D50` per fraction — defaults applied silently.
- ▢ Forgetting `red_soursin` doesn't limit mud — large mud source/sink can propagate; verify dt.
- ▢ Suspended sand without 3D — only `soursin_2d` available; less accurate.
- ▢ `morfac` very high without conservation check — silent mass drift.

## References

- Van Rijn 1984, 1993, 2004 (Sediment Transport).
- SANTOSS team (Van der A et al. 2013).
- Krone 1962; Partheniades 1965.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src/compute_sediment`. Auto-draft = false; review_required = true.
