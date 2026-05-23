---
title: "swan output writers implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-output-writers-implementation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN output writers — SWBLOK, SWTABP, SWSPEC internals

## Scope note

Code-level walk-through of how SWAN writes block (BLOCK), table (TABLE), and spectral (SPECout, NESTout) outputs. Includes integer-encoded factor format, format-flag dispatch, derived-quantity computation from `AC2`, and file pointer management.

Companion to `swan-command-file-reference.md` (covers output command syntax) and `swan-nesting-io-implementation.md` (covers NESTout specifically).

## Source basis

Codex deep scan 2026-05-06 of `/mnt/e/models/swan/source_code/swan/src/swanout1.ftn`, `swanout2.ftn`, `swanser.ftn`.

## A. SWORDC + SWOUTP dispatcher

- `SWORDC` at `[file=src/swanout1.ftn line=527]` decodes request metadata (`NVOQP`, `VOQR`, `OQPROC`, time gating via `OUTR(1:2)`) but does NOT call writer backends itself.
- `SWOUTP` at `[file=src/swanout1.ftn line=435-509]` is the runtime dispatcher.

### Routing by RTYPE

`[file=src/swanout1.ftn line=436-447]`: `RTYPE(1:3) == 'BLK'` → `SWBLOK / SWBLKP / SWBLKV`
`[file=src/swanout1.ftn line=454-462]`: `RTYPE(1:3) == 'TAB'` → `SWTABP`
`[file=src/swanout1.ftn line=469-503]`: `RTYPE(1:2) == 'SP'` → `SWSPEC`

### Spectral subtype routing

`[file=src/swanout1.ftn line=469-472]`: 3rd char distinguishes relative/absolute (`R`/`A`); 4th char `'C'` indicates 2D. So `'SPRC'` = "Spectrum Relative Cartesian (2D)", `'SPAC'` = absolute 2D, `'SPE1'` = 1D.

Character-test routing (instead of full string switch) is used throughout.

## B. SWBLOK (BLOCK output)

- Subroutine: `[file=src/swanout2.ftn line=18]`
- Output mode by `RTYPE`: `'BLKP'/'BLKD'/else` → `IPD = 1/2/3` at `[file=src/swanout2.ftn line=163-172]`

### Integer-encoded FACTOR

When `DFAC ≤ 0` (default), SWBLOK computes a factor from data range:
```fortran
IFAC = INT(10. + LOG10(...)) - 13
DFAC = 10. ** IFAC
```
at `[file=src/swanout2.ftn line=250-275]`. `FMAX` scans matrix values for scalar/vector fields.

So output value = (file integer) × `DFAC`. The `FACTOR` line in the file shows the multiplier the consumer must apply.

### Per-quantity write loop

`[file=src/swanout2.ftn line=246-349]`:
- `DO JVAR = 1, NVAR`
- Scalar vs vector branch at `[file=src/swanout2.ftn line=285]`, `[file=src/swanout2.ftn line=307]`
- Each field written via `SBLKPT` at `[file=src/swanout2.ftn line=304-305]`, `[file=src/swanout2.ftn line=340-345]`

### Header formatting in SBLKPT

`[file=src/swanout2.ftn line=360]` (`SBLKPT` body):
- Quantity header with factor/unit at `[file=src/swanout2.ftn line=517-520]`
- Optional `CHTIME` (time stamp) at `[file=src/swanout2.ftn line=521-524]`
- X/Y matrix-style blocks at `[file=src/swanout2.ftn line=540-559]`

So a BLOCK output file looks like:
```
[QUANT]   [unit]   FACTOR=Xe-NN
TIME=YYYYMMDD.HHMMSS
(matrix of integers row by row)
```

## C. SWTABP (TABLE output)

- Subroutine: `[file=src/swanout2.ftn line=1172]`

### Format branches

| `RTYPE` | Format | file:line |
|---------|--------|-----------|
| `TABD` | NOHEADER | `[file=src/swanout2.ftn line=1405]` |
| `TABP` | HEADER (legacy print) | `[file=src/swanout2.ftn line=1410]` |
| `TABI` | HEADER + indexed first column | `[file=src/swanout2.ftn line=1410]` + `[file=src/swanout2.ftn line=1419-1425]`, `[file=src/swanout2.ftn line=1564-1569]` |
| `TABT` | SWAN standard | `[file=src/swanout2.ftn line=1480]` |
| `TABS` | SWAN standard with site metadata | same; quantity-definitions at `[file=src/swanout2.ftn line=1481-1533]` |

### Per-point loop

`[file=src/swanout2.ftn line=1560-1604]`:
- `DO IP = 1, MIP`
- Each quantity formatted and appended per row
- Special time-quantity handling when `IVTYPE == 40` at `[file=src/swanout2.ftn line=1572-1577]`

So `TABLE 'STATIONS' SWAN 'fname' HSIGN PER` goes through the `TABT/TABS` branch with quantity-definitions header.

## D. SWSPEC (SPECout writer)

- Subroutine: `[file=src/swanout2.ftn line=1719]`
- 2D vs 1D split on `RTYPE(4:4) == 'C'`:
  - 2D header: `[file=src/swanout2.ftn line=1944-1976]`
  - 1D header: `[file=src/swanout2.ftn line=1976-2000]`
  - 2D write: `WRSPEC` at `[file=src/swanout2.ftn line=2057-2059]`
  - 1D write: triplets at `[file=src/swanout2.ftn line=2060-2071]`

### `WRSPEC` (the actual integer-encoded spectrum writer)

- Subroutine: `[file=src/swanser.ftn line=5448]`
- Computes max amplitude `[file=src/swanser.ftn line=5553-5563]`
- If tiny: emit `'ZERO'` at `[file=src/swanser.ftn line=5564-5566]`
- Else: emit `'FACTOR'` with scaled physical factor at `[file=src/swanser.ftn line=5568-5572]`
- Integerize bins via `NINT(ACLOC(ID,IS) / EFAC)` at `[file=src/swanser.ftn line=5575]`

### `FACTOR` normalization

`[file=src/swanser.ftn line=5568]`:
```
EFAC = 1.01 * max * 10**(-DEC_SPEC)
```
Then written as `EFAC * 2 * PI**2 / 180` at `[file=src/swanser.ftn line=5571]` to convert radian-based density to Hz/degree convention for the file.

So the spectral output file's units are not raw `m²/(Hz·rad)` — there's a 2π² conversion baked into `FACTOR`.

## E. Quantity computation from `AC2`

- Derived wave quantities computed in `SWOEXA` at `[file=src/swanout1.ftn line=3194]`
- Local spectrum `ACLOC` interpolated from `AC2` at `[file=src/swanout1.ftn line=3438-3460]`

### HSIGN

- `IVTYPE = 10` (HSIGN)
- Computation: integrate spectral energy density, then `Hs = 4 * sqrt(ETOT)` at `[file=src/swanout1.ftn line=3482-3512]`
- Exact assignment line: `[file=src/swanout1.ftn line=3511]`

### Peak period (RTPEAK)

- Simple peak: `IVTYPE = 12` at `[file=src/swanout1.ftn line=3752-3768]`
- Parabolic-fit peak: `IVTYPE = 53` at `[file=src/swanout1.ftn line=3775-3818]`
- Both use `2π / σ_peak`

So `HSIGN`, `RTPEAK`, `PER` (mean period), `DIR` (mean direction), etc., are all derived from `AC2` per output point inside `SWOEXA`. The user's command file lists these by name (`HSIGN PER DIR`); SWAN looks up `IVTYPE` and dispatches to the appropriate computation.

## F. Time-stamped output and file pointer management

### When `CHTIME` is written

- BLOCK: each `SBLKPT` call writes the time at `[file=src/swanout2.ftn line=521-524]`
- TABLE TABS: time written once before point loop at `[file=src/swanout2.ftn line=1557-1559]`
- SPEC: time written once per call at `[file=src/swanout2.ftn line=2005-2007]`

So spectral output has fewer time stamps than block output (one per file write per call vs one per point).

### File open / append behavior

"Open once when `NREF == 0`, then reuse unit in `OQI(1)`":
- BLOCK: `[file=src/swanout2.ftn line=183-189]`
- TABLE: `[file=src/swanout2.ftn line=1384-1396]`
- SPEC: `[file=src/swanout2.ftn line=1895-1902]`

Implication: subsequent writes are **append-style on already-open units** — fast, but if SWAN crashes mid-write, files end with partial records.

### Explicit rewrite (only special paths)

MATLAB block output reopens with `STATUS='REPLACE'` at `[file=src/swanout2.ftn line=191-193]`. Normal text outputs are not reopened each timestep.

## Decision Guide

| Need | Use |
|------|-----|
| Compact ASCII grid output | `BLOCK` (factored integers, smallest file) |
| Time series at fixed stations | `TABLE` (one row per time per point) |
| Frequency × direction spectrum at points | `SPECOUT SPEC2D` |
| 1D frequency-only spectrum | `SPECOUT SPEC1D` |
| Boundary file for fine-grid nest | `NESTOUT` (covered separately) |

## Working Rules

1. **The integer-encoded `FACTOR` is essential** — consumers must apply it. Plain integer values are not the physical quantity.
2. **`HEADER` vs `NOHEADER`** affects file size, not content. Use `NOHEADER` for downstream scripts that consume only data rows.
3. **Spectrum file `FACTOR` includes `2π²/180` conversion** — to extract m²/(Hz·deg), multiply integer by `FACTOR`.
4. **All output writes are append on the same unit** — sigterm during run leaves partial files.
5. **`HSIGN = 4*sqrt(ETOT)`** is the canonical formula; ensure your downstream comparison computes Hs the same way.

## Common Pitfalls

- Forgetting to apply `FACTOR` when reading SWAN output — values look 1000× off.
- **`TABLE TABD` (no header)** consumed by a script expecting headers — silent column shift.
- **`SPECOUT SPEC1D` written with `RTYPE='SPRE'`** vs `'SPRC'` (2D) — different column layout.
- **Multiple time blocks in one file** — append-only, so consumer must split on `'TIME'` markers.
- ▢ User-experience cases — placeholder.

## References

- `src/swanout1.ftn` — `SWOUTP` dispatcher, `SWORDC`, `SWOEXA` quantity computation.
- `src/swanout2.ftn` — `SWBLOK`, `SBLKPT`, `SWTABP`, `SWSPEC`, `WRSPEC` (placeholder).
- `src/swanser.ftn` — `WRSPEC` actual integerized spectrum writer.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex scan | 30+ file:line citations |
| Coverage | dispatcher, BLOCK, TABLE, SPEC writers, HSIGN/RTPEAK computation, file pointer policy |
| Review status | `review_required: true` |
