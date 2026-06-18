---
title: "Delft3D-WAQ Processes Library Description — Technical Reference Manual 정리"
model: Delft3D
doc: Delft3D-WAQ_Processes_Technical_Reference_Manual.pdf
canonical_source: manual
citation_status: verified
verification_method: "Delft3D-WAQ_Processes_Technical_Reference_Manual.pdf pdftotext -layout 직접 추출 후 TOC(전 17장) + 대표 프로세스군 지배식·계수·옵션 페이지 인용. REAROXY(p.29-31)·SATUROXY(p.43-44)·NITRIF_NH4(p.69-70)·DENWAT/DENSED_NO3(p.78-79)·DEC*(p.310-313)·SED_/S_(p.482-483)·TEMPERATUR(p.534-535)·§1.1-1.4·§1.6(p.1-3,24,26) 직접 확인 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
---

# Delft3D-WAQ Processes Library Description — Technical Reference Manual

> D-Water Quality(DELWAQ) 수질 프로세스 라이브러리의 **과학 공식 reference**. 산소·영양염·유기물·1차생산·온도·침강 등 각 프로세스의 PROCESS명·지배식·계수·단위·옵션 스위치를 프로세스 단위로 기술. 611p, Version 2026.02 (Rev 80917, 3 May 2026), Deltares 발행 (표지 p.41-44, p.70). 본 노트는 TOC 전수 + 대표 프로세스군의 식·계수를 페이지 인용으로 정리. 소스코드 대응은 [[delft3d_waq_process_library]], 조류 모듈은 [[delft3d_waq_algae_models]], 사용자 흐름은 `delft3d-waq-user-manual` 참조.

## 1. 문서 정체

- 정식명: **Processes Library Description — Technical Reference Manual** (PDF Title 메타데이터: "Processes Library User Manual") (표지 p.12-27, 메타데이터).
- Released for: Delft3D FM Suite 2026.02 / D-HYDRO Suite 2026.02 / SOBEK Suite 3.8.1 / WAQ Suite 2026.02 (p.표지 줄33-36).
- 위치: D-Water Quality 매뉴얼군의 **Technical Reference Manual** 파트. state variable·input/output parameter 개요와 라이브러리 내 모든 프로세스의 상세 기술을 담음 (§1.1, p.1).
- 사용 전제: 프로세스 상세 기술은 **PLCT (Processes Library Configuration Tool)** 와 함께 사용 — state variable·input parameter·default value·output parameter를 수식에 연결 (§1.1, p.1).
- 각 프로세스 기술의 구조 (§1.1, p.1): 도입(배경·개념) → **Implementation**(적용 substance·연계 보조 프로세스) → **Formulation**(수식·계수) → **Direction**(스키마화 1DV/1DH/2DV/2DH/3D) → **Directives for use** → **References** → **Parameter Tables**(input/output 파라미터 표).
- 관련 매뉴얼: 프로세스 unique name·관계 인덱스는 별도 **Processes Library Tables** 매뉴얼의 Table 1.1~16.1 (§1.3, p.3). 사용자 정의 프로세스 추가는 'Open Processes Library, User Manual' (§1.3, p.3). 층상 퇴적 접근은 'Sediment Water Interaction' 매뉴얼 (§1.2, p.2).

## 2. 전체 목차 (장별 페이지, p.iii-vii)

| 장 | 제목 | 시작 p. |
|---|---|---|
| 1 | How to find your way in this manual | 1 |
| 2 | Oxygen and BOD | 28 |
| 3 | Nutrients | 68 |
| 4 | Primary producers | 102 |
| 5 | Macrophytes | 213 |
| 6 | Light regime | 244 |
| 7 | Primary consumers and higher trophic levels | 274 |
| 8 | Organic matter (detritus) | 309 |
| 9 | Inorganic substances and pH | 343 |
| 10 | Organic micropollutants | 412 |
| 11 | Heavy metals and radio-active isotopes | 451 |
| 12 | Bacteria and viruses | 472 |
| 13 | Sediment and mass transport | 481 |
| 14 | Temperature | 533 |
| 15 | Microplastics associated with tyre abrasion (TRWP) | 538 |
| 16 | Various auxiliary processes | 549 |
| 17 | Deprecated processes descriptions | 570 |
| — | References | 581 |

수질 프로세스 그룹 13개 챕터 명시 (§1.2, p.2). 5·15장은 목록(p.2)에 누락되어 있으나 본문 존재 (TOC p.iv, vi).

### 주요 절 (대표)

- **2장 산소/BOD**: 2.1 Reaeration (REAROXY, p.29), 2.3 Saturation of DO (SATUROXY, p.43), 2.7 BOD/COD/SOD decomposition (p.53), 2.8 Sediment oxygen demand (p.62) (TOC p.iii).
- **3장 영양염**: 3.1 Nitrification (p.69), 3.3 Denitrification (p.78), 3.4 Adsorption of phosphate (p.84), 3.5 vivianite·3.6 apatite, 3.7 opal silicate 용해 (p.99) (TOC p.iv).
- **4장 1차생산자**: BLOOM(p.104)·DYNAMO(p.167)·PROTIST(p.127)·VEGMOD(p.201) (TOC p.iv).
- **8장 유기물(detritus)**: 8.1 Decomposition (p.310), 8.2 Consumption of electron-acceptors (CONSELAC, p.321), 8.3 Settling (p.335), 8.4 Sediment mineralization S1/2 (p.340) (TOC p.v).
- **9장 무기물질·pH**: CO2 air-water exchange(p.344), pH·탄산염 speciation(p.353), 메탄(p.364-373), sulfide·iron 산화·침전(p.377-405) (TOC p.v).
- **13장 퇴적·질량수송**: 13.1 Settling of sediment (p.482), 13.3 층상퇴적 수송(p.492), 13.5/13.6 flocculation(p.510/512), 13.11 bottom shear stress(p.524) (TOC p.vi).
- **14장 온도**: TEMPERATUR (p.534) (TOC p.vi).

## 3. 대표 프로세스 지배식 reference

### 3.1 재포기 REAROXY — DO 공기-수체 교환 (§2.1, p.29-31)

substance OXY, 최상부 수층에만 작용 (p.29). DO 포화농도는 보조 프로세스 SATUROXY가 공급 (p.29).

$$R_{rear} = klrear \times (C_{oxs} - \max(C_{ox},0))/H$$
$$klrear = klrear20 \times tcrear^{(T-20)}, \quad klrear20 = \frac{a\,v^b}{H^c} + d\,W^2$$
$$f_{sat} = 100 \times \frac{\max(C_{ox},0)}{C_{oxs}}$$

($H$ 수심 [m], $W$ 10 m 풍속 [m/s], $v$ 유속 [m/s], $klrear$ [m/d]) (p.30). 재포기율은 항상 양의 DO 기준으로 계산 (OXY는 음수=환원물질 등가 가능) (p.30).

전달계수 옵션 스위치 **SWRear = 0–7, 9–13** (p.29). 계수 $a,b,c,d$ verbatim (p.30-31):

| SWRear | 출처 | a | b | c | d | 비고 |
|---|---|---|---|---|---|---|
| 0 | constant×H | klrear20×H | 0 | 0 | 0 | klrear20 단위 [d⁻¹] 입력 |
| 1 | constant | klrear20/H | 0 | 0 | 0 | |
| 2 | Churchill et al. (1962) | 5.026 | 0.969 | 0.673 | 0 | 하천 |
| 3 | O'Connor & Dobbins (1956) | 3.863 | 0.5 | 0.5 | 0 | 하천 |
| 4 | O'Connor & Dobbins, scaled | 3.863×klrear20 | 0.5 | 0.5 | 0 | 하천 |
| 5 | Owens et al. (1964) | 5.322 | 0.67 | 0.85 | 0 | 하천 |
| 6 | Langbein & Durum (1967) | 11.23 | 1.0 | 0.33 | 0 | 하천 |

(SWRear=10은 Schmidt수 기반 자체 온도 의존, 예외 — p.30.)

### 3.2 DO 포화농도 SATUROXY (§2.3, p.43-44)

substance OXY. 옵션 스위치 **SWSatOxy = 1, 2** (p.43).

SWSatOxy=1:
$$C_{oxs} = \left[a - bT + (cT)^2 - (dT)^3\right]\left(1 - \frac{C_{cl}}{m}\right)$$

SWSatOxy=2 (Weiss 1970 형):
$$C_{oxs} = \exp\!\left[a + \frac{b}{T_f} + c\ln(T_f) + d\,T_f + SAL(m + nT_f + oT_f^2)\right]\frac{32000}{22400}, \quad T_f = \frac{T+273}{100}$$

고정 계수 (p.44):

| SWSatOxy | a | b | c | d | m | n | o |
|---|---|---|---|---|---|---|---|
| 1 | 14.652 | 0.41022 | 0.089392 | 0.042685 | 105 | – | – |
| 2 | −173.4292 | 249.6339 | 143.3483 | −21.8492 | −0.033096 | 0.014259 | −0.0017 |

유효범위 T 0–40 ℃, 염분 0–40 kg/m³ (Weiss 1970) (p.44). Cl은 SALINCHLOR 프로세스로 염분에서 도출 (p.44).

### 3.3 질산화 NITRIF_NH4 (§3.1, p.69-70)

substance NH4, NO3, OXY. 수층·퇴적층 generic 적용. 옵션 스위치 **SWVnNit** (p.69).
전체 반응: $NH_4^+ + 2O_2 + H_2O \Rightarrow NO_3^- + 2H_3O^+$, 산소요구 **4.57 gO₂/gN** (p.69).

Michaelis-Menten kinetics (SWVnNit = 1.0):
$$R_{nit} = k0nit + knit \times \frac{C_{am}}{Ksam\cdot\varphi + C_{am}} \times \frac{C_{ox}}{Ksox\cdot\varphi + C_{ox}}$$
$$knit = knit20 \times ktnit^{(T-20)}$$

분기 조건 (p.70): $knit=0$ if $T<T_c$ or $C_{ox}\le0$; 영차항 $k0nit$은 저온($T<T_c$, $C_{ox}>0$)→$k0temp$, 무산소($T\ge T_c$, $C_{ox}\le0$)→$k0ox$, $C_{ox}\le Coxc\cdot\varphi$ → 0. $\varphi$=porosity (p.70). MM은 기질 농도가 반포화상수보다 작아지면 1차 kinetics로 전환 (p.70). 대안: pragmatic kinetics (SWVnNit=0.0, 영차+1차, p.70).

### 3.4 탈질 DENWAT_NO3 / DENSED_NO3 (§3.3, p.78-79)

substance NO3, OXY. DENWAT는 수층·퇴적층 generic, DENSED는 S1/2 옵션 시 추가; 층상퇴적 옵션에서는 둘 대신 **CONSELAC** 사용 (p.78). 옵션 스위치 **SWVnDen** (p.78).
전체 반응: $4NO_3^- + 4H_3O^+ \Rightarrow 2N_2 + 5O_2 + 6H_2O$, 산소공급 **2.86 gO₂/gN** (p.78-79).

MM kinetics (SWVnDen = 1.0):
$$R_{den} = (k0den + kden)\times \frac{C_{ni}}{Ksni\cdot\varphi + C_{ni}} \times f_{ox}$$
$$f_{ox} = \begin{cases}1 - \dfrac{C_{ox}}{Ksox\cdot\varphi+C_{ox}} & C_{ox}\ge0\\ 1.0 & C_{ox}<0\end{cases}, \quad kden = kden20 \times ktden^{(T-20)}$$

$f_{ox}$는 산소 억제인자. 임계산소 $Coxc\cdot\varphi$ 이상에서 $kden=0$; 영차항 $k0den$ 분기는 질산화와 대칭 ($k0temp$/$k0ox$/0) (p.79).

### 3.5 유기물(detritus) 분해 DECFAST/DECMEDIUM/DECSLOW/DECREFR/DECDOC/DECPOC5 (§8.1, p.310-313)

다섯 입자성 분획(POC1 fast, POC2 medium, POC3 slow, POC4 refractory, POC5 stem/root) + 용존 refractory(DOC) (p.312-313). 적용 substance: POC/PON/POP/POS1-5, DOC/DON/DOP/DOS, NH4, PO4, SUD 등 (p.311). POC5는 비수송(inactive) substance로 정의 필수 (p.311). 무산소·무질산·무황산 시 CO2와 함께 CH4 생성; 전자수용체 OXY/NO3/SO4 소비와 CO2/CH4 생성 flux는 별도 프로세스 **CONSELAC**가 생성 (p.313).

광화(mineralization) 1차 kinetics, comprehensive 옵션 SWOMDec=0.0 (p.313):
$$R_{min\,j,i} = f_{el} \times f_{acc\,j,i} \times kmin_i \times C_{x\,j,i}, \quad kmin_i = kmin_{i,20}\times ktmin^{(T-20)}$$

($f_{el}$ 전자수용체 제한, $f_{acc}$ 영양염 stripping 가속, $i$=분획 1-5, $j$=영양소 C/N/P/S) (p.313). 1차율은 영양염(N,P) 가용성에 선형 — $kmin_{i,20}$이 $kmin_{i,min,20}$~$kmin_{i,max,20}$ 사이 보간 (p.313). 분해율은 산화>탈질>황산환원>메탄생성 순으로 에너지 감소, 상호배타적 (p.310-311).

### 3.6 침강 SED_(i)/S_(i)/CALVS_(i) (§13.1, p.482-483)

SED_(i): IM1, IM2, IM3 (무기퇴적물). S_(i): CBOD5/CBOD5_2/3, CBODu/_2, NBOD5/NBODu, COD_Cr, COD_Mn (p.482). CALVS_(i): 사용자 침강속도→flocculation 보정 (p.482). 영차+1차 kinetics, Krone (1962) 침강확률 (p.482):

$$R_{set\,i} = f_{\tau i}\times \frac{F_{set\,i}}{H}$$
$$F_{set\,i} = \min\!\left(F'_{set\,i},\ \frac{C_{x\,i}\,H}{\Delta t}\right) \ (H\ge H_{min}),\quad F'_{set\,i}=F_{set0\,i}+s_i C_{x\,i}$$
$$f_{\tau i} = \begin{cases}1.0 & \tau=-1.0\\ \max\!\left(f_{\tau min\,i},\ 1-\dfrac{\tau}{\tau c_i}\right) & \text{else}\end{cases}$$

($s$ 침강속도 [m/d], $\tau$ 전단응력 [Pa], $\tau c$ 임계전단응력) (p.483). $\tau c\le0$이면 침강flux=0 (p.483). "buffer" 모델(Kessel et al. 2011)에서 flux를 S1/S2로 분배 가능 (p.483).

### 3.7 수온 TEMPERATUR (§14.1, p.534-535)

substance TEMPERATURE. 절대온도(SwitchTemp=0) 또는 잉여온도(=1) 모델링; Sweers (1976) 열교환계수 기반 (p.534).
$$dModTemp = -RcHeat\times FactRcHeat\times SurTemp + ZHeatExch$$
$$RcHeat = \frac{4.48 + 0.049T + F_{wind}(1.12 + 0.018T + 0.00158T^2)\times 86400}{C_p\,\rho_w\,Depth}$$
$$\rho_w = 1000.0 - 0.088T, \quad F_{wind} = 0.75(3.5 + 2.05\,V_{wind})$$

($V_{wind}$ 10 m 풍속) (p.534). 유효범위: 풍속 측정 한계 10–15 m/s, 온도 0–30 ℃; 표면온도는 0.5–1 m 상층 평균으로 정의 (p.535). 잉여온도 모델 시 배경온도는 시공간 상수여야 함 (p.535).

## 4. 운영·호환 정보

- **물-퇴적 상호작용 2방식** (§1.2, p.2): 단순 'S1-S2'(추가 substance가 2 퇴적층 표현, UI 지원) vs 고급 'layered sediment'(퇴적 격자 추가, Delft3D 전용, 별도 매뉴얼). 별도 명시 없으면 프로세스 기술은 수층·퇴적층 공통 (generic, p.2).
- **기술 포맷 2종** (§1.2, p.2): original format(불완전·파라미터 표 없음 가능) vs improved format(2000 이후, input/output 표 포함, 최신·고급 버전).
- **What's new / 하위호환** (§1.4, p.24-26): configuration(프로세스 sub-set) 개념 제거; state variable DetC/DetN/DetP/DetSi/OOC/OON/OOP/OOSi → POC1/PON1/POP1/POC2/PON2/POP2/Opal로 대체 (p.24); S1-S2 resuspension/burial/digging은 단일 프로세스 S12TraXXXX(+ Res_DM/Bur_DM/Dig_DM)로 통합 (p.24); biogenic silica는 DetSi/OOSi 2종 → Opal 단일로 통합(OOSi inflow 주의) (§1.6, p.26); 일부 프로세스가 chlorinity 대신 salinity 사용으로 전환 (p.26).
- **미수록/비표준 모듈** (§1.2, p.2-3): MICROPHYT(microphytobenthos), DEB(grazers, shellfish), aquatic macrophytes 모듈은 요청 시 제공. 사용자 정의 프로세스 추가는 open source 기능, 'Open Processes Library, User Manual' 참조 (p.3).

## 5. 미커버 영역 (추가 가치 시 후속)

- 9장 무기물질·pH (CO2 air-water exchange·탄산염 speciation·메탄·sulfide·iron) — 식 미인용 (TOC p.v).
- 4장 BLOOM/DYNAMO/PROTIST 성장식 상세 — [[delft3d_waq_algae_models]] 중복, 본 노트는 §4.1 3방식 개요(p.103)만. BLOOM·DYNAMO·PROTIST는 상호배타적 (p.103).
- 10·11장 micropollutant·중금속 partitioning, 7장 grazing(CONSBL/DEBGRZ), 5장 macrophytes, 13.5/13.6 flocculation, 15장 TRWP — 식 미인용 (TOC).
- 관련 매뉴얼 미정리: **Processes Library Tables** (프로세스 unique name 인덱스 Table 1.1-16.1, §1.3 p.3), **Input File Description** — 본 매뉴얼 범위 밖.

⚠ PDF 메타데이터 Title은 "Processes Library User Manual"이나 표지·헤더는 "Technical Reference Manual"로 표기 — 본 노트는 헤더 기준명 사용.
