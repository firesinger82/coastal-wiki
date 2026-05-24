---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/03-theory-and-formulation.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# ADCIRC Theory And Formulation

## Metadata

- date: 2026-04-12
- title: Theory and formulation
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/theory/index.html
- local path: not downloaded yet

## Why This Matters

This is the bridge between user-facing setup and the numerical assumptions that actually control behavior.

## Core Claims

- ADCIRC solves 2DDI and 3D free-surface circulation problems on unstructured finite element grids
- the documentation explicitly points to a detailed theory PDF for full formulation details
- the theory layer is the right place to separate physics issues from setup issues

## Practical Value

- method details: frames GWCE, momentum treatment, and boundary-condition logic
- implementation detail: points to the full theory PDF when parameter semantics need physical context
- validation detail: helps judge whether a symptom reflects formulation limits or poor setup
- limitations: overview page alone is not sufficient for detailed parameter tuning

## Relevance Tags

- solver: ADCIRC
- physics: shallow-water circulation
- numerics: finite element formulation
- diagnostics: stability interpretation
- failure mode: misdiagnosed numerical issues

## Transferability

Important whenever setup decisions need theoretical justification.

## Extraction Targets

- first list of theory-backed parameters worth tracking in experiment cards
- theory terms to standardize in this wiki

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
