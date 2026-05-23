# ADCIRC JMA-MSM NWS13 Foundation

Date: 2026-04-12

Purpose:
- capture the actual local forcing workflow used most often
- separate official ADCIRC facts from local operational assumptions

## Workflow Statement

Current dominant workflow:
- source meteorology: `JMA-MSM`
- ADCIRC forcing interface: `NWS=13`

## Official Facts

From ADCIRC docs:
- `NWS=13` is the OWI NetCDF format for gridded wind and pressure
- `fort.22.nc` is the default file name unless overridden
- `&owiWindNetcdf` in `fort.15` includes:
  - `NWS13ColdStartString`
  - `NWS13File`
  - `NWS13WindMultiplier`
  - `NWS13GroupForPowell`
- `WTIMINC` is the grid-to-mesh interpolation timestep in seconds
- `NWS=13` supports overlays, moving grids, irregular timesteps, and curvilinear grids

## Local Inference

Because the docs define the ADCIRC-readable schema rather than a native JMA-MSM reader, the local workflow almost certainly depends on a conversion or packaging step:
- raw or intermediate `JMA-MSM`
- transformed into OWI-NWS13-compliant NetCDF
- passed to ADCIRC as `fort.22.nc` or another file name through `NWS13File`

This is an inference based on the docs plus the user’s stated workflow.

## What Must Be True For This Workflow To Work

### Source Layer

- JMA-MSM wind and pressure fields exist for the simulation window
- the temporal coverage spans the full ADCIRC run period needed for the forcing
- the spatial domain covers the ADCIRC mesh after conversion

### Conversion Layer

- output file conforms to the OWI-NWS13 convention
- required variables are mapped correctly:
  - `U10`
  - `V10`
  - `PSFC`
  - `lat`
  - `lon`
  - `time`
- time units are interpretable by ADCIRC
- pressure units are correct for the `NWS=13` convention
- overlay rank/group metadata is valid if multiple grids are used

### ADCIRC Interface Layer

- `NWS = 13`
- `WTIMINC` is chosen appropriately
- `&owiWindNetcdf` exists in `fort.15`
- `NWS13ColdStartString` matches the actual cold-start time
- `NWS13File` points to the forcing file if not using the default `fort.22.nc`

## Risks Specific To This Workflow

- source coverage does not fully span the simulation or hotstart interval
- converted NetCDF schema is close to OWI-NWS13 but not fully compliant
- `NWS13ColdStartString` does not align with the simulation start
- `WTIMINC` is inconsistent with source cadence or chosen interpolation strategy
- mesh is not fully covered by the forcing grid
- meteorological forcing is introduced too abruptly when hotstarting

## Existing Official Example We Can Learn From

The testsuite includes:
- `adcirc_katrina-2d-nws13`
- `adcirc_katrina-2d-nws13-parallel`

Observed local artifact structure from the testsuite:
- `fort.14`
- `fort.15`
- `fort.22.nc`
- `control/`

The testsuite `fort.15` also shows:
- `NWS = 13`
- `&owiWindNetcdf`
- `NWS13ColdStartString='20050819.000000'`
- `NOUTGW` configured for met output

## What This Means For Our Knowledge System

We should track storm-surge work in three linked notes:
- source-data note
  - example: JMA-MSM acquisition and characteristics
- conversion note
  - example: JMA-MSM to OWI-NWS13 mapping
- ADCIRC forcing note
  - example: `fort.15` and runtime settings for `NWS=13`

## Missing Local Knowledge

Still missing:
- the exact local conversion method from JMA-MSM into OWI-NWS13 NetCDF
- the actual variable mapping and unit handling used in your workflow
- your preferred hotstart strategy for storm-surge runs
- your preferred evaluation outputs and archive policy

## Next Step

Create a concrete checklist for `JMA-MSM + NWS=13` requirements and then document the local conversion method when you are ready.

## Current Status

The workflow has now advanced beyond a pure foundation note.

Use the local rule document for operational decisions:
- `adcirc-local-nws13-operating-principles.md`
