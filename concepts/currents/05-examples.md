---
title: "조류 — 05 학습 예제 (KHOA 수치조류도)"
topic: currents
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: 실제 KHOA 수치조류도 CSV (813,703 rows) 직접 로드·파싱·정점 추출. 결과 데이터는 검증된 source의 직접 출력. 좌표·단위·한계는 [tides-khoa-cross-verification.md §5] 검증."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 조류 — 05 학습 예제

## 1. 한국 4정점 — 수치조류도 격자 추출

> 출처: `khoa-tide-model` / `해양수산부 국립해양조사원_수치조류도 기반 조화상수_20250814.csv` (cp949, 813,703 rows). 단위: **cm/s** (조류 속도). 위상 기준은 KHOA 공시 별도 확인 필요 (source-needed — 현재 G/g/κ 명시 없음).

### 1.1 추출 코드

```python
import pandas as pd
import numpy as np

df = pd.read_csv(
    "<KHOA_수치조류도_조화상수.csv>",  # khoa-tide-model source (국립해양조사원 수치조류도 기반 조화상수)
    encoding='cp949'
)
df[['lon','lat']] = df['좌표'].str.split(' ', expand=True).astype(float)

# 한국 해역 필터
korea = df[(df.lon.between(124,132)) & (df.lat.between(32,42))].copy()

# 임의 정점 가장 가까운 격자
def nearest_point(lat_t, lon_t):
    s = korea.copy()
    s['dist'] = np.sqrt((s.lon - lon_t)**2 + (s.lat - lat_t)**2)
    return s.nsmallest(1, 'dist').iloc[0]
```

### 1.2 결과 — 4 정점 비교

| 정점 | target (lat, lon) | nearest 격자 | M₂ (cm/s) | S₂ | K₁ | O₁ |
|---|---|---|---|---|---|---|
| 인천 인근 (서해) | (37.45, 126.55) | (37.4490, 126.5525) | **40.22 @ 57.72°** | 14.14 @ 114.79° | 2.20 @ 225.55° | 1.40 @ 190.46° |
| 명량해협 인근 | (34.55, 126.30) | (34.5507, 126.3136) | **41.54 @ 286.78°** | 12.86 @ 329.70° | 3.34 @ 147.06° | 2.23 @ 108.65° |
| 부산 인근 (남해) | (35.10, 129.05) | (35.1033, 129.0494) | **3.34 @ 241.90°** | 1.40 @ 258.66° | 1.04 @ 119.16° | 0.83 @ 77.05° |
| 동해 묵호 인근 | (37.55, 129.12) | **— (격자 없음)** | — | — | — | — |

### 1.3 관찰

**서해·명량 (강함)**:
- M₂ 진폭 ≈ 40-42 cm/s — 한국 서해 일반 통설 (1-3 m/s 왕복성) 대비 **낮은 격자값**
- 격자는 해역 평균값. 명량해협 통과 부근 sub-grid 가속 (5+ m/s)은 미해상

**부산 (약함)**:
- M₂ ≈ 3.34 cm/s — 남해 외해 typical
- 일주조 K₁·O₁이 반일주조 S₂·N₂보다 강함 (form factor 일주조성)
- F = (1.04 + 0.83) / (3.34 + 1.40) = 1.87/4.74 = **0.39** → 혼합조 (mainly semidiurnal)

**동해 (커버리지 없음)**:
- 수치조류도 CSV는 **황해 + 동중국해 + 일부 남해**만 커버
- 동해 (128-131°E, 37-40°N) **0 grid points**
- 동해 조류 분석은 별도 자료 (NAO.99Jb regional 1/12°, 또는 KHOA OpenAPI 조류 관측 직접)

## 2. 수치조류도 데이터 범위 검증

### 2.1 좌표 커버리지

```python
print(f"전체 lon: {df.lon.min():.3f} – {df.lon.max():.3f}")  
print(f"전체 lat: {df.lat.min():.3f} – {df.lat.max():.3f}")
print(f"전체 rows: {len(df):,}")

korea = df[(df.lon.between(124,132)) & (df.lat.between(32,42))]
print(f"한국 해역: {len(korea):,} rows ({100*len(korea)/len(df):.1f}%)")
```

결과 (검증됨):
- 전체 lon: 117.591 – 129.972
- 전체 lat: 25.162 – 40.896
- 전체 rows: 813,703
- 한국 해역 (124-132°E, 32-42°N): **234,738 rows (28.8%)**

### 2.2 동해 누락 확인

```python
east_sea = df[(df.lon.between(128,131)) & (df.lat.between(37,40))]
print(f"동해 (128-131°E, 37-40°N): {len(east_sea)} grid points")
# → 0
```

### 2.3 격자 spacing (서해 sample)

```python
sub = df[(df.lon.between(126,127)) & (df.lat.between(37,38))]
# 3,502 points in 1°×1° (서해 인천 인근)
# lat 간격 median ≈ 0.0002° (≈ 22 m)
# lon 간격 median ≈ 0.011° (≈ 1.2 km)
```

→ **비균일 곡선 격자**. lat 방향 매우 조밀, lon 방향 비교적 sparse. 서해처럼 조류 강한 곳에서 해상도 높임.

## 3. 정점별 검증 — KHOA 조위 조화상수와 정합 확인

조류 진폭 절대값은 조위 진폭과 직접 비교 불가 (다른 물리량). 그러나 **위상**은 비교 가능:
- 인천 조위 M₂ G = 228.79° ([`tides-khoa-cross-verification.md` §3](../../textbook/notes/tides-khoa-cross-verification.md))
- 인천 인근 수치조류도 M₂ 지각 = 57.72°
- 차이 (228.79 - 57.72) = 171.07° ≈ **반대 위상 (180°)**

해석: 조위 만조 시점에서 조류는 turning (게류) → 합리적. 조위와 조류의 90° phase offset이 일반적 (왕복성 천해 조류) — 더 정밀 검증은 격자 위상 기준 (G/g) 확인 후.

## 4. 한계 명시

- **단일 (진폭, 위상) 페어**만 제공 — (Lsmaj, Lsmin, θ, g) 4 parameter 중 일부만. **회전 방향 정보 없음**
- **단위 추정**: 파일명 + range로 cm/s 추정. KHOA 원본 문서 확인 권장
- **위상 기준**: GMT (G) or KST (g) — 명시 없음 (KHOA 공시 자료라 g 추정, 확인 필요)
- **동해 미커버**: 별도 source 필요
- **격자 평균**: sub-grid (명량 협수로 등) 가속 미해상

## 5. ADCP 관측 데이터로 UTide 2D 분석 — 골격

> KHOA 관측 데이터 다운로드 후 실행. 본 §은 코드 골격, 실제 실행은 KHOA OpenAPI 키 확보 후.

```python
import pandas as pd
from utide import solve, reconstruct

# 1) ADCP 데이터 로드 (가정: 시각·u·v 컬럼)
df = pd.read_csv("adcp_observation.csv", parse_dates=["t"])
# 시각대 변환 (KST → UTC, UTide 권장)
df["t_utc"] = df["t"].dt.tz_localize("Asia/Seoul").dt.tz_convert("UTC").dt.tz_localize(None)

# 2) 2D 조화분해
coef = solve(
    df["t_utc"].values, df["u_cm_s"].values, df["v_cm_s"].values,
    lat=35.0,                       # 정점 위도
    nodal=True, trend=True,
    method='robust',                # 천해 비선형 / outlier 강함
    conf_int='linear',
    constit=['M2','S2','K1','O1','N2','K2','M4','MS4','M6'],
)

# 3) 분조별 조류타원 출력
for n, A, a_min, theta, g in zip(coef['name'], coef['Lsmaj'], coef['Lsmin'], coef['theta'], coef['g']):
    rotation = "CCW" if a_min > 0 else "CW" if a_min < 0 else "reversing"
    print(f"{n:>5s}: Lsmaj={A:6.2f} cm/s  Lsmin={a_min:6.2f}  θ={theta:6.1f}°  g={g:6.1f}°  [{rotation}]")

# 4) 임의 시간 예측
t_pred = pd.date_range("2025-01-01","2025-12-31",freq="10min").values
pred = reconstruct(t_pred, coef)
# pred['u'], pred['v'] = 예측 조류 성분

# 5) 수치조류도 격자값과 정합 비교
nearest = nearest_point(target_lat=35.0, target_lon=129.0)  # §1.1 함수
print(f"수치조류도 M2 = {nearest['m2_진폭']:.2f} cm/s @ {nearest['m2_지각']:.2f}°")
# UTide 결과 M2 = coef[name=='M2'] / Lsmaj 와 비교
```

검증 기준:
- UTide M₂ Lsmaj ↔ 수치조류도 격자 M₂ 진폭: 같은 정점에서 ±20% 이내 (격자 해상도 한계)
- 위상 차이: 격자 기준이 명시되면 (G/g 변환) 동일 정밀도로 비교

## 6. 보강

- **수치조류도 위상 기준** (G/g) 확인 — KHOA 원본 문서 별도 조사
- **수치조류도 "진폭"** 정확한 정의 (단일 성분 / |U| / Lsmaj 중 어느 것)
- 동해 조류 별도 자료 — NAO.99Jb regional, KHOA OpenAPI 직접
- ADCP 실측 데이터 사용 시 격자값과 검증 사례 추가 (`experience/`로)
- 명량·진도 실제 관측 사례 (강한 비선형)

## 7. 연결

- `01-concept.md` — 정의·분류
- `02-theory.md` — 조류타원 4 parameter
- `03-analysis-methods.md` — UTide 2D 분석 절차
- `04-code-and-tools.md` — UTide·수치조류도 CSV 코드
- `concepts/tides/05-examples.md` §3 — 인천 조위 조화상수 (위상 정합 비교)
- 소스 노트:
  - [`textbook/notes/tides-khoa-cross-verification.md`](../../textbook/notes/tides-khoa-cross-verification.md) §5 — 수치조류도 단위 검증
