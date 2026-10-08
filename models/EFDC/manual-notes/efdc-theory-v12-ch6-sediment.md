---
title: "EFDC+ Theory v12 Ch 6 SEDIMENT TRANSPORT — 식 level cross-walk (Original SedTran non-cohesive/cohesive/consolidation + SEDZLJ 매핑)"
topic: efdc-theory-v12-ch6-sediment
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf 본문 pp.72-95 (§6.1-§6.4.1, 물리 PDF p.85-108) 직접 추출 — 식 (6.1)~(6.110) + Fig 6.1-6.4 캡션 인용. §6.4 SEDZLJ 상세식(6.111~)은 source-analysis [[efdc_sedzlj]] 에 소스 직접 read 로 기커버 → 본 노트는 이론↔소스↔legacy(2003) cross-walk. primary sources: Hamrick 1992/Tetra Tech 2007b · van Rijn 1984 · Smith-McLean 1977 · Garcia-Parker 1991 · Krone/Partheniades · Mehta et al. 1989 · Hwang-Mehta 1989 · Ziegler-Nisbet 1994 · Jones-Lick 2000."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-04
verification_by: "Claude Opus 4.8 (1M context) — PDF Read pages 85-108 직접 + source-analysis/legacy cross-ref"
verification_date: 2026-07-04
related:
  - models/EFDC/manual-notes/efdc-theory-v12-ch2-hydrodynamics.md
  - models/EFDC/manual-notes/efdc-theory-v12-ch5-temperature-heat.md
  - models/EFDC/manual-notes/efdc-sediment-theory-2003.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
  - concepts/sediment-transport/02-theory.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC+ Theory v12 Ch 6 SEDIMENT TRANSPORT — 식 level cross-walk

> 출처: [`EFDC_Theory_Document_Ver_12.pdf`](../raw/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf) Chapter 6 (문서 pp.72-120, 본 노트는 §6.1-§6.4.1 = pp.72-95, 물리 PDF p.85-108), DSI LLC.
> **cross-walk 3축**: (a) 이론식 (본 노트) ↔ (b) 소스 [[efdc_sedzlj]](SEDZLJ branch 직접 read) + [[efdc_sediment]](Original SedTran dispatch) ↔ (c) legacy [[efdc-sediment-theory-2003]](Tetra Tech 2002/2003 Hamrick reference).
> Theory Ch-series: [[efdc-theory-v12-ch2-hydrodynamics]](수력)·[[efdc-theory-v12-ch5-temperature-heat]](온도) 에 이은 **Ch 6 유사이동**.

## 0. §6.1 두 모듈 (p.72)

EFDC+ 는 유사이동 **2 옵션**:

1. **EFDC (Original) Sediment Transport** — Hamrick's work (Tetra Tech 2007b). cohesive/non-cohesive **별도 계산 프로세스** (Fig 6.1). 각 class 사용자정의 상수 erosion rate.
2. **SEDZLJ** — SNL-EFDC 유래 (Jones-Lick 2000; Thanh et al. 2008; Ziegler-Lick 1988/1986). 응집성 무관 **통합 처리** (Fig 6.2). SEDFlume 측정 site-specific erosion rate → 공간변동.

ECIG는 NSEDFLUME=98·99를 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) R8.5.0 PDF는 0을 Original로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 1을 erosion rate lookup 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 2를 거듭제곱식과 core별 저층 물성 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 3을 거듭제곱식과 전체 저층 물성 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 prescan은 98·99를 1로 바꾼다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 INPUT은 원래 NSEDFLUME를 다시 읽는다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 INPUT에서 98·99를 다시 1로 바꾸는 대입을 찾지 못했다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) s_sedic의 변경 주석은 toxic 선택을 ISTRAN(5)>0으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽)

## 1. §6.2 Suspended Sediment Transport (pp.72-76) — 공통 프레임

### 1.1 §6.2.1 Governing Equations (pp.72-74)

generic transport Eq 3.1 의 유사 형태 (수평 물리확산항 생략 — 수치확산 작음). curvilinear-sigma (Eq 6.1):

$$\frac{\partial}{\partial t}(m_x m_y HC_j) + \frac{\partial}{\partial x}(m_y HuC_j) + \frac{\partial}{\partial y}(m_x HvC_j) + \frac{\partial}{\partial z}(m_x m_y wC_j) - \frac{\partial}{\partial z}(m_x m_y w_{s,j}C_j) = \frac{\partial}{\partial z}\left(\frac{m_x m_y}{H}A_b\frac{\partial}{\partial z}C_j\right) + S_{s,j}^E + S_{s,j}^I \quad (6.1)$$

$C_j$ = class $j$ 농도 (g/m³), $w_{s,j}$ = 침강속도, $A_b$ = 연직 eddy diffusivity, $S^E/S^I$ = external(point/non-point load)/internal(reactive decay·floc 형성/파괴 시 class간 교환) source-sink. 연직 BC (Eq 6.2-6.3):

$$-\frac{A_b}{H}\frac{\partial}{\partial z}C_j - w_{s,j}C_j = J_{o,j}\ \ \text{at}\ z=0; \qquad -\frac{A_b}{H}\frac{\partial}{\partial z}C_j - w_{s,j}C_j = 0\ \ \text{at}\ z=1 \quad (6.2,6.3)$$

$J_{o,j}$ = 수관-bed 순교환 flux (수관 방향 양). (cf. concept: [[concepts/sediment-transport/02-theory]] §3 Rouse.)

### 1.2 §6.2.2 Numerical Solution (pp.74-76) — fractional step 4단계

salinity 이동식과 동일 high-order upwind (Hamrick 1992), **fractional step** (Eq 6.4-6.12):

| step | 식 | 내용 |
|---|---|---|
| 1 advection+ext src | 6.4 | **MPDATA** anti-diffusive (Smolarkiewicz-Clark 1986) + optional FCT (Smolarkiewicz-Grabowski 1990) — [[efdc_transport_scheme]] CALTRAN_AD 대응 |
| 2 settling | 코드·문서 대조 | 코드는 위에서 아래로 암시적 침강을 계산한다. (`SedTran-Original/calsnd.f90:390` — `CLEFT = 1.+WSETA(L,K-1,NS)*WVEL`; `SedTran-Original/calsnd.f90:392` — `SND(L,K,NX) = CRIGHT/CLEFT`; `SedTran-Original/calsnd.f90:402` — `CRIGHT = max(SND(L,K,NX),0.)-SNDF(L,K,NX)*WVEL`; EFDC_Theory_Document_Ver_12.pdf, PDF 88쪽·인쇄 75쪽) PDF 식 6.6의 더하기 부호와 코드의 최상층 1+wsΔt/Hk 나눗셈을 구분한다. (`SedTran-Original/calsnd.f90:390` — `CLEFT = 1.+WSETA(L,K-1,NS)*WVEL`; `SedTran-Original/calsnd.f90:392` — `SND(L,K,NX) = CRIGHT/CLEFT`; EFDC_Theory_Document_Ver_12.pdf, PDF 88쪽·인쇄 75쪽, 식 6.6) PDF 식 6.7의 상층 유입항은 Δ1H를 쓰지만 코드는 현재 층 HPK를 쓴다. (`SedTran-Original/calsnd.f90:402` — `CRIGHT = max(SND(L,K,NX),0.)-SNDF(L,K,NX)*WVEL`; `SedTran-Original/calsnd.f90:403` — `SND(L,K,NX) = CRIGHT/CLEFT`; EFDC_Theory_Document_Ver_12.pdf, PDF 88쪽·인쇄 75쪽, 식 6.7) 비균등 층에서는 이 계수 차이를 보존해야 한다. (`SedTran-Original/calsnd.f90:402` — `CRIGHT = max(SND(L,K,NX),0.)-SNDF(L,K,NX)*WVEL`; `SedTran-Original/calsnd.f90:403` — `SND(L,K,NX) = CRIGHT/CLEFT`; EFDC_Theory_Document_Ver_12.pdf, PDF 88쪽·인쇄 75쪽) |
| 3 bed exchange | 6.9-6.11 | resuspension/deposition. non-cohesive $J_0^{***}=w_s(C_{eq}-C_1^{***})$ (6.10) / cohesive deposition $J_0^{***}=-P_d w_s C_1^{***}$ (6.11). flux limiter $L_o$ (6.9) = top bed layer 만 1 step 완전 재부유 |
| 4 vertical diffusion | 6.12 | implicit, bed·수면 zero diffusive flux |

## 2. §6.3 EFDC (Original) Sediment Transport Module (pp.77-95)

Fig 6.3 개념도 (bottom shear τbx/τby → erosion/bedload/suspended load → settling/deposition/consolidation). non-cohesive·cohesive 별도 프로세스.

### 2.1 §6.3.1 Non-Cohesive Sediment (pp.77-88)

#### (a) Settling velocity — van Rijn 1984 piecewise (Eq 6.13-6.18)


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽, 식 6.14; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽, 식 6.17; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽, 식 6.20)

$$w_{soj} = \sqrt{g'd_j}\begin{cases} R_{dj}/18, & d\le100\,\mu m \\ \frac{10}{R_{dj}}(\sqrt{1+0.01R_{dj}^2}-1), & 100<d_j\le1000\,\mu m \\ 1.1, & d_j>1000\,\mu m \end{cases} \quad (6.14)$$

100 μm와 1000 μm의 등호 소속은 문서와 코드가 다르다. (`SedTran-Original/setstvel.f90:28` — `if( D < 1.0E-4 )then`; `SedTran-Original/setstvel.f90:31` — `if( D >= 1.0E-4 .and. D < 1.E-3 )then`; `SedTran-Original/setstvel.f90:35` — `if( D >= 1.E-3 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽) 방해 침강은 현재 계급의 SDEN에 전체 SNDT를 곱한다. (`SedTran-Original/csndset.f90:21` — `CSNDSET = (1.-SDEN*SND)**ROPT`; `SedTran-Original/calsnd.f90:244` — `WSETA(L,K,NS) = WSEDO(NS)*CSNDSET(SNDT(L,K+1),SDEN(NS),ISNDVW)`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽) 문서의 계급별 역밀도 합과 같으려면 계급 밀도가 같아야 한다. (`SedTran-Original/csndset.f90:21` — `CSNDSET = (1.-SDEN*SND)**ROPT`; `SedTran-Original/calsnd.f90:244` — `WSETA(L,K,NS) = WSEDO(NS)*CSNDSET(SNDT(L,K+1),SDEN(NS),ISNDVW)`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽) Shields 구간 경계 4·10·20·150의 등호 소속도 문서와 코드가 다르다. (`SedTran-Original/setshld.f90:33` — `if(DSR <= 4.0 )then`; `SedTran-Original/setshld.f90:36` — `if(DSR > 4.0 .and. DSR <= 10.0 )then`; `SedTran-Original/setshld.f90:39` — `if(DSR > 10.0 .and. DSR <= 20.0 )then`; `SedTran-Original/setshld.f90:42` — `if(DSR > 20.0 .and. DSR <= 150.0 )then`; `SedTran-Original/setshld.f90:45` — `if(DSR > 150.0 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽)


100 μm와 1000 μm의 등호 소속은 문서와 코드가 다르다. (`SedTran-Original/setstvel.f90:28` — `if( D < 1.0E-4 )then`; `SedTran-Original/setstvel.f90:31` — `if( D >= 1.0E-4 .and. D < 1.E-3 )then`; `SedTran-Original/setstvel.f90:35` — `if( D >= 1.E-3 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽) 방해 침강은 현재 계급의 SDEN에 전체 SNDT를 곱한다. (`SedTran-Original/csndset.f90:21` — `CSNDSET = (1.-SDEN*SND)**ROPT`; `SedTran-Original/calsnd.f90:244` — `WSETA(L,K,NS) = WSEDO(NS)*CSNDSET(SNDT(L,K+1),SDEN(NS),ISNDVW)`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽) 문서의 계급별 역밀도 합과 같으려면 계급 밀도가 같아야 한다. (`SedTran-Original/csndset.f90:21` — `CSNDSET = (1.-SDEN*SND)**ROPT`; `SedTran-Original/calsnd.f90:244` — `WSETA(L,K,NS) = WSEDO(NS)*CSNDSET(SNDT(L,K+1),SDEN(NS),ISNDVW)`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽) Shields 구간 경계 4·10·20·150의 등호 소속도 문서와 코드가 다르다. (`SedTran-Original/setshld.f90:33` — `if(DSR <= 4.0 )then`; `SedTran-Original/setshld.f90:36` — `if(DSR > 4.0 .and. DSR <= 10.0 )then`; `SedTran-Original/setshld.f90:39` — `if(DSR > 10.0 .and. DSR <= 20.0 )then`; `SedTran-Original/setshld.f90:42` — `if(DSR > 20.0 .and. DSR <= 150.0 )then`; `SedTran-Original/setshld.f90:45` — `if(DSR > 150.0 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 91쪽·인쇄 78쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 92쪽·인쇄 79쪽)

#### (b) Critical Shields + transport mode (Eq 6.19-6.23)

$$\theta_{csj}=\frac{\tau_{csj}}{g'd_j}=\frac{u_{*csj}^2}{g'd_j}=f(R_{dj}) \quad (6.19)$$

van Rijn 1984 5-구간 numerical (Eq 6.20): $0.24(R_{dj}^{2/3})^{-1}$ / $0.14(\cdot)^{-0.64}$ / $0.04(\cdot)^{-0.1}$ / $0.013(\cdot)^{0.29}$ / $0.055$. transport mode by bed shear velocity $u_*=\sqrt{\tau_b}$ (6.21): $u_*<u_{*csj}$ 무이동(deposit) / $u_{*csj}<u_*<w_{soj}$ **bedload** (6.23) / $u_*>w_{soj}$ **suspended**. (임계 130 μm — Fig 6.4 교점.)

#### (c) Bedload — general Φ + 5 formulation (Eq 6.24-6.35)

$$\frac{q_B}{\rho_s d\sqrt{g'd}}=\Phi(\theta,\theta_{cs}); \quad \theta=\frac{\tau_b}{g'd_j}=\frac{u_*^2}{g'd_j} \quad (6.24,6.25)$$

일반형 $\Phi=\phi(\theta-\theta_{cs})^\alpha(\sqrt\theta-\gamma\sqrt{\theta_{cs}})^\beta$ (6.26), $\phi=0.053/(R_d^{1/5}\theta_{cs}^{2.1})$ (6.27, van Rijn 1984). α/β/γ 사용자정의 → **5 공식**: van Rijn 1984 (6.28) · Engelund-Hansen 1967 (6.29) · **Meyer-Peter-Müller 1948** (6.30) · Bagnold 1956 (6.31) · Wu et al. 2000 (6.32). [riverine Ackers-White/Laursen/Yang 은 (6.25) 부적합 → 미포함.] bedload flux 벡터화 (6.33) + upwind cell-face (6.34) + bed 순제거율 $J_b$ (6.35, 4면 compass).

#### (d) Suspended load — Rouse equilibrium concentration (Eq 6.36-6.71)

near-bed 평형농도 개념. Eq 6.36-6.48 로 Rouse 프로파일 유도: Rouse number $R=w_s/(u_*\kappa)$ (6.45), $C=(z_{eq}/z)^R C_{eq}-J_o/w_s$ (6.48), 순 flux $J_o=w_s(C_{eq}-C_{ne})$ (6.49), 층평균 $J_o=w_s(\bar C_{eq}-\bar C)$ (6.51). depth-avg 2D 확장 (6.55-6.63).

**평형농도 $C_{eq}=C_{eq}(d,\rho_s,\rho_w,w_s,u_*,\nu)$ (6.64)** — 3 옵션 (Garcia-Parker 1991 리뷰):
- **Smith-McLean 1977** (6.65): $C_{eq}=\rho_s\frac{0.65\gamma_o T}{1+\gamma_o T}$, $\gamma_o=2.4\times10^{-3}$, $T=(\tau_b-\tau_{cs})/\tau_{cs}$ (6.66)
- **van Rijn 1984** (6.67): $C_{eq}=0.015\rho_s\frac{d}{z_{eq}^*}T^{3/2}R_d^{-1/5}$
- **Garcia-Parker 1991** (6.68-6.71): $C_{jeq}=\rho_s\frac{A(\lambda Z_j)^5}{1+3.33A(\lambda Z_j)^5}$, $A=1.3\times10^{-7}$ — **straining $\lambda$ + hiding $F_H$ factor** 로 **armoring**(multi-class) 표현. 단일 class 시 λ=F_H=1.

### 2.2 §6.3.2 Cohesive Sediments (pp.88-92)

#### (a) Settling — floc, 4 옵션 (Eq 6.72-6.82)

응집(flocculation) 반영. 일반형 $w_{se}=w_{se}(d,C,du/dz,q)$ (6.72):
- 식 6.73의 유리함수 대신 코드 IOPT=1은 log10 농도의 가우스형 지수식을 쓴다. (`SedTran-Original/csedset.f90:38` — `TMPSED = SED/2000.`; `SedTran-Original/csedset.f90:39` — `TMP = LOG10(TMPSED)`; `SedTran-Original/csedset.f90:40` — `TMP = -16.*TMP*TMP/9.`; `SedTran-Original/csedset.f90:41` — `TMP = 10.**TMP`; EFDC_Theory_Document_Ver_12.pdf, PDF 101쪽·인쇄 88쪽, 식 6.73)
- 식 6.74의 좌변 cws 표기는 원문이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 102쪽·인쇄 89쪽, 식 6.74) 코드는 반올림 전 계수와 /3600을 사용한다. (`SedTran-Original/csedset.f90:59` — `RNG     = 1.11075 + 0.0386*SHEAR`; `SedTran-Original/csedset.f90:60` — `BG      = EXP( -4.20706 + 0.1465*SHEAR )`; `SedTran-Original/csedset.f90:62` — `CSEDSET = WTMP/3600.`; EFDC_Theory_Document_Ver_12.pdf, PDF 101쪽·인쇄 88쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 102쪽·인쇄 89쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 104쪽·인쇄 91쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 105쪽·인쇄 92쪽) 전단 G의 직접 차분은 파랑 조건에서만 사용한다. (`SedTran-Original/calsed.f90:123` — `STRESS = QQ(L,0)/CTURB2`; `SedTran-Original/calsed.f90:154` — `SHEAR = HPI(L)*SQRT( DZIGSD4U(L,K) )*SQRT( (U(LEC(L),K+1)-U(LEC(L),K)+U(L,K+1)-U(L,K))**2  &`; `SedTran-Original/calsed.f90:155` — `+ (V(LNC(L),K+1)-V(LNC(L),K)+V(L,K+1)-V(L,K))**2 )`; EFDC_Theory_Document_Ver_12.pdf, PDF 101쪽·인쇄 88쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 102쪽·인쇄 89쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 104쪽·인쇄 91쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 105쪽·인쇄 92쪽)
- **Opt3 Ziegler-Nisbet 1994** (6.77-6.80): $w_s=a d_f^b$, floc diameter $d_f=\sqrt{\alpha_f/(C\sqrt{\tau_{xz}^2+\tau_{yz}^2})}$
- **Opt4 generalized** (6.81-6.82): $C'=\tau C$ 3-구간 power-law

#### (b) Deposition — Krone (Eq 6.83)

$$J_o^d=\begin{cases} -w_s C_d\left(\frac{\tau_{cd}-\tau_b}{\tau_{cd}}\right)=-w_s P_d C_d, & \tau_b<\tau_{cd} \\ 0, & \tau_b\ge\tau_{cd} \end{cases} \quad (6.83)$$

작은 입경의 Krone는 τ≤TCRSUS에서만 1−τ/TCRSUS이다. (`SedTran-SEDZLJ/s_sedzlj.f90:150` — `elseif( TAU(L) <= TCRSUS(NS) )then`; `SedTran-SEDZLJ/s_sedzlj.f90:151` — `PROB(NS) = ONE - TAU(L)/(TCRSUS(NS))                          ! *** Krones deposition probability is calculated`; `SedTran-SEDZLJ/s_sedzlj.f90:153` — `PROB(NS) = 0.0                                                ! *** Zero probability when TAU > TCRSUS`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 식 6.130의 비교 연산자 누락과 조건은 코드와 다르다. (`SedTran-SEDZLJ/s_sedzlj.f90:150` — `elseif( TAU(L) <= TCRSUS(NS) )then`; `SedTran-SEDZLJ/s_sedzlj.f90:151` — `PROB(NS) = ONE - TAU(L)/(TCRSUS(NS))                          ! *** Krones deposition probability is calculated`; `SedTran-SEDZLJ/s_sedzlj.f90:153` — `PROB(NS) = 0.0                                                ! *** Zero probability when TAU > TCRSUS`; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽, 식 6.130) BEDLOAD_CUTOFF는 사용자 입력이며 10 μm 미만 입력을 64 μm로 보정한다. (`SedTran-SEDZLJ/s_sedic.f90:701` — `if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) BEDLOAD_CUTOFF는 고정 200 μm가 아니다. (`SedTran-SEDZLJ/s_sedic.f90:701` — `if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 부유 분율의 영 조건은 TCRE와 TCRSUS의 차이를 반영한다. (`SedTran-SEDZLJ/s_bedload.f90:121` — `if( TAU(L) <= TCRE(NS) .or. USW(L,NS) <= 0.0 )then`; `SedTran-SEDZLJ/s_bedload.f90:126` — `PSUS(L,NS) = max((LOG(USW(L,NS))-LOG(SQRT(TCRSUS(NS))/DWS(NS)))/(LOG(4.0)-LOG(SQRT(TCRSUS(NS))/DWS(NS))),0.0)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽)

#### (c) Erosion — surface/mass, Partheniades-type (Eq 6.84-6.90)

mass erosion(τb>depth-varying 강도 τs, 급속) vs surface erosion(점진). surface (Eq 6.84-6.85):


문서 원문 (EFDC_Theory_Document_Ver_12.pdf, PDF 101쪽·인쇄 88쪽, 식 6.73; EFDC_Theory_Document_Ver_12.pdf, PDF 102쪽·인쇄 89쪽, 식 6.74; EFDC_Theory_Document_Ver_12.pdf, PDF 102쪽·인쇄 89쪽, 식 6.76; EFDC_Theory_Document_Ver_12.pdf, PDF 104쪽·인쇄 91쪽, 식 6.85; EFDC_Theory_Document_Ver_12.pdf, PDF 105쪽·인쇄 92쪽, 식 6.87)

$$J_o^r=w_r C_r=\frac{dm_e}{dt}\left(\frac{\tau_b-\tau_{ce}}{\tau_{ce}}\right)^\alpha\ \text{or}\ \frac{dm_e}{dt}\exp\left(-\beta\left(\frac{\tau_b-\tau_{ce}}{\tau_{ce}}\right)^\gamma\right),\quad \tau_b\ge\tau_{ce} \quad (6.84,6.85)$$

초과응력의 음의 지수 침식식 6.85를 찾지 못했다. (`SedTran-Original/csedress.f90:49` — `TMPVAL = (1.+VDRO)/(1.+VDR)`; `SedTran-Original/csedress.f90:50` — `FACTOR = EXP(-TMPVAL)`; `SedTran-Original/csedress.f90:51` — `CSEDRESS = FACTOR*WRSPO*(1.+VDRO)/(1.+VDR)`; EFDC_Theory_Document_Ver_12.pdf, PDF 104쪽·인쇄 91쪽, 식 6.85) CSEDRESS의 지수는 간극비 보정이다. (`SedTran-Original/csedress.f90:49` — `TMPVAL = (1.+VDRO)/(1.+VDR)`; `SedTran-Original/csedress.f90:50` — `FACTOR = EXP(-TMPVAL)`; `SedTran-Original/csedress.f90:51` — `CSEDRESS = FACTOR*WRSPO*(1.+VDRO)/(1.+VDR)`; EFDC_Theory_Document_Ver_12.pdf, PDF 101쪽·인쇄 88쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 102쪽·인쇄 89쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 104쪽·인쇄 91쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 105쪽·인쇄 92쪽)


식 6.87의 임계 밀도 이하 값은 코드에서 1E−12이다. (`SedTran-Original/csedtaus.f90:31` — `if( BULKDEN <= 1.065 )then`; `SedTran-Original/csedtaus.f90:32` — `CSEDTAUS = 1.0E-12`; EFDC_Theory_Document_Ver_12.pdf, PDF 105쪽·인쇄 92쪽, 식 6.87)

### 2.3 §6.3.3 Consolidation of Mixed Beds (pp.92-95, Eq 6.91-6.110)

Gibson 혼합층 압밀은 문서의 유도식이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽) 현재 CALBED의 IBMECH=1은 전체 VDRBED를 최소 간극비로 지수 완화한다. (`SedTran-Original/calbed.f90:96` — `TMPEXP = EXP(-DTSED/SEDVRDT)`; `SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`; EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽) 부분 간극비·혼합 투수계수·유효응력 기울기를 푸는 경로는 찾지 못했다. (`SedTran-Original/calbed.f90:96` — `TMPEXP = EXP(-DTSED/SEDVRDT)`; `SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`; EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽) 식 6.108·6.109의 체적 보존 대응과 Darcy 해법의 존재를 구분한다. (`SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`; `SedTran-Original/calbed.f90:106` — `HBED(L,K) = TMPTOP*HBED1(L,K)/TMPBOT`; `SedTran-Original/calbed.f90:185` — `QWTRBED(L,K) = QWTRBED(L,K-1) - DELTI*TMPVAL*(VDRBED(L,K)-VDRBED1(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽, 식 6.108; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽, 식 6.109)

## 3. §6.4 SEDZLJ — source-analysis 매핑 (pp.95-120)

§6.4 이론(6.111~ Eq)의 상세는 **소스 직접 read** 로 [[efdc_sedzlj]] 에 기커버 (7 sub-routine 2019 lines). 본 노트는 이론식↔소스 대응만:

| Theory v12 §6.4 | source-analysis [[efdc_sedzlj]] | 핵심 |
|---|---|---|
| §6.4.1 Background (p.95) | §Scope | hindcast erosion/deposition 비유일성 → SEDFlume 직접측정 동기 |
| §6.4.2 Bed Shear Stress (p.97) | §3 `s_shear.f90` | Christoffersen-Jonsson 1985 wave-current (Eq 3.8/3.10/4.11/4.12/4.23/4.25) |
| §6.4.3 Erosion Rate (p.98) | 코드·문서 대조 | R8.5.0 PDF의 NSEDFLUME=2·3은 거듭제곱식 방식이다. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 s_sedzlj는 NSEDFLUME=1에서 lookup 값을 사용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 s_sedzlj의 그 밖의 분기는 거듭제곱식을 사용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:535` — `ERATEMOD = (SN00*EXP(SN11*LOG(ERATEND(NSC0,NTAU0)) + SN01*LOG(ERATEND(NSC1,NTAU0))) + SN10*EXP(SN11*LOG(ERATEND(NSC0,NTAU1)) +  &   ! *** log-linear interpolation`; `SedTran-SEDZLJ/s_sedzlj.f90:539` — `SN00 = ACTDEPA(NSC0)*(0.1*TAU(L))**ACTDEPN(NSC0)                             ! *** Erosion rate 1 (cm/s)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 98은 현재 표준 거듭제곱식 번호로 확인하지 않음. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:535` — `ERATEMOD = (SN00*EXP(SN11*LOG(ERATEND(NSC0,NTAU0)) + SN01*LOG(ERATEND(NSC1,NTAU0))) + SN10*EXP(SN11*LOG(ERATEND(NSC0,NTAU1)) +  &   ! *** log-linear interpolation`; `SedTran-SEDZLJ/s_sedzlj.f90:539` — `SN00 = ACTDEPA(NSC0)*(0.1*TAU(L))**ACTDEPN(NSC0)                             ! *** Erosion rate 1 (cm/s)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) |
| §6.4.4 Suspended Load (p.104) | §2.1-2.3 | Gessler 1965 / Krone deposition probability |
| §6.4.5 Bedload (p.105) | §5 `s_bedload.f90` | Van Rijn 1981 (Eq 20a/20b/21) |
| §6.4.6 Bed Armoring (p.107) | §2.4-2.8 | active layer TACT + layer reconstitution |
| (bed slope) | §4 `s_slope.f90` | Lick 2009 Eq 3.36 SH_SCALE |

> **Original vs SEDZLJ 알고리즘 대비** (theory-doc-v12 §4.1 후보 `efdc-sedzlj-vs-sedtran-comparison` 부분충족): Original = van Rijn 1984 평형농도(Rouse) + class별 상수 erosion / SEDZLJ = SEDFlume 직접측정 erosion rate + 통합 multi-class active-layer. 공통 = Eq 6.1 부유이동 + van Rijn bedload 계열.

## 4. Ch 6 소스/legacy 매핑 요약

| 매뉴얼 § | 이론식 | 소스/legacy |
|---|---|---|
| §6.2 부유이동 (공통) | 6.1-6.12 | [[efdc_transport_scheme]] CALTRAN/CALTRAN_AD (MPDATA) |
| §6.3.1 non-cohesive | 6.13-6.71 | Original SedTran ([[efdc_sediment]]), legacy [[efdc-sediment-theory-2003]] §6 |
| §6.3.2 cohesive | 6.72-6.90 | Krone/Partheniades — legacy 2003 §7, SEDZLJ Gessler-Krone [[efdc_sedzlj]] §2.1 |
| §6.3.3 consolidation | 코드·문서 대조 | Gibson 혼합층 압밀은 문서의 유도식이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽) 현재 CALBED의 IBMECH=1은 전체 VDRBED를 최소 간극비로 지수 완화한다. (`SedTran-Original/calbed.f90:96` — `TMPEXP = EXP(-DTSED/SEDVRDT)`; `SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`; EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽) 부분 간극비·혼합 투수계수·유효응력 기울기를 푸는 경로는 찾지 못했다. (`SedTran-Original/calbed.f90:96` — `TMPEXP = EXP(-DTSED/SEDVRDT)`; `SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`; EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽) 식 6.108·6.109의 체적 보존 대응과 Darcy 해법의 존재를 구분한다. (`SedTran-Original/calbed.f90:103` — `VDRBED(L,K)  = SEDVDRM + (VDRBED1(L,K)-SEDVDRM)*TMPEXP`; `SedTran-Original/calbed.f90:106` — `HBED(L,K) = TMPTOP*HBED1(L,K)/TMPBOT`; `SedTran-Original/calbed.f90:185` — `QWTRBED(L,K) = QWTRBED(L,K-1) - DELTI*TMPVAL*(VDRBED(L,K)-VDRBED1(L,K))`; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽, 식 6.108; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽, 식 6.109) |
| §6.4 SEDZLJ | 6.111~ | [[efdc_sedzlj]] 소스 직접 (Card C36 NSEDFLUME) |

## 5. 관련

- [[efdc_sedzlj]] — SEDZLJ branch 소스 직접 read (본 노트가 이론↔소스 매핑한 대상)
- [[efdc-sediment-theory-2003]] — Tetra Tech 2002/2003 Hamrick legacy reference (§6.3 Original 의 원전)
- [[efdc-theory-v12-ch2-hydrodynamics]] · [[efdc-theory-v12-ch5-temperature-heat]] — Theory Ch-series 연속
- `concepts/sediment-transport/02-theory.md` — Shields/Rouse/settling 도메인 관점 (Soulsby 1997 cross)
- **Primary sources**: Hamrick 1992 / Tetra Tech 2007b · van Rijn 1984 · Smith-McLean 1977 · Garcia-Parker 1991 · Meyer-Peter-Müller 1948 · Krone / Partheniades · Mehta et al. 1989 · Hwang-Mehta 1989 · Shrestha-Orlob 1996 · Ziegler-Nisbet 1994 · Sanford-Maa 2001 · Jones-Lick 2000 · Ziegler-Lick 1988/1986.
