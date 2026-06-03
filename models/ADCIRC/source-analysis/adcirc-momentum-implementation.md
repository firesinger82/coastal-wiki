---
title: "ADCIRC momentum.F — 2D 운동량 방정식 solver: barotropic+tidal+baroclinic pressure / advection 4 formulation / Coriolis·bottom friction 2×2 implicit / hybrid friction (NOLIBF)"
topic: adcirc
canonical_source: self
citation_status: verified
verification_method: "models/ADCIRC/raw/source_code/adcirc/src/momentum.F (2686) 직접 read — Mom_Eqs_New_NC/New_Conserv/Non_Conserv_pc subroutine + 항 구성(barotropic pressure :385, atm :394, tidal potential :441, baroclinic :473, advection :581-658, wind stress :705-733, VCOEFXX/YY/XY/YX 2×2 implicit :751-772 Coriolis CorifA) + bottom friction TK 식(gwce.F:2479 hybrid) + NOLIBF(timestep.F:129) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — 운동량 방정식 항·formulation·friction verbatim"
verification_date: 2026-06-03
related:
  - models/ADCIRC/source-analysis/adcirc-gwce-implementation.md
  - models/ADCIRC/source-analysis/adcirc-3d-mode.md
  - models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md
---

# ADCIRC momentum.F — 2D 운동량 방정식 solver

> `src/momentum.F`(2686) 직접 read. GWCE([[adcirc-gwce-implementation]])가 **연속방정식→수위(ζ)** 를 풀고, momentum.F 가 **운동량→유속(U,V)** 을 푸는 companion. 매 time step: GWCE 로 ζ 풀고 → momentum 으로 새 유속 `UU2/VV2`. ADCIRC 의 depth-integrated shallow-water 핵심 절반. (3D 는 [[adcirc-3d-mode]] vsmy.F)

## 1. 운동량 방정식 항 (Mom_Eqs_New_NC, line 166-1208)

depth-integrated 2D 운동량(비보존형) RHS 구성:

| 항 | 위치 | 내용 |
|---|---|---|
| **barotropic pressure** | `:385` | `g·∂ζ/∂x` (수위경사). element별 면적 가중(`:452`) |
| **atmospheric pressure** | `:394` | barotropic 에 합산 (역기압 효과) |
| **dynamic water level offset** | `:431` | barotropic 에서 차감 (jgf) |
| **tidal potential** | `:441` | NTIP — earth/body tide + SAL 가 barotropic 에 합산 |
| **baroclinic pressure gradient** | `:473` | 3D ocean model 결합(WJP, `CBaroclinic`) |
| **advection** | `:581-658` | non-lumped elemental, U/V-momentum 별 (4 formulation §2) |
| **wind stress** | `:705-733` | `WSX = DTO2·IFWIND·(WSX1/H1+WSX2/H2)`, `fwind` ramp |
| **absorbing layer** | `:740` | sponge layer 에서 wind 무효화 |
| **Coriolis + bottom friction + lateral** | `:751-772` | 2×2 implicit (§3) |

## 2. Advection 4 formulation (subroutine 분기)

| subroutine | line | formulation |
|---|---|---|
| `Mom_Eqs_New_NC` | 166 | **non-conservative**(기본, = Original) |
| `Mom_Eqs_New_Conserv` | 1230 | conservative C1/C2 |
| `Mom_Eqs_Non_Conserv_pc` | 2005 | non-conservative predictor-corrector |

- 플래그: `CME_Orig`/`CME_New_NC`/`CME_New_C1`/`CME_New_C2`(advection) + `CME_LS_IBPQ/IBPV/IBPSQ/IBPSV`(lateral stress integration-by-parts: flux/velocity/symmetric). `IFNLCT`=비선형 finite-amplitude·advection 토글.
- conservative(C1/C2)는 mass-consistent advection(wetting-drying·강한 비선형에 안정). IBP lateral stress 는 경계 처리 차이.

## 3. Coriolis + bottom friction 2×2 implicit solve (line 751-772) ★

운동량의 Coriolis·friction·lateral 을 **node별 2×2 행렬 implicit**:
```fortran
VCOEFXX = DTO2*(TKM(1,I) + SPNGCOEF_X)        ! x-x: friction + sponge
VCOEFYY = DTO2*(TKM(2,I) + SPNGCOEF_Y)        ! y-y
CorifA  = CORIF(I) + IFNLCT*TANPHI(I)*UU1(I)  ! Coriolis + 구면 metric(tan φ) 비선형
VCOEFXY = DTO2*(TKM(3,I) - CorifA)            ! x-y: lateral - Coriolis
VCOEFYX = DTO2*(TKM(3,I) + CorifA)            ! y-x: lateral + Coriolis
```
- `TKM(1/2/3)` = friction+lateral tensor 성분, `CORIF` = f = 2Ωsinφ, `TANPHI` = 구면좌표 metric(고위도 보정).
- 2×2 [VCOEFXX VCOEFXY; VCOEFYX VCOEFYY] 를 풀어 `(UU2,VV2)` — Coriolis·friction 을 implicit 처리해 안정.

## 4. Bottom friction TK — hybrid (gwce.F:2479, NOLIBF)

```fortran
TK = FRIC·( IFLINBF + (|U|/H)·( IFNLBF + IFHYBF·(1+(HBREAK/H)^FTHETA)^(FGAMMA/FTHETA) ) )
```
- `NOLIBF`(timestep.F:129) → `IFLINBF`(0 선형)/`IFNLBF`(1 quadratic)/`IFHYBF`(2 hybrid) 토글.
- **선형**(NOLIBF=0): `TK=FRIC` (Cf 상수). **quadratic**(1): `TK=FRIC·|U|/H` (= C_d|U|/H). **hybrid**(2): 깊은 물 H≫HBREAK → quadratic, 얕은 물 H<HBREAK → `(HBREAK/H)^FGAMMA` 증가(Manning-like). `FTHETA`/`FGAMMA` 형상, `HBREAK` break depth.
- `FRIC` = bottom friction 계수 (`nodalattr.F` Manning's n 또는 fort.13 공간변화). 3 time level: TK0/TK/TK2 (gwce.F:2477-2482).
- BEDSTR = `H·|U|·TK·ρ` (bed shear N/m², timestep.F:1634).

## 5. GWCE ↔ momentum 결합

- **semi-implicit 순서**: GWCE([[adcirc-gwce-implementation]]) 가 ζ^{n+1} (TK friction 도 GWCE 행렬에 들어감, gwce.F:442) → momentum 이 ζ gradient 로 U,V^{n+1}.
- wetting-drying([[adcirc-wetting-drying-implementation]]): dry node 유속 0, MJU/노드 mask.
- 3D([[adcirc-3d-mode]]): C3D 시 vsmy.F velocity/stress form 으로 연직 분해(여기는 2D depth-integrated).

## 6. 연결

- [[adcirc-gwce-implementation]] — 연속방정식→ζ (companion; friction TK 공유)
- [[adcirc-3d-mode]] — 3D velocity/stress form (vsmy.F), baroclinic
- [[adcirc-wetting-drying-implementation]] — dry node 유속 처리
- tidal potential(NTIP)·SAL — barotropic 에 합산되는 조석 forcing (별도 조석 노트 후보)
- Luettich & Westerink ADCIRC theory (운동량 방정식 정식)
