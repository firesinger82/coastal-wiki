---
title: "연안표사 수치모델 — one-line/N-line shoreline 모델 + process-based(파→radiation stress→longshore current→sediment flux): Delft3D·XBeach·EFDC·ROMS cross-link"
topic: littoral-drift
canonical_source: self
citation_status: verified
verification_method: "process-based 모델 cross-link 부분(§2-§6)은 본 위키 내 verified 모델 source-analysis 노트가 뒷받침 — Delft3D([`delft3d_sediment_transport_formulae.md`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md) eqtran iform 카탈로그·[`sediment/delft3d_sediment.md`](../../models/Delft3D/source-analysis/sediment/delft3d_sediment.md)·[`delft3d_sediment_morphology.md`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md))·XBeach([`xbeach_morphology.md`](../../models/XBeach/source-analysis/xbeach_morphology.md) transus/sedtransform file:line·[`xbeach-morphology-foundation.md`](../../models/XBeach/source-analysis/xbeach-morphology-foundation.md))·EFDC([`sediment/efdc_sediment.md`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)·[`sediment/efdc_sedzlj.md`](../../models/EFDC/source-analysis/sediment/efdc_sedzlj.md))·ROMS([`sediment/roms_sediment.md`](../../models/ROMS/source-analysis/sediment/roms_sediment.md)·[`roms_wec.md`](../../models/ROMS/source-analysis/roms_wec.md)) 노트 직접 read 후 인용. radiation stress→longshore current 인과 chain 은 [`02-theory.md`](02-theory.md)(Holthuijsen §7.4.2-3) 뒷받침. one-line/N-line 모델(§1, GENESIS·LITPACK·UNIBEST)은 본 위키 내 source-analysis 미보유 → bibliographic(source-needed)."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/littoral-drift/01-concept.md
  - concepts/littoral-drift/02-theory.md
  - models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md
  - models/XBeach/source-analysis/xbeach_morphology.md
  - models/EFDC/source-analysis/sediment/efdc_sediment.md
  - models/ROMS/source-analysis/sediment/roms_sediment.md
  - concepts/sediment-transport/04-code-and-tools.md
---

# 연안표사 수치모델 — code & tools

> [`01-concept.md`](01-concept.md)(CERC·Komar-Inman empirical formula)·[`02-theory.md`](02-theory.md)(radiation stress→longshore current 유도)의 정형을 **수치적으로 푸는 모델 계층**. 두 갈래: (1) **one-line/N-line shoreline 모델** — empirical longshore formula 를 적분해 해안선 위치를 진화시킴(빠름, 장기), (2) **process-based** — wave→radiation stress→longshore current→sediment flux 를 직접 풀어 bed 진화 산출(느림, 사건~중기). process-based 는 본 위키 검수완료 모델로 cross-link.

## 1. One-line / N-line shoreline 모델 (bibliographic)

> 본 §의 모델은 본 위키 내 source-analysis 미보유 → **citation_status: source-needed**. 식·구현 detail 은 각 모델 매뉴얼/원논문 직접 확인 필요(미실재 인용 금지).

**One-line 이론**: 해안선을 단일 contour line 으로 표현, 횡단면 형상은 평형(equilibrium profile) 으로 평행이동 가정. longshore transport gradient 가 해안선을 전·후진:

$$\frac{\partial y}{\partial t} = -\frac{1}{D_c}\frac{\partial Q_l}{\partial x}$$

- $y$ = 해안선 위치, $x$ = alongshore 좌표, $D_c$ = active profile height(berm+closure depth), $Q_l$ = longshore transport rate([`01-concept.md §3`](01-concept.md#3-cerc-formula-1984-shore-protection-manual)의 CERC/Komar 식 등으로 산출).

| 모델 | 분류 | 개발/배포 | 특징 (source-needed — 매뉴얼 확인) |
|---|---|---|---|
| **GENESIS** | one-line | US Army Corps CERC (CEDAS/NEMOS) | CERC formula 기반, 구조물(groin·breakwater·seawall)·양빈 처리. coastal engineering 표준 shoreline change |
| **LITPACK (LITLINE/LITDRIFT)** | one-line + cross-section transport | DHI (MIKE 패밀리) | LITDRIFT 가 단면 longshore current+transport 분포 산출 → LITLINE 이 해안선 진화 |
| **UNIBEST (CL+ / LT)** | one-line + longshore transport | Deltares | UNIBEST-LT(longshore transport on profile) + UNIBEST-CL+(coastline) |
| **N-line / multi-line** | 다중 contour | (GenCade 등) | cross-shore 분포까지 다중 line 으로 — one-line 과 process-based 의 중간 |

→ 본 위키는 process-based 모델만 source-analysis 보유. one-line 모델 적용·검증 case 는 향후 별도 노트(미생성). **GenCade** = GENESIS + Cascade(regional sediment budget) 결합형(매뉴얼 확인 필요).

## 2. Process-based 의 인과 chain (어디서 longshore transport 가 나오나)

[`02-theory.md §5`](02-theory.md#5-에너지--s_xy--current-의-인과-chain)의 chain 을 모델 구현 관점으로:

$$\underbrace{\text{wave model}}_{H,\theta,k}\!\to\!\underbrace{S_{xy}\ \text{or VF}}_{\text{radiation stress / vortex force}}\!\to\!\underbrace{\text{flow solver}}_{v_l\ \text{longshore current}}\!\to\!\underbrace{\tau_b(\text{wave+current})}_{\text{BBL}}\!\to\!\underbrace{\text{transport formula}}_{q_{b}+q_{s}}\!\to\!\underbrace{\text{Exner}}_{\partial z_b/\partial t}$$

- **wave 결합 방식**이 모델마다 다름: radiation stress($S_{xy}$ 구배) vs **vortex-force(VF)** 형. 후자가 현대적(ROMS WEC_VF — [`roms_wec.md §A`](../../models/ROMS/source-analysis/roms_wec.md)).
- longshore transport 는 **별도 closure 식이 아니라**, longshore current($v_l$) + wave orbital 이 만든 bed shear 가 transport formula(Soulsby·van Rijn·Bijker 등)에 들어가 산출되는 **2D 결과**. 즉 process-based 에서 "longshore transport rate" 는 alongshore 방향 transport flux 의 단면 적분.
- **bed-slope 보정**(downslope 우세)·**wave skewness/asymmetry**(onshore bias) 가 transport 방향·크기를 조정.

## 3. Delft3D — eqtran formula gateway + online morphology

bed shear → transport formula gateway **`eqtran`** 가 **iform** 코드로 식 선택([`delft3d_sediment_transport_formulae.md §2`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md)). longshore drift 관련 핵심 식:

| iform | routine | 식 |
|---|---|---|
| −1 / −2,−4 | `tram1` / `tram2` | **van Rijn 1993 / 2004**(TRANSPOR2004), reference concentration+suspended 모두 산출 |
| 5 | `tranb5` | **Bijker** (wave-current bed+suspended; littoral drift 고전 식) |
| 11 / 12 | `trab11` / `trab12` | **Soulsby & van Rijn** / **Soulsby** |
| 20 | `trab20` | **Soulsby / van Rijn — XBeach adaptations**(평형농도 equi_conc) |

(iform 카탈로그 verbatim: [`delft3d_sediment_transport_formulae.md §2`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md), `eqtran.f90:292-566`)

- bed shear 입력은 **skin friction**(Soulsby 2004 muddy bed, `compbsskin.f90`, ar=0.26·as=0.22) 이 cohesive 침식을 구동([`delft3d_sediment_transport_formulae.md §3`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md)).
- transport → **Exner bed update**: `bott3d` 가 suspended divergence + bedload divergence + 침식/퇴적으로 `BODSED` 변화 → `dps = dps − depchg`, **MORFAC** 로 형태가속([`delft3d_sediment_morphology.md §3`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md)·[`sediment/delft3d_sediment.md §F`](../../models/Delft3D/source-analysis/sediment/delft3d_sediment.md)).
- wave 결합: Delft3D-WAVE(SWAN) → radiation stress/forcing → FLOW 가 longshore current 생성. canonical 알고리즘 = Lesser et al. 2004([`delft3d_sediment_morphology.md §1`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md)).

→ littoral drift 용도: sandy coast 는 `iform=−2`(van Rijn 2004) 또는 wave-dominated 는 `tranb5`(Bijker)·`trab20`(Soulsby/van Rijn) 선택([`sediment/delft3d_sediment.md` Decision Guide](../../models/Delft3D/source-analysis/sediment/delft3d_sediment.md)).

## 4. XBeach — surf zone 전용 transport (transus → bed_update)

surf zone 단기(storm) longshore+cross-shore 해석에 특화. transport 는 **`transus`**(sedtransform), bed 진화는 **`bed_update`**([`xbeach_morphology.md`](../../models/XBeach/source-analysis/xbeach_morphology.md)).

transport formula 3종(`form` 선택, [`xbeach_morphology.md §B`](../../models/XBeach/source-analysis/xbeach_morphology.md), `morphevolution.F90:173-176`):

| form | 식 | 비고 |
|---|---|---|
| `soulsby_vanrijn` | **Soulsby & van Rijn**(평형농도 ceqb/ceqs split) | default workhorse |
| `vanthiel_vanrijn` | **van Thiel de Vries / van Rijn**(임계유속 wave-current blend) | surf zone 권장 |
| `vanrijn1993` | **van Rijn 1993**(ripple roughness·reference conc.) | |

- **stirring**: current $v_{mg}$ + short-wave orbital $u_{rms}^2$ + `Cd` 결합 → 평형농도([`xbeach_morphology.md §B`](../../models/XBeach/source-analysis/xbeach_morphology.md), `:1612-1633`). longshore current 가 stirring·advection 의 current 성분.
- **suspended/bedload split**: `Sus = sus·(cu·ureps·hu − Dc·hu·dcsdx)·wetu`, `Sub = bed·(cub·urepb·hu)·wetu`([`xbeach_morphology.md §E`](../../models/XBeach/source-analysis/xbeach_morphology.md), `:276-279`).
- **wave skewness/asymmetry**: Ruessink-van Rijn `ua = sws·(facSk·Sk − facAs·As)·urms` 가 advection velocity 에 가산 → onshore bias([`xbeach_morphology.md §G`](../../models/XBeach/source-analysis/xbeach_morphology.md), `:3032-3039`).
- **bed-slope 보정** 3축: `bdslpeffmag`(Roelvink/Soulsby), `bdslpeffini`(임계유속), `bdslpeffdir`(Talmon 방향)([`xbeach_morphology.md §F`](../../models/XBeach/source-analysis/xbeach_morphology.md)).
- **MORFAC**: transport 가 아니라 **bed change** 에 곱해짐(`dzg = morfac·dt/(1−por)·flux_div`); storm hindcast 는 morfac=1 권장([`xbeach_morphology.md §A`](../../models/XBeach/source-analysis/xbeach_morphology.md)·[`xbeach-morphology-foundation.md`](../../models/XBeach/source-analysis/xbeach-morphology-foundation.md)).

→ littoral-drift 토픽의 **1순위 surf-zone 모델**(README §경계: XBeach = 사건~연간 short-term).

## 5. EFDC — Original(CALSND) vs SEDZLJ + wave-current shear

`ISTRAN(6)`(cohesive)·`ISTRAN(7)`(noncohesive) 분기, `LSEDZLJ` 로 두 bed 모델 선택([`sediment/efdc_sediment.md §A`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)).

- **Original noncohesive**(`calsnd`/`bedload`): bedload `ISBDLD=1` **van Rijn 1984** / `=2` **Engelund-Hansen**; suspended reference conc. `CSNDZEQ`/`CSNDEQC` 로 **van Rijn Part II·Garcia-Parker·Smith-McLean·Hamrick** 4계열([`sediment/efdc_sediment.md §D`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)).
- **SEDZLJ**: multi-class·multi-bed-layer 통합. erosion 은 Sedflume rate, deposition 은 Gessler/Krone 확률, bedload 는 **van Rijn 1981**, bed-slope 는 Lick 2009([`sediment/efdc_sedzlj.md`](../../models/EFDC/source-analysis/sediment/efdc_sedzlj.md)).
- **wave-current bed shear**: SEDZLJ 는 **Christoffersen-Jonsson 1985**(`s_shear.f90`, `SHEAR=SHEARC+SHEARW`) — wave-dominated coast 에 유일한 현실적 옵션. Original 의 `QQ/CTURB2` 는 current-driven 한정([`sediment/efdc_sediment.md §F`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)).

→ littoral drift: wave-dominated sandy beach 는 **SEDZLJ**(`LSEDZLJ=.TRUE.`) 권장; Christoffersen-Jonsson wave-current shear 가 longshore transport 의 bed shear 입력([`sediment/efdc_sediment.md` Decision Guide](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)).

## 6. ROMS (CSTMS) — vortex force(WEC) + bedload

ROMS 의 longshore current 는 **WEC(Wave Effects on Currents) vortex-force** 형으로 생성([`roms_wec.md`](../../models/ROMS/source-analysis/roms_wec.md)) — radiation stress 형(Mellor) 은 이 tree 에 없음(`WEC_VF`만, `roms_wec.md §A`).

- **WEC_VF**: vortex force 가 quasi-Eulerian 운동량에 `rustr3d/rvstr3d` 로 가산([`roms_wec.md §B`](../../models/ROMS/source-analysis/roms_wec.md)); breaking dissipation(Thornton-Guza·Church-Thornton) 이 surf-zone setup·longshore current driver([`roms_wec.md §F`](../../models/ROMS/source-analysis/roms_wec.md)). Uchiyama et al. 2010 / McWilliams et al. 2004 canonical.
- **transport(CSTMS)**: bedload = **Meyer-Peter-Müller** / **Soulsby-Damgaard**(combined wave+current) / **van der A et al. 2013**(wave asymmetry crest/trough)([`sediment/roms_sediment.md §C`](../../models/ROMS/source-analysis/sediment/roms_sediment.md)). **van Rijn 미구현**(이 tree).
- suspended 는 **Partheniades 초과전단** `ero = dt·Erate·(1−por)·bed_frac·(τ/τ_ce−1)`([`sediment/roms_sediment.md §G`](../../models/ROMS/source-analysis/sediment/roms_sediment.md)); suspended sediment 는 일반 tracer 로 `step3d_t` 이송([`sediment/roms_sediment.md §F`](../../models/ROMS/source-analysis/sediment/roms_sediment.md)).
- **BBL**(SSW/MB/SG) 가 wave-current 결합 bed shear 산출([`sediment/roms_sediment.md §E`](../../models/ROMS/source-analysis/sediment/roms_sediment.md)·[`roms_wec.md §E`](../../models/ROMS/source-analysis/roms_wec.md)).

→ littoral drift: 광역 shelf↔surf zone 결합·rip current 까지 보려면 `WEC_VF + ROLLER_RENIERS + BBL_MODEL=SSW + SED_VAN_DER_A`([`roms_wec.md` Decision Guide](../../models/ROMS/source-analysis/roms_wec.md)).

## 7. 모델 비교 — longshore transport 산출 방식

| 모델 | wave→current 결합 | bed shear(wave-current) | longshore transport formula | bed 진화 | 본 위키 노트 |
|---|---|---|---|---|---|
| **GENESIS/LITPACK/UNIBEST** | (one-line, empirical $Q_l$) | — | CERC/Komar 적분 | $\partial y/\partial t$ shoreline | source-needed |
| **Delft3D** | SWAN radiation stress | Soulsby 2004 skin | van Rijn·Bijker·Soulsby(eqtran iform) | Exner(`bott3d`)+MORFAC | [§3](#3-delft3d--eqtran-formula-gateway--online-morphology) |
| **XBeach** | radiation stress(surfbeat) | wave+current stirring | Soulsby-vR·vanThiel-vR·vR1993 | `bed_update`+MORFAC | [§4](#4-xbeach--surf-zone-전용-transport-transus--bed_update) |
| **EFDC** | (wave field 입력) | Christoffersen-Jonsson(SEDZLJ) | van Rijn·Engelund-Hansen·Sedflume | active-layer(SEDZLJ)/CALBED | [§5](#5-efdc--originalcalsnd-vs-sedzlj--wave-current-shear) |
| **ROMS** | **vortex force**(WEC_VF) | BBL(SSW/MB/SG) | MPM·Soulsby-Damgaard·van der A | Exner(`step3d_t`) | [§6](#6-roms-cstms--vortex-forcewec--bedload) |

핵심: **one-line 은 $Q_l$ empirical 식을 직접 적분**, **process-based 는 $v_l$+bed shear → transport formula 의 2D 결과로 longshore transport 가 emergent**. 같은 transport 식(van Rijn·Soulsby·Bijker)을 여러 모델이 공유하나, **wave→current 결합(radiation stress vs vortex force)·bed shear closure** 가 모델 간 차이의 본질.

## 8. 인용 정형

- one-line 식 $\partial y/\partial t = -(1/D_c)\partial Q_l/\partial x$ + GENESIS/LITPACK/UNIBEST — **source-needed**(본 위키 source-analysis 미보유, 각 매뉴얼 확인 필요)
- Delft3D eqtran iform(van Rijn/Bijker/Soulsby) — [`delft3d_sediment_transport_formulae.md §2`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md)(`eqtran.f90`) **verified**
- XBeach transus/sedtransform(Soulsby-vR·vanThiel-vR·vR1993) + skewness `ua` — [`xbeach_morphology.md §B,§E,§G`](../../models/XBeach/source-analysis/xbeach_morphology.md)(`morphevolution.F90`) **verified**
- EFDC van Rijn/Engelund-Hansen + Christoffersen-Jonsson shear — [`sediment/efdc_sediment.md §D,§F`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)·[`sediment/efdc_sedzlj.md`](../../models/EFDC/source-analysis/sediment/efdc_sedzlj.md) **verified**
- ROMS WEC vortex force + MPM/Soulsby-Damgaard/van der A bedload + Partheniades 부유 — [`roms_wec.md`](../../models/ROMS/source-analysis/roms_wec.md)·[`sediment/roms_sediment.md §C,§G`](../../models/ROMS/source-analysis/sediment/roms_sediment.md) **verified**
- radiation stress→longshore current 인과 chain — [`02-theory.md`](02-theory.md)(Holthuijsen §7.4.2-3) **verified**

## 9. 연결

- [`01-concept.md`](01-concept.md) — CERC·Komar-Inman empirical $Q_l$(one-line 모델의 입력 식)
- [`02-theory.md`](02-theory.md) — radiation stress→longshore current 유도(process-based chain 의 이론)
- [`03-analysis-methods.md`](03-analysis-methods.md)(미생성) — tracer·beach profile survey(모델 검증 데이터)
- [`05-examples.md`](05-examples.md)(미생성) — 한국 안목항·울산항 사례(모델 적용)
- [`concepts/sediment-transport/04-code-and-tools.md`](../sediment-transport/04-code-and-tools.md) — 일반 표사 code & tools(인접 토픽, Delft3D-SED·EFDC SED 공유)
- 모델 source-analysis:
  - [`models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md`](../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae.md)·[`sediment/delft3d_sediment.md`](../../models/Delft3D/source-analysis/sediment/delft3d_sediment.md)·[`delft3d_sediment_morphology.md`](../../models/Delft3D/source-analysis/delft3d_sediment_morphology.md)
  - [`models/XBeach/source-analysis/xbeach_morphology.md`](../../models/XBeach/source-analysis/xbeach_morphology.md)·[`xbeach-morphology-foundation.md`](../../models/XBeach/source-analysis/xbeach-morphology-foundation.md)
  - [`models/EFDC/source-analysis/sediment/efdc_sediment.md`](../../models/EFDC/source-analysis/sediment/efdc_sediment.md)·[`sediment/efdc_sedzlj.md`](../../models/EFDC/source-analysis/sediment/efdc_sedzlj.md)
  - [`models/ROMS/source-analysis/sediment/roms_sediment.md`](../../models/ROMS/source-analysis/sediment/roms_sediment.md)·[`roms_wec.md`](../../models/ROMS/source-analysis/roms_wec.md)
