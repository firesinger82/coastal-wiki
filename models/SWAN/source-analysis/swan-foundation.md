---
title: "swan foundation"
topic: general
canonical_source: self
citation_status: verified
verification_method: "SWAN source code 직접 분석 (models/SWAN/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/swan-foundation.md (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# SWAN — wave physics, numerics, and I/O foundation

## Scope note

A foundation reference for SWAN (Simulating WAves Nearshore) covering:
- the **action balance equation** that SWAN solves,
- the **propagation** scheme (geographic and spectral space, sweeping algorithm),
- the **source/sink** physical processes available,
- the **boundary condition** options,
- the **stationary vs nonstationary** mode decision,
- key **numerical scheme** choices (BSBT/SORDUP/SecondOrder/Lock-up).

This note treats SWAN's content end-to-end so subsequent notes can dive into specific subsystems (wind input, breaking, nesting, output) without re-establishing context.

## Source basis

Citations from the `manuals` collection filtered to `model=swan` (~902 chunks: 4 official PDFs `swanuse/swantech/swanimp/swanpgr` + 195 online_doc HTML chapters from `swanmodel.sourceforge.io`). Source code is at `gitlab.tudelft.nl/citg/wavemodels/swan` and is not directly cited in this foundation note (SWAN's Fortran is non-trivial to map subroutine-by-subroutine; reserved for a later subroutine-inventory note).

## 1. The action balance equation

SWAN is a **third-generation phase-averaged spectral wave model** based on the action balance equation. It computes the evolution of the wave action density `N(σ,θ;x,y,t)` (action = energy / relative frequency) as a function of geographic position, time, frequency, and propagation direction `[file=pdf:swan:swantech section="Chapter 1 Introduction > 1.4 Scope of this document" page=10]`.

The governing equation is:
```
∂N/∂t + ∂(cx·N)/∂x + ∂(cy·N)/∂y + ∂(cσ·N)/∂σ + ∂(cθ·N)/∂θ = Stot/σ
```
where `cx, cy, cσ, cθ` are the propagation velocities in geographic (`x,y`) and spectral (`σ,θ`) space, and `Stot` is the sum of source/sink terms.

**Why action density rather than energy density?** Action `N = E/σ` is conserved in slowly varying media even when energy is not. The wave-action conservation form is the standard for spectral wave models (WAM, WAVEWATCH III, SWAN).

**Why relative frequency `σ`?** Internally SWAN uses the relative (intrinsic) frequency to keep formulations clean in current. Output to the user can be transformed to absolute frequency `[file=website:swan:node61 section="Transformation from relative to absolute frequency"]` — relevant when validating against fixed-position wave-buoy measurements.

## 2. Propagation

### 2.1 Geographic space (cx, cy)

In the absence of currents, propagation velocity equals group velocity `(cg,x, cg,y)`. With currents, the velocities differ because the wave crest moves at phase speed but the energy moves at group speed `[file=pdf:swan:swantech section="Chapter 3 Numerical approaches > 3.5"]`.

### 2.2 Spectral space (cσ, cθ)

Refraction (cθ) and shifting in frequency (cσ) come from spatial gradients of depth and current. These spectral velocities are zero in deep water with no current.

### 2.3 Numerical scheme — sweeping + BSBT

SWAN's solver uses **directional sweeping** in geographic space, processing four quadrants of (cx, cy) signs in sequence:
- Quadrant 1: cx > 0 and cy > 0
- Quadrant 2: cx < 0 and cy > 0
- Quadrant 3: cx < 0 and cy < 0
- Quadrant 4: cx > 0 and cy < 0

For each sweep, propagation is implicit upwind. Default scheme is **BSBT** (Backward Space, Backward Time) — first-order upwind, robust, dissipative. Alternative schemes:
- `SORDUP` — second-order upwind for stationary
- `SecondOrder` — for nonstationary higher accuracy
- See `[file=pdf:swan:swantech section="Chapter 3.2.2 Note on the choice of scheme" page=83]`

BSBT is the default for shallow-water coastal/estuary work because of its robustness against spectral oscillation; it is somewhat dissipative on long swells over large grids.

### 2.4 Action-density limiter and under-relaxation

To stabilize source terms (especially wind input and quadruplet interactions), SWAN applies an **action density limiter** that bounds the per-iteration change of N `[file=pdf:swan:swantech section="Chapter 3.7 Action density limiter and under-relaxation" page=98]`:
```
∆Ni,j,l,m  ←  ∆Ni,j,l,m / max(1, |∆Ni,j,l,m|/limit)
```
In practice this matters mostly for stationary mode where iteration convergence depends on it. Most users do not need to tune it.

## 3. Source and sink processes

SWAN's source-term ledger `Stot = Sin + Snl3 + Snl4 + Sds + Sother` covers:

| Process | Symbol | Representative formulation | Activation flag |
|---------|--------|----------------------------|-----------------|
| Wind input | `Sin` | Snyder/Komen, Janssen, Yan, ST6, Rogers — choice via GEN1/GEN2/GEN3 | `GEN3` for full third-generation |
| Whitecapping | `Sds,w` | Hasselmann, Westhuysen, ST6 | `WCAP` |
| Quadruplet wave-wave (4-wave) | `Snl4` | DIA (Discrete Interaction Approximation) | `QUADrupl` |
| Triad wave-wave (3-wave) | `Snl3` | LTA (Lumped Triad Approximation) | `TRIad` |
| Depth-induced breaking | `Sds,br` | Battjes-Janssen, alpha/gamma | `BREaking` |
| Bottom friction | `Sds,b` | JONSWAP, Madsen, Collins | `FRICtion` |
| Vegetation, mud, sea ice, turbulence | `Sds,*` | various | optional |
| Bragg scattering | `Sbr` | Ardhuin & Herbers (2002) | optional |

The full process list with on/off flags per release is in `[file=website:swan:node13 section="Activation of physical processes"]`. SWAN ships a curated default per `MODE STATIONARY` / `NONSTATIONARY` setup; users override individual processes via dedicated commands.

**Practical note on whitecapping** — Whitecapping in SWAN is primarily steepness-controlled (pulse-based, Hasselmann 1974 / WAMDI 1988). For stratified shallow seas the default is usually fine; for fetch-limited cases consider the ST6 set of source terms.

**Practical note on triads** — Triad interactions transfer energy from primary peak to super-harmonics. Important in the surf zone. Off by default; activate via `TRIad` in the command file when modeling shoaling/breaking near the coast.

## 4. Boundary and initial conditions

The action balance equation is hyperbolic and requires **wave boundary conditions** at up-wave open boundaries `[file=pdf:swan:swantech section="Chapter 4 Wave boundary and initial conditions" page=125]`. Options (cited via `BOUND` command in the command file):

| Option | Meaning | Use case |
|--------|---------|----------|
| Parametric 1D (JONSWAP, PM, Gaussian) | Hs, Tp, γ; SWAN expands to 2D internally | First-pass synthetic forcing |
| Parametric 2D | Hs, Tp, γ + directional spread | When directional content matters |
| 2D spectrum from file (`BCspectra`) | full energy spectrum E(σ,θ) | Nesting from another SWAN/WAVEWATCH run |
| Per-point 1D / 2D from file | spatially varying along boundary | Realistic large-domain coupling |

Land boundaries automatically reflect/absorb according to land-water mask. Water boundaries beyond the model domain absorb energy that propagates outward.

For **nesting**, write a coarse-grid run with `NGRID` outputs (boundary spectrum file), then use `BOUND NEST 'sname' 'fname'` in the fine-grid run. Source code path: `swan/src/swanpre2.ftn` lines 2479 (BOUNDARY), 1984 (NESTOUT) — see also the code-qa skill output.

### 4.1 Initial conditions

Stationary runs do not need initial conditions — SWAN iterates from zero. Nonstationary runs accept:
- `INITial DEFAULT` — internally seed from JONSWAP at boundary
- `INITial PARametric` — synthetic Hs/Tp seed
- `INITial HOTStart` — restart from `.hot` file produced by previous run

## 5. Stationary vs nonstationary mode

The `MODE` command selects:

| Mode | When to use | Time stepping |
|------|-------------|---------------|
| `STATIONARY` | quasi-equilibrium wave field with steady forcing (typical engineering hindcast for a fixed wind state) | iterates within one snapshot until convergence |
| `NONSTATIONARY` | time-varying winds (storm passage), time-varying currents, evolving boundary | implicit time stepping with `DT` from command file |

Decision points:
- **Wind/forcing changes appreciably across the simulation window** → nonstationary.
- **Single design event, snapshot wind** → stationary (much cheaper).
- **Coupled with hydrodynamics (ADCIRC-SWAN, Delft3D-WAVE)** → nonstationary required.

Convergence of stationary runs is monitored via residual on Hs / change-per-iteration. Nonstationary uses a fixed `DT` (e.g., 10–30 min for storm passages); too large and nonlinear source terms get under-resolved.

`[file=website:swan:node34 section="Lock-up"]` discusses stationary lock-up — SWAN waits for the action density to stabilize before proceeding.

## 6. Output

SWAN writes via `BLOCK`, `TABLE`, `SPECout`, `NESTout` commands. Common outputs:
- 2D fields (`BLOCK`): Hs, Tp, mean direction, peak direction, wave length, etc.
- Time series at points (`TABLE`): same parameters at lat/lon stations
- Full 2D spectra (`SPECout`): energy spectrum E(σ,θ) at points, for downstream analysis or nesting
- Boundary nest files (`NESTout`): 2D spectra along a line, for downstream finer-grid runs

Output grids can differ from the computational grid `[file=website:swan:node12 section="Output grids"]`. This decouples model resolution from analysis resolution.

## 7. Decision Guide — SWAN run type

| Question | Stationary | Nonstationary |
|----------|-----------|---------------|
| Wind stationary across run window? | Yes | No |
| Storm passage / time-varying forcing? | No | Yes |
| Coupled with circulation (ADCIRC/Delft3D)? | No | Yes |
| Triad / breaking on shallow flat bathymetry? | OK | OK (triad needs short DT) |
| Computational budget tight? | Stationary cheaper | Nonstationary expensive |

| Bottom condition | Recommended scheme |
|-----------------|---------------------|
| Smooth shelves, large grids | BSBT (default), maybe SORDUP for stationary |
| High shoaling rates, surf zone | SecondOrder + TRIad on |
| Long swells, low frequencies | tighten frequency discretization (`SET FREQ`) |

## 8. Working Rules

1. **Define the spectral grid before everything.** Frequency range (typically 0.04–1.0 Hz) and direction sectors (24 or 36 sectors) drive every later cost. Doubling sectors doubles run time.
2. **Boundary condition is the dominant uncertainty.** A stationary run with parametric JONSWAP and wrong `Hs/Tp` produces precisely-wrong wave heights inland. Validate boundary against buoy or coarse-grid spectrum first.
3. **Triads are off by default.** In surf-zone shoaling work, you must explicitly turn `TRIad` on or you'll under-predict secondary peaks.
4. **For nesting, NEVER mix domains with different spectral grids.** SWAN requires the same `SET FREQ`/`SET DIR` between coarse and fine.
5. **Stationary-mode iteration limit (`SET MAXIT`) matters for convergence on stiff source terms.** Increase if Hs residuals don't drop.

## 9. Common Pitfalls

- **JONSWAP `γ` typo** — Default γ=3.3 is reasonable for wind-driven wave but wrong for swell. Set explicitly.
- **Stationary on storm event** — looks fine but propagates an "average" wave, missing the surge phase.
- **Mixing GEN3 with bottom-friction-off** — GEN3 wind input grows with fetch; without dissipation the spectrum runs away.
- **Output points outside the computational grid** — silently dropped from `TABLE` output. Verify station list against grid bounding box.
- ▢ **User-experience cases** — placeholder for project-specific incidents (regional Korea coast tuning, JMA wind input nesting, etc.).

## 10. Next Expansion

- Per-source-term deep dive (Sin formulations, ST6 vs WAM, Battjes-Janssen variants).
- Nesting workflow (NGRID → BOUND NEST) with file format details.
- ADCIRC-SWAN unstructured coupling notes (separate file; relevant for users running the unstructured-mesh SWAN variant via the ADCIRC-SWAN testsuite).
- Output post-processing (BLOCK to NetCDF, TABLE to ASCII, SPECout consumption).
- SWAN subroutine inventory once `map-subroutines` runs on it (currently in progress).

## References

### Primary (PDFs)

- `[file=pdf:swan:swantech]` — Scientific/Technical documentation (governing equations, numerics).
- `[file=pdf:swan:swanuse]` — User Manual (commands, file formats).
- `[file=pdf:swan:swanimp]` — Implementation Manual.
- `[file=pdf:swan:swanpgr]` — Programmer Manual.

### Online doc (per-chapter HTML, swanmodel.sourceforge.io)

- `[file=website:swan:node12]` — Output grids.
- `[file=website:swan:node13]` — Activation of physical processes (per-process flag matrix).
- `[file=website:swan:node27]` — Boundary and initial conditions.
- `[file=website:swan:node34]` — Lock-up (stationary convergence).
- `[file=website:swan:node61]` — Transformation from relative to absolute frequency.
- `[file=website:swan:node64]` — Wave boundary and initial conditions.

### Key swantech sections

- Chapter 1.4 (page 10) — model scope.
- Chapter 2.2 (pages 18–19) — propagation kinematics.
- Chapter 2.3 (pages 21–52) — source and sink terms.
- Chapter 3.2 (pages 79–83) — discretization and BSBT.
- Chapter 3.5 (pages 93–96) — sweeping algorithm.
- Chapter 3.7 (pages 98–100) — action density limiter.
- Chapter 4 (pages 125–126) — boundary conditions.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 (this session) |
| Generated | 2026-05-06 |
| RAG retrieval | rag_proxy on `manuals` filtered `model=swan` (902 chunks across pdf+website doc_types) |
| Coverage | wave physics, numerics, sources, BC, modes, output (foundation level — does not enumerate every command) |
| Review status | `review_required: true` — modeler should verify section numbers against current swantech page numbering |
| Companion notes (planned) | swan-source-terms-detailed, swan-nesting-workflow, swan-adcirc-coupling |
