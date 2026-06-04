---
title: "adcirc met forcing implementation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-met-forcing-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC met forcing — NWS dispatch, OWI readers, wind drag

## Scope

Where ADCIRC reads wind/pressure forcing, how `NWS` selects format, exact reader paths for NWS=2/12/13/14/15, wind-drag computation, and inverse-barometer pressure handling. Critical for the upcoming JMA-MSM → NWS=13 workflow.

## A. NWS dispatch

- Top-level normalization at `[file=src/read_input.F line=1755-1774]`:
  - Strips `1000`s ice flag → `NCICE`
  - Strips `100`s radiation-stress flag → `NRS`
  - Validates against `allowable_nws` (allows ±, +100i variants)
- Cold-start init: `coldStartMeteorologicalForcing` at `[file=src/wind.F line=1811-2057]` (`IF(NWS...)` blocks for 1, ±2, 3, ±4, ±5, 6, ±7, ±8, 10, 11, ±12, ±13, ±14, ±15, 16, 19, 20, 29, 30)
- Hot-start runtime: `hotStartMeteorologicalForcing` at `[file=src/wind.F line=2135-3228]` (`SELECT CASE` for 0, 17 + IF blocks for the rest)
- Per-NWS print banner at `[file=src/read_input.F line=1825-2070]`

### Per-value dispatch line map

| NWS | Cold-start init | Hot-start runtime | Print banner |
|-----|-----------------|-------------------|--------------|
| 0 | (skip) | `wind.F:2135-2146` | `read_input.F:1819-1824` |
| +1 | -- | `wind.F:2149-2164` | `read_input.F:1825-1832` |
| ±2 | -- | `wind.F:2170-2201` (NWS=2), `wind.F:2203-2217` (NWS=-2) | `read_input.F:1833-1852` |
| +3 | -- | `wind.F:2223-2291` | `read_input.F:1853-1864` |
| ±4 | -- | `wind.F:2298-2346, 2348-2381` | `read_input.F:1865-1890` |
| ±5 | -- | `wind.F:2387-2436, 2438-2472` | `read_input.F:1891-1916` |
| +6 | -- | `wind.F:2481-2526` | `read_input.F:1917-1929` |
| ±7 | -- | `wind.F:2535-2558, 2560-2585` | `read_input.F:1933-1952` |
| +10 | -- | `wind.F:2693-2741` | `read_input.F:1976-1989` |
| +11 | -- | `wind.F:2751-2796` | `read_input.F:1990-2002` |
| ±12 | -- | `wind.F:2800-2848` | `read_input.F:2004-2031` |
| ±13 | -- | `wind.F:2852-2885, 3032-3067` | `read_input.F:2658, 4671` |
| ±14 | -- | `wind.F:2937-3027` | `read_input.F:2033-2058` |
| ±15 | -- | `wind.F:3071-3096` | `read_input.F:2059-2069, 2767-2774` |

## A2. NWS=8 (parametric vortex, mod_nws08) — verified 2026-06-04

- `nws08.F90`(1600, module `mod_nws08`): **parametric 태풍 vortex** wind — best-track(중심위치·중심기압·Rmax)으로 wind/pressure 격자장 합성. `&nws08Control` namelist.
- **2 vortex 모델**: `vortexModel="Holland"`(Holland 1980 gradient wind) 또는 **`"CLE15"`**(Chavas-Lin-Emanuel 2015, outer-region radial structure). `backgroundWindModel`: `radialVelocityWeighted` 또는 `LC12`(Lin-Chavas 2012 이동 비대칭). `windspeed_averaging_minute`(1/10), `WindMultiplier`.
- EFDC [[efdc_cyclone_wind]](Holland/Hubbert/McConochie/Willoughby)와 같은 계열 — ADCIRC 측 symmetric parametric TC. GAHM/AHM(asymmetric, 별도)과 구분. storm-surge 직결.

## B. NWS=2 (single-grid wind/pressure file)

- Reader inline in `hotStartMeteorologicalForcing`: `wind.F:2170-2201` (NWS=2), `wind.F:2203-2217` (NWS=-2)
- Reads fort.22 directly: `READ(22,*) ... WVNX/WVNY/PRN`
- WTIMINC defines bracketing times `WTIME1/WTIME2`, advances file snapshots at `[file=src/wind.F line=2172-2181, 2189]`
- Linear interpolation: `WTRATIO = (TimeLoc - WTIME1) / WTIMINC`, then `WVNX/WVNY/PRN` interpolated at `[file=src/wind.F line=2189-2199]`

## C. NWS=12 (OWI legacy ASCII)

- Module: `OWIWIND`
- Dispatch: cold-start init at `[file=src/wind.F line=1928-1934]`, runtime at `[file=src/wind.F line=2800-2808]`
- Implementation: `NWS12INIT` at `[file=src/owiwind.F line=168-255]`, `NWS12GET` at `[file=src/owiwind.F line=269-369]`
- File expectations: pressure/wind file pairs, defaults `fort.221/222`, optional `fort.223/224`, `fort.217/218`, or dynamic file list from `fort.22` when `numSets<0` at `[file=src/owiwind.F line=798-807, 830-836, 888-903]`

### Header / time block

- Per-snap grid/date header read with format `11` at `[file=src/owiwind.F line=489-490, 508-509, 579-580]`
- Pressure field + u/v wind arrays with format `22` at `[file=src/owiwind.F line=554-569]`
- File header start/end dates parsed from columns `56:65` and `71:80` at `[file=src/owiwind.F line=1085-1099]`

## D. NWS=13 (OWI NetCDF) — relevant for JMA-MSM workflow

- Module: `OWIWIND_NETCDF` (separate from NWS=12)
- `USE OWIWIND_NETCDF`, calls `NWS13INIT`/`NWS13GET` at `[file=src/wind.F line=1780, 2045-2049, 2857-2860, 3035-3037]`
- **NetCDF variable/dimension names not defined in inspected files** — controlled by namelist:
  - `NWS13File`
  - `NWS13ColdStartString`
  - `NWS13WindMultiplier`
  - `NWS13GroupForPowell`
  - all at `[file=src/read_input.F line=269-270, 516-519]`
- Time matching: model seconds (`TIMELOC`, `WTIME1/WTIME2`) passed to `NWS13GET` at `[file=src/wind.F line=2046-2049, 2858-2861]`
- No `TIMCO` symbol in these files

## E. NWS=14, 15 (newer)

- **NWS=14**: GRIB2/NetCDF meteorological reader family at `[file=src/read_input.F line=2032-2058]`
  - `NWS14INIT`, `NWS14GET` at `[file=src/wind.F line=2947, 2953-2955, 2968-2970]`
  - Cold start: `[file=src/wind.F line=2002-2010, 2022-2024]`
- **NWS=-14**: hybrid path combining NWS14 background + OWI overlay at `[file=src/wind.F line=2958-2964, 2973-2980]`
  - Hot start: `[file=src/wind.F line=2014-2019, 2028-2030]`
- **NWS=15**: HWind forcing at `[file=src/read_input.F line=2059-2069]`
  - `NWS15INIT`, `NWS15GET` at `[file=src/wind.F line=2055-2057, 3071-3074]`

## F. Wind drag

- Stress form: `WSX/WSY = Ramp * airwaterdensityrat * WDragCo * WindComponent * WindMag`
  i.e., proportional to `Cd * (rho_air/rho_water) * U10²`
- Examples: `[file=src/wind.F line=2288-2289, 3014-3015]`
- Garratt formula: `Cd = 0.001 * (0.75 + 0.067 * WindSpeed)` at `[file=src/wind.F line=514-521]`
- Cap: `WindDrag = MIN(GarrattWindDrag(...), WindDragLimit)` at `[file=src/wind.F line=531-539]`
- Default cap: `WindDragLimit = 0.0035` at `[file=src/wind.F line=122]`
- Configurable via `/metControl/ WindDragLimit` namelist at `[file=src/read_input.F line=238, 484-487]`
- **Legacy `CDCAP` token NOT present in these files** — modern code uses `WindDragLimit`

## G. Pressure-only effect (inverse barometer)

- Atmospheric pressure stored as water-surface equivalent (`PR2`) relative to `PRBCKGRND_MH2O`:
  ```
  PRDIFF = Ramp * (PR_forcing - PRBCKGRND_MH2O)
  PR2 = PRBCKGRND_MH2O + PRDIFF
  ```
  at `[file=src/wind.F line=2197-2200, 3016-3022]`
- `PRBCKGRND_MH2O` converted from mb to meters of water at `[file=src/wind.F line=352-355]`
- `NOIVB`: forces `PR2 = PRBCKGRND_MH2O` (disables IB contribution) at `[file=src/wind.F line=3018-3021, 1415-1418]`

## H. fort.71-74 met output

- Output **control** is in `read_input.F` (not the actual write):
  - Station met (NOUTM, units 71/72): `[file=src/read_input.F line=3988-3993, 4003-4014, 4051]`
  - Global met (NOUTGW, units 73/74): `[file=src/read_input.F line=4345-4353, 4360-4371]`
- **No `WRITE(71/72/73/74,...)`** in `wind.F`/`owiwind.F`/`owi_ice.F`/`read_input.F` — actual write loop is elsewhere (in `write_output.F`, see ADCIRC outputs note)

## Decision Guide — JMA-MSM workflow

| Step | Tool | Result |
|------|------|--------|
| Download JMA-MSM | external (already in WORK_LOG) | NetCDF files per day |
| Convert to OWI NetCDF | `tools/scripts/jma_to_fort22.py` | NWS=13 compatible NetCDF |
| Set NWS=13 in fort.15 | text edit | format declaration |
| Set NWS13 namelist | `NWS13File`, `NWS13ColdStartString` | reader configuration |
| Run | adcprep + padcirc | hourly wind/pressure forcing |

## Working Rules

1. **NWS=13 needs the namelist (`/owiNETCDF/`)**, not just `NWS=13` in fort.15. Without namelist, file expectations default and likely don't match converter output.
2. **NWS sign matters**: positive vs negative changes whether `WSX/WSY` are stress (positive) or wind speed (negative — multiplied by Cd internally).
3. **CDCAP** is renamed to `WindDragLimit` in v55+; legacy fort.15 `CDCAP` lines may be ignored.
4. **NOIVB=1** to disable inverse barometer when only wind matters; default behavior includes IB pressure effect on water level.
5. **fort.22 ASCII (NWS=2) requires equal-time-step header** — uneven time stamps break `WTIMINC` interpolation.

## Common Pitfalls

- **NWS=13 with wrong NetCDF variable names** — fails silently or wrong forcing; use the canonical OWI converter tool.
- **NWS=±14 (hybrid)** — only use when you have both background (e.g., GFS) AND mesoscale overlay (e.g., HWRF); otherwise NWS=14 alone.
- **Wind multiplier scaling** — `NWS13WindMultiplier` for unit conversion. Default 1.0; check if your NetCDF is in m/s or knots.
- **NOIVB** with hurricane storm-surge — disabling IB underestimates surge by 1-3 cm per mb pressure drop.
- ▢ User-experience cases — placeholder.

## References

- `src/wind.F` — main NWS dispatch + per-NWS readers.
- `src/owiwind.F` — OWI legacy reader (NWS=12).
- `src/owi_ice.F` — ice forcing.
- `src/read_input.F` — namelist parsing, NWS validation.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 50+ file:line citations |
| Coverage | NWS dispatch table, NWS=2/12/13/14/15 readers, wind drag, IB, output control |
| Review status | `review_required: true` |
