---
title: "Storm Surge 분석법 — tide-surge separation + Mann-Kendall trend + return period (Pugh §6:1, §7:8, §8:3:2-3)"
topic: storm-surge
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "Pugh 'Tides, Surges and Mean Sea-Level' (textbook/md/sea-level.md, source_id: sea-level) §6:1 non-tidal residual 정의 (line 7026-7030), §7:8 Tide-surge interaction (line 9013-9080), §8:3:2 Annual maxima ranking (line 9328-9510), §8:3:3 Joint tide-surge probability eq (8:5) convolution integral (line 9580-9660). Mann-Kendall trend test 는 [`concepts/sst/03-analysis-methods.md`](../sst/03-analysis-methods.md) §1:2 canonical (Mann 1945, Kendall 1948) 인용 + surge residual 시계열 적용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — Pugh 본문 직접 인용 + Mann-Kendall 은 sst/03 canonical cross-ref"
verification_date: 2026-05-24
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - concepts/sst/03-analysis-methods.md
  - concepts/tides/03-analysis-methods.md
---

# Storm Surge 분석법

> [`02-theory.md`](02-theory.md) 의 dynamics 를 관측 시계열에서 추출·분석하는 절차. 4 단계: **(1) tide-surge separation → (2) interaction 진단 → (3) trend 검정 → (4) return period 추정**.

## 1. Tide-surge separation (Pugh §6:1)

### 1.1 정의 — non-tidal residual

관측 sea-level $\eta_{\text{obs}}(t)$ 을 두 성분으로 분해:

$$\eta_{\text{obs}}(t) = T(t) + S(t)$$

- $T(t)$ = 조화 분석으로 예측된 천문조 (predicted tide, [`concepts/tides/03-analysis-methods.md`](../tides/03-analysis-methods.md))
- $S(t)$ = **non-tidal residual** = 폭풍해일 + 기타 비조석 성분

> "the non-tidal residual ... as the difference between the observed and predicted levels" (Pugh §6:1, textbook/md/sea-level.md line 7028-7030)

대안 명칭: **non-tidal component**, **meteorological residual**, **set-up** (Pugh §6:1 line 7032).

### 1.2 절차

1. **장기 관측 시계열** 수집 (보통 1년+, 정점 별 분석)
2. **조화 분석**: t_tide / UTide 등으로 amplitude·phase 추정 → predicted tide 재합성
3. **잔차 계산**: $S(t) = \eta_{\text{obs}}(t) - T(t)$
4. **시각 검토**: 잔차에 다음 패턴이 보이면 separation 오류 (Pugh Figure 2:14):
   - 일정한 timing drift (e.g., 시계 20분 누적 오차)
   - datum shift (0.5 m 등 step)
   - daily trace misidentification

### 1.3 한계 — interaction caveat

> "This definition is adequate for most purposes but requires a further term to allow for interaction between tide and surge where this is important (see Section 7:8)" (Pugh §6:1, line 7030)

천해 (북해 남부, 한국 서해) 에서는 §2 의 interaction 보정 필요.

## 2. Tide-surge interaction 진단 (Pugh §7:8)

### 2.1 (T+S)² 비선형 결합

bottom friction 처럼 sea-level 의 제곱에 의존하는 process 가 있을 때:

$$C^2 = (T + S)^2 = T^2 + S^2 + 2TS$$

→ $2TS$ 항이 interaction 의 수학적 표현 (Pugh §7:8 line 9015-9020).

### 2.2 진단 — 3 가지 표현

interaction 강도를 데이터에서 확인하는 방법 (Pugh §7:8 line 9070-9080):

1. **Surge amplitude vs tidal phase** — 시간대별 surge 평균을 high water 기준 ±시간으로 plot (Figure 7:13 형식)
2. **Surge 표준편차 vs tidal level** — Pugh 의 Southend 예: mid-tide σ=0.27 m, mean high water σ=0.19 m, mean low water σ=0.18 m → interaction 존재 신호
3. **Observed surge vs tidal level scatter** — 회귀 기울기가 0 이 아니면 interaction

### 2.3 Southend 사례 — interaction 의 100yr return 영향

> "the interaction reduces the 100-year return level at Southend by 0.5 m, which is highly significant for the design of coastal defences against flooding (Pugh and Vassie, 1980)" (Pugh §7:8 line 9035-9040, textbook/md/sea-level.md line 9035)

→ interaction 무시 시 design level **0.5 m 과대 추정** (Southend, 영국).

### 2.4 한국 서해 적용

한국 서해 (인천·군산) 는 천해·대조차 → 북해 남부와 dynamics 유사. 본 분석 패러다임 적용 가능 (개별 case study 는 [`concepts/storm-surge/05-examples.md`](05-examples.md) (예정) 에 위임).

## 3. Trend 검정 — Mann-Kendall (canonical: concepts/sst/03)

### 3.1 표준 절차 reference

Mann-Kendall 비모수 trend test (Mann 1945, Kendall 1948) 의 정의·통계량·다중계절 (Hirsch et al. 1982) 확장 + Sen's slope (Sen 1968) 모두 [`concepts/sst/03-analysis-methods.md §1:2`](../sst/03-analysis-methods.md) canonical 인용. 본 §는 storm-surge residual 시계열 적용만.

### 3.2 Storm surge climate 적용 변수

| 변수 | 정의 | 시계열 길이 |
|---|---|---|
| **연 최대 surge** $S_{\max,y}$ | 매년 non-tidal residual peak | n ≥ 30 권장 |
| **연 평균 surge 분산** $\sigma^2_{S,y}$ | residual 의 yearly variance | n ≥ 25 |
| **극값 빈도** $N_{S > \tau, y}$ | 임계값 $\tau$ (e.g., 1m) 초과 시간 | n ≥ 25 |

### 3.3 한국 적용 주의

KHOA Annual Report 의 연도별 이상조위 빈도 (Annual Report 2012-2025) 는 Mann-Kendall 분석 가능 자료. 단 시계열 길이 (대부분 ~13년) 가 강한 trend 검출에는 짧음 — 30 년+ 시계열은 인천·부산 등 장기 정점 한정.

## 4. Return period — Annual maxima ranking (Pugh §8:3:2)

### 4.1 절차

> "tabulate the maximum values reached in as many years as possible (NERC, 1975). Seasonal cycles in extreme levels make the use of sample periods shorter than a year invalid." (Pugh §8:3:2 line 9330)

1. 연 최대 sea-level $\eta_{\max,y}$ 를 $M$ 년 수집
2. 오름차순 정렬: $\eta_1 \le \eta_2 \le \dots \le \eta_M$
3. rank $r$ 의 비초과확률 $P(\eta \le \eta_r)$ 추정 (Pugh eq, line 9416):

$$P = \frac{2r - 1}{2M}$$

4. probability paper plot → 외삽으로 100-yr level $\eta_{100}$ 추정

### 4.2 데이터 요건

> "at least 25 values are needed for a satisfactory analysis" (Pugh §8:3:2 line 9510)

10 년으로도 가능하지만 25 년+ 권장.

### 4.3 Trend 사전 보정

> "trends, which may be due to changes in mean sea level, tidal ranges or the intensity of meteorological surges, may be removed before the ranking analysis begins. The annual maxima should be trend-adjusted to some common year" (Pugh §8:3:2 line 9508)

→ Mann-Kendall 로 trend 검출 후 SLR 제거 → 공통 기준연도로 normalize → ranking.

### 4.4 한계

> "If the largest meteorological surge for the year coincides with a low tidal level, the information is ignored despite its obvious relevance to the problem of estimating extreme level probabilities" (Pugh §8:3:2 line 9510-9515)

→ 데이터 낭비 (1 년 = 1 statistic). §5 의 joint probability 가 보완책.

## 5. Return period — Joint tide-surge probability (Pugh §8:3:3)

### 5.1 Convolution integral

tide $T$, surge $S$, total level $\eta$ 의 확률밀도함수를 각각 $D_T(\eta)$, $D_S(\eta)$, $D_0(\eta)$ 라 하면 (Pugh eq 8:5, line 9605):

$$D_0(\eta) = \int_{-\infty}^{\infty} D_T(\eta - y) \cdot D_S(y) \, dy$$

→ tide·surge 확률 분포의 **convolution** = total level 확률 분포.

**가정**: tide·surge 가 통계적 독립. interaction 존재 시 (§2.3 Southend) $D_S$ 가 tidal level 의존 함수로 확장 (Pugh and Vassie 1980).

### 5.2 데이터 요건

- **Tide**: 18.6 년 (nodal 주기 1 완전 사이클) tidal prediction 권장 (Pugh §8:3:3 line 9603)
- **Surge**: 1 년+ residual 관측 (4 년+ 권장, line 9636)
- hourly resolution 으로 0.1 m class 양자화

### 5.3 Return period 변환

dimensionless 확률 $P$ → return period $T_R$ (시간 단위) (Pugh line 9627):

$$T_R[\text{hours}] = 1/P$$

→ 100-yr return level 은 $\log_{10}(P) = -5.94$ 의 contour (Pugh line 9628).

### 5.4 장점 (Pugh line 9632-9650)

1. **짧은 관측으로도 stable** — 1 년부터 결과, 4 년이 desirable minimum
2. **데이터 낭비 없음** — annual maxima 와 달리 모든 시간 사용
3. **외삽 불필요** — Newlyn 예 (18 년 데이터, Figure 8:5)
4. **저수위 확률도 자동 산출** — datum design 에 사용
5. **변경 시나리오 incorporate 가능** — 방조제 신설 시 $D_T$ 만 갱신
6. **SLR 추가는 단순 덧셈**

### 5.5 단점 (Pugh line 9651-9660)

(a) 데이터 품질 요구 (timing accuracy < 수 분, 아니면 tidal residual 오염)
(b) 추가 계산 비용
(c) interaction 무시 시 약간 과대 추정 (§2.3)

## 6. 방법 선택 — annual maxima vs joint probability

| 항목 | Annual maxima (§4) | Joint probability (§5) |
|---|---|---|
| 최소 데이터 | 25 년 | 1-4 년 |
| 외삽 의존 | 강 | 약 |
| 데이터 낭비 | 큼 (1년 = 1점) | 없음 |
| 저수위 분석 | 별도 작업 | 동시 산출 |
| Interaction 처리 | trend 보정만 | $D_S$ 확장 가능 |
| 계산 비용 | 낮음 | 중 |
| 한국 적용 권장 | 인천·부산 (50년+) | KHOA 신규 정점 (5-15년) |

### 6.1 보완 (Pugh line 9665-9680)

- 둘 다 **outside the tropics** 효과적 — 한국 태풍 surge 처럼 rare extreme tropical event 는 modeling approach (numerical hindcast + Monte Carlo) 가 적절
- Smith (1984) — POT (peaks-over-threshold) 분석 방법
- Middleton and Thompson (1986) — exceedance probability 방법 (surge 가 tide 보다 dominant 한 경우)

## 7. 한국 적용 워크플로 (4-단계 통합)

| 단계 | 도구 | 산출 |
|---|---|---|
| **1. Separation** | UTide / t_tide → KHOA 조위 관측 분해 | $T(t)$, $S(t)$ |
| **2. Interaction 진단** | $S$ 의 surge-vs-tidal-level scatter | 한국 서해 정점 interaction 존재 여부 |
| **3. Trend** | Mann-Kendall on annual $S_{\max}$ ([`concepts/sst/03`](../sst/03-analysis-methods.md)) | SLR + storm climate trend |
| **4. Return period** | Joint probability (5-15년 KHOA) 또는 annual maxima (인천 50년+) | 100-yr design level |

도구 상세 — [`04-code-and-tools.md`](04-code-and-tools.md) (현재 ADCIRC NWS 운영 중심).

## 8. 인용 정형

본 §의 핵심 인용 (source_id: sea-level = Pugh 'Tides, Surges and Mean Sea-Level'):

- $\eta_{\text{obs}} = T + S$ → non-tidal residual 정의 — Pugh §6:1 (line 7026-7030)
- $(T+S)^2 = T^2 + S^2 + 2TS$ → interaction 항 — Pugh §7:8 (line 9015)
- Southend 100-yr level 0.5 m 감소 — Pugh & Vassie 1980, Pugh §7:8 (line 9035)
- $P = (2r-1)/(2M)$ ranking — Pugh §8:3:2 (line 9416)
- 25-year minimum, trend pre-adjustment — Pugh §8:3:2 (line 9508-9510)
- Convolution eq (8:5): $D_0 = \int D_T \cdot D_S$ — Pugh §8:3:3 (line 9605)
- $T_R[\text{hr}] = 1/P$, $\log_{10}P = -5.94$ → 100-yr — Pugh §8:3:3 (line 9627-9628)
- Mann-Kendall canonical — [`concepts/sst/03-analysis-methods.md §1:2`](../sst/03-analysis-methods.md)

## 9. 관련 문헌

- **Pugh, D.T.** *Tides, Surges and Mean Sea-Level: A Handbook for Engineers and Scientists*. (source_id: sea-level)
- **Pugh, D.T. & Vassie, J.M.** (1980) — extended joint probability for Southend (Pugh §7:8, §8:3:3 references)
- **NERC (1975)** — annual maxima method standard reference (Pugh §8:3:2)
- **Mann, H.B.** (1945) Econometrica 13:245-259 — Mann-Kendall test (canonical in [`concepts/sst/03`](../sst/03-analysis-methods.md))
- **Kendall, M.G.** (1948) *Rank Correlation Methods* — companion ref
- **Hirsch, R.M., Slack, J.R., & Smith, R.A.** (1982) Water Resour. Res. 18:107-121 — Seasonal MK (canonical in [`concepts/sst/03`](../sst/03-analysis-methods.md))
- **Sen, P.K.** (1968) JASA 63:1379-1389 — Sen's slope (canonical in [`concepts/sst/03`](../sst/03-analysis-methods.md))
- **Smith, R.L.** (1984) — POT 분석 (Pugh §8:3:3 reference, line 9670)
- **Middleton, J.F. & Thompson, K.R.** (1986) — exceedance probability (Pugh §8:3:3, line 9672)

### 9.1 연구 문헌 (research/inbox promote, source-needed)

- **White, B.N., Blanton, B., Luettich, R., Smith, R.L.** (2026) "Fusing Sparse Observations and Dense Simulations for Spatial Extreme Value Analysis: Application to U.S. Coastal Sea Levels" arxiv:[2603.03247](https://arxiv.org/abs/2603.03247) — **GEV(비정상 location) + LMC(linear model of coregionalization) 2-stage frequentist** 로 NOAA 조위 29 + ADCIRC 100 sites 융합, US 연안 해수면 1979-2021 100년 return level. cross-source 상관(공간 interspersed network, co-located 불요)이 정보전달 기제. LOO-CV 에서 gauge-only 대비 RMSE **35% 감소**, block-CV 로 공간외삽서도 이득 지속. R 패키지 `evfuse`. → 본 §3-5 return period 방법론의 **관측-시뮬 융합 확장**. citation_status: source-needed.

## 10. 연결

- [`01-concept.md`](01-concept.md) — 5 인자 정성
- [`02-theory.md`](02-theory.md) — shallow-water + IB + wind stress equation
- [`04-code-and-tools.md`](04-code-and-tools.md) — ADCIRC NWS modes + KHOA OpenAPI 운영 (verified)
- [`05-examples.md`](05-examples.md) (예정) — 한국 태풍 case study
- [`concepts/tides/03-analysis-methods.md`](../tides/03-analysis-methods.md) — 조화 분석 (separation step 1)
- [`concepts/sst/03-analysis-methods.md`](../sst/03-analysis-methods.md) — Mann-Kendall canonical
- [`experience/khoa-annual-climate-trend.md`](../../experience/khoa-annual-climate-trend.md) — Korean SLR + surge climate trend
