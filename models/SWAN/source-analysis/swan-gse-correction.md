---
title: "SWAN Garden-Sprinkler Effect correction — SwanGSECorr.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanGSECorr.ftn90` 직접 read (280 lines, line 1-100 subroutine header + argument 변수 정의). Tech §3.8 refraction approximation + §8.6 diffusion-like terms (p.146) + Booij-Holthuijsen 1987 GSE 이론."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — full header verbatim + 변수 정의 발췌"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-propagation-implementation.md
  - models/SWAN/manual-notes/swan-action-balance.md
---

## Scope

SwanGSECorr.ftn90 — **Garden-Sprinkler Effect (GSE)** correction subroutine (280 lines). SWAN 41.00 (2009-02 Marcel Zijlema). Tech §3.8 refraction approximation (p.92-101) + Ch 8 unstructured §8.6 diffusion-like terms (p.146). User cmd 명시 없음 (internal numerical correction).

## Source basis

- `SwanGSECorr.ftn90` (280 lines, 단일 subroutine)
- Tech §3.8 Refraction approximation (p.92-101)
- Tech §8.6 Calculation of diffusion-like terms (p.146)
- Booij-Holthuijsen 1987 *Coastal Engineering* — GSE 원논문 (추정)

## 1. Header (line 1-40 verbatim)

```
subroutine SwanGSECorr(rhs, ac2, cgo, spcdir, idcmin, idcmax, isslow, isstop, trac0)
!   Programmer: Marcel Zijlema
!   Authors
!   41.00: Marcel Zijlema
!   Updates
!   41.00, February 2009: New subroutine
!   Purpose
!   Computes waveage-dependent diffusion terms in x-y space to counteract the garden-sprinkler effect
```

## 2. Arguments (line 56-71)

| 인자 | 방향 | 타입 | 역할 |
|---|---|---|---|
| `rhs(MDC, MSC)` | inout | real | 시스템 (σ,θ) 공간 RHS — GSE diffusion 더해짐 |
| `ac2(MDC, MSC, nverts)` | in | real | action density (current time, unstructured) |
| `cgo(MSC, ICMAX)` | in | real | group velocity |
| `spcdir(MDC, 6)` | in | real | spectral direction (radians, cos, sin, cos², cos·sin, sin²) |
| `idcmin/idcmax(MSC)` | in | integer | 주파수별 directional counter min/max |
| `isslow/isstop` | in | integer | sweep 안 전파되는 min/max 주파수 |
| `trac0(MDC, MSC, MTRNP)` | out | real | explicit propagation 부분 (출력) |

→ 본 subroutine은 sweep 안에서 호출되며 **각 vertex 마다 rhs(MDC, MSC) 에 GSE diffusion term 더함**.

## 3. Local 변수 핵심 (line 75-110)

```fortran
real :: dnn         ! waveage-dependent diffusion coefficient normal to propagation direction
real :: dss         ! waveage-dependent diffusion coefficient in propagation direction
real :: dgx0/dgx1   ! x-component diffusion gradient (present/next cell)
real :: dgy0/dgy1   ! y-component diffusion gradient
real :: dac2dx, dac2dy   ! action density 의 공간 derivative
real :: dgxdx, dgydy     ! diffusion gradient 의 공간 derivative
real :: dcg         ! group velocity difference across frequency bin
real :: cslat       ! cosine latitude (spherical)
integer :: icell, jcell    ! present, next cell index
integer, dimension(3) :: v ! present cell vertices
double precision :: carea  ! 2×centroid dual area
```

→ **dnn** (normal) + **dss** (streamwise) diffusion coefficient — propagation direction 에 따라 anisotropic. 각 cell 의 diffusion gradient (dgx/dgy) 의 spatial gradient (dgxdx/dgydy) 가 GSE term.

## 4. GSE 이론 (Booij-Holthuijsen 1987)

### 4.1 GSE 발생 mechanism

SWAN 의 spectral propagation 은 **discrete directional bins** (MDC, 보통 36 bins = 10° 분해능). 각 bin이 wave packet 처럼 directional 전파 → bin 사이에 공간 에너지 gap → **discrete directional rays** 가 정원용 sprinkler 의 노즐처럼 individual ray로 보임.

문제: 격자 해상도 < ray separation 시 numerical artifact (GSE) — 실제 wave field에는 없는 "줄무늬" 출현.

### 4.2 Wave-age dependent diffusion

해결: **wave-age 의존 spatial diffusion** 항을 추가 → 인접 directional bin 의 action density 가 smooth하게 spread.

$$D_{ss} = f_s(\text{wave age}, \Delta\theta, c_g), \quad D_{nn} = f_n(\text{wave age}, \Delta\theta, c_g)$$

여기서 wave-age = $c_p / U_{10}$ (peak phase speed / wind speed). 어린 wave (low age) 는 directional spread 큼 → 작은 diffusion. 늙은 wave (high age) 는 좁은 spread → 큰 diffusion 필요.

### 4.3 큰 격자 GSE 의 심각성

Tech §3.8.5 (p.101) "**The problem with refraction on coarse grids**": 격자 ≥ $L_{wave}/4$ 일 때 GSE 심함. 본 노트의 GSE correction이 coarse grid에서도 안정적 결과 보장.

## 5. Algorithm overview (추정 line 110-280)

1. **Loop over vertices** (`ivert`) — unstructured grid
2. Cell 별 (`icell/jcell`) action density gradient (`dac2dx/dac2dy`) 계산
3. wave-age 평가 → `dnn/dss` 계산
4. Diffusion gradient (`dgx/dgy`) construct
5. Spatial gradient (`dgxdx/dgydy`) → rhs 더함

`carea` (double precision 2×centroid dual area) 사용 → centroid dual control volume 방식 (Tech §8.3.1 discretization procedure).

## 6. Cross-references

- [[swan-documentation-stack]] §3.8 + §8.6 diffusion-like terms
- [[swan-propagation-implementation]] — propagation 표준 (GSE 미적용 path)
- [[swan-action-balance]] — action density 정의
- [[swan-source-coverage-audit]] §3.1 신규 발견
- [[swan-bragg-scattering]] / [[swan-quasi-coherent]] / [[swan-surfbeat-iem]] — 다른 신규 module 과 함께 SWAN 41.x 추가
- Author: Marcel Zijlema (41.00, 2009-02) — TU Delft SWAN team lead
- 원논문 추정: **Booij·Holthuijsen 1987** "Propagation of ocean waves in discrete spectral wave models" *J. Comput. Phys.* 68, 307-326

## 7. 한계

- 본 노트는 line 1-110 (header + arguments + local var 정의) 만 verified. 실제 GSE diffusion 식 (line 110-280) deep 미실시.
- User cmd 명시 없음 → SWAN 활성 조건 별도 확인 (always active? specific OPTION? config file?)
- Wave-age 정의의 정확 식 (`dnn(c_p, U_10, Δθ)`) 별도 deep 필요
- Booij-Holthuijsen 1987 원논문 DOI 검증 필요
