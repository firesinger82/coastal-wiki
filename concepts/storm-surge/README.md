# concepts/storm-surge — 폭풍해일 (Storm Surge)

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·인자 (기압·바람·tide-surge interaction·wave setup)·한국 적용 (Pugh 1987 Ch 6 + ADCIRC + KHOA) |
| `02-theory.md` | (미생성) | shallow-water + wind-driven setup 방정식, inverse-barometer 정량 |
| `03-analysis-methods.md` | (미생성) | tide-surge separation, joint probability, return period |
| `04-code-and-tools.md` | (미생성) | ADCIRC NWS modes·SWAN coupling·OWI/GRIB input·KHOA observed surge |
| `05-examples.md` | (미생성) | quarter-annular baseline + hurricane case + 한국 태풍 (Maemi 2003, Hinnamnor 2022) |
| `06-model-application.md` | (미생성) | ADCIRC primary + Delft3D·SCHISM·SLOSH 비교 — `models/ADCIRC/` 작성 후 verified |

## 사용된 source_id

- `pugh-sea-level` — [`textbook/md/sea-level.md`](../../textbook/md/sea-level.md) (Pugh "Tides, Surges and Mean Sea-Level" Ch 6 직접)
- `adcirc-theory` — [`models/ADCIRC/raw/manuals/pdfs/adcirc_theory_2004_12_08.pdf`](../../models/ADCIRC/raw/manuals/) (Luettich & Westerink ADCIRC Theory)
- `khoa-annual-reports` — [`textbook/notes/khoa-annual-reports-overview.md`](../../textbook/notes/khoa-annual-reports-overview.md) (한국 태풍·이상조위 자료)
- `adcirc-source-analysis-storm-surge` — [`models/ADCIRC/source-analysis/storm-surge/`](../../models/ADCIRC/source-analysis/storm-surge/) (7개 노트, source-code level NWS=12-30 분석 — promote 완료 2026-05-23)

## 연결

- `concepts/tides/02-theory.md` §8 — SLR + 평균해면 (storm surge baseline)
- `concepts/waves/` — wave setup (storm surge 위 추가)
- `concepts/sst/02-theory.md` §6 — mixed layer (열대저기압 강도 결정)
- `experience/khoa-annual-climate-trend.md` — SLR + 태풍 빈도 trend
- `experience/khoa-sst-warming-trend.md` — Kuroshio/marine heatwave (태풍 강도화 동인)
- `models/ADCIRC/` — primary storm surge 모델
- `models/ADCIRC/source-analysis/storm-surge/` (7개, promote 완료) — ADCIRC NWS source-code 분석

## 작업 계획

[CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일 시작. 02~06 은 sourced claim 누적 시 생성.

다음 단계 후보:
1. ✅ `01-concept.md` verified (2026-05-23)
2. `02-theory.md` — Pugh §6:3 inverse-barometer + §6:4 wind stress + §7:8 tide-surge interaction 정형 인용
3. `04-code-and-tools.md` — ADCIRC NWS modes·OWI format·KHOA 이상조위 observation
4. `05-examples.md` — 한국 태풍 case (Maemi 2003 / Bolaven 2012 / Hinnamnor 2022) — KHOA 백서 직접 인용
5. ✅ `_staging adcirc-storm-surge*.md` 7개 → `models/ADCIRC/source-analysis/storm-surge/` promote 완료 (2026-05-23). 추후 `06-model-application.md` 에서 본 노트들 인용
