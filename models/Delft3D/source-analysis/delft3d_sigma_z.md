---
title: "delft3d sigma z"
topic: general
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_sigma_z.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How Delft3D-FLOW switches between sigma and Z-layer vertical coordinates via the `Zmodel` flag, what `THICK` means in each, how Z-layer fixed levels handle surface/bottom drying via `KFSMIN/KFSMAX` and partial-thickness layers, the internal pressure-gradient differences (sigma anti-creep `dengra` vs Z `z_dengra`), the `ZTBML` near-bed layer modification, sigma vs Z mass conservation in advection/diffusion, and `KMAX` handling. Use this when choosing a vertical coordinate, debugging sigma slope-induced spurious mixing, or interpreting vertical-discretization-related errors.

## Source basis

- `flow2d3d_io/src/input/dimrd.f90:500-529, 328-345`, `rdxyzo.f90:258-330` — `Zmodel`, `THICK`, `Zbot/Ztop`, `MNKmax` parsing.
- `flow2d3d_data/include/procs.igs:51` — `Zmodel` doc.
- `flow2d3d_manager/src/tricom_step.F90:870-889` — runtime dispatch.
- `flow2d3d_kernel/src/inichk/inivol.f90:97-107`, `comvol.f90:95-99`, `layerdep.f90:75-96` — sigma volumes.
- `flow2d3d_kernel/src/inichk/z_inizm.f90:168-328`, `z_kfmnmx.f90:73-117` — Z-layer init, layer bounds.
- `flow2d3d_kernel/src/compute/z_drychk.f90:136-306` — Z runtime drying.
- `flow2d3d_kernel/src/compute/dens.f90:180-187`, `cucnp.f90:412-508`, `dengra.f90:213-403` — sigma internal pressure.
- `flow2d3d_kernel/src/compute/z_dengra.f90:42-131`, `z_cucnp.f90:473-476` — Z internal pressure.
- `flow2d3d_kernel/src/compute/sud.f90:932-937`, `difuvl.f90:353-411`, `difu.f90:578-604`, `z_sud.f90:329-954`, `z_difu.f90:362-558`, `z_updtvol.f90:94-96` — flux/diffusion forms.

## A. ZMODEL flag

Read from MDF in `dimrd`: default `.false.`, keyword `Zmodel`, `Y/y` sets true (`dimrd.f90:500-529`).

Global: "Z-model instead of sigma layers" (`procs.igs:51`).

Runtime dispatch in manager (`tricom_step.F90:870-889`):
- Sigma → `trisol`.
- Z-layer → `z_trisol` or `z_trisol_nhfull` for full non-hydrostatic.

## B. Sigma: THICK + free-surface following

Sigma layer thickness fractions read as `Thick` or `laydis` (`rdxyzo.f90:258-282`).

Cell volume + U/V areas scale with **total water depth `(s1 + dps)`** and `thick(k)`:
- `inivol.f90:97-107` (init).
- `comvol.f90:95-99` (runtime).

Layer depths scale with instantaneous depth (`layerdep.f90:75-96`):
- `dep(kmax+1) = dpd + wlev`.
- Sigma depths use `thick * (dpd + wlev)`.

This is the "sigma stretches with free surface" property — every layer thickness changes every step.

## C. Z-layer: fixed levels + surface/bottom drying

For Z-model, **`Zbot` and `Ztop` are required** after `Thick` (`rdxyzo.f90:295-330`).

Initialization converts `thick(k)` into fixed vertical grid heights over `abs(ztop − zbot)` (`z_inizm.f90:231-241`); cumulative fixed levels stored in `zk` (`:252-254`).

Z wet-layer bounds via `z_kfmnmx`:
- **Bottom layer `kfmin`**: where `zk(k)` reaches bed depth, with **partial bottom thickness** `dep + zk(k)` (`:73-77`).
- **Surface layer `kfmax`**: where `zk(k) + dzmin >= s1v`, with **partial top thickness** based on `s1v` (`:92-101`).
- Dry points zero all active layer thicknesses (`:111-117`).

During time stepping, `z_drychk` updates surface/bottom active ranges + layer thicknesses:
- Fully dry water cells: zero surrounding velocity masks, fluxes, `dzs1` (`z_drychk.f90:136-150`).
- New `kfsmax` from `s1` and `zk` (`:185-190`).
- New bed `kfsmin` from bed depth (`:198-200`).
- Recomputed `dzs1` gives partial single, bottom, surface, and interior layers (`:252-259`).

So Z-layer effectively has **partial-thickness top and bottom layers**, whose number changes as `s1` evolves.

## D. Internal pressure gradient

**Sigma** (`dens.f90:180-187`):
- Density-column integrals `sumrho` only computed when `.not. zmodel`.

Sigma baroclinic forcing in momentum (`cucnp.f90:492-508`):
- Uses `rho, sumrho, sig(k)`, left/right water depths.

**Anti-creep** density-Jacobian style routine (`dengra.f90:213-403`):
- Builds left/right sigma-interface elevations from `sig, thick, s0+dps` (`:213-225`).
- Merges/interpolates columns before computing gradients and density derivatives (`:229-403`).

Anti-creep is **important** for stratified flows over steep bathymetry — without it, sigma-coordinate spurious diapycnal mixing is significant.

**Z-model** (`z_dengra.f90:42-131`):
- Documented as "Fixed Layer Approach" (`:42`).
- Integrates horizontal density differences vertically over active fixed layers using `dzu0/dzv0` and `kfsz0` (`:96-110`).
- V direction similar (`:117-131`).

Z-momentum then uses `drhodx` directly (`z_cucnp.f90:473-476`).

Z-model's fixed-layer integration is naturally free of sigma-coordinate slope error.

## E. Hybrid coordinate

There is **no true sigma-Z hybrid coordinate switch** in this code. `Zmodel` is binary:
- `procs.igs:51` — "Z-model instead of sigma layers."
- `tricom_step.F90:870, 889` — `trisol` vs `z_trisol`.

`ZTBML` exists but is **not** a hybrid coordinate — it modifies near-bed Z-layer thicknesses for smoother bottom shear representation (`z_inizm.f90:318-328`); calls `z_taubotmodifylayers`.

## F. Bottom-following vs fixed-level advection / diffusion

**Sigma** horizontal fluxes use `hu/hv * thick(k)`:
- `sud.f90:932-937`.
- Scalar advection recovers velocity from `qxk/(guu*hu*thick)` and `qyk/(gvv*hv*thick)` (`difuvl.f90:353-411`).

**Z-layer** uses active-layer bounds and **real layer thicknesses** `dzu0/dzs0/dzv0`:
- Momentum: `z_sud.f90:329-368`.
- Z flux: `dzu0 * u1 * guu` (`:950-954`).

**Sigma vertical diffusion** uses sigma spacing:
- `tsg = 0.5*(thick(k) + thick(k+1))`.
- Scales by inverse total depth `h0i` (`difu.f90:578-604`).

**Z vertical diffusion** uses actual metric distance:
- `delz = 0.5*(dzs1(k) + dzs1(k+1))` (`z_difu.f90:529-558`).

So sigma is "metric per layer" with depth scaling; Z is "metric per layer" in physical units.

## G. Mass conservation for Z with drying surface

Z volumes recomputed from physical layer thickness:
- `volum1 = dzs1 * gsqs` (`z_updtvol.f90:94-96`).

In transport, Z initialization uses `volum1/timestep` on LHS, `volum0*r0/timestep` on RHS (`z_difu.f90:378-382`).

When surface layer count changes, **extra old/new layer mass is folded into remaining active layer** rather than discarded (`:362-371`); shrinking columns accumulate old mass from removed layers into `kmin` (`:384-389`).

`z_drychk` also copies concentration into newly-wetted top/bottom layers (`z_drychk.f90:293-306`).

This is the mass-conservation guarantee for Z with moving free surface + drying.

## H. KMAX handling

`kmax` from `MNKmax`, must be positive (`dimrd.f90:328-345`). `Thick` expects exactly `kmax` values (`rdxyzo.f90:266-277`).

Both sigma and Z allocate arrays with dimension `kmax`, but **Z allocates extra Z-specific arrays behind `kfacz`**:
- Real arrays: `esm_alloc_real.f90:150, 164, 204-206`.
- Integer arrays: `esm_alloc_int.f90:130-132`.

In sigma, loops generally run `1:kmax` because every column has all sigma layers active (`sud.f90:329, 932, 956`).

In Z, `kmax` is storage/global maximum, but **active loops use per-column `kfmin/kfmax` ranges** (`z_sud.f90:329, 446`; `z_difu.f90:532`; `z_drychk.f90:251`).

So Z runs are slightly more expensive for column-active layer iteration but skip dry layers naturally.

## Decision Guide

| Domain feature | Coordinate |
|---|---|
| Mild bathymetry, depth ratio < 5 | Sigma |
| Steep slope, canyon, abrupt shelf | Z-model (avoids sigma PGF error) |
| Surge over dunes (top of grid wets/dries) | Z-model with sufficient `Ztop` |
| Stratified estuary, mild bathymetry | Sigma + anti-creep automatic |
| Deep ocean + shallow shelf combined | Z-model |
| Idealized box, smooth bathymetry | Sigma (cheaper) |
| Storm overtop of seawall | Z-model |
| Sediment with sigma slope concerns | Z-model preferred |
| Near-bed roughness improvement | Z-model + `ZTBML` |

## Working Rules

- For sigma, `THICK` should be denser near surface and bottom (geometric or stretched) — uniform `thick=0.1` (10 layers) gives poor surface/bottom resolution.
- Z-model: `Ztop` should be ≥ max expected `s1` (e.g., MSL + storm surge + tide); `Zbot` ≤ min bathymetry.
- Z-model layer count: `kmax = 20–50` typical for coastal applications; more layers cost ~linearly.
- For Z-model with steep bathymetry, use `ZTBML` for smoother bottom roughness representation.
- Anti-creep is automatic for sigma; **don't** disable unless you're testing the difference (sigma slope error is strong in stratified canyons).
- Cold-start with sigma → restart as Z-model: not supported. Pick early.
- Hybrid coordinates not supported in this version — use Z-model if you need fixed levels in part of the domain (entire domain becomes Z).

## Common Pitfalls

- ▢ Setting `Zmodel=Y` then forgetting `Ztop/Zbot` — model halts.
- ▢ Z-model with `Ztop` lower than max wave + tide — top layer stuck dry; surface boundary not reaching surface.
- ▢ Sigma model with very steep bathymetry expecting clean stratification — sigma slope error gives spurious diapycnal mixing.
- ▢ Treating `THICK` as physical thickness in sigma — it's a fraction; physical thickness = `thick * (s1 + dps)`.
- ▢ Z-model with `dzmin` too small — partial thin layers cause CFL violation.
- ▢ Looking for hybrid coordinate `Zsigma` — doesn't exist; pick one.
- ▢ Confusing `ZTBML` (near-bed layer modification) with hybrid coordinate — it's a refinement only.

## Next expansion

- Sigma vs Z-model benchmark on canyon test case.
- `ZTBML` calibration for bottom-shear sensitive sediment cases.
- Anti-creep `dengra` deep-dive.

## References

- Phillips 1957 (sigma coordinate baseline).
- Stelling & Van Kester 1994 (anti-creep correction).
- Bijvelds 2001 (Z-model implementation).
- Delft3D-FLOW Theory Manual.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src`. Auto-draft = false; review_required = true.
