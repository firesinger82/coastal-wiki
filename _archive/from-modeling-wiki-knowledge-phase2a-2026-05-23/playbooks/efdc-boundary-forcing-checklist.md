# Playbook

## Problem

How to review EFDC boundary and forcing setup in a disciplined way before blaming friction or secondary tuning parameters for poor current performance.

## Entry Conditions

Use this playbook when:
- water level fit is acceptable or close to acceptable
- current mismatch remains significant
- the domain is coastal, estuarine, harbor-like, or tidal-channel dominated
- there is uncertainty about how open-boundary, inflow, wind, or density-related forcing has been interpreted

Do not use this playbook as written when:
- the model is still failing basic numerical sanity
- geometry/bathymetry is known to be badly broken and has not been checked yet
- there is no stable comparison frame for evaluating the result

## Inputs Needed

- current EFDC configuration and forcing files
- current trusted bathymetry/domain version
- observed water-level and current comparison set
- boundary grouping or boundary-cell definitions used in the model
- current notes:
  - `knowledge/methods/efdc-boundary-condition-foundation.md`
  - `knowledge/methods/efdc-calibration-foundation.md`
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
  - `knowledge/heuristics/efdc-check-comparison-basis-before-friction-tuning.md`

## Procedure

1. Freeze the calibration window and comparison targets.
   - Choose the exact period, stations, and metrics to evaluate.
   - Do not change the evaluation frame while auditing forcing unless the frame itself is invalid.

2. Confirm the seaward/open-boundary concept.
   - Identify the cells or groups treated as open boundary.
   - Check whether the boundary location is physically defensible for the intended exchange zone.
   - Ask whether the open boundary is too close to the area of interest, forcing the model to absorb unresolved dynamics.

3. Check time-series versus harmonic forcing interpretation.
   - Record whether the run uses time-series forcing, harmonic forcing, or a combination.
   - Verify constituent phase and amplitude conventions where harmonic forcing is used.
   - Verify that any time-series forcing is aligned to the correct time base and units.

4. Audit river and freshwater inflow.
   - Check whether inflows exist that should be represented but are missing.
   - Check whether discharge magnitude and timing are plausible.
   - Check whether inflow grouping and location are physically consistent with the real system.

5. Audit wind and other external forcing.
   - Record whether wind is active in the calibration window.
   - Check whether omitted wind could explain current mismatch even when stage still looks acceptable.
   - Check whether event windows include surge-like or weather-driven response that the forcing setup does not capture.

6. Audit density-related forcing assumptions.
   - Record whether temperature and salinity effects are active, simplified, or omitted.
   - If omitted, ask whether that omission is still defensible for the current mismatch zone.
   - Note whether current structure may be density-sensitive even when water level is not.

7. Check boundary-group consistency.
   - Review whether boundary cells are grouped in a physically coherent way.
   - Check whether mixed cell behavior inside one forcing group is hiding a conceptual setup error.
   - Make sure calibration edits do not silently desynchronize boundary logic across related cells or groups.

8. Re-run the diagnosis before friction tuning.
   - After boundary/forcing corrections, re-check stage and current behavior.
   - Only then decide whether friction, wet/dry, or mixing are the next calibration levers.

## Stop Conditions

Stop and escalate when:
- the boundary location itself is not defensible
- phase/amplitude or time-base conventions cannot be reconstructed confidently
- major inflow or external forcing data are missing
- the model is being forced to compensate for unresolved offshore or upstream physics
- boundary uncertainty is still large enough that friction tuning would be non-diagnostic

## Outputs

This playbook should produce:
- one written boundary/forcing audit for the current calibration window
- a list of confirmed forcing assumptions
- a list of unresolved forcing risks
- one justified next action: revise boundary/forcing, move to wet/dry inspection, or move to friction tuning

## References

- related experiments:
  - future EFDC experiment cards should be linked here once recorded
- related heuristics:
  - `knowledge/heuristics/efdc-check-comparison-basis-before-friction-tuning.md`
- related sources:
  - `knowledge/methods/efdc-boundary-condition-foundation.md`
  - `knowledge/methods/efdc-calibration-foundation.md`
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
