---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/heuristics/xbeach-validate-hydrodynamics-before-trusting-morphology.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: experience-only
notes: P1 triage mixed default (model=XBeach; source-needed)
---
# Heuristic Note

## Rule

In XBeach, do not trust erosion or morphology results until the wave/boundary setup and hydrodynamic response are credible first.

## Applies When

- `morphology = 1` and sediment transport are enabled
- the case is being used to interpret shoreline retreat, dune erosion, profile change, or erosion volume
- the run depends on nontrivial wave-boundary choices such as `surfbeat`, `nonh`, `parametric`, `jonstable`, or `swan`
- a baseline case is still being established

## Does Not Apply When

- the run is explicitly a morphology stress test with no claim of physical realism
- the purpose is only smoke/regression testing of executable health
- hydrodynamic credibility has already been checked against a trusted reference or observations for the same setup class

## Evidence

- supporting experiments:
  - `experiments/2026/xbeach/2026-04-30-example-1d-smoke-test.md`
- supporting sources:
  - `knowledge/methods/xbeach-boundary-and-wave-setup.md`
  - `knowledge/methods/xbeach-morphology-foundation.md`
  - `knowledge/methods/xbeach-first-baseline-case-selection.md`
  - `knowledge/methods/xbeach-sources/02-delilah-reference.md`
  - `knowledge/methods/xbeach-sources/03-holland-coast-reference.md`

## Why It Works

Morphology in XBeach is downstream of mode choice, wave boundary type, water-level treatment, current response, transport formulation, and slope-handling logic. If those upstream pieces are wrong, the bed-change pattern can look plausible while still being driven by the wrong hydrodynamics. Validating hydrodynamics first reduces false confidence in erosion results and keeps later parameter tuning interpretable.

## Fast Checks Before Use

- is `wavemodel` explicitly recorded and justified?
- are `wbctype`, `bcfile`, and tide inputs fixed and reproducible?
- is the case being judged as 1D or 2DH, and is that choice intentional?
- has the run shown stable, interpretable hydrodynamic behavior before morphology is discussed?
- are `form`, `morfac`, `avalanching`, `wetslp`, and `dryslp` logged explicitly?

## Failure Modes

This heuristic can mislead if it becomes an excuse to postpone morphology work forever. For some workflows, morphology exploration is exactly how you discover whether the boundary or transport setup is insufficient. The point is not to ban early morphology tests; it is to avoid treating early morphology output as trustworthy scientific evidence before the hydrodynamic setup has earned that trust.

## Confidence

medium
