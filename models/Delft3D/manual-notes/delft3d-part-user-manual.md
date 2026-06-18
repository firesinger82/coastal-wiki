---
title: "Delft3D-PART User Manual — 입자추적(random walk) 지배방정식·oil/leeway process·입력파일 reference"
model: Delft3D
doc: Delft3D-PART_User_Manual.pdf
canonical_source: manual
citation_status: verified
verification_method: "Delft3D-PART_User_Manual.pdf pdftotext -layout 직접 추출 후 TOC + 핵심 기술 장 페이지 인용. Ch 2 개념(random walk·Monte Carlo, p.5-7), Ch 4 numerical/settling defaults(p.25-26·37), Ch 6 Conceptual model 지배방정식 eq.6.1-6.30(p.90-105), Ch 7 Algorithmic eq.7.1-7.5(p.108-109), Ch 6.7 data requirements(p.106-107), Appendix A 입력파일 포맷(p.112-113) 페이지 인용. 본문 페이지는 매뉴얼 인쇄 footer 'N of 128' 기준"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
  - models/Delft3D/source-analysis/delft3d_part.md
  - models/Delft3D/manual-notes/delft3d-manuals-overview.md
---

# Delft3D-PART User Manual

> Deltares Delft3D-PART(Particle Tracking, mid-field water quality + oil spill) 사용자 매뉴얼. random walk 입자추적의 지배방정식(분산계수·연직 k-L 모델·oil weathering·leeway)과 입력파일 reference를 페이지 인용으로 정리. 소스코드 관점은 [[delft3d_part]]와 상보.

## 0. 문서 정체

| 항목 | 값 |
|---|---|
| 제목 | Delft3D-PART, User Manual — *Simulation of mid-field water quality and oil spills, using particle tracking* (표지, p.표지) |
| 제품군 | D-Water Quality / Delft3D suite (p.표지) |
| Version | 3.0, Revision 80761 (p.표지) |
| 날짜 | 3 May 2026 (p.표지) |
| 발행 | Deltares, Boussinesqweg 1, 2629 HV Delft, NL (p.판권) |
| 분량 | 138p PDF / 본문 footer "N of 128" 체계 |
| 상태 | 표지에 "DRAFT" 워터마크(추출 텍스트 상 `T/AF/DR` 잔재) |

추출 시 `Internal Error: xref ... reconstruct` 경고가 있었으나 본문은 정상 추출됨.

## 1. TOC (장별 페이지)

| 장 | 제목 | p. |
|---|---|---|
| 1 | A guide to this manual | 1 |
| 2 | Introduction to Delft3D-PART | 5 |
| 3 | Getting started (Delft3D-MENU·coupling·PART-GUI) | 10 |
| 4 | Graphical User Interface (data groups·process params) | 18 |
| 5 | Tutorial (Case 1 Tracer / Case 2 Oil) | 50 |
| **6** | **Conceptual model (지배방정식)** | **90** |
| **7** | **Algorithmic implementation (advection·dispersion scheme)** | **108** |
| — | References | 110 |
| **A** | **Input files Delft3D-PART** | **112** |
| B | Advice on modelling sedimentation | 125 |

§4 세부: Hydrodynamics(4.3, p.19), Substances/Tracers·Oil(4.4, p.21), Time frame(4.5, p.23), Numerical params(4.7, p.25), Instantaneous/Continuous releases(4.8-4.9, p.27/30), Process params: decay·sed/erosion·physical·oil(4.10, p.34-44), Output(4.12, p.45).
§6 세부: random walk 원리(6.2, p.91), Dispersion coeff(6.3, p.91), 3D flow field(6.4, p.95), Oil spill module(6.5, p.96), Leeway(6.6, p.103), Data requirements(6.7, p.106).

## 2. 개념 (Ch 2, p.5-7)

- Delft3D-PART = **Delft3D suite 유일의 stochastic 모델**. 용존/입자성 물질을 다수의 discrete particle로 표현, random-walk(Monte Carlo) 기반 (Rubinstein 1981) (p.5, p.7).
- 적용 범위: **mid-field (200 m – 15 km)**, 순간/연속 방류, plume(예: oil spill), salt·bacteria·rhodamine dye·oil·BOD 등 보존성/1차 감쇠 물질 (p.5). → "Mid-field Water Quality module"라고도 불림.
- 입자 위치는 advection + diffusion/dispersion(random) + settling으로 변함. 입자 질량은 decay(1차)·evaporation(oil)으로 변함 (p.7).
- 모듈: **Tracer**(보존성/1차 감쇠), **Oil spill**(floating + dispersed 분율), specialised(agent-based 생태, 예: 어류 유생) (p.5, p.90). unstructured grid(D-Flow FM)에서 oil 3D·agent-based는 미검증/미구현 (p.90).
- 농도 산출: hydrodynamic segment 또는 **zoom grid**(임의 위치 직사각 counting grid, HD segment보다 통상 훨씬 작음) 내 입자 수 카운팅 (p.7).
- 시간규모 제약: 정확도(다수 입자) 위해 통상 **수 주 이내** (p.5).

## 3. 지배방정식 (Ch 6, Conceptual model)

### 3.1 Random walk 2-step (§6.2, p.91)
매 time step: (1) advection step (저면/표면 전단응력, 흐름 + 바람), (2) random walk step (크기·방향이 horizontal/vertical dispersion에 연계된 확률과정).

### 3.2 수평 분산 — 시간의존 (§6.3.2, p.91-92)
kinetic gas theory(Csanady 1973)에서 출발. Lagrangian 상관계수 $\langle \vec v(0),\vec v(\tau)\rangle = |v_0|^2 e^{-\tau/t_L}$ (eq.6.2) → 확산계수

$$E = v_0^2 t_l\,(1-\exp(-t/t_l)) \quad (6.3)$$

극한이 $E=at$(큰 $t_l$)와 $E=a$(작은 $t_l$). PART는 그 사이 멱지수 $0<b<1$로 fit:

$$D_{x,y} = a\,t^{b} \quad (6.4)$$

- $a,b$는 캘리브레이션 계수 (Bent et al. 1991). $t$는 해당 입자 방출시각 $t=0$부터 측정 (p.92).
- 3D 모델이라 dispersion coeff는 작음(order 1 m²/s) (p.92).
- 감도: $a$는 단시간, $b$는 장시간 범위 지배 (§6.7, p.106).

### 3.3 저면 전단응력·침강 (§6.3.2, p.92-93)
$$\tau_b = \frac{\rho g(u^2+v^2)}{C^2} \quad (6.5)$$
($C$=Chézy). $\tau_b<\tau_{cr,sed}$이면 입자 부착(sedimentation, 저면에 별도 sediment layer 생성); $\tau_b>\tau_{cr,sed}$이면 반사; $\tau_b>\tau_{cr,ero}$이면 퇴적 입자 즉시 재부유 (p.92-93).

농도의존 침강속도:
$$v_s = c^{\,n}\!\left(A_0 + A_1\sin\frac{2\pi(t+\phi)}{T}\right) \quad (6.6)$$
$c$=국지농도, $n$=농도의존 지수($n=0$이면 단순 sin), $A_0$ 비주기성분, $A_1$ 진폭, $T$ 주기[h], $\phi$ 위상[h]. $v_s<0$이면 입자 상승 (p.93).

### 3.4 연직 분산 — k-L 모델 (§6.3.3, p.93-94)
$$D_z = \frac{c_\mu^{1/4} L\sqrt{k}}{\sigma_C} \quad (6.7)$$
- $c_\mu\approx0.09$ (Rodi 1984), $\sigma_C=0.7$ (Prandtl-Schmidt, 열·염 수송).
- Bakhmetev(1932) mixing length: $L=\kappa(H-Z)\sqrt{Z/H}$, $Z=-(z-\zeta)$ (eq.6.8), $\kappa=0.41$. **Z는 아래방향**(표면 0, 저면 H).
- TKE 선형 프로파일 $k=k_b(Z/H)+k_s(1-Z/H)$ (eq.6.9); $k_b=u_{*b}/\sqrt{c_\mu}=\tau_b/(\sqrt{c_\mu}\rho_0)$, $k_s$ 동형(wind stress) (eq.6.10).
- 전단응력: $\tau_b = g\rho_0|v|^2/C_{2D}^2$, $\tau_w=\rho_a C_d|w|^2$ (eq.6.11). 기본값 $g=9.81$, $\rho_a=1.25$ kg/m³, $C_{2D}=50$ m^{1/2}/s, $|w|$=10 m 풍속.
- 합성 k-L 식 (eq.6.12):
$$D_z(z') = \frac{\kappa}{\sigma_C}H(1-z')\sqrt{z'}\sqrt{u_{*b}^2 z' + u_{*s}^2(1-z')},\quad z'=Z/H$$
- **공간의존 $D_z$ 미사용** (추가 stochastic drift term 회피). 표면·저면 입자 축적 방지를 위해 depth-averaging (p.94):
$$\bar D_z = \frac{\kappa H}{\sigma_C}\left[\frac{u_{*b}}{6} + \pi\frac{u_{*s}}{16}\right] \quad (6.13)$$
성층 효과 반영을 위해 depth-averaged 값에 선형 scale 허용.

### 3.5 3D flow field — 2DH 보정 프로파일 (§6.4, p.95-96)
2DH FLOW에 연직 프로파일 중첩("2.5 DH" 모드):
- 저면 전단 **로그 프로파일**: $v_z = C\ln\!\big(\tfrac{H-Z}{Z_0}+1\big)\times v$ (eq.6.14), 정규화 $C$ (eq.6.15). 조도길이 $Z_0\sim$ 2 cm (p.95).
- 바람 **포물선 프로파일**: $v_z = \alpha\big[3(1-\tfrac{Z}{H})-2(1-\tfrac{Z}{H})\big]W$ (eq.6.16), wind drag $\alpha\sim0.03$; 연직적분 0(평균 바람효과는 2DH 장에 이미 포함되어야 함) (p.96).

## 4. Oil spill module (§6.5, p.96-102)

floating ↔ dispersed 2상. Dispersion(entrainment)은 wind wave breaking → Delvigne et al.(1986). Evaporation은 1차 감쇠 또는 Fingas (p.96).

| process | 식 | p. |
|---|---|---|
| 초기 반경 (Fay-Hoult) | $R_0=\frac{k_2^2}{k_1}\big(\frac{V_0^5 g(\rho_w-\rho_0)/\rho_w}{\nu_w^2}\big)^{1/12}$ (6.17); $k_1{=}1.14,k_2{=}1.45$ | 96 |
| 표면 oil 바람 advection | drift $=C_{wd}(V_w-V_f)$ (6.18); floating oil에만 적용 | 97 |
| 편향각(deflection) | 풍향 대비 oil advection 각, 위도의존 상수, 통상 0–25°(북반구 우측) | 97, 106 |
| 증발 (Fingas log) | $\%evap=[.165(\%D)+.045(T-15)]\ln t$ (6.19) | 98 |
| 증발 (Fingas √, diesel류) | $\%evap=[.0254(\%D)+.01(T-15)]\sqrt t$ (6.20) | 98 |
| 휘발분 1차증발 | $\frac{dF_v}{dt}=-\big(\frac{F_{vol}-F_v}{1-F_v}\big)k$ (6.21); $F_{vol}-F_v<0$이면 0 | 98 |
| 점성-증발분 | $\eta=\eta_0 e^{C_v F_v}$ (6.22); $C_v{=}1$(경질, $\nu<500$cSt)/$10$(중질) | 98-99 |
| Entrainment (Delvigne-Sweeney) | $Q=5.08\cdot10^{-8}C_0 S_{cov}D_e^{0.57}F_{wc}$ (6.24); white-cap 풍속 임계 5 m/s | 99-100 |
| ↳ droplet 적분형 | $Q(\delta)=C''D_e^{0.57}F_{wc}N(\delta)\delta^3$, $N(\delta)=N_0\delta^{-2.3}$, $D_e=0.0034\rho_w gH_0/\sqrt2$, $H_0=0.243U_w^2/g$, $F_{wc}=f_w/t_p$, $t_p=8.13U_w/g$, $f_w=\max(0,0.032(U_w-5))$ (6.23); $\delta_{max}\approx70\,\mu$m (NOAA 1994) | 99-100 |
| Emulsification (Mackay) | $\tilde F_{wc}=C_1(U_w+1)(1-\frac{F_{wc}}{C_2})^2$ (6.25); $C_1{=}2\cdot10^{-6}$(유화성)/0, $C_2{=}0.25$(경질)/0.75(중질, 500cSt 기준 전환) | 101 |
| ↳ 점성 변화 | $\frac{\mu}{\mu_0}=e^{2.5F_{wc}/(1-C_3 F_{wc})}$ (6.26), $C_3{=}0.65$ (Reed 1989) | 101 |
| ↳ 증발 억제 | $F_{ew}=\frac{C_2-F_{wc}}{C_2}F_{vol}$ (6.27); 함수율 최대 도달 시 증발 정지 | 102 |
| 밀도(에멀전) | $\rho_{em}=F_w\rho_w+(1-F_w)\rho_{oil}$ (6.28); ADIOS 형식(증발분·온도 의존 제외) | 102 |
| Sticking | 0–1 난수 < sticking probability이면 육지/저면 부착 | 102 |

dispersion rate 산정 3방식: ① 일정 분율/일(바람·파 무관), ② Delvigne-Sweeney(임계 5 m/s), ③ Delvigne-Sweeney + 사용자정의 임계 (p.99). 침강은 통상 음(부력); oil weathering(산화·박테리아 분해)은 1차 decay로 모사 (p.102).

## 5. Leeway modelling (§6.6, p.103-105)

- **Delft3D FM 2026.02 이후** 제공. PIW(person in water)·SAR 객체 이동. 바람(10 m)·파에 의한, 주변류(0.3–1.0 m 수심) 대비 상대 운동. 기반: Allen & Plourde (1999); 객체별 leeway factor는 AMSA(2022) National SAR Manual (p.103).
$$\text{lw\_speed} = \alpha\cdot U_s + U_m \quad (6.29)$$
$$\text{DW\_dir} = \pm\,\text{Divergence} \quad (6.30)$$
$\alpha$=풍속 multiplier(SI에서 fraction으로 해석), $U_m$=leeway modifier[m/s]. divergence는 +/−/0 세 그룹으로 입자 분리 모사 (p.104-105). 두 옵션: 파라미터 직접 지정 / 표준 표 선택 (p.105, §A.4).

## 6. Algorithmic implementation (Ch 7, p.108-109)

- transport = advection + (wind + horizontal/vertical dispersion), 별도 수치 scheme (p.108).
- **Advection** (§7.2): 선형보간 HD 속도장의 **해석적 적분**(analytical integration). 셀 경계 속도 선형보간 + 연직 프로파일. mass-conservation of water 보장, 폐(육지)경계는 속도 점근적 소멸로 자동 처리, 개경계 통과 입자는 제외 (p.108).
  $$x(t+\Delta t)=x(t)+\int_0^{\Delta t}\!\tfrac{dx}{dt}dt \quad (7.1)$$
  $\alpha_x=C(\sigma)\frac{Q^+-Q^-}{V}$, $\beta_x=C(\sigma)\frac{Q^{+/-}}{V}$ (7.2); path acceleration 무시 $ds/dt=1$ (7.3); 부피보존 $\partial_x(\alpha_x x+\beta_x)=0$ (7.4)는 FLOW 결합 시 만족 (p.108-109).
  - **유일 advection scheme = option 1** (입력 reference, p.113).
  - structured grid: 셀 단위 추적. unstructured(D-Flow FM): 셀을 삼각형으로 분해 후 부피보존적으로 flow field 분배 (§7.2.1, p.109).
- **Dispersion** (§7.3): Euler-type. 2DH 모드 wind advection도 이 scheme. white noise(균등분포, 평균 0, [-1,+1]) 기반, 시간당 최대 변위
  $$\Delta S = \sqrt{6 D\,\Delta t} \quad (7.5)$$
  isotropic(선호 방향 없음), 경계는 순수 reflective (p.109).

## 7. 수치/물리 파라미터 기본값 (Ch 4)

### 7.1 입자 수 — 농도 해상도 (§4.7.1, p.25-26)
정확도 ∝ √(입자 수). 최소 농도 해상도:
$$C_{min}=\frac{m_{particle}}{A_{cell}h_{layer}}=\frac{M_{total}}{N_{total}A_{cell}h_{layer}} \quad (4.1)$$
예: $M{=}10000$ kg, $A{=}200$ m², $h{=}4$ m, 목표 $C_{min}{=}0.001$ kg/m³ → $N\ge12500$ (p.25-26). 입자 수 > 1000이면 warning (p.113).

### 7.2 연직 분산 옵션 (§4.7.2, p.26)
- *Depth averaged algebraic*: 식(6.13) 기반, 전수심 함수(위치별 변동).
- *Constant dispersion*: 시공간 일정(사용자 상수). → 입력 reference에서 **option 0(constant)이 권장**, option 1이 k-L (p.114).
- Scale factor 기본 **1.0** (p.26).

### 7.3 침강속도 도메인 (§4.10.2, p.37, Domain 표)
| 파라미터 | 하한 | 기본 | 단위 |
|---|---|---|---|
| 농도의존 지수 $n$ | 0 | 0 | - |
| grid refinement factor | 0 | 1 | - |
| $A_0$ value | 0 | 0 | m/s |
| $A_1$ value | 0 | 0 | m/s |
| Period $T$ | 0 | 0 | hours |
| Phase $\phi$ | 0 | 0 | hours |
| $V_{min}$ | 0 | 0 | m/s |
| $V_{max}$ | 0 | 1000 | m/s |

계산 $v_s\notin[V_{min},V_{max}]$이면 경계값으로 reset; breakpoint는 $A_0,A_1,T,\phi,V_{min},V_{max}$ 동일해야 (p.37).

## 8. 결합·입출력 (Ch 3, Appendix A)

- HD 결합: Delft3D-FLOW 또는 D-Flow FM. sigma-/Z-layer 지원; sigma+Z 조합은 미검증(기본 거부, 키워드로 override) (p.90, p.113). 조석주기 반복 가능(예: 12 h 주기로 36 h 모사, Fig.3.4 p.12), 연직 aggregation 가능(예: 10→5층, Fig.3.5 p.13).
- 핵심 파일: `<*.mdp>`(Master Definition Part), `<*.inp>`(ASCII 입력), `<*.hyd>`(HD database), `<*.ini>`(oil 초기조건, §A.5), 그리드 `*.lga`/`*.cco`(structured)·`*-waqgeom.nc`(unstructured) (p.22-23, p.112-113). 보고서 `<*.out>` — 화면에 에러 미출력, 'ERROR'(대문자) 검색 권장 (p.8, p.112).

### 입력파일 포맷 (§A.2, p.112-113)
- free-format. `;`이후 주석, 빈 줄 무시, 문자열 따옴표 필수. FORTRAN 다중 leading-zero 회피 (p.112). 기호: `-`(새 줄), `*`(직전 `-`줄과 같은 줄), `∆`(선택). time-function은 breakpoint(첫=시작, 마지막=종료) + 값, 기본 선형보간(동일 시각 2레코드로 block 모사) (p.112).
- verbatim 라인:
  - `'V3.66.00'` — 버전 식별, 변경 금지(불일치 시 실행 안 됨); run id 5×40자 문자열 (p.113).
  - 모델 타입: `1 - tracer`(기본), `4 - oil model`; 2/3/5는 obsolete (p.113).
  - `<type> tracks(0/1) extra_output(0/1) sed/erosion(0/1)` — tracks=1이면 매 step 출력(입자 多시 거대 파일, >1은 multiplier; GUI 미지원), 3번째 정수는 미사용(필수), 4번째 sed/erosion on(1)/off(0) (p.113).
  - `num.scheme time_step(s)` — scheme=1 only, time step `0`=flow time step (p.113).
  - `vert.disp option scale disp_coeff` — `0=constant`(권장)/`1=depth averaged(k-L)` (p.113-114).
  - sigma-z: 키워드 `allow-sigma-z-layers` / `no-sigma-z-layers`(기본) (p.113).
- 추가 절: A.3 oil module constants(p.120), A.4 leeway parameters(p.121), A.5 oil 초기조건 파일(p.122), A.6 polygon 파일(p.123).

## 9. Data requirements / 감도 (§6.7, p.106-107)

HD database(가장 정확해야, dye 캘리브레이션), wind drag(이방성; Delft Hydraulics 경험상 문헌 권장 3%보다 **1% 다용**), wind field, deflection angle(0–25°, 위도의존), roughness length(권장 **2 cm**), 수평분산 $a,b$, 방출량(결과 선형 비례), 방출 시각·위치, oil constants(점성 유래 entrainment·sticking probability) (p.106-107).

## 10. 미커버 / 보완 필요

- §3·§4·§5 GUI 조작·튜토리얼(Friesian Tidal Inlet tracer/oil case)은 운영 절차이므로 식 외 상세 미전사 — 필요 시 p.50-89 재독.
- Appendix A.3-A.6(oil constants·leeway·ini·polygon)·Appendix B(sedimentation 가이드, p.125)의 구체 표는 본 노트에 절 식별만, 수치 전사 미수행. ⚠ 필요 시 해당 페이지 재추출.
- Fingas %D·droplet $N_0$·$C''$ 등 oil 캘리브레이션 상수의 구체 권장값 표는 본문 산문 서술 위주 — 정밀 적용 시 A.3 확인.
