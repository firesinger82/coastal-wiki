---
title: "swan output formats"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-output-formats.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

SWAN's output dispatch system: `BLOCK` gridded output (`BLKP/BLKD/BLKV`), `TABLE` point output (`TABD/TABI/TABS/TABT/TABP`), 1D vs 2D spectral output (`SPEC1D`/`SPEC2D`), `NESTOUT` for parent-child nesting (writes spectral file consumed by `BOUND NEST`), NetCDF activation via build option (no `NCNAME` keyword), file naming/unit assignment, MPI per-rank file naming (`-NNN`), and the `OUTPUT tbeg deltt` time-frequency control. Use this when wiring outputs for a SWAN run, debugging spectrum file structure, or interpreting BLOCK vs TABLE files.

## Source basis

- `swanpre2.ftn:1160-1226, 1243, 1482-2467` — output parsers, frequency control.
- `swanout1.ftn:435, 681-706` — `SWOUTP` dispatch, `SWORDC` enable.
- `swanout2.ftn:178-2154` — writers, NetCDF routing, spectrum format.
- `swn_outnc.ftn90:1003-1641` — NetCDF variable definitions.
- `swanmain.ftn:1760-2277` — output variable types.
- `swanpre2.ftn:2649-4144` — `BOUND NEST`, `BCFILE`, `SwBOUN`.
- `ocpmix.ftn:1665-1849`, `swmod1.ftn:460` — file unit assignment.
- `src/CMakeLists.txt:26-95`, `switch.pl:34` — NetCDF build.

## A. BLOCK output (gridded)

Parsed as `BLOCK 'sname' HEADER/NOHEADER 'fname' ... <DSPR/HSIGN/DIR/.../TPS/...>` with optional `OUTPUT tbeg deltt` (`swanpre2.ftn:1160`).

Request types (`:1194`):

| Type | Meaning |
|---|---|
| `BLKP` | Paper / header text format |
| `BLKD` | Datafile / no-header format |
| `BLKV` | VTK filenames |

Variables resolved through `OVKEYW`. Examples:
- `HS`/`HSIGN` → ivtype 10 (`swanmain.ftn:1760`).
- `DIR` → 13 (`:1795`).
- `TPS` → 53 (`:2277`).

`SVARTP` matches against `OVKEYW` and aliases (`swanpre2.ftn:2452`).

Writer dispatch: `SWOUTP` → `SWBLOK / SWBLKP / SWBLKV` (`swanout1.ftn:435`).

Format: datafile writes each scalar/vector component as gridded block via `FLT_BLOCK`; `IDLA` controls ordering (`swanout2.ftn:560`). Header/paper writes frame/title/unit/time + x/y grid labels (`:510`).

## B. TABLE output (point)

Parsed as `TABLE 'sname' HEADER/NOHEADER/INDEXED 'fname' <...>` + optional `OUTPUT tbeg deltt` (`swanpre2.ftn:1565`).

Request types (`:1588`):

| Type | Meaning |
|---|---|
| `TABD` | Datafile (binary-friendly) |
| `TABI` | Indexed |
| `TABS` | SWAN-standard |
| `TABT` | SWAN-standard with time |
| `TABP` | Paper / formatted |

`SWTABP` writes one row per output point; continues if many quantities requested (`swanout2.ftn:1257`).

Headers (`:1410-1480`):
- `TABP/TABI`: run/table/version + quantity short names + units.
- `TABS/TABT`: `TIME, LOCATIONS` or `LONLAT, QUANT`, quantity metadata, units, exception values.

Rows fixed-field text:
- Time: `A18`.
- `TABD`: uses `FLT_TABLE`.
- Other: `F13.X`.
- Vector quantities: two columns.

## C. SPEC1D / SPEC2D

Parsed by `SPECOUT 'sname' SPEC1D/SPEC2D ABS/REL S/L 'fname' ... OUTPUT ...` (`swanpre2.ftn:1867`):
- `SPEC1D` → request type `SPE1`.
- `SPEC2D` → request type `SPEC`.

`SWSPEC` documents (`swanout2.ftn:1823`):
- `SPEC` = 2D spectral output.
- `SPE1` = 1D frequency spectrum.

File header: SWAN-standard spectral file, then optional `TIME, LOCATIONS/LONLAT, RFREQ` or `AFREQ`, frequency list. For 2D: `NDIR/CDIR` direction list (`:1907`).

Quantity:
- 2D: one `VaDens`/`EnDens` quantity, units `m²/Hz/degr` or `J/m²/Hz/degr` (`:1944`).
- 1D: three quantities — density, mean direction, directional spread (`:1977`).

Computation: `SWCMSP` (`:2154`):
- `|OTYPE|=2` for 2D.
- `|OTYPE|=1` for 1D (integrates over θ).

2D calls `WRSPEC`; 1D writes `LOCATION` and one line per frequency with density, direction, spread (`:2057`).

## D. NESTOUT (parent dump)

Parsed as `NESTOUT 'sname' 'fname' (OUTPUT tbeg deltnst ...)`; output point set must be type `N` (`swanpre2.ftn:1978`).

Internally creates output request `RTYPE='SPRC'` (`:2015`).

That means **spectral, relative-frequency, complete 2D directional output**, written through same `SWSPEC` machinery.

Resulting parent file is SWAN-standard spectral file with locations, `RFREQ`, directions, 2D density blocks — suitable as child boundary file (`swanout2.ftn:1934`).

## E. BOUND NEST (child consumption)

`SWBOUN` reads `BOUNDARY`. Structure explicitly documents `NEST: Read filename; Call BCFILE` (`swanpre2.ftn:2649`).

For file/spec boundary input, `SWBOUN` reads `FILE/SPEC`, increments boundary-file count, calls `BCFILE` (`:3666`).

`BCFILE` opens parent spectral file, reads `SWAN, TIME, LOCATIONS/LONLAT`, frequencies, directions, stores file characteristics. Spectral densities are read later by `RESPEC` during computation (`:4015`).

For `BCTYPE='NEST'`, file locations interpolate to child boundary grid points via `SWBCPT` (`:4144`).

So **NESTOUT writes; BOUND NEST reads** — same spectral file format.

## F. NetCDF (build option, no `NCNAME` keyword)

There is **no literal `NCNAME` symbol** in this source tree.

NetCDF activated by build option `NETCDF`:
- Appends `-netcdf` to `switch.pl` (`CMakeLists.txt:26`).
- `switch.pl` enables lines marked `!NCF` (`switch.pl:34`).
- CMake uses `srclistnc.cmake` and links NetCDF Fortran (`CMakeLists.txt:95`).

Runtime routing by `.nc/.NC` filename checks in `!NCF` paths for block/table/spec output (`swanout2.ftn:178, 1876`).

NetCDF variables defined via `STNAMES` (`swn_outnc.ftn90:1641`):
- `depth, xcur/ycur, hs, tm01, tp, theta0, spread, xwnd/ywnd, tps`.
- Partition variables.

`create_variables` defines map or point variables (`:1604`).

Spectral NetCDF also writes auxiliary `depth, currents, hs, wind` unless `NOAUX` (`:1003`).

## G. Units / file naming

Output requests store (`swanpre2.ftn:1243`):
- `OQI(1)=NREF`.
- `OQI(2)=request index`.
- `OQI(3)=number of variables`.
- `OUTP_FILES(NREOQ)=FILENM`.

If filename blank → output to `PRINTF`; otherwise `NREF=0` and writer opens later (`:1222`).

In MPI/parallel mode SWAN appends `-NNN` node numbers to many output filenames (`:1226, 1915`).

`FOR` assigns free unit numbers when `IUNIT=0`; qualifiers `O/N/S/U` and `F/U`; opens sequential formatted/unformatted (`ocpmix.ftn:1665`). Free unit search starts at `FUNLO`, skips reserved 411-417 (`:1849`).

Standard units: `INPUTF=3, PRINTF=4, SCREEN=6` (`swmod1.ftn:460`).

## H. Output frequency

`OUTPUT` parsed as pseudo-variable `IVTYPE=98` (`swanpre2.ftn:2467`).

For BLOCK/TABLE/SPEC/NESTOUT, `OUTPUT` reads:
- `tbeg` → `OQR(1)`.
- `delt` → `OQR(2)`.

Using `INCTIM/INITVD` (`swanpre2.ftn:1482, 1957, 2038`).

Runtime: `SWORDC` enables output (`swanout1.ftn:681`):
- If final time reached with negative interval.
- If `TIMCO >= TNEXT` with positive interval.
- Then advances next output time by `OUTR(2)`.

**Stationary mode always outputs** (`:706`) — once per stationary computation.

## Decision Guide

| Need | Output |
|---|---|
| Hsig map for plotting | `BLOCK 'COMPGRID' HEADER 'hs.dat' HSIGN OUTPUT t0 1 hr` |
| Hsig time series at gauge | `TABLE 'pts' HEADER 'hs_pts.dat' TIME XP YP HSIGN TPS DIR OUTPUT t0 30 min` |
| 1D frequency spectrum at point | `SPECOUT 'pts' SPEC1D ABS 'spec.dat'` |
| 2D directional spectrum | `SPECOUT 'pts' SPEC2D ABS 'spec2d.dat'` |
| Parent → child nesting | `NESTOUT 'nest_pts' 'nest.spec' OUTPUT t0 1 hr` |
| Child consumption | `BOUNDspec NEST 'nest.spec' OPEN` |
| NetCDF map output | Build with `NETCDF` flag; use `.nc` extension in filename |
| MPI parallel runs | Output filenames auto-append `-NNN` per rank |

## Working Rules

- Always use `HEADER` for `BLOCK/TABLE` unless you really want machine-readable raw data.
- For SPEC2D files, ensure `RFREQ`/`AFREQ` (relative vs absolute frequency) matches downstream tool expectations.
- For nesting: parent and child must use **compatible** frequencies and directions (typically same, or child wider range).
- Output frequency: BLOCK every 1 hour, TABLE every 15-30 min, SPEC at peak storm time only (very large files).
- NetCDF output requires SWAN built with `-DNETCDF` flag — verify with linker output.
- For parallel SWAN: `-NNN` files need post-processing to merge — use SWAN's `SWAN-merge` tool or manual concatenation.
- `BLKV` (VTK) useful for ParaView visualization.

## Common Pitfalls

- ▢ Looking for `NCNAME` keyword — doesn't exist; NetCDF activated by build flag + `.nc` filename.
- ▢ Setting `OUTPUT t0 1` thinking units are seconds — depends on `INCTIM` mode; check `MODE` settings.
- ▢ Stationary run outputting once per `MXITST` iteration — actually outputs once per stationary computation.
- ▢ SPEC2D file size — very large; restrict to a few stations and few output times.
- ▢ Output filename collision in MPI (without `-NNN` suffix support) — check that suffix is appended.
- ▢ Parent nest `NESTOUT` with too-coarse output frequency — child boundary stale between updates.
- ▢ `BOUND NEST` reading file with mismatched frequency bins — interpolation may produce zeros at child range edges.
- ▢ Forgetting `OUTPUT tbeg deltt` — output uses default (often once at end).

## Next expansion

- BLOCK variable list (full ivtype table).
- SPEC2D file format example.
- NetCDF SWAN viewer tool reference.
- SWAN-merge for MPI output post-processing.

## References

- SWAN User Manual (Output and Output options).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.
