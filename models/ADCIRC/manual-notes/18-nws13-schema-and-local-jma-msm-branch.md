---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/18-nws13-schema-and-local-jma-msm-branch.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
---
# NWS13 Schema And Local JMA-MSM Branch

## Metadata

- date: 2026-04-12
- title: official NWS13 schema and the local JMA-MSM branch
- source type: manual
- authors: ADCIRC development team plus local workflow statement
- year: active documentation site plus current local practice
- link: https://adcirc.github.io/adcirc/user_guide/model_configuration/meteorological_forcing/nws13.html ; https://adcirc.github.io/adcirc/technical_reference/input_files/fort22.html
- local path: E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc\docs\user_guide\model_configuration\meteorological_forcing\nws13.rst

## Why This Matters

This is the key bridge between official ADCIRC meteorological schema and the actual local storm-surge workflow.

## Core Claims

- official ADCIRC docs define `NWS=13` as OWI NetCDF gridded wind and pressure
- the documented schema includes `U10`, `V10`, `PSFC`, `lat`, `lon`, and `time`
- `&owiWindNetcdf` in `fort.15` controls cold-start alignment and optional file naming
- the local standard branch uses `JMA-MSM` upstream of `NWS=13`
- therefore a conversion layer is part of the real workflow, even though the docs only define the ADCIRC-facing side

## Practical Value

- method details: tells us what the ADCIRC-readable target format must be
- implementation detail: shows that `JMA-MSM` handling belongs in preprocessing, not only in run control
- validation detail: points directly to schema, unit, and time-alignment failure modes
- limitations: the exact local conversion code is still unknown

## Relevance Tags

- solver: ADCIRC
- physics: meteorological forcing
- numerics: `NWS=13`
- diagnostics: schema and timing alignment
- failure mode: forcing conversion mismatch

## Transferability

High for local gridded storm-surge workflows using converted meteorological products.

## Extraction Targets

- document the local `JMA-MSM -> NWS13` conversion path
- document the archive and validation checks for converted forcing

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
