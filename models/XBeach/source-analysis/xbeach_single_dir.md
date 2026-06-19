---
title: "xbeach single dir"
topic: general
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_single_dir.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

> **canonical 역할 (2026-06-04 중복 정리)**: 본 노트 = `single_dir=1` **모드**(instationary 를 1 bin 으로 축약 + stationary directional 보정). 정상상태 파작용 **solver 자체**는 [[xbeach_wave_stationary]](wave_stationary/wave_stationary_directions), 시간전진 파작용은 [[xbeach_wave_action_balance]] 가 canonical.

## Scope

`single_dir=1` activation (surfbeat-only, default 1 in 2D, 0 in 1D), the mechanism: full multi-direction stationary directional update at `wavint`, but instationary action collapsed to **one representative direction bin** (`s%ntheta=1`) every step. Cost saving (instationary loops over 1 bin instead of `ntheta`), refraction+shoaling carried by stationary solve over `ntheta_s`, accuracy trade-off (loses directional spreading + per-bin refraction in surfbeat). Use this when sea state is narrow in direction and local mean direction is good representative.

## Source basis

- `params.F90:103-106, 251-263, 1359-1360` — activation, defaults.
- `initialize.F90:315-347` — directional grid setup.
- `wave_timestep.F90:83-104` — surfbeat dispatch.
- `wave_stationary_directions.F90:71-570` — stationary directional solve.
- `wave_instationary.F90:140-465` — instationary solve.
- `wave_functions.F90:24-1188, 283-285` — auxiliary, refraction.
- `variables.def:69-80` — directional state arrays.

## A. Activation

`single_dir` only enabled for surfbeat (`params.F90:103-106`).

Defaults (`:251-263`):
- 2D surfbeat: `1` (on).
- 1D: `0` (off).

When enabled:
- Normal instationary directional grid collapsed to **one bin**.
- Separate stationary directional grid created with `dtheta_s`.

Setup (`initialize.F90:315-347`):
- `s%ntheta = 1` (instationary).
- `s%ntheta_s` from `dtheta_s` (stationary).

In `wave_timestep.F90`, surfbeat dispatch branches on `par%single_dir`. Single-dir path:
1. Updates smoothed fields.
2. Conditionally recomputes stationary directions.
3. **Always** calls `wave_instationary` (`:83-104`).

## B. Stationary directional update at wavint

Wave directions recomputed when (`wave_timestep.F90:88-92`):
- `mod(t, wavint)` hits interval.
- New stationary BC arrives.
- First wave step `t == dt`.

Stationary call: `wave_stationary_directions(s, par, 1)` where `callTypeDirections` selects `s%ntheta_s, s%hhws, s%ee_s, s%dtheta_s` (`wave_stationary_directions.F90:71-155`).

So full multi-direction solve runs only at `wavint` events, not every step.

## C. Instationary action advances every step

Even when stationary directions update only at `wavint`, **`wave_instationary(s, par)` is called every surfbeat wave step** (`wave_timestep.F90:97-103`).

In instationary solver, `single_dir` sets only direction slot `1` from `s%thetamean` (`wave_instationary.F90:140-142`).

Action step still runs:
- Energy ÷ intrinsic frequency.
- Advect in x/y/θ.
- Multiply back (`:191-229`).

But over **only 1 direction bin** (huge cost saving).

## D. Refraction and shoaling

Refraction for `single_dir` carried by stationary directional solve over `ntheta_s`:
- Direction velocities with flavour `2` (`wave_stationary_directions.F90:222-228`).
- Theta-advection when `refraction=1` (`:342-351`).
- Recomputes `s%thetamean` from `s%thet_s` (`:566-570`).

Instationary solve then shoals/propagates action along single representative direction using `cgx/cgy` from `costh/sinth` (`wave_functions.F90:1176-1188`).

**True theta-bin refraction advection disabled** when only 1 bin (`:283-285`).

## E. Cost saving

The expensive per-step surfbeat action and roller loops run over `s%ntheta`, **forced to `1` in single_dir** (`initialize.F90:315-320`, `wave_instationary.F90:191-326`).

Model still pays for stationary directional solve over `s%ntheta_s`, but only at `wavint` or new BC events.

For typical config:
- Full surfbeat: 36 directions × cost per step.
- single_dir: 1 direction × cost per step + occasional 36-dir stationary at `wavint`.

Net saving: ~30-50% for typical `wavint=15-30 s`.

## F. wavint scheduling

`wavint` read when stationary OR `single_dir=1` (`params.F90:1359-1360`).

In single-dir surfbeat, smoothed stationary fields updated every step with time scale based on `wavint` (`wave_functions.F90:24-32`).

Actual stationary direction recomputation scheduled by modulo/new-BC/first-step condition.

## G. Appropriate use

Use `single_dir` when:
- Sea state narrow in direction.
- Local mean direction is good representative.

Matches implementation: full stationary spectrum updates `s%thetamean`; time-dependent surfbeat energy collapsed into one propagated direction.

For Korean coast typhoon hindcast: typically OK (narrow swell + sea); for crossing seas (e.g., bidirectional swell), use full directional surfbeat (`single_dir=0`).

## H. Accuracy trade-off

Explicit in data layout (`variables.def:69-80`):
- `ee_s/thet_s`: multi-direction stationary solve.
- `ee/rr/thet`: only one direction bin in instationary surfbeat.

**Loses** in surfbeat evolution:
- Directional spreading.
- Directional crossing (multiple wave systems).
- Per-bin refraction dynamics.

Full directional surfbeat keeps `s%ntheta` bins; recomputes mean direction from `s%ee*s%thet` (`wave_instationary.F90:462-465`).

## Decision Guide

| Sea state | Setting |
|---|---|
| Narrow swell-dominated, single direction | `single_dir=1` (default 2D) |
| Bidirectional sea + swell | `single_dir=0` (full directional) |
| Storm wind sea, broad spread | `single_dir=0` |
| 1D model | `single_dir=0` (default) |
| Quick screening | `single_dir=1` (cheap) |
| Production surf-zone with crossing seas | `single_dir=0` (more accurate) |
| Validation against directional buoy | `single_dir=0` |
| Korean coast typhoon | `single_dir=1` (typically OK) |

## Working Rules

- `wavint=15-30 s` typical for storms; smaller for fast-changing conditions.
- `dtheta_s=10°` for stationary grid; finer if directional resolution matters.
- `single_dir=1` works with `wbctype=parametric/swan/jons_table`.
- For nonh mode, `single_dir` is irrelevant (nonh is wave-resolving, no directional spectrum).
- Output `thetamean` to verify single representative direction tracks expected.
- For short-wave runup with crossing seas, do not use `single_dir`.

## Common Pitfalls

- ▢ Setting `single_dir=1` for stationary mode — only enabled for surfbeat.
- ▢ Expecting same accuracy as full directional in cross-sea cases — fundamentally limited.
- ▢ Setting `wavint` very small with `single_dir=1` — defeats cost saving (stationary recompute every step).
- ▢ Crossing seas tracked by `thetamean` only — averages out dual peaks; misleading.
- ▢ Comparing storm response with/without `single_dir` — may differ in surf-zone setup.

## References

- Roelvink et al. 2009 (XBeach surfbeat baseline).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
