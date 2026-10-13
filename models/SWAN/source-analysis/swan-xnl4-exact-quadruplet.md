---
title: "SWAN XNL4 exact quadruplet — mod_xnl4v5.ftn90 (Van Vledder) verified"
topic: swan
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 HEAD 대비 추가·수정 줄의 원문 인용을 현재 소스·과거 커밋·보관 HTML·swantech PDF 39–41쪽과 96쪽·swanuse PDF 72쪽에 대조했다. 결론은 recovery R2·R7 최종본과 git E 판정에 대조했다. 소스 줄 수와 subroutine 선언 수를 다시 셌다." # [10-13 전수 검증 정정]
note_author: "Claude Opus 4.7 (1M context) raw source direct read"
note_date: 2026-06-01
verification_by: "Claude Opus 4.7 (1M context) — header + version 1.01-5.06 history verbatim + switch documentation"
verification_date: 2026-06-01
last_source_check: 2026-10-13 (recovery 대조 반영)
related:
  - models/SWAN/manual-notes/swan-documentation-stack.md
  - models/SWAN/source-analysis/swan-source-coverage-audit.md
  - models/SWAN/source-analysis/swan-source-terms-implementation.md
  - models/SWAN/source-analysis/wave/swan-source-terms-implementation.md
---

## Scope

`mod_xnl4v5.ftn90`은 WRT 방법으로 4파 상호작용 적분을 계산한다. 작성자는 Gerbrant van Vledder다. 근거: `src/mod_xnl4v5.ftn90:4–5`; swantech PDF 39–41쪽 / 인쇄 31–33쪽. 이 파일의 전체 줄 수는 8989개다. 이 파일에서 행 시작의 `subroutine` 선언을 세면 28개다. DIA 구현은 swantech §3.6, PDF 96쪽 / 인쇄 88쪽에서 설명한다. XNL 선택값 51·52·53은 swanuse PDF 72쪽 / 인쇄 64쪽의 `QUADRUPL` 절에 있다. [10-13 전수 검증 정정]

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

소스는 Gerbrant van Vledder를 작성자로 적는다. ALKYON 표지는 `src/mod_xnl4v5.ftn90:463–464`에 있다. 파일 머리의 변경 이력은 1999-02-16의 1.01에서 2005-04-11의 5.06까지 적혀 있다. 근거: `src/mod_xnl4v5.ftn90:5–29`. [10-13 전수 검증 정정]

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
| **`iq_cple`** (coupling coefficient) | 구현된 결합계수는 1=Webb, 2=Herterich–Hasselmann이다. (`src/mod_xnl4v5.ftn90:7940` `case(1)`; `src/mod_xnl4v5.ftn90:7941` `xc_webb`; `src/mod_xnl4v5.ftn90:7946` `case(2)`; `src/mod_xnl4v5.ftn90:7947` `xc_hh`) |
| `iq_disp` | 1 심해 (geometric) / 2 linear w²=gk·tanh(kd) / 3 nonlinear |
| `iq_dscale` | 0/1 — Herterich-Hasselmann 수심 scaling |
| `iq_filt` | 0/1 — wave-number space filtering 활성 |
| `iq_gauleg` | 0 / >0 — Gauss-Legendre interpolation 점수 |
| `iq_geom` | 0 directional only / 1 geometric (Resio-Tracy, iq_disp=1 시) |
| `iq_grid` | 1 sector 대칭 / 2 sector 대칭+비대칭 / 3 full circle 비대칭 |
| `iq_integ` | 0-3 integration output 옵션 |
| `iq_interp` | 1 bi-linear / 2 nearest bins |

범위 검사는 5를 거부한다. (`src/mod_xnl4v5.ftn90:7931` `if (iq_cple < 1 .or. iq_cple > 4) then`)
같은 파일의 구현(7936–7951)·기본값(5696–5712)·출력 문구(6379–6383)는 선언 주석(76–81)의 목록과 서로 다르다. 선언·범위 검사만으로 다른 결합계수를 구현했다고 적지 않는다. 근원인 코드 내부 주석·메시지 불일치 후보는 E·약함으로 기록한다. (`src/mod_xnl4v5.ftn90:7940` `case(1)`; `src/mod_xnl4v5.ftn90:7946` `case(2)`)

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

$$\frac{\partial N_1}{\partial t}=\iiint G(\vec k_1,\vec k_2,\vec k_3,\vec k_4)\,\delta(\vec k_1+\vec k_2-\vec k_3-\vec k_4)\delta(\sigma_1+\sigma_2-\sigma_3-\sigma_4)[N_1N_3(N_4-N_2)+N_2N_4(N_3-N_1)]\,d\vec k_2d\vec k_3d\vec k_4$$ 근거: swantech PDF 39쪽 / 인쇄 31쪽 (2.81). [10-13 전수 검증 정정]

$N_1$의 kernel은 $N_1N_3(N_4-N_2)+N_2N_4(N_3-N_1)$이다. 공명 조건도 문서 (2.80)의 지표 순서를 유지한다. (swantech PDF 39쪽 / 인쇄 31쪽, (2.80)–(2.81); `src/mod_xnl4v5.ftn90:6774` `nprod = qn13p*(qn4-qn2) + qn2*qn4*qn13d`; `src/mod_xnl4v5.ftn90:6734` `qn13p = qn1*qn3`; `src/mod_xnl4v5.ftn90:6735` `qn13d = qn3-qn1`)

- $G$는 식 (2.81)의 결합계수다. 구현된 결합계수는 1=Webb, 2=Herterich–Hasselmann이다. 근거: swantech PDF 39쪽 / 인쇄 31쪽; `src/mod_xnl4v5.ftn90:7940–7947`. [10-13 전수 검증 정정]
- $n_i = N(\vec{k}_i)$ = action density at wavenumber $\vec{k}_i$
- 항: gain - loss 형식 (energy 보존)

### 4.3 DIA (Hasselmann 1985) vs XNL4

전형적인 분할 수·성능·권고 격자를 실행 기본값이라고 쓰지 않는다. 코드 기본 곡선 분할 수는 30이다. (`src/mod_xnl4v5.ftn90:5654` `nlocus0 = 30`)

매뉴얼은 XNL 계산에 보통 DIA의 $10^3$–$10^4$배 계산 노력이 필요하다고 설명한다. 문서는 당시 사용 범위를 작은 공간 격자의 고도로 이상화된 시험으로 제한한다. 문서는 최고 주파수를 예상 첨두주파수의 약 6배로 권장한다. 권장 주파수 수는 약 40개다. 권장 주파수 증가 비율은 1.07이다. 권장 방향 간격은 약 $10^\circ$다. 근거: swantech PDF 41쪽 / 인쇄 33쪽. [10-13 전수 검증 정정]

## 5. User cmd `QUADRUPL` (swanuse.pdf p.64)

`QUADRUPL` 명령으로 XNL4 활성. SWAN 표준 DIA 비활성 → S_nl term 을 본 module 이 대체. ASCII configuration 파일 + BQF (Binary Quadruplet Format, line 41 `luq_bqf`) precomputed locus 저장.

## 6. Cross-references

- [swan-documentation-stack](../manual-notes/swan-documentation-stack.md) §2.3.4 S_nl + §3.6 DIA + cmd QUADRUPL
- [swan-source-terms-implementation](wave/swan-source-terms-implementation.md) / [wave/swan-source-terms-implementation](wave/swan-source-terms-implementation.md) — DIA implementation (대조)
- [swan-source-coverage-audit](swan-source-coverage-audit.md) §3.2 신규 발견 (Van Vledder XNL4)
- Original author: **Gerbrant van Vledder** (TU Delft/Alkyon Consultants 1999-2005)
- 원논문 추정: **Van Vledder 2006** "The WRT method for the computation of non-linear four-wave interactions in discrete spectral wave models" *Coastal Engineering* 53, 223-242, doi:10.1016/j.coastaleng.2005.10.011

## 7. 한계

- XNL 내부에서는 $N(k_x,k_y)=N(\sigma,\theta)c_g/k$를 사용한다. 출력에서는 역 Jacobian을 곱한다. (`src/mod_xnl4v5.ftn90:7545` `nspec(ikq,iaq) = aspec(ikq,iaq)/q_k(ikq)*cg(ikq)`; `src/mod_xnl4v5.ftn90:7730` `jacobian = q_k(ikq)/cg(ikq)`)
- SWAN 호출부는 반환된 source를 조립한다. XNL이 함께 계산한 diagonal을 이 호출부에서 사용하지 않는다. (`src/swancom4.ftn:2987` `SNL(IDIR,ISIG,IGRID) = XNL(ISIG,IDIR)`)
- Van Vledder 2006 Coastal Eng paper DOI 검증 별도.
- BQF (Binary Quadruplet Format) 파일 사양 별도.
- [swan-bragg-scattering](swan-bragg-scattering.md) — Bragg 산란
- [swan-quasi-coherent](swan-quasi-coherent.md) — QCM


## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

대조 보고서: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md) · [R7](../../../_staging/recovery/compare/swan-implementation-history-vs-code.md).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-084 | 4파 상호작용 · swantech PDF 40쪽 / 인쇄 32쪽, (2.84) | swantech PDF 40쪽 / 인쇄 32쪽, (2.84) $\theta=1$ when $\lvert\vec k_1-\vec k_3\rvert\le\lvert\vec k_1-\vec k_4\rvert$; $\theta=0$ when $>$. | `src/mod_xnl4v5.ftn90:6563` `if (dk13 >= dk14) symfac(iloc) = 0.` | C | 코드는 거리의 제곱이 같은 경계도 제거한다. 자기 주석 6555행은 `<`라고 적는다. 해석: 연속 적분에서 측도 0인 경계를 이산 격자에서 제외하는 조건을 문서가 적지 않았다. |
| R2:SS-088 | 4파 상호작용 · swantech PDF 40쪽 / 인쇄 32쪽, (2.88) | swantech PDF 40쪽 / 인쇄 32쪽, (2.88) $\partial_tN(\vec k_1)\approx\sum_{i_{k3}=1}^{n_k}\sum_{i_{\theta3}=1}^{n_\theta}T(\vec k_1,\vec k_3)\Delta k_{i_{k3}}\Delta\theta_{i_{\theta3}}$. | `src/mod_xnl4v5.ftn90:7667` `t13 = 2.*t13`; `src/mod_xnl4v5.ftn90:7677` `xnl(ik1,ia1) = xnl(ik1,ia1) + t13*q_k(ik3)*q_delta*q_dk(ik3)` | B | 식 (2.82)의 2와 극좌표 면적 요소 $d\vec k_3=k_3dk_3d\theta_3$의 $k_3$가 인쇄식에 없다. 코드는 두 인자를 모두 포함한다. 문서는 $T$의 재정의를 제시하지 않는다. |
| R2:SS-089 | 4파 상호작용 · swantech PDF 41쪽 / 인쇄 33쪽, (2.89) | swantech PDF 41쪽 / 인쇄 33쪽, (2.89) $S_{nl4}^{d}=S_{nl4}^{d_N}R(k_pd)/R(k_pd_N)$. | `src/mod_xnl4v5.ftn90:6068` `q_scale = dfac1/dfac2`; `src/mod_xnl4v5.ftn90:7659` `t13 = t13*q_scale`; `src/mod_xnl4v5.ftn90:2738` `N(nsig,nang) Action density`; `src/mod_xnl4v5.ftn90:2796` `compute sums for total energy andwave number`; `src/mod_xnl4v5.ftn90:2803` `dnn = n(isig,iang)*dsigma(isig)*delta`; `src/mod_xnl4v5.ftn90:2813` `kms = (sum0/sumk)**2`; `src/mod_xnl4v5.ftn90:1027` `if(iq_dscale ==1) then`; `src/mod_xnl4v5.ftn90:1028` `call q_dscale(aspec,sigma,angle,nsig,ndir,depth,q_grav,q_dfac)`; `src/mod_xnl4v5.ftn90:5700–5704` 의 `iquad==2`·`iq_dscale=1`; `src/mod_xnl4v5.ftn90:7496` `if(iq_search==0 .or. iq_type/=3) then`; `src/mod_xnl4v5.ftn90:7518` `q_scale = 1.`; `src/mod_xnl4v5.ftn90:7526` 의 `q_searchgrid`; `src/mod_xnl4v5.ftn90:5954` `if(igrid==0) then` 뒤 5962 `goto 9999`. `b2ae30e:src/mod_xnl4v5.ftn90:2803`과 `7ee8981:src/mod_xnl4v5.ftn90:2803`의 `dnn  = n(isig,iang)*dsigma(isig)*delta`가 HEAD `43e9bbb`에도 유지된다. [git 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md). `src/mod_xnl4v5.ftn90:1010`의 `a = aspec`가 최근접 보정에 쓰이는 모듈 배열도 같은 작용 밀도임을 보인다 | E · 강함 | XNL의 `Q_DSCALE`은 에너지 평균 파수를 구한다는 주석과 달리 작용 밀도로 가중한다. 문서 (2.47)의 에너지 가중 평균과 넓은 스펙트럼에서 다르다. 단일 주파수에서는 두 평균이 같다. SWAN 호출부는 `AQUAD(ISIG,IDIR) = ASWAN(IDIR,ISIG,IGRID)`로 작용 밀도를 넘긴다(`src/swancom4.ftn:2960`). XNL WAM 배율 경로와 최근접 수심 격자 보정에 이 평균이 쓰인다. 최근접 검색을 끈 경로는 `q_scale=1`이다. 현재 수심의 격자를 바로 찾는 경로도 최근접 보정을 우회한다. 해당 계산에는 전처리 배제 표시가 없다. 결함 후보의 범위는 이 XNL 경로이며 기본 DIA에는 적용되지 않는다. `git log -G`는 관련 식을 `b2ae30e`(2022-08-10, `initial release`)까지 추적한다. `7ee8981`·patch B `0dabfa4`·HEAD에서 같은 식이 유지된다. 이 날짜는 저장소 최초 반입일이다. [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R2:SS-216 | 4파 상호작용 · swantech PDF 40–41쪽 / 인쇄 32–33쪽, 원문 `typically 40 pieces`, 비용 | swantech PDF 40–41쪽 / 인쇄 32–33쪽, 원문 `typically 40 pieces`, 보통 DIA의 $10^3$–$10^4$배 계산 노력, 최고 주파수 약 첨두의 6배, 약 40개 주파수·비율 1.07·방향 간격 약 $10^\circ$. | `src/mod_xnl4v5.ftn90:5654` `nlocus0 = 30`; `src/mod_xnl4v5.ftn90:5764` 의 `NLOCUS` 입력 | H | 전형적인 분할 수·성능·권고 격자이다. 실행 기본값이라고 쓰지 않는다. 코드 기본 곡선 분할 수는 30이다. [10-13 전수 검증 정정] |
| R2:SS-217 | 4파 상호작용 · swantech PDF 41쪽 / 인쇄 33쪽, 원문 `looking at the 'nearest' water depth dN`. | swantech PDF 41쪽 / 인쇄 33쪽, 원문 `looking at the 'nearest' water depth dN`. | `src/mod_xnl4v5.ftn90:5666` `iq_search = 0`; `src/mod_xnl4v5.ftn90:5798` 의 `SEARCH` 입력; 6065–6068의 수심별 보정 | C | 가장 가까운 BQF를 찾는 기능은 설정으로 활성화한다. 모든 XNL 계산의 기본 동작은 아니다. BQF 검증·재사용 계산은 SS-514이다. |
| R2:SS-514 | XNL의 궤적 적분·보간·필터·꼬리 선택 | swantech PDF 40–41쪽 / 인쇄 32–33쪽은 궤적 분할·스펙트럼 격자·BQF 재사용을 설명한다. | `src/mod_xnl4v5.ftn90:5654` `nlocus0 = 30`; `src/mod_xnl4v5.ftn90:5659` 의 `iq_interp = 1`; `src/mod_xnl4v5.ftn90:5665` 의 `iq_qrule = 1`; `src/mod_xnl4v5.ftn90:5676–5678` 의 `qf_krat`·`qf_dmax`·`qf_frac`; `src/serv_xnl4v5.ftn90:862–866`의 분산 관계 근사; `src/mod_xnl4v5.ftn90:7545,7566,7589`의 작용밀도 변환·최대값·필터 문턱 | C | (2.79)–(2.88)의 연속 적분에 수치 선택을 추가한다. 파수 비의 기본 경계는 2.5다. 방향 차의 기본 경계는 75도다. 밀도 필터의 기본 계수는 `qf_frac = 0.1`이다. 필터 문턱은 `qn_min = qf_frac*qn_max*q_kpow(ik3)`이다. `qn_max = maxval(nspec)`는 파수 공간 작용밀도의 최대값이다. R2의 에너지 밀도 표기를 작용밀도로 정정한다. 적분 간격·분산 관계 근사는 물리식과 별도로 구분한다. C는 이 절에 `nlocus0`·보간·필터 기본값과 분산 관계 근사의 세부가 없는 점이다. BQF 재사용 기능 자체는 문서에 있다. [10-13 결론 검증 보완] [10-13 전수 검증 정정] |
| R2:SS-515 | XNL 입출력 좌표 변환과 도함수 사용 범위 | swantech PDF 39–41쪽 / 인쇄 31–33쪽은 $N(\vec k)$의 정의와 WRT 격자를 설명한다. | `src/mod_xnl4v5.ftn90:7545`의 `nspec(ikq,iaq) = aspec(ikq,iaq)/q_k(ikq)*cg(ikq)`; `src/mod_xnl4v5.ftn90:7730` 의 `jacobian = q_k(ikq)/cg(ikq)`; `src/swancom4.ftn:2960` `AQUAD(ISIG,IDIR) = ASWAN(IDIR,ISIG,IGRID)`; `src/swancom4.ftn:2987` 의 `SNL(IDIR,ISIG,IGRID) = XNL(ISIG,IDIR)` 반환 | C | XNL 내부에서는 $N(k_x,k_y)=N(\sigma,\theta)c_g/k$를 사용한다. 출력에서는 역 Jacobian을 곱한다. SWAN 호출부는 반환된 source를 조립한다. XNL이 함께 계산한 diagonal을 이 호출부에서 사용하지 않는다. 유한 수심 배율의 입력 평균 차이는 SS-089이다. C는 이 절에 호출부의 밀도 변환 대입과 반환된 `DIAG`의 사용 여부가 없는 점이다. [10-13 결론 검증 보완] |
| R2:SS-516 | XNL 최근접 보간의 diagonal 도함수에 3차 항이 남는다 | swantech PDF 40쪽 / 인쇄 32쪽, (2.88) $\partial_tN(\vec k_1)\approx\sum_{i_{k3}=1}^{n_k}\sum_{i_{\theta3}=1}^{n_\theta}T(\vec k_1,\vec k_3)\Delta k_{i_{k3}}\Delta\theta_{i_{\theta3}}$. | `src/mod_xnl4v5.ftn90:6780` `qd1    = qn3*(qn4-qn2) + qn2*qn4*qn3`; `src/mod_xnl4v5.ftn90:6781` `qd3    = qn1*(qn4-qn2) - qn2*qn4*qn1`; `src/mod_xnl4v5.ftn90:6886` `qd1    = qn3*(qn4-qn2) - qn2*qn4`; `src/mod_xnl4v5.ftn90:6887` `qd3    = qn1*(qn4-qn2) + qn2*qn4`. `src/mod_xnl4v5.ftn90:5659` `iq_interp  = 1`; `src/mod_xnl4v5.ftn90:5786` `if(trim(cpar)=='INTERP')   iq_interp  = int(rpar)`; `src/mod_xnl4v5.ftn90:6763` `if(iq_interp==2) then`; `src/mod_xnl4v5.ftn90:6734` `qn13p = qn1*qn3`; `src/mod_xnl4v5.ftn90:6735` `qn13d = qn3-qn1`; `src/mod_xnl4v5.ftn90:6774` `nprod = qn13p*(qn4-qn2) + qn2*qn4*qn13d`. `src/swancom4.ftn:2978–2993`은 `XNL,DIAG`를 받지만 `SNL`에는 `XNL`만 복사한다. `b2ae30e:src/mod_xnl4v5.ftn90:6780`과 `7ee8981:src/mod_xnl4v5.ftn90:6780`의 `qd1    = qn3*(qn4-qn2) + qn2*qn4*qn3`가 HEAD에도 남는다. [git 판정](../../../_staging/recovery/compare/SWAN-git-verify-E.md) | E · 약함 | XNL 최근접 보간의 대각 도함수에는 3차 원천항의 1차 미분에 맞지 않는 3차 항이 남는다. 같은 원천항을 미분한 이중 선형 경로의 6886–6887행은 2차식이다. 기본 `INTERP=1`은 문제 분기를 사용하지 않는다. 설정 파일의 `INTERP=2`는 문제 분기에 도달한다. 해당 계산에는 전처리 배제 표시가 없다. SWAN 호출부는 반환된 `DIAG`를 원천항 갱신에 사용하지 않는다. 따라서 결함 후보의 강도는 약함이다. `git log -G`는 이 식을 `b2ae30e`(2022-08-10, `initial release`)까지 추적한다. `7ee8981`·patch B `0dabfa4`·HEAD `43e9bbb`에서도 식이 유지된다. 저장소 최초 반입일을 오류 발생일로 단정하지 않는다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
| R2:SS-517 | XNL 결합계수 선택과 깊은 물 대체 | swantech PDF 39–41쪽 / 인쇄 31–33쪽의 WRT 설명. | `src/mod_xnl4v5.ftn90:7940`의 `case(1)`; `src/mod_xnl4v5.ftn90:7946` 의 `case(2)`; `src/serv_xnl4v5.ftn90:108` `if(depth*k > 30.) then`. `src/mod_xnl4v5.ftn90:7943`의 주석 `finite depth coupling coefficient of Herterich and Hasselmann` | C | 실제 `x_cple` 선택은 1=Webb와 2=Herterich–Hasselmann 경로이다. 선언 주석·출력 문구의 다른 목록은 SS-720의 코드 내부 불일치 후보로 기록한다. 범위 검사에 허용한 정수와 구현한 `CASE`를 같은 것으로 취급하지 않는다. 군속도 계산은 `if(depth*k > 30.) then`에서 깊은 물 식을 쓴다. C는 swantech PDF 39–41쪽 / 인쇄 31–33쪽에 이 수치 분기와 선택 세부가 없는 점에 한정한다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] |
| R2:SS-720 | 노트 · source-analysis/swan-xnl4-exact-quadruplet.md:77 | `source-analysis/swan-xnl4-exact-quadruplet.md:77` `1 Webb 심해 / 2 Zakharov 심해 / 3 Hasselmann-Herterich 유한수심 / 4 Zakharov 유한수심 / 5 Lin-Perrie 유한수심`. | `src/mod_xnl4v5.ftn90:7940` `case(1)`; `src/mod_xnl4v5.ftn90:7941` `xc_webb`; `src/mod_xnl4v5.ftn90:7946` `case(2)`; `src/mod_xnl4v5.ftn90:7947` `xc_hh`. `src/mod_xnl4v5.ftn90:76–81`의 선언 주석은 1=Webb, 2=Zakharov 심해, 3=Hasselmann & Herterich 유한수심, 4=Zakharov 유한수심, 5=Lin & Perrie이다. 5696·5704·5712의 기본값은 1·1·2이다. 6379–6383의 출력 문구는 1=Webb, 2=Herterich & Hasselmann, 3=Gorman, 4=Zakharov 심해, 5=Zakharov 유한수심이다. 7931의 범위 검사는 `if (iq_cple < 1 .or. iq_cple > 4) then`이다. 7936–7951의 구현은 `case(1)`·`case(2)`이다 | B | 노트는 `src/mod_xnl4v5.ftn90:76–81`의 선언 주석을 옮겼다. 같은 파일의 구현(7936–7951)·기본값(5696–5712)·출력 문구(6379–6383)는 이 목록과 서로 다르다. 구현된 결합계수는 1=Webb, 2=Herterich–Hasselmann이다. 범위 검사는 5를 거부한다. 선언·범위 검사만으로 다른 결합계수를 구현했다고 적지 않는다. 노트 판정은 B로 유지한다. 근원인 코드 내부 주석·메시지 불일치 후보는 E·약함으로 별도 기록한다. 표본 지적의 인용 끝 행은 80에서 81로 바로잡았다. Lin & Perrie 항목이 81행에 있기 때문이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 표본 조정] |
| R2:SS-721 | 노트 · source-analysis/swan-xnl4-exact-quadruplet.md:116 | `source-analysis/swan-xnl4-exact-quadruplet.md:116`의 `[n_1 n_3 (n_2 + n_4) - n_2 n_4 (n_1 + n_3)]`. | `src/mod_xnl4v5.ftn90:6774` `nprod = qn13p*(qn4-qn2) + qn2*qn4*qn13d`. `src/mod_xnl4v5.ftn90:6734` `qn13p = qn1*qn3`; `src/mod_xnl4v5.ftn90:6735` `qn13d = qn3-qn1` | B | 문서와 코드의 지표 정의를 고정한 뒤 $N_1$의 kernel을 $N_1N_3(N_4-N_2)+N_2N_4(N_3-N_1)$로 적는다. 공명 조건도 문서 (2.80)의 지표 순서를 유지한다. [10-13 결론 검증 보완] |
| R2:SS-722 | 노트 · source-analysis/swan-xnl4-exact-quadruplet.md:124 | `source-analysis/swan-xnl4-exact-quadruplet.md:124` `정확도 ~30-50% 오차`; 126 `오차 1-5%`·`50-100배 느림`. | — | H | 코드 판독으로 정확도 백분율이나 실행 시간 배율을 확정하지 않는다. 출처가 없는 수치는 삭제한다. 매뉴얼의 비용 수치를 인용할 때는 권장 격자와 이상화 시험 조건을 함께 적는다. [10-13 결론 검증 정정] |
| R7:H-306 | FD-RIAM | `website/modifications/modifications.htm:306` `An exact method called the FD-RIAM, for the computation of the nonlinear 4-wave interactions in finite-depth water, is implemented. This method is extremely time consuming. Hence, it should not be used for production runs.`; `website/modifications/modifications.htm:561–564`은 40.81에서 RIAM 제거를 기록한다. | `src/swancom4.ftn:2978` `CALL XNL_MAIN( AQUAD,SIGMA,DIRR,NSIG,NDIR,DEPTH(IGRID),IQUAD,`; 이력: `122b595:src/swancom4.ftn:2980` `CALL XNL_MAIN( AQUAD,SIGMA,DIRR,NSIG,NDIR,DEPTH(IGRID),IQUAD,` | D 현재 해당 구현 없음 | 40.31의 FD-RIAM 추가 이력은 40.81의 제거 이력으로 대체되었다. 41.45와 현재 코드의 XNL_MAIN을 FD-RIAM으로 부르지 않는다. `122b595`와 `43e9bbb`의 src에서 `FD.?RIAM` 검색 결과는 각각 0행이다. [10-13 결론 검증 정정] [10-13 결론 검증 보완] [10-13 git 이력 판정] |
