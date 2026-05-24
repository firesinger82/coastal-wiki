# Playbook

## Problem

How to reconstruct and classify the current `wide6` ADCIRC branch well enough to use it as a baseline for later replay, revalidation, and mesh-tool comparison.

## Entry Conditions

Use this playbook when:
- `wide6` or an equivalent retained local branch is the current best candidate baseline
- final run artifacts exist, but provenance is incomplete
- the next decision depends on whether the baseline is reproducible enough to compare against new preprocessing paths

## Inputs Needed

- retained final artifacts: `fort.14`, `fort.15`, `fort.13`, forcing files, and any trusted outputs
- candidate raw inputs: shapefiles, DEM/bathymetry sources, tidal/meteorological inputs
- preprocessing scripts, notebooks, helper utilities, and backups associated with `wide6`
- current notes in `knowledge/methods/` and open questions in `context/active-questions.md`

## Procedure

1. Freeze the canonical candidate branch.
   - Name the exact retained artifact set being audited.
   - Record paths and timestamps.
   - Do not mix backup variants into the canonical set unless explicitly justified.

2. Build a provenance inventory.
   - List confirmed raw inputs.
   - List confirmed scripts/utilities.
   - List confirmed manual interventions.
   - List explicit unknowns.

3. Run structural sanity checks.
   - Verify mesh structure expectations for the retained `fort.14`.
   - Verify boundary classes and open-boundary depth sanity.
   - Verify `fort.15` settings against the current retained run interpretation.

4. Reconstruct the minimum replay path.
   - Identify the smallest subset of steps that can regenerate a close structural equivalent.
   - Separate exact replayable steps from approximate reconstruction steps.
   - Log which steps remain MATLAB-only, manual-only, or ambiguous.

5. Classify baseline status.
   - `reproducible`: source inputs, transforms, and final artifacts line up well enough for a fair replay.
   - `partially reproducible`: core path is recoverable, but some interventions remain ambiguous.
   - `non-reproducible`: essential upstream steps cannot be recovered with current evidence.

6. Decide the next action.
   - If reproducible: proceed to controlled revalidation against new tooling.
   - If partially reproducible: constrain comparison claims and prioritize closing the highest-impact unknowns.
   - If non-reproducible: stop treating the branch as a fair gold standard and switch to a cleaner baseline path.

## Stop Conditions

Stop and escalate when:
- more than one retained branch competes for canonical status and no objective tie-break exists
- key raw inputs cannot be identified at all
- structural mismatches suggest the retained artifacts do not belong to the same effective workflow
- baseline status remains unknown, but downstream tool comparison is already being framed as if it were fair

## Outputs

This playbook should produce:
- one named canonical baseline candidate
- a provenance inventory with confirmed/unknown buckets
- a baseline status label: reproducible, partially reproducible, or non-reproducible
- a short list of next checks needed before fair mesh-tool comparison

## References

- related experiments:
  - `experiments/2026/adcirc/2026-04-12-quarterannular-baseline-mve.md`
  - `experiments/2026/adcirc/2026-04-12-quarterannular-dt-sensitivity-mve.md`
- related heuristics:
  - `knowledge/heuristics/adcirc-baseline-before-tool-revalidation.md`
- related sources:
  - `knowledge/methods/adcirc-wide6-validation-checklist.md`
  - `knowledge/methods/adcirc-fort15-checklist-v1.md`
  - `knowledge/methods/adcirc-bathymetry-input-foundation.md`
  - `knowledge/methods/adcirc-forcing-input-foundation.md`
  - `knowledge/methods/adcirc-wide6-provenance-gap.md`
