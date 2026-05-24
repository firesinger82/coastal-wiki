---
title: "adcirc parameter glossary v1"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-parameter-glossary-v1.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC Parameter Glossary V1

Date: 2026-04-12

This is a first-pass glossary for parameters and concepts that should be tracked early.

It is intentionally narrow. The goal is to stabilize vocabulary before the first experiment.

## Files

- `fort.14`
  - grid and boundary information
  - required

- `fort.15`
  - model parameters and periodic boundary conditions
  - required

- `fort.13`
  - nodal attributes
  - optional but common

## Core Geometry And Boundary Terms

- `AGRID`
  - alphanumeric grid identification string
  - useful for labeling baseline cases consistently

- `DP(JN)`
  - bathymetric depth relative to the geoid
  - positive below the geoid, negative above the geoid
  - if nodes can dry, wetting and drying must be enabled

- `IBTYPE(k)`
  - boundary type identifier
  - controls whether the boundary acts like mainland, island, river/open-ocean normal-flow, or barrier classes
  - early source of setup mistakes if misunderstood

## Stability-Relevant Terms

- `tau0`
  - weighting applied to the primitive continuity equation within the generalized wave continuity formulation
  - FAQ guidance indicates higher values are generally used in shallower water
  - should become one of the first logged parameters in stability experiments

- `WarnElev`
  - warning threshold for large free-surface elevation
  - warning output can be an early signal of growing instability

- `ErrorElev`
  - hard-stop threshold for clearly erroneous water-surface elevations

## Execution Terms

- `adcprep`
  - parallel preprocessor used to partition mesh and prepare subdomain inputs

- `adcirc`
  - serial executable

- `padcirc`
  - parallel executable

## Output Terms To Track Early

- `fort.61.nc`
  - elevation time series at specified stations

- `fort.63.nc`
  - elevation time series at all nodes

- `fort.64.nc`
  - velocity time series at all nodes

## Why This Glossary Exists

- to reduce vocabulary drift between source notes and future experiment cards
- to identify what must be logged for the first baseline and first stability experiments
- to keep file names, executable names, and parameter names consistent in this wiki

## Next Expansion Candidates

- first-pass fort.15 parameter groups for time stepping, output, and forcing
- first-pass boundary-condition vocabulary for ocean, land, barrier, and river cases
