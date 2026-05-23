---
slug: xbeach_swan_handoff
title: XBeach SWAN Spectrum Hand-off (read_swan_file, FILELIST, LOCLIST, internal interpolation)
model: xbeach
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary
---

## Scope

XBeach `read_swan_file` reading SWAN ASCII spectral output: expected sections (`RFREQ/AFREQ`, `NDIR/CDIR`, `VaDens/EnDens`, `FACTOR`, frequency × direction matrix), internal reconstruction with `EnDens` → variance density conversion, mandatory interpolation to fixed XBeach grid (`nfint=801`, `naint=401`), `FILELIST` for time-varying spectra and `LOCLIST` for spatial spectra, the difference from JONSWAP parametric path, validation gaps (SWAN frequency may not be monotonically increasing), and typical workflow. Use this when wiring SWAN→XBeach coupling for storm runs.

## Source basis

- `wave_boundary_update.f90:58, 120-187, 264-1323` — SWAN reading + interpolation.
- `wave_boundary_main.f90:318-349` — LOCLIST.
- `params.F90:482, 1593, 2671` — `dthetaS_XB`, `wbctype` validation, `instat=swan` mapping.
- `interp.F90:70-96` — interpolation routines.
- `waveparamsnew.F90:488-672` — JONSWAP comparison.

## A. Expected file format (read_swan_file)

ASCII SWAN spectrum file:

1. Scans for `RFREQ` or `AFREQ`, reads `nf`, then one frequency per line (`wave_boundary_update.f90:848-867`).

2. Requires `NDIR` or `CDIR`, reads `nang`, then one direction per line (`:883-898`).

3. Skips `QUANT` scaffolding; requires `VaDens` or `EnDens`, reads exception value, searches for `FACTOR`, reads factor, reads `nf × nang` matrix (`:964-1007`).

## B. SWAN 2D spectrum blocks

Frequency block: `RFREQ` or `AFREQ`. Code does **not actually transform** relative ↔ absolute frequencies, despite comment (`:875`).

Direction block: `NDIR` (nautical, converted via `270 - direction`) or `CDIR` (Cartesian, rotated by `par%dthetaS_XB`) (`:910-916`).

Matrix is **frequency-major**: each row = one frequency, columns = direction bins (`:1008-1010`).

## C. Internal reconstruction

Internal storage: `S(nf, nang), f(nf), ang(nang)`, direction-integrated `Sf(nf)` (`:9`).

After reading (`:1019-1068`):
- Exception values zeroed.
- Direction order flipped/reordered if needed.
- SWAN `FACTOR` applied.
- `EnDens` → variance density: `÷ (rho · g)`.
- Degrees → radians: `·180/π` (target `m²/Hz/rad`).
- `Sf` reconstructed by trapezoidal angular integration over `S`.

## D. Interpolation to fixed grid

SWAN input loaded as-is, then **interpolated to XBeach standard grid**: `nfint=801, naint=401` (`:58, 134`).

Target frequency: `0..fmax`, `df=fmax/(801-1)` (`:1277`).
Target direction: `0..2π`, 401 bins (`:1283`).

2D interpolation uses `linear_interp_2d(..., 'interp', 0)` — outside source extent → zero (`:1305`, `interp.F90:70`).

XBeach corrects each interpolated frequency row to match original `Sf` (`:1320-1323`).

So interpolation is **mandatory** even when bins match — XBeach rebuilds onto its standard grid.

## E. Multiple spectra over time / space

**Time-varying**: file starts with `FILELIST`; rows = `rtbc dtbc readfile`:
- Read current line, apply morphological-time correction to `rtbc`, increment `listline`, read SWAN file (`:264-304`).

**Spatial**: master file starts with `LOCLIST`, rows = `x y filename`. Sub-files may themselves be `FILELIST` (`wave_boundary_main.f90:318-349`).

So multi-spectrum cases combine `LOCLIST` (per-location) + `FILELIST` (per-time per location).

## F. Difference from JONSWAP parametric

JONSWAP **does not read 2D matrix**; reads parameters (`waveparamsnew.F90:488-672`):
- `Hm0, Tp` or `fp`, `gammajsp`, `s` (spreading), `mainang`/`dir0`.

Constructs synthetic grid, generates JONSWAP shape, optional TMA, scales to `Hm0`, applies cosine spreading, fills `S(ii,i) = y(ii) · Dd(i)`.

For Korean coast realistic spectra: SWAN hand-off preferred; JONSWAP for sensitivity tests.

## G. Limitations / validation gaps

Hard failures: missing `NDIR/CDIR`, `VaDens/EnDens`, `ZERO`, `NODATA`, general read errors (`:893-997`).

**Important limitation**: code comments SWAN `f` "not monotonically increasing in most simulations", but downstream `linear_interp` expects ascending sorted X (`:861`, `interp.F90:96`).

**Validation gap**: this is real unless upstream SWAN output is sorted manually before use.

`wbctype=swan` rejected for stationary wave model (`params.F90:1593`).

`dthetaS_XB` only read for SWAN BCs, bounded `-360..360` (`:482`).

## H. Typical workflow

1. Set `instat = swan` → maps to `wbctype=swan`, `wavemodel=surfbeat` unless already nonhydrostatic (`params.F90:2671`).

2. Provide `bcfile` as:
   - One SWAN spectrum file.
   - `FILELIST` of time-varying SWAN files.
   - `LOCLIST` of spatial locations + per-location files.

3. XBeach reads spectra → interpolates to standard grid → combines for representative wave-train selection → generates wave components → maps variance along offshore boundary → writes `eebc, qxbc/qybc` or nonhydrostatic time series (`wave_boundary_update.f90:120-187`).

## Decision Guide

| Need | Setup |
|---|---|
| Single steady SWAN spectrum | `instat=swan, bcfile=spec.swn` |
| Time-varying (storm) | `instat=swan, bcfile=filelist.txt` (with FILELIST header) |
| Spatial variation along boundary | `instat=swan, bcfile=loclist.txt` (with LOCLIST header) |
| 2D map of SWAN spectra | `LOCLIST` + per-location `FILELIST` |
| Reproducibility (no random) | `random=0` plus `bcfile` |
| Storm validation | SWAN at multiple times during peak |
| Quick parametric study | JONSWAP `wbctype=parametric` (no SWAN file) |

## Working Rules

- Verify SWAN frequency monotonic before using (sort if needed externally).
- `dthetaS_XB` typically 0 for grid-aligned coast; non-zero if XBeach grid rotated relative to SWAN.
- For Korean storm: SWAN hindcast at hourly intervals; FILELIST of those for time-varying coupling.
- Output `eebc` to verify SWAN spectrum was applied correctly.
- If using `EnDens`, ensure SWAN computes energy density (not variance density directly).
- Stationary XBeach + SWAN: not allowed; use surfbeat or nonh.

## Common Pitfalls

- ▢ Non-monotonic SWAN frequency — silent interpolation error.
- ▢ SWAN 2D spectrum without `VaDens`/`EnDens` keyword — read fails.
- ▢ Setting `wavemodel=stationary` with `instat=swan` — rejected.
- ▢ Time gap between SWAN files larger than `rtbc` — XBeach extrapolates first/last spectrum.
- ▢ `LOCLIST` with insufficient locations along boundary — interpolation gaps.
- ▢ `dthetaS_XB` wrong sign or magnitude — direction off.
- ▢ Comparing JONSWAP and SWAN-driven runs assuming equivalence — different physics; use one consistently.

## References

- Roelvink et al. 2009 (XBeach SWAN coupling).
- SWAN User Manual (spectrum output).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
