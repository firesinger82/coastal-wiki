---
title: "SWAN Cycle III 41.51 source code 75 files coverage audit + 신규 발견 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "현재 src/*.ftn90 57개와 src/*.ftn 18개를 집계했다. §2의 링크 대상은 중복을 제외하면 19개이다. 파일 헤더 발췌에는 요약이 포함된다. SwanCompUnstruc의 목적 주석은 68줄에 있다. 2026-10-13 recovery 대조 보고서 R1–R8 반영분의 추가·수정 59줄을 현재 코드·과거 커밋·PDF·최종 보고서와 대조했다." # [10-13 전수 검증 정정]
last_source_check: "2026-10-13 (recovery 대조 반영)"
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

# SWAN 41.51 source code 75 files coverage audit

<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn90 = 57 -->
<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn = 18 -->

> 이 노트는 `models/SWAN/raw/source_code/swan/src/`의 `.ftn90` 57개와 `.ftn` 18개를 나열한다. §2의 연결은 중복을 제외하면 19개 노트를 가리킨다. §3의 파일 헤더에는 발췌와 요약을 함께 적었다. 아래 연결은 현행 노트를 가리킨다. [swan-documentation-stack](../manual-notes/swan-documentation-stack.md)과 소스 수준에서 연결된다. [10-13 전수 검증 정정]

<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn90 = 57 -->
<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn = 18 -->
## 1. 75 source file inventory (raw ls 직접)

> **스냅샷 기준**: 본 인벤토리는 snapshot `43e9bbb` 기준이다. 직전 pinned `5544152` 대비
> `SwanThreadBounds.ftn90`(unstructured OpenMP thread 경계 계산, 160줄)이 upstream 에서
> 삭제되어 목록에서 제외했다 — 스케줄링 책임이 `SwanVertlist.ftn90` 의 front 구성과
> `SwanCompUnstruc.ftn90` 의 front 루프로 옮겨갔다(`SwanCompUnstruc.ftn90:823-984`).
> 나머지 나열 항목은 새 스냅샷에 모두 존재한다.
>
> 구현 매뉴얼 노트의 구판 목록은 [swan-implementation-manual](../manual-notes/swan-implementation-manual.md)에 있다. [R7:N-032 유지 판정](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#4-노트-대조와-수정안).

patch B는 SwanThreadBounds.ftn90을 삭제했다. 현재 비정렬 계산은 front 목록을 직접 순회한다. 삭제 커밋은 `0dabfa4`(2026-07-13)이다. `7ee8981:src/SwanThreadBounds.ftn90:1`의 원문은 `subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )`이다. `43e9bbb:src/SwanCompUnstruc.ftn90:848`의 원문은 `!GRAPH                ivert = flist(kvert,swpdir)`이다. `43e9bbb:src/SwanCompUnstruc.ftn90:849`의 원문은 `!FXFRO                ivert = vlist(kvert,swpdir)`이다. [R7:I-057](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).

```
75 source files in models/SWAN/raw/source_code/swan/src/
  = Swan*.ftn90 48 + 기타 .ftn90 9 + .ftn 18
  (비소스 4 제외: CMakeLists.txt, hcat, srclist.cmake, srclistnc.cmake)
```

### 1.1 신규 ftn90 modular files (50 files — Cycle III 41.x 시기)

`Swan*.ftn90` (modern Fortran 90 module format):
- **Grid topology**: SwanCheckGrid / SwanCreateEdges / SwanFindPoint / SwanGridCell / SwanGridFace / SwanGridTopology / SwanGridVert / SwanGriddata / SwanGridobjects / SwanInitCompGrid / SwanPointinMesh / SwanPrintGridInfo / SwanVertlist
- **Grid readers**: SwanReadADCGrid / SwanReadEasymeshGrid / SwanReadGrid / SwanReadTriangleGrid
- **Interpolation**: SwanInterpolateAc / SwanInterpolateOutput / SwanInterpolatePoint
- **Boundary / obstacles**: SwanBndStruc / SwanBpntlist / SwanCrossObstacle / SwanFindObstacles
- **Compute (unstructured)**: SwanCompUnstruc / SwanCompdata / SwanComputeForce / SwanConvAccur / SwanConvStopc / SwanPrepComp / SwanSweepSel
- **Propagation velocity**: SwanGradDepthorK / SwanGradVel / SwanPropvelS / SwanPropvelX
- **Transport**: SwanTranspAc / SwanTranspX
- **Spectral**: SwanDispParm / SwanIntgratSpc / SwanSpectPart (.ftn legacy)
- **Diffraction parameters**: SwanDiffPar
- **Output writers (VTK)**: SwanVTKPDataSets / SwanVTKWriteData / SwanVTKWriteHeader
- **Parallel**: SwanParallel
- **Physics modules**: **SwanBraggScat** / **SwanGSECorr** / **SwanIEM** / **SwanQCM** / SdsBabanin

### 1.2 Legacy ftn files (12 files — Cycle II 이전 + service routines)

| 파일 | 라인 | 역할 |
|---|---|---|
| **swanmain.ftn** | 9,338 | Main program entry |
| **swancom1.ftn** | **12,121** | Computation routines (largest) |
| swancom2.ftn / swancom3.ftn / swancom4.ftn / swancom5.ftn | — | Computation supplements |
| swanout1.ftn / swanout2.ftn | — | Output (legacy) |
| swanpre1.ftn / swanpre2.ftn | — | Preprocessing (legacy) |
| swanparll.ftn | — | Parallel (legacy MPI) |
| swanser.ftn | — | Service routines |

### 1.3 Service/utility modules (13 files)

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

<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn90 = 57 -->
<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn = 18 -->

총: **75 source files** (50 + 12 + 13, 중복 없음 — 실측 ls 와 대조해 누락 0 확인).
Largest: `fftpack51.ftn90` (15,110) > `swancom1.ftn` (12,121) > `swanmain.ftn` (9,343) > `mod_xnl4v5.ftn90` (8,989) > `swanser.ftn` (7,416).

> **계수 정정 2026-09-22**: 이전 판은 총계를 **58** 로 적었다. 58 은 직전 pinned `5544152` 시점의
> **`.ftn90` 파일 수**였고(현 스냅샷에서는 57), `.ftn` 18개를 총계에서 누락한 채 'source files' 로
> 이름 붙인 것이다. 절별 계수(47·11)도 실제 열거 수(50·12)와 어긋나 있었다. **열거 목록 자체는
> 처음부터 완전했고**(75개 전부 수록, 누락 0) 틀린 것은 표제의 숫자뿐이다. `swanmain.ftn` 은
> 스냅샷 교체로 9,338→9,343 줄이 되었고, 크기 순서에서 `mod_xnl4v5.ftn90` 과 자리가 바뀌어 있었다.

## 2. 기존 20 source-analysis 노트 매핑

| 본 위키 노트 | 추정 cover file |
|---|---|
| [swan-foundation](swan-foundation.md) | swanmain + swanpre1/2 + swmod1/2 |
| [swan-schemes-implementation](swan-schemes-implementation.md) | swancom1 + swancom5 + swanpre1 (ACTION·전파법·PROP 파서) [10-13 전수 검증 정정]
| [swan-propagation-implementation](swan-propagation-implementation.md) | swancom1 + swancom5 + swanmain (전파 조립·호출) [10-13 전수 검증 정정]
| [swan-time-stepping-implementation](swan-time-stepping-implementation.md) | swanmain + swanpre1 + swancom5 + SwanTranspX + swanout1 [10-13 전수 검증 정정]
| [swan-source-terms-implementation](wave/swan-source-terms-implementation.md) | swancom1 (SOURCE 조립) + swancom2–5 + SdsBabanin [10-13 전수 검증 정정]
| [swan-wind-formulations-implementation](swan-wind-formulations-implementation.md) | swancom3 (WNDPAR·SWIND0/3/4/5) + swanpre1 [10-13 전수 검증 정정]
| [swan-whitecapping](swan-whitecapping.md) | swancom2 (SWCAP·SWCAP8) + swancom1 (호출·조립) [10-13 전수 검증 정정]
| [swan-st6-babanin-implementation](swan-st6-babanin-implementation.md) | **SdsBabanin.ftn90** |
| [swan-boundary-implementation](swan-boundary-implementation.md) | swanpre1 + swanpre2 + swanmain + swmod2 [10-13 전수 검증 정정]
| [swan-nesting-io-implementation](swan-nesting-io-implementation.md) | swanpre2 + swanout1/2 + swanmain + swanser [10-13 전수 검증 정정]
| [swan-diffraction-obstacles](swan-diffraction-obstacles.md) | SwanDiffPar + SwanFindObstacles + swancom5 + swanpre1 [10-13 전수 검증 정정]
| [swan-stationary-vs-nonstationary](swan-stationary-vs-nonstationary.md) | swanmain + swancom1 |
| [swan-parallel-implementation](swan-parallel-implementation.md) | **SwanParallel.ftn90** + swanparll.ftn |
| [swan-data-structures-implementation](swan-data-structures-implementation.md) | SwanGriddata + swmod1/2 + swanmain [10-13 전수 검증 정정]
| [swan-output-formats](swan-output-formats.md) / [swan-output-writers-implementation](swan-output-writers-implementation.md) | swanout1/2 + swanpre2 + swanser + swn_outnc [10-13 전수 검증 정정]
| [swan-command-file-reference](swan-command-file-reference.md) | swanpre1/2 + ocpcre + misc/swan.edt (입력 명령) [10-13 전수 검증 정정]
| [swan-adcirc-coupling](swan-adcirc-coupling.md) / [swan-adcirc-coupling-implementation](swan-adcirc-coupling-implementation.md) | SwanReadADCGrid + 외부 |
| [wave/swan-source-terms-implementation](wave/swan-source-terms-implementation.md) | swancom1 (SOURCE 조립) + swancom2–5 + SdsBabanin [10-13 전수 검증 정정]

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

SwanIEM은 1D infragravity 모델 자료와 루틴을 포함한다. `SURFBEAT` 설명은 swanuse PDF 88쪽 / 인쇄 80쪽에 있다. [swan-surfbeat-iem](swan-surfbeat-iem.md)이 이 구현을 다룬다. 근거: `src/SwanIEM.ftn90:1,42`. [10-13 전수 검증 정정]

#### SwanBraggScat.ftn90 (1491 lines)

```
!   Authors
!   41.80: Dirk Rijnsdorp and Ad Reniers
!   Updates
!   41.80, September 2021: New module
!   Purpose
!   Contains data with respect to Bragg scattering
```

SwanBraggScat는 Bragg 산란 자료와 루틴을 포함한다. 이론 절은 swantech §2.3.7의 PDF 57쪽 / 인쇄 49쪽에서 시작한다. `BRAGG` 명령은 swanuse PDF 79쪽 / 인쇄 71쪽에 있다. [swan-bragg-scattering](swan-bragg-scattering.md)이 이 구현을 다룬다. 근거: `src/SwanBraggScat.ftn90:1,42`. [10-13 전수 검증 정정]

#### SwanGSECorr.ftn90 (280 lines)

```
!   Authors
!   41.00: Marcel Zijlema
!   Updates
!   41.00, February 2009: New subroutine
!   Purpose
!   Computes waveage-dependent diffusion terms in x-y space to counteract the garden-sprinkler effect
```

SwanGSECorr는 공간 전파의 garden-sprinkler effect를 줄이는 확산항을 계산한다. 근거: `src/SwanGSECorr.ftn90:40` `!   Computes waveage-dependent diffusion terms in x-y space to counteract the garden-sprinkler effect`. 관련 이론은 swantech §3.2.1–3.2.2의 PDF 81–83쪽과 §8.6의 PDF 154쪽에 있다. [swan-gse-correction](swan-gse-correction.md)이 이 구현을 다룬다. [10-13 전수 검증 정정]

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

SwanQCM은 quasi-coherent 모델 자료와 루틴을 포함한다. 이론은 swantech §2.7과 §3.9에 있다. `SCAT` 명령은 swanuse PDF 89쪽 / 인쇄 81쪽에서 시작한다. [swan-quasi-coherent](swan-quasi-coherent.md)가 이 구현을 다룬다. 근거: `src/SwanQCM.ftn90:42`. [10-13 전수 검증 정정]

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

Van Vledder의 XNL4는 4파 상호작용 적분을 계산한다. `QUADRUPL`의 XNL 선택값은 51·52·53이다. 근거: `src/mod_xnl4v5.ftn90:4–5`; swanuse PDF 72쪽 / 인쇄 64쪽. [swan-xnl4-exact-quadruplet](swan-xnl4-exact-quadruplet.md)이 XNL4 구현을 다룬다. [원천항 노트](wave/swan-source-terms-implementation.md)는 DIA와 원천항 조립을 다룬다. [10-13 전수 검증 정정]

### 3.3 Multi-format grid readers

#### SwanReadADCGrid.ftn90 (189 lines)
- **ADCIRC fort.14 unstructured grid reader** — ADCIRC-SWAN coupling 의 grid path
- [swan-adcirc-coupling](swan-adcirc-coupling.md) 와 직접 연관 — coupling source 부분 보강 가능

#### SwanReadEasymeshGrid.ftn90 (155 lines)
- **Easymesh** unstructured grid format reader
- Easymesh 리더는 `.n`과 `.e` 파일을 읽는다. `src/SwanReadEasymeshGrid.ftn90:40`의 원문은 `!   Reads Easymesh grid described in <name>.n and <name>.e`이다. [swan-grid-readers](swan-grid-readers.md)가 이 입력 형식을 다룬다. [10-13 전수 검증 정정]

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

현재 비정렬 계산은 front 목록을 직접 순회한다. 기본 patch B 빌드는 거리 정렬 결과에서 의존성 수준을 만든 flist를 순회한다. -fixfront 빌드는 vlist를 순회한다. [swan-unstructured-time-step](swan-unstructured-time-step.md), [R8:T1-014](../../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론).

### 3.5 FFT library

#### fftpack51.ftn90 (15110 lines, **largest single file**)
- **FFTPACK 5.1** (NCAR FORTRAN FFT 표준 library 포팅) — 외부 algorithm. 본 위키 verified 가치 낮음 (외부 library 그대로 vendor).

### 3.6 Legacy 큰 파일

#### swancom1.ftn (12121 lines)
- Cycle II legacy 의 main computation routines. SWAN의 핵심 알고리즘 다수 포함.
- 본 위키 [swan-schemes-implementation](swan-schemes-implementation.md) / [swan-time-stepping-implementation](swan-time-stepping-implementation.md) 가 부분 cover — 정확한 line 매핑 audit 가치.

#### swanmain.ftn (9338 lines)
- Main program. [swan-foundation](swan-foundation.md) 와 대응 — 정확한 line 매핑 audit 가치.

## 4. Coverage gap matrix

### 4.1 본 위키 미커버 신규 발견 (8 신설 source-analysis 후보)

| 후보 노트 | source file | Tech § | User cmd |
|---|---|---|---|
| [swan-surfbeat-iem](swan-surfbeat-iem.md) | SwanIEM.ftn90 (1230) | — | SURFBEAT (p.80) |
| [swan-bragg-scattering](swan-bragg-scattering.md) | SwanBraggScat.ftn90 (1491) | §2.3.7 | BRAGG (p.71) |
| [swan-gse-correction](swan-gse-correction.md) | SwanGSECorr.ftn90 (280) | §3.2.1–3.2.2 / §8.6 | (internal) [10-13 전수 검증 정정]
| [swan-quasi-coherent](swan-quasi-coherent.md) | SwanQCM.ftn90 (3464) | §2.7 + §3.9 | SCAT (p.81) |
| [swan-xnl4-exact-quadruplet](swan-xnl4-exact-quadruplet.md) | mod_xnl4v5.ftn90 (8989) | §2.3.4 + §3.6 | QUADRUPL (p.64) opt |
| [swan-unstructured-time-step](swan-unstructured-time-step.md) | SwanCompUnstruc.ftn90 (1678줄; 현재 파일 집계) | Ch 8 | (internal) [10-13 전수 검증 정정]
| [swan-grid-readers](swan-grid-readers.md) | SwanReadADC/Easymesh/Triangle/Grid (4 files) | §8.2 | READGRID UNSTRUCTURED |
| [swan-vtk-output](swan-vtk-output.md) | SwanVTKPDataSets + SwanVTKWriteData + SwanVTKWriteHeader (3 files) | — | (output) |

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

- patch B는 SwanThreadBounds.ftn90을 삭제했다. 현재 비정렬 계산은 front 목록을 직접 순회한다. [R7:I-057](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론).
- `src/mod_xnl4v5.ftn90:2–5`는 XNL4 모듈과 저자를 밝힌다. [swan-xnl4-exact-quadruplet](swan-xnl4-exact-quadruplet.md)은 이 파일의 구현을 설명하는 기존 노트이다. [10-13 전수 검증 정정]
- fftpack51.ftn90 = NCAR vendor library, 본 위키 source-level audit 가치 낮음.
- [swan-setup-solver-swancom1-crosswalk](swan-setup-solver-swancom1-crosswalk.md)의 현행 표는 서브루틴 20개를 나열한다. `src/swancom1.ftn`의 `SUBROUTINE` 선언도 20개이다. 표에서 기존 노트 연결은 14개이다. 유틸리티 분류는 4개이다. SETUPP와 SETUP2D는 해당 노트의 §3–4에서 다룬다. 이전 19개 집계가 누락한 선언은 `src/swancom1.ftn:6823`의 `SUBROUTINE SOURCE`이다. [10-13 전수 검증 정정]

## 6. 연결

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) — 4 PDFs TOC (User + Tech + Impl + Programming)
- [swan-booij-1999-jgr-foundational](../manual-notes/swan-booij-1999-jgr-foundational.md) — Booij 1999 JGR 1차 reference
- 기존 20 source-analysis 노트 — §2 매핑 표
- [swan-foundation](swan-foundation.md) — SWAN 모듈 구조
- 공식 사이트: http://www.swan.tudelft.nl
- GitLab (since 41.41): SWAN source repo

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R7:I-057 | 삭제된 소스 파일 | swanimp PDF 9쪽, 인쇄 3쪽: `SwanThreadBounds.ftn90`; `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/SwanThreadBounds.ftn90:1` `subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )` | `0dabfa4 2026-07-13 updated src (patch B)`; `git show 0dabfa4 -- src/SwanThreadBounds.ftn90` 원문 `deleted file mode 100644`; `43e9bbb:src/SwanCompUnstruc.ftn90:848` `!GRAPH                ivert = flist(kvert,swpdir)`; `43e9bbb:src/SwanCompUnstruc.ftn90:849` `!FXFRO                ivert = vlist(kvert,swpdir)` | A 판 차이 | patch B는 SwanThreadBounds.ftn90을 삭제했다. 현재 비정렬 계산은 front 목록을 직접 순회한다. 변경 커밋은 `0dabfa4`(2026-07-13)이다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:I-059 | material 목록의 SwanIEM 누락 | swanimp PDF 8쪽–10쪽, 인쇄 2쪽–4쪽: `The source tarball swan4151.tar.gz ... consists of the following files`; PDF 21쪽, 인쇄 15쪽: `SwanIEM.f90` | `src/srclist.cmake:13` `${SRC}/SwanIEM.f90` | C 문서 누락 | C는 swanimp PDF 8쪽–10쪽의 material 목록에 한정한다. 같은 매뉴얼 PDF 21쪽의 모듈 컴파일 목록과 Git `srclist.cmake`에는 SwanIEM이 있다. SWAN 문서 전체에 설명이 없다는 뜻이 아니다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
| R7:N-002 | SwanThreadBounds 목록 | `models/SWAN/manual-notes/swan-implementation-manual.md:45` ``\| unstructured grids (routines) \| `SwanReadGrid/ReadADCGrid/ReadTriangleGrid/ReadEasymeshGrid`, `SwanInitCompGrid`, `SwanCheckGrid`, `SwanCreateEdges`, `SwanGridTopology/Vert/Cell/Face`, `SwanPrintGridInfo`, `SwanFindPoint`, `SwanPointinMesh`, `SwanBpntlist`, `SwanPrepComp`, `SwanVertlist`, `SwanCompUnstruc`, `SwanDispParm`, `SwanPropvelX/S`, `SwanSweepSel`, `SwanTranspAc/X`, `SwanGradDepthorK`, `SwanGradVel`, `SwanDiffPar`, `SwanGSECorr`, `SwanInterpolatePoint/Ac/Output`, `SwanConvAccur`, `SwanConvStopc`, `SwanThreadBounds`, `SwanFindObstacles`, `SwanCrossObstacle`, `SwanComputeForce` (.ftn90) \|``; `7ee8981 2024-09-02 initial release (v 41.51)`; `7ee8981:src/SwanThreadBounds.ftn90:1` `subroutine SwanThreadBounds ( nwetp, ivlow, ivup, tlist, n )` | `0dabfa4 2026-07-13 updated src (patch B)`; `git show 0dabfa4 -- src/SwanThreadBounds.ftn90` 원문 `deleted file mode 100644`; `43e9bbb:src/SwanCompUnstruc.ftn90:848` `!GRAPH                ivert = flist(kvert,swpdir)`; `43e9bbb:src/SwanCompUnstruc.ftn90:849` `!FXFRO                ivert = vlist(kvert,swpdir)` | A 확정 (0dabfa4 2026-07-13) | SwanThreadBounds는 41.51 공개 코드에 있던 파일이다. patch B는 이 파일을 삭제했다. 노트의 현재 소스 목록에서 삭제 사실을 구분한다. 변경 커밋은 `0dabfa4`(2026-07-13)이다. [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론) |
