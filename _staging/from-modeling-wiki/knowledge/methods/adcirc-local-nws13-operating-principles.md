# ADCIRC Local NWS13 Operating Principles

Date: 2026-04-13
Status: active

Purpose:
- define the local operating rules for `JMA-MSM -> NWS=13`
- separate what is standard, what is allowed, and what is still exceptional

## Core Rule

The default local meteorological forcing path is:
- `JMA-MSM -> OWI-NWS13 NetCDF -> ADCIRC NWS=13`

This is now a confirmed local workflow, not just a planning assumption.

## Standard Operating Mode

Until a project explicitly says otherwise, the standard mode is:
- source acquisition through the local `JMA MSM 다운로드 & fort.22.nc 변환기`
- hourly JMA-MSM NetCDF download from the RISH Kyoto MSM-S archive
- raw files stored under a year directory inside the chosen save folder
- single output file named `fort.22.nc`
- single-group `OWI-NWS13` structure with one `Main` group

Observed example:
- raw files: `E:\AI_ENV\2003\0901.nc`, `0902.nc`, `0903.nc`
- output: `E:\AI_ENV\fort.22.nc`

## Required Structural Conditions

For a local file to be treated as valid `NWS=13` input, it must have:
- `CF-1.6 OWI-NWS13` metadata
- a `Main` group at minimum
- variables:
  - `lat`
  - `lon`
  - `time`
  - `U10`
  - `V10`
  - `PSFC`
- units:
  - `U10`, `V10`: `m s-1`
  - `PSFC`: `mb`
- a time axis that decodes correctly against the intended cold-start

## Operational Preference Order

Use this preference order:
1. GUI one-shot or staged workflow for normal local forcing creation
2. notebook workflow for inspection, debugging, schema verification, or custom edits
3. manual NetCDF surgery only when both of the above fail

Reason:
- the GUI is the confirmed acquisition path
- the notebooks preserve editable logic
- direct file editing has the weakest reproducibility

## Single-Group Versus Overlay Rule

Current default:
- single-group `Main` only

Current exception:
- overlay groups are allowed only when a project proves they are needed

Reason:
- the generated local file is currently confirmed only for the single-group case
- the official testsuite shows overlay-capable examples, but local generation of those groups is not yet confirmed

So the local rule is:
- do not design around overlays by default
- escalate to overlays only when the forcing domain, resolution strategy, or production case requires it

## Cold-Start Alignment Rule

The forcing file and the ADCIRC run must agree on:
- simulation start date and hour
- time origin in the NetCDF file
- `NWS13ColdStartString` in `fort.15`

If these are not aligned, treat the forcing as invalid until proven otherwise.

## File Placement Rule

Default local placement:
- raw downloads under a year directory beneath the chosen save folder
- final `fort.22.nc` in the chosen working directory or run directory

Preferred run practice:
- copy or generate the final `fort.22.nc` directly into the run directory that owns the corresponding `fort.15`

Avoid:
- treating desktop or ad hoc temp directories as long-term forcing storage

## Archive Rule

For each retained forcing set, preserve at minimum:
- date range used for download
- save folder used
- raw file naming pattern observed
- final `fort.22.nc`
- matching `fort.15` cold-start fields
- short provenance note stating source archive and generation date

## What Is Not Yet Standard

These are not part of the default operating rule yet:
- overlay-group `NWS=13` generation
- batch or CLI invocation of the converter
- non-GUI production generation
- alternative source archives for the same local workflow

## Decision Boundary

If a new project can use:
- hourly JMA-MSM
- one forcing grid
- one `fort.22.nc`
- one matching cold start

then it should stay on the default local `NWS=13` path.

If a project needs:
- overlays
- unusual timesteps
- nonstandard source products
- full automation without GUI

then it leaves the default operating mode and must be documented as an exception.
