---
slug: delft3d_delwaq
title: Delft3D-DELWAQ Coupling (FLOW .hyd export, .sub substances, process library, decoupled timestep)
model: delft3d
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/delft3d/source_code/Delft3D/src
---

## Scope

How Delft3D-FLOW exports the `.hyd` steering file (`com-<run>.hyd` or `_unstructured.hyd`) plus binary `.vol/.are/.flo/.poi/.len`; the DELWAQ engine in `engines_gpl/waq/waq_computation` (main `dlwqmain` → `run_integration_schemes`); `.sub` substance configuration files in `subFiles/` (substance, parameter, output, active-processes tags); the process library `proc_def.dat` with `dlwqp1` preprocessor; the **decoupled timestep** (FLOW `Flwq` interval gives WAQ files; DELWAQ `idt` is independent); FLOW's volume-balance check (`wrwaqbal`); multi-domain via `ddcouple` and `waqmerge`; and `.his`/`.map` binary formats. Use this when wiring water-quality post-processing of FLOW output.

## Source basis

- FLOW export: `flow2d3d_io/src/output/wrwaqhyd.f90:120-250`, `wrwaqpnt.F90:150-293`, `wrwaqvol.f90:96-116`, `wrwaqflo.f90:74-105`, `wrwaqfil.F90:546-613`, `wrwaqbal.f90:98-311`.
- WAQ data: `utils_lgpl/waq_hyd_data/hydrodynamics_utils.f90:101-189`.
- WAQ engine: `waq/waq_computation/CMakeLists.txt:1-7, delwaq2_main.F90:23-57`.
- WAQ run: `waq/resources/scripts/run_delwaq.sh:13-56`.
- Substances: `waq/resources/process_lib/subFiles/01_Tracers.sub:1-55, 02_Oxygen_bod.sub:1-56`.
- Process lib: `waq/waq_process/CMakeLists.txt:24-28`, `waq_preprocessor/dlwqp1.f90:327-801`, `wq_processes/wq_processes_initialise.f90:311-584, wq_processes_proces.f90:52-401`.
- Time: `flow2d3d_io/src/input/rdwaqpar.f90:111-216`, `wrwaqfil.F90:260`, `waq_io/inputs_block_2.f90:365-398`, `inputs_block_3.f90:686-697`.
- Multi-domain: `tools_gpl/waq_tools/ddcouple/ddcouple.f90:41-166`, `write_hyd.f90:190-208`, `waqmerge/overall_hyd.F90:24-69`.
- Output: `waq/waq_kernel/results/write_binary_output.f90:34-147`.

## A. FLOW hyd output

FLOW writes ASCII `.hyd` steering + binary side files.

`wrwaqhyd` creates:
- `com-<run>.hyd` and `_unstructured.hyd`.
- Marks `task full-coupling`.
- Writes geometry, hyd/conversion times, grid dimensions, exchange counts.
- Filenames for `.vol, .are, .flo, .poi, .len`, etc.

(`wrwaqhyd.f90:120-250`).

Hyd data structure (`hydrodynamics_utils.f90:101-189`):
- `volumes-file, areas-file, flows-file, pointers-file`.
- Exchange counts.
- `volume, area, flow, ipoint`.

Topology to `.poi`: 4-column from/to/from-1/to+1 pointer table; `.lga` stores grid + exchange dimensions (`wrwaqpnt.F90:150-293`).

Volumes: binary records `itime, vol(1:noseg)` after aggregating FLOW cells to WAQ segments (`wrwaqvol.f90:96-116`).

Areas + averaged flows: accumulated over FLOW steps, divided by `naccum`; written in `wrwaqflo` (areas) + `wrwaqfil` (flows) (`wrwaqflo.f90:74-105, wrwaqfil.F90:546-613`).

## B. DELWAQ engine location

`engines_gpl/waq` contains DELWAQ.

Main computation library: `engines_gpl/waq/waq_computation`. `dlwqmain` calls `run_integration_schemes` (`CMakeLists.txt:1-7, delwaq2_main.F90:23-57`).

Executable wrapper: `$bindir/delwaq` (`run_delwaq.sh:13-56`).

## C. Substance configuration (.sub files)

`.sub` files in `engines_gpl/waq/resources/process_lib/subFiles/`.

Define `substance ... active/inactive`, `parameter`, `output`, `active-processes`.

Example tracer file: `01_Tracers.sub:1-55` — substance, parameters, outputs, active-processes.

Oxygen/BOD: `02_Oxygen_bod.sub:1-56` — DO, BOD substances + reaeration + oxygen demand processes.

Parser recognizes those tags + attributes (`data_processing.f90:405-631`).

Generator (`waqpb_lib/wrisub.f90:36-88`) writes same schema.

## D. Process library coupling

Default process library installed as `proc_def.dat`/`.def` with CSV + subFiles (`waq_process/CMakeLists.txt:24-28`).

Preprocessor accepts `-p`, otherwise uses `../share/delft3d/proc_def.dat`. Reads with `rd_tabs`, builds process properties, sorts dependencies, writes process work file (`dlwqp1.f90:327-801`).

Runtime: `wq_processes_initialise` does same for DELWAQ2; can load open process shared library (`wq_processes_initialise.f90:311-584`).

Process execution controller: `wq_processes_proces` (`wq_processes_proces.f90:52-401`).

## E. DELWAQ timestep decoupled from FLOW

FLOW's WAQ export is **output/conversion interval**: `Flwq` gives start/interval/stop → `itwqff/itwqfi/itwqfl` (`rdwaqpar.f90:111-216`).

FLOW only writes WAQ files when `mod(nst-itwqff, itwqfi)==0` (`wrwaqfil.F90:260`).

DELWAQ's integration timestep: read **independently** in DELWAQ input block 2 — constant or variable (`inputs_block_2.f90:365-398`).

Compatibility: volume records must be monotonic/equidistant; DELWAQ `idt` must **divide** the hyd interval (NOT equal FLOW `dt`) (`inputs_block_3.f90:686-697`).

So FLOW dt and DELWAQ dt are independent — typical DELWAQ uses much larger timesteps than FLOW.

## F. Conservation across hyd

FLOW checks volume closure between start/end volumes + integrated fluxes (`wrwaqbal.f90:98-311`):
- Updates theoretical volumes via `flow(iq) · idt`.
- Adds loads.
- Corrects vertical flows for closure errors.
- Reports remaining error.
- Advances `vol = vol2`.

Internal hyd-balance checker reads `.hyd`, reports segment/exchange counts, outputs volume/discharge error maps/his (`tools_gpl/waq_tools/internal/checkhydbal/`).

## G. Multi-domain DELWAQ (after DD FLOW)

`ddcouple` for "Merging of hydrodynamic data sets from dd or parallel Delft3D 4 FLOW runs" (`ddcouple.f90:41-166`).

Works with collections of domain hydrodynamics + DD boundaries.

Merged `.hyd` writer emits `domains` and `dd-boundaries` sections (`write_hyd.f90:190-208`).

`waqmerge` creates overall unstructured hyd with per-domain `.hyd` entries (`overall_hyd.F90:24-69`).

So DD-FLOW + DELWAQ workflow:
1. Run FLOW with DD.
2. `ddcouple` merges per-subdomain `.hyd` files.
3. Run DELWAQ on merged hyd.

## H. .his / .map binary formats

**`.map`** (`write_binary_output.f90:34-83`):
- 4 × 40-char title strings.
- `notot, num_cells`.
- Variable names.
- Each record: `itime` + values for every segment.

**`.his`** (`:101-147`):
- Titles.
- `notot, num_monitoring_points`.
- Variable names.
- Dump-location names.
- Each record: `itime` + values for each monitoring point.

ODS reader confirms layout; distinguishes by extension (`open_data_structure_file_utils.f90:69-222`).

`maptonetcdf` utility reads same header (`tools_gpl/waq_tools/maptonetcdf/`).

## Decision Guide

| Need | Setup |
|---|---|
| Single FLOW domain WQ post-processing | Run FLOW with `Flwq`, then DELWAQ on `.hyd` |
| Standard tracer | Use `01_Tracers.sub` |
| DO + BOD | Use `02_Oxygen_bod.sub` |
| Custom substances | Write own `.sub`; reference `proc_def.dat` |
| Multi-domain DD FLOW | `ddcouple` to merge hyd, then DELWAQ |
| Higher DELWAQ timestep than FLOW | Set DELWAQ `idt` to multiple of `Flwq · FLOW dt` |
| Conservation check | Use `checkhydbal` tool |
| NetCDF output | `maptonetcdf` post-conversion |
| Korean coastal eutrophication | DELWAQ with full nutrient process suite |

## Working Rules

- FLOW `Flwq` interval typically 1 hour for coastal; 15 min for fast estuary.
- DELWAQ `idt` must divide hyd interval; common ratio 1:1 to 1:6.
- Process library `proc_def.dat` from Deltares — don't modify; extend via `.sub` files.
- Verify FLOW volume closure (`wrwaqbal` output) before running DELWAQ — bad closure → wrong WQ.
- For DD-FLOW + DELWAQ: `ddcouple` after FLOW completes; merged hyd then DELWAQ.
- `.his` for time series; `.map` for spatial; both binary — use ODS reader or `maptonetcdf`.
- Substance ordering in `.sub` matters — must match expected by process library.

## Common Pitfalls

- ▢ Running DELWAQ with `idt` not dividing hyd interval — runtime check fails.
- ▢ Forgetting `Flwq` in FLOW MDF — no `.hyd` written; DELWAQ has nothing.
- ▢ FLOW with poor mass closure — DELWAQ inherits errors; check `wrwaqbal`.
- ▢ Multi-domain DELWAQ without `ddcouple` — separate per-subdomain runs unsupported.
- ▢ `.sub` file referencing process not in library — preprocessor errors.
- ▢ Comparing DELWAQ time vs FLOW — may diverge after first conversion; use hyd time.
- ▢ Hot-start DELWAQ across hyd file change — segment indices may shift.

## References

- Postma 1985 (DELWAQ baseline).
- WL | Delft Hydraulics tech reports.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src`. Auto-draft = false; review_required = true.
