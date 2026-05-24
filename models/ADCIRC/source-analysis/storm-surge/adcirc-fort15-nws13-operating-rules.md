---
title: "ADCIRC fort.15 NWS=13 — local 운영 룰"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/adcirc/src/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-fort15-nws13-operating-rules.md (at commit a9618df^) (modeling-wiki 4월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/raw/source_code/adcirc/src/
---

# ADCIRC fort.15 NWS13 Operating Rules

Date: 2026-04-13
Status: active

Purpose:
- isolate the `fort.15` fields that matter specifically for the local `NWS=13` workflow
- define what should be fixed, what must match the forcing file, and what changes only in exception cases

## Scope

This note covers only the `fort.15` fields tied directly to `NWS=13` operation.

It does not try to restate all of `fort.15`.

## Core Rule

For local meteorological forcing, the `fort.15` forcing block must agree with the generated `fort.22.nc`.

If the file and the `fort.15` block disagree, treat the setup as invalid.

## Primary Fields

### `NWS`

Default rule:
- use `NWS = 13` for ADCIRC-only runs

Local coupled exception:
- use `NWS = 313` when the run is ADCIRC+SWAN coupled and still driven by the same `OWI-NWS13` forcing file

Observed examples:
- `E:\ADCIRC_essential\02_Run\fort.15` uses `13`
- `E:\numerical_models\adcirc\projects\mokpo_case\run\fort.15` uses `313`

Operational rule:
- do not change between `13` and `313` casually
- the value must follow the run type, not personal preference

### `WTIMINC`

Meaning:
- interpolation timestep for meteorological forcing ingestion

Observed local example:
- `mokpo_case` uses `3600 600` in a coupled file as `WTIMINC RSTIMINC`

Operational rule:
- the first value must stay consistent with the forcing cadence you actually generated
- for the current local GUI-generated JMA-MSM branch, hourly forcing means `WTIMINC=3600` is the local default assumption
- do not change `WTIMINC` first when debugging forcing problems; first verify time origin and file structure

### `&owiWindNetcdf`

This namelist is mandatory for local `NWS=13` use.

The fields we must track are:
- `NWS13File`
- `NWS13ColdStartString`
- `NWS13GroupForPowell`
- `NWS13WindMultiplier`

## Namelist Field Rules

### `NWS13File`

Default rule:
- point to the actual forcing file used by the run

Local preference:
- use `fort.22.nc` in the run directory unless there is a clear reason not to

Operational rule:
- if the file is renamed or stored elsewhere, the run directory and `fort.15` must still agree exactly

### `NWS13ColdStartString`

This is the most important field in the namelist.

Default rule:
- it must match the actual meteorological time origin used to build the forcing file

Observed examples:
- `E:\ADCIRC_essential\02_Run\fort.15`: `20030911.000000`
- `mokpo_case`: `20030901.000000`
- local executed GUI run produced `fort.22.nc` with time units:
  - `minutes since 2003-09-01T00:00:00+00:00`

Operational rule:
- treat `NWS13ColdStartString` as a synchronization field, not a cosmetic label
- if the generated `fort.22.nc` starts at `2003-09-01 00:00:00`, then `NWS13ColdStartString` must say `20030901.000000`
- if this field is wrong, fix it before touching `WTIMINC`, drag, or any storm parameters

### `NWS13GroupForPowell`

Observed local examples:
- `1` in `ADCIRC_essential`
- `1` in `mokpo_case`

Operational rule:
- keep this at the local standard value unless a documented forcing-law reason requires otherwise
- do not tune this in ordinary storm-surge setup work

### `NWS13WindMultiplier`

Observed local examples:
- `1.0` in `ADCIRC_essential`
- `1.0` in `mokpo_case`

Operational rule:
- keep at `1.0` by default
- only change as an explicitly documented experiment or calibration step
- if changed, record the reason in the run note because this directly alters forcing magnitude

## Default Local Block

For the normal local single-file workflow, the intended pattern is:

```text
NWS = 13
WTIMINC = 3600
&owiWindNetcdf
NWS13File='fort.22.nc'
NWS13ColdStartString='YYYYMMDD.HHMMSS'
NWS13GroupForPowell=1
NWS13WindMultiplier=1.0
/
```

For coupled ADCIRC+SWAN runs, the same logic applies but `NWS` may be `313` and the line containing `WTIMINC` may also include `RSTIMINC`.

## Freeze Policy

Keep fixed during ordinary setup:
- `NWS`
- `NWS13GroupForPowell`
- `NWS13WindMultiplier`

Must match the generated forcing file:
- `NWS13File`
- `NWS13ColdStartString`
- `WTIMINC`

Change only with explicit run-type change:
- `NWS = 13` versus `NWS = 313`

## First Triage Order For NWS13 Problems

If a run does not behave as expected, check in this order:
1. does `fort.22.nc` exist where `NWS13File` says it does
2. does the file contain `Main/lat/lon/time/U10/V10/PSFC`
3. does the time origin in the NetCDF file match `NWS13ColdStartString`
4. is `WTIMINC` consistent with the forcing cadence
5. only then inspect coupling or drag-related settings

## Current Local Standard

As of `2026-04-13`, the local standard is:
- GUI-based JMA-MSM download and conversion
- `fort.22.nc` as the forcing file name
- hourly source cadence
- single-group `Main` schema
- `NWS13GroupForPowell=1`
- `NWS13WindMultiplier=1.0`

Anything outside that should be documented as an exception, not treated as an invisible default.
