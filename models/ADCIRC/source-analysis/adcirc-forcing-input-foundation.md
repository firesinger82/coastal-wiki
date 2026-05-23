---
title: "adcirc forcing input foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-forcing-input-foundation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC Forcing Input Foundation

Date: 2026-04-12

Purpose:
- organize how external forcing enters ADCIRC before project-specific setup begins
- separate lateral boundary forcing from meteorological forcing

## Why This Matters

When people say "forcing" in ADCIRC, they often mix together:
- open-boundary water-level forcing
- flux or river forcing
- meteorological forcing

The official docs split these across different files and mechanisms.
The knowledge system should do the same.

## Boundary Forcing

### Boundary Geometry

The locations and types of open and flux boundaries are defined in `fort.14`.

Official docs state:
- open boundaries are where water surface elevation is specified
- flux boundaries are where normal flux is specified

### Boundary Time Information

Boundary values are not all stored in the same place.

Official docs indicate:
- periodic open-boundary elevation forcing is defined in `fort.15`
- non-periodic open-boundary elevation forcing is defined in `fort.19`
- periodic flux forcing is defined in `fort.15`
- non-periodic flux forcing is defined in `fort.20`

This means boundary forcing is partly a mesh problem and partly a runtime forcing problem.

## Meteorological Forcing

### Official Structure

Meteorological forcing is selected with `NWS` in `fort.15`.
The required input family then depends on the `NWS` value.

The docs group meteorological forcing into several families:
- direct node-based input
- gridded meteorological data
- parametric hurricane models
- data-assimilated hurricane products
- coupled-wave variants

### Core Selection Variables

Before choosing values, the method choice must answer:
- where does the source data come from?
- is the source already in an ADCIRC-readable format?
- does the source cover the whole domain and time window?
- what conversion step is needed?
- what does `WTIMINC` mean for that forcing family?

### Official Constraints Repeated Across Docs

- the forcing domain must cover the ADCIRC mesh when the format requires gridded coverage
- time synchronization matters
- file format and units must match ADCIRC expectations
- `WTIMINC` is required for many `ABS(NWS) > 1` forcing types

## Local Standard Branch

For local storm-surge work, the dominant path is:
- source meteorology: `JMA-MSM`
- ADCIRC interface: `NWS=13`

Official fact:
- `NWS=13` is OWI NetCDF gridded wind and pressure
- the documented schema uses `U10`, `V10`, `PSFC`, `lat`, `lon`, and `time`
- `&owiWindNetcdf` in `fort.15` controls file name and cold-start alignment

Local inference:
- `JMA-MSM` is not read natively by ADCIRC as `JMA-MSM`
- therefore a conversion or packaging layer is part of the real workflow

That conversion layer is part of preprocessing knowledge and should be documented as such.

Observed local evidence from `E:\ADCIRC_essential`:
- `01_Input_BC/JMA_MSM_Converter.exe` exists
- `02_Run/fort.22.nc` exists
- `02_Run/fort.15` contains `&owiWindNetcdf` with:
  - `NWS13File='fort.22.nc'`
  - `NWS13ColdStartString='20030911.000000'`
  - `NWS13GroupForPowell=1`
  - `NWS13WindMultiplier=1.0`

This is enough to state that the local conversion branch is real, not hypothetical:
- `JMA-MSM`
- local converter step
- `fort.22.nc`
- ADCIRC `NWS=13`

Observed local evidence from `E:\numerical_models\adcirc\data\wind\jma`:
- this path is a converter project and build directory, not a raw meteorology archive
- it contains `build`, `dist`, and `venv`
- `dist/JMA_MSM_Converter.exe` exists
- `build/JMA_MSM_Converter/EXE-00.toc` records the packaged source entry as `E:\1125\wide\bc_input\wind\jma_msm_gui.py`
- `build/JMA_MSM_Converter/xref-JMA_MSM_Converter.html` identifies the app as a `tkinter` GUI and shows imports for `netCDF4`, `xarray`, and `requests`
- the embedded runtime environment includes `netCDF4`, `xarray`, `pandas`, `requests`, `dask`, and `PyInstaller`

This narrows the workflow interpretation further:
- the local `JMA-MSM -> NWS13` branch is backed by a custom Python converter
- the converter was packaged as a Windows GUI executable
- the conversion likely includes NetCDF writing and data wrangling in Python
- the original source path is known from build metadata, but the source file is not currently present at that path on this machine

Observed GUI evidence from the running converter:
- the window title is `JMA MSM 다운로드 & fort.22.nc 변환기`
- the GUI exposes at least two tabs:
  - `1. 다운로드`
  - `2. 변환 한번에 실행`
- the download tab asks for:
  - start date
  - end date
  - save folder
- the displayed upstream source is:
  - `RISH Kyoto University`
  - `http://database.rish.kyoto-u.ac.jp/arch/jmadata/data/gpv/netcdf/MSM-S/`
- the displayed variables include:
  - `u`
  - `v`
  - `psea`
  - `temp`
  - `rh`
- the displayed temporal resolution is:
  - `1시간`

Observed additional GUI evidence from the other tabs:
- the conversion tab accepts:
  - an input NC file
  - simulation start time
  - output file path
- the integrated run tab exposes:
  - `전체 실행 (다운로드 -> 변환)`
  - quick start and end date fields

This changes the workflow interpretation again:
- the converter is not only a file reformatter
- it also acts as a raw-data acquisition client
- the raw input location may be ephemeral and chosen by the user at runtime through the save-folder field
- the real contract is therefore:
  - date range
  - download source
  - saved raw or intermediate NetCDF files
  - conversion into `fort.22.nc`

Observed local evidence from `E:\numerical_models\adcirc\tools\utilities`:
- `JMA_MSM.ipynb` exists
- `merge_nc.ipynb` exists
- `nc2fort22.ipynb` exists
- the notebook evidence shows an explicit two-stage workflow:
  - multiple source NetCDF files matching `09*.nc` are merged with `xarray.open_mfdataset(...)`
  - the merged output is written as `combined.nc`
  - `combined.nc` is then converted to `fort.22.nc`
- `nc2fort22.ipynb` maps:
  - `psea -> PSFC`
  - `u -> U10`
  - `v -> V10`
- the same notebook also shows:
  - pressure is converted from `Pa` to `mb`
  - output variable units are set to ADCIRC-expected `mb` and `m s-1`

This is the strongest local forcing evidence so far because it shows:
- a retained notebook-based workflow, not only a packaged executable
- an intermediate artifact `combined.nc`
- an explicit local variable and unit mapping toward `NWS=13`

Combined with the GUI evidence, the current best local forcing chain is:
- choose a date range in the GUI
- download hourly JMA-MSM NetCDF data from the RISH Kyoto archive into a user-selected folder
- merge source files into `combined.nc` or `merged.nc`
- convert local variables into ADCIRC `NWS=13` fields
- write `fort.22.nc`

Observed execution evidence from `2026-04-13`:
- the save folder used in the GUI was `E:\AI_ENV`
- the downloader created:
  - `E:\AI_ENV\2003\0901.nc`
  - `E:\AI_ENV\2003\0902.nc`
  - `E:\AI_ENV\2003\0903.nc`
- the converter created:
  - `E:\AI_ENV\fort.22.nc`

This is the first full local chain confirmed by execution:
- date range: `2003-09-01` to `2003-09-03`
- raw download folder: `E:\AI_ENV\2003`
- raw filename pattern: `MMDD.nc`
- final output: `E:\AI_ENV\fort.22.nc`

Observed structural evidence from the generated `E:\AI_ENV\fort.22.nc`:
- root attributes include:
  - `group_order=Main`
  - `institution=Oceanweather Inc. (OWI)`
  - `conventions=CF-1.6 OWI-NWS13`
  - `source=JMA MSM (RISH Kyoto)`
- the file contains one group: `Main`
- the `Main` group contains:
  - dimensions: `time=72`, `yi=252`, `xi=240`
  - variables: `lat`, `lon`, `time`, `U10`, `V10`, `PSFC`
- the time variable uses:
  - `minutes since 2003-09-01T00:00:00+00:00`
  - `proleptic_gregorian`
- the first decoded timestamps are hourly from `2003-09-01 00:00:00`

Comparison against the official local testsuite file:
- the official `adcirc_katrina-2d-nws13/fort.22.nc` uses the same core variable set and units inside each group
- the main difference is grouping strategy:
  - generated local file: one `Main` group
  - official katrina example: `Main`, `0_15`, and `0_05`

Current interpretation:
- the generated local file matches the base single-grid `OWI-NWS13` schema
- the official katrina example demonstrates an overlay-group variant of the same schema
- for a standard local `NWS=13` workflow, the generated file looks structurally compatible
- for overlay-group workflows, more than one group may be required

## Tooling Relevant To Forcing Ingestion

The official tools page surfaces `MetGet` as a meteorological forcing acquisition and development system.

Implication:
- forcing preparation can be a data-engineering problem of its own
- acquisition, formatting, and blending may need to be treated as a separate pipeline before ADCIRC ever reads the files

This does not automatically mean `MetGet` should be adopted now.
It means the workflow should be evaluated against a formal ingestion path rather than ad hoc file preparation.

## What We Should Record For Every Forcing Method

### Boundary Forcing

- boundary type
- source dataset
- periodic or non-periodic
- source datum and units
- file path and file family

Observed local evidence:
- `E:\ADCIRC_essential\01_Input_BC\update_tidal_bc*.m` scripts update tidal open-boundary forcing
- these scripts read boundary nodes from `fort.14`
- they write constituent data back into `fort.15`
- at least one local workflow uses `NAO99Jb` plus `tide_fac_utide`

### Meteorological Forcing

- `NWS` family
- source dataset
- raw cadence
- converted cadence
- spatial coverage
- units and variable mapping
- conversion script or tool
- cold-start and hotstart alignment policy

Local record to preserve:
- executable or script name for conversion
- build/project directory for the converter
- notebook path and intermediate-file workflow if that is the real editable branch
- exact raw download source URL
- date-range selection policy
- exact input directory or file pattern for downloaded `JMA-MSM`
- exact output file name and location for `fort.22.nc`
- intermediate merged file names such as `combined.nc`
- whether the converter emits single-grid or overlay-group NWS13 files
- whether the GUI wraps a reusable CLI or only an interactive workflow

Current local answer to part of that record:
- downloaded files were saved under `E:\AI_ENV\2003`
- the observed raw filenames follow `MMDD.nc`
- the observed output file path was `E:\AI_ENV\fort.22.nc`
- the observed generated file is a single-group `OWI-NWS13` NetCDF with `Main/lat/lon/time/U10/V10/PSFC`

## Current Decision Boundary

At this stage:
- keep `JMA-MSM -> NWS=13` as the primary local meteorological branch
- do not yet generalize that into a universal ADCIRC best practice
- do not jump to `WTIMINC` tuning before the source-to-file path is documented
