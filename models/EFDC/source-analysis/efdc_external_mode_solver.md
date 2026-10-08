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
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC 외부모드 solver (congrad / congradc)

> 외부 모드의 해법 호출은 프로세스 수와 MDCHH에 따라 CONGRAD·CONGRADC·Congrad_MPI로 나뉜다. (`calpuv2c.f90:660` — `if( MDCHH == 0 ) Call Congrad_MPI   ! *** MSCHH> = 1 not parallelized yet @todo`; `calpuv2c.f90:662` — `if( MDCHH == 0 ) CALL CONGRAD`; `calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`)

## 1. 외부모드 5-point 방정식 (congrad.f90:70)

외부 압력 상태 P는 G*(HP+BELV)이다. (`calpuv2c.f90:975` — `P(L) = G*(HP(L) + BELV(L))`)
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
- CONGRAD는 RSQ<=RSQM이면 종료한다. (`congrad.f90:143` — `RSQ   = RSQ   + RCG(L)*RCG(L)`; `congrad.f90:171` — `if( RSQ <= RSQM )then`)
- 단일 프로세스는 MDCHH>=1에서 CONGRADC를 호출한다. (`calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`; `calpuv9c.f90:706` — `if( MDCHH >= 1 ) CALL CONGRADC`; `congradc.f90:69` — `if( MDCHH >= 1 )then`) CONGRADC는 하부격자 수로 결합 경로이다. (`calpuv2c.f90:663` — `if( MDCHH >= 1 ) CALL CONGRADC`; `calpuv9c.f90:706` — `if( MDCHH >= 1 ) CALL CONGRADC`)

## 3. external-internal mode split 내 위치

- 외부 모드와 내부 모드는 같은 물리 단계에서 순차 호출한다. (`hdmt2t.f90:627` — `call CALPUV2C`; `hdmt2t.f90:650` — `call CALUVW`; `hdmt.f90:690` — `call CALPUV9C`; `hdmt.f90:772` — `call CALUVW`)
- 3TL 보정은 같은 시각에서 계산 구간을 다시 수행한다. (`hdmt.f90:1342` — `GOTO 500`; `calpuv2c.f90:1002` — `GOTO 1000`) 습윤건조 상태 변경은 외부 해법을 다시 수행할 수 있다. (`hdmt.f90:1342` — `GOTO 500`; `calpuv2c.f90:1002` — `GOTO 1000`) 해법 비용 비중은 확인하지 않음. (`hdmt.f90:1342` — `GOTO 500`; `calpuv2c.f90:1002` — `GOTO 1000`)

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
