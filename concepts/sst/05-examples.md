---
title: "SST 분석 실습 — Marine Heatwave 식별 + 한국 연안 trend 재현"
topic: sst
canonical_source: self
citation_status: source-needed
verification_method: "Hobday et al. 2016 MHW 알고리즘 5단계 정형 (Progress in Oceanography 141:227-238) + 본 위키 분석 실제 코드 (tools/sst-cross-check/) 인용. 한국 MHW 사건은 KHOA Annual Report 2023-2025 §3.1 SST anomaly 표 직접 인용. MHW 실제 detection 코드는 골격만 — 실행·결과 verified 는 추가 작업 (TODO §6)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — 골격 작성, MHW 실행 verification 대기"
verification_date: 2026-05-23
related:
  - concepts/sst/03-analysis-methods.md
  - tools/sst-cross-check/
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

## 4. 예제 4 — Marine Heatwave (MHW) 식별 (한국 서귀포 2023-2025, TODO)

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

### 4.3 권장 출력 (TODO 실행 후 보강)

서귀포 (33.24°N, 126.56°E) 2023-2025 예상 MHW events:
- 2023-08 ~ 2023-09: 동중국해 광역 MHW (KHOA 2023 §3.1 인용)
- 2024-09: anomaly +3.40 °C 한국 평균 (KHOA 2024 §3.1) — 정점별 III/IV 카테고리 추정
- 2025-09: 인천 anomaly +1.89 °C (KHOA 2025 §3.1) → 서귀포 더 강했을 가능성

표 형식 (예시):

| Event start | End | Duration (days) | Max anomaly (°C) | Category |
|---|---|---:|---:|---|
| 2023-08-15 | 2023-09-22 | 39 | +3.2 | III-severe (추정) |
| 2024-09-01 | 2024-10-18 | 48 | +4.1 | IV-extreme (추정) |

⚠ 위 표는 KHOA 보고된 평균 anomaly 기반 추정 — Hobday 알고리즘 daily 실행으로 정밀화 필요.

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

## 6. TODO (verified 승급 조건)

본 §의 다음 항목들은 실제 실행·검증 후 verified 승급:

1. ☐ ERDDAP point fetch 코드 — 실제 호출·CSV 저장 (~1분)
2. ☐ Hobday 2016 detection 알고리즘 — 본 위키 코드 (`tools/sst-cross-check/identify_mhw.py`) 작성·검증
3. ☐ 서귀포·제주·거제도 등 KHOA 13정점 인근 격자 MHW 식별 결과 표
4. ☐ 2024-09 한국 인근 anomaly map (cartopy plot)
5. ☐ Lee et al. 2023 paper 의 한국 MHW 빈도 trend 와 본 결과 비교

verified 후 `experience/khoa-mhw-2023-2025.md` 새 노트로 분리 권장.

## 7. 관련 외부

- [Hobday MHW Python package (marineHeatWaves)](https://github.com/ecjoliver/marineHeatWaves) — 공식 구현
- [NOAA ERDDAP OISST v2.1](https://coastwatch.pfeg.noaa.gov/erddap/griddap/ncdcOisst21Agg.html) — point query
- [marineheatwaves.org](https://marineheatwaves.org/) — community resource

## 8. 연결

- [`03-analysis-methods.md`](03-analysis-methods.md) §4 — MHW 정의
- [`04-code-and-tools.md`](04-code-and-tools.md) §3 — OISST daily 다운로드
- [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §5·§7 — 한국 SST anomaly·MHW 기록
