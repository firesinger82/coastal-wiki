# concepts/tides — 조석

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·용어·전형값 (Lubbad slides) |
| `02-theory.md` | **verified** | 기조력·평형조석·분조·동력학적 조석 (Stewart §17.4-17.5 + KHOA glossary) |
| `03-analysis-methods.md` | **verified** | 조화분해·response method (Stewart §17.5 + Foreman 1977 appendix + KHOA) |
| `04-code-and-tools.md` | **verified** | t_tide / UTide / pytides / pyTMD — DOI·repo·논문 인용 |
| `05-examples.md` | 미생성 | 실습 |
| `06-model-application.md` | 미생성 | EFDC/ADCIRC 조석 forcing |

## 사용된 source_id

- `lubbad2009-tides-slides` — [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md)
- `stewart-physical-ocean` — [`textbook/notes/tides-stewart-ch17.md`](../../textbook/notes/tides-stewart-ch17.md)
- `tidal-heights-manual` — [`textbook/notes/tides-foreman1977-appendix.md`](../../textbook/notes/tides-foreman1977-appendix.md) (appendix only, 본문 OCR 보강 대기)
- `khoa-portcals-glossary` — [`/mnt/d/wsl_env/maritime-glossary-mcp/glossary.json`](../../textbook/sources.yml) (직접 lookup, 페이지 없음)

## 작업 계획

[plan.md](../../plan.md), [CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일(README + 01-concept)로 시작. 02~06은 sourced claim 누적되면 생성.

다음 단계:
1. ~~`01-concept.md` verified~~ (완료, 2026-05-21)
2. ~~`02-theory.md` 작성 (Stewart + KHOA glossary)~~ (완료, 2026-05-21)
3. ~~`03-analysis-methods.md` 작성 (Stewart §17.5 + Foreman appendix + KHOA)~~ (완료, 2026-05-21)
4. ~~`04-code-and-tools.md` 작성 (t_tide/UTide/pytides/pyTMD)~~ (완료, 2026-05-21)
5. `05-examples.md` — 학습 예제 (재현 가능 코드 + 데이터)
6. `06-model-application.md` — EFDC `models/EFDC/` 작성 후 4대 분조 forcing 링크

보강 대기:
- Foreman 1977 본문 (p.1-47) OCR 재변환 → Rayleigh criterion, nodal correction 수식 정밀화
- 각 도구의 라이선스 표 (LICENSE 파일 직접 확인)
- Egbert & Erofeeva (2002) TPXO 정식 인용 (pyTMD 데이터)
