---
title: "swan command file reference"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-command-file-reference.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN command file (.swn) — commands, parsers, and cross-reference

## Scope note

Every SWAN run is driven by a **command file** (typically `INPUT` or `*.swn`), processed line-by-line by `swanpre1.ftn` and `swanpre2.ftn`. This note maps each top-level command to:
- **purpose** (one sentence),
- **reader subroutine** (`SWREAD`, `SWREOQ`, `SWREPS`, etc.),
- **file:line** of the parsing block,
- **required vs optional** (per a typical run),
- **key sub-keywords / arguments**,
- **manual cross-reference** (swanuse / swantech / online_doc).

Companion to `swan-foundation.md`. Where the foundation note covers *why*, this note covers *what* you write in the command file and *where* SWAN reads it.

## Source basis

- **Codex source scan** of `/mnt/e/models/swan/source_code/swan/src/` (33 commands with file:line citations) — 2026-05-06.
- **RAG retrieval** against `manuals` collection filtered to `model=swan` (902 chunks: PDFs `swanuse/swantech/swanimp/swanpgr` + 195 online_doc HTML chapters).

## Command-file structure (typical order)

```
PROJECT 'name' 'nr' 'title1' 'title2' 'title3'
SET LEVEL 0.0 NAUT
MODE NONSTATIONARY TWODIMENSIONAL
COORDINATES SPHERICAL CCM

CGRID REGULAR ... CIRCLE 36 0.04 1.0
INPGRID BOTTOM ... 
READINP BOTTOM ... 'fname'
INPGRID WIND NONSTATIONARY ...
READINP WIND ... SERIES 'fname'

BOUND SHAPESPEC JONSWAP ... PEAK
BOUND SIDE W CONSTANT ... 
INITIAL DEFAULT

GEN3 WESTHUYSEN
WCAP KOMEN
QUADRUPL ...
BREAKING CONSTANT 1.0 0.73
FRICTION JONSWAP CONSTANT 0.067
TRIAD

NUMERICAL ACCUR 0.02 0.02 ... STAT 50
PROPAGATION SORDUP

POINTS 'STATIONS' FILE 'stations.txt'
BLOCK 'COMPGRID' NOHEAD 'fort.18' LAY 4 HSIGN PER DIR
TABLE 'STATIONS' HEADER 'fort.19' HSIGN PER

COMPUTE NONSTATIONARY 20070101.000000 30 MIN 20070103.000000

STOP
```

Reading order in the parser is **fixed**: `PROJECT` and `SET` first, then `MODE/COORD/CGRID/INPGRID/READINP/BOUND` setup, then physics/numerics, then output (`POINTS/FRAME/.../BLOCK/TABLE`), then `COMPUTE`. `STOP` ends parsing.

## Commands by group

### Group 1 — Setup

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `PROJECT` | Project id/number + 3 title lines | `SWREAD` | `[file=src/swanpre1.ftn line=523]` | optional | `'NAME' 'NR' TITLE1 TITLE2 TITLE3` | `[file=pdf:swan:swanuse]` ch.4 |
| `SET` | Global physical/numerical defaults | `SWREAD` | `[file=src/swanpre1.ftn line=2169]` | optional | `LEVEL`, `DEPMIN`, `MAXMES`, `GRAV`, `RHO`, `CDCAP`, `NAUT`/`CART`, `PWTAIL`, `EXCMARK`, `NSWEEP`, `CURV` | `[file=pdf:swan:swanuse]` |
| `MODE` | Stationary/nonstationary, 1D/2D | `SWREAD` | `[file=src/swanpre1.ftn line=738]` | optional | `STATIONARY`/`NONSTATIONARY`, `ONED`/`TWOD`, `NOUPDAT` | `[file=pdf:swan:swantech]` ch.3.1 |
| `COORDINATES` | Cartesian or spherical | `SWREAD` | `[file=src/swanpre1.ftn line=821]` | optional | `CART`, `SPHE [REARTH]`, projection `QC`/`CCM`, `REPEATING` | `[file=pdf:swan:swanuse]` |

### Group 2 — Grids and input data

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `CGRID` | Computational grid + spectral discretization | `SWREAD` | `[file=src/swanpre1.ftn line=1608]` | **yes** | `REG/CURV/UNSTRUC ...`, `EXC`, spectral `CIR/SEC [DIR1 DIR2] [MDC] [FLOW] [FHIGH] [MSC]` | `[file=website:swan:node11]` Computational grid |
| `INPGRID` | Define input field grid (BOT/CUR/WI/etc.) | `SWREAD` (calls `SINPGR`) | `[file=src/swanpre1.ftn line=1354]` | conditional | field selector `BOT/CUR/VX/VY/FR/WI/WX/WY/WLEV/ASTD/NPLA/TURB/MUDL/AICE/HICE/HSS/TSS/DSS`, grid `REG/CURV/UNSTRUC`, `NONSTAT` | `[file=website:swan:node26]` Input grids and data |
| `READINP` | Read input field data files | `SWREAD` (calls `SREDEP`/`SwanReadGrid`) | `[file=src/swanpre1.ftn line=1453]` | conditional | `UNSTRUC (ADC/TRIA/EASY 'FNAME')` or `[FAC] ('FNAME'/SERIES 'FNAME') [IDLA] FREE/FORMAT/UNFORMATTED` | `[file=website:swan:node26]` |

### Group 3 — Boundary and initial

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `BOUND` | Wave boundary conditions | `SWREAD`/`SWBOUN` | `[file=src/swanpre1.ftn line=1873]`, `[file=src/swanpre2.ftn line=2695]` (SWBOUN body) | conditional | `SHAP`, `JON/BIN/PM/GAUS/TMA`, `WAMN/WW3/NE`, `OPEN/CLOS`, segment/side specs | `[file=website:swan:node27]` Boundary and initial conditions; `[file=pdf:swan:swantech]` ch.4 page 125 |
| `INITIAL` | Initial wave state | `SWREAD`/`INITVA` | `[file=src/swanpre1.ftn line=1309]` | optional | `PAR ...`, `ZERO`, `HOTS/REST` (restart) | `[file=website:swan:node27]` |

### Group 4 — Physics activations

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `WIND` | Wind forcing/source coupling flags | `SWREAD` | `[file=src/swanpre1.ftn line=2773]` | optional | wind-source values paired with GEN choice | `[file=website:swan:node28]` Physics |
| `GEN1` | 1st-generation wind input | `SWREAD` | `[file=src/swanpre1.ftn line=2808]` | optional | `CF10..CFPM` parameters | `[file=pdf:swan:swantech]` ch.2.3 page 21 |
| `GEN2` | 2nd-generation wind input | `SWREAD` | `[file=src/swanpre1.ftn line=2843]` | optional | `CF10..CFPM` parameters | same |
| `GEN3` | 3rd-generation wind input family | `SWREAD` | `[file=src/swanpre1.ftn line=2904]` | optional | `JANS`, `YAN`, `WESTH`, `BAB`, `ST6`, `UP/DOWN`, `VECTAU/SCATAU`, `TRUE10/U10P`, `DRAG (WU/FIT/SWELL)`, `AGROW` | `[file=website:swan:node28]` Physics |
| `WCAP` | Whitecapping dissipation | `SWREAD` | `[file=src/swanpre1.ftn line=2459]` | optional | `KOM`, `JANS`, `LHIG`, `BJ`, `KBJ`, `AB [CDS2 BR] (CUR [CDS3])` | `[file=pdf:swan:swantech]` ch.2.3 |
| `QUADRUPL` | Nonlinear quadruplet (4-wave) | `SWREAD` | `[file=src/swanpre1.ftn line=3286]` | optional | `[IQUAD] [LAMBDA] [CNL4] [CSH1] [CSH2] [CSH3]` | `[file=pdf:swan:swantech]` ch.2.3 |
| `BREAKING` | Surf breaking | `SWREAD` | `[file=src/swanpre1.ftn line=2376]` | optional | `CON`, `VAR/NEL`, `RUE`, `TG`, `BKD`, `ASYM`, `DIR [SPREAD]`, `FREQD [POWER FMIN FMAX]` | `[file=pdf:swan:swantech]` ch.2.3.3 page 29 |
| `FRICTION` | Bottom friction | `SWREAD` | `[file=src/swanpre1.ftn line=2544]` | optional | `JON (CON/VAR)`, `COLL`, `MAD`, `RIP` with method coefficients | `[file=pdf:swan:swantech]` ch.2.3.3 |
| `TRIAD` | Nonlinear triad (3-wave) | `SWREAD` | `[file=src/swanpre1.ftn line=3337]` | optional | `LTA`, `DCTA`, `SPB`, `FTIM`, `COLL/NONC`, `BIPH (ELD/SAPR/WIT)`, `TRA/IC (FG/MS/BR/QU)` | `[file=pdf:swan:swantech]` ch.2.3 |
| `DIFFRACTION` | Diffraction approximation | `SWREAD` | `[file=src/swanpre1.ftn line=2114]` | optional | `[IDIFFR] [SMPAR] [SMNUM] [CGMOD]` | `[file=pdf:swan:swantech]` |

### Group 5 — Numerics

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `PROPAGATION` | Propagation sweep / scheme | `SWREAD` | `[file=src/swanpre1.ftn line=791]` | optional | `BSBT/BTBS`, `GSE [WAVEAGE]`, `FLUXLIM` | `[file=website:swan:node29]` Numerics |
| `NUMERICAL` | Solver stopping/scheme controls | `SWREAD` | `[file=src/swanpre1.ftn line=1939]` | optional | `STOPC/ACCUR ...`, `STAT/NONST`, `DIRIMPL ... DEP/WNUM`, `REFRLIM`, `SIGIMPL/SIGEXPL/FIL`, `CTHETA`, `CSIGMA`, `SETUP` | `[file=website:swan:node29]` |
| `COMPUTE` | Run computation | `SWREAD` | `[file=src/swanpre1.ftn line=875]` | **yes** | `STAT [TIME]` or `[TBEGC] [DELTC] [TENDC]` time unit | `[file=website:swan:node34]` Lock-up |

### Group 6 — Output point/frame definitions

These define **where** outputs are computed but don't write anything by themselves. Output writing requires `BLOCK`, `TABLE`, `SPECOUT`, `NESTOUT` (Group 7) referring to a name defined here.

| Command | Purpose | Reader | file:line | Req? | Key args |
|---------|---------|--------|-----------|------|----------|
| `POINTS` | Named point set | `SWREPS` | `[file=src/swanpre2.ftn line=536]` | optional | `'SNAME'`, repeated `[XP YP]` or `FILE 'FNAME'` |
| `FRAME` | Named rectangular grid | `SWREPS` | `[file=src/swanpre2.ftn line=323]` | optional | `'SNAME' [XPFR YPFR ALPFR XLENFR YLENFR MXFR MYFR]` |
| `GROUP` | Named subgrid (computational index range) | `SWREPS` | `[file=src/swanpre2.ftn line=372]` | optional | `'SNAME' SUBGRID [IX1 IX2 IY1 IY2]` |
| `RAY` | Named ray set | `SWREPS` | `[file=src/swanpre2.ftn line=609]` | optional | `'RNAME' [XP1 YP1 XQ1 YQ1]` with repeated `[INT XP YP XQ YQ]` |
| `ISOLINE` | Isoline points on a ray | `SWREPS` | `[file=src/swanpre2.ftn line=694]` | optional | `'SNAME' 'RNAME' DEPTH/BOTTOM [DEP]` |
| `CURVE` | Polyline output set | `SWREPS` | `[file=src/swanpre2.ftn line=462]` | optional | `'SNAME' [XP1 YP1]` then `[INT XP YP]` |
| `NGRID` | Nested output grid | `SWREPS` | `[file=src/swanpre2.ftn line=794]` | optional | `'SNAME'` + structured `[XPN YPN ALPN XLENN YLENN MXN MYN]` or `UNSTRUC (TRIA/EASY 'FNAME')` |

### Group 7 — Output writers

These reference a name from Group 6 (or use `'COMPGRID'` for the full computational grid) and produce files.

| Command | Purpose | Reader | file:line | Req? | Key args | Manual ref |
|---------|---------|--------|-----------|------|----------|------------|
| `BLOCK` | Block/grid output | `SWREOQ` | `[file=src/swanpre2.ftn line=1171]` | optional | `'SNAME'`, `HEADER/NOHEAD`, `'FNAME'`, `LAYOUT [IDLA]`, var list via `SVARTP`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node12]` |
| `TABLE` | Tabular output at points | `SWREOQ` | `[file=src/swanpre2.ftn line=1577]` | optional | `'SNAME'`, `HEADER/NOHEADER/INDEXED/SWAN/STAB`, `'FNAME'`, var list, `UNIT`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node12]` |
| `SPECOUT` | Spectral output | `SWREOQ` | `[file=src/swanpre2.ftn line=1873]` | optional | `'SNAME'`, `SPEC1D/SPEC2D`, `ABS/REL`, `S/L`, `'FNAME'`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node12]` |
| `NESTOUT` | Nesting boundary spectra | `SWREOQ` | `[file=src/swanpre2.ftn line=1984]` | optional | `'SNAME'`, `'FNAME'`, `OUTPUT [TBEG] [DELT]` | `[file=website:swan:node27]` |

### Group 8 — Control

| Command | Purpose | Reader | file:line |
|---------|---------|--------|-----------|
| `STOP` | End command processing | `SWREAD` | `[file=src/swanpre1.ftn line=497]` |
| `$` | Comment to end-of-line | scanner (`INKEYW` path) | (handled by lexer, not a command block) |

## Connectivity / dependency graph

```
                ┌─── PROJECT / SET / MODE / COORD ──┐
                │                                   │
                ▼                                   │
              CGRID  ─── defines computational grid + spectral grid
                │
                ▼
       INPGRID + READINP  ─── for each input field (BOT, WIND, CUR, ICE, ...)
                │
                ▼
         BOUND / INITIAL  ─── boundary spectra + initial state
                │
                ▼
    GEN1/2/3 + WCAP + QUADRUPL + BREAKING + FRICTION + TRIAD + DIFFRACTION
                │   ─── physical source/sink term selectors
                ▼
       PROPAGATION + NUMERICAL  ─── numerical scheme + stopping
                │
                ▼
      POINTS/FRAME/GROUP/RAY/ISOLINE/CURVE/NGRID  ─── output locations
                │
                ▼
       BLOCK/TABLE/SPECOUT/NESTOUT  ─── output writers
                │
                ▼
              COMPUTE  ─── start the run
                │
                ▼
              STOP
```

Critical orderings:
- `CGRID` must be **before** `INPGRID/READINP/BOUND/INITIAL` (the spatial domain is defined there).
- Physics/numerics commands can appear in any order between setup and `COMPUTE`.
- Output writers require their named target (`POINTS`, `FRAME`, etc.) to be defined earlier in the file.
- A single `.swn` file can contain multiple `COMPUTE` blocks (e.g., stationary then nonstationary or successive time windows) — physics commands between them re-modify the run.

## Decision Guide

| Run type | Required commands | Optional but typical |
|----------|-------------------|----------------------|
| Stationary 2D wave hindcast | PROJECT, MODE STAT, CGRID, INPGRID/READINP BOT, INPGRID/READINP WIND, BOUND, GEN3, NUMERICAL ACCUR, COMPUTE STAT, STOP | WCAP, BREAKING, FRICTION, BLOCK, TABLE |
| Nonstationary storm passage | + MODE NONSTAT, INPGRID WIND NONSTAT, COMPUTE NONSTAT | + INITIAL HOTS for restart, NESTOUT for downstream nesting |
| Nesting from coarse run | (in coarse run) NGRID + NESTOUT | (in fine run) BOUND NEST 'sname' 'fname' |
| Surf-zone with shoaling | + TRIAD ON, BREAKING with appropriate alpha/gamma | + finer spectral resolution (`MSC=36+`, `MDC=36+`) |

## Working Rules

1. **`SET PWTAIL` matters for stationary convergence** — too steep tail underestimates whitecapping, may prevent convergence.
2. **`NUMERICAL STOPC ...` is the convergence gate for stationary** — default tolerances are loose; tighten for high-quality validation.
3. **`COMPGRID` is a built-in name** for the computational grid — you don't need to define it via `FRAME`/`POINTS`.
4. **`NESTOUT` writes 2D spectra** — the receiving fine-grid `BOUND NEST` reads them, both grids must share `SET FREQ` and `SET DIR` parameters.
5. **`COMPUTE NONSTAT` time format**: `YYYYMMDD.HHMMSS` (default), or with `SET TIMEFORMAT` set differently — be explicit when sharing scripts.
6. **Multiple `INPGRID WIND` blocks override each other** — keep one canonical wind input per run.

## Common Pitfalls

- **`CGRID` after `INPGRID`** → SWAN doesn't know the domain when reading inputs. Always order `CGRID` first.
- **`READINP` without preceding `INPGRID`** → "input grid not yet defined" error. Pair them.
- **Mixing structured and unstructured** in the same `INPGRID/READINP` block → fails. Each input field must match the type declared in its `INPGRID`.
- **Forgetting `MODE STAT` ↔ `COMPUTE STAT`** mismatch → SWAN ignores the inconsistency and assumes nonstationary; debug from the log header.
- **`SET LEVEL` left at 0** when modeling a tide-influenced domain — wave-current interaction wrong.
- **`FRICTION JONSWAP CONSTANT 0.067`** = default; valid for storms but too dissipative for swell — switch to `FRICTION COLL` or measured Madsen for swell-dominated cases.
- **Output before `COMPUTE`** → the `BLOCK/TABLE/SPECOUT/NESTOUT` records the run state; if placed before `COMPUTE`, you get an empty file. Put output commands BEFORE `COMPUTE` (they're declarative; they fire during/after `COMPUTE`).
- ▢ **User-experience cases** — placeholder for project-specific incidents (regional Korea coast, JMA wind, ADCIRC-SWAN coupling).

## Next expansion

- Per-command complete syntax reference (full BNF for each — currently this note treats sub-keywords at summary level).
- ADCIRC-SWAN unstructured coupling — separate note covering how `BOUND` and `READINP UNSTRUC` interact with the coupled model.
- SWAN command file templates per use case (storm hindcast, swell propagation, surf-zone, ice-covered) — separate `protocols/` notes.
- Comparative reference: SWAN command vs WAVEWATCH III input vs Delft3D-WAVE namelist.

## References

### Source code (Codex scan, 2026-05-06)

- `src/swanpre1.ftn` — main `SWREAD` body, parses Group 1–5 commands.
- `src/swanpre2.ftn` — `SWREOQ` / `SWREPS` for Groups 6–7; `SWBOUN` body for `BOUND` details.
- Full subroutine inventory: `[file=/mnt/e/models/swan/manuals/refs/subroutines.md]`.

### Manuals (curated, retrieved 2026-05-06 against `manuals` collection, model=swan)

- `[file=pdf:swan:swanuse]` — User Manual (canonical command reference).
- `[file=pdf:swan:swantech]` — Technical Doc (governing equations, source-term formulations).
- `[file=pdf:swan:swanimp]` — Implementation Manual.
- `[file=pdf:swan:swanpgr]` — Programmer Manual.
- `[file=website:swan:node11]` — Computational grid.
- `[file=website:swan:node12]` — Output grids.
- `[file=website:swan:node13]` — Activation of physical processes (per-process flag matrix).
- `[file=website:swan:node26]` — Input grids and data.
- `[file=website:swan:node27]` — Boundary and initial conditions.
- `[file=website:swan:node28]` — Physics.
- `[file=website:swan:node29]` — Numerics.
- `[file=website:swan:node34]` — Lock-up (stationary convergence).

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 (this session) |
| Generated | 2026-05-06 |
| Source-scan tool | `codex exec --model gpt-5.3-codex` over `/mnt/e/models/swan/source_code/swan/src/` |
| RAG retrieval | rag_proxy on `manuals` filtered `model=swan` (902 chunks across pdf+website doc_types) |
| Coverage | 33 top-level commands; sub-keywords at summary level (full BNF deferred to per-command notes) |
| Review status | `review_required: true` — modeler should validate file:line citations against current SWAN trunk (this scan was post-2024 release-line) |
| Companion notes | `swan-foundation.md`, `swan/manuals/refs/subroutines.md` |
