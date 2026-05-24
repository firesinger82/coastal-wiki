---
title: "delft3d heat"
topic: general
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_heat.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

The actual `KTEMP` dispatch in `heatu.f90` (note: differs from older docs — KTEMP=1 absolute, =2 composite, =3 excess, =4 Murakami, =5 ocean/Proctor; **not the labels in some user manuals**). What each model computes (excess `hlc`, Murakami absolute with all radiation components + Bowen sensible + Berliand-style longwave + shortwave with Secchi extinction, ocean/Proctor with Dalton/Stanton bulk, composite using `qradin`), atmospheric input fields per `KTEMP` via `inctem/updtem`, temperature transport coupling (LSAL+1 ordering), and surface BC implementation as top-layer source/sink (NOT separate boundary). Use this when picking heat model for stratified case.

## Source basis

- `compute/heatu.f90:162-1276` — main heat routine.
- `main/z_trisol.f90:1159-1604` — dispatch.
- `timedep/inctem.f90:171`, `updtem.f90:189` — time-dep input.
- `timedep/windtostress.f90:141` — wind-magnitude.
- `flow2d3d_io/src/input/dimpro.f90:151`, `preprocessor/rdnamc.f90:93` — temp constituent ordering.
- `compute/difu.f90:695` — transport.

## Key finding (vs prompt)

Code in `heatu.f90` has actual dispatch:
- `KTEMP=1`: absolute heat budget, internal solar + atmospheric radiation (`heatu.f90:381`).
- `KTEMP=2`: similar absolute/composite, but incoming total radiation = `qradin` (`:510`).
- `KTEMP=3`: **excess-temperature** model (`:633`).
- `KTEMP=4`: **Murakami** heat model (`:716`).
- `KTEMP=5`: **ocean / Proctor bulk** (`:925`).

This may differ from manual labels — verify version.

## A. Dispatch

`z_trisol` updates heat time-series with `inctem` when `ktemp > 0` (`z_trisol.f90:1159`); later calls `heatu` for `ktemp > 0`, passing temperature index `ltem`, sources/sinks, concentrations `r0`, evaporation, depth, wind, pressure, geometry (`:1604`).

In `heatu`, all constituents looped, but heat exchange applies only to real temperature `l == ltem` or configured background-temperature constituents `flbcktemp(l)` (`heatu.f90:377`).

## B. Excess heat (KTEMP=3)

Heat-loss coefficient (`:655`):
```
hlc = 4.48 + 0.049·T + fwind·(3.5 + 2.05·W10)·(1.12 + 0.018·T + 0.00158·T²)
```
Optional `lambda` override.

Limited if `qtotmx` set: `qltemp = -hlc·(T - tback)` (`:667`).

Heat tendency:
```
dT/dt = -hlc·(T - tback) / (rho_w · Cp · h)
```

Implemented as source when `T <= tback`; source + implicit sink when `T > tback` (`:678`).

Sigma divides by top-layer thickness; Z multiplies by `gsqs` (`:691`).

Use for **simple lake/reservoir warm-up cases** with prescribed `tback` (background equilibrium temperature).

## C. Murakami absolute (KTEMP=4)

Components (`heatu.f90:747-826`):

**Latent heat**:
```
tl = 2.5e6 - 2.3e3·T  (vaporization latent heat)
qeva = 1.2e-9 · W10 · delvap · rhow · tl    (with keva options)
```

**Sensible** (Bowen ratio): `qco = bowrat · qeva` (`:796`).

**Longwave/back radiation**:
```
qbl = em · sigma_b · (0.39 - 0.058·sqrt(ea)) · TairK^4 · cloud
    + 4 · em · sigma_b · TairK^3 · (Twater - Tair)
```
(`:807`).

**Shortwave**: user `qsun` with albedo `qsn = qsun·(1-albedo)`; vertically attenuated with `extinc = 1.7/secchi` (`:826`).

So Murakami is the **full absolute heat budget** with all four components — most physically complete.

## D. Ocean / Proctor (KTEMP=5)

Computes solar from measured `qradin`, gridded `swrfarr`, or astronomy + cloud + albedo (`:996`).

Atmospheric pressure `presa = patm/100` (`:994`).

Vapor pressures + specific humidities (`:1055`).

Latent: `qeva = dalton · rhoa · W10 · (qw - qal) · tl` (`:1085`).

Sensible: `qco = stanton · rhoa · hcp · W10 · (Twater - Tair)` (`:1109`).

Optional free convection (`:1113`); infrared back radiation (`:1179`).

This is the COARE-style bulk model — preferred for open-ocean coastal applications.

## E. Composite (KTEMP=2)

Composite-style branch (`:590-594`):
- Evaporation, convection, back radiation as in `KTEMP=1`.
- Incoming radiation prescribed as total `qin = qradin`.
- Net flux: `qtot = (qin - ql) / (rho_w · Cp)` added to surface layer.

Use when measured total downward radiation available but want internal computation of other terms.

## F. Atmospheric inputs

Time-dependent via `inctem` (`:171`): RH, dry bulb, solar, total radiation, background temp, air temp, cloud, vapor pressure.

`updtem` maps required columns by `ktemp` (`updtem.f90:189`):

| `KTEMP` | Required inputs |
|---|---|
| `1` | RH, dry bulb, solar |
| `2` | RH, dry bulb, `qradin` |
| `3` | `tback` |
| `4` | RH, Tair, solar, vapor pressure |
| `5` | RH, Tair, cloud, optional `qradin` |

Spatial meteo files for `relhum, airtemp, cloud, swrf, Secchi_depth` fetched in `heatu` (`:325`).

Wind speed via `w10mag`; `windtostress` derives Stanton/Dalton from drag for lake mode (`windtostress.f90:141`).

## G. Temperature transport coupling

Temperature is **normal transported constituent**.

`dimpro` assigns salinity first when `Sub1` contains `S`, then temperature when contains `T`. **If salinity enabled, temperature = `LSAL+1`** (`dimpro.f90:151`).

Names: `salinity, temperature` order (`rdnamc.f90:93`).

Transport uses generic `r0/r1/sour/sink`; `heatu` adds heat to `sour/sink` at index `ltem` (`heatu.f90:162`).

`difu` treats `sour` explicitly, `sink` implicitly in scalar transport solve (`difu.f90:695`).

## H. Surface BC implementation

Surface heat BC **NOT separate boundary** — injected as **top-layer source/sink**.

Active surface layer: `kfsmx0(nm)` (Z-model) or `k0=1` (sigma) (`heatu.f90:396`).

Floating structures suppress heat exchange when `kspu/kspv == 2` (`:393`).

For absolute/bulk models: non-solar losses applied at top layer; **shortwave penetrates** through layers using Secchi extinction and per-layer `qink` (`:1211`).

Sigma: source terms ÷ layer thickness/depth.
Z: source terms × horizontal cell area `gsqs` (`:1222`).

## Decision Guide

| Application | KTEMP | Atmospheric inputs |
|---|---|---|
| Simple lake/reservoir warmup | `3` excess | `tback` (equilibrium temp) |
| Estuary with measured radiation | `2` composite | RH, Tair, `qradin` |
| Coastal with full ATM model | `4` Murakami | RH, Tair, solar, vapor pressure |
| Open ocean with COARE | `5` ocean/Proctor | RH, Tair, cloud, optional `qradin` |
| Idealized test | `1` absolute | RH, dry bulb, solar |
| Spatially varying weather | Use `swrfarr` (gridded) | + spatial Secchi for solar penetration |
| Korean coastal storm-surge | `5` ocean (most physical) | KMA observation |
| Reservoir with stratification | `3` excess + thermocline IC | + `lambda` if needed |

## Working Rules

- KTEMP=4 (Murakami) is most physically complete; use for production.
- KTEMP=3 (excess) is fastest; reasonable for quick warm-up tests.
- Solar penetration (Secchi) controls thermocline depth — calibrate Secchi vs MODIS-derived.
- Output `qsn, qbl, qco, qeva` (radiation components) for energy budget.
- For Korean coast: KTEMP=5 with ECMWF-style RH, Tair, cloud.
- Verify temperature constituent index = `LSAL+1` in case salinity is on.
- Stratification may require `KTEMP > 0` even for quick tests — temperature evolves naturally.

## Common Pitfalls

- ▢ Mixing KTEMP labels from manual vs code — verify with `heatu.f90` line numbers.
- ▢ Forgetting `Secchi_depth` for Murakami — solar penetration uniform; thermocline wrong.
- ▢ Missing `tback` for KTEMP=3 — default applies; usually wrong.
- ▢ KTEMP=5 without `qradin` — falls back to astronomy + cloud; less accurate.
- ▢ Temperature index confusion — `LSAL+1` if salinity on, else `1`.
- ▢ Hot-start across KTEMP change — heat budget inconsistent.
- ▢ Floating structure suppression (`kspu/kspv=2`) silently zeros heat exchange.

## References

- Murakami et al. (heat balance components).
- Proctor (ocean bulk).
- Sweers 1976 (Berliand longwave).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src`. Auto-draft = false; review_required = true.
