---
title: "SWASH 선형솔버 라이브러리 source-analysis — SwashSolvers.ftn90 (PCG·SIP·BiCGSTAB·Keller-box tridiag·nested-Newton)"
topic: swash-linear-solvers
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 raw source 직접 read: src/SwashSolvers.ftn90(5705줄) — nconct-23 Keller-box band(:133-137)·SIP Stone1968(:1856-1862)·Brugnano-Casulli2009(:5328-5334) file:line 직접 검증. 소스주석 verbatim primary(Eisenstat1981·Stone1968·van der Vorst1992·Bondeli1991·Brugnano-Casulli2009). swash-nonhydrostatic-pressure-solver.md의 BiCGSTAB·PCG·Keller-box tridiag·ILU 설명을 보완. 2026-10-15 SWASH recovery 대조 보고서 반영"
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — SwashSolvers.ftn90:130-141·1854-1865·5324-5337 직접 read 검증"
verification_date: 2026-07-04
related:
  - models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md
  - models/SWASH/source-analysis/swash-implicit-layered-flow.md
  - models/Delft3D/source-analysis/delft3d_adi_solver.md
---

# SWASH 선형솔버 라이브러리 source-analysis — `SwashSolvers.ftn90`

> 소스: [`src/SwashSolvers.ftn90`](../raw/source_code/swash/src/SwashSolvers.ftn90) (5705줄, header 목록 :4-23). SWASH v12.01.
> 압력계·수위계의 격자별 솔버 구분은 §0에 정리했다. [10-15 대조 정정]
> 호출: `SwashImpDep2DHflow.ftn90:3581`(sip) · `SwashImpLayP2DHflow.ftn90:5893/6009`(sip)·`:5925`(bicgstab).

## 0. 솔버 선택 = 계의 차원/대칭성

압력계·수위계와 격자에 따라 솔버가 갈린다 ([theory-unstructured:ST2-225 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]

| 계 | 성질 | 솔버 | primary |
|---|---|---|---|
| 구조 2DH 수심평균 압력 | 대칭 5-대각 | `sip` | Stone 1968; `src/SwashExpDep2DHflow.ftn90:4092` [10-15 대조 정정] |
| 구조 1DH 수심평균 압력 | 삼중대각 | `tridiag` | `src/SwashExpDep1DHflow.ftn90:1265` [10-15 대조 정정] |
| 구조 다층 비정수압 | 비대칭 `nconct`-band 연직결합 | `bicgstab` | van der Vorst 1992; `src/SwashExpLay1DHflow.ftn90:2443` [10-15 대조 정정] |
| 비구조 수심평균 압력 | — | `bicgstabu` | `src/SwashExpDepUflow.ftn90:1440` [10-15 대조 정정] |
| 비구조 다층 압력 | — | `bicgstab3` | `src/SwashExpLayUflow.ftn90:2450` [10-15 대조 정정] |
| 비구조 수위 | — | `pcgu`·`newtonU` | `src/SwashImpDepUflow.ftn90:1140,1233` [10-15 대조 정정] |
| Keller-box 연직 | tri-diagonal | `tridiag`·`dac` | Thomas·Bondeli 1991 |
| piecewise-linear 자유수면/porosity | mildly-nonlinear | `newton1D/2D` | Brugnano-Casulli 2009 |

**Keller-box band 증거** (:133-137):
```fortran
! note: nconct-23 is equivalent with kmax-1 and 2 for Keller-box and standard pressure gradient approximations, respectively  (:133)
do j = 0, nconct-23
   vo(nm,k) = vo(nm,k) + amat(nm,k,ishif(j))*vi(nm,min(k+j,qmax))   ! :137 연직결합 band
enddo
```
→ Keller-box 는 연직 band 폭 `kmax-1`, 표준 압력구배는 2. 압력행렬 `amat(nm,k,ishif(j))` 의 `nconct` band 가 solver 선택을 결정.

## 1. Matrix-vector product (:25-609)

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `avm` | :25 | 무전처리 `vo = A·vi` (최대 25-band + 연직 nconct) |
| `ave` | :190 | **Eisenstat trick** 전처리 mat-vec (추가연산 반감) |
| `avmp` | :454 | 전처리 mat-vec, layered 변형 |
| `ivl`/`ivu` | :610/:732 | ILU 인자 전진(하)/후진(상) 삼각치환 |

Eisenstat trick 인용 (:237-239): **S.C. Eisenstat, SIAM J. Sci. Stat. Comput. 2, 1-4, 1981** — 전처리 CG 의 추가작업 반감.

## 2. ILU 전처리 3-종 (:2258-3311)

`ilu`(:2258, right)·`iludr`(:2694, ILUD-row)·`iluds`(:3050, ILUD-split). 규칙 (:989-1008): `A = LU − R`, `diag(L)=diag(U)=I`, off-diag = A, `diag(LU)=diag(A)`. **MILUD** 변형 = `rowsum(LU)=rowsum(A)`. **RILUD** = 스칼라 `amod` 가중평균 (0=ILUD·1=MILUD, :1004-1008).

## 3. PCG — 대칭 depth-averaged (:937 single / :1374 double)

Preconditioned Conjugate Gradient. 종료기준 (:1055-1058 주석): `‖b − Ax_j‖ < reps·‖b − Ax_0‖`.
```fortran
epslin = reps*rnrm0                         ! :1215  (machine eps ueps 로 floor :1215-1226)
alpha  = rho/a                              ! :1266
rnorm  = sqrt(rho)                          ! :1333
if( .not. rnorm > epslin ) exit             ! :1339
beta   = rho/rhold                          ! :1341
```
파라미터 결속 (:1076-1078): `reps=pnums(21)`·`maxit=nint(pnums(24))`·`amod=pnums(26)`.

구조 격자 PCG의 초기 기준은 전처리 잔차 내적이다 (`src/SwashSolvers.ftn90:1207` `rho = rho + resd(nm)*z(nm)`; `src/SwashSolvers.ftn90:1213` `rnrm0 = sqrt(rho)`; [inputs-physics-numerics:SI2-279](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론)). [10-15 대조 정정]

## 4. SIP — Stone 강암시 (:1811, 기본 depth-avg)

```
H.L. Stone, SIAM J. Numer. Anal. 5, 530-558, 1968   (:1856-1858)
```
동일 sparsity incomplete LU. **완화 파라미터 `0≤alfa≤1`, 권장 ~0.91 (alfa>0.95 시 발산 가능), alfa=0=표준 ILU** (:1861-1862). 파라미터 결속 (:1937-1939, PCG 와 별도): `reps=pnums(22)`·`maxit=nint(pnums(25))`·`alfa=pnums(27)`. solve 루프 :2064-2232.

압력 `SOLVER`를 생략하면 반복 상한은 500이다 (`src/SwashInit.ftn90:458` `pnums(25) = 500.`). [10-15 대조 정정]
`SOLVER`를 쓰고 `MAXITER`를 생략하면 상한은 100이다 (`src/SwashReadInput.ftn90:1543–1546` `call ININTG('MAXITER'  , itmp1    , 'STA', 100 )`, `pnums(25) = real(itmp1)`). [10-15 대조 정정]
문서의 단일 기본값 500과 다른 이 입력 경로는 E·중간이다 (`swashuse PDF p.93`(인쇄 p.85) `Default: [maxiter] = 500`; [theory-unstructured:ST2-403](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]

## 5. BiCGSTAB — 비대칭 layered (:3312)

```
H.A. van der Vorst, Bi-CGSTAB, SIAM J. Sci. Stat. Comput. 13, 631-644, 1992   (:3329-3331)
```
layered 비정수압 압력계(비대칭·nconct-band)용. split vs right 전처리 옵션 + Eisenstat (:3324-3336). scalar `alpha`·`beta`·`omega` (:3413+).

## 6. Keller-box 연직 tridiag (:4297 tridiag / :4517 tridiag2) + DAC (:4737)

`tridiag` = Thomas double-sweep (연직 Keller-box tri-diagonal). `dac`(:4737) = **Bondeli 분할정복 병렬 tridiag**:
```
S. Bondeli, Parallel Computing 17, 419-434, 1991   (:4783-4785)
```
"highly parallelizable, double sweep 대비 ~2× 연산" (:4785 주석). interface 계 `alpha(2*NPROC-2)`·교환 `arrc(8,NPROC)`.

## 7. Nested-Newton — piecewise-linear 자유수면/porosity (:5283 1D / :5491 2D) ★신규

기존 어떤 노트에도 없던 솔버. Casulli mildly-nonlinear 계:
```
max[l, min(u,x)] + Ax = b    (A SPD, l/u/b known)   (:5328)
L. Brugnano & V. Casulli, SIAM J. Sci. Comput. 31, 1858-1873, 2009   (:5332-5334)
```
- `newton1D`(:5283) tri-diagonal / `newton2D`(:5491) penta-diagonal(2DH 자유수면·subgrid porosity).
- 하드코딩 수렴 (:5363-5364): `maxit=100`·`reps=1.d-14`, outer/inner 반복 + 대각행렬 `q0` 리셋.
- **연결점**: wetting-drying·vegetation/porosity 계와 직결(max/min clip = wet/dry·porous 제약) — 기존 노트들과 미연결이던 novel piece.

## 8. 실무 노트
- 구조 PCG의 `reps`·`maxit`·`amod`는 `pnums(21)`·`pnums(24)`·`pnums(26)`을 읽는다 (`src/SwashSolvers.ftn90:1076–1078`). [10-15 대조 정정]
- SIP의 `reps`·`maxit`·`alfa`는 `pnums(22)`·`pnums(25)`·`pnums(27)`을 읽는다 (`src/SwashSolvers.ftn90:1937–1939`). [10-15 대조 정정]
- 구조·비구조 BiCGSTAB의 오차·반복 상한은 `pnums(22)`·`pnums(23)`·`pnums(25)`를 읽는다 (`src/SwashSolvers.ftn90:3449–3451`; `src/SwashUServ.ftn90:1321–1323`; [theory-unstructured:ST2-430](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#4-노트-대조와-수정안)). [10-15 대조 정정]
- **single/double 쌍둥이** (`pcg/pcg2`·`tridiag/tridiag2`·`dac/dac2`): 심해 layered 병조건 계는 double precision 압력해 가능.

## 9. 관련
- [비정수압 압력 솔버](swash-nonhydrostatic-pressure-solver.md) — 압력 projection·행렬 조립(amat/rhs). [10-15 대조 정정]
- [암시적 다층 유동](swash-implicit-layered-flow.md) — Keller-box gradient 조립(본 노트 tridiag/bicgstab 의 공급원). [10-15 대조 정정]
- [Delft3D ADI 솔버](../../Delft3D/source-analysis/delft3d_adi_solver.md) — cross-model: Delft3D SIP 계보 (동일 Stone 1968 lineage). [10-15 대조 정정]
- **Primary (소스 verbatim)**: Eisenstat 1981 · Stone 1968 · van der Vorst 1992 · Bondeli 1991 · Brugnano-Casulli 2009.

## 문서와 코드 차이 (10-15 대조)

대조 근거: [guide-syntax-build](../../../_staging/recovery/compare/swash-guide-syntax-build-vs-code.md#5-차이-결론), [inputs-physics-numerics](../../../_staging/recovery/compare/swash-inputs-physics-numerics-vs-code.md#5-차이-결론), [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md#5-차이-결론).
문서 쪽은 PDF 쪽이다.
인쇄 쪽은 PDF 쪽에서 8을 뺀 값이다.

문서 판은 SWASH 12.01 매뉴얼 swashuse·swashtech다(공개 저장소 `7949227`, 2026-05-06, "release v12.01"에서 마지막 변경). 코드 판은 `VERNUM 12.01`이다(공개 저장소 main `a486d5f`, 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| guide-syntax-build:SG1-112 | PREConditioner 선택지 | `swashuse PDF p.137`(인쇄 p.129): `Two options are available: ILU and ILUD.`.`NONHYDrostatic ... PREConditioner ILUD\|ILU`.<br>`swashuse PDF p.160`(인쇄 p.152)과<br>`misc/swash.edt:215`는 `PREConditioner  ILUDS\|ILUD\|ILU\|NONE`을 싣는다. | `src/SwashReadInput.ftn90:1553–1561` `if ( KEYWIS('ILUDS') ) then` / `icond = 1` / `else if ( KEYWIS('ILUD') ) then` / `icond = 2` / `else if ( KEYWIS('ILU') ) then` / `icond = 3` / `else if ( KEYWIS('NONE') ) then` / `icond = 3` / `pnums(28) = -1.` | C 문서 누락 | 코드는 ILUDS·ILUD·ILU·NONE을 읽는다. `swashuse PDF p.160`(인쇄 p.152)의 부록 도식과 swash.edt는 네 선택지를 모두 적는다. C는 ILU·ILUD만 설명한 `swashuse PDF p.137`(인쇄 p.129)의 본문으로 한정한다. 같은 PRECOND 선택지를 다룬 SG1-911과 참조 범위를 구분한다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| guide-syntax-build:SG1-896 | solver 허용오차·weight 기본값 | `swashuse PDF p.100`(인쇄 p.92)은 TOL=0.01와 Newton TOL=0.001을 설명한다. p.91·93·101은 주요 solver 가중치 기본값을 설명한다. | `src/SwashCheckPrep.ftn90:1307–1334` `if ( pnums(21) < 0. ) then` / `if ( inewt == 0 ) then` / `pnums(21) = 0.01` / `else` / `pnums(21) = 0.001` / `endif` / `endif` / `if ( pnums(22) < 0. ) then` / `call msgerr (1, 'incorrect termination criterion for the SIP or BiCGSTAB solver')` / `pnums(22) = 0.01` / `endif` / `if ( pnums(23) < 0. ) then` / `call msgerr (1, 'incorrect termination criterion for the BiCGSTAB method')` / `pnums(23) = 0.` / `endif` / `!` / `! check and set weight factors / relaxation parameter for linear solvers` / `!` / `if ( pnums(26) > 1. ) then` / `call msgerr (1, 'incorrect weight factor for the CG method')` / `pnums(26) = -1.` / `endif` / `if ( pnums(26) < 0. ) then` / `if ( optg /= 5 ) then` / `pnums(26) = 0.9` / `else` / `pnums(26) = 0.` / `endif`<br>`src/SwashCheckPrep.ftn90:1340–1362` `if ( pnums(27) < 0. ) then` / `if ( optg == 5 ) then` / `pnums(27) = 0.` / `else if ( kmax == 1 .or. ihydro == 3 ) then` / `pnums(27) = 0.91` / `else if ( qmax == 1 ) then` / `pnums(27) = 0.93` / `else` / `if ( ihydro == 1 ) then` / `if ( icond == 1 ) then` / `pnums(27) = 0.` / `else if ( icond == 2 ) then` / `pnums(27) = 0.99` / `else if ( icond == 3 ) then` / `pnums(27) = 0.55` / `endif` / `else if ( ihydro == 2 ) then` / `if ( icond == 3 .and. ifloat /= 0 ) then` / `pnums(27) = 0.` / `else` / `pnums(27) = 0.9` / `endif` / `endif` | C 문서 누락 | Newton별 TOL 기본값과 주요 weight·relax 기본값은 문서에 있다. C는 음수 허용오차·잘못된 weight를 되돌리는 검사 및 문서에 없는 세부 기본 선택 조건에 한정한다. 예를 들어 비정형·1층·ihydro=3 분기 뒤의 `qmax == 1`이면 `relax=0.93`이다. STANDARD·ILU·부체 조합에서는 `relax=0`이다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| inputs-physics-numerics:SI2-189 | SOLVER·기본 solver 선택 | `swashuse PDF p.91–92`(인쇄 p.83–84): “SIP ... depth-averaged”; “BiCGSTAB ... multi-layered”; “For unstructured meshes, the ILU-BiCGSTAB solver is chosen instead.” | `src/SwashExpDep2DHflow.ftn90:4092`: `call sip( amat, rhs, dq )`<br>`src/SwashExpLay1DHflow.ftn90:2443`: `call bicgstab ( amatp(1:mcgrd,1:qmax,1:nconct), rhsp(1:mcgrd,1:qmax), dq(1:mcgrd,1:qmax) )`<br>`src/SwashExpLayUflow.ftn90:2450`: `call bicgstab3 ( amatp(1:ncells,1:qmax,0:nconct), rhsp(1:ncells,1:qmax), dq(1:ncells,1:qmax) )`<br>`src/SwashExpDep1DHflow.ftn90:1265`: `call tridiag ( a, b, c, d, dq, kgrpnt )` | C 문서 누락 | 인용한 명시적 구조 격자 2DH 수심평균 비정수압 Poisson 식은 SIP로 푼다. 명시적 1DH 수심평균은 tridiag로 푼다. 다층 1DH는 BiCGSTAB로 푼다. C는 `swashuse PDF p.91–92`(인쇄 p.83–84)의 수심평균 solver 설명에서 1DH 직접해법 예외가 빠진 것으로 한정한다. SI2-289와 같은 구분이다. [10-15 결론 검증 정정] |
| inputs-physics-numerics:SI2-190 | 잔차 종료식·두 허용오차 합 | `swashuse PDF p.92`(인쇄 p.84): `\Vert r_m\Vert _2/\Vert b\Vert _2<\epsilon`; `\Vert r_m\Vert _2/\Vert r_0\Vert _2<\epsilon`; “If both these accuracies are given, the sum of the two is used as termination criterion.” | `src/SwashSolvers.ftn90:3689`: `epslin = reps(1)*bnorm + reps(2)*rnrm0`; `src/SwashSolvers.ftn90:3704` `10    if ( rnorm > epslin .and. j < maxit ) then` | F 표기 차이 | 문서 p.92는 우변·초기 잔차에 대한 두 상대 허용오차와 두 기준의 합을 설명한다. 코드의 가중합은 이 정규화와 양립한다. 문서의 엄격한 부등호와 달리 코드는 등호에서도 종료한다. 이 경계 표기 차이를 F로 분류한다. 별도의 기계 정밀도 하한은 SI2-211이다. `8756667:src/SwashSolvers.ftn90:3689,3704`부터 가중합과 종료 조건은 같다. AD의 판 차이 없음은 유지한다. 두 기준의 합을 명시한 p.92 원문을 반영하여 AD의 B 결론은 F로 바로잡는다. [10-15 결론 검증 정정] [10-15 git 이력 판정] |
| inputs-physics-numerics:SI2-207 | NONHYDROSTATIC 본문의 PRECFQ·ILUDS·NONE 설명 누락 | `swashuse PDF p.89`(인쇄 p.81) 도식의 SOLVER에는 `[precfq]`가 없다. PRECONDITIONER 도식은 `ILUD\|ILU`이다.<br>`swashuse PDF p.160`(인쇄 p.152)은 `[precfq]`와 `ILUDS\|ILUD\|ILU\|NONE`을 표시한다. | `src/SwashReadInput.ftn90:1545`: `call ININTG('PRECFQ'   , itmp2    , 'STA', 1   )`; `src/SwashReadInput.ftn90:1547` `pnums(28) = real(itmp2)`; `src/SwashReadInput.ftn90:1553–1554` `if ( KEYWIS('ILUDS') ) then` / `icond = 1`; `src/SwashReadInput.ftn90:1559–1561` `else if ( KEYWIS('NONE') ) then` / `icond = 3` / `pnums(28) = -1.` | C 문서 누락 | 코드는 전처리 갱신 빈도를 받으며 기본값은 1이다. ILUDS는 분할 전처리이다. NONE은 갱신 빈도 -1을 설정한다. C는 p.89–93 본문의 의미·기본값·활성 조건 설명 누락으로 한정한다. 이름은 p.160 부록에 있다. 실제 갱신 조건은 SI2-286이다. [10-15 결론 검증 정정] |
| inputs-physics-numerics:SI2-211 | 수렴 기준 안전 하한·배율 | `swashuse PDF p.92–93`(인쇄 p.84–85)에는 다음 안전 하한과 수위 규모 배율이 없다. | `src/SwashSolvers.ftn90:3690`: `ueps   = 1000.*real(epsmac)*bnorm`; `src/SwashSolvers.ftn90:3692` `if ( epslin < ueps .and. rnorm > 0. ) then`; `src/SwashSolvers.ftn90:3700` `epslin = ueps`<br>`src/SwashImpLay1DHflow.ftn90:1445–1447`: `s0mx   = maxval(abs(s0))` / `reps   = pnums(58)` / `epslin = max(reps,reps*s0mx)` | C 문서 누락 | BiCGSTAB가 기계 정밀도 규모의 하한으로 허용오차를 올린다. projection 수위 반복은 수위 규모를 이용한다. 선형 압력 잔차의 기준과 수위 재반복의 기준은 서로 다르다. |
| inputs-physics-numerics:SI2-279 | 1DH 수위 직접 solver·PCG norm | `swashuse PDF p.99–100`(인쇄 p.91–92)은 PCG를 일반 수위 solver로 설명한다. 1DH의 직접 solver 예외와 전처리 norm 식은 적지 않는다. | `src/SwashImpDep1DHflow.ftn90:954`: `call tridiag ( a, b, c, d, ds, kgrpnt )`<br>`src/SwashSolvers.ftn90:1207`: `rho = rho + resd(nm)*z(nm)`; `src/SwashSolvers.ftn90:1213` `rnrm0 = sqrt(rho)` | C 문서 누락 | Newton을 끈 1DH 수위식은 tridiag로 푼다. 구조격자 PCG의 초기 기준은 전처리 잔차 내적이다. 이를 비전처리 2-norm이라고 한정하지 않는다. |
| theory-unstructured:ST2-219 | (11.2) SIP 분해 | `swashtech PDF p.115`(인쇄 p.107): `M=LU=A+K` | `src/SwashSolvers.ftn90:1997–2009` `p1 = alfa*cmat(nmd,2)`, `p2 = alfa*cmat(ndm,1)`, `!`, `cmat(nm,4) = amat(nm,2)/(1.+p1)`, `cmat(nm,5) = amat(nm,4)/(1.+p2)`, `!`, `p1 = p1*cmat(nm,4)`, `p2 = p2*cmat(nm,5)`, `p3 = amat(nm,1) + p1 + p2 - cmat(nm,4)*cmat(nmd,1) - cmat(nm,5)*cmat(ndm,2) + small`, `!`, `cmat(nm,3) = 1./p3`, `cmat(nm,1) = (amat(nm,3)-p2)*cmat(nm,3)`, `cmat(nm,2) = (amat(nm,5)-p1)*cmat(nm,3)` | F 표기 차이 | 해석: 코드는 두 삼각 인수를 `cmat`의 다섯 계수로 저장한다. `K=LU-A`를 별도 배열로 저장하지 않아도 같은 분해 정의다. |
| theory-unstructured:ST2-222 | (11.3) 반복식 | `swashtech PDF p.116`(인쇄 p.108): `U\vec N^{s+1}=L^{-1}K\vec N^s+L^{-1}\vec b` | `src/SwashSolvers.ftn90:2092` `resd(nm) = rhs(nm) - amat(nm,1)*x(nm) - amat(nm,2)*x(nmd) - amat(nm,3)*x(nmu) - amat(nm,4)*x(ndm) - amat(nm,5)*x(num)`; `src/SwashSolvers.ftn90:2210` `x   (nm) = x   (nm) + resd(nm)`<br>`src/SwashSolvers.ftn90:2157` `resd(nm) = cmat(nm,3) * (resd(nm) - cmat(nm,4)*resd(nmd) - cmat(nm,5)*resd(ndm))`; `src/SwashSolvers.ftn90:2209` `resd(nm) = resd(nm) - cmat(nm,1)*resd(nmu) - cmat(nm,2)*resd(num)` | F 표기 차이 | 해석: 코드의 잔차 보정은 `x^{s+1}=x^s+(LU)^{-1}(b-Ax^s)`다. `LU=A+K`를 대입하고 `U`를 곱하면 원문 (11.3)을 얻는다. 양의 `K` 부호는 맞다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-224 | 수렴까지 반복·정지 조건 | `swashtech PDF p.116`(인쇄 p.108): `repeated s = 0, 1, 2, ... until convergence is reached.`<br>`swashuse PDF p.92`(인쇄 p.84)의 우변·초기 잔차 2-노름 설명; p.93: `[rhsaccur] relative accuracy with respect to the right-hand side.`, `[maxiter] maximum number of iterations.` | `src/SwashSolvers.ftn90:1937–1938` `reps  = pnums(22)`, `maxit = nint(pnums(25))`; `src/SwashSolvers.ftn90:2047` `epslin = reps*bnorm`<br>`src/SwashSolvers.ftn90:2064` `do j = 1, maxit`; `src/SwashSolvers.ftn90:2232` `if ( .not. rnorm > epslin ) exit`; `src/SwashSolvers.ftn90:2241` `if ( rnorm > epslin .and. iamout > 0 .and. INODE == MASTER ) then` | C 문서 누락 | 해석: SIP는 우변 2-노름 기준의 허용오차와 최대 반복수를 사용한다. `swashuse PDF p.92–93`(인쇄 p.84–85)은 정확도·최대 반복수와 기본값을 설명한다. C는 swashtech 제11장 p.116에 없는 구체적 종료 기준과 미수렴 출력 조건으로 한정한다. 두 매뉴얼 전체의 수렴 설정 누락이 아니다. [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-228 | SIP 인용과 참고문헌의 연결 | `swashtech PDF p.115`(인쇄 p.107): `Stone, 1968; Ferziger and Perić, 1999`; p.119–128 참고문헌 [1]–[118] | `src/SwashSolvers.ftn90:1856–1858` `!   H.L. Stone`, `!   Iterative solution of implicit approximations of multidimensional partial differential equations`, `!   SIAM J. of Numer. Anal., vol. 5, 530-558, 1968` | C 문서 누락 | 해석: 대상 참고문헌에는 두 저자·연도 인용의 서지 항목이 없다. 코드 주석은 Stone 논문의 완전한 서지를 제공한다. Ferziger–Perić의 본문 식·계수를 필요로 하는 판정은 이번 범위에 없다. |
| theory-unstructured:ST2-403 | SIP 계수·오차 문턱·최대 반복수 | `swashuse PDF p.92–93`(인쇄 p.84–85)은 SIP·ILU의 완화계수와 오차 문턱을 설명한다. p.93: `Default: [maxiter] = 500`.<br>`swashtech PDF p.115–116`(인쇄 p.107–108)에는 수치 기본값이 없다. | `src/SwashInit.ftn90:455–458` `pnums(22) = 0.01`, `pnums(23) = 0.`, `pnums(24) = 100.`, `pnums(25) = 500.`<br>`src/SwashCheckPrep.ftn90:1340–1344` `if ( pnums(27) < 0. ) then`, `if ( optg == 5 ) then`, `pnums(27) = 0.`, `else if ( kmax == 1 .or. ihydro == 3 ) then`, `pnums(27) = 0.91`<br>`src/SwashSolvers.ftn90:1937–1939` `reps  = pnums(22)`, `maxit = nint(pnums(25))`, `alfa  = pnums(27)`<br>`src/SwashReadInput.ftn90:1540–1546`의 `if ( KEYWIS('SOLV') ) then` 안에서 `call ININTG('MAXITER'  , itmp1    , 'STA', 100 )`으로 읽고 `pnums(25) = real(itmp1)`을 대입한다.<br>`src/SwashExpDep2DHflow.ftn90:4092`는 SIP를 호출한다.<br>`src/SwashSolvers.ftn90:1938`은 `pnums(25)`를 반복 상한으로 읽는다. 비구조 BiCGSTAB도<br>`src/SwashUServ.ftn90:1323`에서 같은 카드를 읽는다. 이 입력·소비 경로에는 비활성 전처리 접두어가 없다. | E 코드 결함 후보 | 구조 격자 수심 평균 SIP의 자동 `alfa=0.91`과 상대 문턱 0.01은 문서와 일치한다. 비구조 자동 `pnums(27)=0`도 문서에 있다. 압력 SOLVER를 생략하면 반복 상한은 500이다. SOLVER를 쓰고 MAXITER를 생략하면 상한은 100이다. 문서의 단일 기본값 500과 다른 이 입력 경로는 E 중간이다. 명시적으로 MAXITER를 주면 그 값이 적용된다. [SWASH-git-verify-E2.md §2 SI2-194](../../../_staging/recovery/compare/SWASH-git-verify-E2.md)와 같은 카드 차이다. `8756667 2022-09-03 initial release`의 `8756667:src/SwashInit.ftn90:417`은 500을, `8756667:src/SwashReadInput.ftn90:1194`는 100을 사용한다. `7949227 2026-05-06 release v12.01`의 파서 `7949227:src/SwashReadInput.ftn90:1543`에도 100이 있다. `608ffd7`·`9554c98`은 이를 고치지 않았다. AD §3의 후속 변경 무관 판정은 유지하되, 입력 경로를 보탠 결론은 C에서 E 중간으로 고친다. [10-15 결론 검증 정정] [10-15 git 이력 판정] |
| theory-unstructured:ST2-404 | SIP 작은 분모 보정·정밀도 하한·실패 출력 | `swashuse PDF p.92–93`(인쇄 p.84–85)은 수렴 오차·반복 상한을 설명한다.<br>`swashtech PDF p.115–116`(인쇄 p.107–108) 및 사용설명서의 해당 설명에는 아래 작은 분모 보정·정밀도 하한·실패 출력 조건이 없다. | `src/SwashSolvers.ftn90:1885–1886` `double precision, parameter :: epsmac = 1d-18   ! machine precision number`, `real            , parameter :: small  = 1.e-15  ! a small number`; `src/SwashSolvers.ftn90:2005` `p3 = amat(nm,1) + p1 + p2 - cmat(nm,4)*cmat(nmd,1) - cmat(nm,5)*cmat(ndm,2) + small`; `src/SwashSolvers.ftn90:2047–2048` `epslin = reps*bnorm`, `ueps   = 1000.*real(epsmac)*bnorm`; `src/SwashSolvers.ftn90:2058` `epslin = ueps`; `src/SwashSolvers.ftn90:2241–2243` `if ( rnorm > epslin .and. iamout > 0 .and. INODE == MASTER ) then`, `!`, `write (PRINTF, '(a)') ' ++ sip: no convergence for solving system of equations'` | C 문서 누락 | 분해 분모에는 `10^{-15}`를 더한다. 요구 오차가 코드의 정밀도 하한보다 작으면 하한으로 올린다. 반복 한도 도달의 메시지는 `iamout>0`인 마스터에서만 출력한다. 이 블록은 실패 시 자동 재풀이를 하지 않는다. 반복 상한의 입력 경로 차이는 ST2-403과 같다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-424 | 전역 노름 합산 | `swashuse PDF p.92–93`(인쇄 p.84–85)은 수렴 노름을 설명한다. p.144는 MPI 통신을 설명한다.<br>`swashtech PDF p.116–117`(인쇄 p.108–109)에는 아래 전역 합산 호출이 없다. | `src/SwashSolvers.ftn90:2044` `call SWREDUCE ( bnorm, 1, SWREAL, SWSUM )`; `src/SwashSolvers.ftn90:2223` `call SWREDUCE ( rnorm, 1, SWREAL, SWSUM )`<br>`src/swanparll.ftn:2007–2008` `!MPI      CALL MPI_ALLREDUCE ( ARR, TEMP, ILEN, SWREAL,`<br>`!MPI     &                     ITYPRD, MPI_COMM_WORLD, IERR )` | C 문서 누락 | SIP 노름은 프로세스별 제곱 합을 전역 합산한 뒤 제곱근을 취한다. MPI_ALLREDUCE는 MPI 스위치에서만 활성화된다. [10-15 결론 검증 보완] |
| theory-unstructured:ST2-430 | BiCGSTAB의 오차·반복수 카드 | models/SWASH/source-analysis/swash-linear-solvers.md:104 ``- **파라미터 카드 2-분리**: PCG/BiCGSTAB=`pnums(21/24/26)`, SIP=`pnums(22/25/27)`.`` | `src/SwashSolvers.ftn90:3449–3451` `reps(1) = pnums(22)`, `reps(2) = pnums(23)`, `maxit   = nint(pnums(25))`<br>`src/SwashUServ.ftn90:1321–1323` `reps(1) = pnums(22)`, `reps(2) = pnums(23)`, `maxit   = nint(pnums(25))`<br>`src/SwashSolvers.ftn90:1076–1078` `reps  = pnums(21)`, `maxit = nint(pnums(24))`, `amod  = pnums(26)`; `src/SwashSolvers.ftn90:1937–1939`의 SIP 카드 대입. | B 문서 오기 | 구조 PCG의 reps·maxit·amod는 `pnums(21)`·`pnums(24)`·`pnums(26)`을 읽는다. SIP의 reps·maxit·alfa는 `pnums(22)`·`pnums(25)`·`pnums(27)`을 읽는다. 구조·비구조 BiCGSTAB의 오차·반복 상한은 `pnums(22)`·`pnums(23)`·`pnums(25)`를 읽는다. Newton의 내부 카드 대응은 ST2-405와 같다. [SWASH-git-verify-AD.md §3 ST2-430](../../../_staging/recovery/compare/SWASH-git-verify-AD.md). `8756667 2022-09-03 initial release`의 `8756667:src/SwashSolvers.ftn90:3449–3451`부터 BiCGSTAB는 `pnums(22)`·`pnums(23)`·`pnums(25)`를 읽는다. `7949227`과 main에도 같다. PCG 카드에서 바뀐 과거 판의 문제가 아니므로 B를 유지한다. [10-15 결론 검증 정정] [10-15 git 이력 판정] |
