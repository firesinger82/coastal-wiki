---
title: "ADCIRC momentum.F — 2D 운동량 방정식 solver: barotropic+tidal+baroclinic pressure / advection 4 formulation / Coriolis·bottom friction 2×2 implicit / hybrid friction (NOLIBF)"
topic: adcirc
canonical_source: self
citation_status: verified
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
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
VCOEFXY = DTO2*(TKM(3,I) - CorifA)            ! x-y: 항력 교차 성분과 코리올리
VCOEFYX = DTO2*(TKM(3,I) + CorifA)            ! y-x: 항력 교차 성분과 코리올리
```
- `LoadIT_Fric`이 참이고 외부 경압 결합 조건이 거짓이며 속성 값 개수가 3인 분기는 `TKM`에 저면 마찰과 내부파 항력을 합한다 (`src/nodalattr.F:2762` `TKM(1,I) = TK(I) + IT_Fric(I,1)`; `src/nodalattr.F:2763` `TKM(2,I) = TK(I) + IT_Fric(I,2)`; `src/nodalattr.F:2764` `TKM(3,I) = IT_Fric(I,3)`; `src/nodalattr.F:2619` `LoadITFric: IF (LoadIT_Fric) THEN`; `src/nodalattr.F:2656` `Baroc: IF (CBaroclinic.and.abs(IDEN).ge.5) THEN`; `src/nodalattr.F:2755` `ELSE`; `src/nodalattr.F:2757` `IF (IT_FricNoOfVals == 3) THEN`). [10-12 전수 검증 보완] 내부파 항력이 없는 경로는 대각 성분에 `TK`를 대입하고 교차 성분을 0으로 둔다 (`src/nodalattr.F:2777` `TKM(1,:) = TK`; `src/nodalattr.F:2778` `TKM(2,:) = TK`; `src/nodalattr.F:2779` `TKM(3,:) = 0.0d0`). 운동량 분산 보정 루틴은 `IF (NOLIBF.NE.3.OR.HBREAK.LE.0d0) RETURN`에서 반환한다 (`src/nodalattr.F:2818` `IF (NOLIBF.NE.3.OR.HBREAK.LE.0d0) RETURN`). 보정 실행 경로는 `DP(I)`가 1000 미만인 절점을 건너뛴 뒤 `TKM` 대각 성분에 분산 보정을 더한다 (`src/nodalattr.F:2838` `TKM(1,I) = TKM(1,I) + Cd*adju*UVBar/H1`; `src/nodalattr.F:2839` `TKM(2,I) = TKM(2,I) + Cd*adjv*UVBar/H1`; `src/nodalattr.F:2822` `IF (DP(I).LT.1000d0) CYCLE`). [10-12 전수 검증 보완] 코리올리는 `VCOEFXY·VCOEFYX`에서 `TKM(3,I)`와 결합한다 (`src/momentum.F:770` `VCOEFXY = DTO2*(TKM(3,I) - CorifA)`; `src/momentum.F:771` `VCOEFYX = DTO2*(TKM(3,I) + CorifA)`).
- 2×2 [VCOEFXX VCOEFXY; VCOEFYX VCOEFYY] 를 풀어 `(UU2,VV2)` — Coriolis·friction 을 implicit 처리해 안정.

## 4. Bottom friction TK — hybrid (gwce.F:2479, NOLIBF)

```fortran
TK = FRIC·( IFLINBF + (|U|/H)·( IFNLBF + IFHYBF·(1+(HBREAK/H)^FTHETA)^(FGAMMA/FTHETA) ) )
```
- `NOLIBF=0·1·2`는 각각 선형 감쇠·이차·혼합 바닥 마찰 분기를 선택한다 (`src/nodalattr.F:2025` `IFLINBF=1`; `src/nodalattr.F:2030` `IFLINBF=0`; `src/nodalattr.F:2035` `IFLINBF=0`). 현재 코드는 `NOLIBF=3`도 허용한다 (`src/read_input.F:1485` `IF((NOLIBF.LT.0).OR.(NOLIBF.GT.3)) THEN`; `src/nodalattr.F:2440` `NOLIBFRIC: IF (NOLIBF.eq.3) THEN`). `NOLIBF=3`, 양수 `HBREAK`, `DP(I)`가 1000 이상인 경로의 운동량 분산 보정은 `MLD`와 시간평균 유속을 사용한다 (`src/nodalattr.F:2818` `IF (NOLIBF.NE.3.OR.HBREAK.LE.0d0) RETURN`; `src/nodalattr.F:2825` `UVBar = SQRT(UBar(I)*UBar(I)+VBar(I)*VBar(I))`; `src/nodalattr.F:2828` `Cd = HBREAK*(max(4d-3,MLD(I))**FTHETA - 1d0)`; `src/nodalattr.F:2822` `IF (DP(I).LT.1000d0) CYCLE`). [10-12 전수 검증 보완]
- 기본 바닥 마찰 `TK` 계산은 `MIN`으로 `2.0/DTDP` 상한을 적용한다 (`src/nodalattr.F:2468` `TK(I) = MIN(FRIC(I)*`; `src/nodalattr.F:2469` `&                     (IFLINBF +                                          ! linear`; `src/nodalattr.F:2470` `&                     (UV1/H1) * (IFNLBF +                               ! nonlinear`; `src/nodalattr.F:2471` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid`; `src/nodalattr.F:2472` `&                  2.0/DTDP)`). 혼합 바닥 마찰의 인자는 `(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)`다 (`src/nodalattr.F:2471` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid`). 해석: `(HBREAK/H1)**FGAMMA` 근사는 원문의 `(HBREAK/H1)**FTHETA`가 1보다 훨씬 클 때 성립한다 (`src/nodalattr.F:2471` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid`). [10-12 전수 검증 보완]
- `FRIC` = bottom friction 계수 (`nodalattr.F` Manning's n 또는 fort.13 공간변화). 3 time level: TK0/TK/TK2 (gwce.F:2477-2482).
- BEDSTR = `H·|U|·TK·ρ` (bed shear N/m², timestep.F:1638-1638).


([theory 보고서 §5 1031행 (`C08`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C08 추가 마찰 분기·수치 상한 누락) 근거: `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:3168` `IF(NOLIBF.EQ.3) READ(15,*) CF,HBREAK,FTHETA`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2472` `&                  2.0/DTDP)`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2818` `IF (NOLIBF.NE.3.OR.HBREAK.LE.0d0) RETURN`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2822` `IF (DP(I).LT.1000d0) CYCLE`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2828` `Cd = HBREAK*(max(4d-3,MLD(I))**FTHETA - 1d0)`<br>해석: 보고서 C08의 선형·이차·혼합 설명은 NOLIBF=3과 TK 상한을 포함하지 않는다. 기존 기본식에 이 구현 조건을 보완해야 한다. 결론: 문서 누락. 현재 바닥 마찰 노트에는 NOLIBF=3의 별도 처리와 기본 TK의 2/DTDP 상한을 추가해야 한다.

## 5. GWCE ↔ momentum 결합

- GWCE와 운동량의 호출 순서 및 predictor-corrector 예외는 [시간 단계 노트의 solveGWCE 절](adcirc-timestep-orchestration.md#2-solvegwce--gwcemomentum-결합-순서-gwcef166-226-)을 정본으로 사용한다 (`src/gwce.F:182–222`; `src/timestep.F:1073,1107`). [10-12 결론 검증 정정]
- wetting-drying([[adcirc-wetting-drying-implementation]]): dry node 유속 0, MJU/노드 mask.
- TIMESTEP은 `C3D` 조건에서 `Apply3DBottomFriction`을 호출한다 (`src/timestep.F:594` `if (C3D) then`; `src/timestep.F:599` `CALL Apply3DBottomFriction(Q, SIGMA, DP, ETA2, G, IFNLFA, NP,`). TIMESTEP은 `METONLY`가 거짓인 유동 계산 블록의 `C3DVS` 조건에서 `VSSOL`을 호출한다 (`src/timestep.F:1127` `IF (C3DVS) THEN`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`; `src/timestep.F:813` `IF (.NOT.METONLY) THEN`). [10-12 전수 검증 보완] `solveMomentumEq`의 2D 풀이 선택은 `C2DDI` 조건 안에 있다 (`src/momentum.F:125` `IF (C2DDI) THEN`).


([theory 보고서 §5 1028행 (`C05`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C05 TK와 GWCE 좌변) 근거: `models/ADCIRC/raw/source_code/adcirc/src/gwce.F:442` `TK(I) = max(abs(TKM(1,I))+abs(TKM(3,I)),`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:443` `&                     abs(TKM(2,I))+abs(TKM(3,I)))`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:445` `CALL CalculateTimeVaryingTau0(TK, NNeigh, NeiTab, NP)`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:516` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:538` `MsFacLOnDiag =OnDiag*AreaIE*(1.d0/DT+Tau0Avg_S/2.d0)/DT/12.d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/momentum.F:751` `VCOEFXX = DTO2*(TKM(1,I) + SPNGCOEF_X)`<br>보고서 C05의 노트는 gwce.F의 TK를 독립 좌변 마찰항처럼 설명한다. 해석: 해당 TK는 시간 가변 τ₀ 입력이다. τ₀를 통한 간접 효과와 운동량 좌변 TKM 계수를 구분해야 한다. 결론: 문서 오기. 현재 GWCE의 TK는 시간 가변 τ₀를 통해 좌변에 영향을 주며 독립 마찰 강성항으로 직접 들어가지 않는다.

## 6. 연결

- [[adcirc-gwce-implementation]] — 연속방정식→ζ (companion; friction TK 공유)
- [[adcirc-3d-mode]] — 3D velocity/stress form (vsmy.F), baroclinic
- [[adcirc-wetting-drying-implementation]] — dry node 유속 처리
- tidal potential(NTIP)·SAL — barotropic 에 합산되는 조석 forcing (별도 조석 노트 후보)
- Luettich & Westerink ADCIRC theory (운동량 방정식 정식)
