---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/19-local-adcirc-essential-workflow.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: P2 catalog (audit deferred to per-note verification)
---
# Local ADCIRC Essential Workflow

## Metadata

- date: 2026-04-12
- title: local preprocessing and run structure under E:\\ADCIRC_essential
- source type: local workflow
- authors: local workspace artifacts
- year: active local project state
- link: local folder structure and scripts
- local path: E:\ADCIRC_essential

## Why This Matters

This is the first concrete local evidence that the ADCIRC foundation workflow is not just conceptual.

## Core Claims

- the local workflow is explicitly separated into:
  - `00_Mesh`
  - `01_Input_BC`
  - `02_Run`
  - `03_Validation`
  - `04_ETC`
- `00_Mesh` contains `OceanMesh2D-Projection` and a local `fort.14`
- `01_Input_BC` contains tidal boundary update scripts and `JMA_MSM_Converter.exe`
- `02_Run` contains a runnable ADCIRC input set including `fort.13`, `fort.14`, `fort.15`, `fort.22.nc`, and `run.bat`

## Practical Value

- method details: confirms the local team is already organizing the workflow as mesh, boundary/forcing input, and run stages
- implementation detail: strongly suggests `OceanMesh2D` is the actual local mesh branch
- validation detail: confirms `fort.22.nc` is already materialized in the run stage
- limitations: the exact CLI or UI usage of `JMA_MSM_Converter.exe` is still undocumented

## Relevance Tags

- solver: ADCIRC
- physics: preprocessing and run control
- numerics: workflow staging
- diagnostics: local evidence
- failure mode: undocumented local procedure

## Transferability

High for the local ADCIRC knowledge system.

## Extraction Targets

- write down the exact purpose of each top-level directory
- document the handoff objects between mesh, boundary, forcing, and run phases

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
