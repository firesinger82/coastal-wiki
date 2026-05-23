---
title: "swan nesting io implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-nesting-io-implementation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN nesting I/O — NESTOUT writer, BOUND NEST reader, format checks

## Scope note

How a coarse SWAN run writes a nest file (`NESTOUT`) and how the receiving fine-grid run reads it back (`BOUND NEST` → `BCFILE` → runtime `RBFILE`). Includes spectrum format remapping (`CHGBAS`), error/warning emission paths for malformed or short files.

Companion to `swan-boundary-implementation.md` (covers `SWBOUN` body in general; this note focuses on the NEST-specific path end-to-end).

## Source basis

Codex deep scan 2026-05-06 of `swanpre2.ftn` (NESTOUT parser, NGRID setup, BCFILE), `swanout1.ftn`/`swanout2.ftn` (writer side), `swanmain.ftn` (runtime read + injection), `swanser.ftn` (`WRSPEC` ASCII writer).

## A. NESTOUT command parsing

In the output-request parser:
- `[file=src/swanpre2.ftn line=1984]` — `IF (KEYWIS('NEST'))` enters the `NESTout 'sname' 'fname'` block
- `[file=src/swanpre2.ftn line=2002]` — `SWNMPS` resolves `'SNAME'` to a defined point set; checks type `N` (nest) at `[file=src/swanpre2.ftn line=2004]`
- `[file=src/swanpre2.ftn line=2017]` — filename via `INCSTR('FNAME', FILENM, 'REQ', ' ')`
- `[file=src/swanpre2.ftn line=2026, 2028]` — output-request bookkeeping: `OQI(1) = NREF` (unit placeholder), `OUTP_FILES(NREOQ) = FILENM`

First runtime write opens the file (`FOR ... 'UF'` formatted unformatted? actually 'UF' = "unformatted" — but `WRSPEC` writes ASCII, so 'UF' here is an internal type code, not Fortran unformatted) at `[file=src/swanout2.ftn line=1888, 1899, 1901]`. Actual Fortran unit is written back to `OQI(1)` after open.

## B. NESTOUT runtime writer

- `[file=src/swanout1.ftn line=477]` — `RTYPE='SPRC'` dispatches to `CALL SWSPEC(...)` (NESTOUT's writer)
- `[file=src/swanout2.ftn line=1895]` to `[file=src/swanout2.ftn line=2001]` — on first call (`NREF == 0`), `SWSPEC` writes the **header**: TIME, LOCATIONS, FREQ grid, DIR grid, QUANT (quantity metadata)
- `[file=src/swanout2.ftn line=2005]` — each subsequent write emits the current time block (`CHTIME`) for nonstat runs
- `[file=src/swanout2.ftn line=2024]` to `[file=src/swanout2.ftn line=2075]` — per-time-step loop over locations writes spectra:
  - 2D spectrum → `WRSPEC` (full directional×frequency)
  - 1D spectrum → `LOCATION` line + per-frequency entries
- `[file=src/swanser.ftn line=5571, 5575]` — `WRSPEC` writes `FACTOR` + integerized bins. **Output is SWAN-standard ASCII spectral format**, not unformatted binary, despite the 'UF' open code.

## C. NGRID command setup (output grid)

- `[file=src/swanpre2.ftn line=794, 803]` — `NGRID 'SNAME'` parsing
- Structured nest case: rectangle parameters + 4-side discretization at `[file=src/swanpre2.ftn line=901-958]` produces boundary points
- Unstructured case: extracts boundary vertices from mesh markers (`VM /= 0`) at `[file=src/swanpre2.ftn line=963-973]`
- Runtime validation: `SPRCON` validates N-grid points against computational grid via `SINUPT` at `[file=src/swanmain.ftn line=4609-4637]`

## D. BOUND NEST reader on fine grid

- `BOUNDNEST` (`NE`) command path calls `BCFILE(FILENM, 'NEST', ...)` at `[file=src/swanpre2.ftn line=2943, 2988]`
- `BCFILE` reads header/type/locations/freq/dir at `[file=src/swanpre2.ftn line=4078-4352]`; metadata stored in `BFILED` + spectral axis arrays
- Runtime read each step via `RBFILE` at `[file=src/swanmain.ftn line=6916, 7469]`
- `TIMCO` matching: explicit at `[file=src/swanmain.ftn line=7724, 7781, 8034]` — reader advances until `TIMCO <= TIMF2`, then linearly interpolates between `TIMF1` and `TIMF2`

## E. Spectrum format identity check (does fine grid require exact match?)

**No exact match required** — SWAN remaps via `CHGBAS`:
- Direction grid: `CHGBAS(BSPDIR → SPCDIR)` at `[file=src/swanmain.ftn line=8451]`
- Frequency grid: `CHGBAS(BSPFRQ → SPCSIG)` at `[file=src/swanmain.ftn line=8482]`

So nesting from a coarse run with different `SET FREQ`/`SET DIR` will work but uses linear remapping. For tightly-validated cases, share both spectral grids exactly between coarse and fine.

### Above-highest-frequency tail

When the boundary file's highest frequency is below the fine grid's, SWAN extrapolates with the diagnostic high-frequency tail (`PWTAIL`):
- Tail extrapolation at `[file=src/swanmain.ftn line=8458]` to `[file=src/swanmain.ftn line=8496]`
- Truncation detection at `[file=src/swanmain.ftn line=8458-8464]`
- Tail fill at `[file=src/swanmain.ftn line=8494-8496]`

**No hard error** when fine grid extends above coarse grid's frequency range. The user sees this only if they analyze the high-frequency tail of the fine result.

## F. Pitfalls visible in the code

| Symptom | Code path | Behavior |
|---------|-----------|----------|
| Nest freq range narrower than fine grid | `[file=src/swanmain.ftn line=8458-8464]` truncation detect; `[file=src/swanmain.ftn line=8494-8496]` power-law tail fill | **No hard error** — silently extrapolates with `PWTAIL` |
| Nest TIME range too short for full fine-grid run | `[file=src/swanmain.ftn line=8019]` "data on boundary file exhausted" warning; `[file=src/swanmain.ftn line=8022]` marks `BFILED(1) = -1`; subsequent calls skip updates `[file=src/swanmain.ftn line=7695]` | Continues with last known spectrum; **no fail** |
| Malformed file / short read | `[file=src/swanmain.ftn line=8508]` 'read error', `[file=src/swanmain.ftn line=8514]` 'insufficient data' | Error message but run continues with partial data |
| Not a true nesting file / no boundary points | Header parse errors at `[file=src/swanpre2.ftn line=4168, 4177, 4199]` | Runtime error; user sees in PRINTF |

So **time-range exhaustion silently propagates the last spectrum** — the receiving run does NOT fail. Watch for "exhausted" warnings in the log output.

## Decision Guide

| Concern | Action |
|---------|--------|
| Want exact spectral consistency between coarse and fine | use same `SET FREQ` and `SET DIR` commands in both runs |
| Worried about high-frequency cutoff in fine | extend coarse run's frequency range OR accept tail extrapolation |
| Coarse run shorter than fine simulation | run coarse for at least `[fine_start, fine_end]` |
| Multiple fine grids inside one coarse | one `NESTOUT` per fine grid (define separate `NGRID` per fine) |

## Working Rules

1. **NESTOUT writes ASCII** (despite the `'UF'` open code) — files are human-readable, useful for debugging.
2. **`CHGBAS` remap is automatic** — no warning if grids differ. Inspect `BSPFRQ` and `SPCSIG` headers for any quality concerns.
3. **TIMCO matching is anchored at run start** — if you change `COMPUTE NONSTAT` start time between coarse and fine, the reader still advances until `TIMCO ≤ TIMF2`. Mismatch silently uses earliest available time.
4. **Time exhaustion = silent failure mode** — set up monitoring on the log file for "data on boundary file exhausted" messages.
5. NGRID must be defined **before** referencing it in `NESTOUT`.

## Common Pitfalls

- **Time exhaustion** — coarse run ends earlier than fine-grid simulation: the fine run continues with the last spectrum (no error). Always log-check.
- **Spectral grid mismatch silent quality loss** — re-running coarse with fine's spectral grid is cheap insurance for validation work.
- **'UF' confusion** — open code 'UF' is internal SWAN, file is ASCII.
- **NGRID after NESTOUT** in command file — parser fails, but error is unspecific.
- **Multiple NESTOUT to same file** — appends not overwrites; debugging gets harder.
- ▢ User-experience cases — placeholder.

## References

- `src/swanpre2.ftn` — `NESTOUT` parser, `NGRID` setup, `BCFILE` (NEST reader header).
- `src/swanout1.ftn` — `SWORDC` dispatch to `SWSPEC`.
- `src/swanout2.ftn` — `SWSPEC` writer body, time block writes.
- `src/swanmain.ftn` — `RBFILE` runtime read, `CHGBAS` remap, exhaustion handling.
- `src/swanser.ftn` — `WRSPEC` ASCII writer.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | NESTOUT writer (header + per-time block), BOUND NEST reader, NGRID setup, CHGBAS remapping, exhaustion/error paths |
| Review status | `review_required: true` |
