---
citation_status: source-needed
origin: _staging/from-modeling-wiki/knowledge/methods/adcirc-sources/04-theory-pdf-v44xx.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# ADCIRC Theory PDF V44.xx

## Metadata

- date: 2026-04-12
- title: Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.xx
- source type: report
- authors: Rick Luettich, Joannes Westerink
- year: 2004
- link: https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf
- local path: not downloaded yet

## Why This Matters

This is still the most concrete formulation document surfaced by the official docs.

## Core Claims

- ADCIRC uses a generalized wave continuity equation formulation to avoid spurious oscillations associated with a primitive Galerkin continuity formulation
- the document provides the weak-form derivation, momentum formulations, boundary-condition treatment, and implementation notes
- the report is detailed enough to anchor stability discussions instead of relying on folklore

## Practical Value

- method details: direct source for GWCE, 2D/3D momentum, and boundary handling
- implementation detail: useful when a fort.15 decision needs a formulation-level rationale
- validation detail: provides the theoretical basis for interpreting convergence and oscillation behavior
- limitations: the report is old relative to current releases, so use it together with current docs and release notes

## Relevance Tags

- solver: ADCIRC
- physics: hydrodynamics
- numerics: GWCE
- diagnostics: oscillation and stability interpretation
- failure mode: instability

## Transferability

Highly reusable for any future diagnostic work involving timestep, wet/dry behavior, or boundary-condition pathologies.

## Extraction Targets

- shortlist of parameters tied directly to GWCE weighting and stability
- first glossary of theory terms for the wiki

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
