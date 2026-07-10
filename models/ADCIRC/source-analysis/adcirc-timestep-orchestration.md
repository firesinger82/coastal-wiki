---
title: "ADCIRC time-step orchestration (timestep.F TIMESTEP + solveGWCE) — per-step 실행 순서: ramp→friction→radiation stress→BPG→boundary flux→GWCE_New(ζ)→momentum(U,V)→predictor-corrector + BPG2D/SCALAR_TRANS_2D/CALC_SIGMAT"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/timestep.F (TIMESTEP 55-1493, solveGWCE 호출 1069) + gwce.F (solveGWCE 166-226: GWCE_New→UPDATER→Mom_Eqs_New_NC→UPDATER, CPRECOR predictor-corrector) + adcirc.F:476(CALL TIMESTEP) 직접 read. ramp/friction/radiation stress/BPG2D/boundary flux 순서 file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — per-step 실행 순서·predictor-corrector verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
  - models/ADCIRC/source-analysis/adcirc-momentum-implementation.md
  - models/ADCIRC/source-analysis/adcirc-nodal-attributes.md
  - models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md
---

# ADCIRC time-step orchestration (timestep.F / solveGWCE)

> `timestep.F`(TIMESTEP 55-1493) + `gwce.F`(solveGWCE 166-226) 직접 read. ADCIRC 한 time step 의 **실행 순서** — 기존 노트들([[adcirc-gwce-implementation]] continuity, [[adcirc-momentum-implementation]] momentum, [[adcirc-tidal-forcing]], [[adcirc-nodal-attributes]] friction, [[adcirc-baroclinic-coupling]])이 **언제 호출되는지** 묶는 orchestration. main loop `adcirc.F:476 DO ITIME → CALL TIMESTEP(ITIME)`.

## 1. TIMESTEP per-step 순서 (timestep.F)

| 단계 | 내용 | line |
|---|---|---|
| 1 | **temporal ramp** (DRAMP/DRampElev/DRampExtFlux 점진 forcing) | 282-365 |
| 2 | **predictor-corrector 시간레벨 shift** (3TL: ETA0←1←2) | 373+ |
| 3 | **bathymetry update** (NDDT time-varying depth, 점진 ETA2 보정) | 121-196 |
| 4 | **bottom friction** `Apply2DBottomFriction`(→TK) + `Apply2DInternalWaveDrag` + `Apply2DMomentumDisp` / 3D `Apply3DBottomFriction` | 210-226 |
| 5 | **ice** concentration update (NCICE, fort.25) | 248-258 |
| 6 | **wave radiation stress** update `RSGET`/`RS2GET`/`ComputeWaveDrivenForces` | 288-330 |
| 7 | **baroclinic 압력경사** `BPG2D`(C2DDI) / `BPG3D`(C3DVS) | 482-486 |
| 8 | **external boundary flux** `COMPUTE_EXTERNAL_BOUNDARY_FLUX`(→QN2) | 593 |
| 9 | **`CALL solveGWCE`** — GWCE+momentum 해 (§2) | **1069** |
| 10 | 진행률/output 준비 | 1268+ |

- met-only(`METONLY`) 또는 ramp 구간엔 GWCE/momentum skip 분기(jgf48.4627, :438).

## 2. solveGWCE — GWCE↔momentum 결합 순서 (gwce.F:166-226) ★

```fortran
IF(CPRECOR) THEN                       ! predictor-corrector
  CALL GWCE_New(...)                   ! ① 연속 → ETA2^{n+1} (predictor)
  CALL UPDATER(ETA2,...)               !    MPI halo 교환
  CALL Mom_Eqs_New_NC()                ! ② 운동량 → UU2,VV2
  CALL UPDATER(UU2,VV2); UPDATER(QX2,QY2)
  CALL GWCE_New_pc(...)                ! ③ 연속 corrector (갱신 U,V로 재계산)
  CALL UPDATER(ETA2,...)
ELSEIF(CGWCE_New) THEN                  ! 비-PC
  CALL GWCE_New(...)                   ! 연속 → ETA2
  CALL UPDATER(ETA2,...)               ! (momentum 후속)
ENDIF
```
- **순서: 연속(ζ) → 운동량(U,V)** (semi-implicit; GWCE 행렬에 friction TK 포함, [[adcirc-gwce-implementation]] §C JCG solve).
- **predictor-corrector**(`CPRECOR`): ζ predictor → U,V → ζ corrector(갱신 유속 기반) — 비선형 안정·정확도. `LoadEleSlopeLim`(DG slope limiter) 시 추가 UPDATER.
- 각 solve 후 **`UPDATER`** = MPI subdomain halo 교환([[adcirc-parallel-implementation]]).

## 3. TIMESTEP 내부 helper subroutine

| subroutine | line | 역할 |
|---|---|---|
| `SCALAR_TRANS_2D` | 1571 | 2D scalar(염분·온도·passive) transport |
| `CALC_SIGMAT_2D` | 1846 | sigmat 밀도(EOS) — baroclinic |
| `BPG2D` | 1880 | 2D baroclinic pressure gradient(BPGX/BPGY → VIDBCPDXOH, [[adcirc-baroclinic-coupling]]) |
| `BPG3D` | 2040 | 3D baroclinic pressure gradient([[adcirc-3d-mode]]) |

## 4. 전체 한 스텝 데이터 흐름

```
ramp → friction TK(nodalattr Manning→Cd) → radiation stress(wave) → BPG(baroclinic) → boundary flux(QN2)
  → solveGWCE: GWCE_New[연속, tidal potential+atm+BPG 포함] → ETA2 → momentum[U,V] → (corrector)
  → wetting-drying mask → scalar transport → output
```
- forcing 항(tidal potential·wind·atm·radiation stress·baroclinic)은 TIMESTEP 에서 누적되어 GWCE_New/Mom_Eqs 의 RHS 로 들어감.

## 5. 시간 적분 레벨

> ⚠ **정정(L4 후속 2026-07-10)**: 이 절의 이전 서술("3TL IS2TIM=0 leapfrog+trapezoidal / 2TL IS2TIM=1, ISTL, DTDYN, ISDYNSTP")은 **EFDC 파라미터의 혼용 오기**였음 — `rg IS2TIM|ISTL|DTDYN adcirc/src/` 전역 0건(해당 파라미터는 EFDC `aaefdc.f90:3187-3188` dispatch 의 것). 아래가 ADCIRC 실제 구조.

- **GWCE 3-time-level**: 자유표면 상태 `ETA0/ETA1/ETA2`(n−1, n, n+1) — [[adcirc-gwce-implementation]] §B (`gwce.F:2514-2522`).
- **시간 가중**: fort.15 입력 `A00,B00,C00`(read_input.F:2996) — RHS 에 `C00`(n−1)·`(A00+B00)`(n) 가중(`gwce.F:1540-1543`, `A00pB00` 조립 `:1444`). 별도 θ 파라미터 없음(§B "No semi-implicit Theta").
- **predictor-corrector**: `CPRECOR` 플래그(`gwce.F:71,182`) — ζ predictor → U,V → ζ corrector.
- **mass 옵션**: `ILump=0` consistent(JCG solve) / `1` lumped 대각역산(`gwce.F:418-420, 2001-2017`).
- DT/DT2/DTO2 = [[adcirc-momentum-implementation]] §2.2 와 동일 시간계수.

## 6. 연결

- [[adcirc-gwce-implementation]] — GWCE_New(연속 solve, §9 호출)
- [[adcirc-momentum-implementation]] — Mom_Eqs_New_NC(운동량 solve, solveGWCE ②)
- [[adcirc-nodal-attributes]] — Apply2DBottomFriction(friction TK, §1 단계4)
- [[adcirc-baroclinic-coupling]] — BPG2D/VIDBCPDXOH(§1 단계7)
- [[adcirc-tidal-forcing]] — tidal potential(GWCE_New RHS)
- [[adcirc-parallel-implementation]] — UPDATER MPI halo 교환
- adcirc.F:476 main loop → TIMESTEP → SWAN coupling(PADCSWAN_RUN) → output
