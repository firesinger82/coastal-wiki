# ADCIRC fort.15 Checklist V1

Date: 2026-04-12

Purpose:
- read `fort.15` in a disciplined order
- decide what must stay frozen in the baseline
- decide what is safe to vary in the first controlled experiment

This checklist is designed around the baseline case:
- `raw/code/adcirc/adcirc-testsuite/adcirc/adcirc_quarterannular-2d-netcdf/fort.15`

## Read Order

1. identity and execution context
2. formulation and physics switches
3. stability and time-stepping controls
4. forcing and boundary specification
5. outputs and analysis settings
6. restart and solver controls

## 1. Identity And Execution Context

Check:
- run description string
- run identification string
- `NFOVER`
- `NABOUT`
- `NSCREEN`
- `IHOT`

Why:
- these tell you whether the run is a cold start or hot start
- they also control how much runtime information is exposed on screen

Baseline interpretation:
- `IHOT = 0` means cold start

Touch policy:
- green: run description text
- yellow: `NSCREEN`
- red: `IHOT`, unless the experiment is explicitly about hotstart behavior

## 2. Formulation And Physics Switches

Check:
- `ICS`
- `IM`
- `NOLIBF`
- `NOLIFA`
- `NOLICA`
- `NOLICAT`
- `NWP`
- `NCOR`

Why:
- these determine the model formulation, coordinate system, wetting/drying behavior, and whether spatially varying fields come from nodal attributes

Baseline interpretation:
- `ICS = 1`
- `IM = 0`
- `NOLIBF = 1`
- `NOLIFA = 1`
- `NOLICA = 1`
- `NOLICAT = 1`
- `NWP = 0`
- `NCOR = 0`

Touch policy:
- red: `ICS`, `IM`, `NOLIFA`, `NOLICA`, `NOLICAT`
- yellow: `NOLIBF`
- red: `NWP`, `NCOR` unless the whole experiment is about those features

Notes:
- local docs indicate `IM` is a major formulation switch and common 2D barotropic values include `IM=0`
- `NOLIFA` affects finite-amplitude treatment and interacts with `H0`

## 3. Stability And Time-Stepping Controls

Check:
- `G`
- `TAU0`
- `DT`
- `STATIM`
- `REFTIM`
- `RNDAY`
- `DRAMP`
- GWCE time weighting factors
- `H0`

Why:
- these are the first parameters to inspect when a run is unstable or behaving strangely

Baseline interpretation:
- `TAU0 = 0.005`
- `DT = 174.656`
- `RNDAY = 5.0`
- `DRAMP = 2.0`
- `H0 = 1.0`

Touch policy:
- green: `RNDAY`, if only shortening a test run for faster turnaround
- yellow: `DRAMP`
- yellow: `H0`
- red for baseline preservation, but first experiment candidate: `DT`
- red for baseline preservation, later stability candidate: `TAU0`

Pre-run questions:
- is the chosen `DT` consistent with the mesh and expected CFL behavior?
- does `TAU0` stay within a sensible range for this case?
- does `H0` make sense given `NOLIFA` and drying behavior?

Useful source guidance:
- docs state typical positive `TAU0` values are often in the `0.005` to `0.1` range
- FAQ suggests instability triage should consider CFL, element quality, nonlinear features, and `tau0`

## 4. Forcing And Boundary Specification

Check:
- `NTIP`
- `NWS`
- `NRAMP`
- `NTIF`
- `NBFR`
- constituent names and frequencies
- open-boundary forcing values

Why:
- this block defines whether the model is tide-only, met-forced, or coupled to more complex forcing

Baseline interpretation:
- `NTIP = 0`
- `NWS = 0`
- `NBFR = 1`
- the open-boundary constituent is `M2`

Touch policy:
- green: none in the very first experiment
- yellow later: `NRAMP`
- red early: `NWS`, `NBFR`, tidal constituent setup

Notes:
- keeping `NWS = 0` is one reason the quarter-annular case is good for foundation work
- boundary forcing should stay frozen until the baseline case is reproduced and understood

## 5. Output And Analysis Settings

Check:
- station output settings for elevation and velocity
- global output settings
- harmonic analysis controls
- hotstart write controls

Why:
- output settings determine what evidence survives after the run
- changing output format can break comparability even when dynamics are unchanged

Baseline interpretation:
- this testsuite path is the NetCDF variant
- testsuite metadata expects `fort.61.nc`, `fort.62.nc`, `fort.63.nc`, `fort.64.nc`, `maxele.63.nc`, and `maxvel.63.nc`

Touch policy:
- green: shortening output windows only if clearly documented
- yellow: station counts and frequencies
- red early: switching output families or removing expected baseline outputs

## 6. Restart And Solver Controls

Check:
- hotstart generation settings
- algebraic solution parameters such as `ITITER`, `ISLDIA`, `CONVCR`, `ITMAX`

Why:
- these are often not the first place to change things, but they matter for reproducibility and convergence behavior

Touch policy:
- red in the first controlled experiment

## Freeze List For The First Controlled Experiment

Keep fixed:
- `ICS`
- `IM`
- `NOLIFA`
- `NOLICA`
- `NOLICAT`
- `NWS`
- `NBFR`
- constituent setup
- output family
- solver controls

Allowed first variable:
- `DT`

Allowed second-wave variables:
- `RNDAY` for shorter debug runs
- `TAU0` after `DT` sensitivity is understood

## Evidence To Save For Every fort.15 Change

- changed line or parameter
- reason for the change
- expected effect
- actual effect
- whether the change should be promoted to a heuristic or just remain an experiment note
