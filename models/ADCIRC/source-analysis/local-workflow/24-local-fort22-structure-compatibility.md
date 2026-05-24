---
citation_status: source-needed
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/24-local-fort22-structure-compatibility.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: local-workflow-notes
source_id: models/ADCIRC
notes: "local user workflow (E:\\ paths) — not external doc catalog. source-needed retained; verified status requires raw file presence audit. Future home may be experience/ or source-analysis/."
---
# Local fort.22 Structure Compatibility

Date: 2026-04-13

Purpose:
- record the actual structure of the generated local `fort.22.nc`
- compare it against the official local `adcirc-testsuite` `NWS=13` example

## Generated Local File

Observed file:
- `E:\AI_ENV\fort.22.nc`

Observed root attributes:
- `group_order=Main`
- `institution=Oceanweather Inc. (OWI)`
- `conventions=CF-1.6 OWI-NWS13`
- `source=JMA MSM (RISH Kyoto)`

Observed group structure:
- one group: `Main`

Observed `Main` dimensions:
- `time=72`
- `yi=252`
- `xi=240`

Observed `Main` variables:
- `lat(yi,xi)` with `degrees_north`
- `lon(yi,xi)` with `degrees_east`
- `time(time)` with `minutes since 2003-09-01T00:00:00+00:00`
- `U10(time,yi,xi)` with `m s-1`
- `V10(time,yi,xi)` with `m s-1`
- `PSFC(time,yi,xi)` with `mb`

Observed time behavior:
- `calendar=proleptic_gregorian`
- decoded timestamps start at `2003-09-01 00:00:00`
- the first five steps are hourly

## Official Comparison File

Compared against:
- `E:\AI_ENV\modeling-wiki\raw\code\adcirc\adcirc-testsuite\adcirc\adcirc_katrina-2d-nws13\fort.22.nc`

Observed comparison result:
- the official file uses the same core variable set and units inside each group:
  - `lat`
  - `lon`
  - `time`
  - `U10`
  - `V10`
  - `PSFC`
- the official file includes multiple groups:
  - `Main`
  - `0_15`
  - `0_05`

## Interpretation

This supports a practical distinction:
- single-group `OWI-NWS13`: one `Main` group only
- overlay-group `OWI-NWS13`: multiple named groups with the same internal schema

Current local conclusion:
- the generated `E:\AI_ENV\fort.22.nc` is structurally consistent with the base schema used in the official testsuite
- it appears suitable for standard local `NWS=13` use
- it does not, by itself, demonstrate overlay-group generation

## What This Closes

This note closes these uncertainties:
- the generated local file is not just named like `fort.22.nc`; it follows an `OWI-NWS13` group-and-variable schema
- the variable names and units match the official example pattern

## What Still Remains Open

- whether local production cases ever need overlay groups instead of a single `Main` group
- whether the GUI or notebook workflow can generate those extra groups when needed
