# Experiment Card

## Metadata

- date: 2026-04-12
- title: quarter annular dt sensitivity first controlled change
- status: planned
- domain: coastal hydrodynamics
- model / solver: ADCIRC
- owner: firesinger

## Objective

Test whether a single-variable change in `DT` is the cleanest first modification against the quarter-annular baseline.

## Setup

- geometry / domain: quarter annular harbor example
- mesh / grid: testsuite baseline mesh
- boundary conditions: unchanged from baseline
- initial conditions: cold start baseline
- forcing: tide-only baseline, `NWS = 0`
- parameter values: all baseline values preserved except `DT`
- timestep / CFL: baseline `DT = 174.656`; modified `DT` candidate to be selected before execution
- numerics: preserve baseline `TAU0 = 0.005`, `IM = 0`, `ICS = 1`
- hardware / runtime constraints: prefer a short and cheap first controlled run

## Inputs

- input datasets: bundled testsuite files only
- source files:
  - `raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf/fort.14`
  - `raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf/fort.15`
- config files:
  - `raw/code/adcirc/adcirc-testsuite/test_list.yaml`
- related raw sources:
  - parameter definitions
  - TAU0 documentation
  - ADCIRC FAQ instability guidance

## Expected Behavior

Reducing `DT` should preserve model structure while lowering one obvious source of instability risk, making it a clean first sensitivity variable.

## Observed Behavior

Not run yet.

## Failure Signature

- divergence / instability: watch for warning elevation growth or clear numerical blow-up
- conservation issues: not primary target yet
- oscillation / noise: watch for nonphysical surface oscillation
- nonphysical result: watch for obviously spurious elevations or velocities
- convergence stall: monitor screen and solver behavior
- performance bottleneck: runtime increase from smaller `DT`
- other: output mismatch with expected baseline family

## Diagnostics

- logs: capture screen output and warning messages
- plots: compare at least one elevation output against baseline if run is executed
- metrics: first pass can be qualitative plus output-file presence
- visual inspection: compare whether expected output files are produced cleanly

## Hypotheses

1. `DT` is the safest first experiment variable because it does not alter forcing, topology, or formulation.
2. If behavior changes strongly under modest `DT` reduction, the baseline may already sit near a stability boundary.
3. `TAU0` should be studied only after `DT` sensitivity is understood.

## Intervention

Change only `DT`.

Candidate policy before execution:
- first candidate: reduce `DT` moderately, not aggressively
- preserve all other baseline settings

## Outcome

- improved: not evaluated yet
- unchanged: not evaluated yet
- worsened: not evaluated yet

## Reusable Lessons

- one-variable-first is enforceable in this workflow
- `DT` is the first controlled sensitivity knob for the quarter-annular baseline

## Promotion Candidates

- heuristic candidate: start with `DT` before touching more structural parameters
- failure-pattern candidate: none yet
- playbook candidate: first sensitivity-study protocol

## Confidence

- confidence level: medium
- why: this is a structurally clean first experiment, but no run result exists yet

## Next Step

Choose the actual modified `DT` value and define what counts as success before execution.
