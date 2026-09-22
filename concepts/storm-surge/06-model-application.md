---
title: "폭풍해일 — 06 모델 적용 (ADCIRC · Delft3D · ROMS · EFDC)"
topic: storm-surge
canonical_source: link-hub
citation_status: verified
has_source_needed: true
verification_method: "본 페이지는 link-hub — §1~§9 의 모델 메커닉 단언은 각 모델 verified source-analysis 노트로 소급한다(CONVENTIONS §3, 구현 복제 금지). **§10.1 full PDF 격상 (2026-09-22)**: 기존 abstract-level `source-needed` 스텁 2건을 전문 판독으로 승격 — arXiv:2601.03856v1(González·Denamiel·Macías, 2026-01-07 [physics.geo-ph]) 와 arXiv:2510.20074(Saviz Naeini·Snaiki·Di Luca, 2025) 를 curl + pdftotext 로 받아 §2.1-2.2·§3.2·§5 및 침수모형·한계 절을 직접 인용. 전자에서 확인: 양 모델 구성 대조(ADCIRC 비정형 10 m·바람+기압+조석경계 vs Meteo-HySEA 정형 5단 nested 7 m·기압만·조석경계 없음), 진폭은 장소별 엇갈림·주기는 일관 과대(중앙 37 vs 27분 등), 2017 사건에서 관측 20%+ 초과를 두 모델 모두 5% 미만으로 재현(강제 지배), 저자 자신의 **미판정 선언**(누가 옳은지 조밀 관측망 검증 필요), 주기 과대의 원인 가설이 **wet-dry 기법**. 후자에서 확인: 침수가 **bathtub**(정수압 평형·운동량/마찰/시간발전 무시·wave setup/runup 무시·정적지형·방재구조물 미반영)이고 $\\eta_{peak}$ 가 **풍속 경험식** 산출이며 **천문조 제외** — 전부 저자 명시 한계. ★본 위키 판단은 이 두 편을 §1 모델 스펙트럼 위에 위치시킨 것(10.1.2)과 wet-dry↔공진주기 연결(10.1.1)이며, 원문 인용과 구분해 표기했다. 잔존 source-needed = 메테오쓰나미 결론의 태풍 해일 전이 가능성 미확인(§10.1.1 말미), §10 의 SCHISM 미커버·타모델 한국 적용 미보강."
note_author: "Claude Opus 4.8 (1M context) → §10.1 격상 Claude Opus 5 (1M context)"
note_date: 2026-06-12
---

# 폭풍해일 — 06 모델 적용

> **Canonical source**: 모델 메커닉(구현·서브루틴·알고리즘)은 `models/<model>/`이 진실의 원천. 이 페이지는 **요약 + 링크만** ([CONVENTIONS.md](../../CONVENTIONS.md) §3, drift 방지). 구현 디테일은 복제하지 않고 source-analysis 노트로 링크.

폭풍해일은 **저기압·바람에 의한 이상고조**로, 수치적으로는 **천수방정식(depth-integrated SWE)** 을 바람응력·기압·조석·마찰·범람과 함께 푸는 문제. 이론은 [`02-theory.md`](02-theory.md)(Pugh §6 + GWCE), 인자는 [`01-concept.md`](01-concept.md) 참조.

## 1. 모델 선택 (도메인별)

| 모델 | 적합 도메인 | surge 위상 |
|---|---|---|
| **ADCIRC** | open-coast·대영역·비정형 메시 (de facto 표준) | barotropic 2DDI GWCE — **한반도 광역 surge 1순위** |
| **Delft3D-FLOW / D-Flow FM** | 하구·연안 structured(FLOW) / 비정형(FM) | ADI(structured) / Stelling-Kernkamp(FM) SWE |
| **ROMS (+COAWST)** | 해양순환 결합 surge·baroclinic | barotropic mode + wave/sediment 결합 |
| **EFDC** | 만·하구 천해 surge·범람 | external mode(수위) + 천해 |

## 2. 한국 적용 표준 흐름

ADCIRC barotropic + 태풍 parametric/재분석 바람 + (선택) SWAN 결합 wave setup. KHOA 정점 검증. 자세한 입출력·NWS 모드는 [`04-code-and-tools.md`](04-code-and-tools.md), 검증 사례는 [`05-examples.md`](05-examples.md).

## 3. ADCIRC — canonical (주 surge 모델)

지배방정식과 surge 구성요소 (전부 `models/ADCIRC/source-analysis/` verified 링크):

- **수위(연속)**: [GWCE](../../models/ADCIRC/source-analysis/adcirc-gwce-implementation.md) — generalized wave-continuity로 ζ 산출 (surge 본체). 선형solver는 [ITPACKV JCG](../../models/ADCIRC/source-analysis/adcirc-itpack-solver.md), 실행순서는 [timestep orchestration](../../models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md).
- **유속(운동량)**: [momentum](../../models/ADCIRC/source-analysis/adcirc-momentum-implementation.md) — U,V 2D 운동량(GWCE companion).
- **기상 강제력(surge 구동)**: [met-forcing](../../models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md) — 바람응력 + 기압. NWS 모드 카탈로그는 [storm-surge/ NWS families](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md) + [foundation](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md).
- **조석–해일 상호작용**: [tidal-forcing](../../models/ADCIRC/source-analysis/adcirc-tidal-forcing.md) — 조석 body-force + SAL. 천해 비선형 결합은 [`03-analysis-methods.md`](03-analysis-methods.md)(Pugh tide-surge separation).
- **바닥마찰**: [nodal-attributes](../../models/ADCIRC/source-analysis/adcirc-nodal-attributes.md) — Manning→Cd 등 공간변화 마찰(surge 진폭 지배 인자).
- **범람(wet/dry)**: [wetting-drying](../../models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md) — NOLIFA/H0/NODECODE 침수.
- **경계·구조물**: [boundary-conditions](../../models/ADCIRC/source-analysis/adcirc-boundary-conditions.md)(radiation/flux/sponge) + [weir-boundary](../../models/ADCIRC/source-analysis/adcirc-weir-boundary.md)(제방·월류).
- **wave setup(해일 가산)**: [SWAN coupling](../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md) — radiation stress가 surge에 추가. wave 측은 [`../waves/06-model-application.md`](../waves/06-model-application.md).
- **경압(보통 surge엔 2D barotropic)**: [3D mode](../../models/ADCIRC/source-analysis/adcirc-3d-mode.md) · [baroclinic coupling](../../models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md).
- 메시 구축(개인 프로젝트)은 canonical 아님 → 바이블 검증 통과 시 `experience/` 로 카테고리화 (canonical 미수록, source-needed).

## 4. Delft3D-FLOW / D-Flow FM

- **structured FLOW**: [ADI solver](../../models/Delft3D/source-analysis/delft3d_adi_solver.md)(SUD/UZD double-sweep) — 수위·운동량 implicit. 바람·기압 강제력으로 surge.
- **unstructured FM**: [kernel scheme](../../models/Delft3D/source-analysis/delft3d_dflowfm_kernel_scheme.md)(furu/s1nod Guus-NestedNewton) + [overview](../../models/Delft3D/source-analysis/delft3d_dflowfm_overview.md) · 입력 [mdu](../../models/Delft3D/source-analysis/delft3d_dflowfm_mdu_input.md). 비정형 연안 surge·범람.

## 5. ROMS (+COAWST)

- **barotropic mode**: [2D barotropic](../../models/ROMS/source-analysis/roms_barotropic_2d.md) — fast-mode 수위(surge 성분). 조석 강제는 [tidal forcing](../../models/ROMS/source-analysis/roms_tidal_forcing.md).
- ROMS 단독 surge는 드물고, **COAWST 결합**(wave·sediment·atm)로 활용 — [`models/ROMS/web-refs/roms-official-resources.md`](../../models/ROMS/web-refs/roms-official-resources.md) §3.6.

## 6. EFDC

- **external mode**: [external mode solver](../../models/EFDC/source-analysis/efdc_external_mode_solver.md)(congrad 5-point Jacobi-CG 수위) + [hydro core](../../models/EFDC/source-analysis/efdc_hydro_core.md). 만·하구 천해 surge·범람. 내부 wind-wave는 [waves](../../models/EFDC/source-analysis/efdc_waves.md).

## 7. 검증 (한국 사례)

[`05-examples.md`](05-examples.md)의 관측 검증 case와 대응:
- **Maemi 2003**(마산 최악, source-needed) · **Hinnamnor 2022**(포항 +36cm spike, verified) · **Bolaven 2012**(군산외해 ADCP 잔차, verified)
- 독립 설계모델 검증: 서승원·이화영(2012) pADCIRC+unSWAN 목포 100년 191cm — [[khoa-design-surge-eva-2026]] §4 3중일치.

## 8. 다른 토픽과의 교차

- [`../tides/06-model-application.md`](../tides/06-model-application.md) — 조석 강제(같은 ADCIRC/Delft3D, surge와 동일 SWE에 중첩).
- [`../waves/06-model-application.md`](../waves/06-model-application.md) — wave setup이 surge에 가산(ADCIRC+SWAN / Delft3D-WAVE).
- [`02-theory.md`](02-theory.md) — GWCE 유도 + Pugh §6-7.

## 9. ML 우회 (surrogate)

위 full-physics 모델을 **ML emulator가 대체/보정** — [`07-ml-emulators.md`](07-ml-emulators.md): direct emulator(PACT·Global LI·DeepSurge), bias-corrector(StormNet·HURRI-GAN), 학습전략(Regional surrogate). ADCIRC 출력이 대부분 surrogate의 학습 target.

## 10. 보강 — `verified` 승격·미커버

- **SCHISM** 미커버(본 위키 미수록 모델) — 한반도 surge 연구 다수 사용, 향후 후보.
- Delft3D/ROMS/EFDC surge **한국 적용 사례** 정량 검증은 미보강(현재 ADCIRC 중심).
- 각 모델 surge 입력카드(바람·기압 강제력 포맷) 요약은 source-analysis 본문 참조.

### 10.1 연구 문헌 ✅ verified (full PDF 판독 2026-09-22)

두 편 모두 전문을 읽었다. 하나는 **ADCIRC 와 정면으로 붙은 비교 연구**이고,
다른 하나는 본 §1 스펙트럼의 **아래쪽 끝(hazard/risk 층)** 이 어떻게 생겼는지 보여준다.

#### 10.1.1 Meteo-HySEA vs AdriSC-ADCIRC — 같은 강제, 다른 답, 판정 불가

González·Denamiel·Macías (2026) "Assessing Meteo-HySEA Performance for Adriatic Meteotsunami
Events", arXiv:[2601.03856](https://arxiv.org/abs/2601.03856)v1 [physics.geo-ph], 2026-01-07
(Univ. Málaga + Ruđer Bošković Inst. + Inst. Adriatic Crops).

**메테오쓰나미**(기압擾亂이 구동하는 해면진동)를 대상으로 하지만, 본 위키에 중요한 것은
**동일 대기강제 아래 두 솔버를 맞붙인 통제 비교**라는 점이다.

| | **AdriSC-ADCIRC** (CPU) | **Meteo-HySEA** (multi-GPU) |
|---|---|---|
| 격자 | 비정형, 취약 항만에서 **최대 10 m** | **정형 two-way nested 5단** — 1 km→250 m→60 m→30 m→**7 m** |
| 대기강제 | WRF 1.5 km **1분** 바람 + 기압 | WRF 1.5 km **기압**(1 km 격자로 재표본) |
| 해양 경계 | ROMS 1 km 시간별 SSH — **조석 포함**(Otranto) | **없음** — 초기 해면만 ROMS 에서, *"focusing purely on the atmospheric disturbance-driven dynamics"* |
| 침수 | (본 논문 범위 밖) | **직접 모의** |

★ **진폭은 장소마다 엇갈리고, 주기는 일관되게 어긋난다.**
2014-06-25 사건에서 Meteo-HySEA 는 Vela Luka 에서 더 크고(≈1.0 m vs 0.6 m)
Stari Grad·Vrboska 에서는 더 작다(0.5 vs 0.6 / 0.4 vs 0.5 m). 그런데 **주기는 세 항만 모두에서
Meteo-HySEA 가 크다** — 중앙 주기 18 vs 17분, **37 vs 27분**, **16 vs 10분**.[^mh-amp]

★ **병목은 솔버가 아니라 강제다.** 2017 사건에서 관측 진동의 **20% 이상이 0.2 m 를 넘는데,
두 모델 모두 5% 미만**만 그 문턱을 넘는다 — 강제 종류(ERAI/ERA5)를 바꿔도 마찬가지다.[^mh-force]
저자들의 첫 번째 결론이 이것이다: *"Meteotsunami simulation accuracy is fundamentally limited
by the quality of atmospheric forcing"* — 고해상 WRF 다운스케일링을 해도 중규모 기압擾亂의
강도·공간변동이 과소평가된다.[^mh-concl]

★ **그리고 둘 중 누가 맞는지 이 연구는 판정하지 못한다.** 저자들이 향후 과제로 명시한다 —
조밀한 관측망(조위계·기압계·HF 레이더) 검증이 있어야
*"Meteo-HySEA 의 더 긴 진동 지속이 더 현실적인 항만 seiche 를 잡는 것인지,
ADCIRC 의 더 강한 감쇠가 물리적 에너지 소산을 더 잘 표현하는 것인지"* 를 가릴 수 있다.[^mh-concl]

★ **주기 과대의 가설이 침수-건조 기법이다.** 저자들은 원인으로 *"the wet–dry technique, in which
the geomorphology of basins and harbors evolves over time as the wet areas are updated"* 를 지목한다.[^mh-concl]
즉 **마스크 갱신이 만·항의 유효 형상을 바꾸고, 그것이 공진 주기를 바꾼다.**
[[wetting-drying-cross-model]] 이 8모델의 마스크 임계·판정 방식을 대조했는데,
그 선택이 **침수 범위뿐 아니라 공진 주기까지 움직인다**는 사례다.
같은 축의 다른 사례가 [[../swash-zone/06-model-application]] §3 — 침수-건조 임계가 처오름 정의를 바꾼다.

계산 효율은 Meteo-HySEA 쪽이 압도적이고(GPU, order-of-magnitude), 침수를 직접 모의해
외해 진동 → 육상 범람까지 사슬을 잇는다 — 단 *"고품질·고해상 연안 지형수심 자료"* 가 전제다.[^mh-concl]

> **한계 표기**: 본 항은 **메테오쓰나미** 사례다. 태풍 폭풍해일에 같은 결론이 옮겨가는지는
> 이 논문이 다루지 않았고 본 위키도 확인하지 않았다 `source-needed`.

#### 10.1.2 기후 투영 hazard/risk — 본 스펙트럼의 아래쪽 끝

Saviz Naeini·Snaiki·Di Luca (2025) "Projecting Hurricane Risk in Atlantic Canada under Climate
Change", arXiv:[2510.20074](https://arxiv.org/abs/2510.20074) (ÉTS/UQÀM).

2단계 설계다 — ① 물리기반 합성 태풍 경로 대앙상블로 **재현기간 풍속**과 **침수 심도·범위**의
변화를 기준기간(1979–2014) → 근미래(2024–2059) → 원미래(2060–2095)로 투영(해수면 상승 포함),
② 바람을 총손실의 **운영 대리변수**로 삼아 노출·취약도와 결합해 기대손실 산정.

★ **그런데 침수 모형이 bathtub 이다.** 해안과 수리적으로 연결되고 표고가 $\eta_{peak}$ 보다 낮은
육상 격자를 침수로 판정하고 $Depth = \eta_{peak} - $ 지반고로 계산한다. 저자들이 가정을 직접 나열한다 —
**정수압 평형**(물이 즉시 채워짐), **유동 관성·마찰·침수의 시간발전 무시**, **wave setup·runup 무시**,
정적 지형(폭풍 중 지형변화 없음), 방재구조물은 DEM 에 해상되지 않는 한 미반영.[^ac-bathtub]

★ 더 결정적인 것은 그 $\eta_{peak}$ 의 출처다 — **풍속에서 단순 경험식으로** 해일을 추정하며,
저자들이 *"a key limitation, as the true relationship is highly sensitive to local bathymetry"*
라고 적는다. **천문조도 제외**돼 있다.[^ac-limit]

본 §1 의 모델 스펙트럼에 놓으면 위치가 분명하다 — ADCIRC·Delft3D 가 SWE 를 푸는 층,
[[../compound-flooding/06-model-application]] 의 SFINCS·LISFLOOD-FP 가 단순화 SWE 층이라면,
**이 연구의 침수는 방정식을 풀지 않는 층**이다. 광역·다세대(多世代) 앙상블과 손실 산정을 위해
물리를 버린 교환이며, 저자들도 향후 과제 1순위로 *"replacement of the bathtub approach with
hydrodynamic modeling that resolves timing, velocities, and wave effects"* 를 든다.[^ac-limit]

같은 향후 과제 목록의 다음 항목이 본 위키와 맞물린다 — *"expand to compound events, such as
storm surge coincident with heavy rainfall"*. 그것이 [[../compound-flooding/01-concept]] 의 주제이고,
확률적으로 그 결합을 어떻게 다루는지는 [[../compound-flooding/03-analysis-methods]] 가 맡는다.[^ac-limit]

> **인용 시 주의**: 이 논문의 "침수 증폭" 수치를 수리동역학 모의 결과처럼 인용하면 안 된다.
> bathtub + 경험식 해일 + 무조석의 산출이다.

### 10.2 §10.1 출처

[^mh-amp]: González et al. (2026) arXiv:2601.03856v1 §3.2 Performance of the Meteo-HySEA model — 2014-06-25(WRF-ERA5): Vela Luka *"approximately 1 m vs. 0.6 m"*, Stari Grad *"0.5 m vs. 0.6 m"*, Vrboska *"0.4 m vs. 0.5 m"*(앞이 Meteo-HySEA). 06-26 사건은 Vela Luka 0.3 vs 0.4, Vrboska 0.15 vs 0.2, Stari Grad 양쪽 ≈0.19 m. 주기: *"Meteo-HySEA consistently overestimates the periods of meteotsunami oscillations relative to AdriSC-ADCIRC"* — WRF-ERA5 중앙 주기 18분(vs 17), 37분(vs 27), 16분(vs 10). 2017 사건도 19(vs 17)·36(vs 29)·15(vs 14)분. 같은 절이 **관측** 중앙 주기는 Vela Luka 14분·Stari Grad 16분이라고 적으며 *"the harbor geomorphology is likely not well captured by either model, particularly in Stari Grad"* 로 맺는다. 모델 구성은 §2.1–§2.2: AdriSC-ADCIRC = 2DDI, 비정형 mesh *"refined to spatial resolutions of up to 10 m"*, WRF 1.5 km 분 단위 바람·기압 + ROMS 1 km 시간별 SSH(조석 포함) 남측 경계; Meteo-HySEA = HySEA 계열 two-way nested + multi-GPU, Table 1 의 5단 격자(1 km / 250 m / 60 m / 30 m / 7 m), 기압장을 1 km 영격자에 맞춰 재표본, 시간축은 인접 두 스냅샷의 convex 선형보간, 그리고 *"does not include tidal or large-scale sea-level boundary forcing at the open boundary, focusing purely on the atmospheric disturbance-driven dynamics."*
[^mh-force]: 同 §3.2 (2017 사건) — *"more than 20% of the observed oscillations exceed 0.2 m at Vela Luka and Stari Grad, whereas fewer than 5% of wave heights modeled by Meteo-HySEA or AdriSC-ADCIRC (forced by either WRF-ERAI or WRF-ERA5) exceed this threshold."* 두 모델 모두 2017-06-28·06-30·07-01 의 0.15 m 초과 장시간 진동을 재현하지 못한다고 같은 절이 적는다.
[^mh-concl]: 同 §5 Concluding remarks — ① *"Meteotsunami simulation accuracy is fundamentally limited by the quality of atmospheric forcing. Even with high-resolution WRF downscaling, mesoscale pressure disturbances are often underestimated in intensity and spatial variability."* ② 주기 과대의 원인 가설 *"This issue may stem from the wet–dry technique, in which the geomorphology of basins and harbors evolves over time as the wet areas are updated."* ③ GPU *"enables high-resolution multi-grid simulations to run orders of magnitude faster than conventional CPU-based models"* + 침수 직접 모의 *"extending the modeling chain from offshore oscillations to onshore flooding"* — 단 *"high-quality, high-resolution topobathymetric data are required"*. ④ 미판정 *"systematic validation with dense observational networks (tide gauges, pressure sensors, HF radar) is needed to determine whether the longer persistence of oscillations in Meteo-HySEA reflects more realistic harbor seiches or ADCIRC's stronger damping better represents physical energy dissipation."*
[^ac-bathtub]: Saviz Naeini et al. (2025) arXiv:2510.20074 §coastal flood hazard modeling — *"All land grid cells hydraulically connected to the coast and having an elevation lower than the estimated η_peak are identified as inundated. The inundation depth at each affected grid cell was then computed as Depth = η_peak − Ground Elevation."* 가정 나열: *"The approach assumes hydrostatic equilibrium (water instantly fills connected areas to the peak level) and neglects hydrodynamic effects such as flow momentum, friction, or the temporal evolution of the inundation. Furthermore, the contributions of wave setup and runup are neglected. The model also treats the landscape as static and does not account for morphological changes during the storm or the presence and potential failure of local flood defense structures unless these features are accurately resolved within the underlying DEM."*
[^ac-limit]: 同 §Discussion/Limitations — *"the bathtub flood model is a significant simplification of flood dynamics, neglecting hydrodynamic effects and wave action. The use of a simplified empirical formula to estimate storm surge from wind speed is a key limitation, as the true relationship is highly sensitive to local bathymetry. The exclusion of astronomical tides is another simplification that could affect peak water levels."* 향후 과제: *"for coastal flooding, replacement of the bathtub approach with hydrodynamic modeling that resolves timing, velocities, and wave effects"* 및 *"the scope of risk assessment should expand to compound events, such as storm surge coincident with heavy rainfall, and to dynamic interactions where wind damage alters subsequent flood vulnerability."* 2단계 설계(hazard 투영 → 바람 대리 risk)와 기간 구분(1979–2014 / 2024–2059 / 2060–2095, SLR 포함)은 §Abstract·§Introduction.

## 11. 연결

- [`01-concept.md`](01-concept.md) · [`02-theory.md`](02-theory.md) · [`03-analysis-methods.md`](03-analysis-methods.md) · [`04-code-and-tools.md`](04-code-and-tools.md) · [`05-examples.md`](05-examples.md) · [`07-ml-emulators.md`](07-ml-emulators.md)
- 모델: [`models/ADCIRC/`](../../models/ADCIRC/) · [`models/Delft3D/`](../../models/Delft3D/) · [`models/ROMS/`](../../models/ROMS/) · [`models/EFDC/`](../../models/EFDC/)
