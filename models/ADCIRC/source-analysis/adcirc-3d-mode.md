---
title: "adcirc 3d mode"
topic: general
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-3d-mode.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

ADCIRC's two distinct 3D paths: (1) `couple2baroclinic3D.F` which **imports external 3D fields** as a 2D-DDI baroclinic forcing, and (2) **true ADCIRC-3D** activated by `IM=1/11/21/31` with sigma-layer prognostic salinity/temperature, MY2.5 turbulence, and full baroclinic pressure gradients. How GWCE is modified, what EOS options exist, what station/global outputs are produced (fort.41-46), and the limitations vs full ocean models (no TEOS-10, simple/UNESCO EOS, prescribed eddy viscosity options + legacy MY2.5). Use this when configuring 3D for stratified estuary/shelf, debugging baroclinic forcing, or interpreting fort.42/45 velocity output.

## Source basis

- `read_input.F:1176-1191, 3072, 5139-5482, 5682` — `IM, IDEN, IGC/NFEN, EQNSTATE`, 3D output controls.
- `adcirc.F:316-319, 348` — top-level dispatch, baroclinic init.
- `couple2baroclinic3D.F:39-787` — external-coupling module.
- `cstart.F:348` — `Initial_BC3D_NetCDF` call.
- `timestep.F:1121, 1125, 1918, 2150-2355` — VSSOL call, BPG3D, dispersion.
- `gwce.F:780-1450` — GWCE 3D additions.
- `vsmy.F:1168, 1543-3871, 4061-4315` — internal solve, EOS, MY2.5.
- `global_3dvs.F:94, 193, 568` — symbols, FEGRIDS.
- `write_output.F:2993-3331` — 3D output dispatch.

## A. Two distinct paths

ADCIRC has **two different 3D paths** that are easy to confuse:

| Path | Activation | What it does |
|---|---|---|
| External baroclinic coupling | `C2DDI .and. CBaroclinic .and. abs(IDEN) >= 5` | Imports `BPGX, BPGY, SigTS, NB, NM, MLD, CDisp, DispX, DispY` from external NetCDF; injects depth-integrated baroclinic terms into 2D ADCIRC. **Not a 3D solver inside ADCIRC.** (`couple2baroclinic3D.F:39-787`, `cstart.F:348`) |
| True ADCIRC-3D | `IM=1, 11, 21, 31` (sets `C3D=.TRUE.`, `C3DVS=.TRUE.`); `IM=21, 31` also set `CBaroclinic=.TRUE.` | Prognostic 3D velocity (VSSOL), optional T/S transport, baroclinic pressure (BPG3D), MY2.5 turbulence (`read_input.F:1176-1191`) |

The **external coupling** is for ADCIRC users who run an external 3D ocean model (e.g., HYCOM, ROMS) and want its baroclinic effects in their 2D ADCIRC tide+surge run. It does **not** require running ADCIRC in 3D mode.

## B. Sigma layers

Vertical grid via `IGC, NFEN`:
- `NFEN` = number of vertical finite-element nodes (`read_input.F:5139`).
- `IGC=0`: read sigma levels directly; bottom `B=-1`, surface `A=1` required (`:5176`).
- `IGC≠0`: call `FEGRIDS()` (`:5211`).

`FEGRIDS` supports (`global_3dvs.F:568`):
- Evenly spaced.
- Logarithmic.
- Log-linear.
- Double-log.
- p-grid.
- Sine grids.

Coordinate constants: `A=1`, `B=-1`, `AMB=A-B` (`global_3dvs.F:193`).

## C. Density / EOS

Salinity/temperature transport when `C3D_BTrans=.TRUE.` (`vsmy.F:1548-1553` 은 **dispatch만** — 실제 solver 는 `transport.F`/`TRANS_3D`, [[adcirc-transport-solver]] 참조):

| `IDEN` | Transports |
|---|---|
| `2` | Salinity only |
| `3` | Temperature only |
| `4` | Both |

After transport, `CALC_SIGMAT_3D()` for `IDEN > 1` (`vsmy.F:1630`).

`Eqnstate` from input (`read_input.F:5682`):

| `Eqnstate` | EOS | Code lines |
|---|---|---|
| `1` | Simple linear (Mellor / Cushman-Roisin) | `vsmy.F:4061` |
| `2` | McDougall et al. 2003 | `:4154` |
| `3` | UNESCO 1980 | `:4315` |

**Limitation**: no TEOS-10 (Conservative Temperature, Absolute Salinity). For modern ocean accuracy, this is a gap.

## D. Internal vs external mode

External (depth-integrated): GWCE + 2D momentum (always solved).

Internal (3D shear): `VSSOL()` (`timestep.F:1121`), called only when `C3DVS=.TRUE.`.

VSSOL 내부의 연직 시간적분(2TL θ³-가중 Alp1/Alp2/Alp3·복소 q=u+iv tridiagonal·연직 linear FE·w adjoint 보정)은 → **[[adcirc-3d-vssol-vertical-scheme]]** (2026-07-11 신설, 본 노트의 미커버 갭 해소).

Before VSSOL, barotropic pressure terms loaded into `MOM_LV_X`, aliased as `BTP` (`timestep.F:1125`, `global_3dvs.F:94`).

After internal solve, `Qkp1` vertically integrated for:
- Depth-averaged `UU, VV`.
- Depth-averaged fluxes.
- Bottom stress.
- Velocity dispersion terms (passed back to external) (`vsmy.F:1168`).

## E. GWCE modification for 3D

GWCE receives two 3D/baroclinic additions:
1. **Velocity dispersion** (from 3D shear).
2. **Depth-integrated baroclinic pressure gradient**.

If `C3D=.FALSE.`, dispersion averages zeroed (`gwce.F:780`).
If `CBaroclinic=.FALSE.`, baroclinic gradient averages zeroed (`:786`).

For 3D mode (`gwce.F:1196, 1283, 1405, 1450`):
- Bottom stresses: `BSX1/BSY1` (3D-derived).
- Velocity-dispersion gradients from `DUU1, DUV1, DVV1`.
- Baroclinic forcing from `VIDBCPDXOH/VIDBCPDYOH`.
- Enter GWCE forcing as `−DispXAvg − BCXAvg` and `−DispYAvg − BCYAvg`.

For true 3D baroclinic (`IM=21/31`):
- `BPG3D()` computes vertical baroclinic pressure `BCP`, profiles `BPG`, depth-integrated `VIDBCPDXOH/VIDBCPDYOH` (`timestep.F:2150-2355`).

## F. Vertical mixing

Vertical eddy viscosity controlled by `IEVC, EVMin, EVCon` (`read_input.F:5235`).

| `IEVC` | Profile |
|---|---|
| `0` | Read profile from input |
| (other) | Empirical: constant, `ω H²`, `κ u* z`, `H Uavg`, `Uavg²` (`vsmy.F:1823, 1840, 1870, 1931, 1983`) |
| `50, 51` | **MY2.5 quasi-equilibrium** (`vsmy.F:2035, 2403`) |

MY2.5 closure:
- Solves `q²` and `q²L`.
- `Km = Sm q l`.
- Stratification through `SIGT` gradients; shear from `Q` (`vsmy.F:2740`).
- Computes `Km, Kq, Kh` (`:2821`).

**Limitation**: this is built-in MY2.5 — older, lacks GLS / k-ε / k-ω modern alternatives. For full closure flexibility, ADCIRC would need GOTM-style integration (not present).

## G. 3D output (fort.41-46)

Station output:
- `fort.41` — 3D density/salinity/temperature stations (`read_input.F:5296`, `write_output.F:2993`).
- `fort.42` — 3D velocity stations (real/imaginary horizontal + `WZ`) (`:5350`, `:3059, 3623`).
- `fort.43` — 3D turbulence stations (`q20, l, EV`) (`:5395`, `:3125`).

Global output:
- `fort.44` — 3D density/salinity/temperature global (`:5438`, `:3209`).
- `fort.45` — 3D velocity global (`:5460`, `:3254`).
- `fort.46` — 3D turbulence global (`:5482`, `:3299`).

Optional: `fort.48` — internal BPG output (`global_3dvs.F:335`, `write_output.F:3331`).

## H. Limitations vs full ocean model

External coupling (`couple2baroclinic3D.F:39-787`):
- Consumes external fields, interpolates spatially/temporally.
- Injects depth-integrated terms into 2D ADCIRC.
- **NOT** a 3D ocean solver inside ADCIRC.

True ADCIRC-3D:
- Prognostic S/T transport ✓.
- Baroclinic pressure gradients ✓.
- MY2.5 closure (legacy) — no GLS/k-ε/k-ω.
- EOS: simple / McDougall 2003 / UNESCO 1980 — **no TEOS-10**.
- The coupling module itself comments that "better practice would be conservative-temperature/absolute-salinity interpolation before density calculation" (`couple2baroclinic3D.F:40`).
- Vertical mixing options largely prescribed/empirical or built-in MY2.5.

Bottom line: ADCIRC-3D is suitable for **storm surge with stratification effects** or **coastal estuarine** problems where MY2.5 is sufficient. For deep-ocean or fully baroclinic ocean studies, use ROMS/HYCOM and couple via `couple2baroclinic3D.F`.

## Decision Guide

| Application | Setting |
|---|---|
| 2D tide/surge with prescribed baroclinic forcing | `IM=0`, `IDEN=5+` baroclinic coupling NetCDF (`Initial_BC3D_NetCDF`) |
| 3D barotropic (no S/T) | `IM=11`, `IDEN=0`, prescribed `IEVC` |
| 3D salinity transport only | `IM=21`, `IDEN=2` |
| 3D temperature only | `IM=21`, `IDEN=3` |
| 3D both S/T (estuarine) | `IM=21`, `IDEN=4`, `Eqnstate=2` (McDougall) |
| 3D + MY2.5 turbulence | `IM=21`, `IEVC=50` or `51` |
| Storm surge with stratification | `IM=21`, `IDEN=4`, `MY2.5` |
| Modern EOS needs (TEOS-10) | Not supported — use external ROMS/HYCOM |
| Output S/T at stations | `fort.41` enabled via `NSPOOLD/NTRSPE` |
| Output 3D velocity globally | `fort.45` |

## Working Rules

- `IM=21` is the most common 3D-baroclinic configuration. <!-- source-needed: 커뮤니티 관행 단언 — ADCIRC 매뉴얼/문헌/공식 예제 인용 필요 -->
- `NFEN=21` (20 sigma layers) is standard for shelf/estuary; up to `NFEN=51` for deep stratification. <!-- source-needed: 관행 수치 — 매뉴얼/문헌 인용 필요 -->
- For Korean coastal storm surge with thermohaline forcing, use `IM=21` + external HYCOM via `couple2baroclinic3D.F` (`IDEN>=5`).
- MY2.5 (`IEVC=50/51`) is recommended over prescribed profiles for stratified runs.
- Output `fort.41` (T/S stations) early in run to verify EOS computation.
- Boundary conditions for S/T need their own time series (typically from external model or climatology).

## Common Pitfalls

- ▢ Setting `IM=11` and expecting baroclinic — `IM=11` is barotropic 3D; need `IM=21+` for baroclinic.
- ▢ Setting `IDEN=4` without providing both S and T BCs — model crashes. <!-- source-needed: crash 경로 file:line 인용 필요 -->
- ▢ Using simple linear EOS (`Eqnstate=1`) for realistic ocean — gives unrealistic pycnocline. <!-- source-needed: 물리 결과 단언 — 문헌/교과서 인용 필요 -->
- ▢ Confusing `couple2baroclinic3D.F` (external coupling) with true 3D — they look similar but only the latter solves 3D internally.
- ▢ `IEVC=50` (MY2.5) cold-started with zero `q²` — singular dissipation; init with positive minimum. <!-- source-needed: singular 거동 file:line 또는 문헌 인용 필요 -->
- ▢ Hot-start with different `IM` — 3D state arrays incompatible.
- ▢ Comparing ADCIRC-3D temperature to TEOS-10 reference — slight bias due to legacy EOS; document explicitly.
- ▢ Forgetting to set bottom drag for 3D — bottom stress comes from 3D BBL, not 2D Manning.

## Next expansion

- HYCOM → couple2baroclinic3D.F NetCDF format example.
- MY2.5 (IEVC=50) calibration recipe.
- IM=21 vs IM=31 differences.
- Coupling external WAVES (SWAN-3D not standard).

## References

- Luettich & Westerink (ADCIRC theory v53+ docs).
- Mellor & Yamada 1982 (MY2.5).
- McDougall et al. 2003 (EOS).
- UNESCO 1981 (EOS-80).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
