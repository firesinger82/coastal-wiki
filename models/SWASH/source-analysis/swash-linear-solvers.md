---
title: "SWASH 선형솔버 라이브러리 source-analysis — SwashSolvers.ftn90 (PCG·SIP·BiCGSTAB·Keller-box tridiag·nested-Newton)"
topic: swash-linear-solvers
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 raw source 직접 read: src/SwashSolvers.ftn90(5705줄) — nconct-23 Keller-box band(:133-137)·SIP Stone1968(:1856-1862)·Brugnano-Casulli2009(:5328-5334) file:line 직접 검증. 소스주석 verbatim primary(Eisenstat1981·Stone1968·van der Vorst1992·Bondeli1991·Brugnano-Casulli2009). [[swash-nonhydrostatic-pressure-solver]] §6 TODO(bicgstab/pcg line-by-line·Keller-box tridiag·ILU) 해소."
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
> 비정수압 projection 이 생성하는 **압력-Poisson 계**를 실제로 푸는 엔진. [[swash-nonhydrostatic-pressure-solver]] 가 solver 이름·라인만 4행 표로 나열하고 §6 TODO 로 남긴 gap(bicgstab/pcg 알고리즘·Keller-box tridiag·ILU 구성)을 해소.
> 호출: `SwashImpDep2DHflow.ftn90:3581`(sip) · `SwashImpLayP2DHflow.ftn90:5893/6009`(sip)·`:5925`(bicgstab).

## 0. 솔버 선택 = 계의 차원/대칭성

압력계 구조에 따라 솔버가 갈림 (기존 노트 §4 를 mechanism-level 로 심화):

| 계 | 성질 | 솔버 | primary |
|---|---|---|---|
| depth-averaged 압력 | 대칭 5-대각 | `sip`(기본)·`pcg` | Stone 1968·Eisenstat 1981 |
| layered 비정수압 | 비대칭 `nconct`-band 연직결합 | `bicgstab` | van der Vorst 1992 |
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

## 4. SIP — Stone 강암시 (:1811, 기본 depth-avg)

```
H.L. Stone, SIAM J. Numer. Anal. 5, 530-558, 1968   (:1856-1858)
```
동일 sparsity incomplete LU. **완화 파라미터 `0≤alfa≤1`, 권장 ~0.91 (alfa>0.95 시 발산 가능), alfa=0=표준 ILU** (:1861-1862). 파라미터 결속 (:1937-1939, PCG 와 별도): `reps=pnums(22)`·`maxit=nint(pnums(25))`·`alfa=pnums(27)`. solve 루프 :2064-2232.

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
- **파라미터 카드 2-분리**: PCG/BiCGSTAB=`pnums(21/24/26)`, SIP=`pnums(22/25/27)`. 카드 소스 `SwashReadInput.ftn90:1871`(TOL→pnums(21))·`:1546`(maxit→pnums(25)).
- **single/double 쌍둥이** (`pcg/pcg2`·`tridiag/tridiag2`·`dac/dac2`): 심해 layered 병조건 계는 double precision 압력해 가능.

## 9. 관련
- [[swash-nonhydrostatic-pressure-solver]] — 압력 projection·행렬 조립(amat/rhs) + §6 TODO(본 노트가 해소)
- [[swash-implicit-layered-flow]] — Keller-box gradient 조립(본 노트 tridiag/bicgstab 의 공급원)
- [[delft3d_adi_solver]] — cross-model: Delft3D SIP 계보 (동일 Stone 1968 lineage)
- **Primary (소스 verbatim)**: Eisenstat 1981 · Stone 1968 · van der Vorst 1992 · Bondeli 1991 · Brugnano-Casulli 2009.
