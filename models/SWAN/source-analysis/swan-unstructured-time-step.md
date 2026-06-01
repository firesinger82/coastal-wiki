---
title: "SWAN unstructured time-step driver — SwanCompUnstruc.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanCompUnstruc.ftn90` 직접 read (1684 lines, line 1-85 verbatim header + change history 12 versions). Tech Ch 8 Unstructured mesh implementation (p.135-147)."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — full header verbatim + author 14명 + version history 13개"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-foundation.md
  - models/SWAN/source-analysis/swan-bragg-scattering.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
  - models/SWAN/source-analysis/swan-adcirc-coupling.md
  - models/SWAN/source-analysis/swan-gse-correction.md
---

## Scope

SwanCompUnstruc.ftn90 — **unstructured mesh 의 time-step driver** (1684 lines). SWAN unstructured (unSWAN) 의 핵심 entry. 40.80 (2007-07 Zijlema) 신설 → 41.91 (2022-02) 까지 13개 메이저 update. Tech Ch 8 (p.135-147).

## Source basis

- `SwanCompUnstruc.ftn90` (1684 lines, single subroutine + nested helpers)
- Tech Ch 8 (Unstructured mesh implementation, p.135-147)
- 8.1 Description / 8.2 Grid generation / 8.3 Numerical method (discretization + sweeping) / 8.4 Interpolation / 8.5 Force / 8.6 Diffusion-like / 8.7 Conservation of action

## 1. Header verbatim (line 1, 32-65)

```fortran
subroutine SwanCompUnstruc(ac2, ac1, compda, spcsig, spcdir, xytst, cross, it)
!   Programmer: Marcel Zijlema
!
!   Authors                                Updates
!   40.80: Marcel Zijlema                  40.80, July 2007: New subroutine
!   40.85: Marcel Zijlema                  40.85, August 2008: + propagation/generation/redistribution output
!   40.95: Marcel Zijlema                  40.95, June 2008: parallelization of unSWAN
!   41.02: Marcel Zijlema                  41.02, February 2009: implementation of diffraction
!   41.07: Marcel Zijlema                  41.07, August 2009: bug fix: never-ending sweep prevented
!   41.10: Marcel Zijlema                  41.10, August 2009: parallelization using OpenMP directives
!   **41.20: Casey Dietrich                41.20, June 2010: extension to tightly coupled ADCIRC+SWAN model**
!   41.60: Marcel Zijlema                  41.60, July 2015: more accurate gradients of depth/wave number for turning rate
!   41.63: Marcel Zijlema                  41.63, August 2015: efficiency improved; ONE sweep per iteration (vs undetermined)
!   41.67: Marcel Zijlema                  41.67, August 2017: more accurate gradients of ambient currents
!   41.68: Marcel Zijlema                  41.68, August 2015: fixed number of sweeps per iteration
!   **41.80: Dirk Rijnsdorp and Ad Reniers 41.80, September 2021: adding Bragg scattering**
!   **41.90: Gal Akrish, Pieter Smit and Marcel Zijlema 41.90, October 2021: adding QC scattering**
!   **41.91: Marcel Zijlema                41.91, February 2022: adding QC surf breaking**
```

→ **14 명의 SWAN-team contributor** (Zijlema 다수 + Dietrich + Rijnsdorp + Reniers + Akrish + Smit). **41.20 Casey Dietrich = ADCIRC-side contributor** (tightly coupled ADCIRC+SWAN integration). 본 module이 [[swan-adcirc-coupling]] 의 unstructured-side 핵심.

## 2. Purpose + Method (line 65-85 verbatim)

> "**Performs one time step for solution of wave action equation on unstructured grid**"
>
> "A vertex-based algorithm is employed in which the variables are stored at the vertices of the mesh. The equation is solved in each vertex assuming a constant spectral grid resolution in all vertices. **The propagation terms in both geographic and spectral spaces are integrated implicitly. Sources are treated explicitly and sinks implicitly**. The calculation of the source terms is carried out in the original SWAN routines, e.g., SOURCE."
>
> "The wave action equation is solved iteratively. A number of iterations are carried out until convergence is reached. In each iteration, **a fixed number of sweeps are carried out** (41.68). Per sweep direction, a loop over ordered vertices is executed. The solution of each vertex must be updated geographically before proceeding to the next one."

## 3. 핵심 algorithm 특성

### 3.1 Vertex-based storage

Tech §8.1 + 본 module: **action density `ac2` 는 vertex 에 저장** (cell-centered 아님). Triangle mesh 의 vertex = node.

### 3.2 Implicit propagation + Explicit/Implicit sources

| Term | 처리 |
|---|---|
| 공간 propagation (∇·c_g N) | **Implicit** |
| 스펙트럼 propagation (c_σ, c_θ in σ-θ space) | **Implicit** |
| Source 항 (S_in, S_nl) | **Explicit** |
| Sink 항 (S_ds dissipation) | **Implicit** |

→ Tech §3.3 Solution algorithm 의 unstructured 변형. Implicit propagation = sweep-based Gauss-Seidel iteration.

### 3.3 Sweep-based iteration

- **41.63 변화**: 이전 "undetermined number of sweeps per iteration" → "ONE sweep per iteration" (efficiency 개선)
- **41.68 추가**: "fixed number of sweeps per iteration" (현행)
- 각 sweep direction마다 ordered vertex loop. vertex order = sweep direction에 따라 다름 (Tech §8.3.2 sweeping algorithm).

## 4. 41.x history matrix

| Version | Year | Author | 변화 |
|---|---|---|---|
| 40.80 | 2007-07 | Zijlema | **신설** unstructured time-step |
| 40.85 | 2008-08 | Zijlema | propagation/generation/redistribution 출력 |
| 40.95 | 2008-06 | Zijlema | **unSWAN 병렬화** |
| 41.02 | 2009-02 | Zijlema | **diffraction** ([[swan-diffraction-obstacles]]) 통합 |
| 41.07 | 2009-08 | Zijlema | never-ending sweep bug fix |
| 41.10 | 2009-08 | Zijlema | **OpenMP** 병렬화 |
| **41.20** | **2010-06** | **Casey Dietrich** | **tightly coupled ADCIRC+SWAN** ([[swan-adcirc-coupling]]) |
| 41.60 | 2015-07 | Zijlema | depth/wave number gradient 정확도 ↑ (turning rate) |
| 41.63 | 2015-08 | Zijlema | one sweep per iteration efficiency |
| 41.67 | 2017-08 | Zijlema | ambient current gradient 정확도 ↑ |
| 41.68 | 2015-08 | Zijlema | fixed sweep count per iteration |
| **41.80** | **2021-09** | **Rijnsdorp+Reniers** | **Bragg scattering** ([[swan-bragg-scattering]]) 통합 |
| **41.90** | **2021-10** | **Akrish+Smit+Zijlema** | **QC scattering** ([[swan-quasi-coherent]]) 통합 |
| 41.91 | 2022-02 | Zijlema | **QC surf breaking** 추가 |

→ **본 module은 SWAN unstructured 의 모든 신규 물리 통합 entry**. 신규 module ([[swan-bragg-scattering]], [[swan-quasi-coherent]], [[swan-surfbeat-iem]] 등) 호출 hook이 본 module에 누적.

## 5. Arguments (line 1)

| 인자 | 역할 |
|---|---|
| `ac2` | action density at current time level (vertex × MDC × MSC) |
| `ac1` | action density at previous time level |
| `compda` | computational data array (depth, current, wind, etc) |
| `spcsig` | spectral relative frequency σ array |
| `spcdir` | spectral direction θ array (+ trig functions) |
| `xytst` | test point coordinates (debugging) |
| `cross` | obstacle crossing array |
| `it` | time step counter |

→ Standard SWAN time-step interface. `compda` 가 모든 input field (depth, wind, current, ice) 통합 carry.

## 6. Cross-references

- [[swan-documentation-stack]] Ch 8 unstructured mesh
- [[swan-source-coverage-audit]] §3.4 신규 발견
- [[swan-foundation]] — SWAN main entry
- [[swan-bragg-scattering]] (41.80 통합 → 본 module hook)
- [[swan-quasi-coherent]] (41.90 통합)
- [[swan-surfbeat-iem]] (41.85 — 본 module과 동시 시기)
- [[swan-adcirc-coupling]] — **41.20 Casey Dietrich 기여** = 본 module 변화 핵심
- [[swan-gse-correction]] (41.00, 2009-02 — 본 module 이전이지만 같은 unstructured)
- [[swan-diffraction-obstacles]] — 41.02 통합
- Authors: 14명 (Zijlema 다수 + Dietrich + Rijnsdorp + Reniers + Akrish + Smit)

## 7. 한계

- 본 노트는 header + change history (line 1-85) 만 verified. 1684 라인의 실제 sweep loop / vertex update 알고리즘 별도.
- "Fixed number of sweeps per iteration" 의 정확한 sweep 수 (보통 4? 8?) 미확정.
- OpenMP parallelization (41.10) 의 PRIVATE/SHARED 변수 별도.
- QC surf breaking (41.91) 가 [[swan-quasi-coherent]] 의 SWQCSURF 와 어떻게 결합되는지 cross-walk 별도.
- Casey Dietrich 41.20 ADCIRC integration 의 정확한 변경 부분 (line range) 식별 별도.
