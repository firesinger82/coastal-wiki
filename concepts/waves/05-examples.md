---
title: "파랑 — 05 학습 예제"
topic: waves
canonical_source: self
citation_status: verified
verification_method: "코드 패턴은 scipy.signal.welch / numpy 표준. JONSWAP 식은 Holthuijsen §6.3.3. wave climate 정량은 KHOA Annual Report 2025 출처."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 파랑 — 05 학습 예제

## 1. 관측 자료 필드 구조 (한국 MPT 정점)

해양수산부(MOF)·기상청(KMA)·국립해양조사원(KHOA) MPT 파랑 관측 정점은 정점별 raw 시계열 JSON으로 제공된다. 정점·기간에 따라 필드 완성도 차이 (NaN 다수).

### 1.1 출력 필드 (예시)

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

## 2. 정점별 통계 — H_s·T_p·방향 (분석 코드 예제)

> 아래는 raw 시계열 → 정점별 요약 통계 산출의 일반 패턴 (교육용 예제, 경로·정점은 가정값).

```python
import pandas as pd
import numpy as np
import json
from pathlib import Path

MOF_DIR = Path("./mof_data")  # 관측 자료 디렉토리 (사용자 지정)

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

## 4. 한국 해역 wave climate 패턴

### 4.1 일반 통설 + KHOA 2025 정량

| 해역 | H_s 풍파 | T_p 평균 | 우세 방향 | 특이사항 |
|---|---|---|---|---|
| 서해 (황해) | 0.5-1.5 m | 4-7 s | W/NW (겨울 NE 강함) | fetch 짧음, fetch-limited |
| 남해 | 0.7-1.5 m | 5-9 s | S/SE | 외해 너울 영향 |
| 동해 | 0.8-1.5 m | 6-10 s | NE/SE | 깊은 외해, 너울 강함 |

### 4.2 KHOA Annual Report 2025 — 정량 통계 (`khoa-annual-reports`)

§3 자료 분석 결과 §3.19 발췌:

> **2025년 월별 해역별 최대 유의파고 평균**: 3월 **3.97 m** (전 해역 평균). 해역별 최대: **동해안 4.55 m** (3월).
>
> **2025년 누년 편차 (2025 − 누년)**: 전 기간 낮은 경향, **9월 −4.37 m** (가장 큰 음의 편차).

→ 2025년은 누년 대비 **낮은 wave activity** 연도. 특히 9월 (태풍 시즌) 누년 대비 매우 낮음.

### 4.3 14년 추세 분석 가능성

`khoa-annual-reports` 2012-2025 시계열로 가능:
- 정점별 연평균 H_s 추세 (sea state climate change)
- extreme 빈도 (P95·P99·max) 변동
- 풍계 변동 (계절 풍 패턴)

→ `experience/khoa-annual-climate-trend.md` (작성 검토).

> 한국 특정 지점(예: 영덕·축산항 인근) 적용 사례는 바이블 검증(객관 데이터) 후 `experience/`에 카테고리화 — 본 canonical 미수록. [citation_status: source-needed]

## 5. 보강·미해결

- 정점 전체 통계 산출 (1년·3년·10년) → wave climate 정량
- 정점별 정확한 H_s 분포·JONSWAP 적합 결과 → `experience/`로 검증 후
- TW (KHOA 조위) 정점과 MPT (해양수산부 파랑) 정점 위치 매핑
- 방향 스펙트럼 (D(f, θ)) 가용 정점 식별 (multi-sensor 또는 ADCP)

## 6. 연결

- `01-concept.md` — 정의·파라미터
- `02-theory.md` — 분산관계, energy
- `03-analysis-methods.md` — FFT·통계·JONSWAP
- `04-code-and-tools.md` — SWAN·WW3·XBeach
- `06-model-application.md` — 관측 정점을 모델 검증 reference로
- `experience/` (작성 검토) — 정점 wave climate 실제 분석
- 외부:
  - 해양수산부 해양 관측 시스템 (MPT 정점)
  - 기상청 해양 기상 정보
  - KHOA 바다누리 파랑 (TW 코드)
