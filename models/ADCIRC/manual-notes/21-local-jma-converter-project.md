---
citation_status: source-needed
origin: _staging/from-modeling-wiki/knowledge/methods/adcirc-sources/21-local-jma-converter-project.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# Local JMA-MSM Converter Project

Date: 2026-04-12

Purpose:
- record what the local `E:\numerical_models\adcirc\data\wind\jma` path actually contains
- reduce uncertainty around the `JMA-MSM -> NWS=13` converter branch

## Observed Structure

The path `E:\numerical_models\adcirc\data\wind\jma` contains:
- `build`
- `dist`
- `venv`

This is not a raw meteorological data archive.
It is a converter project and build directory.

## Executable Evidence

Observed files:
- `dist/JMA_MSM_Converter.exe`
- `build/JMA_MSM_Converter/EXE-00.toc`
- `build/JMA_MSM_Converter/xref-JMA_MSM_Converter.html`
- `build/JMA_MSM_Converter/warn-JMA_MSM_Converter.txt`

Implication:
- the local converter was packaged with `PyInstaller`
- the executable is not an opaque black box anymore; build metadata survives locally

## Entry Script Evidence

`xref-JMA_MSM_Converter.html` identifies:
- `jma_msm_gui.py`
- `tkinter`
- `netCDF4`
- `requests`
- `xarray`

`EXE-00.toc` records the packaged source entry as:
- `E:\1125\wide\bc_input\wind\jma_msm_gui.py`

Interpretation:
- the converter is a Python GUI application
- it likely performs download and/or file-read steps, transformation, and NetCDF writing
- the original source path is known from build metadata

Current limitation:
- `E:\1125\wide\bc_input\wind\jma_msm_gui.py` is not present on this machine at the recorded location

## Runtime Stack Evidence

The embedded virtual environment includes:
- `netCDF4`
- `xarray`
- `pandas`
- `requests`
- `dask`
- `PyInstaller`

This strongly suggests:
- NetCDF creation or editing is part of the converter
- tabular and gridded time-series handling is implemented in Python
- the converter may fetch, preprocess, and serialize meteorological data before ADCIRC reads it as `fort.22.nc`

## What This Closes

This note closes these uncertainties:
- the converter exists locally in more than one place
- it is a Python-based custom converter
- it was packaged as a Windows GUI executable
- the GUI is used for raw-data download as well as conversion, not only for local file selection

## What Still Remains Open

- exact expected on-disk raw `JMA-MSM` filenames after download
- exact output schema details beyond the known `NWS13` file role
- exact GUI workflow or batch invocation
- exact variable, unit, and timestamp mapping policy
