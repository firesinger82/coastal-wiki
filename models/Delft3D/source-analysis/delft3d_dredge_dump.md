---
title: "delft3d dredge dump"
topic: general
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_dredge_dump.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How Delft3D's Dredge-and-Dump (DAD) module is wired between FLOW and the shared morphology kernel, how scheduling works (time-table `active` flags, depth-threshold `DredgeDepth`, `MaxVolRate`), how sediment is removed from the bed administration (not the water column directly), how dump volumes are distributed (percentage / sequential / proportional), how multi-fraction dredging works, the `REMOVED FROM MODEL` outlet for unmodeled losses, and how output is logged. Use this when wiring a navigation channel maintenance run, designing a beach nourishment scheme, or auditing dredge-dump mass balance.

## Source basis

- `utils_gpl/morphology/packages/morphology_kernel/src/dredge.f90:30-37, 99-126, 176-1655` — core DAD module.
- `flow2d3d/packages/flow2d3d_kernel/src/compute_sediment/dredge_d3d4.f90:1-137` — FLOW wrapper.
- `flow2d3d/packages/flow2d3d_io/src/input/rddredge_d3d4.f90:59-62` — input wrapper.
- `flow2d3d/packages/flow2d3d_kernel/src/main/bott3d.f90:775-1285`, `z_bott3d.f90:1264-1267` — call sites.
- `utils_gpl/morphology/packages/morphology_io/src/rddredge.f90:258-1695` — input reader.
- `utils_gpl/morphology/packages/morphology_data/src/dredge_data_module.f90:58-227` — data structures.
- `utils_gpl/morphology/packages/morphology_kernel/src/dredge_comm.f90:13-18` — MPI / DD communicate.
- `flow2d3d/packages/flow2d3d_io/src/output/wrihisdad.f90`, `wrthisdad.f90`, `wrimapdad.f90` — output.

## A. Location and entry point

DAD is implemented in the **shared morphology kernel**, wrapped by FLOW:

| File | Role |
|---|---|
| `utils_gpl/morphology/packages/morphology_kernel/src/dredge.f90` | Core: module `m_dredge`, public `dredge` (`:30-37`) |
| `flow2d3d/packages/flow2d3d_kernel/src/compute_sediment/dredge_d3d4.f90` | FLOW wrapper `dredge_d3d4` (`:1`); calls core `dredge` (`:116-119`) |
| `flow2d3d/packages/flow2d3d_io/src/input/rddredge_d3d4.f90` | Reader wrapper, calls shared `rddredge` (`:59-62`) |

Runtime call sites:
- `bott3d.f90:1282-1285` — when `dredge` enabled.
- `z_bott3d.f90:1264-1267` — Z-model equivalent.

Initialization path: `tricom_init.F90:1095-1099` reads DAD input; `:1247` initializes partition data.

## B. Dredging scheduling

Two scheduling mechanisms: **time-table `active`** + **depth-threshold `DredgeDepth`**.

### Time scheduling (table-driven)

- `.dad` reader loads `General/TimeSeries` via `readtable` (`rddredge.f90:345-354`).
- Default `active` table binding read + checked (`:416-433`); per-area active table at `:804-823`.
- Runtime: `update_active_flags` chooses morphological time or hydrodynamic time using `TS_MorTimeScale` (`dredge.f90:176-180`), evaluates active table, sets `pdredge%active = values(1)>0` (`:188-200`).

### Depth-threshold scheduling

`DredgeDepth, Volume, MaxVolRate` parsed at `rddredge.f90:826-828`.

- If no `DredgeDepth` but rate given: sand-mining / fixed-rate dredging (`:841-847`).
- Otherwise: dredging to specified depth (`:849-856`).

Runtime threshold logic computes `z_dredge = reflevel − dredge_depth`, compares with `triggerlevel`, only triggers where sediment exists (`dredge.f90:514-551`).

### Trigger modes

Enums: point-by-point, all-by-one, all-by-average (`dredge_data_module.f90:58-63`).
- Legacy `TriggerAll, DredgeTrigger` read at `rddredge.f90:440-448, 938-953`.
- Runtime cases (`dredge.f90:514-645`): point/all-by-one (`:514-596`); average-trigger-all (`:597-645`).

### Rate limiting

- `MaxVolRate` converted from m³/year to m³/s (`rddredge.f90:859-860`).
- Runtime: `maxvol = maxvolrate * dt * morfac` (`dredge.f90:375-379`).
- Morph spinup or `morfac=0`: special handling (`:364-374`).

## C. Sediment sink (bed-only, not water column)

Dredging removes sediment from **bed administration**, not the water column directly:

- Dredge thickness stored in `dadpar%dzdred(nm)` (`dredge.f90:1154-1159`).
- Bed-composition sink: `gettoplyr(morlyr, dadpar%dzdred, dbodsd, ...)`. Comment: `dbodsd` is "kg/m² sediment removed" (`:1162-1167`).
- Volumes per fraction from `dbodsd / cdryb`; bed level `dps` updated (`:1175-1195`).

General suspended-sediment exchange uses `sinkse/sourse` (`bott3d.f90:775-776`), but DAD runs **later** as a bed operation (`:1282-1285`). DAD does **not** add/remove from concentration arrays directly.

## D. Dumping

Source material from `dadpar%voldred`, then assigned to dump areas as `dadpar%voldump`:

- Per-step dredged volume per fraction accumulated (`dredge.f90:1184-1187`).
- `distribute_sediments_over_dump_areas` (`:1202-1209`); cumulative totals (`:1231-1241`).

Distribution modes:

| Mode | Code | Behavior |
|---|---|---|
| Percentage | `:1243-1284` | `link_percentage * voldred` |
| Sequential | `:1286-1324` | Fills linked dump areas up to capacity |
| Proportional | `:1325-1365` | Uses dump capacity weights |

Actual dumping converts dump volume to deposit thickness:
```
dbodsd(lsed, nm) += dpadd * cdryb(lsed)
```
(`:1645-1655`); then updates `dps` (`:1657`).

The "rate" is **inherited from dredging volume rate**, not separate dump-rate. `MaxVolRate` limits source generation (`:375-379`); nourishment volumes from `percsupl * maxvol` (`:402-414`).

## E. Mass conservation

Within modeled dredge/dump links, volume is carried fraction-wise (`dredge_data_module.f90:211-227`):
- `voldred(ia, lsed)` — source.
- `voldump(ib, lsed)` — dump target.
- `link_sum` — cumulative transported.

- Percentage links: add `voltim*fracdumped` to both `link_sum` and `voldump` (`dredge.f90:1275-1279`).
- Sequential / proportional: allocate remaining `voldredged` into `voldump` (`:1300-1322, 1344-1363`).

### `REMOVED FROM MODEL` outlet

If dump capacity insufficient or percentages don't sum to 100, reader creates a **synthetic dump area** named `REMOVED FROM MODEL`:
- Outlet links created at `rddredge.f90:1512-1599`.
- Extra arrays allocated at `:1617-1629`.
- Named `REMOVED FROM MODEL` at `:1682-1695`.

Conservation is explicit in DAD accounting, but material can intentionally leave the physical model via this outlet.

## F. Coupling to morphology / MorMer

DAD is coupled **after** the normal morphology bed update:

1. `bott3d` computes normal `dbodsd`, calls `updmorlyr`, computes `depchg` (`bott3d.f90:1027-1088`).
2. Standard bed update (`:1112-1121`).
3. **DAD updates `dps` directly via `dredge_d3d4`** (`:1282-1285`).

For DAD dumping, FLOW updates bed composition again:
- `updmorlyr(gdmorlyr, dbodsd, dz_dummy, ...)` (`dredge_d3d4.f90:121-137`).
- Comment: this is sediment administration for dumping only; no actual bed update through `dz_dummy` (`:121-126`).

Cross-domain / MorMer-style merge uses `dredgecommunicate`:
- MPI: `dfreduce(..., dfsum, ...)`.
- Otherwise: `dd_dredgecommunicate` (`dredge_comm.f90:13-18`).
- Core calls for dump capacity + dredged volumes (`dredge.f90:99-126`).

## G. Multi-fraction dredge / dump

First-class support:

- `lsedtot` passed through DAD core (`dredge.f90:37-40`).
- `voldred(source, lsedtot+1)` — extra column for **non-modeled subsoil sediment** (`dredge_data_module.f90:220-221`).
- Links: `link_percentage(nalink, lsedtot)`, `link_sum(nalink, lsedtot)` (`:211-215`).

Reading:
- Per-fraction dump percentages by sediment name (`rddredge.f90:1057-1073`).
- Percentages assigned per fraction (`:1047-1055`).
- Nourishment per-fraction `SedPercentage`, must sum to 100% (`:1176-1188, 1246-1264`).

Runtime:
- Dredging accumulates `voldred` over all fractions (`dredge.f90:1184-1187`).
- Dumping applies `dbodsd` over all fractions (`:1652-1655`).

## H. Output / logging

**Input log** to `lundia`:
- DAD start/end (`rddredge.f90:258-260, 1614-1615`).
- Counts of dredge / dump / nourishment areas (`:723-725`).
- Per-area: depth, rate, distributions, dump targets (`:799-856, 887-923, 1312-1347`).

**HIS DAD** (history):
- Constant: area names, link definitions, percentages, distances (`wrihisdad.f90:130-188`).
- Time-varying: `LINK_SUM, DREDGE_VOLUME, DUMP_VOLUME, DREDGE_TFRAC, PLOUGH_TFRAC` (`wrthisdad.f90:143-213`).

**MAP DAD**:
- Integer masks for dredge + dump areas: `DREDGE_####, DUMP_####` (`wrimapdad.f90:135-181`).

## Decision Guide

| Application | Setup |
|---|---|
| Channel maintenance (e.g., harbor approach) | DAD with `DredgeDepth` per area, `active` table for seasonal restrictions, percentage distribution |
| Beach nourishment | Sand-mining (no `DredgeDepth`, fixed `MaxVolRate`), nourishment to dump area |
| Reservoir flushing | DAD with depth threshold, `REMOVED FROM MODEL` outlet for downstream loss |
| Multi-fraction dredge | `lsedtot > 1`, per-fraction dump percentages |
| Long-term simulation | Pair DAD with `morfac` acceleration; `MaxVolRate * morfac` is the effective rate |
| Quick equilibrium-state design | DAD off, only standard morphology |
| Cross-domain (DD) coupled dredge | `dredgecommunicate` handles automatically |

## Working Rules

- `MaxVolRate` is in **m³/year** in input — code converts internally. Don't pass m³/s.
- `morfac` multiplies effective dredge rate — adjust `MaxVolRate` if you don't want morfac amplification.
- `REMOVED FROM MODEL` outlet is silent — check `LINK_SUM` for outlet entries to detect mass leaving model.
- Per-area `active` table is in **hydrodynamic time** unless `TS_MorTimeScale=true` — make sure the units match.
- Dredge mass is removed bed-side; if you need water-column suspended sediment from dredge plume, use a separate source term — DAD does not generate it.
- Multi-fraction nourishment percentages **must sum to 100%** per area; reader checks and stops if not.
- For navigation depth maintenance, `triggerlevel` ≈ `DredgeDepth + 0.5 m` is a good buffer to avoid constant dredging at threshold.

## Common Pitfalls

- ▢ Setting `MaxVolRate` in m³/s — code expects m³/year; will be 31M× too small.
- ▢ Dump capacities don't cover dredge volume — `REMOVED FROM MODEL` outlet absorbs it silently.
- ▢ Per-fraction dump percentages don't sum to 100% — reader stops with error.
- ▢ Activating DAD without sediment fractions defined (`lsedtot=0`) — model crashes.
- ▢ Confusing `active` table with `triggerlevel` — both gate dredging; `active=0` overrides depth trigger.
- ▢ Looking for water-column sink from dredge plume — not implemented; DAD is bed-only.
- ▢ Comparing `LINK_SUM` across `morfac` settings expecting same value — `morfac=10` gives 10× volumes for same `dt`.
- ▢ Restart with DAD: bed administration recovers but `LINK_SUM` resets to zero each run unless `cumLink_continue` is set (check version-specific support).

## Next expansion

- Channel maintenance scheduling recipe (real-world example).
- Multi-fraction nourishment input file example.
- DAD restart / hot-start details.

## References

- Roelvink 2006 (process-based morphology).
- Lesser et al. 2004 (Delft3D morphology framework).
- Delft3D-FLOW User Manual (DAD section, Deltares).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src`. Auto-draft = false; review_required = true.
