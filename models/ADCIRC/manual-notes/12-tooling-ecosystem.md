---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/12-tooling-ecosystem.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# ADCIRC Tooling Ecosystem

## Metadata

- date: 2026-04-12
- title: Tools, ADCIRCpy, and ASGS
- source type: code
- authors: ADCIRC docs team, NOAA ADCIRCpy maintainers, ASGS operators
- year: active ecosystem
- link: https://adcirc.github.io/adcirc/tools/index.html ; https://github.com/oceanmodeling/adcircpy ; https://github-wiki-see.page/m/StormSurgeLive/asgs/wiki/ASGS-Operators-Guide
- local path: not downloaded yet

## Why This Matters

Tooling should be added only when it reduces manual friction without hiding the model basics.

## Core Claims

- the official tools page surfaces preprocessing, setup, automation, and postprocessing tools including ADCIRCpy, ASGS, Kalpana, FigureGen, OceanMesh2D, and others
- ADCIRCpy is a Python layer for automating input generation, runs, and common plotting tasks
- ASGS is the operational automation pattern for recurrent ADCIRC plus SWAN production workflows

## Practical Value

- method details: helps stage future automation in the right order
- implementation detail: ADCIRCpy is the first likely automation candidate after baseline understanding exists
- validation detail: ASGS is more appropriate for later operational or repeat forecast workflows than early foundation work
- limitations: introducing these too early can hide fort.14 and fort.15 understanding

## Relevance Tags

- solver: ADCIRC
- physics: operations
- numerics: workflow automation
- diagnostics: postprocessing support
- failure mode: premature abstraction

## Transferability

High, but only after the first baseline and first manual experiment are stable.

## Extraction Targets

- define the trigger for when ADCIRCpy becomes worth installing
- define the trigger for when ASGS becomes worth adopting

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
