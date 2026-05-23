---
title: "delft3d drying flooding"
topic: general
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_drying_flooding.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How Delft3D-FLOW handles drying/flooding: the legacy `Dryflp` keyword vs current `Dpsopt` (and the fact that `Dpsopt` wins when both present), what `MEAN/MAX/MIN/DP` actually compute (`nfltyp` 1-4), how `Dryflc` and `DCO` are used, the role of `KFU/KFV/KFS` masks (geometric vs dynamic), how mass conservation is enforced at the front via `drychk`, the differences between sigma and Z-layer drying (including `KFSZ, KFUZ, KFSMIN, KFSMAX`), and the ADI iteration sequence with up to multiple `sud` repeats. Use this when configuring tidal-flat domains, debugging mass loss at the front, or interpreting `KFS` time series.

## Source basis

- `flow2d3d_io/src/input/rdnum.f90:368-468` — `Dryflp/Dpsopt`, `Dryflc`, `Drycrt`, `Dco` reads.
- `flow2d3d_kernel/src/inichk/caldps.f90:111-195` — `dpsopt` → `nfltyp` mapping.
- `flow2d3d_io/src/input/ck_dpopt.f90:180-189` — accepted `dpsopt` values.
- `flow2d3d_kernel/src/compute/upwhu.f90:126-163` — DCO and upwind reconstruction.
- `flow2d3d_kernel/src/inichk/chkdry.f90:139-399` — initial KFU/KFS, KFS recompute.
- `flow2d3d_kernel/src/inichk/chkkc.f90:171-403` — KCU/KCV setup.
- `flow2d3d_kernel/src/compute/checku.f90:120-132` — runtime KFU drying/flooding.
- `flow2d3d_kernel/src/compute/drychk.f90:120-156` — `KFS` recompute, isolation of dry cells.
- `flow2d3d_kernel/src/compute/adi.f90:360-428` — sigma ADI iteration.
- `flow2d3d_kernel/src/compute/z_drychk.f90:136-264`, `z_inizm.f90:185-193, 168-169` — Z-model drying.
- `flow2d3d_kernel/src/compute/z_adi.f90:391-466` — Z ADI iteration.
- `flow2d3d_kernel/src/compute/z_hormom_mdui.f90:191-201`, `taubot.f90:406-414` — cut-cell.
- `flow2d3d_kernel/src/compute/sud.f90:345-363` — `tetau` upwind weight.

## A. Dryflp vs Dpsopt

- `Dryflp` is **legacy**, now read into `dpsopt` for backward compatibility (`rdnum.f90:368-380`).
- If both `DRYFLP` and `DPSOPT` are present, **`DPSOPT` wins** (`:384-391`).

Dispatch by `dpsopt` in `caldps`:

| `dpsopt` | `nfltyp` | Behavior |
|---|---|---|
| `MEAN` | `1` | Default; `dps` from arithmetic mean of corner depths |
| `MAX` | `2` | `dps` from max → encourages drying (conservative for inundation extent) |
| `MIN` | `3` | `dps` from min → encourages flooding |
| `DP` | `4` | Direct depth value, no averaging |

Reference: `caldps.f90:111, 142, 168, 195`.

`ck_dpopt` allows `MEAN/DP/MAX/MIN`, **not `NO`** (`:180-189`). Runtime branches for `nfltyp==0` (no drying/flooding repeat) exist but no current `caldps` path sets `nfltyp=0` (`adi.f90:417-422`).

## B. Dryflc and DCO

`Dryflc`: drying/flooding threshold (`rdnum.f90:410-412`).

`Drycrt`: defaults to `0.5*dryflc`; capped at `dryflc` (`:418-434`). This is the trigger for **drying** (vs `Dryflc` for flooding).

`Dco`: marginal depth for smoothing/upwind behavior near dry points (`:442-468`).

`upwhu` applies upwind water-level/depth reconstruction when (`upwhu.f90:126-163`):
- `HU < DCO`.
- Structures present.
- `DPUOPT='UPW'`.
- Z-model active.

## C. KFU/KFV velocity-point activation

Initial `KFU/KFV` copied from geometric masks `KCU/KCV` (`chkdry.f90:139-148`); restart can preserve them. Z-model equivalent at `z_inizm.f90:185-193`.

Runtime drying:
- `KFU = 0` when active `HU < drycrt` (`checku.f90:120-132`).
- Reopens `KFU = 1` when `HU` and adjacent water level both exceed `dryflc`.
- `KFV` uses same routine with `icx` swapped by callers.

So **drying** uses `drycrt` (smaller), **flooding** uses `dryflc` (larger) — gives hysteresis.

## D. KFS / KCU / KCV cell activation

`KCU/KCV` are **static** geometry/connectivity masks set from active rows/columns and obstacles/thin dams (`chkkc.f90:171-403`).

`KFS` is **dynamic** — recomputed from surrounding velocity masks:
```
KFS = max(KFU east/west, KFV north/south)
```
(`drychk.f90:152-156`; init at `chkdry.f90:379-399`).

So `KFS` is "any of my four faces is open" — cell is hydraulically active if any face flows.

## E. Mass conservation at the front

When a water-level point becomes dry, `drychk` isolates it by zeroing all four adjacent velocity masks **and** the adjacent `qxk/qyk` fluxes (`drychk.f90:120-132`).

ADI then **repeats `SUD`** if drying occurred and `nfltyp/=0` (`adi.f90:422-428`).

This is the front-conservation mechanism: no flux through newly dry faces, and the continuity solve is rebuilt with the isolated cell.

## F. Sigma vs Z-layer drying

**Sigma**:
- Uses 2D masks + layer fractions.
- Fluxes: `guu*hu*thick*u1`, `gvv*hv*thick*v1` (`chkdry.f90:369-376`).

**Z-model**:
- Has vertical wet/dry masks: `KFSZ, KFUZ, KFVZ`.
- Min/max layer arrays: `KFSMIN, KFSMAX`.
- `z_drychk` zeroes vertical masks/fluxes for dried cells, recalculates `KFSMIN/KFSMAX`, `KFSZ1`, `DZS1` (`z_drychk.f90:136-264`).
- Minimum z-layer thickness tied to `0.1 * Dryflc` (`z_inizm.f90:168-169`).

Z-model thus tracks per-layer wet/dry status, allowing partial-column drying (top-to-bottom) — important for surge over dunes and step-bathymetry cases.

## G. Cut-cell handling

Cut-cell support (`kcscut`) is present in **z-model momentum/roughness handling**, not in core wet/dry decision.

Examples:
- `z_hormom_mdui` detects `kcscut` for staircase boundaries; recomputes cross velocity averaging (`z_hormom_mdui.f90:191-201`).
- `taubot` includes z-model `kcscut` in actual-average condition (`taubot.f90:406-414`).

This refines momentum balance near angled coastlines but does **not** replace the wet/dry algorithm.

## H. Iteration sequence

**Sigma ADI** (`adi.f90:360-428`):
1. `sud` solve.
2. `drychk`.
3. Recompute volumes.
4. Synchronize dry status.
5. Repeat `sud` if a point dried.

**Z ADI** (`z_adi.f90:391-466`):
1. `z_sud`.
2. `z_drychk`.
3. `z_drychku` for U/V geometry.
4. Volume update.
5. Repeat if dry.

Upwind weights effectively frozen before continuity solve: `sud` computes `tetau` from `s0, umean, DCO`, structures, and `DPUOPT` before momentum/continuity (`sud.f90:345-363`).

## Decision Guide

| Domain feature | Setting |
|---|---|
| Tidal flats with regular wet/dry | `Dpsopt=MEAN`, `Dryflc=0.05–0.1 m`, `Dco=0.1–0.5 m` |
| Steep tidal channels | `Dpsopt=MAX` for conservative inundation extent |
| Wide flat areas with shallow flooding | `Dpsopt=MIN` for early flooding |
| Idealized depth from grid | `Dpsopt=DP` |
| Stepped bathymetry (Z-model) | Z-model + `Dpsopt=MAX` |
| Cut-cells for angled coastline | Z-model + `kcscut` flag (auto in newer versions) |
| Storm surge over dunes | Z-model with cut-cells, `Dryflc=0.05` |
| Validate mass closure | Output `KFS, qxk, qyk`; verify `dh/dt` matches flux divergence |

## Working Rules

- **Avoid `Dryflp` keyword** — use `Dpsopt` directly. Legacy `Dryflp=NO` is no longer accepted.
- `Drycrt` is auto half of `Dryflc` — explicitly set if you want different hysteresis.
- `Dco` at ~0.1 m smooths the velocity reconstruction near drying — too small (~0.01) causes oscillations; too large (~1 m) over-smears.
- For sigma model, drying repeats `sud`. Number of repeats reported in log; >5 means timestep too large.
- Z-model partial-column drying needs `Ztop` set above maximum expected water level — undersized → top layer stuck dry.
- Watch `KFS=0` at unexpected cells — usually missing connectivity in `KCU/KCV` (thin dam, obstacle).
- `dpsopt=MAX` is conservative for flood mapping (less water gets in); `MIN` is conservative for outlet design (more water flows out).

## Common Pitfalls

- ▢ Setting `Dryflp=NO` — silently fails; current code only accepts `MEAN/MAX/MIN/DP`.
- ▢ `Dryflc=0.01` (very small) — flickering wet/dry; expensive ADI repeats; mass not actually lost but performance suffers.
- ▢ Z-model with `Ztop` ~ MSL — first surge event hits top of grid; partial column saturates.
- ▢ Hot-start with different `Dpsopt` than cold run — `nfltyp` mismatch; `dps` field inconsistent.
- ▢ Not checking ADI repeat count — silent pathology when `>10` repeats per step; usually CFL violation.
- ▢ Cut-cells expected to fix wet/dry oscillations — they don't; they fix momentum at angled boundaries only.
- ▢ Monitoring `KCU/KCV` for drying — those are static; use `KFU/KFV/KFS`.

## Next expansion

- Z-model partial-column conservation walkthrough.
- DPSOPT comparison on identical tidal-flat case.
- ADI iteration count diagnostics.

## References

- Stelling 1984 (semi-implicit ADI baseline).
- Casulli & Stelling 1998 (drying/flooding in shallow-water solvers).
- Delft3D-FLOW Theory Manual (Deltares).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d/packages/flow2d3d_kernel/src`. Auto-draft = false; review_required = true.
