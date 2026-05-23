# ADCIRC Preprocessing Foundation Spec

Date: 2026-04-12
Status: active

## Goal

Stabilize the preprocessing knowledge required before project-specific ADCIRC experiments, with first priority on:
- mesh generation tool selection
- bathymetry and topography input path
- external forcing input path

## Scope

In scope:
- official ADCIRC documentation on mesh, bathymetry, boundaries, and forcing
- local workflow framing for `JMA-MSM -> NWS=13`
- source notes, method notes, and gap tracking

Out of scope for this phase:
- final parameter tuning
- case-specific `fort.15` recommendations
- production automation rollout
- plugin or MCP expansion without a clear bottleneck

## Current Decisions

- active model: `ADCIRC`
- current local meteorological branch: `JMA-MSM -> NWS=13`
- preprocessing is now higher priority than experiment design
- mesh-tool shortlist should stay focused on `SMS` and `OceanMesh2D`
- current local evidence leans toward `OceanMesh2D` as the active mesh branch
- current local evidence confirms a real converter-backed `JMA-MSM -> fort.22.nc -> NWS=13` path
- current local evidence also shows that the converter is a PyInstaller-built Python GUI project, not just an opaque executable
- current local evidence now also includes notebook-based conversion logic under `E:\numerical_models\adcirc\tools\utilities`
- current local evidence now includes one executed end-to-end run that produced a single-group `OWI-NWS13` `fort.22.nc`

## Deliverables

- `adcirc-preprocessing-foundation.md`
- `adcirc-mesh-tool-selection.md`
- `adcirc-bathymetry-input-foundation.md`
- `adcirc-forcing-input-foundation.md`
- `adcirc-information-gaps.md`
- preprocessing-related source notes under `knowledge/methods/adcirc-sources/`

## Evidence Base

Primary evidence should come from:
- official ADCIRC docs and technical reference
- cloned ADCIRC repository documentation
- cloned `adcirc-testsuite` examples
- local workflow evidence when available

## MCP And Plugin Policy

No new MCP server or plugin is required for this phase yet.

Reason:
- the bottleneck is not tool access
- the bottleneck is workflow definition and evidence capture

Revisit only if:
- PDF ingestion becomes frequent
- local vault browsing becomes the main interface
- forcing conversion analysis needs a specialized external tool

## Next Closure Targets

1. record the local mesh-tool decision basis
2. record the local bathymetry source and datum policy
3. record the exact `JMA-MSM -> NWS13` conversion path
4. define minimal QC checks for mesh, bathymetry, and forcing artifacts
