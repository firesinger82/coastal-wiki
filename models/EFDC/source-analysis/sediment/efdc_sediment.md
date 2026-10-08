---
title: "efdc sediment"
topic: sediment-transport
canonical_source: self
citation_status: verified
verification_method: "EFDC source code 직접 분석 (models/EFDC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/efdc_sediment.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
last_source_check: 2026-10-08 (recovery 재판독 대조)
---

## Scope

How EFDC+ branches between the original sediment-transport module (`SedTran-Original` with separate cohesive `CALSED` + noncohesive `CALSND`) and the unified SEDZLJ multi-bed-layer model, what `ISTRAN(6)/ISTRAN(7)` actually gate, the formulae used (Krone-Partheniades for original cohesive, Van Rijn / Engelund-Hansen for original noncohesive, Christoffersen-Jonsson wave-current shear for SEDZLJ), and how bed-water coupling enters CALTRAN. Use this when picking a model, debugging bed-elevation drift, or interpreting active-layer dynamics.

## Source basis

- `mod_scaninp.f90:381, 407` — `ISTRAN` checks for SEDZLJ enable, noncohesive/bedload setup.
- `varalloc.f90:843-1156` — array allocation per branch.
- `SedTran-Original/ssedtox.f90:863-1278` — runtime dispatch.
- `SedTran-Original/calsed.f90` — cohesive Krone-Partheniades.
- `SedTran-Original/calsnd.f90`, `bedload.f90`, `fsbdld.f90`, `csndzeq.f90`, `csndeqc.f90` — noncohesive.
- `SedTran-SEDZLJ/s_main.f90`, `s_sedic.f90`, `s_sedzlj.f90`, `s_shear.f90` — SEDZLJ.
- `Transport/calconc.f90:191-534` — coupling to water-column transport.
- `varinit.f90:319-340` — `SED/SND` constituent registration.

## A. ISTRAN flag dispatch

`ISTRAN(6)` = cohesive, `ISTRAN(7)` = noncohesive.

Setup phase:
- `mod_scaninp.f90:381` — checks cohesive before enabling `LSEDZLJ`.
- `:407` — checks noncohesive/bedload setup.
- `varalloc.f90:843` — cohesive arrays allocated.
- `:865` — noncohesive arrays allocated.
- `:909` — shared bed arrays allocated when either flag is active.

Runtime dispatch in `SSEDTOX`:

| Condition | Behavior | File:Line |
|---|---|---|
| `ISTRAN(6) >= 1 .and. LSEDZLJ` | Calls `SEDZLJ_MAIN`, bypasses Original bed/water logic | `SedTran-Original/ssedtox.f90:863-867` |
| `ISTRAN(6) >= 1 .and. !LSEDZLJ` | Original cohesive `CALSED` | `:872-874` |
| `ISTRAN(7) >= 1 .and. !LSEDZLJ` | Original noncohesive `CALSND` | `:878-880` |

**Important**: SEDZLJ disables `ISTRAN(7)` in setup because SEDZLJ unifies cohesive+noncohesive in its size-class model (`SedTran-SEDZLJ/s_sedic.f90:353-355`).

## B. SEDZLJ active-layer / multi-bed model

> 본 §는 dispatch + 핵심 변수 overview. **SEDZLJ_MAIN/SEDZLJ/SEDZLJ_SHEAR/SEDZLJ_SLOPE/BEDLOADJ 의 sub-routine deep coverage 는 [[efdc_sedzlj]]** (Christoffersen-Jonsson 1985 wave-current, Gessler 1965 / Krone deposition probability, Sedflume erosion rate, Van Rijn 1981 bedload, Lick 2009 slope correction).

SEDZLJ-specific arrays allocated under `if( LSEDZLJ )`: `BULKDENS, D50, LAYERACTIVE, PERSED, TAU, TAUCOR, TSED, TSED0, ...` (`varalloc.f90:1119-1156`).

Core / layer input arrays in `SEDIC`: `ERATE, PNEW, TAUTEMP, TSED0S, ...` (`SedTran-SEDZLJ/s_sedic.f90:226-236`).

Initial layer flags / masses:
- `LAYERACTIVE = 2` marks original in-place sediment layers; `0` absent (`s_sedic.f90:358-368`).
- `KBT` set to first layer with mass, top-down (`:392-404`).

Runtime active-layer mechanics in `s_sedzlj.f90`:
1. Find next lower layer from `LAYERACTIVE` (`:213-225`).
2. Compute surface layer, `D50AVG`, critical shear, active-layer mass `TACT` (`:227-277`).
3. Create / maintain active layer if unerodible fractions exist (`:279-289`).
4. Redistribute mass between active / deposition / parent layers (`:300-340`).
5. Final layer collapse / reindexing — update `KBT, HBED, SEDB, SEDBT` (`:747-827`).

This is the multi-layer cohesive-noncohesive bed model that distinguishes SEDZLJ from the Original module's lumped-bed treatment.

## C. Original cohesive (Krone-Partheniades)

`SedTran-Original/calsed.f90:12-16` documents itself as "standard EFDC cohesive sediment transport" (i.e., not SEDZLJ).

**Erosion** (Partheniades-style):
- Activates if `TAUBSED > TAURS` (`:333-337`).
- Excess shear normalized: `TAUE = (TAUBSED − TMPSTR*TAURS) / TAURTMP` (`:338-353`).
- Erosion rate: `WESE = TMPSEDHID*WESE*(TAUE^TEXP)` or spatial exponent `TEXPS` (`:360-367`).

**Deposition** (Krone):
- Cohesive grain stress probability: `PROBDEP = (TAUDSS − TAUBSED) / TAUDSS` (`:382-384`).
- Total bed stress probability: `PROBDEP = (TAUDSS − TAUBHYDRO) / TAUDSS` (`:385-387`).
- Combined: `WSETMP = PROBDEP*WSETA`; `SEDF(L,0,NS) = -WSETMP*SED(...) + WESE` (`:414-423`).

Alternative "Partheniades probability of deposition" via `FPROBDEP` (`:388-400`); function formula at `fprobdep.f90:37-50`.

## D. Original noncohesive (Van Rijn / Engelund-Hansen)

Bedload option dispatch in `bedload.f90`:

| `ISBDLD(NS)` | Formula | File:Line |
|---|---|---|
| `1` | Van Rijn 1984 | `:118-163` |
| `2` | 코드·문서 대조 | ISBDLD=2는 θ^SBDLDA를 계산한다. (`SedTran-Original/bedload.f90:192` — `BDLDTMPA = (SBDLDG1(NX)*SHIELDS)**SBDLDA(NX)`; EFDC_Theory_Document_Ver_12.pdf, PDF 94쪽·인쇄 81쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 95쪽·인쇄 82쪽) 식 6.29의 θ^2.1·(sqrt θ)^β와 맞추려면 SBDLDA=2.1+β/2라는 입력 조건이 필요하다. (`SedTran-Original/bedload.f90:192` — `BDLDTMPA = (SBDLDG1(NX)*SHIELDS)**SBDLDA(NX)`; EFDC_Theory_Document_Ver_12.pdf, PDF 94쪽·인쇄 81쪽, 식 6.29) SBDLDB는 이 분기에서 쓰지 않는다. (`SedTran-Original/bedload.f90:192` — `BDLDTMPA = (SBDLDG1(NX)*SHIELDS)**SBDLDA(NX)`; EFDC_Theory_Document_Ver_12.pdf, PDF 94쪽·인쇄 81쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 95쪽·인쇄 82쪽) |

### D.0 `FSBDLD` — 무차원 bedload 수송계수 Φ 4 옵션 (verified 2026-06-03) ★

`fsbdld.f90`(54): bedload 수송률 `Q_b ∝ Φ·√(g'·d³)` 의 **무차원 계수 Φ** 산출. `ISBDLD(NS)`(=ISOPT) 선택:

| ISOPT | 출처 | Φ 식 |
|---|---|---|
| `0` | user 상수 | `Φ = SBDLDP` (입력값) |
| `1` | **van Rijn 1984 Part I** (Bed Load, JHE 110:1431) | `RD = (1/(d·√(g'd)·1e6))^0.2`; `Φ = 0.053·RD/θ_cr^{2.1}` (θ_cr=CSHIELDS critical Shields) |
| `2` | modified Engelund-Hansen | `Φ = 2.0367·(DEP/D50)^{0.333}·(PEXP/PHID)^{1.125}` |
| `3` | **Wu, Wang & Jia 2000** (J Hydr Res 38) | `Φ = 0.0053/(0.03·(PHID/PEXP)^{0.6})^{2.2}` |

- **PEXP/PHID** = hiding-exposure probability(노출/은폐) — multi-class 상호작용. ISOPT 2/3 은 `(PEXP/PHID)` 비로 mixture 보정(coarse 노출↑·fine 은폐↑). ISOPT1 은 단일 D50 의 critical-Shields 의존.
- `g'd = GPDIASED` = (s−1)g·d (수중 중력 가속), `θ_cr` = [[efdc_sedzlj]] §3 Shields와 동일 critical.
- ISBLFUC=2의 y 면 평균 줄은 남측 UCELLCTR를 사용한다. (`SedTran-Original/bedload.f90:367` — `QSBDLDY(L,NX) = 0.5*SVB(L)*(QSBDLDP(L)*VCELLCTR(L) + QSBDLDP(LS)*UCELLCTR(LS))`; EFDC_Theory_Document_Ver_12.pdf, PDF 94쪽·인쇄 81쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 95쪽·인쇄 82쪽) 이 성분 혼합은 원문 확인 사실이다. (`SedTran-Original/bedload.f90:367` — `QSBDLDY(L,NX) = 0.5*SVB(L)*(QSBDLDP(L)*VCELLCTR(L) + QSBDLDP(LS)*UCELLCTR(LS))`; EFDC_Theory_Document_Ver_12.pdf, PDF 94쪽·인쇄 81쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 95쪽·인쇄 82쪽) 해석: y 벡터 평균의 오기 가능성을 제기할 수 있다(정적 판독, 실행 미확인). (`SedTran-Original/bedload.f90:367` — `QSBDLDY(L,NX) = 0.5*SVB(L)*(QSBDLDP(L)*VCELLCTR(L) + QSBDLDP(LS)*UCELLCTR(LS))`; EFDC_Theory_Document_Ver_12.pdf, PDF 94쪽·인쇄 81쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 95쪽·인쇄 82쪽)

Suspended-load:
- `CSNDZEQ` Van Rijn Part II citation + formula (`:46-61`).
- 코드는 기준높이를 최하층 두께의 0.5 이하로 제한한다. (`SedTran-Original/calsnd.f90:448` — `ZEQMAX   = 0.5*DZC(L,KSZ(L))`; `SedTran-Original/calsnd.f90:449` — `ZEQ(L)   = min(ZEQ(L),ZEQMAX)`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) 문서 식 6.54의 M개 층 평균을 찾지 못했다. (EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽, 식 6.54) van Rijn 농도의 임계응력은 TAURS이다. (`SedTran-Original/csndeqc.f90:80` — `if( REY <= 10. ) TAURS = (4.*WS/REY)**2`; `SedTran-Original/csndeqc.f90:81` — `if( REY  > 10. ) TAURS = 0.16*WS*WS                      ! *** Corrected 2021-06 from 0.016.  0.16 = 0.4^2 from VanRijn 1984`; `SedTran-Original/csndeqc.f90:83` — `VAL = (TAUB/TAURS)-1.`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) 농도식의 기준높이는 3·SNDDMX이다. (`SedTran-Original/csndeqc.f90:86` — `RATIO = SNDDIA/(3.*SNDDMX)`; `SedTran-Original/csndzeq.f90:59` — `ZEQ1 = 0.5*VAL1*(DEP**0.7)*(SNDDMX**0.3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) CSNDZEQ의 수심 의존 기준높이와 같은 값으로 고정하지 않는다. (`SedTran-Original/csndeqc.f90:86` — `RATIO = SNDDIA/(3.*SNDDMX)`; `SedTran-Original/csndzeq.f90:59` — `ZEQ1 = 0.5*VAL1*(DEP**0.7)*(SNDDMX**0.3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽)

### D.1 Noncohesive 외부함수 3종 detail (verified 2026-06-03) ★

`calsnd.f90`(부유) + `bedload.f90` 가 호출하는 3 external function (모두 `SedTran-Original/`, EFDC+ DSI 2021-24). `ISNDEQ(NS)` = reference-concentration option, `ISBDLD/ISNDM1/2` = mode. 호출 (calsnd.f90:426/446/455):
```fortran
FACSUSL = FSEDMODE(WSETA, USTAR, USTARSND, RSNDM(NX), ISNDM1(NX), ISNDM2(NX), 2)
ZEQ     = CSNDZEQ(ISNDEQ(NS), DIASED, GPDIASED, TAUR, TAUBSND, SEDDIA50, HP, SSG, WSETA)
SNDEQB  = CSNDEQC(ISNDEQ(NS), DIASED, SSG, WSETA, TAUR, TAUBSND, SEDDIA50, SIGP, ZEQ, VDRBED, ISNDAL)
```

현재 calsnd는 TAUR를 전단 응력 인수로 평형 농도 계산에 전달한다. (`SedTran-Original/calsnd.f90:455` — `SNDEQB(L) = CSNDEQC(ISNDEQ(NS),DIASED,SSG(NS),WSETA(L,0,NS),TAUR(NS),TAUBSND(L),SEDDIA50(L,KBT(L)),SIGP,ZEQ(L),VDRBED(L,KBT(L)),ISNDAL)      !`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:46` — `\* TAUR: CRITICAL STRESS IN (m/s)\*\*2`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:48` — `\*            NOTE: IF TAUR < 0, THEN TAUR AND TAUN ARE INTERNALLY`; EFDC_Manual.pdf, PDF 45쪽·인쇄 41쪽) R8.5.0 PDF는 TAUR를 평형 농도로 설명한다. (`SedTran-Original/calsnd.f90:455` — `SNDEQB(L) = CSNDEQC(ISNDEQ(NS),DIASED,SSG(NS),WSETA(L,0,NS),TAUR(NS),TAUBSND(L),SEDDIA50(L,KBT(L)),SIGP,ZEQ(L),VDRBED(L,KBT(L)),ISNDAL)      !`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:46` — `\* TAUR: CRITICAL STRESS IN (m/s)\*\*2`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:48` — `\*            NOTE: IF TAUR < 0, THEN TAUR AND TAUN ARE INTERNALLY`; EFDC_Manual.pdf, PDF 45쪽·인쇄 41쪽) PDF의 TAUR 의미와 단위가 현재 코드와 다르다. (`SedTran-Original/calsnd.f90:455` — `SNDEQB(L) = CSNDEQC(ISNDEQ(NS),DIASED,SSG(NS),WSETA(L,0,NS),TAUR(NS),TAUBSND(L),SEDDIA50(L,KBT(L)),SIGP,ZEQ(L),VDRBED(L,KBT(L)),ISNDAL)      !`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:46` — `\* TAUR: CRITICAL STRESS IN (m/s)\*\*2`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:48` — `\*            NOTE: IF TAUR < 0, THEN TAUR AND TAUN ARE INTERNALLY`; EFDC_Manual.pdf, PDF 45쪽·인쇄 41쪽) 현재 calsnd와 bedload는 TCSHIELDS를 사용한다. (`SedTran-Original/calsnd.f90:460` — `CSHIELDS = TCSHIELDS(NS)`; `SedTran-Original/bedload.f90:84` — `CSHIELDS = TCSHIELDS(NS)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:54` — `\* TCSHIELDS: CRITICAL SHIELDS STRESS (DIMENSIONLESS)`; EFDC_Manual.pdf, PDF 45쪽·인쇄 41쪽) 현재 calsnd는 ISLTAUC의 1·2·3 분기를 검사한다. (`SedTran-Original/calsnd.f90:459` — `if( ISLTAUC(NS) == 1 )then`; `SedTran-Original/calsnd.f90:468` — `if( ISLTAUC(NS) == 2 )then`; `SedTran-Original/calsnd.f90:477` — `if( ISLTAUC(NS) == 3 )then`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:56` — `\* ISLTAUC: 1 TO IMPLEMENT SUSP LOAD ONLY WHEN STRESS EXCEEDS TAUC FOR EACH GRAINSIZE`; EFDC_Manual.pdf, PDF 45쪽·인쇄 41쪽) PDF는 두 변수를 미사용으로 적는다. (`SedTran-Original/calsnd.f90:455` — `SNDEQB(L) = CSNDEQC(ISNDEQ(NS),DIASED,SSG(NS),WSETA(L,0,NS),TAUR(NS),TAUBSND(L),SEDDIA50(L,KBT(L)),SIGP,ZEQ(L),VDRBED(L,KBT(L)),ISNDAL)      !`; `SedTran-Original/calsnd.f90:459` — `if( ISLTAUC(NS) == 1 )then`; `SedTran-Original/calsnd.f90:460` — `CSHIELDS = TCSHIELDS(NS)`; `SedTran-Original/calsnd.f90:468` — `if( ISLTAUC(NS) == 2 )then`; `SedTran-Original/calsnd.f90:477` — `if( ISLTAUC(NS) == 3 )then`; `SedTran-Original/bedload.f90:84` — `CSHIELDS = TCSHIELDS(NS)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:46` — `\* TAUR: CRITICAL STRESS IN (m/s)\*\*2`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:48` — `\*            NOTE: IF TAUR < 0, THEN TAUR AND TAUN ARE INTERNALLY`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:50` — `\*            COMPUTED USING VAN RIJN'S FORMULAS`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:54` — `\* TCSHIELDS: CRITICAL SHIELDS STRESS (DIMENSIONLESS)`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:56` — `\* ISLTAUC: 1 TO IMPLEMENT SUSP LOAD ONLY WHEN STRESS EXCEEDS TAUC FOR EACH GRAINSIZE`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:58` — `\*                 2 TO IMPLEMENT SUSP LOAD ONLY WHEN STRESS EXCEEDS TAUCD50`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:60` — `\*                 3 TO USE TAUC FOR NONUNIFORM BEDS, THESE APPLY ONLY TO RESUSPENSION`; `models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/EFDC_Cards/Card_Image_42.md:62` — `\* FORMULAS NOT EXPLICITLY CONTAINING CRITICAL SHIELDS STRESS SUCH AS G-P`; EFDC_Manual.pdf, PDF 45쪽·인쇄 41쪽)


**(1) `FSEDMODE(...,IMODE)` — bedload(IMODE=1)/suspended(IMODE=2) 분배 (무차원)** `fsedmode.f90`:
- `US = ISNDM2==0 ? USTOT : USGRN` (total vs grain shear velocity 선택), `USDWS = U*/W_s`. `WS==0 → 0`.
- `ISNDM1` 5 모드:

| ISNDM1 | bedload(IMODE=1) | suspended(IMODE=2) |
|---|---|---|
| `0` | 1.0 | 1.0 (둘 다 활성) |
| `1` | 1.0 | binary: `U*/W_s ≥ RSNDM` → 1 |
| `2` | 1.0 | linear: `(U*/W_s − 0.4)/9.6` clamp[0,1] |
| `3` | binary: `U*/W_s < RSNDM` → 1 | binary: `≥ RSNDM` → 1 |
| `4` | linear: `1 − TMPVAL` | linear: `TMPVAL=(U*/W_s−0.4)/9.6` |

→ `RSNDM` = U*/W_s 임계(이송 mode 전환). linear 식의 0.4·9.6 은 van Rijn suspension 개시(U*/W_s≈0.4)~full suspension 범위.

**(2) `CSNDZEQ(IOPT,...)` — 기준농도 reference height z_eq/H (무차원)** `csndzeq.f90`:

| IOPT | 출처 | z_eq |
|---|---|---|
| `1` | Garcia-Parker 1991 (JHE 117:414) | **0.05** (상수) |
| `2` | Smith-McLean 1977 (JGR 82:1735) | `26.3·D_max·(τ_b−τ_r)/g'd · (D/D_max)/DEP`, min 0.01 |
| `3` | **van Rijn 1984 Part II** (JHE 110:1623) | `0.5·0.11·(1−e^{−0.5T})·(25−T)·DEP^{0.7}·D_max^{0.3}/DEP`, min 0.01 (T=τ_b/τ_rs−1) |
| `4/5` | Hamrick Sedflume | **0.01** (상수) |

**(3) `CSNDEQC(IOPT,...)` — near-bed 평형 기준농도 (noncohesive)** `csndeqc.f90`:
- **공통 gate**: `U*=√τ_b`; **`U* < W_s → C=0`** (Hamrick: U*<W_s 면 bedload 만, calsnd 부유 0).

| IOPT | 출처 | 식 핵심 |
|---|---|---|
| `1` | **Garcia-Parker 1991** | `Z = D_fac·λ·Re^{0.6}·U*/W_s` (Re Eq42, λ=1−0.29σ_φ Eq51, D_fac=(d/D50)^0.2 if ISNDAL≥1), `c=1.3e-7·Z^5/(1+3.33·Z^5)` (Eq45), ×1e6·SSG |
| `2` | **Smith-McLean 1977** | `γ=2.4e-3(τ_b/τ_r−1)`, `c=0.65γ/(1+γ)`, ×1e6·SSG |
| `3` | 코드·문서 대조 | 코드는 기준높이를 최하층 두께의 0.5 이하로 제한한다. (`SedTran-Original/calsnd.f90:448` — `ZEQMAX   = 0.5*DZC(L,KSZ(L))`; `SedTran-Original/calsnd.f90:449` — `ZEQ(L)   = min(ZEQ(L),ZEQMAX)`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) 문서 식 6.54의 M개 층 평균을 찾지 못했다. (EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽, 식 6.54) van Rijn 농도의 임계응력은 TAURS이다. (`SedTran-Original/csndeqc.f90:80` — `if( REY <= 10. ) TAURS = (4.*WS/REY)**2`; `SedTran-Original/csndeqc.f90:81` — `if( REY  > 10. ) TAURS = 0.16*WS*WS                      ! *** Corrected 2021-06 from 0.016.  0.16 = 0.4^2 from VanRijn 1984`; `SedTran-Original/csndeqc.f90:83` — `VAL = (TAUB/TAURS)-1.`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) 농도식의 기준높이는 3·SNDDMX이다. (`SedTran-Original/csndeqc.f90:86` — `RATIO = SNDDIA/(3.*SNDDMX)`; `SedTran-Original/csndzeq.f90:59` — `ZEQ1 = 0.5*VAL1*(DEP**0.7)*(SNDDMX**0.3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) CSNDZEQ의 수심 의존 기준높이와 같은 값으로 고정하지 않는다. (`SedTran-Original/csndeqc.f90:86` — `RATIO = SNDDIA/(3.*SNDDMX)`; `SedTran-Original/csndzeq.f90:59` — `ZEQ1 = 0.5*VAL1*(DEP**0.7)*(SNDDMX**0.3)`; EFDC_Theory_Document_Ver_12.pdf, PDF 98쪽·인쇄 85쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 100쪽·인쇄 87쪽) |
| `4` | Hamrick Sedflume (no crit) | `c = 4e-9·(Re^{1.333}·U*/W_s − 1)^5/(1+e)·SSG·1e6` |
| `5` | Hamrick Sedflume (with crit) | IOPT4 + `TMPVAL>1` gate (임계 이하 0) |

- **τ_rs** (IOPT3 critical, csndzeq·csndeqc 공통): `Re≤10 → (4W_s/Re)²` / `Re>10 → 0.16·W_s²`. **2021-06 0.016→0.16 정정** (0.16=0.4², van Rijn 1984). ★ 수정 이력.
- `Re = 1e4·d·(9.8(SSG−1))^{0.333}` (van Rijn grain Reynolds), `SIGPHI`=φ 표준편차, `SNDDMX`=D90/Dmax, `VDR`=void ratio.
- bad option → `STOPP`.

→ Original noncohesive 의 **van Rijn(IOPT3)·Garcia-Parker(1)·Smith-McLean(2)·Hamrick Sedflume(4/5)** 4계열. SEDZLJ([[efdc_sedzlj]])는 이 reference-concentration 대신 Sedflume erosion rate 직접 사용 — 두 모델의 noncohesive 부유 기원 차이.

## E. Bed update per timestep

`CALCONC` calls `SSEDTOX` when sediment is active and sediment time has accumulated:
- 2TL: `Transport/calconc.f90:508-521`.
- 3TL: `:506-517`.

Inside `SSEDTOX` (Original):
- `CALBLAY` (bed-layer accounting) after bed/water exchange if `KB > 1` (`SedTran-Original/ssedtox.f90:1108-1119`).
- `CALBED` (physical bed properties) only when not SEDZLJ (`:1282-1287`).

SEDZLJ updates bed state inside `s_sedzlj.f90`; `SSEDTOX` bypasses Original `CALBED` (`:1282-1287`).

## F. Wave-current bottom shear

**Original path**:
- `hdmt2t.f90:409-428` — wave-current turbulence for non-SEDZLJ.
- Sets grain stress: `TAUBSED = QQ/CTURB2`, `TAUBSND = QQ/CTURB2` (`:433-438`).
- Wave-boundary-layer logic excludes SEDZLJ (`caltbxy.f90:276-321`).

**SEDZLJ path**:
- `SEDZLJ_MAIN` calls `SEDZLJ_SHEAR` (`s_main.f90:53-55`).
- `s_shear.f90:9-12` documents Christoffersen-Jonsson wave/current shear.
- Combined: `SHEAR = SHEARC + SHEARW` (`:282-310`).
- Growth-limited result stored in `TAU(L)` (`:314-322`).

The Christoffersen-Jonsson form properly accounts for nonlinear wave-current interaction in the bottom boundary layer; the Original module's simple `QQ/CTURB2` formulation is less accurate in wave-dominated environments.

## G. Deposition boundary handling

- Water-column open-BC concentrations reset after CALTRAN (`Transport/calconc.f90:262-267`).
- Original cohesive hard-bottom cells skip bed exchange (`SedTran-Original/calsed.f90:320-323`).
- Original noncohesive skips hard-bottom in erosion/deposition loops (`SedTran-Original/calsnd.f90:361, 371`).
- Bedload boundary fluxes explicitly zeroed for outflow / recirculation BCs (`SedTran-Original/bedload.f90:35-45`).
- Original noncohesive moves bedload entering hard-bottom into suspended load (`calsnd.f90:767-809`).
- SEDZLJ hard-bottom / shallow cells bypass bed processes but still receive settling from above (`s_main.f90:121-132`); SEDZLJ bedload boundary at `:157-176`.

## H. Coupling to CALTRAN

Sediment classes registered as active water-column constituents:
- Cohesive `SED` pointers added when `ISTRAN(6) > 0` (`varinit.f90:319-328`).
- Noncohesive `SND` pointers added when `ISTRAN(7) > 0` (`:331-340`).

With `ISQUICK == 1`, CALTRAN_QUICKEST transports every active constituent through `WCV`; otherwise CALTRAN does (`Transport/calconc.f90:198-203`); anti-diffusion is gated by `ISQUICK == 0` at `:228-230, 250`.

After CALTRAN + vertical diffusion, totals `SEDT/SNDT` recomputed (`:407-463`); sediment bed/water source-sink applied via `SSEDTOX` (`:490-517`).

SEDZLJ uses **same** transported `SED` arrays (incl. `NSEDS2`) in settling and bed exchange (`s_main.f90:73-80`; `s_sedzlj.f90:699-702`).

## Decision Guide

| Application | Choice |
|---|---|
| Estuarine cohesive mud + minor sand | Original `ISTRAN(6)=1, ISTRAN(7)=0`, Krone-Partheniades |
| River bedload-dominated | Original `ISTRAN(7)=1`, Van Rijn (`ISBDLD=1`) |
| Wave-dominated coast / sandy beach | SEDZLJ (`LSEDZLJ=.TRUE., ISTRAN(6)=1`); SEDZLJ disables `ISTRAN(7)` automatically |
| Multi-fraction (clay + silt + sand) bed evolution | SEDZLJ (multi-bed layers, Christoffersen-Jonsson shear) |
| Reservoir sedimentation, decadal | SEDZLJ |
| Quick screening / parametric | Original (lighter, simpler) |
| Toxics / contaminant tracking with sediment | Original cohesive + ISTRAN(5) toxics |

## Working Rules

- SEDZLJ requires `LSEDZLJ=.TRUE.` in input AND `ISTRAN(6)>=1`. Setting only one is silent failure.
- D50만으로 모든 임계응력과 침강속도를 자동 계산하는지는 확인하지 않음. (`SedTran-SEDZLJ/s_sedic.f90:88` — `read(30,*) (TCRE(K),K = 1,NSEDS)`; `SedTran-SEDZLJ/s_sedic.f90:92` — `read(30,*) (TCRSUS(K),K = 1,NSEDS)`; `SedTran-SEDZLJ/s_sedic.f90:448` — `DWS(K) = DWSIN(K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 113쪽·인쇄 100쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 114쪽·인쇄 101쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽) SEDZLJ는 TCRE·TCRSUS·DWSIN을 독립 입력으로 읽는다. (`SedTran-SEDZLJ/s_sedic.f90:88` — `read(30,*) (TCRE(K),K = 1,NSEDS)`; `SedTran-SEDZLJ/s_sedic.f90:92` — `read(30,*) (TCRSUS(K),K = 1,NSEDS)`; `SedTran-SEDZLJ/s_sedic.f90:448` — `DWS(K) = DWSIN(K)`; EFDC_Theory_Document_Ver_12.pdf, PDF 113쪽·인쇄 100쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 114쪽·인쇄 101쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽) Confluence의 자동 계산은 안내용이다. (`models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Sediment/Original_EFDC_Sediment_Model.md:42` — `Figure 4 shows the form with the *Non-Cohesives Suspended* tab. It is similar in function and operation to the *Cohesives* tab. Grain size for each non-cohesive class is required for the sediment transport computations. This value is also used as the grain size for the d**50** calculations. A number of options for computing equilibrium concentrations are available in the *Equilibrium Conc* frame. This includes the option of equilibrium concentrations calculated from Sedflume data with or without critical shear stress. Setting the settling velocity or the critical shear stress values to numbers <0 results in EFDC computing those parameters values using the Van Rijn equations (1984a, 1984b). Pressing F2 for help pops up information relevant to the current input field.`; `models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Sediment/Original_EFDC_Sediment_Model.md:42` — `Setting the settling velocity or the critical shear stress values to numbers <0 results in EFDC computing those parameters values using the Van Rijn equations (1984a, 1984b).`; EFDC_Theory_Document_Ver_12.pdf, PDF 113쪽·인쇄 100쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 114쪽·인쇄 101쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽) 기존 퇴적물의 음의 WSEDO·TAUR 입력은 SETSTVEL·SETSHLD를 호출한다. (`input.f90:2167` — `if( WSEDO(NS) < 0.0 )then`; `input.f90:2168` — `WSEDO(NS) = SETSTVEL(SEDDIA(NS),SSG(NS))`; `input.f90:2207` — `if( TAUR(NS) < 0.0 )then`; `input.f90:2208` — `call SETSHLD(TAUR(NS),TCSHIELDS(NS),SEDDIA(NS),SSG(NS),DSTR,USTR)`; EFDC_Theory_Document_Ver_12.pdf, PDF 113쪽·인쇄 100쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 114쪽·인쇄 101쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽) 두 입력 경로를 구분한다. (`input.f90:2167` — `if( WSEDO(NS) < 0.0 )then`; `input.f90:2168` — `WSEDO(NS) = SETSTVEL(SEDDIA(NS),SSG(NS))`; `input.f90:2207` — `if( TAUR(NS) < 0.0 )then`; `input.f90:2208` — `call SETSHLD(TAUR(NS),TCSHIELDS(NS),SEDDIA(NS),SSG(NS),DSTR,USTR)`; EFDC_Theory_Document_Ver_12.pdf, PDF 113쪽·인쇄 100쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 114쪽·인쇄 101쪽; EFDC_Theory_Document_Ver_12.pdf, PDF 115쪽·인쇄 102쪽)
- Original cohesive has a fixed bed model (`KB=1` is common); SEDZLJ supports many bed layers (typical 5–10).
- Wave-current shear: SEDZLJ's Christoffersen-Jonsson is the only realistic option for wave-action coastlines. Original `QQ/CTURB2` works for purely current-driven cases.
- Watch `TAU(L)` time series at validation stations — this is the bottom shear actually driving sediment (for SEDZLJ).
- Hard-bottom cells (no erodible material) need `IBEDH(L,K)=1` flagged; without that, both modules will erode through "rock."
- Bedload at outflow boundaries is auto-zeroed (`bedload.f90:35-45`); this is correct but means net export looks zero. Suspended load is what you measure.

## Common Pitfalls

- ▢ Setting `LSEDZLJ=.TRUE.` and also expecting Original cohesive parameters (TAURS etc.) to apply — they don't; SEDZLJ has its own input cards.
- ▢ Reading `ISTRAN(7)` setting in output for SEDZLJ — it gets disabled; check `LSEDZLJ` instead.
- ▢ Original module + waves without `caltbxy` wave-BBL — bottom shear underestimated by 30-50%.
- ▢ SEDZLJ run with `TAUCOR` (cohesive critical shear) too high for fine sand fractions — non-erosion (no transport at typical events).
- ▢ Forgetting `SED` constituent ramp `NTSCR6` — sediment concentrations spike at startup.
- ▢ Bed thickness `HBED` going negative — check `LAYERACTIVE` consistency; may need full restart.
- ▢ Mass conservation across bed/water interface looks off — verify `SEDF` sign convention (positive = bed→water in this code).

## Next expansion

- SEDZLJ multi-fraction calibration recipe (D50, TAUCOR, ERATE).
- Compare Original cohesive vs SEDZLJ on identical estuary case.
- Coupling sediment to wave model (active wave field via CALTBXY).

## References

- Krone 1962; Partheniades 1965 (cohesive erosion/deposition).
- Van Rijn 1984 Parts I-III; Engelund & Hansen 1967.
- Christoffersen & Jonsson 1985 (wave-current BBL).
- James et al. 2010 (SEDZLJ).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/efdc/source_code/EFDCPlus_Stable/EFDC`. Auto-draft = false; review_required = true.
