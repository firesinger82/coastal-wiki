# Experiment Card

## Metadata

- date: 2026-04-12
- title: quarter annular baseline familiarization
- status: planned
- domain: coastal hydrodynamics
- model / solver: ADCIRC
- owner: firesinger

## Objective

Understand and preserve the first known-good ADCIRC baseline before changing any inputs.

## Setup

- geometry / domain: quarter annular harbor example
- mesh / grid: testsuite `fort.14`, `NE=96`, `NP=63`
- boundary conditions: baseline open-boundary harmonic forcing with `M2`
- initial conditions: baseline testsuite defaults
- forcing: no wind forcing (`NWS = 0`)
- parameter values: preserve testsuite baseline values first
- timestep / CFL: baseline `DT = 174.656`; CFL check still to be derived
- numerics: baseline testsuite defaults, including `TAU0 = 0.005`
- hardware / runtime constraints: none yet, foundation inspection only

## Inputs

- input datasets: none beyond bundled testsuite files
- source files:
  - `raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf/fort.14`
  - `raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf/fort.15`
- config files:
  - `raw/code/adcirc/adcirc-testsuite/test_list.yaml`
- related raw sources:
  - official getting-started guide
  - examples index
  - parameter definitions

## Expected Behavior

The baseline case should serve as a stable, known-good reference with expected NetCDF outputs and no custom modifications.

## Observed Behavior

Not run yet.

## Failure Signature

- divergence / instability: not evaluated yet
- conservation issues: not evaluated yet
- oscillation / noise: not evaluated yet
- nonphysical result: not evaluated yet
- convergence stall: not evaluated yet
- performance bottleneck: not evaluated yet
- other: this first card is for baseline understanding, not a failure chase

## Diagnostics

- logs: not collected yet
- plots: not collected yet
- metrics: not collected yet
- visual inspection: baseline input anatomy inspected

## Hypotheses

List plausible causes in ranked order.

1. A stable first workflow depends more on preserving the baseline case than on parameter tuning.
2. The first useful experiment will likely involve one fort.15 change against this baseline.
3. Future instability work should log `TAU0`, `DT`, boundary setup, and mesh quality together.

## Intervention

No intervention yet. This card exists to define the baseline before the first controlled change.

## Outcome

- improved: foundation clarity improved
- unchanged: no model behavior change yet
- worsened: none

## Reusable Lessons

- the first experiment should start from the quarter annular NetCDF testsuite path
- baseline understanding is itself a prerequisite artifact, not overhead

## Promotion Candidates

- heuristic candidate: start from an official testsuite case before making local custom changes
- failure-pattern candidate: none yet
- playbook candidate: baseline-case adoption checklist

## Confidence

- confidence level: medium
- why: the baseline path and files are confirmed locally, but no execution or output verification has happened yet

## Next Step

Extract a fort.15 checklist and define the first one-variable modification experiment.
