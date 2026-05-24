---
title: "roms grid metrics"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_grid_metrics.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How `SPHERICAL` (compile-time) and `spherical` NetCDF flag (runtime) interact, what metrics `pm, pn, dmde, dndx, pmask` mean and where they're used, the `fomn = f/(pm*pn)` Coriolis form, the canonical grid NetCDF (`grd_spherical.cdl`) variable layout, tile decomposition via `NtileI(ng) × NtileJ(ng)`, per-tile bounds via `get_tile`, MPI ghost-cell exchange via `mp_exchange*`, and the orthogonal `TS_DIF2/UV_VIS2` mixing options that consume metrics. Use this when configuring a curvilinear/spherical grid, choosing `NtileI/NtileJ` for MPI scaling, or understanding tile bounds in custom kernels.

## Source basis

- `checkdefs.F:2832` — `SPHERICAL` compile flag.
- `get_grid.F:2619-4272` — runtime grid file read.
- `grid_coords.F:91-216` — lon/lat → fractional indices (`hindices`).
- `mod_grid.F:36-263` — metric variables, `pm`, `pn`, `dmde/dndx`, `pmask`.
- `metrics.F:344-581` — `omn, fomn`, `pmask` derivation.
- `rhs3d.F:47-648` — metrics in momentum.
- `Data/ROMS/CDL/grd_spherical.cdl` — canonical grid NetCDF template.
- `mod_param.F:23` — `NtileI/J` definition.
- `read_phypar.F:369-5081` — `NtileI/J` reading and check.
- `tile_indices.F:11-143`, `get_bounds.F:777-1036` — tile bound computation.
- `tile.h:15-29` — tile-storage range definitions.
- `mp_exchange.F:2-849` — MPI exchange routines.
- `t3dmix.F:18`, `uv3dmix.F:18`, `t3dmix2_s.h`, `uv3dmix2_s.h` — mixing kernels.

## A. SPHERICAL flag

`SPHERICAL` is **compile-time** option (`checkdefs.F:2832`).

Runtime grid file also carries NetCDF `spherical` logical, required by `get_grid` (`:2619, 2758`).

For spherical grids:
- Reads `lon_rho/lat_rho` only when `spherical=T` (`:4211, 4272`).
- Cartesian `x_rho/y_rho` read as `xr/yr`, but nesting contact fill guarded with `.not.spherical` (`:3751-3850`).

Lon/lat → fractional grid indices via `hindices` (e.g., for floats, stations) (`grid_coords.F:91-216`).

## B. Curvilinear metrics

Definitions in `mod_grid.F`:
- `pm` = inverse XI grid spacing = `m` metric (`:63`).
- `pn` = inverse ETA grid spacing = `n` metric (`:69`).
- Stored as `GRID(ng)%pm`, `GRID(ng)%pn` (`:220`).
- `dmde, dndx` = curvature terms (compile-time `CURVGRID && UV_ADV`) (`:36, 194`).
- `pmask` = PSI-point slip/no-slip mask (`:76, 263`).

Metrics in momentum RHS (`rhs3d.F`):
- `dmde/dndx` curvature added (`:631, 648`).

`pmask` derivation: from surrounding `rmask` in `metrics` (`:522, 535, 581`).

## C. fomn = f/(pm*pn)

Documented as `f/(pm*pn)` at RHO points (`mod_grid.F:41`).

Computation (`metrics.F:344-373`):
```
omn = 1/(pm*pn)
fomn = f * omn
```
Then exchanged across tile halos.

3D Coriolis term uses `Hz * fomn` (`rhs3d.F:562-570`).

## D. Grid NetCDF format

Canonical template: `Data/ROMS/CDL/grd_spherical.cdl`.

C-grid dimensions (`:3`):
- `xi_psi, xi_rho, xi_u, xi_v`.
- `eta_psi, eta_rho, eta_u, eta_v`.

Core variables:
- `spherical` (logical) (`:15`).
- `xl, el` (domain bounds) (`:29`).
- `h` (bathymetry) (`:33`).
- `f` (Coriolis) (`:37`).
- `pm, pn, dndx, dmde` (metrics) (`:45`).
- Both Cartesian (`x_rho`, `y_rho`) and spherical (`lon_rho`, `lat_rho`) coordinates (`:53-77`).
- Masks: `mask_rho, mask_u, mask_v, mask_psi` (`:113`).

## E. Tile decomposition

`NtileI(ng), NtileJ(ng)` set XI/ETA tile counts (`mod_param.F:23`).

Read from physical input file (`read_phypar.F:369-372`).

In distributed mode, **`NtileI*NtileJ` must equal the number of PETs/tasks** (`:5043-5081`).

`tile_indices` sets decomposition bounds for every tile (`:11-143`):
- Loops `0:NtileI*NtileJ-1`.
- Calls `get_tile`.

## F. Per-tile domain bounds

`get_tile` computes non-overlapping physical bounds, then C-grid staggered bounds (`get_bounds.F:777-904`).

2D tile partition formula (`:1020-1036`):
```
ChunkSizeI = (Imax + NtileI − 1) / NtileI
ChunkSizeJ = (Jmax + NtileJ − 1) / NtileJ
(Itile, Jtile) = mapping from tile index
Istr/Iend/Jstr/Jend clipped to domain
```

Most kernels include `tile.h` (`:15-29`):
- Pulls `LBi/UBi/LBj/UBj` from `BOUNDS(ng)`.
- Defines private storage ranges from `Istr/Iend/Jstr/Jend`.

So **kernels operate on non-overlapping tiles** with halo regions for MPI exchange.

## G. MPI ghost exchange

`mp_exchange_mod` provides 2D/3D/4D tile halo exchanges (`mp_exchange.F:2-54`).

`tile_neighbors` builds rank table `(-1:NtileI, -1:NtileJ)` mapping adjacent tile ranks (`:73-123`).

Handles periodic wrap-around and ghost counts in EW/NS (`:155-230`).

`mp_exchange2d` workflow (`:290-610`):
1. Pack west/east boundaries.
2. Send via `mpi_irecv/mpi_send`.
3. Unpack into `Istr-m` and `Iend+m` ghost cells.

South/north analogous (`:654-849`).

## H. Mixing options (TS_DIF2, UV_VIS2)

Compile-time options:
- `TS_DIF2` → second-order harmonic tracer mixing.
- `UV_VIS2` → second-order harmonic momentum viscosity.

Dispatch in `rhs3d` (`:47-195`).

Orthogonal to grid geometry but **kernels use metrics**:
- `t3dmix.F:18` → `t3dmix2_*` under `TS_DIF2`.
- S-coordinate harmonic tracer kernel uses `pmon_u, pnom_v, pm, pn`; time-steps with `dt*pm*pn` (`t3dmix2_s.h:99-288`).
- `uv3dmix.F:18` → `uv3dmix2_*` under `UV_VIS2`.
- S-coordinate momentum kernel uses `pm, pn, pmon_*, pnom_*`; metric-scaled fluxes (`uv3dmix2_s.h:125-296`).

For biharmonic mixing: `TS_DIF4, UV_VIS4` (similar pattern, fourth-order).

## Decision Guide

| Configuration | Setup |
|---|---|
| Global / regional spherical | `SPHERICAL` CPP, `lon_rho/lat_rho` in grid file |
| Idealized Cartesian | No `SPHERICAL`, `x_rho/y_rho` only |
| Curvilinear regional | `CURVGRID, UV_ADV`, provide `dndx/dmde` |
| Open ocean tile decomposition | `NtileI×NtileJ ≈ #cores`; aspect ~`Lx/Ly` |
| Korean coastal nested | `NtileI=4, NtileJ=2` for 8-core; scale up linearly |
| MPI scaling test | Vary `NtileI/J` keeping product = #cores |
| Harmonic mixing (default) | `TS_DIF2, UV_VIS2` with `tnu2`/`visc2` from input |
| Biharmonic for resolved fronts | `TS_DIF4, UV_VIS4` with `tnu4`/`visc4` |

## Working Rules

- For Korean coast (~30°N): use `SPHERICAL` for accurate Coriolis distribution.
- `NtileI*NtileJ` must equal MPI rank count exactly — runtime check.
- For wide-shallow domains (e.g., shelf), use `NtileI > NtileJ` (more tiles in long direction).
- For tall domains (e.g., zonal coastline), `NtileJ > NtileI`.
- Ghost cell width: typically 2 (controlled by `Hadvection` order); higher for biharmonic mixing.
- Output `pm, pn, dmde, dndx, pmask` to history once for verification.

## Common Pitfalls

- ▢ Grid NetCDF without `spherical` variable — `get_grid` errors.
- ▢ `SPHERICAL` compiled but NetCDF says `spherical=F` — inconsistency.
- ▢ Setting `NtileI*NtileJ ≠ #ranks` — runtime abort.
- ▢ Curvilinear grid without providing `dndx/dmde` — `CURVGRID` compile fails or curvature missing.
- ▢ Periodic domain without periodic flags in input — exchange wraps unexpectedly.
- ▢ `UV_VIS2` thinking it's advection scheme — it's mixing; advection is separate.

## Next expansion

- Grid generation tooling reference (Pyroms, gridgen, SeaGrid).
- MPI scaling benchmark walkthrough.
- Curvilinear grid distortion check.

## References

- Shchepetkin & McWilliams 2005 (ROMS curvilinear).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
