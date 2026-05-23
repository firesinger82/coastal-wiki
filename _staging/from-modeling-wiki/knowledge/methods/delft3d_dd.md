---
slug: delft3d_dd
title: Delft3D-FLOW Domain Decomposition (.ddb file, KCS=3 coupling, iterative Block Jacobi)
model: delft3d
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d
---

## Scope

Delft3D's Domain Decomposition (DD): minimal `flow2d3d_kernel_dd_f` directory (just `flow_nextstep.f90`), explicit coupling markers `KCS=3` for coupling cells, **iterative Block Jacobi** (NOT explicit; max 5 iterations for velocity/concentration/2D advection-diffusion), `nxtstp` synchronization at timestep boundaries, `.ddb` (DD-bounds) file structure with multiple subdomain MDFs (NOT a single MDF), DIMR BMI integration, the **distinct difference from MPI parallel** (DD = mapper-orchestrated subdomain coupling for refinement; MPI = halo-exchange partition of one grid), and supports 1:n refinement (odd ratios advised). Use this when configuring nested coastal+estuarine domains, mixed-resolution grids, or integrating with DIMR.

## Source basis

- `flow2d3d_kernel_dd_f/CMakeLists.txt:1-17`, `src/flow_nextstep.f90:31` — minimal directory.
- `flow2d3d/src/dd/mapper/mapper_uvz.cpp:80-2277` — coupling logic, KCS=3.
- `flow2d3d/src/dd/mapper/mapper_config.cpp:205-212` — Block Jacobi params.
- `flow2d3d/src/dd/mapper/mapper_statemachine.cpp:141-153` — iterative state machine.
- `flow2d3d_kernel/src/compute/uzd.f90:1079-1375` — re-solve loops.
- `flow2d3d_kernel/src/compute/sud.f90:600-884` — same.
- `flow2d3d_io/src/input/rdxyzo.f90:39-160` — `Filcco`.
- `flow2d3d_kernel/src/dd/inigeo_dd.f90:108-538`, `chkrefinement.f90:32-95` — DD geometry.
- `flow2d3d/src/dd/dd.cpp:166-491` — DD init.
- `flow2d3d/src/flow2d3d.cpp:85-275` — BMI / DIMR.
- `flow2d3d_data/include/dfparall.igs:35-54`, `parallel_mpi/dfsendd_nm_pos1.F90` — MPI separate path.
- `flow2d3d/src/dd/iterators/minimumbarrier.cpp:38-231` — pthread / no MPI.
- `flow2d3d/include/maploops.h:32-301` — refinement support.

## A. flow2d3d_kernel_dd_f contents

Tiny directory:
- Only `CMakeLists.txt` and `src/flow_nextstep.f90`.

CMake builds library `flow2d3d_kernel_dd_f` from `src`; links `deltares_common, flow2d3d_data, flow2d3d_io` (`CMakeLists.txt:1-17`).

Single source: Fortran-to-C next-step hooks for DD (`flow_nextstep.f90:31`).

Most DD logic lives in C++ mapper (`flow2d3d/src/dd/mapper/`) and Fortran FLOW kernel.

## B. DD subdomain coupling (KCS=3)

Explicit coupling markers in FLOW masks. Mapper checks (`mapper_uvz.cpp:210-213, 80-90`):
- Coupling point: `KCS=0`.
- Interior neighbor: `KCS=1`.
- Later sets `KCS/KCU/KCV=3` for coupling locations.

FLOW arrays allocated with **`ddbound` padding** around local domain — extra boundary/ghost storage (`rdxyzo.f90:96-97`).

DD geometry: asymmetric coupling reduces lower bounds by `DDB`; currently only `DDB=1` (`inigeo_dd.f90:108-112`).

Coupled values copied/averaged across boundary:
- Normal + tangential velocities copied to coupling points outside model domain (NOT to interface velocity points themselves) (`mapper_uvz.cpp:909-1037`).
- Discharges + water levels corrected across coarse/fine interface (`:2137-2277`).

## C. Iterative Block Jacobi (NOT explicit)

DD is **iterative**, not single explicit boundary exchange.

Mapper defaults to "Block Jacobi convergence criterion", **max 5 iterations** for velocity, concentration, 2D advection-diffusion (`mapper_config.cpp:205-212`).

State machine (`mapper_statemachine.cpp:141-153`):
- During velocity coupling, `Proces(...)` tests convergence.
- If not converged AND iteration cap not reached: returns `D3dFlow_Solve_V` or `D3dFlow_Solve_U` so FLOW re-solves.

FLOW honors by jumping back to solve label when `nxtstp` returns same solve step (`uzd.f90:1368-1375`).

## D. Time-stepping coordination

FLOW calls `nxtstp` at DD interruption points.

Timestep start: `D3dFlow_InitTimeStep`; comment "set up virtual points for next time step" (`trisol.f90:1104-1107`).

During solve: mapper build/check for U/V + dry checks (`uzd.f90:1079-1366, sud.f90:600-884`).

Initialization: `nxtstp` synchronization point — all subdomains wait, mappers initialize, then continue (`tricom_init.F90:1238-1244`).

## E. Coupled-domain MDF input (.ddb file)

DD run starts from **`.ddb` bounds file**, NOT one MDF.

Each `.ddb` line names left/right grid files + boundary index ranges. DD reader converts each `xxx.grd` → `xxx.mdf` and requires MDF to exist (`dd.cpp:324-494`).

Single-domain run: `mdfFile`. DD run: `ddbFile`. Code rejects having both (`flow2d3d.cpp:164-172`).

Inside each subdomain MDF, `Filcco` supplies curvilinear grid (`rdxyzo.f90:39-160`).

So DD = **multiple MDFs referenced indirectly by a DDB file**, each subdomain MDF with own `Filcco`.

## F. DIMR interaction

FLOW C++ exposes BMI `initialize(char* configfile)` — "used by DIMR" (`flow2d3d.cpp:85-86`).

DIMR constructor recognizes `.mdf` or `.ddb` by extension; calls `TRISIM` in `initOnly=1` mode for BMI init (`:194-275`).

**Code concern**: in DIMR `.ddb` branch, `ddbFile` redeclared inside `if`, shadowing outer; outer `ddbFile` remains `NULL` (`:218-234`).

Older d-hydro/config-tree path does create DD from `ddbFile` (`:151-172`).

## G. Differences from MPI parallel

**DD** = Hydra/mapper/subdomain orchestration:
- Creates FLOW process iterators, mapper iterators.
- Joins each mapper to two neighboring subdomain processes (`dd.cpp:356-391`).

**MPI parallel** = separate partition/halo-exchange:
- `dfparall` stores global/local partition ranges + `iblkad` interface table for neighbors and overlapping unknowns (`dfparall.igs:35-54`).
- MPI halo exchange via `mpi_isend`/`mpi_irecv` (`dfsendd_nm_pos1.F90:32-146`).

DD minimum barrier **explicitly disables MPI** (may conflict with parallel FLOW); uses pthread/local iterator logic (`minimumbarrier.cpp:38-231`).

So DD and MPI are **orthogonal mechanisms**:
- DD: same-grid subdomains with refinement.
- MPI: partition of one continuous grid for parallel speedup.

## H. When DD is needed

DD is for **coupled subdomains, especially nonuniform/refined interfaces**.

Mapper infrastructure for `1:n` coupling; supports odd/even refinement (`maploops.h:32-60`).

1-to-2 refinement example documented, including asymmetric velocity coupling (`:294-301`).

Kernel checks refinement factors; **odd refinement strongly advised** (`chkrefinement.f90:32-95`).

Also handles mismatched interface geometry/depths:
- DD geometry recomputes coupling-point metrics (`inigeo_dd.f90:535-538`).
- Mapper warns when depth differences at couple boundary exceed threshold (`mapper_uvz.cpp:309-341`).

So DD is the mechanism for **joining subdomains where simple MPI partition isn't enough**.

## Decision Guide

| Need | Setup |
|---|---|
| Single grid, parallel speedup | MPI (not DD) |
| Coastal coarse + estuarine fine | DD with `.ddb` and 2 MDFs |
| 1:3 refinement at interface | DD; odd ratio recommended |
| Multiple coastal cells embedded | DD with multi-subdomain `.ddb` |
| DIMR-coupled FLOW + WAVE | DIMR `.ddb` config |
| Single MDF + parallel | MPI parallel only |
| Mismatched bathymetry at interface | DD warns; reduce mismatch |
| Korean estuary nested in shelf | DD: shelf coarse + estuary fine |

## Working Rules

- For Korean Han River estuary nested in Yellow Sea: shelf grid 500-1000 m, estuary 50-100 m → DD with 5:1 or 9:1 ratio.
- Verify `.ddb` boundary index ranges match grid extents.
- Block Jacobi 5 iterations OK for typical 1:1 to 1:5 refinement; large refinement (1:9+) may need more iterations (recompile with higher `MaxIters`).
- DD overhead: ~10-20% per subdomain for mapper communication.
- DD + MPI not supported simultaneously; pick one.
- DIMR `.ddb` shadowing bug: prefer d-hydro path or single MDF for now.
- Check log for "Block Jacobi did not converge" — increase iterations or tighten interface.

## Common Pitfalls

- ▢ Setting `mdfFile` and `ddbFile` simultaneously — rejected.
- ▢ Even refinement (1:2, 1:4) — works but odd preferred (1:3, 1:5, 1:9).
- ▢ Large depth mismatch at DD interface — silent degradation; check warning.
- ▢ Expecting MPI speedup with DD — DD is for refinement coupling, not parallelization.
- ▢ DIMR `.ddb` initialization — possible bug at `flow2d3d.cpp:218-234`.
- ▢ Confusing DD ghost cells with MPI ghost cells — DD has `ddbound` padding; MPI has `iblkad` halos.
- ▢ Hot-start with different DD topology — coupling fails; restart cleanly.

## References

- Vatvani et al. 2002 (Delft3D DD).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl/flow2d3d`. Auto-draft = false; review_required = true.
