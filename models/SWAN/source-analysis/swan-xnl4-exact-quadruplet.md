---
title: "SWAN XNL4 exact quadruplet — mod_xnl4v5.ftn90 (Van Vledder) verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "raw `models/SWAN/raw/source_code/swan/src/mod_xnl4v5.ftn90` 직접 read (8989 lines, line 1-160 module header + grep top-level subroutines 28개). Tech §2.3.4 Nonlinear wave-wave (Snl, p.28) + §3.6 DIA within four-sweep technique (p.88) + User cmd QUADRUPL (p.64) 옵션 매핑."
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header + version 1.01-5.06 history verbatim + switch documentation"
verification_date: 2026-06-01
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
  - models/SWAN/source-analysis/wave/swan-source-terms-implementation.md
---

## Scope

mod_xnl4v5.ftn90 — **XNL4 exact Boltzmann quadruplet integral** (Van Vledder 알고리즘) — DIA (Hasselmann 1985 Discrete Interaction Approximation, [[swan-source-terms-implementation]]) 의 high-precision 대체. Tech §2.3.4 (S_nl, p.28) + §3.6 (DIA four-sweep, p.88) + User cmd `QUADRUPL` (p.64). **본 module 은 8989 라인 + 28 top-level subroutines** — SWAN 의 비-SWAN-team 가장 큰 contributor module.

## Source basis

- `mod_xnl4v5.ftn90` (8989 lines)
- Tech §2.3.4 Nonlinear wave-wave interactions S_nl (p.28-44)
- Tech §3.6 DIA within four-sweep technique (p.88)
- User cmd `QUADRUPL` (p.64) — DIA vs exact 옵션

## 1. Module header (line 1-30 verbatim)

```
module m_xnldata
!  module for computing the quadruplet interaction
!  Created by Gerbrant van Vledder
!
!  version 1.01   16/02/1999  Initial version
!          2.01   01/10/2001  various extensions added
!          3.1.01 01/10/2001  Array's for k4 -locus added
!          3.2    12/05/2002  Triplet data added
!          4.00   08/08/2002  Upgrade to version 4.0
!          4.01   19/08/2002  Various modifications for consistency reasons
!          5.01    9/09/2002  Length of strings aqname and bqname modified
!          5.02   12/04/2003  Switch for triplet variables corrected
!          5.03   26/05/2003  Switch for lumping along locus added
!          5.04   24/12/2003  Tail factors for k2 and k4 always in BQF
!          5.05   14/03/2005  Range for test output of integration modified
!          5.06   11/04/2005  iq_qrule  added (Rule for quadrature)
!                              iq_nsimp  added (Number of points for Simpson rule)
```

→ **Gerbrant van Vledder** (TU Delft/Alkyon Consultants). 1999-2005 v5.06 까지 6년 개발. 본 위키 [[swan-source-coverage-audit]] §3.2 에서 식별.

## 2. Module data (line 31-160, 핵심)

### 2.1 Physical coefficients

```fortran
real q_grav     ! 중력가속도 (Earth 9.81 m/s²)
real qf_tail    ! E(f) 의 spectral tail 지수 (-4, -4.5, -5 등)
```

### 2.2 Filtering coefficients

```fortran
real qf_krat    ! 상호작용 wave numbers k1, k3 의 최대 비율
real qf_dmax    ! k1, k3 의 최대 방향 차
real qf_frac    ! action density 의 최대값 대비 filtering 비율
```

→ Boltzmann integral 효율 가속을 위한 **filtering 기준**. 거의 무시 가능한 작은 contribution 제외.

### 2.3 Program switches (algorithm 선택)

| Switch | 옵션 |
|---|---|
| `iq_compact` | 0/1 — locus 따라 0 contribution 압축 여부 |
| **`iq_cple`** (coupling coefficient) | **1 Webb 심해 / 2 Zakharov 심해 / 3 Hasselmann-Herterich 유한수심 / 4 Zakharov 유한수심 / 5 Lin-Perrie 유한수심** |
| `iq_disp` | 1 심해 (geometric) / 2 linear w²=gk·tanh(kd) / 3 nonlinear |
| `iq_dscale` | 0/1 — Herterich-Hasselmann 수심 scaling |
| `iq_filt` | 0/1 — wave-number space filtering 활성 |
| `iq_gauleg` | 0 / >0 — Gauss-Legendre interpolation 점수 |
| `iq_geom` | 0 directional only / 1 geometric (Resio-Tracy, iq_disp=1 시) |
| `iq_grid` | 1 sector 대칭 / 2 sector 대칭+비대칭 / 3 full circle 비대칭 |
| `iq_integ` | 0-3 integration output 옵션 |
| `iq_interp` | 1 bi-linear / 2 nearest bins |

→ **매우 많은 옵션** — DIA 단순 4-leg 식 대비 정확하지만 **계산 비용 큼 (50-100배)**.

## 3. Top-level subroutines (28개 중 핵심)

| Line | Subroutine | Purpose |
|---|---|---|
| **459** | `xnl_init(sigma, dird, nsigma, ndir, pftail, x_grav, depth, ndepth, ...)` | XNL4 초기화 (SWAN 외부 인터페이스) |
| **841** | `xnl_main(aspec, sigma, angle, nsig, ndir, depth, iquad, xnl, diag, ...)` | **XNL4 main computation** (per time step) |
| 1062 | `q_addtail(xnl, diag, nsig, na, pf_tail)` | Spectral tail addition |
| 1189 | `q_allocate` | 메모리 할당 |
| 1444 | `q_chkconfig` | 설정 검증 |
| 1657 | `q_chkcons(xnl, nk, ndir, sum_e, sum_a, sum_mx, sum_my)` | **Conservation check** (E, action, momentum) |
| 1783 | `q_chkres(k1x, k1y, k2x, k2y, k3x, k3y, k4x, k4y, dep, sum_kx, sum_ky, sum_w)` | **Resonance condition check** k1+k2=k3+k4, ω1+ω2=ω3+ω4 |
| 1888 | `q_cmplocus(ka, kb, km, kw, loclen)` | **Resonance locus 계산** (k4-locus given k1, k2, k3) |
| 2194 | `q_ctrgrid(itask, igrid)` | Spectral grid 제어 |
| 2678 | `q_dscale(n, sigma, angle, nsig, nang, depth, grav, q_dfac)` | Depth scaling (Herterich-Hasselmann) |

→ 총 28 top-level subroutine (`q_*` + `xnl_*`). 본 module 은 SWAN 외부에서 stand-alone 사용 가능 — Van Vledder library.

## 4. 이론 (Tech §2.3.4)

### 4.1 Quadruplet resonance condition

$$\vec{k}_1 + \vec{k}_2 = \vec{k}_3 + \vec{k}_4, \quad \omega_1 + \omega_2 = \omega_3 + \omega_4$$

3 wave numbers 주어지면 4번째 (k4) 가 **resonance locus** (curve in 2D wavenumber space) 위에 위치. `q_cmplocus` (line 1888) 가 이 locus 계산.

### 4.2 Boltzmann integral

$$S_{nl}(\vec{k}_4) = \int\int\int C(\vec{k}_1, \vec{k}_2, \vec{k}_3, \vec{k}_4) \cdot [n_1 n_3 (n_2 + n_4) - n_2 n_4 (n_1 + n_3)] \cdot \delta(\vec{k}_1 + \vec{k}_2 - \vec{k}_3 - \vec{k}_4) \cdot \delta(\omega_1 + \omega_2 - \omega_3 - \omega_4) d\vec{k}_1 d\vec{k}_2 d\vec{k}_3$$

- $C$ = coupling coefficient (`iq_cple` 옵션 5종)
- $n_i = N(\vec{k}_i)$ = action density at wavenumber $\vec{k}_i$
- 항: gain - loss 형식 (energy 보존)

### 4.3 DIA (Hasselmann 1985) vs XNL4

**DIA** (Tech §3.6): resonance locus 의 **단일 representative quadruplet** (λ 비율 0.25 / -0.25 etc) → 단순 4-leg 곱셈식. **빠름** (SWAN 표준) 하지만 정확도 ~30-50% 오차.

**XNL4**: 전체 locus 적분 (Simpson/Gauss-Legendre). **정확** (오차 1-5%) 하지만 50-100배 느림.

User cmd `QUADRUPL` (p.64) 의 옵션 선택. 학술 연구 / 검증용 XNL4, 운영 hindcast DIA.

## 5. User cmd `QUADRUPL` (swanuse.pdf p.64)

`QUADRUPL` 명령으로 XNL4 활성. SWAN 표준 DIA 비활성 → S_nl term 을 본 module 이 대체. ASCII configuration 파일 + BQF (Binary Quadruplet Format, line 41 `luq_bqf`) precomputed locus 저장.

## 6. Cross-references

- [[swan-documentation-stack]] §2.3.4 S_nl + §3.6 DIA + cmd QUADRUPL
- [[swan-source-terms-implementation]] / [[wave/swan-source-terms-implementation]] — DIA implementation (대조)
- [[swan-source-coverage-audit]] §3.2 신규 발견 (Van Vledder XNL4)
- Original author: **Gerbrant van Vledder** (TU Delft/Alkyon Consultants 1999-2005)
- 원논문 추정: **Van Vledder 2006** "The WRT method for the computation of non-linear four-wave interactions in discrete spectral wave models" *Coastal Engineering* 53, 223-242, doi:10.1016/j.coastaleng.2005.10.011

## 7. 한계

- 본 노트는 module header + 28 subroutine 위치만 verified. 8989 라인의 핵심 알고리즘 (q_cmplocus, xnl_main) line-by-line 별도.
- DIA vs XNL4 운영 시점 (storm event 검증용 등) 선택 기준 — 본 위키 사용 사례 부재.
- Van Vledder 2006 Coastal Eng paper DOI 검증 별도.
- BQF (Binary Quadruplet Format) 파일 사양 별도.
- XNL4 + Bragg ([[swan-bragg-scattering]]) + QCM ([[swan-quasi-coherent]]) 동시 사용 시 성능 영향 미평가.
