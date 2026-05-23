---
title: "ADCIRC Storm Surge — NWS family 비교 (NWS=12/13/14/19/20)"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/adcirc/src/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge-nws-families.md (modeling-wiki 4월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/raw/source_code/adcirc/src/
---

# ADCIRC Storm Surge NWS Families

Date: 2026-04-12

Purpose:
- compare the main meteorological forcing families relevant to storm-surge work
- clarify why the local workflow centers on `NWS=13`

## Scope

This is still a foundation note.

It compares forcing families and data requirements.
It does not choose final project parameter values.

## Main Families Relevant To Storm Surge

### `NWS=3`

- type: gridded wind forcing on lon/lat grid
- useful for: simpler wind-run style examples
- official example link: APES Wind Run
- limitation: not the main path for the current local workflow

### `NWS=4`

- type: PBL hurricane model input at selected nodes
- useful for: older storm event examples such as Hurricane Isabel
- limitation: more legacy/example-oriented relative to the current local preference

### `NWS=13`

- type: OWI-style NetCDF gridded wind and pressure
- useful for: high-quality gridded forcing with overlays, curvilinear grids, and irregular timesteps
- current local status: primary working path

### `NWS=20`

- type: Generalized Asymmetric Holland Model
- useful for: parametric tropical cyclone forcing with official preference over deprecated `NWS=19`
- strength: compact forcing representation for hurricane workflows
- limitation: less aligned with your stated JMA-MSM-driven workflow

### `NWS=-14` / `NWS=14`

- type: GRIB2 or NetCDF gridded wind and pressure
- useful for: more generic gridded forcing workflows
- strength: broad compatibility with gridded products
- limitation: different configuration path from the OWI-NWS13 convention

## Why `NWS=13` Fits The Current Workflow

Direct facts from ADCIRC docs:
- `NWS=13` is the OWI NetCDF format for gridded wind and pressure
- it supports moving storm-centered grids, overlays, arbitrary and irregular timesteps, and curvilinear grids
- ADCIRC expects an OWI-NWS13-style NetCDF structure and a matching `&owiWindNetcdf` namelist in `fort.15`

Current local workflow fact from the user:
- you mainly experiment with `JMA-MSM` data using `NWS=13`

Inference:
- the working path is not "ADCIRC reads raw JMA-MSM by name"
- the working path is "JMA-MSM is converted into an OWI-NWS13-compatible NetCDF product that ADCIRC can read through `NWS=13`"

That inference is consistent with the official docs and with the fact that the docs describe the expected `NWS=13` file convention, not a JMA-MSM-native reader.

## Practical Implication

For this wiki, `storm surge` should be split into:
- forcing source layer
  - example: JMA-MSM
- ADCIRC forcing interface layer
  - example: `NWS=13`
- conversion layer
  - local scripts or preprocessing that map source data into ADCIRC-readable format

This separation is important because:
- source availability problems belong to the forcing source layer
- NetCDF schema problems belong to the conversion layer
- ADCIRC run interpretation belongs to the interface and model layers

## Official `NWS=13` Requirements We Must Preserve

- OWI-NWS13 conventions in the NetCDF file
- wind fields `U10`, `V10`
- pressure field `PSFC`
- time dimension with valid units
- `lat` and `lon` variables
- group ordering and ranking if overlays are used
- `fort.15` namelist `&owiWindNetcdf`

## Local Workflow Statement

This wiki should treat:
- `JMA-MSM -> OWI-NWS13 NetCDF -> ADCIRC NWS=13`

as the default storm-surge forcing pathway unless a project explicitly says otherwise.

## Next Step

Create a dedicated requirements checklist for the `JMA-MSM + NWS=13` path.
