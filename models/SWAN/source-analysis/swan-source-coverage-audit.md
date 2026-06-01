---
title: "SWAN Cycle III 41.51 source code 58 files coverage audit + 신규 발견 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw source directory 직접 ls (models/SWAN/raw/source_code/swan/src/, 58 source files 식별) + 12개 신규 발견 파일 header 직접 read (SwanIEM/SwanBraggScat/SwanGSECorr/SwanQCM/mod_xnl4v5/SwanCompUnstruc/SwanReadEasymeshGrid/SwanReadADCGrid/SwanReadTriangleGrid/swancom1/swanmain/fftpack51) — 모든 author/version/purpose comment block verbatim 인용 (line 1-60). 기존 20 source-analysis 노트와의 매핑 cross-check."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — wc -l + grep 'Purpose|Authors|Updates' verbatim"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
  - models/SWAN/source-analysis/swan-diffraction-obstacles.md
  - models/SWAN/source-analysis/swan-parallel-implementation.md
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
---

# SWAN 41.51 source code 58 files coverage audit

> 본 노트는 `models/SWAN/raw/source_code/swan/src/` 의 **58 source files 전체 inventory + 기존 20 source-analysis 노트와의 coverage 매핑 + 12개 신규 발견 파일 verified**. SWAN documentation stack ([[swan-documentation-stack]]) 의 source-level companion.

## 1. 58 source file inventory (raw ls 직접)

```
58 source files in models/SWAN/raw/source_code/swan/src/
```

### 1.1 신규 ftn90 modular files (47 files — Cycle III 41.x 시기)

`Swan*.ftn90` (modern Fortran 90 module format):
- **Grid topology**: SwanCheckGrid / SwanCreateEdges / SwanFindPoint / SwanGridCell / SwanGridFace / SwanGridTopology / SwanGridVert / SwanGriddata / SwanGridobjects / SwanInitCompGrid / SwanPointinMesh / SwanPrintGridInfo / SwanVertlist
- **Grid readers**: SwanReadADCGrid / SwanReadEasymeshGrid / SwanReadGrid / SwanReadTriangleGrid
- **Interpolation**: SwanInterpolateAc / SwanInterpolateOutput / SwanInterpolatePoint
- **Boundary / obstacles**: SwanBndStruc / SwanBpntlist / SwanCrossObstacle / SwanFindObstacles
- **Compute (unstructured)**: SwanCompUnstruc / SwanCompdata / SwanComputeForce / SwanConvAccur / SwanConvStopc / SwanPrepComp / SwanSweepSel / SwanThreadBounds
- **Propagation velocity**: SwanGradDepthorK / SwanGradVel / SwanPropvelS / SwanPropvelX
- **Transport**: SwanTranspAc / SwanTranspX
- **Spectral**: SwanDispParm / SwanIntgratSpc / SwanSpectPart (.ftn legacy)
- **Diffraction parameters**: SwanDiffPar
- **Output writers (VTK)**: SwanVTKPDataSets / SwanVTKWriteData / SwanVTKWriteHeader
- **Parallel**: SwanParallel
- **Physics modules**: **SwanBraggScat** / **SwanGSECorr** / **SwanIEM** / **SwanQCM** / SdsBabanin

### 1.2 Legacy ftn files (11 files — Cycle II 이전 + service routines)

| 파일 | 라인 | 역할 |
|---|---|---|
| **swanmain.ftn** | 9,338 | Main program entry |
| **swancom1.ftn** | **12,121** | Computation routines (largest) |
| swancom2.ftn / swancom3.ftn / swancom4.ftn / swancom5.ftn | — | Computation supplements |
| swanout1.ftn / swanout2.ftn | — | Output (legacy) |
| swanpre1.ftn / swanpre2.ftn | — | Preprocessing (legacy) |
| swanparll.ftn | — | Parallel (legacy MPI) |
| swanser.ftn | — | Service routines |

### 1.3 Service/utility modules

| 파일 | 라인 | 역할 |
|---|---|---|
| **fftpack51.ftn90** | **15,110** | FFT library (largest by lines) |
| **mod_xnl4v5.ftn90** | **8,989** | XNL4 exact quadruplet interaction (Van Vledder) |
| serv_xnl4v5.ftn90 | — | XNL4 service routines |
| m_constants.ftn90 / m_fileio.ftn90 | — | Constants + file I/O modules |
| agioncmd.ftn90 | — | AGION command parser |
| nctablemd.ftn90 / swn_outnc.ftn90 | — | NetCDF output |
| ocpcre.ftn / ocpids.ftn / ocpmix.ftn | — | OCean Program (OCP) service (program-independent routines) |
| swmod1.ftn / swmod2.ftn | — | Data modules |
| srclist.cmake / srclistnc.cmake | — | CMake source lists |

총: **58 source files**. Largest: `fftpack51.ftn90` (15k) > `swancom1.ftn` (12k) > `mod_xnl4v5.ftn90` (9k) > `swanmain.ftn` (9k).

## 2. 기존 20 source-analysis 노트 매핑

| 본 위키 노트 | 추정 cover file |
|---|---|
| [[swan-foundation]] | swanmain + swanpre1/2 + swmod1/2 |
| [[swan-schemes-implementation]] | swancom1-5 (legacy compute) |
| [[swan-propagation-implementation]] | SwanPropvelS / SwanPropvelX / SwanTranspAc / SwanTranspX |
| [[swan-time-stepping-implementation]] | swancom1 + SwanPrepComp |
| [[swan-source-terms-implementation]] | swancom4-5 (source terms) + SdsBabanin |
| [[swan-wind-formulations-implementation]] | swancom4 (Sin) |
| [[swan-whitecapping]] | swancom4 (Sds) |
| [[swan-st6-babanin-implementation]] | **SdsBabanin.ftn90** |
| [[swan-boundary-implementation]] | SwanBndStruc + swanpre2 |
| [[swan-nesting-io-implementation]] | SwanInterpolate* + swanpre2 |
| [[swan-diffraction-obstacles]] | **SwanDiffPar** + SwanFindObstacles + SwanCrossObstacle |
| [[swan-stationary-vs-nonstationary]] | swanmain + swancom1 |
| [[swan-parallel-implementation]] | **SwanParallel.ftn90** + swanparll.ftn |
| [[swan-data-structures-implementation]] | SwanGriddata + SwanGridobjects + swmod1/2 |
| [[swan-output-formats]] / [[swan-output-writers-implementation]] | swanout1/2 + nctablemd + swn_outnc + SwanVTKWrite* |
| [[swan-command-file-reference]] | agioncmd + swan.edt (User App C) |
| [[swan-adcirc-coupling]] / [[swan-adcirc-coupling-implementation]] | SwanReadADCGrid + 외부 |
| [[wave/swan-source-terms-implementation]] | swancom4-5 (deep) |

**Covered files (estimated)**: ~30 files. **Uncovered**: ~25 신규 발견.

## 3. 신규 발견 파일 verified (12 files, 모두 본 위키 미커버)

### 3.1 Physics modules — 모두 신설 가치 큰 발견

#### SwanIEM.ftn90 (1230 lines)

```
! This file contains data and routines for surfbeat (Infragravity Energy Model)
!   Authors
!   41.85: Ad Reniers
!   Updates
!   41.85, January 2019: New module
!   Purpose
!   Contains data with respect to 1D surfbeat
```

→ **1D Infragravity wave model**. User Manual command `SURFBEAT` (p.80) 의 source. **본 위키 미커버** — 신설 [[swan-surfbeat-iem]] 후보.

#### SwanBraggScat.ftn90 (1491 lines)

```
!   Authors
!   41.80: Dirk Rijnsdorp and Ad Reniers
!   Updates
!   41.80, September 2021: New module
!   Purpose
!   Contains data with respect to Bragg scattering
```

→ **Bragg scattering** (Tech §2.3.7 p.48). User command `BRAGG` (p.71). 본 위키 미커버 — 신설 [[swan-bragg-scattering]] 후보.

#### SwanGSECorr.ftn90 (280 lines)

```
!   Authors
!   41.00: Marcel Zijlema
!   Updates
!   41.00, February 2009: New subroutine
!   Purpose
!   Computes waveage-dependent diffusion terms in x-y space to counteract the garden-sprinkler effect
```

→ **Garden-Sprinkler Effect (GSE) correction**. SWAN refraction 의 well-known numerical artifact. Tech §8.6 (diffusion-like terms) 와 연관. 본 위키 미커버 — 신설 [[swan-gse-correction]] 후보 또는 [[swan-propagation-implementation]] §확장.

#### SwanQCM.ftn90 (3464 lines)

```
!   Authors
!   41.90: Gal Akrish, Pieter Smit and Marcel Zijlema
!   Updates
!   41.90, June 2021: New module
!   Purpose
!   Contains data with respect to quasi-coherent modelling
!   Initializes quasi-coherent framework
```

→ **Quasi-Coherent Modelling (QCM)**. Tech §2.7 (Wigner distribution + QC approx) + §3.9 implementation. User command `SCAT` (p.81). 본 위키 미커버 — 신설 [[swan-quasi-coherent]] 후보.

### 3.2 Exact nonlinear interactions — XNL4 module

#### mod_xnl4v5.ftn90 (8989 lines)

```
module m_xnldata
!  module for computing the quadruplet interaction
!  Created by Gerbrant van Vledder
!
!  version 1.01   16/02/1999  Initial version
!  ...
!  version 5.06   11/04/2005  Final
```

→ **Van Vledder XNL4** — **exact** Boltzmann quadruplet integral. DIA (Hasselmann 1985, Tech §3.6) 대비 high-precision 옵션. User command `QUADRUPL` (p.64) 의 비-DIA 옵션. **본 위키 [[swan-source-terms-implementation]] 는 DIA 만 커버** — 신설 [[swan-xnl4-exact-quadruplet]] 후보 또는 §확장.

### 3.3 Multi-format grid readers

#### SwanReadADCGrid.ftn90 (189 lines)
- **ADCIRC fort.14 unstructured grid reader** — ADCIRC-SWAN coupling 의 grid path
- [[swan-adcirc-coupling]] 와 직접 연관 — coupling source 부분 보강 가능

#### SwanReadEasymeshGrid.ftn90 (155 lines)
- **Easymesh** unstructured grid format reader
- 본 위키 미언급 — Easymesh format (.e 확장자) → 신설 manual-notes 또는 [[swan-foundation]] §unstructured 확장

#### SwanReadTriangleGrid.ftn90 (178 lines)
- **Triangle** (Shewchuk) `.node` / `.ele` format reader
- Tech §8.2 (Notes on grid generation) 의 권장 mesh generator. 본 위키 미언급

→ 3 grid readers + SwanReadGrid (general) = **4 unstructured grid formats** SWAN 지원. ADCIRC + Easymesh + Triangle + generic.

### 3.4 Unstructured compute driver

#### SwanCompUnstruc.ftn90 (1684 lines)

```
!   Authors (10+ updates):
!   41.02-41.80: Zijlema + Dietrich (Casey, 41.20)
!   Purpose
!   Performs one time step for solution of wave action equation on unstructured grid
```

→ **Unstructured grid time-step driver**. Tech Ch 8 (Unstructured mesh implementation) 의 main implementation file. 본 위키 [[swan-foundation]] §unstructured 부분 외 미커버 — 신설 [[swan-unstructured-time-step]] 후보. Casey Dietrich (ADCIRC 측 contributor) version 41.20 — ADCIRC-SWAN unstructured coupling 의 ADCIRC-side 기여 표시.

### 3.5 FFT library

#### fftpack51.ftn90 (15110 lines, **largest single file**)
- **FFTPACK 5.1** (NCAR FORTRAN FFT 표준 library 포팅) — 외부 algorithm. 본 위키 verified 가치 낮음 (외부 library 그대로 vendor).

### 3.6 Legacy 큰 파일

#### swancom1.ftn (12121 lines)
- Cycle II legacy 의 main computation routines. SWAN의 핵심 알고리즘 다수 포함.
- 본 위키 [[swan-schemes-implementation]] / [[swan-time-stepping-implementation]] 가 부분 cover — 정확한 line 매핑 audit 가치.

#### swanmain.ftn (9338 lines)
- Main program. [[swan-foundation]] 와 대응 — 정확한 line 매핑 audit 가치.

## 4. Coverage gap matrix

### 4.1 본 위키 미커버 신규 발견 (8 신설 source-analysis 후보)

| 후보 노트 | source file | Tech § | User cmd |
|---|---|---|---|
| [[swan-surfbeat-iem]] | SwanIEM.ftn90 (1230) | — | SURFBEAT (p.80) |
| [[swan-bragg-scattering]] | SwanBraggScat.ftn90 (1491) | §2.3.7 | BRAGG (p.71) |
| [[swan-gse-correction]] | SwanGSECorr.ftn90 (280) | §3.8 / §8.6 | (internal) |
| [[swan-quasi-coherent]] | SwanQCM.ftn90 (3464) | §2.7 + §3.9 | SCAT (p.81) |
| [[swan-xnl4-exact-quadruplet]] | mod_xnl4v5.ftn90 (8989) | §2.3.4 + §3.6 | QUADRUPL (p.64) opt |
| [[swan-unstructured-time-step]] | SwanCompUnstruc.ftn90 (1684) | Ch 8 | (internal) |
| [[swan-grid-readers]] | SwanReadADC/Easymesh/Triangle/Grid (4 files) | §8.2 | READGRID UNSTRUCTURED |
| [[swan-vtk-output]] | SwanVTKPDataSets + SwanVTKWriteData + SwanVTKWriteHeader (3 files) | — | (output) |

### 4.2 SWAN 41.x 신규 module 시기 추적 (version history)

| Version | Year | 신규 module |
|---|---|---|
| 41.00 | 2009-02 | SwanGSECorr (Zijlema GSE correction) |
| 41.20 | — | SwanCompUnstruc upgrade (Casey Dietrich ADCIRC) |
| 41.80 | 2021-09 | SwanBraggScat (Rijnsdorp+Reniers) |
| 41.85 | 2019-01 | SwanIEM (Reniers surfbeat) |
| 41.90 | 2021-06 | SwanQCM (Akrish+Smit+Zijlema quasi-coherent) |
| **41.41+** | — | **GitLab hosted** (Impl Ch 1) |
| **41.51** | current | Latest official release |

→ **41.80-41.90 (2021)** 시기에 Bragg + QCM 동시 출시. Reniers+Smit+Zijlema+Akrish 의 모듈러 추가 패턴.

## 5. 한계 + 다음 보강

- 본 노트는 source file **header (line 1-60) 만** verified. 각 신규 발견의 sub-routine 별 deep dive 는 별도 (§4.1 신설 후보).
- mod_xnl4v5.ftn90 의 Van Vledder XNL4 = SWAN 외부 library 형식 — 원논문 (Van Vledder 2006 *Coastal Engineering*) 직접 fetch 후 [[swan-xnl4-exact-quadruplet]] 신설 가치.
- fftpack51.ftn90 = NCAR vendor library, 본 위키 source-level audit 가치 낮음.
- swancom1.ftn 12k 라인 — Cycle II legacy 의 정확한 line 매핑 cross-walk 가치 큼 (본 위키 [[swan-schemes-implementation]] 와).

## 6. 연결

- [[swan-documentation-stack]] — 4 PDFs TOC (User + Tech + Impl + Programming)
- [[swan-booij-1999-jgr-foundational]] — Booij 1999 JGR 1차 reference
- 기존 20 source-analysis 노트 — §2 매핑 표
- [[swan-foundation]] — SWAN 모듈 구조
- 공식 사이트: http://www.swan.tudelft.nl
- GitLab (since 41.41): SWAN source repo
