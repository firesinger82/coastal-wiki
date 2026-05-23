---
title: "adcirc swan coupling"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-swan-coupling.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How the `padcswan` binary couples ADCIRC and SWAN over a shared unstructured mesh, the actual NWS encoding (`3xx` for `NRS=3`, **not literal `NWS=83/84`**), how time-stepping is coordinated by integer ratio `SWAN_DT/DT`, what fields are exchanged each direction, how the build system selects SWAN sources for the coupled binary, and the hot-start protocol for the combined run. Use this when wiring a coupled tide+wave simulation, debugging coupling interval mismatches, or interpreting `NRS=3` log entries.

## Source basis

- `couple2swan.F:67-1236` — main coupling module: init, run, finalize, RS computation.
- `driver.F:30-57` — `CSWAN` driver entry/finalize.
- `adcirc.F:428-483` — main loop coupling call.
- `read_input.F:1080-1083, 1790-1817, 2255-2261` — `NRS` parsing and encoding.
- `wind.F:52-60` — allowable NWS table.
- `timestep.F:664-682, 695-725, 1214-1218` — wind passing, RS interpolation, hotfile timing.
- `hstart.F:325-337`, `write_output.F:4969-5112`, `netcdfio.F90:5555-7045, 8017-8085` — hot-start.
- `../thirdparty/swan/SwanReadADCGrid.ftn90:44-153` — SWAN reads `fort.14`.
- `../thirdparty/swan/swanmain.ftn:895-902, 8696-8983` — SWAN-side coupling hooks.
- `../work/makefile:195-663` — build targets.

## A. Entry points

| Routine | Purpose | Lines |
|---|---|---|
| `PADCSWAN_INIT` | Initialize SWAN, exchange grids/initial state | `couple2swan.F:947` |
| `PADCSWAN_RUN(ITIME)` | Per-coupling-step SWAN run + RS update | `:1092` |
| `PADCSWAN_FINAL` | Cleanup | `:1236` |
| `ComputeRadiationStresses` | Integrate SWAN spectra to RS components | `:112` |
| `ComputeWaveDrivenForces` | Convert RS gradients to nodal forces | `:210` |

Driver glue (`driver.F:30-57`): imports `CSWAN` driver, calls `PADCSWAN_INIT` then `PADCSWAN_FINAL`.

Time-loop call (`adcirc.F:428-483`):
```
if (mod(ITIME, CouplingInterval) == 0) call PADCSWAN_RUN(ITIME)
```

SWAN-side hooks activated by `switch.pl -adcirc` — only present in coupled binary (`makefile:232-233, 558-560`).

## B. Time stepping

- ADCIRC runs every `DT`; SWAN `DT` imported as `SWAN_DT` (`couple2swan.F:950, 965`).
- **Coupling interval = integer ratio** `SWAN_DT / DT` (`:1079-1081`).
- ADCIRC calls SWAN only on that interval (`adcirc.F:475-483`).
- During SWAN run, interpolation midpoint used for time-centering (`couple2swan.F:1212-1215`).

**Note**: there is **no `CWTIM_INC` symbol** in this tree; coupling interval comes from SWAN `TIMECOMM:DT` block divided by ADCIRC `DT`.

## C. SWAN → ADCIRC (radiation stress)

1. SWAN spectra integrated into `ADCIRC_SXX/SXY/SYY` (`couple2swan.F:112-119, 177-196`).
2. Gradients converted to nodal wave forces in `SWAN_RSNX2/SWAN_RSNY2` (`:360-364, 399-404, 421-427`).
3. ADCIRC extrapolates/interpolates into `RSNX2/RSNY2` for `NRS=3` (`timestep.F:695-703`).
4. Added to wind stress in momentum (`timestep.F:721-725`).

## D. ADCIRC → SWAN (water level, currents, wind)

Allocated arrays (`couple2swan.F:67-75, 974-982`):
- `SWAN_ETA2` — water level.
- `SWAN_UU2`, `SWAN_VV2` — currents.
- `SWAN_WX2`, `SWAN_WY2` — winds (if `COUPWIND`).

Init copies ADCIRC `ETA2/UU2/VV2` plus winds (`:993-1009`).

Each coupling step:
- WL/currents updated from ADCIRC (`:1128-1142`).
- Dry nodes set depth zero / current zero.
- Wind passed from ADCIRC met → SWAN if `COUPWIND` (`timestep.F:664-682`).

SWAN-side memory grab post-preprocess (`../thirdparty/swan/swanmain.ftn:8696-8983`).

## E. Mesh sharing

SWAN unstructured ADCIRC reader explicitly opens `fort.14` (`SwanReadADCGrid.ftn90:44-103`):
- Reads `ncells, nverts`, node coords + depth, triangles (`:114-153`).

Coupler uses SWAN `nverts/xcugrd/ycugrd` for output/exchange (`couple2swan.F:596-598, 800-835`).

So **same `fort.14` is used by both ADCIRC and SWAN** — single mesh, no interpolation needed.

## F. NWS encoding (NWS=3xx, not 83/84)

**Important**: `wind.F:52-60` allowable base `NWS` list **excludes 83/84**.

Instead, `read_input.F:1790-1817` parses radiation-stress coupling from **hundreds digit**:
```
NRS = ABS(NWS / 100)        ! strip hundreds
NWS = NWS − 100*sign*NRS    ! remaining is base met forcing
```

`NRS=3` is documented as "WAVES WILL BE COUPLED TO SWAN" (`:2255-2261`).

So:

| Input NWS | NRS | Effective base NWS | Meaning |
|---|---:|---:|---|
| `308` | `3` | `8` | OWI hindcast met + SWAN waves |
| `312` | `3` | `12` | OWI WIN/PRE + SWAN |
| `320` | `3` | `20` | GAHM vortex + SWAN |
| `300` | `3` | `0` | No met, only SWAN waves |
| `8` | `0` | `8` | OWI met only, no waves |

Literal `NWS=83/84` is **invalid** in this code path.

## G. Build / link

`makefile` distinguishes:

| Target | Flags | SWAN |
|---|---|---|
| `padcirc` (parallel ADCIRC) | `FFLAGS3 $(DP)`, no SWAN VPATH | Not built |
| `padcswan` (coupled) | parallel + `-DCSWAN`, SWAN VPATH, SWAN switch `-pun -adcirc` | Built and linked |

References: `makefile:195-233, 480-509, 634-635, 661-663`.

So **always use `padcswan` for coupled runs**; `padcirc` even with `NRS=3` won't have SWAN linked.

## H. Hot-start

ADCIRC hot-start reads base `RSNX/RSNY`; for `NRS=3` also reads `SWAN_RSNX/RSNY` history (`hstart.F:325-337`).

Binary hot-start writes:
- Base RS arrays.
- If `NRS=3`: SWAN RS arrays (`write_output.F:4969-5112`).

NetCDF hot-start defines `swan_rsx1/rsy1/rsx2/rsy2` (`netcdfio.F90:5555-5568`); writes for `nrs==3` (`:6966-7045`).

SWAN spectral hot-start is **separate**:
- ADCIRC sets `SwanHotStartUnit` (`read_input.F:1080-1083`).
- `timestep.F:1214-1218` defers SWAN hotfile write until after next SWAN step.
- SWAN calls `BACKUP` then clears flag (`swanmain.ftn:895-902`).

**Possible issue noted in code**: NetCDF read path inquires SWAN variable IDs but reads `hs%rs1/rs2` IDs into `swan_*` arrays — not `hs%swan_rs*` (`netcdfio.F90:8017-8085`). This may indicate a latent bug in NetCDF restart of SWAN-coupled runs; verify before relying on it.

## Decision Guide

| Goal | Setup |
|---|---|
| Tide + wave coupling, OWI met | Compile `padcswan`; set `NWS=312` (or `308` for OWI ASCII met) |
| GAHM hurricane + waves | `NWS=320` (NRS=3, base=20 GAHM) |
| Wave-only test (no met) | `NWS=300` |
| Coupling interval (5 min, ADCIRC dt=2s) | `SWAN_DT=300` in SWAN input → ratio 150 |
| Tight coupling (every ADCIRC step) | `SWAN_DT = DT` — expensive, rarely needed |
| Hot-start coupled run | `IHOT=67/68` for ADCIRC; SWAN auto via `SwanHotStartUnit` |
| Restart NetCDF coupled | Verify `swan_rs*` arrays write/read correctly; possible latent bug |

## Working Rules

- Use `padcswan` binary; verify with `padcswan --help` or check link map for `swan` symbols.
- `SWAN_DT` typically 60-1800 s; ADCIRC `DT` 0.5-5 s. Ratio 100-300 is normal.
- Set ADCIRC `OutputControl` and SWAN `BLOCK` outputs at compatible intervals for diagnostic plots.
- In log, look for "WAVES WILL BE COUPLED TO SWAN" confirming `NRS=3` parsed.
- `COUPWIND` flag in `couple2swan.F`: if true, ADCIRC met goes to SWAN; if false, SWAN reads its own wind file (rarely used).
- For ADCIRC v55+, NetCDF hot-start is preferred; for older versions, fort.67/68 binary is more stable.
- SWAN spectral hot-start (`HOTSTART` in SWAN input) is separate from ADCIRC hot-start; both must align on time.

## Common Pitfalls

- ▢ Setting `NWS=83` literally — invalid; use `NWS=308` etc.
- ▢ Using `padcirc` with `NWS=308` — base met works but no SWAN linked; runs without waves silently.
- ▢ `SWAN_DT` not divisible by `DT` — coupling interval rounds; output frequency anomalies.
- ▢ Hot-start ADCIRC at time T but SWAN cold-start — wave field absent for first SWAN step; spurious zero RS.
- ▢ Hot-start SWAN before ADCIRC catches up — cyclic dependency; ensure both at same `TIMELOC`.
- ▢ Met forcing time alignment — `STATIM/REFTIM` apply to ADCIRC; SWAN reads `INPGRID` time block independently. Match epochs.
- ▢ NetCDF restart with `NRS=3` — possible bug at `netcdfio.F90:8017-8085` (`hs%rs1/rs2` vs `hs%swan_rs*`); test on small case before production.

## Next expansion

- Build recipe for `padcswan` on Linux/Intel.
- COUPWIND vs separate SWAN met forcing recipe.
- NetCDF hot-start verification test.
- Comparison vs older NWS=83 (legacy) coupling.

## References

- Dietrich et al. 2011 (ADCIRC+SWAN unstructured coupling).
- Booij et al. 1999 (SWAN baseline).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
