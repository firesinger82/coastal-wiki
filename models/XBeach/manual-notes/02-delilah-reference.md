---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/xbeach-sources/02-delilah-reference.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/XBeach
notes: "P2 catalog audit 2026-05-24 — xbeach.readthedocs.io 공식 docs URL audit confirmed via WebFetch (examples.html: DELILAH 2D directional spreading + Holland Coast 1976 storm morfac=1 모두 local note 인용과 일치). Mixed local  + 외부 공식 URL — primary citation = readthedocs"
---
# XBeach DELILAH Reference Note

## Metadata

- date: 2026-04-30
- title: XBeach DELILAH reference case
- source type: example / manual
- authors: XBeach documentation stack
- year: active documentation reference
- link: https://xbeach.readthedocs.io/en/latest/examples.html
- local path:
  - numerical_models/xbeach/XBEACH_MANUAL.md
  - official examples page summary

## Why This Matters

DELILAH is the clearest currently documented hydrodynamic reference case for the XBeach lane in this workspace. It gives a role-specific anchor for answering whether a 2D surfbeat setup with directional forcing behaves credibly before morphology is trusted.

## Core Claims

- DELILAH is documented as a field-experiment reference case
- it is framed as a **2D hydrodynamic** case
- the local note characterizes it as:
  - grid: `177 x 70`
  - representative grain size: `D50 = 0.0002 m`
  - `surfbeat` mode
  - directional spreading
  - comparison against field observations
- in this workspace, its strongest role is hydrodynamic reference, not first morphology baseline

## Practical Value

- method details:
  - anchors the idea that 2D surfbeat directional-wave behavior should be checked against a documented reference before treating a custom case as trustworthy
- implementation detail:
  - gives a concrete target profile for later source-note enrichment: 2D, surfbeat, directional wave setup, field-comparison framing
- validation detail:
  - explicitly tied to field data comparison rather than just internal smoke testing
- limitations:
  - the exact local runnable DELILAH package is not yet attached in this workspace
  - this note currently functions as a documented role reference, not a reproduced case note

## Relevance Tags

- solver: XBeach
- physics: hydrodynamics
- numerics: 2D surfbeat directional forcing
- diagnostics: field-data comparison
- failure mode: none yet

## Transferability

This reference is most transferable when the question is:
- whether a 2D surfbeat setup is physically credible
- whether directional boundary logic is being treated seriously enough
- whether a run should be judged as hydrodynamic baseline rather than morphology evidence

It is less transferable when the main question is first-pass dune/profile erosion interpretation.

## Extraction Targets

- exact DELILAH boundary setup if obtainable later
- how directional spreading is parameterized in the documented example
- what output variables or metrics are used in the field-data comparison
- whether a local runnable reproduction already exists elsewhere in the workspace or online example assets

## Working Role In This Wiki

Use DELILAH as:
- the first **hydrodynamic credibility reference** for XBeach
- a reminder that 2D surfbeat runs should be judged on forcing and current/wave behavior before morphology is discussed

Do not use DELILAH as:
- the first morphology baseline
- a generic smoke test
- proof that any custom 2D run is automatically valid just because it also uses `surfbeat`

## Links

- related experiments: none yet
- related heuristics:
  - `knowledge/heuristics/xbeach-validate-hydrodynamics-before-trusting-morphology.md`
- related failure patterns:
  - `knowledge/failure-patterns/xbeach-morphology-interpretation-drift.md`
- related method notes:
  - `knowledge/methods/xbeach-boundary-and-wave-setup.md`
  - `knowledge/methods/xbeach-first-baseline-case-selection.md`
  - `knowledge/methods/xbeach-morphology-foundation.md`
