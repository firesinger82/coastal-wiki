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
---

## Scope

How EFDC+ branches between the original sediment-transport module (`SedTran-Original` with separate cohesive `CALSED` + noncohesive `CALSND`) and the unified SEDZLJ multi-bed-layer model, what `ISTRAN(6)/ISTRAN(7)` actually gate, the formulae used (Krone-Partheniades for original cohesive, Van Rijn / Engelund-Hansen for original noncohesive, Christoffersen-Jonsson wave-current shear for SEDZLJ), and how bed-water coupling enters CALTRAN. Use this when picking a model, debugging bed-elevation drift, or interpreting active-layer dynamics.

## Source basis

- `mod_scaninp.f90:381, 407` — `ISTRAN` checks for SEDZLJ enable, noncohesive/bedload setup.
- `varalloc.f90:843-1156` — array allocation per branch.
- `SedTran-Original/ssedtox.f90:868-1287` — runtime dispatch.
- `SedTran-Original/calsed.f90` — cohesive Krone-Partheniades.
- `SedTran-Original/calsnd.f90`, `bedload.f90`, `fsbdld.f90`, `csndzeq.f90`, `csndeqc.f90` — noncohesive.
- `SedTran-SEDZLJ/s_main.f90`, `s_sedic.f90`, `s_sedzlj.f90`, `s_shear.f90` — SEDZLJ.
- `Transport/calconc.f90:188-517` — coupling to water-column transport.
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
| `ISTRAN(6) >= 1 .and. LSEDZLJ` | Calls `SEDZLJ_MAIN`, bypasses Original bed/water logic | `SedTran-Original/ssedtox.f90:868-872` |
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
| `2` | Engelund-Hansen | `:166-200` |

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
- ISBDLD(NS) dispatch: `bedload.f90:118-163`(van Rijn) / `:166-200`(Engelund-Hansen). FSBDLD = Φ 만; 수송률·방향·slope 보정은 `bedload.f90`.

Suspended-load:
- `CSNDZEQ` Van Rijn Part II citation + formula (`:46-61`).
- `CSNDEQC` Van Rijn Part II concentration formula (`:72-88`).

### D.1 Noncohesive 외부함수 3종 detail (verified 2026-06-03) ★

`calsnd.f90`(부유) + `bedload.f90` 가 호출하는 3 external function (모두 `SedTran-Original/`, EFDC+ DSI 2021-24). `ISNDEQ(NS)` = reference-concentration option, `ISBDLD/ISNDM1/2` = mode. 호출 (calsnd.f90:426/446/455):
```fortran
FACSUSL = FSEDMODE(WSETA, USTAR, USTARSND, RSNDM(NX), ISNDM1(NX), ISNDM2(NX), 2)
ZEQ     = CSNDZEQ(ISNDEQ(NS), DIASED, GPDIASED, TAUR, TAUBSND, SEDDIA50, HP, SSG, WSETA)
SNDEQB  = CSNDEQC(ISNDEQ(NS), DIASED, SSG, WSETA, TAUR, TAUBSND, SEDDIA50, SIGP, ZEQ, VDRBED, ISNDAL)
```

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
| `3` | **van Rijn 1984 Part II** | `c = 0.015·(d/3D_max)·T^{1.5}/Re^{0.3}`, T=τ_b/τ_rs−1, ×1e6·SSG |
| `4` | Hamrick Sedflume (no crit) | `c = 4e-9·(Re^{1.333}·U*/W_s − 1)^5/(1+e)·SSG·1e6` |
| `5` | Hamrick Sedflume (with crit) | IOPT4 + `TMPVAL>1` gate (임계 이하 0) |

- **τ_rs** (IOPT3 critical, csndzeq·csndeqc 공통): `Re≤10 → (4W_s/Re)²` / `Re>10 → 0.16·W_s²`. **2021-06 0.016→0.16 정정** (0.16=0.4², van Rijn 1984). ★ 수정 이력.
- `Re = 1e4·d·(9.8(SSG−1))^{0.333}` (van Rijn grain Reynolds), `SIGPHI`=φ 표준편차, `SNDDMX`=D90/Dmax, `VDR`=void ratio.
- bad option → `STOPP`.

→ Original noncohesive 의 **van Rijn(IOPT3)·Garcia-Parker(1)·Smith-McLean(2)·Hamrick Sedflume(4/5)** 4계열. SEDZLJ([[efdc_sedzlj]])는 이 reference-concentration 대신 Sedflume erosion rate 직접 사용 — 두 모델의 noncohesive 부유 기원 차이.

## E. Bed update per timestep

`CALCONC` calls `SSEDTOX` when sediment is active and sediment time has accumulated:
- 2TL: `Transport/calconc.f90:491-504`.
- 3TL: `:506-517`.

Inside `SSEDTOX` (Original):
- `CALBLAY` (bed-layer accounting) after bed/water exchange if `KB > 1` (`SedTran-Original/ssedtox.f90:1117-1128`).
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

- Water-column open-BC concentrations reset after CALTRAN (`Transport/calconc.f90:250-255`).
- Original cohesive hard-bottom cells skip bed exchange (`SedTran-Original/calsed.f90:320-323`).
- Original noncohesive skips hard-bottom in erosion/deposition loops (`SedTran-Original/calsnd.f90:361, 371`).
- Bedload boundary fluxes explicitly zeroed for outflow / recirculation BCs (`SedTran-Original/bedload.f90:35-45`).
- Original noncohesive moves bedload entering hard-bottom into suspended load (`calsnd.f90:767-809`).
- SEDZLJ hard-bottom / shallow cells bypass bed processes but still receive settling from above (`s_main.f90:121-132`); SEDZLJ bedload boundary at `:157-176`.

## H. Coupling to CALTRAN

Sediment classes registered as active water-column constituents:
- Cohesive `SED` pointers added when `ISTRAN(6) > 0` (`varinit.f90:319-328`).
- Noncohesive `SND` pointers added when `ISTRAN(7) > 0` (`:331-340`).

CALTRAN transports every active constituent through `WCV` (`Transport/calconc.f90:188-193`); anti-diffusion at `:213-219`.

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
- `D50` per size class drives both critical shear and settling — populate carefully.
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
