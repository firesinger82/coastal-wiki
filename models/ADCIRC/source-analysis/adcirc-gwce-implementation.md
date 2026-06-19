---
title: "adcirc gwce implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-gwce-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC GWCE solver — matrix assembly, time integration, JCG solve

## Scope

The Generalized Wave Continuity Equation is ADCIRC's mass-conservation equation for water surface elevation. This note documents matrix assembly, lumped vs consistent mass, time integration scheme, JCG solver dispatch, boundary contributions, and SAL (self-attraction & loading) integration.

## A. Matrix assembly

- Primary routine: `GWCE_New` at `[file=src/gwce.F line=237]`. Rebuild gated by `NCIFBLCK` at `[file=src/gwce.F line=427]` (`IF(NCChange.GT.0 .or. CGWCE_HDP)`).
- Lumping weights at `[file=src/gwce.F line=418-420]`:
  - `OnDiag = (1+ILump)*2`, `OffDiag = (1-ILump)`
  - `ILump=0` → consistent mass; `ILump=1` → diagonal-only (lumped)
- Mass + tau0 factors at `[file=src/gwce.F line=538-540]`: `MsFacLOnDiag`, `MsFacLOffDiag`
- Flux-gradient stiffness: `GA00DPAvgOAreaIE4*FDX/FDY` products into `Coef` at `[file=src/gwce.F line=564-592]`
- Friction/`Tau0Var` enters via `Tau0Avg[_S]` in mass-like factors at `[file=src/gwce.F line=517, 538-539, 607, 623]` — affects both consistent and lumped paths
- LHS assembly at `[file=src/gwce.F line=429-636]` (`Coef`/`Coefd`)
- RHS forcing assembly at `[file=src/gwce.F line=998-1617]`
- Boundary elimination modifies LHS at `[file=src/gwce.F line=638-673]`; RHS compensation via `OBCCoef` at `[file=src/gwce.F line=1846-1854]`
- `ILump` switch points: `[file=src/gwce.F line=141, 430, 455, 595, 709, 1846, 1856]`
- Memory allocation: `alloc_main11` (consistent) vs `alloc_main11_lumped` at `[file=src/gwce.F line=141-154]`

## B. Time integration

- `DT` enters matrix terms directly at `[file=src/gwce.F line=538-539, 623, 1429, 1741, 1758]`
- `DTDP` is for model clocking only at `[file=src/adcirc.F line=348]` and hotstart timing at `[file=src/hstart.F line=719-720]` — **not** in GWCE matrix
- Three-time-level state in `GWCE_New_pc`: `ETA0, ETA1, ETA2` at `[file=src/gwce.F line=2514-2522]`
- Time weighting: `C00` (n-1) + `(A00+B00)` (n) for free-surface RHS at `[file=src/gwce.F line=1540-1543]`; corrector at `[file=src/gwce.F line=2851-2852]`
- State shift each step: `Eta1=Eta2`, optionally `Eta0=Eta1` at `[file=src/gwce.F line=1622-1631]`
- ETA2 update at `[file=src/gwce.F line=2007]` or `[file=src/gwce.F line=2020]`

**No semi-implicit `Theta` parameter.** The only `FTHETA` is a friction-law exponent (corrector) at `[file=src/gwce.F line=2477-2482]`, not time-weighting.

## C. Solver

- Consistent mass (`ILump=0`): `JCG` at `[file=src/gwce.F line=2001-2004]`
- Lumped mass: bypass Krylov, explicit diagonal inversion at `[file=src/gwce.F line=2010-2017]`
- `ITMAX` cap: `IPARM(1)=ITMAX` at `[file=src/gwce.F line=146]`, `[file=src/gwce.F line=2002]`
- Convergence tolerance: `RPARM(1)=CONVCR` at `[file=src/gwce.F line=150]`
- Iteration count returned in `IPARM(1)` → captured as `NUMITR` at `[file=src/gwce.F line=2005]`

## D. Boundary contributions

- Open-boundary harmonic synthesis: `ETA2(NBDI) += EMO*FF*RampElev*cos(AMIG*timeh + FACE - EFA)` at `[file=src/gwce.F line=1638-1650]`, driven by `NBFR`
- Aperiodic `fort.19` interpolation at `[file=src/gwce.F line=1659-1673]` using `ESBIN1/ESBIN2`
- Boundary topology (`NOPE, NETA, NBD, NBV, LBCODEI`) consumed via `USE BOUNDARIES` at `[file=src/gwce.F line=270-271]`, `[file=src/cstart.F line=64]`, `[file=src/hstart.F line=58]`
- Normal-flow / radiation / gradient boundary fluxes contribute to RHS at `[file=src/gwce.F line=1725-1834]`, per-`LBCODEI` formulas, `Tau0Var` coupling at `[file=src/gwce.F line=1740-1764, 1782-1805]`
- Elevation-specified boundaries: row/column modification on LHS at `[file=src/gwce.F line=652-673]`; scaled RHS enforcement at `[file=src/gwce.F line=1840-1861]`
- No-flux land suppression via `NODECODE` masking at `[file=src/gwce.F line=474-477, 1010-1015]`; dry/landlocked nodes init in cold start at `[file=src/cstart.F line=1221-1223, 1258-1260]`

## E. SAL integration (NTIP=2 path)

- Reader: `readSelfAttractionAndLoadingFile` at `[file=src/adcirc.F line=292-293]` — comment notes `fort.24`
- SAL added to tidal potential in hot start: `+ SALTMUL * SALTAMP(J,I) * COS(ARGSALT)` at `[file=src/hstart.F line=1522, 1530-1532]`
- GWCE consumes via `TiP1`/`TiPN*` at `[file=src/gwce.F line=1181-1184]`, used in forcing gradients at `[file=src/gwce.F line=1450-1452, 1462-1464]`
- So SAL-modified tidal potential propagates into GWCE RHS

## F. Wetting-drying mask

- Element wet/dry mask: `NCELE = NC1*NC2*NC3*NOFF(IE)` at `[file=src/gwce.F line=477, 605, 1015, 1074]`
- Any dry node (`NODECODE=0`) nulls that element's contribution
- Subgrid wetting/drying: `wetFracVertETA1/2` modifies LHS at `[file=src/gwce.F line=465-473, 541-547]` and RHS at `[file=src/gwce.F line=1055-1063, 1436-1439]`
- Initial dry-node logic in cold start: `[file=src/cstart.F line=1221-1231, 1258-1268]`
- No separate dry-node check inside GWCE — purely multiplicative masking via `NODECODE`

## Decision Guide — 진단 (트러블슈팅)

| Symptom | Likely cause | Source-level investigation |
|---------|--------------|----------------------------|
| Tidal amplitude wrong (지역 bias) | flux-gradient term + tau0 + bottom-friction interaction | Check `Tau0Var` + `FRIC` flow into `Coef` (`gwce.F:538-592`) |
| Iteration count high | poor preconditioning or stiff diagonals | `NUMITR` in stdout; tighten `CONVCR` |
| Boundary spike | tide block format wrong in fort.15 | `NBFR` block mismatch (`gwce.F:1638-1650`) |
| Mass loss at wet/dry front | `NCELE` masking issue | `gwce.F:477` dry-element zeroing |

## Working Rules

1. **`DT` not `DTDP` is the GWCE time step inside the matrix.** They're equal in standard runs but check `read_input.F` if customizing.
2. **`ILump=1` (lumped) skips JCG entirely** — much faster but less accurate. Default for ADCIRC v55+ is `ILump=0`.
3. **`Tau0Var` enters mass factors, not friction directly.** It weights the GWCE matrix; friction is separate via `FRIC` from Manning conversion.
4. **SAL = `fort.24` ASCII or NetCDF** with one block per tide constituent. NTIP=2 must be set.
5. **NUMITR > 50 iteration suggests stiff matrix** — increase `ITMAX`, tighten mesh, or check very-shallow elements.

## Common Pitfalls

- **TAU0=-5 with no `Tau0FullDomainMin/Max` line** — defaults take over; result depends on sandbox state.
- **Boundary ELEVALPHA wrong** — phases shifted across NBFR block; check `read_input.F:3431-3456` parse order.
- **Hot-restart with different `ILump`** — matrix shape differs; restart fails or silently runs lumped.
- **NTIP=2 without fort.24** — runtime error or zero SAL contribution.

## References

- `src/gwce.F` — main solver.
- `src/momentum.F` — companion momentum equations.
- `src/cstart.F` / `src/hstart.F` — cold/hot start paths.
- `src/adcirc.F` — high-level driver, NTIP/SAL init.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 30+ file:line citations |
| Coverage | matrix assembly, time integration, JCG, boundary, SAL, wet/dry mask |
| Review status | `review_required: true` |
