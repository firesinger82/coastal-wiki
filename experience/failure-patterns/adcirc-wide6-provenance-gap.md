---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/failure-patterns/adcirc-wide6-provenance-gap.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: experience-only
notes: P1 triage mixed default (model=ADCIRC; source-needed)
---
# Failure Pattern

## Pattern Name

wide6 baseline provenance gap

## Symptom

A local ADCIRC mesh or retained run branch appears to be the best available baseline, but the exact sequence of source inputs, script transforms, manual edits, and final retained artifacts cannot be reconstructed with confidence.

Typical signs:
- final `fort.14`, `fort.15`, or `fort.13` exists, but the exact generating path does not
- multiple backups or branch names point to slightly different retained states
- known helper scripts exist, but their relationship to the final retained output is partial
- revalidation discussion keeps drifting back to tool choice before baseline reconstruction is closed

## Common Context

- solver / model: ADCIRC
- mesh / geometry: local `wide6` candidate mesh and related retained preprocessing branches
- forcing: mixed tidal and NWS13/JMA-MSM preparation context
- parameter regime: partially tuned retained branch with incomplete provenance

## Likely Causes

1. iterative manual interventions were applied without a final reproducibility ledger
2. retained scripts and retained artifacts drifted apart during tuning and rescue edits
3. backup naming, alternate forcing branches, and experimental side paths were preserved without a canonical "final branch" declaration
4. baseline quality was inferred from survivorship rather than from a replayable reconstruction check

## Quick Triage

1. freeze the candidate baseline artifact set first: final `fort.14`, `fort.15`, `fort.13`, forcing files, and key outputs
2. build a provenance inventory with four buckets: confirmed source inputs, confirmed scripts, confirmed manual interventions, and explicitly unknown steps
3. compare script signatures and file content against the retained artifacts to separate reproducible steps from unrecoverable steps
4. classify the baseline as reproducible, partially reproducible, or non-reproducible before using it as a revalidation target

## Supporting Evidence

- related experiments:
  - `experiments/2026/adcirc/2026-04-12-quarterannular-baseline-mve.md`
  - `experiments/2026/adcirc/2026-04-12-quarterannular-dt-sensitivity-mve.md`
- related sources:
  - `knowledge/methods/adcirc-wide6-provenance-gap.md`
  - `knowledge/methods/adcirc-wide6-fort14-replay-recipe.md`
  - `knowledge/methods/adcirc-ocsmesh-vs-fort14-replay-mapping.md`
  - `knowledge/methods/adcirc-oceanmesh2d-translation-review.md`
  - `context/active-questions.md`

## Common False Leads

- false lead 1: assuming the most stable surviving branch is automatically a valid baseline
- false lead 2: debating `Gmsh` versus `OCSMesh` before the retained baseline is even reconstructable
- false lead 3: treating missing provenance as a documentation inconvenience instead of a reproducibility failure

## Confidence

medium
