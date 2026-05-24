---
citation_status: source-needed
origin: _staging/from-modeling-wiki/knowledge/methods/adcirc-sources/02-getting-started.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# ADCIRC Getting Started

## Metadata

- date: 2026-04-12
- title: Getting Started
- source type: manual
- authors: ADCIRC development team
- year: active documentation site
- link: https://adcirc.github.io/adcirc/getting_started/index.html
- local path: not downloaded yet

## Why This Matters

This is the shortest path from zero to a runnable baseline.

## Core Claims

- core prerequisites include a Fortran compiler, MPI, optional but recommended NetCDF, and CMake for the CMake flow
- the build can be done by traditional Make or CMake
- the first parallel workflow is `adcprep --partmesh`, `adcprep --prepall`, then `mpirun ... ./padcirc`
- a starter run path points directly to the `adcirc-testsuite`

## Practical Value

- method details: distinguishes serial and parallel execution paths
- implementation detail: clarifies which executables are expected early
- validation detail: points to the testsuite as the first runnable baseline
- limitations: does not replace the deeper file and parameter references

## Relevance Tags

- solver: ADCIRC
- physics: setup
- numerics: execution workflow
- diagnostics: startup validation
- failure mode: build and run mistakes

## Transferability

Useful for any local ADCIRC installation and for deciding what the first baseline run should look like.

## Extraction Targets

- baseline build checklist
- first run checklist
- first example candidate from testsuite

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
