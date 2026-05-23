---
title: "efdc hydraulic structures"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_hydraulic_structures.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

The EFDC+ hydraulic structure module: structure types via `NQCTYP` (5=culvert, 6=sluice gate, 7=weir, 8=orifice, 9=navigation lock, 10=floating skimmer [unsupported], 11=submerged weir; lookup-table types -2..4 handled in `CALQVS`), the actual formulas (sharp-crested weir Q ∝ H^1.5, V-notch H^2.5, broad-crested, Villemonte submerged correction; sluice gate free/submerged/weir-transition by ratio; culvert full/inlet/outlet/normal control by Manning conveyance), pumps via operation rules (no separate `NQCTYP`), control logic (time-series, upstream-WSEL, head-difference rules), the input format spread across `EFDC.INP` cards C32/C32A/C32B + auxiliary `qctl.inp/qctlser.inp/qctrules.inp` (no `.hyd` or `modstruct.inp`), and how structure flow couples to external/internal mode via `QSUM/QSUME`. Use this when wiring weirs/gates/pumps for navigation channels, flood control, or reservoir operation.

## Source basis

- `mod_hydstructure.f90:9-1296` — `HYDSTRUCMOD` module.
- `Transport/calqvs.f90:756-1217` — `CALQVS` dispatch.
- `input.f90:1352-6671` — input cards C23, C32, C32A, C32B.
- `input.f90:6344-6671` — `qctl.inp`, `qctlser.inp`, `qctrules.inp`.
- `hdmt.f90:587-589`, `hdmt2t.f90:527-529` — `CALQVS` calls.
- `calpuv9c.f90:609-784`, `caluvw.f90:697-736` — coupling.
- `setbcs.f90:303-362` — initial structure masks.

## A. Entry points and types

`HYDSTRUCMOD` scope: culverts, weirs, sluice gates (`mod_hydstructure.f90:9-11`).

Main runtime entry: `COMPUTE_HSFLOW(NCTL)` (`:116`); called from `CALQVS` for `NQCTYP > 4` (`Transport/calqvs.f90:1217-1220`).

Structure equation types in module:

| `NQCTYP` | Type | Lines |
|---|---|---|
| `5` | Culvert | `:267` |
| `6` | Sluice gate | `:361` |
| `7` | Weir | `:439` |
| `8` | Orifice | `:476` |
| `9` | Navigation lock / mask toggle (no direct flow) | `:531` |
| `10` | Floating skimmer wall — **unsupported** | `:707` |
| `11` | Submerged weir | `:711` |

Lookup-table types `NQCTYP = -2..4` handled in `CALQVS` not `COMPUTE_HSFLOW` (`calqvs.f90:756-1028`).

## B. Weirs (NQCTYP=7)

Computes (`:439-445`):
- `HUD = ZHU - USINV` (upstream head over invert).
- `HDD = ZHD - USINV` (downstream head over invert).
- `CDD = HS_COEFF(IHYD, 2)`.

**Sharp-crested formulas** by cross-section:

| Section | Formula | Lines |
|---|---|---|
| Rectangular | `Q = (2/3)·CDD·WOPEN·√(2g)·HUD^1.5` | `:446-448` |
| V-notch / triangle | `Q = (8/15)·CDD·√(2g)·tan(θ/2)·HUD^2.5` | `:450-452` |
| Trapezoid | Rectangular + triangular | `:454-458` |

**Broad-crested** (`HS_XSTYPE=8`):
```
Q = CDD · WOPEN · √(2g) · HUD^1.5
```
(`:460-463`).

**Villemonte submerged** when downstream water above invert:
```
Q *= (1 - HDD/HUD)^0.385
```
(`:471-473`).

## C. Gates (NQCTYP=6 sluice)

Opening width + height controlled by `WOPEN, HOPEN` (`:363-365`).

Branch chooses among (`:376-418`):
- Free sluice/orifice.
- Submerged orifice.
- Weir-like transition.

Selection by ratios `HDD/HUD` and `HUD/HB`.

**Control logic** (`:166-1185`):
- **Time-series controls**: interpolate height/width/sill via `GATE_OPENING_INTERP` (`:166, 174, 1259`).
- **Rule controls**:
  - `ITYPE=2`: upstream WSEL trigger.
  - `ITYPE=3`: WSEL difference trigger.
- Bit `1` controls height; bit `2` width; bit `4` sill/lower gate (`:203, 211, 219`).
- Each calls `GATE_OPERATION_RULES`.
- Gates ramp by `RATE * DELT / 60` until limit reached (`:1168-1185`).

## D. Pumps

**No separate `NQCTYP` for pumps** in `COMPUTE_HSFLOW`. Pumps via operation rules when rule `PARAM` has bit `16` set; then `PUMP_OPERATION_RULES` returns `QHS` directly (`:191-197`).

Pump rule data: target `FLOW`, `RATE` (`:41`, `input.f90:6580-6581`).

Pump ramps flow up/down by `RATE * DELT / 60` until `LIM.FLOW` (`mod_hydstructure.f90:1084-1095`).

**Q-vs-head tables** are general `QCTL.INP` lookups, NOT pump-specific:
- 1D and 2D head/elevation tables (`input.f90:6344-6387`).
- Rules can switch lookup table IDs via bit `32` (`:6671`, `mod_hydstructure.f90:1296`).

## E. Culverts (NQCTYP=5)

Geometry + conveyance from `CROSS_SECTION` (`:271-271`):
```
KCON = area / Manning_n · hydraulic_radius^0.6667
```
(`:957-959`).

**Flow regimes** (`:306-327`):

| Condition | Regime | Formula |
|---|---|---|
| `HDD > DIA` or `HUD > 1.5·DIA` | Full pipe | `Q = KCON·√S` |
| `S >= SCR` | Supercritical inlet control | `Q = QCR` |
| `S < SCR` and `HDD >= HCR` | Subcritical tailwater control | Manning velocity at tailwater depth |
| `HDD < HCR` and `S < SCR` | Subcritical outlet control | Normal-depth Manning velocity |

**No explicit entrance/exit-loss coefficients** in the culvert branch. C32A reads geometry, length, Manning `HS_MANN`, invert elevations, four generic coefficients — but culvert uses length/Manning/conveyance, not `HS_COEFF` losses (`:1668-1669, 287, 319`).

## F. Operating rules

Control state values: closed/off, open/on, opening, closing (`mod_hydstructure.f90:30-35`).

Control types: uncontrolled, time-series, upstream-level rules, head-difference rules (`:73-78`).

Input files:

| File | Fields |
|---|---|
| `QCTLSER.INP` | time, height, width, sill, flow, table ID (`input.f90:6439, 6456, 6488, 6491`) |
| `QCTRULES.INP` | trigger level, on/off, ID, height, width, sill, flow, rate (`:6510, 6544, 6573, 6581`) |

## G. Input format

**No reader for `.hyd` or `modstruct.inp`**. Hydraulic structures from `EFDC.INP` cards + auxiliary files:

| Card / file | Content |
|---|---|
| C23 | counts `NQCTL, NQCTLT, NHYDST, NQCTLSER, NQCTRULES` (`:1352-1357`) |
| C32 | per-structure location/type/table/multipliers/control metadata (`:1607-1616`) |
| C32A | equation parameters for `NHYDST` structure equations (`:1661-1668`) |
| C32B | per-structure control assignment + initial state/opening (`:1702-1714`) |
| `qctl.inp` | lookup/rating tables (`:6344-6348`) |
| `qctlser.inp` | control time series (`:6439-6445`) |
| `qctrules.inp` | rule triggers (`:6510-6516`) |

## H. Coupling to external/internal mode

`CALQVS` called in both hydro drivers before solve (`hdmt.f90:587-589`, `hdmt2t.f90:527-529`).

Hydraulic structure flows added as **layer source/sink** terms:
- Upstream `QSUM(LU,K)` reduced.
- Downstream `QSUM(LD,K)` increased.
(`mod_hydstructure.f90:742-776`).

`CALQVS` then sums layer sources into external-mode source `QSUME` (`Transport/calqvs.f90:1729-1736`).

External pressure/free-surface solve uses `QSUME` in pressure RHS + depth update (`calpuv9c.f90:609, 771-784`).

Internal vertical velocity uses baroclinic residual `QSUM(L,K) - DZC(L,K)*QSUME(L)` (`caluvw.f90:697-736`).

**Navigation locks** couple via face masks (not discharge): set `SUB/SVB` and 3D mask arrays open/closed (`mod_hydstructure.f90:675-700`).

Initial/default structure masks set in `SETBCS` (`setbcs.f90:303-362`).

## Decision Guide

| Structure | `NQCTYP` | Notes |
|---|---|---|
| Sharp-crested rectangular weir | `7`, `HS_XSTYPE=1` | Free flow; Villemonte submerged auto |
| V-notch weir | `7`, `HS_XSTYPE=2` | Triangular Q∝H^2.5 |
| Trapezoidal weir | `7`, `HS_XSTYPE=3` | Combined rectangular+triangular |
| Broad-crested weir | `7`, `HS_XSTYPE=8` | C-coefficient typically 0.55-0.6 |
| Submerged weir | `11` | Always submerged; uses `HS_COEFF(:,3)` |
| Sluice gate | `6` | Auto-detects free/submerged/transition |
| Vertical lift gate (controlled) | `6` with rule control | Time-series or WSEL trigger |
| Culvert (circular) | `5`, `HS_XSTYPE=4` | Full/partial flow auto |
| Box culvert | `5`, `HS_XSTYPE=1` | Rectangular cross-section |
| Pump (Q-target) | Operation rule with bit 16 | Constant or ramping rate |
| Q-vs-head pump | Use `QCTL.INP` lookup | Not via `NQCTYP` |
| Navigation lock | `9` | Mask-based (no direct flow); use scheduling |

## Working Rules

- For weirs, `WOPEN` is crest length (m); `HOPEN` is invert depth.
- Sluice gate `WOPEN×HOPEN` defines opening area; ramp via `RATE` parameter.
- Culvert Manning n in `HS_MANN`; typical 0.012-0.018 for concrete, 0.024 for corrugated metal.
- Pumps via operation rules require `QCTRULES.INP` with bit-16 `PARAM`.
- Time-series control vs rule control: `QCTLSER.INP` for prescribed schedules; `QCTRULES.INP` for state-dependent.
- Navigation locks (`NQCTYP=9`) toggle face masks; set `IL_LCK` for which faces; for full lock simulation, supplement with mass tracking externally.
- Verify structure flow in output: `QHS` per structure; sign convention upstream→downstream positive.
- For coastal cases (Korean tidal gates): typically `NQCTYP=6` with rule control responding to upstream tide.

## Common Pitfalls

- ▢ Looking for `.hyd` file — doesn't exist; use `EFDC.INP` cards C32/C32A/C32B + auxiliary files.
- ▢ Setting `NQCTYP=10` (floating skimmer) — explicitly unsupported.
- ▢ Pump as `NQCTYP` — not implemented; use operation rules with bit 16.
- ▢ Culvert with no `HS_MANN` — defaults give wrong conveyance.
- ▢ Submerged weir `NQCTYP=11` confused with submerged sharp-crested via Villemonte (`NQCTYP=7`) — different formulations.
- ▢ Forgetting Villemonte submerged correction for `NQCTYP=7` — automatic only when `HDD/HUD > 0`; check downstream WSEL.
- ▢ Rule control without `QCTRULES.INP` parameters — rule fails silently.
- ▢ Channel `MDCHH` for narrow waterway vs hydraulic structure — different mechanisms; choose one.

## Next expansion

- Tide gate operating-rule example (Korean coast).
- Pump scheduling for reservoir.
- Culvert array (multi-cell) configuration.

## References

- USACE 1990 (Hydraulic Design of Spillways).
- Villemonte 1947 (submerged weir).
- Manning open-channel flow.
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
