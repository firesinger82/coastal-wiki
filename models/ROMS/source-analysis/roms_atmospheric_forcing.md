---
title: "roms atmospheric forcing"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_atmospheric_forcing.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How `BULK_FLUXES` calls `bulk_flux` in the 3D nonlinear driver, the input fields required (`Tair, Pair, Qair, rain, Uwind, Vwind, swrad, lwrad/lwrad_down`), the COARE 3.0 algorithm with fixed 3-iteration Monin-Obukhov stability loop, longwave options (Berliand under `LONGWAVE`, downwelling under `LONGWAVE_OUT`, direct net), wind stress with rain momentum impact, cool-skin (`COOL_SKIN`) but **no separate warm-layer** in this routine, spectral shortwave penetration via `SOLAR_SOURCE` and Paulson-Simpson Jerlov water type (`lmd_swfrac`), and history output of bulk-flux variables. Use this when wiring atmospheric forcing for a coupled run, debugging COARE convergence, or interpreting heat-flux components.

## Source basis

- `Nonlinear/main3d.F:51, 441-454` — bulk_flux dispatch.
- `Nonlinear/bulk_flux.F:20-1336, 74-79, 150-1558, 768-920, 1493-1558` — bulk flux algorithm.
- `Nonlinear/get_data.F:222-544` — input loading.
- `Nonlinear/set_data.F:216-628` — interpolation.
- `Nonlinear/pre_step3d.F:324-892`, `lmd_swfrac.F:17-67` — shortwave penetration.
- `External/varinfo.yaml:2034, 2067` — variable metadata.
- `Modules/mod_ncparam.F:168` — `Hout` definitions.
- `Utility/def_his.F:5109-5352`, `wrt_his.F:1834-2200` — history output.

## A. Dispatch

`BULK_FLUXES` brings `bulk_flux` into 3D nonlinear driver (`main3d.F:51`).

During VBC setup, `main3d` calls `bulk_flux(ng, tile)` **before** `set_vbc` (`:441-448`).

## B. Inputs

`bulk_flux` passes atmospheric forcing into `bulk_flux_tile`:
- `Hair/Qair, Pair, Tair, Uwind, Vwind, rain`.
- `lhflx, lrflx, shflx, srflx`.
- Output stresses `sustr/svstr` (`bulk_flux.F:150-396`).

Input loading in `get_data.F`:

| Field | Lines |
|---|---|
| `swrad` | `:427` |
| `lwrad`/`lwrad_down` | `:463/483` |
| `Tair` | `:503` |
| `Qair` | `:524` |
| `rain` | `:544` |
| `Pair` | `:222` |

Interpolation in `set_data.F`: `Tair/Qair/swrad/lwrad_down/Uwind/Vwind/rain/Pair` (`:216-628`).

## C. COARE 3.0 iteration

Documented as COARE 3.0 recovery via `COARE_30` (`bulk_flux.F:74, 79`).

Initialization (`:653-747`):
- Humidity, density, latent heat.
- Gustiness.
- Neutral roughness.
- First Monin-Obukhov guesses.

**Stability loop fixed at `IterMax = 3`** (`:429, 830`).

COARE 3.0 Charnock + scalar roughness under `COARE_30` (`:797, 859`).

Stability functions: `bulk_psiu`, `bulk_psit` (`:1493, 1558`).

Three iterations is enough for typical conditions (>95% convergence per Fairall et al. 1996); for extreme cases, the routine accepts the 3-iter result without convergence check.

## D. Heat flux assembly

**Longwave** branches:

| Option | Behavior | Lines |
|---|---|---|
| `LONGWAVE` | Berliand formula (clear-sky bulk) | `:616` |
| `LONGWAVE_OUT` | Downwelling minus SST emission | `:635` |
| (default) | Direct net `lrflx` | `:643` |

**Sensible**: turbulent `Hs` + rain sensible heat `Hsr` (`:986`).

**Latent**: turbulent `Hl` + Webb correction `Hlw` (`:1011, 1025`).

**Final kinematic flux**:
```
stflux(:,:,itemp) = srflx + lrflx + lhflx + shflx
```
(`:1276`).

So total surface heat flux assembled from four components, all output separately for diagnostics.

## E. Wind stress

Winds either wind-minus-current (relative) or raw `Uwind/Vwind` (`bulk_flux.F:527-553`).

Wind magnitude computed (`:587`).

Stress includes rain momentum impact, normalized by `Wmag`, projected to `Taux/Tauy` (`:1040-1050`).

Final `sustr/svstr`: rho-scaled, staggered averages in kinematic units (`:1316-1336`).

Wind-minus-current (`relative_wind=T`) is more physical but requires currents; for forecast-quality sensitivity, raw winds are fine.

## F. Cool skin (no warm layer)

File cites Fairall cool-skin/warm-layer (`:20`).

Implemented: **`COOL_SKIN`** only:
- Declarations (`:448`).
- Initial `delTc = blk_dter` (`:768`).
- Iterative cool-skin update (`:920`).

**No separate warm-layer state/update** found in `bulk_flux.F`.

For diurnal warm-layer effects on SST, use external pre-processed SST forcing or extend the routine.

## G. Shortwave penetration (SOLAR_SOURCE)

`LWRAD_DOWN` affects **longwave only** via `idLdwn` and `LONGWAVE_OUT` (`varinfo.yaml:2067`); used as downwelling longwave (`bulk_flux.F:635`).

**Spectral shortwave penetration** is separate option `SOLAR_SOURCE`:
- `pre_step3d.F:324`: computes `swdk` at W-points.
- `:892`: adds `dt * srflx * swdk` to tracer flux divergence.
- `lmd_swfrac.F:17, 67`: Paulson-Simpson **two-band Jerlov water type `Jwtype`**.

So shortwave doesn't all go to surface — penetrating fraction `swdk(z)` heats deeper layers.

Jerlov types: I (clear ocean), IA, IB, II, III; coastal water typically II or III.

## H. History output

Switches `Hout(:,:)` (`mod_ncparam.F:168`).

Bulk-related definitions in `def_his.F`:
- `idTsur(itemp)` — surface tracer heat flux (`:5109`).
- Latent/sensible/longwave (`:5141`).
- `Tair, rain, EminusP, swrad` (`:5219`).
- `sustr, svstr` (`:5352`).

Writes in `wrt_his.F`:
- `Pair, Tair, Uwind, Vwind` (`:1834`).
- `stflx` (`:1994`).
- Latent/sensible/longwave (`:2028`).
- `rain, EminusP, swrad` (`:2126`).
- `sustr, svstr` (`:2200`).

`Qair` is **input variable only** (`varinfo.yaml:2034`); no `Hout(idQair, ng)` history write path.

## Decision Guide

| Forcing source | Setup |
|---|---|
| ECMWF / NCEP reanalysis (full bulk inputs) | `BULK_FLUXES + COARE_30 + LONGWAVE_OUT + SOLAR_SOURCE` |
| Net-flux only (`stflux/swrad` precomputed) | No `BULK_FLUXES`; provide `stflux` directly |
| Berliand longwave (no `lwrad_down`) | `LONGWAVE` (clear-sky) |
| Cool-skin enhancement | `COOL_SKIN` |
| Wind-relative stress (with currents) | `relative_wind=T` |
| Coastal water (Jerlov II) | `SOLAR_SOURCE` with `Jwtype=2` (or 3) |
| Open ocean (Jerlov I/IA) | `SOLAR_SOURCE` with `Jwtype=1` |
| No solar penetration (all surface) | Skip `SOLAR_SOURCE` |
| Storm hindcast (spatially varying RH) | `Hair/Qair` from atmospheric model |

## Working Rules

- Bulk inputs typically from atmospheric model (e.g., ERA5, GFS) at 1-3 hour intervals.
- `LONGWAVE_OUT` is more accurate than `LONGWAVE` (Berliand) — use when downwelling longwave available.
- COARE iteration count fixed at 3; in tropical/equatorial regions, may want to extend (modify `IterMax`).
- For Korean coastal (Yellow Sea, East Sea): Jerlov II or III; output `srflx` to verify magnitude.
- Output `lhflx, shflx, lrflx, srflx` separately for energy budget audits.
- Cool-skin diurnal cycle visible in `delTc` output; ~0.1-0.3 K typical.
- Wind stress typically ~10⁻³ τ for U10=10 m/s; verify magnitudes.

## Common Pitfalls

- ▢ Setting `LONGWAVE` and `LONGWAVE_OUT` simultaneously — undefined; choose one.
- ▢ Missing `Qair` (specific humidity) — bulk fails; provide either `Qair` or `Hair` (relative humidity).
- ▢ `swrad` unit confusion — must be W/m² (not μmol photons / m² / s for radiation).
- ▢ Negative `stflux` interpreted as cooling — sign convention is positive into ocean.
- ▢ Expecting warm-layer correction — not implemented; use `COOL_SKIN` only.
- ▢ `BULK_FLUXES` with `relative_wind=T` but ocean current ~0 — same as raw winds; no harm.
- ▢ SOLAR_SOURCE with wrong Jerlov type — heat penetrates too deep / too shallow; calibrate against profiles.
- ▢ `Qair` not in history output — search code for `idQair` then add Hout entry if needed.

## Next expansion

- ERA5 → ROMS forcing recipe.
- Cool-skin diurnal cycle validation case.
- Jerlov water-type tuning vs MODIS.

## References

- Fairall et al. 1996 (COARE 3.0).
- Berliand & Berliand 1952 (longwave parameterization).
- Paulson & Simpson 1977 (solar penetration).
- Jerlov 1976 (water types).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
