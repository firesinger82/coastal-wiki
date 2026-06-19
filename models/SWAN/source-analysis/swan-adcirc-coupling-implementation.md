---
title: "swan adcirc coupling implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-adcirc-coupling-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN unstructured path + ADCIRC-SWAN coupling

## Scope note

How SWAN's unstructured-grid path differs from the structured `SWCOMP` solver, and how it integrates with ADCIRC for coupled storm-surge runs. The unstructured engine (`SwanCompUnstruc`) is a separate code path: triangle-mesh vertex-based, ordered-vertex sweeps, dedicated ADCIRC `fort.14` reader (`SwanReadADCGrid`).

## Source basis

Codex deep scan 2026-05-06 of:
- `Swan*.ftn90` — unstructured engine, grid types, ADCIRC reader
- `swancom1/5.ftn`, `swanmain.ftn` — structured/unstructured dispatch
- `swanpre1/2.ftn` — `CGRID UNSTRUC`, `READ UNSTRUC ADC`, unstructured limitations

## A. Top-level structured/unstructured branch

- `OPTG = 5` set by `CGRID UNSTRUC` parser at `[file=src/swanpre1.ftn line=1643-1649]`
- `READ UNSTRUC ...` parser at `[file=src/swanpre1.ftn line=1463-1493]` sets `grid_generator` and dispatches to `SwanReadGrid`
- Runtime dispatch in `swanmain.ftn`:
  - Structured: `SWCOMP` when `OPTG ≠ 5` at `[file=src/swanmain.ftn line=618-623]`
  - Unstructured: `SwanCompUnstruc` when `OPTG == 5` at `[file=src/swanmain.ftn line=624-627]`
- `SwanCompUnstruc` engine purpose (vertex-based, implicit geo+spectral) at `[file=src/SwanCompUnstruc.ftn90 line=66-83]`

## B. SwanGriddata / SwanGridobjects modules

`[file=src/SwanGriddata.ftn90 line=60-85]` — core unstructured storage:
- Counts: `ncells`, `nfaces`, `nverts` (+ global variants)
- Connectivity raw: `kvertc` (cell→3 vertices), `kvertf` (face→2 vertices)
- Mapping: `ivertg` (global index of local vertex)
- Boundary tags: `vmark`, `excmark`
- Sweep controls: `nsweep`, `asort`, `usort`

Derived runtime objects at `[file=src/SwanGridobjects.ftn90 line=152-193]`:
- `verttype`, `celltype`, `facetype` — full mesh topology

`vmark` interpretation:
- Binary collapse: `VMARKER = min(1, vmark)` at `[file=src/SwanGridVert.ftn90 line=91]`
- BC vertices: `vmark >= excmark` → `VBC=1` at `[file=src/SwanPrepComp.ftn90 line=81-85]`

Connectivity:
- `CELLV1..3` from `kvertc` at `[file=src/SwanGridCell.ftn90 line=144-149]`
- `FACEV1..2` from `kvertf` at `[file=src/SwanGridFace.ftn90 line=140-143]`
- Per-vertex adjacent cells + `NEXTCELL` ring at `[file=src/SwanGridCell.ftn90 line=278-350]`

`ie2v` doesn't exist — equivalent edge-to-vertex is `kvertf`/`FACEV1,FACEV2`.

## C. Unstructured propagation

- Geographic velocity routine: `SwanPropvelX` at `[file=src/SwanPropvelX.ftn90 line=1]`:
  - `cax = cgo*cos(theta)`, `cay = cgo*sin(theta)` at `[file=src/SwanPropvelX.ftn90 line=87-89]`
  - Optional diffraction scaling at `[file=src/SwanPropvelX.ftn90 line=94-101]`
  - Ambient current advection at `[file=src/SwanPropvelX.ftn90 line=105-110]`
- Called from unstructured main loop at `[file=src/SwanCompUnstruc.ftn90 line=918]`

### Sweep replacement

No 4-quadrant fixed sweep. Instead **ordered-vertex sweeps** over `nsweep` directions with per-cell intersection checks at `[file=src/SwanCompUnstruc.ftn90 line=829-979]`. Active spectral bins per sweep selected by `SwanSweepSel` at `[file=src/SwanCompUnstruc.ftn90 line=983-987]`. Spectral velocities per sweep from `SwanPropvelS` at `[file=src/SwanCompUnstruc.ftn90 line=994-1000]`.

### Solver dispatch

- Direct divide if no refraction/freq shift at `[file=src/SwanCompUnstruc.ftn90 line=1206-1228]`
- `SOLMAT` (Thomas tridiag) at `[file=src/SwanCompUnstruc.ftn90 line=1237-1238]`
- `SWSIP` (penta-diag SIP, implicit sigma) at `[file=src/SwanCompUnstruc.ftn90 line=1251-1255]`
- `SOLMT1` (tridiag for explicit sigma) at `[file=src/SwanCompUnstruc.ftn90 line=1264-1266]`

Same solver family as structured path — only the sweep loop differs.

## D. ADCIRC fort.14 reader (`SwanReadADCGrid`)

- `READ UNSTRUC ADC` parser trigger: `[file=src/swanpre1.ftn line=1478-1483]`
- Reader dispatch: `SwanReadGrid` at `[file=src/swanpre1.ftn line=1492]`, then `[file=src/SwanReadGrid.ftn90 line=73-77]`
- Actual `.14` parser: `SwanReadADCGrid` at `[file=src/SwanReadADCGrid.ftn90 line=1]`

Consumed `fort.14` fields:
- Title (line 1) skipped at `[file=src/SwanReadADCGrid.ftn90 line=101]`
- `ne, np` → `ncells, nverts` at `[file=src/SwanReadADCGrid.ftn90 line=105]`
- Node lines `node_id x y depth` at `[file=src/SwanReadADCGrid.ftn90 line=121-123]`
- Element lines `elem_id idum n1 n2 n3` (triangle connectivity) at `[file=src/SwanReadADCGrid.ftn90 line=135]`
- Open boundary counts/segments + node lists → `vmark` at `[file=src/SwanReadADCGrid.ftn90 line=148-157]`
- Land boundary counts/types (n1, itype) + node lists (or pairs for itype=4/24) → `vmark` at `[file=src/SwanReadADCGrid.ftn90 line=159-175]`

So SWAN reads ADCIRC's `fort.14` directly when in unstructured mode — no translation to a SWAN-native mesh format.

## E. ADCIRC-SWAN coupling pathway

- Coupled-run entry points: `PADCSWAN_INIT` and `PADCSWAN_RUN` pass timestep into `SWMAIN` at `[file=src/swanmain.ftn line=101-104]`
- The actual `couple2swan.F` wrapper that ADCIRC uses to call SWAN is **not in this source tree** (it lives in the ADCIRC repo).
- For `READ UNSTRUC ADC`: SWAN reads its own copy of `fort.14` — no in-memory mesh sharing in this snapshot.
- Force feedback to ADCIRC: `SwanComputeForce` at `[file=src/SwanComputeForce.ftn90 line=38]`

## F. Unstructured limitations

Explicit code-level unsupported features:

| Feature | Where blocked |
|---------|---------------|
| `GROUP` command | `[file=src/swanpre2.ftn line=378-380]` |
| WAM nesting BC | `[file=src/swanpre2.ftn line=2872-2874]` |
| WAVEWATCH III nesting BC | `[file=src/swanpre2.ftn line=2921-2923]` |
| Wave setup | `[file=src/swanpre1.ftn line=2089-2092]` |
| Filtered De Wit biphase | `[file=src/swanpre1.ftn line=3449-3452]` |

`GSE` and `FLUXLIM`:
- Parser is shared at `[file=src/swanpre1.ftn line=796-806]`
- Unstructured has dedicated `SwanGSECorr` at `[file=src/SwanGSECorr.ftn90 line=1]`, `[file=src/SwanGSECorr.ftn90 line=127]`
- No hard ban on FLUXLIM — uses shared `PROPFL`, `PNUMS` flags + unstructured `PHILIM`/`RESCALE` routines

## Decision Guide

| Scenario | Path | Note |
|----------|------|------|
| Standalone SWAN, regional structured grid | structured `SWCOMP` | default |
| Coupled ADCIRC-SWAN, unstructured ADCIRC mesh | unstructured `SwanCompUnstruc` | `READ UNSTRUC ADC 'fort.14'` |
| Want WW3/WAM nesting | structured | unstructured doesn't support these BCs |
| Want wave setup | structured | unstructured disabled |
| Need GSE anti-spoke | either | both paths support, separate routines |

## Working Rules

1. **`fort.14` is shared** between ADCIRC and SWAN in coupled runs but each reads its own copy. Keep them on the same disk path to avoid drift.
2. **Unstructured supports a subset of features** — don't assume parity with structured. Check the unsupported list above before designing a setup.
3. **The unstructured engine is a separate solver** — debugging requires reading `SwanCompUnstruc.ftn90` not `swancom1.ftn`.
4. **`vmark` in fort.14 boundary blocks** drives SWAN's BC vertex selection. ADCIRC and SWAN interpret these consistently because both read the same file.
5. Coupled runs: SWAN's compute time step (`COMPUTE NONSTAT DELTC`) must align with ADCIRC's coupling interval, or feedback gets stale.

## Common Pitfalls

- **Using `READ UNSTRUC ADC` then setting wave setup** — silent disable; user expects setup, gets none.
- **Trying to nest from WAM/WW3 onto unstructured fine grid** — hard error at parse.
- **Inconsistent `fort.14` between ADCIRC and SWAN copies** — mesh diverges silently; results disagree at boundaries.
- **`GROUP` output on unstructured** — silently disabled.

## Next expansion

- The actual `couple2swan.F` wrapper (lives in adcirc repo, separate analysis).
- Time-stepping coordination between ADCIRC and SWAN — exchange interval, lagged vs synchronous coupling.
- `SwanComputeForce` in detail (force back to ADCIRC).

## References

- `src/SwanCompUnstruc.ftn90` — unstructured solver core.
- `src/SwanGriddata.ftn90`, `src/SwanGridobjects.ftn90`, `src/SwanGridCell.ftn90`, `src/SwanGridVert.ftn90`, `src/SwanGridFace.ftn90` — mesh data types.
- `src/SwanPropvelX.ftn90`, `src/SwanPropvelS.ftn90` — propagation velocities on triangle mesh.
- `src/SwanReadGrid.ftn90`, `src/SwanReadADCGrid.ftn90` — fort.14 reader.
- `src/SwanGSECorr.ftn90` — unstructured GSE correction.
- `src/SwanComputeForce.ftn90` — force feedback to ADCIRC.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | dispatch, mesh data, propagation, fort.14 reader, coupling hooks, limitations |
| Out of scope | couple2swan.F (lives in ADCIRC), full force-feedback algorithm |
| Review status | `review_required: true` |
