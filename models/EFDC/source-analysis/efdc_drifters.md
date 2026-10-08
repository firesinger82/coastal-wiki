---
title: "efdc drifters"
topic: general
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_drifters.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

## Scope

EFDC+'s drifter module: directory and procedural Fortran structure (no classes), main entry points (`DRIFTER_INP, DRIFTER_CALC, DRIFTER_OUT`), particle release (`drifter.inp` only — old card C68 deprecated; per-particle fixed points with begin/end times; no area-release class), advection via RK4 with **inverse-distance-power-2 interpolation** (NOT strict trilinear), random walk (`RANDCAL` using model `AH/AV` or constant `LA_HORDIF/LA_VERDIF`), vertical settling via group `GRPWS`, particle status (`LLA, LLA_Global` codes for active/initialized/exited/settled), `EE_DRIFTER.OUT` binary + `efdc_drifters.nc` NetCDF output formats, and coupling to hydrodynamic state (`U2/V2/W2`, `AH/AV`, `HP/BELV/Z/ZZ`). Use this when wiring oil-spill simulation, conservative tracer particles, or larvae transport.

## Source basis

- `Drifter/mod_drifter.f90:21-2754` — main module.
- `Drifter/mod_Variables_MPI_Drifter.f90:13-64` — MPI state.
- `MPI_Communication/mod_Communicate_Drifters.f90:12-35` — MPI exchange.
- `aaefdc.f90:1106-1107` — `DRIFTER_INP` call.
- `hdmt.f90:1378-1384`, `hdmt2t.f90:1062-1067` — `DRIFTER_CALC` call.
- `input.f90:3185` — old C68 deprecated.

## A. Directory, entry points

Main module: `Drifter/mod_drifter.f90`, `MODULE DRIFTER` at `:21`.

**Procedural Fortran, not class-based**. Persistent module state: particle lists, release windows, groups, settling velocity, MPI ownership (`:46-68`).

Main entry points:
- `DRIFTER_INP` (`:793`): reads `drifter.inp`, allocates/initializes.
- `DRIFTER_CALC` (`:91`): advances particles each hydro step.
- `DRIFTER_OUT` (`:676`): writes trajectory.
- NetCDF helpers: `create_nc_lpt, close_nc_lpt, write_nc_lpt` (`:2617, 2708, 2718`).

MPI support:
- Drifter MPI state: `mod_Variables_MPI_Drifter.f90:13-64`.
- Ghost-domain communication: `mod_Communicate_Drifters.f90:12-35`.

Setup/call sites:
- `aaefdc.f90:1106-1107`: `DRIFTER_INP` when `ISPD > 0`.
- `hdmt.f90:1378-1384`, `hdmt2t.f90:1062-1067`: `DRIFTER_CALC`.

## B. Particle release

EFDC+ does **NOT** use old EFDC card C68 (`input.f90:3185` says "not used in EFDC+").

Drifter input from **`drifter.inp`** (`Drifter/mod_drifter.f90:814`).

Control line (`:816`):
```
LA_ZCAL, LA_PRAN, LA_DIFOP, LA_HORDIF, LA_VERDIF,
DEPOP, ADJVERP, SLIPFACTOR, IOSWD, OSWDA, OSWDB
```

Global release window + output frequency (`:818`).
Particle count + group count (`:820`).

**Group properties** (`:923-929`):
- Oil flag.
- Settling velocity `GRPWS`.
- Bed-fix flag `BEDFIX`.

**Per-particle fixed-point releases** (`:972-984`):
- If `DEPOP == 1`: `XLA, YLA, DLA, LA_BEGTI, LA_ENDTI, LA_GRP`.
- Otherwise: `XLA, YLA, ZLA, LA_BEGTI, LA_ENDTI, LA_GRP`.

Time scheduling per particle:
- Active-day list filtering (`:253-263`).
- Release initialization when current time reaches `LA_BEGTI(NP)` (`:314-319`).

**No separate area-release or release-time-series class**. "Area" appears in `INIT_OIL` for oil-spill surface area (`:2313-2329`) — particles already defined.

## C. Advection / interpolation

LA_DIFOP가 0이 아니거나 ISHDMF가 0이면 코드 위치 갱신은 Euler 경로를 사용한다. (`Drifter/mod_drifter.f90:389` — `if( LA_DIFOP /= 0 .or. ISHDMF == 0 )then`; `Drifter/mod_drifter.f90:410` — `KDX1 = DELTD*(U2NP + DAHX1)`) 그 밖의 경우 코드 위치 갱신은 RK4 경로를 사용한다. (`Drifter/mod_drifter.f90:467` — `XLA(NP) = XLA1 + (KDX1 + 2.0*KDX2 + 2.0*KDX3 + KDX4)/KWEIGHT`) RK4의 공간 보간 단계는 같은 U2·V2·W2 유속 배열을 사용한다. (`Drifter/mod_drifter.f90:467` — `XLA(NP) = XLA1 + (KDX1 + 2.0*KDX2 + 2.0*KDX3 + KDX4)/KWEIGHT`) Theory의 단계별 시간 인자와 이 코드 시간 수준을 구별한다. (`Drifter/mod_drifter.f90:389` — `if( LA_DIFOP /= 0 .or. ISHDMF == 0 )then`; `Drifter/mod_drifter.f90:410` — `KDX1 = DELTD*(U2NP + DAHX1)`; `Drifter/mod_drifter.f90:467` — `XLA(NP) = XLA1 + (KDX1 + 2.0*KDX2 + 2.0*KDX3 + KDX4)/KWEIGHT`)

Particle velocity: `DRF_VELOCITY` (`:1858`).

**Important**: code comment says **inverse-distance-power-2** interpolation, NOT strict trilinear (`:1846-1848`).

Horizontal velocities reconstructed at cell centroids from face velocities:
- Bottom layer: `UKB, VKB` from `U2, V2, RSSBC*, STCUV` (`:1916-1918`).
- Top layer: `UKT, VKT` (`:1920-1927`).

Vertical interpolation for horizontal velocity uses `ZSIG, ZCTR, DZCTR` (`:1932-1940`).

Vertical velocity `W2` linearly interpolated between layer interfaces (`:1942-1948`).

Horizontal **inverse-distance weighting over 3×3 neighbor stencil** accumulates (`:2017-2023`); returns `U2NI, V2NI, W2NI` (`:2027-2029`).

코드는 인접 위치의 유속을 공간 가중치로 보간한다. (`Drifter/mod_drifter.f90:1917` — `UKB  = 0.5*STCUV(L)*( RSSBCE(L)*U2(LE,K1) + RSSBCW(L)*U2(L,K1) )`; `Drifter/mod_drifter.f90:1926` — `UKT  = 0.5*STCUV(L)*( RSSBCE(L)*U2(LE,K3) + RSSBCW(L)*U2(L,K3) )`) 정적 원문 대조는 보간 방식의 존재를 확인한다. (`Drifter/mod_drifter.f90:1917` — `UKB  = 0.5*STCUV(L)*( RSSBCE(L)*U2(LE,K1) + RSSBCW(L)*U2(L,K1) )`; `Drifter/mod_drifter.f90:1926` — `UKT  = 0.5*STCUV(L)*( RSSBCE(L)*U2(LE,K3) + RSSBCW(L)*U2(L,K3) )`) 다른 보간 방식과의 수치 분산 크기 비교는 확인하지 않음. (`Drifter/mod_drifter.f90:1917` — `UKB  = 0.5*STCUV(L)*( RSSBCE(L)*U2(LE,K1) + RSSBCW(L)*U2(L,K1) )`; `Drifter/mod_drifter.f90:1926` — `UKT  = 0.5*STCUV(L)*( RSSBCE(L)*U2(LE,K3) + RSSBCW(L)*U2(L,K3) )`)

## D. Random walk diffusion

Controls documented (`:777-788`).

Step scales precomputed:
```
DIFFH = SQRT(2 · LA_HORDIF · DELTD)
DIFFV = SQRT(2 · LA_VERDIF · DELTD)
```
(`:280-281`).

Applied **after** RK4 (`:481-482`).

`RANDCAL` (`:2033`):

**Horizontal**:
- Enabled for `LA_PRAN == 1` or `3` (`:2038-2039`).
- Uses model `AH(L,K)` when `LA_DIFOP == 0`, else constant `DIFFH` (`:2040-2044`).
- Adds random displacement to `XLA, YLA` (`:2045-2051`).

**Vertical**:
- Enabled for `LA_PRAN >= 2` AND `LA_ZCAL == 1` (`:2054-2055`).
- Uses model `AV(L,K)` or constant `DIFFV` (`:2056-2060`).
- Adds random displacement to `ZLA` (`:2061-2065`).

When `LA_DIFOP == 0`, drift due to diffusivity gradients added through `DIFGRAD` during RK passes (`:409, 427, 445, 464, 2195-2245`).

## E. Vertical settling / buoyancy

Each group has `GRPWS` = "Settling velocity of drifter [m/s]" (`:847-850`), read from `drifter.inp` (`:925-929`).

Vertical RK update **subtracts** settling/rising from interpolated `W2NP`:
```
KDZ = DELTD · (W2NP - GRPWS(NW) + DAVZ...)
```
(`:415, 433, 451, 470`).

If `LA_ZCAL == 0`, vertical position **fixed** at initial depth: `ZLA = HPLA + BELVLA - DLA` (`:417-474`).

**Oil buoyancy special case**: if oil density < 1000 AND `GRPWS == 0`, particle forced near surface at `DLA = 0.005` (`:1212-1217`).

코드 소멸 기준은 DVOL≤10⁻⁹ m³이다. (`Drifter/mod_drifter.f90:324` — `if( DVOL(NP) <= 1D-9 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 246쪽·인쇄 233쪽) 이 부피는 1 mm³이다. (`Drifter/mod_drifter.f90:324` — `if( DVOL(NP) <= 1D-9 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 246쪽·인쇄 233쪽) Confluence도 1 mm³를 사용한다. (`models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Lagrangian_Particle_Tracking/Oil_Spill_Modeling_with_LPT.md:23` — `It should be noted that EFDC will cause the drifter to disappear when the oil per drifter is less than 1.0 mm3. The user may manually choose to hide concentrations of oil higher than this by using the crop below in *2DH View*. For post-processing of the oil simulation, *2DH View* provides several options for displaying the oil. Oil thickness, mass, and volume may also be displayed.`; EFDC_Theory_Document_Ver_12.pdf, PDF 246쪽·인쇄 233쪽) Theory PDF 246쪽은 질량 10⁻⁹ kg로 설명한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 246쪽·인쇄 233쪽)

## F. Particle status

Main status variables:
- `JSPD = 1`: not initialized; `JSPD = 0`: initialized (`:945-947`).
- `LLA(NP)`: local cell index.
- `LLA_Global(NP)`: global cell/status (output + MPI) (`:858-872`).

Active particles: `LLA >= 2` AND `LLA_Global >= 2`. Skipped if `LLA < 2` (`:368-369`).

End-of-tracking-window:
- Initialized + past `LA_ENDTI` → `LLA_Global = 1`; else `0`. Local `LLA = 0` (`:300-310`).

Settled/deposited:
- If `BEDFIX(group) == 1` AND particle reaches bed: `LLA = 0, LLA_Global = 1` (`:336-347`).

Dry-cell stop:
- `LLA = 0, LLA_Global = 1` when bed-fixed particle in dry cell (`:352-361`).

Exit / outside:
- `SET_DRIFTER_OUT` sets `LLA = 1, LLA_Global = 1` (`:1763-1776`).
- Open-boundary exit (`:1600-1612`).
- Withdrawal/outflow exit (`:1617-1637`).
- Hydraulic-structure outside (`:1714-1745`).

**"Beached" not represented as named status**. Near-wall handling moves particle back/onto valid edge, flags `BEDGEMOVE = .TRUE.` (`:1444-1528`).

## G. Trajectory output

Binary: `OUTDIR // 'EE_DRIFTER.OUT'`, created on first call (`:145-164`).

Header (`:158-161`):
- `VER, HSIZE`.
- `NPD, KC, XYZSCL`, oil flag.

Per-output record (`:723-749`):
- `EETIME`, active count `NACT`.
- Normal: `NP, LLA_Global, IX, IY, IZ` (coords scaled by `XYZSCL`).
- Oil: adds `IV = NINT(1D6 * DVOL)` (cubic cm).

NetCDF: `efdc_drifters.nc` (`:2628-2697`):
- Dimensions: `TRACKS = NPD`, unlimited `TIME`.
- Variables: `time, lat, lon, elev`; optional `oil_vol, oil_mass`.
- Maps model x/y to lon/lat if needed.

## H. Coupling with hydrodynamic state

Caller advances drifters after mean mass transport (`hdmt.f90:1370-1384`, `hdmt2t.f90:1057-1067`).

Time step: `DT` or `DTDYN` depending on dynamic time-step flag (`:123-128`).

Position/depth: uses `HP, H1P, BELV, Z, ZZ` (`:383-386, 1201-1209, 2103-2180`).

Velocity: hydrodynamic `U2, V2, W2`, face masks/scales `RSSBC*, STCUV`, neighbor maps `LEC, LNC, LADJ` (`:1906-1948`).

Diffusion: `AH, AV` for random walk + diffusivity-gradient drift (`:2040-2241`).

Grid/mask: `XCOR, YCOR, AREA, INSIDECELL, SUB/SVB/SUB3D/SVB3D, KSZ, KC` (`:1150-1839`).

Boundary/structure: `LPBN/LPBS/LPBE/LPBW, QSUM, BCPS, WITH_RET, HYD_STR` (`:1600-1745`).

Wind/oil: `WNDVELE, WNDVELN, WINDST`, temperature `TEM` (`:2076-2090, 2269-2301`).

## Decision Guide

| Application | Setup |
|---|---|
| Conservative passive tracer | `LA_PRAN=0`, `LA_ZCAL=1`, `GRPWS=0` |
| With horizontal random walk | `LA_PRAN=1`, `LA_HORDIF=1.0` (or use `AH`) |
| With both H + V random walk | `LA_PRAN=3` |
| Settling sediment | `GRPWS=0.001 m/s` (or measured) |
| Buoyant oil (3D) | Group with oil flag, `GRPWS=0` (auto-buoyant) |
| Larvae with vertical migration | `LA_ZCAL=1`, `LA_PRAN=3`, time-varying `GRPWS` (modify code) |
| Drifters fixed at bed | `BEDFIX=1` |
| Drifters fixed at depth | `LA_ZCAL=0` (no vertical motion) |
| Korean coast oil spill | Group with oil flag, wind drift `OSWDA, OSWDB` calibrated |

## Working Rules

- Particle count: 1000-10000 typical; cost scales linearly.
- For oil spills, separate groups for surface oil, dispersed droplets, evaporated.
- `LA_HORDIF, LA_VERDIF`: typical 0.1-1 m²/s (constant); or use model `AH/AV`.
- Random-seed reproducibility: not built in; for reproducibility, use `LA_DIFOP=1` (constant) and seed RNG externally.
- Output frequency: balance trajectory smoothness vs file size.
- For Korean tidal oil spill: particles often re-enter via rebound at coast — verify `BEDGEMOVE` events.
- NetCDF output preferred over binary for analysis.

## Common Pitfalls

- ▢ Looking for old C68 card — deprecated; use `drifter.inp`.
- ▢ Expecting trilinear interpolation — actually inverse-distance-power-2 (slightly more diffusive).
- ▢ Setting `LA_PRAN=2` (vertical only) without `LA_ZCAL=1` — vertical random walk silently disabled.
- ▢ Group with negative `GRPWS` (rising) without proper init — vertical position drifts upward forever.
- ▢ Oil density < 1000 AND `GRPWS != 0` — overrides settling; force surface; verify intended behavior.
- ▢ Boundary exit not detected — check `LPBN/LPBS` etc. consistency.
- ▢ "Beached" particles disappear — actually `LLA=0, LLA_Global=1`; check status.
- ▢ MPI runs: drifter ownership transfers across ranks via `mod_Communicate_Drifters` — debug with per-PE log.

## Next expansion

- Oil-spill workflow recipe (Korean Coast).
- Larvae vertical-migration custom code.
- Random seed reproducibility.

## References

- Visser 1997 (random walk theory).
- ASCE 1996 (oil-spill modeling).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
