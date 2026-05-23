---
slug: roms_nesting
title: ROMS Nesting (one-way, two-way, contact regions, refinement / composite / mosaic)
model: roms
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/roms/source_code/roms
---

## Scope

How ROMS sets up nested grids, what a contact region is, how parent→child (one-way) and child→parent (two-way) data flows are sequenced, where time-stepping is coordinated across grids, and where to find runnable examples. Use this when configuring telescoping nests, debugging mass-flux mismatches at refinement boundaries, or generating contact-NetCDF files.

## Source basis

- `ROMS/Include/cppdefs.h:557-562` — `NESTING`, `ONE_WAY`, `NESTING_DEBUG`, `TIME_INTERP_FLUX`.
- `ROMS/Utility/set_contact.F` — contact-region construction from contact NetCDF.
- `ROMS/Nonlinear/nesting.F` — runtime exchange (`get_refine`, `do_twoway`, `fine2coarse`, `correct_tracer`, `check_massflux`).
- `ROMS/Nonlinear/main3d.F:194-1122` — nested time-stepping orchestration.
- `ROMS/External/roms_dogbone_refined.in`, `roms_dogbone_composite.in` — concrete examples.

## A. Nesting setup

- `cppdefs.h:557-562`:
  - `NESTING` — master switch.
  - `ONE_WAY` — disables fine-to-coarse feedback.
  - `NESTING_DEBUG` — extra diagnostics including mass-flux conservation checks.
  - `TIME_INTERP_FLUX` — time-interpolated boundary flux instead of stepwise hold.
- `set_contact.F:152-179` validates `Ngrids ≥ 2` and enforces `Ncontact = (Ngrids-1)*2`.
- Nest-type flags are read from contact NetCDF and propagated as runtime switches: `coincident`, `composite`, `mosaic`, `refinement` (`set_contact.F:259-279`).
- Runtime nesting structures: `ContactRegion(ibry,rg)`, `CompositeGrid(ibry,rg)`, `RefinedGrid(rg)` (`set_contact.F:2226-2254`).
- Under `NESTING`, model init **always** calls `set_contact` before stepping (`inp_par.F:193-201`).

## B. Contact-region matrix

The contact NetCDF (`NGCNAME = roms_ngc.nc` in input, `roms_test_chan.in:1134-1138`) carries:

| Field | Meaning | Code |
|---|---|---|
| `donor_grid` | Source grid index per contact region | `set_contact.F:295-313` |
| `receiver_grid` | Destination grid index | `set_contact.F:295-313` |
| `contact_region` | Region membership per point | `:411-433` |
| `on_boundary` | Which receiver edge each point belongs to | `:411-433` |
| `Lweight` | Bilinear weights, `nLweights=4` (mandatory) | `:496-506, 174-211` |
| `Qweight` | Quadratic weights, `nQweights=9` (optional, with `QUADRATIC_WEIGHTS`) | `:508-520` |

Weights split into `Rcontact` (rho-points), `Ucontact` (u-points), `Vcontact` (v-points). Generation tooling: typically `coawst` `make_contact.m` / `Contact.m` or the Python equivalent — the in-tree code only **consumes** the NetCDF.

## C. One-way (parent → child)

- `main3d.F:623-631` — for refined grids, each step calls `nesting(..., nputD)` to impose contact-zone values from donor snapshots.
- `main3d.F:1118-1122` — coarser donor grids call `nesting(..., ngetD)` after advancing, storing latest donor states for child interpolation.
- `nesting.F:2356-2373` — `get_refine` is called at donor step bottom so coarse snapshots are at `time(dg)` and `time(dg)+dt(dg)`, enabling child-time interpolation.
- `nesting.F:249-270` — refined-grid path separates donor extraction (`ngetD`) and child filling (`nputD`), with **free-surface first** ordering.
- Two donor times are maintained via `RollingIndex`/`RollingTime`; new donor sample stamped at `time(dg)+dt(dg)` (`nesting.F:2435-2449`).

## D. Two-way (child → parent)

- `nesting.F:284-330` — `n2way` branch:
  1. Optional tracer-flux correction (`correct_tracer`).
  2. `fine2coarse` for 2D state.
  3. `fine2coarse` for 3D state.
- `nesting.F:3047-3060` — `correct_tracer` adjusts coarse-grid tracer boundary values using refined accumulated horizontal tracer fluxes (mass-conservative feedback).
- `nesting.F:3462-3549` — `fine2coarse` replaces coarse interior with averaged fine values where fine is donor.
- `u2dbc_im.F:451-454`, `v2dbc_im.F:483-486` — nested U/V boundary branches impose donor mass flux on refined edges for volume/mass conservation intent.
- `NESTING_DEBUG` (`nesting.F:50-52`) enables explicit mass-flux conservation checking (`check_massflux`).

## E. Time-stepping coordination

- `main3d.F:194-221` — Stepping is structured as: kernel loop → nest-layer loop → step loop.
- `ntimesteps` sets per-layer step counts for the current interval.
- `main3d.F:225-236` — Each grid in a layer updates its own `nnew/nrhs/nstp` and clock.
- `nesting.F:986-1056` — `do_twoway` gates feedback timing using:
  - `RefineSteps` — number of fine substeps per coarse step.
  - `Telescoping` — multi-level refinement flag.
  - Layer order test (`il == nl`).
- `nesting.F:1062-1068` — `TwoWayInterval` is updated by `RefineSteps(ng)*dt(ng)` when exchange occurs.
- `set_contact.F:2308-2333` — `RefineSteps`, `RefineStepsCounter`, `TwoWayInterval` are allocated/initialized from refinement metadata.

## F. Boundary condition options (nesting-relevant)

- `Chapman_explicit` free-surface BC per edge (`zetabc.F:186, 345, 504, 663`).
- `Flather` 2D momentum BC per edge (`u2dbc_im.F:224`, `v2dbc_im.F:230`).
- `reduced` (Reduced Physics) 2D momentum BC per edge (`u2dbc_im.F:400`, `v2dbc_im.F:432`).
- `nested` edge BC path applies nesting flux constraints for refined-grid boundaries (`u2dbc_im.F:454`, `v2dbc_im.F:486`).
- Input syntax: per-edge ordering for `LBC(isFsur/isUbar/isVbar)` documented at `roms_test_chan.in:164-186`.

## G. Examples

| File | Configuration |
|---|---|
| `roms_test_chan.in` | Single-grid (`Ngrids=1`); shows nesting knobs but doesn't instantiate |
| `roms_test_head.in` | Single-grid; same |
| `roms_dogbone_refined.in` | **Concrete 2-grid refinement** (`Ngrids=2, NestLayers=2, GridsInLayer=1 1`); contact file `dogbone_ngc_refined.nc` |
| `roms_dogbone_composite.in` | **Concrete 2-grid composite** (`Ngrids=2, NestLayers=1, GridsInLayer=2`); contact file `dogbone_ngc_composite.nc` |

`contact.F` and `nesting_get_data.F` referenced in older docs are **not present** in this tree — relevant code is in `set_contact.F` and `nesting.F`.

## Decision Guide

| Goal | Setup |
|---|---|
| Coastal zoom inside basin model | Refinement, one-way (parent → child), `LBC(isFsur)=Chapman` + `LBC(isUbar)=Flather` on shared edges |
| Two-way coupled coastal-shelf | Refinement, two-way, `NESTING_DEBUG` on for first runs |
| Multi-tile non-overlapping domains | Composite, `NestLayers=1, GridsInLayer=N` |
| Telescoping nests (3 levels) | Multiple layers, `RefineSteps` aligned with each level's `dt` |
| Want mass conservation guarantee | Two-way + verify with `NESTING_DEBUG` `check_massflux` output |
| Diagnose noisy fine-coarse interface | Turn on `TIME_INTERP_FLUX`; check `Lweight` interpolation order in NGC file |

## Working Rules

- Always start with one-way + `NESTING_DEBUG`. Verify mass conservation before enabling two-way.
- Refinement ratio: 3:1 or 5:1 odd is preferred; 2:1 works but staggered grid alignment is more delicate.
- Child `dt` ratio should match `RefineSteps`. Mismatch causes time-interpolation artifacts at the boundary.
- For nesting, parent and child must use the **same** `Vtransform/Vstretching` — vertical interpolation across different `Hz` definitions is silently wrong.
- Contact NetCDF generation is fragile — build with the official tool (Matlab `Contact.m` or Python port), don't hand-edit.
- For two-way, child grid must contain a buffer of cells inside the parent (typically 4+ cells from boundary) — `fine2coarse` averages over this region.

## Common Pitfalls

- ▢ Mismatched `Vtransform` between parent and child — silent vertical-coordinate corruption.
- ▢ Refinement ratio not power-of-prime (e.g., 4:1) — interpolation weights become singular at corners.
- ▢ Two-way enabled without verifying mass conservation in one-way first — feedback amplifies errors.
- ▢ Forgetting to add `NESTING` macro at compile time — model runs single-grid silently.
- ▢ Composite grids with overlapping interior — `Lweight` is undefined on overlap; use `mosaic` (non-overlapping) or `refinement`.
- ▢ Updating the parent forcing files but forgetting child forcing files — child runs with stale boundary data with no error.

## Next expansion

- Tooling note: contact NetCDF generation workflow (`Contact.m`, COAWST tooling, Python alternatives).
- Telescoping example walkthrough (3-level nest).
- Two-way performance/scaling benchmarks.

## References

- Debreu et al. 2012 (AGRIF nesting concepts).
- Penven et al. 2006 (ROMS nesting AGRIF).
- COAWST manual (Warner et al.) for contact-region tooling.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
