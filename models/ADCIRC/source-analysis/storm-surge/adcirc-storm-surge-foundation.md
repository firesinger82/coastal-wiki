---
title: "ADCIRC Storm Surge — Foundation note (요구사항 분류)"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/adcirc/src/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge-foundation.md (modeling-wiki 4월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/raw/source_code/adcirc/src/
---

# ADCIRC Storm Surge Foundation

Date: 2026-04-12

Purpose:
- define what must be understood before doing ADCIRC storm-surge experiments
- organize source material and parameter families without committing to project-specific values yet

This is a foundation note, not a tuning guide.

## What Storm Surge Adds Beyond The Baseline

Compared with the tide-only quarter-annular baseline, storm-surge work adds:
- meteorological forcing
- often larger and more realistic domains
- more complex drag and bottom-friction choices
- stronger need for ramping and hotstart discipline
- validation against water levels, surge envelopes, and sometimes wind fields

## Questions This Topic Must Answer

- what meteorological forcing style should be used?
- what input files are required for that forcing style?
- what parameter families matter most for surge setup?
- what outputs should be retained for surge evaluation?
- which official examples are the best first reference cases?

## Required Source Material Categories

Before real storm-surge setup begins, collect:

### Official Documentation

- `NWS` parameter documentation
- meteorological parameter line / `WTIMINC` documentation
- wind-stress documentation
- ramping documentation
- `fort.22` technical reference
- examples documentation

### Official Example Cases

- Hurricane Katrina (`NWS=20`)
- Global Storm Tide - Hurricane Katrina (`NWS=-14`)
- Hurricane Isabel Wind Run (`NWS=4`)
- APES Wind Run (`NWS=3`)

### Setup Guidance

- typical parameter selections for storm surge
- FAQ entries related to instability, hotstart, and meteorological forcing

### Later But Important

- validation-oriented reports or workshop material
- operational tooling such as `ADCIRCpy` or `ASGS`

## Parameter Families Involved

These are the families that matter. This note does not yet assign project values.

### 1. Meteorological Forcing Family

Main driver:
- `NWS`

Why it matters:
- `NWS` selects the meteorological forcing input type
- it also changes what the meteorological parameter line in `fort.15` must contain

Relevant official options for surge-related work include:
- `NWS = 8`
  - symmetric vortex model
- `NWS = 12`
  - OWI gridded wind and pressure
- `NWS = 13`
  - ramped meteorological forcing
- `NWS = 14`
  - GRIB2/NetCDF forcing
- `NWS = 20`
  - Generalized Asymmetric Holland Model

Important official guidance:
- docs explicitly discourage `NWS=19` in favor of `NWS=20`

### 2. Meteorological Timing Family

Examples:
- `WTIMINC`
- related meteorological line fields depending on `NWS`

Why it matters:
- these control how frequently forcing is supplied and how it aligns with model time
- for storm forcing, timing mismatch can be as damaging as bad physics choices

### 3. Ramping Family

Examples:
- `NRAMP`
- `DRAMP`
- meteorological ramp additions such as `DRAMPMete`

Why it matters:
- official tips note that meteorological forcing should often be ramped in rather than shocked into the system
- this becomes especially important for hotstart workflows

### 4. Core Numerical Family

Examples:
- `IM`
- `DT`
- `TAU0`
- `H0`
- advection-related switches

Why it matters:
- storm-surge runs increase stress on the numerical setup
- docs and FAQ both point to formulation, timestep, CFL, and `tau0` as stability-relevant

### 5. Bottom And Surface Drag Family

Examples from official storm-surge parameter selections:
- wind drag law
- upper wind drag limit
- minimum bottom drag coefficient
- Manning's n nodal attributes
- surface directional effective roughness length

Why it matters:
- official storm-surge examples show these are central design choices, not minor details
- many of these are driven through nodal attributes rather than just one scalar in `fort.15`

### 6. Tidal And Boundary Family

Examples:
- tidal constituents
- open-boundary forcing setup
- vertical datum choices

Why it matters:
- storm surge is rarely interpreted in isolation from tide or storm tide
- official example tables show tidal constituent selection remains part of many surge workflows

## Input Materials Typically Needed

At the concept level, storm-surge setup usually needs:
- mesh and bathymetry/topography
- boundary definitions
- tidal forcing data, if storm tide rather than surge-only
- meteorological forcing source appropriate to the chosen `NWS`
- nodal attributes for bottom and surface effects
- vertical datum context

This is an inference from the official docs plus examples and parameter tables, not yet a project-specific checklist.

## Output And Evaluation Families

Storm-surge work should be expected to care about:
- water level outputs such as `fort.61/63`
- maximum water level outputs such as `maxele.63`
- velocity outputs such as `fort.62/64` and `maxvel.63`
- meteorological outputs such as global wind/pressure files when forcing is active

Why:
- surge evaluation is not just "did the run finish"
- it needs event-focused outputs and usually max-envelope style products

## Official Example Pathways

Start reading examples in this order:

1. `APES Wind Run (NWS = 3)`
   - simplest wind-forcing bridge from tide-only baseline

2. `Hurricane Isabel Wind Run (NWS = 4)`
   - introduces event-style meteorological forcing without jumping immediately to the most complex current option

3. `Hurricane Katrina (NWS = 20)`
   - strong reference for parametric storm-surge workflow using the currently preferred asymmetric Holland family

4. `Global Storm Tide - Hurricane Katrina (NWS = -14)`
   - later example for large-scale storm tide with gridded forcing

## What To Read First

Read these before selecting actual storm-surge parameters:
- `nws_parameters.rst`
- `fort22.rst`
- `typical_parameter_selections.rst`
- `ramping.rst`
- `ramping_met_forcing_at_hotstart.rst`
- storm-surge example pages

## What We Know Already

Directly from official sources:
- `NWS` controls meteorological forcing type and changes the shape of the met-parameter line
- `NWS=20` is preferred over the deprecated `NWS=19`
- official examples include Katrina and global storm-tide cases
- official storm-surge parameter tables show drag, timestep, `h0`, advection, and tidal constituents are all central concerns

## What We Are Not Deciding Yet

Not decided in this note:
- which `NWS` option is best for your real project
- what `DT`, `TAU0`, or drag values should be used
- what mesh resolution is appropriate
- whether the workflow should be hindcast, hazard, or forecast style

## Next Foundation Steps For Storm Surge

1. Create a storm-surge source subset under `knowledge/methods/adcirc-sources/`
2. Make one note for `NWS` families and one note for storm-surge examples
3. Build a `storm surge requirements checklist` that lists required materials by forcing type
4. Document the local `JMA-MSM -> NWS=13` path explicitly
5. Only after that, begin project-specific parameter reasoning
