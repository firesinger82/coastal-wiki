---
title: "SWAN Bragg scattering — SwanBraggScat.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw source `models/SWAN/raw/source_code/swan/src/SwanBraggScat.ftn90` 직접 read (1491 lines, line 1-150 module header + line 524-1382 subroutine 위치). [[swan-documentation-stack]] §2.3.7 Bragg scattering (Tech p.48) + User Manual cmd `BRAGG` (p.71) 매핑."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header verbatim + grep subroutines"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/manual-notes/swan-booij-1999-jgr-foundational.md
---

## Scope

SwanBraggScat.ftn90 모듈의 SWAN Bragg scattering (저면 spectrum 과 wave 의 비선형 산란) 구현. SWAN 41.80 (2021-09 Rijnsdorp+Reniers) 신규 module — 1차 reference physics. Tech §2.3.7 (p.48) + User cmd BRAGG (p.71).

## Source basis

- `models/SWAN/raw/source_code/swan/src/SwanBraggScat.ftn90` (1491 lines)
- Tech §2.3.7 (swantech.pdf p.48) — Bragg scattering theory
- User cmd BRAGG (swanuse.pdf p.71)

## 1. Module header (line 30-45 verbatim)

```
module SwanBraggScat
!   Authors
!   41.80: Dirk Rijnsdorp and Ad Reniers
!   Updates
!   41.80, September 2021: New module
!   Purpose
!   Contains data with respect to Bragg scattering
```

## 2. Module-level data (line 53-65)

```fortran
integer :: mkbx, mkby                              ! wave number space size (x, y) for bottom spectrum
real    :: dkbx, dkby                              ! wave number space resolution
real, allocatable :: botspc(:,:)                   ! bottom spectrum (user-provided)
real, allocatable :: dpmean(:)                     ! mean depth at computational grid points
real, allocatable :: fb(:,:,:)                     ! bed elevation spectrum at computational grid points
real, allocatable :: fbdxy(:,:,:,:)                ! bottom spectrum at wave number difference k-k' for all grid points
```

→ **2D wavenumber spectrum** 의 저면 정의 (`botspc`) + **convolution-based** wave number difference spectrum (`fbdxy(k-k')`).

## 3. Subroutine inventory (7 sub-routines, line 69-1491)

| Line | Subroutine | Purpose |
|---|---|---|
| **69** | `SWBRBOT` | 평균 수심 + bed elevation spectrum 계산 (computational grid 별) |
| **524** | `fit2(x,y,z,n,a,b,c,ierr)` | 2D polynomial fit (depth grid → comp grid) |
| **561** | `SWFBXY(dep2, mudl2, spcsig, spcdir)` | Wave number difference spectrum 계산 |
| **771** | `SWFB(fbd, dep2, kwave, ecos, esin)` | Bed elevation spectrum 보간 (wave dir·freq 별) |
| **942** | `SWBRAGG1` | Bragg source term version 1 |
| **1094** | `SWBRAGG2` | Bragg source term version 2 (extended) |
| **1247** | `SWBRAGG3` | Bragg source term version 3 (membrg variant) |
| **1382** | `FILBRG` | Bragg source term filtering / output |

## 4. SWBRBOT — mean depth + bed elevation spectrum (line 69-)

핵심 use clause:
```fortran
use ocpcomm4
use swcomm2
use swcomm3, only: pbrag, PI, MXC, MYC, MCGRD
use m_genarr, only: DEPTH, XCGRID, YCGRID, KGRPNT
use SwanGriddata, only: nverts, xcugrd, ycugrd
```

→ `DEPTH`, `XCGRID/YCGRID`, `KGRPNT` (input depth grid + computational grid mapping) + `SwanGriddata` (unstructured vertex coord).

Local 변수 핵심:
- `nreg` = region of depth points around comp grid point (size for mean + spectrum)
- `ix, iy` loop counter (depth grid window)
- `ixc, iyc` loop counter (comp grid)
- `vard` = variance of small scale bed elevation
- `lensav, lenwrk` = FFT work array sizes (fftpack51 호출 추정)
- `p0, p1, p2` = polynomial fit coefficients (real*8)

알고리즘 (추정):
1. Comp grid point 주변 depth grid window 추출
2. 평균 수심 `dpmean(ic)` 계산
3. 잔차 (depth - polynomial fit) → bed elevation small-scale variance `vard`
4. FFT 적용 → 2D wave number spectrum `fb(:,:,ic)`

## 5. 3 Bragg source term variants (`SWBRAGG1/2/3`)

Tech §2.3.7 에 따른 3 가지 Bragg source term 식 구현 추정. User cmd `BRAGG` (p.71) 의 옵션 선택 가능:
- SWBRAGG1: 기본 Bragg (k-k' resonance 1차)
- SWBRAGG2: extended (mud layer `mudl2` 결합 추정 — line 561 `SWFBXY` 도 `mudl2` 인자 보유)
- SWBRAGG3: membrg variant (`membrg` 인자) — membrane-like reflection?

각 `SWBRAGG*` 인자:
- `imatra` = source term matrix
- `ac2` = action density spectrum
- `dep2` = depth
- `kwave, cgo` = wave number + group velocity
- `fbd` = bed elevation spectrum (SWFB 의 출력)
- `idcmin/idcmax/isstop` = directional index bounds
- `ecos/esin` = direction cosine/sine arrays
- `plbrag` = print/diagnostic
- `redc0` = reduction coefficient

→ 모두 `imatra` 에 contribution 누적 = SWAN source term matrix 의 diagonal/off-diagonal 항 추가.

## 6. User cmd BRAGG (swanuse.pdf p.71)

사용자 입력으로 `pbrag` (parameter) + `botspc(2D wavenumber spectrum)` 외부 파일 제공. SWAN 시작 시 `SWBRBOT` 가 보간 → `SWFBXY` 가 difference spectrum 구성 → 시간 step 마다 `SWBRAGG*` 가 source term 추가.

## 7. 이론적 기반

**Bragg scattering** = bottom topography (랜덤 또는 결정적) 와 wave 의 **k-k' 공명 산란**:

$$k_1 + k_2 = K_b$$

여기서 $K_b$ 는 bottom topography 의 2D wavenumber spectrum.

조건: $\lambda_{wave}/2 \approx \lambda_{bottom}$ (long-wave / short-bed wave 공명).

해안공학 응용: sand bar field, ripple field 위 wave 전파 시 wave energy redistribution.

## 8. Cross-references

- [[swan-documentation-stack]] §2.3.7 Bragg scattering theory
- [[swan-source-terms-implementation]] — S_total = S_in + S_ds + S_nl + **S_bragg** 통합
- [[swan-source-coverage-audit]] §3.1 신규 발견 식별
- User Manual BRAGG cmd (p.71)
- Authors: Dirk Rijnsdorp + Ad Reniers (41.80, 2021-09)

## 9. 한계

- 본 노트는 module header + subroutine inventory + use clause. 식 (Bragg source term 공식) 직접 인용은 별도 Tech §2.3.7 deep read 필요.
- SWBRAGG1 vs 2 vs 3 분리 기준 (User cmd BRAGG 옵션 매핑) 직접 검증 필요.
- 외부 bottom spectrum 입력 포맷 (`botspc(mkbx, mkby)`) 의 User Manual cmd BRAGG 사양 별도.
- FFT 사용 추정 — fftpack51 직접 호출 위치 확인 필요.
