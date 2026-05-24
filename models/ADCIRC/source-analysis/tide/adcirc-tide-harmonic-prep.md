---
title: "adcirc tide harmonic prep"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-tide-harmonic-prep.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

Exactly what ADCIRC's reader expects in the fort.15 NBFR boundary harmonic block (`AMIG/FF/FACE` + per-node `EMO/EFA`), how `fort.24`/`fort.24.nc` self-attraction-and-loading (SAL) is read (only when `NTIP=2`), how constituent name matching works (strict, case-sensitive trim), the units/sign/phase conventions ADCIRC applies, and what `REFTIM` does to the harmonic time base. Use this when converting external databases (NAO99jb, FES2022b, TPXO) to ADCIRC inputs, or debugging tide phase/amplitude validation errors.

**Key fact**: ADCIRC has **no built-in parser** for FES/NAO/TPXO databases. It only consumes preprocessed `fort.15` harmonic block and optional `fort.24` SAL.

## Source basis

- `read_input.F:1705-1731, 3344-3497, 6282-6463` — `NTIP`, NBFR boundary block, SAL reader.
- `gwce.F:1638-1650` — boundary elevation synthesis.
- `timestep.F:251-258, 1517-1562` — `TimeH` and tidal-potential application.
- `hstart.F:1525-1532` — SAL into TIP2.

## A. fort.15 NBFR boundary harmonic block

```
NBFR
do j = 1, NBFR
   BOUNTAG(j)                      ! constituent tag string
   AMIG(j)  FF(j)  FACE(j)         ! frequency, nodal factor, equilibrium argument (deg)
end do
do j = 1, NBFR
   ELEVALPHA(j)                    ! constituent tag (printed only, no validation)
   do i = 1, NETA
      EMO(i,j)  EFA(i,j)           ! amplitude (m), phase lag (deg)
   end do
end do
```

References (`read_input.F`):
- `NBFR` read + arrays allocated: `:3410-3418`.
- Per-constituent header `BOUNTAG, AMIG, FF, FACE`: `:3431-3436`.
- `FACE` deg → rad after read: `:3436`.
- Per-constituent boundary block `ELEVALPHA + EMO/EFA`: `:3450-3455`.
- `EFA` deg → rad after logging: `:3493-3497`.

Important: `ELEVALPHA` is **only printed** as "verification"; **no match/validation against `BOUNTAG`** (`:3485-3490`). You must keep the per-constituent ordering consistent yourself.

## B. fort.24 SAL reader

Called from main startup (`adcirc.F:292-293`); reader at `read_input.F:6282-6463`.

**Active only for `NTIP=2`**:
- `NTIP < 2`: SAL arrays zeroed (`:6460-6462`).
- `NTIP=0`: tidal potential entirely off.
- `NTIP=1`: tidal potential active, no SAL.
- `NTIP=2`: tidal potential + SAL.

NetCDF preferred if `fort.24.nc` exists (`:6330-6344`).

### NetCDF format

Required dims/vars (`:6353-6365`):
- Dimensions: `node`, `num_constituents`, `char_len`.
- Variables: `constituents`, `frequency`, `sal_amplitude`, `sal_phase`.

Constituent count must equal `NTIF` (`:6367-6371`).

### ASCII format (`fort.24`)

Per-constituent block (`:6429-6455`):
```
<dummy_char>  <dummy_char>          ! 2 dummy chars
<dummy_real>                        ! ignored
<dummy_int>                         ! ignored
<const_name>                        ! e.g. "M2"
do i = 1, num_nodes
   JJ  SALTAMP(JJ)  SALTPHA(JJ)
end do
```

`SALTPHA` deg → rad after read.

## C. Constituent matching

`fort.15` tidal-potential tags are **`TIPOTAG`** (different from `BOUNTAG`!) (`:3347-3349`).

- NetCDF SAL: `TRIM(TIPOTAG(I)) == TRIM(const_name)` (`:6378-6385`).
- ASCII SAL: each SAL `const_name` matched to some `TIPOTAG(J)` (`:6436-6443`).

**Strict, case-sensitive**, no aliasing.

## D. Phase / sign / units

| Quantity | Input units | Internal (post-read) | Sign |
|---|---|---|---|
| `FACE`, `FACET` (eq. arg.) | degrees | radians | added to argument |
| `EFA` (boundary phase lag) | degrees | radians | **subtracted** in `cos(arg − EFA)` |
| `SALTPHA` (SAL phase) | degrees | radians | **subtracted** in `cos(arg − SALTPHA)` |
| `EMO`, `SALTAMP` | meters | (no conversion) | direct multiplier |

Boundary synthesis (`gwce.F:1644-1649`):
```
Eta2(NBDI) += EMO * FF * RampElev * cos(AMIG*timeh + FACE − EFA)
```

SAL synthesis into `TIP2` (`timestep.F:1547-1548`, `hstart.F:1525-1532`):
```
TIP2 += SALTMUL * SALTAMP * cos(ARGT − SALTPHA)
```

ADCIRC uses **lag-subtracted** phase (`cos(arg − phase)`). FES2022b convention is the same; NAO99jb and TPXO also use lag convention. **Confirm** before using a database.

## E. FF and FACE meaning

- `FF` (boundary): nodal factor (multiplies amplitude at runtime).
- `FFT` (tidal potential): same role for potential and SAL.
- `FACE` (boundary): equilibrium argument `(V₀ + u)` (added to argument).
- `FACET` (tidal potential): same role for potential.

These come from astronomical theory; standard tools (T_TIDE, UTIDE, pyTMD) compute them per epoch.

## F. REFTIM and TimeH

`REFTIM` is the harmonic reference time in **days** (`:2541`).

```
TimeH = IT * DTDP + (StaTim − RefTim) * 86400
```
(`timestep.F:251-258`).

Harmonic synthesis uses `timeh`, **not** raw model time (`gwce.F:1642-1644`, `timestep.F:1532-1535`).

**This is the most common source of phase errors**: `FACE`/`FACET` from your database are computed for some epoch (often midnight UTC of a specific day). `REFTIM` must match that epoch, expressed in your run's time-axis convention.

## G. NAO99jb / FES2022b workflow

ADCIRC has **no native NAO/FES parser**. You preprocess externally:

1. Pick run start `STATIM` and epoch `REFTIM`.
2. For each constituent (M2, S2, K1, O1, etc.), get astronomical `f` (nodal factor), `(V₀+u)` (eq. arg) for `REFTIM` from T_TIDE / UTIDE / pyTMD.
3. From FES/NAO database, extract per-boundary-node amplitude and Greenwich phase lag at the configured constituent set.
4. Write `fort.15` NBFR block:
   - Header line `NBFR`.
   - Per constituent: `BOUNTAG`, then `AMIG, FF, FACE` (FF and FACE both for `REFTIM` epoch, FACE in degrees).
   - Per constituent: `ELEVALPHA`, then per-node `EMO  EFA` (EFA in degrees, **lag** convention).

For SAL, similar process; write to `fort.24` ASCII or `fort.24.nc` NetCDF.

## H. Validation pitfalls

- ▢ **Wrong epoch** for `REFTIM` vs `FACE/FACET` — phase off by a constant. Symptom: high phase RMSE but reasonable amplitude.
- ▢ **Lead vs lag** phase convention — sign flip. Symptom: phase off by ~180° on some constituents. Confirm `cos(arg − phase)` form.
- ▢ **Greenwich vs local** zone phase — many databases give Greenwich (UTC); ADCIRC's `STATIM/REFTIM` defines its own zone (usually UTC by convention).
- ▢ **Amplitude in cm not m** — silent factor of 100.
- ▢ **Constituent name mismatch** — strict trim; "M2" != "m2" (case sensitive in some compilers).
- ▢ **Order mismatch** between `BOUNTAG` and `ELEVALPHA` blocks — `ELEVALPHA` is only printed; you must keep order consistent manually.
- ▢ **Forgetting nodal correction** — if you use astronomical reference `(V₀+u)` for *one* date but run for years, `f` and `(V₀+u)` change. ADCIRC applies them as constants — for runs > 1 month, recompute or accept reduced accuracy.
- ▢ **NTIP=2 without `fort.24`** — SAL arrays stay zero; the model runs but you lose SAL physics. Check log for "fort.24 not found."

## Decision Guide

| Need | Setup |
|---|---|
| Tide-only run | `NTIP=1`, fort.15 NBFR block; **no fort.24** |
| Tide + SAL (recommended) | `NTIP=2`, fort.15 NBFR + fort.24 |
| FES2022b global | T_TIDE/pyTMD for FF/FACE; FES interpolation for amplitudes/phases at boundary nodes |
| NAO99jb regional (Asia/Pacific) | Same workflow; NAO99jb covers M2/S2/K1/O1 well |
| Combined FES + tide gauge | Boundary from FES; verify against gauges in interior |
| TPXO global | Similar; conventions match |
| Long run (>1 yr) | Document FF/FACE epoch; consider re-running with new astronomical reference quarterly |
| Storm hindcast (no tide) | `NTIP=0`, no NBFR block |

## Working Rules

- Always write `STATIM`, `REFTIM`, and the FF/FACE epoch in the run README. These three must align.
- Use 8-character constituent names ("M2      ", "S2      ", etc.) padded; ADCIRC trims, but consistent is safer.
- Output `fort.51` harmonic analysis at validation stations to compute model-side amplitude/phase, then compare against gauge harmonic constants — this is far more diagnostic than time-series RMSE.
- For Korean coast, NAO99jb gives good M2/S2/K1/O1 starting point; FES2022b adds N2, K2, P1 if you need finer accuracy.
- SAL from fort.24 typically reduces M2 amplitude by ~5-10% in shelf seas — if your run shows persistent +10% M2 overprediction, missing SAL is a likely cause.

## Common Pitfalls

(See "H. Validation pitfalls" above — most issues come from epoch and phase convention.)

Additional:
- ▢ Hot-start across `NTIP` change — harmonic accumulators / SAL arrays inconsistent.
- ▢ Modifying NBFR block but not regenerating SAL constituent set — names mismatch silently.
- ▢ Nesting (boundary forcing from coarse-grid output) — coarse `EMO/EFA` may not be exact at fine boundary nodes; interpolate carefully.

## Next expansion

- T_TIDE / pyTMD recipe for FF/FACE generation.
- FES2022b → fort.15 conversion script.
- SAL preparation from FES2022b loading-tide grids.
- Validation harmonic analysis (`fort.51`) post-processing.

## References

- Westerink et al. 1992 (ADCIRC tide formulation).
- Hendershott 1972 (SAL theory).
- T_TIDE: Pawlowicz et al. 2002.
- UTIDE: Codiga 2011.
- FES2022b: Lyard et al. 2024.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
