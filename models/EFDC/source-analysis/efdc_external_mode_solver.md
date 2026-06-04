---
title: "EFDC 외부모드 solver(congrad.f90/congradc.f90) — 수위(P) 5-point 방정식을 Jacobi-preconditioned Conjugate Gradient로 해. 외부(2D depth-integrated) mode"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/congrad.f90 (225) + congradc.f90 (231) 직접 read — CONGRAD 외부모드 CG(11), 5-point stencil CCC/CCN/CCS/CCW/CCE(70/109), residual RCG·Jacobi precond CCCI(74)·search PCG·ALPHA/BETA(87+)·OMP file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — CG 외부모드 solver verbatim"
verification_date: 2026-06-04
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_dispersion.md
---

# EFDC 외부모드 solver (congrad / congradc)

> `congrad.f90`(225) + `congradc.f90`(231) 직접 read. EFDC 의 **external mode(2D depth-integrated 수위) 방정식**을 **Conjugate Gradient(CG)** 로 해. [[efdc_hydro_core]] 의 external-internal mode split 에서 external mode(자유표면 중력파)를 implicit 하게 푸는 핵심 solver. ADCIRC GWCE JCG([[adcirc-itpack-solver]])·XBeach SIP 와 같은 역할.

## 1. 외부모드 5-point 방정식 (congrad.f90:70)

수위 `P`(=자유표면 압력/elevation)의 이산 방정식 — 곡선격자 cell L 의 5-point stencil:
```fortran
CCC(L)·P(L) + CCN·P(LN) + CCS·P(LS) + CCW·P(LW) + CCE·P(LE) = FPTMP(L)
```
- `CCC`(center 대각) + `CCN/CCS/CCW/CCE`(북/남/서/동 이웃) = external mode 행렬계수(continuity + barotropic 운동량 결합, [[efdc_hydro_core]]). `FPTMP` = RHS(forcing).
- symmetric → CG 적합.

## 2. Jacobi-preconditioned CG (congrad.f90) ★

```fortran
RCG(L) = FPTMP − (CCC·P + CCN·P_N + CCS·P_S + CCW·P_W + CCE·P_E)    ! residual r
PCG(L) = RCG(L)·CCCI(L)                                              ! z = M⁻¹r (Jacobi precond, CCCI=1/CCC)
RPCG = Σ RCG·PCG                                                     ! r·z
[iter]: APCG = A·PCG(5-point matvec) → ALPHA=RPCG/Σ(PCG·APCG)
        P += ALPHA·PCG ; RCG −= ALPHA·APCG ; BETA=RPCGN/RPCG ; PCG = z + BETA·PCG
        RSQ < tol 까지
```
- **Jacobi(대각) 전처리** `CCCI = 1/CCC` — 간단·빠름(EFDC 격자 대각우세). CG 표준 recurrence(ALPHA step + BETA conjugate direction).
- **OMP 병렬**: matvec(APCG)·내적이 OpenMP `$OMP` 분할(NOPTIMAL/LDMOPT 도메인). 수렴 `RSQ/RSQ0 < RSQM`.
- `congradc.f90` = 변형(complex/특수 경계 또는 다른 전처리 버전).

## 3. external-internal mode split 내 위치

- EFDC 는 **mode splitting**([[efdc_hydro_core]]): external(2D 빠른 중력파, 작은 dt 또는 implicit) + internal(3D shear, 큰 dt). CONGRAD 가 external mode 수위를 **semi-implicit** 하게 → 중력파 CFL 제약 완화(큰 dt 가능).
- 매 time step external mode 호출. 수렴 반복수가 hydro 비용의 큰 부분(대규모 격자).

## 4. 비교

| 모델 | 외부모드/수위 solver |
|---|---|
| **EFDC** | CONGRAD — Jacobi-precond CG(5-point) |
| ADCIRC | ITPACK JCG([[adcirc-itpack-solver]]) |
| XBeach nonh | SIP(Stone)([[xbeach_solver]]) |
| D-Flow FM | Guus(Nested Newton)([[delft3d_dflowfm_kernel_scheme]]) |

→ 모두 elliptic 수위/압력 계의 반복解(EFDC=대칭 CG).

## 5. 연결

- [[efdc_hydro_core]] — external-internal mode split(CONGRAD 가 external mode 해)
- [[efdc_dispersion]] — HMD 가 들어가는 운동량(external mode 계수 CCC 등에 반영)
- [[adcirc-itpack-solver]] / [[xbeach_solver]] — 타 모델 수위/압력 solver 대비
