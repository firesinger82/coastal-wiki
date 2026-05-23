---
title: "swan boundary implementation"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-boundary-implementation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN boundary processing — SWBOUN parsing + nest file readers + runtime injection

## Scope note

End-to-end mapping of SWAN's boundary system: how a `BOUND` line in the command file gets parsed (`SWBOUN`), how external spectrum files (NESTOUT, WAM-NEST, WAVEWATCH III) are read, how stored boundary spectra get applied to the model state `AC2` at boundary points during the run, and the internal data structures that connect them.

Companion to `swan-command-file-reference.md` (covers BOUND command syntax) and `swan-source-terms-implementation.md` (covers source-term injection elsewhere in the matrix). This note covers the boundary-only path.

## Source basis

- **Codex deep code analysis** 2026-05-06 of:
  - `/mnt/e/models/swan/source_code/swan/src/swanpre1.ftn` — top-level `SWREAD` dispatch
  - `swanpre2.ftn` — `SWBOUN` body (parametric shapes, segments, sides), `BCFILE`/`BCWAMN`/`BCWW3N` (file readers)
  - `swanmain.ftn` — runtime injection (`SNEXTI`, `RBFILE`, `SINTRP`)
  - `swmod2.ftn` — boundary type definitions

## A. SWBOUN body — parsing flow

### Dispatch from SWREAD

`SWREAD` swaps in **global** grid dimensions before calling `SWBOUN`, so all boundary parsing operates on global grid indexing (relevant for parallel runs):

```fortran
swanpre1.ftn:1873-1883
  swap MXC/MYC/MCGRD/NGRBND <- MXCGL/MYCGL/MCGRDGL/NGRBGL
  CALL SWBOUN(...)
  swap back
```

### Top-level parse order (within SWBOUN)

`SWBOUN` body at `[file=src/swanpre2.ftn line=2779-3002]` dispatches in this order:
1. `SHAP...` (shape defaults)
2. `WAMN...` (WAM-NEST file)
3. `WW3` / `WWIII` (WaveWatch III file)
4. `NE...` (SWAN nest file)
5. (else) — fall through to side/segment definitions

So SHAPESPEC must come **before** any side/segment definitions in the `.swn` file.

### Parametric frequency-shape dispatch

At `[file=src/swanpre2.ftn line=2802-2819]`:
- `JON` → `FSHAPE = 2` (+ optional `GAMMA`)
- `PM` → `FSHAPE = 1`
- `GAUS` → `FSHAPE = 4` (+ `SIGFR` stored to `PSHAPE(2)` in rad/s)
- `BIN` → `FSHAPE = 3`
- `TMA` → `FSHAPE = 5` (+ `GAMMA`, `D`)

### Frequency convention and DSPR

At `[file=src/swanpre2.ftn line=2821-2835]`:
- `MEAN` flips sign of `FSHAPE` (negative encodes mean period instead of peak); default is `PEAK`
- `DSPR DEGR` → `DSHAPE = 1` (degrees)
- `DSPR POW` → `DSHAPE = 2` (power)

This is why a wrong `MEAN` vs `PEAK` setting produces wave energy at half/twice the intended frequency — the negative sign on `FSHAPE` is the encoding.

### SEGMENT path

At `[file=src/swanpre2.ftn line=3063-3191]`:
- Coordinate mode parsed: `XY/LOC` (geographic) or `IJ/GRI/K` (grid index)
- Reads segment endpoint pairs via `READXY` (geographic) or `ININTG` (integer)
- Converts geographic to grid indices via `CVMESH` / `SwanFindPoint`
- Stores selected boundary points as a linked list under `TMP%JX/JY`

### SIDE path

At `[file=src/swanpre2.ftn line=3329-3519]`:
- Side keyword parsed: `N/NW/W/SW/S/SE/E/NE`
- Direction modifier: `CCW` (default) or `CLOCKW`
- Computes best matching computational side index `ISIDM`
- Resolves end indices `(IX1, IY1) → (IX2, IY2)`
- Optionally swaps endpoints based on orientation
- Walks that side accumulating boundary points

### Boundary-point mapping records

Each computational boundary point gets a 6-element tuple stored in `BGPTMP%BGP(1..6)` at `[file=src/swanpre2.ftn line=3692-3702]` and `[file=src/swanpre2.ftn line=3836-3847]`:
- `BGP(1)` — grid point index
- `BGP(2)` — type flag
- `BGP(3), BGP(4)` — weight1, spectrum1 (interpolation source)
- `BGP(5), BGP(6)` — weight2, spectrum2

This is the linkage between geographic boundary points and spectral storage.

## B. Boundary spectrum file readers

### NESTOUT format (.bnd, SWAN-native)

- Header reader: `BCFILE` at `[file=src/swanpre2.ftn line=3878-4366]` reads SWAN/TPAR header, locations, `FREQ` grid, `DIR` grid, quantity metadata into `BSPFIL` structures.
- Runtime spectrum loop: `RBFILE` calling `RESPEC` at `[file=src/swanmain.ftn line=7796-7963]` per boundary point per time step.

### WAM-NEST format

- Header reader: `BCWAMN` at `[file=src/swanpre2.ftn line=4369-4952]` reads WAM resolution/header, pre-scans points; per-point read at `[file=src/swanpre2.ftn line=4709-4756]`.
- Runtime: `[file=src/swanmain.ftn line=7823-7847]` and `[file=src/swanmain.ftn line=7961-7963]`.

### WAVEWATCH III format

- Header reader: `BCWW3N` at `[file=src/swanpre2.ftn line=4956-5468]` reads WW3 header/freq/dir + point metadata; per-point loop `[file=src/swanpre2.ftn line=5327-5392]`.
- Runtime: `[file=src/swanmain.ftn line=7848-7873]`, `[file=src/swanmain.ftn line=7883-7891]`, `[file=src/swanmain.ftn line=8403-8418]`.

### Spectral grid consistency — IMPORTANT

**No hard equality check** between file's frequency/direction grid and computational `SPCSIG`/`SPCDIR`. Instead spectra are remapped via `CHGBAS`:
- Direction interpolation: `[file=src/swanmain.ftn line=8450-8453]`
- Frequency interpolation: `[file=src/swanmain.ftn line=8481-8483]`

Implication: nesting from a coarser SWAN run with **a different spectral grid** will work but uses linear remapping (not exact). For tightly-validated cases, ensure both runs share `SET FREQ` and `SET DIR`.

The reader does validate **coordinate-type compatibility** (Cartesian vs spherical) at `[file=src/swanpre2.ftn line=4125-4129]` (`LOC` vs `LONLAT` against `KSPHER`).

## C. Boundary application during the run

### Time-stepped update (nonstationary)

`SNEXTI` at `[file=src/swanmain.ftn line=6908-6919]` updates each boundary file via `RBFILE`. `RBFILE` refreshes/interpolates `BSPECS(:,:,:,1)` to current model time `TIMCO`.

### Injection into AC2

`[file=src/swanmain.ftn line=6937-6946]` is the actual injection:
- For each boundary grid point, spatial interpolation between two stored boundary spectra (`K1`, `K2`, weights from `BGRIDP`) is computed.
- Result is written **directly** into `AC2(1, 1, INDXGR)` via `SINTRP`.

So boundary spectra **overwrite** `AC2` at boundary points each time step — not added, not averaged.

### STAT vs NONSTAT in RBFILE

At `[file=src/swanmain.ftn line=7724-7750]` and `[file=src/swanmain.ftn line=8033-8057]`:
- Stationary file → single spectrum, no time interpolation
- Nonstationary file → maintains old + new spectra, linearly interpolates in time using weight `W1` before `SNEXTI` applies them

## D. Internal data structures

### BSPCDAT (per-file metadata)

`[file=src/swmod2.ftn line=672-677]`:
```fortran
TYPE BSPCDAT
  INTEGER :: BFILED(20)
  INTEGER :: BSPLOC(:)
  REAL    :: BSPDIR(:), BSPFRQ(:)
END TYPE
```
- `BFILED` — file unit + flags
- `BSPLOC` — mapping into global `BSPECS` index
- `BSPDIR/BSPFRQ` — file's spectral grid (used by CHGBAS for remapping)

### BSDAT (parametric spec definitions)

`[file=src/swmod2.ftn line=682-687]`:
```fortran
TYPE BSDAT
  INTEGER :: NBS
  INTEGER :: FSHAPE, DSHAPE
  REAL    :: SPPARM(4)   ! Hs, Tp, dir, dspr/power
END TYPE
```

### BGPDAT (point mapping)

`[file=src/swmod2.ftn line=692-695]`:
```fortran
TYPE BGPDAT
  INTEGER :: BGP(6)   ! the 6-tuple from SWBOUN
END TYPE
```

### Runtime arrays in swanmain

`[file=src/swanmain.ftn line=433-435]` and `[file=src/swanmain.ftn line=3673-3674]`:
- `BSPECS(MDC, MSC, NBSPEC, 2)` — old/new boundary spectra
- `BGRIDP(6 * NBGRPT)` — flattened mapping (`BGP` records concatenated)

### Boundary-point ID assignment

At `[file=src/swanpre2.ftn line=5629]`, `[file=src/swanpre2.ftn line=5717-5720]`, `[file=src/swanpre2.ftn line=5794-5797]`, `IBSP1`/`IBSP2` get assigned (= `NBSPEC + ...`) and weighted indexes are stored into `BGP(3..6)` for each computational boundary point.

## E. SHAPESPEC defaults

- **JONSWAP/TMA `GAMMA`**: 3.3 if not given — `[file=src/swanpre2.ftn line=2805]` and `[file=src/swanpre2.ftn line=2817]`.
- **Period convention**: `PEAK` is default; `MEAN` is encoded by **negating `FSHAPE`** — `[file=src/swanpre2.ftn line=2821-2825]`.
- **`DSPR` mode**: parsed at `[file=src/swanpre2.ftn line=2828-2835]`; spread/power stored in `SPPARM(4)` via `DD` input at `[file=src/swanpre2.ftn line=3626-3635]`.

## Decision Guide — boundary debugging

| Symptom | Likely cause | Where to look |
|---------|--------------|---------------|
| Wrong wave height at boundary | Wrong shape: `MEAN` vs `PEAK` | `FSHAPE` sign at `swanpre2.ftn:2821-2825` |
| Nesting from coarse run loses high frequencies | Frequency range mismatch + linear remap | `CHGBAS` calls, `swanmain.ftn:8481-8483` |
| Boundary file format mismatch (WAM/WW3/SWAN) | Wrong reader called | Check `BOUND` keyword (`NE` vs `WAMN` vs `WW3`) at `swanpre2.ftn:2779-3002` |
| Spectrum injected at wrong points | Side/segment mismatch in coordinates | `SEG`/`SIDE` parse at `swanpre2.ftn:3063` (SEG) and `3329` (SIDE) |
| Time alignment wrong (nonstat) | `TIMCO` mismatch with file | `RBFILE` interpolation at `swanmain.ftn:8033-8057` |
| Nested run hangs at boundary | File length too short for run window | `RBFILE` end-of-file handling (search for IOSTAT) |

## Working Rules

1. **`SHAPESPEC` first**, then segment/side. Reverse breaks the parser.
2. **For nesting, share `SET FREQ` and `SET DIR`** between coarse and fine. SWAN remaps automatically but quality drops at the edges of the file's spectral range.
3. **Coordinate mode** (`LOC` vs `IJ`) must match the grid type chosen at `CGRID`. The SEGMENT path checks; the SIDE path infers.
4. Boundary spectra in `BSPECS` are **overwriting** `AC2` at boundary points each time step, not added. So a stale time stamp in the file silently propagates the wrong spectrum.

## Common Pitfalls

- **`MEAN` typo** — accidentally typing `MEAN` when you wanted `PEAK` flips frequency interpretation through the `FSHAPE` sign trick; result quietly wrong.
- **Different freq grid in nested file** — auto-remap covers it but degrades; for tight validation, regenerate coarse run with the fine grid's `SET FREQ`.
- **No CGRID consistency error** — SWAN won't fail on grid mismatch; you must check the `BSPDIR`/`BSPFRQ` recorded in the boundary file vs your run's `SPCSIG`/`SPCDIR`.
- **Side `CCW` vs `CLOCKW` confusion** — produces inverted endpoint order; spectra get swapped along the boundary.
- ▢ **User-experience cases** — placeholder.

## Next expansion

- `RBFILE` internals (the per-time-step header/spectrum read with all branches).
- ADCIRC-SWAN coupled boundary handling (separate, depends on the unstructured path).
- WAM-NEST format detail (the most fragile reader; older format).

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swanpre1.ftn` — `SWREAD` boundary dispatch, global-grid swap.
- `src/swanpre2.ftn` — `SWBOUN`, `BCFILE`, `BCWAMN`, `BCWW3N` (parsers + readers).
- `src/swanmain.ftn` — `SNEXTI`, `RBFILE`, `SINTRP` (runtime injection).
- `src/swmod2.ftn` — `BSPCDAT`, `BSDAT`, `BGPDAT` type definitions.

### Manual cross-reference

- `[file=pdf:swan:swantech]` ch.4 page 125 — Wave boundary and initial conditions.
- `[file=website:swan:node27]` — Boundary and initial conditions section.
- `[file=website:swan:node64]` — Wave boundary and initial conditions detail.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex source scan | 30+ file:line citations |
| Coverage | parsing flow, three nest readers, runtime injection, internal types, SHAPESPEC defaults |
| Out of scope | RBFILE per-format internals, ADCIRC-SWAN coupling |
| Review status | `review_required: true` |
