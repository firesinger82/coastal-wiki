---
title: "SWAN Quasi-Coherent Modelling (QCM) — SwanQCM.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanQCM.ftn90` 직접 read (3464 lines, line 1-80 module header + grep subroutine 12개 위치). Tech §2.7 (Wigner distribution evolution + QC approximation, p.58-64) + §3.9 implementation (p.102) + User cmd SCAT (p.81)."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header verbatim + subroutine map"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/source-analysis/swan-bragg-scattering.md
---

## Scope

SwanQCM.ftn90 — SWAN 41.90 (2021-06) Akrish·Smit·Zijlema 신규 module. **Wigner distribution** 기반 quasi-coherent wave modelling — phase-resolving wave 효과 (diffraction, scattering, interference) 를 spectral SWAN 안에 통합. 본 module 은 SWAN의 가장 큰 신규 물리 추가 중 하나. Tech §2.7 + §3.9 + User cmd `SCAT` (p.81).

## Source basis

- `SwanQCM.ftn90` (3464 lines) — module + 12 subroutines
- Tech §2.7 Quasi-coherent modelling (p.58-64): Wigner distribution / evolution eq / QC approx
- Tech §3.9 QC implementation (p.102)
- User cmd `SCAT` (p.81)

## 1. Module header (line 34-46)

```
module SwanQCM
!   Authors
!   41.90: Gal Akrish, Pieter Smit and Marcel Zijlema
!   Updates
!   41.90, June 2021: New module
!   Purpose
!   Contains data with respect to quasi-coherent modelling
```

## 2. Module data (line 54-78)

```fortran
integer :: mkxc, mkyc        ! wavenumber space size (x, y)
integer :: mxd, myd          ! dissipation grid size (x, y)
integer :: ncoz              ! coherent region / scattering wavenumber space size

integer :: lensav, lensvd, lenwfd, lenwft  ! FFT work array sizes

real, allocatable :: disbk0(:), disbk1(:)  ! bulk dissipation surf-breaking (previous + current iter)
real, allocatable :: kx(:), ky(:)          ! wavenumber components
real, allocatable :: xpsc(:)               ! coherent scattering region for FFT
real, allocatable :: xpd(:), ypd(:)        ! spatial lag grid (surf breaking)
real, allocatable :: kxd(:), kyd(:)        ! wavenumber 공간 (lag grid)
```

핵심: **dual grid system** — 일반 spectral grid (mkxc·mkyc) + **spatial lag grid** (mxd·myd, surf breaking dissipation 전용) + coherent scattering wavenumber (ncoz). FFT 4개 (lensav/lensvd/lenwfd/lenwft).

## 3. Subroutine inventory (12 sub-routines)

| Line | Subroutine | Purpose (Tech §2.7/§3.9 매핑) |
|---|---|---|
| **83** | `SWQCINIT(BGRIDP, COMPDA)` | QCM framework 초기화 (FFT 준비 + wavenumber 격자) |
| **697** | `SWQCDFT(sigft, cgft, dep2, kwave, cgo, cft, rft, sft, wft, wsave)` | Direct FFT — spectral → 공간 (action density) |
| **943** | `SWQCUFT(uxft, uyft, dep2, ux2, uy2, cft, rft, sft, wft, wsave)` | Velocity field FFT (ambient current 결합) |
| **1165** | `QCSOURCE(imatra, imatda, iter, ac2, dep2, ux2, uy2, ...)` | **QC source term assembly** — main contribution to S |
| **1417** | `SWQCWIG(W, dwdx, dwdy, ac2, dep2, rdx, rdy, spcdir, spcsig)` | **Wigner distribution W 계산** + 공간 gradient |
| **1656** | `SwanGradWig(W, dwdx, dwdy, ac2, dep2, spcdir, spcsig)` | Wigner gradient (unstructured grid 변형) |
| **2050** | `SWQCSCAT(memqcm, W, dwdx, dwdy, sigft, cgft, uxft, uyft, dep2, kwave, cgo, spcdir, spcsig)` | **QC scattering source** (W 기반 산란) |
| **2367** | `SWQCSURF(memqcb, ac2, dep2, cfd, wfd, wsavd, kwave, cgo, spcdir, spcsig)` | **QC surf breaking** (공간 lag grid + 일관된 dissipation) |
| **2698** | `bdiss` (nested, in SWQCSURF) | Bulk dissipation 계산 |
| **3106** | `varchk` (nested) | Variance check (numerical safety) |
| **3187** | `FILQCM(imatra, idcmin, idcmax, isstop, memqcm, memqcb, plqcs, plwbrk, redc0, dissc0)` | Source term filtering + output |
| **3342** | `tukeywin(a, n)` | Tukey window function (FFT 주변 effect 억제) |

## 4. 이론 (Tech §2.7)

### 4.1 Wigner distribution (Tech §2.7.1, p.58)

스펙트럼 action density $N(\sigma, \theta; x, t)$ 가 **Wigner distribution** $W(k; x, t)$ 로 변환:

$$W(\vec{k}, \vec{x}, t) = \int \langle a^*(\vec{x} - \vec{r}/2, t) a(\vec{x} + \vec{r}/2, t) \rangle e^{-i\vec{k}\cdot\vec{r}} d^2r$$

여기서 $a(\vec{x}, t)$ = complex envelope, ⟨⟩ = ensemble average.

**Wigner 의 장점**: 일반 spectral action density 가 모든 점에서 양의 값인 반면, W 는 **interference pattern (음의 lobe 포함)** 도 표현 가능 → diffraction·focusing 등 phase 효과 자연 표현.

### 4.2 Evolution equation (Tech §2.7.2, p.61)

$$\partial_t W + \vec{c}_g \cdot \nabla_x W + \vec{c}_\theta \cdot \nabla_k W = S_W$$

기존 SWAN action balance ([[swan-action-balance]]) 와 동일 구조이지만 **k-space gradient 항이 W 의 미세 변동에 sensitive** → spatial coherence 표현.

### 4.3 QC approximation (Tech §2.7.3, p.64)

Full Wigner evolution 계산 비용 큼 → **quasi-coherent approximation**: W 를 일반 spectrum + 작은 coherent 부분으로 분리:

$$W = N_0 + W_c, \quad |W_c| \ll |N_0|$$

`SwanQCM.ftn90` 의 `ncoz` (coherent region size) 가 이 분리의 격자 크기.

## 5. Implementation (Tech §3.9, p.102)

1. **SWQCINIT** — FFT 준비, wavenumber 격자 초기화
2. **SWQCWIG** — Wigner W 계산 (current 시점)
3. **SWQCDFT / SWQCUFT** — FFT 적용 (spectral ↔ spatial 변환)
4. **SWQCSCAT** — scattering source term (W 기반)
5. **SWQCSURF** — surf breaking 의 quasi-coherent 처리 (`disbk0/disbk1` iteration)
6. **QCSOURCE** — 위 모두 통합 → imatra·imatda 누적
7. **FILQCM** — 출력

iteration 반복: `disbk0` (previous) → `disbk1` (current) → convergence.

## 6. User cmd `SCAT` (swanuse.pdf p.81)

`SCAT` 명령으로 QCM 활성. SWAN의 표준 spectral model 위에 phase-resolving 효과를 추가. 해안공학 응용: harbor diffraction, breakwater 회절, coherent multiple reflection.

## 7. Cross-references

- [[swan-documentation-stack]] §2.7 Wigner + §3.9 implementation
- [[swan-action-balance]] — 표준 spectral N(σ,θ;x,t) (QC 분리의 N_0 부분)
- [[swan-diffraction-obstacles]] — 별도 mild-slope diffraction (Holthuijsen 2003) vs QC 회절
- [[swan-bragg-scattering]] — k-k' 산란 (Bragg) vs spatial coherence (QC) 의 서로 다른 산란 mechanism
- Authors: Gal Akrish + Pieter Smit + Marcel Zijlema (41.90, 2021-06)
- 원논문 추정: Smit·Janssen 2013 *J Fluid Mech* (QC 기반) + Akrish 2020s 후속

## 8. 한계

- Wigner W 의 정확 식 (line 1417 SWQCWIG) 직접 인용 별도. Tech §2.7.2 식 (eq 번호 미확정).
- `SWQCSURF` 의 surf breaking 처리 (`disbk0/disbk1` iteration) 가 표준 SWAN BREAKING (Battjes-Janssen) 과 어떻게 결합되는지 별도 추적.
- Authors 원논문 (Akrish·Smit·Zijlema) DOI 검증 필요 (현재 source code header 기반 추정).
- 본 module 의 cost (3464 lines, 12 subroutines, 4 FFT) 가 spectral SWAN 대비 큼 → 실용 적용 시기·격자 크기 검증 가치.
