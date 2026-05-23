# data/khoa-analysis/

`experience/` 정량 분석의 raw + intermediate JSON.

## 파일 list

| 파일 | 정점·기간 | 사용처 |
|---|---|---|
| `khoa_msl_2007_2025.json` | 13정점 × 19년 MSL 시계열 | `experience/khoa-annual-climate-trend.md` |
| `khoa_msl_trends.json` | 13정점 선형회귀 slope/R² (mm/yr) | 위 같음 |
| `khoa_m2_2012_2025.json` | M2 진폭 partial — 2012-2015, 2020-2022 | 위 같음 §4 |
| `khoa_sst_phase1.json` | 13정점 × 2019-2025 월별 SST | `experience/khoa-sst-warming-trend.md` |
| `khoa_sst_phase2.json` | 13정점 × 2017-2018 partial | 위 같음 |
| `khoa_sst_merged.json` | 13정점 × 9년 (2017-2025) 통합 + 연평균 | 위 같음 |
| `khoa_sst_trends_clean.json` | 13정점 SST 선형회귀 (°C/decade) | 위 같음 |

## 재현 방법

추출 스크립트 (Node.js):
- 원본: `D:\Numerical_models\00_Common\KHOA_WHITE_PAPER\markdowns\` (15개 .md)
- 추출 로직: 본 디렉토리 옆 형제 experience 파일의 `verification_method` 인용 참조
- 회귀: 표준 선형회귀 (slope, intercept, R²)

## 데이터 무결성

생성 시각: 2026-05-23
사용 보고서: KHOA Annual Report 2012-2025 (15권, 188,929 줄)

내용 변경 시 짝 experience 파일의 `verification_date` 갱신 필요.
