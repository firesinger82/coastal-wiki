---
title: "XBeach Master Manual (Deltares 2015) — 물리 정식화 + params.txt keyword reference"
model: XBeach
doc: XBeach_manual_master.pdf
canonical_source: manual
citation_status: verified
verification_method: "XBeach_manual_master.pdf pdftotext -layout 직접 추출(/tmp/xbeach-master-manual.txt, 145p) 후 TOC(p.1-3) + Ch2 Processes and model formulation(p.6-41) + Ch3 Boundary conditions(p.43-48) + Ch4 Input description(p.49-92) + Appendix B Advanced coefficients(p.103-113) 페이지 인용. 지배방정식(wave action 2.1, GLM-SWE 2.50, 비정수압 q 2.60-2.64, groundwater 2.65-2.75, A-D sediment 2.76, bed update 2.110)·dissipation/roller 식·params.txt 구조·physical-process 스위치 표·grid/wave-bc keyword 표·time/wave-dissipation/roller/sediment/morphology 기본값 표 인용."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/XBeach/README.md
---

# XBeach Master Manual (Deltares 2015)

> XBeach 공식 마스터 매뉴얼 145p의 객관 정리. 표지·완전 TOC(장별 페이지)·핵심 물리 정식화(파동작용·roller·GLM 천수방정식·비정수압·지하수·sediment·morphology·avalanching·ship)·params.txt 구조·keyword/default reference. 기존 example 참조 노트([[01-local-manual-stack]]·[[02-delilah-reference]]·[[03-holland-coast-reference]])와 구분되는 매뉴얼 물리+parameter 레이어. source-analysis 다수와 대응.

## 1. 문서 정체

| 항목 | 값 |
|---|---|
| 제목 | XBeach Manual — Model description and reference guide to functionalities (표지, p.i) |
| 발행처 | Deltares, UNESCO-IHE, TU Delft (p.i) |
| 저자 | Dano Roelvink, Ap van Dongeren, Robert McCall, Bas Hoonhout, Arnold van Rooijen, Pieter van Geer, Lodewijk de Vet, Kees Nederhoff 외 (p.i) |
| 상태/날짜 | State: final, 27 April 2015 (p.i, 각 페이지 footer) |
| PDF 메타 | Author: Kees Nederhoff, 145p (pdfinfo) |
| 키워드 | hydrostatic / surfbeat / non-hydrostatic, morphodynamics, dune erosion, overwash, breaching, coral reefs, vegetation, ships (p.i) |

본문 페이지 footer는 "X of 141"로 표기(예: 본문 §2.1 시작은 footer "6 of 141"). 아래 인용의 `(p.NN)`은 이 footer 기준 본문 페이지.

## 2. 전체 목차 (장별 페이지, p.1-3 TOC)

| 장 | 절 | p. |
|---|---|---|
| 1 Introduction | Readers guide / Manual version | 4-5 |
| 2 Processes and model formulation | | 6 |
| | 2.1 Domain and definitions (coordinate / grid set-up) | 6 |
| | 2.2 Hydrodynamics options (stationary / surfbeat / non-hydrostatic) | 7-12 |
| | 2.3 Short wave action (action balance / dissipation / radiation stress / wave shape / turbulence / roller) | 13-22 |
| | 2.4 Shallow water equations (viscosity / bed shear / vegetation / wind) | 23-26 |
| | 2.5 Non-hydrostatic pressure correction | 26 |
| | 2.6 Groundwater flow (continuity / equation of motions) | 27-31 |
| | 2.7 Sediment transport (A-D / params / formulations / nonlinearity / dilatancy / bed slope) | 32-37 |
| | 2.8 Bottom updating (fluxes / avalanching / bed composition) | 38-40 |
| | 2.9 Ship-induced wave motions | 41 |
| 3 Boundary conditions | 3.1 Waves / 3.2 SWE / 3.3 Sediment / 3.4 Cyclic | 43-48 |
| 4 Input description | 4.1 General … 4.14 Time parameters | 49-92 |
| 5 Bibliography | | 93 |
| A Hands on exercises | Delfland·Kijkduin·Santa Rosa·Yanchep | 99-101 |
| B Advanced model coefficients | B.1-B.17 | 103-119 |
| C Numerical implementation | grid·wave action·SWE·sediment·bed update·BC·non-hydrostatic | 121-139 |

## 3. 도메인·격자 (§2.1, p.6)

- 계산 x축은 항상 해안을 향함(approx. 해안선 수직), y축은 alongshore. world 좌표계, curvilinear 필수(직교는 특수 경우). 직교 시 origin (xori,yori) + 방위 alfa(East 기준 반시계)로 local→world (§2.1.1, p.6).
- **staggered grid**: 수위·수심·농도·파/roller 에너지·radiation stress는 cell center, 유속·sediment transport·radiation stress gradient는 u-/v-point(cell interface) (§2.1.2, p.6). 출력 변수: `uu`,`vv`(interface), `u`,`v`(center, 보간, 출력용), `zs`/`zb`는 상향 양(positive upward) (p.6).

## 4. Hydrodynamics 모드 (§2.2, p.7)

원래 short-wave averaged·wave-group resolving 모델(Roelvink et al. 2009)에 모드 추가. keyword `wavemodel` 로 선택 (p.7):

| 모드 | keyword | 내용 |
|---|---|---|
| Stationary | `wavemodel = stationary` | wave-averaged, infragravity 무시. HISWA(Holthuijsen 1989)와 유사하나 wave growth/period 변화 없음. breaking은 Baldock(1998) (§2.2.1, p.8) |
| Surfbeat (instationary) | `wavemodel = surfbeat` | wave-group scale 단파 포락(엔벨로프)+연관 장파(infragravity) 해상. 소산 Roelvink(1993a)/Daly(2012), roller(Svendsen 1984 등) (§2.2.2, p.9) |
| Non-hydrostatic (wave-resolving) | `wavemodel = nonh` | NLSWE + 압력보정(q). SWASH(Zijlema 2011) 1-layer 버전 유사. 개별 파 전파/소산. 단파 runup·overwash·diffraction 포함. surfbeat보다 훨씬 고비용 (§2.2.3, p.11) |

모든 입력 시간은 **morphological time**으로 지정; `morfac` 적용 시 입력 시계열이 내부적으로 morfac로 나뉨(`morfacopt = 1`) (p.7).

surfbeat 세부 옵션(p.10): 1D(ny=0) directional spreading 유지/단일 bin(`dtheta = thetamax-thetamin`, `snells=1`로 Snell 법칙); 2DH on-the-fly refraction(`dtheta` 폭 지정) 또는 stationary solver로 mean direction 후 전파(`single_dir = 1`, `dtheta_s`).

## 5. 단파 작용 (Short wave action, §2.3)

### 5.1 파동작용 균형 (§2.3.1, p.13, keyword `swave`)

$$\frac{\partial A}{\partial t}+\frac{\partial c_x A}{\partial x}+\frac{\partial c_y A}{\partial y}+\frac{\partial c_\theta A}{\partial \theta}=-\frac{D_w+D_f+D_v}{\sigma}\quad(2.1)$$

$A=S_w/\sigma$ (2.2), 빈도는 spectral parameter $f_{m-1,0}$로 대표. $\sigma=\sqrt{gk\tanh kh}$ (2.3). 전파속도 $c_x=c_g\cos\theta$, $c_y=c_g\sin\theta$, $c_\theta$는 굴절항 (2.4) (p.13). $D_w,D_f,D_v$는 각각 파·바닥마찰·식생 소산.

- **wave-current interaction** (`wci=1`, §2.3.1.1, p.13): Eikonal 방정식으로 파수 k 보정 (2.5), gully·rip current에서 중요. 기본은 wci 미적용으로 $\sigma=\omega$.

### 5.2 소산 (§2.3.2, p.14)

breaking 식 5종 (Table, p.15):

| 식 | 파 유형 | keyword |
|---|---|---|
| Roelvink (1993a) | instationary | `roelvink1` |
| Roelvink extended | instationary | `roelvink2` ($H^3/h$ 비례) |
| Daly et al. (2010) | instationary | `roelvink_daly` |
| Baldock et al. (1998) | stationary | `baldock` |
| Janssen & Battjes (2007) | stationary | `janssen` |

Roelvink: $D_w=2\frac{\alpha}{T_{rep}}Q_b E_w$, $Q_b=1-\exp[-(H_{rms}/H_{max})^n]$, $H_{max}=\gamma(h+\delta H_{rms})$ (2.11) — `alpha`(O(1)), `gamma`(breaker index), `delta` (p.14). roelvink2는 $H_{rms}/h$ 추가 인자 (2.12). Daly: $H_{rms}>\gamma h$이면 breaking, $<\gamma_2 h$이면 정지(`gamma2`) (2.13). Baldock (2.14): $D_w=\frac14\alpha Q_b g f_{rep}(H_b^2+H_{rms}^2)$, $H_b=\frac{0.88}{k}\tanh(\gamma kh/0.88)$ (p.15). Janssen & Battjes (2.15)는 Baldock 개정. 방향 분배 (2.16) (p.16).

- **바닥마찰** (§2.3.2.2, p.16): $D_f=\frac23\frac{\rho}{\sqrt\pi}f_w(\frac{\pi H_{rms}}{T_{m01}\sinh kh})^3$ (2.17), `fw` 단파마찰계수(coral reef에서 중요, flow의 cf와 무관). 도출: $D_f\approx0.21 f_w u_{orb}^3$(monochromatic, 2.22), $0.28 f_w u_{orb}^3$(stationary, 2.23) (p.16).
- **식생** (§2.3.2.3, p.17): Mendez & Losada(2004)+Suzuki(2011) 층별 합산 $D_v=\sum D_{v,i}$ (2.24-2.25). keyword `vegetation`, `veggiefile`, `veggiemapfile`. $C_D,b_v,N_v,\alpha_i(=h_v/h)$.

### 5.3 Radiation stress·wave shape·turbulence·roller

- **radiation stress** (§2.3.3, p.18): linear theory 적분 (2.26).
- **wave shape** (§2.3.4, p.18): 단파 평균이라 파형 미해상. 비선형 보정 2종 — Ruessink(2012) Ursell 기반(`waveform = ruessink_vanrijn`, 2.27-2.28), Van Thiel de Vries(2009)/Rienecker-Fenton 8조파(`waveform = vanthiel`, 2.29-2.31). Ruessink는 정확한 파형 미산출 → bore-averaged turbulence와 조합 불가 (p.19).
- **turbulence** (§2.3.5, p.20): 표면 breaking turbulence를 바닥으로 전달. `turb` = `wave_averaged`(2.33) / `bore_averaged`(2.34, vanthiel 파형 필요) / `none`. $k_s=(D_r/\rho_w)^{2/3}$ (2.35, Battjes 1975), $L_{mix}$ roller 두께 (2.36).
- **roller energy balance** (§2.3.6, p.21): $\frac{\partial E_r}{\partial t}+\frac{\partial E_r c\cos\theta}{\partial x}+\frac{\partial E_r c\sin\theta}{\partial y}=S-D$ (2.40), $D_r=2\beta\frac{g}{c_g}E_r$ (2.45), `beta` O(0.1). roller 기여 radiation stress $S_{xx,r}=E_r\cos^2\theta$ 등 (2.43) (p.21-22).

## 6. 천수방정식 (Shallow water equations, §2.4, p.23)

저빈도파·평균류는 depth-averaged **GLM**(Generalized Lagrangian Mean, Andrews & McIntyre 1978) 정식. Lagrangian $u^L=u^E+u^S$ (2.48), Stokes drift $u^S=\frac{E_w\cos\theta}{\rho hc}$ (2.49). GLM 운동량·연속식 (2.50, p.23):

$$\frac{\partial u^L}{\partial t}+u^L\frac{\partial u^L}{\partial x}+v^L\frac{\partial u^L}{\partial y}-fv^L-\nu_h(\ldots)=\frac{\tau_{sx}}{\rho h}-\frac{\tau_{bx}^E}{\rho h}-g\frac{\partial\eta}{\partial x}+\frac{F_x}{\rho h}+\frac{F_{v,x}}{\rho h}$$

bed shear는 **Eulerian** 유속으로 계산(GLM 아님) (p.23).

- **수평점성** (§2.4.1, p.23): 기본 Smagorinsky(1963) (2.51), `nuh`=$c_S$=0.1. `smag=0`이면 직접 nuh 지정.
- **bed shear stress** (§2.4.2, p.24): Ruessink(2001) (2.52). `bedfriction` 5종 (Table, p.24): `cf`(무차원), `chezy`(C), `manning`(n), `white-colebrook`(ks), `white-colebrook-grainsize`(D90). 값은 `bedfriccoef`(단일) 또는 `bedfricfile`(셀별). 모래해안 전형: Chézy~55 m^{1/2}/s, Manning~0.02, ks~0.01-0.15 m (p.24-25).
- **식생 damping** (§2.4.3, p.25): drag force $F_v=\frac12\rho C_D b_v N u|u|$ (2.57), Lagrangian 유속 사용 (2.58).
- **wind** (§2.4.4, p.26): $\tau_s=\rho_a C_d|W|W$ (2.59), 기본 off, `windv` 또는 wind file.

## 7. 비정수압 압력보정 (§2.5, p.26)

`wavemodel = nonh` 시 NLSWE+비정수압 q. wave action balance off(`swave = 0`). 표면 동압=0·선형 변화 가정으로 depth-averaged q 산출 (p.26). 수직운동량 (2.60), bed kinematic BC $w_b=u\partial(\zeta-h)/\partial x$ (2.61), Keller-box(Lam & Simpson 1976; Stelling & Zijlema 2003)로 $q_b$ (2.62), local continuity (2.64). breaking은 Smit(2013) **HFA**(hydrostatic front approximation): $\partial\zeta/\partial t>0.6$이면 bore 가정, $<0.3$이면 복원(`maxbrsteep`, `secbrsteep`) (p.27).

## 8. 지하수 흐름 (§2.6, p.27, keyword `gwflow = 1`)

Darcy(laminar)+Forchheimer(turbulent) 파라미터화, 수직 surface-groundwater 교환 포함. 연속식 $\nabla\cdot U=0$ (2.65). Darcy (2.67, `gwscheme = laminar`, 도수전도도 `kx`/`ky`/`kz`). turbulent (2.68, `gwscheme = turbulent`, MODFLOW-2005 유사, `gwReturb`=$Re_{crit}$). head: hydrostatic(`gwnonh = 0`, 수치안정 위해 `dwetlayer`) 또는 non-hydrostatic(`gwnonh = 1`, 형상 `gwheadmodel = parabolic/exponential`) (p.28-29). 교환 메커니즘 3종: 침투 $S_{inf}$ (2.70), 용출 $S_{exf}$ (2.71), submarine $S_{sub}$ (2.72); 가파른 투수사면은 수평교환 `gwhorinfil = 1` (2.73). 지하수위 갱신 (2.74), 표면수위 보정 (2.75). 초기조건 `gw0`/`gw0file` (p.31).

## 9. Sediment transport (§2.7, p.32)

### 9.1 이류-확산 (§2.7.1, p.32)

depth-averaged A-D + source-sink(평형농도 기반, Galappatti & Vreugdenhil 1985):

$$\frac{\partial hC}{\partial t}+\frac{\partial hCu^E}{\partial x}+\frac{\partial hCv^E}{\partial y}-\frac{\partial}{\partial x}\Big(D_h h\frac{\partial C}{\partial x}\Big)-\frac{\partial}{\partial y}\Big(D_h h\frac{\partial C}{\partial y}\Big)=\frac{hC_{eq}-hC}{T_s}\quad(2.76)$$

적응시간 $T_s=\max(f_{Ts}\,h/w_s,\,T_{s,min})$ (2.77), `tsfac`($f_{Ts}$), `Tsmin`.

### 9.2 일반 파라미터 (§2.7.2, p.32)

평형농도 $C_{eq}$는 유속크기 $v_{mg}$·궤도속도 $u_{rms}$·침강속도 $w_s$의 함수. `lws=1`이면 $v_{mg}=|u^E|$ (2.78); `lws=0`이면 이전 step+`cats` 평균(2.79). $u_{rms}$ linear theory (2.80, 수심에 `delta`$H_{rms}$ 가산). breaking turbulence 보정 $u_{rms,2}^2=u_{rms}^2+1.45k_b$ (2.81). $w_s$ Hallermeier(1981)/van Rijn 기반(2.82-2.84), 고농도 감소 `fallvelred=1` Richardson-Zaki(1954) (2.85-2.87).

### 9.3 Transport 식 2종 (§2.7.3, p.33)

총 평형농도 $C_{eq}=\max[\min(C_{eq,b},C_{max})+\min(C_{eq,s},C_{max}),0]$ (2.88), `cmax`. `bed`/`sus`/`bulk` 스위치로 bed·suspended load 포함 제어.

- **Soulsby-Van Rijn** (`form = soulsby_vanrijn`, §2.7.3.1, p.34): $C_{eq}\propto(\sqrt{v_{mg}^2+0.018 u_{rms,2}^2/C_d}-U_{cr})^{2.4}$ (2.89), $A_{sb}/A_{ss}$ (2.90), $D_*$ (2.91), $U_{cr}$ (2.92), drag $C_d$ (2.93, `z0`).
- **Van Thiel-Van Rijn** (`form = vanthiel_vanrijn`, **기본값**, §2.7.3.2, p.35): drag 없음, $U_{cr}$를 currents(Shields 1936)·waves(Komar-Miller 1975) 가중합. $C_{eq,b}\propto(\sqrt{v_{mg}^2+0.64u_{rms,2}^2}-U_{cr})^{1.5}$, suspended는 지수 2.4 (2.94-2.98).

### 9.4 비선형·dilatancy·bed slope

- **wave nonlinearity** (§2.7.4, p.36): skewness/asymmetry로 advection velocity $u_a=(f_{Sk}S_k+f_{As}A_s)u_{rms}$ (2.100), `facSk`/`facAs`(alias `facua`). 높을수록 강한 onshore transport.
- **dilatancy** (§2.7.5, p.36, `dilatancy = 1`): Van Rhee(2010) 임계 Shields 감소 (2.101), `pormax`($n_l$), `rheeA`(A, 단입자 0.75/연속체~1.7). permeability $k_l$ Den Adel(1987) (2.102).
- **bed slope** (§2.7.6, p.37): magnitude는 Roelvink(2.104, `bdslpeffmag = roelvink_total/roelvink_bed`) 또는 Soulsby(2.105, `soulsby_total`); direction은 Talmon(1995) (`bdslpeffdir = talmon`, 2.106-2.108); initiation Soulsby(2.109, `bdslpeffini = total/bed`).

## 10. Bottom updating (§2.8, p.38)

- **flux 기반** (§2.8.1): $\frac{\partial z_b}{\partial t}+\frac{f_{mor}}{1-p}(\frac{\partial q_x}{\partial x}+\frac{\partial q_y}{\partial y})=0$ (2.110). `morfac` O(1-10), `sedtrans`. morfac 두 방식: `morfacopt=1`(입력 morphological time, 극단 단기 적합) / `morfacopt=0`(조석주기 단위, 장기 적합, Roelvink 2006) (p.38).
- **avalanching** (§2.8.2, p.39, `avalanching`): 임계사면 초과 시 인접셀 물질 교환. `dryslp`(기본 1.0)/`wetslp`(기본 0.3), 속도제한 `dzmax` (2.110).
- **bed composition** (§2.8.3, p.39): 다중 분율+다중 bed layer로 armoring/sorting. 3종 layer: top(수주와 교환, 두께 보존)·variable("breathing", 두께 적응)·bottom(고정 두께). 두께 `dzg1`/`dzg2`/`dzg3` 또는 `dzg`. 너무 두꺼우면 균일화·너무 얇으면 수치혼합 (p.39-40).

## 11. Ship-induced waves (§2.9, p.41, `ships=1`)

비정수압 버전 사용. 항행 선박을 미리 정의된 track 위 이동 pressure head로 표현. ship grid에 draft 지정→매 step global grid 보간(volume 보존)→pressure head 갱신으로 파 생성(Zhou 2013). track은 AIS에서 취득 가능 (p.41).

## 12. Boundary conditions (Ch3, p.43)

- **offshore(front)** (§3.2.1, p.45): 기본 absorbing-generating(Method of Characteristics), `epsi`(Kalman-update, 기본 자동 `epsi=-1`). 대안: `front = wall`(no flux)/`wlevel`/`nonh_1d`/`waveflume`(continuity, 실험실 set-up용).
- **lateral(left/right)** (§3.2.2, p.46): 기본 **Neumann**(no-gradient, `left = neumann`). 대안 `wall`/`no_advec`/`neumann_v`.
- **tide** (§3.2.3, p.46): `tideloc` = 0(uniform `zs0`)/1/2/4 시계열, `zs0file`.
- **river/point discharge** (§3.2.4, p.47): 다중 위치, m³/s 시계열.
- **sediment** (§3.3, p.47): 모든 곳 Neumann(경계횡단 gradient=0).
- **cyclic** (§3.4, p.48, `cyclic=1`): 두 lateral 경계를 물리적으로 연결(shadow zone 제거), MPI 루틴 사용. 양측 두 grid row bathy 동일 필요.

## 13. params.txt 입력 (Ch4, p.49)

### 13.1 구조 (§4.1, p.49)

실행 `xbeach.exe`가 작업디렉토리 `params.txt`를 읽음(없으면 미실행). 한 줄당 `keyword = value` 1쌍, 순서 무관, `=` 없는 줄은 주석. 대부분 keyword는 default 보유. log: `xbeach.log`/`XBlog.txt`에 설정·미설정(default) 전부 기록. 매뉴얼 표기: `*`=필수, `+`=advanced expert(일반 적용에 비권장) (p.49). JONSWAP 필수: grid(`xfile`/`yfile` 또는 `xyfile`, `nx`/`ny`), `depfile`, `tstop`, 방향격자(`thetamin`/`thetamax`/`dtheta`), `wbctype=jons`+`bcfile` (p.49).

1D params.txt 예시(p.49): `depfile`, `posdwn=0`, `nx=265`, `ny=0`, `vardx=1`, `thetamin=-90`/`thetamax=90`/`dtheta=15`, `tstop=3600`, `rho=1025`, `tideloc=2`/`zs0file`, `wbctype=jons`/`bcfile`, `outputformat=netcdf`/`tint`/`tstart`, `nglobalvar`.

### 13.2 Physical processes 스위치 (§4.2 Table, p.50)

| keyword | 기능 | default |
|---|---|---|
| `swave` | short waves | 1 |
| `lwave` | short wave forcing on NLSWE | 1 |
| `flow` | flow 계산 | 1 |
| `sedtrans` | sediment transport | 1 |
| `morphology` | morphology | 1 |
| `avalanching` | avalanching | 1 |
| `nonh`+ | non-hydrostatic pressure | 0 |
| `gwflow`+ | groundwater | 0 |
| `vegetation`+ | 식생 상호작용 | 0 |
| `ships`+ | ship waves | 0 |
| `single_dir`+ | stationary refraction(surfbeat mean dir) | 0 |
| `snells`+ | Snell 법칙 refraction | 0 |
| `swrunup`+ | short wave runup | 0 |
| `setbathy` | 시계열 prescribed bathy | 0 |

### 13.3 Grid/bathymetry (§4.3, p.51)

`nx`/`ny`=cross-shore/alongshore 격자점 수, 계산격자 (nx+1)×(ny+1). `depfile` 크기 [nx+1, ny+1], 한 줄=cross-shore transect, 기본 positive down(`posdwn`). grid 종류: fast 1D(ny=0), 1D(ny=2), 2DH(ny>2). 등간격 `dx`/`dy`, 비등간격 `vardx=1`+`xfile`/`yfile`. Delft3D grid `gridform=delft3d`+`xyfile`. 방향격자 convention `thetanaut`(0=Cartesian, 1=Nautical) (p.51-53).

주요 grid keyword 기본값(§4.3 Table, p.52-53): `alfa`=0.0, `dtheta`=10.0(0.1-20), `dtheta_s`=10.0, `dx`/`dy`=-1.0, `gridform`=xbeach, `nx`=50(2-10000), `ny`=2(0-10000), `posdwn`=1.0, `thetamax`=90.0(-180~180), `thetamin`=-90.0, `thetanaut`=0, `vardx`=0, `xori`/`yori`=0.0.

### 13.4 Wave 입력 (§4.4, p.54)

`wbctype` 종류(§3.1/Table, p.54-55): `off`, `stat`(stationary sea state), `bichrom`, `ts_1`/`ts_2`(1·2차 시계열), `jons`(JONSWAP), `swan`(SWAN 2D 출력), `vardens`(formatted), `ts_nonh`(비정수압용 elev+velocity), `reuse`, `stat_table`, `jons_table`. spectral(`jons`/`swan`/`vardens`/`jons_table`)은 `bcfile`로 정의, 시계열 길이 `rt`(기본 3600s)·해상도 `dtbc`(기본 1.0s, morfac 무영향)로 생성·재사용 (p.57). JONSWAP 파일 예: `Hm0`/`Tp`/`mainang`/`gammajsp`/`s`/`fnyq` (p.59). 기타 spectral keyword: `random`(기본 1, random seed), `fcutoff`(기본 0.0), `sprdthr`(0.08), `Tm01switch`(0), `nspr`(0) (p.57-58).

### 13.5 Time parameters (§4.14, p.92)

시뮬레이션은 항상 t=0 시작, 출력은 `tstart`까지 지연 가능. 시간스텝은 최대 Courant `CFL`로 결정.

| keyword | 설명 | default | range |
|---|---|---|---|
| `CFL` | 최대 Courant-Friedrichs-Lewy | 0.7 | 0.1-0.9 |
| `tstop` | 정지시각(morphological time) | 2000.0 | 1.0-1e6 s |
| `tunits`+ | udunits 시간단위 | 's' | |

## 14. Appendix B — Advanced coefficient 기본값 (p.103-119)

매뉴얼 본문이 "기본 vanthiel/roelvink2" 등 언급하나 정확한 default·range는 Appendix B 표에 집약. 핵심 발췌:

### B.2 Wave dissipation (p.103-104)
표준값 `gamma`=0.55·`n`=10은 `break=roelvink1`로 calibration; roelvink2는 $H^3/h$ 비례라 calibration 영향 (p.103).

| keyword | default | range |
|---|---|---|
| `break` | **roelvink2** | roelvink1/baldock/roelvink2/roelvink_daly/janssen |
| `alpha`+ | 1.0 | 0.5-2.0 |
| `gamma` | 0.55 | 0.4-0.9 |
| `gamma2` | 0.3 | 0.0-0.5 (roelvink_daly) |
| `gammax`+ | 2.0 | 0.4-5.0 (최대 H/h) |
| `n`+ | 10.0 | 5.0-20.0 |
| `delta`+ | 0.0 | 0.0-1.0 |
| `fw`+ | 0.0 | 0.0-1.0 |
| `fwcutoff` | 1000.0 | |

### B.3 Rollers (p.105)
`roller`+ =1, `beta`+ =0.1(0.05-0.3, 낮을수록 setup/return flow/longshore current shoreward shift 증가), `rfb`+ =0.

### B.4 Wave-current interaction (p.105)
`cats`+ =4.0 (1.0-50.0, Trep 단위 current averaging).

### B.7 Sediment transport (p.107-110)

| keyword | default | range |
|---|---|---|
| `form` | **vanthiel_vanrijn** | soulsby_vanrijn/vanthiel_vanrijn |
| `Tsmin`+ | 0.5 | 0.01-10.0 s |
| `facSk`+ | 0.1 | 0.0-1.0 |
| `facAs`+ | 0.1 (matches facua) | 0.0-1.0 |
| `facua`+ | 0.1 | 0.0-1.0 |
| `facsl`+ | 1.6 | 0.0-1.6 (bedslope) |
| `sus`+ | 1 | 0-1 |
| `sws`+ | 1 | 0-1 (short wave stirring) |
| `lws`+ | 1 | 0-1 (long wave stirring) |
| `lwt`+ | 0 | 0-1 (long wave turbulence) |
| `bdslpeffmag` | roelvink_total | none/roelvink_total/roelvink_bed/soulsby_total/... |
| `bdslpeffdir` | none | none/talmon |
| `bdslpeffini` | none | none/total/bed |
| `pormax` | 0.5 | 0.3-0.6 |
| `reposeangle` | 30.0 | 0.0-45.0 deg |
| `rheeA` | 0.75 | 0.75-2.0 |
| `smax`+ | -1.0 | -1.0-3.0 |
| `fallvelred` | 0 | 0-1 |

### B.10 Morphology (p.112)

| keyword | default | range |
|---|---|---|
| `morfac` | 1.0 | 0.0-1000.0 |
| `morfacopt`+ | 1 | 0-1 |
| `morstart` | 120.0 | 0-1e7 s |
| `morstop` | 2000.0 | 0-1e7 s |
| `dryslp` | 1.0 | 0.1-2.0 (avalanching, 수면 위) |
| `wetslp` | 0.3 | 0.1-1.0 (수면 아래) |
| `dzmax`+ | 0.05 | 0.0-1.0 m/s/m |
| `hswitch`+ | 0.1 | 0.01-1.0 m (wet/dry slope 전환 수심) |
| `struct` | 0 | 0-1 (hard structure) |
| `ne_layer` | <file> | (비침식층 위 침식가능층 두께; 0=완전 비침식, 10=10m 침식가능) |

### B.11 Bed update (p.113)
다중 분율/layer 시 variable layer split/merge 기준 `frac_dz`/`split`/`merge`, variable layer 선택 `nd_var`. prescribed bed evolution `setbathy`/`nsetbathy`/`setbathyfile` (p.113).

## 15. Numerical implementation (Appendix C, p.121-139, 개요)

TOC 기준(p.3): C.1 grid set-up, C.2 wave action(surfbeat·stationary solver), C.3 SWE(mass·momentum balance·time integration·groundwater), C.4 sediment transport, C.5 bottom updating(avalanching·bed composition), C.6 BC, C.7 non-hydrostatic(global/local continuity·horizontal/vertical momentum). 상세 이산화는 source-analysis 노트 영역 — 본 매뉴얼 노트는 정식화·reference 집중.

## 16. 주요 참고문헌 (§5 Bibliography, p.93-)

핵심: Andrews & McIntyre (1978, GLM), Baldock et al. (1998), Battjes (1975), Daly et al. (2010/2012), Galappatti & Vreugdenhil (1985, A-D), Holthuijsen et al. (1989, HISWA), Janssen & Battjes (2007), Roelvink et al. (2009, 원논문)·Roelvink (1993a), Soulsby (1997), van Rijn (1984/2007), van Thiel de Vries (2009), Ruessink et al. (2012), Smit et al. (2013, HFA), Zijlema et al. (2011, SWASH), Van Rhee (2010, dilatancy), Suzuki et al. (2011, vegetation) (p.93-).
