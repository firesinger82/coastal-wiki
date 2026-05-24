---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/failure-patterns/xbeach-morphology-interpretation-drift.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: experience-only
notes: P1 triage mixed default (model=XBeach; source-needed)
---
# Failure Pattern

## Pattern Name

morphology interpretation drift

## Symptom

A XBeach run produces plausible-looking erosion, deposition, dune retreat, or profile change, but the interpretation drifts ahead of what the hydrodynamic setup actually justifies.

Typical signs:
- bed change is discussed confidently even though boundary and wave setup were not frozen clearly
- morphology conclusions are drawn from a case that was only meant as a smoke test
- different `wavemodel`, `wbctype`, or transport settings are compared as if only morphology changed
- high `morfac` results are interpreted as event-faithful storm behavior without qualification
- scarping or profile differences are attributed only to forcing while avalanching and slope controls were not reviewed

## Common Context

- solver / model: XBeach
- mesh / geometry: 1D or 2DH coastal erosion baseline under setup exploration
- forcing: wave/tide forcing still being stabilized, or baseline role not yet clearly classified
- parameter regime: `morphology = 1`, sediment transport active, and one or more morphology controls not logged carefully

## Likely Causes

1. hydrodynamic credibility was never established before discussing morphology
2. boundary setup, mode choice, or case role changed between runs without being treated as a first-order difference
3. `morfac` or transport-form changes were treated as harmless implementation details instead of interpretation-changing assumptions
4. avalanching and slope-limiting logic were ignored while reading dune/profile outcomes
5. a smoke/regression case was mistaken for a scientific morphology baseline

## Quick Triage

1. classify the case role first
   - smoke/regression
   - hydrodynamic reference
   - morphology-oriented baseline
2. freeze the upstream setup identity
   - `wavemodel`
   - `wbctype`
   - `bcfile`
   - tide inputs
   - 1D vs 2DH framing
3. verify morphology controls were logged
   - `form`
   - `morfac`
   - `morfacopt`
   - `avalanching`
   - `wetslp`
   - `dryslp`
4. ask whether the result is event-faithful or accelerated
5. only then decide whether the morphology output deserves physical interpretation

## Supporting Evidence

- related experiments:
  - `experiments/2026/xbeach/2026-04-30-example-1d-smoke-test.md`
- related sources:
  - `knowledge/methods/xbeach-morphology-foundation.md`
  - `knowledge/methods/xbeach-first-baseline-case-selection.md`
  - `knowledge/heuristics/xbeach-validate-hydrodynamics-before-trusting-morphology.md`
  - `knowledge/playbooks/xbeach-first-storm-baseline-checklist.md`
  - `knowledge/methods/xbeach-sources/03-holland-coast-reference.md`

## Common False Leads

- false lead 1: "the erosion pattern looks reasonable, so the setup must be right"
- false lead 2: treating `morfac` as a speed knob with no interpretation cost
- false lead 3: comparing two morphology outputs without checking whether boundary/mode assumptions also changed
- false lead 4: using a smoke-test case as if it were a validated morphology reference

## Confidence

medium
