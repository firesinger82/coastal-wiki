---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/xbeach-sources/03-holland-coast-reference.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/XBeach
notes: "P2 catalog audit 2026-05-24 — xbeach.readthedocs.io 공식 docs URL audit confirmed via WebFetch (examples.html: DELILAH 2D directional spreading + Holland Coast 1976 storm morfac=1 모두 local note 인용과 일치). Mixed local  + 외부 공식 URL — primary citation = readthedocs"
---
# XBeach Holland Coast Reference Note

## Metadata

- date: 2026-04-30
- title: XBeach Holland Coast reference case
- source type: example / manual
- authors: XBeach documentation stack
- year: active documentation reference
- link: https://xbeach.readthedocs.io/en/latest/examples.html
- local path:
  - numerical_models/xbeach/XBEACH_MANUAL.md
  - official examples page summary

## Why This Matters

Holland Coast is the strongest currently documented morphology-oriented reference case for the XBeach lane in this workspace. It is the best first anchor for dune/profile erosion interpretation because the documentation already frames it as an event-scale erosion case rather than just a hydrodynamic comparison.

## Core Claims

- Holland Coast is documented as a **1D dune-erosion** style example
- the local note characterizes it as:
  - grid: `1564 x 0`
  - representative grain size: `D50 = 0.000245 m`
  - storm duration: `42 hours` (`tstop = 151200 s`)
  - `morfac = 1`
  - a reconstruction of a `1976` storm
- because `morfac = 1`, the example is especially useful as an event-faithful early morphology reference rather than an accelerated exploratory test

## Practical Value

- method details:
  - provides a role-specific reference for profile and dune-erosion interpretation
- implementation detail:
  - gives a concrete reference pattern for later source-note enrichment: 1D, storm duration, event-faithful morphology framing
- validation detail:
  - useful for checking whether a custom morphology baseline is closer to profile/dune response logic than to generic smoke testing
- limitations:
  - the exact local runnable Holland Coast package is not yet attached in this workspace
  - this note is still a documented reference note rather than a reproduced local case note

## Relevance Tags

- solver: XBeach
- physics: morphodynamics
- numerics: 1D storm-event setup
- diagnostics: profile / dune erosion interpretation
- failure mode: none yet

## Transferability

This reference is most transferable when the question is:
- how to interpret a first morphology-oriented XBeach baseline
- whether a run should be treated as event-faithful or accelerated
- how dune/profile response should be separated from pure hydrodynamic credibility work

It is less transferable when the main question is 2D directional hydrodynamic validation.

## Extraction Targets

- exact Holland Coast parameter set if later obtainable from local or official example assets
- which outputs are most important for dune/profile comparison
- whether local scripts or notebooks can reproduce a profile-comparison plot similar to the manual note
- whether the case can become the first local scientific morphology baseline rather than only a conceptual reference

## Working Role In This Wiki

Use Holland Coast as:
- the first **morphology-oriented reference baseline** for XBeach
- the default conceptual anchor for event-faithful dune/profile erosion interpretation

Do not use Holland Coast as:
- the smoke/regression test case
- the first 2D hydrodynamic validation case
- evidence that accelerated morphology settings are always acceptable in early baseline work

## Links

- related experiments: none yet
- related heuristics:
  - `knowledge/heuristics/xbeach-validate-hydrodynamics-before-trusting-morphology.md`
- related failure patterns:
  - `knowledge/failure-patterns/xbeach-morphology-interpretation-drift.md`
- related method notes:
  - [[xbeach-morphology-foundation]]
  - [[xbeach-first-baseline-case-selection]]
  - [[xbeach-parameter-glossary-v1]]
