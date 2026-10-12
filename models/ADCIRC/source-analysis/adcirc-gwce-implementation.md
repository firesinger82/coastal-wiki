---
title: "adcirc gwce implementation"
topic: general
canonical_source: self
citation_status: verified
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-gwce-implementation.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

# ADCIRC GWCE solver — matrix assembly, time integration, JCG solve

## Scope

The Generalized Wave Continuity Equation is ADCIRC's mass-conservation equation for water surface elevation. This note documents matrix assembly, lumped vs consistent mass, time integration scheme, JCG solver dispatch, boundary contributions, and SAL (self-attraction & loading) integration.


([fort15 보고서 §5 L81, L82, L716, C02 (L840)](../../../_staging/recovery/compare/ADCIRC-fort15-vs-code.md#5-차이-결론); 항목: TAU0=-5.x의 필수 줄과 제한 순서) 근거: 확인한 원문: `docs/technical_reference/parameter_definitions/index.rst:531` ` Include this line only if TAU0= -5. Specified values that the spatially and time varying TAU0 scheme must stay between. Suggested values are Tau0FullDomainMin = 0.005 and Tau0FullDomainMax = 0.2. `<br>`src/read_input.F:2505` ` IF ( (Tau0.le.-5.d0).and.(Tau0.gt.-6.d0) ) THEN `<br>`src/read_input.F:2506` ` READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax `<br>`src/nodalattr.F:1979` ` IF ( .not.LoadTau0MinMax ) THEN `<br>`src/nodalattr.F:1981` ` Tau0MinMax(I,1) = Tau0FullDomainMin `<br>`src/nodalattr.F:1982` ` Tau0MinMax(I,2) = Tau0FullDomainMax `<br>`src/nodalattr.F:2190` ` Tau0Temp(i)=Tau0MinMax(i,1)+1.5*TK(i) `<br>`src/nodalattr.F:2194` ` IF(Tau0Temp(i).gt.Tau0MinMax(i,2)) THEN `<br>`src/nodalattr.F:2195` ` Tau0Temp(i)=Tau0MinMax(i,2) `<br>`src/nodalattr.F:2213` ` CaseySum = CaseySum + Tau0Temp(NeiTab(I,J)) `<br>`src/nodalattr.F:2215` ` TAU0VAR(I) = CaseySum / NNeigh(I) `<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:270` `` applied during the update. Each node's :math:`\tau_0` is then spatially averaged ``<br>`docs/user_guide/model_configuration/model_parameters/tau0.rst:271` ``` with all immediate neighbors. Time-averaging (for ``TAU0 = -6 or -7``) is ```<br>해석: 문서의 정확히 -5 조건은 같은 문서의 -x.1 출력 선택과 양립하지 않는다. 코드는 -6<TAU0<=-5에서 min/max 줄을 반드시 읽는다. 문서의 suggested values는 생략 기본값이 아니다. 절점 제한 후 이웃 평균을 적용하므로 서로 다른 절점 경계 안에 최종값이 남는다는 보장은 없다. 결론: 문서 오기. -6<TAU0<=-5이면 코드는 다음 줄의 min/max를 읽어 절점 제한 후 공간 평균에 사용한다.
([theory 보고서 §5 1024행 (`C01`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C01 DTDP의 계산 역할) 근거: `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2521` `READ(15,*) DTDP`<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2522` `IF(DTDP.LT.0.d0) THEN`<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2528` `DT=-DTDP`<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2529` `DTDP=DT`<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2535` `DT=DTDP`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:538` `MsFacLOnDiag =OnDiag*AreaIE*(1.d0/DT+Tau0Avg_S/2.d0)/DT/12.d0`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1256` `EVMAvgODT=((EVMN1+EVMN2+EVMN3)/3.d0)/DT`<br>보고서 C01이 인용한 노트는 DTDP를 모델 시계에만 쓰는 값으로 제한한다. 해석: DT=abs(DTDP)이고 GWCE가 DT를 사용하므로 같은 판 코드와 모순된다. 결론: 문서 오기. DTDP는 DT로 전달되어 GWCE 계산에 사용되므로 모델 시계에만 쓰는 값이라는 노트 설명은 오기이다.
([theory 보고서 §5 1025행 (`C02`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C02 시간 가중치와 FTHETA) 근거: `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:3010` `READ(15,*) A00,B00,C00`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:516` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1540` `&        - GDPAvgOAreaIE4_S0*( C00*( SFCXADJ*FDX1*E0XGrad2A+`<br>`models/ADCIRC/raw/source_code/adcirc/src/gwce.F:1543` `&                                    SFCYADJ*FDY1*E1YGrad2A ) )`<br>`models/ADCIRC/raw/source_code/adcirc/docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:46` `` :math:`\mathrm{A00} = \mathrm{C00} = 0.5\theta, \quad \mathrm{B00} = 1-\theta` ``<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:2471` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid`<br>보고서 C02의 노트는 반암시적 시간 가중을 배제한다. 해석: 독립 변수명 Theta의 부재는 A00·B00·C00 시간 가중의 부재를 뜻하지 않는다. FTHETA는 별도 바닥 마찰 지수이다. 결론: 문서 오기. 현재 GWCE는 A00·B00·C00로 세 시간 수준을 가중하며 FTHETA는 바닥 마찰 지수이다.
([theory 보고서 §5 1026행 (`C03`)](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md#5-차이-결론); 항목: C03 TAU0=−5의 필수 다음 줄) 근거: `models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2505` `IF ( (Tau0.le.-5.d0).and.(Tau0.gt.-6.d0) ) THEN`<br>`models/ADCIRC/raw/source_code/adcirc/src/read_input.F:2506` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:1981` `Tau0MinMax(I,1) = Tau0FullDomainMin`<br>`models/ADCIRC/raw/source_code/adcirc/src/nodalattr.F:1982` `Tau0MinMax(I,2) = Tau0FullDomainMax`<br>보고서 C03의 노트는 입력 줄을 생략하면 기본값이 대신한다고 적는다. 해석: 이 READ에는 생략을 허용하는 IOSTAT 분기가 없다. 뒤의 절점 속성 대체는 필수 입력 줄을 건너뛰는 규칙이 아니다. 결론: 문서 오기. −6<TAU0≤−5 입력은 다음 줄의 전영역 최소·최대를 필수로 읽으므로 생략 시 기본값을 쓴다는 노트 설명은 오기이다.
([features 보고서 §5 A08 (439줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: ALI가 사용하는 수심) 근거: docs/user_guide/model_configuration/tides/ali_dispersion_conrtol.rst:47 ``where Ma is the Mach number (:math:`Ma = \frac{\sqrt{gH}}{Cs}`) and H is the``<br>docs/user_guide/model_configuration/tides/ali_dispersion_conrtol.rst:48 `total water depth.`<br>src/global.F:558 `INTEGER :: IFNL_HDP = 0 ! use H (1) or D (0) in LHS surface gradient term`<br>src/gwce.F:501 `IF(level0)THEN`<br>src/gwce.F:502 `DPAvg = (H1N1+H1N2+H1N3)/3.d0`<br>src/gwce.F:505 `DPAvg = (DP(NMI1)+DP(NMI2)+DP(NMI3))/3.d0 +   ! BAVG if GWCE_NL_HDP = .FALSE.`<br>src/gwce.F:506 `&              IFNLFA*IFNL_HDP*(ETA2(NMI1) + ! HAVG otherwise`<br>src/gwce.F:507 `&              ETA2(NMI2)+ETA2(NMI3))/3.d0 ;`<br>src/gwce.F:512 `Ma2   = G*DPavg/Cs2`<br>src/gwce.F:513 `Cfac = (1.0D0 - 0.25D0*Ma2 - Ad*DPavg**Bd)**2`<br>src/read_input.F:1360 `IFNL_HDP = 1`<br>해석: 문서가 권고한 IMDig6=3은 IFNL_HDP=1을 설정하므로 그 권고 구성에서는 총수심을 쓴다. 문서가 다른 IM 조합에서 적용되는 IFNL_HDP 조건을 생략했다. 결론: 문서 누락. 비-subgrid GWCE의 ALI 수심은 IFNL_HDP=0일 때 정수심 DP의 평균이다.
([features 보고서 §5 K50 (614줄)](../../../_staging/recovery/compare/ADCIRC-features-vs-code.md#5-차이-결론); 항목: ALI의 Cs=0 처리) 근거: src/read_input.F:861 `if (Cs.le.0.0D0) then`<br>src/read_input.F:862 `Cs2 = huge(0.0D0)`<br>해석: 문서의 음수 설명은 0을 포함하는 실제 조건을 생략한다. 결론: 문서 누락. ALI의 Cs가 0 이하이면 코드는 Cs2를 huge 값으로 설정한다.

## A. Matrix assembly

- Primary routine: `GWCE_New` at `[file=src/gwce.F line=237]`. Rebuild gated by `NCIFBLCK` at `[file=src/gwce.F line=427]` (`IF(NCChange.GT.0 .or. CGWCE_HDP)`).
- Lumping weights at `[file=src/gwce.F line=418-420]`:
  - `OnDiag = (1+ILump)*2`, `OffDiag = (1-ILump)`
  - `ILump=0` → consistent mass; `ILump=1` → diagonal-only (lumped)
- Mass + tau0 factors at `[file=src/gwce.F line=538-540]`: `MsFacLOnDiag`, `MsFacLOffDiag`
- Flux-gradient stiffness: `GA00DPAvgOAreaIE4*FDX/FDY` products into `Coef` at `[file=src/gwce.F line=564-592]`
- Friction/`Tau0Var` enters via `Tau0Avg[_S]` in mass-like factors at `[file=src/gwce.F line=517, 538-539, 607, 623]` — affects both consistent and lumped paths
- LHS assembly at `[file=src/gwce.F line=429-636]` (`Coef`/`Coefd`)
- RHS forcing assembly at `[file=src/gwce.F line=998-1617]`
- Boundary elimination modifies LHS at `[file=src/gwce.F line=638-673]`; RHS compensation via `OBCCoef` at `[file=src/gwce.F line=1846-1854]`
- `ILump` switch points: `[file=src/gwce.F line=141, 430, 455, 595, 709, 1846, 1856]`
- Memory allocation: `alloc_main11` (consistent) vs `alloc_main11_lumped` at `[file=src/gwce.F line=141-154]`

## B. Time integration

- `DT` enters matrix terms directly at `[file=src/gwce.F line=538-539, 623, 1429, 1741, 1758]`
- GWCE 조립은 `DT`를 사용한다 (`[file=src/gwce.F line=538]` `MsFacLOnDiag =OnDiag*AreaIE*(1.d0/DT+Tau0Avg_S/2.d0)/DT/12.d0`). 양수 `DTDP` 입력은 `DT`에 그대로 대입한다 (`[file=src/read_input.F line=2535]` `DT=DTDP`). 음수 `DTDP` 입력은 predictor-corrector를 켠다 (`[file=src/read_input.F line=2522]` `IF(DTDP.LT.0.d0) THEN`; `[file=src/read_input.F line=2523]` `CPRECOR    = .TRUE.`). 이 분기는 `DT`와 `DTDP`를 같은 양수 값으로 바꾼다 (`[file=src/read_input.F line=2528]` `DT=-DTDP`; `[file=src/read_input.F line=2529]` `DTDP=DT`).
- Three-time-level state in `GWCE_New_pc`: `ETA0, ETA1, ETA2` at `[file=src/gwce.F line=2514-2522]`
- Time weighting: `C00` (n-1) + `(A00+B00)` (n) for free-surface RHS at `[file=src/gwce.F line=1540-1543]`; corrector at `[file=src/gwce.F line=2851-2852]`
- State shift each step: `Eta1=Eta2`, optionally `Eta0=Eta1` at `[file=src/gwce.F line=1622-1631]`
- ETA2 update at `[file=src/gwce.F line=2007]` or `[file=src/gwce.F line=2020]`

GWCE는 θ라는 이름의 별도 입력값을 읽지 않는다 (`[file=src/read_input.F line=3010]` `READ(15,*) A00,B00,C00`). `A00·B00·C00`는 중력항의 새·현재·이전 수위 시간 가중치다 (`[file=src/read_input.F line=3010]` `READ(15,*) A00,B00,C00`; `[file=src/gwce.F line=516]` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`; `[file=src/gwce.F line=1540]` `&        - GDPAvgOAreaIE4_S0*( C00*( SFCXADJ*FDX1*E0XGrad2A+`; `[file=src/gwce.F line=1543]` `&                                    SFCYADJ*FDY1*E1YGrad2A ) )`). `A00`가 비영이면 새 수위 강성항이 좌변에 들어간다 (`[file=src/gwce.F line=516]` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`). 해석: θ라는 이름이 없다는 사실은 GWCE가 명시적이라는 뜻이 아니다 (`[file=src/gwce.F line=516]` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`). `FTHETA`는 혼합 바닥 마찰 법칙의 지수다 (`[file=src/nodalattr.F line=2471]` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid`).

## C. Solver

- 일반 `GWCE_New`의 `ILump.eq.0` 경로는 `JCG`를 호출한다 (`[file=src/gwce.F line=2000]` `IF (ILump.eq.0) THEN ! default, fully consistent LHS`; `[file=src/gwce.F line=2003]` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`).
- 일반 `GWCE_New`의 `ELSE` 경로는 대각 계수에 따라 역산 또는 0 대입을 수행한다 (`[file=src/gwce.F line=2009]` `ELSE ! lumped LHS`; `[file=src/gwce.F line=2016]` `ETAS(I) = GWCE_LV(I) * RDIAG`). [10-12 전수 검증 보완] 대각 계수가 0이면 `RDIAG`를 0으로 둔다 (`src/gwce.F:2011` `IF (COEFDTemp(I).eq.0.0d0) THEN`; `src/gwce.F:2012` `RDIAG = 0.0d0`). [10-12 전수 검증 보완] 그 외에는 대각 계수의 역수를 사용한다 (`src/gwce.F:2013` `ELSE`; `src/gwce.F:2014` `RDIAG = 1.0d0 / COEFDTemp(I)`). [10-12 전수 검증 보완]
- `ITMAX` cap: `IPARM(1)=ITMAX` at `[file=src/gwce.F line=146]`, `[file=src/gwce.F line=2002]`
- Convergence tolerance: `RPARM(1)=CONVCR` at `[file=src/gwce.F line=150]`
- Iteration count returned in `IPARM(1)` → captured as `NUMITR` at `[file=src/gwce.F line=2005]`

## D. Boundary contributions

- Open-boundary harmonic synthesis: `ETA2(NBDI) += EMO*FF*RampElev*cos(AMIG*timeh + FACE - EFA)` at `[file=src/gwce.F line=1638-1650]`, driven by `NBFR`
- Aperiodic `fort.19` interpolation at `[file=src/gwce.F line=1659-1673]` using `ESBIN1/ESBIN2`
- Boundary topology (`NOPE, NETA, NBD, NBV, LBCODEI`) consumed via `USE BOUNDARIES` at `[file=src/gwce.F line=270-271]`, `[file=src/cstart.F line=64]`, `[file=src/hstart.F line=58]`
- Normal-flow / radiation / gradient boundary fluxes contribute to RHS at `[file=src/gwce.F line=1725-1834]`, per-`LBCODEI` formulas, `Tau0Var` coupling at `[file=src/gwce.F line=1740-1764, 1782-1805]`
- Elevation-specified boundaries: row/column modification on LHS at `[file=src/gwce.F line=652-673]`; scaled RHS enforcement at `[file=src/gwce.F line=1840-1861]`
- No-flux land suppression via `NODECODE` masking at `[file=src/gwce.F line=474-477, 1010-1015]`; dry/landlocked nodes init in cold start at `[file=src/cstart.F line=1221-1223, 1258-1260]`

## E. SAL integration (NTIP=2 path)

- Reader: `readSelfAttractionAndLoadingFile` at `[file=src/adcirc.F line=292-293]` — comment notes `fort.24`
- SAL added to tidal potential in hot start: `+ SALTMUL * SALTAMP(J,I) * COS(ARGSALT)` at `[file=src/hstart.F line=1522, 1530-1532]`
- GWCE consumes via `TiP1`/`TiPN*` at `[file=src/gwce.F line=1181-1184]`, used in forcing gradients at `[file=src/gwce.F line=1450-1452, 1462-1464]`
- So SAL-modified tidal potential propagates into GWCE RHS

## F. Wetting-drying mask

- Element wet/dry mask: `NCELE = NC1*NC2*NC3*NOFF(IE)` at `[file=src/gwce.F line=477, 605, 1015, 1074]`
- Any dry node (`NODECODE=0`) nulls that element's contribution
- Subgrid wetting/drying: `wetFracVertETA1/2` modifies LHS at `[file=src/gwce.F line=465-473, 541-547]` and RHS at `[file=src/gwce.F line=1055-1063, 1436-1439]`
- Initial dry-node logic in cold start: `[file=src/cstart.F line=1221-1231, 1258-1268]`
- No separate dry-node check inside GWCE — purely multiplicative masking via `NODECODE`

## Decision Guide — 진단 (트러블슈팅)

| Symptom | Likely cause | Source-level investigation |
|---------|--------------|----------------------------|
| Tidal amplitude wrong (지역 bias) | flux-gradient term + tau0 + bottom-friction interaction | Check `Tau0Var` + `FRIC` flow into `Coef` (`gwce.F:538-592`) |
| Iteration count high | poor preconditioning or stiff diagonals | `NUMITR` in stdout; tighten `CONVCR` |
| Boundary spike | tide block format wrong in fort.15 | `NBFR` block mismatch (`gwce.F:1638-1650`) |
| Mass loss at wet/dry front | `NCELE` masking issue | `gwce.F:477` dry-element zeroing |

## Working Rules

1. GWCE 행렬의 시간 간격은 `DT`다 (`[file=src/gwce.F line=538]` `MsFacLOnDiag =OnDiag*AreaIE*(1.d0/DT+Tau0Avg_S/2.d0)/DT/12.d0`). 입력 reader는 양수 `DTDP`를 `DT`에 대입한다 (`[file=src/read_input.F line=2535]` `DT=DTDP`). 음수 입력 경로도 부호 변환 뒤 `DTDP=DT`로 대입한다 (`[file=src/read_input.F line=2528]` `DT=-DTDP`; `[file=src/read_input.F line=2529]` `DTDP=DT`).
2. 일반 `GWCE_New`는 `ILump.eq.0`에서 `JCG`를 호출한다 (`[file=src/gwce.F line=2000]` `IF (ILump.eq.0) THEN ! default, fully consistent LHS`; `[file=src/gwce.F line=2003]` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`). 그 `ELSE` 경로는 대각 계수에 따라 역산 또는 0 대입을 수행한다 (`[file=src/gwce.F line=2009]` `ELSE ! lumped LHS`; `[file=src/gwce.F line=2016]` `ETAS(I) = GWCE_LV(I) * RDIAG`). 대각 계수가 0인 경우를 포함한 계산식은 [Solver 절](#c-solver)을 정본으로 사용한다. `GWCE_New_pc`는 같은 `ILump` 게이트 없이 `JCG`를 별도로 호출한다 (`[file=src/gwce.F line=3070]` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`). 확인하지 않음: 임의 `ILump·CPRECOR` 조합의 실행 지원과 성능. [10-12 결론 검증 정정]
3. **`Tau0Var` enters mass factors, not friction directly.** It weights the GWCE matrix; friction is separate via `FRIC` from Manning conversion.
4. **SAL = `fort.24` ASCII or NetCDF** with one block per tide constituent. NTIP=2 must be set.
5. **NUMITR > 50 iteration suggests stiff matrix** — increase `ITMAX`, tighten mesh, or check very-shallow elements.

## Common Pitfalls

- `IF ( (Tau0.le.-5.d0).and.(Tau0.gt.-6.d0) ) THEN`이면 다음 위치 입력 줄의 `Tau0FullDomainMin, Tau0FullDomainMax`를 읽는다 (`[file=src/read_input.F line=2505]` `IF ( (Tau0.le.-5.d0).and.(Tau0.gt.-6.d0) ) THEN`; `[file=src/read_input.F line=2506]` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`). 이 `READ`에는 생략을 허용하는 `IOSTAT` 처리가 없다 (`[file=src/read_input.F line=2506]` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`). 해석: 입력 줄을 생략하면 reader가 다음 위치 입력을 이 두 값으로 소비한다 (`[file=src/read_input.F line=2506]` `READ(15,*) Tau0FullDomainMin, Tau0FullDomainMax`). `Tau0Dig1.eq.-5`이고 `LoadTau0MinMax`가 거짓이면 후속 경로는 두 위치 입력값을 절점 최소·최대 값에 복사한다 (`[file=src/nodalattr.F line=1979]` `IF ( .not.LoadTau0MinMax ) THEN`; `[file=src/nodalattr.F line=1981]` `Tau0MinMax(I,1) = Tau0FullDomainMin`; `[file=src/nodalattr.F line=1982]` `Tau0MinMax(I,2) = Tau0FullDomainMax`; `src/nodalattr.F:1977` `IF ( Tau0Dig1.eq.-5 ) THEN`). [10-12 전수 검증 보완]
- **Boundary ELEVALPHA wrong** — phases shifted across NBFR block; check `read_input.F:3445-3470` parse order.
- **Hot-restart with different `ILump`** — matrix shape differs; restart fails or silently runs lumped.
- **NTIP=2 without fort.24** — runtime error or zero SAL contribution.

## References

- `src/gwce.F` — main solver.
- `src/momentum.F` — companion momentum equations.
- `src/cstart.F` / `src/hstart.F` — cold/hot start paths.
- `src/adcirc.F` — high-level driver, NTIP/SAL init.

## Provenance

| Field | Value |
|-------|-------|
| Authored by | Claude Opus 4.7 |
| Generated | 2026-05-07 |
| Codex scan | 30+ file:line citations |
| Coverage | matrix assembly, time integration, JCG, boundary, SAL, wet/dry mask |
| Review status | `review_required: true` |
