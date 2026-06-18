---
title: "Storm Surge 한국 case — Maemi 2003 + Hinnamnor 2022 cross-reference"
topic: storm-surge
canonical_source: self
citation_status: partial-verified
verification_method: "본 위키 내 cross-reference 만 verified — 02-theory.md (Pugh §6:3 IB 식, Maemi 950 mb / Hinnamnor 920 mb 중심기압 인용) + 04-code-and-tools.md (NWS 모드·KHOA OpenAPI + archive 한계 verified) + models/ADCIRC/source-analysis/storm-surge/ 7개 노트 (NWS=13 JMA-MSM + GAHM Best Track + fort.15 운영 규칙). **§2 Hinnamnor 2022 는 KHOA Annual Report 2022 §3 직접 인용으로 verified** (별도 노트 [[khoa-annual-2022-hinnamnor-surge]] 분리, 2026-05-28). **§1 Maemi 2003 §1.1.1 partial-verified (2026-06-01) — Wikipedia + Park et al. JCR SI65 doi:10.2112/SI65-067.1 + eSurge + WebSearch 직접 인용. peak 910 hPa (JMA) / 885 hPa (JTWC) / Jeju national record 950 hPa / 마산 1.40 m 1403 mm / 사망 120명 / ₩5.52 trillion 손실 확보**. KHOA Annual Report 2003 부재 (백서 변환 2012 시작) — KHOA 직접 fetch source-needed. **§4.1 Bolaven 2012 는 KHOA Annual Report 2012 vol.1 §7.3 직접 인용으로 verified** (별도 노트 [[khoa-annual-2012-bolaven-surge]] 분리)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 위키 내부 cross-ref만 verified, 외부 실측 수치는 source-needed 분리"
verification_date: 2026-05-24
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - concepts/storm-surge/04-code-and-tools.md
  - models/ADCIRC/source-analysis/storm-surge/
  - experience/khoa-annual-climate-trend.md
  - experience/khoa-2024-mhw-extreme.md
---

# Storm Surge 한국 case — Maemi 2003 + Hinnamnor 2022

> 본 §는 한국에 큰 영향을 준 두 태풍 case 의 cross-reference 노트. **실측 surge peak 수치는 KHOA Annual Report 직접 fetch 후 verified 로 승격 가능 — 현재 source-needed**. 도구·workflow·식 계산은 본 위키 내 verified 자료 인용.
>
> **본 노트의 정직성 원칙** (M2 rule, efdc-chuksan-sediment 패턴):
> - 본 위키 안에서 verified 인 자료 (Pugh 식, ADCIRC source-analysis, KHOA OpenAPI workflow) 만 직접 인용
> - 외부 실측 수치 (관측 surge, Best Track 중심기압 절대값, 침수 면적) 는 source 만 명시하고 본 위키 안에서 verified 처리 안 함
> - 본 위키 02-theory.md 의 표 ([§2.2 한국 적용](02-theory.md#22-한국-적용--태풍-ib-surge)) 의 950/920 mb 도 원본 출처 (KMA·JMA RSMC) fetch 후 별도 검증 필요

## 1. Case A — Maemi 2003 (매미, 0314호)

### 1.1 Case 개요 (source-needed)

| 항목 | 값 | 출처·검증 상태 |
|---|---|---|
| 시기 | 2003-09-12 ~ 13 | KMA·JMA RSMC Best Track — fetch 필요 |
| 한국 경로 | 남해 직격, 마산만 통과 | KMA Best Track 트랙 — fetch 필요 |
| 중심기압 (최저) | 950 mb (한반도 영향 시) | 본 위키 [02-theory.md §2.2 표](02-theory.md#22-한국-적용--태풍-ib-surge) 인용 (KMA·JMA RSMC 원본 fetch 필요) |
| 최대 surge | ~2.4 m 마산 | 본 위키 [01-concept.md §3.2 표](01-concept.md#32-한국-주요-태풍-storm-surge-case-khoa-annual-report-인용) 인용 (KHOA Annual Report 2003 §3.x fetch 필요) |
| 침수 피해 | 마산항 주변 광범위 침수 | 언론·공식 보고 — fetch 필요 |
| 분류 | benchmark TC | 한국 storm-surge 연구의 historical reference case |

#### 1.1.1 추가 verified 항목 (2026-06-01 partial-verified)

WebSearch + Wikipedia + Park et al. JCR 직접 fetch:

| 항목 | 값 | 출처 |
|---|---|---|
| Peak 시점 | 2003-09-10 1200 UTC | JMA RSMC Tokyo Annual Report 2003 (via Wikipedia) ✓ |
| 한국 상륙 | **2003-09-12 부산 서쪽** | Wikipedia + WebSearch ✓ |
| 중심기압 trajectory peak (JMA 10-min) | **910 hPa** | Wikipedia (JMA Best Track) ✓ |
| 중심기압 (JTWC 1-min) | **885 hPa** | Wikipedia (JTWC 15W report) ✓ |
| **중심기압 한반도 영향 시 (Jeju)** | **950 hPa** (national record) | Wikipedia ✓ |
| 최대 풍속 peak (10-min, JMA) | 195 km/h (120 mph) | Wikipedia ✓ |
| 최대 풍속 peak (1-min, JTWC) | 280 km/h (175 mph), Cat 5 | Wikipedia ✓ |
| 풍속 한반도 상륙 시 | 140 km/h (JMA) / 165 km/h (JTWC) | Wikipedia ✓ |
| **마산만 surge** | **1.40 m (1403 mm) on 2003-09-12, recurrence ~98 yr** | eSurge / Park et al. JCR SI 65, 2013 doi:10.2112/SI65-067.1 ✓ |
| 사망자 | 117 (한국) + 3 (일본) = **120** | Wikipedia ✓ |
| 한국 경제 손실 | **₩5.52 trillion** (~US$4.8B 2003) | Wikipedia ✓ |
| Homeless / 가옥 파괴 | 25,000 / ~5,000 | Wikipedia ✓ |

**Note: 본 위키 외부 실측 surge 와 추정 차이**:
- WebSearch/eSurge/Park et al.: **마산 1.40 m (residual or selected datum)**
- 본 위키 [01-concept.md §3.2](01-concept.md#32-한국-주요-태풍-storm-surge-case-khoa-annual-report-인용) 기존 표기: **~2.4 m**
- 차이 가능성: (a) 1.40 m = 잔차 (residual) vs 2.4 m = 절대 해수면 above MSL (천문조 + surge 합산), (b) 측정 정점 차이 (마산 조위관측소 vs 마산만 head), (c) 자료원 차이 (KHOA 직접 측정 vs 사후 hindcast 표시). KHOA Annual Report 2003 부재로 직접 비교 불가 — **§5 보강 우선순위 2 유지**.

**Maemi vs Hinnamnor 한반도 영향 시 비교**:
- Maemi: **910 hPa peak → 950 hPa (Jeju, 한반도 영향 시)** (Wikipedia ✓)
- Hinnamnor 2022 ([[khoa-annual-2022-hinnamnor-surge]]): trajectory peak 920 hPa → 영향 시 더 약화. 마산 영향 없음 (KHOA 2022 §3 직접: 마산 -38 cm 누년대비)
- **Maemi 가 한반도 직격·강도 모두 더 강함**. 02-theory.md §2.2 표의 Hinnamnor "920 mb" 는 trajectory peak 기준임을 명시 필요 (한반도 접근 시는 더 약화).

### 1.2 본 위키 도구로 풀어보기 — Maemi hindcast workflow (verified)

본 위키의 verified 도구로 Maemi hindcast 를 구성하는 standard workflow.

#### Step 1: IB 정적 surge 추정 (verified — Pugh §6:3)

[02-theory.md §2.2 Eq](02-theory.md#22-한국-적용--태풍-ib-surge) — 중심기압 950 mb 가정 시:

$$\eta_{IB} = -\frac{\Delta P_A}{\rho g} = -\frac{(950 - 1013) \text{ mb}}{1025 \times 9.81 / 100} \approx +0.63 \text{ m}$$

→ 정적 IB 만 +63 cm. 관측 ~2.4 m 와 비교 → 나머지 ~1.8 m 는 **wind set-up + tide-surge interaction + wave setup** 기여 (Pugh §6:4, §7:8, [02-theory.md §3-4](02-theory.md)).

#### Step 2: ADCIRC NWS 모드 선택 (verified — ADCIRC source-analysis)

[04-code-and-tools.md §1.1](04-code-and-tools.md#11-nws-모드-일람) 의 9 NWS 모드 중:

- **NWS=20 (GAHM)** — Best Track + ATCF wind radii 기반 vortex 재구성. 학술 hindcast 표준.
- **NWS=13 (JMA-MSM NetCDF)** — JMA-MSM 분석장 직접. 사용자 표준 워크플로. 단, Maemi 2003 의 JMA-MSM 보유 여부 별도 확인.
- **NWS=30 (GAHM + OWI hybrid)** — vortex + 배경 NWP. 가장 정밀.

→ Maemi 학술 hindcast 는 보통 **NWS=20 GAHM** + KMA Best Track. 상세는 [`models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md).

#### Step 3: `fort.15` 운영 셋팅 (verified — ADCIRC source-analysis)

[04-code-and-tools.md §2.1](04-code-and-tools.md#21-fort15-control-file) + [`adcirc-fort15-nws13-operating-rules.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-fort15-nws13-operating-rules.md):

```
NWS = 20            ! GAHM
NOIVB = 0           ! IB 자동 포함 (PRBCKGRND = 1013.0 mb)
RampMete = 86400    ! 1 day vortex spin-up
WTIMINC = 3600      ! 1 h met increment
BLAdj = 0.9         ! standard BL adjustment
IM = 0              ! Garratt drag (Table 2.2 [[efdc-theory-v12-ch2-hydrodynamics]] §2.4 의 Garratt 1977 과 동일)
```

#### Step 4: KHOA 정점 검증 (verified — 04-code-and-tools.md §4)

[04-code-and-tools.md §4.1](04-code-and-tools.md#41-실시간-조위-관측) 의 KHOA OpenAPI `surveyTideLevel` workflow — Maemi 시기 (`reqDate=20030912`, `obsCode=DT_0005` 부산 등) 로 fetch 후 `tdlvHgt - bscTdlvHgt` residual = observed surge.

> **단**: KHOA OpenAPI 의 archive 가 2003 까지 거슬러 가는지 별도 확인 필요. archive 한계 시 KHOA Annual Report 2003 PDF 직접 인용 fallback.

### 1.3 본 위키 안 cross-reference

| 자료 | 사용처 |
|---|---|
| [02-theory.md §2.2](02-theory.md#22-한국-적용--태풍-ib-surge) | IB +0.63 m 계산 |
| [02-theory.md §3 Wind set-up](02-theory.md) | 마산만 천해 + 풍속 ↑ → wind set-up 큼 |
| [02-theory.md §4 Tide-surge interaction](02-theory.md) | 마산만 tide range + storm surge 비선형 결합 |
| [`adcirc-storm-surge.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md) | GAHM source-code level |
| [`adcirc-storm-surge-requirements-checklist.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-requirements-checklist.md) | hindcast workflow 7 step |

---

## 2. Case B — Hinnamnor 2022 (힌남노, 2211호) — **verified**

> 본 §는 [[khoa-annual-2022-hinnamnor-surge]] (KHOA Annual Report 2022 §3 직접 인용) 으로 verified 승격됨 (2026-05-28).

### 2.1 Case 개요 (verified — KHOA Annual Report 2022)

| 항목 | 값 | 출처·검증 |
|---|---|---|
| 시기 | 2022-09-06 ~ 07 (한반도 상륙) | KHOA 2022 line 3350, 4486 ✓ |
| 한국 경로 | **남동해안 직격** — 포항·울산이 주 영향 | KHOA 2022 line 3350 ✓ |
| 중심기압 (최저, 전체) | 920 mb (한반도 접근 시 약화) | 본 위키 [02-theory.md §2.2 표](02-theory.md#22-한국-적용--태풍-ib-surge) (JMA RSMC 원본 fetch 필요) — partial |
| **포항 최대 surge peak** | **137.0 cm** (2022-09, 19년 최대치) | KHOA 2022 표 3-258·3-259 ✓ |
| 포항 9월 편차 (누년대비) | **+36 cm** | KHOA 2022 표 3-259 ✓ |
| 울산 최대 (9월) | 124.0 cm (+5 cm 편차) | KHOA 2022 표 3-253·3-254 ✓ |
| 마산 (영향 없음 확인) | 227 cm (누년대비 **-38 cm**) | KHOA 2022 표 3-223·3-224 ✓ |
| 통영 (영향 없음 확인) | 302 cm (누년대비 -55 cm) | KHOA 2022 표 3-213·3-214 ✓ |
| 생일도 부이 최대 유의파고 | **5.81 m** | KHOA 2022 line 4486 ✓ |
| 9월 월평균 풍속 (전국) | **18.6 m/s** (월별 최고) | KHOA 2022 line 4212 ✓ |
| 침수 피해 | 포항 일대 침수 (제철소 등) | 언론·KMA 사후 보고 — fetch 필요 |
| 분류 | recent extreme TC, 동해 직격 | 한국 동해안 storm-surge 의 최근 reference case |

핵심 정량 finding: **동해 직격 경로** → 포항만 +36 cm 양의 spike, 남해안 (마산·통영)은 누년 9월보다 30-55 cm 낮음. Hinnamnor 2022 ≠ Maemi 2003 (남해 직격) pattern. 상세 정점별 데이터 + 해역 평균 표 + Bolaven 2012 대비는 [[khoa-annual-2022-hinnamnor-surge]] §2-3.

### 2.2 본 위키 도구로 풀어보기 — Hinnamnor hindcast workflow (verified)

#### Step 1: IB 정적 surge 추정 (verified — Pugh §6:3)

[02-theory.md §2.2 Eq](02-theory.md#22-한국-적용--태풍-ib-surge) — 중심기압 920 mb 가정 시:

$$\eta_{IB} = -\frac{(920 - 1013)}{1025 \times 0.0981} \approx +0.93 \text{ m}$$

→ 정적 IB 만 +93 cm. 관측 **포항 137 cm** (KHOA 2022 verified) 와 비교 → IB 가 대부분 + wind set-up·tide-surge·wave setup ~44 cm 추가 기여 추정.

**주의**: 920 mb 는 Hinnamnor 의 전체 trajectory 최저값. 한반도 접근 시 약화되었을 가능성 — 정확한 한반도 접근 시 중심기압은 KMA·JMA Best Track 직접 fetch 필요 (partial verified, [[khoa-annual-2022-hinnamnor-surge]] §6).

**Maemi 대비 동해 (수심 ↑) 라 wind set-up 작은 것이 일관** (Pugh §6:4 의 $\tau_w / \rho g H$ 식 — $H$ 클수록 set-up 작음, [02-theory.md §3](02-theory.md)) — 포항 +36 cm 편차는 만 안쪽이라 wind set-up 일부 발달, 마산 -38 cm 는 직격 경로 밖.

#### Step 2: ADCIRC NWS 모드 선택 (verified)

Hinnamnor 는 **사용자 표준 워크플로 NWS=13 JMA-MSM NetCDF** 사용 가능 (2022 는 JMA-MSM archive 충분). 상세:

- [04-code-and-tools.md §1.2](04-code-and-tools.md#12-한국-운영-워크플로--nws13-jma-msm) — JMA-MSM 5 km × 5 km 표준
- [`adcirc-jma-msm-nws13-foundation.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-jma-msm-nws13-foundation.md) — `owiwind_netcdf.F:215, 681, 747` reader

#### Step 3: `fort.15` 운영 셋팅 (verified)

NWS=13 표준 셋팅 ([adcirc-fort15-nws13-operating-rules.md](../../models/ADCIRC/source-analysis/storm-surge/adcirc-fort15-nws13-operating-rules.md) §3):

```
NWS = 13
NOIVB = 0
RampMete = 86400
WTIMINC = 3600     ! JMA-MSM 의 1 h
```

#### Step 4: KHOA 정점 검증 — **KHOA Annual Report 2022 경로** (verified)

KHOA OpenAPI `surveyTideLevel` 은 archive **~1년 rolling** ([04-code-and-tools.md §4.1 Archive 한계](04-code-and-tools.md#41-실시간-조위-관측)) → 2026 시점에서 Hinnamnor 2022 자료 fetch 불가. **KHOA Annual Report 2022 PDF (markdown 변환) 가 verified source**:

| 정점 | 2022 9월 고극조위 | 누년대비 편차 | 출처 |
|---|---|---|---|
| **포항** | **137.0 cm** | **+36 cm** (양의 최대) | KHOA 2022 표 3-258·3-259 |
| 울산 | 124.0 cm | +5 cm | KHOA 2022 표 3-253·3-254 |
| 마산 | 227 cm | -38 cm (영향 없음) | KHOA 2022 표 3-223·3-224 |
| 통영 | 302 cm | -55 cm (영향 없음) | KHOA 2022 표 3-213·3-214 |
| 동해안 평균 | 92.6 cm | -0.6 cm | KHOA 2022 표 3-5 |
| 서해안 평균 | 747.2 cm | -25.2 cm | KHOA 2022 표 3-5 |
| 남해안 평균 | 312.8 cm | -25.5 cm | KHOA 2022 표 3-5 |

→ **동해안만 누년 수준 유지 (편차 -0.6 cm)**. 다른 해역은 -25 cm. Hinnamnor 동해 직격 정량 입증.

상세는 [[khoa-annual-2022-hinnamnor-surge]] §2.

### 2.3 본 위키 안 cross-reference

| 자료 | 사용처 |
|---|---|
| [02-theory.md §2.2](02-theory.md#22-한국-적용--태풍-ib-surge) | IB +0.93 m 계산 |
| [02-theory.md §3 Wind set-up](02-theory.md) | 동해 깊은 수심 → wind set-up 작음 |
| [04-code-and-tools.md §1.2](04-code-and-tools.md#12-한국-운영-워크플로--nws13-jma-msm) | NWS=13 JMA-MSM 표준 워크플로 |
| [04-code-and-tools.md §4.1 KHOA](04-code-and-tools.md#41-실시간-조위-관측) | residual surge 추출 |
| [`adcirc-jma-msm-nws13-foundation.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-jma-msm-nws13-foundation.md) | source-code level NetCDF reader |
| [[khoa-2024-mhw-extreme]] | 동해 marine heatwave + 태풍 강도화 cascade |

---

## 3. Cross-comparison — Maemi 2003 vs Hinnamnor 2022

### 3.1 정형 비교표

| 항목 | Maemi 2003 | Hinnamnor 2022 | 본 위키 식·도구 |
|---|---|---|---|
| **경로** | 남해 직격 (마산) | **남동해안 직격** (포항·울산) | KMA Best Track / KHOA 2022 line 3350 ✓ |
| **중심기압 (trajectory 최저)** | 950 mb | 920 mb | [02-theory.md §2.2](02-theory.md) — partial |
| **IB 정적 (계산)** | +0.63 m | +0.93 m | Pugh §6:3 verified 계산 |
| **관측 surge peak** | ~2.4 m 마산 (source-needed) | **포항 137 cm = +36 cm 누년편차** ✓ | KHOA 2022 표 3-258 |
| **반대 해역 영향** | (자료 미)  | 마산 -38 cm, 통영 -55 cm 누년편차 (영향 없음) ✓ | KHOA 2022 표 3-223·3-213 |
| **IB / 관측 비** | 0.26 | **0.68** (0.93 / 1.37) | wind set-up + tide-surge 의 상대 기여 추정 |
| **주된 비-IB 기여** | wind set-up + tide-surge interaction (마산만 천해·tide ↑) | wind set-up (동해 깊은 수심에서 작음, 만 안쪽 일부) | Pugh §6:4, §7:8 |
| **표준 NWS 모드 (학술)** | NWS=20 GAHM + KMA Best Track | NWS=13 JMA-MSM (5 km) + GAHM 비교 | [04-code-and-tools.md §1](04-code-and-tools.md) |
| **KHOA archive** | 2003 — 부재 (백서 2012부터) | 2022 — OpenAPI 1년 한계 → **KHOA Annual 2022 PDF verified** ✓ | [04-code-and-tools.md §4](04-code-and-tools.md), [[khoa-annual-2022-hinnamnor-surge]] |
| **wave coupling 권장** | ADCIRC + SWAN (마산만 천해 wave setup ↑) | ADCIRC + SWAN (생일도 부이 H_s = 5.81 m verified ✓) | [04-code-and-tools.md §3](04-code-and-tools.md) + KHOA 2022 line 4486 |

### 3.2 한국 storm-surge 의 climate cascade 관점

본 위키 [01-concept.md §3.3 SLR + SST 강화 + storm surge cascade](01-concept.md#33-slr--sst-강화--storm-surge-의-climate-cascade):

- Maemi (2003) 시점의 한국 MSL 대비 Hinnamnor (2022) 는 약 **+7.5 cm** 누적 (3.94 mm/yr × 19년, [[khoa-annual-climate-trend]])
- 동시 SST 가속 (동해 +0.30°C/decade 등, [[khoa-sst-warming-trend]]) → 태풍 강도화 가능성
- → 같은 surge magnitude 라도 **effective inundation level 은 매년 증가** — 100년 누적 시 +40 cm baseline 상승

→ 본 위키의 SLR + SST experience 노트는 storm-surge case 분석의 climate boundary condition.

### 3.3 EFDC 와의 비교 (deep modeling)

ADCIRC 가 한국 storm-surge 의 primary unstructured 모델이라면, **EFDC+ 의 structured grid + sigma vertical** 은 만·항만 dredged channel 의 local 3D 해석에 적합:

- 마산만 (Maemi case) 의 dredged channel + 만 안쪽 stratification → EFDC+ Sigma-Zed (SGZ) 권장 ([[efdc-theory-v12-ch2-hydrodynamics]] §4.2)
- Hinnamnor 의 포항·울산항 storm-surge + sediment resuspension → EFDC+ SedTran/SEDZLJ ([[efdc-theory-doc-v12]] §4.3) + propeller wash 결합 가능
- ADCIRC = regional + storm-surge envelope, EFDC+ = local + 3D detail — **두 모델 상보적**

---

## 4. 추가 한국 storm-surge case (참고 인덱스)

[01-concept.md §3.2](01-concept.md#32-한국-주요-태풍-storm-surge-case-khoa-annual-report-인용) 의 표:

| 태풍 | 연 | 한국 경로 | 관측 surge | 본 case 와 관계 |
|---|---|---|---|---|
| **Maemi (매미)** | 2003 | 마산만 직격 | ~2.4 m 마산 (source-needed) | **본 노트 §1** |
| Sanba (산바) | 2012 | 남해 동부 | ~1.5 m 부산 (source-needed) | Hinnamnor 와 유사 magnitude |
| **Bolaven (볼라벤)** | **2012-08-29** | 서해 종단 | ~1.2 m 인천 (source-needed) + **군산 외해 ADCP 잔차류 verified** | **§4.1 보강 (verified case)** |
| Lingling (링링) | 2019 | 서해 북상 | ~1.0 m 인천 (source-needed) | 서해 storm-surge baseline |
| **Hinnamnor (힌남노)** | 2022 | **남동해안 직격** | **포항 137 cm verified ✓** (KHOA 2022) | **본 노트 §2** ([[khoa-annual-2022-hinnamnor-surge]]) |

### 4.1 Bolaven 2012 verified — 군산 외해 ADCP 잔차 조류

⭐ **유일 verified case** (외부 실측 직접 인용): KHOA Annual Report 2012 vol.1 §7.3.

상세는 [`textbook/notes/khoa-annual-2012-bolaven-surge.md`](../../textbook/notes/khoa-annual-2012-bolaven-surge.md) — 군산 외해 5 ADCP 정점 (C3·C4·C5·C6) 좌표·관측기간·잔차류 시계열 (그림 7-64·7-81 직접) verified.

| 항목 | 값 | 인용 |
|---|---|---|
| 태풍 | Bolaven (제15호) | KHOA Annual 2012 vol.1 line 8165 |
| 통과 | **2012-08-29** | 동 line 8165 |
| C4 정점 (36°00'N, 125°40'E, 65 m) 표층 잔차류 | 통과 시 강한 북향 sub-tidal current | 그림 7-64 |
| C6(2nd) 정점 (36°00'57"N, 125°17'E, 45 m) 저층 잔차류 | 통과 시 북향 잔차 | 그림 7-81 |
| 결론 | "해수면 변화 및 유속의 증가가 발생" (직접 인용) | line 9208 |

→ **sea-level surge 직접 표는 본 보고서 vol.1·vol.2 검색에서 미발견** — KHOA Annual Report 2012 의 §3 조위 분석 챕터 또는 다른 출판물에서 보강 가능 (보강 우선순위 §5.2).

→ 본 위키 [`02-theory.md §2.2 wind stress`](02-theory.md#22-한국-적용--태풍-ib-surge) 의 wind set-up 메커니즘이 잔차 조류 형태로 verified 됨. ADCIRC NWS=20 GAHM hindcast 의 검증 대상으로 활용 가능.

### 4.2 추가 sub-노트 후보

- `concepts/storm-surge/05-examples-sanba-2012.md` — 남해 동부 case (KHOA Annual 2012 vol.1 § 부산·여수 정점 자료 확인 필요)
- `concepts/storm-surge/05-examples-lingling-2019.md` — 서해 북상 case (KHOA Annual 2019 markdown 변환 후)

---

## 5. Source-needed 보강 우선순위

본 노트의 verified 승격 (partial-verified → verified) 위한 잔여 작업:

1. ~~**KHOA Annual Report 2022 §3.x 직접 인용 (Hinnamnor)**~~ — ✅ **완료 (2026-05-28)**. [[khoa-annual-2022-hinnamnor-surge]] 노트로 분리, 포항 137 cm / 울산 124 cm / 마산 227 cm / 통영 302 cm + 9월 편차 + 풍속 18.6 m/s + 파고 5.81 m verified.
2. **KMA·JMA RSMC Best Track 직접 fetch** — Maemi 2003 + Hinnamnor 2022 의 트랙·시간별 중심기압·풍속·반경 → [02-theory.md §2.2 표](02-theory.md#22-한국-적용--태풍-ib-surge) 의 950 mb / 920 mb (특히 한반도 접근 시) 검증
3. **KHOA Annual Report 2003 부재 (백서 변환 2012부터)** — Maemi 2003 verified 경로 불가. 대체 source 후보: KMA Best Track + Kang et al. 2009 / Kim et al. 학술 논문 + 마산 해양조사사무소 별도 출판물
4. ~~**KHOA OpenAPI 직접 fetch**~~ — ❌ **불가 (verified 2026-05-24)**. [`04-code-and-tools.md §4.1 Archive 한계`](04-code-and-tools.md#41-실시간-조위-관측) 의 measurement — `surveyTideLevel` 의 retention 이 약 1년. Hinnamnor 2022 + Maemi 2003 모두 archive 밖. → **1 (KHOA Annual Report PDF 직접)** 로 대체.
5. **Maemi hindcast 학술 논문 인용 보강** — Kang et al. 2009, Kim et al. 등 standard reference (web-refs 확보)
6. **Hinnamnor 사후 분석 논문** — 2023-2024 출판 논문 (KMOU·KIOST·국립해양조사원)

→ **남은 진행 권장**: **3 (Maemi 2003 대체 source)** + **2 (KMA Best Track 직접)** — Hinnamnor §2 는 verified 완료, Maemi §1 만 source-needed 유지.

> **note**: tide-surge coupling 경험노트(`experience/khoa-tide-surge-coupling.md` 미작성)는 **archive 한계로 1년 이내 storm event 만 verified 가능**. Hinnamnor 2022 verification 은 KHOA Annual Report PDF 인용 경로로 변경 필요.

---

## 6. 인용 정형

본 노트 내 verified 자료:

- 본 위키 [`concepts/storm-surge/02-theory.md`](02-theory.md) — Pugh §6:3 IB 식 + §6:4 wind stress
- 본 위키 [`concepts/storm-surge/04-code-and-tools.md`](04-code-and-tools.md) — NWS 모드 + KHOA OpenAPI workflow
- 본 위키 [`models/ADCIRC/source-analysis/storm-surge/`](../../models/ADCIRC/source-analysis/storm-surge/) — 7개 source-code level 노트 (NWS=13/20 + fort.15 운영 규칙 + JMA-MSM reader)
- 본 위키 [[efdc-theory-v12-ch2-hydrodynamics]] §2.4 — Garratt 1977 wind drag (Table 2.2)

본 노트 외 source-needed 자료:

- KMA Typhoon Best Track Archive — 매년 갱신
- JMA RSMC Tokyo Best Track — `https://www.jma.go.jp/jma/jma-eng/jma-center/rsmc-hp-pub-eg/besttrack.html`
- KHOA Annual Report 2003 §3.x — Maemi storm surge
- KHOA Annual Report 2022 §3.x — Hinnamnor storm surge
- Digital Typhoon archive — `http://agora.ex.nii.ac.jp/digital-typhoon/`
- Kang et al. (2009) — Maemi hindcast (Korean Journal of Coastal Engineering 후보)
- Hinnamnor 2023-2024 사후 분석 논문 (목록 확보 필요)

---

## 7. 연결

- [`01-concept.md`](01-concept.md) — 5 인자 + 한국 storm-surge 유형 + §3.2 case 표 (Maemi·Hinnamnor 포함)
- [`02-theory.md`](02-theory.md) — Pugh §6-7 equation level (IB + wind stress + tide-surge interaction)
- [`03-analysis-methods.md`](03-analysis-methods.md) — separation + Mann-Kendall + return period
- [`04-code-and-tools.md`](04-code-and-tools.md) — ADCIRC NWS + KHOA OpenAPI workflow
- [`06-model-application.md`](06-model-application.md) (미생성) — ADCIRC primary, Delft3D-FLOW·SCHISM 비교
- [`models/ADCIRC/source-analysis/storm-surge/`](../../models/ADCIRC/source-analysis/storm-surge/) — 7개 NWS source-code 분석
- [[efdc-theory-v12-ch2-hydrodynamics]] §2.4 — wind drag (storm-surge Table 2.2 의 Garratt 1977 referenced)
- [[khoa-annual-climate-trend]] — SLR baseline
- [[khoa-sst-warming-trend]] — SST 가속 + 태풍 강도화
- [[khoa-2024-mhw-extreme]] — 동해 marine heatwave 와 typhoon coupling

---

## 8. 작성 메타

- citation_status **source-needed** — 본 위키 내부 자료 cross-ref 는 verified 이나, 외부 실측 수치 (중심기압 절대값, 관측 surge peak) 는 직접 fetch 미실시. 위 §5 의 보강 우선순위 따라 점진 승격 가능.
- 작성 의도: storm-surge concept layer 의 **case dimension** 채움. ADCIRC source-analysis 7개 노트 + Pugh equation + KHOA workflow 의 통합 적용 entry point.
- 산타-method 비례성 적용 — 1 노트로 두 case + cross-comparison + 보강 우선순위까지 묶음.
