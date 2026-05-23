# ADCIRC Baseline Anatomy

Date: 2026-04-12

## Selected Baseline

- local path: `E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc-testsuite\adcirc\adcirc_quarterannular-2d-netcdf`
- testsuite name: `adcirc_quarterannular-2d-netcdf`

## Why This Anatomy Matters

This note defines the minimum artifact set for the first real ADCIRC work in this wiki.

The goal is not to understand every file in ADCIRC. The goal is to know the minimum baseline package well enough to:
- reproduce a known-good case
- log changes against a stable starting point
- avoid inventing a custom setup too early

## Top-Level Files

- `fort.14`
  - mesh and boundary information
  - this case starts with a quarter annular grid labeled `Quarter Annular Grid - Example 1`
  - header indicates `NE=96`, `NP=63`

- `fort.15`
  - run description, model switches, timestep, runtime, forcing, output settings, harmonic analysis settings, and metadata
  - notable early values from this baseline:
    - `ICS = 1`
    - `IM = 0`
    - `NOLIBF = 1`
    - `NOLIFA = 1`
    - `NWS = 0`
    - `TAU0 = 0.005`
    - `DT = 174.656`
    - `RNDAY = 5.0`
    - `DRAMP = 2.0`
    - `H0 = 1.0`
    - `NBFR = 1`
    - open-boundary constituent includes `M2`

## Control Folder

- `control/fort.51`
- `control/fort.52`
- `control/fort.53`
- `control/fort.54`

Interpretation:
- this folder appears to hold control or expected harmonic-analysis comparison artifacts for the testsuite
- these files should be treated as regression-reference material, not as editable input

## Testsuite Metadata

From `test_list.yaml`:
- `model: adcirc`
- `parallel: false`
- `hotstart: false`
- expected output files include:
  - `fort.61.nc`
  - `fort.62.nc`
  - `fort.63.nc`
  - `fort.64.nc`
  - `maxele.63.nc`

## Minimum Baseline Manifest

For the first manual baseline understanding, track at least:
- `fort.14`
- `fort.15`
- `control/`
- testsuite metadata entry in `test_list.yaml`
- expected output file list

## First Things To Log Against This Baseline

- any edits to `fort.15`
- any change to output mode or expected output files
- any move from serial to parallel variant
- any change from ASCII to NetCDF variant

## Not To Do Yet

- do not fork a custom mesh yet
- do not introduce coupled-wave complexity yet
- do not bring in automation wrappers before the baseline run logic is understood
