---
title: "ADCIRC Storm Surge — 실험 시작 전 요구사항 체크리스트"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/adcirc/src/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge-requirements-checklist.md (modeling-wiki 4월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/raw/source_code/adcirc/src/
---

# ADCIRC Storm Surge Requirements Checklist

Date: 2026-04-12

Purpose:
- list what must be prepared before storm-surge experiments begin
- keep this at the requirements level, not the tuning level

## General Storm Surge Requirements

- [ ] target domain and mesh identified
- [ ] bathymetry/topography source identified
- [ ] vertical datum context identified
- [ ] tide vs storm-tide decision made
- [ ] meteorological forcing family selected
- [ ] baseline example closest to the intended workflow identified
- [ ] required output families chosen
- [ ] validation data sources identified

## `JMA-MSM + NWS=13` Requirements

### Source Data

- [ ] JMA-MSM coverage window identified
- [ ] JMA-MSM spatial coverage confirmed against the ADCIRC mesh
- [ ] wind and pressure fields available for the required period
- [ ] source temporal cadence recorded

### Conversion To ADCIRC-Readable Forcing

- [ ] conversion path from JMA-MSM to OWI-NWS13 NetCDF documented
- [ ] variable mapping documented for `U10`, `V10`, `PSFC`
- [ ] `lat`, `lon`, `time` handling documented
- [ ] units checked and documented
- [ ] overlay/group policy documented if multiple grids are used
- [ ] output file naming policy documented (`fort.22.nc` or override)

### ADCIRC fort.15 Interface

- [ ] `NWS = 13` confirmed
- [ ] `WTIMINC` policy documented
- [ ] `&owiWindNetcdf` namelist documented
- [ ] `NWS13ColdStartString` policy documented
- [ ] `NWS13File` override policy documented if applicable
- [ ] `NWS13WindMultiplier` use documented if applicable
- [ ] `NWS13GroupForPowell` use documented if applicable

### Ramping And Restart

- [ ] cold start vs hotstart path documented
- [ ] meteorological ramping policy documented
- [ ] if hotstart is used, `NRAMP/DRAMPMete/DRAMPUnMete` handling documented

### Outputs And Evaluation

- [ ] water-level outputs selected
- [ ] max-elevation output selected
- [ ] velocity outputs selected if needed
- [ ] meteorological outputs such as `NOUTGW` policy documented
- [ ] archive and naming policy documented

## What This Checklist Is Not

This checklist does not yet answer:
- what exact `DT` to use
- what exact drag values to use
- what exact mesh resolution to use
- which run is "best"

Those belong after requirements are documented.
