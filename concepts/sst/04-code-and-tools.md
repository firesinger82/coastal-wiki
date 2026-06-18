---
title: "SST 데이터·도구 정리 — KHOA·OISST·HadISST·COBE-SST2·NIFS"
topic: sst
canonical_source: self
citation_status: verified
verification_method: "각 데이터셋의 공식 문서 + 공식 다운로드 URL + 본 위키의 fetch 스크립트 (tools/sst-cross-check/) cross-reference. KHOA endpoint 는 활용가이드 HWP (오픈API 활용가이드_조위관측소 실측 수온.hwp) 직접 추출로 검증. OISST·HadISST·COBE2 endpoint 는 각 기관 공식 데이터 배포 페이지 기준."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — 실제 다운로드·호출 검증"
verification_date: 2026-05-23
related:
  - concepts/sst/01-concept.md
  - concepts/sst/02-theory.md
  - experience/khoa-sst-warming-trend.md
  - experience/khoa-sst-global-crosscheck.md
---

# SST 데이터·도구 정리

> 본 §는 한국 연안 SST 분석에서 자주 쓰이는 5개 데이터셋 (KHOA · NOAA OISST · UKMO HadISST · JMA COBE-SST2 · NIFS KODC) 의 endpoint·인증·호출법·실 사용 예제를 한 곳에 정리.

## 1. 비교 표 — 한 눈에

| 데이터셋 | 종류 | 해상도 | 기간 | API/접근 | 추천 용도 |
|---|---|---|---|---|---|
| **KHOA OpenAPI `surveyWaterTemp`** | in-situ 정점 (49 조위관측소) | 1분~60분 | **2025-01~ 만** | data.go.kr REST | 2025+ 신규 데이터 자동 수집 |
| **NOAA OISST v2.1** | satellite blend (AVHRR + in-situ) | 0.25° daily/monthly | 1981.09~ | NOAA PSL NetCDF | 한국 연안 high-res, 정점별 매칭 |
| **UKMO HadISST v1.1** | ship/buoy reconstruction | 1° monthly | 1870.01~ | UKMO NetCDF | long-term reference (150+ 년) |
| **JMA COBE-SST2** | ICOADS reconstruction | 1° monthly | 1850.01~ | NOAA PSL 미러 NetCDF | 최장 baseline (176+ 년), JMA primary |
| **NIFS KODC 정선** | in-situ 정선 (25 lines, 207 정점) | 시·정점 | **1968~** | form-based CSV | 한국 climate trend 학계 primary |

## 2. KHOA OpenAPI — 조위관측소 실측 수온 (`surveyWaterTemp`)

### 2.1 엔드포인트

```
https://apis.data.go.kr/1192136/surveyWaterTemp/GetSurveyWaterTempApiService
```

서비스 ID: `SV-AP-02-008`, 배포: 2025-03-14. archive 시작: **2025-01-01** (이전 일자는 NODATA_ERROR).

### 2.2 필수·옵션 파라미터

| 파라미터 | 필수? | 예시 | 비고 |
|---|---|---|---|
| `serviceKey` | ✓ | `RT7WPP...` | **URL-decoded** 형식 (data.go.kr 발급 키의 raw 값) |
| `type` | ✓ | `json` | `json` 또는 `xml` |
| `obsCode` | ✓ | `DT_0001` | 조위관측소 코드 (DT_xxxx, IE_xxxx) |
| `reqDate` | 옵션 | `20250904` | YYYYMMDD, 기본값 현재일 |
| `min` | 옵션 | `60` | 시간 간격 (1~60, 기본값 1, 최댓값 60) |
| `numOfRows` | 옵션 | `24` | 페이지당 결과 수 (기본 10, 최대 300) |
| `pageNo` | 옵션 | `1` | 페이지 번호 |

### 2.3 응답 필드

```json
{
  "header": {"resultCode": "00", "resultMsg": "NORMAL_SERVICE"},
  "body": {
    "items": {"item": [
      {"obsvtrNm": "인천", "lat": 37.45194, "lot": 126.59222,
       "obsrvnDt": "2025-09-04 03:00:00", "wtem": 28.4}
    ]}
  }
}
```

| 필드 | 의미 | 단위 |
|---|---|---|
| `obsvtrNm` | 관측소 이름 (한국어) | — |
| `lat`, `lot` | 위도, 경도 (lot 은 typo, 'lon' 의미) | ° |
| `obsrvnDt` | 관측 일시 (KST) | YYYY-MM-DD HH:MM:SS |
| `wtem` | 수온 | °C |

### 2.4 호출 예제 (Python)

```python
import os, requests
from urllib.parse import unquote

# KEY 는 환경변수에 — URL-decoded 형태로 사용
key = unquote(os.environ['KHOA_API_KEY'])  # decoded 키 필요 (requests 가 재인코딩)

url = "https://apis.data.go.kr/1192136/surveyWaterTemp/GetSurveyWaterTempApiService"
params = {
    "serviceKey": key,
    "type": "json",
    "obsCode": "DT_0001",
    "reqDate": "20250904",
    "min": 60,
    "numOfRows": 24,
}
r = requests.get(url, params=params, timeout=15)
data = r.json()
if data['header']['resultCode'] == '00':
    for it in data['body']['items']['item']:
        print(it['obsrvnDt'], it['wtem'])
else:
    print("error:", data['header']['resultMsg'])
```

### 2.5 주요 obsCode (조위관측소, KHOA Annual Report 2025)

한국 연안 주요 조위관측소 예시:

| code | 정점 | 해역 | 좌표 |
|---|---|---|---|
| DT_0001 | 인천 | 서해 | 37.45, 126.59 |
| DT_0007 | 목포 | 서해 | 34.78, 126.38 |
| DT_0028 | 진도 | 서해 | 34.38, 126.31 |
| DT_0005 | 부산 | 남해 | 35.10, 129.04 |
| DT_0016 | 여수 | 남해 | 34.75, 127.77 |
| DT_0029 | 거제도 | 남해 | 34.81, 128.70 |
| DT_0031 | 거문도 | 남해 | 34.03, 127.31 |
| DT_0004 | 제주 | 남해 | 33.53, 126.54 |
| DT_0010 | 서귀포 | 남해 | 33.24, 126.56 |
| DT_0020 | 울산 | 동해 | 35.50, 129.39 |
| DT_0091 | 포항 | 동해 | 36.04, 129.38 |
| DT_0006 | 묵호 | 동해 | 37.55, 129.12 |
| DT_0012 | 속초 | 동해 | 38.21, 128.59 |

전체 목록은 활용가이드 HWP (1.1.2 코드 정보) 참조.

### 2.6 에러 코드

| code | 의미 | 흔한 원인 |
|---|---|---|
| `00` | NORMAL_SERVICE | 정상 |
| `03` | NODATA_ERROR | 해당 일자 데이터 없음 (2024 이전 또는 관측 안 됨) |
| `99` | UNKNOWN_ERROR | 서버 내부 오류 (재시도) |
| `30` | SERVICE_KEY_IS_NOT_REGISTERED_ERROR | 키 등록 안 됨 |
| `31` | DEADLINE_HAS_EXPIRED_ERROR | 키 만료 |

### 2.7 활용 패턴

```bash
# 환경변수
export KHOA_API_KEY="<encoded key from data.go.kr>"
# 매일 정점별 시간별 SST 수집 (cron)
uv run python tools/khoa-validation/fetch_khoa_temp.py  # (스크립트 추후 작성)
```

**중요 주의**: data.go.kr 키는 두 가지 형식 (encoded `%2F%3D` 포함 / decoded `/+=` 포함). Python `requests` 는 params 인자가 자동 URL-encoding 하므로 **decoded 형식** 필요. `urllib.parse.unquote()` 로 변환.

## 3. NOAA OISST v2.1

### 3.1 다운로드

| 항목 | 값 |
|---|---|
| Monthly mean | `https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc` |
| Daily | `https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.day.mean.<YYYY>.nc` |
| 해상도 | 0.25° × 0.25° |
| 시계열 | 1981.09 ~ 현재 |
| 파일 크기 | monthly: ~2 GB, daily/year: ~250 MB |
| 인증 | 없음 (open) |

### 3.2 변수 이름

```python
import xarray as xr
ds = xr.open_dataset("sst.mon.mean.nc")
# ds.sst — SST (°C)
# ds.lat, ds.lon — 0.25° grid (lon 은 0-360 convention)
# ds.time — 월 시작일
```

### 3.3 정점 매칭 (한국 연안 land-pixel fallback)

OISST 0.25° 격자에서 한국 좁은 만·항구 정점은 육지 픽셀로 매핑될 수 있음. `tools/sst-cross-check/fetch_oisst_monthly.py` 의 `find_nearest_ocean()` 함수 — spiral neighborhood 검색으로 최인접 ocean pixel 추출 (좁은 만·항구 정점에서 LAND→sea fallback 적용).

### 3.4 직접 다운로드 예제

```bash
cd ~/coastal-wiki/data/sst-global
wget https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc
```

또는 사용된 스크립트:
```bash
uv run python tools/sst-cross-check/fetch_oisst_monthly.py
```

## 4. UKMO HadISST v1.1

### 4.1 다운로드

| 항목 | 값 |
|---|---|
| URL | `https://www.metoffice.gov.uk/hadobs/hadisst/data/HadISST_sst.nc.gz` |
| 해상도 | 1° × 1° |
| 시계열 | 1870.01 ~ 현재 |
| 파일 크기 | ~ 230 MB (gz), ~ 460 MB (unpacked) |
| 인증 | 없음 (open) |

### 4.2 변수 이름·차원

```python
ds = xr.open_dataset("HadISST_sst.nc")
# ds.sst — SST (°C). 단, land/ice 는 매우 음수 (예: -1000)
# 처리: ds.sst.where(ds.sst > -100) → NaN mask
# ds.latitude (89.5 ~ -89.5), ds.longitude (-179.5 ~ 179.5)
# ds.time — 월 중간일
```

### 4.3 한국 정점 fetch

```bash
uv run python tools/sst-cross-check/fetch_hadisst.py
```

→ 정점별 156년 monthly SST CSV 산출.

## 5. JMA COBE-SST2

### 5.1 다운로드

| 항목 | 값 |
|---|---|
| URL (PSL 미러) | `https://downloads.psl.noaa.gov/Datasets/COBE2/sst.mon.mean.nc` |
| 원본 (JMA NEAR-GOOS) | `https://ds.data.jma.go.jp/goos/data/rrtdb/jma-pro/cobe2_sst_glb_M.html` |
| 해상도 | 1° × 1° |
| 시계열 | **1850.01 ~ 현재** (가장 긴 reanalysis) |
| 파일 크기 | ~ 523 MB |
| 인증 | 없음 (open, PSL 미러 사용 권장) |

### 5.2 변수·호출

```python
ds = xr.open_dataset("cobe2_sst_mon_mean.nc")
# ds.sst — SST (°C), 약 NaN-aware
# ds.lat, ds.lon (0-360), ds.time
```

### 5.3 한국 정점 fetch

```bash
uv run python tools/sst-cross-check/fetch_cobe2.py
```

## 6. NIFS KODC 정선해양관측

### 6.1 접근

| 항목 | 값 |
|---|---|
| URL | `https://www.nifs.go.kr/kodc/observe/line/data` |
| 접근 | **form-based, CSV download** (API 없음) |
| 인증 | 사용자 분류 (기관·교육·종사자) + 용도 입력 |
| 해상도 | 정선 × 정점 × 수심 |
| 시계열 | 1968 ~ 현재 (55+ 년) |

### 6.2 측정 변수

수온(°C), 염분(psu), 용존산소(ml/L), 인산염인(μmol/L), 아질산질소·질산질소·규산규소, 클로로필(µg/L), pH, 투명도(m), 기압(hPa).

### 6.3 수동 다운로드 절차 (별도 가이드)

`research/inbox/` 또는 별도 노트에 상세 가이드 작성 예정. 핵심:
1. 위 URL 접속
2. 해역 (동해/서해/남해/동중국해) → 정선 → 정점 선택
3. 측정 변수 (수온 등) 선택
4. 사용자 분류 + 용도 입력
5. CSV 다운로드

자동화 어려움 — Selenium 등 브라우저 자동화 필요. 현재는 수동.

### 6.4 Published 값 (인용 가능)

- **NIFS Fish Aquat Sci 2023** (Han et al., DOI 10.47853/FAS.2023.e54)
  - 1968-2022, 25 정선 × 207 정점
  - 한국 연안 SST trend: **0.025 °C/year** = 0.25 °C/decade
  - 한국 연안 OHC trend: 동해 0.148, 남해 0.089, 서해 0.061 × 10¹⁸ J/year

## 7. 본 위키 통합 분석 스크립트

| 스크립트 | 기능 |
|---|---|
| `tools/sst-cross-check/fetch_oisst_monthly.py` | OISST v2.1 다운로드 + 정점 추출 |
| `tools/sst-cross-check/fetch_hadisst.py` | HadISST 다운로드 + 정점 추출 |
| `tools/sst-cross-check/fetch_cobe2.py` | COBE-SST2 다운로드 + 정점 추출 |
| `tools/sst-cross-check/analyze_global_trends.py` | window × dataset 선형회귀 |

재현:
```bash
cd ~/coastal-wiki
uv sync                                                     # 의존성 (한 번)
uv run python tools/sst-cross-check/fetch_oisst_monthly.py  # ~3분
uv run python tools/sst-cross-check/fetch_hadisst.py        # ~3분
uv run python tools/sst-cross-check/fetch_cobe2.py          # ~3분
uv run python tools/sst-cross-check/analyze_global_trends.py # <10초
```

## 8. 데이터 선택 가이드

목표별 추천:

| 분석 목적 | 추천 데이터셋 |
|---|---|
| 한국 정점 정밀 in-situ (최근 1년+) | KHOA `surveyWaterTemp` (2025+) |
| 한국 정점 정밀 in-situ (장기) | KHOA Annual Report 백서 추출 또는 NIFS published |
| 한국 정점 정밀 in-situ (1968+ raw) | NIFS KODC 수동 다운로드 |
| 한국 정점 satellite 비교 (1982+) | OISST v2.1 (정점별 매칭 가능) |
| 한국 연안 long-term climate (1870+) | HadISST 또는 COBE-SST2 |
| 한국 연안 가장 긴 baseline (1850+) | COBE-SST2 |
| 동·서·남해 평균 trend | 3-dataset cross-check 권장 (단일 reanalysis 신뢰 risk) |
| Marine heatwave 일별 분석 | OISST daily (0.25°) 또는 MUR (0.01°) |
| 수직 profile (수심별) | NIFS 정선 다층 (수동) |

## 9. 연결

- [`concepts/sst/01-concept.md`](01-concept.md) — 정의·측정 정형화
- [`concepts/sst/02-theory.md`](02-theory.md) — Stewart §5 heat budget
- [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) — KHOA in-situ 분석
- [`experience/khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md) — 글로벌 cross-check
- [`tools/sst-cross-check/`](../../tools/sst-cross-check/) — fetch + analysis 스크립트
- 외부:
  - [NOAA PSL — OISST](https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html)
  - [UKMO — HadISST](https://www.metoffice.gov.uk/hadobs/hadisst/)
  - [JMA — COBE-SST2](https://ds.data.jma.go.jp/tcc/tcc/products/elnino/cobesst2_doc.html)
  - [NIFS KODC](https://www.nifs.go.kr/kodc/)
  - [KHOA OpenAPI](https://www.data.go.kr/data/15142506/openapi.do) (조위관측소 실측 수온)
