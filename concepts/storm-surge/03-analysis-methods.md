---
title: "Storm Surge 분석법 — tide-surge separation + Mann-Kendall trend + return period (Pugh §6:1, §7:8, §8:3:2-3)"
topic: storm-surge
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "Pugh 'Tides, Surges and Mean Sea-Level' (textbook/md/sea-level.md, source_id: sea-level) §6:1 non-tidal residual 정의 (line 7026-7030), §7:8 Tide-surge interaction (line 9013-9080), §8:3:2 Annual maxima ranking (line 9328-9510), §8:3:3 Joint tide-surge probability eq (8:5) convolution integral (line 9580-9660). Mann-Kendall trend test 는 [`concepts/sst/03-analysis-methods.md`](../sst/03-analysis-methods.md) §1:2 canonical (Mann 1945, Kendall 1948) 인용 + surge residual 시계열 적용. **§9.1 full PDF 격상 (2026-09-22)**: arXiv:2603.03247v1 (White·Blanton·Luettich·Smith, 2026-03-03 [stat.ME], 29p) **전문 직접 fetch·판독**(curl + pdftotext) — abstract-level `source-needed` 스텁을 §9.1.1~9.1.4 로 확장. verbatim 인용: §2.1 계측기 고장→$\hat\xi$ 하향편향 동기(+자료 필터 90%·20년, $L_N$=29), §2.2-2.3 ADCIRC 100점 CFSR 강제·공위치 0·최근접 중앙값 21.7 km, §2.4 Mann-Kendall 19/29(66%)·Sen 4.6 mm/yr vs 1/100·0.4 mm/yr + CFSR 에 SLR 부재 원인 명시, §4.2 식(14) 자료원간 상관 0.995/0.837/0.443 + 범위모수 2873~188 km, §4.3-4.4 SE 비 1.34(대서양)/0.92(멕시코만)/전체 1.17·24%>1.5·ADCIRC-only 계통 과소, §4.5 block CV 18%(29점)·36%(25점)·**log-scale 역전 0.298→0.406**, §5.4 저자 자기제한(shape 상관 0.84 불확실). ★**정직 재구성**: 초록 머리 숫자 LOO-CV 35% 와 block CV 18% 를 구분 표기하고, 융합이 모든 모수를 개선하지 않는다는 저자 경고를 본문에 올렸다. ★**Pugh 와의 연결**: §8 이 이미 인용하던 [sea-level] line 9508(극값이 기록계를 파손한 결측의 위험)이 본 논문의 융합 동기와 동일 문제 — 본 노트 내부 대조로 확인. 잔존 source-needed = 한국 적용 조건 미조사·`evfuse` 미실행·max-stable/계층Bayes 계열 미판독(§9.1.4 disclosed)."
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

### 9.1 관측-시뮬레이션 융합 EVA — White et al. (2026) ✅ verified (full PDF 판독 2026-09-22)

**White, B.N., Blanton, B., Luettich, R., Smith, R.L.** (2026) "Fusing Sparse Observations and
Dense Simulations for Spatial Extreme Value Analysis: Application to U.S. Coastal Sea Levels",
arXiv:[2603.03247](https://arxiv.org/abs/2603.03247)v1 [stat.ME], 2026-03-03.
UNC Chapel Hill 통계학과 + RENCI + 해양과학연구소. R 패키지 `evfuse` 공개.

본 §3–5 가 세운 **단일 정점 return period 방법론의 공간 확장**이다. 위키 접점이 둘이라 전문을 읽었다 —
ADCIRC 가 자료원으로 쓰이고([[04-code-and-tools]]), Mann-Kendall 이 전처리 진단으로 쓰인다(§6).

#### 9.1.1 문제 — 두 자료원의 약점이 반대다

| | NOAA 조위계 29점 | ADCIRC 모의 100점 |
|---|---|---|
| 밀도 | 성김 | 촘촘(6,000 km 연안) |
| 기록 | 34–43 연최대치 (90% 결측 필터 + 최소 20년) | **43년 전부 완비**(설계상 결측 없음) |
| 성격 | 직접 관측 | **모델 물리의 산물** |
| 추세 | **19/29(66%) 유의 양의 추세**, Sen 기울기 중앙값 4.6 mm/yr | 1/100 유의(=우연 수준), 중앙값 0.4 mm/yr |
| 치명 약점 | **극값 시 계측기 고장 → 최대치 검열 → $\hat\xi$ 하향 편향** | **CFSR 재해석 강제에 장기 해수면 상승이 없다** |

> ★ **40년 간격의 같은 경고.** Pugh 가 §8:3:2 에서 *"결측 연도가 극값 자체 때문이면 — 예컨대 매우 심한
> 극값이 기록계를 파손한 경우 — 결과의 타당성이 무너진다"* 고 적은 바로 그 문제를, 이 논문이
> **융합의 동기**로 다시 든다: *"simulations are not subject to instrument failure, and the cross-source
> shape correlation in Stage 2 can mitigate such bias."*[^wh-motive] 같은 문헌이 이미 본 노트 §8 의
> 인용 정형에 들어 있다(line 9508-9510) — **경고가 방법론이 된 사례**다.

추세 비대칭도 그 자체로 읽을 거리다. ADCIRC 쪽 추세가 거의 0 인 것은 모델 결함이 아니라
**강제자료에 SLR 이 들어 있지 않기 때문**이라고 저자들이 명시한다.[^wh-trend]
즉 **재해석 강제 hindcast 의 극값 통계에는 해수면 상승이 빠져 있다** — 설계 적용 시 별도 가산이 필요하다.

#### 9.1.2 2단계 구조

- **Stage 1** — 129개 지점 각각에 GEV 독립 적합. 추세가 있는 곳은 **비정상 location**(연도 선형, 2000년 절편 $\hat\mu_0$).
  전처리 진단은 **Mann-Kendall + Sen 기울기**(본 노트 §6 과 동일 도구, [`sst/03`](../sst/03-analysis-methods.md) canonical).
- **Stage 2** — Stage 1 의 모수 추정치 전체를 **선형 공동지역화 모형(LMC)** 의 고차원 공간과정으로 함께 모형화.
  자료원 간 상관이 정보를 옮기는 기제이고, 가능도의 해석적 gradient 로 계산을 감당한다.

핵심 설계는 **공위치(co-located) 지점이 필요 없다**는 것이다. 129점 중 두 자료원이 겹치는 지점은 **0개**이고,
NOAA–ADCIRC 최근접거리 중앙값 **21.7 km**(범위 1.9–119.8 km)로 두 망이 공간적으로 섞여 있다.
이 섞임 자체가 자료원 간 상관을 식별 가능하게 한다.[^wh-design]

추정된 자료원 간 상관은 모수마다 크게 다르다 — $\mathrm{Cor}(\mu_N,\mu_A)=0.995$,
$\mathrm{Cor}(\xi_N,\xi_A)=0.837$, $\mathrm{Cor}(\log\sigma_N,\log\sigma_A)=0.443$.[^wh-cor]
location 이 거의 완전 상관이라 **100개 모의점이 사실상 29점 관측망을 조밀화**하고,
shape 상관이 중요한 이유는 $\xi$ 가 **가장 부정확하게 추정되면서 return level 에 가장 큰 영향**을 주기 때문이다.

#### 9.1.3 결과 — 그리고 정직한 재구성

초록의 머리 숫자는 **LOO-CV 100년 return level RMSE 35% 감소**(gauge-only 대비)다.
전문을 읽으면 그림이 더 갈린다.

| 평가 | 결과 |
|---|---|
| LOO-CV (초록) | 100년 RL RMSE **35% 감소** |
| 지리 block CV, 전 29점 | **18% 감소** (0.665 m vs 0.810 m) |
| block CV, Gulf 4점 제외한 25점 | **36% 감소** (0.496 m vs 0.776 m) |
| **log-scale 모수** | **오히려 악화** — NOAA-only 0.298 vs 융합 0.406 |

★ **융합이 모든 모수를 개선하지 않는다.** log-scale 이 나빠지는 이유를 저자들이 직접 쓴다 —
자료원 간 scale 상관이 0.44 로 중간 수준이라, 공간외삽 상황에서 ADCIRC scale 을 빌려오면
정보가 아니라 잡음이 들어온다. 그래서 *"practitioners should examine per-parameter correlations
before assuming uniform benefit from fusion"* 이라고 못박는다.[^wh-cv]

이득의 **종류**도 지역마다 다르다. 관측이 촘촘한 대서양 연안에서는 **불확실성이 좁아지고**
(SE 비 중앙값 1.34), 성긴 멕시코만에서는 SE 비가 1 근처(0.92)로 **대신 추정값 자체가 위로 옮겨간다** —
ADCIRC 의 두꺼운 꼬리 $\xi$ 가 관측이 성긴 곳에서 $\xi$ 를 끌어올리기 때문이다.
전 연안 SE 비 중앙값은 1.17(융합 쪽 불확실성이 약 85%)이고, 연안의 약 24% 에서 1.5 를 넘는다.
한편 **ADCIRC-only 모형은 관측 기반 추정보다 계통적으로 낮다.**[^wh-geo]

저자들의 자기 제한도 기록해 둔다 — shape 상관 $r=0.84$ 는 현 비공위치 표본설계에서
**불확실성이 커 참값이 상당히 낮을 수 있다**고 스스로 적는다.[^wh-limit]

#### 9.1.4 본 위키 접점과 한계

- **본 §3–5 의 공간 확장** — 단일 정점 GEV·return period 를 연안 전체 지도로 잇는 경로.
- **[[04-code-and-tools]] 의 ADCIRC 가 통계 자료원이 된다** — hindcast 출력이 검증 대상이 아니라 **입력**이다.
- **관측 자료의 층위 문제와 같은 축** — 관측이 성기고 끊긴다는 사실이 방법을 정한다.
  한국 연안 자료의 층위 논의는 [`08-applied-observed-surge-resolution.md`](08-applied-observed-surge-resolution.md)(④응용, **탐색 링크** — 본 절의 근거가 아니다).
- **한국 적용 미검토** `source-needed` — 국내에서 같은 융합을 하려면 KHOA 관측망 + ADCIRC/Delft3D
  hindcast 가 공간적으로 섞여 있어야 한다. 그 조건이 성립하는지는 조사하지 않았다.
- **`evfuse` 미실행** `source-needed` — 패키지 공개 사실만 확인했고 돌려보지 않았다.
- **본 위키는 max-stable·계층 Bayes 계열을 다루지 않는다** `source-needed` — 논문이 비교 대상으로 드는
  Davison et al. 2012·Cooley et al. 2007 계열은 미판독이라 상대 평가를 하지 않는다.

## 9.2 §9.1 출처

[^wh-motive]: White et al. (2026) arXiv:2603.03247v1 §2.1 NOAA Tidal Gauge Observations — *"If tidal gauges fail during extreme events, the resulting censorship of the largest observations would bias ξ̂ downward. This provides additional motivation for fusion: simulations are not subject to instrument failure, and the cross-source shape correlation in Stage 2 can mitigate such bias."* 대응하는 Pugh 의 경고는 [sea-level] §8:3:2(본 노트 §8 이 이미 인용하는 line 9508): *"Missing years of data should not affect the validity of the results provided that the gaps are not due to the extreme values themselves, for example because a very severe extreme level damaged the recording instrument."* 자료 필터는 §2.1 — 연 90% 미만 결측 연도 제외 + 연최대치 20개 미만 관측소 제외 → $L_N=29$, 각 34개 이상(29곳 중 24곳이 40개 초과).
[^wh-trend]: 同 §2.4 Trend Diagnostics — Mann-Kendall(Mann 1945; Kendall 1975) + Sen 기울기(Sen 1968). NOAA 29점 중 **19점(66%)이 p<0.05 유의 양의 추세**, Sen 기울기 중앙값 **4.6 mm/yr**. ADCIRC 100점 중 유의는 1점(*"as expected at α = 0.05"*), 중앙값 **0.4 mm/yr**. 원인 명시: *"the simulations are driven by CFSR reanalysis forcing that does not incorporate long-term sea level rise, so any trends reflect only interannual variability in atmospheric forcing."* 규모 비교도 같은 절 — 4.6 mm/yr × 43년 ≈ 0.2 m vs 100년 return level 1–4 m.
[^wh-design]: 同 §2.2·§2.3 — ADCIRC 는 RENCI(UNC) 가 **CFSR 재해석 대기강제**로 1979–2021 시간별 해면을 $L_A=100$ 연안점에 생산한 historical reconstruction. 전체 $L=129$, *"with no site having both NOAA and ADCIRC observations"*. NOAA–ADCIRC 최근접거리 중앙값 **21.7 km**(1.9–119.8 km). 영역은 남부 텍사스(26.1°N, 97.2°W)–북부 메인(44.9°N, 67.0°W), 연최대치 1979–2021($T_0=43$년).
[^wh-cor]: 同 §4.2 Fitted Spatial Model, 식 (14) — `Cor(µN, µA) = 0.995, Cor(ξN, ξA) = 0.837, Cor(log σN, log σA) = 0.443`. 해석도 같은 절: location 근사 완전상관이 *"the primary driver of fusion"* 이고 100개 모의점이 29점 관측망을 densify 한다. shape 가 중요한 이유 — *"ξ is the least precisely estimated parameter yet has the largest influence on return levels."* 범위모수는 $\hat\rho_1=2873$ km ~ $\hat\rho_4=188$ km 로 한 자릿수 차이.
[^wh-cv]: 同 §4.5 Geographic Block Cross-Validation — 5개 연속 연안 블록(Gulf n=4, Florida n=5, Southeast n=5, Mid-Atlantic n=6, New England n=9)을 차례로 제외하고 Stage 2 재적합. 전 29점 100년 RL RMSE **0.665 m(융합) vs 0.810 m(NOAA-only) = 18% 감소**; Gulf 4점 제외한 25점에서 **0.496 vs 0.776 = 36% 감소**. log-scale 은 역전 — *"NOAA-only log-scale RMSE is 0.298 vs. 0.406 for the joint model"*, 이유는 scale 상관 0.44 로 *"borrowing from ADCIRC scale parameters that differ substantially from NOAA values introduces noise rather than information"*. 결론 문장: *"practitioners should examine per-parameter correlations before assuming uniform benefit from fusion."* 초록의 LOO-CV 35% 는 §Abstract.
[^wh-geo]: 同 §4.3–4.4 — SE 는 대서양 0.10–0.19 m, 멕시코만 0.16–0.54 m. 지역별 이득 성격: 대서양 *"confidence bands narrow substantially (median SE ratio 1.34)"*, 멕시코만 *"SE ratios are close to 1 (median 0.92) and fusion instead shifts point estimates upward, as ADCIRC's heavy-tailed shape estimates pull ξ higher where gauge coverage is sparse"*. 전체 SE 비 중앙값 1.17(융합 불확실성이 NOAA-only 의 약 85%), *"roughly 24% of the coastline shows SE ratios exceeding 1.5"*, 그리고 *"The ADCIRC-only model is systematically lower than gauge-based estimates."*
[^wh-limit]: 同 §5.4 Limitations and Future Work — *"the cross-source shape correlation, while positive, is estimated with high uncertainty under the present sampling design. The reported point estimate of r = 0.84 should be interpreted cautiously; the true value may be substantially lower."* Stage 2 의 Stage 1 MLE 결합정규 가정은 $\hat\mu_0$·$\log\hat\sigma$ 에는 40+ 연최대치로 잘 지지되나 $\hat\xi$ 는 $\xi=0$ 근방에서 수렴이 느리다(Coles 2001)고 같은 절이 적는다.

## 10. 연결

- [`01-concept.md`](01-concept.md) — 5 인자 정성
- [`02-theory.md`](02-theory.md) — shallow-water + IB + wind stress equation
- [`04-code-and-tools.md`](04-code-and-tools.md) — ADCIRC NWS modes + KHOA OpenAPI 운영 (verified)
- [`05-examples.md`](05-examples.md) (예정) — 한국 태풍 case study
- [`concepts/tides/03-analysis-methods.md`](../tides/03-analysis-methods.md) — 조화 분석 (separation step 1)
- [`concepts/sst/03-analysis-methods.md`](../sst/03-analysis-methods.md) — Mann-Kendall canonical
- [`experience/khoa-annual-climate-trend.md`](../../experience/khoa-annual-climate-trend.md) — Korean SLR + surge climate trend
