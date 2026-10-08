---
title: "EFDC+ scalar transport 수치 스킴 — CALTRAN donor-cell upwind + CALTRAN_AD Smolarkiewicz MPDATA anti-diffusion (ISADAC/ISFCT) + CALCONC dispatch"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/caltran.f90 (373) + caltran_ad.f90 (347) + calconc.f90 (528) 직접 read. upwind flux FUHUD=UHDY2·CON1(LUPU) + LUPU/LUPV flow-sign upwind index + anti-diffusive pseudo-velocity UHU + cross-derivative MPDATA 항 + ISADAC/ISFCT 입력(input.f90:306/mod_scaninp.f90:117) file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-03
verification_by: "Claude Opus 4.8 (1M context) — upwind+MPDATA 스킴 + dispatch 구조 verbatim"
verification_date: 2026-06-03
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_vertical.md
  - models/EFDC/source-analysis/efdc_water_quality.md
  - models/EFDC/source-analysis/sediment/efdc_sediment.md
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

# EFDC+ scalar transport 수치 스킴 — CALTRAN / CALTRAN_AD / QUICKEST·ULTIMATE

> `Transport/caltran.f90`(373) + `caltran_ad.f90`(347) + `calconc.f90`(528) 직접 read. **scalar(염분·수온·dye·SFL·toxic·SED·SND·WQ)의 advection 수치 알고리즘** = **1차 donor-cell upwind + Smolarkiewicz MPDATA anti-diffusive corrector**, v12.5 active WC dispatch에는 **`ISQUICK == 1` QUICKEST/ULTIMATE** 경로가 추가됐다 (`calconc.f90:198-203`). 여러 노트가 CALTRAN 호출 맥락(dry mask·open-BC·vertical)을 다뤘으나, 본 노트는 **advection 스킴 자체**의 canonical. [[efdc_hydro_core]](운동량)·[[efdc_vertical]](연직 advection)·[[efdc_water_quality]]·[[efdc_sediment]]·[[efdc_toxics]] 가 공유.

## 1. CALCONC dispatch (calconc.f90)

scalar transport driver. `ISTRAN(NN)>0` constituent 마다 active water-column(IW) 으로 묶어 transport:
```fortran
ISTRAN: 1 염분 / 2 수온 / 3 dye / 4 SFL(shellfish larvae) / 5 toxic / 6 SED(cohesive) / 7 SND(noncohesive) / 8 WQ
```
1. **upwind cell 사전지정** (`calconc.f90:117-132`): `ISQUICK == 0 .or. ISTRAN(4) > 0 .or. (ISTRAN(2) > 0 .and. ISICE == 4)`일 때 수행.
```fortran
LUPU(L,K) = UHDY2(L,K) >= 0 ? LWC(L) : L     ! x-flux donor cell (서/현)
LUPV(L,K) = VHDX2(L,K) >= 0 ? LSC(L) : L     ! y-flux donor cell (남/현)
```
2. 식 3.3은 문서의 분할 유도식이다. (EFDC_Theory_Document_Ver_12.pdf, PDF 68쪽·인쇄 55쪽, 식 3.3) 활성 농도 수송은 상류 농도 또는 QUICKEST 면 농도를 사용한다. (`Transport/caltran.f90:148` — `FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)`; `Transport/caltran.f90:149` — `FVHUD(L,K,IW) = VHDX2(L,K)*CON1(LUPV(L,K),K)`; `Transport/calconc.f90:198` — `if( ISQUICK == 1 )then`; `Transport/calconc.f90:200` — `call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 68쪽·인쇄 55쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 69쪽·인쇄 56쪽) 식 3.10의 단순 두 농도 산술 평균을 계산하는 경로를 찾지 못했다. (`Transport/caltran.f90:148` — `FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)`; `Transport/caltran.f90:149` — `FVHUD(L,K,IW) = VHDX2(L,K)*CON1(LUPV(L,K),K)`; `Transport/calconc.f90:198` — `if( ISQUICK == 1 )then`; `Transport/calconc.f90:200` — `call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 69쪽·인쇄 56쪽, 식 3.10)
3. ISKIP=0과 ISQUICK=0이면 CALTRAN_AD를 호출한다. (`Transport/calconc.f90:228` — `if( ISKIP(IW) == 0 .AND. ISQUICK == 0 )then`; `Transport/calconc.f90:230` — `call CALTRAN_AD( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT )`) CALTRAN_AD는 ISADAC=0이면 반환한다. (`Transport/calconc.f90:230` — `call CALTRAN_AD( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT )`; `Transport/caltran_ad.f90:41` — `if( ISADAC(MVAR) == 0 ) return    ! *** SKIP IF NOT USING ANTI-DIFFUSION`) 그 뒤 CALCONC는 Communicate_CON2를 호출한다. (`Transport/calconc.f90:230` — `call CALTRAN_AD( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT )`; `Transport/caltran_ad.f90:41` — `if( ISADAC(MVAR) == 0 ) return    ! *** SKIP IF NOT USING ANTI-DIFFUSION`)
4. CALCONC는 연직 확산 뒤 CALHEAT를 호출한다. (`Transport/calconc.f90:482` — `call CALHEAT`) CALDYE는 그 뒤이다. (`Transport/calconc.f90:488` — `if( ISTRAN(3) >= 1 ) CALL CALDYE`) SSEDTOX는 후반 퇴적 주기 분기에 있다. (`Transport/calconc.f90:520` — `call SSEDTOX`; `Transport/calconc.f90:533` — `call SSEDTOX`)

### CALDYE 반응과 물의 나이

해석: 문서 식 4.1의 농도 반응률을 보존형 HC식에 넣으려면 체적 계수가 필요하다(정적 판독, 실행 미확인). (`Transport/caltran.f90:169` — `CD(L,K,IT) = CON1(L,K)*H1PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽, 식 4.1) 온도 독립 영차 감쇠는 찾지 못했다. (`Transport/caldye.f90:82` — `DYE(L,K,MD) = DYE(L,K,MD) - ( DYES(MD).KRATE0**(TEM(L,K)-DYES(MD).TREF) + DYE(L,K,MD)*DYES(MD).KRATE1**(TEM(L,K)-DYES(MD).TREF) )*DAGE`; `Transport/caldye.f90:76` — `if( DYES(MD).TREF > 0. .and. ISTRAN(2) > 0 .and. DYES(MD).KRATE0 > 0.0 )then`; `Transport/caldye.f90:86` — `elseif( DYES(MD).KRATE1 /= 0.0 )then`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) 온도 분기는 KRATE0^ΔT+C·KRATE1^ΔT를 뺀다. (`Transport/caldye.f90:82` — `DYE(L,K,MD) = DYE(L,K,MD) - ( DYES(MD).KRATE0**(TEM(L,K)-DYES(MD).TREF) + DYE(L,K,MD)*DYES(MD).KRATE1**(TEM(L,K)-DYES(MD).TREF) )*DAGE`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) TADJ는 그 식에 쓰이지 않는다. (`Transport/caldye.f90:82` — `DYE(L,K,MD) = DYE(L,K,MD) - ( DYES(MD).KRATE0**(TEM(L,K)-DYES(MD).TREF) + DYE(L,K,MD)*DYES(MD).KRATE1**(TEM(L,K)-DYES(MD).TREF) )*DAGE`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) 양의 일차 감쇠는 후진 Euler이다. (`Transport/caldye.f90:91` — `CDYETMP = 1./(1.+DYESTEP*DYES(MD).KRATE1)   ! *** Growth rate`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) 음의 일차율은 지수 증가이다. (`Transport/caldye.f90:88` — `if( DYES(MD).KRATE1 < 0.0 )then`; `Transport/caldye.f90:89` — `CDYETMP = EXP(-DYES(MD).KRATE1*DYESTEP)     ! *** Exponential decay`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) 물의 나이는 ITYPE=2에서 Δt/86400을 더한다. (`Transport/caldye.f90:130` — `elseif( DYES(MD).ITYPE == 2 )then`; `Transport/caldye.f90:132` — `DAGE = DELT/86400.`; `Transport/caldye.f90:139` — `DYE(L,K,MD) = DYE(L,K,MD) + DAGE`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) 문서 식 4.5의 −K를 이 코드와 연결하려면 K=−1이라는 추가 조건이 필요하다. (`Transport/caldye.f90:130` — `elseif( DYES(MD).ITYPE == 2 )then`; `Transport/caldye.f90:132` — `DAGE = DELT/86400.`; `Transport/caldye.f90:139` — `DYE(L,K,MD) = DYE(L,K,MD) + DAGE`; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽, 식 4.5) Confluence는 그 음의 플래그를 명시한다. (`models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Dye.md:24` — `3. *Age of Water (days):* in which case dye is used as a proxy for age, and the 0th-order decay flag is set to -1 so that EE will calculate age. All other columns will be zero in this option.`; EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽) PDF의 C(day)·t(day)·K(1/day) 단위 정의는 영차식의 차원과 맞지 않는다. (EFDC_Theory_Document_Ver_12.pdf, PDF 70쪽·인쇄 57쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 71쪽·인쇄 58쪽)


## 2. CALTRAN — donor-cell upwind (caltran.f90)

### 2.1 upwind flux
```fortran
FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)   ! line 148 - x-방향 upwind 질량 flux
! (FVHUD = VHDX2·CON1(LUPV), FWUU = 연직 W2·CON1(upwind layer))
```
- CALUVW는 UHDY2/VHDX2/W2를 시간 구간 평균으로 만든다. (`caluvw.f90:848` — `UHDY2(L,K) = 0.5*(UHDY(L,K) + UHDY1(L,K))`; `caluvw.f90:868` — `UHDY2(L,K) = 0.5*(UHDY(L,K) + UHDY2(L,K))`; `Transport/caltran.f90:148` — `FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)`) CALTRAN은 이 평균 유량과 이전 농도 CON1로 이류 플럭스를 계산한다. (`Transport/caltran.f90:148` — `FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)`)
- 수송은 이전 층 두께와 농도로 질량을 구성한다. (`Transport/caltran.f90:169` — `CD(L,K,IT) = CON1(L,K)*H1PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`; `Transport/caltran.f90:170` — `FUHUD(L,K,IW)-FUHUD(LEC(L),K,IW) + FVHUD(L,K,IW)-FVHUD(LNC(L),K,IW) ) * DXYIP(L)   &`; `Transport/caltran.f90:171` — `+ (FWUU(L,K-1,IW)-FWUU(L,K,IW)) )`; `Transport/caltran.f90:204` — `CON(L,K) = CD(L,K,IT)*HPKI(L,K)`) 수송은 발산과 원천 항으로 질량을 갱신한다. (`Transport/caltran.f90:169` — `CD(L,K,IT) = CON1(L,K)*H1PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`; `Transport/caltran.f90:170` — `FUHUD(L,K,IW)-FUHUD(LEC(L),K,IW) + FVHUD(L,K,IW)-FVHUD(LNC(L),K,IW) ) * DXYIP(L)   &`; `Transport/caltran.f90:171` — `+ (FWUU(L,K-1,IW)-FWUU(L,K,IW)) )`; `Transport/caltran.f90:204` — `CON(L,K) = CD(L,K,IT)*HPKI(L,K)`) 수송은 현재 층 두께의 역수로 농도를 복원한다. (`Transport/caltran.f90:169` — `CD(L,K,IT) = CON1(L,K)*H1PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`; `Transport/caltran.f90:170` — `FUHUD(L,K,IW)-FUHUD(LEC(L),K,IW) + FVHUD(L,K,IW)-FVHUD(LNC(L),K,IW) ) * DXYIP(L)   &`; `Transport/caltran.f90:171` — `+ (FWUU(L,K-1,IW)-FWUU(L,K,IW)) )`; `Transport/caltran.f90:204` — `CON(L,K) = CD(L,K,IT)*HPKI(L,K)`)

CALTRAN은 원천과 이류를 같은 질량 갱신에 더한다. (`Transport/caltran.f90:183` — `CD(L,K,IT) = CON1(L,K)*H2PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`; `Transport/caltran.f90:184` — `FUHUD(L,K,IW)-FUHUD(LEC(L),K,IW) + FVHUD(L,K,IW)-FVHUD(LNC(L),K,IW) ) * DXYIP(L)   &`; `Transport/caltran.f90:185` — `+ (FWUU(L,K-1,IW)-FWUU(L,K,IW))  )`; EFDC_Theory_Document_Ver_12.pdf, PDF 68쪽·인쇄 55쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 69쪽·인쇄 56쪽) 원천 전용 C* 배열은 없다. (`Transport/caltran.f90:183` — `CD(L,K,IT) = CON1(L,K)*H2PK(L,K) + DDELT*( ( FQC(L,K,IT) +                                                                      &`; `Transport/caltran.f90:184` — `FUHUD(L,K,IW)-FUHUD(LEC(L),K,IW) + FVHUD(L,K,IW)-FVHUD(LNC(L),K,IW) ) * DXYIP(L)   &`; `Transport/caltran.f90:185` — `+ (FWUU(L,K-1,IW)-FWUU(L,K,IW))  )`; EFDC_Theory_Document_Ver_12.pdf, PDF 68쪽·인쇄 55쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 69쪽·인쇄 56쪽) 운동량 중앙차분은 별도 구현이다. (`Transport/caltran.f90:148` — `FUHUD(L,K,IW) = UHDY2(L,K)*CON1(LUPU(L,K),K)`; `Transport/caltran.f90:149` — `FVHUD(L,K,IW) = VHDX2(L,K)*CON1(LUPV(L,K),K)`; `Transport/calconc.f90:198` — `if( ISQUICK == 1 )then`; `Transport/calconc.f90:200` — `call CALTRAN_QUICKEST( IACTIVEWC1(IW), IACTIVEWC2(IW), WCV(IW).VAL0, WCV(IW).VAL1, IW, IT, WCV(IW).WCLIMIT, ISKIP(IW) )`; EFDC_Theory_Document_Ver_12.pdf, PDF 68쪽·인쇄 55쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 69쪽·인쇄 56쪽)

- → **1차 풍상차분**(donor-cell): monotone·positive 보장하나 **수치확산 큼**.

### 2.2 시간 스텝 DDELT (line 62-77)
- 3TL: `ISTL==3 → DT2`(leapfrog full), `ISTL==2 → DT`(corrector, ISUD=0). 2TL/dynamic: `DT`/`DTDYN`.

## 3. CALTRAN_AD — Smolarkiewicz MPDATA anti-diffusive corrector (caltran_ad.f90) ★

donor-cell 의 수치확산을 상쇄하는 **2차 보정 pass** (2020-01 MPI 분리 split):
```fortran
AUHU  = ABS(UHDY2(L,K))                                    ! line 105
UTERM = AUHU*( POS(L,K) - POS(LW,K) )                      ! 1차 anti-diffusive (확산 = |u|Δx 상쇄)
UTERM = UTERM - 0.5*DDELTA*UHDY2*( VVVV+VVVV + WWWW+WWWW + UUUU+UUUU )  ! line 109-112 cross-derivative (다차원 MPDATA)
UHU   = UTERM/( POS(L,K) + POS(LW,K) + BSMALL )            ! line 114 - anti-diffusive pseudo-velocity
FUHUD(L,K,IW) = max(UHU,0.)*POS(LW,K) + min(UHU,0.)*POS(L,K)  ! line 115 - pseudo-velocity 로 재-upwind
```
- **POS** = 양정치(positive-definite) 농도장, `UUUU/VVVV/WWWW` = 정규화 흐름성분.
- **원리** (Smolarkiewicz 1984 MPDATA): donor-cell 의 implicit 확산을 "anti-diffusive velocity" `UHU = |u|(C_L−C_LW)/(C_L+C_LW)` 로 추정해 반대로 다시 upwind → 수치확산 차수 1→2 향상, **양정치 유지**.
- **cross-derivative 항**(line 109-143)이 다차원 MPDATA 의 핵심(1D 분리오차 보정).

## 4. ISQUICK / ISADAC / ISFCT — scalar 스킴 선택·constituent별 토글 (input.f90:311)

입력 카드 C6(constituent별; `ISQUICK`은 scalar):
```fortran
read ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), -, -, -, ISCI(NS), ISCO(NS)
```
| flag | 의미 |
|---|---|
| **ISQUICK** | 현재 C6는 NS=0부터 8까지 행을 읽는다. (`input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) 각 행의 3번째 열은 같은 scalar ISQUICK이다. (`input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; `input.f90:319` — `if( ISQUICK /= 0 .and. ISQUICK /= 1 )then`; `input.f90:324` — `ISQUICK = 0`; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) 마지막 행의 값이 남는다. (`input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; `input.f90:319` — `if( ISQUICK /= 0 .and. ISQUICK /= 1 )then`; `input.f90:324` — `ISQUICK = 0`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:20` — `\* ISCDCA: 0 FOR STANDARD DONOR CELL UPWIND DIFFERENCE ADVECTION (3TL ONLY)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:22` — `\*                1 FOR CENTRAL DIFFERENCE ADVECTION FOR THREE TIME LEVEL STEPS (3TL ONLY)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:24` — `\*                2 FOR EXPERIMENTAL UPWIND DIFFERENCE ADVECTION (FOR RESEARCH) (3TL ONLY)`; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) 코드는 최종 값이 0 또는 1이 아니면 0으로 바꾼다. (`input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; `input.f90:319` — `if( ISQUICK /= 0 .and. ISQUICK /= 1 )then`; `input.f90:324` — `ISQUICK = 0`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:20` — `\* ISCDCA: 0 FOR STANDARD DONOR CELL UPWIND DIFFERENCE ADVECTION (3TL ONLY)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:22` — `\*                1 FOR CENTRAL DIFFERENCE ADVECTION FOR THREE TIME LEVEL STEPS (3TL ONLY)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:24` — `\*                2 FOR EXPERIMENTAL UPWIND DIFFERENCE ADVECTION (FOR RESEARCH) (3TL ONLY)`; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) 6·7·8번째 열은 ldum이다. (`input.f90:311` — `read(1,*,IOSTAT = ISO) ISTRAN(NS), ISTOPT(NS), ISQUICK, ISADAC(NS), ISFCT(NS), ldum, ldum, ldum, ISCI(NS), ISCO(NS)`; `input.f90:319` — `if( ISQUICK /= 0 .and. ISQUICK /= 1 )then`; `input.f90:324` — `ISQUICK = 0`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:20` — `\* ISCDCA: 0 FOR STANDARD DONOR CELL UPWIND DIFFERENCE ADVECTION (3TL ONLY)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:22` — `\*                1 FOR CENTRAL DIFFERENCE ADVECTION FOR THREE TIME LEVEL STEPS (3TL ONLY)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_6.md:24` — `\*                2 FOR EXPERIMENTAL UPWIND DIFFERENCE ADVECTION (FOR RESEARCH) (3TL ONLY)`; EFDC_Manual.pdf, PDF 23쪽·인쇄 19쪽) |
| **ISADAC(NS)** | 0 = donor-cell upwind 만(수치확산 큼) / **1 = anti-diffusion(MPDATA) 적용** |
| **ISFCT(NS)** | flux corrector(FCT) — anti-diffusion 후 **monotonicity 보장**(local min/max clamp, caltran_ad CWMAX/CWMIN 등) |
| ISCI/ISCO | concentration input/output series 토글 |

→ **`ISQUICK == 0`일 때 ISADAC=1 + ISFCT=1** = MPDATA + flux-corrected transport (실무 표준: 염분·수온 front 보존). `ISQUICK == 0`에서 ISADAC=0 = 순수 upwind(안정하나 smearing). `NANTIDIFF` = anti-diffusion 적용 constituent 수 카운트(calconc:93-99). `CALTRAN_AD` 호출은 `ISQUICK == 0`일 때만 발생하고 (`calconc.f90:228-230`), `ISADAC` 반확산 적용도 동일 게이트를 사용한다 (`calconc.f90:250`).

CALTRAN_AD 호출은 ISKIP=0도 검사한다. (`Transport/calconc.f90:228` — `if( ISKIP(IW) == 0 .AND. ISQUICK == 0 )then`) CALTRAN_AD는 ISADAC=0이면 바로 반환한다. (`Transport/caltran_ad.f90:41` — `if( ISADAC(MVAR) == 0 ) return    ! *** SKIP IF NOT USING ANTI-DIFFUSION`)


## 5. 비교·맥락

- **vs 운동량 advection**([[efdc_hydro_core]]): 운동량은 별도(CALUVW 등), 본 스킴은 **scalar 전용**.
- **연직 advection**([[efdc_vertical]] caltran.f90:152-228): 동일 스킴의 연직(FWUU) 성분 + SGZ inactive-layer skip.
- SSEDTOX는 ISTRAN(6) 또는 ISTRAN(7)을 요구한다. (`Transport/calconc.f90:508` — `if( ( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 ) .and. TIMEDAY >= SEDSTART )then`) SSEDTOX는 SEDSTART와 퇴적 주기도 검사한다. (`Transport/calconc.f90:508` — `if( ( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 ) .and. TIMEDAY >= SEDSTART )then`) 독성 수송만 활성인 조건은 이 게이트를 열지 않는다. (`Transport/calconc.f90:508` — `if( ( ISTRAN(6) >= 1 .or. ISTRAN(7) >= 1 ) .and. TIMEDAY >= SEDSTART )then`; `Transport/calconc.f90:512` — `if( SEDTIME >= SEDSTEP )then`; `Transport/calconc.f90:525` — `if( NCTBC == 1 )then`)
- dry-cell/open-BC 처리: [[efdc_wetdry]]·[[efdc_boundary_conditions]] (LMASKDRY/LKSZ skip).

## 6. 연결

- [[efdc_hydro_core]] — UHDY2/VHDX2 face transport(이 스킴의 입력 flux), 운동량 측

CALUVW는 같은 단계에서 수송용 시간 구간 평균 유량을 만든다. (`caluvw.f90:848` — `UHDY2(L,K) = 0.5*(UHDY(L,K) + UHDY1(L,K))`; `Transport/calconc.f90:123` — `if( UHDY2(L,K) >= 0.0 )then`)

- [[efdc_vertical]] — 연직 advection(FWUU) + SGZ
- [[efdc_water_quality]] / [[efdc_sediment]] / [[efdc_sedzlj]] / [[efdc_toxics]] — CALTRAN 으로 이송되는 scalar
- [[efdc_wetdry]] / [[efdc_boundary_conditions]] — dry mask·open-BC 처리
- Smolarkiewicz P.K. 1984 (MPDATA) — anti-diffusion 알고리즘 lineage(코드 주석 미명시, 구조 기반 식별)
