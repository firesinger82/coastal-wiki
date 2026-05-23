---
title: "efdc ice"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_ice.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

EFDC+ ice cover via `ISICE` flag (1=user-specified varying, 2=binary on/off, 3=fully heat-coupled, 4=heat-coupled+frazil transport — note **no `NCICE` symbol or `owi_ice` reader** in this tree), the heat-balance modifications under ice (skip open-water turbulent fluxes; solar attenuation `EXP(-GAMMAI*ICETHICK)`; ice surface temperature solver), ice momentum coupling via `TAUICE = -CDICE*sqrt(U²+V²)` replacing wind stress at ice cells, the absence of dynamic ice mechanics (no rheology/ridging/advection of solid cover), wave routines unaware of ice, and input file formats (`iser.inp`, `istat.inp`, `icemap.inp`, `ice.inp` for thermodynamic IC). Use this when configuring winter cases with ice cover, debugging anomalous wind stress under ice, or interpreting `ICECELL` skips.

## Source basis

- `input.f90:2524-2530, 6888-6911, 7000-7099` — `ISICE`, ice series readers.
- `mod_scaninp.f90:504-855` — input scanning.
- `Transport/mod_heat.f90:251-1490, 1095-1104, 641-753, 1322-1428, 1652-1674` — heat-balance + ice physics.
- `Transport/caltranice.f90:9-172` — frazil transport.
- `caltsxy.f90:612-864, 684-724` — ice cover application + momentum.
- `calpuv2c.f90:220-226`, `calpuv9c.f90:565-573` — momentum coupling.
- `calexp.f90:1091-1385`, `calexp2t.f90:1014-1405` — internal mode + waves.
- `Transport/calconc.f90:296-471` — heat/frazil dispatch.
- `Transport/calqvs.f90:1513-1539` — ice volume → QSUM.
- `Waves/mod_windwave.f90:191-826` — wave routines (no ice).
- `varalloc.f90:1386-1400` — ice arrays.

## A. Activation

**No `NCICE` symbol; no `owi_ice` reader** in this source tree.

Ice controlled by `ISICE` (read from card `C46A` at `input.f90:2524-2530`):
- `ISICE, NISER, TEMPICE, CDICE, ICETHMX, RICETHK0`.
- Also scanned in `mod_scaninp.f90:504-514`.

Wind forcing separate: `NWSER` is wind series count from `WSER.INP` (`input.f90:6888-6911`), **not an ice flag**.

## B. Ice cover dynamics modes

`Transport/mod_heat.f90:1095-1104` documents:

| `ISICE` | Mode |
|---|---|
| `1` | User-specified varying ice cover |
| `2` | Binary on/off cover |
| `3` | Fully heat-coupled (thermodynamic) |
| `4` | Heat-coupled + frazil ice transport |

`ISICE=1/2`:
- Reads external ice cover time series → `ICECOVER`.
- Thickness explicitly "not used" (`caltsxy.f90:612-704`).

`ISICE=3/4`:
- Thermodynamic freeze/melt.
- `ISICE=4` additionally transports frazil ice as tracer; accumulates into cover thickness (`Transport/caltranice.f90:9-172`).

**No dynamic ice mechanics** for ice velocity, rheology, ridging, or horizontal advection of solid cover.

## C. Heat balance

Open-water surface heat balance: longwave + sensible + latent fluxes — but **skipped when `ICECELL(L)` is true** (`Transport/mod_heat.f90:641-669`).

COARE heat exchange same skip pattern (`:699-753`).

**Solar through ice** attenuated:
```
sw_under_ice = sw_above · (1 - albedo_ice) · EXP(-GAMMAI · ICETHICK)
```
(`:1652-1674`).

**Ice surface temperature** solved from radiation, back radiation, evaporation, convection, conduction (`:1322-1343`).

**Ice-water interface** growth/melt: bottom ice conduction + water-interface melt/freeze (`:1385-1428`).

## D. Ice momentum

In ice cells, surface shear replaced by ice-bottom drag (`caltsxy.f90:713-724`):
```
TAUICE = -CDICE · sqrt(U² + V²)
```
Thickness-scaled and capped, then assigned to `TSX/TSY`.

`TSX/TSY` enters external momentum in `CALPUV` (`calpuv2c.f90:220-226`, `calpuv9c.f90:565-573`).

Also enters internal-mode top interface shear in `CALEXP` (`calexp.f90:1374-1385`, `calexp2t.f90:1400-1405`).

## E. Wind stress reduction under ice

Wind stress computed normally in `WINDSTRESS` (`caltsxy.f90:755-864`).

Then for `ICECELL(L)`, `TSX/TSY` **overwritten** by ice-bottom drag (`:713-724`).

Atmospheric wind stress effectively **removed** from ice-covered water; replaced with ice-water drag.

This is **not continuous partial-cover wind-stress scaling**. For `ISICE=1/2`, `ICECOVER` rounded to 0/1 before `ICECELL` set (`:684-699`).

## F. Wave dissipation under ice

**No ice-specific wave damping or `ICECELL/ISICE` logic in wave routines**.

Wind-wave generation uses wind, fetch, depth, wave mask only (`Waves/mod_windwave.f90:191-220`).

Wave dissipation from wave height/period; active checks are wave mask, height threshold, depth — **not ice** (`:730-746, 784-826`).

Wave forcing added to momentum via `FXWAVE/FYWAVE` (`calexp.f90:1091-1097`, `calexp2t.f90:1014-1019`).

So wave physics is **ice-blind** in this version. For ice-affected wave damping, externally process or skip wave coupling under heavy ice.

## G. Hydrodynamic coupling

Heat transport: `CALHEAT` called when temperature transport active (`Transport/calconc.f90:467-471`).

Frazil ice transport: called for `ISICE==4` (`:296-300`).

Ice freeze/melt volume changes → `ICERATE`, added to top-layer source/sink `QSUM(L,KC)` (`Transport/calqvs.f90:1513-1539`).

For 3-time-level mode, ice volume can directly update `HP, H1P`, layer depths (`Transport/mod_heat.f90:1480-1490`).

Momentum coupling via `TSX/TSY` into `CALPUV` and `CALEXP` (cited above).

## H. Input data

| `ISICE` | File | Format |
|---|---|---|
| `1` | `iser.inp` | `VAL(M,1)` = ice on/off or cover; `VAL(M,2)` = thickness (legacy/display only) (`input.f90:7000-7031`) |
| `2` | `istat.inp` | One time series of fractional ice cover, capped at 1 (`:7038-7054`) |
| Multiple | `icemap.inp` | Weights by cell + time map (`:7068-7099`); allocated/scanned `mod_scaninp.f90:839-855` |
| `>2` | `ice.inp` | Initial thermodynamic ice thickness (`mod_heat.f90:251-263`) |

Allocated arrays: `ICECOVER, ICETHICK, ICETEMP, ICEVOL, ICERATE`, frazil arrays (`varalloc.f90:1386-1400`).

## Decision Guide

| Application | `ISICE` |
|---|---|
| Observational ice cover from satellite/data | `1` (varying with time series) |
| Simple winter/summer toggle | `2` (binary) |
| Lake / reservoir thermodynamic | `3` (full heat-coupled) |
| River with frazil ice formation | `4` (with frazil transport) |
| Open ocean (no ice) | omit or `0` |
| Korean East Sea winter | `3` (rare); usually omit |
| Arctic / boreal lakes | `3` or `4` |
| Bay with seasonal ice | `1` from observation OR `3` thermodynamic |

## Working Rules

- `CDICE` (ice-water drag coefficient): typical 0.001-0.005.
- `GAMMAI` (under-ice solar attenuation): 1-3 m⁻¹ for clear ice; higher for snow-covered.
- `RICETHK0` (initial ice thickness for `ISICE>=3`): set realistic value to avoid spin-up.
- `ICETHMX` (max thickness cap): prevents unphysical accumulation.
- For `ISICE=1`, time series must cover entire run period; otherwise extrapolation.
- Wave coupling under ice is OFF in code logic; if needed, externally suppress or use `WINDWAVE` flag.
- For Korean coast: ice rare; if modeling Yellow Sea winter, `ISICE=1` from observation map.

## Common Pitfalls

- ▢ Looking for `NCICE` flag — doesn't exist; use `ISICE`.
- ▢ Looking for `owi_ice` reader — also not present.
- ▢ Setting `ISICE=1` with thickness expecting it matters — thickness ignored for modes 1/2.
- ▢ `ISICE=4` without IC `ice.inp` — model crashes or initializes at zero.
- ▢ Expecting ice mechanics (rheology, ridging) — not implemented.
- ▢ Wave dissipation under ice expected — not present in wave routines.
- ▢ Partial cover affecting wind stress proportionally — `ISICE=1/2` rounds to 0/1 first; binary effect.
- ▢ Hot-start across `ISICE` mode change — ice arrays inconsistent.

## Next expansion

- Korean Yellow Sea winter case study with `ISICE=1`.
- Ice transport `ISICE=4` validation against frazil observations.
- External wave-ice coupling alternatives.

## References

- Hibler 1979 (sea ice rheology — NOT in EFDC+).
- Mellor & Kantha 1989 (thermodynamic sea ice — concepts in EFDC+).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
