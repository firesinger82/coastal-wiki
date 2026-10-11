---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/18-nws13-schema-and-local-jma-msm-branch.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
last_source_check: 2026-10-11 (recovery 재판독 대조)
---
# NWS13 Schema And Local JMA-MSM Branch

## Metadata

- date: 2026-04-12
- title: official NWS13 schema and the local JMA-MSM branch
- source type: manual
- authors: ADCIRC development team plus local workflow statement
- year: active documentation site
- link: https://adcirc.github.io/adcirc/user_guide/model_configuration/meteorological_forcing/nws13.html ; https://adcirc.github.io/adcirc/technical_reference/input_files/fort22.html

## Why This Matters

This is the key bridge between official ADCIRC meteorological schema and the actual local storm-surge workflow.

## Core Claims

- official ADCIRC docs define `NWS=13` as OWI NetCDF gridded wind and pressure
- the documented schema includes `U10`, `V10`, `PSFC`, `lat`, `lon`, and `time`
- NWS=13 reader는 `src/owiwind_netcdf.F`이다. (`src/owiwind_netcdf.F:262` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)
- NWS=13은 전역 속성 `group_order`로 그룹 순서를 읽는다. (`src/owiwind_netcdf.F:265` `call check_err(NF90_GET_ATT(NC_ID,NF90_GLOBAL,"group_order",GroupOrder))`)
- 각 그룹의 차원은 `time`, `yi`, `xi`이다. (`src/owiwind_netcdf.F:346` `call check_err(NF90_INQ_DIMID(NC_IDG,"time",NC_DIM))`; `src/owiwind_netcdf.F:367` `call check_err(NF90_INQ_DIMID(NC_IDG,"xi",NC_DIM))`; `src/owiwind_netcdf.F:369` `call check_err(NF90_INQ_DIMID(NC_IDG,"yi",NC_DIM))`)
- 각 그룹은 `U10`, `V10`, `PSFC`, `lon`, `lat` 변수를 사용한다. (`src/owiwind_netcdf.F:381` `call check_err(NF90_INQ_VARID(NC_IDG,"lon",NC_VAR))`; `src/owiwind_netcdf.F:384` `call check_err(NF90_INQ_VARID(NC_IDG,"lat",NC_VAR))`; `src/owiwind_netcdf.F:683` `call check_err(NF90_INQ_VARID(NC_IDG,"U10",NC_VAR))`; `src/owiwind_netcdf.F:702` `call check_err(NF90_INQ_VARID(NC_IDG,"V10",NC_VAR))`; `src/owiwind_netcdf.F:721` `call check_err(NF90_INQ_VARID(NC_IDG,"PSFC",NC_VAR))`)
- 날짜 파서는 time units 문자열의 앞 14자를 건너뛴다. (`src/owiwind_netcdf.F:321` `READ(UNIT=TimeUnits,FMT='(14X,I4,1X,I2,1X,I2,1X,I2,1X,I2,1X,I2)')`; `src/owiwind_netcdf.F:322` `&    Year,Month,Day,Hour,Minute,Second`)
- 문서 설명의 `minutes from`과 예제의 `minutes since`는 다르다. (`docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:97` `-  *time* (time), Datetime-number with units of “minutes from YYYY-mm-dd`; `docs/user_guide/model_configuration/meteorological_forcing/nws13.rst:129` `|              time:units = "minutes since 1990-01-01T01:00:00" ;`)
- 코드는 NWS13File에 입력 디렉터리 접두사를 붙이지 않는다. (`src/owiwind_netcdf.F:262` `call check_err(NF90_OPEN(TRIM(ADJUSTL(NWS13File)),NF90_NOWRITE,NC_ID))`)
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
