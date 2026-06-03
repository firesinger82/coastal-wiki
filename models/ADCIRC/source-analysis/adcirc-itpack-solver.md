---
title: "ADCIRC GWCE 선형solver — ITPACKV 2D JCG(Jacobi Conjugate Gradient): 대칭 SPD 계 COEF·ETAS=GWCE_LV, Jacobi 전처리 + CG 가속 + 고유값 adaptive(cme/sme zbrent) + pstop 수렴(RPARM(1)=CONVCR)"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/itpackv.F (2942) 직접 read — jcg(63 driver) + itjcg(459 1-iteration) + pjac(1932 Jacobi precond) + pmult(1970 matvec) + parcon/chgcon(1774/893 가속 param) + pstop(721 수렴) + zbrent/eqrt1s(2521/1402 고유값) + dfault(1071). gwce.F:2003 CALL JCG + IPARM/RPARM(145-151) 인터페이스 file:line 인용. 원본 ITPACKV 2D(1990-01) = Kincaid·Grimes·Respess, UT Austin Center for Numerical Analysis(:41-43); ADCIRC에 MODULE ITPACKV로 편입(vjp 1999)·MPI 적응·LGPL."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — JCG 알고리즘·전처리·adaptive·인터페이스 verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
  - models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md
  - models/ADCIRC/source-analysis/adcirc-parallel-implementation.md
---

# ADCIRC GWCE 선형 solver — ITPACKV JCG

> `src/itpackv.F`(2942) 직접 read. [[adcirc-gwce-implementation]] §C 가 인터페이스(ITMAX/CONVCR/NUMITR)를 다뤘고, 본 노트는 **solver 내부 알고리즘**. GWCE 의 consistent-mass(`ILump=0`) 대칭 SPD 행렬을 **ITPACKV 2D 의 JCG(Jacobi Conjugate Gradient)** 로 해. **`itpackv.F` 출처**(헤더 정확): 원본 ITPACKV 2D 코드(1990-01)는 **David Kincaid·Roger Grimes·John Respess, University of Texas Center for Numerical Analysis** 작성(:41-43). 외부 링크 라이브러리가 아니라 **ADCIRC 소스트리에 `MODULE ITPACKV` 로 편입**(vjp 1999)되어 ADCIRC LGPL 저작권을 달고 **MPI 적응(`USE MESSENGER`)·컴파일러 수정**(vjp/jjw)을 받음. = 외부 기원(ITPACK) + ADCIRC 편입·적응.

## 1. 호출 인터페이스 (gwce.F:2003)

```fortran
CALL JCG(NP, MNP, MNEI, NEITAB, COEF, GWCE_LV, ETAS, IWKSP, NW, WKSP, IPARM, RPARM, IER)
NUMITR = IPARM(1)        ! 반복 횟수 반환
```
- 푸는 계: `COEF · ETAS = GWCE_LV` (ETAS = ζ 증분, GWCE_LV = GWCE RHS load vector).
- **희소 저장**: `COEF(MNP, MNEI)` + `NEITAB`(neighbor table) = ITPACKV 2D jagged-diagonal(ELLPACK 류) — 각 node 행의 비영 원소를 최대이웃수 MNEI 열로, 열 index 는 이웃 table. FEM unstructured 격자에 적합.
- **IPARM(12)/RPARM(12)** (DFAULT :1071 기본): `IPARM(1)=ITMAX`(in: 상한, out: NUMITR), `RPARM(1)=CONVCR`(stopping ζ/zeta). 작업공간 `NW = 4·NP + 4·ITMAX`.
- **lumped mass**(`ILump=1`)는 JCG 우회 → 대각 explicit 역산(gwce.F:2010, [[adcirc-gwce-implementation]] §C).

## 2. JCG 알고리즘 (jcg :63 / itjcg :459)

**Jacobi Conjugate Gradient** = Jacobi(대각) splitting 으로 전처리한 CG. ITPACKV 알고리즘 family(jcg/jsi/sor/ssorcg/ssorsi/rscg/rssi) 중 ADCIRC 는 **jcg** 만 PUBLIC(:56).

`itjcg`(한 iteration) 핵심 루틴:
- **`pjac`** (:1932) — Jacobi 전처리: 대각 D⁻¹ splitting (`M = D`, 정규화).
- **`pmult`** (:1970) — 희소 matrix-vector 곱 `COEF·v`(NEITAB 기반).
- **acceleration parameters** `gamma`·`rho` (CG 계수) — `parcon`(:1774) 계산, `chgcon`(:893) adaptive 갱신.
- 새 해 `u1 = ρ(γ·(D⁻¹b − D⁻¹A·u) + u) + (1−ρ)·u0` 형식(2-term CG recurrence).

## 3. Adaptive 고유값 추정 (itcom3 common)

Chebyshev/CG 가속 parameter 를 위해 행렬 spectrum 추정:
- **`cme`/`sme`** = 최대/최소 고유값 추정 (largest/smallest eigenvalue of Jacobi iteration matrix).
- `zbrent`(:2521 Brent 근찾기) + `eqrt1s`(:1402 대칭 삼중대각 고유값) → tri-diagonal(CG 가 생성하는 Lanczos T) 의 고유값 → `cme` 갱신.
- switch: `adapt`(완전 adaptive)/`betadt`/`caseii`/`partad`(부분 adaptive). `ff` = damping factor, `sige`/`specr` = spectral radius.
- → 사용자가 고유값을 몰라도 반복 중 자동 추정해 최적 가속(ITPACK 의 핵심 특징).

## 4. 수렴 판정 (pstop :721)

- `pstop`/`pstop_nrms`(:809) — stopping test: 상대 잔차/해 norm `‖δu‖/‖u‖ < zeta`(=RPARM(1)=CONVCR). `halt`/`stptst` switch.
- 미수렴 시 `IER` 에러코드(ITMAX 초과 등). NUMITR 가 PRINT 로 모니터 → 발산 진단.

## 5. 보조 (전처리·정렬·scaling)

- **`scal`/`unscal`** (:2281/:2424) — 대칭 scaling(diagonal normalization)으로 conditioning 개선.
- **`prbndx`** (:2007) — red-black(b/w) reordering (SSOR/RS 계열용; JCG 엔 미사용이나 라이브러리 포함).
- **`sbelm`** (:2225) — tol 이하 작은 원소 제거.
- `permat`/`pervec`/`peror`(:1855/:1907/:607) — 행렬/벡터 permutation.

## 6. 위치·한계

- GWCE 가 SPD 대칭(consistent mass + tau0 primitive weighting)이라 **JCG 가 적합**(대칭계 CG 수렴 보장). 비대칭이면 발산 가능.
- **MPI**: 각 subdomain 이 자기 JCG 를 풀고, `pmult` 의 matvec 에 halo 교환 필요([[adcirc-parallel-implementation]] UPDATER) — 도메인 분할이 수렴/반복수에 영향.
- ITPACK 알고리즘 코어는 안정(외부 기원·검증된 라이브러리)이나 ADCIRC 편입 시 MODULE화·MPI·컴파일러 수정을 받음(v41.09 이후 코어 안정). 실무 튜닝은 IPARM/RPARM(ITMAX/CONVCR)만.

## 7. 연결

- [[adcirc-gwce-implementation]] §C — solver 인터페이스(IPARM/RPARM, lumped 우회), 본 노트가 그 내부
- [[adcirc-timestep-orchestration]] — solveGWCE → GWCE_New 내부에서 JCG 호출
- [[adcirc-parallel-implementation]] — pmult matvec 의 MPI halo
- ITPACKV 2D (1990-01): David Kincaid, Roger Grimes, John Respess — UT Austin Center for Numerical Analysis. Jacobi/SOR/SSOR/CG adaptive iterative solver. (D.M. Young 의 ITPACK 계보; 본 파일 attribution 은 Kincaid/Grimes/Respess)
