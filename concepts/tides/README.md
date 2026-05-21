# concepts/tides — 조석

## 상태

| 파일 | 상태 | 비고 |
|---|---|---|
| `README.md` | self (governance) | 이 파일 |
| `01-concept.md` | `draft-unsourced` → 사용자 verify 대기 | 정의·용어·전형값 |
| `02-theory.md` | 미생성 | 생성력·평형조석 — `stewart-physical-ocean` 보강 필요 |
| `03-analysis-methods.md` | 미생성 | 조화 분해 — `tidal-heights-manual` 활용 |
| `04-code-and-tools.md` | 미생성 | UTide(Python) / t_tide(MATLAB) / pytides |
| `05-examples.md` | 미생성 | 실습 |
| `06-model-application.md` | 미생성 | EFDC/ADCIRC 조석 forcing |

## 사용된 source_id

- `lubbad2009-tides-slides` — [`textbook/notes/tides-lubbad2009-overview.md`](../../textbook/notes/tides-lubbad2009-overview.md)

## 작업 계획

[plan.md](../../plan.md), [CONVENTIONS.md §8](../../CONVENTIONS.md) — 최소 2파일(README + 01-concept)로 시작. 02~06은 sourced claim 누적되면 생성.

다음 단계:
1. 사용자가 `01-concept.md` `draft-unsourced` → `verified` 검증 (페이지 대조)
2. 보강 source 확보 후 `02-theory.md` 작성 (`stewart-physical-ocean` 또는 `tidal-heights-manual`)
3. `04-code-and-tools.md`에 UTide(Python)·t_tide(MATLAB) 정리 — 공식 GitHub repo/논문 인용
