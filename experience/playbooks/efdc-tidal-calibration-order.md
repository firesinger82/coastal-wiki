---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/playbooks/efdc-tidal-calibration-order.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: experience-only
notes: P1 triage mixed default (model=EFDC; source-needed)
---
# Playbook

## Problem

How to calibrate an EFDC tidal/coastal model in a disciplined order, especially when water level already looks reasonable but current behavior is still mismatched.

## Entry Conditions

Use this playbook when:
- the model is numerically stable enough for diagnosis
- water level amplitude and/or phase is already at least broadly reasonable
- current speed, direction, flood/ebb asymmetry, or timing is still unsatisfactory
- the next calibration move is not yet clear

Do not use this playbook as written when:
- both water level and current are obviously wrong from the start
- the run is still crashing or producing nonphysical states
- the domain setup is still changing too rapidly for fair comparison

## Inputs Needed

- current trusted EFDC configuration and run outputs
- observed water-level and current data used for comparison
- clear record of the model version, bathymetry version, and boundary/forcing inputs
- current notes:
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
  - `knowledge/methods/efdc-parameter-glossary-v1.md`
  - `knowledge/methods/efdc-calibration-foundation.md`
  - `knowledge/failure-patterns/efdc-water-level-good-current-bad.md`
  - `knowledge/heuristics/efdc-check-comparison-basis-before-friction-tuning.md`

## Procedure

1. Freeze the comparison frame.
   - Choose the exact stations, time windows, metrics, and output variables that will be compared.
   - Record whether each comparison is stage, speed, direction, vector components, or depth-averaged quantity.
   - Do not change the comparison definition mid-calibration unless the old definition is proven invalid.

2. Verify the comparison basis.
   - Confirm time alignment and averaging windows.
   - Confirm datum and coordinate conventions.
   - Confirm whether observed and modeled currents are comparable in vertical representation.
   - Confirm whether the observation site is representative of the modeled cell.

3. Check geometry and bathymetry before parameter tuning.
   - Inspect mismatch zones for channel alignment issues, shoals, tidal flats, harbor entrances, and constrictions.
   - Check whether cross-sectional conveyance looks believable.
   - Check whether smoothing or interpolation may have removed key hydraulic structure.

4. Re-check boundary and forcing interpretation.
   - Review tidal constituent phase and amplitude assumptions.
   - Review open-boundary placement and segmentation.
   - Check whether river inflow, wind, or density-driving effects are missing where they should matter.
   - Ask whether stage fit may have been achieved with forcing choices that still produce the wrong momentum response.

5. Inspect wetting/drying behavior.
   - Review shallow exchange zones and marginal cells.
   - Check whether wet/dry behavior is creating unrealistic connectivity or disconnecting real pathways.
   - Note whether current mismatch clusters around shallow or intermittently wet areas.

6. Tune bottom friction in a controlled way.
   - Change friction only after Steps 1-5 are acceptably understood.
   - Use small, logged changes.
   - Prefer physically interpretable zoning over arbitrary global changes when the domain clearly varies.
   - Check whether improved currents damage stage skill, or vice versa.

7. Tune mixing and secondary physics only after the main momentum pathways are credible.
   - Revisit horizontal mixing or diffusion assumptions.
   - Revisit vertical structure assumptions.
   - Revisit density effects if simplification is no longer justified.

8. Record the result as an experiment card.
   - Log what was changed, what stayed fixed, what improved, what worsened, and what remains unresolved.
   - Identify whether the run produced a new heuristic, failure pattern refinement, or follow-up playbook update.

## Stop Conditions

Stop and escalate when:
- comparison fairness is still unresolved after targeted checks
- geometry/bathymetry uncertainty is too large for meaningful parameter tuning
- forcing assumptions are still underdetermined
- friction changes are only trading off stage skill against current skill without improving overall credibility
- the next parameter change cannot be justified by a ranked hypothesis

## Outputs

This playbook should produce:
- one logged calibration step with a fixed comparison frame
- a ranked diagnosis of the current mismatch
- a record of whether the issue was primarily comparison, geometry, forcing, wet/dry, friction, or mixing related
- one clearly justified next calibration move

## References

- related experiments:
  - future EFDC experiment cards should be linked here once recorded
- related heuristics:
  - `knowledge/heuristics/efdc-check-comparison-basis-before-friction-tuning.md`
- related sources:
  - `knowledge/methods/efdc-current-mismatch-diagnosis.md`
  - `knowledge/methods/efdc-parameter-glossary-v1.md`
  - `knowledge/methods/efdc-calibration-foundation.md`
  - `knowledge/failure-patterns/efdc-water-level-good-current-bad.md`
