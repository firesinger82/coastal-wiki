---
title: "ADCIRC NWS=19/20/29/30 — GAHM·AHM·OWI hybrid (source-code analysis)"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/adcirc/src/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge.md (at commit a9618df^) (modeling-wiki 4월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/raw/source_code/adcirc/src/
---

## Scope

ADCIRC's parametric tropical-cyclone forcing (NWS=19 AHM, NWS=20 GAHM), how forward-motion correction `stormMotion = 1.5 * h_speed^0.63` and `VmaxBL` adjustments work, the OWI hybrid options (NWS=29 = AHM+OWI, NWS=30 = GAHM+OWI), the actual NWS encoding (NWS=12 OWI ASCII, NWS=13 OWI NetCDF, NWS=14 GRIB2), the asymmetric Holland model formula via `uvpr` in `vortex.F`, ATCF Best Track input format, inverse-barometer suppression (`NOIVB`), and the ramp `RampMete` for vortex spin-up. Use this when wiring a hurricane hindcast, debugging vortex placement, or selecting NWS for a specific forcing combination.

## Source basis

- `read_input.F:2157, 2190, 2255-2261, 2430, 2884, 2706, 2975` — NWS modes, `BLAdj/GEOFACTOR`, `RampMete`.
- `wind.F:151, 351, 1415, 1471-1594, 1501-1531, 2798-2970, 3018, 5214-5466, 5798-6097, 8288` — NWS dispatch, IB, vortex, parsers.
- `wind/aswip.F:413-1034`, `wind/vortex.F:186, 748-932` — ASWIP, GAHM `uvpr`.
- `owiwind.F:184, 269` — OWI ASCII reader.
- `owiwind_netcdf.F:215, 681, 747` — OWI NetCDF reader.
- `constants.F90:54` — `PRBCKGRND = 1013.0 mb`.
- `docs/user_guide/.../*.rst` — user docs context.

## A. NWS=20 GAHM (Generalized Asymmetric Holland Model)

Entry: `NWS20GET` in `wind.F:1501-1517`. Fills nodal wind + pressure, converts wind → stress, ramps pressure relative to background.

`fort.15` line for NWS=20 (`read_input.F:2706`):
```
IREFYR  IREFMO  IREFDAY  IREFHR  StormNumber  BLAdj  GEOFACTOR
[+ optional ice/restart fields]
```

- `BLAdj` — boundary-layer adjustment factor.
- `GEOFACTOR` — geostrophic vs cyclostrophic balance switch (`wind.F:151`).

`fort.22` parser reads ATCF-like records + appended quadrant `Rmax`, Holland `B`, quadrant `B`, boundary-layer `Vmax` (`wind.F:5798-5811`).

Runtime interpolates `Pc, Pn, Rmax, B, BL Vmax` per node (`wind.F:6097`).

## B. NWS=19 AHM (Asymmetric Holland Model)

Older variant, calls `NWS19GET` (`wind.F:1471`). Reads modified ATCF + appended quadrant `Rmax`, Holland `B` (`wind.F:5214-5424`).

NWS=19 vs NWS=20:
- NWS=19: classic AHM, single Holland B per record.
- NWS=20: generalized — quadrant-dependent B, quadrant-dependent Rmax, BL Vmax fitted from multiple wind-radius isobars.

For most modern hindcasts, NWS=20 (GAHM) is preferred.

## C. OWI hybrid: NWS=29, NWS=30

NWS=29 = NWS=19 (AHM) embedded in **OWI/NWS12 background** (`read_input.F:2157`).
NWS=30 = NWS=20 (GAHM) embedded in OWI/NWS12 background (`:2190`).

Runtime dispatch (`wind.F:1531, 1550`):
- Vortex computed at near-storm nodes.
- OWI grid wind/pressure used elsewhere.
- Smooth blend in transition zone.

Use NWS=29/30 when:
- Storm is in a domain larger than the parametric vortex extent.
- You have OWI hindcast for the broader region.
- Want vortex-resolved core + observed/modeled meteo elsewhere.

**Note**: NWS=29/30 currently blend with NWS12 OWI **only** (not NWS13 NetCDF) in main blending path (`wind.F:1533`).

## D. OWI WIN/PRE and NWS=12/13/14

| NWS | Format | Files |
|---|---|---|
| `12` | OWI ASCII | `fort.221`-`fort.224` (pressure/wind overlays); `fort.22` is OWI control |
| `13` | OWI NetCDF | groups, `U10/V10/PSFC`, time-varying grids, optional storm center |
| `14` | GRIB2/NetCDF | originally CFSv2/GFS products (`wind.F:8288`) |
| `-14` | NWS=14 + OWI overlay | hybrid global+regional |

Code: `owiwind.F:184` (OWI ASCII control), `:269` (interpolate to nodes), `owiwind_netcdf.F:215, 681, 747` (NetCDF).

## E. Asymmetry / forward-speed correction

ASWIP removes forward-motion contribution before fitting vortex parameters (`wind/aswip.F:413, 417`):
```
stormMotion = 1.5 * h_speed^0.63
VmaxBL = (Vmax − stormMotion) / windReduction
```

NWS=19 repeats same correction at runtime (`wind.F:5466`).

GAHM spatially interpolates quadrant/isotach `Rmax, B, BL Vmax` via `spInterp` (`wind.F:6051`, `vortex.F:932`).

The actual GAHM velocity + pressure formula is `uvpr` in `vortex.F`:
- Geostrophic branch: `geof == 1`.
- Translation scaled by vortex speed.
- Reduction to surface.
- Inflow angle.
- 1-min → 10-min wind conversion.
- Pressure from `Pc, Pn, Phi, Rmax, B`.

References: `vortex.F:792, 846, 865, 896`.

## F. Best Track / ATCF format

NWS=19/20 expects ATCF Best Track / Objective Aid / Wind Radii format.

Required fields (`docs/.../nws_parameters.rst:335`):
- Forecast hour.
- Eye lat/lon.
- Max sustained wind.
- Min sea-level pressure.
- Wind radii (34/50/64 kt).
- Background pressure.
- ATCF Rmax.
- Storm name.
- Cycle number.
- Quadrant flags.
- Computed Rmax.
- Holland B.

ASWIP writes basin-prefixed `AL,` ATCF-style records for NWS19/20 (`aswip.F:1024, 1034`).

Pressure deficit is **not a separate ATCF column**; effectively `Pn − Pc` in Holland formulas (`vortex.F:186, 748`).

## G. Inverse barometer / NOIVB

Background pressure: `PRBCKGRND = 1013.0 mb` (`constants.F90:54`).

Converted to meters of water: `PRBCKGRND_MH2O = 100 * PRBCKGRND / (rhoWat0 * g)` (`wind.F:351`).

Pressure forcing applied as ramped anomaly about background:
```
PRDIFF = Ramp * (PR_forcing − PRBCKGRND_MH2O)
PR2 = PRBCKGRND_MH2O + PRDIFF
```
(`wind.F:1524, 1594`).

Compile-time `NOIVB` suppresses inverse barometer:
```
PR2 = PRBCKGRND_MH2O   ! disables IB contribution
```
(`wind.F:1415, 3018`).

Use `NOIVB` when comparing against tide-gauge data already corrected for IB (rare).

## H. Vortex spin-up ramp

There is **no separate NWS19/20-only spin-up ramp** — common meteorological ramp `RampMete` applies to wind stress, pressure anomaly, and output winds.

Ramp duration/configuration:
- `NRAMP, DRAMP` (`read_input.F:2430`).
- Fine-grained `DRampMete` (`:2884`).
- Tanh ramp table generated (`:2975`).

Applied at `wind.F:1487, 1517` for NWS=19/20.

For typical Korean / Pacific hurricane hindcasts: `DRAMP=2.0` (days), `DRampMete=1.0` (days for met-only ramp).

## Validation / typical combinations

| Application | NWS |
|---|---|
| Parametric AHM hurricane (small domain) | `19` |
| Parametric GAHM hurricane (preferred) | `20` |
| AHM + OWI background (large domain) | `29` |
| GAHM + OWI background | `30` |
| OWI ASCII met only (no vortex) | `12` |
| OWI NetCDF met only | `13` |
| GRIB2 CFSv2/GFS only | `14` |
| Global GRIB2 + regional OWI | `-14` |

GAHM docs (`docs/.../generalized_asymmetric_holland_model.rst:670`): evaluated against Best Track, AHM, SLOSH, H*Wind, OWI hindcast winds.

For Korean coast typhoons (e.g., Hinnamnor 2022, Maemi 2003), NWS=20 GAHM with KMA Best Track is the standard.

## Decision Guide

| Need | Setup |
|---|---|
| Single-storm hindcast (Korea, Japan, US East) | `NWS=20` GAHM with Best Track in `fort.22` |
| Multi-storm season | `NWS=20` per storm, sequential hot-starts |
| Hindcast with operational met | `NWS=12` OWI from NWS or `NWS=13` NetCDF |
| Hurricane core resolved + global background | `NWS=30` GAHM + OWI |
| Forecast (cone of uncertainty) | `NWS=20` per ensemble member |
| Wave-coupled storm surge | `NWS=320` (NRS=3 + NWS=20); compile `padcswan` |
| Wind-only IB-corrected hindcast | `NOIVB` compile flag + `NWS=20` |
| No ramp (debugging) | `DRAMP=0`, `DRampMete=0` |

## Working Rules

- For NWS=20: `BLAdj=0.9` typical (10-m wind reduction); `GEOFACTOR=1.0` (geostrophic) for Northern Hemisphere strong storms; `0.0` (cyclostrophic) for very strong / small storms.
- ATCF Rmax often needs adjustment via ASWIP — pre-process with ASWIP, don't feed raw ATCF.
- For NWS=30 hybrid: ensure OWI domain extends well outside vortex radius; otherwise blend produces wind-shadow artifacts.
- Output `fort.73, fort.74` (global pressure/wind) at validation stations to verify forcing.
- `RampMete` ramp ~1-2 days for met spin-up; without it, initial winds shock the cold-start.
- For Korean typhoons, KMA Best Track in JAS basin (no `AL` prefix) — convert to ATCF format with `WP` basin code for ASWIP.

## Common Pitfalls

- ▢ Using raw ATCF with NWS=20 (no ASWIP preprocessing) — quadrant `Rmax`/`B` missing; vortex degenerate.
- ▢ NWS=30 with OWI domain too small — wind shadow at OWI boundary.
- ▢ Mixing forward-speed-corrected and uncorrected ATCF — duplicate motion subtraction.
- ▢ Setting `BLAdj=1.0` thinking it's no adjustment — actually 100% reduction (typical 0.85-0.9 for boundary-layer wind to 10-m wind).
- ▢ Cold-start with strong storm and `DRAMP=0` — initial-condition shock.
- ▢ NWS=29/30 with NWS=13 expecting NetCDF blend — only NWS=12 OWI ASCII supported.
- ▢ Inverse barometer with gauge data already IB-corrected — double-count; use `NOIVB`.
- ▢ Mixed-track ensemble (forecast cone) running in single hindcast — runs but inappropriate for single-track ATCF.

## Next expansion

- ASWIP preprocessing recipe for KMA Best Track.
- NWS=14 GRIB2 setup (CFSv2/GFS).
- NWS=320 coupled hurricane+wave example.
- Inverse-barometer comparison study.

## References

- Holland 1980 (Holland B parameter).
- Powell et al. 2003 (boundary-layer reduction).
- Mattocks & Forbes 2008 (asymmetric Holland).
- Generalized Asymmetric Holland Model — ADCIRC docs.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
