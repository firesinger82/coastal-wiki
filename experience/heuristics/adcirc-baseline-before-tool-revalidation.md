---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/heuristics/adcirc-baseline-before-tool-revalidation.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: experience-only
notes: P1 triage mixed default (model=ADCIRC; source-needed)
---
# Heuristic Note

## Rule

Do not start serious ADCIRC mesh-tool revalidation until the current local baseline has been classified as reproducible, partially reproducible, or non-reproducible.

## Applies When

- a retained local baseline such as `wide6` is being used as the comparison target for `OceanMesh2D`, `Gmsh`, or `OCSMesh`
- the team is tempted to optimize or replace tooling before the current baseline path is closed
- preprocessing artifacts exist, but provenance is still incomplete

## Does Not Apply When

- the goal is only exploratory learning with no claim of fair comparison
- the current baseline has already been replayed and documented well enough for fair reuse
- a clean official example case is being used instead of a tuned local branch

## Evidence

- supporting experiments:
  - `experiments/2026/adcirc/2026-04-12-quarterannular-baseline-mve.md`
  - `experiments/2026/adcirc/2026-04-12-quarterannular-dt-sensitivity-mve.md`
- supporting sources:
  - `knowledge/methods/adcirc-baseline-selection.md`
  - `knowledge/methods/adcirc-wide6-validation-principles.md`
  - `knowledge/methods/adcirc-wide6-provenance-gap.md`
  - `knowledge/methods/adcirc-mesh-revalidation-principles.md`
  - `context/CONTEXT.md`
  - `context/active-questions.md`

## Why It Works

A new mesh tool can only be judged fairly if the target it is trying to match is itself well-characterized. If the current baseline is under-documented, then later differences in geometry, bathymetry, boundaries, or stability behavior cannot be attributed cleanly to the new tool. Closing baseline status first prevents false comparisons, vocabulary drift, and repeated reinvention of unknown manual steps.

## Fast Checks Before Use

- can you point to the exact retained `fort.14`, `fort.15`, and `fort.13` being treated as canonical?
- is there a written list of confirmed source inputs, confirmed scripts, and confirmed manual interventions?
- has the baseline been labeled reproducible, partially reproducible, or non-reproducible?
- are downstream comparisons being framed against a known baseline status rather than an assumed "best branch"?

## Failure Modes

This heuristic can mislead if it becomes an excuse to avoid all exploration. If the baseline never becomes fully reproducible, the correct move is not infinite preservation work; it is to label the baseline honestly and proceed with bounded revalidation against a partially trusted target. It also should not block simple educational tests on official examples.

## Confidence

medium
