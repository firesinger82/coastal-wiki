---
slug: delft3d_part
title: Delft3D-PART (delpar, particle types, .hyd offline coupling, advection + random walk)
model: delft3d
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/part
---

## Scope

Delft3D-PART (`delpar` executable + part_kernel/part_io/part_data libraries): particle types (tracer, oil with floating/dispersed/sticking, red tide, 2D/3D temperature, probabilistic density-driven settling, ABM), **offline coupling** via FLOW's `.hyd` file (volumes, flows, pointers, areas), `part10` analytical advection from face velocities (linear interpolation in cell), random walk via `ldiffh/ldiffz/ioptdv` with constant or VDF-file diffusivities, particle status encoded in position/layer/mass (no enum), multi-substance + decay (`exp(-decays·idelt/86400)` per timestep), output formats (NEFIS map/his + binary tracking `trk-*`). Use this when wiring oil-spill, conservative tracer, or larvae transport offline-coupled to FLOW.

## Source basis

- `delpar/main.f90:24-104`, `part_kernel/delpar.F90:24-443` — entry.
- `part_data/m_part_modeltypes.f90:28` — particle types.
- `part_io/rdpart.f90:202-1820`, `rdfnam.f90:117-212`, `rdhyd.f90:35-152`, `rdhydr.f90:145-239` — input.
- `part_kernel/part10.f90:35-1673`, `part03.f90:47-175`, `part08.f90:67-72`, `part17.f90:36-92` — kernel.
- `part_kernel/fm_reconst_vel.f90`, `fm_update_particles.f90` — FM/unstructured.
- `part_data/partmem.f90:69-238` — memory.
- `part_io/part12.f90:43-226`, `part13.f90:45`, `parths.f90:61`, `writrk.f90:42-49`, `wrttrk.f90:37-168` — output.

## A. Top level

PART is `delpar` executable + shared kernel/I/O/data libraries.

Executable resolves `.inp` from CLI or `runid.par`; calls `delpar(filename)` (`delpar/main.f90:24-104`).

Main steering: `m_delpar::delpar` — "main steering module for the 3d discrete particle model" (`part_kernel/delpar.F90:24-43`).

Branches:
- `partfm` for unstructured/FM hydrodynamics.
- Otherwise: regular curvilinear path — read grid, hydro, PART input; init releases; loop over time (`:129-337`).

## B. Particle types

Integer constants (`m_part_modeltypes.f90:28`):
- Tracer.
- Two-layer temperature.
- Red tide.
- Oil.
- 2D/3D temperature.
- Probabilistic density-driven settling.
- ABM.

Reader documents same menu including oil, density settling, ABM (`rdpart.f90:202-209`).

**Oil special**: `modtyp == model_oil` sets `oil, oil2dh, oil3d` flags (`delpar.F90:195`). Requires at least floating, dispersed, sticking substances per fraction (`rdpart.f90:374-382`).

**Conservative tracer** = `case (1)`; intentionally **no water-quality process step** (`delpar.F90:443-445`).

## C. Hydro forcing (offline-coupled)

PART is **offline-coupled** through hydrodynamic files.

`rdfnam` reads PART `.inp`; `.hyd` filename is in PART input → loaded into `fnam(18)` → metadata via `read_hyd/read_hyd_init` (`rdfnam.f90:117-195`).

`.hyd` provides `.lga, .lgt, .cco, .vol, .flo` filenames (`:212`).

`rdhyd` parses `.hyd`: conversion timestep, WAQ layers, hydro layers, pointers, vertical diffusion, shear stress, salinity, temperature files (`rdhyd.f90:35-152`).

Runtime hydro reading: `rdhydr` opens volume + flow, optional VDF/tau/salinity/temperature; reads two records initially; uses `parttd, dlwqfl, dlwqbl` for time updates (`rdhydr.f90:145-239`).

So PART runs **after** FLOW; reads its output; not real-time coupled.

## D. Advection / interpolation

For regular grid: `part10` is main motion routine — "calculates particle motion from advection, dispersion and settling" (`part10.f90:35-56`).

`part03` converts flows + volumes to velocities + depths before particle update (`part03.f90:47-175`).

Velocity interpolation = component-wise linear inside cell:
```
vx = vx0 + xp · vvx
vy = vy0 + yp · vvy
vz = vz0 + zp · vvz
```
Then step integrated analytically with exponential/linear formulas depending on local gradients (`part10.f90:1017-1125`).

On FM/unstructured: velocity reconstructed in triangular cells from edge-normal velocities with linear gradient `alphafm`; evaluated at particle position (`fm_reconst_vel.f90:37-172, fm_update_particles.f90:188`).

## E. Random walk diffusion

Horizontal in `part10`: if `ldiffh`, computes spreading scale, adds two uniform random deviations `dax, day` using `rnd(rseed)` (`part10.f90:644-652`).

Vertical: controlled by `ldiffz` and `ioptdv`; supports constant, algebraic, file-based VDF; computes `dvz` from `sqrt(disp · itdelt) · random` (`:747-791`).

So vertical can use:
- Constant.
- Algebraic from depth/wind.
- VDF time series file (from FLOW output).

## F. Particle status

**No single enum** — status encoded by position/layer/mass.

Inactive/dead: particle outside active cell reset to `(1,1,1)`; all substance weights zeroed (`part10.f90:539-545`).

Settled: `kpart = layt + 1` when settling into bed; erosion can return to bottom active layer (`:737, 851-853`).

Beached/stuck: mass transferred from mobile substances to `mstick` target when hitting land/bottom (`:1394-1483`).

Decayed: reduces `wpart`; fully decayed = near-zero mass (no separate flag) (`:1671`).

## G. Multi-substance + decay

`nosubs` = number of substances. `wpart(nosubs, npmax)` stores per-particle mass/weight.

Release arrays carry mass per substance (`partmem.f90:69-238`).

`part08` computes mass per particle per substance for instantaneous + continuous releases (`part08.f90:67-72`).

**Decay**: time series in `decay(nosubs, idtset)` interpolated by `part17`.

Per-timestep factor:
```
exp(-decays(isub) · idelt / 86400)
```
Applied to every substance weight in every active particle (`rdpart.f90:1820-1827, part17.f90:36-92, part10.f90:468-1673`).

## H. Output formats

- **Map** (`part12.f90:43-226`): "MAP FILE FOR CURVILINEAR GRID (Nefis and binary / per timestep)"; generates `map-...` files.
- **Plot grid** (`part13.f90:45`): "PLO FILE FOR PLOT GRID".
- **History** (`parths.f90:61`): "HISTORY FILE (*.his)".
- **Particle tracking** (NEFIS `trk-*`):
  - `writrk` writes initial `trk-const` group (`writrk.f90:42-49`).
  - `wrttrk` writes time-varying track groups: `XYZTRK, WPART, TRACK` (`wrttrk.f90:37-168`).

## Decision Guide

| Application | Setup |
|---|---|
| Conservative tracer (dye) | `modtyp=1` (tracer); no decay |
| Oil spill | `modtyp=oil`; floating + dispersed + sticking substances |
| Coliform / pathogen | Tracer + decay rate |
| Larvae transport | Tracer + vertical migration via `ldiffz` |
| Sediment particles (probabilistic) | Probabilistic density-driven settling type |
| Red tide / HABs | Red tide type |
| Temperature tracer | 2D or 3D temperature type |
| Multi-fraction oil | Multiple oil fractions, each with floating/dispersed/sticking |
| Unstructured FM grid | `partfm` path automatic |
| Korean coast oil spill | Oil with KMA wind drift, Korean current via FLOW `.hyd` |

## Working Rules

- PART runs **after** FLOW; ensure `.hyd` covers your simulation period.
- Volume + flow records in `.hyd` must be monotonic; PART interpolates linearly.
- Random seed: set explicitly for reproducibility.
- Particle count: 10K-100K typical; cost scales linearly.
- For Korean oil-spill, KMA wind direct input + FLOW current via `.hyd`.
- Output frequency: `map` for spatial, `his` for monitoring stations, `trk` for individual tracks.
- Decay rate in 1/day units (converted to per-timestep internally).
- Settling velocity in m/s (positive downward).

## Common Pitfalls

- ▢ Running PART without first running FLOW — no `.hyd` to read.
- ▢ FLOW `.hyd` time period shorter than PART simulation — PART extrapolates last record.
- ▢ Oil without all three substances (floating, dispersed, sticking) — runtime error.
- ▢ Conservative tracer with decay rate — invalidates "conservative" assumption.
- ▢ Looking for status enum — encoded in position/layer/mass; check `kpart, wpart`.
- ▢ FM grid running on regular kernel — wrong velocity reconstruction; use `partfm` branch.
- ▢ VDF file from FLOW with different time stepping than PART — interpolation gaps.

## References

- Suter & Stelling 1992 (Delft3D-PART).
- Visser 1997 (random walk).
- ASCE 1996 (oil-spill modeling).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/part`. Auto-draft = false; review_required = true.
