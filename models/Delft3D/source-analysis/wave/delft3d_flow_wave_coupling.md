---
title: "delft3d flow wave coupling"
topic: general
canonical_source: self
citation_status: verified
verification_method: "Delft3D source code 직접 분석 (models/Delft3D/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/delft3d_flow_wave_coupling.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

How Delft3D-FLOW and Delft3D-WAVE (SWAN-based) communicate via the COM file, what `WaveOL` flag actually selects, the wave fields exchanged each direction, the roller-model addition, the coupling timestep mechanism (`Flpp` / `itcomi`, **not `TWAVE`**), conservation behavior at the FLOW-WAVE grid boundary, and the restart/hot-start behavior with online coupling. Use this when wiring a coupled run, debugging WAVE-FLOW timing, or interpreting `wsu/wsv/fxw/fyw` outputs.

## Source basis

- `flow2d3d_io/src/input/dimpro.f90:218, 252` — `WaveOL` parsing, roller flag.
- `flow2d3d_data/include/procs.igs:78` — `WaveOL` mode meanings.
- `flow2d3d_io/src/output/setwav.f90:210, 365-517` — COM file fields written/read.
- `wave/packages/io/src/put_wave_fields.f90:332` — WAVE writes NEFIS fields.
- `wave/packages/kernel/src/wave2com.f90:44` — SWAN → FLOW field transformation.
- `wave/packages/manager/src/wave_main.f90:430` — WAVE-side online loop.
- `flow2d3d_manager/src/tricom_step.F90:645, 699, 771-880` — FLOW-side dispatch + restart.
- `flow2d3d_kernel/src/compute/uzd.f90:668`, `cucnp.f90:631` — wave forces in momentum.
- `flow2d3d_kernel/src/compute_roller/radstr.f90:304`, `massfl.f90:113` — roller.
- `wave/packages/io/src/get_flow_fields.f90:105-229`, `flow2wav.f90:146` — FLOW → WAVE.
- `wave/packages/manager/src/swan_tot.f90:240-272` — SWAN input file generation.
- `flow2d3d_io/src/input/rdtimo.f90:337` — `Flpp` reading.
- `flow2d3d_io/src/output/postpr.f90:794` — `itcomc` advance.
- `flow2d3d_io/src/input/restart_trim_roller.f90:97-163` — roller restart.
- `wave/packages/data/src/swan_input.f90:4211, 4256` — SWAN hotstart.

## A. Mode dispatch (WaveOL)

FLOW flag `WaveOL` (`dimpro.f90:218`):
- `mimic` → `waveol = 1`.
- logical true → `waveol = 2`.
- false → `0`.

Meaning (`procs.igs:78`):
- `0` — existing COM / offline interpolation.
- `1` — existing COM but online-like constant update.
- `2` — Delft3D-WAVE online.

Online FLOW triggers WAVE at `nst == itwav` via `flow_to_wave_command(...perform_step...)` (`tricom_step.F90:699`).

WAVE-side: waits for FLOW command, sets WAVE time from FLOW `timtscale`, runs `swan_tot`, reports OK (`wave_main.f90:430`).

## B. COM-file fields

FLOW COM wave group `WAVTIM` defines (`setwav.f90:210`):
- `TIMWAV` — wave time stamp.
- `HRMS, TP, DIR` — wave height (RMS), peak period, mean direction.
- `DISTOT, DISSURF, DISWCAP, DISBOT` — total/surface/whitecap/bottom dissipation.
- `FX, FY` — wave forces.
- `WSBU, WSBV` — wave-induced bottom shear.

WAVE writes same NEFIS fields plus extras (`put_wave_fields.f90:332`):
- `MX, MY, TPS, UBOT, WLEN`.

WAVE transforms SWAN `hs/dir/period/fx/fy/mx/my/dissip` → FLOW COM `hrms/tp/.../wsbody*` (`wave2com.f90:44`).

FLOW reads `HRMS, TP/TPS, DIR, DISTOT/DISS*, FX/FY, WSBU/WSBV, MX/MY`; optional `UBOT/WLEN` (`setwav.f90:365-517`).

## C. WAVE → FLOW forcing

The code does **not** use exact symbols `TAUWX/TAUWY`. Forcing arrives as COM `FX/FY`, read into FLOW `wsu/wsv` (`setwav.f90:457`).

Momentum equations add:
- Surface wave stress `wsu` plus body force `fxw/wsbodyu` into `ddk` / `mom_m_waveforce` (`uzd.f90:668`).
- Same in non-hydrostatic / other path (`cucnp.f90:631`).

Roller / radiation-stress path computes `wsu/wsv` and `fxw/fyw`; roller force output is `WSU/WSV` (`radstr.f90:304`, `wrrolm.f90:176`).

## D. FLOW → WAVE inputs

WAVE reads from COM and maps to SWAN grid (`get_flow_fields.f90:105, 140, 171, 229`):
- Depth.
- Water level.
- Current.
- Wind.

Currents converted from FLOW u/v points to Cartesian zeta-point velocity before SWAN mapping (`flow2wav.f90:146`).

SWAN input files written per coupling step (`swan_tot.f90:240, 256, 272`):
- `BOTNOW` — bathymetry + water level.
- `CURNOW` — current.
- `WNDNOW` — wind.

## E. Coupling timestep (no `TWAVE`)

There is **no separate `TWAVE` keyword** in this tree. Coupling uses FLOW communication interval `Flpp`:
- Start / interval / stop → `itcomf / itcomi / itcoml` (`rdtimo.f90:337`).
- Each step sets `itwav = itcomc`; WAVE runs when `nst == itwav` (`tricom_step.F90:645`).
- `itcomc` advances by `itcomi` after COM write (`postpr.f90:794`).

So you control coupling frequency by `Flpp` (file communication interval), not a dedicated `TWAVE`.

## F. Roller model

Enabled by MDF `Roller`; optional `Filwcm` sets `wavcmp` (`dimpro.f90:252`).

Roller step sequence (`tritra.f90:377, 391, 407`):
1. Wave energy update.
2. Roller source/sink.
3. Roller energy transport.
4. Turbulence.
5. Radiation stress.

Roller contributes mass flux as `(Ewave + 2*Eroll) / ρ / c` into `rmasu/rmasv` (`massfl.f90:113`).

Use roller for surf-zone resolved cases where breaking-wave momentum redistribution matters (rip currents, undertow).

## G. Conservation at coupling boundary

FLOW-WAVE grid exchange uses **weighted interpolation, not conservative flux remap**:
```
f2 += w * f1
```
(`grmap.f90:76`).

Wave vectors transformed to FLOW curvilinear u/v points — component conversion, not conservation enforcement (`wave2flow.f90:48`).

FLOW hydrodynamic open boundaries with short-wave effects use Riemann / weakly reflective conditions when `wavcmp` is active (`trisol.f90:1304`, `cucbp.f90:317`).

This means: **mass/momentum conservation across the FLOW-WAVE grid boundary is approximate**. For tightly coupled cases, ensure FLOW and WAVE grids match closely or accept small drift.

## H. Restart / hot-start

FLOW online restart:
- Tries to read existing COM wave data immediately at startup.
- If absent, warns and waits until first WAVE computation (`tricom_step.F90:771`).

Roller restart reads from `map-rol-series` (`restart_trim_roller.f90:97-163`):
- `HS, EWAVE1, EROLL1, QXKR, QYKR, QXKW, QYKW, FXW, FYW, WSU, WSV`.

WAVE hotstart uses SWAN hotfiles:
- Writes `HOTFILE` at end (`swan_input.f90:4211`).
- Reads `INITIAL HOTSTART ... NETCDF` when `UseHotFile` / `usehottime` are active (`swan_input.f90:4256`).

## Decision Guide

| Application | Setting |
|---|---|
| Fully coupled storm-surge + wave setup | `WaveOL=true` (mode 2), `Flpp` = 30–60 min |
| Offline wave forcing (precomputed COM) | `WaveOL=false` (mode 0) |
| Quasi-online with prescribed WAVE update | `WaveOL=mimic` (mode 1) |
| Surf-zone wave-driven flow (rip currents) | Add `Roller=true` |
| Restart from prior coupled run | Both FLOW restart + SWAN hotfile (`UseHotFile`) |
| FLOW grid ≠ WAVE grid resolution | Mind grid mapping; use `grmap` weights |
| Multi-domain DD with WAVE | Coupled per-domain; WAVE grid covers all FLOW domains |
| Sediment + wave coupling | Roller + standard sediment + `wavcmp` |

## Working Rules

- `Flpp` should be ~ wave field response time (≈ tide period / 4 for tides; ≈ wind change time scale for surge). Too short = expensive; too long = lagged feedback.
- Always check FLOW and WAVE grid alignment before running coupled — use Delft3D-MOR or Delft3D-Quickplot to verify overlap.
- For storm hindcast: use `WaveOL=true`, `Flpp ~ 60 min`. Acceptable for semi-stationary winds.
- Roller adds CPU cost (~30% on FLOW side); enable only when surf-zone matters.
- SWAN hotfile path: `UseHotFile` triggers read; `WriteHotFile` triggers write at end. Both needed for restart chain.
- COM file is binary NEFIS — use `getdata.pl` or NetCDF conversion for inspection.
- Diagnostic: time series of `WSU` at a station should track wave-orbital × FX magnitude.

## Common Pitfalls

- ▢ Setting `WaveOL=true` but not running Delft3D-WAVE simultaneously — FLOW waits forever at `itwav`.
- ▢ Setting `Flpp` to mismatch WAVE expected interval — first time mismatch crashes WAVE.
- ▢ Using offline COM (`WaveOL=0`) but writing COM with online setup — fields stale immediately.
- ▢ Hot-start without `WriteHotFile` enabled in prior run — SWAN cold-starts; surface gravity waves take 30+ min spin-up.
- ▢ Restart without prior `map-rol-series` file — roller restarts cold; surf-zone solution discontinuous.
- ▢ Looking for `TWAVE` keyword — doesn't exist; use `Flpp`/`itcomi`.
- ▢ Looking for `TAUWX` — actual code uses `wsu/wsv` and `fxw/fyw`.
- ▢ Expecting strict conservation between FLOW and WAVE grids — interpolation is weighted, not conservative.

## Next expansion

- Multi-domain DD coupled with WAVE walkthrough.
- Conservation audit recipe for FLOW-WAVE budget.
- Roller calibration parameters (Beta_b, Alfaroll).

## References

- Roelvink 1993 (roller model).
- Booij et al. 1999 (SWAN third-generation).
- Delft3D-FLOW User Manual (Deltares, latest).
- Delft3D-WAVE User Manual (Deltares).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/delft3d/source_code/Delft3D/src/engines_gpl`. Auto-draft = false; review_required = true.
