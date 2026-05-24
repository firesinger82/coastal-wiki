---
title: "efdc boundary conditions"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_boundary_conditions.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How EFDC+ ingests boundary time series (`PSER` elevation, `NCSER` concentration, `NQSER` flow), where the south/west/east/north pressure-BC index arrays come from, how `SETBCS` (init) vs `SETOPENBC` (runtime) divide labor, how the `MTIDE` harmonic synthesis is added on top of `PSER`, how subgrid channels (`SUBCHAN`) couple to the external solver, and how dry open-boundary cells (`LOPENBCDRY`) are detected and disabled. Use this when wiring tide+harmonic forcing, debugging volumetric source mass closure, or interpreting a multi-boundary card structure.

## Source basis

- `input.f90:264, 548, 732-754, 852-867, 870-1321, 1352-1378, 2721-2995, 3656-3705, 5650-5685, 5717-5755, 5858-6277` — input cards C5, C11, C14–C24, time series headers.
- `calpser.f90:25-66` — runtime PSER interpolation.
- `setbcs.f90:203-490` — initialization of BC mappings + face/momentum mask setup.
- `setopenbc.f90:231-620` — runtime pressure BC application (S/W/E/N), `LOPENBCDRY`.
- `Transport/calcser.f90`, `Transport/calqvs.f90`, `Transport/calfqc.f90` — concentration/flow series interpolation and injection.
- `subchan.f90`, `mod_chanbc.f90` — subgrid channel.
- `calpuv9c.f90:638-642, 771-846, 1277-1304`, `calpuv2c.f90:591-599, 733-734, 747-790, 1191-1217`.

## A. PSER (water surface elevation series)

Read when `NPSER >= 1`. Header: `ITYPE, NREC, TMULT, TOFFSET, RMULADJ, ADDADJ, PSERZDF, INTPSER`.

| ITYPE | Record | Use |
|---|---|---|
| `0` | `(t, η)` | Single-side elevation series |
| `1` | `(t, η_primary, η_secondary)` + secondary adjustment | Cross-channel slope, two-side coupling |

Conversion to pressure-head: `G * η` units (`input.f90:5650-5685`). Datum shifts `PSERZDF/PSERZDS` also × G (`:5661-5665`).

Runtime in `CALPSER`:
- Time scaling by `TMULT`, advance `MTSPLAST`.
- Linear interpolation or Catmull-Rom spline by `INTPSER`.
- Result → `PSERT, PSERST` (`calpser.f90:25-66`).

Application via `SETOPENBC` (called from both external solvers):
- `calpuv9c.f90:638-642` (3TL) or `calpuv2c.f90:591-599` (2TL).
- Applied as `PSERT + PSERZDF/2 + PSERST + PSERZDS/2` at S/W/E/N pressure cells (`setopenbc.f90:252-260, 357-365, 460-469, 566-574`).

`CALEXP` does not read PSER directly; it modifies momentum for open-boundary types `2` and `5` (`calexp.f90:629-669`; 2TL `calexp2t.f90:581-620`).

## B. NCSER (concentration time series)

`NCSER(1:7)` drives **7 constituent families**:

| Index | Constituent | File pattern |
|---|---|---|
| 1 | Salinity | `SSER` |
| 2 | Temperature | `TSER` |
| 3 | Dye | `DSER` |
| 4 | Shellfish larvae | `SFSER` |
| 5 | Toxics | `SDSER`/`SNSER` |
| 6 | Cohesive sediment | `SDSER` |
| 7 | Noncohesive sediment | `SNSER` |

Header: `ISTYP, MCSER, TCCSER, TOFFSET, multiplier, additive`, with either layer weights or per-layer values.

Examples:
- Salinity at `input.f90:5858-5904`.
- Temperature `:5907-5951`.
- Dye `:5955-6015`.
- Sediment/toxic `:6066-6277`.

Open-concentration BC cards (per side, `NCSER*` indices + ramp `NTSCR*`):
- South `input.f90:2721-2737`.
- West `:2807-2823`.
- East `:2893-2909`.
- North `:2979-2995`.

Runtime: `CALCSER` interpolates into `CSERT(K, NS, variable)` (`Transport/mod_calcser.f90:54-157`).

Injection (two paths):
1. **Open-BC**: `CALTRAN` flow-direction-dependent — inflow uses bottom/surface BC + `CSERT`; outflow extrapolates from interior (`Transport/caltran.f90:221-340`).
2. **Volumetric source/river**: `CALFQC` — positive `QSS/QSERCELL` injects `CQS/CSERT`; negative removes local `CONQ` mass (`Transport/calfqc.f90:238-248`).

## C. NQSER (flow time series, river discharge)

Card C23 reads `NQSIJ` and `NQSER` counts (`input.f90:1352-1360`).

C24 reads each volumetric source cell:
`I, J, QSSE, NQSMUL, NQSMF, NQSERQ, NCSERQ(1:7), QWIDTH, QFACTOR, GRPID` (`input.f90:1365-1378`).

MPI mapping preserves `NQSERQ, NCSERQ, QFACTOR, QWIDTH, GRPID` (`MPI_Mapping/Map_Discharge_BCs.f90:50-69`).

`QSER.INP` header: `ISTYP, NREC, TMULT, TOFFSET, RMULADJ, ADDADJ, ICHGQS`.

| ISTYP | Behavior |
|---|---|
| `1` | Reads vertical weight vector `WKQ(K)`; scalar flow distributed by layer |
| else | Each record gives layer flows directly |

Sign clipping by `ICHGQS` (`input.f90:5717-5755`).

Runtime:
- `CALQVS` interpolates → `QSERT(K, NS)` (`Transport/calqvs.f90:428-449`).
- Maps to each source as `QSERCELL(K, LL)`, adds to `QSUM(L, K)` (`:502-531`).
- Inactive layers redistributed into active (`:533-558`).

**Mass conservation**: `QSUME(L)` reset and rebuilt as sum over layers (`:367-375, 1729-1737`); used in external continuity / depth update (`calpuv9c.f90:771-785`; `calpuv2c.f90:733-734`). Withdrawal limits prevent dry/negative volume by clipping outflows to available water (`Transport/calqvs.f90:1742-1899`).

## D. NPBS / NPBE / NPBN / NPBW (pressure BC indices)

C16 reads counts: `NPBS, NPBW, NPBE, NPBN, NPFOR, NPFORT, NPSER, PDGINIT` (`input.f90:870-889`).

Per-boundary pressure cells:

| Card | Side | Tokens |
|---|---|---|
| C18 | South | `IPBS, JPBS, ISPBS, ISPRS, NPFORS, NPSERS` (`:966-1054`) |
| C19 | West | `IPBW, JPBW, ISPBW, ISPRW, NPFORW, NPSERW` (`:1057-1143`) |
| C20 | East | `IPBE, JPBE, ISPBE, ISPRE, NPFORE, NPSERE` (`:1146-1231`) |
| C21 | North | `IPBN, JPBN, ISPBN, ISPRN, NPFORN, NPSERN` (`:1235-1321`) |

`SETBCS` maps these I/J indices to local cell indices `LPB*` and turns off face/momentum/diffusion masks around open boundaries (`setbcs.f90:211-300`).

## E. SETBCS vs SETOPENBC

`SETBCS` = **initialization** (called once at startup):
- Maps river/open-boundary/concentration structures (`:203-209`).
- Maps pressure BC cells and masks (`:211-300`).
- Sets volumetric source multipliers (`:478-490`).

`SETOPENBC` = **runtime external-mode dispatch** (called every external solve):
- `CALPUV9C` calls when `NBCSOP > 0` (`calpuv9c.f90:638-639`).
- `CALPUV2C` same (`calpuv2c.f90:591-592`).
- Loops S, W, E, N and assembles `FP, CC, CS/CW/CE/CN` per side (`setopenbc.f90:240-620`).

## F. SUBCHAN (subgrid channel)

`MODCHAN.INP` read when `ISCHAN > 0`. Supplies `MDCHH, QCHERR, channel type, host cell, U/V channel cells`, plus channel length/friction for `ISCHAN==2` (`input.f90:3656-3689`).

Host and channel I/J → `LMDCHH, LMDCHU, LMDCHV` (`:3692-3705`).

`SUBCHAN`:
- Active when source/receiver have adequate wet depth.
- Forms implicit coefficients, modifies external linear-system diagonal/RHS (`subchan.f90:28-125`).
- Inserted into `CALPUV9C:641-642` and `CALPUV2C:594-599`.
- Solved channel flows updated after pressure solve (`calpuv9c.f90:736-759`; `calpuv2c.f90:697-720`).
- Tracer exchange in `Transport/calfqc.f90:377-402`.

## G. Tide harmonic synthesis (MTIDE, NPFOR)

There is **no `NWTSER` symbol**; equivalent is `MTIDE` plus periodic pressure forcing `NPFOR`.

- C14 reads `MTIDE` (`input.f90:732-754`).
- C15 reads tidal symbols + periods `SYMBOL(M), TCP(M)` (`:852-867`).
- C17 reads harmonic amplitude/phase, converts phase to cos/sin coefficients (`:891-920`).

Boundary cards convert harmonics to `PCB*/PSB*` for each side (× G):
- South `input.f90:980-1005`.
- West `:1070-1096`.
- East `:1159-1185`.
- North `:1249-1275`.

Runtime: `SETOPENBC` computes `cos/sin` from `TIMESEC` and `TCP` (`setopenbc.f90:231-238`), adds `PCB*cos + PSB*sin` to each boundary pressure (`:257-260, 362-365, 466-469, 571-574`).

So total boundary head = PSER series + harmonic synthesis. Either alone or combined.

## H. Wet/dry interaction with active BC nodes

Open BCs disable themselves when forced elevation falls below bed + dry threshold:
- `SETOPENBC` checks `FP1G < BELV(...)`, sets `LOPENBCDRY(L) = .TRUE.`, resets coefficients, skips cell:
  - South `:295-306`. West `:400-411`. East `:504-515`. North `:609-620`.

After pressure solve, `CALPUV` applies open-boundary depths from `P`, checks negative/dry, clamps `HP`, zeros face masks/fluxes, marks `LOPENBCDRY` (`calpuv9c.f90:804-846`; `calpuv2c.f90:747-790`).

Dry-cell transport masks **deliberately keep active boundary-flow cells alive**: if `HP < HDRY`, dry bypass is skipped when `QSUME(L) /= 0.0` (marked "active boundary" at `calpuv9c.f90:1277-1304`; `calpuv2c.f90:1191-1217`). Concentration open-BC updates skip inactive/dry layers via `LKSZ` and `LMASKDRY` checks (`Transport/caltran.f90:225-325`).

## Decision Guide

| Need | Setting |
|---|---|
| Tide-only forcing | `NPSER=0`, `MTIDE >= 1`, harmonic block in C17 |
| Observed water-level time series | `NPSER >= 1`, `PSER.INP` per side |
| Combined tide + meteorological surge | Both: PSER from observation + harmonic block (residual treatment) |
| River inflow with concentration | `NQSIJ + NQSER`, layered `WKQ` if vertical profile matters |
| Salinity tidal forcing at ocean BC | `NCSER(1) >= 1`, ISTYP per layer, ramp via `NTSCR1` |
| Two-side cross-channel slope | PSER `ITYPE=1` |
| Dry intertidal BC cell | Move BC offshore OR accept `LOPENBCDRY` switching it off intermittently |
| Subgrid tidal creek connecting two cells | `ISCHAN >= 1` with `MODCHAN.INP` |
| Multiple BC cells with same time series | Reuse `NPSERS/NPSERW/...` index across cells |

## Working Rules

- Always set `INTPSER=1` (Catmull-Rom) for tidal-data PSER — linear interp introduces sub-tidal noise.
- `RMULADJ` and `ADDADJ` apply to **all** records; check before scaling.
- BC ramp `NTSCR*` is in **timesteps**, not seconds — set proportional to spin-up duration.
- For multi-river runs, group `GRPID` lets you scale a subset uniformly via post-processing — useful for sensitivity tests.
- Harmonic block (C17) `phase` is in **degrees**; if amplitudes are in cm, ensure `RMULADJ=0.01` to convert to m.
- `LOPENBCDRY` events are logged — grep stdout for "OPEN BC DRY" during validation.
- Subgrid channel needs both donor and receiver cells to be active wet for the channel itself to be active; design `MODCHAN.INP` accordingly.

## Common Pitfalls

- ▢ Confusing `NPSER` (count of PSER series) with `NPSERS/NPSERW/NPSERE/NPSERN` (per-cell index pointer to which series to use).
- ▢ Setting `NCSER(6) = 1` for cohesive sediment without also setting `ISTRAN(6) = 1` — concentration series read but never applied.
- ▢ Forgetting `QFACTOR` (default 1.0) — useful to scale a single source without rewriting `QSER.INP`.
- ▢ Using harmonic block without rebuilding `TCP` periods after changing `TBEGIN`/`STARTTIME` — astronomical phase reference shifts.
- ▢ Volumetric source `QSS` injection at a dry cell — will queue but not enter the system; check `LOPENBCDRY` log.
- ▢ `ISTYP=1` QSER without proper `WKQ(K)` (must sum to 1) — silent under-injection.
- ▢ Hot-start with different `NPSER` count than cold run — index pointers misalign.

## Next expansion

- Tide harmonic preparation workflow (T_TIDE / UTIDE → C17 block conversion).
- River+ocean coupled BC ramp recipe.
- Subgrid channel sizing guidelines.

## References

- Hamrick 1992 (open-boundary formulation).
- EFDC+ User's Manual / Theory Documentation (Dynamic Solutions, latest).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
