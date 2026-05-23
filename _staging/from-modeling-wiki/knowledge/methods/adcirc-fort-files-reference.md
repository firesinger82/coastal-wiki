---
slug: adcirc-fort-files-reference
title: ADCIRC fort.* files — purpose, I/O, and connectivity
category: methods
model: adcirc
auto_draft: false
authored_by: claude-opus-4-7
review_required: true
generated: 2026-05-05
basis: source code (codex scan) + curated wiki/manuals (RAG)
---

# ADCIRC fort.* files — purpose, I/O, and connectivity

## Scope note

This note maps every standard `fort.NN` filename in an ADCIRC run to:
- **purpose** (what the file holds),
- **I/O direction** (input / output / both),
- **reader/writer subroutine** with `file:line` from the v55 source tree,
- **manual reference** (ADCIRC Wiki / official PDFs) where the format/parameters are documented,
- **dependencies** (which other `fort.*` files or fort.15 controls drive it).

Coverage focuses on the main solver path under `/mnt/e/models/adcirc/source_code/adcirc/{src,prep,util,wind}/`. Parallel-only artifacts (per-PE `fort.18`, MPI staging) and clearly deprecated units (e.g., legacy `fort.33` solver log) are noted but not detailed.

## Source basis

- **Source-code map** — built 2026-05-05 by scanning `OPEN/READ/WRITE/CLOSE` statements across the main solver tree via Codex (`gpt-5.3-codex`). Cited as `[file=src/... line=N]`.
- **Manual cross-reference** — retrieved via rag_proxy against the `manuals` collection filtered to `model=adcirc` (15 K chunks: official PDFs, ADCIRC Wiki, workshop materials). Cited as `[file=wiki:adcirc:Fort.NN_file]` or `[file=pdf:adcirc:<stem> page=N]`.

Both source and manual citations are preserved per claim. When the two disagree, the source code is treated as ground truth.

## Why this note exists

Every ADCIRC run reads at least `fort.14` + `fort.15` and writes a subset of `fort.61–93` according to flags inside `fort.15`. The full mapping is fragmented across the User Manual, the Theory document, and dozens of wiki pages. A single reference (with file:line citations into the actual reader) lets future debugging skip the manual scan and go straight to the right subroutine.

## File inventory

### Required input files

| fort# | Purpose | Reader | Source citation | Manual reference |
|-------|---------|--------|-----------------|------------------|
| **14** | Mesh geometry: nodes, elements, boundary conditions | `read_global` / `readMesh` | `[file=src/read_input.F line=380]`, `[file=prep/read_global.F line=96]` | `[file=wiki:adcirc:Fort.14_file]` — "contains the grid coordinates, element identifiers and boundary conditions for the model run" |
| **15** | Master control: physics flags (NOLIBF/NOLIFA/NOLICA), forcing selectors (NWS, NTIP), output specifiers (NOUT*) | `READ_INPUT`, `READ_INPUT_3D` | `[file=src/read_input.F line=394]`, `[file=src/read_input.F line=5296]` | `[file=wiki:adcirc:Fort.15_file]`; key parameters at `[file=wiki:adcirc:NOLIBF]`, `[file=wiki:adcirc:NOLIFA]`, `[file=wiki:adcirc:NWS]` |

### Optional input files (selected by `fort.15` flags)

| fort# | Purpose | Activation flag (in fort.15) | Reader | Source citation | Manual reference |
|-------|---------|------------------------------|--------|-----------------|------------------|
| **13** | Nodal attributes (Manning's n, primitive weighting, bridge piers, surface canopy, etc.) | `NWP > 0` | `ReadNodalAttr` | `[file=src/nodalattr.F line=1141]`, `[file=src/nodalattr.F line=1154]` | `[file=wiki:adcirc:Fort.13_file]`; e.g. `mannings_n_at_sea_floor` `[file=wiki:adcirc:Manning_s_n_at_sea_floor]` requires `NOLIBF=1` |
| **22** | Meteorological forcing (wind/pressure) — format selected by NWS | `NWS != 0` | `WIND` / `OWIWIND` | `[file=src/wind.F line=1812]`, `[file=src/owiwind.F line=188]`, `[file=src/wind.F line=910]` | `[file=wiki:adcirc:NWS]` — selects format (NWS=12 OWI legacy, NWS=13 OWI NetCDF, etc.) |
| **23** | Wave radiation stress forcing (one-way wave coupling) | `NRS != 0` | `RS2INIT` (cold start), reopened in hot start | `[file=src/rs2.F line=89]`, `[file=src/cstart.F line=313]` | `[file=wiki:adcirc:Fort.23_file]` |
| **24** | Self-attraction and loading (SAL) tide-by-tide | `NTIP > 0` with SAL terms | `READ_INPUT` | `[file=src/read_input.F line=6425]`, `[file=src/read_input.F line=6453]` | `[file=wiki:adcirc:Fort.24_file]`; format note: `[file=wiki:adcirc:Fort.24_file_format]` — "first four lines for each constituent must be present but are skipped during read" |
| **25** | OWI ice forcing (concentration) | NWS variants with ice | `NCICE1_INIT` | `[file=src/owi_ice.F line=99]`, `[file=src/owi_ice.F line=107]` | (no dedicated wiki page; format follows OWI met conventions) |

### Output files — 2D station / global

Activation: each is gated by a `NOUT*` flag in `fort.15` (e.g., `NOUTE`, `NOUTGE`, `NOUTV`).

| fort# | Purpose | Flag | Writer | Source citation | Manual reference |
|-------|---------|------|--------|-----------------|------------------|
| **61** | Elevation time series at recording stations | `NOUTE`, `NSTAE` | `initOutput2D` / `writeOutput2D` (also reopened in cold/hot start) | `[file=src/write_output.F line=510]`, `[file=src/cstart.F line=376]` | `[file=wiki:adcirc:Fort.61_file]` |
| **62** | Velocity time series at recording stations | `NOUTV`, `NSTAV` | same family | `[file=src/write_output.F line=546]`, `[file=src/cstart.F line=394]` | (sibling of fort.61) |
| **63** | Elevation field at all nodes | `NOUTGE` | same family | `[file=src/write_output.F line=598]`, `[file=src/cstart.F line=487]` | (mesh from `fort.14`) |
| **64** | 2D depth-averaged velocity field at all nodes | `NOUTGV` | same family | `[file=src/write_output.F line=710]`, `[file=src/cstart.F line=584]` | — |
| **75** | Time-varying bathymetry field output | `TimeBathyControl` namelist | same family | `[file=src/write_output.F line=946]`, `[file=src/cstart.F line=467]` | — |
| **81** | Concentration time series at stations | `NOUTC` (with `IM=10`) | same family | `[file=src/write_output.F line=1160]`, `[file=src/cstart.F line=412]` | — |
| **83** | Concentration field at all nodes | `NOUTGC` | same family | `[file=src/write_output.F line=1191]`, `[file=src/cstart.F line=665]` | — |
| **90** | Tau0 (primitive-weighting tau) field output | `OutputTau0` flag in fort.15 | same family | `[file=src/write_output.F line=619]`, `[file=src/cstart.F line=501]` | depends on `tau0` nodal attribute via fort.13 |
| **92** | Sponge-layer field output | sponge options in fort.15 | same family | `[file=src/write_output.F line=641]`, `[file=src/cstart.F line=492]` | — |

### Output files — meteorological

Driven by met forcing (`fort.22`) and met output flags in fort.15.

| fort# | Purpose | Flag | Writer | Source citation | Manual reference |
|-------|---------|------|--------|-----------------|------------------|
| **71** | Atmospheric pressure at met stations | `NOUTM` | `initOutput2D` / `POST71` | `[file=src/write_output.F line=735]`, `[file=prep/post.F line=1921]` | format flag `[file=wiki:adcirc:Fort.91_file_format]` family |
| **72** | Wind velocity at met stations | `NOUTM` | `POST72` | `[file=src/write_output.F line=775]`, `[file=prep/post.F line=2190]` | — |
| **73** | Atmospheric pressure field at all nodes | `NOUTGW` | `POST73` | `[file=src/write_output.F line=817]`, `[file=prep/post.F line=2476]` | `[file=wiki:adcirc:Fort.93_file_format]` — "ascii or binary depending on NOUTGW" |
| **74** | Wind stress/velocity field at all nodes | `NOUTGW` | `POST74` | `[file=src/write_output.F line=904]`, `[file=prep/post.F line=2724]` | — |
| **91** | Ice concentration at met stations | NWS ice variants | `POST91` | `[file=src/write_output.F line=1064]`, `[file=prep/post.F line=2990]` | — |
| **93** | Ice concentration field at all nodes | NWS ice variants | `POST93` | `[file=src/write_output.F line=1039]`, `[file=prep/post.F line=3262]` | — |

### Output files — 3D station

| fort# | Purpose | Flag | Writer | Source citation |
|-------|---------|------|--------|-----------------|
| **41** | 3D density / salinity / temperature at stations | `I3DSD`, `NSTA3DD` | `initOutput3D` / `writeOutput3D`; `POST41` merge | `[file=src/write_output.F line=2993]`, `[file=prep/post.F line=4285]` |
| **42** | 3D velocity at stations | `I3DSV`, `NSTA3DV` | same family; `POST42` merge | `[file=src/write_output.F line=3059]`, `[file=prep/post.F line=4452]` |

### Output files — harmonic analysis

Activated when harmonic-analysis options in fort.15 are set (`NHASE`, `NHASV`, `NHAGE`, `NHAGV`, `NFREQ`).

| fort# | Purpose | Flag | Writer | Source citation |
|-------|---------|------|--------|-----------------|
| **51** | Harmonic elevation at stations | `NHASE`, `NFREQ` | `writeHarmonicAnalysisOutput`; `POST51` merge | `[file=src/write_output.F line=2178]`, `[file=prep/post.F line=1306]` |
| **52** | Harmonic velocity at stations | `NHASV` | `POST52` merge | `[file=src/write_output.F line=2232]`, `[file=prep/post.F line=1420]` |
| **53** | Harmonic elevation at all nodes | `NHAGE` | `POST53` merge | `[file=src/write_output.F line=2339]`, `[file=prep/post.F line=1533]` |

### Special / parallel / deprecated

| fort# | Note | Source citation |
|-------|------|-----------------|
| **33** | Deprecated legacy iterative-solver log unit; superseded by `openLogFile` (`fort.16` and the modern logging module) | `[file=src/gwce.F line=148]`, `[file=src/logging.F90 line=343]` |
| **65** | Secondary comparison-dataset unit used only in the post-processing compare utility (not part of a normal run) | `[file=prep/compare.F line=1696]` |
| **80** | Domain-decomposition + I/O mapping metadata; written by `PREP80`, read by `POST_INIT` to merge per-PE outputs | `[file=prep/prep.F line=7439]`, `[file=prep/post.F line=67]` |
| **82, 84, 85, 94, 95** | Not located by the main-solver scan. Likely ancillary output reserved by ADCIRCpy / FigureGen workflow or unused in the current trunk. | (not found in src/prep/util/wind scan 2026-05-05) |

## Connectivity graph

```
                    ┌────────────────────┐
                    │  fort.15 (control) │
                    │  - NWS, NWP, NTIP  │
                    │  - NOUT* flags     │
                    │  - harmonic setup  │
                    └────────┬───────────┘
                             │ drives
        ┌────────────┬───────┴────────┬──────────────┐
        ▼            ▼                ▼              ▼
   fort.14       fort.13         fort.22        fort.23/24/25
   (mesh)        (nodal attr)    (met forcing)  (waves / SAL / ice)
        │            │                │              │
        └────────────┴────────────────┴──────────────┘
                     │
                     ▼
              ADCIRC main loop
                     │
        ┌────────────┼────────────┬──────────────┬───────────────┐
        ▼            ▼            ▼              ▼               ▼
   fort.61–65   fort.71–74   fort.41–42    fort.51–53      fort.81/83/90/92
   (2D out)     (met out)    (3D station) (harmonic)     (concentration/tau0/sponge)
                     │
                     ▼
              fort.80 metadata
              merges per-PE outputs
              after parallel run
```

## Decision Guide

- **Cold-start vs hot-start affects which fort.* files are reopened**: `cstart.F` initializes `fort.61–65`, `fort.71–75`, `fort.81–93` from scratch; `hstart.F` reopens them from the existing files at the hot-start time. Mismatch in `fort.15` `NHSTAR`/`NHSINC` between the two runs causes silent file format drift.
- **Output flag sign convention**: `NOUTE`, `NOUTV`, etc. negative values switch ASCII vs binary output. Always cross-check with `[file=wiki:adcirc:Fort.91_file_format]` before consuming.
- **NWS bundles fort.22 format**: see `[file=wiki:adcirc:NWS]`. Examples — `NWS=12` OWI legacy, `NWS=13` OWI NetCDF (NetCDF code path different reader). Mixing NWS values between cold and hot start corrupts hot-restart.
- **Manning's n via fort.13 requires `NOLIBF=1`**: from `[file=wiki:adcirc:Fort.13_file Nodal Attributes]` — the run terminates if both are not consistent.

## Working Rules

1. Treat `fort.14` + `fort.15` as the canonical pair — never touch the mesh without keeping the matching `fort.15` (or you get mismatched `NSTAE`/`NSTAV` arrays).
2. Always inspect `fort.80` after a parallel run before opening `fort.61/62/...` — those files are split per PE before merge.
3. When writing scripts that consume ADCIRC output, branch on the file's HEADER (record 1 always carries `RUNDES`, `RUNID`, `AGRID`) — do not infer format from filename alone.
4. For harmonic analysis output (`fort.51–53`), the `NFREQ` block in `fort.15` must match the post-processed file or `POST51/52/53` will silently drop frequencies.

## Common Pitfalls

- **Hot-start ↔ output file mismatch** — restart with different `NOUT*` flag sign (ASCII↔binary) leaves a corrupted partial file. Set `NOUT*` consistently across runs.
- **fort.13 silent ignore** — if `NWP=0` in fort.15, the file is never read no matter what you put in it. Check `[file=src/nodalattr.F line=1051]` for `NWP` parsing.
- **NWS=14 vs NWS=13** — both NetCDF; different reader path. `[file=src/owiwind.F line=188]` shows the dispatch.
- ▢ **User-experience cases** — placeholder for project-specific incidents (wide6 forcing branch, JMA-MSM conversion, etc.). Add as encountered.

## Next expansion

- Per-output decoder reference (e.g., separate note for the binary record layout shared by `fort.61–65/71–75`).
- `fort.15` parameter-by-parameter reference (this note treats fort.15 as a black box; a follow-up note should enumerate the namelist groups: `&time`, `&output`, `&forcing`, `&3D`, etc.).
- Map of `fort.22` per NWS variant (table of expected record shape for NWS=2,3,4,5,6,7,12,13,14,15...).
- ADCIRCpy / pyadcirc reader cross-reference (which Python class consumes which fort.*).

## References

### Source code (this scan, 2026-05-05)

- `src/read_input.F` — main fort.15 reader (`READ_INPUT`, `READ_INPUT_3D`).
- `src/nodalattr.F` — fort.13 reader (`ReadNodalAttr`).
- `prep/read_global.F` — fort.14 mesh assembler.
- `src/wind.F`, `src/owiwind.F` — fort.22 / NWS-dispatched met readers.
- `src/rs2.F` — fort.23 wave radiation stress reader.
- `src/owi_ice.F` — fort.25 ice forcing reader.
- `src/cstart.F`, `src/hstart.F` — cold/hot start reopen logic for outputs.
- `src/write_output.F` — `initOutput2D` / `writeOutput2D` / `initOutput3D` / `writeOutput3D` writers.
- `prep/prep.F`, `prep/post.F` — `PREP80` writer / `POST*` mergers.
- `src/logging.F90` — modern logging (replaces fort.33).

Full subroutine inventory: `[file=/mnt/e/models/adcirc/manuals/refs/subroutines.md]`.

### Manuals (curated, retrieved 2026-05-05 against `manuals` collection, model=adcirc)

- `[file=wiki:adcirc:File_formats]` — top-level "Required: every run needs fort.14 + fort.15" statement.
- `[file=wiki:adcirc:Fort.14_file]`, `[file=wiki:adcirc:Fort.14_file_format]` — mesh format, boundary conditions reference.
- `[file=wiki:adcirc:Fort.15_file]`, plus per-parameter pages: `NOLIBF`, `NOLIFA`, `NWS`, `NWP`, `NTIP`, `NOUTE`, `NOUTGE`, …
- `[file=wiki:adcirc:Fort.13_file]`, `[file=wiki:adcirc:Manning_s_n_at_sea_floor]`, `[file=wiki:adcirc:Primitive_weighting_in_continuity_equation]`.
- `[file=wiki:adcirc:Fort.23_file]`, `[file=wiki:adcirc:Fort.24_file]`, `[file=wiki:adcirc:Fort.24_file_format]`.
- `[file=wiki:adcirc:Fort.61_file]`, `[file=wiki:adcirc:Fort.91_file_format]`, `[file=wiki:adcirc:Fort.93_file_format]`.
- `[file=wiki:adcirc:Grid_Development_and_Editing]` — fort.14 construction guidance.
- `[file=pdf:adcirc:2001_Blain01 page=25]` — Software Design Description; canonical line ordering of `NOLIBF NOLIFA NOLICA NOLICAT NWP NCOR NTIP NWS NRAMP G`.
- `[file=pdf:adcirc:f13BuilderPresADCIRC2014Final_TaylorAsher]` — fort.13 builder workshop slides.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 (this session) |
| Generated | 2026-05-05 |
| Source-scan tool | `codex exec --model gpt-5.3-codex` over `/mnt/e/models/adcirc/source_code/adcirc/{src,prep,util,wind}/` |
| RAG retrieval | rag_proxy on `manuals` collection, `model=adcirc` filter (15 K chunks) |
| Review status | `review_required: true` — modeler should validate file:line citations against current ADCIRC trunk version (this scan was r6155-equivalent / v55-line) |
| Auto re-run | Triggered by quarterly `refresh_models.sh` cron when ADCIRC source updates land |
