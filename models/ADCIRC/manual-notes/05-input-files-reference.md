---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/05-input-files-reference.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# ADCIRC Input Files Reference

## Metadata

- date: 2026-04-12
- title: Input Files reference
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/technical_reference/input_files/index.html
- local path: not downloaded yet

## Why This Matters

This is the main map of what files exist and which are required versus conditional.

## Core Claims

- `fort.14` and `fort.15` are required
- `fort.13`, hotstart files, boundary-condition files, and forcing files are conditional
- the input taxonomy is organized by grid, model parameters, nodal attributes, hot start, boundaries, and forcing

## Practical Value

- method details: clarifies which files should be baseline-tracked first
- implementation detail: gives the file families needed for reproducible experiment cards
- validation detail: helps define which artifacts must be archived for each experiment
- limitations: file names alone do not explain parameter meaning

## Relevance Tags

- solver: ADCIRC
- physics: setup
- numerics: input structure
- diagnostics: reproducibility
- failure mode: missing or mismatched files

## Transferability

Universal for all ADCIRC projects.

## Extraction Targets

- minimal file manifest for baseline runs
- per-experiment file checklist

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
