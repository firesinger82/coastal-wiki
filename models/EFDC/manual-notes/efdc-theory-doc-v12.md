---
title: "EFDC+ Theory Document Version 12 (DSI 2024) — TOC + Development History + 7 챕터 구조"
topic: efdc-theory-doc-v12
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf 표지·Acknowledgement·Contents pages 1-5 직접 추출 — EFDC+ Theory Version 12, DSI LLC (Edmonds WA), October 2024. 표지·Acknowledgement·Contents 페이지의 챕터 구조·페이지 번호·authorship 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — PDF Read pages 1-5 직접 확인 (표지·Acknowledgement·Contents)"
verification_date: 2026-05-24
related:
  - models/EFDC/manual-notes/efdc-manuals-overview.md
  - models/EFDC/manual-notes/efdc-user-manual-r850.md
  - models/EFDC/manual-notes/efdc-sediment-theory-2003.md
  - models/EFDC/README.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC+ Theory Document Version 12 — 이론서 reference

> 출처: [`models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf`](../raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf) (DSI LLC, Edmonds WA, October 2024, 14.4 MB).

## 1. 자료 식별 + 인용 형식

| 항목 | 값 |
|---|---|
| 제목 | EFDC+ Theory |
| 버전 | Version 12 |
| 발행 | DSI LLC (Edmonds WA, www.dsi.llc) |
| 날짜 | October 2024 |
| 파일 | `EFDC_Theory_Document_Ver_12.pdf` |
| 크기 | 14.4 MB |
| 페이지 | 표지·Ack(i)·Contents(ii-iii)·List of Abbreviations(ix)·본문 ~120p+ |

**공식 인용 형식** (표지 페이지 직접):

> DSI LLC. 2024. EFDC+ Theory, Version 12. Published by DSI LLC, Edmonds WA. Available at https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf

## 2. Development History (Acknowledgement, p.i 직접 인용)

EFDC+ 의 authorship 계보:

| 기여자 | 기여 | 시기 |
|---|---|---|
| **Dr. John Hamrick** | 원본 EFDC 출간 (1992) — Environmental Fluid Dynamics Code | 1992 |
| Dr. Hamrick (Tetra Tech) | 다수 enhancement + documentation | 1990s-2000s |
| **Kyeong Park** + 외 | CE-QUAL-ICM (ICM) kinetics for eutrophication 초기 | — |
| **Craig Jones** | SEDiment dynamics — SEDZLJ implementation (Ziegler·Lick·Jones 알고리즘) + separate documentation | — |
| **Jeff Ji** | Rooted Plant Epiphytes Module (RPEM) + separate documentation | — |
| **Scott James** | 기타 code·documentation enhancement | — |
| **DSI LLC engineers** | EFDC+ 통합 + 속도·안정성·정확도 개선 (단일 comprehensive theory doc 통합) | 2009~ 현재 |

**DSI 의 primary contributors (2009~)** — Paul Craig, Thomas Mathis, Tran Duc Kien, Jeffrey Jung, Kester Scandrett, Anurag Mishra.

> "Since 2009, the engineers at DSI have been the primary contributors to the updates and maintenance of this document." (Acknowledgement, p.i)

> "Of course, EFDC source code has been publicly available since the early 2000s, so there have been numerous other contributors, resulting in a large number of versions of EFDC." (Acknowledgement, p.i)

## 3. Contents (pp.ii-iii, 직접 인용)

```
List of Abbreviations                                                       ix

1 INTRODUCTION                                                              1
  1.1 Development History                                                   1
  1.2 EFDC+ Advancements                                                    2
  1.3 Enhancements to EFDC+ since EEMS10.3                                  4
  1.4 EFDC+ Overview                                                        5
  1.5 Conclusion                                                            7

2 HYDRODYNAMICS                                                             8
  2.0.1 Overview                                                            8
  2.1 Governing Equations                                                   8
    2.1.1 Horizontal and Vertical Coordinate Systems                        9
    2.1.2 Basic Hydrodynamic Equations                                      10
    2.1.3 Equation of State                                                 13
    2.1.4 Vertical Turbulent Closure                                        14
    2.1.5 Horizontal Turbulence Closure                                     16
  2.2 Boundary Conditions and External Forcings                             16
    2.2.1 Bottom Friction                                                   16
    2.2.2 Vegetation                                                        17
    2.2.3 Wind Forcings                                                     19
    2.2.4 Wave Action                                                       21
    2.2.5 Local Wind-Generated Waves                                        23
    2.2.6 Harmonic Forcings                                                 25
    2.2.7 Hydraulic Structures                                              26
    2.2.8 Propeller Wash                                                    30
  2.3 Numerical Solution for the Equations of Motion                        32
  2.4 Computational Aspects of the Three Time Level External Mode Solution  37
  2.5 Computational Aspects of the Three-Time Level Internal Mode Solution  42
  2.6 Vertical Layering Options                                             46
    2.6.1 Standard Sigma (SIG) Approach                                     46
    2.6.2 Sigma-Zed Approach (SGZ)                                          47
  2.7 Near-Field Discharge Dilution and Mixing Zone Analysis                48
    2.7.1 Shear-Induced Entrainment                                         49
    2.7.2 Forced Entrainment                                                50
    2.7.3 Model Implementation                                              50
  2.8 Conclusion                                                            52

3 CONSERVATIVE CONSTITUENTS TRANSPORT                                       53
  3.1 Introduction                                                          53
  3.2 Basic Equation of Advection-Diffusion Transport                       53
  3.3 Numerical Solution for Transport Equations                            54

4 DYE MODULE                                                                57
  4.1 Decay                                                                 57
  4.2 Age of Water                                                          58

5 TEMPERATURE AND HEAT TRANSFER                                             59
  5.1 Surface Heat Exchange                                                 60
    5.1.1 Full Heat Balance                                                 60
    5.1.2 COARE 3.6 Bulk Algorithm                                          61
    5.1.3 Equilibrium Temperature                                           62
  5.2 Short Wave Radiation                                                  63
    5.2.1 One-band Light Attenuation Model                                  63
    5.2.2 Two-band Light Attenuation Model                                  64
    5.2.3 Water Quality Linked Light Attenuation                            64
  5.3 Bed Heat Exchange                                                     66
  5.4 Ice Formation and Melt                                                67
    5.4.1 Heat Balance                                                      67
    5.4.2 Ice Surface Temperature                                           68
    5.4.3 Freezing Temperature                                              68
    5.4.4 Ice Melt at Air/Water Interface                                   69
    5.4.5 Ice Growth/Melt at Bottom of Ice                                  69
    5.4.6 Solar Radiation at Bottom of Ice                                  69
  5.5 Water Volume Evaporative Losses                                       70

6 SEDIMENT TRANSPORT                                                        72
  6.1 Introduction                                                          72
  6.2 Suspended Sediment Transport                                          72
    6.2.1 Governing Equations for Suspended Sediment Transport              72
    6.2.2 Numerical Solution                                                74
  6.3 EFDC Sediment Transport Module                                        77
    6.3.1 Non-Cohesive Sediment                                             77
    6.3.2 Cohesive Sediments                                                88
    6.3.3 Consolidation of Mixed Cohesive and Non-Cohesive Sediment Beds    92
  6.4 SEDZLJ Sediment Transport Module                                      95
    6.4.1 Background                                                        95
    6.4.2 Bed Shear Stress                                                  97
    6.4.3 Erosion Rate                                                      98
    6.4.4 Suspended Load                                                    104
    6.4.5 Bedload                                                           105
    6.4.6 Bed Armoring                                                      107

7 CHEMICAL FATE AND TRANSPORT                                               110
  7.1 Development Overview                                                  111
  7.2 Basic Equations                                                       111
  ...
```

## 4. 챕터별 활용 매트릭스

### 4.1 Ch 2 HYDRODYNAMICS (p.8-52, 가장 큼)

운영 해석의 핵심:
- **§2.1.4 Vertical Turbulent Closure** (p.14) — Mellor-Yamada (MY2.5)
- **§2.2.1 Bottom Friction** (p.16) — Manning n 또는 z0 + log law
- **§2.2.2 Vegetation** (p.17) — 식생 항력 (mangrove·갈대)
- **§2.2.4 Wave Action** (p.21) — SWAN 결합 시 radiation stress
- **§2.2.8 Propeller Wash** (p.30) — Propwash WhitePaper 와 함께
- **§2.3-2.5 Three Time Level scheme** (p.32-45) — split-explicit time-stepping (external·internal mode)
- **§2.6 Vertical Layering** (p.46-47) — **SIG vs SGZ 선택**:
  - SIG (Standard Sigma) — terrain-following, 단순
  - SGZ (Sigma-Zed) — hybrid, 깊은 영역 z-level + 얕은 영역 sigma (수직 일관성)
- **§2.7 Near-Field Discharge Dilution** (p.48-51) — 방류구 mixing zone

### 4.2 Ch 5 TEMPERATURE (p.59-71)

한국 적용 (영광·고리 발전소 온배수):
- **§5.1.1 Full Heat Balance** (p.60) — net shortwave + longwave + sensible + latent
- **§5.1.2 COARE 3.6 Bulk Algorithm** (p.61) — modern air-sea flux 알고리즘 (concepts/sst 와 cross-ref)
- **§5.4 Ice Formation and Melt** (p.67-69) — 동해 결빙

### 4.3 Ch 6 SEDIMENT TRANSPORT (p.72-109, 운영 핵심)

**두 분기 모듈** — 사용자가 선택:

| 항목 | EFDC SedTran Module (§6.3) | SEDZLJ Module (§6.4) |
|---|---|---|
| 출처 | Hamrick legacy + Tetra Tech 2003 ([[efdc-sediment-theory-2003]]) | Ziegler·Lick·Jones 알고리즘 (SEDZLJ) |
| 입력 키 (ISTRAN) | ISTRAN(6)=cohesive CALSED·ISTRAN(7)=noncohesive CALSND | unified |
| Bed structure | 분리 (cohesive vs noncohesive) | unified multi-bed-layer, size-class |
| Bed Shear (§6.4.2) | — | wave+current quadratic |
| Erosion (§6.4.3) | — | Lick·Jones formulation |
| Bed Armoring (§6.4.6) | — | active layer + dynamic armoring |
| 활용 | legacy·교과서 비교 | modern operational |

source-code dispatch — [`models/EFDC/source-analysis/efdc_sediment.md`](../source-analysis/sediment/efdc_sediment.md) `ssedtox.f90:863-875`.

### 4.4 Ch 7 CHEMICAL FATE (p.110+)

Hg·PCB·toxics 의 sorption + degradation. 한국 산업 폐기물 분석에 활용 가능.

## 5. 작성 우선순위 (남은 작업)

본 노트는 **TOC + Acknowledgement + 챕터 nav** 수준. 깊이별 후속 노트 후보:

- ✅ [[efdc-theory-v12-ch2-hydrodynamics]] — §2.1-2.7 equation level (gov eq + numerical scheme + SIG/SGZ) — 2026-05-24 작성
- ✅ [[efdc-theory-v12-ch5-temperature-heat]] — §5.1-5.5 equation level (Full Heat Balance/COARE 3.6/Equilibrium Temp + short wave radiation/light attenuation + bed heat + ice formation/melt + evaporation) + mod_heat.f90 소스 교차검증 — 2026-07-04 작성
- ✅ [[efdc-theory-v12-ch6-sediment]] — §6.2 부유이동(Eq6.1-6.12) + §6.3 Original SedTran(non-cohesive van Rijn/Shields/bedload 5공식/Rouse 평형농도 Smith-McLean·Garcia-Parker armoring + cohesive floc 4옵션/Krone/Partheniades + 혼합bed 압밀 Eq6.13-6.110) + §6.4 SEDZLJ→[[efdc_sedzlj]] 소스매핑 — 2026-07-04 작성 (Original↔SEDZLJ 대비 부분충족)
- `efdc-sedzlj-vs-sedtran-comparison.md` — 두 모듈의 알고리즘 1:1 매핑 (ch6 cross-walk §3 에 부분 흡수)

## 6. 관련 자료

- [[efdc-manuals-overview]] — 6 manuals 인덱스
- [[efdc-user-manual-r850]] — 운영 매뉴얼 (입력 파일·실행)
- [[efdc-sediment-theory-2003]] — Hamrick legacy sediment theory (DSI v12 §6.3 의 source)
- [`concepts/sediment-transport/06-model-application.md`](../../../concepts/sediment-transport/06-model-application.md) — EFDC dispatch (concept 레벨)
- [`models/EFDC/source-analysis/`](../source-analysis/) — codex source-code 분석 (이론 식 ↔ Fortran 매핑)
- 외부: [DSI EFDC+ Theory PDF Download](https://www.eemodelingsystem.com/wp-content/Download/Documentation/EFDC_Theory_Document_Ver_12.pdf)

## 이론 문서와 코드의 식 차이

이 절은 이론 문서의 인쇄식과 EFDC+ 12.5 코드의 정적 판독을 대조한다. 어느 쪽이 맞는지는 이 대조로 단정하지 않는다. 코드 인용의 상대 경로 기준은 `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/`이다. 해석 문장은 정적 판독과 실행 미확인을 표시한다.

| 식 번호·쪽 | 문서 식 | 코드 file:line과 원문 | 차이 |
| --- | --- | --- | --- |
| EFDC_Theory_Document_Ver_12.pdf, PDF 35쪽·인쇄 22쪽, 식 2.49 | `E=\frac{1}{8}\rho gH_S^2` | `Waves/wavesxy.f90:221` — `WV(L).HEIGHT = min(0.75*HP(L),WV(L).HEISIG)            ! *** INCLUDING BREAKING WAVE`<br>`Waves/wavesxy.f90:222` — `if( WV(L).HEIGHT >= WHMI .and. HP(L) > HDRYWAV )then`<br>`Waves/wavesxy.f90:223` — `WDEP1 = HP(L)`<br>`Waves/wavesxy.f90:224` — `WPRD  = 2.*PI/WV(L).FREQ`<br>`Waves/wavesxy.f90:225` — `if( WVLCAL == 1 )then`<br>`Waves/wavesxy.f90:226` — `call BISEC(DISRELATION,WLMIN,WLMAX,EPS,WPRD,WDEP1,0._8,0._8,RRLS)`<br>`Waves/wavesxy.f90:227` — `WV(L).LENGTH = RRLS`<br>`Waves/wavesxy.f90:228` — `endif`<br>`Waves/wavesxy.f90:229` — `WV(L).K   = max( 2.*PI/WV(L).LENGTH, 0.01 )`<br>`Waves/wavesxy.f90:230` — `WV(L).KHP = min(WV(L).K*HP(L),SHLIM)`<br>`Waves/wavesxy.f90:231` — `WK = 2.0*WV(L).KHP                             ! *** 4*PI/WV(L).LENGTH*HP(L) = 2KH`<br>`Waves/wavesxy.f90:232` — `WE = 9.81*1000.*WV(L).HEIGHT**2 /16.           ! *** TOTAL WAVE ENERGY : KG/S2`<br>`Waves/wavesxy.f90:233` — `WVENEP(L) = WE/1000.                           ! *** WAVE ENERGY/RHO: M3/S2`<br>`Waves/mod_windwave.f90:741` — `WVENEP(L)= G*WV(L).HEIGHT**2./16.                         ! *** ENERGY/RHO (M3/S2) FOR RANDOM WAVE` | 문서 계수는 1/8이다. 외부 파랑과 내부 SMB 코드의 계수는 모두 1/16이다. 외부 코드의 HEIGHT는 제한을 적용한 HEISIG이다. 밀도 정규화는 이 2배 차이를 없애지 않는다.<br>해석: 파고·진폭 정의와 저장 단위를 확인하지 않고 두 에너지식을 같다고 해석할 수 없다(정적 판독, 실행 미확인). |
| EFDC_Theory_Document_Ver_12.pdf, PDF 73쪽·인쇄 60쪽, 식 5.2 | `H_L=\varepsilon\sigma(T_s+273.15)^4(0.39-0.05\sqrt{e_a})(1+B_c C)+4\varepsilon\sigma(T_s+273.15)^3(T_s-T_a)` | `Transport/mod_heat.f90:646` — `HBLW = 1.312E-14*((TEM(L,KC)+273.)**4)*(0.39-0.05*SQRT(VPAT(L)))*(1.-.8*CLOUDT(L)) + &`<br>`Transport/mod_heat.f90:647` — `5.248E-14*((TEM(L,KC)+273.)**3)*(TEM(L,KC)-TATMT(L))` | 문서는 구름 인자 1+0.8C이다. 코드는 1−0.8C이다. 문서는 273.15이고 코드는 273이다. 코드는 ρcp로 나눈 계수 1.312E−14와 5.248E−14를 사용한다.<br>해석: 계수비 4의 일치만으로 장파식 전체의 정합을 확인할 수 없다(정적 판독, 실행 미확인). |
| EFDC_Theory_Document_Ver_12.pdf, PDF 76쪽·인쇄 63쪽, 식 5.12 | `\beta_w=0.255-0.0085T_w-0.000204T_w^2` | `Transport/mod_heat.f90:1580` — `BETA  = 0.255-(8.5E-3*TSTAR)+(2.04E-4*TSTAR*TSTAR)`<br>`Transport/mod_heat.f90:1588` — `TSTAR = (ET+TDEW_F)*0.5`<br>`Transport/mod_heat.f90:1589` — `BETA  = 0.255-(8.5E-3*TSTAR)+(2.04E-4*TSTAR*TSTAR)` | 문서의 이차항 부호는 음수이다. 코드의 이차항 부호는 양수이다. 코드는 Tw 대신 평형온도와 이슬점의 평균 TSTAR를 사용한다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽, 식 6.94<br>EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽, 식 6.102<br>EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽, 식 6.110 | `\varepsilon_c=\dfrac{\psi_{wc}}{\psi_{sc}}`<br>`q=-\left(\dfrac{K}{1+\varepsilon}\right)_{k+\frac12}\dfrac{2\lambda_{k+\frac12}}{\left(\Delta_{k+1}+\Delta_k\right)}\left[\left(f_{sc}\varepsilon_c\right)_{k+1}-\left(f_{sc}\varepsilon_c\right)_k\right]+\left(\dfrac{K}{1+\varepsilon}\right)_{k+\frac12}\left(\dfrac{\bar\rho_s}{\rho_w}-1\right)_{k+\frac12}`<br>`\varepsilon_c=\dfrac{\varepsilon-f_{sn}\varepsilon_n}{f_{sc}}` | `SedTran-Original/calbed.f90:96` — `TMPEXP = EXP(-DTSED/SEDVRDT)`<br>`SedTran-Original/calbed.f90:97` — `do K = 1,KB`<br>`SedTran-Original/calbed.f90:98` — `do LP = LF,LL`<br>`SedTran-Original/calbed.f90:99` — `L = LSED(LP)`<br>`SedTran-Original/calbed.f90:100` — `if( K <= KBT(L) )then`<br>`SedTran-Original/calbed.f90:101` — `VDRBED1(L,K) = VDRBED(L,K)`<br>`SedTran-Original/calbed.f90:102` — `HBED1(L,K)   = HBED(L,K)`<br>`SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`<br>`SedTran-Original/calbed.f90:104` — `TMPTOP = 1. + VDRBED(L,K)`<br>`SedTran-Original/calbed.f90:105` — `TMPBOT = 1. + VDRBED1(L,K)`<br>`SedTran-Original/calbed.f90:106` — `HBED(L,K) = TMPTOP*HBED1(L,K)/TMPBOT`<br>`SedTran-Original/calbed.f90:184` — `TMPVAL = HBED(L,K)/(1. + VDRBED(L,K))`<br>`SedTran-Original/calbed.f90:185` — `QWTRBED(L,K) = QWTRBED(L,K-1) - DELTI*TMPVAL*(VDRBED(L,K)-VDRBED1(L,K))` | 점착성 간극수 체적과 고체 체적을 나눈 별도 ε_c 계산을 찾지 못했다. CALBED는 전체 VDRBED만 갱신한다.<br>혼합 투수계수·유효응력 경사로 Darcy 유량을 구하는 경로를 찾지 못했다. 코드는 간극비 변화에서 간극수 유량을 역산한다.<br>전체 간극비에서 비점착성 간극수 기여를 빼어 ε_c를 복원하는 계산을 찾지 못했다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽, 식 4.5 | `\displaystyle \frac{dC}{dt}=-K` | `Transport/caldye.f90:130` — `elseif( DYES(MD).ITYPE == 2 )then`<br>`Transport/caldye.f90:131` — `! *** Age of Water (0th order growth)`<br>`Transport/caldye.f90:132` — `DAGE = DELT/86400.`<br>`Transport/caldye.f90:134` — `!$OMP PARALLEL DO PRIVATE(ND,K,LP,L)`<br>`Transport/caldye.f90:135` — `do ND = 1,NDM`<br>`Transport/caldye.f90:136` — `do K = 1,KC`<br>`Transport/caldye.f90:137` — `do LP = 1,LLWET(K,ND)`<br>`Transport/caldye.f90:138` — `L = LKWET(LP,K,ND)`<br>`Transport/caldye.f90:139` — `DYE(L,K,MD) = DYE(L,K,MD) + DAGE` | ITYPE=2는 경과 일수 Δt/86400을 더한다. Confluence는 영차 플래그 −1을 설명하므로 K=−1이면 문서 식의 부호를 코드와 맞출 수 있다. 엔진은 이 갱신에서 KRATE0를 사용하지 않는다. PDF는 C의 단위를 day, t의 단위를 day, K의 단위를 1/day로 정의한다. 영차 dC/dt의 단위는 day/day이므로 PDF의 K 단위와 맞지 않는다. 이 단위 불일치 판정은 차원 해석이다.<br>해석: 문서의 영차 변화율 단위 정의와 차원이 맞지 않는다(정적 판독, 실행 미확인). |
| EFDC_Theory_Document_Ver_12.pdf, PDF 185쪽·인쇄 172쪽, 식 8.81<br>EFDC_Theory_Document_Ver_12.pdf, PDF 185쪽·인쇄 172쪽, 식 8.83 | `\displaystyle KNit\cdot NH4=fNit(T)\left(\frac{DO}{KHNit_{DO}+DO}\right)\left(\frac{NH4}{KHNit_N+NH4}\right)Nit_m`<br>`\displaystyle KNit=fNit(T)\left(\frac{DO}{KHNit_{DO}+DO}\right)\left(\frac{KHNit_N}{KHNit_N+NH4}\right)KNit_m` | `Eutrophication/mod_wq.f90:945` — `call fson_get(json_data, "nitrification.max_rate",                                 WQNITM)`<br>`Eutrophication/mod_wq.f90:3593` — `WQNIT(L) = WQTDNIT(IWQT(L)) * O2WQ(L) / (WQKHNDO + O2WQ(L) + 1.E-18) * RNH4WQ(L) / (WQKHNN + RNH4WQ(L) + 1.E-18)`<br>`Eutrophication/mod_wq.f90:4357` — `WQF14 = - DTWQO2*WQNIT(L)` | WQNIT의 분자에 NH4가 있다. 코드가 이 계수를 NH4 손실률로 다시 곱한다. 문서의 Nitm·NH4/(KH+NH4)와 달리 코드 총속도에는 NH4가 한 번 더 곱해진다.<br>문서의 계수 분자는 KHNitN이다. 코드의 분자는 현재 NH4이다.<br>해석: 코드 총속도에는 NH4가 한 번 더 곱해져 문서식과 NH4 차수가 다르다(정적 판독, 실행 미확인). |
| EFDC_Theory_Document_Ver_12.pdf, PDF 199쪽·인쇄 186쪽, 식 8.127 | `\displaystyle \frac{\partial(RPD)}{\partial t}=F_{PRSD}\cdot P_{RPS}\cdot RPS-L_{RPD}RPS` | `Eutrophication/mod_rpem.f90:388` — `SOURSINK = -RLRPD                                                    ! EQ. (4)  RLRPD-Loss rate for plant detritus at bottom of water column (/day)`<br>`Eutrophication/mod_rpem.f90:392` — `WQRPD(L) = FACIMP*(WQRPD(L)+DTWQ*FRPSD*RLRPS*WQRPS(L))` | 문서는 생산 PRPS·RPS를 쇄설물 공급으로 사용하고 RPS에 손실률을 곱한다. 코드는 비호흡 손실 RLRPS·RPS를 공급으로 사용하고 RPD를 감쇠시킨다. PDF p.199 이미지에서 두 대상을 확인했다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽, 식 8.155<br>EFDC_Theory_Document_Ver_12.pdf, PDF 206쪽·인쇄 193쪽, 식 8.157 | `\displaystyle JRP_{RS}=KRPO_{RS}\cdot(RPR-RORS\cdot RPS)`<br>`\displaystyle JRP_{RS}=KRP_{RS}\left(\frac{I_{SS}}{I_{SS}+I_{SSS}}\right)RPR` | `Eutrophication/mod_rpem.f90:342` — `RJRPRS(L) = RKRPORS*(ROSR*WQRPR(L)-WQRPS(L))`<br>`Eutrophication/mod_rpem.f90:349` — `RJRPRS(L) = RKRPRS*RISS(L)/(RISS(L)+RISSS+1E-18)` | 코드는 RKRPORS·(ROSR·RPR−RPS)를 사용한다. 문서는 KRPO·(RPR−RORS·RPS)를 사용한다. 같은 입력 비를 주면 영점 비가 역수이다.<br>문서의 광 제한 이동률에 RPR을 곱한다. 코드는 그 생물량 인자를 곱하지 않는다. 따라서 입력 RKRPRS의 필요 단위도 문서의 1/day와 다르다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 204쪽·인쇄 191쪽, 식 8.150<br>EFDC_Theory_Document_Ver_12.pdf, PDF 205쪽·인쇄 192쪽, 식 8.153<br>EFDC_Theory_Document_Ver_12.pdf, PDF 207쪽·인쇄 194쪽, 식 8.158<br>EFDC_Theory_Document_Ver_12.pdf, PDF 209쪽·인쇄 196쪽, 식 8.168 | `\displaystyle f_3(T)=\exp\left(KTP_{RPS}[T-TPREF_{RPS}]\right)`<br>`\displaystyle R_{RPS}=RREF_{RPS}\cdot\exp\left(KTR_{RPS}[T-TRREF_{RPS}]\right)`<br>`\displaystyle R_{RPR}=RREF_{RPR}\cdot\exp\left(KTR_{RPR}[T-TRREF_{RPR}]\right)`<br>`\displaystyle R_{RPE}=RREF_{RPE}\cdot\exp\left(KTR_{RPE}[T-TRREF_{RPE}]^2\right)` | `Eutrophication/mod_rpem.f90:1250` — `RPEMTPrps(NT) = EXP(-rKTP1RPS*(WTEMP-TP1RPS)*(WTEMP-TP1RPS) )`<br>`Eutrophication/mod_rpem.f90:1253` — `RPEMTPrps(NT) = EXP(-rKTP2RPS*(WTEMP-TP2RPS)*(WTEMP-TP2RPS) )`<br>`Eutrophication/mod_rpem.f90:301` — `RRPS(L) = RMRPS*XLIMTRRPS(L)                                              ! EQ. (15)  RRPS - Temperature limited shoot respiration (/day)`<br>`Eutrophication/mod_rpem.f90:1268` — `RPEMTRrps(NT) = EXP(-rKTR1RPS*(WTEMP-TR1RPS)*(WTEMP-TR1RPS) )`<br>`Eutrophication/mod_rpem.f90:1271` — `RPEMTRrps(NT) = EXP(-rKTR2RPS*(WTEMP-TR2RPS)*(WTEMP-TR2RPS) )`<br>`Eutrophication/mod_rpem.f90:317` — `RRPR(L) = RMRPR*XLIMTRRPR(L)                                    ! EQ. (18)`<br>`Eutrophication/mod_rpem.f90:1286` — `RPEMTRrpr(NT) = EXP(-rKTR1RPR*(WTEMP-TR1RPR)*(WTEMP-TR1RPR) )`<br>`Eutrophication/mod_rpem.f90:1289` — `RPEMTRrpr(NT) = EXP(-rKTR2RPR*(WTEMP-TR2RPR)*(WTEMP-TR2RPR) )`<br>`Eutrophication/mod_rpem.f90:325` — `RRPE(L) = RMRPE*XLIMTRRPE(L)`<br>`Eutrophication/mod_rpem.f90:1277` — `RPEMTRrpe(NT) = EXP(-rKTR1RPE*(WTEMP-TR1RPE)*(WTEMP-TR1RPE) )`<br>`Eutrophication/mod_rpem.f90:1280` — `RPEMTRrpe(NT) = EXP(-rKTR2RPE*(WTEMP-TR2RPE)*(WTEMP-TR2RPE) )` | 지상부 생산에 대한 단일 선형 지수 온도 대안은 없다. 코드가 양쪽 Gaussian 함수만 구성한다.<br>지상부 호흡은 최적 온도 양쪽의 음의 이차 지수함수이다. 문서의 기준 온도에 대한 선형 지수함수와 다르다.<br>뿌리 호흡은 최적 온도 양쪽의 음의 이차 지수함수이다. 문서의 선형 지수함수와 다르다.<br>문서는 양의 계수·제곱 온도차 지수이다. 코드는 최적 구간의 1과 구간 밖 음의 Gaussian 지수를 사용한다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽, 식 8.185<br>EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽, 식 8.187<br>EFDC_Theory_Document_Ver_12.pdf, PDF 213쪽·인쇄 200쪽, 식 8.189<br>EFDC_Theory_Document_Ver_12.pdf, PDF 214쪽·인쇄 201쪽, 식 8.191 | `\displaystyle \begin{aligned}\frac{\partial RPON_W}{\partial t}&=\frac{1}{H}\left(FNR_{RPS}\cdot R_{RPS}+(1-F_{RPSD})\cdot FNRL_{RPS}\cdot L_{RPS}\right)\cdot RPSNC\cdot RPS\\&\quad+\frac{1}{H}\left(FNR_{RPE}\cdot R_{RPE}+FNRL_{RPE}\cdot L_{RPE}\right)\cdot RPENC\cdot RPE\\&\quad+\frac{1}{H}FNRL_{RPD}\cdot L_{RPD}\cdot RPSNC\cdot RPD\end{aligned}`<br>`\displaystyle \begin{aligned}\frac{\partial LPON_W}{\partial t}&=\frac{1}{H}\left(FNL_{RPS}\cdot R_{RPS}+(1-F_{RPSD})\cdot FNLL_{RPS}\cdot L_{RPS}\right)\cdot RPSNC\cdot RPS\\&\quad+\frac{1}{H}\left(FNL_{RPE}\cdot R_{RPE}+FNLL_{RPE}\cdot L_{RPE}\right)\cdot RPENC\cdot RPE\\&\quad+\frac{1}{H}FNLL_{RPD}\cdot L_{RPD}\cdot RPSNC\cdot RPD\end{aligned}`<br>`\displaystyle \begin{aligned}\frac{\partial DON_W}{\partial t}&=\frac{1}{H}\left(FND_{RPS}\cdot R_{RPS}+(1-F_{RPSD})\cdot FNDL_{RPS}\cdot L_{RPS}\right)\cdot RPSNC\cdot RPS\\&\quad+\frac{1}{H}\left(FND_{RPE}\cdot R_{RPE}+FNDL_{RPE}\cdot L_{RPE}\right)\cdot RPENC\cdot RPE\\&\quad+\frac{1}{H}FNDL_{RPD}\cdot L_{RPD}\cdot RPSNC\cdot RPD\end{aligned}`<br>`\displaystyle \begin{aligned}\frac{\partial NH4_W}{\partial t}&=\frac{1}{H}\left(FNI_{RPS}\cdot R_{RPS}+(1-F_{RPSD})\cdot FNIL_{RPS}\cdot L_{RPS}\right)\cdot RPSNC\cdot RPS\\&\quad+\frac{1}{H}\left(FNI_{RPE}\cdot R_{RPE}+FNIL_{RPE}\cdot L_{RPE}\right)\cdot RPENC\cdot RPE\\&\quad+\frac{1}{H}FNIL_{RPD}\cdot L_{RPD}\cdot RPSNC\cdot RPD\\&\quad-\frac{1}{H}PN_{RPS}\cdot F_{RPSNW}\cdot R_{RPS}\cdot RPSNC\cdot RPS\\&\quad-\frac{1}{H}PN_{RPE}\cdot P_{RPE}\cdot RPENC\cdot RPE\end{aligned}` | `Eutrophication/mod_rpem.f90:424` — `WQRPSRN(L) = RPSNC*WQRPSR(L)                                    ! *** WQRPSRN - Shoot nitrogen biomass loss due to respiration`<br>`Eutrophication/mod_rpem.f90:425` — `WQRPSLN(L) = RPSNC*WQRPSL(L)                                    ! *** WQRPSLN - Shoot nitrogen biomass loss due to non-respiration processes`<br>`Eutrophication/mod_rpem.f90:483` — `+ FNRRPE*WQRPERN(L) + FNRLRPE*WQRPELN(L) + FNRLRPD*WQRPDLN(L) )`<br>`Eutrophication/mod_rpem.f90:1379` — `WQRPDLN  = 0`<br>`Eutrophication/mod_rpem.f90:487` — `+ FNLRPE*WQRPERN(L) + FNLLRPE*WQRPELN(L) + FNLLRPD*WQRPDLN(L) )`<br>`Eutrophication/mod_rpem.f90:491` — `+ FNDRPE*WQRPERN(L) + FNDLRPE*WQRPELN(L) + FNDLRPD*WQRPDLN(L) )`<br>`Eutrophication/mod_rpem.f90:495` — `+ FNIRPE*WQRPERN(L) + FNILRPE*WQRPELN(L) + FNILRPD*WQRPDLN(L) )`<br>`Eutrophication/mod_rpem.f90:574` — `WQV(L,K,INHX) = WQV(L,K,INHX) - DTDHWQ*(RPENC*TMPNH4E*PRPE(L)*WQRPE(L) + RPSNC*TMPNH4S*FRPSNW(L)*PRPS(L)*WQRPS(L))  ! NH4, EQ. COMPLETED` | 문서 쇄설물 N 공급에는 RPSNC·LRPD·RPD가 있다. 코드가 쓰는 WQRPDLN은 0으로 초기화한 뒤 갱신하지 않는다. 저층 두께도 전체 H와 다르다.<br>문서 지상부 NH4 흡수항은 RRPS를 사용한다. 코드는 PRPS를 사용한다. 쇄설물 N 공급 변수 WQRPDLN은 초기값 0에 머문다. PDF p.214 이미지에서 RRPS를 확인했다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 142쪽·인쇄 129쪽, 식 7.63 | `\displaystyle \left.\frac{\partial C}{\partial t}\right\rvert_{volat}=\frac{K_v}{H_{KC}}\left(f_dC-\frac{C_a}{\frac{H_L}{RT_K}}\right)` | `ChemFate/caltox.f90:781` — `TOXPFTW(L,K,NT) = ( TOXPFTW(L,K,NT)/(1. + TOXPFTW(L,K,NT)) ) - TOXPFW(L,K,NFD,NT)`<br>`ChemFate/caltox_kinetics.f90:224` — `PFTWC = TOXPFTW(L,KC,NT)              ! *** Solids partitioning fraction`<br>`Transport/calvolterm.f90:129` — `DISFRAC = 1./(1. + PFTW)                                         ! *** Dissolved fraction`<br>`Transport/calvolterm.f90:133` — `VOLTERM = MULT*KV*HPKCI*( CONC - AIRCON*0.001 )`<br>`ChemFate/caltox_kinetics.f90:229` — `TOX(L,KC,NT) = TOX(L,KC,NT) - VOLTERM*TOXTIME` | 문서의 인쇄 우변은 양의 변화율이다. 코드는 휘발량을 뺀다. PFTW는 이미 정규화한 입자상 분율이지만 코드는 용존 분율을 1/(1+PFTW)로 다시 만든다. 대기 농도 항은 Henry 비로 나누지 않는다. MULT 입력도 추가한다. 농도·시간 단위 차이는 매개변수 표에 적었다. |
| EFDC_Theory_Document_Ver_12.pdf, PDF 248쪽·인쇄 235쪽, 식 10.3<br>EFDC_Theory_Document_Ver_12.pdf, PDF 250쪽·인쇄 237쪽, 식 10.26<br>EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽, 식 10.27<br>EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽, 식 10.28<br>EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽, 식 10.29<br>EFDC_Theory_Document_Ver_12.pdf, PDF 251쪽·인쇄 238쪽, 식 10.30 | `\displaystyle S_K=\frac{1}{2}C_TA_M\left(\beta_pU^3-\beta_dUK\right)`<br>`\displaystyle \frac{\partial}{\partial t}\left(H\frac{q^2}{2}\right)=\beta_p\left(\frac{1}{2}\frac{1}{m_xm_y\Delta_k}C_TA_M\right)(u^2+v^2)^{\frac{1}{2}}(u^2+v^2)-\beta_d\left(\frac{1}{2}\frac{1}{m_xm_y\Delta_k}C_TA_M\right)(u^2+v^2)^{\frac{1}{2}}\frac{q^2}{2}-\frac{H}{B_1l}q^3`<br>`\displaystyle \frac{\partial}{\partial t}\left(H\frac{q^2}{2}\right)+\left[\beta_d\left(\frac{1}{2}\frac{C_TA_M}{m_xm_y\Delta_k}\right)\frac{(u^2+v^2)^{\frac{1}{2}}}{H}+\frac{q}{B_1l}\right]Hq^2=\beta_p\left(\frac{1}{2}\frac{C_TA_M}{m_xm_y\Delta_k}\right)(u^2+v^2)^{\frac{1}{2}}(u^2+v^2)`<br>`\displaystyle \left\{1+\Delta t\left[\beta_d\left(\frac{C_TA_M}{m_xm_y\Delta_k}\right)\frac{(u^2+v^2)^{\frac{1}{2}}}{H}+\frac{2q}{B_1l}\right]\right\}(Hq^2)^{n+1}=(Hq^2)^n+\Delta t\beta_p\left(\frac{C_TA_M}{m_xm_y\Delta_k}\right)(u^2+v^2)^{\frac{1}{2}}(u^2+v^2)`<br>`\displaystyle \frac{\partial}{\partial t}(Hq^2l)+\left[C_{e4}\beta_d\left(\frac{1}{2}\frac{C_TA_M}{m_xm_y\Delta_k}\right)\frac{(u^2+v^2)^{\frac{1}{2}}}{H}+\frac{q}{B_1l}\right]Hq^2l=C_{e4}\beta_p\left(\frac{1}{2}\frac{C_TA_M}{m_xm_y\Delta_k}\right)(u^2+v^2)^{\frac{1}{2}}(u^2+v^2)l`<br>`\displaystyle \left\{1+\Delta t\left[C_{e4}\beta_d\left(\frac{1}{2}\frac{C_TA_M}{m_xm_y\Delta_k}\right)\frac{(u^2+v^2)^{\frac{1}{2}}}{H}+\frac{q}{B_1l}\right]\right\}(Hq^2l)^{n+1}=(Hq^2l)^n+\Delta tC_{e4}\beta_p\left(\frac{1}{2}\frac{C_TA_M}{m_xm_y\Delta_k}\right)(u^2+v^2)^{\frac{1}{2}}(u^2+v^2)l` | `calqq2t.f90:229` — `TMPQQI = 0.5*BETAMHK_P`<br>`calqq2t.f90:230` — `TMPQQE = 0.5*BETAMHK_D`<br>`calqq2t.f90:231` — `PQQMHKI(L,K) = TMPQQI*(FXMHK(L,K)+FXMHK(L,K+1)+FYMHK(L,K)+FYMHK(L,K+1))`<br>`calqq2t.f90:232` — `PQQMHKE(L,K) = TMPQQE*(FXMHK(L,K)*U(L,K)*U(L,K) + FXMHK(L,K+1)*U(L,K+1)*U(L,K+1) &`<br>`calqq2t.f90:384` — `+ DELT*HPI(L)*(PQQVEGI(L,K)+PQQMHKI(L,K)+PQQSUPI(L,K))`<br>`calqq2t.f90:280` — `PQQL = DELT*HP(L)*(CTE3TMP*PQQB + CTE1*(PQQU+PQQV) + CE4VEG*PQQVEGE(L,K) + CE4MHK*PQQMHKE(L,K) + CE4SUP*PQQSUPE(L,K))`<br>`calqq2t.f90:356` — `+ DELT*HPI(L)*(CE4VEG*PQQVEGI(L,1)+CE4MHK*PQQMHKI(L,1)+CE4SUP*PQQSUPI(L,1))` | 코드는 BETAMHK_P를 음해 소멸계수에 쓴다. 코드는 BETAMHK_D를 명시 생성항에 쓴다. 문서의 βp 생성·βd 소멸 배치와 반대이다.<br>문서의 βp와 βd 위치가 코드의 BETAMHK_P와 BETAMHK_D 위치와 반대이다. 코드 힘의 성분 부호도 문서의 비음수 속도 크기와 구분해야 한다.<br>코드는 q²l에 CE4MHK를 적용한다. 코드의 생성·소멸 β 계수 배치는 문서와 반대이다. |
| EFDC+_Propwash_WhitePaper.pdf, PDF 20쪽·인쇄 2-5쪽, 식 2.8 | `\displaystyle \sigma=\begin{cases}0.5R_{mo}&\text{for }x/D_p<0.5\\0.5R_{mo}+0.075\left(x+0.5D_p\right)&\text{for }x/D_p\geq0.5\end{cases}` | `Propwash/Mod_Active_Ship.f90:911` — `sigma = 0.5*radius_vel_max + 0.075*(ax - radius_prop)` | PDF 20쪽 이미지는 x+0.5Dp를 인쇄한다. 코드는 ax-0.5Dp를 사용한다. |
| EFDC+_Propwash_WhitePaper.pdf, PDF 21쪽·인쇄 2-6쪽, 식 2.12 | `\displaystyle B'=-C_t^{-0.216}\times\beta^{1.024}\times P'^{-1.87}` | `Propwash/Mod_Active_Ship.f90:919` — `Bprime = -(ship.thrust_coeff**(-0.216)) * ship.blade_area_ratio**1.024 / ship.pitch_ratio;    ! eqn (2.33)` | PDF 21쪽 이미지는 피치비의 -1.87승을 인쇄한다. 코드는 피치비로 한 번 나누므로 -1승이다. |
| 유출유 소멸 기준·Theory PDF 246쪽·인쇄 233쪽 | `10⁻⁹ kg` | `Drifter/mod_drifter.f90:324` — `if( DVOL(NP) <= 1D-9 )then`<br>`Drifter/mod_drifter.f90:929` — `DRAT(K) = DRAT(K)/86400.`<br>`Drifter/mod_drifter.f90:2299` — `BIODEG = EXP(-TDEP*DRAT(NG)*DELTD)                     ! *** FRACTION REMAINING AT END OF TIME STEP` | Theory는 질량 기준이다. 코드는 DVOL≤10⁻⁹ m³의 부피 기준이다. Confluence는 1 mm³의 부피 기준이다. |
| SEDZLJ 퇴적 제한값·Confluence (번호 식 없음) | `models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Sediment/SEDZLJ_Sediment_Model.md:42` — `*Deposition Limit of Water Column Sediments* can be determined between zero and one, and this parameter represents the minimum fraction of sediment in the bottom water column layer allowed to deposit in a single time step. Setting this value to zero would cause 100% of the amount to be deposited in one-time step, however, this is also dependent on the settling rate specified.` | `SedTran-SEDZLJ/s_sedzlj.f90:157` — `SMASS(NS)  = SED(L,KSZ(L),NS)*1.0D-06*DZC(L,KSZ(L))*HPCM(L)*MAXDEPLIMIT         ! *** SMASS(NS) is the total sediment mass in the first layer.  It is calculated as a precaution so that no more than the total amount of mass in the first layer can deposit onto the sediment bed PERSED time step.`<br>`SedTran-SEDZLJ/s_sedzlj.f90:158` — `DEPTSS(NS) = CTB(NS)*PROB(NS)*(DWS(NS)*DTSEDJ)                                  ! *** Deposition of a size class is equal to the probability of deposition times the settling rate times the time step times the sediment concentration`<br>`SedTran-SEDZLJ/s_sedzlj.f90:159` — `DEPTSS(NS) = min(MAX(DEPTSS(NS),0.0),SMASS(NS))                                 ! *** Do not allow more sediment to deposit than is available in the water-column layer above the bed` | 코드는 수층 가용 질량에 MAXDEPLIMIT을 곱해 퇴적 상한을 만든다. MAXDEPLIMIT=0이면 퇴적 상한은 0이다. 문서의 ‘최소 분율’과 ‘0이면 전량 퇴적’은 코드와 반대이다. |
