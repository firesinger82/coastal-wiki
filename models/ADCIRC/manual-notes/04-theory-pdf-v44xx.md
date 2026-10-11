---
citation_status: verified
origin: _archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/methods/adcirc-sources/04-theory-pdf-v44xx.md
promoted_date: 2026-05-24
promote_phase: 2a
classification: manual-notes-catalog
source_id: models/ADCIRC
notes: "P2 catalog audit 2026-05-24 — external URL catalog (adcirc.github.io/adcirc.org/github.com) verified via WebFetch sampling (03 theory + 06 parameter_definitions confirm docs structure live)"
last_source_check: 2026-10-11 (recovery 재판독 대조)
---
# ADCIRC Theory PDF V44.xx

## Metadata

- date: 2026-04-12
- title: Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.xx
- source type: report
- authors: Rick Luettich, Joannes Westerink
- year: 2004
- link: https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf

## Why This Matters

This is still the most concrete formulation document surfaced by the official docs.

## Core Claims

- ADCIRC uses a generalized wave continuity equation formulation to avoid spurious oscillations associated with a primitive Galerkin continuity formulation
- the document provides the weak-form derivation, momentum formulations, boundary-condition treatment, and implementation notes
- the report is detailed enough to anchor stability discussions instead of relying on folklore

## Practical Value

- 방법 근거: 2004년 v44.XX 이론 PDF의 식을 v56.2.1 코드와 함께 검토한다. (`docs/theory/index.rst:6` ```Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.XX (PDF) <https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf>`_``; `CMakeLists.txt:92` `set(ADCIRC_VERSION_STRING "v56.2.1")`)
- implementation detail: useful when a fort.15 decision needs a formulation-level rationale
- validation detail: provides the theoretical basis for interpreting convergence and oscillation behavior
- 한계: 이론 PDF와 현재 코드는 판이 다르다. (`raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 1 / 인쇄 쪽 1`; `CMakeLists.txt:92` `set(ADCIRC_VERSION_STRING "v56.2.1")`) 현재 호출 순서의 단독 근거로 이 PDF를 사용하지 않는다. (`src/timestep.F:1073` `call solveGWCE(it, ITIME_BGN, timeloc, timeh)`; `src/timestep.F:1107` `call solveMomentumEq()`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`)

## 이론 문서와 코드(v56.2.1)의 식 차이

주 이론 매뉴얼은 v44.XX(2004)이다. (`docs/theory/index.rst:6` ```Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.XX (PDF) <https://adcirc.org/wp-content/uploads/sites/2255/2018/11/adcirc_theory_2004_12_08.pdf>`_``)
대조한 코드는 v56.2.1이다. (`CMakeLists.txt:92` `set(ADCIRC_VERSION_STRING "v56.2.1")`)
아래 차이에는 판 차이가 섞여 있다. 어느 쪽이 맞는지는 단정하지 않는다.

이 표는 theory 보고서 §1.3의 주요 불일치를 정리한다. 문서 식 열은 차이에 직접 대응하는 원문 식 또는 항을 적는다.
`raw/manuals/pdfs/`는 `models/ADCIRC/` 기준이다. `src/`·`docs/`는 `models/ADCIRC/raw/source_code/adcirc/` 기준이다.

| 식 번호·문서·쪽 | 문서 식·원문 항 | 코드 src/파일:줄과 원문 | 차이 |
|---|---|---|---|
| 식 (1.29) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 13 / 인쇄 쪽 13` | `-\bar{E}_h^s\frac{\partial\zeta^{*s}}{\partial x}` | `src/gwce.F:1256` `EVMAvgODT=((EVMN1+EVMN2+EVMN3)/3.d0)/DT`; `src/gwce.F:1259` `&         -EVMAvgODT*(ESN1*FDX1+ESN2*FDX2+ESN3*FDX3))/AreaIE2`; `src/gwce.F:1262` `&         -EVMAvgODT*(ESN1*FDY1+ESN2*FDY2+ESN3*FDY3))/AreaIE2` | 해석: 문서의 수위 증분 항에는 1/Δt가 없다. 코드의 EVMAvgODT는 1/DT를 포함한다(정적 판독, 실행 미확인). |
| 무번호 경계 유량 식 · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 9 / 인쇄 쪽 9`<br>TIME-WEIGHTS · `docs/user_guide/model_configuration/model_parameters/a00_b00_c00.rst:8-12` | `Q_{N_i}=\alpha_1Q_{N_i}^{s+1}+\alpha_2Q_{N_i}^s+\alpha_3Q_{N_i}^{s-1}` | `src/gwce.F:516` `GA00DPAvgOAreaIE4 = ALPHAL(IE)*A00*G*DPAvg*Cfac/AreaIE4`; `src/gwce.F:1540` `&        - GDPAvgOAreaIE4_S0*( C00*( SFCXADJ*FDX1*E0XGrad2A+`; `src/gwce.F:1543` `&                                    SFCYADJ*FDY1*E1YGrad2A ) )`; `src/gwce.F:1741` `&        QFORCEJ=(QN2(1)-QN0(1))/DT2 + Tau0VAR(NBDJ)*QN1(1)` | 해석: A00·B00·C00는 중력항의 세 수위 시간 수준을 가중한다. 코드의 경계 τ₀QN은 QN1만 사용한다. 이 PDF의 식 (1.17)도 QN^s만 사용하므로 문서 내부 설명이 일관되지 않다(정적 판독, 실행 미확인). |
| 식 (2.5)·(2.6) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 17 / 인쇄 쪽 17` | `H\tau_{xx}&=2E_h\frac{\partial Q_x}{\partial x}`<br>`H\tau_{yx}&=E_h\left[\frac{\partial Q_x}{\partial y}+\frac{\partial Q_y}{\partial x}\right]`<br>`H\tau_{xx}&=2HE_h\frac{\partial U}{\partial x}`<br>`H\tau_{yx}&=HE_h\left[\frac{\partial U}{\partial y}+\frac{\partial V}{\partial x}\right]` | `src/momentum.F:518` `LSXXN1=EVMEle*DQX1DX`; `src/momentum.F:521` `LSXYN1=0.5d0*EVMEle*(DQX1DY+DQY1DX)`; `src/momentum.F:566` `LSXXN1=EVMH1N1*DU1DX`; `src/momentum.F:569` `LSXYN1=0.5d0*EVMH1N1*(DU1DY+DV1DX)` | 해석: 같은 E_h=EVM 입력에서 문서의 대칭 응력 계수는 현재 코드의 두 배다(정적 판독, 실행 미확인). |
| 식 (2.7) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 18 / 인쇄 쪽 18`<br>식 (2.9)·(2.12) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 22·23 / 인쇄 쪽 22·23` | `-\left\langle\frac{K_{slip}U}{H\rho_o},\phi_j\right\rangle` | `src/nodalattr.F:2470` `&                     (UV1/H1) * (IFNLBF +                               ! nonlinear`<br>`src/momentum.F:751` `VCOEFXX = DTO2*(TKM(1,I) + SPNGCOEF_X)`; `src/momentum.F:783` `MOM_LV_X(I) = NCI*(MOM_LV_X(I)+WSX+(1.D0-VCOEFXX)*UU1(I)` | 해석: 이 장의 τ_b/ρ₀=K_slip U 정의를 적용하면 문서의 바닥 항은 ρ₀를 다시 나눈다. 코드는 정규화 뒤 ρ₀를 다시 나누지 않는다(정적 판독, 실행 미확인). |
| 식 (2.10)·(2.11) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 22·23 / 인쇄 쪽 22·23` | `-\frac{3}{H_jA_{NE_j}}` | `src/momentum.F:1634` `&             -1.5d0*(LSXXN3*FDX3+LSXYN3*FDY3)`; `src/momentum.F:1648` `&             -1.5d0*(LSYXN1*FDX1+LSYYN1*FDY1)`; `src/momentum.F:1712` `IF (TotalArea(I).ne.0.d0) THEN` | 해석: 코드의 FD=2A∂φ를 적용하면 응력 계수는 −3/A_NEj이다. 문서의 유량 운동량 공간식에는 추가 1/H_j가 있다(정적 판독, 실행 미확인). |
| 식 (2.13)·(2.16) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 26·29 / 인쇄 쪽 26·29` | `\left[1+\frac{\Delta tK_{slip_j}^s}{2H_j^{s+1}}\right]`<br>`\left[1-\frac{\Delta tK_{slip_j}^s}{2H_j^{s+1}}\right]` | `src/timestep.F:579` `CALL Apply2DBottomFriction(UU1, VV1, DP, ETA2, G, IFNLFA, NP,`<br>`src/nodalattr.F:2466` `H1  = DP(I) + IFNLFA*ETA2(I)`<br>`src/momentum.F:751` `VCOEFXX = DTO2*(TKM(1,I) + SPNGCOEF_X)`; `src/momentum.F:783` `MOM_LV_X(I) = NCI*(MOM_LV_X(I)+WSX+(1.D0-VCOEFXX)*UU1(I)`; `src/momentum.F:799` `AUV(1,I) = 1d0 + VCOEFXX*NCI` | 해석: 문서는 바닥 마찰 계수의 양쪽 분모에 새 수심 H^(s+1)을 쓴다. 코드는 GWCE 전에 이전 시간 수준 수심으로 계산한 같은 TK를 운동량 양쪽에 사용한다. 수심이 일정하면 이 차이가 사라진다(정적 판독, 실행 미확인). |
| 식 (2.14)·(2.15) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 27·28 / 인쇄 쪽 27·28` | `+\frac{f\Delta t}{2}Q_{y_j}^{s+1}`<br>`-\frac{f\Delta t}{2}Q_{x_j}^{s+1}` | `src/momentum.F:1746` `VCOEFXY = DTO2*(TKM(3,I) - CorifA)`; `src/momentum.F:1759` `MOM_LV_X(I) = NCI*(MOM_LV_X(I)+WSX+(1.D0-VCOEFXX)*QX1(I)`; `src/momentum.F:1760` `&               - VCOEFXY*QY1(I)) !-VIDBCPDX) !-DispX)`; `src/momentum.F:1762` `&               - VCOEFYX*QX1(I)) !-VIDBCPDY) !-DispY)` | 해석: 문서 우변의 코리올리 유량은 새 시간 수준이다. 코드 우변의 코리올리 유량은 QX1·QY1이다. 코드 좌변에는 새 시간 수준의 교차 계수가 따로 있다(정적 판독, 실행 미확인). |
| TAU-1 · `docs/user_guide/model_configuration/model_parameters/tau0.rst:200,204-205` | `D\ge10:\tau_0=0.005;\quad D<10:\tau_0=0.020` | `src/nodalattr.F:2158` `IF(Depth.LE.10.) Tau0NodalValue=0.020d0`; `src/nodalattr.F:2159` `IF(Depth.GT.10.) Tau0NodalValue=0.005d0` | 해석: D=10에서 문서는 0.005를 적는다. 코드는 0.020을 대입한다(정적 판독, 실행 미확인). |
| TAU-2 · `docs/user_guide/model_configuration/model_parameters/tau0.rst:210-214` | `D\ge200:\tau_0=0.005;\ 1<D<200:\tau_0=1/D;\ D<1:\tau_0=1` | `src/nodalattr.F:2149` `IF (Scheme.eq.-2.d0) THEN`; `src/nodalattr.F:2151` `IF(Depth.GE.200.) Tau0NodalValue=0.005`; `src/nodalattr.F:2152` `IF((Depth.LT.200.).AND.(Depth.GE.1.)) THEN`; `src/nodalattr.F:2153` `Tau0NodalValue=1./Depth`; `src/nodalattr.F:2155` `IF(Depth.LT.1.) Tau0NodalValue=1.0` | 해석: 문서는 D=1을 어떤 분기에도 넣지 않는다. 코드는 1≤D<200에서 1/D를 쓴다(정적 판독, 실행 미확인). |
| TAU-FRACTION · `docs/user_guide/model_configuration/model_parameters/tau0.rst:35-37` | `TAU0=-x.1:\ \text{same as }-x` | `src/nodalattr.F:1924` `Tau0Var(I)=Tau0NodalValue(Tau0,DP(I))`; `src/nodalattr.F:1989` `IF ( Tau0Dig2.eq.-1 ) THEN`; `src/nodalattr.F:2149` `IF (Scheme.eq.-2.d0) THEN`; `src/nodalattr.F:2158` `IF(Depth.LE.10.) Tau0NodalValue=0.020d0` | 해석: −2.1은 코드에서 −2와 같은 1/D 분기를 타지 않는다. D=100에서 −2의 대입값은 0.01이다. 같은 수심에서 −2.1의 대입값은 0.005다(정적 판독, 실행 미확인). |
| TAU-UPDATE · `docs/user_guide/model_configuration/model_parameters/tau0.rst:262-265` | `docs/user_guide/model_configuration/model_parameters/tau0.rst:264` `"update" is done when the model starts. After this, updates are done only after`; `docs/user_guide/model_configuration/model_parameters/tau0.rst:265` `a time step in which there is a change in wet/dry state somewhere in the model` | `src/gwce.F:427` `NCIFBLCK: IF(NCChange.GT.0 .or. CGWCE_HDP ) THEN !if any subdomain grid has changed`; `src/gwce.F:445` `CALL CalculateTimeVaryingTau0(TK, NNeigh, NeiTab, NP)` | 해석: 문서는 초기화 뒤 wet/dry 변화가 있는 단계에서만 갱신한다고 적는다. 코드 갱신 진입 조건에는 CGWCE_HDP도 있다(정적 판독, 실행 미확인). |
| WIND-Z0-MARINE · `docs/user_guide/model_configuration/meteorological_forcing/wind_stress.rst:65,67` | `z_{0m}=(0.018/g)c_d\|w\|` | `src/nodalattr.F:2950` `z0m=(0.018d0/G)*WindDragCo*WindMag**2.d0` | 해석: 문서 식은 풍속의 1제곱이다. 코드는 WindMag**2.d0을 사용한다(정적 판독, 실행 미확인). |
| PDF-TIDAL-L0 · `raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 23 / 인쇄 쪽 17` | `L_o=3\sin^2(\phi)-1;\quad L_1=\sin(2\phi);\quad L_2=\cos^2(\phi)` | `src/adcirc.F:303` `L_N(0,I) = 1.5d0*COS(SFEA(I))*COS(SFEA(I)) - 1d0`; `src/adcirc.F:305` `L_N(1,I) = SIN(2d0*SFEA(I))`; `src/adcirc.F:307` `L_N(2,I) = COS(SFEA(I))*COS(SFEA(I))` | 해석: 장주기 위도 함수의 코드값은 Report 1 값의 −1/2이다. 같은 분조 진폭에서 장주기 항의 부호와 크기가 다르다(정적 판독, 실행 미확인). |
| 각 문서 식 (4) · `raw/manuals/pdfs/1993_Westerink02.pdf, PDF 쪽 16 / 인쇄 쪽 4`<br>`raw/manuals/pdfs/1994_Blain03.pdf, PDF 쪽 17 / 인쇄 쪽 5`<br>`raw/manuals/pdfs/1995_Hench.pdf, PDF 쪽 14 / 인쇄 쪽 4` | `\cos\left[\frac{2\pi(t-t_0)}{T_{jn}+j\lambda+\nu_{jn}(t_0)}\right]` | `src/timestep.F:1539` `ARGT=AMIGT(J)*(timeh-NCYC*PERT(J))+FACET(J)`; `src/timestep.F:1556` `ARGTP   = ARGT + NA*SLAM(I)`; `src/timestep.F:1558` `TIP2(I) = TIP2(I) + TPMUL * L_N(NA,I) * COS(ARGTP)` | 해석: 문서는 위상 항을 주기 분모 안에 넣는다. 코드는 각주파수×시간 뒤에 경도·천문 위상을 더한다(정적 판독, 실행 미확인). |
| 식 (3.5) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 32 / 인쇄 쪽 32` | `m_{x\sigma}`<br>`\frac{\partial u}{\partial x_\sigma}` | `src/vsmy.F:784` `Zk = HsOAMB * ( Sigma(k) - B ) - DP(NH)`; `src/vsmy.F:797` `SigmaNN = B + AMB * ( Zk + DP(N2) ) / HsN2`; `src/vsmy.F:800` `&                 inarray_vertical, SigmaNN, qN2_z, k )`; `src/vsmy.F:847` `&            + ( qN1_z*b1 + qN2_z*b2 + qN3_z*b3 )*b1/Areas(NEle)`; `src/vsmy.F:871` `LStress(k)=3.d0*EVM(NH)*(DqDXDPhiDX2A+DqDYDPhiDY2A)` | 해석: 문서의 기본 3D 수평 응력은 같은 σ면의 속도 미분을 사용한다. 현재 VSSOL은 이웃 열을 같은 z로 보간한다. 서로 다른 수심의 열에서 비영 수평 응력이 있으면 공간 연산자가 다르다(정적 판독, 실행 미확인). |
| PDF-VERTICAL-STRESS-DIAG · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 30 / 인쇄 쪽 30` | `\displaystyle \frac{\tau_{zx}}{\rho_o}=E_z\frac{\partial u}{\partial z}=\mathit{vertical\ stress}` | `src/vsmy.F:1188` `DUDS = (Qkp1(NH,2)-Qkp1(NH,1))/(Sigma(2)-Sigma(1))`; `src/vsmy.F:1189` `BSX(NH) = EV(NH,1)*REAL(DUDS)`; `src/vsmy.F:1190` `BSY(NH) = EV(NH,1)*AIMAG(DUDS)` | 해석: ISLIP=0 바닥 진단은 σ 미분을 사용한다. 코드는 이 진단에 z 미분 배율 (a−b)/H를 곱하지 않는다. 전체 연직 운동량 확산 계수와 구분한다(정적 판독, 실행 미확인). |
| 3D-ISLIP-1·3 · `docs/technical_reference/parameter_definitions/index.rst:1273,1278,1287,1291` | `\tau_b/\rho_0=KP\,q_b`<br>`\tau_b/\rho_0=KP\,\|q_b\|q_b` | `src/nodalattr.F:2559` `TK(NH)= FRIC(NH) * ABS(Q(NH,1))`; `src/nodalattr.F:2571` `If ( TK(NH) > abs( Q(NH,1) ) ) TK(NH) = abs( Q(NH,1) )`; `src/nodalattr.F:2572` `If ( TK(NH) < KP * abs( Q(NH,1) ) ) TK(NH) = KP * abs( Q(NH,1) )`<br>`src/vsmy.F:1010` `&           - q(NH,1)*DT1MAlp2*TK(NH)/HsOAMB`; `src/vsmy.F:1015` `&           + DTAlp2*TK(NH)/Hsp1OAMB` | 해석: 현재 비영 ISLIP 분기는 log-law TK를 사용한다. KP는 이차 계수 하한으로 남아 있다. 문서의 지정 선형·이차 계수 설명과 다르다(정적 판독, 실행 미확인). |
| 3D-THETA-ROLES · `docs/technical_reference/parameter_definitions/index.rst:1449,1451` | `\Theta_1:\text{dissipation},\quad\Theta_2:\text{vertical diffusion}` | `src/vsmy.F:2875` `coef2 = delt*theta1/HOamb2`; `src/vsmy.F:2883` `coef1 = 1.d0 + delt*theta2*tdiss`; `src/vsmy.F:2885` `Mqa(n) = Inm(n,1)*coef1+KQnm(n,1)*coef2`; `src/vsmy.F:2892` `coef3 = 1.d0 - delt*(1.d0-theta2)*tdiss` | 해석: 코드의 THETA1은 연직 확산을 가중한다. 코드의 THETA2는 소산을 가중한다. 문서의 두 역할 설명은 반대다(정적 판독, 실행 미확인). |
| 3D-IEVC-42 · `docs/technical_reference/parameter_definitions/index.rst:1414,1416` | `E_{\mathrm{upper}}=2\|UU\|/9.001,\quad E_b=0.002\|UU\|/9.001` | `src/vsmy.F:2006` `EVBASE=2.D0*H*UAVMAGS/9.001D0`; `src/vsmy.F:2007` `EVTOT(1)=EVBASE/1000.D0` | 해석: 코드는 상부값과 바닥값의 분자에 문서에 없는 추가 H를 곱한다(정적 판독, 실행 미확인). |
| PDF-SOLVER-LU · `raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 55 / 인쇄 쪽 49` | `is time-independent and is therefore assembled and LU decomposed only once.` | `src/gwce.F:427` `NCIFBLCK: IF(NCChange.GT.0 .or. CGWCE_HDP ) THEN !if any subdomain grid has changed`; `src/gwce.F:2000` `IF (ILump.eq.0) THEN ! default, fully consistent LHS`; `src/gwce.F:2003` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,`; `src/gwce.F:2014` `RDIAG = 1.0d0 / COEFDTemp(I)   ! COEFD --> COEFDTemp  08-11-2022 SB` | 해석: 현재 consistent 행렬은 JCG로 푼다. 현재 lumped 행렬은 대각 나눗셈으로 푼다. NCChange 또는 CGWCE_HDP 조건에서 행렬을 다시 조립한다(정적 판독, 실행 미확인). |
| PDF-FE-RULE2A-REMOVED · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 70 / 인쇄 쪽 70` | `It was removed from the code as of version XX.XX.` | `src/read_input.F:1344` `CME_AreaInt_Orig = .TRUE.`<br>`src/momentum.F:720` `IF (CME_AreaInt_Orig) THEN       !Original (incorrect) area integration`; `src/momentum.F:721` `MOM_LV_X(I)=MOM_LV_X(I)/MJU(I)` | 해석: 현재 코드에는 original 면적 적분 선택 분기가 남아 있다. 문서의 XX.XX는 실제 제거 판 번호를 특정하지 않는다(정적 판독, 실행 미확인). |
| PDF-WETDRY-OLD · `raw/manuals/pdfs/1994_Westerink01.pdf, PDF 쪽 33 / 인쇄 쪽 21` | `since the current implementation of ADCIRC-2DDI does not include wetting/drying elements` | `src/wetdry.F:241` `IF(HTOT.LE.H0) THEN`; `src/wetdry.F:274` `NNODECODE(I) = 0`; `src/wetdry.F:275` `NODECODE(I) = 0`; `src/wetdry.F:1414` `IF(NNODECODE(I).NE.NODECODE(I)) THEN`; `src/wetdry.F:1415` `NODECODE(I)=NNODECODE(I)` | 해석: Report 2는 당시 구현의 wetting/drying 요소 부재를 적는다. 현재 코드는 총 수심 조건에서 절점 상태를 건조로 바꾼다(정적 판독, 실행 미확인). |
| 식 (1.15) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 6 / 인쇄 쪽 6` | `-\int_{\Gamma}\left[\frac{\partial Q_N}{\partial t}+\tau_o Q_N\right]\phi_j\,d\Gamma=0` | `src/gwce.F:1537` `&         (OnDiag*ESN1*SPM1 + OffDiag*(ESN2*SPM2+ESN3*SPM3))*MsFacR`; `src/gwce.F:1546` `&        +(SFCXADJ*JXAvg*FDX1 + SFCYADJ*JYAvg*FDY1)*0.5d0`; `src/gwce.F:2003` `CALL JCG(NP,MNP,MNEI,NEITAB,COEF,GWCE_LV,ETAS,` | 해석: 문서는 좌변=우변을 적은 뒤 우변 끝에 =0을 다시 적는다. 코드는 일반적으로 0이 아닌 하중벡터를 푼다. 문서 식의 표기 오류 가능성으로 구분한다(정적 판독, 실행 미확인). |
| 식 (6.15) · `raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf, PDF 쪽 63 / 인쇄 쪽 63` | `Auv_{1,k}N_yv_{k-1}` | `src/vsmy.F:1100` `&                 +iy*(Auv1km1+Auv1k+Auv1kp1)*VelNorm` | 해석: 문서의 중앙 계수 Auv_(1,k)Ny에는 v_(k−1)가 붙는다. 코드는 세 Auv1 계수의 합에 VelNorm을 곱한다. 문서 첨자는 법선 조건을 절점마다 대입한 식과 다르다(정적 판독, 실행 미확인). |
| 식 (83b) · `raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 45 / 인쇄 쪽 39` | `\left(VH\frac{\partial U}{\partial y}\right)^k\cong(VH)_{el}^k\sum_{j=1}^{n_{el}}U_j^k\frac{\partial\phi_i}{\partial y}` | `src/gwce.F:1473` `&              QX1Avg*(U1N1*FDX1+U1N2*FDX2+U1N3*FDX3)`; `src/gwce.F:1474` `&             +QY1Avg*(U1N1*FDY1+U1N2*FDY2+U1N3*FDY3))/AreaIE2` | 해석: 문서의 합은 절점 첨자를 j로 적고 기저 미분 첨자를 i로 고정한다. 코드는 각 꼭짓점 U 값에 그 꼭짓점의 FDY를 곱한다. 문서의 ∂φ_i는 첨자 오기일 가능성이 있다. 이 차이를 구현 차이로 단정하지 않는다(정적 판독, 실행 미확인). |
| 식 (100)·(103) · `raw/manuals/pdfs/1992_Luettich02.pdf, PDF 쪽 51·52 / 인쇄 쪽 45·46` | `-\frac{\Delta t}{2}\left\langle f_j'{}^kU_j^{k+1}\phi_j,\phi_i\right\rangle_{\Omega_{el}}`<br>`-\frac{\Delta t}{2}f_j'{}^kM_{ij}^{(1L)}V_j^k` | `src/momentum.F:770` `VCOEFXY = DTO2*(TKM(3,I) - CorifA)`; `src/momentum.F:771` `VCOEFYX = DTO2*(TKM(3,I) + CorifA)`; `src/momentum.F:783` `MOM_LV_X(I) = NCI*(MOM_LV_X(I)+WSX+(1.D0-VCOEFXX)*UU1(I)`; `src/momentum.F:784` `&               - VCOEFXY*VV1(I))`; `src/momentum.F:785` `MOM_LV_Y(I) = NCI*(MOM_LV_Y(I)+WSY+(1.D0-VCOEFYY)*VV1(I)`; `src/momentum.F:786` `&               - VCOEFYX*UU1(I))` | 해석: 문서 식 (100)의 y 코리올리 항은 좌변 음수·우변 양수다. 코드 y 코리올리 항은 좌변 양수·우변 음수다. 식 (103)의 x 우변은 음수지만 코드의 교차 마찰이 0인 x 우변은 양수다(정적 판독, 실행 미확인). |
| 식 (3)·(9) · `raw/manuals/pdfs/1995_Hench.pdf, PDF 쪽 13 / 인쇄 쪽 3`<br>`raw/manuals/pdfs/1995_Hench.pdf, PDF 쪽 16 / 인쇄 쪽 6` | `-\left(\frac{\tan\varphi}{R}U+f\right)U` | `src/momentum.F:771` `VCOEFYX = DTO2*(TKM(3,I) + CorifA)`; `src/momentum.F:785` `MOM_LV_Y(I) = NCI*(MOM_LV_Y(I)+WSY+(1.D0-VCOEFYY)*VV1(I)`; `src/momentum.F:786` `&               - VCOEFYX*UU1(I))` | 해석: 문서 y 운동량의 좌변 코리올리·곡률 항은 음수다. 코드 y 좌변의 같은 항은 양수다. 상수 f·곡률 없음 조건에서도 코리올리 부호가 다르다(정적 판독, 실행 미확인). |
| 식 (10) · `raw/manuals/pdfs/1995_Hench.pdf, PDF 쪽 16 / 인쇄 쪽 6` | `\frac{\cos\varphi_0}{\cos\varphi}\frac{\partial}{\partial x'}\frac{\partial\zeta}{\partial t}\Biggl\{U-` | `src/gwce.F:1447` `JXAvg = CorifAvg*QY1Avg`; `src/gwce.F:1452` `&          +WSXAvg-BSXAvg+MXAvg-DispXAvg-BCXAvg+Tau0QXAvg`; `src/gwce.F:1473` `&              QX1Avg*(U1N1*FDX1+U1N2*FDX2+U1N3*FDX3)`; `src/gwce.F:1475` `&             +IFNLCAT*U1Avg*ESAvg/DT` | 해석: 문서의 x 발산 앞 ∂ζ/∂t는 중괄호 전체 밖에 있다. 코드는 U∂ζ/∂t만 다른 힘 항과 더한다. 코드는 이류·압력·바닥 항 전체에 수위 시간미분을 곱하지 않는다(정적 판독, 실행 미확인). |

전체 식 대조와 수정 기준은 [ADCIRC-theory-vs-code](../../../_staging/recovery/compare/ADCIRC-theory-vs-code.md)의 §1·§4를 참조한다.

## Relevance Tags

- solver: ADCIRC
- physics: hydrodynamics
- numerics: GWCE
- diagnostics: oscillation and stability interpretation
- failure mode: instability

## Transferability

Highly reusable for any future diagnostic work involving timestep, wet/dry behavior, or boundary-condition pathologies.

## Extraction Targets

- shortlist of parameters tied directly to GWCE weighting and stability
- first glossary of theory terms for the wiki

## Links

- related experiments: none yet
- related heuristics: none yet
- related failure patterns: none yet
