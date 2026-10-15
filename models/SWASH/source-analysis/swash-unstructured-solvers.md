---
title: "SWASH 비정형 격자 솔버 + Perot 재구성 source-analysis — SwashUServ.ftn90 (pcgu·bicgstabu·newtonU + Perot covolume)"
topic: swash-unstructured-solvers
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 raw source 직접 read: src/SwashUServ.ftn90(2823줄) — Perot 재구성(:140-157)·newtonU Casulli2009 IJNMF60(:2379-2381) file:line 직접 검증. 소스주석 primary van der Vorst1992·van der Ploeg1994·Pommerell1992·Casulli2009. 구조격자 swash-linear-solvers.md 의 비정형 쌍둥이 — 비정형 솔버와 Perot 재구성의 소스 인용. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
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
> **정체**: 비정형(unstructured triangular) 격자용 선형솔버 라이브러리 + **Perot 재구성**. 구조격자 [swash-linear-solvers](swash-linear-solvers.md)(`SwashSolvers.ftn90`)의 **비정형 쌍둥이**. [10-15 대조 정정]

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

## 1. Perot 재구성 (`perot`, :17-162) [10-15 대조 정정]

삼각격자 면법선 flux `u(iface,k)` → 셀중심 속도벡터 `uvc`. 비정형 FV 의 **C-grid staggering 유사물**(`SwashUServ.ftn90:17-70`)로, `uvc` 는 `src/` 의 **16개 파일**에서 쓰인다(`SwashU*.ftn90` 은 21개).
```fortran
! 면 방향(orientation) 부호: 인접셀 outward normal
if( icell == icelll ) rsgn =  1.       ! :141
if( icell == icellr ) rsgn = -1.       ! :143
```

- `uvc(icell,k,1) = uvc(icell,k,1) + rsgn * lf * ( xf - xc ) * u(iface,k)` (`src/SwashUServ.ftn90:148`) [10-15 대조 정정]
- `uvc(icell,k,2) = uvc(icell,k,2) + rsgn * lf * ( yf - yc ) * u(iface,k)` (`src/SwashUServ.ftn90:149`) [10-15 대조 정정]
- `uvc(icell,:,:) = uvc(icell,:,:) / area` (`src/SwashUServ.ftn90:157`) [10-15 대조 정정]
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
> 구조 격자의 `newton1D/2D`는 Brugnano–Casulli, SIAM J. Sci. Comput. 31, 1858–1873, 2009를 인용한다 (`src/SwashSolvers.ftn90:5332–5334,5540–5542`; [선형 솔버 노트](swash-linear-solvers.md) §7). 비구조 격자의 `newtonU`는 Casulli, IJNMF 60, 391–408, 2009를 인용한다 (`src/SwashUServ.ftn90:2379–2381`). [10-15 전수 검증 정정]

## 6. CSR 저장 (`csrf`, :2586)
`ia`(row starts)·`ja`(columns)·`di`(주대각 위치)·`irw`(row별 열순서)·`nod`(off-diag) (:2620-2650) — 비정형 sparse 행렬 저장.

## 7. 주요 findings
- **구조격자 솔버노트의 비정형 쌍둥이** — `swash-linear-solvers`(2026-07-04, sip/pcg/bicgstab/tridiag/newton1/2D 구조격자)에 대응하는 비정형 `pcgu`·`bicgstabu`·`iluu`·`iludu`·`newtonU`를 정리한다. (`src/SwashUServ.ftn90:299,973,1100,1211,2324`) [10-15 대조 정정]
- **Perot 재구성**은 면법선 성분으로 셀 속도벡터를 재구성한다 (`src/SwashUServ.ftn90:56,148–157`). `src/`에서 식별자 `uvc`를 포함하는 파일은 선언·할당·사용을 합쳐 16개이다. 기술매뉴얼의 관련 서지는 B. Perot, “Conservation properties of unstructured staggered mesh schemes”, J. Comput. Phys. 159:58–89, 2000이다 (swashtech PDF p.124, 참고문헌 [72]). [10-15 전수 검증 보완]
- **2편의 2009 Casulli 논문**(구조 Brugnano-Casulli SIAM 31 vs 비정형 Casulli IJNMF 60) — 동일 wet/dry 폐합, 별개 문헌.
- 파라미터 카드 `pnums(24)` 공유(구조 pcg 와 동일 maxit 카드).

## 8. 관련
- [swash-linear-solvers](swash-linear-solvers.md) — 구조격자 솔버(SwashSolvers.ftn90, 본 노트의 쌍둥이) [10-15 대조 정정]
- [swash-explicit-depthavg-flow](swash-explicit-depthavg-flow.md) — 비정형 depth-avg flow [10-15 대조 정정]
- [swash-grid-oceanpack-infra](swash-grid-oceanpack-infra.md) — 격자 인프라(비정형 cell/face 자료구조) [10-15 대조 정정]
- 소스 주석의 문헌은 van der Vorst 1992, van der Ploeg 1994, Pommerell 1992, Casulli 2009이다 (`src/SwashUServ.ftn90:1260–1262,364–366,1143,2379–2381`). Perot 2000의 서지는 swashtech PDF p.124의 참고문헌 [72]에 있다. [10-15 전수 검증 보완]

## 문서와 코드 차이 (10-15 대조)

행 ID의 약칭은 [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)를 가리킨다.
문서 인용은 PDF 쪽 번호를 쓴다.
swashuse의 인쇄 쪽 번호는 PDF 쪽 번호에서 8을 뺀다.

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227` 2026-05-06 "release v12.01"에서 마지막 변경. 코드 판: VERNUM 12.01, 공개 저장소 main `a486d5f` 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| theory-unstructured:ST2-053 | (5.25) 직교 재구성 | swashtech PDF p.79: `\mathbf u_c=\frac1{A_c}\sum_{f\in\partial c}S_f\Delta s_{fc}u_f\mathbf n_f`; `\mathbf r_{fc}=\Delta s_{fc}\mathbf n_{c,f}`; | `src/SwashUServ.ftn90:148` `uvc(icell,k,1) = uvc(icell,k,1) + rsgn * lf * ( xf - xc ) * u(iface,k)`; :157 `uvc(icell,:,:) = uvc(icell,:,:) / area` | F 표기 차이 | 해석: `s_{c,f}\mathbf r_{fc}=\Delta s_{fc}\mathbf n_f`를 (5.24)에 대입하면 (5.25)를 얻는다. 코드는 (5.24)를 사용하므로 중심 대체 셀에서도 벡터식 자체를 유지한다. |
| theory-unstructured:ST2-211 | 제9장 수치 접근 본문 | swashtech PDF p.111: `This chapter is under preparation.`;<br>swashuse PDF p.92의 비구조 ILU-BiCGSTAB 설명; p.99–101의 PCG·Newton 설명(ST2-225) | `src/SwashUServ.ftn90:2363` `!   Solves a piecewise linear system by means of the Newton-type iteration method`; :2515 `call pcgu2 ( amata, rhsa, sol1 )`; | C 문서 누락 | 해석: C는 준비 중인 swashtech 제9장 p.111의 수치 접근 본문 누락에 한정한다. 해법의 종류와 옵션은 swashuse p.92·99–101에 있다. 코드의 Newton 반복 안에서는 `pcgu2`를 호출한다. 두 매뉴얼 전체에 해법 설명이 없다는 판정이 아니다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-399 | Newton 기본 선택·마름 체적 | swashuse PDF p.99–101은 Newton 방법과 비구조 격자의 기본 선택을 설명한다.<br>swashtech PDF p.111에는 본문이 없다.; | `src/SwashInit.ftn90:463` `inewt     = -1`;<br>`src/SwashCheckPrep.ftn90:618–626` `if ( inewt < 0 ) then`, `if ( optg /= 5 ) then`, `inewt = 0`, `else`, `inewt = 1`, `endif`, `endif`, `!`, `if ( inewt /= 0 .and. mtimei /= 2 ) inewt = 0`;<br>`src/SwashImpDepUflow.ftn90:1233` `call newtonU ( amatn, rhsn, ds )`;<br>`src/SwashUServ.ftn90:2492–2504` `if ( s < -h + epsdry ) then`, `!`, `! water level drops below bottom level`, `!`, `v = a * epsdry`, `p = 0d0`, `!`, `else`, `!`, `! volume cell is non-negative`, `!`, `v = a * h`, `p = a`; :2508–2515 `amata(icell,0) = amat(icell,0) + p`, `rhsa (icell  ) = rhs (icell  ) - v`, `!`, `enddo`, `!`, `! solve system of equations by means of preconditioned CG method`, `!`, `call pcgu2 ( amata, rhsa, sol1 )` | C 문서 누락 | 비구조 반음해의 자동 `inewt=1`은 사용설명서와 일치한다. Newton에서 수위 보정 s와 현재 수심 h가 `if ( s < -h + epsdry ) then`을 만족하면 `v = a * epsdry`, `p = 0d0`를 사용한다. 이 조건은 epsdry를 포함하므로 단순히 바닥 아래라고 축약하지 않는다. 내부 선형계는 배정도 PCG로 푼다. C는 이 체적·도함수의 수치 처리에 한정한다. [SWASH-git-verify-AD.md §3의 후속 변경 무관 목록](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)에 포함된다. 문서 마지막 변경은 `7949227 2026-05-06 release v12.01`이다. 뒤의 `608ffd7`·`9554c98`은 이 행의 조건·식을 바꾸지 않았다. 판 차이 A의 근거가 아니다. [10-15 결론 검증 정정] [10-15 git 이력 판정] |
| theory-unstructured:ST2-405 | 비구조 선형계의 CSR·전처리·문턱 | swashuse PDF p.91–93·100–101은 압력·수위 해법과 전처리·오차 매개변수를 설명한다.<br>swashtech PDF p.111·115–116에는 비구조 CSR 저장과 카드 대응이 없다.; | `src/SwashUServ.ftn90:1321–1323` `reps(1) = pnums(22)`, `reps(2) = pnums(23)`, `maxit   = nint(pnums(25))`; :1333–1335 `k = irw(icell,jc)`, `!`, `if ( k /= 0 ) ax2(ip+jc-1) = amat(icell,k-1)`; :1345 `if ( icond == 2 ) then`; :1349 `call iludu`; :1351 `else if ( icond == 3 ) then`; :1355 `call iluu`;<br>`src/SwashCheckPrep.ftn90:643` `if ( optg == 5 ) icond = 3`;<br>`src/SwashUServ.ftn90:762–763`의 내부 PCG는 `reps  = dble(pnums(21))`, `maxit = nint(pnums(24))`를 읽는다. `src/SwashUServ.ftn90:2444–2445` `reps  = dble(pnums(21))`, `maxit = nint(pnums(24))`; :2463–2464 `epslin = reps*rnrm0`, `ueps   = 1d3*epsmac*rnrm0`; :2560 `if ( .not. rnorm > epslin ) exit iterloop` | C 문서 누락 | 비구조 수심 평균 압력의 BiCGSTAB는 CSR로 계수를 옮긴다. 자동 전처리 선택은 ILU(0)이다. Newton과 내부 수위 PCG는 압력 BiCGSTAB와 다른 오차·반복수 카드를 사용한다. C는 CSR 저장과 내부 카드 대응에 한정한다. BiCGSTAB를 PCG 카드와 혼동한 노트 오기는 ST2-430이다. 반복 상한 기본값의 별도 차이는 ST2-403이다. [10-15 결론 검증 보완] [10-15 전수 검증 보완] |
