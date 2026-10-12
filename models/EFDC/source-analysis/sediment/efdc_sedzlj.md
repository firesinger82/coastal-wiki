---
title: "efdc SEDZLJ sediment transport (s_main / s_sedzlj / s_shear / s_slope / s_bedload)"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable raw source 직접 read (models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/), Card C36 매뉴얼 페이지 (models/EFDC/raw/manuals/confluence/spaces/ECIG/.../Card_Image_36.md) 직접 인용. Theory v12 §6.4 SEDZLJ cross-ref (manual-notes/efdc-theory-doc-v12.md:136), legacy 비교는 efdc-sediment-theory-2003.md."
note_author: "Claude Opus 4.7 (1M context) source-code 직접 read"
note_date: 2026-05-28
verification_by: "사용자 + Claude source-code direct read"
verification_date: 2026-05-28
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

## Scope

<a id="cv-e-body-29-16"></a>ECIG는 NSEDFLUME=98·99를 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) R8.5.0 PDF는 0을 Original로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 1을 erosion rate lookup 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 2를 거듭제곱식과 core별 저층 물성 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 3을 거듭제곱식과 전체 저층 물성 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 prescan은 `if( ISTRAN(6) > 0 )then` 안에서 NSEDFLUME=98·99를 1로 바꾼다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) (`mod_scaninp.f90:381` — `if( ISTRAN(6) > 0 )then`) [10-12 전수 검증 보완] 현재 INPUT은 원래 NSEDFLUME를 다시 읽는다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 INPUT에서 98·99를 다시 1로 바꾸는 대입을 찾지 못했다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) s_sedic의 변경 주석은 toxic 선택을 ISTRAN(5)>0으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 판정·근거: [정본 §5 행 878, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436](../../manual-notes/efdc-user-manual-r850.md#cv-e-input-2567). [10-12 결론 검증 보완]

## Source basis

- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_main.f90` (359 lines) — SEDZLJ_MAIN driver.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90` (917 lines) — 핵심 erosion/deposition + active-layer 관리.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90` (340 lines) — wave-current bottom shear (Christoffersen-Jonsson 1985).
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_slope.f90` (110 lines) — bed slope shear amplification (Lick 2009).
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90` (293 lines) — Van Rijn 1981 bedload transport.
- `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90` (769 lines) — bed initial condition (별도 covered).
- `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md` — Card C36 `NSEDFLUME` flag 정의.
- `models/EFDC/manual-notes/efdc-theory-doc-v12.md:47, 136, 177-179, 199` — Theory v12 §6.4 SEDZLJ TOC + Craig Jones contributor.
- `models/EFDC/manual-notes/efdc-sediment-theory-2003.md:104, 155, 169, 183` — Hamrick 2003 legacy SedTran 비교.

## 1. SEDZLJ_MAIN driver (`s_main.f90`)

```fortran
! s_main.f90:54-60
call SEDZLJ_SHEAR            ! *** wave-current bottom shear stress TAU(L)
if( ISSLOPE ) call SEDZLJ_SLOPE   ! *** bed slope adjustment
if( ICALC_BL > 0 )then       ! *** Bedload active
  call BEDLOADJ              ! *** Van Rijn transport
endif
```

```fortran
! s_main.f90:150 (per cell loop)
call SEDZLJ(L)               ! *** erosion + deposition + active layer + mass balance
```

### Dispatch 조건

`s_main.f90:64`:
```fortran
if( NSEDFLUME > 0 )then
```

Card C36 `NSEDFLUME`:
- **0** = EFDC main sediment functions (SedTran-Original, [[efdc_sediment]] §C-D)
- 본문 대조: [정본](efdc_sedzlj.md#cv-e-body-29-16). 판정·근거: [정본 §5 행 878, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436](../../manual-notes/efdc-user-manual-r850.md#cv-e-input-2567). [10-12 결론 검증 보완]
- 본문 대조: [정본](efdc_sedzlj.md#cv-e-body-29-16). 판정·근거: [정본 §5 행 878, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436](../../manual-notes/efdc-user-manual-r850.md#cv-e-input-2567). [10-12 결론 검증 보완]

### Settling (anti-diffusion, KC > 1)

`s_main.f90:96-136` — vertical layer-by-layer settling solve.
`s_main.f90:234-345` — `ISTOPT(6) > 0` 시 anti-diffusion tridiagonal solver (TVAR1S/W/N/E + TVAR2/3 working arrays). Thomas algorithm 형태.

### Bedload BC handling

`s_main.f90:158-230` — `NSBDLDBC > 0` 시 bedload outflow/recirculation BC. `LSBLBCU` (upstream) → `LSBLBCD` (downstream) cell 간 bedload mass 이송.

## 2. SEDZLJ erosion/deposition core (`s_sedzlj.f90`)

`SEDZLJ(L)` — 단일 cell `L` 기준 시간 step 처리.

### 2.1 Suspended load deposition probability (line 134-154)

코드는 `if( CTB(NS) < 1.0E-20 ) CYCLE`을 지나 후류 침식이 없는 `elseif( D50(NS) >= BEDLOAD_CUTOFF )then`에서 Gessler의 정규 누적분포 근사를 계산한다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) (`SedTran-SEDZLJ/s_sedzlj.f90:131` — `if( CTB(NS) < 1.0E-20 ) CYCLE`; `SedTran-SEDZLJ/s_sedzlj.f90:135` — `if( PROP_ERO(L,0) > 0. )then`; `SedTran-SEDZLJ/s_sedzlj.f90:138` — `elseif( D50(NS) >= BEDLOAD_CUTOFF )then`) [10-12 전수 검증 보완] 식 6.131의 erf(Y/2)와 다르다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽, 식 6.131) Y=0의 코드 값은 약 0.5이고 문서 값은 0이다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 다항 첫 계수는 코드 0.43618이고 문서 0.4632이다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 작은 입경의 Krone 분기는 앞선 후류 침식 조건을 통과하지 않고 `elseif( TAU(L) <= TCRSUS(NS) )then`일 때 `PROB(NS) = ONE - TAU(L)/(TCRSUS(NS))`를 계산한다. (`SedTran-SEDZLJ/s_sedzlj.f90:150` — `elseif( TAU(L) <= TCRSUS(NS) )then`; `SedTran-SEDZLJ/s_sedzlj.f90:151` — `PROB(NS) = ONE - TAU(L)/(TCRSUS(NS))                          ! *** Krones deposition probability is calculated`; `SedTran-SEDZLJ/s_sedzlj.f90:153` — `PROB(NS) = 0.0                                                ! *** Zero probability when TAU > TCRSUS`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) (`SedTran-SEDZLJ/s_sedzlj.f90:150` — `elseif( TAU(L) <= TCRSUS(NS) )then`) [10-12 전수 검증 보완] 식 6.130의 비교 연산자 누락과 조건은 코드와 다르다. (`SedTran-SEDZLJ/s_sedzlj.f90:150` — `elseif( TAU(L) <= TCRSUS(NS) )then`; `SedTran-SEDZLJ/s_sedzlj.f90:151` — `PROB(NS) = ONE - TAU(L)/(TCRSUS(NS))                          ! *** Krones deposition probability is calculated`; `SedTran-SEDZLJ/s_sedzlj.f90:153` — `PROB(NS) = 0.0                                                ! *** Zero probability when TAU > TCRSUS`; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽, 식 6.130) BEDLOAD_CUTOFF는 사용자 입력이며 10 μm 미만 입력을 64 μm로 보정한다. (`SedTran-SEDZLJ/s_sedic.f90:701` — `if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) BEDLOAD_CUTOFF는 고정 200 μm가 아니다. (`SedTran-SEDZLJ/s_sedic.f90:701` — `if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 부유 분율의 영 조건은 TCRE와 TCRSUS의 차이를 반영한다. (`SedTran-SEDZLJ/s_bedload.f90:121` — `if( TAU(L) <= TCRE(NS) .or. USW(L,NS) <= 0.0 )then`; `SedTran-SEDZLJ/s_bedload.f90:126` — `PSUS(L,NS) = max((LOG(USW(L,NS))-LOG(SQRT(TCRSUS(NS))/DWS(NS)))/(LOG(4.0)-LOG(SQRT(TCRSUS(NS))/DWS(NS))),0.0)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 앞선 `if( PROP_ERO(L,0) > 0. )then` 분기는 `PROB(NS) = 0.0`을 대입한다. (`SedTran-SEDZLJ/s_sedzlj.f90:135` — `if( PROP_ERO(L,0) > 0. )then`; `SedTran-SEDZLJ/s_sedzlj.f90:136` — `PROB(NS) = 0.0`) [10-12 전수 검증 보완] 그 ELSE는 `PROB(NS) = 0.0`을 대입한다. (`SedTran-SEDZLJ/s_sedzlj.f90:153` — `PROB(NS) = 0.0`) [10-12 전수 검증 보완] 부유 분율 PSUS의 영 조건과 로그식은 `if( USW(L,NS) < 4.0 )then` 안에 속한다. (`SedTran-SEDZLJ/s_bedload.f90:120` — `if( USW(L,NS) < 4.0 )then`) [10-12 전수 검증 보완] 그 ELSE는 `PSUS(L,NS) = 1.0`을 대입한다. (`SedTran-SEDZLJ/s_bedload.f90:130` — `PSUS(L,NS) = 1.0`) [10-12 전수 검증 보완] <a id="cv-e-hydro-716"></a>결론: 코드 결함 후보. SEDZLJ는 독립 입력한 임계응력과 침강속도에서 부유 분율 PSUS가 1을 넘을 수 있어 코드 결함 후보이다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:19` — `\dfrac{q_s}{q_t}=\begin{cases}0,&\tau^b<\tau_{cs}\\\dfrac{\ln(u_*/w_s)-\ln\left(\sqrt{\tau_{cs}/\rho_w}/w_s\right)}{\ln(4)-\ln\left(\sqrt{\tau_{cs}/\rho_w}/w_s\right)},&\tau^b>\tau_{cs}\ \text{and }\dfrac{u_*}{w_s}<4\\1,&\dfrac{u_*}{w_s}>4\end{cases}`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:120` — `if( USW(L,NS) < 4.0 )then                                 ! *** "USW(L,NS) < 4.0" is an out of range check`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:121` — `if( TAU(L) <= TCRE(NS) .or. USW(L,NS) <= 0.0 )then`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:126` — `PSUS(L,NS) = max((LOG(USW(L,NS))-LOG(SQRT(TCRSUS(NS))/DWS(NS)))/(LOG(4.0)-LOG(SQRT(TCRSUS(NS))/DWS(NS))),0.0)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:130` — `PSUS(L,NS) = 1.0`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:448` — `DWS(K) = DWSIN(K)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:683` — `TEMP = (ONE-PSUS(L,NS))*ETOT(NS)                      ! *** Calculate erosion into bedload             (g/cm^2)`; [EFDC-theory-hydro-vs-code §5 행 eq-6-124](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:716)) <a id="cv-e-hydro-717"></a>결론: 문서 오기. 이론 문서 식 6.130의 조건은 오기이며 코드는 임계응력 이하에서 1−τ/τc를 적용하고 그 위에서 0을 사용한다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:21` — `P_j=\begin{cases}0&\text{for }\tau^b\tau_{cs,j}\\\left(1-\dfrac{\tau^b}{\tau_{cs,j}}\right)&\text{for }\tau^b>\tau_{cs,j}\end{cases}`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:150` — `elseif( TAU(L) <= TCRSUS(NS) )then`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:151` — `PROB(NS) = ONE - TAU(L)/(TCRSUS(NS))                          ! *** Krones deposition probability is calculated`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:153` — `PROB(NS) = 0.0                                                ! *** Zero probability when TAU > TCRSUS`; [EFDC-theory-hydro-vs-code §5 행 eq-6-130](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:717)) <a id="cv-e-hydro-718"></a>결론: 문서 오기. SEDZLJ는 정규 누적확률을 근사하며 문서의 erf(Y/2)와 다항 계수 0.4632는 이 확률 정의와 모순된다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:21` — `P_j(Y)=\operatorname{erf}\left(\dfrac{Y}{2}\right)=\dfrac{2}{\sqrt{\pi}}\displaystyle\int_0^{Y/2}\exp(-\xi^2)\,\mathrm{d}\xi`<br>`_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:22` — `P_j=1-F(Y)(0.4632X-0.1202X^2+0.9373X^3)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:139` — `PY  = 1.7544*(TCRSUS(NS)/(TAU(L) + 1.0D-18)-ONE)              ! *** 1.7544 = 1/sigma =  1./0.57 from Gessler`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; [EFDC-theory-hydro-vs-code §5 행 eq-6-131, eq-6-133](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:718)) [10-12 결론 검증 보완]

```fortran
! s_sedzlj.f90:139-149
PY  = 1.7544 * (TCRSUS(NS)/(TAU(L) + 1e-18) - 1)   ! *** 1.7544 = 1/0.57 from Gessler
if( PY >= 0.0 )then
  PFY = SQR2PI*EXP(-0.5*PY*PY)                     ! *** Normal PDF
  PX  = ONE/(ONE + 0.33267*PY)
  PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX² + 0.93729*PX³)
else
  PY  = ABS(PY)
  ...
  PROB(NS) = PFY*(0.43618*PX - 0.12016*PX² + 0.93729*PX³)
endif
```

코드는 `if( CTB(NS) < 1.0E-20 ) CYCLE`을 지나 후류 침식이 없는 `elseif( D50(NS) >= BEDLOAD_CUTOFF )then`에서 Gessler의 정규 누적분포 근사를 계산한다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) (`SedTran-SEDZLJ/s_sedzlj.f90:131` — `if( CTB(NS) < 1.0E-20 ) CYCLE`; `SedTran-SEDZLJ/s_sedzlj.f90:135` — `if( PROP_ERO(L,0) > 0. )then`; `SedTran-SEDZLJ/s_sedzlj.f90:138` — `elseif( D50(NS) >= BEDLOAD_CUTOFF )then`) [10-12 전수 검증 보완] 식 6.131의 erf(Y/2)와 다르다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽, 식 6.131) Y=0의 코드 값은 약 0.5이고 문서 값은 0이다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 다항 첫 계수는 코드 0.43618이고 문서 0.4632이다. (`SedTran-SEDZLJ/s_sedzlj.f90:141` — `PFY = SQR2PI*EXP(-0.5d0*PY*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:142` — `PX  = ONE/(ONE + 0.33267*PY)`; `SedTran-SEDZLJ/s_sedzlj.f90:143` — `PROB(NS) = ONE - PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; `SedTran-SEDZLJ/s_sedzlj.f90:148` — `PROB(NS) = PFY*(0.43618*PX - 0.12016*PX*PX + 0.93729*PX**3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 117쪽·인쇄 104쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽) 앞선 `if( PROP_ERO(L,0) > 0. )then` 분기는 `PROB(NS) = 0.0`을 대입한다. (`SedTran-SEDZLJ/s_sedzlj.f90:135` — `if( PROP_ERO(L,0) > 0. )then`; `SedTran-SEDZLJ/s_sedzlj.f90:136` — `PROB(NS) = 0.0`) [10-12 전수 검증 보완] 판정·근거: [정본 §5 행 eq-6-131, eq-6-133](efdc_sedzlj.md#cv-e-hydro-718). [10-12 결론 검증 보완]

**Krone** for $D_{50} <$ `BEDLOAD_CUTOFF` (≈ 200 μm):

```fortran
! s_sedzlj.f90:150-153
elseif( TAU(L) <= TCRSUS(NS) )then
  PROB(NS) = ONE - TAU(L)/TCRSUS(NS)               ! *** Krone (1962)
else
  PROB(NS) = 0.0
endif
```

### 2.2 Deposition flux

```fortran
! s_sedzlj.f90:158
DEPTSS(NS) = CTB(NS) * PROB(NS) * (DWS(NS) * DTSEDJ)
! *** CTB = bottom-layer concentration (g/cm³)
! *** DWS = settling velocity (cm/s)
! *** DTSEDJ = SEDZLJ time step (s)
```

`MAXDEPLIMIT` (line 157) 으로 layer 1 의 전 sediment mass 초과 deposition 차단.

### 2.3 Bedload deposition — Van Rijn equilibrium probability

```fortran
! s_sedzlj.f90:191-201
CSEDVR(NS) = 0.18*2.65*TRANS(L,NS)/DISTAR(NS)*0.65    ! *** Van Rijn 1981 Eq 21 equilibrium bedload conc
PROBVR(NS) = MIN(CSEDSS/CSEDVR(NS), 1.0)              ! *** Van Rijn deposition probability
DEPBL(NS)  = PROBVR(NS) * CBL(L,NS) * DWS(NS) * DTSEDJ
```

코드는 기존 소류사 질량을 `SMASS(NS) = CBL(L,NS)`로 읽고 확률비의 분자 농도를 `CSEDSS = SMASS(NS)/(DWS(NS)*DTSEDJ)`로 계산한다. (`SedTran-SEDZLJ/s_sedzlj.f90:190` — `CSEDSS = SMASS(NS)/(DWS(NS)*DTSEDJ)                     ! *** Concentration eroded into bedload from the last time step`; `SedTran-SEDZLJ/s_sedzlj.f90:195` — `PROBVR(NS) = min(CSEDSS/CSEDVR(NS),1.0)               ! *** van Rijn probability of deposition from bedload`; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) (`SedTran-SEDZLJ/s_sedzlj.f90:189` — `SMASS(NS) = CBL(L,NS)`) [10-12 전수 검증 보완] 확률은 1 이하로 제한한다. (`SedTran-SEDZLJ/s_sedzlj.f90:190` — `CSEDSS = SMASS(NS)/(DWS(NS)*DTSEDJ)                     ! *** Concentration eroded into bedload from the last time step`; `SedTran-SEDZLJ/s_sedzlj.f90:195` — `PROBVR(NS) = min(CSEDSS/CSEDVR(NS),1.0)               ! *** van Rijn probability of deposition from bedload`; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) 평형 농도에는 입자 밀도 2.65를 고정한다. (`SedTran-SEDZLJ/s_sedzlj.f90:191` — `CSEDVR(NS) = (0.18*2.65*TRANS(L,NS)/DISTAR(NS)*0.65)    ! *** van Rijn's (1981, Eq. 21) equilibrium bedload concentration (here TRANS is the transport parameter for bedload calculations)`; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) 이 소류사 퇴적 경로는 `if( ICALC_BL > 0 .and. PROP_ERO(L,0) == 0.0 )then`에서 작은 입경과 CBL이 1E-20 미만인 항목을 건너뛴다. (`SedTran-SEDZLJ/s_sedzlj.f90:184` — `if( ICALC_BL > 0 .and. PROP_ERO(L,0) == 0.0 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:186` — `if( D50(NS) < BEDLOAD_CUTOFF ) CYCLE`; `SedTran-SEDZLJ/s_sedzlj.f90:188` — `if( CBL(L,NS) < 1E-20 ) CYCLE`) [10-12 전수 검증 보완] 코드는 `if( CSEDVR(NS) <= 0.0 )then`에서 PROBVR에 1을 대입하고 ELSE에서 인용한 min 식을 적용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:192` — `if( CSEDVR(NS) <= 0.0 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:193` — `PROBVR(NS) = 1.0`) [10-12 전수 검증 보완] 그 뒤 `if( CSEDSS <= 0.0 )` 조건은 PROBVR을 PROB로 덮어쓴다. (`SedTran-SEDZLJ/s_sedzlj.f90:197` — `if( CSEDSS <= 0.0 ) PROBVR(NS) = PROB(NS)`) [10-12 전수 검증 보완] <a id="cv-e-hydro-721"></a>결론: 문서에만 있음. 식 6.144는 평형 유도식이며 SEDZLJ는 이를 독립 소류사 침식식으로 계산하지 않는다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:23` — `E_b=Pw_sC_e`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:189` — `SMASS(NS) = CBL(L,NS)                                   ! *** Local mass available for deposition is the bedload concentration times the bedload height`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:190` — `CSEDSS = SMASS(NS)/(DWS(NS)*DTSEDJ)                     ! *** Concentration eroded into bedload from the last time step`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:195` — `PROBVR(NS) = min(CSEDSS/CSEDVR(NS),1.0)               ! *** van Rijn probability of deposition from bedload`; [EFDC-theory-hydro-vs-code §5 행 eq-6-144](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:721)) <a id="cv-e-hydro-722"></a>결론: 문서 누락. 이론 문서는 소류사 퇴적계수에 이류·침퇴적 갱신 후의 보유 질량과 확률 상한을 사용하는 시간 갱신 규약을 누락한다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:23` — `P=\dfrac{E_b}{w_sC_e}`<br>`_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:24` — `P_j=\dfrac{f_jE_b}{w_{sj}f_jC_{ej}}=\dfrac{E_b}{w_{sj}C_{ej}}`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:189` — `SMASS(NS) = CBL(L,NS)                                   ! *** Local mass available for deposition is the bedload concentration times the bedload height`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:190` — `CSEDSS = SMASS(NS)/(DWS(NS)*DTSEDJ)                     ! *** Concentration eroded into bedload from the last time step`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:192` — `if( CSEDVR(NS) <= 0.0 )then                             ! *** If there is no equilibrium bedload available`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:195` — `PROBVR(NS) = min(CSEDSS/CSEDVR(NS),1.0)               ! *** van Rijn probability of deposition from bedload`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:284` — `CBL(L,NS) = CBL(L,NS) + ( DXYIPCM(L)*DTSEDJ*( QSBDLDX(L,NS)-QSBDLDX(LE,NS) + QSBDLDY(L,NS)-QSBDLDY(LN,NS) ) + QBLFLUX(L,NS) )`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:201` — `DEPBL(NS) = min(MAX(DEPBL(NS),0.0),SMASS(NS))           ! *** Do not allow more bedload deposition than bedload mass available`; [EFDC-theory-hydro-vs-code §5 행 eq-6-145, eq-6-147](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:722)) <a id="cv-e-hydro-723"></a>결론: 코드 결함 후보. SEDZLJ의 평형 소류사 농도식은 입력 SEDDENS 대신 고정 상수 2.65를 사용한다. E를 유지한다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:24` — `C_e=0.117\dfrac{\rho_sT}{d_*}`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:191` — `CSEDVR(NS) = (0.18*2.65*TRANS(L,NS)/DISTAR(NS)*0.65)    ! *** van Rijn's (1981, Eq. 21) equilibrium bedload concentration (here TRANS is the transport parameter for bedload calculations)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:260` — `read(10,*) WATERDENS, SEDDENS(CORE)          ! *** read in the water density and sediment solid's density`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:150` — `BLVEL(L,NS) = 1.5*TRANS(L,NS)**0.6*SQRT(((SEDDENS(NCORENO(IL(L),JL(L)))/WATERDENS) -1.0)*980.0*D50(NS)/10000.0)    ! *** eqn. 20a  (cm/s)`; [EFDC-theory-hydro-vs-code §5 행 eq-6-146](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:723)) [10-12 결론 검증 보완]


### 2.4 Active layer mass

```fortran
! s_sedzlj.f90:273-277
if( TAU(L)/TAUCRIT < 1.0 )then
  TACT = TACTM * D50AVG(L) * (BULKDENS(1,L) / 10000.0)
else
  TACT = TACTM * D50AVG(L) * (TAU(L)/TAUCRIT) * (BULKDENS(1,L)/10000.0)
endif
```

TACT는 밀도를 곱한 활성층 질량 기준량이다. (`SedTran-SEDZLJ/s_sedzlj.f90:274` — `TACT = TACTM*D50AVG(L)*(BULKDENS(1,L)/10000.0)`; `SedTran-SEDZLJ/s_sedzlj.f90:276` — `TACT = TACTM*D50AVG(L)*(TAU(L)/TAUCRIT)*(BULKDENS(1,L)/10000.0)`; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) 길이로 환산하면 TACTM·d50·max(1,τ/τce)이다. (`SedTran-SEDZLJ/s_sedzlj.f90:274` — `TACT = TACTM*D50AVG(L)*(BULKDENS(1,L)/10000.0)`; `SedTran-SEDZLJ/s_sedzlj.f90:276` — `TACT = TACTM*D50AVG(L)*(TAU(L)/TAUCRIT)*(BULKDENS(1,L)/10000.0)`; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) TACTM은 입력값이다. (`SedTran-SEDZLJ/s_sedic.f90:113` — `read(10,*) TACTM !read in active layer multiplier`; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) 문서의 계수 2는 공통 코드 기본값으로 확인하지 않음. (`SedTran-SEDZLJ/s_sedic.f90:113` — `read(10,*) TACTM !read in active layer multiplier`; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) <a id="cv-e-hydro-724"></a>결론: 문서 누락. SEDZLJ는 입력 TACTM과 응력비 하한으로 활성층을 정하며 고정 2와 200 μm를 모든 경우에 강제하지 않는다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:24` — `T_a=2d_{50}\dfrac{\tau^b}{\tau_{ce}}`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:273` — `if( TAU(L)/TAUCRIT < 1.0 )then`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:274` — `TACT = TACTM*D50AVG(L)*(BULKDENS(1,L)/10000.0)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:276` — `TACT = TACTM*D50AVG(L)*(TAU(L)/TAUCRIT)*(BULKDENS(1,L)/10000.0)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:113` — `read(10,*) TACTM !read in active layer multiplier`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:701` — `if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.`; [EFDC-theory-hydro-vs-code §5 행 eq-6-148, K25](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:724)) [10-12 결론 검증 보완]


`TACTM` = active-layer thickness multiplier (보통 2~10), `D50AVG` = bed-surface 평균 입경 (μm), `BULKDENS` = 건조밀도 (g/cm³).

### 2.5 TAUCRIT (critical shear) 보간

```fortran
! s_sedzlj.f90:425-435
if( LAYERACTIVE(K,L) == 1 )then
  ! *** Active/deposited layer — D50AVG 선형 보간
  TAUCRIT = TAUCRITE(NSC0) + (TAUCRITE(NSC1)-TAUCRITE(NSC0))/(NSCD(2)-NSCD(1)) &
                            * (D50AVG(L) - NSCD(1))
  TAUCOR(K,L) = TAUCRIT
elseif( LAYERACTIVE(K,L) == 2 )then
  ! *** In-place sediment layer — Sedflume data depth interpolation
  SN01 = TSED(K,L)/TSED0(K,L)
  SN11 = (TSED0(K,L)-TSED(K,L))/TSED0(K,L)
  TAUCRIT = SN01*TAUCOR(K,L) + SN11*TAUCOR(K+1,L)
endif
```

`LAYERACTIVE(K,L)`:
- `0` = 층 부재
- `1` = active/deposited (computed from D50 grain-size class)
- `2` = in-place (initial-condition, Sedflume-derived)

### 2.6 Erosion rate 두 옵션

#### NSEDFLUME = 1 (Sedflume-derived log-linear interpolation)

`s_sedzlj.f90:530-536` (active layer):

```fortran
! *** TAU 와 D50 의 4-point log-linear interpolation
SN00 = (TAUDD(2)-TAU(L))/(TAUDD(2)-TAUDD(1))
SN10 = (TAUDD(1)-TAU(L))/(TAUDD(1)-TAUDD(2))
SN01 = D50TMPP/NSCTOT
SN11 = (NSCTOT-D50TMPP)/NSCTOT
ERATEMOD = ( SN00*EXP(SN11*LOG(ERATEND(NSC0,NTAU0)) + SN01*LOG(ERATEND(NSC1,NTAU0))) &
            +SN10*EXP(SN11*LOG(ERATEND(NSC0,NTAU1)) + SN01*LOG(ERATEND(NSC1,NTAU1))) ) &
           * BULKDENS(K,L) * SQRT(1./SH_SCALE(L))
```

`ERATEND(NSC, NTAU)` = Sedflume 실험 erosion rate (cm/s) table — d50 class × TAU level.

#### NSEDFLUME의 거듭제곱식 분기

R8.5.0 PDF의 NSEDFLUME=2·3은 거듭제곱식 방식이다. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 s_sedzlj는 NSEDFLUME=1에서 lookup 값을 사용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 인용한 539줄은 `elseif( LAYERACTIVE(K,L) == 1 )then` 안에서 NSEDFLUME=1이 아닌 경우의 거듭제곱식이다. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:535` — `ERATEMOD = (SN00*EXP(SN11*LOG(ERATEND(NSC0,NTAU0)) + SN01*LOG(ERATEND(NSC1,NTAU0))) + SN10*EXP(SN11*LOG(ERATEND(NSC0,NTAU1)) +  &   ! *** log-linear interpolation`; `SedTran-SEDZLJ/s_sedzlj.f90:539` — `SN00 = ACTDEPA(NSC0)*(0.1*TAU(L))**ACTDEPN(NSC0)                             ! *** Erosion rate 1 (cm/s)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) (`SedTran-SEDZLJ/s_sedzlj.f90:523` — `elseif( LAYERACTIVE(K,L) == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`) [10-12 전수 검증 보완] 98은 현재 표준 거듭제곱식 번호로 확인하지 않음. (`SedTran-SEDZLJ/s_sedzlj.f90:530` — `if( NSEDFLUME == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:535` — `ERATEMOD = (SN00*EXP(SN11*LOG(ERATEND(NSC0,NTAU0)) + SN01*LOG(ERATEND(NSC1,NTAU0))) + SN10*EXP(SN11*LOG(ERATEND(NSC0,NTAU1)) +  &   ! *** log-linear interpolation`; `SedTran-SEDZLJ/s_sedzlj.f90:539` — `SN00 = ACTDEPA(NSC0)*(0.1*TAU(L))**ACTDEPN(NSC0)                             ! *** Erosion rate 1 (cm/s)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 이 경로는 보간한 침식률에 ACTDEPMAX 상한을 적용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:543` — `ERATEMOD = min(ERATEMOD,ACTDEPMAX(NSC0))`) [10-12 전수 검증 보완] 깊은 층의 비 lookup 경로는 `if( TAU(L) > TAUCOR(K,L) )then`에서 거듭제곱식을 계산한다. (`SedTran-SEDZLJ/s_sedzlj.f90:489` — `if( LAYERACTIVE(K,L) == 2 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:491` — `if( NSEDFLUME == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:506` — `if( TAU(L) > TAUCOR(K,L) )then`) [10-12 전수 검증 보완] 그 조건의 ELSE는 `ERATEMOD = 0.0`을 대입한다. (`SedTran-SEDZLJ/s_sedzlj.f90:520` — `ERATEMOD = 0.0`) [10-12 전수 검증 보완] 판정·근거: [정본 §5 행 878, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436](../../manual-notes/efdc-user-manual-r850.md#cv-e-input-2567). [10-12 결론 검증 보완]


```fortran
! s_sedzlj.f90:539-543 (active layer)
SN00 = ACTDEPA(NSC0) * (0.1*TAU(L))**ACTDEPN(NSC0)         ! *** A * tau^N
SN10 = ACTDEPA(NSC1) * (0.1*TAU(L))**ACTDEPN(NSC1)
SN11 = D50TMPP/NSCTOT
ERATEMOD = ((SN10-SN00)*SN11 + SN00) * BULKDENS(K,L) * SQRT(1./SH_SCALE(L))
ERATEMOD = MIN(ERATEMOD, ACTDEPMAX(NSC0))                  ! *** Limit erosion rate
```

shear는 dynes/cm² 단위지만 power law는 **Pascal 단위** 전제 (0.1 변환). `SH_SCALE` = bed slope 보정 (§4).

### 2.7 Mass balance after erosion

```fortran
! s_sedzlj.f90:572-580 (standard branch)
WHERE( TAU(L) >= TCRE(1:NSEDS) )                       ! *** Size class별 critical shear 비교
  ELAY(1:NSEDS)  = PERSED(1:NSEDS,K,L) * EBD            ! *** Size-class erosion (g/cm²)
  ETOT(1:NSEDS)  = ETOT(1:NSEDS) + ELAY(1:NSEDS)
  TTEMP(1:NSEDS) = PERSED(1:NSEDS,K,L)*TSED(K,L) - ELAY(1:NSEDS)
ELSEWHERE
  ELAY  = 0.0
  TTEMP = PERSED * TSED
ENDWHERE
```

→ class 별 `TCRE` (resuspension) ≠ overall bed `TAUCRIT` (erosion onset). 작은 입자는 먼저 erode, 큰 입자는 lagging → armoring.

### 2.8 Layer reconstitution

`s_sedzlj.f90:300-342` — 시간 step 끝 active layer 재구성:
- Net deposition (`TSED(1) > TACT`) → 잉여 mass 를 layer 2 로 이송 (line 306-312)
- Net erosion, sufficient lower mass (`TSED(1) < TACT`, `TSED(1)+TSED(SLLN) > TACT`) → lower layer 에서 borrow (line 314-318)
- Net erosion, insufficient → layer 2 흡수 + SLLN advance (line 320-339)

### 2.9 Output → EFDC water column

```fortran
! s_sedzlj.f90:700-723
SEDF(L,0,1:NSEDS2) = QBFLUX(1:NSEDS2)*10000./DTSEDJ                  ! *** Suspended sed flux (g/m²/s)
SED(L,KSZ(L),NS)   = SED2(L,KSZ(L),NS) + (SEDF(L,0,NS) - SEDF(L,KSZ(L),NS)) * WDTDZ
HBED(L,1:KB)       = 0.01 * TSED(1:KB,L) / BULKDENS(1:KB,L)          ! *** Bed thickness (m)
SEDBT(L,1:KB)      = TSED(1:KB,L) * 10000.                           ! *** Bed mass (g/m²)
```

## 3. Wave-current shear (`s_shear.f90`) — Christoffersen-Jonsson 1985

`s_main.f90:54` 가 호출. 핵심:

### 3.1 Wave forcing 입력 옵션

`ISWNWAVE`:
- 0 = EFDC+ internal windwave (line 55-72)
- 1 = wind-fetch wave (CERC/SPM 식, line 74-185) — FZONE 8 sector + AVGDEPTH-based wave height/period
- 2 = STWAVE external wave (line 187-220)

### 3.2 Current friction (Parker 2004)

```fortran
! s_shear.f90:261
FC = (0.42 / LOG(11.*HP(L) / (2.0*ZBTEMP(L))))**2
! *** ZBTEMP = D50AVG × 10⁻⁶ m (skin friction) 또는 ZBSKIN
```

<a id="cv-e-body-29-251"></a>유동 응력의 코드 목표값은 FC·cm/s 유속²이다. (`SedTran-SEDZLJ/s_shear.f90:266` — `SHEAR = FC*VELMAG**2`; EFDC_Theory_Document_Ver_12.pdf, PDF 110쪽·인쇄 97쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽) WATERDENS는 그 곱에 들어가지 않는다. (`SedTran-SEDZLJ/s_shear.f90:266` — `SHEAR = FC*VELMAG**2`; EFDC_Theory_Document_Ver_12.pdf, PDF 110쪽·인쇄 97쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽) 문서 응력과 같은 단위 해석에는 ρw=1 g/cm³ 조건이 필요하다. (`SedTran-SEDZLJ/s_shear.f90:266` — `SHEAR = FC*VELMAG**2`; EFDC_Theory_Document_Ver_12.pdf, PDF 110쪽·인쇄 97쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽) <a id="cv-e-hydro-709"></a>결론: 문서 누락. SEDZLJ의 유동 응력 경로는 물 밀도 1 g/cm³에 해당하는 수치 가정을 사용한다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:14` — `\tau_b=\rho_wc_fV^2`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:261` — `FC = ( 0.42/LOG(11.*HP(L)/(2.0*ZBTEMP(L))) )**2                             ! *** Friction factor for current only (dimensionless)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:265` — `! *** Compute bed shear due to currents only (dynes/cm2)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:266` — `SHEAR = FC*VELMAG**2`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:315` — `if( SHEAR > TAU(L)*(1.+GROWTH) )then`; [EFDC-theory-hydro-vs-code §5 행 eq-6-113](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:709)) [10-12 결론 검증 보완]

```fortran
SHEAR = FC * VELMAG²   ! *** dynes/cm² (VELMAG in cm/s)
```

본문 대조: [정본](efdc_sedzlj.md#cv-e-body-29-251). 판정·근거: [정본 §5 행 eq-6-113](efdc_sedzlj.md#cv-e-hydro-709). [10-12 결론 검증 보완]


### 3.3 Combined wave-current (Christoffersen-Jonsson 1985)

```fortran
! s_shear.f90:285-302
FWW    = 2.0*(0.0747 * (KN*WVFREQ(L)/WVORBIT(L)))**0.66        ! *** Pure wave friction (Beta = 0.0747)
SIGMAWV = FC/FWW * (VELMAG/(WVORBIT*100))**2                   ! *** Eq 3.8
MMW    = SQRT(1 + SIGMAWV² + 2*SIGMAWV*|cos(VELANG-WVANG)|)    ! *** Eq 3.10 wave-current angle adjustment
JJW    = WVORBIT/(KN*WVFREQ) * SQRT(MMW*FWW/2)                 ! *** Eq 4.12
FWW    = MMW*0.15/JJW                                          ! *** Updated combined friction (Step 3 end)

! *** Wave boundary layer
DELW    = KN * 0.273 * SQRT(JJW)                               ! *** Eq 4.11 thickness (m)
APROUGH = KN * DELW/KN * EXP(-5.62*DELW/KN * SQRT(SIGMAWV/MMW)) ! *** Eq 4.23 apparent roughness

! *** Current friction iterated with apparent roughness
FC = 2.0*(1.0/(2.38*LOG(H/(2.718*KN)) - 2.38*LOG(APROUGH/KN)))**2  ! *** Eq 4.25
! *** Iterate SIGMAWV, MMW, JJW, FWW once more
```

식 번호는 Christoffersen & Jonsson 1985 "An assessment of the wave-current sediment-transport theory" (Coastal Engineering) 원논문 인용. β=0.0747 (line 285 끝) 은 동 논문 추정.

### 3.4 Final combined shear

```fortran
! s_shear.f90:305-310
SHEARW   = 0.5 * FWW * MMW * WVORBIT²            ! *** Wave-only shear (m²/s²)
SHEARW   = 10000. * SHEARW                       ! *** Convert to cm²/s² = dynes/cm²·1/ρ
QQWV3(L) = SHEARW                                ! *** Wave shear output
QQWCR(L) = SHEARC                                ! *** Current shear output
SHEAR    = SHEARC + SHEARW                       ! *** Total
```

### 3.5 Growth limiter

```fortran
! s_shear.f90:315-322
! *** Limit rate of shear growth to 10% per timestep (suppress instability)
if( SHEAR > TAU(L)*(1.+GROWTH) )then              ! *** GROWTH = 0.1
  TAU(L) = TAU(L) + GROWTH*(SHEAR-TAU(L))
else
  TAU(L) = SHEAR
endif
```

결론: 코드 결함 후보. SEDZLJ의 응력 갱신은 주석의 10% 상한을 넘고 분기 경계에서 목표 응력과 반대로 변하는 코드 결함 후보이다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:14`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:47` — `GROWTH = 0.1_8`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:314` — `! *** Limit the rate of growth to 10% of previous value for bed shear (current and wave)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:315` — `if( SHEAR > TAU(L)*(1.+GROWTH) )then`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:316` — `TAU(L) = TAU(L) + GROWTH*(SHEAR-TAU(L))`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:321` — `TAU(L) = SHEAR`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mod_hydstructure.f90:330` — `! *** limit the rate of growth/reduction (5%)`; [EFDC-theory-hydro-vs-code §5 행 B22](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:757)) [10-12 결론 검증 보완]


### 3.6 Constant TAU 옵션

```fortran
! s_shear.f90:329-334
else
  ! *** TAUCONST > 0 → spatial constant
  TAU(L)  = TAUCONST
  TAUB(L) = 0.1 * TAU(L)
endif
```

## 4. Bed slope shear amplification (`s_slope.f90`) — Lick 2009

`s_main.f90:56` `if( ISSLOPE ) CALL SEDZLJ_SLOPE`.

```fortran
! s_slope.f90:79-89
DZBETA  = DELX/XDIST*DELZX + DELY/YDIST*DELZY    ! *** Pitch (flow direction slope)
DZTHETA = DELY/XDIST*DELZX + DELX/YDIST*DELZY    ! *** Roll (cross-flow slope)
COSB = 1.0/SQRT(1+DZBETA²)
SINB = DZBETA/SQRT(1+DZBETA²)
COST = 1.0/SQRT(1+DZTHETA²)
TANT = DZTHETA
TEMP1 = (1.0+(FCO+FB)/(FG*COSB*COST))² - (TANT/TAN(ALPHA))²

if( TEMP1 > 0.0 )then
  SH_SCALE(L) = MAX(0.1, BB/AA*SINB + COSB*COST*SQRT(TEMP1))   ! *** Lick 2009 Eq 3.36
else
  SH_SCALE(L) = 0.1
endif
```

`SH_SCALE` ≥ 1 → adverse slope (uphill flow) 가 effective shear 증폭. `SEDZLJ` line 499, 517, 542 의 `SQRT(1/SH_SCALE)` 가 ERATEMOD 보정.

### 4.1 Lesser et al. bedload velocity correction

```fortran
! s_slope.f90:95-98
ALPHA_PX(L) = 1.0 - TUNEP*(TAN(ALPHA)/(COS(ATAN(DELZX/XDIST))*(TAN(ALPHA)-DELZX/XDIST))-1)  ! *** Pitch x
ALPHA_RX(L,NS) = -TUNER*SQRT(TCRE(NS)/TAU(L)) * DELZY/YDIST                                  ! *** Roll x
! (PY, RY 동일 패턴)
```

Lesser et al. (Delft3D) 추정 — gravity 가 bedload velocity vector를 downslope 으로 회전.

## 5. Bedload transport (`s_bedload.f90`) — Van Rijn 1981

`s_main.f90:58` `if( ICALC_BL > 0 )then`, `s_main.f90:59` `call BEDLOADJ`.

```fortran
! s_bedload.f90:147-150 (Van Rijn 1981 식 번호 코멘트 직접)
TRANS(L,NS) = MAX((TAU(L)-TCRE(NS))/TCRE(NS), 0.0)                          ! *** Eq 21
DZBL(L,NS)  = D50(NS)/10000.0 * 0.3 * DISTAR(NS)**0.7 * SQRT(TRANS(L,NS))   ! *** Eq 20b - bedload layer thickness
BLVEL(L,NS) = 1.5 * TRANS(L,NS)**0.6 &
            * SQRT(((SEDDENS/WATERDENS) - 1.0) * 980.0 * D50(NS)/10000.0)   ! *** Eq 20a - bedload velocity (cm/s)
```

코드의 소류사 이류는 유입−유출이다. (`SedTran-SEDZLJ/s_bedload.f90:284` — `CBL(L,NS) = CBL(L,NS) + ( DXYIPCM(L)*DTSEDJ*( QSBDLDX(L,NS)-QSBDLDX(LE,NS) + QSBDLDY(L,NS)-QSBDLDY(LN,NS) ) + QBLFLUX(L,NS) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) 문서 식 6.137의 양의 플럭스 발산과 다르다. (`SedTran-SEDZLJ/s_bedload.f90:284` — `CBL(L,NS) = CBL(L,NS) + ( DXYIPCM(L)*DTSEDJ*( QSBDLDX(L,NS)-QSBDLDX(LE,NS) + QSBDLDY(L,NS)-QSBDLDY(LN,NS) ) + QBLFLUX(L,NS) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽, 식 6.137) 코드는 소류사 대상 입경의 `if( ISKIP(NS) == 0 )then`에서 인용한 층두께 식을 계산한다. (`SedTran-SEDZLJ/s_bedload.f90:148` — `DZBL(L,NS)  = D50(NS)/10000.0*0.3*DISTAR(NS)**0.7*SQRT(TRANS(L,NS))   ! *** eqn. 20b`; EFDC_Theory_Document_Ver_12.pdf, PDF 118쪽·인쇄 105쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 120쪽·인쇄 107쪽) (`SedTran-SEDZLJ/s_bedload.f90:143` — `if( D50(NS) < BEDLOAD_CUTOFF ) CYCLE`; `SedTran-SEDZLJ/s_bedload.f90:144` — `if( ISKIP(NS) == 0 )then`) [10-12 전수 검증 보완] 식 6.140의 3d·D*^0.6·T^0.9와 다르다. (`SedTran-SEDZLJ/s_bedload.f90:148` — `DZBL(L,NS)  = D50(NS)/10000.0*0.3*DISTAR(NS)**0.7*SQRT(TRANS(L,NS))   ! *** eqn. 20b`; EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽, 식 6.140) 코드는 그 계산값에 수심 상한을 적용한다. (`SedTran-SEDZLJ/s_bedload.f90:149` — `DZBL(L,NS)  = min(DZBL(L,NS), HPCM(L))`) [10-12 전수 검증 보완] <a id="cv-e-hydro-719"></a>결론: 문서 오기. 이론 문서 식 6.137의 우변 발산 부호는 음수이어야 하며 코드는 유입에서 유출을 뺀다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:22` — `\dfrac{\partial(mC_b)}{\partial t}=\dfrac{\partial(mq_{bx})}{\partial x}+\dfrac{\partial(mq_{by})}{\partial y}+Q_b`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:284` — `CBL(L,NS) = CBL(L,NS) + ( DXYIPCM(L)*DTSEDJ*( QSBDLDX(L,NS)-QSBDLDX(LE,NS) + QSBDLDY(L,NS)-QSBDLDY(LN,NS) ) + QBLFLUX(L,NS) )`; [EFDC-theory-hydro-vs-code §5 행 eq-6-137](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:719)) [10-12 결론 검증 보완]


<a id="cv-e-eq-6-140"></a>**문서와 코드 차이 · eq-6-140** [10-12 결론 검증 보완]

결론: B 문서 오기.
문서 식 6.140의 `3 d d*^0.6 T^0.9`는 van Rijn Part I 식 (11)의 도약 길이 λb이다.
두께 h_b는 식 (10)의 `0.3 d d*^0.7 T^0.5`이다.
코드 s_bedload.f90:148은 식 (10)을 쓴다.
(EFDC_Theory_Document_Ver_12.pdf, PDF 119쪽·인쇄 106쪽, 식 6.140; `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:148`; van Rijn, L. C. (1984), [Sediment transport, part I: bed load transport](https://documents.epfl.ch/users/b/bl/blanckae/www/HydrauliqueFluviale/Papers/1984_JHE_VanRijn_a.pdf), J. Hydraul. Eng. 110(10), 1431–1456, 1442쪽 식 (10) `δb/D = 0.3 D*^0.7 T^0.5`, 1443쪽 식 (11) `λb/D = 3 D*^0.6 T^0.9`; [대조 보고서 §5 행 eq-6-140](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md#5-차이-결론))
코드 주석 `eqn. 20b`의 문헌 귀속은 미해결이다.
(`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_bedload.f90:148`; [외부 판정 eq-6-140](../../../../_staging/recovery/compare/external-results-ef.md)) [10-12 외부 원문 판정]

참고문헌 정정: [서지 대조 정본](../../manual-notes/efdc-theory-doc-v12.md#cv-e-ref-vanrijn). [10-12 결론 검증 보완]

- `TRANS` = transport parameter (excess shear ratio)
- `DZBL` = bedload layer thickness (m)
- `BLVEL` = bedload velocity (cm/s)
- `DISTAR` = $D_*$ = dimensionless particle diameter $= D_{50} \cdot (g(s-1)/\nu^2)^{1/3}$

결론: 문서 누락. SEDZLJ는 BEDLOAD_CUTOFF가 10 μm보다 작으면 64 μm로 바꾼다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:24`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:699` — `! *** Bedload size cutoff for bedload (e.g. > 64) and approach for probability of deposition`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:701` — `if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.`; [EFDC-theory-hydro-vs-code §5 행 B24](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:758)) [10-12 결론 검증 보완]


## 6. 입력 파라미터

### 6.1 Card C36 (SEDZLJ dispatch)

`models/EFDC/raw/manuals/confluence/spaces/ECIG/.../Card_Image_36.md`:

```
C36 | ISEDINT | ISEDBINT | NSEDFLUME | ISMUD | ISNDWC | ISEDVW | ISNDVW | KB | ISDTXBUG
    | 2       | 1        | 0         | 0     | 0      | 0      | 0      | 8  | 0
```

ECIG의 C36 헤더는 5번째 열을 ISNDWC로 표시한다. (`models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:48` — `\* ISNDWC: NOT USED`; EFDC_Manual.pdf, PDF 40쪽·인쇄 36쪽) R8.5.0 PDF와 현재 코드의 5번째 열은 ISBEDMAP이다. (`input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; EFDC_Manual.pdf, PDF 40쪽·인쇄 36쪽) 결론: 판 차이. EFDC+ 12.5는 C36의 다섯째 값을 ISBEDMAP으로 읽는다. (근거: `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:48` — `\* ISNDWC: NOT USED`<br>`_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Manual.pdf/p037-054.md:16` — `C36 ISEDINT ISEDBINT NSEDFLUME ISMUD ISBEDMAP ISEDVW ISNDVW KB ISDTXBUG`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; [EFDC-input-cards-vs-code §5 행 880](../../../../_staging/recovery/compare/EFDC-input-cards-vs-code.md:2568))


| 변수 | 의미 | 코드 위치 |
|---|---|---|
| `NSEDFLUME` | 코드·문서 대조 | ECIG는 NSEDFLUME=98·99를 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) R8.5.0 PDF는 0을 Original로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 1을 erosion rate lookup 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 2를 거듭제곱식과 core별 저층 물성 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) PDF는 3을 거듭제곱식과 전체 저층 물성 방식으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 prescan은 `if( ISTRAN(6) > 0 )then` 안에서 NSEDFLUME=98·99를 1로 바꾼다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) (`mod_scaninp.f90:381` — `if( ISTRAN(6) > 0 )then`) [10-12 전수 검증 보완] 현재 INPUT은 원래 NSEDFLUME를 다시 읽는다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) 현재 INPUT에서 98·99를 다시 1로 바꾸는 대입을 찾지 못했다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) s_sedic의 변경 주석은 toxic 선택을 ISTRAN(5)>0으로 설명한다. (`mod_scaninp.f90:382` — `if( NSEDFLUME == 98 .or. NSEDFLUME == 99 )then`; `mod_scaninp.f90:384` — `NSEDFLUME = 1`; `input.f90:1974` — `read(1,*,IOSTAT = ISO)ISEDINT,ISEDBINT,NSEDFLUME,ISMUD,ISBEDMAP,ISEDVW,ISNDVW,KB,ISDTXBUG`; `SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) |
| `KB` | 최대 bed layer 수 (active + in-place) | `s_sedzlj.f90:215, 282` |
| `ISEDINT` | 0 = constant / 1 = SEDW.INP+SNDW.INP / 2 = SEDB.INP+SNDB.INP / 3 = 둘 다 | `s_sedic.f90` |
| `ISEDBINT` | 0 = mass/area / 1 = mass fraction + BEDLAY.INP | `s_sedic.f90` |
| `ISEDVW` | cohesive settling velocity option (0 constant, 98 Lick flocculation, 99 Lick+floc advection) | `csedvis.f90` |

### 6.2 핵심 array 변수 (`mod_var_global.f90`)

| Symbol | 단위 | 의미 |
|---|---|---|
| `TSED(K,L)` | g/cm² | Layer K, cell L 의 단위면적 sediment mass |
| `PERSED(NS,K,L)` | — | Size class NS 의 mass 분율 (sum = 1) |
| `LAYERACTIVE(K,L)` | flag | 0/1/2 (부재/active deposited/in-place) |
| `BULKDENS(K,L)` | g/cm³ | 건조밀도 |
| `TAUCOR(K,L)` | dynes/cm² | Layer-specific critical shear |
| `TCRE(NS)` | dynes/cm² | Size-class critical shear (resuspension onset) |
| `TCRSUS(NS)` | dynes/cm² | Suspension critical shear (deposition threshold) |
| `TAU(L)` | dynes/cm² | Total bed shear (s_shear 출력) |
| `SH_SCALE(L)` | — | Bed slope shear scale (s_slope) |
| `D50AVG(L)` | μm | Cell L 의 bed 평균 D50 |
| `HBED(L,K)` | m | Bed layer 두께 |

## 7. SedTran-Original 와의 비교

[[efdc_sediment]] §C-D 의 원형 SedTran 와 SEDZLJ 의 핵심 차이:

| 항목 | SedTran-Original | SEDZLJ |
|---|---|---|
| Cohesive erosion | Krone-Partheniades (constant M) | Sedflume-derived ERATEND table 또는 power law |
| Cohesive deposition | Krone (PROB = 1 - τ/τc) | Krone (작은 D50) + Gessler (큰 D50) |
| Non-cohesive | Van Rijn / Engelund-Hansen (calsnd.f90) | 통합 Van Rijn (s_bedload.f90) |
| Bed structure | 단일 또는 단순 다층 | Active layer + multi in-place layer (`LAYERACTIVE` 0/1/2) |
| Wave-current shear | EFDC main (calwave2 등) | Christoffersen-Jonsson 1985 (s_shear.f90) |
| Bed slope | 없음 | Lick 2009 (s_slope.f90) `SH_SCALE` |
| Mass-class 정밀도 | water-column class만 | Bed mass-class + propwash fast/slow split |
| Toxic linkage | 코드·문서 대조 | 현재 toxic 연계 선택은 ISTRAN(5)>0이다. (`SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:38` — `\*                      98 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:40` — `\*                      99 USE THE SEDZLJ SEDIMENT TRANSPORT SUB-MODEL WITH TOXICS`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) s_sedic의 변경 주석은 NSEDFLUME=99 toxic 선택을 폐기했다고 기록한다. (`SedTran-SEDZLJ/s_sedic.f90:49` — `! similations.  Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md:36` — `\* NSEDFLUME: 0 USE THE SEDIMENT TRANSPORT FUNCTIONS IN EFDC MAIN CODE`; EFDC_Manual.pdf, PDF 39쪽·인쇄 35쪽) |

## 8. Wave coupling

### 8.1 Wave parameter 입력 옵션 (`s_shear.f90`)

| `ISWAVE` × `ISWNWAVE` | 거동 | Code line |
|---|---|---|
| 0 | wave 없음 (current shear만) | 264 |
| > 0 × 0 | EFDC+ WINDWAVECAL 호출 (UDEL, FREQ, DIR) | 55-72 |
| > 0 × 1 | Wind-fetch wave (FZONE 8 sector + AVGDEPTH) | 74-185 |
| > 0 × 2 | STWAVE external NetCDF | 187-220 |

### 8.2 Wave breaking dispersion 별개

수평 운동량 확산의 wave breaking 가산항은 본 노트 아닌 [[efdc_dispersion]] §2.3 calhdmf.f90:246-294.

## 9. Cross-references

- **Dispatch / SedTran 비교**: [[efdc_sediment]] §A (ISTRAN(6)/(7), SEDZLJ enable)
- **수평 momentum diffusion**: [[efdc_dispersion]] (Smagorinsky + AHO, 별개 layer)
- **Vertical turbulence**: [[efdc_turbulence]] (Mellor-Yamada / Galperin / GOTM)
- **Theory 식**: [[efdc-theory-doc-v12]] §6.4 SEDZLJ (TOC line 136)
- **2003 legacy**: [[efdc-sediment-theory-2003]] §5 bed armoring (DSI SEDZLJ 에 흡수, line 169)
- **Card C36**: `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_36.md`
- **EE12 GUI tutorial**: `models/EFDC/raw/manuals/confluence/spaces/EHG/pages/EEMS_12_Tutorials/How-To_Guides_for_EE12/Sediment_Transport_Modeling.md` + Yen & Lee U-Shaped Flume SEDZLJ tutorial

## 10. 미해결 / 추가 보강 후보

- ~~`s_sedic.f90` (769 lines) — bed initial-condition reader.~~ **§11 完 verified line 1-769 (2026-06-01 §11.1-5 + 2026-06-02 §11.6-8 + 2026-06-03 §11.9-14: hard-bottom ZELBEDA·KBT + 신규퇴적 ERATEND/TAUCRITE·ACTDEP power-law + Cheng1998 settling + IHTSTRT hotstart SEDBED_HOT.SDF restore + fetch/STWAVE wave 입력 + toxics용 SEDB/SEDBT/VDRBED + WSEDO/SEDDIA 단위변환 + empty-layer collapse).**
- `s_tecplot.f90` (310 lines) — SEDZLJ Tecplot 출력 — 분석 측면에서 별도 노트 필요 시.
- Propwash 연동 (`Variables_Propwash` use, line 27) — `s_sedzlj.f90:135-180, 559-617` 의 `PROP_ERO(L,1:NSEDS)` 처리. [[efdc_propwash]] (별도 노트) 후보.
- Mass erosion fast class (`NSEDS2 > NSEDS`, `s_sedzlj.f90:165-180, 604-617`) — propwash 시 fast/normal 분리 동작.
- Toxics linkage (`NSEDFLUME = 99`) — **deprecated 2016-12 ([[efdc_sedzlj]] §11.4)**. 매뉴얼 Card C36 의 NSEDFLUME=99 표기는 stale → ISTRAN(5)>0 가 현행.
- Wave-current 식 번호와 Christoffersen-Jonsson 1985 원논문 페이지 cross-check (현재는 코드 코멘트 기준 인용).

## 11. SEDIC initialization (`s_sedic.f90`, 769 lines 全 verified — §11.1-5 2026-06-01, §11.6-8 deep 2026-06-02, §11.9-14 line 380-769 deep 2026-06-03)

SEDZLJ bed 초기화: 입력 read(bed.sdf/erate.sdf) → VAR_BED core map(NCORENO) → Sedflume core data → core→cell 매핑 → 층질량/LAYERACTIVE 초기화.

### 11.1 Subroutine 호출 + 입력 파일 (line 53-58, master process)

```fortran
open(UNIT = 10, FILE = 'erate.sdf')   ! line 57 - Sedflume erosion rate table + TACTM
open(UNIT = 30, FILE = 'bed.sdf')     ! line 58 - bed parameters + size class
```

### 11.2 bed.sdf 입력 (line 63-96)

```fortran
read(30,*) VAR_BED, KB, ICALC_BL, SEDSTEP, SEDSTART, IHTSTRT, IMORPH, ISWNWAVE, MAXDEPLIMIT, HPMIN
if( HPMIN < 0.003 .or. HPMIN >= 1.0 ) HPMIN = 0.25                  ! line 65 fallback
if( SEDSTEP < TIDALP/REAL(NTSPTC) ) SEDSTEP = TIDALP/REAL(NTSPTC)    ! line 67

read(30,*) ZBSKIN, TAUCONST, ISSLOPE, BEDLOAD_CUTOFF                 ! line 80
read(30,*) (D50(K), K=1,NSEDS)                                       ! line 84 - 중앙 입경
read(30,*) (TCRE(K), K=1,NSEDS)                                      ! line 88 - 침식 임계
read(30,*) (TCRSUS(K), K=1,NSEDS)                                    ! line 92 - 부유 임계
read(30,*) (DWSIN(K), K=1,NSEDS)                                     ! line 96 - 침강속도 입력
```

매핑:
- `VAR_BED` = 1 → spatially varying bed
- `KB` = max bed layer (Card C36 일치)
- `HPMIN` = SEDZLJ 활성 최소 수심 (m), [0.003, 1.0] 외 시 0.25 fallback
- `ZBSKIN` = bed skin friction roughness ([[efdc_sedzlj]] §3.2 s_shear:243)
- `TAUCONST` > 0 → spatial constant shear ([[efdc_sedzlj]] §3.6)
- `ISSLOPE` = bed slope correction 활성 ([[efdc_sedzlj]] §4)
- `BEDLOAD_CUTOFF` = D50 임계 (Krone vs Gessler dispatch, [[efdc_sedzlj]] §2.1)

### 11.3 erate.sdf (line 112-113)

```fortran
read(10,*) TACTM   ! active layer thickness multiplier — [[efdc_sedzlj]] §2.4 핵심 식 입력
```

### 11.4 NSEDFLUME = 99 deprecated note (line 47-50, 정확 인용)

> "2016-12 — Rearranged SEDZLJ initialization and added parameters for better toxics simulations. **Deprecated NSEDFLUME = 99 (i.e. SEDZLJ toxics) Toxics are handled by ISTRAN(5)>0. NEQUIL no longer used**. Paul M. Craig"

→ §6.1 Card C36 매뉴얼 (2018-01-08) 의 "NSEDFLUME = 99" 표기는 **stale** — 현행 ISTRAN(5)>0.

### 11.5 MPI broadcast (line 117-)

Master only read, 그 후 `Broadcast_Scalar/Array` 분배. `mod_var_global.f90` SEDZLJ 변수 전체.

### 11.6 VAR_BED core map (line 142-210) — deep 2026-06-02

`VAR_BED >= 1` (spatially variable bed) → **NCORENO(I,J) core 번호 맵** 읽기 (unit 20):
- **DSI standard**: `I2D_Global(I,J) = CORE` (cell별 core 번호)
- **SNL standard**: `read(20,'(120(I1,1X))')(I2D_Global(I,J), I=1,IC)` (J행별 1-digit core)
- local domain 매핑(MPI). VAR_BED=0 시 단일 core 전역.

### 11.7 Sedflume core data read (line 255-302) — deep

각 core (unit 10, NCORENO 가 참조):
- `TSED0S(K,CORE)` 층두께 + `BDEN(CORE,K)` bulk density + `WATERDENS, SEDDENS(CORE)` (물·sediment solid 밀도) + `PNEW(CORE,K,NS)` 층별 size fraction(%)
- **erosion data (NSEDFLUME 분기)**:
  - **NSEDFLUME==1** (Sedflume 측정): `TAULOC(M)` shear 카테고리(ITBM개) + `ERATETEMP(CORE,K,M)` 층·shear별 침식률
  - **NSEDFLUME==2** (power-law): `TAULOC=[0, 1000]` + `EA(CORE,K), EN(CORE,K), MAXRATE(CORE,K)` (A·τ^N, [[efdc_sedzlj]] §2.2). `MAXRATE` cm/s → g/m²/s `×BDEN` (dry bulk density)

### 11.8 core→cell 매핑 + 초기화 (line 306-380) — deep

`NCORENO(I,J)>0` 인 cell L 에 core 값 할당:
- `TAUCOR(K,L) = TAUTEMP(CORE,K)` (층별 critical shear) + `ERATE(K,L,M) = ERATETEMP` (NSEDFLUME=1)
- `PERSED(NS,K,L) = PNEW/100` (mass fraction, `/DTOTAL` 정규화 mass balance)
- **porosity·bulk density**: dry density 입력 시 `PORBED = 1 - BDEN/SEDDENS`, `BULKDENS = BDEN`; wet 시 별식. BULKDENS≤0 → STOPP
- **Non-cohesive 비활성**: `SNDBT=0`, `ISTRAN(7)=0` (SEDZLJ 가 cohesive+noncohesive 내부 CALTRAN 처리)
- **초기 층질량** (NSEDFLUME≠3): `LAYERACTIVE = 2`(in-place, TSED0S>0) 또는 `0`; `TSED = TSED0 = TSED0S × BULKDENS` (g/cm²)
- **post-process**: `TSED0/BULKDENS < 1e-8` 또는 `K≤2`(active layer) → `HBED=TSED=TSED0=0`, `TAUCOR=1000` (무침식)
> §3 s_shear·§2 s_sedzlj 가 사용하는 bed state (TAUCOR/ERATE/PERSED/TSED/LAYERACTIVE/BULKDENS)를 모두 SEDIC 가 초기화.

### 11.9 Hard-bottom 표고 + KBT (line 392-405) — deep 2026-06-03

cold-start(IHTSTRT==0) cell별 bed 기하 계산:
```fortran
KBT(L) = -1                                ! line 396 - 질량 있는 첫 층
do K = 1,KB                                ! topdown
  if( TSED0(K,L)>0. .and. KBT(L)==-1 .and. K>2 ) KBT(L) = K     ! line 398
  TSET0T(L) = TSET0T(L) + TSED0(K,L)/BULKDENS(K,L)              ! 총 sediment 두께 누적
  HBED(L,K) = 0.01*TSED(K,L)/BULKDENS(K,L)                      ! line 400 - 층두께 (cm→m)
  HBEDA(L)  = HBEDA(L) + HBED(L,K)
enddo
if( KBT(L)==-1 ) KBT(L) = KB
ZELBEDA(L) = BELV(L) - HBEDA(L)            ! line 404 - Hard Bottom Elevation
```
- **KBT(L)** = top active layer index (질량 있는 최상위 층, K>2 parent layer 부터). 질량 전무 시 KB.
- s_shear는 `if( TAUCONST == 0 )then` 안의 `if( HP(L) < HPMIN )then`에서 CYCLE로 응력 갱신을 건너뛴다. (`SedTran-SEDZLJ/s_shear.f90:266` — `SHEAR = FC*VELMAG**2`; EFDC_Theory_Document_Ver_12.pdf, PDF 110쪽·인쇄 97쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽) (`SedTran-SEDZLJ/s_shear.f90:51` — `if( TAUCONST == 0 )then`; `SedTran-SEDZLJ/s_shear.f90:249` — `if( HP(L) < HPMIN )then`; `SedTran-SEDZLJ/s_shear.f90:250` — `CYCLE    ! *** Leave the shear unchanged from the last time HP >= HPMIN`) [10-12 전수 검증 보완] `NSEDFLUME`가 3이 아니면(1 또는 2) BULKDENS는 건조 벌크밀도로 직접 읽는다 [10-12 검증 보완] (`SedTran-SEDZLJ/s_sedic.f90:320` — `if( NSEDFLUME == 3 )then`; `SedTran-SEDZLJ/s_sedic.f90:322` — `else`). (`SedTran-SEDZLJ/s_sedic.f90:258` — `read(10,*) (BDEN(CORE,K),K = 1,KB)             ! *** read in the bulk density of the core`; `SedTran-SEDZLJ/s_sedic.f90:367` — `TSED(K,L)  = TSED0S(K,NCORENO(IL(L),JL(L)))*BULKDENS(K,L)  ! *** TSED  in units of (g/cm^2).`; EFDC_Theory_Document_Ver_12.pdf, PDF 110쪽·인쇄 97쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽) 현재 s_sedic는 `if( .true. )then`에서 `BULKDENS(K,L) = BDEN(CORE,K)`를 대입하므로 습윤 밀도 변환 ELSE를 실행하지 않는다. (`SedTran-SEDZLJ/s_sedic.f90:258` — `read(10,*) (BDEN(CORE,K),K = 1,KB)             ! *** read in the bulk density of the core`; `SedTran-SEDZLJ/s_sedic.f90:367` — `TSED(K,L)  = TSED0S(K,NCORENO(IL(L),JL(L)))*BULKDENS(K,L)  ! *** TSED  in units of (g/cm^2).`; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽, 식 6.116) (`SedTran-SEDZLJ/s_sedic.f90:335` — `if( .true. )then`; `SedTran-SEDZLJ/s_sedic.f90:338` — `BULKDENS(K,L) = BDEN(CORE,K)`) [10-12 전수 검증 보완] 침식률 깊이 보간은 위쪽 ERATE의 로그에 현재 잔여 질량비 SN01을 곱한다. (`SedTran-SEDZLJ/s_sedzlj.f90:499` — `+ SN10*EXP(SN11*LOG(ERATE(K+1,L,NTAU1))+SN01*LOG(ERATE(K,L,NTAU1))) )*BULKDENS(K,L)*SQRT(ONE/SH_SCALE(L))`; `SedTran-SEDZLJ/s_sedzlj.f90:494` — `SN01 = TSED(K,L)/TSED0(K,L)                  ! *** weighting factor 3`; `SedTran-SEDZLJ/s_sedzlj.f90:495` — `SN11 = (TSED0(K,L)-TSED(K,L))/TSED0(K,L)     ! *** weighting factor 4`; `SedTran-SEDZLJ/s_sedzlj.f90:498` — `ERATEMOD = ( SN00*EXP(SN11*LOG(ERATE(K+1,L,NTAU0))+SN01*LOG(ERATE(K,L,NTAU0))) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 110쪽·인쇄 97쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽) (`SedTran-SEDZLJ/s_sedzlj.f90:498` — `ERATEMOD = ( SN00*EXP(SN11*LOG(ERATE(K+1,L,NTAU0))+SN01*LOG(ERATE(K,L,NTAU0))) &`) [10-12 전수 검증 정정] 문서 식 6.118의 현재 두께 정의와 가중치가 반대이다. (`SedTran-SEDZLJ/s_sedzlj.f90:499` — `+ SN10*EXP(SN11*LOG(ERATE(K+1,L,NTAU1))+SN01*LOG(ERATE(K,L,NTAU1))) )*BULKDENS(K,L)*SQRT(ONE/SH_SCALE(L))`; `SedTran-SEDZLJ/s_sedzlj.f90:494` — `SN01 = TSED(K,L)/TSED0(K,L)                  ! *** weighting factor 3`; `SedTran-SEDZLJ/s_sedzlj.f90:495` — `SN11 = (TSED0(K,L)-TSED(K,L))/TSED0(K,L)     ! *** weighting factor 4`; `SedTran-SEDZLJ/s_sedzlj.f90:498` — `ERATEMOD = ( SN00*EXP(SN11*LOG(ERATE(K+1,L,NTAU0))+SN01*LOG(ERATE(K,L,NTAU0))) &`; EFDC_Theory_Document_Ver_12.pdf, PDF 112쪽·인쇄 99쪽, 식 6.118) 인용한 보간은 `if( LAYERACTIVE(K,L) == 2 )then` 안에서 `if( NSEDFLUME == 1 )then`과 `if( K+1 <= KB )then`을 통과할 때 적용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:489` — `if( LAYERACTIVE(K,L) == 2 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:491` — `if( NSEDFLUME == 1 )then`; `SedTran-SEDZLJ/s_sedzlj.f90:497` — `if( K+1 <= KB )then`) [10-12 전수 검증 보완] 마지막 층의 ELSE는 아래쪽 ERATE의 로그 대신 `LOG(1.0E-9)`를 사용한다. (`SedTran-SEDZLJ/s_sedzlj.f90:501` — `ERATEMOD = ( SN00*EXP(SN11*LOG(1.0E-9)+SN01*LOG(ERATE(K,L,NTAU0))) &`) [10-12 전수 검증 보완] 판정·근거: [정본 §5 행 eq-6-113](efdc_sedzlj.md#cv-e-hydro-709). <a id="cv-e-hydro-710"></a>결론: 문서 누락. 이론 문서 식 6.114는 HPMIN 미만에서 마찰계수 계산과 응력 갱신을 건너뛰어 이전 응력을 유지하는 규약을 누락한다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:14` — `c_f=\begin{cases}\dfrac{\kappa^2}{\left(\ln\dfrac{11H}{2z_b}\right)^2}&\text{for }H\geq H_{min}\\0.0&\text{for }H<H_{min}\end{cases}`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:249` — `if( HP(L) < HPMIN )then`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:250` — `CYCLE    ! *** Leave the shear unchanged from the last time HP >= HPMIN`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/varzerosnl.f90:27` — `HPMIN = 0.25      ! *** Minimum depth to compute shears`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_shear.f90:51` — `if( TAUCONST == 0 )then`; [EFDC-theory-hydro-vs-code §5 행 eq-6-114, B21](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:710)) <a id="cv-e-hydro-711"></a>결론: 문서에만 있음. SEDZLJ의 활성 입력 경로는 BDEN을 건조밀도로 받으며 습윤밀도 변환 else 분기는 if(.true.) 때문에 실행하지 않는다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:16` — `x_s\rho_s=\dfrac{\rho_s(\rho-\rho_w)}{\rho_s-\rho_w}=\dfrac{2.6}{1.6}(\rho-1)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:334` — `! *** Compute bed porosity and dry bulk density, depending on whether the SEDZLJ input files have wet or dry density`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:335` — `if( .true. )then`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:337` — `PORBED(L,K) = 1.-BDEN(CORE,K)/SEDDENS(CORE)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:338` — `BULKDENS(K,L) = BDEN(CORE,K)                                             ! *** Dry Bulk Density (BULKDENS)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:341` — `PORBED(L,K) = ( BDEN(1,K)-SEDDENS(CORE) ) / ( 1.-SEDDENS(CORE) )`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedic.f90:342` — `BULKDENS(K,L) = (1.-PORBED(L,K))*BDEN(CORE,K)                            ! *** Dry Bulk Density (BULKDENS)`; [EFDC-theory-hydro-vs-code §5 행 eq-6-116](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:711)) <a id="cv-e-hydro-712"></a>결론: 문서 오기. 이론 문서 식 6.118은 남은 층 두께 정의와 보간 가중치를 반대로 배치했으며 코드는 침식 전 위 경계값을 사용한다. (근거: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p109-126.md:16` — `\ln[E(T)]=\left(\dfrac{T_0-T}{T_0}\right)\ln(E^j)+\dfrac{T}{T_0}\ln\left(E^{j+1}\right)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:494` — `SN01 = TSED(K,L)/TSED0(K,L)                  ! *** weighting factor 3`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:495` — `SN11 = (TSED0(K,L)-TSED(K,L))/TSED0(K,L)     ! *** weighting factor 4`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:498` — `ERATEMOD = ( SN00*EXP(SN11*LOG(ERATE(K+1,L,NTAU0))+SN01*LOG(ERATE(K,L,NTAU0))) &`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/SedTran-SEDZLJ/s_sedzlj.f90:499` — `+ SN10*EXP(SN11*LOG(ERATE(K+1,L,NTAU1))+SN01*LOG(ERATE(K,L,NTAU1))) )*BULKDENS(K,L)*SQRT(ONE/SH_SCALE(L))`; [EFDC-theory-hydro-vs-code §5 행 eq-6-118](../../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:712)) [10-12 결론 검증 보완]
- **ZELBEDA = BELV − HBEDA** = hard-bottom 표고(bed 아래 불침식 기반). §3 s_shear 의 morphology 기준면.

### 11.10 Newly-deposited sediment: ERATEND + TAUCRITE (line 408-436) — deep

bed.sdf 후반부 — **신규 퇴적층(deposited)** 의 침식 파라미터 (NSICM = size-class-for-initial-condition 개수):
```fortran
read(30,*) (SCND(NSC),NSC=1,NSICM)         ! line 413 - size class 입경 (micron)
read(30,*) (TAUCRITE(NSC),NSC=1,NSICM)     ! line 415 - size별 침식 임계 (dynes/cm²)
if( NSEDFLUME==1 )then
  do NSC=1,NSICM; read(30,*)(ERATEND(NSC,M),M=1,ITBM); enddo   ! Sedflume 측정 침식률 table
else
  do NS=1,NSICM; read(30,*) ACTDEPA(NS),ACTDEPN(NS),ACTDEPMAX(NS); enddo  ! power-law E=A·τ^N
endif
```
- **SCND** = initial-condition size class 입경 (in-place core 의 D50 와 별개; **deposited sediment** 의 분류). 정밀도 offset `SCND(1)-=1e-6`, `SCND(NSICM)+=1e-6` (line 679-680).
- **TAUCRITE** = size class별 신규퇴적 erosion 임계 shear.
- **ERATEND(NSC,M)** (NSEDFLUME=1) = size·shear-category별 침식률 (in-place 의 ERATETEMP 대응, §11.7).
- **ACTDEPA/N/MAX** (NSEDFLUME=2) = 신규퇴적층 power-law `A·τ^N` 계수 + 상한 ([[efdc_sedzlj]] §2.2 in-place EA/EN/MAXRATE 대응). §2.4 active layer 가 이 deposited 파라미터로 침식.

### 11.11 DISTAR + settling velocity (Cheng 1998) (line 438-450) — deep

```fortran
DISTAR(K) = D50(K)/10000.*(((SEDDENS(1)/WATERDENS)-1.)*980./0.01**2)**(1./3.)   ! line 439
if( DWSIN(K) == -1 )then     ! DWS 미입력 → Cheng(1998)
  DWS(K) = 0.01/(D50(K)*0.0001)*(SQRT(25.+1.2*DISTAR(K)**2)-5.)**1.5            ! cm/s
else
  DWS(K) = DWSIN(K)          ! 직접 입력
endif
```
- **DISTAR** = dimensionless grain size $D_* = D_{50}\left[\frac{(s-1)g}{\nu^2}\right]^{1/3}$ (CGS: $\nu=0.01$ cm²/s, $g=980$). §11.2 의 `DWSIN(K)=-1` 시 settling 자동 계산.
- **Cheng 1998** model: $w_s=\frac{\nu}{d}(\sqrt{25+1.2D_*^2}-5)^{1.5}$ (cm/s). §11.2 에서 `DWSIN` 음수면 여기서 산출.

### 11.12 IHTSTRT > 0 — hotstart restart `SEDBED_HOT.SDF` (line 452-566) — deep

cold-start 대신 이전 run 의 bed state 복원:
- **version 체크** (line 458-469): 첫 줄 `TBEGINSEDZLJ, VER`. `VER<1240` → 파일 reset(구버전 헤더 없음).
- **read (global, master)**: `LAYERACTIVE`(8I8) / `KBT` / `D50AVG`(E17.9) / `BULKDENS` / `TSED` / `TSED0`(VER≥1240) / `PERSED` (6E17.9). broadcast → `Map2Local` local 매핑.
- **PERSED 정규화** (line 504-509): `DTOTAL=SUM(PERSED)`, `/DTOTAL` mass-balance 정밀도 보장.
- **bedload restart** (line 514-540): `ICALC_BL>0 & Restart_In_Ver>1000` → `CBL`(bedload 농도) read; `ISTRAN(5)>0` → `CBLTOX`(bedload toxics) read. ([[efdc_toxics]] 연계)
- **hard-bottom cell** (line 542-556): `LBED(L)` true → `LAYERACTIVE=0, TSED=TSED0=0, PORBED=BEDPORC`; else `PORBED=1−BULKDENS/SEDDENS(CORE)`.
- format: `34567 E17.9` / `34568 6E17.9` / `34569 8I8`.

### 11.13 Wave 입력 (line 570-607)

`ISWNWAVE` (§11.2 bed.sdf 입력) 분기:
- **==1** `fetch.inp`: `FWDIR(L,FDIR)` 8방위 wave fetch (내부 wind-wave 생성용).
- **==2** `stwave.inp`: STWAVE 결합 — `STWVHT`(파고)/`STWVTP`(주기)/`STWVDR`(방향) per cell, `STWVNUM` 데이터셋 × `STWVTIM` 간격. §3 s_shear 의 wave-current bed shear (Christoffersen-Jonsson) 입력.

### 11.14 Toxics용 bed array 초기화 + 단위 변환 (line 678-763) — deep ★

```fortran
WSEDO(1:NSEDS)  = DWS(1:NSEDS)/100.0      ! line 696 - 침강속도 cm/s → m/s (SEDZLJ 외부용)
SEDDIA(1:NSEDS) = D50(1:NSEDS)/1.d6        ! line 697 - 입경 micron → m
if( BEDLOAD_CUTOFF < 10. ) BEDLOAD_CUTOFF = 64.   ! line 701 - bedload 입경 임계 default 64 micron
```
- SEDZLJ는 코드 주석이 압밀이 없다고 명시한다. (`SedTran-SEDZLJ/s_sedic.f90:704` — `! *** SEDZLJ DOES NOT HAVE CONSOLIDATION.  SO PORBED, PORBED1, VDRBED ARE TEMPORALLY CONSTANT`; EFDC_Theory_Document_Ver_12.pdf, PDF 106쪽·인쇄 93쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 107쪽·인쇄 94쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 108쪽·인쇄 95쪽)
- **toxics-용 bed array** (CALTOX/CALTOXB 가 사용, [[efdc_toxics]]):
  - `SEDBT(L,K) = TSED·10000` (g/cm²→g/m²), `SEDB(L,K,NS) = SEDBT·PERSED` (class별 질량), `SEDDIA50` 층 D50, `VDRBED=PORBED/(1−PORBED)` void ratio.
  - prev-timestep copy: `HBED1/PORBED1/VDRBED1/SEDB1`.
- **D50AVG** (line 682-693, cold-start): bed 표면 질량층의 `SUM(PERSED·D50)`, 최소 `D50(1)`.
- **empty-layer collapse** (line 727-760, IHTSTRT>0): active(1)+deposition(2) 층을 KBT 로 합치고 그 사이/위 빈 층 0. restart 후 층 구조 정돈.
- 종료: `SNDVDRD=BEDPORC/(1−BEDPORC)`(non-cohesive void ratio, SEDZLJ 미사용) + `deallocate(TAUTEMP,BDEN,PNEW)` (임시 core 배열 해제).

> **§11 완결 (line 1-769 전체 verified)**: SEDIC 가 §2 s_sedzlj·§3 s_shear 의 in-place/deposited bed state + §11.14 toxics(CALTOX/CALTOXB) bed array + WSEDO/SEDDIA 단위까지 모두 초기화. cold-start(core map→Sedflume→층질량) vs hotstart(SEDBED_HOT.SDF restore) 두 경로.
