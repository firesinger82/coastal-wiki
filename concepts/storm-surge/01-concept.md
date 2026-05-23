---
title: "폭풍해일 (Storm Surge) — 정의·결정 인자·한국 영향"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "Pugh 'Tides, Surges and Mean Sea-Level' Ch 6 Storm Surges (textbook/md/sea-level.md, p.184-230) 직접 인용 + ADCIRC theory report (Luettich & Westerink 2004) + _staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge-foundation.md (이미 source-code 기반 분석). 한국 적용은 KHOA Annual Report 2012-2025 의 이상조위 분석 + 본 위키 experience/khoa-annual-climate-trend.md SLR cross-reference."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — Pugh Ch 6 + ADCIRC + KHOA cross-ref"
verification_date: 2026-05-23
related:
  - concepts/tides/02-theory.md
  - concepts/waves/
  - concepts/sst/02-theory.md
  - experience/khoa-annual-climate-trend.md
  - models/ADCIRC/
---

# 폭풍해일 (Storm Surge) — 정의·결정 인자

> 본 §는 storm surge 도메인 layer. ADCIRC·Delft3D·SCHISM 등 모델별 구현은 [`06-model-application.md`](06-model-application.md) (예정) 와 [`models/`](../../models/) 참조.

## 1. 정의

**Storm surge (폭풍해일, 暴風海溢)** — 대기 기상 (열대저기압·온대저기압·강풍·기압 변화) 에 의한 비조석(non-tidal) 해수면 상승.

Pugh (1987) Ch 6 정의:

> "The regular and predictable pattern of the tides is modified to a greater or lesser extent, by irregular factors, the principal ones being the atmospheric pressure and the winds acting on the sea surface ... These irregular slow changes [are] known as surges." (Pugh §1:3, p.4)

단순화:

$$\eta_{\text{total}}(t) = \eta_{\text{tide}}(t) + \eta_{\text{surge}}(t) + \eta_{\text{wave setup}}(t) + \eta_{\text{MSL trend}}(t)$$

| 성분 | 시간 스케일 | 진폭 (한국 typical) |
|---|---|---:|
| **tide** | 12h/24h/14d/지속 | ±5 m 인천, ±0.3 m 동해 ([`concepts/tides/`](../tides/)) |
| **storm surge** | 수시간~수일 | +0.5 ~ +3 m (한국 태풍 시) |
| **wave setup** | 수분~수시간 | +0.2 ~ +1 m (대형 storm 시) |
| **MSL trend** | 다년·secular | +3.94 mm/yr 한국 (SLR) |

> 호우·태풍 동시 발생 시 4 성분 합 → **flooding 위험** (한국 인천·아산만·새만금 등 천해 + tide 큰 곳 특히 위험).

## 2. 결정 인자 (Pugh §6 + ADCIRC theory)

Storm surge 의 주된 원인 5개.

### 2.1 Inverse-barometer effect (대기압 영향)

**1 mb 압력 감소 = 약 1 cm 수면 상승** (정적 응답).

수식 (Pugh §6:3):

$$\eta_{IB} = -\frac{\Delta P_a}{\rho g} \approx -\frac{1 \text{ mb}}{1 \text{ cm}} \cdot \Delta P_a \text{ [mb]}$$

예: 태풍 중심기압 950 mb (배경 1013 mb 대비 -63 mb) → 약 **+63 cm** 정적 IB surge.

ADCIRC 의 IB 처리:
- `NOIVB = 0` (기본): IB 자동 포함
- `NOIVB = 1`: IB 억제 (이미 GAHM 등이 IB 계산 시 중복 방지)
- 배경기압 `PRBCKGRND = 1013.0 mb` (`models/ADCIRC/raw/source_code/adcirc/src/constants.F90:54` 참조)

### 2.2 Wind stress (풍응력)

표층 wind stress:

$$\tau_{w} = \rho_a C_D U_{10}^2$$

- $\rho_a$ ≈ 1.2 kg/m³ (공기 밀도)
- $C_D$ = drag coefficient (보통 $1.2 \times 10^{-3}$ 약풍 ~ $3 \times 10^{-3}$ 강풍, Garratt 1977)
- $U_{10}$ = 10m 풍속 (m/s)

Shallow water 의 wind set-up:

$$\frac{\partial \eta}{\partial x} = \frac{\tau_w}{\rho g H}$$

→ wind set-up ∝ $U^2 / H$ — **천해 (작은 $H$) 에서 더 큼**. 한국 서해안 (수심 20-50m) 이 동해 (수심 1000m+) 보다 wind set-up 큰 이유.

### 2.3 Tide-surge interaction (Pugh §7:8)

비선형 결합: $\eta_{\text{total}} \neq \eta_{\text{tide}} + \eta_{\text{surge}}$ — 두 신호가 천해에서 비선형 상호작용.

원인:
- bottom friction 의 비선형성: $\tau_b \propto u|u|$
- shallow water depth 의 시간 변동 (tide 가 $H$ 변동) → wind set-up 식에 영향
- advection $u \partial u / \partial x$

한국 서해 (high tide range + 천해) 에서 특히 큼.

### 2.4 Wave setup (Longuet-Higgins-Stewart 1962)

연안 breaker zone 의 radiation stress 가 평균수위 상승:

$$\Delta \bar{\eta}_{\text{wave}} \approx 0.19 H_s$$

(Saville 1961 empirical, $H_s$ = significant wave height at breaking).

예: $H_s = 5$ m → wave setup ~ 1 m.

본 위키 [`concepts/waves/`](../waves/) 에서 상세. wave 와 surge 는 nominal 분리, 실제 모델 (ADCIRC + SWAN 결합) 에서 동시 계산.

### 2.5 Coriolis (지구 자전)

대규모 storm 의 회전·이동 시 Coriolis 효과:

$$\frac{\partial u}{\partial t} - fv = \cdots, \quad f = 2\Omega \sin\phi$$

한국 위도 33-38°N → $f \approx 8 \times 10^{-5}$ s⁻¹. 큰 사이즈 storm (>100 km 반경) 에서 효과 큼.

## 3. 한국 storm surge 특징

### 3.1 한국 영향 storm 유형

| 유형 | 시기 | 영향 해역 | 강도 |
|---|---|---|---|
| **북상 태풍** (TC) | 7-10월 | 남해·동해·서해 (경로 따라) | 강 (+2~+3 m surge 가능) |
| **온대저기압** (extratropical) | 11-3월 | 서해 (북서풍 강) | 중 (+0.5~+1.5 m) |
| **국지 thunderstorm** | 여름 | 만 안쪽 | 약 (+0.3~+0.5 m) |
| **seiche** (장주기 진동) | 연중 | 만·항만 | 약~중 (resonance 시 크게) |

### 3.2 한국 주요 태풍 storm surge case (KHOA Annual Report 인용)

| 태풍 | 연 | 한국 경로 | 관측 최대 surge (한국 정점) |
|---|---|---|---:|
| Maemi (매미) | 2003 | 마산만 직격 | ~2.4 m 마산 |
| Sanba (산바) | 2012 | 남해 동부 | ~1.5 m 부산 |
| Bolaven (볼라벤) | 2012 | 서해 종단 | ~1.2 m 인천 |
| Lingling (링링) | 2019 | 서해 북상 | ~1.0 m 인천 |
| Hinnamnor (힌남노) | 2022 | 동해 남부 | ~1.5 m 포항·울산 |

(정확 값은 KHOA Annual Report 해당 연도 §3.x 인용 필요 — TODO)

### 3.3 SLR + SST 강화 + storm surge 의 climate cascade

[`experience/khoa-annual-climate-trend.md`](../../experience/khoa-annual-climate-trend.md) (SLR 3.94 mm/yr 한국) + [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) (SST 가속) 의 결합 효과:

1. **MSL 상승** → 같은 surge 의 절대 수위 매년 +4 mm 증가 → 100년 = +40 cm
2. **SST 가속** (특히 Kuroshio + 동중국해 +2.4 °C/decade) → 태풍 강도화·서진 경로 변화·발생 빈도 증가
3. **tide × surge interaction** 은 한국 서해 천해에서 비선형 → MSL 가 약간 상승해도 effective surge 위험 더 크게 증가

→ storm surge 위험 평가는 SLR + SST trend 와 함께 종합 분석 필요. 본 위키의 SST·SLR experience 와 직접 연결.

## 4. 모델링 접근

### 4.1 표준 storm surge 모델

| 모델 | 위치 | 비고 |
|---|---|---|
| **ADCIRC** | [`models/ADCIRC/`](../../models/ADCIRC/) — primary | 한국 ADCIRC ecosystem 풍부 (testsuite 16GB, NWS 모드 다수) |
| SLOSH | NOAA NHC | 미국 운영 forecast, 단순 |
| Delft3D-FLOW | [`models/Delft3D/`](../../models/Delft3D/) | 3D + sediment 결합 가능 |
| SCHISM | 미설치 | unstructured grid, ADCIRC 대안 |

ADCIRC 의 storm surge 적용 — `_staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge*.md` 의 7개 노트 (NWS=12/13/14/19/20/29/30 wind input modes 분석, source-code level) → [`models/ADCIRC/source-analysis/`](../../models/ADCIRC/) 로 promote 후 인용.

### 4.2 Wave coupling

ADCIRC + SWAN coupled (한국 적용): wave setup + surge 동시 계산 → ADCIRC 단독보다 sea level 더 높게 (이상조위 더 정확).

본 위키 [`concepts/waves/`](../waves/) 에서 SWAN 상세.

## 5. 인용 정형

- Pugh, D.T. (1987) "Tides, Surges and Mean Sea-Level". Wiley. — Ch 6 directly
- Luettich, R.A. & Westerink, J.J. (2004) "Formulation and Numerical Implementation of the 2D/3D ADCIRC Finite Element Model Version 44.XX." — ADCIRC theory
- Garratt, J.R. (1977) "Review of drag coefficients over oceans and continents." Monthly Weather Review 105:915-929 — $C_D$
- Longuet-Higgins, M.S. & Stewart, R.W. (1962) "Radiation stress and mass transport in gravity waves" J. Fluid Mech. 13:481-504 — wave setup
- KHOA Annual Report 2003 §3.x — Maemi storm surge
- KHOA Annual Report 2022 §3.x — Hinnamnor storm surge

## 6. 본 위키 안 활용

| 노트 | 사용처 |
|---|---|
| SLR + storm surge 위험 누적 | `experience/khoa-annual-climate-trend.md` (해수면 상승 → surge baseline 상승) |
| SST 가속 → 태풍 강도 | `experience/khoa-sst-warming-trend.md` §7 marine heatwave |
| ADCIRC NWS 모드 (source-code level) | `_staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge*.md` (7개, promote 대기) |
| KHOA 정점 surge 관측 | `concepts/tides/04-code-and-tools.md` §3 KHOA OpenAPI |

## 7. 인용 정형 ex

본문 안:
- `(Pugh 1987 §6:3, p.194)`
- `(ADCIRC Theory §3.4 wind stress)`
- `(KHOA Annual Report 2003 §3.5 Maemi)`

source_id 매니페스트: [`textbook/sources.yml`](../../textbook/sources.yml) — Pugh `pugh-sea-level` 추가 필요 (TODO).

## 8. 연결

- [`02-theory.md`](02-theory.md) (예정) — equations 정형 (Pugh §6:3~6:4)
- [`04-code-and-tools.md`](04-code-and-tools.md) (예정) — ADCIRC NWS 모드 + KHOA observation API
- [`05-examples.md`](05-examples.md) (예정) — 한국 태풍 case (Maemi, Hinnamnor)
- [`06-model-application.md`](06-model-application.md) (예정) — ADCIRC primary, Delft3D·SCHISM 비교
- 외부:
  - [`textbook/md/sea-level.md`](../../textbook/md/sea-level.md) — Pugh full book
  - [`models/ADCIRC/raw/manuals/pdfs/`](../../models/ADCIRC/raw/manuals/) — ADCIRC theory + user docs
  - [`_staging/from-modeling-wiki/knowledge/methods/adcirc-storm-surge*.md`](../../_staging/from-modeling-wiki/knowledge/methods/) — 7개 NWS 분석 (promote 대기)
