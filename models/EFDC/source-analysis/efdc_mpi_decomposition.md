---
title: "efdc mpi decomposition"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_mpi_decomposition.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

EFDC+'s 2D logical decomposition (with 1D as degenerate case), JSON-based partition input (`decomp.jnp`, NOT `DECOMP.inp`), MPI graph topology (Cartesian disabled to allow inactive holes), local↔global mapping arrays (`IL2IG/JL2JG, IG2IL/JG2JL`), ghost cell exchange via `communicate_ghost_cells` interfaces, parallel PCG solver `Congrad_MPI` with `DSI_All_Reduce`, master-gather output pattern (no per-PE science output), static load balance (no dynamic repartitioning), and master-only restart files. Use this when configuring an MPI run, debugging ghost-cell exchange, or interpreting `decomp.jnp` partition decisions.

## Source basis

- `MPI_Domain_Decomp/Scan_JSON_Decomp.f90:9-107`, `Read_JSON_Decomp.f90:52-57` — JSON parser.
- `MPI_Utilities/Setup_MPI_Topology.f90:53-138` — MPI topology setup.
- `MPI_Utilities/mod_Variables_MPI.f90:121-150` — mapping arrays.
- `MPI_Domain_Decomp/Parent_Grid.f90`, `Child_Grid.f90`, `Scan_Cell.f90` — grid setup.
- `cellmap.f90:65-109` — cell map.
- `MPI_Mapping/Create_List_No_Ghost_Cells.f90:34-45` — ghost exclusion.
- `MPI_Communication/mod_Communicate_Ghost_Routines.f90:19-248` — ghost exchange.
- `MPI_Communication/Communicate_Groups.f90:50-1185` — face lists, PCG exchange.
- `calpuv9c.f90:31, 693-850` — parallel CALPUV9C.
- `MPI_Domain_Decomp/Congrad_MPI.f90:63-131` — parallel PCG.
- `MPI_Communication/mod_allreduce.f90:55-69` — `DSI_All_Reduce`.
- `MPI_Out/Mod_Map_Write_EE_Binary.f90:49-59`, `MPI_Mapping/Mod_Map_Gather_Sort.f90:85-92` — output.
- `mod_restart.f90:49-870` — master-only restart.

## A. Domain split

EFDC+ uses **2D logical decomposition** described by `n_x_partitions, n_y_partitions`. 1D row/column = degenerate case where one dimension is `1`.

JSON decomp reader (`Scan_JSON_Decomp.f90:41-52`) loads from `decomp.jnp`:
- `number_i_subdomains, number_j_subdomains`.
- Active subdomain count.
- x widths, y widths.
- Active flags.

Rank assignment row-major over `(i,j)` active flags: active cells get `process_map(i,j)=nD`; inactive slots remain `-1` (`:94-107`).

MPI topology explicitly 2D: `dimensions(1)=n_x_partitions`, `dimensions(2)=n_y_partitions` (`Setup_MPI_Topology.f90:53-57`).

**Cartesian topology path is disabled** (`if( .false. )`); active path creates **MPI graph topology** so inactive holes can be skipped (`:61, 81, 138`). This is unusual — most ocean models use Cartesian.

## B. Global / local mapping

Core maps (`mod_Variables_MPI.f90:121-124`):
- `IL2IG, JL2JG` — local→global I/J.
- `IG2IL, JG2JL` — global→local I/J.

`Map2Global` maps local `L` to global `L`; `Map2Local` reverse (`:139-150`).

Build pipeline:
- `Parent_Grid` fills `IG2IL/JG2JL` over each PE's global I/J extent (`:44-51`).
- `Child_Grid` fills `IL2IG/JL2JG` (`:46-53`).
- `CELLMAP` builds `LIJ_Global, LIJ`, `IL_Global/JL_Global`, `Map2Global`, `Map2Local` (`cellmap.f90:65-109`).

Ghost cells excluded from output/reduction maps by iterating only `I,J = 3..IC-2/JC-2` (`Create_List_No_Ghost_Cells.f90:34-45`).

So **2 ghost layers** at each subdomain edge.

## C. Ghost exchange

Generic `communicate_ghost_cells` interfaces for 1D/3D/4D real, integer, logical (`mod_Communicate_Ghost_Routines.f90:19-23`).

Convention: active cells sent, ghost cells populated (`:52`).

`Communicate_Initialize` precomputes face lists `Comm_Cells(:, active/ghost, west/east/south/north)` (`Communicate_Groups.f90:50-55`).

Examples:
- West active: `I=3,4`.
- East ghost: `I=IC-1, IC`.
- North active rows: `J=JC-3, JC-2`.
- South ghost rows: `J=1,2`.
(`:62-141`).

1D exchange sends to W/E/N/S with **blocking `MPI_SEND/MPI_RECV`** through `DSIcomm` (`:122-248`).

`Communicate_1D2` exchanges two 1D arrays in one message; used by MPI PCG for `RCG, PCG` (`:1107-1185`).

## D. Partition input file

The actual file is **`decomp.jnp`**, despite some comments mentioning `DECOMP.inp`. Parsed as JSON (`Scan_JSON_Decomp.f90:9-41`).

Required fields:
- `number_i_subdomains`, `number_j_subdomains`.
- `number_active_subdomains`.
- `i_subdomain_widths`, `j_subdomain_widths`.
- `active_flag`.

Width sums validated against global `IC/JC` in second read pass (`Read_JSON_Decomp.f90:52-57`).

## E. CALPUV9C parallel PCG

`CALPUV9C` imports MPI, `MPI_All_Reduce`, ghost routines (`calpuv9c.f90:31`).

In MPI mode, calls `Congrad_MPI` when `MDCHH == 0`. **Channel interaction (`MDCHH >= 1`) NOT parallelized** (`:693-695`).

After solve: exchanges pressure ghost values (`:701`), later `HP` ghosts (`:850`).

`Congrad_MPI` (`MPI_Domain_Decomp/Congrad_MPI.f90:63-131`):
- Computes local residuals.
- Exchanges `RCG/PCG`.
- Uses `GhostMask` to exclude ghost cells from dot products.
- Global PCG scalars summed with `DSI_All_Reduce`: `RPCG, PAPCG, RPCGN, RSQ`.

`DSI_All_Reduce` wraps `MPI_ALLREDUCE`; falls back to local assignment when `num_Processors == 1` (`mod_allreduce.f90:55-69`).

## F. Output gathering

Model fields gathered to global arrays on master, **NOT independent per-PE science outputs**.

`Mod_Map_Gather_Sort.f90:85-92`:
- Local arrays collapsed without ghost cells.
- Gathered with `MPI_Gatherv`.
- Sorted by global `L`.

`Gather_Soln` uses `num_active_l_local` and `MPI_Gatherv` for values + global mapping (`Mod_Gather_Soln.f90:89-103`).

`Map_Write_EE_Binary` maps hydro/output arrays to global; `EE_LINKAGE` called only on `master_id` (`Mod_Map_Write_EE_Binary.f90:49-59`, `aaefdc.f90:3156-3159`).

Per-PE files are **logs/debug only**: `EFDC_out_proc_###.log, log_mpi_proc_###.log, map_mpi_proc_###.log` (`Setup_MPI_Debug_File.f90:67-92`).

## G. Load balancing

**Static, manual**. Decomposition file controls x widths, y widths, active flags.

`Scan_Cell` (`Scan_Cell.f90:145-193`):
- Computes each PE's active-cell count including ghosts.
- Sets `LCM` to maximum local count plus padding.

So **poor partition widths or inactive-mask choices create imbalance**; **runtime does NOT repartition dynamically**.

For Korean coastal domain with rivers/bays, manual partition tuning matters — e.g., put ocean PEs with similar cell counts; group river inlets onto adjacent PEs.

## H. Hot-start / restart with MPI

Restarts are **global master-owned** files, NOT per-PE.

`Restart_Out` (`mod_restart.f90:49-67`):
- Gathers restart arrays first.
- Non-master ranks return.
- Only master writes `RESTART*.OUT` or `CRASHST.OUT`.

`Restart_In` (`:518-870`):
- Reads `restart.inp` only on master (`:518, 520`).
- Broadcasts global arrays to all ranks (`:769, 777, 791`).
- Populates each PE's local arrays through `Map2Local(LG).LL` (`:868, 870`).

This means restart with different processor count is supported (re-decomposes from global state).

## Decision Guide

| Configuration | Setup |
|---|---|
| 16-core run, square domain | `n_x_partitions=4, n_y_partitions=4` |
| Wide-shallow domain | `n_x_partitions=8, n_y_partitions=2` |
| Domain with islands/holes (estuary) | Set `active_flag=0` for hole subdomains |
| Channel network (linear) | 1D decomp, e.g., `n_x_partitions=N, n_y_partitions=1` |
| Restart with different #cores | Just change `decomp.jnp`; master broadcasts global state |
| Debugging communication | Enable `Setup_MPI_Debug_File` per-PE logs |
| Production run | Disable per-PE debug logs |

## Working Rules

- `decomp.jnp` total active cells should match expected core count.
- Width sums must equal global `IC/JC` exactly — runtime check.
- 2-cell ghost width fixed; cannot change.
- `MDCHH >= 1` (subgrid channels) is **not MPI-parallel** — serializes that part of the run.
- Output is master-gathered — single file per timestep, easier post-processing but master may bottleneck for huge domains.
- Hot-start works across processor count changes (master broadcasts).
- For load balance: aim for ~equal active-cell count per PE; visualize `decomp.jnp` before running.

## Common Pitfalls

- ▢ Looking for `DECOMP.inp` — file is `decomp.jnp` (JSON).
- ▢ `n_x_partitions × n_y_partitions ≠ MPI ranks` — runtime abort.
- ▢ Using cartesian topology — disabled in code; graph topology used.
- ▢ Setting `MDCHH >= 1` for high-PE-count run — no parallelization; severe slowdown.
- ▢ Expecting per-PE NetCDF output — only master writes; no per-rank science files.
- ▢ Width sum off by 1 — common manual error; runtime warns but may run with wrong total.
- ▢ Inactive subdomain in middle of domain — graph topology handles it; verify via `process_map`.
- ▢ Hot-start with corrupt `restart.inp` — only master sees the error; other ranks hang waiting for broadcast.

## Next expansion

- `decomp.jnp` generation tooling.
- Load-balance audit for Korean coastal mesh.
- `MDCHH` parallel implementation status.

## References

- EFDC+ MPI Implementation Notes (Dynamic Solutions).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
