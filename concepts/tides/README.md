# concepts/tides — 조석

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | **verified** | 정의·용어·전형값 (Lubbad slides) |
| `02-theory.md` | **verified** | 기조력·평형조석·분조·동력학적 조석 (Stewart §17.4-17.5 + KHOA glossary) |
| `03-analysis-methods.md` | **verified** | 조화분해·response method (Stewart §17.5 + Foreman 1977 appendix + KHOA) |
| `04-code-and-tools.md` | **verified** | t_tide / UTide / pytides / pyTMD — DOI·repo·논문 인용 |
| `05-examples.md` | **verified** | UTide/pytides 공식 예제 + 한국 KHOA template |
| `06-model-application.md` | `source-needed` | EFDC/ADCIRC/XBeach/Delft3D — `models/<model>/` 채워지면 verified |

## 사용된 source_id

- `lubbad2009-tides-slides` — [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md)
- `stewart-physical-ocean` — [`textbook/notes/tides-stewart-ch17.md`](../../textbook/notes/tides-stewart-ch17.md)
- `tidal-heights-manual` — [`textbook/notes/tides-foreman1977-appendix.md`](../../textbook/notes/tides-foreman1977-appendix.md) (appendix only, 본문 OCR 보강 대기)
- `khoa-portcals-glossary` — [`textbook/sources.yml`](../../textbook/sources.yml) (KHOA PortCALS 용어집)
- `khoa-tide-model` — [`textbook/notes/tides-khoa-nonharmonic-research.md`](../../textbook/notes/tides-khoa-nonharmonic-research.md) (KHOA 공식 비조화상수·국립해양조사원고시 제2021-7호)
- `khoa-tide-model` — [`textbook/notes/tides-khoa-cross-verification.md`](../../textbook/notes/tides-khoa-cross-verification.md) (3개 source 산재값 cross-verification + 변도성 2007 위상 기준 + 수치조류도)
- `khoa-annual-reports` — [`textbook/notes/khoa-annual-reports-overview.md`](../../textbook/notes/khoa-annual-reports-overview.md) (15권 2012-2025 공식 백서, 조위·파랑·해수유동 통합)

## 작업 계획

[plan.md](../../plan.md), [CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일(README + 01-concept)로 시작. 02~06은 sourced claim 누적되면 생성.

다음 단계:
1. ~~`01-concept.md` verified~~ (완료, 2026-05-21)
2. ~~`02-theory.md` 작성 (Stewart + KHOA glossary)~~ (완료, 2026-05-21)
3. ~~`03-analysis-methods.md` 작성 (Stewart §17.5 + Foreman appendix + KHOA)~~ (완료, 2026-05-21)
4. ~~`04-code-and-tools.md` 작성 (t_tide/UTide/pytides/pyTMD + TPXO/FES/NAO/GOT)~~ (완료, 2026-05-21)
5. ~~`05-examples.md` 작성 (UTide/pytides 공식 예제 + 한국 template)~~ (완료, 2026-05-21)
6. ~~`06-model-application.md` 골격~~ (완료 source-needed, `models/<model>/` 채워지면 verified)

보강 대기:
- `models/EFDC/manual-notes/` 작성 → 06-model-application source-needed → verified
- `models/ADCIRC/manual-notes/` + tidal database web-refs
- `models/XBeach/manual-notes/`, `models/Delft3D/manual-notes/`
- 한국 KHOA 인천 정점 데이터로 §3 template 실행 → verified 승격
- Foreman 1977 본문 (p.1-47) OCR 재변환 → Rayleigh criterion, nodal correction 수식 정밀화
- 각 도구의 라이선스 표 (LICENSE 파일 직접 확인)
