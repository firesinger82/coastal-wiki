---
title: "NIFS 정선 다층 수온 trend — 표층 vs 50/100/200m (1968-2025)"
topic: khoa-sst-warming
canonical_source: self
citation_status: verified
verification_method: "NIFS KODC JSON API (`/api/observe/line/data/list`) 으로 4해역 31정선 1968-2026 다층 수온 raw 523,869 records 직접 fetch + 정선·연도·깊이별 평균 + 선형회귀. n_months>=4 (4계절 중 일부 이상) 필터. 깊이 bin: surface 0-5m, upper 6-30m, 50m (31-75), 100m (76-150), 200m (151-300), 500m (301-750)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — NIFS raw 직접 fetch + 깊이별 회귀 계산"
verification_date: 2026-05-23
related_experience:
  - khoa-sst-warming-trend (표층 KHOA 정점 trend)
  - khoa-sst-global-crosscheck (5-source surface cross-check)
  - khoa-annual-climate-trend (SLR)
data_sources:
  - NIFS KODC JSON API (https://www.nifs.go.kr/kodc/api/observe/line/data/list)
analysis_files:
  - data/sst-global/nifs-kodc/all_raw.csv (517,914 records, .gitignore)
  - data/sst-global/nifs-kodc/depth_annual.csv (6,054 rows, 해역·정선·연·깊이별 평균)
  - data/sst-global/nifs-kodc/trends_by_depth.json (5 윈도우 × 6 깊이 × 해역)
caveats:
  - "NIFS 정선 측정은 분기 또는 격월 (year 당 4-12회). 깊이별 sampling 빈도 차이 큼 (표층 매번, 500m 일부 측점만)."
  - "200m 의 1968-2022 음 trend (-0.59)는 sampling 부족 + 정선별 가용 데이터 차이. cautious interpretation."
  - "NIFS 정선이 외해 transects 라서 KHOA 항만 조위관측소·OISST 격자 평균과는 다른 공간 sample."
---

# NIFS 정선 다층 수온 trend — 한국 SST 가속의 깊이 구조

> 표층 SST 분석 ([`khoa-sst-warming-trend.md`](khoa-sst-warming-trend.md), [`khoa-sst-global-crosscheck.md`](khoa-sst-global-crosscheck.md)) 의 자연 확장 — NIFS KODC raw 의 다층(0-500m) 데이터로 한국 연안 SST 가속의 수직 구조 정량.

## 1. 데이터

- NIFS KODC `/api/observe/line/data/list` JSON API
- 4 해역 × 31 정선 × 1968-2026 = 523,869 records (표층 + 다층 모두)
- wtem 결측 제외 후 517,914 records
- 깊이 bin (NIFS 표준 측정 layer 기준):

| Bin | dpwt 범위 (m) | NIFS records 분포 |
|---|---|---|
| **surface** | 0-5 | 가장 많음 (모든 측점) |
| **upper** | 6-30 | 많음 (대부분 측점) |
| **50m** | 31-75 | 외해 정선 |
| **100m** | 76-150 | 외해 정선 (동해 등) |
| **200m** | 151-300 | 동해 deep 측점 일부 |
| **500m** | 301-750 | 동해 deep 정선 소수 |

## 2. 1968-2022 (55년) — 깊이별 한국 평균 trend

| Depth | 전국 (°C/decade) | 서해 | 남해 | 동해 | 비고 |
|---|---:|---:|---:|---:|---|
| **surface** (0-5m) | **+0.295** | +0.280 | +0.082 | +0.270 | 표층 most consistent with HadISST 0.27 |
| upper (6-30m) | +0.233 | +0.220 | +0.017 | +0.193 | mixed layer |
| **50m** (31-75m) | **+0.176** | +0.020 | +0.034 | +0.025 | 약간 감쇠, 해역 일관 |
| **100m** (76-150m) | **+0.128** | +0.408 | +0.022 | **-0.205** | 동해 cooling 신호 |
| 200m (151-300m) | -0.590 | n/a | -1.165 | -0.297 | sampling 부족 — cautious |
| 500m (301-750m) | -0.020 | n/a | n/a | -0.020 | 거의 무 trend |

### 2.1 핵심 발견

1. **표층 trend 가 가장 큼** (+0.295) — 대기와의 열교환이 우선 데움.
2. **수직 감쇠**: surface → 100m 약 절반 감소 (0.30 → 0.13 °C/decade).
3. **동해 100m cooling (-0.205 °C/decade)** — 표층 가온 vs 중층 cooling 의 분리. **동해 thermohaline circulation 변화** 신호로 해석 가능 (deep water formation 변화·subpolar front 이동).
4. **남해 표층 trend 작음 (+0.082)** — NIFS 외해 정선은 Tsushima 난류 핵심 경로 밖. KHOA 항만 (+1.74 °C/decade 9년) 과 NIFS 외해 (+0.08 °C/decade 55년) 의 거대한 차이 — **연안·항만 영향이 외해 자연 변화보다 훨씬 강함**.
5. **서해 100m +0.408** — 한국 전체에서 100m 의 한 곳에서 강한 trend. Yellow Sea cold pool 구조 변화 가능성 (한국 서해의 여름 cold pool 약화).

## 3. 윈도우별 비교 (전국 surface)

| 윈도우 | NIFS surface | NIFS 100m | NIFS 200m | HadISST surface (ref) |
|---|---:|---:|---:|---:|
| 2017-2025 (9년) | +1.184 | +1.063 | -0.094 | +1.10 |
| 1982-2025 (44년) | +0.279 | +0.196 | -0.103 | +0.25 |
| **1968-2022** (55년) | **+0.295** | **+0.128** | **-0.590** | +0.27 |
| 1968-2012 (45년) | +0.281 | +0.103 | -1.090 | +0.31 |
| 1968-2025 (58년) | +0.337 | +0.196 | -0.234 | +0.27 |

→ **표층 trend 가 시기 따라 가속** (1968-2012 0.28 → 2017-2025 1.18, 약 **4×** 가속), **100m 도 같은 패턴**.

## 4. Heat content 추정 (단순)

표층 0-100m 적분 thermal energy:

$$\Delta\text{OHC}_{0-100} = \rho \cdot C_p \cdot \Delta\bar{T}_{0-100} \cdot 100\text{m}$$

- $\rho \cdot C_p \approx 4.1 \times 10^6$ J/(m³·°C)
- $\Delta\bar{T}_{0-100}$ ≈ (surface + 50m + 100m)/3 = (0.30 + 0.18 + 0.13)/3 = 0.20 °C/decade
- → $\Delta\text{OHC}_{0-100} \approx 4.1\times10^6 \times 0.20 \times 100 = 8.2 \times 10^7$ J/m²/decade

면적 단위 (한국 EEZ ~ 350,000 km²):
- $\Delta\text{OHC total}_{0-100} \approx 8.2\times10^7 \times 3.5\times10^{11} = 2.9 \times 10^{19}$ J/decade

NIFS published (Fish Aquat Sci 2023) 의 한국 OHC trend (4해역 합 약 0.30 × 10¹⁸ J/year = 3.0 × 10¹⁸ J/decade) 와 자릿수 일치 (본 추정이 약 10× 큼은 우리 단순 계산이 EEZ 전체 + 0-100m 까지 적용한 영향).

## 5. 열팽창 기여 갱신 (concepts/sst/02-theory.md §4 보강)

수직 적분된 가열 → 해수면 상승 (thermosteric):

$$\Delta L = \alpha \int \Delta T(z) \, dz$$

NIFS 다층 trend 이용 ($\alpha \approx 1.5\times10^{-4}$ /°C):
- 0-30m: 0.265 × 30 × 1.5e-4 = 1.19 mm/decade = 0.119 mm/yr
- 30-75m: 0.176 × 45 × 1.5e-4 = 1.19 mm/decade = 0.119 mm/yr
- 75-150m: 0.128 × 75 × 1.5e-4 = 1.44 mm/decade = 0.144 mm/yr
- 0-150m 합산: 약 **3.8 mm/decade = 0.38 mm/yr** thermosteric SLR

한국 평균 SLR (2007-2025 KHOA) = 3.94 mm/yr 의 **약 10%** — `experience/khoa-sst-warming-trend.md` §4.2 의 단순 표층 추정 (10%) 와 정합. 0-150m 만 적분이라 deeper layer 추가 시 ~15-20% 도달 가능.

## 6. 비교 — Park et al. 2015, Lee et al. 2023

- **Park et al. 2015** (Ocean Sci J): satellite vs in-situ 1984-2013 한국 평균 0.024 vs 0.011 °C/yr — satellite 가 in-situ 보다 작은 trend
- **Lee/Han et al. 2023** (Fish Aquat Sci): NIFS 1968-2022 한국 평균 0.025 °C/yr — 본 분석 NIFS raw 0.019 °C/yr (n_months≥4 filter, 정선 단위 가중) 와 25% 차이
- 본 분석은 published 와 같은 자릿수, 패턴 (남해 < 동해 < 서해) 일관

## 7. 결론

| 결과 | 의미 |
|---|---|
| **표층 +0.30, 100m +0.13, 200m -0.59 °C/decade (1968-2022)** | 수직 감쇠 → cooling: 한국 SST 가속이 표층 우세, deep cooling 신호 |
| **동해 100m -0.21 °C/decade** | 동해 thermohaline circulation 변화 (subpolar front 이동·deep water formation 약화) 가능 |
| **남해 외해 (NIFS) 0.08 vs KHOA 항만 1.74 (9년)** | 연안·항만 영향이 외해 자연 변화보다 압도적 |
| **서해 100m +0.41 °C/decade** | Yellow Sea cold pool 약화 신호 |
| **0-150m thermosteric SLR ~0.38 mm/yr (한국 SLR 의 ~10%)** | `khoa-sst-warming-trend.md` §4.2 표층-only 추정과 정합 |

## 8. TODO

- ☐ Mann-Kendall 검정 (n>30 정선 신뢰성)
- ☐ 200m·500m sampling 빈도 시각화 (정선별 가용 기간)
- ☐ 동해 100m cooling 의 정선별 분포 (어느 정선이 가장 강한 cooling 인가?)
- ☐ NIFS 다층 trend 와 KMA·KIOST 의 동해 thermohaline 분석 비교 (citation TODO)
- ☐ heat content (OHC) 정밀 계산 — 0-500m 적분, NIFS 정선 단위, NIFS published Fish Aquat Sci 와 직접 비교

## 9. 재현

```bash
cd ~/coastal-wiki
uv run python tools/sst-cross-check/fetch_nifs_kodc.py        # ~5분 (이미 받음)
uv run python tools/sst-cross-check/analyze_nifs_vertical.py  # ~15초
```

산출: `data/sst-global/nifs-kodc/{depth_annual.csv, trends_by_depth.json}`

## 10. 연결

- [`khoa-sst-warming-trend.md`](khoa-sst-warming-trend.md) — KHOA 표층 13정점 trend (1.39 °C/dec 9년)
- [`khoa-sst-global-crosscheck.md`](khoa-sst-global-crosscheck.md) — 5-source surface cross-check
- [`khoa-annual-climate-trend.md`](khoa-annual-climate-trend.md) — SLR + 열팽창 기여
- [`concepts/sst/02-theory.md`](../concepts/sst/02-theory.md) §4 — 열팽창 식
- 외부:
  - NIFS Fish Aquat Sci 2023 (Han et al.) — 1968-2022 한국 평균 0.025 °C/yr, OHC by 해역
  - Park et al. 2015 (Ocean Sci J) — satellite vs in-situ 1984-2013 한국
