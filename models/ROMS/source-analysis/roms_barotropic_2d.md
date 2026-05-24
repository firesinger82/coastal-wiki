---
title: "roms barotropic 2d"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_barotropic_2d.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How ROMS splits the fast barotropic (depth-integrated 2D) mode from the slow baroclinic (3D) mode, how `NDTFAST` and the time-averaging weights are set, how the LF-AM3 / FB-LF-AM3 / FB-AB3-AM4 schemes work, and how 2D state is fed back to 3D for transport consistency. Use this when tuning `NDTFAST`, diagnosing barotropic instability, or wiring nesting transports.

## Source basis

- `ROMS/Nonlinear/main3d.F:665-819,950-957` — outer 3D step, fast-loop entry, scheme dispatch, nest exchange of `Zt_avg`/`DU_avg1`/`DV_avg1`.
- `ROMS/Nonlinear/step2d_LF_AM3.h` — actual 2D kernel: continuity (924-1042), momentum (1128-2693), Coriolis/stress, BCs.
- `ROMS/Utility/set_weights.F:12-182` — primary/secondary weight design, `nfast` derivation.
- `ROMS/Utility/read_phypar.F:608` and `inp_par.F:640` — `NDTFAST → dtfast = dt/NDTFAST`.
- `ROMS/Nonlinear/step3d_uv.F:1306-1526` — 3D→2D coupling and mass-flux correction.
- `ROMS/Utility/checkdefs.F:3596` — 2D-only check (`!SOLVE3D ⇒ NDTFAST=1`).

## A. Mode-splitting structure

- Outer 3D step enters `LOOP_2D`; `step2d` is called tile-by-tile for each fast substep `my_iif=1..nfast+1`, with predictor/corrector controlled by `PREDICTOR_2D_STEP`, `kstp`, `knew`, `krhs` (`main3d.F:675,687,819`).
- `NDTFAST` is the user input; `dtfast(ng)=dt(ng)/ndtfast(ng)` (`read_phypar.F:608`, `inp_par.F:640`).
- `nfast(ng)` is **not** equal to `NDTFAST` — it is derived from the nonzero support of the primary weight `weight(1,*,ng)` (`set_weights.F:47-175`). The filter typically extends past `NDTFAST` to give phase-accurate averaging.
- Scheme selection is **compile-time**: legacy LF-AM3, FB LF-AM3, or FB AB3-AM4 (`main3d.F:665,716,810`).
- Fast-time accumulators `Zt_avg1`, `DU_avg1/2`, `DV_avg1/2` are built across substeps and finalized at `iif=nfast+1` before exchange/sync (`step2d_LF_AM3.h:777-859`).

## B. Continuity equation

- Depth-integrated continuity uses divergence of transport: `rhs_zeta=(DUon(i,j)-DUon(i+1,j))+(DVom(i,j)-DVom(i,j+1))` (`step2d_LF_AM3.h:924-941`).
- Time-stepping by stage:
  - First step: forward Euler / backward Euler.
  - Predictor: leapfrog (`2*dtfast`).
  - Corrector: AM3 weights `5/12, 8/12, -1/12` applied via stored `rzeta` history (`step2d_LF_AM3.h:943-998`).
- `zeta(i,j,knew)=zeta_new` is loaded every substep; predictor stores `rzeta(:,:,krhs)` for the next corrector (`:1029-1042`).

## C. Momentum equations

- `rhs_ubar / rhs_vbar` start from barotropic pressure-gradient forcing including baroclinic correction when 3D is active (`:1128-1186`).
- Coriolis is in flux form: `0.5 * Drhs * fomn` with `fomn=f/(pm*pn)` (`:1464-1472`).
- Bottom stress (`bustr/bvstr`) subtracts; surface wind stress (`sustr/svstr`) adds; both metric-scaled by `om_* * on_*` (`:2174-2529`).
- `ubar/vbar` time stepping mirrors `zeta`: FE/BE first → LF predictor → AM3 corrector with `5/12, 8/12, -1/12` (`:2577-2693`).

## D. Coupling back to baroclinic

Two-step consistency restoration after the fast loop:

1. Replace barotropic mode of new 3D velocity with fast-time averages (`step3d_uv.F:1306-1352`):
   - Compute the (incorrect) vertical mean from the new `u(:,:,:,nnew)`.
   - Subtract that mean and add `DU_avg1`/`DV_avg1` (the filtered 2D transport).
2. Adjust mass fluxes (`step3d_uv.F:1507-1526`):
   - Correct `Huon`, `Hvom` so that the depth-integrated 3D transport equals `DU_avg2`, `DV_avg2`.
   - This is what guarantees tracer-equation mass conservation; without it, advected tracers drift.

In nesting, the time-averaged `DU_avg1`, `DV_avg1`, `Zt_avg` are exchanged via `n2dfx` (`main3d.F:950-957`).

## E. NDTFAST vs time-averaging vs stability

- The filter (`set_weights.F:12-182`) enforces:
  - Zeroth moment normalization: `Σ weight(1,*) = 1`.
  - Center-of-gravity at `NDTFAST` (so the average is centered on the slow time level, not biased forward).
  - Secondary weights for the staggered combinations `(-1/12, 8/12-1/12, 5/12)` used by LF-AM3 (`:785-836`).
- This is the anti-aliasing bridge: too small `NDTFAST` ⇒ filter cannot kill aliased high-frequency 2D modes ⇒ noisy `zeta`.
- Hard rule: 2D-only runs (`!SOLVE3D`) must use `NDTFAST=1` (`checkdefs.F:3596`). Split stepping is only valid with a 3D mode to filter into.

## F. Open boundary in 2D

- BC application points are explicit in the 2D kernel: `zetabc_tile`, `u2dbc_tile`, `v2dbc_tile` (`step2d_LF_AM3.h:1095,2936`).
- Free-surface options: `Chapman_explicit`, `Chapman_implicit` (`zetabc.F:186-209`).
- Velocity options: `Flather` (`u2dbc_im.F:224`, `v2dbc_im.F:230`) and reduced-physics (`u2dbc_im.F:400`, `v2dbc_im.F:432`).
- Volume-conservation OBC adjustment is applied via `set_DUV_bc_tile` (pre-step transport consistency) and `obc_flux_tile` (post-BC integral flux correction) (`:759, 2947`).

## Decision Guide

| Question | Answer |
|---|---|
| 2D-only run? | `NDTFAST=1` (forced) |
| 3D coastal, dt~600s | `NDTFAST=20–60`; aim for ~`dt/NDTFAST ≤ 0.5*Δx/√(g·Hmax)` then halve |
| Seeing barotropic noise / ringing? | Increase `NDTFAST` first; only switch scheme if noise persists with `NDTFAST=60+` |
| Tracer conservation drift? | Verify `Huon/Hvom` correction is happening (debug `step3d_uv.F:1507-1526`); not an `NDTFAST` issue |
| Nesting transport mismatch? | Confirm `DU_avg1/DV_avg1/Zt_avg` are exchanged at `n2dfx` step |
| `Flather` vs `Chapman`? | `Flather` for tide-radiating boundaries; `Chapman_implicit` for free-surface elevation in stratified domains |

## Working Rules

- Set `NDTFAST` so `dtfast` resolves the fastest gravity wave by 4–8 substeps, then add margin: `NDTFAST = ceil(dt * sqrt(g*Hmax) / (0.4 * dx_min))`.
- Do **not** assume `nfast == NDTFAST`. Trust the filter; the actual averaging window from `set_weights.F` may be 1.5–2× `NDTFAST`.
- Watch `Zt_avg1` and `DU_avg1` diagnostics in tile output: if they drift relative to `zeta`/`ubar` snapshots, the 2D filter is under-resolved.
- For nesting, parent and child must use compatible `NDTFAST` so exchanged averages line up in time. Telescoping nests need `RefineSteps` to align with `nfast`.

## Common Pitfalls

- ▢ Setting `NDTFAST=1` "to speed things up" — corrupts the filter; kills mass conservation.
- ▢ Choosing `Flather` on a closed coast — radiation-condition assumes an open boundary; results in artificial drainage.
- ▢ Long runs with steady winds and low `NDTFAST` show slow barotropic drift; symptom is `zeta` mean creeping. Cure is filter, not boundary.
- ▢ Tracer mass loss after restart suggests the mass-flux correction is being short-circuited (e.g., turning off `MASKING` or modifying `Huon` outside `step3d_uv.F`).

## Next expansion

- Cross-link to vertical coordinate note (`Hz, z_w, z_r` use the new `zeta`).
- Quantitative comparison of LF-AM3 vs FB-AB3-AM4 stability margins (requires literature mining beyond source).

## References

- Shchepetkin & McWilliams 2005 (split-explicit ROMS architecture).
- Shchepetkin & McWilliams 2009 (FB-AB3-AM4 derivation).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
