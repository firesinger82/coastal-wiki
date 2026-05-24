# concepts/storm-surge — 폭풍해일 (Storm Surge)

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·인자 (기압·바람·tide-surge interaction·wave setup)·한국 적용 (Pugh 1987 Ch 6 + ADCIRC + KHOA) |
| `02-theory.md` | **verified** | shallow-water + wind-driven setup 방정식, inverse-barometer 정량 |
| `03-analysis-methods.md` | **verified** | tide-surge separation (Pugh §6:1) + interaction 진단 (§7:8) + Mann-Kendall trend (sst/03 canonical) + return period annual maxima (§8:3:2) + joint probability convolution (§8:3:3) |
| `04-code-and-tools.md` | **verified** | ADCIRC NWS modes·OWI/GRIB·KHOA observation·SWAN coupling·운영 workflow |
| `05-examples.md` | **source-needed** | Maemi 2003 + Hinnamnor 2022 case cross-ref (본 위키 내부 verified · 외부 실측 surge 수치 KHOA Annual Report fetch 필요) — 2026-05-24 |
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
2. ✅ `02-theory.md` verified (2026-05-23) — Pugh §6:3 IB + §6:4 wind stress + §7:8 tide-surge interaction
3. ✅ `03-analysis-methods.md` verified (2026-05-24) — Pugh §6:1, §7:8, §8:3:2-3 + Mann-Kendall (sst/03 cross-ref)
4. ✅ `04-code-and-tools.md` verified — ADCIRC NWS modes·OWI format·KHOA observation
5. ✅ `05-examples.md` source-needed (2026-05-24) — Maemi 2003 + Hinnamnor 2022 cross-ref. 위키 내부 자료 verified, 외부 실측 KHOA Annual Report·KMA/JMA Best Track fetch 후 verified 승격. Bolaven 2012 등은 별도 sub-노트 후보.
6. ✅ `_staging adcirc-storm-surge*.md` 7개 → `models/ADCIRC/source-analysis/storm-surge/` promote 완료 (2026-05-23). 추후 `06-model-application.md` 에서 본 노트들 인용
