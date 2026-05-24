---
title: "roms wec"
topic: general
canonical_source: self
citation_status: verified
verification_method: "ROMS source code 직접 분석 (models/ROMS/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/roms_wec.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

The ROMS WEC (Wave Effects on Currents) module: vortex-force formulation (`WEC_VF` — note **no `WEC_MELLOR` symbol** in this tree), Stokes drift (bulk vs spectrum), surface and bottom streaming, wave breaking dissipation (Thornton-Guza, Church-Thornton), the separate roller model (Svendsen, monochromatic, Reniers), wave-enhanced BBL via SSW/MB/SG, and COAWST coupling fields exchanged with SWAN (no WW3 found in this checkout). Use this when activating wave-current interaction for surf zone, debugging Stokes-drift output, or wiring SWAN-ROMS coupling.

## Source basis

- `globaldefs.h:840-888, 861-879` — `WEC` derived flags.
- `Include/shoreface.h:21-25, test_head.h:17-20` — example CPP activations.
- `rhs3d.F:60-1087` — WEC stresses in 3D momentum.
- `WEC/wec_vf.F:1-905` — vortex force.
- `WEC/wec_stokes.F:1-723` — Stokes drift.
- `WEC/wec_streaming.F:5-529` — streaming.
- `WEC/wec_dissip.F:1-160` — breaking dissipation.
- `WEC/wec_roller.F:1-295` — roller.
- `BBL/bbl.F:1-25`, `ssw_bbl.h:84-737`, `mb_bbl.h:10-639`, `sg_bbl.h:371-603` — BBL.
- `main3d.F:392-454` — driver call sites.
- `Master/mct_roms_swan.h:153-575` — SWAN coupling fields.

## A. WEC activation

`WEC_VF` is user-facing; `globaldefs.h:861-867` automatically turns it into internal `WEC`.

Stokes selection (`:873-879`):
- If `SWAN_COUPLING` → `SPECTRUM_STOKES`.
- Else → `BULK_STOKES`.

Roller options (`:881-888`):
- `ROLLER_SVENDSEN, ROLLER_MONO, ROLLER_RENIERS` + `WEC` → internal `WEC_ROLLER`.

Example activations:
- `Include/shoreface.h:21-25`: `WEC_VF, WDISS_CHURTHOR, BOTTOM_STREAMING, SURFACE_STREAMING`.
- `Include/test_head.h:17-20`: `WEC_VF + SWAN_COUPLING`.

**No `WEC_MELLOR` symbol** found. Code uses generic "radiation stress or Vortex Force" wording when adding `rustr3d/rvstr3d` (`rhs3d.F:1068-1087`).

## B. Vortex force in 3D momentum

`rhs3d` imports + calls `wec_vf` only under `WEC_VF` (`:60-103`).

`wec_vf.F:1-18` documents: computes vortex-force terms in quasi-Eulerian velocities.

Process:
1. Fills `MIXING%rustr3d/rvstr3d` (`wec_vf.F:128-143`).
2. `rhs3d` subtracts those 3D WEC stresses from `ru/rv` (`:1068-1087`).

Horizontal Stokes/Eulerian correction (`wec_vf.F:826-905`).
Vertical vortex-force term `K` from Stokes drift × vertical shear (`:550-652`).

## C. Stokes drift

`wec_stokes.F` compiles under `SOLVE3D && WEC` (`:1-4`).

Driver call: `main3d.F:411-427` (in `WEC_VF` preprocessing block).

| Mode | Inputs | Code lines |
|---|---|---|
| Bulk Stokes | `Hwave, Dwave, Lwave` | `:103-107` |
| Spectrum Stokes | `spec_wn, spec_us, spec_vs` | `:108-112` |

Bulk `u_stokes/v_stokes` profiles (`:344-379, 490-525`).
Spectral `u_stokes/v_stokes` (`:380-486, 526-627`).

Vertical Stokes velocity + depth-mean Stokes velocities (`:659-723`).

**Bulk** uses parametric significant-wave formula; **Spectrum** uses full SWAN spectrum integral. Spectrum more accurate but requires `SWAN_COUPLING`.

## D. Surface and bottom streaming

`wec_streaming.F:5-8`: compiles for `SOLVE3D + BOTTOM_STREAMING` or `SURFACE_STREAMING`.

Called by `rhs3d` after `wec_vf` (`:100-103`).

**Bottom streaming** inputs: `Hwave, Dwave, Lwave, Pwave_top`; under wave coupling, `Dissip_fric` (`wec_streaming.F:96-102`).

Bottom streaming acceleration formed and added to `rustr3d/rvstr3d` (`:381-478`).

**Surface streaming** acts only in top layer through `Akv * Surst * waven` (`:480-529`).

Surface streaming captures Stokes-drift-induced near-surface acceleration; bottom streaming captures wave-orbital-induced bottom drift. Both important for surf zone.

## E. Wave-enhanced BBL

Cross-link to `roms_sediment.md`; same BBL module supports both sediment and WEC.

`bbl.F:1-25` selects `SSW_BBL`, `MB_BBL`, or `SG_BBL`.

`main3d.F:451-454` calls `bblm` before `set_vbc`.

**SSW** consumes wave/current including wave height or `Uwave_rms`, direction, bottom period, optionally Stokes drift (`ssw_bbl.h:84-127`):
- Computes bottom wave orbital velocity/excursion + combined wave-current stress (`:435-737`).

**MB** explicitly implements Soulsby combined wave-current stress (`mb_bbl.h:10-639`).

**SG** also computes wave-current interaction + combined stresses (`sg_bbl.h:371-603`).

## F. Wave breaking source / acceleration

Optional dissipation formulations (`wec_dissip.F:1-5`):
- `WDISS_THORGUZA` — Thornton-Guza.
- `WDISS_CHURTHOR` — Church-Thornton.

Driver calls `wec_dissip` before Stokes when active (`main3d.F:420-426`).

Both formulas set `Dissip_break`; `Dissip_wcap` zeroed (`wec_dissip.F:140-160`).

Non-conservative wave acceleration from `Dissip_break` applied in `wec_vf`:
- U momentum: `:654-703`.
- V momentum: `:724-740`.

This is the wave-breaking-induced setup/setdown driver in the surf zone.

## G. Roller model

`wec_roller.F:1-4`: `SOLVE3D && WEC_ROLLER`.

Driver calls before Stokes drift (`main3d.F:423-426`).

| Variant | Lines |
|---|---|
| Svendsen | `:217-227` |
| Monochromatic | `:229-240` |
| Reniers (evolution equation, source-sink) | `:242-295` |

Roller acceleration added in `wec_vf` under `WEC_ROLLER` (`:679-682, 705-755`).

Reniers is most general (full source-sink balance); Svendsen is simplest (geometric); monochromatic for analytic tests.

## H. SWAN coupling fields

MCT coupling shown is **ROMS-SWAN**. `SWAN_COUPLING` defines generic `WAV_COUPLING` (`globaldefs.h:840-844`).

`main3d.F:392-405` couples ocean to waves every `CoupleSteps(Iwaves)`.

SWAN → ROMS exchange (`Master/mct_roms_swan.h:153-163`):

| SWAN | ROMS |
|---|---|
| `Wdir` | `FORCES%Dwave` (:329-345) |
| `Wamp` | `Hwave` (:347-363) |
| `Wlen` | `Lwave` (:365-384) |
| `Wptop` | `Pwave_top` (:386-402) |
| `Wpbot` | `Pwave_bot` (:404-420) |
| `Wdiss` | `Wave_dissip` (:422-438) |
| `Wubot` | `Ub_swan` (:440-456) |
| `Wbrk` (only `SVENDSEN_ROLLER`) | `Wave_break` (:458-476) |

ROMS → SWAN: bathymetry, SSH, U, V, bottom roughness (`:482-575`).

**No WW3 / WAVEWATCH** coupling implementation in this checkout. ESMF wave coupling includes WAM or void wave component, not WW3 (`Master/esmf_wav.F:23-32`).

## Decision Guide

| Application | Setup |
|---|---|
| Surf-zone resolved (rip currents) | `WEC_VF, WDISS_CHURTHOR, BOTTOM_STREAMING, SURFACE_STREAMING, ROLLER_RENIERS` |
| Idealized wave-current test | `WEC_VF` only, bulk Stokes |
| SWAN-coupled hindcast | `WEC_VF + SWAN_COUPLING + SPECTRUM_STOKES` |
| Streaming-only (no vortex force) | Set `BOTTOM_STREAMING + SURFACE_STREAMING` without `WEC_VF` |
| Roller for surf-zone setup | Add `ROLLER_SVENDSEN` (simplest) |
| Wave-driven sediment | `WEC_VF + BBL_MODEL=SSW` |
| Output Stokes drift | History variables `u_stokes, v_stokes` |
| WW3 coupling | Not available in this version |

## Working Rules

- WEC_VF is the modern recommendation; older "radiation stress" form (Mellor) not in this tree.
- For surf zone, all four (`WEC_VF + roller + streaming + breaking dissipation`) typically active.
- SWAN coupling gives spectral Stokes drift (better near coastlines); bulk Stokes for offline forcing.
- `WEC_VF` adds significant compute cost (~30%); skip for non-coastal regional runs.
- Output `Hwave, Dwave, Lwave` to confirm SWAN coupling delivering correct fields.
- For Korean coast: SWAN-ROMS coupling for surge+waves; ROMS WEC_VF if surf-zone resolution.

## Common Pitfalls

- ▢ Looking for `WEC_MELLOR` — not in this tree; use `WEC_VF`.
- ▢ Activating `WEC_VF` without wave forcing (no SWAN, no bulk) — empty arrays.
- ▢ Bulk Stokes with very narrow-band spectrum (e.g., swell) — bulk formula underestimates surface Stokes.
- ▢ Forgetting `BBL_MODEL` with `WEC_VF` — bottom-stream component missing.
- ▢ Using `ROLLER_SVENDSEN` for non-breaking conditions — produces no roller energy; harmless but wasteful.
- ▢ Expecting WW3 — only WAM/SWAN coupling in ESMF/MCT framework.

## Next expansion

- WEC validation case (rip current, Yuhang Beach, etc.).
- Bulk vs spectrum Stokes comparison.
- Roller variant (Svendsen vs Reniers) sensitivity.

## References

- Uchiyama et al. 2010 (vortex force ROMS).
- McWilliams et al. 2004 (vortex force theory).
- Thornton & Guza 1983; Church & Thornton 1993 (breaking).
- Reniers et al. 2004 (roller).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `/mnt/e/models/roms/source_code/roms`. Auto-draft = false; review_required = true.
