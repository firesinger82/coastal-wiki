---
title: "파랑 — 05 학습 예제 (한국 MPT 정점)"
topic: waves
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference: DASHBOARD/mof_data/ 74 정점 메타데이터 (stations_enriched.json) + 1 정점 raw 시계열 구조 (MPT201, 189,077 records, sgnfctWvhgtVl0 필드 확인). 코드 패턴은 scipy.signal.welch 표준."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 파랑 — 05 학습 예제

## 1. 데이터 출처 — 한국 MPT 74 정점

`dashboard-khoa-data` / `mof_data/`:
- **74 정점** 통합 메타데이터 (`stations_enriched.json`)
- 정점당 raw 시계열 JSON (예: `MPT201_raw.json` = 189,077 records)
- 기관별: KMA (기상청) 29, MOF (해양수산부) 34, KHOA (국립해양조사원) 11
- 해역별: 서해 19, 남해 23, 동해 32

### 1.1 출력 필드 (sample MPT201)

```json
{
  "obsvId": "MPT201",
  "obsvDt": "2014-07-12 10:30:00",
  "sgnfctWvhgtVl0": 0.46,        // 유의파고 H_s (m), sensor 0
  "sgnfctWvhgtVl1": 0.757,        // sensor 1 (백업)
  "pkprdVl0": 5.87,              // 피크 주기 T_p (s)
  "wvdrtVl0": 275.36,            // 파향 (°, 진북 0°, CW)
  "maxWvhgtVl0": null,           // 최대 파고 (있을 때만)
  "maxWvprdVl0": null
}
```

→ 정점·기간에 따라 필드 완성도 차이 (NaN 다수).

## 2. 정점별 통계 — H_s·T_p·방향

### 2.1 분석 코드 (Python)

```python
import pandas as pd
import numpy as np
import json
from pathlib import Path

MOF_DIR = Path("/mnt/d/Numerical_models/01_Models/DASHBOARD/mof_data")

# 정점 메타데이터
sta = json.load(open(MOF_DIR / "stations_enriched.json"))
sta_map = {s['id']: s for s in sta}

def load_station(obs_id):
    """raw JSON → DataFrame"""
    raw = json.load(open(MOF_DIR / f"{obs_id}_raw.json"))
    df = pd.DataFrame(raw)
    df['t'] = pd.to_datetime(df['obsvDt'])
    df['Hs'] = pd.to_numeric(df.get('sgnfctWvhgtVl0'), errors='coerce')
    df['Tp'] = pd.to_numeric(df.get('pkprdVl0'), errors='coerce')
    df['dir'] = pd.to_numeric(df.get('wvdrtVl0'), errors='coerce')
    return df.dropna(subset=['Hs'])

# 정점별 요약
def summarize(obs_id):
    df = load_station(obs_id)
    meta = sta_map[obs_id]
    return {
        'id': obs_id,
        'name': meta['name'],
        'sea': meta['sea'],
        'org': meta['org'],
        'lat': meta['lat'], 'lng': meta['lng'],
        'n': len(df),
        'period': f"{df['t'].min()} ~ {df['t'].max()}",
        'Hs_mean': df['Hs'].mean(),
        'Hs_p95': df['Hs'].quantile(0.95),
        'Hs_max': df['Hs'].max(),
        'Tp_mean': df['Tp'].mean(),
        'Tp_at_Hs_max': df.loc[df['Hs'].idxmax(), 'Tp'] if not df.empty else None,
    }
```

### 2.2 정점 비교 (해역별 대표)

> 실제 통계는 데이터 로드·집계 후 산출. 본 §은 분석 frame.

| 정점 | 해역 | 기관 | typical H_s | 비고 |
|---|---|---|---|---|
| MPT101 덕적도 | 서해 | KMA | ~1.0 m | 인천 외해 |
| MPT235 군산항 | 서해 | MOF | ~0.5 m | 항만 보호 |
| MPT117 서해(170) | 서해 외해 | KMA | ~1.5 m | 외해 buoy |
| MPT003 남해동부 | 남해 | KHOA | ~1.2 m | |
| MPT201 (기장) | 남해 | MOF | ~0.7 m | 부산 인근 |
| MPT222 강릉 | 동해 | MOF | ~0.9 m | |
| MPT237 경주(전동) | 동해 | MOF | ~1.0 m | |
| MPT238 영덕(고래불) | 동해 | MOF | ~1.0 m | 축산항 인근 (사용자 정점) |

→ 정확한 통계는 분석 실행 후 `experience/` 또는 본 페이지 patch.

## 3. JONSWAP 적합 (single observation period)

H_s + T_p + γ ≈ 3.3 가정 하 JONSWAP 스펙트럼 재구성:

```python
import numpy as np

def jonswap_spectrum(f, Hs, Tp, gamma=3.3):
    """JONSWAP variance density spectrum E(f). Holthuijsen §6.3.3.
    f: array of frequencies (Hz)
    Hs: significant wave height (m)
    Tp: peak period (s)
    """
    fp = 1 / Tp
    sigma = np.where(f < fp, 0.07, 0.09)
    # alpha 결정 (Hs로 normalize)
    Gamma = np.exp(-0.5 * ((f - fp) / (sigma * fp))**2)
    # PM shape
    Spm = (5/16) * Hs**2 * fp**4 * f**-5 * np.exp(-1.25 * (f/fp)**-4)
    E = Spm * gamma**Gamma
    # Normalize so that 4*sqrt(m0) = Hs
    m0 = np.trapz(E, f)
    E = E * (Hs**2 / (16 * m0))
    return E

# Example: MPT201 평균 풍파 (Hs=0.7, Tp=5.5)
f = np.linspace(0.02, 0.5, 200)
E_jonswap = jonswap_spectrum(f, Hs=0.7, Tp=5.5)
# m0 검증
m0 = np.trapz(E_jonswap, f)
print(f"H_m0 = 4·sqrt(m0) = {4*np.sqrt(m0):.3f} m  (input H_s = 0.7 m)")
```

> 실제 적합은 관측 스펙트럼 (시계열 → FFT) 과 비교 — `03-analysis-methods.md` §6 참조.

## 4. 한국 해역 wave climate 패턴 (일반론·정량 검증 대기)

| 해역 | H_s 풍파 | T_p 평균 | 우세 방향 | 특이사항 |
|---|---|---|---|---|
| 서해 (황해) | 0.5-1.5 m | 4-7 s | W/NW (겨울 NE 강함) | fetch 짧음, fetch-limited |
| 남해 | 0.7-1.5 m | 5-9 s | S/SE | 외해 너울 영향 |
| 동해 | 0.8-1.5 m | 6-10 s | NE/SE | 깊은 외해, 너울 강함 |

→ MPT 데이터 직접 분석으로 정량 (보강).

## 5. 축산항 사례 (사용자 관심 정점)

**축산항** (경북 영덕, lat=36.510, lon=129.451):
- 가장 가까운 MOF 파랑 정점: **MPT238 영덕(고래불)** (lat=36.577, lon=129.433, distance ≈ **7.5 km**)
- 가장 가까운 KHOA 파랑 정점: **TW_0095 고래불해수욕장** (lat=36.580, lon=129.454, distance ≈ **7.7 km**)
- 자료: `swan-library-firesinger/metadata/validation_stations_chuksan.csv`

축산항 SWAN 시뮬 검증에 위 2 정점 사용.

## 6. spectrum_archive 활용 (`swan-library-firesinger`)

사용자가 구축 중인 **한국 연안 spectrum archive** (3-layer 비전):

### Layer 1 — WINK-compatible Baseline
- 13 middle-domain `NESTOUT` boundary files
- WINK detail-domain boundary files
- Point outputs for validation stations
- Official-style reference dataset

### Layer 2 — General Coastal Spectrum Archive
- 임의 detail-domain boundary 생성용 spectral DB
- 외부 SWAN 재실행 불필요한 nesting 워크플로

### Layer 3 — Suitability Checker
- 새 detail 도메인 boundary가 archive 데이터로 충분한지 자동 판정

→ 사용자 자료 `references/spectrum_archive_roadmap.md` 참조. 본 wiki에서는 별도 experience 또는 [`models/SWAN/source-analysis/spectrum-archive-vision.md`](../../models/SWAN/source-analysis/) (작성 검토).

## 7. 보강·미해결

- 74 정점 전체 통계 산출 (1년·3년·10년) → wave climate 정량
- 정점별 정확한 H_s 분포·JONSWAP 적합 결과 → `experience/`로 검증 후
- TW (KHOA 조위) 정점과 MPT (해양수산부 파랑) 정점 위치 매핑 (축산항·인천 등 주요 지점)
- 방향 스펙트럼 (D(f, θ)) 가용 정점 식별 (multi-sensor 또는 ADCP)
- WINK 도메인 경계 spectrum 시각화

## 8. 연결

- `01-concept.md` — 정의·파라미터
- `02-theory.md` — 분산관계, energy
- `03-analysis-methods.md` — FFT·통계·JONSWAP
- `04-code-and-tools.md` — SWAN·WW3·XBeach + WINK 패턴
- `06-model-application.md` — 본 정점을 모델 검증 reference로
- `experience/` (작성 검토) — 74정점 wave climate 실제 분석
- 외부:
  - 해양수산부 해양 관측 시스템 (MPT 정점)
  - 기상청 해양 기상 정보
  - KHOA 바다누리 파랑 (TW 코드)
