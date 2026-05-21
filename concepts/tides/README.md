# concepts/tides — 조석

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·용어·전형값 (Lubbad slides) |
| `02-theory.md` | **verified** | 기조력·평형조석·분조·동력학적 조석 (Stewart §17.4-17.5 + KHOA glossary) |
| `03-analysis-methods.md` | 미생성 | 조화 분해 구현 — `tidal-heights-manual` 활용 |
| `04-code-and-tools.md` | 미생성 | UTide(Python) / t_tide(MATLAB) / pytides |
| `05-examples.md` | 미생성 | 실습 |
| `06-model-application.md` | 미생성 | EFDC/ADCIRC 조석 forcing |

## 사용된 source_id

- `lubbad2009-tides-slides` — [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md)
- `stewart-physical-ocean` — [`textbook/notes/tides-stewart-ch17.md`](../../textbook/notes/tides-stewart-ch17.md)
- `khoa-portcals-glossary` — [`/mnt/d/wsl_env/maritime-glossary-mcp/glossary.json`](../../textbook/sources.yml) (직접 lookup, 페이지 없음)

## 작업 계획

[plan.md](../../plan.md), [CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일(README + 01-concept)로 시작. 02~06은 sourced claim 누적되면 생성.

다음 단계:
1. ~~`01-concept.md` verified~~ (완료, 2026-05-21)
2. ~~`02-theory.md` 작성 (Stewart + KHOA glossary)~~ (완료, 2026-05-21)
3. `03-analysis-methods.md` — 조화분해 구현 상세. `tidal-heights-manual` + Stewart §17.5 Harmonic/Response method
4. `04-code-and-tools.md` — UTide(Python)·t_tide(MATLAB)·pytides 공식 repo·논문 인용
5. `06-model-application.md` — EFDC `models/EFDC/` 작성 후 4대 분조 forcing 링크
