---
title: "swan adcirc coupling"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-adcirc-coupling.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

SWAN-side mechanism for sharing the ADCIRC unstructured mesh (`fort.14`), how `READ UNSTRUC ADC` parses, where boundary spectra are interpolated to vertex AC2, time-stepping in coupled mode (host owns MPI/time advance), how wave-induced forces (`fx, fy`) are passed back to ADCIRC via `SwanComputeForce`, and the build path (SWAN library linked into `padcswan`). Use this when debugging the SWAN side of `padcswan`, configuring nesting on unstructured grids, or interpreting SWAN-side BC reads.

## Source basis

- `swanpre1.ftn:1462-1492, 1344-1350, 944-1286, 791-3074` — `READ UNSTRUC`, input grid types, propagation flags.
- `SwanReadADCGrid.ftn90:42-176`, `SwanGriddata.ftn90:54-72`, `SwanReadGrid.ftn90:73-78` — ADCIRC mesh reader.
- `swanmain.ftn:101-104, 128, 266-695, 1105-1109, 1110-1112, 4037-6960, 5053-5161, 8798-8823` — main loop, coupling flags.
- `swanparll.ftn:140-319` — MPI bypass in coupled mode.
- `swanpre2.ftn:2702-3151` — boundary list / segment validation.
- `SwanComputeForce.ftn90:35-307` — wave-driven force computation.
- `switch.pl:31, 93-96` — `-adcirc` switch.
- `src/CMakeLists.txt:26-117`, `srclist.cmake:28-64` — SWAN library build.

## A. Unstructured mesh (READ UNSTRUC ADC)

`READ UNSTRUC` parser at `swanpre1.ftn:1462-1492`:
- Default keyword: `ADC` → `grid_generator = meth_adcirc`, depth source `IGTYPE(1)=3`, calls `SwanReadGrid`.
- Triton (`TRI`), GMSH alternatives also supported.

`SwanReadADCGrid.ftn90:42-176`:
- Hard-codes `grdfil = 'fort.14'` and opens it (`:91-97`).
- Reads `ncells, nverts`, vertex coords + depth (`:103-123`).
- Reads triangle connectivity `kvertc(1:3, cell)` (`:126-136`).
- Loads ADCIRC open/land boundary markers into `vmark` (`:146-176`).

So **ADCIRC's `fort.14` is the single shared mesh** — no separate SWAN mesh file in coupled runs.

## B. Coupling interface (PADCSWAN_RUN, no `couple2adcirc`)

Standalone SWAN `PROGRAM` is **bypassed** in coupled mode (`swanmain.ftn:101-104`). ADCIRC's `couple2swan.F` calls SWAN via `PADCSWAN_INIT` / `PADCSWAN_RUN`; SWAN-side workhorse is `SWMAIN` (`swanmain.ftn:128`).

There is **no `couple2adcirc.F` in the SWAN tree** — coupling logic lives in ADCIRC's `couple2swan.F` (covered in `adcirc-swan-coupling.md`).

ADCIRC-specific preprocessing switch: `-adcirc` (`switch.pl:31, 93-94`); applied by uncommenting `!ADC` lines.

ADCIRC-coupled default drag note at `swanmain.ftn:1105-1109` — switch documented inline.

## C. Time stepping / MPI

SWAN normal loop (`swanmain.ftn:569-694`):
1. `SNEXTI` updates BC/input fields (`:586-595`).
2. Compute (`SWCOMP` for structured, `SwanCompUnstruc` for unstructured `OPTG=5`) (`:610-628`).
3. Output.
4. Advance: `TIMCO = TIMCO + DT`; printed as "Time of computation" (`:686-694`).

`DT, TINIC, TFINC, TIMCO` globals at `swmod1.ftn:2978-2993`.

**Coupled mode**: ADCIRC passes timestep to SWAN per source comment; **no return-timestep API** in this SWAN tree (`swanmain.ftn:101-104`). ADCIRC controls when SWAN runs.

**MPI**: init/finalize omitted in coupled (`!NCOH`) builds; **host owns MPI** (`swanparll.ftn:140-319`, `switch.pl:95-96`). Serial vs parallel: `PARLL = .TRUE.` if `NPROC > 1` (`:189-196`).

## D. Boundary / nesting on unstructured

Boundary command initializes unstructured boundary list via `SwanBpntlist` (`swanpre2.ftn:2702-2709`).

Parallel/local boundary global map: `bvertg` (`:2744-2768`).

Segment boundary accepts XY or vertex index `K`; validates vertex on unstructured boundary (`:3095-3151`).

`BGRIDP` built for unstructured boundary vertices using global-to-local map (`swanmain.ftn:4037-4058`).

Boundary spectra applied to boundary vertices by interpolation into `AC2` (`swanmain.ftn:6932-6960`).

So nesting works the same way as structured SWAN — parent dumps `NESTOUT`, child reads via `BOUND NEST` — but vertex-based.

## E. Wind / current / water level from ADCIRC

Input grid types: `CUR, WIND, WLEV`, unstructured (`swanpre1.ftn:1344-1350`).

Storage slots (`swmod1.ftn:1935-1947`):
- Currents: `JVX*, JVY*`.
- Water level: `JWLV*`.
- Wind: `JWX*, JWY*`.

Direct mesh input uses global/local vertex index `JVERT` (`swanmain.ftn:5053-5062`).

Per-step updates:
- Water level → `COMPDA(...,JWLV2)`; depth → `JDP2` (`:5077-5094`).
- Currents → `JVX2/JVY2` (`:5098-5130`).
- Wind → `JWX2/JWY2` (`:5145-5161`).

Time-varying unstructured fields use direct `ARR(JVERT)` when `IGTYPE==3` (`:8798-8823`).

This means ADCIRC writes directly into SWAN vertex-indexed arrays each coupling step — no spatial interpolation.

## F. Wave-driven forces back to ADCIRC

`SwanComputeForce.ftn90:35-307`:
- Coupled ADCIRC extension noted (`:35-39`).
- API returns `fx, fy` as `intent(out)` wave-induced forces (`:61-67`).
- Computes radiation stresses from `AC2` over frequency/direction (`:150-199`).
- Computes stress gradients on vertex duals (`:206-289`).
- Final forcing (`:304-307`):
```
fx = -ρ * g * (∂Sxx/∂x + ∂Sxy/∂y)
fy = -ρ * g * (∂Sxy/∂x + ∂Syy/∂y)
```

Handoff to ADCIRC is via caller-owned `fx/fy`; caller is `couple2swan.F` (outside this tree).

## G. Build / link

This SWAN checkout builds static library `swan${VERSION}` (`src/CMakeLists.txt:93-105`).

SWAN executable links library (`:112-117`).

Source list includes ADCIRC mesh reader, unstructured solver, force routine (`srclist.cmake:28-64`).

NetCDF source list includes same (`srclistnc.cmake:31-67`).

`padcswan` target is **not** present in this SWAN checkout; ADCIRC-side build must link against this SWAN library or compiled objects (see `adcirc-swan-coupling.md` for ADCIRC `padcswan` makefile target).

## Decision Guide

| Need | Setting |
|---|---|
| ADCIRC unstructured mesh sharing | `READ UNSTRUC ADC` (default keyword); needs `fort.14` |
| Coupled hot-start | SWAN `HOTSTART` synchronized via ADCIRC `SwanHotStartUnit` |
| Nesting child of coupled parent | `BOUND NEST 'parent.spec'` (coarser SWAN parent) |
| Disable SWAN-side MPI init in coupled | Use `-adcirc` switch in `switch.pl` |
| Disable wind-input from ADCIRC met | Set SWAN's own `INPGRID WIND` instead of `COUPWIND` in ADCIRC |
| Output radiation stresses for diagnostic | Use `BLOCK ... 'fname' ...FX FY...` (or compute from `HSIGN`, `DIR`) |

## Working Rules

- `padcswan` build expects this SWAN library; do not modify SWAN source without rebuilding the library.
- If you change SWAN source, rebuild library AND relink `padcswan`.
- For nesting unstructured child from structured parent: standard NESTOUT/BOUND NEST works; spectra interpolate to vertices.
- `vmark` carries ADCIRC's open/land boundary markers — use these to debug missing BC application.
- For Korean coast unstructured runs: same `fort.14` for ADCIRC tide and SWAN waves; ensure boundary type strings (`open` vs `land`) consistent.
- SWAN side uses `JVERT` (vertex index) directly — no IJ-grid concept on unstructured.

## Common Pitfalls

- ▢ Specifying separate SWAN mesh file in coupled mode — ignored; SWAN reads `fort.14`.
- ▢ Building SWAN library without `-adcirc` switch — coupled-build features missing.
- ▢ Looking for `couple2adcirc.F` in SWAN tree — doesn't exist; logic is on ADCIRC side.
- ▢ Setting SWAN `MODE NONSTAT` with mismatched `DELTC` — ADCIRC controls timestep; SWAN's internal `DT` must align.
- ▢ Hot-start ADCIRC alone without SWAN spectral file — wave init at zero; first SWAN step has no wave history.
- ▢ Expecting return timestep API — none; ADCIRC commands SWAN unilaterally.

## Next expansion

- BSBT vs SORDUP vs S&L performance on coastal unstructured (cross-link to `swan_modes_dispatch.md`).
- COAWST-style 3-way coupling (ROMS+SWAN+WW3) reference.
- SWAN library build flags walkthrough.

## References

- Booij et al. 1999 (SWAN third-generation).
- Dietrich et al. 2011 (ADCIRC+SWAN unstructured).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/swan/source_code/swan/src`. Auto-draft = false; review_required = true.
