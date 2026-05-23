---
slug: swan-data-structures-implementation
title: SWAN data structures — AC1/AC2, COMPDA, BSPECS, memory tables
category: methods
model: swan
auto_draft: false
authored_by: claude-opus-4-7
review_required: true
generated: 2026-05-06
basis: deep Codex source scan of swan/src/{swmod1,swmod2,swanmain,swancom1,SwanGriddata}.ftn(90)
---

# SWAN data structures — AC1/AC2, COMPDA, BSPECS, memory tables

## Scope note

The arrays that hold SWAN's state during a run: action density, spectral grid, geographic grid, working scratch space (`COMPDA`), boundary storage, source-term memo tables, and per-process matrix workspace. With declaration file:line, dimensions, allocation/deallocation points.

## Source basis

Codex deep scan 2026-05-06 of:
- `src/swmod1.ftn`, `src/swmod2.ftn` — module declarations (`M_GENARR`)
- `src/swanmain.ftn` — top-level runtime arrays
- `src/swancom1.ftn` — solver workspace
- `src/SwanGriddata.ftn90` — unstructured-grid module

## A. Action density (`AC1`, `AC2`)

| Array | Declaration | Allocation | Shape | Note |
|-------|-------------|------------|-------|------|
| `AC2` | `[file=src/swmod2.ftn line=1027]` (`M_GENARR`, `SAVE, ALLOCATABLE :: AC2(:,:,:)`) | `[file=src/swanpre1.ftn line=4980]` `ALLOCATE(AC2(MDC,MSC,MCGRD))`; zero at `[file=src/swanpre1.ftn line=4989]` | `(MDC, MSC, MCGRD)` | new/current time level |
| `AC1` | `[file=src/swanmain.ftn line=296]` | `[file=src/swanmain.ftn line=502]` only when nonstationary or S&L (`PROPSL=3`) prop, condition at `[file=src/swanmain.ftn line=500]` | same | old/previous time level |

Semantics documented in argument lists at `[file=src/swanmain.ftn line=266]`, `[file=src/swanmain.ftn line=6826-6827]`.

**`AC1 ← AC2` swap** is an explicit copy at the start of each time step inside `SNEXTI` `[file=src/swanmain.ftn line=6892-6900]`:
```fortran
DO IXY = 1, MCGRD
  DO ISS = 1, MSC
    DO IDD = 1, MDC
      AC1(IDD,ISS,IXY) = AC2(IDD,ISS,IXY)
```

## B. Spectral grid (`SPCSIG`, `SPCDIR`, `DDIR`, `FRINTF`, `FRINTH`)

- Module storage `[file=src/swmod2.ftn line=1029]`: `SPCSIG(:)` shape `(MSC)`, `SPCDIR(:,:)` shape `(MDC,6)`.
- Interface forms used in `swanmain.ftn`: `SPCDIR(MDC,6)`, `SPCSIG(MSC)` at `[file=src/swanmain.ftn line=3642]`, `[file=src/swanmain.ftn line=6830-6831]`.
- `SPCSIG` built geometrically from `SLOW` × `SFAC`; `FRINTF = log(SHIG/SLOW)/(MSC-1)`, `FRINTH = sqrt(SFAC)` at `[file=src/swanpre1.ftn line=4685-4691]`.
- `DDIR` computed at `[file=src/swanpre1.ftn line=1773]` (full circle `2π/MDC`) or `[file=src/swanpre1.ftn line=1789]` (sector).
- `SPCDIR(:,1)` = direction angle (rad); columns 2..6 = `cos`, `sin`, `cos²`, `cos·sin`, `sin²` `[file=src/swanpre1.ftn line=4706]`, `[file=src/swanmain.ftn line=6816-6821]`.
- Field semantics documented at `[file=src/swmod1.ftn line=2030-2037]`.

## C. Geographic grid

| Array | What | Where |
|-------|------|-------|
| `XCGRID(:,:)`, `YCGRID(:,:)` | structured node coordinates | `[file=src/swmod2.ftn line=1025]`, `[file=src/swmod2.ftn line=1028]` |
| `KGRPNT(:,:)` | structured (IX,IY) → wet-point compact index | same module; populated at `[file=src/swanpre1.ftn line=5166-5169]` |
| `MCGRD` | number of wet computational points | `[file=src/swmod1.ftn line=2046]` |
| `vmark`, `nverts`, `ivertg` | unstructured: vertex boundary marker, count, index | `[file=src/SwanGriddata.ftn90 line=65]`, `[file=src/SwanGriddata.ftn90 line=71-72]`; consumed at `[file=src/swanmain.ftn line=146]`, `[file=src/swanmain.ftn line=5053]`, `[file=src/swanmain.ftn line=9101]` |
| `ncells`, `nfaces` | unstructured topology counters (NTRIA equivalent) | `[file=src/SwanGriddata.ftn90 line=62-64]` |

`KGRPNT` indirection is the structured wet-point compaction: `INDX = KGRPNT(IX, IY)` at `[file=src/swanmain.ftn line=7103-7105]`.

## D. Workspace `COMPDA`

`[file=src/swanmain.ftn line=296]` declared, `[file=src/swanmain.ftn line=463]` allocated as `COMPDA(MCGRD, MCMVAR)`.

This codebase doesn't use a literal `JCOMPDA` symbol; instead integer index pointers are defined as named constants `[file=src/swanmain.ftn line=1498-1527]`:

| Index | Field | Definition |
|-------|-------|------------|
| `JDP2` | new-time depth | `=8` `[file=src/swanmain.ftn line=1505]` |
| `JVX2` | new-time current X | `=11` `[file=src/swanmain.ftn line=1508]` |
| `JVY2` | new-time current Y | `=12` `[file=src/swanmain.ftn line=1509]` |
| `JWX2` | new-time wind X | `=16` `[file=src/swanmain.ftn line=1513]` |
| `JWY2` | new-time wind Y | `=17` `[file=src/swanmain.ftn line=1514]` |
| `JFRC2` | bottom friction | `[file=src/swanmain.ftn line=1529]`, used at `[file=src/swancom1.ftn line=7266]`, `[file=src/swancom1.ftn line=3581]` |

Layout `(MCGRD, MCMVAR)` confirmed in shape declarations `[file=src/swanmain.ftn line=4746]`. Each field column is the value at every wet point; "new-time" suffix indicates the post-time-update value (vs "1" suffix = old time, used for interpolation).

`WIND10` (10-m wind speed) is **derived in source-term routines** from `JWX2/JWY2` rather than stored as a dedicated `COMPDA` column.

## E. Boundary storage (`BSPECS`, `BGRIDP`)

- `BSPECS` declared `[file=src/swanmain.ftn line=295]` and allocated `(MDC, MSC, NBSPEC, 2)` at `[file=src/swanmain.ftn line=433]`.
- Rank semantics confirmed at `[file=src/swanmain.ftn line=6945]`:
  - rank 1 = direction bin
  - rank 2 = frequency bin
  - rank 3 = boundary spectrum index (`K1`/`K2`)
  - rank 4 = time slot (old/new for nonstat interpolation)

- `BGRIDP` declared `[file=src/swanmain.ftn line=294]`, allocated as `BGRIDP(6 * NBGRPT)` at `[file=src/swanmain.ftn line=435]`.
- Per-boundary-point packing at `[file=src/swanmain.ftn line=4025-4030]`:
  - 6 ints per point: `[INDXGR, type, W1×1000, K1, W2×1000, K2]`
- Runtime decode at `[file=src/swanmain.ftn line=6938-6946]`:
  - `INDXGR = BGRIDP(6i-5)`, `type = BGRIDP(6i-4)`, `W1 = 0.001 * BGRIDP(6i-3)`, `K1 = BGRIDP(6i-2)`, `K2 = BGRIDP(6i)`

## F. Source-term memory tables

- `MEMNL4(MDC, MSC, MCGRD)` — quadruplet DIA workspace; declared `[file=src/swancom1.ftn line=871]`. Allocated full size only when `IQUAD >= 3` at `[file=src/swancom1.ftn line=1030]`; zero-size placeholder otherwise `[file=src/swancom1.ftn line=1042]`, `[file=src/swancom1.ftn line=1046]`.
- `MEMSINB(MDC, MSC, MCGRD)` (paired with `MEMSINA`) — Babanin/DBYB wind input workspace; declared `[file=src/swancom1.ftn line=876]`. Allocated only when `IWIND == 8` at `[file=src/swancom1.ftn line=1100-1104]`; zero-size placeholder otherwise `[file=src/swancom1.ftn line=1115-1116]`.
- Both reset to zero after allocation at `[file=src/swancom1.ftn line=1152]`, `[file=src/swancom1.ftn line=1157]`.
- Both also reset per-wet-point/per-bin during sweep setup at `[file=src/swancom1.ftn line=1545]`, `[file=src/swancom1.ftn line=1586]`.
- Both deallocated at end of `SWCOMP` at `[file=src/swancom1.ftn line=2466]`, `[file=src/swancom1.ftn line=2471]`.

## G. Per-process matrix workspace

`IMATDA, IMATRA, IMATLA, IMATUA, IMAT5L, IMAT6U` — all dimensioned `REAL :: (MDC, MSC)` at `[file=src/swancom1.ftn line=5349-5351]`.

Solver routines explicitly zero all six arrays after use at `[file=src/swancom1.ftn line=9441-9446]`.

**OpenMP semantics** — these arrays are NOT in the explicit shared/private list of the `DEFAULT(SHARED)` region at `[file=src/swancom1.ftn line=1170]`, `[file=src/swancom1.ftn line=1175]`. They are **passed as routine-local arguments** in per-point/per-sweep calls at `[file=src/swancom1.ftn line=2947-2951]`, `[file=src/swancom1.ftn line=2983]`, so each thread/invocation gets its own routine-local copy. This is why parallel runs don't corrupt the matrix workspace despite the SHARED default.

## Working Rules

1. To debug action density at a specific point: `AC2(:, :, KGRPNT(IX, IY))` is the structured access; for unstructured use `AC2(:, :, vertex_index)`.
2. For interpolation between time levels, `AC1` and `AC2` are both populated only in nonstationary; in stationary `AC1` is unallocated.
3. `COMPDA(:, JDP2)` is the **wet** depth at new time level (after water-level update). `COMPDA(:, JDP1)` is the previous time level (used for time interpolation in source terms).
4. `MEMNL4`/`MEMSINB` are zero-sized when their respective options are off — `IF (ALLOCATED(MEMNL4))` checks won't disambiguate; check `IQUAD` / `IWIND` instead.

## Common Pitfalls

- **Hot-restart spec mismatch**: if MDC, MSC, or MCGRD differ between runs, `AC2` allocation is a different shape. Hot-start file format embeds these dimensions; mismatch = fatal at read.
- **Custom `COMPDA` field index** — adding a new field requires updating both the index constant in `swanmain.ftn:1498-1527` and `MCMVAR` in the allocation. Forgetting one corrupts neighboring fields.
- **OpenMP bug fingerprint**: if you see "matrix corrupted" only with `OMP_NUM_THREADS > 1`, check that any custom code added to the source-term loop didn't use a SHARED variable when it should have been PRIVATE.
- ▢ User-experience cases — placeholder.

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swmod1.ftn`, `src/swmod2.ftn` — module declarations.
- `src/swanmain.ftn` — runtime arrays, OpenMP region.
- `src/swancom1.ftn` — solver workspace, MEM tables.
- `src/SwanGriddata.ftn90` — unstructured grid module.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 50+ file:line citations |
| Coverage | all primary in-memory data structures and their allocation lifecycle |
| Review status | `review_required: true` |
