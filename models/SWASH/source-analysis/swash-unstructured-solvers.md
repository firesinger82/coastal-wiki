---
title: "SWASH 비정형 격자 솔버 + Perot 재구성 source-analysis — SwashUServ.ftn90 (pcgu·bicgstabu·newtonU + Perot covolume)"
topic: swash-unstructured-solvers
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 raw source 직접 read: src/SwashUServ.ftn90(2823줄) — Perot 재구성(:140-157)·newtonU Casulli2009 IJNMF60(:2379-2381) file:line 직접 검증. 소스주석 primary van der Vorst1992·van der Ploeg1994·Pommerell1992·Casulli2009. 구조격자 [[swash-linear-solvers]] 의 비정형 쌍둥이 — explicit-depthavg 노트:295 '미검수' 명시 갭 충전."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — SwashUServ.ftn90:138-159·2370-2383 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/SWASH/source-analysis/swash-linear-solvers.md
  - models/SWASH/source-analysis/swash-explicit-depthavg-flow.md
  - models/SWASH/source-analysis/swash-grid-oceanpack-infra.md
---

# SWASH 비정형 격자 솔버 + Perot 재구성 — `SwashUServ.ftn90`

> 소스: [`src/SwashUServ.ftn90`](../raw/source_code/swash/src/SwashUServ.ftn90) (2823줄, Programmer M. Zijlema, header :4-16).
> **정체**: 비정형(unstructured triangular) 격자용 선형솔버 라이브러리 + **Perot 재구성**. 구조격자 [[swash-linear-solvers]](`SwashSolvers.ftn90`)의 **비정형 쌍둥이** — 그 노트는 구조격자만 다뤘고, [[swash-explicit-depthavg-flow]]:295 가 "`bicgstabu` 내부 알고리즘 별도파일 **미검수**"로 남긴 갭을 충전.

## 0. 서브루틴 구조

| 서브루틴 | 라인 | 역할 | 구조격자 대응 |
|---|---|---|---|
| `perot` | :17 | 면법선 성분 → 셀중심 속도벡터 (Perot covolume) | (staggered C-grid 대응) |
| `chkdiv` | :163 | 수평 divergence 연산 (질량보존 진단) | — |
| `pcgu` / `pcgu2` | :299/:636 | PCG single/double (대칭 비정형 압력계) | pcg/pcg2 |
| `iluu` / `iludu` | :973/:1100 | ILU / ILUD-MILUD-RILUD 전처리 | ilu/iludr/iluds |
| `bicgstabu` / `bicgstab3` | :1211/:1707 | BiCGSTAB (비대칭 layered) | bicgstab |
| `newtonU` | :2324 | nested-Newton piecewise-linear (wet/dry·porosity) | newton1D/2D |
| `csrf` | :2586 | Compressed Sparse Row(CSR) 저장 구성 | — |

> 개발 이력(update 스탬프): perot 2017 · pcgu/bicgstabu 2020 · iluu/iludu/newtonU 2023 — 비정형 솔버 branch 는 상대적으로 최근·성장 중.

## 1. Perot 재구성 (`perot`, :17-162) ★어디에도 미커버

삼각격자 면법선 flux `u(iface,k)` → 셀중심 속도벡터 `uvc`. 비정형 FV 의 **C-grid staggering 유사물**로, 위키가 이미 문서화한 모든 "U" flow/output/turbulence 루틴의 기반.
```fortran
! 면 방향(orientation) 부호: 인접셀 outward normal
if( icell == icelll ) rsgn =  1.       ! :141
if( icell == icellr ) rsgn = -1.       ! :143
! Perot covolume 공식:
uvc(icell,k,1) += rsgn*lf*(xf-xc)*u(iface,k)   ! :148  (lf=면길이, (xf-xc)=면중심-셀중심)
uvc(icell,k,2) += rsgn*lf*(yf-yc)*u(iface,k)   ! :149
uvc(icell,:,:) /= area                         ! :157  셀면적 정규화
```
`chkdiv`(:163) = "horizontal divergence operators for checking purposes"(:180) 질량보존 진단.

## 2. PCG 비정형 (`pcgu`, :299) — van der Ploeg 전처리
```
A. van der Ploeg (1994), Preconditioning for sparse matrices with applications, PhD thesis, TU Delft   (:364, :701)
```
`maxit=nint(pnums(24))`(:426), `epslin=reps*rnrm0`(:530), machine-eps floor `ueps=1000*epsmac*rnrm0`(:531-541).

## 3. ILU 전처리 (`iluu`:973 / `iludu`:1100)
```
amod=0 ⇒ ILU, amod=1 ⇒ MILU, RILU=average   (:1140-1142)
A = LU − R, diag(L)=diag(U)=I, offdiag(L,U)=offdiag(A), diag(LU)=diag(A)   (Pommerell 1992, :1143-1148)
```

## 4. BiCGSTAB 비정형 (`bicgstabu`, :1211 / `bicgstab3`, :1707)
```
H.A. van der Vorst, Bi-CGSTAB, SIAM J. Sci. Stat. Comput. 13, 631-644, 1992   (:1260-1262)
```
비대칭 layered 비정수압 압력계. scalar `alpha=rho/sigma`·`beta=alpha/gamma`·omega(:1293+).

## 5. nested-Newton 비정형 (`newtonU`, :2324) — ★인용 divergence 주의
piecewise-linear 계 `max[l, min(u,x)] + Ax = b` (A SPSD, Heaviside p):
```
V. Casulli, A high-resolution wetting and drying algorithm for free-surface hydrodynamics,
IJNMF vol. 60, 391-408, 2009   (:2379-2381)
```
> ⚠ **인용 divergence**: 구조격자 `newton1D/2D`는 **Brugnano-Casulli, SIAM J. Sci. Comput. 31, 1858-1873, 2009** 인용([[swash-linear-solvers]] §7), 비정형 `newtonU`는 **Casulli, IJNMF 60, 391-408, 2009** — 동일 mildly-nonlinear wet/dry+porosity 폐합에 **서로 다른 2009 Casulli 논문 2편**. cross-model 노트서 혼동 금지.

## 6. CSR 저장 (`csrf`, :2586)
`ia`(row starts)·`ja`(columns)·`di`(주대각 위치)·`irw`(row별 열순서)·`nod`(off-diag) (:2620-2650) — 비정형 sparse 행렬 저장.

## 7. 주요 findings
- **구조격자 솔버노트의 비정형 쌍둥이** — `swash-linear-solvers`(2026-07-04, sip/pcg/bicgstab/tridiag/newton1/2D 구조격자)가 남긴 pcgu/bicgstabu/iluu/iludu/newtonU 를 충전. explicit-depthavg:295 "bicgstabu 미검수" 해소.
- **Perot 재구성**(:17)은 비정형 FV 핵심인데 위키 전역 미커버였음 — 모든 "U" 루틴의 속도벡터 기반. **논문 인용은 소스주석에 없음**(canonical ref = J.B. Perot, J. Comput. Phys. 159:58-89, 2000 — uncited-attributable).
- **2편의 2009 Casulli 논문**(구조 Brugnano-Casulli SIAM 31 vs 비정형 Casulli IJNMF 60) — 동일 wet/dry 폐합, 별개 문헌.
- 파라미터 카드 `pnums(24)` 공유(구조 pcg 와 동일 maxit 카드).

## 8. 관련
- [[swash-linear-solvers]] — 구조격자 솔버(SwashSolvers.ftn90, 본 노트의 쌍둥이)
- [[swash-explicit-depthavg-flow]] — 비정형 depth-avg flow(:295 미검수 갭 → 본 노트 충전)
- [[swash-grid-oceanpack-infra]] — 격자 인프라(비정형 cell/face 자료구조)
- **Primary(소스 verbatim)**: van der Vorst 1992 · van der Ploeg 1994 · Pommerell 1992 · Casulli 2009 IJNMF 60. (Perot 2000 = uncited-attributable.)
