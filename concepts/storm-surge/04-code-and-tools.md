---
title: "Storm Surge 도구·데이터 — ADCIRC NWS·OWI·SWAN coupling·KHOA observation"
topic: storm-surge
canonical_source: self
citation_status: verified
verification_method: "ADCIRC source-code level NWS 분석 (models/ADCIRC/source-analysis/storm-surge/ 7개 노트, 본 위키 promote 완료) + ADCIRC theory (Luettich & Westerink 2004) + KHOA OpenAPI surveyTideLevel 운영 (본 위키 [`concepts/tides/04-code-and-tools.md`](../tides/04-code-and-tools.md) 인용 + 본 위키 직접 fetch 경험)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — ADCIRC source-analysis + KHOA API cross-ref"
verification_date: 2026-05-23
related:
  - concepts/storm-surge/01-concept.md
  - concepts/storm-surge/02-theory.md
  - models/ADCIRC/source-analysis/storm-surge/
---

# Storm Surge 도구·데이터

> 본 §는 한국 storm surge 실무에 자주 쓰이는 모델·데이터·API 운영 정리.

## 1. ADCIRC NWS 모드 — meteorological forcing 입력 옵션

ADCIRC 의 `fort.15` 의 `NWS` 파라미터로 meteorological forcing source 결정. 상세 source-code 분석은 [`models/ADCIRC/source-analysis/storm-surge/`](../../models/ADCIRC/source-analysis/storm-surge/) 의 7 노트 참조.

### 1.1 NWS 모드 일람

| NWS | source | 형식 | 한국 typical 사용 |
|---|---|---|---|
| **0** | no meteo | — | 조석 단독 (storm 없는 baseline) |
| **6** | 단순 wind/pressure | 일정 grid time series | 학습용 |
| **12** | OWI ASCII | Oceanweather Inc. 분리 win/pre | 미국·유럽 운영 |
| **13** | OWI NetCDF | 동일, NetCDF | **한국 JMA-MSM 운영** (사용자 워크플로) |
| **14** | GRIB2 | direct | NWP raw 입력 |
| **19** | AHM (Asymmetric Holland Model) | parametric TC + Best Track | 단일 태풍 학술 분석 |
| **20** | GAHM (Generalized AHM) | quadrant-dependent | **modern 권장**, ATCF + 4-quadrant |
| **29** | AHM + OWI | hybrid (vortex + background) | 태풍 + 백그라운드 NWP |
| **30** | GAHM + OWI | 동일, GAHM | 가장 정밀, 권장 |

### 1.2 한국 운영 워크플로 — NWS=13 (JMA-MSM)

사용자 표준 워크플로 (modeling-wiki → 본 위키 promote 완료):

- 입력: JMA-MSM (일본기상청 Mesoscale Model) → NetCDF
- ADCIRC 의 NWS=13 reader (`owiwind_netcdf.F:215, 681, 747`) 가 직접 읽음
- 상세 운영 룰: [`models/ADCIRC/source-analysis/storm-surge/adcirc-jma-msm-nws13-foundation.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-jma-msm-nws13-foundation.md)
- `fort.15` 핵심 필드: [`adcirc-fort15-nws13-operating-rules.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-fort15-nws13-operating-rules.md)

### 1.3 NWS=20 GAHM 권장 이유

| 항목 | NWS=19 AHM | NWS=20 GAHM |
|---|---|---|
| Holland B | 단일 record 별 | quadrant-dependent (4개) |
| Rmax | 단일 | quadrant-dependent |
| BL Vmax | 별도 | ATCF wind radii 로부터 fitting |
| Best Track | basic | extended (ATCF + appended fields) |

NWS=20 GAHM 은 NWS=19 의 일반화 — 비대칭 storm 구조 더 정확. 본 위키 노트: [`adcirc-storm-surge.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge.md) 가 source-code level 디테일.

## 2. ADCIRC 입력 파일

### 2.1 `fort.15` (control file)

ADCIRC 의 모든 parameter. 핵심 storm-surge 관련 필드:

| 필드 | 의미 |
|---|---|
| `NWS` | meteorological forcing source (위 §1.1) |
| `NOIVB` | inverse-barometer suppression flag |
| `RampMete` | vortex spin-up ramp (sec) — typical 1-2 days |
| `WTIMINC` | met forcing time increment |
| `BLAdj` | boundary-layer adjustment (NWS=20) |
| `GEOFACTOR` | geostrophic vs cyclostrophic balance |
| `IM` | drag coefficient option (Garratt, Powell 등) |
| `TAU0` | numerical weighting (typical 0.01) |

### 2.2 `fort.14` (mesh)

unstructured triangular mesh — 한국 ADCIRC 적용 시 일반적으로 수 십만 ~ 수 백만 nodes. 한국 서해·남해 dense, 외해 coarse.

### 2.3 `fort.22` (wind/pressure)

forcing 데이터 — NWS 따라 형식 다름:
- NWS=12/13/14: gridded wind/pressure
- NWS=19/20/29/30: ATCF Best Track + appended quadrant fields

### 2.4 `fort.61-65` (출력)

| 파일 | 내용 |
|---|---|
| `fort.61` | tide-only elevation (stations) |
| `fort.62` | tide-only velocity (stations) |
| `fort.63` | full elevation (all nodes) |
| `fort.64` | full velocity (all nodes) |
| `maxele.63` | **maximum elevation envelope** (surge map) |
| `maxvel.63` | max velocity envelope |

## 3. SWAN + ADCIRC coupling

연안 storm surge + wave setup 동시 모델링:

- ADCIRC = water level + 2DDI/3D current
- SWAN = wave spectral
- Coupled (Dietrich et al. 2011) — radiation stress 통해 wave setup 추가

코드: ADCIRC+SWAN 통합 binary, mesh 공유.

본 위키 [`concepts/waves/`](../waves/) 의 SWAN 자료 + [`models/SWAN/`](../../models/SWAN/) 의 source-analysis 와 결합 가능.

## 4. KHOA observation — storm surge 관측 데이터

### 4.1 실시간 조위 관측

KHOA OpenAPI `surveyTideLevel` — 자세한 사용법은 [`concepts/tides/04-code-and-tools.md`](../tides/04-code-and-tools.md) §3 참조.

storm 시 관측 surge 추출:

```python
import os, requests
from urllib.parse import unquote
key = unquote(os.environ['KHOA_API_KEY'])

# 인천 (DT_0001), Hinnamnor 2022-09-06 직접 영향 시점
url = "https://apis.data.go.kr/1192136/surveyTideLevel/GetSurveyTideLevelApiService"
params = {
    "serviceKey": key,
    "type": "json",
    "obsCode": "DT_0001",
    "reqDate": "20220906",
    "min": 10,  # 10분 단위
    "numOfRows": 144,  # 24시간 × 6 = 144
}
r = requests.get(url, params=params, timeout=20)
data = r.json()
# data['body']['items']['item'] 의 tdlvHgt (실측) vs bscTdlvHgt (예측)
# surge = tdlvHgt - bscTdlvHgt
```

### 4.2 한국 정점 surge 분리 (residual)

총 sea level 에서 tide 예측값 빼기:

$$\eta_{surge}(t) = \eta_{obs}(t) - \eta_{tide,pred}(t)$$

KHOA OpenAPI 가 둘 다 제공 (`tdlvHgt` 실측, `bscTdlvHgt` 예측). 차이가 storm-induced surge.

### 4.3 한국 13 정점 코드

[`concepts/sst/04-code-and-tools.md`](../sst/04-code-and-tools.md) §2.5 의 표 동일 — KHOA SST 와 같은 정점들의 tide gauge.

| code | 정점 | 해역 |
|---|---|---|
| DT_0001 | 인천 | 서해 |
| DT_0005 | 부산 | 남해 |
| DT_0004 | 제주 | 남해 |
| DT_0010 | 서귀포 | 남해 |
| ... 외 9개 ... | | |

## 5. NWP (Numerical Weather Prediction) forcing 데이터

ADCIRC NWS=12/13/14 입력 NWP source:

| Source | 해상도 | 한국 가용성 |
|---|---|---|
| **JMA-MSM** | 5 km × 5 km | 한국 ADCIRC 운영 표준 (NWS=13 사용자 워크플로) |
| KMA UM | 1.5 km | 국내 운영, NetCDF 변환 필요 |
| ECMWF IFS | 0.1° / 0.25° | 글로벌, ERA5 reanalysis 한정 사용 |
| NOAA GFS | 0.25° | 글로벌, 운영 forecast |
| OWI (Oceanweather Inc.) | 다양 | 미국·태평양 운영 |

## 6. 한국 storm surge 적용 패키지·도구

| 도구 | 용도 |
|---|---|
| **ADCIRC** | primary unstructured surge 모델 (한국 KMOU·KIOST·기상청 모두 사용) |
| Delft3D-FLOW | 3D + sediment 결합 surge (단점: 구조 grid) |
| SCHISM | unstructured (ADCIRC 대안, growing) |
| SLOSH | NOAA NHC 단순 운영 (한국 미사용) |
| ASGS | ADCIRC Surge Guidance System (운영 wrapper) |
| ADCIRCpy | Python wrapper (`models/ADCIRC/raw/source_code/adcircpy/`) |
| AdcircModules | C++ utility (mesh manipulation) |

## 7. 운영 예제 — 한국 태풍 hindcast 워크플로

전형적 한국 태풍 hindcast (예: Hinnamnor 2022) 단계:

1. **태풍 best track** — JMA RSMC 또는 KMA → ATCF format 변환
2. **JMA-MSM NetCDF** download — 태풍 기간 + 3일 spin-up (RampMete)
3. **ADCIRC mesh** — 한국 ECS-Korea mesh (학계 표준 형태) 또는 사용자 정의
4. **`fort.15`** 편집:
   - `NWS = 13`
   - `RampMete = 86400` (1 day spin-up)
   - `NOIVB = 0` (IB 포함)
5. **ADCIRC 실행** — MPI parallel, 보통 64-256 cores
6. **검증** — KHOA 정점 surge (관측 vs 모델 hindcast)
7. **maxele.63 → 한국 연안 surge envelope map** (matplotlib + cartopy)

상세 절차 — [`adcirc-storm-surge-requirements-checklist.md`](../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-requirements-checklist.md)

## 8. 검증 metrics

surge 모델 검증 시 standard metrics:

| Metric | 정의 | 한국 ADCIRC typical |
|---|---|---|
| RMSE (peak) | 관측 peak vs 모델 peak | 0.1-0.3 m |
| Phase error | timing difference (hours) | ±1-3 h |
| Skill score (Willmott 1981) | $1 - \sum(O-M)^2 / \sum(|M-\bar{O}| + |O-\bar{O}|)^2$ | > 0.85 (well-tuned) |
| Maximum envelope RMSE | spatial max surge | 0.2-0.5 m |

## 9. 외부 자료·논문

- ADCIRC user docs: `models/ADCIRC/raw/manuals/`
- ADCIRC theory: [`adcirc_theory_2004_12_08.pdf`](../../models/ADCIRC/raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf) (Luettich & Westerink 2004)
- Dietrich et al. (2011) "Modeling hurricane waves and storm surge using integrally-coupled, scalable computations" Coastal Engineering 58:45-65
- Willmott, C.J. (1981) "On the validation of models" Physical Geography 2:184-194
- 한국 적용:
  - Kim et al. 2014 "ADCIRC application to typhoon storm surges in Korea" — citation TODO
  - 한국 동해·서해 mesh resources — KMOU·KIOST 보유 (학회 발표 기준)

## 10. 연결

- [`01-concept.md`](01-concept.md) — 정의·5 인자
- [`02-theory.md`](02-theory.md) — equation level (Pugh Ch 6 + ADCIRC GWCE)
- [`models/ADCIRC/source-analysis/storm-surge/`](../../models/ADCIRC/source-analysis/storm-surge/) — 7 source-code 노트
- [`concepts/tides/04-code-and-tools.md`](../tides/04-code-and-tools.md) §3 — KHOA OpenAPI 인용
- [`concepts/sst/04-code-and-tools.md`](../sst/04-code-and-tools.md) §2 — KHOA 13정점 코드
- [`concepts/waves/`](../waves/) — SWAN coupling 자료
