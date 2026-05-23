# ADCIRC Topic Map

Date: 2026-04-12

Purpose:
- organize ADCIRC knowledge by topic before deep experiment work begins
- separate "what this topic needs" from "what values we should use"

## Current Stage

This map is for foundation building, not parameter tuning.

For each topic, the immediate goal is to capture:
- what question the topic answers
- what inputs and source materials are required
- what parameter families are involved
- what outputs or diagnostics matter
- which official examples or docs should be read first

## Core Topics

### 1. Baseline Structure

- status: foundation started
- purpose: understand the minimum runnable ADCIRC package
- current notes:
  - `adcirc-baseline-selection.md`
  - `adcirc-baseline-anatomy.md`
  - `adcirc-fort15-checklist-v1.md`

### 2. Preprocessing Foundations

- status: foundation started
- purpose: stabilize the mesh, bathymetry, boundary, and forcing pipeline before project-specific setup
- current notes:
  - `adcirc-preprocessing-foundation.md`
  - `adcirc-mesh-tool-selection.md`
  - `adcirc-bathymetry-input-foundation.md`
  - `adcirc-forcing-input-foundation.md`
  - `adcirc-information-gaps.md`

### 3. Storm Surge

- status: foundation started
- purpose: understand what additional materials and controls are needed beyond tide-only runs
- current notes:
  - `adcirc-storm-surge-foundation.md`
  - `adcirc-storm-surge-nws-families.md`
  - `adcirc-jma-msm-nws13-foundation.md`
  - `adcirc-storm-surge-requirements-checklist.md`

### 4. Tides And Boundary Forcing

- status: partially started through preprocessing notes
- purpose: organize tidal constituents, open-boundary forcing, and tide-only validation logic

### 5. Meteorological Forcing

- status: started
- purpose: understand `NWS` families, `WTIMINC`, `fort.22`, and ramping behavior

### 6. Mesh, Geometry, And Stability

- status: partially started through preprocessing notes
- purpose: connect mesh quality, timestep, CFL, wetting/drying, and `TAU0`

### 7. Output And Diagnostics

- status: not started
- purpose: define which output files matter for baseline verification, storm-surge evaluation, and failure diagnosis

### 8. Validation

- status: not started
- purpose: organize what comparison data and metrics are needed for real projects

### 9. Automation And Operations

- status: deferred
- purpose: place `ADCIRCpy`, `ASGS`, and repeated-run tooling after manual understanding is stable

## Topic Order

Recommended order:
1. baseline structure
2. preprocessing foundations
3. storm surge
4. tides and boundary forcing
5. mesh, geometry, and stability
6. output and diagnostics
7. validation
8. automation and operations

## Rule

Do not convert a topic note into a parameter recommendation note too early.

Foundation notes should answer:
- what this topic touches
- what evidence is needed
- what official sources define it

They should not yet answer:
- the final best parameter values for a specific project
