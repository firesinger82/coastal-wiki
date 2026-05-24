---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/06-parameter-definitions.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# ADCIRC Parameter Definitions

## Metadata

- date: 2026-04-12
- title: Parameter Definitions
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/technical_reference/parameter_definitions/index.html
- local path: not downloaded yet

## Why This Matters

This is the main source for interpreting fort.14 and fort.15 fields without guesswork.

## Core Claims

- the page gives explicit meanings for many fort.14 and fort.15 fields
- boundary types, bathymetry sign conventions, and barrier semantics are stated directly
- some parameter constraints are strict enough that violating them terminates a run

## Practical Value

- method details: supports careful reading of mesh and boundary semantics
- implementation detail: should drive the first parameter glossary in this wiki
- validation detail: helps check whether a setup violates structural assumptions before running
- limitations: the page is extensive, so it should be mined selectively rather than read linearly each time

## Relevance Tags

- solver: ADCIRC
- physics: boundary and bathymetry semantics
- numerics: parameter meaning
- diagnostics: pre-run validation
- failure mode: invalid configuration

## Transferability

Crucial for future experiment cards, decisions, and failure-pattern notes.

## Extraction Targets

- first set of parameters to log in every experiment card
- first pre-run sanity checklist

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
