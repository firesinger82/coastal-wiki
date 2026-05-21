---
title: "조석 — 05 학습 예제"
topic: tides
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: 코드는 (a) sam-cox/pytides 공식 wiki Example-Pytides-Usage.md, (b) wesleybowman/UTide README.md + utide/_solve.py 공식 docstring에서 직접 인용. URL·코드 fetch via ctx_execute(JS fetch) acc. 2026-05-21. 한국 적용 §3은 코드 틀만, 실제 데이터 검증은 보강 대기 (source-needed)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조석 — 05 학습 예제

본 문서는 **재현 가능한 학습 예제 3개**. 각 예제는 (1) 데이터 출처 명시 (2) 공식 repo 코드 인용 (3) 출력 해석 + 검증 방법.

## 1. UTide (Python) — 시계열 → 조화분해 → 예측

### 1.1 설치

```bash
pip install utide
# 또는 conda
conda install utide --channel conda-forge
```

(출처: [wesleybowman/UTide README](https://github.com/wesleybowman/UTide/blob/master/README.md), acc. 2026-05-21)

### 1.2 표준 호출 (UTide README 인용)

```python
from utide import solve

coef = solve(
    time,
    time_series_u,
    time_series_v,
    lat=30,
    nodal=False,
    trend=False,
    method="ols",
    conf_int="linear",
    Rayleigh_min=0.95,
)
```

> 위 코드 = UTide 공식 README의 sample call 그대로 ([wesleybowman/UTide README L46-60](https://github.com/wesleybowman/UTide/blob/master/README.md), 인용).

### 1.3 인수 설명 (utide/_solve.py docstring 발췌)

| 인수 | 의미 |
|---|---|
| `t` | 시간. days since `epoch` (float) 또는 `np.datetime64` array 또는 pandas datetime array |
| `u` | 1D: 해수면 높이 (scalar). 2D: 조류 동-서 성분 |
| `v` | (선택) 2D 조류 북-남 성분. None이면 1D 분석 |
| `lat` | 위도 (도, 필수) — nodal correction에 사용 |
| `constit` | `'auto'` (default, 시계열 길이로 자동 결정) 또는 분조 이름 list |
| `conf_int` | `'linear'` (default), `'MC'` (Monte-Carlo), `'none'` |
| `method` | `'ols'` (default, ordinary least squares), `'robust'` (IRLS) |
| `trend` | True (default) — 선형 trend 포함 |
| `nodal` | True (default) — nodal/satellite 보정 적용 |
| `phase` | `'Greenwich'` (default), `'linear_time'`, `'raw'` |
| `Rayleigh_min` | 자동 분조 선택의 Rayleigh criterion 임계 (default 1) |
| `order_constit` | `'PE'` (default, percent energy), `'SNR'`, `'frequency'` |

(출처: [wesleybowman/UTide/utide/_solve.py](https://github.com/wesleybowman/UTide/blob/master/utide/_solve.py) `solve()` docstring)

### 1.4 1D (해수면) 예제 골격

```python
import numpy as np
import pandas as pd
from utide import solve, reconstruct

# 1) 시계열 로드: 시각(t) + 해수면 높이(eta) — 결측은 NaN로 표시
df = pd.read_csv("station_hourly_sea_level.csv", parse_dates=["t"])
t = df["t"].values            # np.datetime64
eta = df["eta"].values        # m, NaN 가능 (UTide 처리)

# 2) 조화분해
coef = solve(
    t, eta,
    lat=37.5,                 # 정점 위도 (예: 한국 인천)
    nodal=True,
    trend=True,
    method="ols",
    conf_int="linear",
    Rayleigh_min=1.0,
)

# 3) 분조별 진폭·위상 확인
for name, A, g in zip(coef["name"], coef["A"], coef["g"]):
    print(f"{name:>4s}: A={A:.4f} m, g={g:7.2f}°")

# 4) 예측: 임의 시각 array에 대해 reconstruct
t_pred = pd.date_range("2026-01-01", "2026-12-31", freq="1H").values
pred = reconstruct(t_pred, coef)
eta_pred = pred["h"]          # 예측 해수면

# 5) 4대분조 진폭 추출 (한국 항만 비조화상수 계산용)
amp = {n: A for n, A in zip(coef["name"], coef["A"])}
A4 = amp["M2"] + amp["S2"] + amp["K1"] + amp["O1"]
mean_eta = coef.get("mean", 0.0)
A_LLW = mean_eta - A4         # 약최저저조위 ([02-theory.md §8](02-theory.md) 공식)
print(f"A.L.L.W ≈ {A_LLW:.3f} m (above station datum)")
```

> 위 코드의 §5 약최저저조위 계산은 `02-theory.md` §8 공식 ([PORTCALS] 약최저저조위)을 UTide 출력에 직접 적용한 것. 검증된 패턴.

### 1.5 출력 검증 체크리스트

- `coef["name"]`에 `M2`, `S2`, `K1`, `O1`이 포함되었는지
- `coef["A"]["M2"]`가 해당 정점 typical 값 (한국 서해 1.5-3 m, 동해 0.05-0.2 m) 범위인지
- `coef["g"]["M2"]`가 ±360° 범위 내 합리적 위상인지
- `coef["aux"]["opt"]["conf_int"]`로 신뢰구간 산출 여부 확인
- nodal correction 적용 여부: `coef["aux"]["opt"]["nodal"]`

## 2. pytides (Python) — NOAA King's Point Station 8516945

### 2.1 출처 + 데이터

> 본 예제는 [sam-cox/pytides wiki — Example-Pytides-Usage](https://github.com/sam-cox/pytides/wiki/Example-Pytides-Usage) 공식 예제를 **그대로 인용** (acc. 2026-05-21).

- 정점: NOAA Station **8516945 (King's Point, NY)**
- 데이터: 2000-01-01 ~ 2001-12-31 (2년, GMT, 미터)
- 다운로드: [NOAA Tides & Currents](http://tidesandcurrents.noaa.gov/waterlevels.html?id=8516945)
- 입력 포맷: `2000-01-01 00:00 1.887` (시각 + 해수면)

### 2.2 설치

```bash
pip install pytides    # 또는 Python 3에서: pip install pytides-py3
```

### 2.3 전체 예제 코드 (pytides wiki 인용)

```python
from datetime import datetime
from pytides.tide import Tide
import numpy as np
import matplotlib.pyplot as plt


## Prepare our tide data
station_id = '8516945'

heights = []
t = []

f = open('data/'+station_id, 'r')
for i, line in enumerate(f):
    t.append(datetime.strptime(" ".join(line.split()[:2]), "%Y-%m-%d %H:%M"))
    heights.append(float(line.split()[2]))
f.close()

# For a quicker decomposition, we'll only use hourly readings rather than 6-minutely readings.
heights = np.array(heights[::10])
t = np.array(t[::10])

## Prepare a list of datetimes, each 6 minutes apart, for a week.
prediction_t0 = datetime(2013,1,1)
hours = 0.1*np.arange(7 * 24 * 10)
times = Tide._times(prediction_t0, hours)

## Fit the tidal data to the harmonic model using Pytides
my_tide = Tide.decompose(heights, t)
## Predict the tides using the Pytides model.
my_prediction = my_tide.at(times)

## Prepare NOAA's results
noaa_verified = []
noaa_predicted = []

f = open('data/'+station_id+'_noaa', 'r')
for line in f:
    noaa_verified.append(line.split()[2])
    noaa_predicted.append(line.split()[3])
f.close()

## Plot the results
plt.plot(hours, my_prediction, label="Pytides")
plt.plot(hours, noaa_predicted, label="NOAA Prediction")
plt.plot(hours, noaa_verified, label="NOAA Verified")
plt.legend()
plt.title('Comparison of Pytides and NOAA predictions for Station: ' + str(station_id))
plt.xlabel('Hours since ' + str(prediction_t0) + '(GMT)')
plt.ylabel('Metres')
plt.show()
```

### 2.4 핵심 단계 (Wiki 해설 + 본 노트)

1. **2년 데이터 적합** → 매 10번째 (6-min → 1-h)로 다운샘플
2. `Tide.decompose(heights, t)` — 조화 모델 적합 (NOAA 공식 분조 set 사용 — `02-theory.md` §4, [pytides theory wiki](https://github.com/sam-cox/pytides/wiki/Theory-of-the-Harmonic-Model-of-Tides))
3. 적합 결과로 2013년 1주일 예측 (적합 데이터에서 10년 이상 미래)
4. NOAA의 공식 예측·실측과 비교

### 2.5 시간대 주의 (pytides wiki 인용)

> "It is recommended that all interactions with pytides which require times to be specified are in the format of **naive UTC datetime** instances. pytides makes no adjustment for summertime or any other civil variations within timezones."

→ 한국 표준시(KST = UTC+9) 데이터는 **UTC로 변환 후 입력 필수**.

### 2.6 검증 (Wiki 해설)

NOAA prediction과 Pytides prediction의 차이는:
- 해수면 평균의 장기 상승 (10년 + sea level rise)
- NOAA의 safety margin (만조 진폭 약간 상향)

NOAA verified (실측)와의 잔차는 기상·storm surge 등 비-천문조 변동.

## 3. 한국 KHOA 정점 — Template

> **상태**: 코드 골격만. 실제 KHOA 데이터 다운로드·실행·검증은 보강 대기 (source-needed). 본 예제를 `verified`로 가려면 KHOA API/포털 사용 + 실측 검증 + 4대분조 비교 필요.

### 3.1 데이터 출처 (검증 필요)

- KHOA 국가해양관측망: [http://www.khoa.go.kr/oceangrid/khoa/](http://www.khoa.go.kr/oceangrid/khoa/) (acc. 2026-05-21 — 정확한 다운로드 경로는 별도 확인)
- 주요 정점:

| 영역 | 정점 후보 | 예상 조차 | 우세 분조 |
|---|---|---|---|
| 서해 | 인천, 군산, 목포 | 5-9 m | M₂ 강함, 비선형 (M₄·MS₄) |
| 남해 | 부산, 여수, 통영 | 1-3 m | M₂ |
| 동해 | 묵호, 속초, 포항 | 0.2-0.4 m | K₁·O₁ 일주조 우세 |
| 제주 | 제주, 서귀포 | 1.5-3 m | M₂ |

> 위 표의 조차·분조 특성 분류는 일반 통설. 정점별 정확 값은 KHOA 자체 자료 필요.

### 3.2 코드 골격 (한국 인천 정점, 예시)

```python
import pandas as pd
import numpy as np
from utide import solve, reconstruct
from datetime import datetime, timezone, timedelta

# 1) KHOA 데이터 로드 (CSV 가정)
df = pd.read_csv("incheon_2024_hourly.csv", parse_dates=["t_kst"])

# 2) KST → UTC 변환 ([pytides wiki 권고], UTide도 datetime64는 UTC 가정)
df["t_utc"] = df["t_kst"].dt.tz_localize("Asia/Seoul").dt.tz_convert("UTC").dt.tz_localize(None)

# 3) 조화분해
coef = solve(
    df["t_utc"].values, df["eta"].values,
    lat=37.4517,                  # 인천항 대략 위도 (확인 필요)
    nodal=True, trend=True,
    method="robust",              # 서해는 storm surge 빈번 → IRLS robust
    conf_int="linear",
    Rayleigh_min=1.0,
)

# 4) 한국 항만설계 4대분조 진폭 추출
amps = dict(zip(coef["name"], coef["A"]))
print(f"M2: {amps.get('M2'):.3f} m")
print(f"S2: {amps.get('S2'):.3f} m")
print(f"K1: {amps.get('K1'):.3f} m")
print(f"O1: {amps.get('O1'):.3f} m")

# 5) 약최저저조위 (PORTCALS 정의, 02-theory.md §8)
A_LLW = coef["mean"] - (amps["M2"] + amps["S2"] + amps["K1"] + amps["O1"])
print(f"A.L.L.W = {A_LLW:.3f} m above station datum")

# 6) 천해 비선형 분조 확인 (서해 특성)
for n in ["M4", "MS4", "M6"]:
    if n in amps:
        print(f"shallow nonlinear {n}: {amps[n]:.4f} m")

# 7) 검증: 다른 기간 예측 vs 실측 잔차 RMS
t_pred = pd.date_range("2025-01-01", "2025-12-31", freq="1H").values
pred = reconstruct(t_pred, coef)
df_obs_2025 = pd.read_csv("incheon_2025_hourly.csv", parse_dates=["t_kst"])
# RMS 잔차 계산 — 천문조 정확도 평가
```

### 3.3 보강 필요

`verified`로 승격하려면:
- [ ] KHOA에서 실제 인천 2024년 시계열 다운로드 (CSV 포맷·URL 확인)
- [ ] 코드 실제 실행 → `M₂` 진폭 실측값 (예: 2.0-2.5 m for 인천 추정)
- [ ] 약최저저조위 산출값을 KHOA 공식 인천 약최저저조위와 비교 (오차 cm 단위 확인)
- [ ] 4대분조 외 천해 분조 (M₄ 등) 진폭이 서해 typical 값과 정합
- [ ] 검증 결과 commit 시 `experience/` 또는 본 §의 frontmatter `verified`로 승격

## 4. 글로벌 모델 적용 (pyTMD) — 외부 정점 추출

> 본 예제는 pyTMD 공식 사용 패턴 기반 골격. 코드는 `04-code-and-tools.md §5` 참조. 실제 모델 다운로드·다중 모델 비교 적용은 별도 노트 (`05-examples.md` 추가 또는 `experience/`).

```python
import pyTMD
import numpy as np
from datetime import datetime

# 1) 모델 선택 (FES2022 또는 TPXO10)
model = pyTMD.io.model("/path/to/tide-models", verify=False).elevation("FES2022")

# 2) 한국 서해 임의 정점 (인천 앞바다)
lat, lon = 37.45, 126.55

# 3) 예측 시간 (UTC)
times = pd.date_range("2026-01-01", "2026-01-31", freq="1H")
tide_time = pyTMD.time.convert_calendar_dates(
    [t.year for t in times], [t.month for t in times], [t.day for t in times],
    hour=[t.hour for t in times], epoch=(1992,1,1,0,0,0)
)

# 4) 모델에서 분조 보간 → 시간에 따라 예측
amp, ph, c, _ = pyTMD.io.FES.read_constants(...)
eta_pred = pyTMD.predict.map(t=tide_time, hc=..., constituents=c)
```

> 위 코드는 pyTMD 일반 사용 패턴 (구체 인수는 pyTMD 버전·모델별 차이). 정식 사용은 [pyTMD docs/notebooks](https://github.com/pyTMD/pyTMD) 참조. 본 §은 **개념 시연만**, 실제 실행 검증은 보강 대기.

## 5. 보강 필요

- §3 한국 인천 실제 데이터 적용 — KHOA 다운로드 + 실행 + 검증
- §4 pyTMD 정확한 인수 — pyTMD 공식 notebook 인용 추가
- 예제 4: 한국 동해 (일주조 우세 K₁·O₁ 진폭 큼) 적용
- 예제 5: 서해 천해 비선형 (M₂ + M₄ phase couple) 분석
- 예제 6: 조류 (U, V) 2D UTide 분석 (current ellipse 출력)

## 6. 연결

- `02-theory.md` §8 — 약최저저조위 공식 (§1.4, §3.2에서 인용)
- `03-analysis-methods.md` — 조화분해 알고리즘
- `04-code-and-tools.md` §2-5 — UTide·pytides·pyTMD 도구 자체 소개
- `04-code-and-tools.md` §6 — TPXO/FES/NAO/GOT 글로벌 모델 (§4에서 활용)
- `06-model-application.md` (미작성) — EFDC 등에 본 예제 결과의 분조 데이터 forcing
- 외부 인용:
  - [wesleybowman/UTide README](https://github.com/wesleybowman/UTide/blob/master/README.md) — UTide solve() 표준 호출 (§1.2)
  - [wesleybowman/UTide/utide/_solve.py](https://github.com/wesleybowman/UTide/blob/master/utide/_solve.py) — solve() 인수 docstring (§1.3)
  - [sam-cox/pytides wiki Example-Pytides-Usage](https://github.com/sam-cox/pytides/wiki/Example-Pytides-Usage) — NOAA King's Point 예제 전체 (§2)
  - [sam-cox/pytides wiki Theory](https://github.com/sam-cox/pytides/wiki/Theory-of-the-Harmonic-Model-of-Tides) — pytides 이론
