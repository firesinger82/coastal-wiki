---
title: "SST 분석 기법 — 회귀·climatology·anomaly·MHW·spectral"
topic: sst
canonical_source: self
citation_status: verified
verification_method: "Hobday et al. 2016 MHW 정의 (Progress in Oceanography 141, 227-238), IPCC AR6 WG1 Annex II 통계 부록, Mann-Kendall test 표준 정의 (Mann 1945, Kendall 1948), Sen's slope (Sen 1968). 본 위키 적용: experience/khoa-sst-warming-trend.md + khoa-sst-global-crosscheck.md 분석 절차 재정리. tools/sst-cross-check/ 스크립트 1:1 대응."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — 표준 정의 인용 + 본 위키 실제 적용 cross-ref"
verification_date: 2026-05-23
related:
  - concepts/sst/02-theory.md
  - experience/khoa-sst-warming-trend.md
  - experience/khoa-sst-global-crosscheck.md
  - tools/sst-cross-check/analyze_global_trends.py
---

# SST 분석 기법

> 본 §는 한국 연안 SST 분석에서 자주 쓰이는 통계·신호처리 기법을 정형화. 본 위키의 [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md), [`khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md) 에서 실제 적용된 절차.

## 1. 시계열 회귀 (Trend)

### 1.1 선형회귀 (OLS)

연평균 SST $T_i$ 와 연도 $y_i$ ($i = 1 \ldots n$):

$$T_i = \beta_0 + \beta_1 y_i + \epsilon_i$$

기울기 (slope):

$$\beta_1 = \frac{\sum (y_i - \bar{y})(T_i - \bar{T})}{\sum (y_i - \bar{y})^2}$$

단위: °C/year. 본 위키 관례: **°C/decade** 표시 (= slope × 10).

결정계수 $R^2 = 1 - \frac{\sum (T_i - \hat{T}_i)^2}{\sum (T_i - \bar{T})^2}$ — trend 가 설명하는 분산 비율.

### 1.2 Mann-Kendall 검정 (비모수 trend test)

OLS 의 정규성 가정 약함 → 비모수 Mann-Kendall (Mann 1945, Kendall 1948).

검정통계량 $S$:

$$S = \sum_{i=1}^{n-1} \sum_{j=i+1}^{n} \text{sgn}(T_j - T_i)$$

null hypothesis: 무 trend. $|Z| > 1.96$ 이면 95% 유의.

**한국 SST 적용**: 본 위키의 9년 시계열 (n=9) 은 Mann-Kendall 의 효과적 적용에 짧음 — 30년+ 시계열 (HadISST·COBE2 등) 에서 권장.

### 1.3 Sen's slope (robust trend)

Outlier 강건한 slope (Sen 1968):

$$\beta_S = \text{median}\left\{ \frac{T_j - T_i}{y_j - y_i} : j > i \right\}$$

OLS slope 과 비교 시 outlier 영향 작음. 본 위키에서는 OLS 우선, robust check 시 Sen.

## 2. Climatology (기후평년)

### 2.1 정의

장기 평균 — 보통 30년 (WMO standard) — 의 월별·계절별·연별 평균값.

$$\bar{T}_m^{\text{clim}} = \frac{1}{N_y} \sum_{y \in [y_0, y_1]} T_{y,m}$$

표준 climatology period:
- WMO: 1991-2020 (현재 권장)
- 이전: 1961-1990, 1981-2010
- NOAA OISST: 1991-2020 기본

### 2.2 한국 적용

| Source | Climatology baseline |
|---|---|
| KHOA Annual Report 2025 | 누년 (정점별 가용 전체) |
| NIFS KODC | **1991-2020** (사이트 default download 옵션) |
| OISST v2.1 | 1991-2020 |

본 위키의 [`khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §5.1 (인천 2025 편차) 는 KHOA 누년 climatology 기준.

## 3. Anomaly (편차)

SST anomaly:

$$T'_{y,m} = T_{y,m} - \bar{T}_m^{\text{clim}}$$

월별 평균 cycle 제거 → 양·음 trend 와 변동성 signal 명확.

**한국 적용**:
- KHOA 2024 9월 SST anomaly = +3.40 °C (KHOA 2024 §3.1 인용, 본 위키)
- KHOA 2025 9월 인천 anomaly = +1.89 °C
- 글로벌 ERSST anomaly map — 한국 인근 +1~+3 °C 지역적 hotspot

## 4. Marine Heatwave (MHW) 정의 — Hobday 2016

### 4.1 정의 (Hobday et al. 2016)

**MHW** = 일별 SST 가 climatology 90th percentile 을 **5일 이상 연속** 초과하는 사건.

수학적:

$$\text{MHW event: } T_d > P_{90,d}^{\text{clim}}, \quad \text{duration} \geq 5 \text{ days}$$

$P_{90,d}^{\text{clim}}$ = climatology 기간의 day-of-year $d$ 의 90th percentile (보통 11일 윈도우 평활화).

### 4.2 MHW 분류 (Hobday et al. 2018, *Oceanography* 31)

강도 카테고리:
- **Moderate** (I): 90-99 percentile
- **Strong** (II): 90 ~ 90+2σ
- **Severe** (III): up to 90+3σ
- **Extreme** (IV): >90+3σ

### 4.3 한국 적용

- OISST v2.1 daily 0.25° 격자가 표준 source — 1981.09 부터 가능
- Python `marineHeatWaves` 패키지 (Hobday 공식 구현) 사용 가능
- 본 위키 적용 예: [`concepts/sst/05-examples.md`](05-examples.md) 에서 코드·결과

### 4.4 한국 최근 MHW 사건

- 2023-08 ~ 2023-10: 동해 + 남해 광역 MHW (KHOA 2023 §3.1)
- 2024-09: 한국 평균 SST anomaly +3.40 °C (KHOA 2024 §3.1) — Category III-IV
- 2025-09: 인천 anomaly +1.89 °C (KHOA 2025 §3.1)

## 5. Spectral 분석 (변동성 주기)

### 5.1 Fourier 분석 — 연 cycle 제거

monthly SST 시계열의 power spectrum:

$$\hat{T}(f) = \sum_{t} T_t e^{-2\pi i f t}$$

주요 peak:
- **f = 1/12 month⁻¹** (annual cycle, 가장 큰 amplitude)
- **f = 1/6** (semiannual, monsoon 영향)
- **f = 1/(2-7 yr)** (ENSO)
- **f = 1/(20-30 yr)** (PDO)

### 5.2 Wavelet 분석

Non-stationary 신호 (시간에 따라 frequency 변하는 경우) — Morlet wavelet.

본 위키에서는 wavelet 분석 아직 미적용. 향후 NIFS 50+ 년 자료 spectral 분해 시 권장.

### 5.3 EOF (Empirical Orthogonal Function)

공간장의 주요 변동 패턴 분해. 한국 SST 의 EOF1 = trend, EOF2 = ENSO 영향, EOF3 = PDO 등으로 해석 가능.

## 6. 검증 통계

본 위키 cross-check 시 사용:

### 6.1 RMSE (in-situ vs satellite)

$$\text{RMSE} = \sqrt{\frac{1}{n} \sum (T_{\text{insitu}} - T_{\text{sat}})^2}$$

한국 KHOA in-situ vs OISST 격자 평균: 보통 0.5-1.0 °C RMSE (Park et al. 2015 ref).

### 6.2 Trend 차이 정량

본 위키의 5-source cross-check ([`khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md) §2):
- 같은 시간 윈도우에서 dataset 간 slope 차이를 비교
- 2017-2025: KHOA 1.39, OISST 1.11, HadISST 1.10, COBE2 1.47, NIFS raw 1.17 — **range 0.37 °C/decade**

## 7. Heat content (수온 적분)

수직 적분 thermal energy (지난 §02-theory.md §4 참조):

$$\text{OHC}_0^H = \rho \cdot C_p \cdot \int_0^H T(z) \, dz$$

단위: J/m². NIFS published (Fish Aquat Sci 2023):
- 동해 OHC trend: 0.148 × 10¹⁸ J/year (가장 큰 누적)
- 남해 0.089, 서해 0.061 × 10¹⁸ J/year

본 위키 NIFS raw 의 다층 trend 분석 → [`experience/nifs-vertical-trends.md`](../../experience/nifs-vertical-trends.md) (예정).

## 8. 코드 매핑

본 위키의 분석 스크립트와 위 기법:

| 스크립트 | 사용 기법 |
|---|---|
| `tools/sst-cross-check/analyze_global_trends.py` | OLS regression (§1.1) — 5 source × 6 윈도우 |
| `tools/sst-cross-check/analyze_nifs_trends.py` | OLS — 정선·해역 평균 |
| `tools/khoa-validation/analyze_utide.py` | UTide harmonic (조석용, SST 무관) |

향후 추가 예정:
- MHW 식별 (Hobday 2016) — `tools/sst-cross-check/identify_mhw.py`
- Sen's slope robust check
- EOF 한국 SST 공간장 분해

## 9. 인용 정형

- 선형회귀 OLS — 표준 (인용 불필요)
- Mann-Kendall — Mann (1945) Econometrica, Kendall (1948) Rank Correlation Methods
- Sen's slope — Sen (1968) JASA 63(324)
- MHW — Hobday et al. (2016) Progress in Oceanography 141:227-238
- MHW Category — Hobday et al. (2018) Oceanography 31(2):162-173
- WMO climatology — WMO Technical Regulations Vol I

## 10. 연결

- [`01-concept.md`](01-concept.md) — 정의·시공간 스케일
- [`02-theory.md`](02-theory.md) — 열수지·열팽창
- [`04-code-and-tools.md`](04-code-and-tools.md) — 데이터셋·endpoint
- [`05-examples.md`](05-examples.md) — MHW 식별 실습 (예정)
- [`experience/khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md) — 5-source 회귀 비교
- [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §5 — anomaly cross-check
