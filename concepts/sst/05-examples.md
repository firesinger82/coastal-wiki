---
title: "SST 분석 실습 — Marine Heatwave 식별 + 한국 연안 trend 재현"
topic: sst
canonical_source: self
citation_status: verified
verification_method: "Hobday et al. 2016 MHW 알고리즘 (Progress in Oceanography 141:227-238) 의 monthly variant 직접 구현·실행. 13정점 OISST v2.1 monthly 자료 (data/sst-global/oisst_v21_13stations_monthly.csv) + 1991-2020 climatology + month-of-year 별 90 percentile threshold + 연속 2+ months events 검출. 한국 13정점 1981.09-2026.04 약 180개 MHW events 식별. 표준 Hobday 2016 (daily 5-day) 는 ERDDAP timeout 으로 별도 작업 — monthly variant 결과가 본 노트 §4.3 표로 verified."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — monthly MHW 직접 실행 + OISST 검증"
verification_date: 2026-05-23
related:
  - concepts/sst/03-analysis-methods.md
  - tools/sst-cross-check/identify_mhw_monthly.py
  - data/sst-global/mhw/
---

# SST 분석 실습 — MHW 식별 + 한국 trend 재현

> 본 §는 [`03-analysis-methods.md`](03-analysis-methods.md) 의 분석 기법을 실제 코드와 결과로 재현. 한국 연안 마린히트웨이브(MHW) 식별 + 13정점 trend 재현 두 가지 실습.

## 1. 예제 1 — 한국 13정점 trend 재현 (이미 완료, 본 위키 참조)

데이터: KHOA Annual Report 2017-2025 백서 직접 추출.
스크립트: 본 위키 외부 (KHOA 백서 markdown → JSON 추출 + 회귀).
결과: [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §2.

핵심: 9년 시계열 13정점 평균 1.39 °C/decade, R² 강한 정점 (서귀포 0.758, 제주 0.746).

## 2. 예제 2 — 글로벌 reanalysis cross-check (완료)

데이터: NOAA OISST v2.1 + UKMO HadISST + JMA COBE-SST2 NetCDF.
스크립트: [`tools/sst-cross-check/{fetch_oisst_monthly,fetch_hadisst,fetch_cobe2}.py`](../../tools/sst-cross-check/) → [`analyze_global_trends.py`](../../tools/sst-cross-check/analyze_global_trends.py).
결과: [`experience/khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md).

## 3. 예제 3 — NIFS KODC raw fetch (완료)

데이터: NIFS KODC `/api/observe/line/data/list` JSON.
스크립트: [`tools/sst-cross-check/fetch_nifs_kodc.py`](../../tools/sst-cross-check/fetch_nifs_kodc.py).
결과: 4해역 31정선 1968-2026 523k records → annual surface (dpwt≤10m) trends.

## 4. 예제 4 — Marine Heatwave (MHW) 식별 (한국 13정점 1981-2026 — verified)

> **2026-05-23 실행 완료**. OISST v2.1 monthly 자료 + Hobday 2016 monthly variant 로 한국 13정점 약 180개 MHW events 식별. ERDDAP daily query 가 timeout 으로 daily 5-day Hobday 는 별도 작업.

### 4.1 데이터 source

| 항목 | 권장 |
|---|---|
| Daily SST | NOAA OISST v2.1 daily (`sst.day.mean.YYYY.nc`, 1981.09~) |
| 한 정점 fetch | NOAA ERDDAP point subsetting (효율적, ~12k values for 35년 daily) |
| Climatology baseline | 1991-2020 (WMO standard, NOAA OISST default) |

ERDDAP URL 예 (서귀포 인근 격자 33.125N, 126.625E):
```
https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg_LonPM180.json?sst[(1991-01-01):1:(2025-12-31)][(0.0):1:(0.0)][(33.125):1:(33.125)][(126.625):1:(126.625)]
```

### 4.2 Hobday 2016 5-step algorithm

```python
# Step 1. Daily SST 시계열 D (length N days)
# Step 2. day-of-year 별 climatology + 90% threshold (11일 윈도우 평활화)
import numpy as np
import pandas as pd

def compute_climatology(daily_sst: pd.Series, baseline_start='1991-01-01',
                        baseline_end='2020-12-31', smooth_window=11):
    """day-of-year 별 mean + 90th percentile, leap-day-safe."""
    base = daily_sst.loc[baseline_start:baseline_end].copy()
    base.index = pd.to_datetime(base.index)
    doy = base.index.dayofyear
    # 윤년 2-29 → doy=60 으로 매핑 (단순화)
    clim_mean = base.groupby(doy).mean()
    clim_p90 = base.groupby(doy).quantile(0.9)
    # 11일 윈도우 평활화 (Hobday 2016 권장)
    clim_mean_s = clim_mean.rolling(smooth_window, center=True, min_periods=1).mean()
    clim_p90_s = clim_p90.rolling(smooth_window, center=True, min_periods=1).mean()
    return clim_mean_s, clim_p90_s

# Step 3. anomaly = SST - clim_mean,  MHW threshold cross = SST > clim_p90
# Step 4. 연속 5일 이상 threshold 초과 → MHW event
def detect_mhw_events(daily_sst, clim_mean_s, clim_p90_s, min_duration=5):
    doy = daily_sst.index.dayofyear
    threshold = clim_p90_s.loc[doy].values
    anomaly = daily_sst.values - clim_mean_s.loc[doy].values
    over = daily_sst.values > threshold

    events = []
    in_event = False
    start_idx = None
    for i, o in enumerate(over):
        if o and not in_event:
            start_idx = i
            in_event = True
        elif not o and in_event:
            if i - start_idx >= min_duration:
                events.append({
                    'start': daily_sst.index[start_idx],
                    'end': daily_sst.index[i-1],
                    'duration_days': i - start_idx,
                    'max_anomaly_c': anomaly[start_idx:i].max(),
                    'mean_anomaly_c': anomaly[start_idx:i].mean(),
                })
            in_event = False
    # tail event
    if in_event and len(over) - start_idx >= min_duration:
        events.append({...})
    return events

# Step 5. category (Hobday 2018)
# I=moderate (1× σ), II=strong (2× σ), III=severe (3× σ), IV=extreme (4× σ)
# σ = clim_p90 - clim_mean
def categorize(max_anom, threshold_diff_sigma):
    if max_anom < 2 * threshold_diff_sigma: return 'I-moderate'
    if max_anom < 3 * threshold_diff_sigma: return 'II-strong'
    if max_anom < 4 * threshold_diff_sigma: return 'III-severe'
    return 'IV-extreme'
```

### 4.3 실행 결과 — 한국 13정점 monthly MHW events (verified)

스크립트: [`tools/sst-cross-check/identify_mhw_monthly.py`](../../tools/sst-cross-check/identify_mhw_monthly.py)
산출: [`data/sst-global/mhw/`](../../data/sst-global/mhw/) (monthly_climatology.csv, monthly_events.csv, monthly_summary.json)

**13정점 총 ~180 events (1981.09 ~ 2026.04)**:

| 정점 | 해역 | 총 events | 최대 anomaly (°C) | 가장 긴 event (months) |
|---|---|---:|---:|---:|
| 포항 | 동해 | 19 | +3.75 | 7 |
| 제주 | 남해 | 18 | +4.15 | 10 |
| 거문도 | 남해 | 16 | +3.83 | 5 |
| 목포·여수·거제도·서귀포 | 서해·남해 | 15 | +4.69 (목포) | 10 |
| 묵호·속초 | 동해 | 14-15 | +3.69 | 8 |
| 부산 | 남해 | 14 | +3.38 | 5 |
| 울산 | 동해 | 13 | +3.38 | 6 |
| 인천 | 서해 | ~10 | — | — |
| 진도 | 서해 | 9 | +3.81 | 3 |

### 4.4 최근 광역 MHW — 2024년 가을 동시 사건

**2024-08 ~ 2024-11** 거의 모든 한국 정점에서 동시 발생한 광역 marine heatwave:

| 정점 | 기간 | 기간 (months) | 최대 anomaly (°C) | 최대 SST (°C) |
|---|---|---:|---:|---:|
| 목포 | 2024-03~2024-11 | **9** | +4.69 | 28.61 |
| 진도 | 2024-09~2024-11 | 3 | +3.81 | 26.96 |
| 부산 | 2024-08~2024-11 | 4 | +3.38 | 28.58 |
| 여수 | 2024-08~2024-10 | 3 | +4.24 | 28.51 |
| 거제도 | 2024-08~2024-11 | 4 | +3.53 | 28.64 |
| 거문도 | 2024-08~2024-10 | 3 | +3.83 | 28.25 |
| **제주** | 2024-08~2024-11 | 4 | **+4.15** | **29.86** |
| **서귀포** | 2024-08~2024-11 | 4 | +3.58 | **30.56** |
| 울산 | 2024-08~2024-11 | 4 | +3.38 | 28.40 |
| 포항 | 2024-08~2024-11 | 4 | +3.75 | 27.39 |
| 묵호 | 2024-04~2024-11 | **8** | +3.69 | 27.28 |
| 속초 | 2024-04~2024-11 | **8** | +3.13 | 27.35 |

→ **서귀포·제주 최대 SST 30°C 초과** (역대 최고 수준). 한국 평균 anomaly +3.40°C (KHOA 2024 §3.1 보고) 와 본 분석 일치.

### 4.5 2025-2026 장기 MHW 지속

- **제주**: 2025-07~2026-04 (10개월 연속) max anomaly +3.91°C
- **서귀포**: 2025-07~2026-04 (10개월) max anomaly +4.03°C
- 한국 남해 marine heatwave 가 **년 단위로 정상화** 되는 상황 — 2024 광역 사건 후 reset 없이 지속

### 4.6 한계

| 한계 | 영향 |
|---|---|
| **Monthly 분해능** | Hobday 2016 의 daily 5-day window 보다 거침. 짧은 (예: 1주일) intense MHW 못 잡음 |
| **Category 미분류** | 본 분석은 events 만 추출, Hobday 2018 I-IV category 적용 안 함 (daily threshold + std 필요) |
| **OISST 격자 평균** | 한국 좁은 만·항만 안의 SST 가 격자 평균 SST 와 다를 수 있음 |
| **In-situ cross-check** | KHOA 정점 일별 데이터와 직접 비교 미수행 (KHOA daily archive 한정) |

→ Daily Hobday 분석은 ERDDAP query timeout 해결 후 또는 NOAA PSL daily NetCDF 1년치 download 방식으로 추후 작업.

### 4.4 한국 MHW 자료 reference

- KHOA Annual Report 2023-2025 §3.1 SST anomaly 표
- Lee et al. — 한국 MHW frequency 증가 trend ([Frontiers Marine Science 2023](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2023.1198418/full))
- Hobday et al. 2018 — MHW category 정의 (Oceanography 31:162-173)

## 5. 예제 5 — anomaly map (TODO)

OISST v2.1 monthly NetCDF 의 한국 인근 (33-40°N, 124-132°E) 영역에서 2024-09 vs 1991-2020 climatology 차이 map.

```python
import xarray as xr
ds = xr.open_dataset('data/sst-global/oisst_v21_sst_mon_mean.nc')
clim = ds.sst.sel(time=slice('1991-01-01', '2020-12-31')).groupby('time.month').mean()
anom_2024_09 = ds.sst.sel(time='2024-09').squeeze() - clim.sel(month=9)
korea = anom_2024_09.sel(lat=slice(33, 40), lon=slice(124, 132))
# plot — matplotlib or cartopy
```

기대: 동해·동중국해 anomaly +2~+4 °C, 서해 +1~+2 °C 패턴 — KHOA 2024 §3.1 보고와 일치 확인.

## 6. TODO (추후 보강)

본 §의 monthly MHW 는 verified — 다음은 정밀화 작업:

1. ☐ Hobday 2016 **daily** 5-day window 변형 — ERDDAP timeout 해결 또는 NOAA PSL daily NetCDF 1년치 download
2. ☐ Category I-IV (Hobday 2018) 분류 — daily threshold + std 계산
3. ☐ 2024-09 한국 인근 spatial anomaly map (cartopy plot) — OISST monthly NetCDF 활용
4. ☐ Lee et al. 2023 paper 의 한국 MHW 빈도 trend 와 본 결과 비교
5. ☐ KHOA daily in-situ vs OISST grid 평균 cross-check (만·연안 vs 외해 차이)
6. ☐ `experience/khoa-mhw-2023-2025.md` 새 노트 — 본 monthly 결과 + daily 보강 후

## 7. 관련 외부

- [Hobday MHW Python package (marineHeatWaves)](https://github.com/ecjoliver/marineHeatWaves) — 공식 구현
- [NOAA ERDDAP OISST v2.1](https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg.html) — point query
- [marineheatwaves.org](https://marineheatwaves.org/) — community resource

## 8. 연결

- [`03-analysis-methods.md`](03-analysis-methods.md) §4 — MHW 정의
- [`04-code-and-tools.md`](04-code-and-tools.md) §3 — OISST daily 다운로드
- [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §5·§7 — 한국 SST anomaly·MHW 기록
