---
title: "XBeach Kingsday technical reference (2015 v1.22 r4567)"
model: XBeach
layer: 2
depends_on: []
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "Exhaustive locator/provenance cross-reference for XH001-XH207 using OpenDataLoader v2.4.7 page-aware PDF extraction, original DOCX document-order blocks, and original-bound OLE DOC text extracts; semantic dispositions inherited from immutable X00 with targeted independent spot checks"
verification_by: "Codex (cross-ref)"
verification_date: 2026-09-09
note_author: "Codex"
note_date: 2026-09-09
source_scope: "XBeach Kingsday technical reference 2015 v1.22 r4567"
---

# XBeach Kingsday technical reference (2015 v1.22 r4567)

이 문서는 XBeach 문서 전수검수의 HIGH 207건 중 이 출처에 속하는 판본 한정 판정을 통합한다. 문서의 설명은 다른 판본이나 현재 코드의 기본값으로 자동 확장하지 않는다. PDF 인용은 physical page와 문서 자체의 printed page를 구분한다. DOCX locator는 원본 문서의 문단·표 행 순서와 직접 인용을 쓰며 PDF page를 부여하지 않는다. OLE DOC의 부분 정렬 항목은 원본에 결박된 text extract의 행·해시·직접 인용과 보고서 printed section만 기록하고 physical page를 주장하지 않는다. 같은 work의 reciprocal DOC/DOCX↔PDF 후보는 공동검토 묶음으로 배치했지만 두 finding은 독립 원장 항목이며 묶음이 의미 동일성을 주장하지 않는다.

## 검증 범위

XH001-XH207의 원본 정체·해시·표현 행·페이지 또는 문서 block locator는 전수 확인했다. `cross-format-partial` 15건은 불완전한 PDF 정렬을 citation으로 쓰지 않고, DOCX 9건은 원본 block, OLE DOC 6건은 원본에 결박된 text-extract 행과 직접 인용으로 대체했다. 의미 판정은 immutable X00 전수독해 결과를 보존하며, 별도의 독립 의미 재독해는 posdwn, 손상된 vardens, standing-wave, 1D solver, NetCDF와 DOCX retrieval 표본에 집중했다. 따라서 공동검토 묶음은 중복 제거를 위한 의미 동치 판정이 아니다.

## 출처 고정

- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.docx` — SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`
- `models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.pdf` — SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`

## 모드·격자·좌표

<a id="xh042"></a>
<a id="xh076"></a>
### K-001 — XH042, XH076

**판정:** 판본 한정 사실로 채택.

- Grid/physical defaults include depthscale=1, g=9.81 m/s², rho=1025 kg/m³, 10° directional bins, limits -90° to 90° and Cartesian coordinates.
- Defaults include 'depthscale=1', 'g=9.81 m/s²', 'rho=1025 kg/m³', directional bins '10°', directional limits '−90° to 90°' and Cartesian 'thetanaut=0'.

**출처 locator:**

- XH042: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B598, B599, B600, B626, B627, B628, B629, B630, B631, B632, B633, B634, B635, B636 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 2135-2137,2141-2151); 직접 인용: “thetanaut | specify thetamin and thetamax in cartesian (0) or nautical (1) convention | 0 | 0 - 1 | -”; “thetamin | Lower directional limit (angle w.r.t computational x-axis) | -90.0 | -180.0 - 180.0 | deg”; “thetamax | Higher directional limit (angle w.r.t computational x-axis) | 90.0 | -180.0 - 180.0 | deg”. PDF page는 주장하지 않음.
- XH076: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.55, 56, 57, printed page/frontmatter 53, 54, 55, audit extract lines 2946-2958,3015-3064; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 비정수압 물리·수치법

<a id="xh002"></a>
### K-002 — XH002

**판정:** 판본 한정 사실로 채택.

- Non-hydrostatic pressure is assumed linear over depth with zero dynamic pressure at the surface, while vertical momentum advection and diffusion are described as negligible.

**출처 locator:**

- XH002: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.16, 30, printed page/frontmatter 14, 28, audit extract lines 253-255,524; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh005"></a>
<a id="xh055"></a>
### K-003 — XH005, XH055

**판정:** 판본 한정 사실로 채택.

- Breaking defaults include break=roelvink2, alpha=1, gamma=0.55, gamma2=0.3, gammax=2 and n=10, while the cited calibration concerns roelvink1 and the text distinguishes H³/h from H² dissipation scaling.
- The table defaults are 'break=roelvink2', 'alpha=1', 'gamma=0.55', 'n=10', 'gamma2=0.3' and 'gammax=2', although the prose says gamma and n were calibrated for roelvink1 and roelvink2 changes dissipation scaling from H² to H³/h.

**출처 locator:**

- XH005: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B247, B984, B987, B988, B989, B990, B991, B992, B993, B994, B995, B996, B997, B998 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 322,1287,2247-2258); 직접 인용: “… for option break=roelvink1. For break=roelvink2 the wave dissipation is proportional to H3/h instead of H2; this affects the calibration. For stationary runs the break=baldock …”; “facsd+ | Fraction of the local wave length to use for shoaling delay depth | 1.0 | 0.0 - 2.0 | -”; “n+ | Power in Roelvink dissipation model | 10.0 | 5.0 - 20.0 | -”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
- XH055: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.20, 75, 76, printed page/frontmatter 18, 73, 74, audit extract lines 613-691,3668-3730; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh041"></a>
<a id="xh093"></a>
### K-004 — XH041, XH093

**판정:** 판본 한정 사실로 채택.

- The non-hydrostatic scheme uses minmod ψ=max(0,min(r,1)), is second order in smooth regions and first order near sharp gradients, retains first-order source integration, and sets free-surface dynamic pressure to zero.
- The limited MacCormack predictor-corrector is second order in smooth regions and first order near discontinuities, with formally first-order source and turbulent-stress time integration.

**출처 locator:**

- XH041: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1948, B1949, B1950, B1951, B1957, B1973 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 1999-2010,2022,2072); 직접 인용: “… in regions where the solution is smooth, and reduces to first order accuracy near sharp gradients in the solutions to avoid unwanted oscillations. Furthermore, …”; “… consists of a first order predictor step and a flux limited corrector step. The hydrostatic pressure is integrated using the midpoint rule and central …”; “… and mass conservative. When first order computations are considered accurate enough is set to . For higher order accuracy the first order prediction is …”. PDF page는 주장하지 않음.
- XH093: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.135, 136, 138, 139, 140, 141, printed page/frontmatter 133, 134, 136, 137, 138, 139, audit extract lines 7547-7683,8468-8801,8879-8915,9151; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh046"></a>
<a id="xh085"></a>
### K-005 — XH046, XH085

**판정:** 판본 한정 사실로 채택.

- Numerical defaults include CFL=0.7, tstop=2000, maxerror=5×10^-5, maxiter=500, upwind=2, beta=0.1, roller=1, cats=4, hwci=0.1 m, eps=0.005 m, hmin=0.2 m and secorder=0.
- Defaults include 'CFL=0.7', stationary 'maxerror=5e−5 m' and 'maxiter=500', 'scheme=upwind_2', 'beta=0.1', 'roller=1', 'cats=4 Trep', 'hwci=0.1 m', 'eps=0.005 m', 'hmin=0.2 m' and 'secorder=0'.

**출처 locator:**

- XH046: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.100, 101, 108, 109, 110, printed page/frontmatter 98, 99, 106, 107, 108, audit extract lines 2574-2595; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH085: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.100, 108, 109, 110, printed page/frontmatter 98, 106, 107, 108, audit extract lines 4856-4862,5038-5118; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh050"></a>
<a id="xh089"></a>
### K-006 — XH050, XH089

**판정:** 판본 한정 사실로 채택.

- Non-hydrostatic defaults include Topt=10 s, viscfac=1.5, length factor 1, dispc=1, maxbrsteep=0.6, nhbreaker=2, tridiagonal solver, tolerance 0.005, 30 iterations and relaxation 0.92.
- Non-hydrostatic defaults include 'Topt=10 s', 'breakviscfac=1.5', 'breakvisclen=1', 'dispc=1', 'maxbrsteep=0.6', 'nhbreaker=2', 'solver=tridiag', 'solver_acc=0.005', 'solver_maxit=30' and 'solver_urelax=0.92'.

**출처 locator:**

- XH050: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.118, 119, printed page/frontmatter 116, 117, audit extract lines 2655-2669; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH089: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.118, 119, printed page/frontmatter 116, 117, audit extract lines 5434-5516; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh056"></a>
### K-007 — XH056

**판정:** 판본 한정 사실로 채택.

- The text gives uorb=πHrms/(Tp sinh(kh)), frictional dissipation coefficients 0.21 for wave groups and 0.28 for stationary waves, and reef wave-friction factors potentially at least 10 times the current-friction factor.

**출처 locator:**

- XH056: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.21, 22, printed page/frontmatter 19, 20, audit extract lines 811,827-885; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh058"></a>
### K-008 — XH058

**판정:** 판본 한정 사실로 채택.

- The manual gives roller dissipation Dr=2gβrEr/c and GLM velocities uL=uE+uS and vL=vE+vS with Stokes components proportional to Ew/(ρhc).

**출처 locator:**

- XH058: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.26, 27, printed page/frontmatter 24, 25, audit extract lines 1226-1236,1280-1292; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 빌드·MPI·버전 범위

<a id="xh018"></a>
<a id="xh072"></a>
### K-009 — XH018, XH072

**판정:** 판본 한정 새 사실로 채택.

- Landward wave entry is excluded, stationary waves require Neumann lateral boundaries, abs1d assumes one-dimensional behavior, cyclic boundaries require one alongshore MPI domain, and wbcversion=3 spectra must share time discretization and format.
- The documented boundary limits exclude landward wave forcing, restrict stationary lateral waves to Neumann conditions and abs1d to flume-like cases, and require MPI with a single domain for cyclic boundaries.

**출처 locator:**

- XH018: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.46, 47, 48, 50, printed page/frontmatter 44, 45, 46, 48, audit extract lines 834,870,879,899; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH072: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.46, 47, 48, 49, 50, 71, printed page/frontmatter 44, 45, 46, 47, 48, 69, audit extract lines 2701-2802,3502-3516; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh027"></a>
### K-010 — XH027

**판정:** 판본 한정 새 사실로 채택.

- Spatial spectra require 'wbcversion=3' and 'nspectrumloc=ns', interpolate energy rather than height linearly, and prohibit mixed spectrum formats or inconsistent FILELIST time discretizations.

**출처 locator:**

- XH027: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.71, printed page/frontmatter 69, audit extract lines 1245-1254; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh051"></a>
<a id="xh090"></a>
### K-011 — XH051, XH090

**판정:** 판본 한정 새 사실로 채택.

- The final tables give latitude=0°, Earth rotation=0.0417 hour^-1, automatic MPI decomposition with mmpi=2 and nmpi=4, and rotate=1.
- The tables specify 'lat=0°', 'wearth=0.0417 hour⁻1' defined as reciprocal rotation time, and MPI defaults 'mpiboundary=auto', 'mmpi=2', 'nmpi=4'.

**출처 locator:**

- XH051: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.119, 120, printed page/frontmatter 117, 118, audit extract lines 2671-2676; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH090: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.119, 120, printed page/frontmatter 117, 118, audit extract lines 5526-5570; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 지하수

<a id="xh039"></a>
### K-012 — XH039

**판정:** 판본 한정 사실로 채택.

- Infiltration uses first-order schemes with backward-Euler wetting-front updates and describes bed pressure as 'high-pass filtered at 4/Trep', a filter description requiring later verification.

**출처 locator:**

- XH039: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1888, B1889 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 1825-1829); 직접 인용: “… of non-hydrostatic surface water flow is high-pass filtered at 4/Trep, the superscript n corresponds to the time step number and Δt is the size …”; “… in cells where the groundwater and surface water are not connected and there exists surface water. As shown in the infiltration rate is a …”. PDF page는 주장하지 않음.
<a id="xh040"></a>
<a id="xh091"></a>
### K-013 — XH040, XH091

**판정:** 판본 한정 사실로 채택.

- The numerical appendix specifies second-order upwinding and leapfrog stepping, first-order backward Euler groundwater stepping, a stated high-pass period 4/Trep, Thomas solution in 1D and SIP solution in 2D.
- The groundwater pressure system is tridiagonal and solved by Thomas in 1D, but has five diagonals and uses Stone's Strongly Implicit Procedure in 2D.

**출처 locator:**

- XH040: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1907, B1908 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 1891-1893); 직접 인용: “… head curvature, and b contains the known forcing terms. For a one dimensional cross-shore case, A is reduced to a tridiagonal matrix. The vector …”; “… diagonals that are not placed along the main diagonal, and vector b contains additional forcing terms from the alongshore contribution. The solution to the …”. PDF page는 주장하지 않음.
- XH091: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.121, 125, 126, 129, printed page/frontmatter 119, 123, 124, 127, audit extract lines 5647,6137,6172,6218,6775-6780; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh049"></a>
<a id="xh088"></a>
### K-014 — XH049, XH088

**판정:** 판본 한정 사실로 채택.

- Groundwater defaults include aquifer depth -10 m, dwet=0.1 m, initial level 0 m, critical Reynolds number 100, parabolic head shape, laminar hydrostatic flow and kx=ky=kz=10^-4 m/s.
- Groundwater defaults include aquifer bottom '−10 m', 'dwetlayer=0.1 m', 'gw0=0 m', 'gwReturb=100', parabolic head, laminar flow, hydrostatic pressure and 'kx=ky=kz=0.0001 m/s'.

**출처 locator:**

- XH049: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.116, 117, printed page/frontmatter 114, 115, audit extract lines 2640-2653; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH088: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.116, 117, 118, printed page/frontmatter 114, 115, 116, audit extract lines 5349-5419; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh062"></a>
### K-015 — XH062

**판정:** 판본 한정 사실로 채택.

- Groundwater exchange is omitted from momentum, infiltration is instantaneous, aquifer-bottom flux is zero, and the non-hydrostatic groundwater option approximates rather than resolves vertical profiles.

**출처 locator:**

- XH062: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.31, 32, 33, 34, 35, printed page/frontmatter 29, 30, 31, 32, 33, audit extract lines 1628-1884; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 지형변화·지층·avalanching

<a id="xh015"></a>
### K-016 — XH015

**판정:** 판본 한정 사실로 채택.

- The manual gives morfac as order '1–10', illustrates '10 minutes × 6 = one morphological hour', and prohibits accelerated tidal timing with morfacopt=1 when alongshore tidal-current inertia would change.

**출처 locator:**

- XH015: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.42, printed page/frontmatter 40, audit extract lines 795-805; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh016"></a>
<a id="xh069"></a>
### K-017 — XH016, XH069

**판정:** 판본 한정 사실로 채택.

- Morphological acceleration is described as order 1–10, with defaults morfac=1, morfacopt=1, dryslp=1, wetslp=0.3, hswitch=0.1 m, dzmax=0.05, morstart=120 and morstop=2000.
- Avalanching defaults are 'dryslp=1.0', 'wetslp=0.3', 'hswitch=0.1 m' and 'dzmax=0.05', while morphology defaults include 'morfac=1', 'morfacopt=1', 'morstart=120 s' and 'morstop=2000 s'.

**출처 locator:**

- XH016: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B446, B1077, B1078, B1079, B1080, B1081, B1082, B1083, B1084, B1085, B1086 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 807,2289-2298); 직접 인용: “dzmax+ | Maximum bed level change due to avalanching | 0.05 | 0.0 - 1.0 | m/s/m”; “… and wet area (keyword: wetslp and dryslp). It is considered that inundated areas are much more prone to slumping and therefore two separate critical …”; “wetslp | Critical avalanching slope under water (dz/dx and dz/dy) | 0.3 | 0.1 - 1.0 | -”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
- XH069: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.42, 43, 80, 81, printed page/frontmatter 40, 41, 78, 79, audit extract lines 2593-2619,3895-3949; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh032"></a>
<a id="xh081"></a>
### K-018 — XH032, XH081

**판정:** 판본 한정 사실로 채택.

- A non-erodible-layer value of 0 prohibits erosion, while the documented 10 m example represents an effectively infinitely deep structure.
- The ne_layer values are erodible thicknesses, with '0' fully non-erodible and '10' allowing 10 m of erosion, above an infinitely deep non-erodible layer.

**출처 locator:**

- XH032: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.80, 81, printed page/frontmatter 78, 79, audit extract lines 1341; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH081: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.80, 81, printed page/frontmatter 78, 79, audit extract lines 3897-3899; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh037"></a>
### K-019 — XH037

**판정:** 판본 한정 사실로 채택.

- With setbathy enabled, initial bathymetry comes from setbathyfile instead of depfile and 'morphology=0' is advised because prescribed changes override computed morphology.

**출처 locator:**

- XH037: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1788 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 1724); 직접 인용: “… of the setbathyfile file time series, not from the depfile file. It is strongly advised to turn of the computation of morphological updating (keyword: …”. PDF page는 주장하지 않음.
<a id="xh043"></a>
### K-020 — XH043

**판정:** 판본 한정 사실로 채택.

- Wave-input defaults include 'taper=100 s', 'dtbc=1 s' unaffected by morfac, 'rt=3600 s', 'nmax=0.8', 'sprdthr=0.08', 'trepfac=0.01', 'Hrms=1 m', 'Tlong=80 s', 'Trep=10 s' and 'wavint=60 s'.

**출처 locator:**

- XH043: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B664, B579, B671, B672, B673, B674, B675, B676, B677, B678, B679, B680, B681, B682, B683, B684, B709, B710, B711, B712, B713, B714, B715, B716, B579, B874, B875, B876, B877, B663, B879, B664, B881 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 2173-2205); 직접 인용: “… | Time step used to describe time series of wave energy and long wave flux at offshore boundary (not affected by morfac) | 1.0 …”; “… wave period for instat = stat, bichrom, ts_1 or ts_2 | 10.0 | 1.0 - 20.0 | s | Tm01 by default using keyword …”; “wavint | Interval between wave module calls (only in stationary wave mode) | 60.0 | 1.0 - 3600.0 | s”. PDF page는 주장하지 않음.
<a id="xh048"></a>
<a id="xh087"></a>
### K-021 — XH048, XH087

**판정:** 판본 한정 사실로 채택.

- setbathy overrides depfile and requires morphology=0, while bed-layer defaults include frac_dz=0.7, merge=0.01, split=1.01 and ndvar=2.
- Bed-layer controls default to 'frac_dz=0.7', merge threshold '0.01', split threshold '1.01' and variable-layer index '2'.

**출처 locator:**

- XH048: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.116, printed page/frontmatter 114, audit extract lines 2633-2638; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH087: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.115, 116, printed page/frontmatter 113, 114, audit extract lines 5313-5345; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh092"></a>
### K-022 — XH092

**판정:** 판본 한정 사실로 채택.

- Sediment erosion is explicit and deposition implicit, thetanum=1 is upwind and 0.5 central, storage effects may matter at high morfac, and lateral avalanching and bed diffusion are omitted.

**출처 locator:**

- XH092: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.130, 131, 132, printed page/frontmatter 128, 129, 130, audit extract lines 6872,6986,7072-7180; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 파랑 경계·스펙트럼

<a id="xh001"></a>
<a id="xh052"></a>
### K-023 — XH001, XH052

**판정:** 판본 한정 사실로 채택.

- One-dimensional operation uses ny=0 and one directional bin with snells=1, stationary mode omits infragravity motions, and non-hydrostatic sandy-beach morphology is described as unvalidated.
- The manual specifies 'ny=0' for one-dimensional runs, 'dtheta=thetamax−thetamin' for a single directional bin and 'snells=1' to retain oblique mean-wave refraction.

**출처 locator:**

- XH001: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.11, 12, printed page/frontmatter 9, 10, audit extract lines 219-225; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH052: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.11, 12, 13, 14, 15, 16, printed page/frontmatter 9, 10, 11, 12, 13, 14, audit extract lines 313-326,344-390; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh044"></a>
<a id="xh077"></a>
### K-024 — XH044, XH077

**판정:** 판본 한정 사실로 채택.

- Wave defaults include dtbc=1 s, rt=3600 s, nmax=0.8, sprdthr=0.08, trepfac=0.01, taper=100 s, Hrms=1 m, Trep=10 s, Tlong=80 s and JONSWAP fp=0.08 Hz, gammajsp=3.3, s=10, mainang=270°, fnyq=0.3 Hz and dfj=fnyq/200.
- JONSWAP defaults are 'Hm0=0 m', 'fp=0.08 Hz', 'gammajsp=3.3', 's=10', 'mainang=270°', 'fnyq=0.3 Hz' and 'dfj=fnyq/200'.

**출처 locator:**

- XH044: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B710, B711, B712, B713, B714, B715, B716 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 2190-2196); 직접 인용: “dfj | Step size frequency used to create JONSWAP spectrum [s-1] | fnyq/200 | fnyq/1000 | fnyq/20”; “fnyq | Highest frequency used to create JONSWAP spectrum [s-1] | 0.3 | 0.2 | 1.0”; “gammajsp | Peak enhancement factor in the JONSWAP expression [-] | 3.3 | 1.0 | 5.0”. PDF page는 주장하지 않음.
- XH077: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.61, 62, 63, 64, 68, 69, printed page/frontmatter 59, 60, 61, 62, 66, 67, audit extract lines 3164-3229,3325-3357,3413-3453; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 표사이동

<a id="xh007"></a>
<a id="xh057"></a>
### K-025 — XH007, XH057

**판정:** 판본 한정 사실로 채택.

- The alternative waveform uses eight harmonics, w=1 for skewness and w=0 for asymmetry, and the Ruessink option is incompatible with bore-averaged turbulence.
- The Van Thiel waveform uses eight harmonics with 'w=1' giving a skewed wave and 'w=0' an asymmetric wave, while Ruessink's waveform cannot be combined with bore-averaged turbulence.

**출처 locator:**

- XH007: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.24, 25, printed page/frontmatter 22, 23, audit extract lines 404-418; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH057: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.24, 25, printed page/frontmatter 22, 23, audit extract lines 1018-1123,1188; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh038"></a>
### K-026 — XH038

**판정:** 판본 한정 사실로 채택.

- Surfbeat wave transport uses second-order upwind reconstruction and explicit integration, while shallow-water mass and momentum use a second-order explicit leapfrog scheme.

**출처 locator:**

- XH038: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1859, B1861, B1882 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 1758,1764,1813); 직접 인용: “… using the momentum balance. The water levels are updated using the mass balance. The water level gradients influence the momentum balance and the velocities …”; “… same as in the original implementation. The advection in u- and v-direction is computed simply by adding the four fluxes and dividing by the …”; “… points. Depending on the direction of this component, the wave energy at the cell boundary is computed using linear extrapolation based on the two …”. PDF page는 주장하지 않음.
<a id="xh045"></a>
<a id="xh080"></a>
### K-027 — XH045, XH080

**판정:** 판본 한정 사실로 채택.

- Defaults include wind drag Cd=0.002, air density 1.25 kg/m³, D15/D50/D90=0.00015/0.0002/0.0003 m, layer thicknesses 0.1 m, nd=3, ngd=1, porosity 0.4 and sediment density 2650 kg/m³.
- Defaults are 'Cd=0.002', 'rhoa=1.25 kg/m³', 'windv=0', 'D15=0.00015 m', 'D50=0.0002 m', 'D90=0.0003 m', layer thicknesses '0.1 m', 'nd=3', 'ngd=1', 'por=0.4' and 'rhos=2650 kg/m³'.

**출처 locator:**

- XH045: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B1022, B1023, B1024, B1025, B1026, B1057, B1058, B1059, B1060, B1061, B1062, B1063, B1064, B1065, B1066, B1067, B1068, B1069, B1070 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 2269-2287); 직접 인용: “… | Nominal thickness of variable sediment class layer | Nominal thickness of variable sediment class layer | 0.1 | 0.01 - 1.0 | m …”; “dzg3+ | Thickness of bottom sediment class layers | Thickness of bottom sediment class layers | 0.1 | 0.01 - 1.0 | m | …”; “dzg+ | Thickness of top sediment class layers | Thickness of top sediment class layers | 0.1 | 0.01 - 1.0 | m | …”. PDF page는 주장하지 않음.
- XH080: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.77, 78, 79, 80, printed page/frontmatter 75, 76, 77, 78, audit extract lines 3788-3804,3835-3886; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh047"></a>
<a id="xh086"></a>
### K-028 — XH047, XH086

**판정:** 판본 한정 사실로 채택.

- Transport defaults include Tsmin=0.5 s, facAs=facSk=facua=0.1, form=vanthiel_vanrijn, reposeangle=30°, tsfac=0.1, turbulence=boreavg, waveform=vanthiel, z0=0.006 m, cmax=0.1, sourcesink=0 and thetanum=1.
- Transport defaults include 'Tsmin=0.5 s', 'facAs=facSk=facua=0.1', 'form=vanthiel_vanrijn', 'reposeangle=30°', 'tsfac=0.1', 'turb=bore_averaged', 'waveform=vanthiel', 'z0=0.006 m', 'cmax=0.1', 'sourcesink=0' and 'thetanum=1'.

**출처 locator:**

- XH047: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.111, 112, 113, 114, printed page/frontmatter 109, 110, 111, 112, audit extract lines 2599-2631; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH086: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.111, 112, 113, 114, printed page/frontmatter 109, 110, 111, 112, audit extract lines 5143-5292; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh064"></a>
### K-029 — XH064

**판정:** 판본 한정 사실로 채택.

- Sediment stirring adds 1.45kb to squared orbital velocity, hindered settling uses wsred=(1-C)^αws, and each bed/suspended equilibrium component is capped at 0.5Cmax.

**출처 locator:**

- XH064: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.37, printed page/frontmatter 35, audit extract lines 1988-2055; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
<a id="xh065"></a>
### K-030 — XH065

**판정:** 판본 한정 사실로 채택.

- Soulsby transport uses exponent 2.4 and coefficients 0.005/0.012, while van Thiel–van Rijn uses bed exponent 1.5, suspended exponent 2.4 and coefficients 0.015/0.012.

**출처 locator:**

- XH065: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.38, 39, printed page/frontmatter 36, 37, audit extract lines 2062-2239; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 흐름 마찰·점성

<a id="xh006"></a>
### K-031 — XH006

**판정:** 판본 한정 사실로 채택.

- Short-wave friction is independent of flow friction, defaults to 'fw=0' with 'fwcutoff=1000 m', and the reef discussion recommends fw of order ten times cf or greater.

**출처 locator:**

- XH006: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.21, printed page/frontmatter 19, audit extract lines 347,2253-2254; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
<a id="xh010"></a>
<a id="xh061"></a>
### K-032 — XH010, XH061

**판정:** 판본 한정 사실로 채택.

- Other friction defaults are Manning n=0.02, White-Colebrook roughness 0.01 m and D90=0.0003 m, with Manning cf=gn²/h^(1/3) and grain roughness ks=3D90.
- Other documented friction defaults are Manning '0.02', White-Colebrook roughness '0.01' and grain-size roughness input 'D90=0.0003 m'.

**출처 locator:**

- XH010: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B310, B311, B312, B313 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 2115-2118); 직접 인용: “White-Colebrook grain size | D90 | white-colebrook-grainsize | 0.0003 m”; “White-Colebrook | ks | white-colebrook | 0.01”; “Manning | n | manning | 0.02”. PDF page는 주장하지 않음.
- XH061: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.28, 29, printed page/frontmatter 26, 27, audit extract lines 1413-1482; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
## 흐름·조석·유량 경계

<a id="xh019"></a>
### K-033 — XH019

**판정:** 판본 한정 사실로 채택.

- The offshore boundary defaults to two-dimensional absorbing-generating conditions with 'epsi=−1' for automatic filtering, 'freewave=0' using cg and 'order=2' adding bound long waves.

**출처 locator:**

- XH019: XBeach_manual_kingsday.docx, 원본 DOCX 문서순 block B496, B949, B950, B951, B952, B953 (SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`; audit extract lines 881,2230-2234); 직접 인용: “… obliquely-reflected waves to pass through the boundary. It is possible to account for situations with boundary-perpendicular and boundary-parallel currents. In order to differentiate between …”; “… wave steering, 1 = first order wave steering (short wave energy only), 2 = second order wave steering (bound long wave corresponding to short …”; “left | Switch for lateral boundary at ny+1 | neumann | neumann, wall, no_advec, neumann_v”. PDF page는 주장하지 않음. 불완전한 PDF 정렬은 citation에서 폐기함.
<a id="xh020"></a>
<a id="xh074"></a>
### K-034 — XH020, XH074

**판정:** 판본 한정 사실로 채택.

- Discharge is prescribed in m³/s with sign distinguishing inflow from outflow and is introduced with zero vertical momentum.
- Discharges are in 'm³/s', positive along model axes internally and inward at boundaries, while a zero-length orifice adds vertical mass with zero momentum.

**출처 locator:**

- XH020: XBeach_manual_kingsday.docx, DOC/DOCX→동일 work PDF 정렬, physical PDF p.51, printed page/frontmatter 49, audit extract lines 914-916; 원본 SHA-256 `c78396a23cec17b13be94ab1deef921c89b3d0c6a3d1f7d05e7d741e432c6543`.
- XH074: XBeach_manual_kingsday.pdf, 직접 PDF, physical PDF p.51, printed page/frontmatter 49, audit extract lines 2823-2827; 원본 SHA-256 `6c7c1c639a2cf587717baa93b5d22dbabe4145a5c36adf74bbae019fba9e43d4`.
