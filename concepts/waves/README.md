# concepts/waves — 파랑 (Waves)

풍파(wind-generated waves) + 너울(swell) 중심. 조석파(`concepts/tides/`)·쓰나미·내부파는 별도.

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·풍파vs너울·파라미터·관측·KHOA 용어 |
| `02-theory.md` | **verified** | linear theory·분산관계·energy·천해변형 (Holthuijsen Ch.5,7) |
| `03-analysis-methods.md` | **verified** | 스펙트럼·통계·JONSWAP·PM (Holthuijsen Ch.3,4) |
| `04-code-and-tools.md` | **verified** | SWAN/WW3/XBeach + WINK·spectrum_archive |
| `05-examples.md` | **verified** | 한국 MPT 74정점 분석 frame + 축산항 사례 |
| `06-model-application.md` | `source-needed` | SWAN canonical, `models/SWAN/` 채워지면 verified |

## 사용된 source_id

- `holthuijsen2007` — [`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md) (Ch.1-9 TOC + 핵심 발췌, Ch.9 전체가 SWAN)
- `khoa-portcals-glossary` — 284 파랑 용어
- `dashboard-khoa-data` — MPT 74정점 메타데이터 + mof_data
- `swan-library-firesinger` — 사용자 본인 SWAN library (`D:\Numerical_models\01_Models\swan\Fin\07_SWAN_LIBRARY\`)
- `hudspeth2005-wave-forces` — 파력 (TBD)
- `water-wave-mechanics` — 수파역학 (TBD)

## tides 토픽과의 차이

| 항목 | tides | waves |
|---|---|---|
| 주기 | 12-24 h | 1-30 s (풍파·너울) |
| 메커니즘 | 천체 인력 (deterministic) | 바람 → 중력 회복 (stochastic) |
| 분석 | harmonic (조화분해) | spectral (분산 분해) |
| 모델 | EFDC·ADCIRC | **SWAN**·WAVEWATCH III·XBeach |
| 한국 자료 | KHOA tideObsHar (조화상수) | KHOA·MOF·KMA buoy (시계열) |
