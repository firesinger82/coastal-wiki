# concepts/waves — 파랑 (Waves)

풍파(wind-generated waves) + 너울(swell) 중심. 조석파(`concepts/tides/`)·쓰나미·내부파는 별도.

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·풍파vs너울·파라미터·관측·KHOA 용어 |
| `02-theory.md` | **verified** | linear theory·분산관계·energy·천해변형 (Holthuijsen Ch.5,7) |
| `03-analysis-methods.md` | **verified** | 스펙트럼·통계·JONSWAP·PM (Holthuijsen Ch.3,4) |
| `04-code-and-tools.md` | **verified** | SWAN/WW3/XBeach |
| `05-examples.md` | **verified** | 한국 MPT 74정점 분석 frame |
| `06-model-application.md` | **verified** | SWAN canonical (`models/SWAN/` 2 노트 verified) + WW3/XBeach 외부 인용 |
| `07-wave-transmission.md` | ✅ **verified** (2026-06-18) | 부유체·구조물 파 투과/반사 — inbox promote(1402.1555 실험 + 1403.3766 floating disk array, full-PDF) + SWAN obstacle 투과(Goda/d'Angremond) 대비 |
| `08-wave-current-interaction.md` | ✅ **verified** (2026-06-18) | 파-흐름 상호작용(Doppler·refraction·blocking) — inbox promote(2511.12711 eddy dipole 풍파 + 2606.03231 reduced wave-current, full-PDF) + SWAN action balance/QC 대비 |

## 사용된 source_id

- `holthuijsen2007` — [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) (Ch.1-9 TOC + 핵심 발췌, Ch.9 전체가 SWAN)
- `khoa-portcals-glossary` — 284 파랑 용어
- 해양수산부(MOF)·KHOA 공식 관측망 — MPT 74정점 메타데이터 + mof_data (공식 운영자료; 정식 source_id 미등록 → source-needed)
- `hudspeth2005-wave-forces` — 파력 (TBD)
- `water-wave-mechanics` — 수파역학 (TBD)
- `khoa-annual-reports` — [`textbook/notes/khoa-annual-reports-overview.md`](../../textbook/notes/khoa-annual-reports-overview.md) (15권 2012-2025, MPT 정점·유의파 통계)

## tides 토픽과의 차이

| 항목 | tides | waves |
|---|---|---|
| 주기 | 12-24 h | 1-30 s (풍파·너울) |
| 메커니즘 | 천체 인력 (deterministic) | 바람 → 중력 회복 (stochastic) |
| 분석 | harmonic (조화분해) | spectral (분산 분해) |
| 모델 | EFDC·ADCIRC | **SWAN**·WAVEWATCH III·XBeach |
| 한국 자료 | KHOA tideObsHar (조화상수) | KHOA·MOF·KMA buoy (시계열) |
