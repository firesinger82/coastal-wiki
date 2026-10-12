---
title: "EFDC+ 퇴적물 diagenesis source-analysis — mod_diagen.f90 (Cerco-Cole/Di Toro 2-layer sediment flux, SOD Brent 폐합)"
topic: efdc-sediment-diagenesis
canonical_source: self
citation_status: verified
verification_method: "EFDC+ Stable(12.4, sha 3ed76b6) raw source 직접 read: Eutrophication/mod_diagen.f90(1394) — SOD ZBRENT root(:969)·ammonium 벤딕 flux(:998)·s=SOD/O2 closure(:1177) file:line 직접 검증. 소스주석 primary Numerical Recipes(:1259). 범위=SMMBE 드라이버 + ammonia/nitrification 2-layer flux(H2S/CH4/PO4/Si 요약). [[efdc_water_quality]] 는 dispatch만·[[efdc_rpem_vegetation]] 은 pool 소비만."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-07-07
verification_by: "Claude Opus 4.8 (1M context) — mod_diagen.f90:967-975·996-1001·1174-1179 직접 read 검증"
verification_date: 2026-07-07
related:
  - models/EFDC/source-analysis/efdc_water_quality.md
  - models/EFDC/source-analysis/efdc_rpem_vegetation.md
  - models/EFDC/source-analysis/sediment/efdc_sedzlj.md
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# EFDC+ 퇴적물 diagenesis — `mod_diagen.f90` (`WQ_DIAGENESIS`)

> 소스: [`Eutrophication/mod_diagen.f90`](../raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90) (1394). EFDC+ Stable = 12.4.
> **정체**: Cerco-Cole 1994(CE-QUAL-ICM) / Di Toro 2001 **2-layer 퇴적물 flux** 서브모델. **pore-water pool `SM2NH4/NO3/PO4` + 벤딕 flux `WQBFNH4/NO3/PO4D/O2(SOD)/COD` 생산** — [[efdc_rpem_vegetation]]·수질 F1 이 이 pool 을 소비. [[efdc_water_quality]]:98-104 은 dispatch(`IWQBEN==1`·`SMMBE`)만, flux 알고리즘 미문서.
> ★**line range 정정**: water_quality:21 은 `mod_diagen.f90:9-1029` 이라 했으나 module `END`는 :1107, **flux kernel(SEDFLUXNEW/ZBRENT/SOLVSMBE)은 :1121-1393** — stale 인용은 solver 전체를 놓침.

## 0. 구조

| 서브루틴 | 라인 | 역할 |
|---|---|---|
| `SMRIN1_JNP` | 95-580 | `wq_3dsd.jnp` 입력 + **온도의존 Arrhenius θ^(T-20) 테이블 구성**(:481-503) |
| `WQSDICI` | 591-662 | 초기조건(POM G-class·pore-water 농도) |
| `SMMBE` | 674-1105 | **master 드라이버**: deposition→POM 물질수지→diagenesis flux→benthic stress→mixing→셀별 NH4/NO3/H2S/CH4/PO4/Si flux |
| `SOLVSMBE` | 1121-1141 | 2×2 2-layer 선형계(Cramer) |
| `SEDFLUXNEW` | 1152-1237 | **flux kernel**: 시행 surface transfer coeff 로 NH4→NO3→H2S/CH4 순차해 → SOD residual |
| `ZBRENT` | 1263-1393 | Brent 근찾기(SOD/표면전달계수, Numerical Recipes p.253) |

## 1. POM G-class diagenesis (SMMBE)

```fortran
SMTDCD(IT,M) = SMKPOC(M)*SMTHKC(M)**TT20                          ! :484 3 G-class(G1 반응성/G2 난분해/G3 불활성) Arrhenius
! deposition(algae WQDFB + refractory + labile G1) :774-790
SMPOC(L,M) = (SMPOC + SMDFC*SMDTOH)/(SMW2DTOH + SMTDCD*DTWQ)      ! :816 POM 물질수지(burial+decay, 2-layer)
SMDGFN(L)  = SMHSED*(SMTDND(,1)*SMPON(,1) + SMTDND(,2)*SMPON(,2)) ! :824 G1+G2 → diagenesis flux(N/P/C, pore-water 공급)
```
코드는 저층 DO를 읽어 만든 보조 변수 XSMO20에 3.0의 하한을 적용한다. (`Eutrophication/mod_diagen.f90:828` — `XSMO20(L) = max( WQV(L,KSZ(L),IDOX), 3.0 )`) (`Eutrophication/mod_diagen.f90:828` — `XSMO20(L) = max( WQV(L,KSZ(L),IDOX), 3.0 )`) [10-12 전수 검증 정정] SMW12는 산소 Monod 항과 G1 POC 항에 저서 스트레스 계수 (1−SMKBST·SMBST)를 곱한다. (`Eutrophication/mod_diagen.f90:885` — `SMW12(L)  = SMDP(IZ)*SMTDDP(ISMT(L)) * SMPOC(L,1) * XSMO20(L) * (1.0-SMKBST*SMBST(L)) / (SMKMDP+XSMO20(L)+ 1.E-18) + SMDPMIN(IZ)`) SMW12는 SMDPMIN을 더한다. (`Eutrophication/mod_diagen.f90:885` — `SMW12(L)  = SMDP(IZ)*SMTDDP(ISMT(L)) * SMPOC(L,1) * XSMO20(L) * (1.0-SMKBST*SMBST(L)) / (SMKMDP+XSMO20(L)+ 1.E-18) + SMDPMIN(IZ)`) SMKL12는 온도 보정 확산과 SMRBIBT·SMW12의 합이다. (`Eutrophication/mod_diagen.f90:885` — `SMW12(L)  = SMDP(IZ)*SMTDDP(ISMT(L)) * SMPOC(L,1) * XSMO20(L) * (1.0-SMKBST*SMBST(L)) / (SMKMDP+XSMO20(L)+ 1.E-18) + SMDPMIN(IZ)`) <a id="cv-e-wq-750"></a>결론: 문서 누락. EFDC+ 12.5의 diagenesis는 저층 DO를 최소 3.0 g O₂/m³로 제한한 값으로 교환·반응·분배를 계산한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:19`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:20`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:22`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:24`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:25`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:28`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:29`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:21`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:30`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:828` — `XSMO20(L) = max( WQV(L,KSZ(L),IDOX), 3.0 )`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:885` — `SMW12(L)  = SMDP(IZ)*SMTDDP(ISMT(L)) * SMPOC(L,1) * XSMO20(L) * (1.0-SMKBST*SMBST(L)) / (SMKMDP+XSMO20(L)+ 1.E-18) + SMDPMIN(IZ)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:886` — `SMKL12(L) = SMDD(IZ)*SMTDDD(ISMT(L)) + SMRBIBT*SMW12(L)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:934` — `SK1NH4SM = ( SMKNH4(IZ)*SMTDNH4(ISMT(L)) * XSMO20(L) ) / ( (SMKMO2N+XSMO20(L)+ 1.E-12) * (SMKMNH4+SM1NH4(L)) )`; [EFDC-theory-wq-vs-code §5 행 L272, L273, L274, L275, L278, L286, L287, L290, L305, L306, L614, L649, L650](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:750)) [10-12 결론 검증 보완]

결론: 문서에만 있음. EFDC+ 12.5는 퇴적하는 분해성 입자와 흡착 인을 G1에 배분한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:15`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:20`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:784` — `! *** Labile POM source terms, only G1 class`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:786` — `SMDFN(L,1) = SMDFN(L,1) + WQDFLN(L)  ! *** LPON`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:787` — `SMDFP(L,1) = SMDFP(L,1) + WQDFLP(L)  ! *** LPOP`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:788` — `SMDFC(L,1) = SMDFC(L,1) + WQDFLC(L)  ! *** LPOC`; [EFDC-theory-wq-vs-code §5 행 L261, L262, L263, L540](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:748))

결론: 코드 결함 후보. EFDC+ 12.5의 퇴적층 규소 공급은 공통 공급량을 규소 조류군마다 반복하는 결함 후보이다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:15`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:27`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:30`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1035` — `if( ALGAES(NAL).ISILICA > 0 ) SMDFSI(L) = SMDFSI(L) + (ALGAES(NAL).WQASC*WQDFB(L,NAL) + WQDFSI(L) + SMJDSI) * SMDTOH(ISMZMAP(L))`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:773` — `SMDFNA = SMDFNA + SMFNBA(NAL,M)*ALGAES(NAL).WQANCA*WQDFB(L,NAL)  ! *** RPON`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:778` — `SMDFN(L,M) = SMDFNA + SMFNR(ISMZMAP(L),M)*WQDFRN(L)                ! *** RPON`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:786` — `SMDFN(L,1) = SMDFN(L,1) + WQDFLN(L)  ! *** LPON`; [EFDC-theory-wq-vs-code §5 행 L264, L300, L313](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:749))


## 2. Ammonia/nitrification 2-layer + ★SOD Brent 폐합

```fortran
SK1NH4SM = SMKNH4*SMTDNH4*O2/((SMKMO2N+O2)*(SMKMNH4+SM1NH4))     ! :936 nitrification 2-Monod(O2·NH4)
! ammonia 2-layer 계수 A1/A2NH4SM, source B2NH4SM = SMDGFN + SMHODT*SM2NH4  :937-941
SMSOD = ZBRENT(L, ..., SK1NH4SM,A1NH4SM,..., SM2NH4(L),...)      ! :969 ★SOD = flux balance 의 근(Brent)
RSMSS = SMSOD1/(XSMO20(L)+1.E-18)                                ! :1177 ★s=SOD/O2(0) Di Toro 폐합
RNSODSM = SMO2NH4*RJNITSM ; SMSOD = CSODSM + RNSODSM             ! :1232 SOD = 탄소성(H2S/CH4) + 질소성(nitrification)
WQBFO2(L) = -SMSOD*SODMULT(IZ)                                    ! :989 SOD 벤딕 flux
WQBFNH4(L)  = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))   ! Eutrophication/mod_diagen.f90:996 — `WQBFNH4(L)  = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))` [10-12 전수 검증 정정]
WQBFNO3(L) = SMSS(L)*(SM1NO3(L) - WQV(L,KSZ(L),INOX))            ! :999
WQBFCOD(L) = SMJAQH2S(L) - SMSS(L)*WQV(L,KSZ(L),ICOD)            ! :1000
```

<a id="cv-e-body-18-64"></a>전체 diagenesis의 SOD는 Brent 근 찾기의 해이다. (`Eutrophication/mod_diagen.f90:967` — `SMSOD = ZBRENT(L, ISMERR, SMCH4S, SMK1CH4, SMO2JC,                                &`; EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) 코드 전달계수는 RSMSS=SMSOD1/(XSMO20+1E-18)이다. (`Eutrophication/mod_diagen.f90:1175` — `RSMSS = SMSOD1 / (XSMO20(L)+ 1.E-18)`; EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) XSMO20에는 저층 DO의 3.0 하한을 적용한다. (`Eutrophication/mod_diagen.f90:828` — `XSMO20(L) = max( WQV(L,KSZ(L),IDOX), 3.0 )`; EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) Theory PDF 234쪽도 SOD를 추정한 뒤 NH4·NO3·S2−/CH4를 풀고 Brent 방법으로 반복하도록 설명한다. (`Eutrophication/mod_diagen.f90:967` — `SMSOD = ZBRENT(L, ISMERR, SMCH4S, SMK1CH4, SMO2JC,                                &`; EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) 판정·근거: [정본 §5 행 L272, L273, L274, L275, L278, L286, L287, L290, L305, L306, L614, L649, L650](efdc_sediment_diagenesis.md#cv-e-wq-750). [10-12 결론 검증 보완]


WQBFNH4는 암모늄태 질소의 플럭스이다. (`Eutrophication/mod_diagen.f90:996` — `WQBFNH4(L)  = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))   ! *** Ammonium flux  (g NH4/m2/day)`) 이 플럭스의 단위는 g N/m²/day이다. (`Eutrophication/mod_diagen.f90:996` — `WQBFNH4(L)  = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))   ! *** Ammonium flux  (g NH4/m2/day)`) NH4 화합물 전체 질량 g NH4로 해석하지 않는다. (`Eutrophication/mod_diagen.f90:996` — `WQBFNH4(L)  = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))   ! *** Ammonium flux  (g NH4/m2/day)`) 결론: 문서 오기. EFDC+ 12.5의 WQBFNH4는 암모늄태 질소의 g N/m²/day 플럭스이다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p181-198.md:17`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p199-216.md:14`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:996` — `WQBFNH4(L)  = SMSS(L) * (SMFD1NH4*SM1NH4(L) - WQV(L,KSZ(L),INHX))   ! *** Ammonium flux  (g NH4/m2/day)`; [EFDC-theory-wq-vs-code §5 행 L653](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:846))

kernel 순차해(SEDFLUXNEW): NH4→NO3(layer1 source = nitrification 산물 `RJNITSM`:1192, 양층 denitrif)→H2S/CH4(:1179-1231), 2×2 판별식 solver(:1131).

결론: 문서 오기. EFDC+ 12.5는 퇴적층 하층 탈질 반응속도를 제곱하지 않고 온도계수만 곱한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:23`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:945` — `RK2NO3SM = SMK2NO3(IZ)*SMTDNO3(ISMT(L))`; [EFDC-theory-wq-vs-code §5 행 L283](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:751))

결론: 문서 누락. EFDC+ 12.5는 황화물·메탄 경로의 환원성 탄소 공급을 비음수로 제한한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:25`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:26`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:958` — `B1H2SSM  = 0.0`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:951` — `SMO2JC = SMO2C*SMDGFC(L)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1202` — `SMJ2H2S = max(SMO2JC - SMO2NO3*RJDENSM, 0.0)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1208` — `B22H2S = B2H2SSM + SMJ2H2S`; [EFDC-theory-wq-vs-code §5 행 L289, L294](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:752))

결론: 문서 누락. EFDC+ 12.5는 메탄 포화농도 관련 계수에서 1/1.024를 0.97656으로 근사한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:27`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:492` — `SMTD1CH4(IT) = 0.97656**TT20 * 20.0`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:962` — `SMCH4S  = (10.0 + HP(L) + SMHSED(IZ)) * SMTD1CH4(ISMT(L)) * SMKL12(L)`; [EFDC-theory-wq-vs-code §5 행 L298](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:753))

결론: 문서 누락. EFDC+ 12.5는 SOD의 Brent 해법에 코드에서 지정한 반복 한도와 허용오차를 사용한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:30`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1286` — `parameter (IZMAX = 100,EPS = 3.0E-8,TOL = 1.0E-5,RMIN = 1.0E-4,RMAX = 100.0)`; [EFDC-theory-wq-vs-code §5 행 L616](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:830))


## 3. 병렬 flux (요약)
- 코드는 메탄 분기에서 `if( SMTT2 < 80.0 )then`일 때 계산한 sech 항을 수체 방향 용존 메탄 플럭스에 곱한다. (`Eutrophication/mod_diagen.f90:1221` — `SMSECH = 2.0 / (SMTT3 + 1.0/SMTT3)`; `Eutrophication/mod_diagen.f90:1225` — `AQJCH4SM = CSODMSM*SMSECH`) (`Eutrophication/mod_diagen.f90:1219` — `if( SMTT2 < 80.0 )then`) [10-12 전수 검증 보완] 메탄 산화에 의한 탄소성 SOD는 CSODMSM에서 용존 메탄 플럭스를 뺀 값이다. (`Eutrophication/mod_diagen.f90:1226` — `CSODSM = CSODMSM - AQJCH4SM`) 기체 메탄 플럭스는 공급 플럭스에서 CSODMSM을 뺀 값이다. (`Eutrophication/mod_diagen.f90:1227` — `GJCH4SM = SMJ2H2S - CSODMSM`) 코드는 `if( SAL(L,KSZ(L)) > SMCSHSCH )then`에서 황화물 경로를 선택하고 그 ELSE에서 메탄 경로를 선택한다. (`Eutrophication/mod_diagen.f90:1221` — `SMSECH = 2.0 / (SMTT3 + 1.0/SMTT3)`; `Eutrophication/mod_diagen.f90:1225` — `AQJCH4SM = CSODMSM*SMSECH`; `Eutrophication/mod_diagen.f90:1226` — `CSODSM = CSODMSM - AQJCH4SM`; `Eutrophication/mod_diagen.f90:1227` — `GJCH4SM = SMJ2H2S - CSODMSM`) (`Eutrophication/mod_diagen.f90:1203` — `if( SAL(L,KSZ(L)) > SMCSHSCH )then`) [10-12 전수 검증 보완] `if( SMTT2 < 80.0 )then`의 ELSE는 `SMSECH = 0.0`을 대입한다. (`Eutrophication/mod_diagen.f90:1223` — `SMSECH = 0.0`) [10-12 전수 검증 보완] <a id="cv-e-wq-845"></a>결론: 문서 오기. EFDC+ 12.5의 메탄 sech 항은 수주로 나가는 용존 메탄 플럭스에 적용된다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:25`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1221` — `SMSECH = 2.0 / (SMTT3 + 1.0/SMTT3)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1225` — `AQJCH4SM = CSODMSM*SMSECH`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1226` — `CSODSM = CSODMSM - AQJCH4SM`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1227` — `GJCH4SM = SMJ2H2S - CSODMSM`; [EFDC-theory-wq-vs-code §5 행 L652](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:845)) [10-12 결론 검증 정정]
- **인산 DO의존 sorption power-law**(:1009 `SMP1PO4=SMP2PO4·SMDP1PO4**(O2/SMCO2PO4)`, O2<임계 시 호기층 P trapping) + 2-layer 해 → `WQBFPO4D`(:1025). silica 동형(:1042).

결론: 문서 누락. EFDC+ 12.5는 지정 개방경계 셀에서 퇴적층 교환 계수를 0으로 설정한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p217-234.md:20`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:893` — `do L1 = 1,NBCSOP`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:895` — `SMKL12(L) = 0.0`; [EFDC-theory-wq-vs-code §5 행 L615](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:829))


## 4. 주요 findings
- 본문 대조: [정본](efdc_sediment_diagenesis.md#cv-e-body-18-64). 판정·근거: [정본 §5 행 L272, L273, L274, L275, L278, L286, L287, L290, L305, L306, L614, L649, L650](efdc_sediment_diagenesis.md#cv-e-wq-750). [10-12 결론 검증 보완]
- 코드 SEDFLUXNEW는 NH4, NO3, H2S/CH4의 순서로 계산한다. (`Eutrophication/mod_diagen.f90:1183` — `call SOLVSMBE(RSM1NH4,RSM2NH4,A11NH4,A22NH4SM,A1NH4SM,A2NH4SM,B11NH4,B22NH4)`; `Eutrophication/mod_diagen.f90:1193` — `call SOLVSMBE(RSM1NO3,RSM2NO3,A11NO3,A22NO3SM,A1NO3SM,A2NO3SM,B11NO3,B22NO3)`; `Eutrophication/mod_diagen.f90:1210` — `call SOLVSMBE(RSM1H2S,RSM2H2S,A11H2S,A22H2SSM,A1H2SSM,A2H2SSM,B11H2S,B22H2S)`; EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) Theory PDF 234쪽의 SOD 반복 절차도 해당 물질을 계산한 뒤 SOD를 갱신한다. (EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) 원래 CE-QUAL-ICM의 소스 해법은 확인하지 않음. (`Eutrophication/mod_diagen.f90:1183` — `call SOLVSMBE(RSM1NH4,RSM2NH4,A11NH4,A22NH4SM,A1NH4SM,A2NH4SM,B11NH4,B22NH4)`; `Eutrophication/mod_diagen.f90:1193` — `call SOLVSMBE(RSM1NO3,RSM2NO3,A11NO3,A22NO3SM,A1NO3SM,A2NO3SM,B11NO3,B22NO3)`; `Eutrophication/mod_diagen.f90:1210` — `call SOLVSMBE(RSM1H2S,RSM2H2S,A11H2S,A22H2SSM,A1H2SSM,A2H2SSM,B11H2S,B22H2S)`; EFDC_Theory_Document_Ver_12.pdf, PDF 234쪽·인쇄 221쪽) 결론: 코드 대조 대상 아님. EFDC의 물질별 호출 순서는 확인했다. CE-QUAL-ICM과의 차이 주장은 출전이 없는 H이다. (근거: `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1183` — `call SOLVSMBE(RSM1NH4,RSM2NH4,A11NH4,A22NH4SM,A1NH4SM,A2NH4SM,B11NH4,B22NH4)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1193` — `call SOLVSMBE(RSM1NO3,RSM2NO3,A11NO3,A22NO3SM,A1NO3SM,A2NO3SM,B11NO3,B22NO3)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Eutrophication/mod_diagen.f90:1210` — `call SOLVSMBE(RSM1H2S,RSM2H2S,A11H2S,A22H2SSM,A1H2SSM,A2H2SSM,B11H2S,B22H2S)`; [EFDC-theory-wq-vs-code §5 행 L651](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:844))
- **P sorption power-law**(step 아님, 연속 지수 ramp) — 단순설명의 binary on/off 와 대조.
- **퇴적물 온도 = 확산/relaxation 상태**(:744 `SMT=(SMT+SM1DIFT·TEM)·SM2DIFT`, 저수온 lag), 범위밖 시 `ERROR.LOG`+clamp(정지 아님).
- 코드는 메탄 분기에서 `if( SMTT2 < 80.0 )then`일 때 계산한 sech 항을 수체 방향 용존 메탄 플럭스에 곱한다. (`Eutrophication/mod_diagen.f90:1221` — `SMSECH = 2.0 / (SMTT3 + 1.0/SMTT3)`; `Eutrophication/mod_diagen.f90:1225` — `AQJCH4SM = CSODMSM*SMSECH`) (`Eutrophication/mod_diagen.f90:1219` — `if( SMTT2 < 80.0 )then`) [10-12 전수 검증 보완] 코드는 `if( SAL(L,KSZ(L)) > SMCSHSCH )then`에서 황화물 경로를 선택하고 그 ELSE에서 메탄 경로를 선택한다. (`Eutrophication/mod_diagen.f90:1221` — `SMSECH = 2.0 / (SMTT3 + 1.0/SMTT3)`; `Eutrophication/mod_diagen.f90:1225` — `AQJCH4SM = CSODMSM*SMSECH`; `Eutrophication/mod_diagen.f90:1226` — `CSODSM = CSODMSM - AQJCH4SM`; `Eutrophication/mod_diagen.f90:1227` — `GJCH4SM = SMJ2H2S - CSODMSM`) (`Eutrophication/mod_diagen.f90:1203` — `if( SAL(L,KSZ(L)) > SMCSHSCH )then`) [10-12 전수 검증 보완] `if( SMTT2 < 80.0 )then`의 ELSE는 `SMSECH = 0.0`을 대입한다. (`Eutrophication/mod_diagen.f90:1223` — `SMSECH = 0.0`) [10-12 전수 검증 보완] 판정·근거: [정본 §5 행 L652](efdc_sediment_diagenesis.md#cv-e-wq-845). [10-12 결론 검증 정정]
- **line range stale**(water_quality:21 `9-1031` → kernel :1121-1393 누락).

## 5. Primary sources
- **Cerco & Cole 1994** *Three-Dimensional Eutrophication Model of Chesapeake Bay*(CE-QUAL-ICM, USACE TR EL-94-4) — 직접 부모(water_quality:223 은 1995 저널판 인용).
- **Di Toro 2001** *Sediment Flux Modeling*(Wiley) — 2-layer 호기/혐기 물질수지·`s=SOD/[O2(0)]` 폐합·G-class·SOD root의 정본.
- **Press et al. Numerical Recipes** p.253 — Brent `ZBRENT`(소스 in-code :1259).

## 6. 관련
- [[efdc_water_quality]] — WQSKE1 수관 eutrophication(diagenesis 는 저면 flux 공급, ★:21 line range 정정 대상)
- [[efdc_rpem_vegetation]] — SM2NH4/NO3/PO4 pool 소비처(본 노트가 생산 측)
- [[efdc_sedzlj]] — POM deposition source(diagenesis 입력)
