---
slug: swan-source-terms-implementation
title: SWAN source/sink terms — code-level implementation
category: methods
model: swan
auto_draft: false
authored_by: claude-opus-4-7
review_required: true
generated: 2026-05-06
basis: deep Codex source scan of swan/src/{swancom1-4,SdsBabanin}.ftn + swantech ch.2.3
---

# SWAN source/sink terms — code-level implementation

## Scope note

How SWAN's source-term ledger `Stot = Sin + Sds,w + Snl4 + Snl3 + Sds,b + Sds,br` is actually integrated in the source code — which routine implements which formulation, the variable names, the implicit-vs-explicit splitting strategy per term, and the entry into the per-grid-point matrix `(IMATDA, IMATRA)`.

Companion to `swan-propagation-implementation.md` (which covers the propagation matrix). Together they describe the per-iteration solve.

## Source basis

- **Codex deep code analysis** of `/mnt/e/models/swan/source_code/swan/src/{swancom1.ftn, swancom2.ftn, swancom3.ftn, swancom4.ftn, SdsBabanin.ftn90}` — 2026-05-06.
- **Manual cross-reference** from swantech ch.2.3 (Sources and sinks, pages 21–52).

## Implicit/explicit splitting principle

Each source term is split between matrix diagonal (`IMATDA`) and RHS (`IMATRA`). The convention:
- **`IMATDA`** = implicit contribution (multiplies the unknown `AC2` after solve)
- **`IMATRA`** = explicit contribution (adds directly to RHS, computed from prior `AC2`)

A common idiom — Patankar's positive-coefficient rule:
```
if S_local > 0:  IMATRA += S_local * AC2     # treat as positive source on RHS
else:            IMATDA += -S_local           # treat as positive sink on diagonal
```
This keeps the diagonal positive (stable for Thomas/SIP) regardless of source-term sign.

## A. Wind input (`Sin`)

Top-level dispatch in `SWCOMP` source-term loop:

| Formulation | Routine | Routine file:line | Caller |
|-------------|---------|-------------------|--------|
| GEN1 / GEN2 | `WNDPAR` | `[file=src/swancom3.ftn line=30]` | `[file=src/swancom1.ftn line=7443]` |
| GEN3 linear seed | `SWIND0` | `[file=src/swancom3.ftn line=1526]` | `[file=src/swancom1.ftn line=7418]` |
| GEN3 Snyder/Komen | `SWIND3` | `[file=src/swancom3.ftn line=1842]` | `[file=src/swancom1.ftn line=7454]` |
| GEN3 Janssen | `SWIND4` | `[file=src/swancom3.ftn line=2094]` | `[file=src/swancom1.ftn line=7464]` |
| GEN3 Yan / Westhuysen wind branch | `SWIND5` | `[file=src/swancom3.ftn line=2668]` | `[file=src/swancom1.ftn line=7475]` |
| Babanin / ST6 (`SWIND_DBYB`) | `SdsBabanin.ftn90:344` | (`SWIND_DBYB`) | `[file=src/swancom1.ftn line=7489]` |

Inputs each formulation reads (key variables): `WIND10, UFRIC, THETAW, ANYWND, AC2, KWAVE, SPCSIG, CGO, FPM` and parameter array `PWIND(*)`.

### Matrix accumulation per formulation
- `WNDPAR` — both branches: `IMATDA += SWIND_IMP`, `IMATRA += SWIND_EXP` `[file=src/swancom3.ftn line=512-513]`
- `SWIND0` — explicit only: `IMATRA += SWINEA` `[file=src/swancom3.ftn line=1782]`
- `SWIND3` — explicit only: `IMATRA += SWINEB * AC2` `[file=src/swancom3.ftn line=2061]`
- `SWIND4` — explicit only: `IMATRA += SWINEB * AC2` `[file=src/swancom3.ftn line=2623]`
- `SWIND5` — explicit only: `IMATRA += SWINEB * AC2` `[file=src/swancom3.ftn line=2881]`; `IWCAP=7` triggers Yan-coefficient adjustment `[file=src/swancom3.ftn line=2856]`
- ST6 (`SWIND_DBYB`) — explicit, RHS via `FILSIN`: `[file=SdsBabanin.ftn90 line=1584]` then `IMATRA += memsins` `[file=SdsBabanin.ftn90 line=1696]`

So **most GEN3 wind input is purely explicit** (added to RHS), while GEN1/GEN2 (`WNDPAR`) splits between implicit and explicit. Babanin/ST6 uses a memo-table pattern (`MEMSINB`) computed once and replayed per sweep.

## B. Whitecapping (`Sds,w`)

Dispatcher:
- `SWCAP` for `IWCAP <= 7` — `[file=src/swancom1.ftn line=7506]`
- `SWCAP8` for ST6 — `[file=src/swancom1.ftn line=7511]`

| Formulation | Code location |
|-------------|---------------|
| Komen-family coefficient `C_K` | `[file=src/swancom2.ftn line=2485-2491]` (uses `PWCAP(1,2,9,10,11), KM_WAM, ETOT`) |
| Battjes-Janssen WC coefficient `C_BJ` + `QB_WC` | `[file=src/swancom2.ftn line=2503-2511]` (uses `FRABRE, HM, HRMS, PWCAP(7)`) |
| Westhuysen / Alves-Banner saturation `B`, `FBR`, exponent `P` | `[file=src/swancom2.ftn line=2575-2592]` |
| Babanin / ST6 (`SWCAP8`) | `[file=src/swancom2.ftn line=2693]` with core `CALC_SDS` at `[file=src/swancom2.ftn line=2859]` |

### Matrix accumulation
- Implicit on diagonal: `IMATDA += WCAP(IS)` `[file=src/swancom2.ftn line=2645]` (and ST6 at `[file=src/swancom2.ftn line=2896]`)
- Optional explicit compensation (IWCAP 4/5): `IMATRA += WCIMPL * AC2` `[file=src/swancom2.ftn line=2661]`

So whitecapping is **primarily implicit** — gives positive contribution to diagonal which keeps the Thomas/SIP solve stable.

## C. Quadruplet (`Snl4`, DIA)

DIA setup and dispatch:
- λ-triangle setup (`LAMM2/LAMP2`, `DELTH3/DELTH4`, `DAL1/2/3`) in `FAC4WW`: `[file=src/swancom4.ftn line=245-253]`
- Variants `SWSNL1/2/3/4` for `IQUAD = 1/2/3/4`

Stencil and weighting (off-diagonal bins):
- Interaction stencil and AWG/SWG weights: `[file=src/swancom4.ftn line=1020-1037]`, `[file=src/swancom4.ftn line=1109-1127]`

### Variants and matrix split

| `IQUAD` | Method | Matrix split | file:line |
|---------|--------|-------------|-----------|
| 1 | Semi-implicit DIA | `IMATRA += SFNL/SIGPI`, `IMATDA -= DSNL/PI3` | `[file=src/swancom4.ftn line=1138-1139]` |
| 2 / 3 / 4 / 8 | Patankar split via `FILNL3` | positive to `IMATRA`, negative to `IMATDA` | `[file=src/swancom4.ftn line=2774-2779]`; same logic in `SWSNL2` `[file=src/swancom4.ftn line=1539-1544]` |

### Iteration / under-relaxation

- `IQUAD=3`: recompute `SWSNL3` first iter (or first sweep encounter), then `FILNL3` each sweep — `[file=src/swancom1.ftn line=7637-7664]`
- `IQUAD=4` MDIA (multiple DIA configurations): loop over `IDIA`, accumulate `MEMNL4` in `SWSNL4` (`IDIA==1` reset else add) — `[file=src/swancom4.ftn line=2328-2332]`, then `FILNL3` `[file=src/swancom1.ftn line=7692]`

## D. Triad (`Snl3`, LTA)

Single routine: `SWLTA` at `[file=src/swancom4.ftn line=3711]`, called from `[file=src/swancom1.ftn line=7556]`.

Biphase usage:
- `SINBPH = SIN(-BIPH)` `[file=src/swancom4.ftn line=3964]`
- Biphase `BIPH` computed in `SINTGRL` `[file=src/swancom1.ftn line=5916-5937]`

Source contributions: `SA, SA3` then composite `STRI` at `[file=src/swancom4.ftn line=4028-4089]`.

### Matrix split

Patankar rule: `STRI > 0 → IMATRA`, else `→ IMATDA` `[file=src/swancom4.ftn line=4095-4102]`.

## E. Bottom friction (`Sds,b`)

Single dispatch routine `SBOT` at `[file=src/swancom2.ftn line=27]`, called from `[file=src/swancom1.ftn line=7338]`.

Three formulations branched on `IBOT`:

| `IBOT` | Method | Coefficient | file:line |
|--------|--------|-------------|-----------|
| 1 | JONSWAP | `CFBOT = PBOT(3) / GRAV²` | `[file=src/swancom2.ftn line=327-334]` |
| 2 | Collins | `CFBOT = CFW * UBOT / GRAV` (CFW from `FRCOEF` if VARFR else `PBOT(2)`) | `[file=src/swancom2.ftn line=340-346]` |
| 3 | Madsen | Newton-solve for `FW`, `CFBOT = UBOT * FW / (sqrt(2) * GRAV)` (roughness `AKN` from `FRCOEF` if VARFR else `PBOT(5)`) | `[file=src/swancom2.ftn line=350-386]` |

**Variable bottom friction** read point: `FRCOEF(KCGRD(1))` at `[file=src/swancom2.ftn line=341]`, `[file=src/swancom2.ftn line=351]`, `[file=src/swancom2.ftn line=446]` — corresponds to the `FRICTION ... VAR` command syntax that uses an input grid.

### Per-bin dissipation
```
SBOTEO = CFBOT(IS) * (SPCSIG / SINH(KD))²
```
at `[file=src/swancom2.ftn line=520]`.

### Matrix accumulation
Implicit only on diagonal: `IMATDA += SBOTEO` `[file=src/swancom2.ftn line=538]`.

## F. Depth-induced breaking (`Sds,br`)

Battjes-Janssen breaker fraction routine `FRABRE` at `[file=src/swancom2.ftn line=1586]`, with `QBLOC` update at `[file=src/swancom2.ftn line=1763]`.

Surf-breaking source routine `SSURF` at `[file=src/swancom2.ftn line=1779]`, called from `[file=src/swancom1.ftn line=7401]`.

### α and γ application

- `α` (`PSURF(1)`) appears in `WS` formula: `[file=src/swancom2.ftn line=2113-2117]`
- `γ` enters via `HM = GAMBR * DEP2` (max wave height in shallow): `[file=src/swancom1.ftn line=5960]`, `[file=src/swancom1.ftn line=5982]`
- Default for `PSURF(2)` documented: `[file=src/swancom1.ftn line=7072]`

`QB` (fraction of waves currently breaking) computation path:
```
CALL FRABRE(HM, ETOT, QB(KCGRD(1)), KTETA)
```
at `[file=src/swancom1.ftn line=5999]`, then `QB_LOC = QB(KCGRD(1))` at `[file=src/swancom1.ftn line=6011]`.

### Matrix accumulation
Both implicit and explicit:
- `IMATDA += SURFA1`
- `IMATRA += SURFA0 * AC2`

at `[file=src/swancom2.ftn line=2188-2190]`.

## G. Source-term assembly summary

| Term | Implicit (`IMATDA`) | Explicit (`IMATRA`) | file:line |
|------|---------------------|---------------------|-----------|
| Wind GEN1/2 (`WNDPAR`) | `SWIND_IMP` | `SWIND_EXP` | `[file=src/swancom3.ftn line=512-513]` |
| Wind GEN3 (`SWIND0/3/4/5`) | — | `SWINEA / SWINEB * AC2` | `[file=src/swancom3.ftn line=1782, 2061, 2623, 2881]` |
| Wind ST6 (`DBYB`) | — | `memsins` (via `FILSIN`) | `[file=SdsBabanin.ftn90 line=1696]` |
| Whitecapping | `WCAP` | `WCIMPL * AC2` (IWCAP 4/5) | `[file=src/swancom2.ftn line=2645, 2661]` |
| Bottom friction | `SBOTEO` | — | `[file=src/swancom2.ftn line=538]` |
| Depth breaking (`SSURF`) | `SURFA1` | `SURFA0 * AC2` | `[file=src/swancom2.ftn line=2188-2190]` |
| Quadruplet semi-implicit | `-DSNL/PI3` | `SFNL/SIGPI` | `[file=src/swancom4.ftn line=1138-1139]` |
| Quadruplet Patankar | (negative parts) | (positive parts) | `[file=src/swancom4.ftn line=2774-2779]` |
| Triad LTA | (negative `STRI`) | (positive `STRI`) | `[file=src/swancom4.ftn line=4095-4102]` |
| Solver under-relaxation (global) | `+ ALFA*SPCSIG` | `+ ALFA*SPCSIG*AC2` | `[file=src/swancom1.ftn line=6185-6187]` |

## Decision Guide — debugging source-term issues

| Symptom | Likely culprit | Where to look |
|---------|---------------|---------------|
| Hs grows without bound under wind | wind input explicit + no implicit dissipation | confirm `WCAP` is on (`IMATDA += WCAP`); check `PWCAP` values |
| Energy peak too peaky | quadruplet under-resolved or wrong DIA variant | check `IQUAD`; for stiff cases use `IQUAD=2` Patankar |
| Surf-zone Hs collapses too early | breaking γ too low | inspect `PSURF(2)` and `GAMBR` value at points |
| Long swells over-dissipated | bottom friction too high | for swell, switch to `FRICTION COLL` not JONSWAP default |
| Convergence stalls in stationary | solver-level under-relaxation off | check `ALFA` factor at `swancom1.ftn:6185-6187` |
| Triad term wrong sign | biphase computation error | dump `SINBPH` in `SWLTA` and verify against `BIPH` from `SINTGRL` |

## Working Rules

1. The source-term order in `SWCOMP` is fixed: `SBOT → SSURF → SWIND0 → WNDPAR → SWCAP → quadruplets → triads`. Adding a custom term means inserting in this order.
2. The matrix split (implicit vs explicit) is a **stability vs accuracy** trade-off. Implicit on diagonal is rock-solid. Explicit on RHS allows positive feedback (wind input) but requires either limiter or implicit dissipation to balance.
3. Memo tables (`MEMSINB`, `MEMNL4`) are computed once per iteration and replayed per sweep — debugging output should snapshot these between iteration boundaries, not per sweep.
4. `IMATDA` should remain positive (stable). If it goes negative, look for: a missing implicit dissipation term, or a Patankar-rule violation in custom code.

## Common Pitfalls

- **GEN3 with all options off** — explicit-only wind input + no whitecapping → unbounded growth + limiter clamping forever. Always pair `GEN3` with `WCAP`.
- **`FRICTION ... VAR`** without proper `INPGRID FRCOEF` and `READINP FRCOEF` — `FRCOEF(KCGRD(1))` reads zero/garbage.
- **Quadruplet with `IQUAD=1` on a stiff spectrum** — semi-implicit DIA can oscillate. Switch to Patankar `IQUAD=2`.
- **Computing wave biphase outside `SINTGRL`** in custom modifications — the biphase pipeline shares state; bypassing it gives wrong triad sign.
- ▢ **User-experience cases** — placeholder for project-specific incidents.

## Next expansion

- ST6/Babanin internals (separate note: `SdsBabanin.ftn90` is a complete sub-module worth its own deep dive).
- Saturation-based dissipation (`SwellDissipation`, `Westhuysen`) detail.
- The `SINTGRL` dispatcher itself (it integrates over spectrum to produce ETOT, biphase, QB; central to many terms).

## References

### Source files (Codex deep scan, 2026-05-06)

- `src/swancom1.ftn` — `SWCOMP` outer loop, source-term dispatch, `SINTGRL` integrator.
- `src/swancom2.ftn` — `SBOT` (bottom friction), `SSURF` (breaking), `SWCAP/SWCAP8` (whitecapping), `FRABRE`.
- `src/swancom3.ftn` — wind input family (`WNDPAR`, `SWIND0/3/4/5`).
- `src/swancom4.ftn` — quadruplet (`SWSNL1/2/3/4`, `FAC4WW`, `FILNL3`) and triad (`SWLTA`).
- `src/SdsBabanin.ftn90` — ST6/Babanin wind input + whitecapping.
- Inventory: `[file=/mnt/e/models/swan/manuals/refs/subroutines.md]`.

### Manual cross-reference

- `[file=pdf:swan:swantech]` ch.2.3 (Sources and sinks), pages 21–52:
  - 2.3.1 Wind input formulations (Snyder/Komen, Janssen, Yan, ST6).
  - 2.3.2 Whitecapping (Hasselmann, Westhuysen, ST6).
  - 2.3.3 Bottom friction (JONSWAP, Madsen, Collins).
  - 2.3.4 Depth-induced breaking (Battjes-Janssen).
  - 2.3.5 Quadruplet (DIA).
  - 2.3.6 Triad (LTA).
- `[file=website:swan:node13]` — Activation of physical processes (per-process flag matrix).
- `[file=website:swan:node28]` — Physics overview command.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-06 |
| Codex source scan | 60+ file:line citations across 5 source files |
| Coverage | all source/sink terms — wind, whitecapping, quadruplet, triad, friction, breaking; matrix assembly per term |
| Out of scope (companion notes) | individual ST6/Babanin internals, `SINTGRL` integrator details, saturation-based dissipation specifics |
| Review status | `review_required: true` |
