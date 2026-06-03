---
title: "SWAN Cycle III 41.51 documentation stack — User + Technical + Implementation + Programming TOC verified"
topic: swan
canonical_source: external
external_source: "Delft University of Technology, SWAN team (1993-2026). SWAN Cycle III version 41.51 — 4 official documents: User Manual (swanuse.pdf 154p), Scientific/Technical (swantech.pdf 176p), Implementation Manual (swanimp.pdf 35p), Programming Rules (swanpgr.pdf 51p). 공식: http://www.swan.tudelft.nl + GitLab (since 41.41)."
citation_status: verified
verification_method: "raw PDF 직접 read (models/SWAN/raw/manuals/pdfs/swanuse.pdf / swantech.pdf / swanimp.pdf) — TOC + Chapter 1 발췌. User Manual front matter (Cycle III 41.51, Copyright 1993-2026, GNU FDL 1.2, e-mail m.zijlema@tudelft.nl). Page numbering 모두 PDF 직접 인용."
note_author: "Claude Opus 4.7 (1M context) raw PDF direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — PDF TOC verbatim + Chapter 1 정확 인용"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-command-file-reference.md
---

# SWAN Cycle III 41.51 documentation stack — verified TOC + Chapter 1

> 본 노트는 **SWAN 공식 documentation 4 종의 TOC + Chapter 1 발췌** verified. 본 위키 `models/SWAN/raw/manuals/pdfs/` 의 4 PDF 직접 read 기준. SWAN 의 모든 verified 노트가 인용하는 1차 documentation reference.

## 1. SWAN 4 docs structure (swanuse.pdf Ch 1 + swanimp.pdf Ch 1 직접 인용)

User Manual Chapter 1 (p.1) verbatim:

> "The information about the SWAN package is distributed over four different documents. **This User Manual** describes the specifications for the input of the model. **The Implementation Manual** explains the installation procedure and the usage of SWAN on a single- or multi-processor machine with shared or distributed memory. **The Programming rules** is meant for programmers who want to develop SWAN. **The Scientific/Technical documentation** discusses the physical and mathematical details and the discretizations that have been implemented in the SWAN program."

| Doc | 파일 | Pages | 대상 | 역할 |
|---|---|---|---|---|
| **User Manual** | swanuse.pdf | **154** | 모든 사용자 | Input specification, command syntax, output format |
| **Scientific/Technical** | swantech.pdf | **176** | 알고리즘·물리 deep | Governing equations, source terms, numerical schemes, parallel + unstructured |
| **Implementation Manual** | swanimp.pdf | **35** | 설치·운영 | Build (GNU/CMake), MPI/Metis/netCDF, run, test |
| **Programming Rules** | swanpgr.pdf | **51** | 개발자 | Code style, contribution rules |

추가 자료 (swanimp.pdf Ch 1 verbatim):

> "the SWAN source code, the pre-built SWAN release for Windows, the User Manual, this Implementation Manual, the Scientific/technical documentation, the SWAN programming rules, utilities and some test cases. **All of the material can be found at the official SWAN homepage. Since version 41.41, the SWAN source code is also hosted on GitLab** and can be cloned from this repository."

→ **GitLab hosting since 41.41** (현행 41.51). 본 위키 [`models/SWAN/web-refs/swan-official-resources.md`](../web-refs/swan-official-resources.md) 의 official URL workflow 갱신 후보.

## 2. User Manual (swanuse.pdf) TOC verbatim

**Front matter**: Cycle III 41.51, Copyright 1993-2026 Delft University of Technology, GNU FDL 1.2 license. mail: Faculty of Civil Engineering and Geosciences, Environmental Fluid Mechanics Section, P.O. Box 5048, 2600 GA Delft, The Netherlands. Home page: http://www.swan.tudelft.nl

### Chapters

- **1 About this manual** (p.1)
- **2 General description and instructions for use** (p.3)
  - 2.1 Introduction (p.3)
  - 2.2 Limitations (p.4)
  - 2.3 Internal scenarios, limiters, shortcomings and coding bugs (p.5)
  - 2.4 Relation to WAM, WAVEWATCH III and others (p.7)
  - 2.5 Units and coordinate systems (p.7)
  - 2.6 Choice of grids, time windows and boundary/initial/first guess conditions (p.9)
    - 2.6.1 Introduction / 2.6.2 Input grid(s)+time / 2.6.3 Computational grids + BC/IC/first guess / 2.6.4 Output grids
  - 2.7 Activation of physical processes (p.17)
  - 2.8 Time and date notation (p.19)
- **3 Input and output files** (p.21)
  - 3.1 General / 3.2 I/O facilities / 3.3 Print file and error messages
- **4 Description of commands** (p.23)
  - 4.1 List of available commands (p.23)
  - 4.2 Sequence of commands (p.25)
  - 4.3 Command syntax and limitations (p.26)
  - 4.4 Start-up: **PROJECT** (p.26) / **SET** (p.27) / **MODE** (p.29) / **COORDINATES** (p.30)
  - 4.5 Model description:
    - 4.5.1 Computational grid: **CGRID** (p.31) / **READGRID COORDINATES** (p.33) / **READGRID UNSTRUCTURED** (p.34)
    - 4.5.2 Input grids and data: **INPGRID** (p.36) / **READINP** (p.41) / **WIND** (p.46) / **ICE** (p.46)
    - 4.5.3 Boundary and initial conditions: **BOUND SHAPE** (p.47) / **BOUNDSPEC** (p.48) / **BOUNDNEST1/2/3** (p.52-54) / **INITIAL** (p.56)
    - 4.5.4 Physics: **GEN1/2/3** (p.57-58) / **SSWELL** (p.62) / **NEGATINP** (p.62) / **WCAPPING** (p.63) / **QUADRUPL** (p.64) / **BREAKING** (p.65) / **FRICTION** (p.65) / **TRIAD** (p.67) / **VEGETATION** (p.68) / **MUD** (p.69) / **SICE** (p.70) / **TURBULENCE** (p.71) / **BRAGG** (p.71) / **LIMITER** (p.73) / **OBSTACLE** (p.73) / **OBSTACLE FIG** (p.77) / **SETUP** (p.78) / **DIFFRACTION** (p.79) / **SURFBEAT** (p.80) / **SCAT** (p.81) / **OFF** (p.83)
    - 4.5.5 Numerics: **PROP** (p.84) / **NUMERIC** (p.85)
  - 4.6 Output:
    - 4.6.1 Locations: **FRAME** (p.89) / **GROUP** / **CURVE** (p.90) / **RAY** (p.91) / **ISOLINE** (p.92) / **POINTS** / **NGRID** (p.93)
    - 4.6.2 Quantities: **QUANTITY** (p.94) / **OUTPUT** (p.97) / **BLOCK** (p.97) / **TABLE** (p.107) / **SPECOUT** (p.108) / **NESTOUT** (p.109)
    - 4.6.3 Intermediate results: **TEST** (p.110)
  - 4.7 Lock-up: **COMPUTE** (p.112) / **HOTFILE** (p.113) / **STOP** (p.114)
- **A Definitions of variables** (p.115)
- **B Command syntax** (p.121) — Keywords, Required/optional data, Spelling, Repetitions, Continuation
- **C File swan.edt** (p.127)
- **D Spectrum files, input and output** (p.137)
- **Bibliography** (p.145)
- **Index** (p.146)

→ **57 commands** 식별 (PROJECT…STOP). **§4 command reference 3노트 완성 (deep, 구문·default verbatim)**: [[swan-command-setup-grid-reference]] (§4.4-4.5.3 PROJECT/SET/MODE/COORD/CGRID/READGRID/INPGRID/READINP/WIND/BOUND/INITIAL) + [[swan-command-physics-reference]] (§4.5.4 GEN/WCAPPING/QUADRUPL/BREAKING/FRICTION/TRIAD/VEGETATION) + [[swan-command-numerics-output-reference]] (§4.5.5-4.7 PROP/NUMERIC/FRAME/BLOCK/TABLE/QUANTITY/SPECOUT/COMPUTE/HOTFILE/STOP).

## 3. Scientific/Technical (swantech.pdf) TOC verbatim

### Chapter 1 Introduction (p.1)

**Chapter 1 verbatim**:

> "The main goal of the SWAN model is to **solve the spectral action balance equation without any a priori restrictions on the spectrum for the evolution of wave growth**. This equation represents the effects of **spatial propagation, refraction, shoaling, generation, dissipation and nonlinear wave-wave interactions**. The basic scientific philosophy of SWAN is identical to that of WAM cycle 3. SWAN is a third-generation wave model and it uses the same formulations for the source terms."

> "Whereas the WAM model considers problems on oceanic scales, with SWAN wave propagation is calculated from deep water to the surf zone. Since, WAM makes use of explicit propagation schemes in geographical and spectral spaces, it requires very small grid sizes in shallow water and is thus unsuitable for applications to coastal regions. For that reason, **SWAN employs implicit schemes**, which are more robust and economic in shallow water than the explicit ones. Note that SWAN may be less efficient on oceanic scales than WAM."

**§1.1 Historical background** (p.1, partial):
> "Over the past two decades, a number of advanced spectral wind-wave models, known as third-generation models, has been developed such as **WAM (WAMDI Group, 1988), WAVEWATCH III (Tolman, 1991), TOMAWAC (Benoit et al., 1996) and SWAN (Booij et al., 1999)**."

> "SWAN cycle 1 was formulated to be able to handle only stationary conditions on a rectangular grid. Later on, SWAN cycle 2 model has been developed... Cycle 2 of SWAN is stationary and optionally nonstationary, it can compute the wave propagation not only on a regular rectangular grid, but also on a curvilinear grid. **Previous official versions 30.62, 30.75, 40.01 and 32.10 belong to the cycle 2 of SWAN**."

→ 현행 cycle 3 (41.x). cycle 1/2 historical 식별.

**§1.4 Scope** (p.2):
> "The model is based on the wave action balance equation (or energy balance in the absence of currents) with sources and sinks. Good introductory texts on the background of SWAN are **Young (1999) and Booij et al. (1999)**."

→ **본 위키 [[swan-booij-1999-jgr-foundational]] 가 §1.4 의 정확한 reference**. Young 1999 추가 reference 발견.

### Chapter 2 Governing equations (p.7)

| § | 제목 | 페이지 |
|---|---|---|
| 2.1 | Spectral description of wind waves | 7 |
| 2.2 | Propagation of wave energy | 10 |
| 2.2.1 | Wave kinematics | 10 |
| 2.2.2 | Spectral action balance equation | 11 |
| 2.3 | Sources and sinks | 13 |
| 2.3.1 | General concepts | 13 |
| **2.3.2** | **Input by wind (S_in)** | **19** |
| **2.3.3** | **Dissipation of wave energy (S_ds)** | **21** |
| **2.3.4** | **Nonlinear wave-wave interactions (S_nl)** | **28** |
| 2.3.5 | Vegetation damping | 44 |
| 2.3.6 | Sea-ice damping | 47 |
| **2.3.7** | **Bragg scattering** | **48** |
| 2.3.8 | 1st/2nd-gen formulations | 50 |
| 2.4 | Ambient current influence | 52 |
| 2.5 | Modelling of obstacles | 52 |
| 2.5.1 | Transmission / 2.5.2 Reflection / 2.5.3 Freeboard dep / 2.5.4 Diffraction | 53-56 |
| 2.6 | Wave-induced set-up | 57 |
| **2.7** | **Quasi-coherent modelling** | **58** |
| 2.7.1 | Wigner distribution | 58 |
| 2.7.2 | Wigner distribution evolution equation | 61 |
| 2.7.3 | QC approximation | 64 |

→ **본 위키 [[swan-source-terms-implementation]] / [[swan-wind-formulations-implementation]] / [[swan-whitecapping]] / [[swan-diffraction-obstacles]] 의 정확한 theory 출처**. §2.7 Quasi-coherent (Wigner dist) 는 본 위키 미커버 → 후속 보강 후보.

### Chapter 3 Numerical approaches (p.69)

| § | 제목 | 페이지 |
|---|---|---|
| 3.2 | Discretization (geographical, spectral, conservative elimination) | 70 |
| 3.3 | Solution algorithm | 79 |
| 3.4 | Iteration + stopping criteria | 82 |
| 3.5 | Sweeping approach | 85 |
| 3.6 | DIA within four-sweep technique | 88 |
| 3.7 | Action density limiter + under-relaxation | 89 |
| 3.8 | Refraction approximation (energy transport, non-stationary, c_θ limit, coarse grids) | 92 |
| 3.9 | QC approximation implementation | 102 |
| 3.10 | Curvilinear governing equations | 106 |
| 3.11 | Force computation curvilinear | 108 |
| 3.12-3.13 | Obstacles | 109-111 |
| 3.14 | σ integration | 111 |
| 3.15 | Relative ↔ absolute frequency | 112 |
| 3.16 | Spectra interpolation | 113 |
| 3.17 | Breaking source term computation | 114 |

→ **본 위키 [[swan-propagation-implementation]] / [[swan-schemes-implementation]] / [[swan-time-stepping-implementation]] 의 정확한 theory 출처**.

### Chapters 4-8

- **4 Wave boundary + initial conditions** (p.117) — [[swan-boundary-implementation]] 대응
- **5 Implementation of 2D wave setup** (p.119) — Discretization (5.2.1) + iterative solver (5.2.2)
- **6 Iterative solvers** (p.127) — **6.1 SIP (Strongly Implicit Procedure)**, **6.2 SOR (Successive Over Relaxation)**
- **7 Parallel implementation** (p.129) — Load balancing (7.1), Parallelization of implicit propagation schemes (7.2). 본 위키 [[swan-parallel-implementation]]
- **8 Unstructured mesh implementation** (p.135) — Definitions (8.1), Grid generation (8.2), Discretization + sweeping algorithm (8.3), Force computation (8.5), **Diffusion-like terms (8.6)**, **Conservation of action (8.7)**
- **Bibliography** (p.149)

→ **§5 2D wave setup**, **§6 Iterative solvers (SIP/SOR)**, **§8 Unstructured mesh** 는 본 위키 부분 커버. 후속 보강 후보.

## 4. Implementation Manual (swanimp.pdf) TOC verbatim

| Ch | 제목 | p. |
|---|---|---|
| 1 | Introduction (1.1 The material) | 1-2 |
| 2 | Use of patch files | 7 |
| 3 | Installation | 9 |
| 3.2 | Classic build (Configure, GNU make, scratch, **MPI**, **Metis**, **netCDF**) | 10-16 |
| 3.3 | Building with **CMake** | 18-20 |
| 4 | User dependent changes (file `swaninit`) | 21 |
| 5 | Run instructions | 25 |
| 6 | Testing SWAN | 29 |

→ **deep note 완성**: [[swan-implementation-manual]] verified (2026-06-03) — node1-21 직접 read. source file 인벤토리(§2, [[swan-source-coverage-audit]] 1차 출처) + GNU make(`make config/ser/omp/mpi`) + `switch.pl` 14 옵션(block Jacobi/wavefront) + MPI/Metis(41.45A multilevel k-way)/netCDF(40.91A) + **CMake(41.41+, Ninja, `-DMPI/OPENMP/METIS/NETCDF`)** + swaninit(version 4, time coding 6옵션, processor speed 부하분배) + swanrun + hcat. [[swan-parallel-implementation]] §MPI 와 cross-link.

## 4.1 Programming Rules (swanpgr v1.3) TOC + deep note

| Ch | 제목 |
|---|---|
| 1-2 | Introduction / FORTRAN 90 standards |
| 3-5 | Control statements / Use of modules / Program layout |
| 6-8 | Input-output / Error messages / Pseudo code |
| 9-12 | Performance / Machine dependency / Exceptions / Names |
| 13 | Examples (subroutine·module templates) + Bibliography + Log sheet |

→ **deep note 완성**: [[swan-programming-rules]] verified (2026-06-03) — node1-18 직접 read. ANSI F90 규칙(IMPLICIT NONE+관례 i-n=int, common 금지, allocatable 우선, obsolete F77 금지, GOTO/STOP/WHERE/BLAS 제한) + control 3구조 + module(data hiding, default PRIVATE) + **13-section 주석블록 layout(0.Authors…13.Source text)** + **subroutine template(`SAVE IENT`/`STRACE` trace)** + naming(`sw`/`swmod`). source-analysis 의 서브루틴 주석블록 구조 1차 출처. ※ swanpgr 는 **v1.3(2006-03-22) 이후 미갱신**(swanimp/use/tech 41.51 과 대조).

## 5. 본 위키 매핑 + 후속 보강

### 5.1 본 위키 SWAN 노트 ↔ swantech.pdf chapter 매핑

| 본 위키 노트 | swantech.pdf § |
|---|---|
| [[swan-action-balance]] | §2.2.2 |
| [[swan-source-terms-implementation]] | §2.3.1-2.3.8 |
| [[swan-wind-formulations-implementation]] | §2.3.2 |
| [[swan-whitecapping]] | §2.3.3 |
| [[swan-st6-babanin-implementation]] | §2.3.2-2.3.3 (Babanin ST6) |
| [[swan-diffraction-obstacles]] | §2.5 + §3.12-3.13 |
| [[swan-propagation-implementation]] | §3.2.1-3.2.2 + §3.8 |
| [[swan-schemes-implementation]] | §3.2-3.7 |
| [[swan-time-stepping-implementation]] | §3.3-3.5 |
| [[swan-boundary-implementation]] | §2.5 + Ch 4 |
| [[swan-nesting-io-implementation]] | 4.5.3 (User) + Ch 4 (Tech) |
| [[swan-parallel-implementation]] | Ch 7 + Impl §3.2.4 |
| [[swan-stationary-vs-nonstationary]] | §3.8.3 + cycle 2 history |
| [[swan-adcirc-coupling]] | (외부, swan-coupling 별도) |

### 5.2 swantech.pdf 후속 보강 후보 (현재 본 위키 미커버)

- **§2.6 Wave-induced set-up** + Ch 5 2D wave setup implementation (SIP/SOR solver) → 신설 [[swan-2d-setup]]
- **§2.7 Quasi-coherent modelling** (Wigner distribution + QC approximation, p.58-64) + §3.9 implementation → 신설 [[swan-quasi-coherent]]
- **§3.8 Refraction approximation** (c_θ limitation, coarse-grid problem) — historical overview, 4가지 sub-section (3.8.1-3.8.5) → [[swan-propagation-implementation]] §확장
- **§3.6 DIA within four-sweep technique** (Discrete Interaction Approximation Hasselmann 1985) → [[swan-source-terms-implementation]] §S_nl 확장
- **Ch 6 Iterative solvers (SIP / SOR)** — 본 위키 명시적 미커버 → 신설 [[swan-iterative-solvers]]
- **Ch 8 Unstructured mesh** §8.6 diffusion-like terms + §8.7 conservation of action — 본 위키 부분 커버 (foundation 외)
- **Ch 1.1 historical background** — SWAN cycle 1/2/3 + 30.62/30.75/40.01/32.10 → [[swan-foundation]] §version history

## 6. 신규 인용 (Bibliography 발견 후보)

- **Young (1999)** — *Wind Generated Ocean Waves* (Elsevier) — Tech §1.4 introductory text. 본 위키 미인용
- **WAMDI Group 1988** — WAM 원논문 — Tech §1.1 historical
- **Tolman 1991** — WAVEWATCH III 원논문 — Tech §1.1
- **Benoit et al. 1996** — TOMAWAC — Tech §1.1
- **Booij et al. 1999** — SWAN [[swan-booij-1999-jgr-foundational]] ✓ (verified 2026-06-01)

## 7. 한계

- TOC + Ch 1 만 verified. **Ch 2-8 본문 식 정확 인용은 추후 chapter별 deep notes 필요**.
- Bibliography (Tech p.149 + User p.145) full list 미포함.
- ✅ Appendix A "Definitions of variables" (User p.115-120) — **deep note 완성**: [[swan-output-variable-definitions]] verified (2026-06-03). HSIGN/TM01·02/TMM10/DIR/DSPR/QP/BFI/FORCE 적분식 verbatim + MS↔DSPR Table A.1 + Cartesian/Nautical convention. 이론 Eq(2.11-12·3.59-61) ↔ output quantity 정합.
- ✅ Appendix D "Spectrum files" (User p.137) — **deep note 완성**: [[swan-spectral-file-format]] verified (2026-06-03). BOUNDSPEC/SPECOUT/NESTOUT 파일구조(SWAN version·TIME·LOCATIONS/LONLAT·RFREQ/AFREQ·CDIR/NDIR·QUANT·FACTOR/ZERO/NODATA) + 1D 3-quantity/2D 1-quantity + exception value verbatim.
- Appendix C "swan.edt" (User p.127) — SWAN command file editor template, [[swan-command-file-reference]] 와 cross-walk 가치 (command 3노트로 대부분 커버됨, 잔여 가치 낮음).

## 8. 연결

- [[swan-booij-1999-jgr-foundational]] — Booij 1999 JGR 1차 reference (Tech §1.1, §1.4 직접 인용)
- [[swan-action-balance]] — Tech §2.2.2
- [[swan-foundation]] — SWAN 모듈 구조 (Impl §3 build + Tech Ch1 historical 통합)
- [[swan-command-file-reference]] — User §4 commands 매핑
- 모든 [[swan-*-implementation]] — Tech chapter 매핑 표 (§5.1)
- 공식 사이트: http://www.swan.tudelft.nl (Tech §1, User front matter)
- GitLab 호스팅 (Impl Ch 1): 41.41+ 이후
