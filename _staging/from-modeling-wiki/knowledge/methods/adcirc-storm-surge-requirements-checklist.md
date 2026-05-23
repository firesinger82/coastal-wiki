# ADCIRC Storm Surge Requirements Checklist

Date: 2026-04-12

Purpose:
- list what must be prepared before storm-surge experiments begin
- keep this at the requirements level, not the tuning level

## General Storm Surge Requirements

- [ ] target domain and mesh identified
- [ ] bathymetry/topography source identified
- [ ] vertical datum context identified
- [ ] tide vs storm-tide decision made
- [ ] meteorological forcing family selected
- [ ] baseline example closest to the intended workflow identified
- [ ] required output families chosen
- [ ] validation data sources identified

## `JMA-MSM + NWS=13` Requirements

### Source Data

- [ ] JMA-MSM coverage window identified
- [ ] JMA-MSM spatial coverage confirmed against the ADCIRC mesh
- [ ] wind and pressure fields available for the required period
- [ ] source temporal cadence recorded

### Conversion To ADCIRC-Readable Forcing

- [ ] conversion path from JMA-MSM to OWI-NWS13 NetCDF documented
- [ ] variable mapping documented for `U10`, `V10`, `PSFC`
- [ ] `lat`, `lon`, `time` handling documented
- [ ] units checked and documented
- [ ] overlay/group policy documented if multiple grids are used
- [ ] output file naming policy documented (`fort.22.nc` or override)

### ADCIRC fort.15 Interface

- [ ] `NWS = 13` confirmed
- [ ] `WTIMINC` policy documented
- [ ] `&owiWindNetcdf` namelist documented
- [ ] `NWS13ColdStartString` policy documented
- [ ] `NWS13File` override policy documented if applicable
- [ ] `NWS13WindMultiplier` use documented if applicable
- [ ] `NWS13GroupForPowell` use documented if applicable

### Ramping And Restart

- [ ] cold start vs hotstart path documented
- [ ] meteorological ramping policy documented
- [ ] if hotstart is used, `NRAMP/DRAMPMete/DRAMPUnMete` handling documented

### Outputs And Evaluation

- [ ] water-level outputs selected
- [ ] max-elevation output selected
- [ ] velocity outputs selected if needed
- [ ] meteorological outputs such as `NOUTGW` policy documented
- [ ] archive and naming policy documented

## What This Checklist Is Not

This checklist does not yet answer:
- what exact `DT` to use
- what exact drag values to use
- what exact mesh resolution to use
- which run is "best"

Those belong after requirements are documented.
