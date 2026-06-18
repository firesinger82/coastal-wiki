---
title: "Delft3D-WAQ (D-Water Quality) User Manual — TOC·물질수지·process 식·numerical scheme reference"
model: Delft3D
doc: Delft3D-WAQ_User_Manual.pdf
canonical_source: manual
citation_status: verified
verification_method: "Delft3D-WAQ_User_Manual.pdf pdftotext -layout 직접 추출 후 전체 TOC(Ch1-11+부록 A/B) + 핵심 기술 장 페이지 인용. Ch8 mass balance·advection-diffusion(p.191-199), Ch9 process 식(coliform·DO/BOD reaeration, p.201-211), Ch10 numerical scheme/CFL(p.283-302), §1.5 tech specs(p.6), §4.7 file overview(p.49-50), §2.x integration options(p.17-18) 인용 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
---

# Delft3D-WAQ (D-Water Quality) User Manual — manual-notes

> D-Water Quality(DELWAQ 엔진)의 공식 사용자 매뉴얼. advection-diffusion-reaction 물질수지 개념, 기능군별(coliform·DO/BOD·영양염·식물플랑크톤 등) process 지배식, 그리고 24개 numerical integration scheme + CFL 안정성 조건을 페이지 인용과 함께 정리. 엔진 소스/process library 내부 구조는 [[delft3d_delwaq]]·[[delft3d_waq_process_library]]·[[delft3d_waq_kernel_integration]] 참조 — 본 노트는 **공식 매뉴얼의 물리장·process 식·numerical reference**에 집중.

## 0. 문서 정체

| 항목 | 값 | 출처 |
|---|---|---|
| 제목 | D-Water Quality, User Manual ("Versatile water quality modelling in 1D, 2D or 3D systems including physical, (bio)chemical and biological processes") | 표지 (p.표지) |
| 발행 | Deltares, Delft, The Netherlands. © 2026 | (p.판권) |
| 버전 / Revision | 2026.02 / Rev. 80941, 3 May 2026 | (p.표지) |
| 릴리스 대상 | Delft3D FM Suite 2026.02 / D-HYDRO Suite 2026.02 / SOBEK Suite 3.8.1 / WAQ Suite 2026.02 | (p.표지) |
| 분량 | PDF 391 p (본문 내부 footer 기준 "X of 375") | pdfinfo / footer |

문서는 두 진입 경로를 모두 다룬다: **SOBEK 경로(Ch 2)**와 **Delft3D 경로(Ch 3-7)**. 본 노트의 페이지 인용은 매뉴얼 footer의 "X of 375" 인쇄 페이지 번호를 사용한다.

기술 스펙(§1.5, p.6): 핵심 실행파일·버전 — `<delwaq.exe>` (전처리+실제 수질 시뮬레이션) v5.01.01, WAQ-GUI v3.32.00, PLCT(Processes Library Configuration Tool) v5.04.00, `<coup203.exe>`(수리 DB coupling) v2.48.09, process DB는 `<proc_def.dat>`/`<proc_def.def>` (§1.5 p.6).

## 1. 전체 목차 (장별 페이지)

| 장 | 제목 | p. |
|---|---|---|
| 1 | A guide to this manual | 1 |
| 2 | Introduction to D-Water Quality (SOBEK) | 11 |
| 3 | Introduction to D-Water Quality (Delft3D) — areas of application·coupling·utilities | 40 |
| 4 | Getting started (Delft3D) — start·working dir·WAQ-GUI·steps·data flow | 42 |
| 5 | Graphical User Interface — PLCT(§5.1 p.52)·hydrodynamic coupling(§5.2)·WAQ-GUI input(§5.3) | 52 |
| 6 | Running and post-processing (Delft3D) — pre-proc 검증·`.lst`·`.lsp`·output files | 109 |
| 7 | Tutorials (tut_fti_waq free-surface·SOBEK sewer overflow) | 116 |
| **8** | **Conceptual description** — mass balance·spatial schematisation·advection-diffusion·boundary | **191** |
| **9** | **Principles of water quality modelling** — 기능군별 process 식 | **200** |
| **10** | **Numerical aspects** — dispersion·discretisation·numerical schemes | **283** |
| 11 | Special features — FLOW built-in coupling·domain decomposition·z-model 변환·1D–3D coupling·water age/CART | 306 |
| Ref | References | 324 |
| A | File descriptions — overview·format(`.obs`,`.dmo`,`.tim`,`.dsp`,`.qin`,`.q3d` 등) | 331 |
| B | Standard substance files (salinity/tracers·basic coliform 등) | 344 |

(전체 TOC: 매뉴얼 Contents p.iii–ix, 본문 라인 인용 위치 확인)

§5.3 WAQ-GUI 입력 data group (p.69–108): Description·Hydrodynamics·Dispersion·Substances·Time frame·Initial conditions·Boundary conditions·Process parameters·Numerical options·Discharges·Observation points·Output options·Saving scenario·sediment grid 추가 — 입력 구성 단위.

## 2. 물질수지 개념 (Ch 8)

### 2.1 시간전진 물질수지 (§8.2, p.191)
각 계산셀·각 state variable에 대해 한 시간스텝 전진:
$$M_i^{t+\Delta t} = M_i^{t} + \Delta t\left(\tfrac{\Delta M}{\Delta t}\right)_{Tr} + \Delta t\left(\tfrac{\Delta M}{\Delta t}\right)_{P} + \Delta t\left(\tfrac{\Delta M}{\Delta t}\right)_{S} \quad (8.1)$$
- 항: 시작질량 $M_i^t$, 종료질량 $M_i^{t+\Delta t}$, 수송 변화 $(\Delta M/\Delta t)_{Tr}$, process(물리·(생)화학·생물) 변화 $(\Delta M/\Delta t)_{P}$, source(waste load·하천 유입) 변화 $(\Delta M/\Delta t)_{S}$ (§8.2 p.191).
- **본질적으로 질량보존**: 한 셀에서 흐름으로 빠진 질량이 인접 셀에 양(+)으로 그대로 들어감 (§8.2 p.191). 기본 원리는 state variable·셀 수에 무관 — 차이는 Eq.(8.1)을 푸는 횟수뿐 (§8.2 p.191).
- 흐름·연직 dispersion은 수리모델(Delft3D-FLOW / D-Flow FM)에서 도출, **수평 dispersion은 사용자 입력**(§5.3.3) (§8.2 p.191–192).

### 2.2 공간 schematisation (§8.3, p.192–193)
- 수계를 작은 box(=computational cell)로 분할; 각 셀은 volume + 차원(Δx,Δy,Δz)으로 정의, 직사각이면 어떤 형상도 가능 (p.192).
- 셀 1..N 고유번호, 공유면(shared surface area) 1..Q는 **exchange**로 식별 — exchange는 공유하는 두 셀 번호로 정의 (p.192–193).
- exchange table(Figure 8.2 예: 11셀+5경계셀, 22 flow)은 "From","To","From−1","To+1","Flow" 컬럼; **"From−1"/"To+1"은 일부 고차 scheme이 쓰는 2차 연결**임 (p.193). 경계셀은 음수 번호.

### 2.3 Advection-diffusion 식 (§8.4, p.194–197)
기본형 $\partial M/\partial t = \text{advection}+\text{dispersion}+\text{source}$ (8.2, p.194).

| 항 | 식 | 출처 |
|---|---|---|
| Advective transport | $T^{A}_{x_0} = v_{x_0}\,A\,C_{x_0}$ [g/s] | §8.4.1 p.194 |
| Dispersive (Fick) | $T^{D}_{x_0} = -D_{x_0}\,A\,(\partial C/\partial x)_{x_0}$ | §8.4.2 p.194 |
| Source (유입) | $T_{src}=Q_{src}\,C_{src}$, $Q_{src}>0$ (8.3) | §8.4.3 p.195 |
| Source (취수) | $T_{src}=Q_{src}\,C_{i}$, $Q_{src}<0$ — **취수 시 주변 농도 $C_i$ 사용, 사용자 source 농도 무시** (8.4) | §8.4.3 p.195 |

3D advection-diffusion-reaction 식:
$$\frac{\partial C}{\partial t}+v_x\frac{\partial C}{\partial x}-D_x\frac{\partial^2 C}{\partial x^2}+v_y\frac{\partial C}{\partial y}-D_y\frac{\partial^2 C}{\partial y^2}+v_z\frac{\partial C}{\partial z}-D_z\frac{\partial^2 C}{\partial z^2}=S+f_R(C,t)\quad (8.6)$$
($S$=waste load, $f_R$=process/reaction; §8.4.4 p.196–197). Process는 PDE 형태 $(\partial C^1/\partial t)_R=f_R(C^1,...,C^N,t)$로 쓸 수 있는 것만 — 화학적 평형동역학(equilibrium kinetics)은 제외, 느린 화학반응만 표현 가능 (p.197). 유한체적법은 Δx, A(=Δy·Δz), Δt 크기에 정확도가 좌우됨 (p.196).

### 2.4 경계조건 (§8.5, p.198–199)
- **Closed boundary**: flow·dispersion 항상 0, 농도 입력 불필요 (§8.5.1 p.198).
- **Open boundary**: 해 도출에 필수. 모든 substance 농도·dispersion 계수를 모든 시간스텝에 지정, flow는 수리모델에서 자동 (§8.5.2 p.198). downstream 경계 농도가 해에 영향 — central method면 마지막 셀과 경계의 평균이 계면 농도가 됨; 회피 옵션 (1) 경계에서 국소 upwind advection (2) 경계 dispersive transport 억제 (§8.5.2 p.198).
- **Thatcher-Harleman time lag** (§8.5.3 p.198–199): 유출→유입 전환 시 마지막 유출 농도에서 지정 경계 농도로 cosine 천이:
$$C(t_0+t)=C(t_0)\Big(0.5+0.5\cos\tfrac{\pi t}{2T}\Big)+C_B(t)\Big(0.5-0.5\cos\tfrac{\pi t}{2T}\Big)\quad (8.7)$$
$T$=time lag. 권장값: 하구 1–6 h, polder 약 5 day (p.199).

## 3. 기능군과 process 식 (Ch 9)

substance는 **functional group**으로 조직(Figure 9.1, p.200): Continuity·Salinity-Chloride·Temperature·Conservative/Decayable Tracers·Bacteria·DissolvedOxygen·BOD/COD·Methane·Nutrients(NO3 NH4 PO4 Si, AAP/VIVP/APATP/OPAL)·Organic Matter(POC/PON/POP/POS, DOC/DON/DOP/DOS)·Phytoplankton·Grazers·Heavy Metals(As Cd Cr Cu Hg Ni Pb V Zn)·Organic micro-pollutants·Iron·Sulphur, 그리고 Sediment 층(§9.1 p.200).

### 3.1 보존성·온도 의존 (§9.2–9.3)
- 보존 tracer 최대 5개; **Continuity** = 모든 water source에 1 g/m³ 부여 → 시뮬레이션 내내 1 g/m³ 유지되어야 함, 이탈 시 누락된 water source 또는 수치 불안정 신호 (§9.2 p.200–201).
- Decayable tracer(5개): 1차 감쇠 $C(t)=C_0 e^{-kt}$, 방사성(반감기 $k=\ln2/t_{1/2}$)·소독제 모사 (§9.2 p.201).
- **반응속도 온도의존(거의 모든 process 공통)**: $k=k_{20}\,k_T^{(T-20)}$ (9.1, §9.3 p.201). $k_T$ 통상 1.01–1.10; 1.04면 10°C에서 20°C 속도의 68%, 1.07이면 10° 변화마다 배증/반감 (p.201).

### 3.2 Coliform 박테리아 (§9.4, p.202–203)
substance: TCOLI·FCOLI·ECOLI·ENCOC, 단위 **MPN/m³** (1 MPN/m³ = 1×10⁻⁴ MPN/100ml) (§9.4.2 p.203). 가정: 수주(water column)에만 존재·퇴적/재부유 없음, 성장 없음, 1차 동역학 사망, salinity·UV로 사망률 가산 증가 (p.203). Mancini(1978) 식:
$$R_{mrt}=k_{mrt}\,C_x,\quad k_{mrt}=(k_{mb}+k_{mcl})\,k_{tmrt}^{(T-20)}+k_{mrd}$$
$$k_{mcl}=k_{cl}\,C_{cl},\quad k_{mrd}=k_{rd}\,f(I)$$
$k_{mb}$=기본사망률, $k_{cl}$=염소 관련 상수, $k_{rd}$=복사 관련 상수, $I$=수면 일일 UV 복사 [W/m²] (§9.4.3 p.203). 저온에서는 유의한 사망 없음 (p.204).

### 3.3 용존산소·BOD (§9.5, p.204–211)
광합성/광물화 화학량론: 유기탄소 1 g당 O₂ 2.67 g (=32/12) (§9.5.1 p.204). DO 질량수지 = loads + transport + reaeration + net primary production (9.3, p.206). Streeter-Phelps(1925) DO sag 개념 (p.204).

**Reaeration (§9.5.3 p.209)** — 포화-실측 DO 차에 선형:
$$R_{rear}=k_{lrear}\,(C_{oxs}-C_{ox})/H,\qquad k_{lrear}=\frac{a\,v^{b}}{H^{c}}+d\,W^{2}$$
$a,b,c,d$=**11개 reaeration 옵션별 계수**, $v$=유속, $W$=10 m 풍속, $H$=수심, $C_{oxs}=f(T,C_{cl}\text{ 또는 SAL})$ (포화농도; 염소 또는 salinity 2옵션) (§9.5.3 p.209). 입력 keyword(`.lsp` 보고): `[SWRear]` 정수교환식 switch (1–11), `[KLRear]` 전달계수, `[TCRear]` 온도계수 — process `[RearOXY]`이 flux `[dREAROXY]` 생성 (p.209, .lsp 발췌 라인 6968–7151).

Diurnal production: $R_{gpmax}=48\,R_{gpa}/(t_2-t_1+DL)$ (p.209).

### 3.4 그 외 기능군 process 식 위치
영양염·detrital OM·electron-acceptor §9.7.3 (p.236), 식물플랑크톤 §9.8.3 (p.250, DYNAMO/BLOOM은 [[delft3d_waq_algae_models]]), primary consumption(grazer) §9.9.3 (p.257), 중금속·organic micro-pollutant §9.10.3 (p.263), sediment §9.11.3 (p.271). SOBEK 전용 사전정의 set: Simple oxygen(Streeter-Phelps) §9.12.1 (p.273), Simple eutrophication §9.12.2 (p.276).

## 4. Numerical aspects (Ch 10) — integration scheme reference

### 4.1 Dispersion 도출 (§10.1, p.283)
dispersion 계수는 FLOW 격자로 풀리지 않은 **모든 미해소 수송**을 의미(분자확산 ≫ 아님). 3D식을 y,z에 적분 → 1D 단면평균식 (10.2, p.283): $\partial(AC)/\partial t=\partial/\partial x[D\,\partial(AC)/\partial x]-\partial/\partial x\iint v_x C\,dy\,dz+Af+AS$. 1D/2D는 dispersion이 크므로 주의, 3D는 미해소 eddy 항이 주 (p.283).

### 4.2 시간이산화·θ (§10.4.2, p.291)
일반식 $\dfrac{c^{t+\Delta t}-c^{t}}{\Delta t}+\text{H.O.T.}=(1-\theta)(Lc)^t+\theta(Lc)^{t+\Delta t}$ (10.18). time-splitting factor θ:

| θ | scheme | 성질 |
|---|---|---|
| 0.0 | explicit (Euler explicit) | positive definite, 단 CFL 필요 |
| 1.0 | fully implicit (Euler implicit) | positive definite, 무조건 안정 |
| 0.5 | semi-implicit (Trapezoidal) | 무조건 안정이나 진동·음수 농도 → 수질모델 비선호 |

θ≥0.5이면 무조건 안정; θ<0.5는 안정조건 필요. positivity는 θ=0 또는 1만 보장 (§10.4.2 p.291). 수평·연직에 서로 다른 θ scheme 사용 가능 (p.291).

**CFL 안정조건 (explicit, θ=0)** (§10.4.2 p.291):
$$\Delta t < \frac{V_i}{\sum_{j=1,n} Q_{i\to j}}\quad (10.19)$$
"한 시간스텝에 한 격자셀에서 교체되는 물의 부피가 항상 셀 부피보다 작아야 한다" — 모든 셀에 동시 충족. dispersion 항에도 안정조건 (10.20) 존재; 연직 dispersion 항이 얕은 물의 작은 연직 mesh에서 커져 3D는 거의 항상 연직 implicit 필요 (p.291). (GUI 표현: $\Delta t\le F\cdot V\!ol/\sum Q_{in}$, F=0.2~1.0, §2 p.18.)

**반응항·source항은 항상 explicit** 처리(복잡·비선형 허용); 1차 이산화(H.O.T. 없음), 단 Scheme 2(2nd-order Runge-Kutta)는 예외 (§10.4.2 p.291). 예외: 대형 취수(intake rate가 셀부피 대비 큰 경우)·시간스텝보다 짧게 변하는 waste load는 시간스텝 제약 발생 (p.291).

### 4.3 Numerical schemes 일람 (§10.5, p.294–301)
번호에 "구멍"이 있는 것은 삭제된 scheme 때문(특수상황/대형 3D 부적합) (p.294). 주요 scheme:

| Scheme | 내용 | 특성 | 출처 |
|---|---|---|---|
| 1 | Upwind explicit | 가장 robust, 1차, **CFL 필요**, 실무상 2D | §10.5.1 p.296 / 개요 p.294 |
| 5 | Flux Corrected Transport (FCT) explicit | 가장 정확(2차), **CFL 필요** | §10.5.3 p.297 / p.294 |
| 6–9,17,18 | Steady-state 해 | — | §10.5.4 p.297 |
| 10 | Implicit Upwind + direct solver | 2D 전용, CFL 불필요, scheme5보다 부정확 | §10.5.5 p.298 |
| 11 | 수평 Upwind, 연직 implicit central | 수평/연직 분리해 | §10.5.6 p.298 |
| 12 | 수평 FCT, 연직 implicit central | **3D 권장**(수평 정확+연직 central) | §10.5.7 p.298 |
| 13 | 수평 Upwind, 연직 implicit upwind | — | §10.5.8 p.299 |
| 14 | 수평 FCT, 연직 implicit upwind | — | §10.5.9 p.299 |
| 15 | Implicit Upwind + iterative solver | 수평·연직 모두 implicit, 빠름, 수치혼합 큼 | §10.5.10 p.299 |
| 16 | 수평 implicit upwind, 연직 central + iterative | 위와 유사, 연직 central | §10.5.11 p.300 |
| 19,20 | (삭제됨 — structured grid 전용) | — | p.294/301 |
| 21,22 | Local-theta FCT | scheme5 개선, 국소 explicit↔implicit 전환으로 극값 회피. **21=Salezac limiter, 22=Boris&Book limiter** | §10.5.13 p.301 |
| 23 | QUICKEST (실험적) | **2D 전용** (연직 미지원) | §10.5.14 p.301 |
| 24 | FCT + adaptive time-stepping | scheme5 개선, 국소 time step 축소로 **CFL 불필요·수리 DB와 동일 큰 스텝 가능**, drying/flooding 작은 부피 문제 해결. 단 substance별 추가 velocity/dispersion 불가(연직만 허용), "no dispersion if flow=0" 필수, 수평 dispersion=0 권장 | §10.5.15 p.301 |

**Rule of thumb (§10.5, p.295)**:
1. Scheme 15/16 → 매우 빠르나 수치 dispersion 클 수 있음
2. Scheme 21/22/24 → 빠르고 안정조건 없음, 정확도는 time step 의존
3. Scheme 12(3D)/5(2D) → 정확하나 CFL 충족 필요
4a. Scheme 1 → scheme5보다 덜 정확하나 robust(큰 스텝)
4b. Scheme 10 → 2D 전용, CFL 불필요

선택 고려: 정확도는 time step↑일수록↓(수치 dispersion); upwind=수치 dispersion, central=음수 농도 가능, implicit=gradient smoothing (p.295). σ-좌표의 인공 연직혼합은 §10.6 (p.302).

**Numerical sub-options (§2 p.18, §5.3.9)** — verbatim 권장값:
| switch | 권장 |
|---|---|
| flow=0이어도 dispersion 허용 (D>0) | YES |
| open boundary·lateral inflow에서 dispersion 허용 (D>0) | NO |
| 경계에서 upwind transport 강제 | YES |

## 5. 파일 구조 (§4.7, Appendix A)

| Module | Input | Output | 출처 |
|---|---|---|---|
| Delft3D-FLOW | `<*.mdf>` | `<com-*.dat>`,`<com-*.def>` | Table 4.1 p.49 |
| DIDO | `<*.grd>`,`<*.dwq>` | `<*.dwq>` | p.49 |
| Couple(`coup203`) | `<com-*.dat/.def>`,`<*.dwq>`,`<couplnef.inp>` | `<*.hyd>`,`<com-*.flo>`,`<com-*.vol>` 등 | p.49 |
| PLCT | `<*.0>` | `<*.sub>`,`<*.0>` | p.49 |
| WAQ-GUI | `<*.hyd>`,`<*.sub>`,`<*.scn>`,`<*.stt>` | `<*.scn>`,`<*.inp>`,`<*.stt>` | p.49 |
| Compute WQ(`delwaq`) | `<*.inp>`,`<com-*.flo/.vol>` 등 | `<*.lst>`,`<*.lsp>`,`<*.mon>`,`<*.ada/.adf>`,`<*.hda/.hdf>`,`<*.his>`,`<*.map>` | p.50 |

- 시나리오는 `<*.scn>`(scenario) + `<*.inp>`(input file, 전처리기·엔진이 사용) 쌍으로 저장 (§6 p.46/p.50). `<*.inp>` 수동 편집은 별도 매뉴얼 'Documentation of the input file' (§3.4 p.6, §5.x p.~110).
- Appendix A.2 file format: `.obs`(observation p.335)·`.dmo`(observation area p.336)·`.tim`(time-series p.336)·`.dsp`(dispersion array p.340)·segment function·`.qin`/`.q3d`(QUICKIN 2D/3D p.342–343).
- 실행 출력: pre-processing 입력검증 `<*.lst>`(list)·`<*.lsp>`(report, 활성 process·input item·flux 진단 포함) (§6.1 p.110).

## 6. 기존 노트와의 경계

- **엔진 소스/적분 커널 내부 동작** → [[delft3d_waq_kernel_integration]], [[delft3d_delwaq]] (source-analysis). 본 노트의 scheme 표는 매뉴얼이 사용자에게 노출하는 관점.
- **Process Library 구조·proc_def** → [[delft3d_waq_process_library]] (source). 본 노트는 매뉴얼이 기술한 process 지배식(reaeration·coliform mortality 등)에 집중.
- **조류(BLOOM/DYNAMO) 모델** → [[delft3d_waq_algae_models]] (§9.8 식물플랑크톤 식 위치만 본 노트에 기록).
- 매뉴얼 세트 전반 위치 → [[delft3d-manuals-overview]].
- 상세 process 식 전체·계수 DB는 본 매뉴얼이 반복적으로 가리키는 **Technical Reference Manual (Deltares 2026c)** 별도 문서 (§8.2 p.191 등). ⚠ 본 노트는 User Manual만 검수 — TRM 식은 source-needed.
