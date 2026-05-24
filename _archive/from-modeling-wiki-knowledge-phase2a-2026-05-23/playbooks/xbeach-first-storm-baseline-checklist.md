# Playbook

## Problem

How to establish the first credible XBeach storm baseline without mixing executable smoke testing, hydrodynamic credibility, and morphology interpretation into one undifferentiated run.

## Entry Conditions

Use this playbook when:
- the XBeach executable is runnable locally
- a first storm-impact baseline is being selected or stabilized
- the team wants to interpret morphology, erosion, or profile change from a new case
- wave and tide boundary setup are not yet a settled routine

Do not use this playbook as written when:
- the goal is only a binary smoke test after rebuilds
- the case is a highly specialized non-hydrostatic or structure-focused study that already requires a custom setup path
- there is already a trusted local baseline for the same class of case

## Inputs Needed

- one candidate case and its `params.txt`
- exact boundary files and tide inputs
- the current operating executable path
- current method notes:
  - `knowledge/methods/xbeach-parameter-glossary-v1.md`
  - `knowledge/methods/xbeach-boundary-and-wave-setup.md`
  - `knowledge/methods/xbeach-morphology-foundation.md`
  - `knowledge/methods/xbeach-first-baseline-case-selection.md`
  - `knowledge/heuristics/xbeach-validate-hydrodynamics-before-trusting-morphology.md`

## Procedure

1. Pick the baseline role first.
   - Decide whether the case is a smoke/regression baseline, hydrodynamic reference baseline, or morphology-oriented baseline.
   - Do not force one case to serve all roles at once.

2. Freeze the setup identity.
   - Record `wavemodel`, `wbctype`, `bcfile`, tide inputs, grid files, bathymetry files, and output settings.
   - Record whether the case is 1D or 2DH.

3. Run the case first as a hydrodynamic credibility check.
   - Before discussing erosion, confirm that the wave and water-level setup are coherent.
   - Inspect whether the run starts, finishes, and produces expected classes of output.
   - If available, compare against documented intent or observations for the case type.

4. Log the morphology switches explicitly.
   - Record `sedtrans`, `morphology`, `form`, `morfac`, `morfacopt`, `avalanching`, `wetslp`, and `dryslp`.
   - If `morfac > 1`, record that the run is accelerated and should not be interpreted the same way as a real-time storm baseline.

5. Decide whether the case is event-faithful or accelerated.
   - For first morphology trust-building, prefer event-faithful framing when possible.
   - If accelerated, mark the result clearly as an efficiency-oriented exploratory baseline, not final evidence.

6. Evaluate the output by role.
   - Smoke baseline: did it run successfully?
   - Hydrodynamic baseline: did the forcing/mode behavior look credible?
   - Morphology baseline: is the bed-change interpretation meaningful given the transport and slope settings?

7. Record the run as an experiment card.
   - Log what role the case served.
   - Log whether it should be reused for smoke, hydrodynamics, morphology, or rejected for one of those roles.

## Stop Conditions

Stop and reframe the baseline when:
- the case cannot be described clearly as smoke, hydrodynamic, or morphology reference
- boundary and wave setup are still changing too much to compare runs fairly
- morphology is being interpreted before upstream forcing credibility is established
- a high `morfac` or unstable setup is being mistaken for a trustworthy storm-erosion baseline

## Outputs

This playbook should produce:
- one clearly classified baseline role for the case
- one reproducible case identity record
- one experiment note explaining whether the case is reusable
- one justified next move: keep, refine, or replace the candidate baseline

## References

- related experiments:
  - `experiments/2026/xbeach/2026-04-30-example-1d-smoke-test.md`
- related heuristics:
  - `knowledge/heuristics/xbeach-validate-hydrodynamics-before-trusting-morphology.md`
- related sources:
  - `knowledge/methods/xbeach-first-baseline-case-selection.md`
  - `knowledge/methods/xbeach-boundary-and-wave-setup.md`
  - `knowledge/methods/xbeach-morphology-foundation.md`
  - `knowledge/methods/xbeach-sources/02-delilah-reference.md`
  - `knowledge/methods/xbeach-sources/03-holland-coast-reference.md`
