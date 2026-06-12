---
title: "adcirc information gaps"
topic: general
canonical_source: self
citation_status: source-needed
classification: local-workflow-notes
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-information-gaps.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC Information Gaps

Date: 2026-04-12

Purpose:
- list the ADCIRC foundation areas where official docs define file semantics but not enough field-ready workflow detail

## Highest-Priority Gaps

### 1. Mesh Tool Decision Rules

We now have stronger local evidence, but several gaps still remain.

We now know:
- `wide6` is the strongest local baseline candidate
- `wide6` points to an `OceanMesh2D` path
- `Gmsh` and `OCSMesh` both exist locally as serious alternative attempts

Observed local evidence:
- `E:\ADCIRC_essential\00_Mesh` already contains `OceanMesh2D-Projection`
- `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6` contains:
  - `OceanMesh2D` and `Gmsh` outputs
  - run outputs
  - validation outputs
  - a detailed local work log

We still do not have:
- a frozen rule for what makes `wide6` reproducible end to end
- a validation gate that distinguishes "wide6 exists" from "wide6 is trustworthy"
- a gap list for translating `OceanMesh2D` behavior into Python or another stack
- a fair revalidation matrix for `Gmsh` versus `OCSMesh`

### 2. Bathymetry Assembly Recipe

We know `fort.14` stores bathymetry, and we know tools exist for DEM integration and subgrid workflows.

Observed local evidence:
- the bundled `OceanMesh2D` setup references `SRTM15+` and `GEBCO` as bathymetry datasets
- this tells us which source families are already close to the local workflow
- the `wide6` branch records `GEBCO + BADA2024`
- the `wide6` work log also records:
  - minimum depth forcing
  - slope limiting
  - smoothing as a stability-critical step

We still do not have:
- the canonical local bathymetry source priority beyond the current `wide6` branch
- datum harmonization policy
- a normalized QC checklist for merged topo-bathy products

### 3. Boundary Construction Practice

We know boundaries are encoded in `fort.14`, and official docs note OceanMesh2D can auto-apply some node strings.

We now know:
- the `wide6` log records auto-classification failure for open boundaries
- the same log records manual GUI classification as necessary

We still do not have:
- the exact repeatable local rule for shoreline versus open-ocean detection
- the rule for river or special structure boundaries
- a formal boundary review and validation checklist

### 4. JMA-MSM To NWS13 Conversion

This is the most important local forcing gap.

We now know:
- `E:\ADCIRC_essential\01_Input_BC\JMA_MSM_Converter.exe` exists
- `E:\ADCIRC_essential\02_Run\fort.22.nc` exists
- `E:\ADCIRC_essential\02_Run\fort.15` is wired to that file through `NWS=13`
- `E:\numerical_models\adcirc\data\wind\jma` is the converter build directory
- the converter is a PyInstaller-packaged Python GUI
- the packaged entry script name is `jma_msm_gui.py`
- the embedded stack includes `netCDF4`, `xarray`, `pandas`, `requests`, and `dask`

We still do not have:
- the exact converter invocation for non-GUI use, if any
- the exact on-disk file naming convention beyond the currently observed `MMDD.nc`
- how overlays are handled, if at all
- whether the GUI also has a batch mode or scriptable backend
- the actual retained source file for `jma_msm_gui.py`

But we now have partial closure on the mapping question:
- notebook evidence in `E:\numerical_models\adcirc\tools\utilities\nc2fort22.ipynb` explicitly maps `psea`, `u`, and `v` into `PSFC`, `U10`, and `V10`
- the same notebook converts pressure from `Pa` to `mb`
- the executed `E:\AI_ENV\fort.22.nc` confirms the resulting variable set and units in practice
- this means the remaining gap is narrower: we still need the trusted production branch, not the basic schema logic

We also have partial closure on the raw-input question:
- the GUI shows that data are downloaded from the RISH Kyoto MSM-S archive
- the GUI takes start date, end date, and save folder directly from the user
- an executed run created `E:\AI_ENV\2003\0901.nc`, `0902.nc`, and `0903.nc`
- this means the missing piece is no longer the upstream source itself
- the remaining piece is whether this naming rule generalizes beyond the observed run and how the intermediate merge stage is handled in production

We also have partial closure on the output-schema question:
- the executed output file is a valid `CF-1.6 OWI-NWS13` NetCDF by its own metadata
- it contains a `Main` group with `lat`, `lon`, `time`, `U10`, `V10`, and `PSFC`
- this matches the base schema seen in the official `adcirc-testsuite` katrina example
- the remaining distinction is single-group versus overlay-group usage

### 5. Data Acquisition Pipeline

We know ADCIRC exposes `MetGet` and several forcing families.
We do not yet know:
- whether local forcing acquisition is already scripted
- whether forcing files are archived reproducibly
- whether input provenance is recorded consistently

### 6. FORTRAN Helper Utility Verification

We now know:
- several local FORTRAN utilities exist for interpolation, DEM transfer, boundary extraction, and QC
- they do not currently appear in the active `wide6` script chain
- some named utilities in `grid` are broken local artifacts rather than working source files
- a usable subset has now been compiled successfully on the current machine

We still do not have:
- task-level validation on real local ADCIRC artifacts
- a rule for which helper should be preferred for bathymetry transfer, boundary support, or mesh QC

## Rule For Handling Gaps

Do not fill these gaps with guessed best practices.

Each gap should be closed by one of:
- official ADCIRC documentation
- local existing scripts or notebooks
- local team workflow evidence
- executed and archived validation runs
