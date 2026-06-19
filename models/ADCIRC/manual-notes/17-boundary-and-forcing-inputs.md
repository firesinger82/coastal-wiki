---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/17-boundary-and-forcing-inputs.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# Boundary And Forcing Inputs

## Metadata

- date: 2026-04-12
- title: boundary-condition structure and forcing input families
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/user_guide/model_configuration/boundary_conditions/boundary_conditions.html ; https://adcirc.github.io/adcirc/technical_reference/input_files/meteorological_forcing_overview.html ; https://adcirc.github.io/adcirc/user_guide/model_configuration/meteorological_forcing/nws_parameters.html ; https://adcirc.github.io/adcirc/user_guide/model_configuration/meteorological_forcing/wtiminc.html
- local path: raw/code/adcirc/adcirc/docs/user_guide/model_configuration

## Why This Matters

This source bundle clarifies that ADCIRC forcing is not one thing. It is boundary forcing plus meteorological forcing with different files and rules.

## Core Claims

- open and flux boundary locations are specified in `fort.14`
- periodic boundary forcing is specified in `fort.15`
- non-periodic elevation forcing uses `fort.19`
- non-periodic flux forcing uses `fort.20`
- meteorological forcing is selected through `NWS`, and the meaning of the meteorological parameter line changes with that choice
- `WTIMINC` is central for many gridded meteorological paths

## Practical Value

- method details: separates boundary forcing from meteorological forcing
- implementation detail: shows which file family must be tracked for each forcing branch
- validation detail: explains why coverage, cadence, and file semantics must be checked before any tuning
- limitations: docs define formats better than they define real-world source pipelines

## Relevance Tags

- solver: ADCIRC
- physics: forcing
- numerics: boundary and met input
- diagnostics: coverage and timing consistency
- failure mode: forcing-family mismatch

## Transferability

Universal for ADCIRC setup work.

## Extraction Targets

- define forcing record templates
- define the local forcing family map

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
