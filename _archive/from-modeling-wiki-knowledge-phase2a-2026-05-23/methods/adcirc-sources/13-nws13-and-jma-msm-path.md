# NWS13 And JMA-MSM Path

## Metadata

- date: 2026-04-12
- title: NWS13 path with local JMA-MSM workflow
- source type: manual
- authors: ADCIRC docs plus local workflow statement
- year: active docs plus current local practice
- link: local synthesis from `nws13.rst`, `fort22.rst`, testsuite `adcirc_katrina-2d-nws13`
- local path: E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc-testsuite\adcirc\adcirc_katrina-2d-nws13

## Why This Matters

This is the first note that connects official ADCIRC NWS13 requirements to the actual local forcing workflow used most often.

## Core Claims

- official docs define `NWS=13` as OWI NetCDF gridded wind and pressure
- testsuite confirms a working `NWS=13` case with `fort.22.nc` and `&owiWindNetcdf`
- local practice uses `JMA-MSM` as the upstream meteorological source
- therefore a conversion or packaging step must exist between `JMA-MSM` and ADCIRC-readable `NWS=13`

## Practical Value

- method details: identifies the real forcing path we should organize around
- implementation detail: clarifies that the conversion layer is a first-class artifact
- validation detail: tells us where schema and timing mismatches may originate
- limitations: the exact local conversion procedure is not documented yet

## Relevance Tags

- solver: ADCIRC
- physics: storm surge
- numerics: meteorological forcing
- diagnostics: schema and timing consistency
- failure mode: forcing mismatch

## Transferability

High for local storm-surge work using gridded meteorological products converted into ADCIRC forcing.

## Extraction Targets

- document the local JMA-MSM to NWS13 conversion path
- document the `fort.15` namelist policy for `NWS=13`
- document the archive policy for `fort.22.nc`

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
