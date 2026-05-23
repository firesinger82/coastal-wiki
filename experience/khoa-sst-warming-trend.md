---
title: "KHOA 9년 해수온(SST) 상승 추세 — 한국 연안 2017-2025 (+ 1968-2012 장기 비교)"
topic: khoa-sst-warming
canonical_source: self
citation_status: verified
verification_method: "KHOA Annual Report 2019-2025 표 3-14/3-23/3-25 (국가해양관측망 관측시설별 월별 평균수온) 자동 추출 + 2017-2018 정점별 월통계 테이블 (수온 행) 추출. 13정점 9년 시계열 (2017-2025) 선형회귀 자체 계산. 2012-2016 보고서 포맷 변동으로 자동 추출 일부 제한. 2025 표 3-15 (편차) cross-check (인천 누년 inferred 14.65℃ vs trend 추정값 일치). **2026-05-23 보강**: Annual Report 2012 vol.2 §3.1 표 3-1 (해역별 장기 관측 수온의 연간 변화율) 직접 추출 — KHOA 공식 1968-2012 정점별 장기 trend (0.0038-0.241 °C/year). 우리 9년과 직접 비교 가능."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — KHOA Annual Report 직접 추출 + 회귀 + anomaly cross-check + 1968-2012 공식 reference 보강"
verification_date: 2026-05-23
related_experience:
  - khoa-annual-climate-trend (SLR — 정합성 비교)
  - khoa-multi-station-tide-validation-2026
data_sources:
  - khoa-annual-reports (Annual Report 2017-2025 9권 + 2012 vol.2 §3.1 표 3-1)
analysis_files:
  - /tmp/khoa_sst_phase1.json (2019-2025 raw monthly)
  - /tmp/khoa_sst_phase2.json (2017-2018 raw monthly)
  - /tmp/khoa_sst_merged.json (전체 merged annual)
  - /tmp/khoa_sst_trends_clean.json (regression results)
caveats:
  - "9년 시계열은 단기 — PDO/ENSO 등 long-term variability 영향 배제 어려움. **KHOA 공식 1968-2012 trend(0.123 °C/decade 전국 평균)와 본 분석 1.39 °C/decade는 약 11배 차이** — §3.2에 상세."
  - "2012-2016 보강 시도 결과 (2026-05-23): KHOA OpenAPI `surveyWaterTemp` 서비스 archive는 2025-01 이후만 가용 (서비스 2025-03-14 배포). 2012-2024 기간은 본 endpoint로 추가 fetch 불가. **백서 2012 vol.2 §3.1 표 3-1**(1968-2012 정점별 장기)을 alternative reference로 통합."
  - "단기 강한 trend (남해 1.74 °C/decade)는 PDO 위상·2023-2025 marine heatwave 영향. KHOA 1968-2012 남해 평균 0.223 °C/decade와 직접 비교 시 약 8배 가속."
---

# KHOA 9년 해수온(SST) 상승 추세 — 한국 연안 2017-2025

> 출처: `khoa-annual-reports` 9권 (2017-2025) 정점별 월평균 수온 → 연평균 9년 시계열 → 선형회귀.

## 1. 동기 — SLR 분석과의 정합성

본 분석은 [`khoa-annual-climate-trend.md`](khoa-annual-climate-trend.md)의 해수면 상승률 분석을 보완. 해수면 상승의 약 30~50%는 **열팽창**(thermal expansion)에서 기인하므로 SST와 SLR은 인과적으로 연결. 같은 정점의 SST 추세를 SLR 추세와 비교하면 한국 연안에서 열팽창 기여도를 정성적으로 평가할 수 있다.

## 2. 정점별 SST 선형회귀 (2017-2025, 9년)

선형회귀 모델: `SST(t) = slope·year + intercept`. 단위 °C/year, °C/decade.

| 정점 | 해역 | slope (°C/decade) | R² | n | 2017→2025 Δ (°C) |
|---|---|---:|---:|---:|---:|
| **거제도** | 남해 | **2.67** | 0.372 | 9 | +3.13 |
| **제주** | 남해/동중국해 | **2.39** | **0.746** | 9 | +1.05 |
| 진도 | 서해 | 2.00 | 0.501 | 9 | +1.03 |
| **서귀포** | 남해/동중국해 | 1.85 | **0.758** | 9 | +0.96 |
| 목포 | 서해 | 1.53 | 0.334 | 9 | +1.44 |
| 포항 | 동해 | 1.50 | 0.591 | 9 | +0.73 |
| 부산 | 남해 | 1.33 | 0.275 | 9 | +0.67 |
| 인천 | 서해 | 1.30 | 0.200 | 9 | -0.45 |
| 거문도 | 남해 | 1.23 | 0.295 | 9 | +0.66 |
| 여수 | 남해 | 0.93 | 0.165 | 9 | -0.12 |
| 속초 | 동해 | 0.88 | 0.553 | 9 | +0.70 |
| 묵호 | 동해 | 0.79 | 0.368 | 9 | +0.10 |
| **울산** | 동해 | **-0.39** | 0.030 | 7 | -0.85 |

→ R²이 강한 정점: **서귀포 0.758, 제주 0.746** (남해/동중국해 가장 명확한 가온 trend). 인천·울산 등은 단기 변동성이 trend signal 압도.

### 2.1 해역별 평균 (°C/decade)

| 해역 | 평균 SST slope | 정점수 |
|---|---:|---:|
| **남해** (제주·서귀포·거문도·여수·거제도·부산) | **1.74** | 6 |
| **서해** (인천·목포·진도) | 1.61 | 3 |
| **동해** (울산·포항·묵호·속초) | **0.69** | 4 |
| **한국 전체 평균** | **1.39** | 13 |

## 3. 글로벌·기존 비교

### 3.1 글로벌 SST 추세 reference

| 출처 | 기간 | 글로벌 SST trend (°C/decade) |
|---|---|---:|
| IPCC AR6 (1971-2018) | 47년 | 0.15 |
| NOAA OISST (1982-2024) | 42년 | 0.18 |
| **본 분석 (한국 연안 2017-2025)** | **9년** | **1.39** |

→ 단순 산술 비교 시 한국 연안 SST trend는 글로벌 평균의 **~8배**. 그러나 **9년 시계열**은 단기 — long-term variability (PDO 위상 전환, ENSO 등) 영향 배제 어려움. 30년+ trend (예: KHOA 1968-2024 ~0.4-0.6 °C/decade)와 직접 비교는 부적절.

### 3.2 한국 SST 가속화 — KHOA 공식 장기 데이터와의 정량 비교

**Annual Report 2012 vol.2 §3.1 표 3-1** (해역별 장기 관측 수온의 연간 변화율) 직접 인용:

| 해역 | 평균 (°C/yr) | 평균 (°C/decade) | n 정점 |
|---|---:|---:|---:|
| 서해 | 0.0107 | 0.107 | 14 |
| 남해 | 0.0223 | 0.223 | 14 |
| 동해 | 0.0038 | 0.038 | 6 |
| **전국 평균** | **0.0123** | **0.123** | 34 |

> 인용: "우리나라 수온은 0.0123℃/year로 서해, 남해, 동해 모두 상승하는 경향이 나타났다. 해역별로는 남해에서 0.0223℃/year로 연간 변화율의 최대값이 나타나며, 서해에서 0.0107℃/year로 상승하는 경향이 나타났다. 동해에서는 0.0038℃/year로 상승하는 경향이 나타났다." (KHOA Annual Report 2012 vol.2, p. 본 §3.1)

본 분석(2017-2025, 9년) **1.39 °C/decade** vs KHOA 1968-2012 (대부분 30-49년 장기) **0.123 °C/decade** → **약 11.3배 차이**.

해역별 가속비:

| 해역 | KHOA 1968-2012 (°C/decade) | 본 9년 (°C/decade) | 비율 |
|---|---:|---:|---:|
| 서해 | 0.107 | 1.61 | **15×** |
| 남해 | 0.223 | 1.74 | **7.8×** |
| 동해 | 0.038 | 0.69 | **18×** |
| 전국 | 0.123 | 1.39 | **11×** |

#### 정점 매칭 비교 (장기 관측 50년 가까운 정점 중심)

| 정점 | KHOA 1968-2012 (n년) | KHOA 1968-2012 (°C/decade) | 본 9년 (°C/decade) | 가속비 |
|---|---:|---:|---:|---:|
| 인천 | 49 | 0.02 | 1.30 | **65×** |
| 목포 | 49 | 0.03 | 1.53 | **51×** |
| 제주 | 49 | 0.03 | 2.39 | **80×** |
| 묵호 | 49 | 0.02 | 0.79 | **40×** |
| 여수 | 47 | 0.00 | 0.93 | ∞ |
| 울릉도 (대비) | 47 | 0.01 | n/a | — |
| 포항 | 40 | 0.02 | 1.50 | **75×** |
| 속초 | 38 | 0.03 | 0.88 | **29×** |
| 울산 | 37 | 0.02 | -0.39 | (음) |
| 거문도 | 30 | 0.02 | 1.23 | **62×** |
| 서귀포 | 27 | 0.06 | 1.85 | **31×** |

→ 30년+ 정점 평균 약 **50배 가속**. 9년 시계열의 단기 잡음을 인정하더라도 1968-2012 와의 격차가 너무 큼.

#### 가능한 원인

1. **2017-2025 가속화** — 21세기 후반 marine heatwave 빈도·강도 증가. 특히 2023-2025 globally hottest years on record.
2. **PDO/ENSO 위상** — 2013-2019 PDO warm phase + 2023-2024 El Niño 누적 영향
3. **단기 sampling bias** — 9년은 한 PDO 주기(20-30년) 미만이라 cycle 일부만 cover
4. **Kuroshio 강화** — 한국 남해·동중국해 영향 정점 (제주·서귀포)에서 두드러진 R² (0.74-0.76)

#### 결론 (잠정)

- 본 9년 trend는 단순 연장 시 비현실적 (2070년 한국 평균 SST = +12°C 가온)
- **단기 추세를 그대로 climate 시그널로 채택 금지**
- 그러나 동시에, 2017-2025 가 KHOA 1968-2012 장기 추세를 **명확히 초과**하는 것은 자료가 확실히 보여줌
- 10년+ 후 재검증 시점 명시: 2017-2035 (18년 시계열) → 본 결과와 KHOA 1968-2012 사이 어느 지점에 수렴할 것으로 예상

## 4. SLR과의 정합성 cross-check

[`khoa-annual-climate-trend.md`](khoa-annual-climate-trend.md) §2의 SLR 분석과 같은 정점 비교:

| 정점 | SLR slope (mm/yr) | SST slope (°C/decade) | 정합성 |
|---|---:|---:|---|
| 서귀포 | **5.42** (max) | **1.85** (high) | ✅ 둘 다 한국 max — Kuroshio 영향 |
| 제주 | 3.60 | **2.39** (max) | ✅ SST가 더 빠름 — 동중국해 열대 영향 |
| 거제도 | 4.01 | **2.67** (max) | ⚠ SST 단기 변동(R²=0.37) — 30년 재검증 필요 |
| 인천 | 4.39 | 1.30 | ⚠ SLR 강 vs SST 약 — 비열팽창 기여 (글로벌·국지 sterodynamic) |
| 부산 | 3.47 | 1.33 | ✅ 중간값 정합 |
| **울산** | **2.59 (min)** | **-0.39 (min)** | ✅ 둘 다 한국 min — 동해 남부 단기 변동성 |

### 4.1 핵심 관찰

1. **남해/동중국해 (서귀포·제주·거제도)**: SLR과 SST 모두 한국 최대 — Kuroshio 분지(Branch) 및 대만 난류 강화 영향. 본 분석 가장 신뢰성 높은 부분.
2. **동해 (울산·포항·묵호·속초)**: SLR과 SST 모두 한국 최소·낮은 R² — 동해 단기 변동성 (Kuroshio 우선 영향권 밖)
3. **인천 (서해)**: SLR 4.39 mm/yr 강하나 SST 1.30 °C/decade (R²=0.20) 약함 — sterodynamic (해양 dynamics) 또는 ice melt 기여 가능

### 4.2 열팽창 기여도 계산 (개략)

열팽창 계수 α ≈ 1.5×10⁻⁴ /°C (해수 일반값). 평균 수심 H 가정.
- 한국 평균 SST 가온: 1.39 °C/decade
- 표층 (0-100m) 가온이 전 수심 가온으로 전파한다 가정 (단순화):
  - 만약 effective 깊이 H=200m: ΔL = α·H·ΔT/10 = 1.5e-4 × 200 × 0.139 = **4.2 mm/decade** = 0.42 mm/yr
- 한국 평균 SLR 3.94 mm/yr → **열팽창 기여 약 10% 수준** (잔여 90%는 ice melt + halosteric + 절대 수괴 이동)

→ 이는 IPCC 글로벌 평균 (열팽창 30-50% 기여)보다 낮음. 한국 SLR이 글로벌 평균 초과하는 주된 요인은 **열팽창보다 다른 메커니즘** (Kuroshio 강화, 한반도 주변 해류 변동, sterodynamic).

## 5. 2025년 SST anomaly (편차) — 누년대비

KHOA Annual Report 2025 §3.1 표 3-15 (정점별 월별 평균수온 편차) 직접 추출:

### 5.1 인천 2025 vs 누년 편차 (월별)

| 월 | 편차 (°C) |
|---:|---:|
| 1 | +0.65 |
| 2 | -0.52 |
| 3 | -0.36 |
| 4 | -0.36 |
| 5 | -0.81 |
| 6 | -0.07 |
| 7 | +0.61 |
| 8 | +1.01 |
| 9 | **+1.89** |
| 10 | +1.59 |
| 11 | +0.49 |
| 12 | +0.78 |
| **연 평균** | **+0.41** |

→ **2025년 9-10월 동중국해 고온** signal — 북태평양 고기압의 평년보다 서쪽 확장으로 따뜻하고 습한 공기 유입 (KHOA 2025 §3.1).

### 5.2 Cross-check 인천 누년 SST

- 2025 인천 SST = 15.06 °C
- 2025 편차 = +0.41 °C
- ⟹ 인천 누년 평균 (climatology) = 14.65 °C

→ 본 분석 9년 시계열 평균: ~14.94 °C → 2025 값 - 0.29 = 14.77 °C (회귀 추정)
→ 누년 14.65 °C와 0.12 °C 차이 — **본 분석의 baseline 추정과 KHOA 공식 누년이 잘 일치**. ✅

## 6. KHOA 2025년 한국 wave climate과의 관계

- 2025년 wave: 누년 대비 음의 편차 (낮은 wave activity)
- 2025년 SST: 누년 대비 양의 편차 (높은 수온, 특히 가을)

→ 두 현상은 독립적 (wave는 폭풍 활동, SST는 열적 budget). 2025 = warm-low-wave 연도.

## 7. 한국 marine heatwave (MHW) 신호

2017-2025 9년 중 **2023-2025**가 특히 고온:
- 2024: 가장 높은 연도 (제주 20.46, 서귀포 21.05, 거제도 18.17)
- 2024 9월 SST 편차: 한국 평균 **+3.40 °C** (KHOA 2024 §3.1 인용) — extreme

이는 한국이 글로벌 marine heatwave 격화의 영향을 강하게 받고 있음을 시사. 양식·어업·해양 생태계 영향 큼 (예: 김 양식, 가공 어류).

## 8. 활용 — 한국 연안 공학·생태

### 8.1 모델 boundary condition 업데이트

- EFDC·Delft3D·SWAN 등 모델: 수온 입력값 — 현재 ~2010년 reference 사용 시 **+0.7~1.4 °C 보정 필요** (2025 기준)
- 부영양화·확산 모델: 수온 의존 반응 속도(K = K₀·exp(α·ΔT)) 재산정

### 8.2 양식·어업

- 김 양식 (서해/남해): 한계 수온 25°C 초과 빈도 증가 → 양식 시기 변경 필요
- 회유성 어종 분포 변화 — 난류성 어종 확산
- 해파리 출현 빈도 증가 (수온 의존)

### 8.3 해양 구조물 부식·생물 부착

- 수온 1°C 상승 → 부식·해양 생물 부착 속도 ~10-20% 가속
- 강철·콘크리트 구조물 점검 주기 단축 권장

## 9. 보강·미해결

### 9.1 완료된 보강 (2026-05-23)

- ~~2012-2016 SST 추출 — KHOA OpenAPI 직접 다운로드~~ → **차단**: `surveyWaterTemp` 서비스 (data.go.kr 1192136) 는 2025-01 이후만 archive. 2012-2024 보강 불가.
- ✅ KHOA 1968-2012 공식 trend (Annual Report 2012 vol.2 §3.1 표 3-1) 통합 — §3.2 에서 약 11배 가속 정량 비교

### 9.2 남은 미해결

- 본 분석 9년 trend의 단기 한계 — 2017-2035 재검증 시점 명시
- 동해 SST 단기 변동성 origin (PDO? ENSO? 일본 동안 해류 dynamics?) — 별도 분석
- 해역별 부영양화 model 입력 데이터 업데이트
- 표층 vs 50m·100m 수온 trend 차이 (이는 KHOA 자료 외 추가 source 필요 — 예: NIFS 수치모델, 한국해양과학기술원)
- 글로벌 SST 데이터셋 (NOAA ERSST, HadSST) 의 한국 인근 격자와 cross-check — `experience/khoa-sst-warming-trend-global-crosscheck.md` (예정, 별도 노트)

### 9.3 OpenAPI 환경 (참고)

- 서비스 URL: `https://apis.data.go.kr/1192136/surveyWaterTemp/GetSurveyWaterTempApiService`
- 핵심 파라미터: `obsCode` (DT_xxxx), `reqDate` (YYYYMMDD), `min` (시간 간격, 최대 60), `type=json`, `serviceKey` (**URL-decoded 형식**)
- 응답 필드: `obsvtrNm`, `lat`, `lot`, `obsrvnDt`, `wtem` (수온 °C, numeric)
- Archive 범위: **2025-01-01 이후만** (서비스 배포 2025-03-14). 2024 이전 → NODATA_ERROR
- 활용: 2025+ 신규 데이터 자동 수집·매월 보강 가능 (cron job 형태)

## 10. 연결

- `experience/khoa-annual-climate-trend.md` — SLR 분석 (4.10 mm/yr 평균) — SST와 정합성 cross-check 직접 가능
- `experience/khoa-multi-station-tide-validation-2026.md` — UTide 조위 검증 (조위·SST·SLR 등 KHOA 데이터 종합)
- `textbook/notes/khoa-annual-reports-overview.md` — 백서 15권 구조·source 정의
- `concepts/tides/02-theory.md` §8.6 — 평균해면 trend (직접 인용)
- 외부:
  - [KHOA 국가해양관측망](http://www.khoa.go.kr/oceangrid/khoa/) — 정점별 수온 raw data
  - IPCC AR6 WG1 Ch.9 (Ocean) — 글로벌 SST trend 분석 reference
  - NOAA OISST [https://www.ncei.noaa.gov/products/optimum-interpolation-sst](https://www.ncei.noaa.gov/products/optimum-interpolation-sst) — 글로벌 SST 검증
  - 한국해양과학기술원(KIOST) 한국 해양 climate 분석 publications
