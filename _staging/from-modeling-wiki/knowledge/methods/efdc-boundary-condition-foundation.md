# EFDC Boundary-Condition Foundation

Date: 2026-04-30

This note captures the current boundary-condition foundation for EFDC coastal and estuarine modeling in this wiki.

Important scope note:
- this note is based on the local EFDC+ manual/KB RAG
- where possible, manual-backed points are separated from practical synthesis
- this note is meant to stabilize calibration vocabulary and setup discipline, not to replace the original manual pages

## Manual-Backed Foundation

The local EFDC+ manual RAG clearly supports the following points.

### 1. Open Boundaries Can Use Time-Series And Harmonic Forcing

EFDC+ open-boundary conditions support a combination of:
- time-series forcing
- harmonic forcing

This matters directly for coastal and estuarine cases where the system may need to represent:
- tides
- river flows
- surge-like water-level response

The theory-side retrieval also confirms that harmonic forcing can be represented through sinusoidal constituent-style expressions.

### 2. Boundary Cells Are Managed As Logical Groups

The EFDC+ Explorer / KB guidance does not frame boundary handling as a pure cell-by-cell manual process.
Instead, it emphasizes grouping cells into physically meaningful sets such as:
- river inflow
- tributary inflow
- one-side open boundary

Why this matters:
- boundary logic should match the physical forcing structure
- calibration gets harder when boundary cells are treated as an unstructured patchwork rather than coherent forcing groups

### 3. River / Freshwater Inflow Is A Distinct Setup Concern

The retrieved guidance explicitly supports preparing river-discharge time series for inflow conditions in coastal/estuarine cases.

Why this matters:
- tidal stage may look reasonable while currents remain biased if freshwater inputs are missing, simplified, or misinterpreted
- this is especially important in estuarine momentum balance and density-sensitive systems

### 4. Group-Level Consistency Matters

The retrieved KB guidance indicates that within EFDC+ boundary grouping, some properties can vary cell by cell while others must remain consistent across the group, especially in the water-quality context.

Even though this note is focused on hydrodynamics, the practical implication is broader:
- boundary grouping is not only a geometry task
- it is also a consistency-management task

## Practical Boundary-Condition Buckets For This Wiki

These are the main boundary-condition buckets future source notes and experiments should log.

### A. Tidal/Open-Boundary Specification

Track:
- time-series versus harmonic representation
- constituent selection where harmonic forcing is used
- phase and amplitude interpretation
- how the seaward/open boundary is segmented

### B. River / Freshwater Inflow

Track:
- discharge time series
- inflow location and grouping
- whether freshwater forcing is omitted, simplified, or explicitly represented

### C. Wind / External Forcing Coupling

Track:
- whether wind forcing is included
- whether surge-like or weather-driven response is important to the calibration window
- whether omitted external forcing could be contaminating current calibration

### D. Density-Relevant Boundary Assumptions

Track:
- whether temperature and salinity forcing are negligible, simplified, or active
- whether density effects were intentionally excluded
- whether that exclusion is still defensible for the case being calibrated

## Calibration-Relevant Consistency Checks

Before tuning parameters, check whether the following are internally consistent:
- open-boundary placement versus the real hydraulic exchange zone
- harmonic constituent phase/amplitude conventions
- river inflow timing and magnitude
- forcing groups versus physical shoreline/channel segmentation
- comparison windows versus forcing windows

## Why Boundary Conditions Matter So Much In EFDC Calibration

In EFDC, it is possible to get a visually reasonable stage response while still driving the wrong momentum field.
That means boundary-condition calibration is not just about matching water level at the open boundary; it is about making sure the domain receives the right hydraulic and external forcing structure.

## Current Working Rule

If stage is acceptable but currents are not, treat boundary-condition interpretation as an early diagnostic layer, not a late fine-tuning layer.

## Manual-Backed Versus Still-Needing-Extraction

### Clearly manual-backed from current retrieval
- open boundaries can use time-series and harmonic forcing
- river inflow/freshwater time series matter in estuarine/coastal setup
- EFDC+ boundary cells are managed through logical grouping concepts

### Still needing more exact extraction
- exact hydrodynamic boundary-control field names for the current EFDC+ version in use
- exact group-level limitations that matter most for hydrodynamics rather than only water quality
- exact recommended patterns for mixed tidal + inflow + wind-driven coastal setups

## Next Expansion Candidates

- targeted source-note extraction for exact EFDC+ boundary control names
- `knowledge/methods/efdc-wetting-drying-foundation.md`
- future `knowledge/playbooks/efdc-boundary-forcing-checklist.md`
