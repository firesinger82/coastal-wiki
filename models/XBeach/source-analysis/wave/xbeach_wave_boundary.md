---
title: "xbeach wave boundary"
topic: currents
canonical_source: self
citation_status: verified
verification_method: "XBeach source code 직접 분석 (models/XBeach/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/xbeach_wave_boundary.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

> **canonical 역할 (2026-06-04 중복 정리)**: 본 노트 = 파 경계 **type/config·spectrum 파일·datastore**(wbctype·JONSWAP·BCF). **생성 알고리즘**(랜덤위상 단파 train→bound IG, Herbers/Van Dongeren)은 [[xbeach_wave_boundary_generation]], **flow 경계조건**(abs_2d 등)은 [[xbeach_flow_boundary_conditions]] 가 canonical. SWAN 입력 읽기는 [[xbeach_swan_handoff]].

## Scope

How XBeach selects a wave-boundary type via `wbctype`, how JONSWAP spectra are generated (legacy `waveparams.F90` vs newer `waveparamsnew.F90`), how BCF files are written and time-interpolated, the role of `wave_bc_nextgen.f90` (scaffold), how directional spreading uses exponent `s`, what the `wave_boundary_datastore.F90` persists, and the front/back boundary options including nonh BC. Use this when configuring incident waves, debugging spectral file structure, or wiring a custom BC time series.

## Source basis

- `params.F90:321, 504, 535, 553, 683-687, 2561, 2644` — `wbctype`/`front`/`back`/`order` parsing.
- `paramsconst.F90:133` — `WBCTYPE_*` constants.
- `params.def:147, 196-198` — `order`, `fwcutoff`.
- `boundaryconditions.F90:127-1307` — runtime BC dispatch and front handling.
- `waveparams.F90:164, 247, 258` — legacy JONSWAP.
- `waveparamsnew.F90:98, 366-2974` — newer spectral path.
- `wave_boundary_main.f90:35, 193, 256` — newer interface main.
- `wave_boundary_update.f90:312` — spectral reader dispatch.
- `wave_boundary_datastore.f90:16-63` — persistent state.
- `wave_bc_nextgen.f90` — scaffold module (commented out).

## A. `wbctype` dispatch

Constants in `paramsconst.F90:133`:
- `parametric, swan, vardens, off, jons_table, reuse, ts_1, ts_2, ts_nonh` → `WBCTYPE_*`.
- **No `WBCTYPE_JONS`** — old `instat=jons` translates to `WBCTYPE_PARAMETRIC` (`params.F90:2644`).

Accepted in `params.txt`:
- `parametric, swan, vardens, off, jonstable, reuse, ts_1, ts_2, ts_nonh` (`params.F90:321`).
- Old `instat` names also accepted: `jons, swan, vardens, off, jons_table, ...` (`:2561`).

Files involved:
- `wave_boundary_init.f90` — empty placeholder (`:1`).
- `wave_boundary_main.f90` — newer interface, exposes `create_incident_waves_surfbeat` (`:35, 193`).
- `wave_boundary_update.f90:312` — spectral reader dispatch:
  - JONSWAP / `jons_table` → `read_jonswap_file`.
  - SWAN → `read_swan_file`.
  - vardens → `read_vardens_file`.

Actual XBeach runtime dispatch in `boundaryconditions.F90`:

| `wbctype` | Action | Line |
|---|---|---|
| `ts_1` | Reads `bc/gen.ezs` | `:127` |
| `ts_2` | Reads `bc/gen.ezs` with bound wave | `:166` |
| Stationary `jons_table` | Reads table directly | `:205` |
| Spectral `parametric/jons_table/swan/vardens` | Calls `spectral_wave_bc` | `:238` |
| `reuse` | Starts from existing BCF lists | `:248` |
| `ts_nonh` | Reads `boun_U.bcf` via `velocity_Boundary` | `:251` |
| `off` | Skips front forcing | `:1198` |

## B. JONSWAP generation

**Legacy** (`waveparams.F90`): dispatches `WBCTYPE_PARAMETRIC` and `WBCTYPE_JONS_TABLE` to `build_jonswap`, writes `E*.bcf` and `q*.bcf` (`:164`). Reads `Hm0, fp, fnyq, dfj, gammajsp, s, mainang`.

Note: legacy reads **`fp`**, not `Tp`, except table input where the second column is read as period and converted with `fp = 1/Tp` (`:247, 258`).

**Newer** (`waveparamsnew.F90`):
- Supports `Tp` or `fp`; if both present, chooses `Tp` (`:491`).
- Reads `Hm0, gammajsp, s` (directional spreading), optional `tma`, `mainang` or `dir0` (`:488, 505, 517`).
- `fnyq` defaults to `max(0.3, 3*max(fp))`, `dfj=fnyq/200` (`:535`).

JONSWAP shape in `jonswapgk` (`waveparamsnew.F90:617, 889`):
- Nondimensional `x = f/fp`.
- `σ` = 0.07 below peak, 0.09 above.
- Density: `x^-5 * exp(-1.25*x^-4) * γ^exp(...)`.
- Normalize by `maxval(y)`.
- Scale to requested wave height: `(Hm0/(4*sqrt(sum(y)*dfj)))²*y` (`:641`).
- `mainang` converted from nautical degrees to internal radians: `1.5*π − mainang*π/180` (`:642`).

## C. BCfile reading and time interpolation

For spectral input files (`waveparamsnew.F90`):
- Detects `FILELIST` directive — list rows give `rtbc, dtbc, spectrum_filename`; `rtbc` is morfac-adjusted (`:366, 385`).
- Without `FILELIST`, reuses same file with `par%rt`, `par%dtbc` (`:401`).
- File-length checker handles ordinary spectral, `FILELIST`, `jons_table`, `reuse` formats (`filefunctions.F90:224`).

Runtime timestep interpolation of generated surfbeat BCF files (`boundaryconditions.F90`):
- Opens `ebcflist.bcf` / `qbcflist.bcf` (`:477`).
- Reads selected list line; opens direct-access energy + flux files (`:571`).
- Keeps two adjacent records `ee1/ee2`, `q1/q2`; advances as time crosses `dtbcfile` (`:597`).
- Linearly interpolates `s%ee` and `q` at `par%t` (`:655`).
- Interpolated flux rotated/divided by depth into `ui/vi` (`:661`).

`wave_boundary_main.f90:256` — in-memory analogue interpolating `waveBoundaryTimeSeries%tbc` to `eebc, qsbc, qnbc` via `linear_interp`.

## D. `wave_bc_nextgen.f90` (scaffold)

Module declared as portable XBeach/Delft3D/FlowFM wave-boundary generator (`:1`), but:
- Public API commented out (`:10`).
- Entire `wave_bc_generate` body commented (`:16`).
- Comments mirror legacy BCF-list/read/interpolate workflow (`:101, 123, 189`).

**Active runtime uses `boundaryconditions.F90` + `spectral_wave_bc_module` from `waveparamsnew.F90`** (`boundaryconditions.F90:43`, `waveparamsnew.F90:98`).

## E. Directional spreading

For JONSWAP spectral input, `s` is the spreading exponent (no `dirspread` keyword in this code).

Implementation: cosine over half-angle (`waveparamsnew.F90:653-665`):
```
tempdir = (ang − mainang) / 2
Dd = cos(tempdir)^(2*nint(s))
```
Effectively `cos^(2s)((θ−mainang)/2)`, normalized to unit directional integral.

For non-spectral stationary/TS forcing (`boundaryconditions.F90:276`): `cos(θ−θ₀)^m`, clipped at zero, normalized.

`sprdthr` does **not** set directional width — it chooses the frequency band around peak: `where(Sf > sprdthr*maxval(Sf))` (`waveparamsnew.F90:1775`). Defaults: `0.08` for surfbeat, `0.00` for nonh (`params.F90:469`).

## F. Datastore (`wave_boundary_datastore.F90`)

Persists newer-interface state across calls. Holds:

**Static boundary parameters** (`:16`):
- Master filename, `np`, `ntheta`, reference coordinates, boundary depth.
- `nonhspectrum, sprdthr, trepfac, theta, xb/yb, random seed, nspr, rho, nmax, fcutoff`.

**Administration timestamps** (`:42`):
- `initialized, startComputeNewSeries, startCurrentSeries`.

**Spectrum administration** (`:50`):
- Number of spectra, filenames/list positions, repeat flag.
- Generation count, spectrum end time.
- `lastwaveelevation`, spectrum coordinates, computed `Hbc/Tbc/Dbc`.

**Generated time series** (`:63`):
- `eebct, qxbct, qybct` (surfbeat).
- `zsbct, ubct, vbct, wbct` (nonh).
- `tbc` (time vector).

## G. Reflection / absorption / nonh BC

Front options (`params.F90:504`): `abs_1d, abs_2d, wall, wlevel, nonh_1d, waveflume`.
Back options (`:535`): `wall, abs_1d, abs_2d, wlevel`.

`order` limited to `1..2` (`params.F90:553`):
- 1st = short-wave energy only.
- 2nd = adds bound long-wave steering.

Front BC behavior:

| Front | Behavior | Code |
|---|---|---|
| `FRONT_ABS_1D` | Radiating with imposed `ui`, mean flow, η deviation | `boundaryconditions.F90:1202` |
| `FRONT_ABS_2D` | Weakly reflective Van Dongeren-style; iterates reflected angle/amplitude; uses imposed `ui` if `ARC=0`, adds reflected `ur` if `ARC=1` | `:1222, 1260, 1283` |
| `FRONT_WALL` | Boundary `uu=0` | `:1302` |
| `FRONT_NONH_1D` | If `ARC=0`: directly imposes `ui/vi/zi/wi`. If `ARC=1`: radiating short-wave form | `:1307` |

Nonh mode auto-changes `front` to `nonh_1d` if needed (`params.F90:1724`).

Spectral and `ts_nonh` forcing reads velocity/elevation time series via `velocity_Boundary` (`boundaryconditions.F90:709, 778, 858`). For surfbeat, `order=1` zeroes generated long-wave flux/elevation in `generate_qbcf` (`waveparamsnew.F90:2974`); runtime also scales `ui` by `lwave*(order−1)` when `nonhspectrum<=0` (`boundaryconditions.F90:918`).

## Decision Guide

| Need | Setting |
|---|---|
| Parametric JONSWAP from `Hm0, Tp` | `wbctype=parametric`, set `Hm0, Tp, mainang, gammajsp, s` |
| Time-varying spectra | `wbctype=jons_table` or `vardens` with `FILELIST` |
| SWAN spectrum hand-off | `wbctype=swan`, supply SWAN 2D spectrum file |
| Reproducibility (reuse prior BCF) | `wbctype=reuse` (skips regeneration) |
| Nonh wave-resolving forcing | `wbctype=ts_nonh` with `boun_U.bcf` |
| 1D analytic time series | `wbctype=ts_1` (or `ts_2` with bound long-wave) |
| Bound long-wave on incident sea+swell | `order=2` |
| Sea-swell only, no IG | `order=1` |
| Pure radiation BC at front | `front=abs_2d`, `ARC=1` |
| Pure imposed wave (no reflection) | `front=abs_1d`, `ARC=0` |
| Simple reflective shore at back | `back=wall` |
| Tide-only nesting | `back=wlevel` |

## Working Rules

- Use newer `waveparamsnew.F90` path (default) — it accepts `Tp` directly. Legacy uses `fp`.
- Default `dfj = fnyq/200` is fine for typical 5–30 s seas; increase resolution by setting `dfj` smaller for narrow-band spectra.
- `mainang` is in **nautical convention** (clockwise from N) — code converts internally.
- `random=0` for reproducible BCF generation (default 1 = random seed).
- For `FILELIST` time-varying BC, ensure the first row's `rtbc` covers your spin-up, otherwise spectra recycle.
- The `wave_bc_nextgen.f90` scaffold is **not** active — don't waste time editing it.
- `sprdthr` default `0.08` is good for typical sea-states; set higher (0.15+) for very narrow-band spectra.
- For nonh runs, `front=nonh_1d` is auto-set if you forget — check the warning log to confirm.

## Common Pitfalls

- ▢ Setting `Tp` in legacy `waveparams.F90` codepath — it reads `fp`; results will be wrong by `fp²` factor.
- ▢ Confusing `s` (directional spread exponent) with `sprdthr` (frequency-band cutoff) — they do different things.
- ▢ `mainang` in cartesian convention (CCW from E) — it's nautical (CW from N); off by 90° if confused.
- ▢ Forgetting `random=0` for sensitivity tests — generated BCF will differ between runs.
- ▢ `wbctype=jons` (the old name) — translates to `parametric`. Use `parametric` directly to avoid confusion.
- ▢ `order=2` with very short window — bound long-wave generation needs sufficient series length to avoid wrap-around.
- ▢ `front=wall` on a wave-incident boundary — model runs but waves don't enter; check by plotting `s%ee` near boundary.

## Next expansion

- SWAN-XBeach spectrum hand-off recipe.
- Bound long-wave generation theory and validation.
- `vardens` (variable density spectrum) format walkthrough.

## References

- Roelvink et al. 2009 (XBeach BC formulation).
- Van Dongeren et al. 2003 (weakly reflective BC).
- Hasselmann et al. 1973 (JONSWAP).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/xbeach/source_code/trunk/src/xbeachlibrary`. Auto-draft = false; review_required = true.
