# models/ADCIRC/source-analysis/storm-surge/

ADCIRC 의 storm-surge 관련 source-code 분석 노트 (공식 NWS 외력 패밀리·GAHM/AHM/OWI). modeling-wiki (2026-04 작성) 에서 promote. (2026-06-18 정화: 개인 JMA-MSM/NWS13 운영 플레이북 3노트 제거 — 위키는 공식 출처만, 케이스는 별도.)

## 파일

| 파일 | 주제 |
|---|---|
| `adcirc-storm-surge.md` | NWS=19/20/29/30 GAHM·AHM·OWI hybrid — source-code level (read_input.F, wind.F, vortex.F 인용) |
| `adcirc-storm-surge-foundation.md` | Foundation — storm-surge 실험 시작 전 이해해야 할 것 |
| `adcirc-storm-surge-nws-families.md` | NWS family 비교 (NWS=12/13/14/19/20) — OWI NetCDF NWS=13 포함 |
| `adcirc-storm-surge-requirements-checklist.md` | 실험 시작 전 요구사항 체크리스트 |

## 인용

각 노트의 본문에 ADCIRC source code 의 file:line 인용 (`read_input.F:2157`, `wind.F:1501` 등). source 위치: [`models/ADCIRC/raw/source_code/adcirc/src/`](../../raw/source_code/) (raw/ .gitignore — 별도 clone 으로 재현 가능).

## 연결

- 도메인 layer: [`concepts/storm-surge/01-concept.md`](../../../../concepts/storm-surge/01-concept.md), [`02-theory.md`](../../../../concepts/storm-surge/02-theory.md)
- raw source: [`models/ADCIRC/raw/source_code/adcirc/src/`](../../raw/source_code/)
- manuals: [`models/ADCIRC/raw/manuals/`](../../raw/manuals/) (PDF + website 등)
- 다른 ADCIRC source-analysis: [`models/ADCIRC/source-analysis/`](../)

## 작성 이력

- 2026-04: modeling-wiki/knowledge/methods/ 에서 작성 (사용자 + codex source-code 분석)
- 2026-05-23: coastal-wiki 통합 시 `_staging/from-modeling-wiki/knowledge/methods/` 경유 → 본 위치로 promote (Claude Opus 4.7 + 사용자)
