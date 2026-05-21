# concepts/currents — 조류 (Tidal Currents)

조석에 의한 해수의 주기적 수평흐름. 조위 (스칼라) → 조류 (2D 벡터) 확장. 분조는 동일 (M₂·S₂·K₁·O₁ 등), 출력은 (진폭, 위상) 2쌍 + 회전 방향 → **조류타원** parameters.

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·창조/낙조/정조/게류·왕복성vs회전성·해류와 구분 |
| `02-theory.md` | **verified** | 분조 분해·조류타원 (UTide 2D parameters)·천해 흐름 |
| `03-analysis-methods.md` | **verified** | UTide 2D·ADCP·KHOA 조류관측 protocol |
| `04-code-and-tools.md` | **verified** | UTide 2D 출력·수치조류도 격자 데이터·KHOA OpenAPI |
| `05-examples.md` | **verified** | KHOA 수치조류도에서 임의 정점 분조 추출 예제 |
| `06-model-application.md` | `source-needed` | EFDC/ADCIRC 조류 출력 — models/ 채워지면 verified |

## 사용된 source_id

- `khoa-portcals-glossary` — 60+ 조류 용어 (가장 풍부)
- `khoa-tide-model` — 수치조류도 광역 조화상수 (813,703 rows, cm/s) + 변도성 2007 위상 기준
- `dashboard-khoa-data` — 4대분조 정밀값 (조류 분조 분해에도 적용)
- `stewart-physical-ocean` — tidal currents 일반 (§17.4 도입부, p.313)
- `lubbad2009-tides-slides` — tidal currents in inlets/bays (p.50)

## tides 토픽과의 관계

조류는 조석 토픽의 자연 확장 — 동일 분조 set, 동일 위상 기준 (G/g/κ, 변도성 2007), 동일 시간 척도. 다음 항목 공유:

- 4대분조 (M₂·S₂·K₁·O₁) — [`concepts/tides/02-theory.md` §4.2-4.3](../tides/02-theory.md)
- 위상 기준 G/g/κ — [`concepts/tides/02-theory.md` §8.3.1](../tides/02-theory.md)
- 분조 각속도 9자리 정밀값 — `khoa-tide-model` skill.md ([cross-verification](../../textbook/notes/tides-khoa-cross-verification.md) §2)
- 조화분해 알고리즘 — [`concepts/tides/03-analysis-methods.md` §1-2](../tides/03-analysis-methods.md)

조류 고유 항목:
- 2D 벡터 분해 (u, v) → 4 미지수 per 분조 → **조류타원** (semi-major, semi-minor, inclination, phase)
- 왕복성 vs 회전성 (Coriolis + 지형 영향)
- 창조류·낙조류 비대칭 (천해 비선형)
