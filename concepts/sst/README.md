# concepts/sst — 해수면 수온 (Sea Surface Temperature)

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·측정 정형화·시공간 스케일·한국 인프라 (Stewart §5-6 + KHOA Annual Reports) |
| `02-theory.md` | **verified** | 해양 열수지·열팽창·해류 forcing — Stewart §5 eq. 5.1-5.6 정형 인용 |
| `03-analysis-methods.md` | **verified** | 시계열 회귀·Mann-Kendall·Sen's slope·climatology·anomaly·MHW (Hobday 2016)·spectral |
| `04-code-and-tools.md` | **verified** | KHOA OpenAPI + NOAA OISST + UKMO HadISST + JMA COBE-SST2 + NIFS KODC 운영 정리 |
| `05-examples.md` | **verified** | trend 재현 + monthly MHW 식별 (Hobday 2016 variant) — 13정점 ~180 events, 2024-08~11 광역 사건 정량 |
| `06-model-application.md` | verified | EFDC/Delft3D/ROMS heat module — models/ source-analysis cross-link. 잔존 source-needed: 한국 적용 paper(`experience/` 정책)·SST forcing endpoint |

## 사용된 source_id

- `stewart-physical-ocean` — [`textbook/notes/sst-stewart-ch5-6.md`](../../textbook/notes/sst-stewart-ch5-6.md) (예정 — 챕터 노트 생성 대기)
- `khoa-annual-reports` — [`textbook/notes/khoa-annual-reports-overview.md`](../../textbook/notes/khoa-annual-reports-overview.md) (정점 인벤토리, 측정 인프라)

## 연결

- `experience/khoa-sst-warming-trend.md` — 한국 연안 SST 추세와 장단기 비교(탐색용)
- `experience/khoa-sst-global-crosscheck.md` — OISST·HadISST·NIFS 자료 비교(탐색용)
- `experience/khoa-annual-climate-trend.md` — SLR 분석 (열팽창 기여도 cross-check)
- `concepts/tides/02-theory.md` §8.6 — 평균해면 trend (SLR-SST 인과 연결)

## 작업 계획

[CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일 시작. 02~06은 sourced claim 누적 시 생성.

다음 단계 후보:
1. ✅ `01-concept.md` verified (2026-05-23)
2. `02-theory.md` (Stewart §5 heat budget — insolation, infrared, sensible, latent, advection — 정형 인용)
3. `04-code-and-tools.md` (KHOA OpenAPI `surveyWaterTemp` + NOAA OISST + HadSST 정리)
4. `textbook/notes/sst-stewart-ch5-6.md` — Stewart 챕터 노트 정식 추출
