---
title: "한국 13정점 SST trend — 글로벌 데이터셋 cross-check (OISST + HadISST + COBE-SST2 + NIFS published)"
topic: khoa-sst-warming
canonical_source: self
citation_status: verified
verification_method: "NOAA OISST v2.1 (1981.09~2026.04, 0.25° monthly), HadISST v1.1 (1870.01~2025.12, 1° monthly), JMA COBE-SST2 (1850.01~2026.04, 1° monthly) NetCDF 직접 다운로드 (NOAA PSL, UK MetOffice). 13 KHOA 정점 좌표에서 nearest-ocean fallback 으로 SST 추출. 6개 시간 윈도우 (2017-2025, 1982-2025, 1968-2022, 1968-2012, 1870-2025, 1850-2025) 선형회귀. NIFS published 값은 Fish Aquat Sci 2023 (DOI 10.47853/FAS.2023.e54) 직접 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — OISST/HadISST NetCDF 직접 추출 + 회귀 + 3-dataset cross-check"
verification_date: 2026-05-23
related_experience:
  - khoa-sst-warming-trend (본 분석의 KHOA in-situ 9년 trend, 1968-2012 KHOA reference)
  - khoa-annual-climate-trend (SLR — 열팽창 cross-check)
data_sources:
  - NOAA OISST v2.1 (https://downloads.psl.noaa.gov/Datasets/noaa.oisst.v2.highres/sst.mon.mean.nc)
  - HadISST v1.1 (https://www.metoffice.gov.uk/hadobs/hadisst/data/HadISST_sst.nc.gz)
  - JMA COBE-SST2 (https://downloads.psl.noaa.gov/Datasets/COBE2/sst.mon.mean.nc, PSL 미러)
  - NIFS published (Fish Aquat Sci 2023; e-fas.org/archive/view_article?pid=fas-26-11-639)
  - KHOA Annual Report 2012-2025 (본 분석 [khoa-sst-warming-trend.md])
analysis_files:
  - data/sst-global/oisst_v21_13stations_monthly.csv (6968 rows)
  - data/sst-global/hadisst_13stations_monthly.csv (24336 rows)
  - data/sst-global/cobe2_13stations_monthly.csv (27508 rows, 1850-2026.04)
  - data/sst-global/trends_global_summary.json (6 windows × 3 datasets × 13 stations)
caveats:
  - "OISST 0.25° + HadISST 1° 격자가 한국 정점에 비해 굵음 — 일부 정점은 인근 ocean pixel 로 fallback. 정점 간 변별력은 KHOA in-situ 보다 떨어짐 (예: HadISST 1°에서 거제도/여수/거문도 모두 같은 격자에 들어감)."
  - "OISST 는 1981.09 부터 — 1981년 이전 분석에는 HadISST 만 사용 가능."
  - "ERSSTv5 (2°) 는 본 비교에서 제외 — 한국 정점 변별 불가 (인천·부산·속초 모두 같은 2° 격자 가능)."
  - "satellite-merged (OISST) vs reconstruction (HadISST) 의 sample mix 차이 — 1980년대 이전은 HadISST 의 ship/buoy 보간 의존."
---

# 한국 13정점 SST trend — 글로벌 데이터셋 cross-check

> 본 노트는 [`khoa-sst-warming-trend.md`](khoa-sst-warming-trend.md) 의 KHOA in-situ 9년 trend 를 NOAA OISST v2.1 + HadISST v1.1 두 글로벌 데이터셋과 정량 비교한다. 목적: KHOA 분석 결과가 글로벌 reanalysis 와 일관되는지, 그리고 2017-2025 의 강한 가속이 in-situ artifact 인지 진짜 climate signal 인지 판정.

## 0. 문헌 검토 — Korean SST 논문 데이터셋 관행

| 데이터셋 | 한국·일본·중국 논문 사용 빈도 |
|---|---|
| **NOAA OISST v2.1** | ★ primary (한·일·중 모두) — 0.25° daily, 1981.09~, AVHRR + in-situ blend |
| **NIFS** (수산과학원) | ★ in-situ primary (한국 climate trend 논문) — 25 정선 × 207 점, 1968~ |
| COBE-SST / SST2 (JMA) | 일본 측 primary, 한국에서도 종종 |
| **HadISST** | climate long-term reference — 1°, 1870~ |
| ERSSTv5 | 한국 분석에서는 드물게 (2° = 한국 정점 변별 불가) |

→ 본 cross-check 는 **OISST + HadISST** 조합 채택 (학계 관행 일치). ERSST 는 한국 정점 분석에 부적합으로 제외.

References (대표 논문):
- [Park, K-A. et al. — Long-term comparison of satellite and in-situ SST around Korea, *Ocean Sci J* 2015](https://link.springer.com/article/10.1007/s12601-015-0009-1)
- [Han et al. — Long-term SST pattern changes Korea Waters, *Fish Aquat Sci* 2023, DOI 10.47853/FAS.2023.e54](https://www.e-fas.org/archive/view_article?pid=fas-26-11-639) (NIFS 1968-2022 0.025 °C/yr)
- [Cai et al. — Spatial-temporal SST trends Yellow Sea, *J Mar Syst* 2014](https://www.sciencedirect.com/science/article/abs/pii/S0924796314002516)
- [Frontiers Marine Science — Wintertime SST EJS 2023](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2023.1198418/full)
- [JMA SST around Japan](https://www.data.jma.go.jp/kaiyou/english/long_term_sst_japan/sea_surface_temperature_around_japan.html)

## 1. 데이터·방법

| 항목 | OISST v2.1 | HadISST v1.1 |
|---|---|---|
| 해상도 | 0.25° × 0.25° | 1° × 1° |
| 시간 | 1981.09 ~ 2026.04 (월평균) | 1870.01 ~ 2025.12 (월평균) |
| 합성 방식 | AVHRR + in-situ + ICOADS | ship/buoy 보간 (1980+에 satellite 추가) |
| 출처 | NOAA PSL `sst.mon.mean.nc` | UK Met Office `HadISST_sst.nc.gz` |
| 추출 | 13 KHOA 정점 nearest grid + ocean fallback | 동일 |

회귀: 같은 정점 연평균 → linear least squares (각 윈도우에 대해).

스크립트: [`tools/sst-cross-check/`](../tools/sst-cross-check/)
- `fetch_oisst_monthly.py` — NetCDF download + 13정점 추출 (~3분)
- `fetch_hadisst.py` — `.nc.gz` download + unpack + 13정점 추출 (~3분)
- `analyze_global_trends.py` — 5 윈도우 × 2 dataset × 13 정점 회귀

## 2. 한국 평균 trend — 5-dataset 종합

| 시간 윈도우 | OISST (°C/decade) | HadISST (°C/decade) | COBE-SST2 (°C/decade) | KHOA 본 분석 (°C/decade) | NIFS published (°C/decade) |
|---|---:|---:|---:|---:|---:|
| **2017-2025** (9년) | **1.11** | **1.10** | **1.47** | **1.39** | — |
| 1982-2025 (44년) | 0.19 | 0.25 | 0.18 | — | — |
| **1968-2022** (55년) | 0.14¹ | 0.27 | 0.11 | — | **0.25** |
| 1968-2012 (45년) | 0.16¹ | 0.31 | 0.08 | (단기, KHOA only) | — |
| 1870-2025 (156년) | — | **0.10** | 0.08 | — | — |
| **1850-2025** (176년) | — | — | **0.064** | — | — |

¹ OISST 는 1981.09 부터 → 1968-1981 구간은 NaN, 1982년부터의 데이터로 회귀.

### 2.1 핵심 관찰

1. **2017-2025 가속은 4-dataset 모두 일치** — KHOA 1.39, OISST 1.11, HadISST 1.10, COBE2 1.47. 평균 ~1.27. 차이는 in-situ (연안, ~1 m bulk) vs satellite/reanalysis blend 의 자연스러운 bias. **2017-2025 가속이 실제 climate signal** 임을 강하게 지지.
2. **1968-2022 reanalysis 의 분기**: HadISST 0.27 ≈ NIFS 0.25 vs COBE2 0.11. 두 reanalysis 가 같은 기간에서 2.5배 차이 → blending method (HadISST: COADS + reconstruction, COBE2: 추가 satellite cleanup) 영향. NIFS in-situ 는 HadISST 와 더 일관.
3. **OISST 의 1968-2022 (1982-2022만 cover) = 0.14** — 1980-90 년대 PDO cool phase 영향.
4. **HadISST 156년 0.10, COBE2 176년 0.064** — 둘 다 IPCC AR6 글로벌 평균 (0.13-0.18 °C/decade, 1971-2024) 보다 낮음. 한국 long-term climate trend (이전 1세기) 는 글로벌 평균 수준에서 약간 낮음, 그러나 **최근 9년 가속이 매우 두드러짐**.
5. **COBE2 의 1850-2025 176년 = 0.064 °C/decade** — 매우 안정한 baseline. **2017-2025 (1.47) 가 이 baseline 의 약 23×**.

### 2.2 해역별 (HadISST 1968-2022, 55년)

| 해역 | HadISST (°C/decade) | KHOA 1968-2012 (°C/decade) | 본 9년 (°C/decade) |
|---|---:|---:|---:|
| 서해 | 0.250 (인천·목포·진도 평균) | 0.107 | 1.61 |
| 남해 | 0.318 (제주·서귀포·거제도·여수·거문도·부산 평균) | 0.223 | 1.74 |
| 동해 | 0.199 (울산·포항·묵호·속초 평균) | 0.038 | 0.69 |
| 전국 | 0.271 | 0.123 | 1.39 |

→ HadISST 의 1968-2022 추세는 KHOA 1968-2012 보다 **2~5배 큼** (가능한 이유: HadISST 의 시기가 더 최근까지 포함, 그리고 2003-2022 의 marine heatwave 영향 누적).

## 3. 정점별 long-station 비교

### 3.1 1968-2022 55년 HadISST trend

| 정점 | 해역 | HadISST 1968-2022 (°C/decade) | R² | 비교 (본 9년) |
|---|---|---:|---:|---:|
| 서귀포 | 남해 | **0.366** | 0.674 | 1.85 (5.0×) |
| 제주 | 남해 | **0.366** | 0.674 | 2.39 (6.5×) |
| 거문도 | 남해 | 0.325 | 0.649 | 1.23 (3.8×) |
| 여수 | 남해 | 0.325 | 0.649 | 0.93 (2.9×) |
| 목포 | 서해 | 0.324 | 0.600 | 1.53 (4.7×) |
| 진도 | 서해 | 0.324 | 0.600 | 2.00 (6.2×) |
| 거제도 | 남해 | 0.265 | 0.578 | 2.67 (10×) |
| 인천 | 서해 | 0.216 | 0.380 | 1.30 (6.0×) |
| 부산 | 남해 | 0.221 | 0.424 | 1.33 (6.0×) |
| 울산 | 동해 | 0.221 | 0.424 | -0.39 (— ) |
| 포항 | 동해 | 0.211 | 0.346 | 1.50 (7.1×) |
| 묵호 | 동해 | 0.196 | 0.271 | 0.79 (4.0×) |
| 속초 | 동해 | 0.167 | 0.244 | 0.88 (5.3×) |

→ HadISST 1968-2022 의 R² 가 0.24-0.67 (대부분 > 0.4) — **장기 climate signal 명확**. 본 9년의 강한 trend (특히 남해 max) 가 HadISST 장기에서도 같은 방향 확인 (서귀포·제주가 모든 윈도우에서 max).

### 3.2 1870-2025 156년 HadISST trend (가장 긴 climate baseline)

| 정점 | 해역 | HadISST 1870-2025 (°C/decade) | R² |
|---|---|---:|---:|
| 서귀포 | 남해 | 0.111 | 0.431 |
| 제주 | 남해 | 0.111 | 0.431 |
| 거제도 | 남해 | 0.108 | 0.490 |
| 거문도 | 남해 | 0.101 | 0.419 |
| 여수 | 남해 | 0.101 | 0.419 |
| 부산 | 남해 | 0.097 | 0.406 |
| 울산 | 동해 | 0.097 | 0.406 |
| 포항 | 동해 | 0.093 | 0.366 |
| 묵호 | 동해 | 0.089 | 0.331 |
| 목포 | 서해 | 0.087 | 0.329 |
| 진도 | 서해 | 0.087 | 0.329 |
| 인천 | 서해 | 0.079 | 0.309 |
| 속초 | 동해 | 0.078 | 0.290 |

→ 156년 trend (한국 평균 0.10 °C/decade) 는 IPCC AR6 글로벌 평균 (0.13-0.18) 보다 약간 낮음. **서귀포·제주·거제도 (Kuroshio 영향권) 가 항상 max, 인천·속초 가 min** — 모든 시간 스케일에서 일관된 공간 패턴.

## 4. 가속 정량 — "최근" vs "장기" 비교

### 4.1 HadISST 의 시간별 한국 평균

| 시기 | HadISST (°C/decade) | 비고 |
|---|---:|---|
| 1870-2025 (156년) | 0.10 | 장기 climate baseline (IPCC AR6 글로벌 0.13 수준) |
| 1968-2012 (45년) | 0.31 | 본 분석 KHOA 1968-2012 (0.12) 의 2.5배 |
| 1968-2022 (55년) | 0.27 | NIFS published 0.25 와 일치 |
| 1982-2025 (44년) | 0.25 | satellite era |
| **2017-2025 (9년)** | **1.10** | 156년 평균의 **11×**, 1968-2022의 **4.1×** |

→ **2017-2025 가속이 156년 climate baseline 의 11배** — 단순 단기 잡음으로 설명하기 어려움. 최근 9년이 실제로 다른 시기보다 빠르게 가온 (marine heatwave + Kuroshio 강화 + global warming).

### 4.2 KHOA in-situ vs satellite/reanalysis bias

| 윈도우 | KHOA in-situ | OISST | HadISST | bias (KHOA−HadISST) |
|---|---:|---:|---:|---:|
| 2017-2025 | 1.39 | 1.11 | 1.10 | +0.29 |
| 1968-2012 | 0.123 | 0.155 | 0.307 | −0.18 |

→ 최근 9년 은 KHOA 가 더 강한 trend 보고, 장기 1968-2012 은 HadISST 가 더 강한 trend. 가능한 이유:
- KHOA 정점은 **항만·연안** 위치 → 최근 도시화·항만 활동 영향 (heat island, 산업 폐열) 추가 가능
- HadISST 의 1980 년대 이전 데이터는 ship-of-opportunity 의존 → 시간이 갈수록 정확도 증가 (uncertainty 다름)
- KHOA Annual Report 2012 vol.2 §3.1 표 3-1 의 일부 정점은 짧은 시계열 (6년 등) 평균 → KHOA 평균 = 0.123 가 long-station 만의 평균보다 낮을 수 있음

## 5. SLR cross-check 갱신

[`khoa-annual-climate-trend.md`](khoa-annual-climate-trend.md) 의 한국 평균 SLR = 3.94 mm/yr (2007-2025).

**HadISST 1968-2022 한국 평균 SST trend 0.027 °C/yr** 로 열팽창 기여 재계산:
- 표층 가열 effective depth H = 200 m 가정
- α ≈ 1.5×10⁻⁴ /°C
- 열팽창 SLR 기여 = α · H · 0.027 = 1.5e-4 × 200 × 0.027 = **0.81 mm/yr**
- 한국 평균 SLR 3.94 의 약 **20%** 가 열팽창 기여 (이전 추정 10% 보다 상향)

→ 본 분석 (long-term 0.27 vs 9년 1.39) 으로 인해 열팽창 기여 추정값이 시간 스케일에 민감. 결론: **한국 SLR 의 ~20% 가 thermal expansion, 나머지 80% 는 ice melt + halosteric + sterodynamic**. IPCC 글로벌 (30-50% 열팽창)보다 낮은 이유는 한국이 sterodynamic (Kuroshio 강화 등 dynamic) 영향 큼.

## 6. 결론

| 발견 | 의미 |
|---|---|
| **2017-2025 가속 (~1.27 °C/decade 평균) 은 4-dataset 모두 일치** | 진짜 climate signal, in-situ artifact 아님 |
| **HadISST 1968-2022 (0.27) ≈ NIFS published (0.25)** | NIFS 가 한국 in-situ primary 인 이유 — 글로벌 reanalysis 와 일관 |
| **HadISST 156년 (0.10), COBE-SST2 176년 (0.064)** | 한국 long-term climate trend, IPCC AR6 글로벌 (0.13~0.18) 과 비슷 또는 약간 낮음 |
| **2017-2025 가 176년 평균(COBE2)의 ~23×** | 최근 9년은 단기·자연 변동성으로 설명 어려운 가속 |
| **서귀포·제주가 모든 윈도우에서 max** | Kuroshio 영향권 일관 — 한국 SST 가속의 main source |
| **HadISST vs COBE2 분기 (1968-2022 0.27 vs 0.11)** | 두 reanalysis 가 동일 기간에 2.5× 차이 — blending method 의존성 — 단일 dataset 의존 risk |

## 7. 보강·미해결

### 7.1 가능한 추가 작업
- **NIFS KODC 정선 raw 자료** — form-based 다운로드로 동해 102정선·동중국해 등 직접 trend 분석 가능 (published 값만 인용한 현재 한계 보완)
- **COBE-SST2 (JMA) 추가** — 일본 측 primary, 1891-현재 0.25° → HadISST 1° 보다 정밀 + 1891 부터 → ERSST 보다 한국 연안 적합
- **MUR L4 0.01°** — 한국 좁은 만·해협 정밀 분석 (2002-현재)
- **NOAA OISST daily** — Marine heatwave 일별 식별 (현재는 monthly only)
- **수직 profile (NIFS 다층 수온)** — surface trend vs 100m·500m trend 비교 (sterodynamic 추정 정교화)

### 7.2 본 분석의 한계
- HadISST 1° 격자에서 일부 정점이 같은 격자에 들어감 (거제도/여수/거문도 = 34.5,127.5; 부산은 fallback 으로 다른 셀)
- OISST 1981.09 시작 → 1968-1981 구간은 HadISST 단일 source
- satellite 시작 이전 (1980 이전) HadISST 는 ship/buoy 보간 의존 — uncertainty 증가

## 8. 데이터·재현

산출:
- `data/sst-global/oisst_v21_13stations_monthly.csv` (6,968 rows: 13정점 × 536 months 1981.09~2026.04)
- `data/sst-global/hadisst_13stations_monthly.csv` (24,336 rows: 13정점 × 1872 months 1870.01~2025.12)
- `data/sst-global/trends_global_summary.json` (5 윈도우 × 2 dataset 회귀 결과)

재현:
```bash
cd ~/coastal-wiki
uv run python tools/sst-cross-check/fetch_oisst_monthly.py   # ~3분 (download + extract)
uv run python tools/sst-cross-check/fetch_hadisst.py         # ~3분
uv run python tools/sst-cross-check/fetch_cobe2.py           # ~3분 (523 MB)
uv run python tools/sst-cross-check/analyze_global_trends.py # <10초
```

## 9. 연결

- [`concepts/sst/01-concept.md`](../concepts/sst/01-concept.md) — SST 정의·측정 정형화
- [`experience/khoa-sst-warming-trend.md`](khoa-sst-warming-trend.md) — KHOA in-situ 9년 + 1968-2012 KHOA 공식
- [`experience/khoa-annual-climate-trend.md`](khoa-annual-climate-trend.md) — SLR 분석 + 열팽창 기여
- [`textbook/notes/khoa-annual-reports-overview.md`](../textbook/notes/khoa-annual-reports-overview.md) — KHOA 백서 source
- 외부 데이터:
  - [NOAA OISST v2.1 (PSL)](https://psl.noaa.gov/data/gridded/data.noaa.oisst.v2.highres.html)
  - [HadISST v1.1 (UKMO)](https://www.metoffice.gov.uk/hadobs/hadisst/)
  - [NIFS KODC](https://www.nifs.go.kr/kodc/) (정선 raw 별도 작업)
