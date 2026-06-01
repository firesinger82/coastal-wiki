---
title: "SWAN Surfbeat IEM (Infragravity Energy Model) — SwanIEM.ftn90 verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/SwanIEM.ftn90` 직접 read (1230 lines, line 1-130 module header + grep 4 subroutines). User cmd SURFBEAT (swanuse.pdf p.80) 매핑."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header verbatim"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-quasi-coherent.md
---

## Scope

SwanIEM.ftn90 — SWAN 41.85 (2019-01 Reniers) 신규 module. **1D surfbeat = infragravity wave (IG)** 모델 — 단파(short wave) 그룹의 bound IG + radiation stress 변동 → free IG 변환. User cmd `SURFBEAT` (p.80).

## Source basis

- `SwanIEM.ftn90` (1230 lines)
- User cmd `SURFBEAT` (swanuse.pdf p.80)
- 본 module 의 Tech 문서 §은 미식별 (SWAN Tech swantech.pdf TOC 에 명시 §없음)

## 1. Module header (line 1-2, 32-46 verbatim)

```
! This file contains data and routines for surfbeat (Infragravity Energy Model)
module SwanIEM
!   Authors
!   41.85: Ad Reniers
!   Updates
!   41.85, January 2019: New module
!   Purpose
!   Contains data with respect to 1D surfbeat
```

→ **Reniers** = surfbeat / IG 이론 1차 (Reniers·MacMahan·Thornton·Stanton 2007 시리즈).

## 2. Module data (line 54-71)

```fortran
integer :: nf, nff, nif                ! nf=총 freq, nif=incident freq 수
integer :: nmax                        ! short-wave pair 최대 수
integer, save :: ntf = -9              ! IG frequencies 수 (< 0 first COMPUTE, > 0 second COMPUTE)

integer, allocatable :: iss(:), iwt(:), itt(:)   ! 인덱스 배열

real :: dfiem                          ! incident spectrum frequency resolution (constant)
real :: e_trsh                         ! energy threshold (Emax fraction)
real, allocatable :: E0(:,:)           ! offshore energy density [J/m²], uniformly distributed
real, allocatable :: Ebig(:,:,:)       ! BOUND infragravity wave energy
real, allocatable :: freq(:)           ! uniformly distributed relative frequencies

logical :: sflog                       ! IG freq distribution: linear (false) or log (true)
```

핵심:
- `Ebig` = **bound infragravity wave energy** — Longuet-Higgins·Stewart 1962 group-bound long wave
- `ntf` 의 부호 = COMPUTE 단계 표시 (first → IG 격자 설정, second → 실제 계산)
- `e_trsh` = small-energy threshold (numerical stability)
- `sflog` = uniform vs logarithmic frequency grid

## 3. Subroutine inventory (4 subroutines)

| Line | Subroutine | Purpose |
|---|---|---|
| **78** | `SwanIEMinitig` | IG 격자 초기화 (incident spectrum → bound IG 격자 생성) |
| **324** | `SwanIEMmeanwav(AC2, HSIBC, SPCSIG, KGRPNT, HS)` | Mean wave 통계 (H_s 등) for IG boundary |
| **488** | `SwanIEMncalc` | IG 계산 핵심 (free vs bound 변환?) |
| **679** | `SwanIEMsrfbeat(HS, AC2, DEP2, SPCDIR, SPCSIG, KGRPNT)` | **Surfbeat source term** — main contribution |

### 3.1 SwanIEMinitig (line 78, header verbatim)

> "Initializes several variables and arrays for the computation of reflected waves"

→ 단순 init 라기보다는 reflected wave (= IG 의 free 부분, 해안에서 반사) 격자 준비.

### 3.2 SwanIEMmeanwav (line 324)

인자: `AC2, HSIBC, SPCSIG, KGRPNT, HS`.
- `AC2` = action density
- `HSIBC` = H_s at IG boundary
- `HS` = significant wave height
→ short-wave 통계로부터 IG bound energy 계산을 위한 mean wave 정보 제공.

### 3.3 SwanIEMncalc (line 488)

자세한 인자 없음. 내부 `Ebig` array 갱신 추정.

### 3.4 SwanIEMsrfbeat (line 679)

인자: `HS, AC2, DEP2, SPCDIR, SPCSIG, KGRPNT`.
→ Surfbeat = depth-modulated wave group → 천해 IG amplification. `DEP2` (수심) 변화 시 bound → free 전환.

## 4. Surfbeat physics 배경

**Infragravity wave (IG)** = 0.01 ~ 0.05 Hz (20~100 s 주기) 의 sub-harmonic ocean wave. 주된 형성 mechanism:

1. **Bound IG** (Longuet-Higgins·Stewart 1962): short-wave group 의 radiation stress 변동 → group-bound long wave
2. **Free IG** at shore: bound IG 가 surf zone 에서 단파 breaking 후 free 로 release → coastal IG sea level oscillation
3. **Edge wave / leaky wave**: 해안 반사된 IG

해안공학 응용:
- **Harbor resonance** (oscillation in marinas/harbors)
- **Storm surge cascade with IG** (storm 시 IG 가 mean sea level 추가)
- **Beach groundwater pumping** (IG 가 swash 영역 침투)
- **Coral reef IG flooding** (open ocean 보다 atoll 가 IG 에 더 노출)

## 5. User cmd `SURFBEAT` (swanuse.pdf p.80)

명령 활성 시 SwanIEM module이 standard SWAN 위에 IG model 부가. 출력에 IG H_s, 주기 등 추가.

## 6. Cross-references

- [[swan-documentation-stack]] — User cmd SURFBEAT (p.80)
- [[swan-source-coverage-audit]] §3.1 신규 발견
- [[swan-quasi-coherent]] — 다른 phase-resolving 시도 (QCM 41.90 vs IEM 41.85)
- [[swan-bragg-scattering]] — 또 다른 phase 효과 (산란)
- Author: Ad Reniers (41.85, 2019-01) — Reniers·MacMahan·Thornton·Stanton 학파
- 외부 reference 추정: Reniers et al. 2002 *Coastal Eng*, Reniers·Roelvink·Battjes 2004 *JGR*

## 7. 한계 + 다음 단계

- 본 module 의 Tech 문서 §매핑 부재 (TOC 미수록) → swantech.pdf 본문 검색 후속
- 외부 reference (Reniers 학파) DOI 검증 필요
- `SwanIEMncalc` 의 정확 알고리즘 (488-678 라인) deep dive 별도
- 1D only ("1D surfbeat" header 명시) → 2D unstructured 확장 여부 추후
- User Manual SURFBEAT (p.80) cmd 사양 직접 인용 별도
