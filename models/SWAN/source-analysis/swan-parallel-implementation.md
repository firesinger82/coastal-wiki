---
title: "swan parallel implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-parallel-implementation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN parallel implementation — MPI domain decomp + OpenMP sweeps

## Scope note

How SWAN's hybrid MPI + OpenMP parallelism actually works in code: MPI initialization, domain decomposition with halos, message passing during sweep, OpenMP region in `SWCOMP`, reduction operations, master-only file I/O, and per-PE output collection.

## Source basis

Codex deep scan 2026-05-06 of:
- `src/swanmain.ftn` — main entry, MPI/OMP setup
- `src/swanparll.ftn` — MPI domain decomposition
- `src/swancom1.ftn` — OpenMP region, sweep parallelism, reductions
- `src/swmod*.ftn` — parallel state holders

## A. MPI initialization

- `MPI_INIT`, `MPI_COMM_RANK`, `MPI_COMM_SIZE` are inside `SWINITMPI` at `[file=src/swanparll.ftn line=140]`, `[file=src/swanparll.ftn line=157]`, `[file=src/swanparll.ftn line=173]`
- These calls are tagged with `!MPI!NCOH` markers — meaning they are conditionally activated at compile time (preprocessor) for MPI builds; serial builds skip them
- Serial defaults: `INODE = 0`, `NPROC = 1` at `[file=src/swanparll.ftn line=152-153]`
- Rank conversion: `INODE = INODE + 1` at `[file=src/swanparll.ftn line=158]` (MPI 0-based → SWAN 1-based)
- Master detection: `IAMMASTER = INODE.EQ.MASTER` at `[file=src/swanparll.ftn line=196]`, with `MASTER` parameter at `[file=src/swmod2.ftn line=1145]` (= 1 in SWAN's 1-based indexing, i.e., MPI rank 0)

## B. MPI domain decomposition

Main path: `SWDECOMP → SWPARTIT → SWBLADM → ...`

- `SWDECOMP` at `[file=src/swanparll.ftn line=2649]`
- `SWBLADM` at `[file=src/swanparll.ftn line=2411]`
- `SWCOLLECT` at `[file=src/swanparll.ftn line=3560]`

### Local extents

`SWBLADM` scans `IPOWN(IX,IY) == INODE` to derive local bounding box `MXF, MXL, MYF, MYL` at `[file=src/swanparll.ftn line=2489-2498]`.

### Halo expansion

Halos applied via `IHALOX, IHALOY`:
```
MXF -= IHALOX
MXL += IHALOX
(clamped to domain bounds)
```
at `[file=src/swanparll.ftn line=2525-2528]`.

### Edge flags

`LMXF, LMXL, LMYF, LMYL` set from bounds + node position (`INODE==1` / `INODE==NPROC`) with orientation-dependent logic at `[file=src/swanparll.ftn line=2534-2543]`.

### Ghost interface metadata

Per-neighbor send/recv indices (`ICSEND`, `ICRECV`) packed into `IBLKAD` at `[file=src/swanparll.ftn line=2557-2643]`.

### Local sizes finalized

```
MXC = MXL - MXF + 1
MYC = MYL - MYF + 1
MCGRD = (recomputed over cropped box)
```
at `[file=src/swanparll.ftn line=2798-2805]`.

**No `IXOFFS`, `IYOFFS`, `MXC_LOCAL`, `MYC_LOCAL` symbols** in this codebase — SWAN reuses `MXF/MXL/MYF/MYL` and resized `MXC/MYC` directly.

## C. MPI message passing during sweep

### Wrappers

- `SWSYNC` (global barrier) at `[file=src/swanparll.ftn line=329]`, `[file=src/swanparll.ftn line=437]` — wraps `MPI_BARRIER` (also `!MPI!NCOH` tagged)
- `SWSENDNB` (point-to-point send) at `[file=src/swanparll.ftn line=454]`, `[file=src/swanparll.ftn line=569-570]` — `MPI_SEND` to `IDEST-1`
- `SWRECVNB` (blocking receive) at `[file=src/swanparll.ftn line=587]`, `[file=src/swanparll.ftn line=708-709]` — `MPI_RECV` from `ISOURCE-1`

### Halo exchange during sweep

`SWEXCHG` (WFR variant) at `[file=src/swanparll.ftn line=3044]`, `[file=src/swanparll.ftn line=3197]`, `[file=src/swanparll.ftn line=3215]` iterates neighbors and calls `SWSENDNB` then `SWRECVNB` using `IBLKAD` interface maps.

Sweep-phase row/interface exchanges (`SWRECVAC`, `SWSENDAC`, `SWEXCHG`) called from `swancom1.ftn` at `[file=src/swancom1.ftn line=1964-1968]`, `[file=src/swancom1.ftn line=2058-2062]`, `[file=src/swancom1.ftn line=2107]`.

**No `MPI_SENDRECV`** family — SWAN uses separate send/recv pattern.

## D. OpenMP parallelism in `SWCOMP`

### Main parallel region

`[file=src/swancom1.ftn line=1170-1188]`:
```fortran
!$OMP PARALLEL DEFAULT(SHARED)
!$OMP+ PRIVATE(...)        ! extensive list
!$OMP+ COPYIN(...)         ! threadprivate imports
```

### Barriers and FLUSH

- Barriers at `[file=src/swancom1.ftn line=1424]`, `[file=src/swancom1.ftn line=1692]`, `[file=src/swancom1.ftn line=1733]`, `[file=src/swancom1.ftn line=1854]`, `[file=src/swancom1.ftn line=2098]`, `[file=src/swancom1.ftn line=2126]`, `[file=src/swancom1.ftn line=2344]`
- `!$OMP FLUSH` at `[file=src/swancom1.ftn line=1855]`, `[file=src/swancom1.ftn line=1994]`, `[file=src/swancom1.ftn line=1996]` — for ordering around lock-based dependency checks (`LLOCK`) in pipelined sweep

### Per-thread buffers

Allocated **inside** the parallel region — each thread owns private work arrays:
- `CAX, CAY, CAS, CAD, SWMATR, LSWMAT, ...` at `[file=src/swancom1.ftn line=1204-1224]`

### Sweep workload

`!$OMP DO SCHEDULE(STATIC, 1)` with `FIRSTPRIVATE/LASTPRIVATE` on `WWINT` at `[file=src/swancom1.ftn line=1936-1938]`.

So OpenMP parallelizes the **per-vertex sweep loop** with each thread getting its own local matrix workspace.

## E. Reduction operations (hybrid MPI + OMP)

### `ACCUR` reduction (% converged points)

In `SACCUR` at `[file=src/swancom1.ftn line=4876-4886]`:
1. Thread-local `IACCURt` atomically accumulated to shared `IACCUR`
2. Master MPI global sum: `CALL SWREDUCE(IACCUR, 1, SWINT, SWSUM)`
3. Compute `% = IACCUR * 100 / NINDX`

### Hs/Tm change reduction

`[file=src/swancom1.ftn line=4779-4787]`:
- `CALL SWREDUCE(ARR, 2, SWREAL, SWSUM)`
- `CALL SWREDUCE(NINDX, 1, SWINT, SWSUM)`

### Curvature criterion

`SWSTPC` at `[file=src/swancom1.ftn line=9922-9928]` packs `[IACCUR, WETGRD]` into `IARR` and does **one** integer reduction.

### Wrappers

`SWREDUCI`/`SWREDUCR` at `[file=src/swanparll.ftn line=1279-1280]`, `[file=src/swanparll.ftn line=1415-1416]` execute `MPI_ALLREDUCE` for integer/real arrays.

## F. Boundary file I/O in parallel

Master-only read pattern:
- `[file=src/swanmain.ftn line=6908-6925]` — `IF (INODE.EQ.MASTER) CALL RBFILE ...` loop over all boundary files
- After read, broadcast: `CALL SWBROADC(BSPECS, ...)` at `[file=src/swanmain.ftn line=6929]`

Same pattern for external field files (`INAR2D` on master, then `SWBROADC`):
- Wind: `[file=src/swanmain.ftn line=8741-8749]`
- Other: `[file=src/swanmain.ftn line=8769-8777]`

`RBFILE` itself imports `IAMMASTER`: `[file=src/swanmain.ftn line=7469]`, `[file=src/swanmain.ftn line=7480]`.

So **only master process opens/reads files**; all other ranks receive via broadcast.

## G. Output collection (per-PE → global)

Two patterns in code:

### Field collection (in-memory)

`SWCOLLECT` at `[file=src/swanmain.ftn line=740]`, `[file=src/swanparll.ftn line=3560]` collects distributed fields to global form on master. Uses `SWGATHER` (MPI gather/gatherv wrapper) at `[file=src/swanparll.ftn line=3716]`, `[file=src/swanparll.ftn line=3725]`, `[file=src/swanparll.ftn line=3746]` for bounds, index maps, field data.

### File output (per-PE files merged by master)

Each process writes its own per-PE file (suffix `-###`):
- `[file=src/swanparll.ftn line=4479-4504]`
- `[file=src/swanparll.ftn line=4513-4559]`
- `[file=src/swanparll.ftn line=4820-4845]`
- `[file=src/swanparll.ftn line=4932-4998]`

Master post-processes: opens all per-PE files, merges by ownership (`BLKND`) into generic outputs.

After merge: per-process intermediate files closed/deleted at `[file=src/swanparll.ftn line=4259-4262]`.

So SWAN ships with a **built-in merge stage** — unlike ADCIRC which uses fort.80 + adcprep+adcpost, SWAN handles per-PE → global file consolidation internally.

## Decision Guide

| Configuration | Run command | Notes |
|---------------|-------------|-------|
| Single CPU serial | `swanrun -input X` | no MPI/OMP |
| OpenMP only (multi-core, single node) | `OMP_NUM_THREADS=N swanrun -input X` | thread per core |
| MPI only (multi-node) | `mpirun -np N swan.exe < X` | requires MPI build |
| Hybrid MPI + OMP | `OMP_NUM_THREADS=K mpirun -np N swan.exe < X` | best for many-core nodes |
| Coupled with ADCIRC | controlled by ADCIRC's MPI | SWAN inherits MPI comm |

## Working Rules

1. **OpenMP defaults to SHARED** in the parallel region — any custom code added inside must explicitly mark variables PRIVATE if per-thread state.
2. **Master-only I/O** is enforced: never call `OPEN`/`READ` from inside a parallel region. Use `IF(IAMMASTER)` or move outside.
3. **`SWREDUCE` is the hybrid reduction primitive** — wraps thread-local + MPI global sum.
4. **`SWCOLLECT` brings distributed arrays to master** — used before global output operations.
5. **Built-in per-PE file merge** — no external `swanpost` step needed; output files are unified after run.

## Common Pitfalls

- **Custom variables in OMP region not declared PRIVATE** → race conditions visible only with `OMP_NUM_THREADS > 1`.
- **Reading an input file from a non-master rank** → blocks or deadlocks the run.
- **Mismatched `IBLKAD`** between neighbors → halo data corruption silently ruins sweep convergence.
- **Forgetting `SWBROADC` after master-side read** → other ranks see uninitialized boundary data.
- **MPI build flags missing** → `!MPI!NCOH` tags become no-ops; runs as serial despite `-np N`.
- ▢ User-experience cases — placeholder.

## References

- `src/swanmain.ftn` — main entry, master-only read patterns, `SWCOLLECT` for output.
- `src/swanparll.ftn` — `SWINITMPI`, `SWDECOMP`/`SWBLADM`, `SWSYNC`/`SWSENDNB`/`SWRECVNB`, `SWEXCHG`, `SWREDUCE`/`SWGATHER`, per-PE file merge.
- `src/swancom1.ftn` — OpenMP `PARALLEL` region, sweep `OMP DO`, `SACCUR`/`SWSTPC` reductions.
- `src/swmod2.ftn` — `MASTER` parameter, `IAMMASTER`, `INODE`, `NPROC`.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 50+ file:line citations |
| Coverage | MPI init + decomp, halo exchange, OpenMP region, reductions, master I/O, output merge |
| Review status | `review_required: true` |
