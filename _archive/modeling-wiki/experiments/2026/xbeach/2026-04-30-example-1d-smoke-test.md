# Experiment Card

## Metadata

- date: 2026-04-30
- title: XBeach example_1d smoke test after SVN update and rebuild
- status: successful
- domain: coastal morphodynamics
- model / solver: XBeach v1.24-range style local build (`xbeach_IFX.exe`)
- owner: Hermes + user workspace

## Objective

Verify that the freshly rebuilt XBeach executable from the updated SVN source can run a known local example case from the operating `bin/` path without immediate runtime failure.

## Setup

- geometry / domain: local bundled 1D example profile
- mesh / grid: `models/example_1d/x.grd`, `y.grd`, `bed.dep`
- boundary conditions: `wbctype = parametric`, `bcfile = jonswap.txt`
- initial conditions: `tideloc = 0`, `zs0 = 0`
- forcing: parametric wave forcing from `jonswap.txt`
- parameter values:
  - `wavemodel = surfbeat`
  - `sedtrans = 1`
  - `morphology = 1`
  - `bedfriction = manning` (default shown in runtime log)
  - `form = vanthiel_vanrijn` (default shown in runtime log)
- timestep / CFL:
  - `tstop = 600`
  - `CFL = 0.7`
- numerics: `MPI_netcdf_Release|x64` Windows build promoted into operating bin
- hardware / runtime constraints: executed through Windows `run_xbeach.bat` from WSL

## Inputs

- input datasets:
  - `models/example_1d/bed.dep`
  - `models/example_1d/x.grd`
  - `models/example_1d/y.grd`
  - `models/example_1d/jonswap.txt`
- source files:
  - `bin/xbeach_IFX.exe`
  - `bin/run_xbeach.bat`
- config files:
  - `models/example_1d/params.txt`
- related raw sources:
  - local XBeach manuals and source tree under `/mnt/e/numerical_models/xbeach`

## Expected Behavior

The promoted executable should launch, parse `params.txt`, initialize the spectral wave boundary, finish the short test run, and exit with code 0.

## Observed Behavior

- model launched successfully through `run_xbeach.bat`
- runtime banner displayed correctly
- parameters were parsed from `params.txt`
- boundary-condition setup and spectral wave boundary generation completed
- simulation completed and ended with exit code 0

## Failure Signature

- divergence / instability: none observed in this smoke test
- conservation issues: not assessed in detail
- oscillation / noise: not assessed in detail
- nonphysical result: not assessed in detail
- convergence stall: none; run completed
- performance bottleneck: none for this small case
- other:
  - warning-like runtime messages appeared, including repeated dispersion-convergence messages during boundary generation
  - `DTHETA_S` was reported as unknown/unused/multiple in the example input

## Diagnostics

- logs:
  - successful runtime log from `run_xbeach.bat`
  - end status: `Done. Exit code: 0`
- plots: not generated during this smoke test review
- metrics:
  - duration about 1 second
  - 265 timesteps
- visual inspection: not yet performed on `xboutput.nc`

## Hypotheses

1. the rebuilt executable is operational and compatible with the local example runner
2. the example case is suitable as a smoke/regression test but not yet a scientific validation baseline
3. the dispersion-convergence warnings may reflect example input characteristics rather than a broken build

## Intervention

- updated the local SVN source tree to revision 6155
- rebuilt using Windows Visual Studio / Intel IFX configuration `MPI_netcdf_Release|x64`
- promoted the rebuilt executable into `bin/xbeach_IFX.exe`

## Outcome

- improved: confidence that the operating executable is rebuilt from the updated source and runnable
- unchanged: no scientific validation yet
- worsened: none observed

## Reusable Lessons

- local XBeach runtime can be validated quickly with `models/example_1d`
- a successful smoke test should be recorded separately from a scientific validation case

## Promotion Candidates

- heuristic candidate: use `example_1d` as the first quick regression/smoke test after rebuilds
- failure-pattern candidate: none yet
- playbook candidate: Windows rebuild plus smoke-test checklist

## Confidence

- confidence level: medium
- why: executable launch and completion were verified, but scientific correctness of outputs was not yet reviewed

## Next Step

Inspect `xboutput.nc` lightly or move to a richer baseline case-selection note for XBeach foundation work.
