---
slug: roms_4dvar
title: ROMS 4D-Var (I4DVAR / RBL4DVAR / R4DVAR weak-constraint, TLM, ADJ)
model: roms
auto_draft: false
authored_by: claude
review_required: true
generated: 2026-05-03
basis: codex source-code analysis of /mnt/e/models/roms/source_code/roms
---

## Scope

How ROMS dispatches the three 4D-Var families (incremental I4DVAR, restricted-B-preconditioned-Lanczos RBL4DVAR, weak-constraint R4DVAR), where the cost function is built and minimized, how TLM/ADJ kernels integrate forward/backward, and how trajectories are stored. Use this when running data assimilation cycles, debugging cost-function divergence, or scaling I/O for long DA windows.

## Source basis

- `ROMS/Drivers/i4dvar_roms.h`, `i4dvar.F` — I4DVAR (strong constraint, incremental).
- `ROMS/Drivers/rbl4dvar_roms.h`, `rbl4dvar.F` — RBL4DVAR (restricted B, Lanczos).
- `ROMS/Drivers/r4dvar_roms.h`, `r4dvar.F`, `tl_r4dvar_roms.h` — R4DVAR / weak-constraint.
- `ROMS/Adjoint/ad_misfit.F`, `ad_main3d.F` — observation misfit, adjoint kernel.
- `ROMS/Tangent/tl_main3d.F` — TLM kernel.
- `ROMS/External/wc13.h`, `roms_wc13.in` — WC13 example configuration.

## A. Driver families

| Family | Driver entry | Outer-loop dispatch | Description |
|---|---|---|---|
| I4DVAR | `i4dvar_roms.h:245` (`ROMS_run`) | `:292` calls `background/increment/analysis` | Strong-constraint incremental |
| RBL4DVAR | `rbl4dvar_roms.h:248` | `:308` | Restricted-B preconditioned Lanczos |
| R4DVAR (incl. weak) | `r4dvar_roms.h:248` | `:307` | Representer / weak-constraint variant |
| W4DVAR | (no standalone file) | `tl_r4dvar_roms.h:352` (`driver='tl_w4dvar'`) | Weak-constraint via R4DVAR family |

Core routines:
- I4DVAR: `i4dvar.F:551, 781, 1716`.
- RBL4DVAR: `rbl4dvar.F:400, 645, 2558`.
- R4DVAR: `r4dvar.F:1988` (driver tag).

## B. Inner loop (cost minimization)

The incremental cost is `J = Jb + Jo`:

- `i4dvar.F:1518-1544` — reports normalized `Jb` and `Jo`.
- `i4dvar.F:1464-1482` — background term `back_cost`.
- `ad_misfit.F:194-196` — observation misfit forcing built from `(NLmodVal + TLmodVal - ObsVal)`.

### B-preconditioning

Model-space ↔ minimization-space transforms:
- `i4dvar.F:1412-1433` — `GRADx(Jo)` to `GRADv` via `ad_variability` then `ad_convolution`.
- `i4dvar.F:1619-1637` — `deltaV` to `deltaX` via `tl_convolution` then `tl_variability` (and `tl_balance` if active).

### R / Cobs (observation error)

- Solver equation comments: `ad_congrad.F:62-92`, `ad_rpcg_lanczos.F:68-113`.
- Actual ObsErr weighting in `ad_misfit.F:194-196`.

### CG / Lanczos solvers

- I4DVAR ⇒ `cgradient` (`i4dvar.F:1513`).
- RBL4DVAR ⇒ `rpcg_lanczos` (`rbl4dvar.F:1343`) or `congrad` (`:1353, 1584`).

## C. Outer loop

| Driver | Loop entry |
|---|---|
| I4DVAR | `i4dvar_roms.h:292` |
| RBL4DVAR | `rbl4dvar_roms.h:308` |
| R4DVAR | `r4dvar_roms.h:307` |

TLM integration in loop:
- I4DVAR: `i4dvar.F:1291-1295` calls `tl_main3d/tl_main2d`.
- RBL4DVAR: `rbl4dvar.F:1535-1539`.

ADJ integration in loop:
- I4DVAR: `i4dvar.F:1353-1357` calls `ad_main3d/ad_main2d`.
- RBL4DVAR: `rbl4dvar.F:1408-1412`.

Time-window length: each phase takes `RunInterval` (`i4dvar.F:791-792`, `rbl4dvar.F:655-656`); TL/AD kernels convert via `ntimesteps` (`tl_main3d.F:179`, `ad_main3d.F:258`).

## D. Observation operator / innovations / residuals

- Observation file: `OBSname == roms_obs.nc` in `s4dvar.in:461`.
- Split-driver scripts rewrite to `..._obs_...nc`: `submit_split_i4dvar.sh:431` (and r4dvar/rbl4dvar analogs).
- Innovation calculation: `(NLmodVal + TLmodVal - ObsVal)` in `ad_misfit.F:194-196`.
- Split drivers load `ObsVal/ObsErr` from `OBS(ng)%name`: `rbl4dvar.F:847-861`, `r4dvar.F:617-631`.
- `wrtMisfit` switch for residual output: `i4dvar.F:406-413`, `rbl4dvar.F:1515-1522`.
- Diagnostics/misfit cost written to DAV: `i4dvar.F:723-735`, final at `:2404-2417`; rbl at `:2773-2780`.

## E. Tangent linear model (TLM)

- Main TLM kernel: `tl_main3d.F:3` (`SUBROUTINE tl_main3d`).
- Forward stepping at `:185`; data ingestion `tl_get_data` at `:210`.
- BASIC STATE fields (`set_depth/set_massflux`) processed at `:229-247`.
- Drivers wire nonlinear history as basis trajectory (`i4dvar.F:1026-1043`).

The TLM is **linearized about the nonlinear trajectory** — that's why the basis trajectory must be stored from the prior nonlinear forward run.

## F. Adjoint model

- Main AD kernel: `ad_main3d.F:3`.
- Reverse-time integration explicit: `STEP_LOOP : DO istep=Nsteps,1,-1` at `:266` (comments `:191-199`).
- Sensitivity forcing from observations at `:697` (`obs_read`) then `:711-714`:
  - `ad_htobs` → weak-constraint.
  - `ad_misfit` → strong-constraint.

## G. Trajectory storage (memory vs disk)

- Disk trajectory files per outer loop: HIS at `i4dvar.F:1030-1043`, QCK at `:1051-1063`, adjoint history at `:1192-1200`.
- Memory vs split-file behavior: split mode repeatedly reads DAV/ITL/TLM/ADM NetCDF because values "are in memory in the unsplit algorithm" (`i4dvar.F:862-867, 993-996`; `rbl4dvar.F:790-793, 805-809`).
- I/O-size/performance tradeoff: explicit multi-file rationale "split ... to reduce size" at `i4dvar.F:1137-1138`; delayed sync/close for performance at `r4dvar.F:367-373`.

## H. Practical examples (WC13)

- WC13 compile/test config: `wc13.h` (case CPP options), `roms_wc13.in:1223` (`APARNAM = i4dvar.in`).
- Batch workflows: `submit_split_i4dvar.sh`, `submit_split_r4dvar.sh`, `submit_split_rbl4dvar.sh`. Standard/norm files and obs substitution at `submit_split_i4dvar.sh:120-131, 151, 431`.
- The `roms_test` exercise PDFs are not in this tree; only URL/comment reference at `submit_mixres_rbl4dvar.sh:60`.

## Decision Guide

| Use case | Choice |
|---|---|
| Sparse data, short window, smooth IC update only | I4DVAR (strong constraint) |
| Strong constraint with better preconditioning, tougher convergence | RBL4DVAR |
| Long window, model-error matters, can afford I/O | R4DVAR weak-constraint (W4DVAR tag) |
| Quick smoke test | WC13 example (`roms_wc13.in`) |
| Scaling DA across cluster | Split-file mode (reads from disk between phases) |
| Single-machine debug | Unsplit mode (in-memory) |
| Verify innovation processing | Set `wrtMisfit=T`, inspect DAV file |
| Observation outliers | Inflate `ObsErr` per-type in `obs.nc` |
| Background covariance localization | Tune `Hdecay/Vdecay` correlation lengths in `s4dvar.in` |

## Working Rules

- Run a strong-constraint I4DVAR first, even if your target is weak-constraint — it builds the basic-state trajectory and shakes out observation file mistakes cheaply.
- Outer loops typically 1–3; inner loops 10–50 (CG iterations). Cost grows linearly with outer × inner.
- Always check the cost-function reduction across outer loops. `J_final / J_initial < 0.5` is normal; > 0.95 means the system is not converging (bad B, bad obs, or trivial increment).
- Run the TLM-AD pair with the inner-product test at least once after any source change. Asymmetry > 1e-10 in double precision is a bug.
- Background covariance correlation lengths: scale-of-eddies in horizontal (10–50 km coastal, 100–300 km open ocean), 50–200 m vertical. Too short ⇒ noisy increments; too long ⇒ smeared.
- For weak-constraint, check that model-error covariance `Q` is non-trivial. Default `Q=B` reduces to strong-constraint in disguise.

## Common Pitfalls

- ▢ Forgetting to update the basic-state trajectory between cycles — TLM linearizes about a stale state and innovations diverge.
- ▢ ObsErr too small (e.g., reporting RMS instead of representativeness error) — inner loop tries to overfit and explodes.
- ▢ Localization not used in B — increments leak across basin, decorrelating obs influence.
- ▢ Mixing I4DVAR with R4DVAR namelist parameters — drivers share `s4dvar.in` partly but not all keys.
- ▢ Running unsplit mode at scale — memory footprint blows up because basic-state and adjoint trajectories live in RAM.
- ▢ Verifying innovation only at the end of the run — turn on `wrtMisfit` always; cheap and diagnostic.
- ▢ Assuming a `w4dvar.F` exists — the weak-constraint path lives inside the R4DVAR family with the `tl_w4dvar` driver tag.

## Next expansion

- TLM-AD inner-product test recipe (line-by-line).
- WC13 walkthrough with concrete cost-function trajectory plots.
- Localization tooling for B (`s4dvar.in` correlation parameters).
- Hybrid 4D-EnVar discussion if/when ROMS picks up that path.

## References

- Moore et al. 2011 (ROMS 4D-Var trio: I4DVAR, R4DVAR, RBL4DVAR).
- Courtier et al. 1994 (incremental 4D-Var).
- Bennett 2002 (representer method, weak constraint).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
