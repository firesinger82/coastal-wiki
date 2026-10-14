# ROMS 노트 전수 대조 5 (2026-10-14)

- 대상: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md`.
- 대상 줄: 새 파일의 전체 232줄. 작업 시작 시 파일의 물리적 줄 수를 기준으로 한다.
- 대조 기준: 현재 소스, 인용된 과거 판본, 위키 wikitext, 대조 보고서의 최종 전수 검증 기록, git 판정 보고서.
- 쓰기 범위: 대상 노트와 이 기록 파일.
- 진행 상태: 완료.

## 기계 확인 후보 판정

- 사용자 제공 불일치 후보는 없다.

## 노트별 결과

### roms-wiki-cppdefs-options-differences-2.md

| 대상 노트 | 대조한 줄 수 | 정정 수 | 보완 수 | 결과 |
|---|---:|---:|---:|---|
| [roms-wiki-cppdefs-options-differences-2.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md) | 232 | 3 | 0 | 전체 대조 완료 |

줄 수는 작업 시작 시 대상 파일의 1–232행을 센 값이다. 정정 수는 작업 시작본과 최종본에서 달라진 물리적 줄을 센 값이다. 정정한 줄은 2·8·22행이다. 모든 정정 줄 끝에 `[10-14 전수 검증 정정]`을 붙였다.

| 대조 범위 | 줄 수 | 대조 내용 |
|---|---:|---|
| 1–20행 | 20 | frontmatter의 출처·판본·검증 방법·날짜·작성자·상태·관련 파일을 확인했다. |
| 21–33행 | 13 | 제목·부모 노트·출처 보고서·문서 판·코드 판·표 머리글·빈 줄을 확인했다. |
| 34–75행 | 42 | 동쪽 운동량·추적자·체적 보존·폐쇄 경계의 과거 CPP 선택과 현재 선택을 대조했다. |
| 76–123행 | 48 | 결합·자료동화·혼합·입출력 옵션의 조건·개명·폐기·문서 오기를 대조했다. |
| 124–215행 | 92 | 북쪽 자유수면·난류·운동량·추적자·체적 보존·폐쇄 경계를 대조했다. |
| 216–232행 | 17 | 주기 경계·관측 nudging·OBC의 과거 구현과 현재 선택을 대조했다. |

위 범위는 겹치지 않는다. 범위별 줄 수의 합은 232줄이다.

### 정정 목록

| 노트:줄 | 전 | 후 | 근거 원문 |
|---|---|---|---|
| [roms-wiki-cppdefs-options-differences-2.md:2](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md#L2) | 제목의 `32+ CPP option category 종합` | 제목의 `대표 CPP 범주` | [대조 보고서](../compare/roms-build-options-history-vs-code.md):3592, RBH-3479의 수정안은 `대표 CPP 범주라는 편집 제목으로 표시한다.`이다. 같은 행은 32개를 현재 전체 범주 수의 근거로 사용하지 않도록 명시한다. |
| [roms-wiki-cppdefs-options-differences-2.md:8](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md#L8) | `"models/ROMS/raw/manuals/wiki/markdown/cppdefs.h.md (myroms.org/wiki/cppdefs.h, _revid=5862_, fetched 2026-05-03) 본문 직접 인용 — Contents 의 32 numbered section 직접 추출 (momentum·tracers·pressure gradient·atmospheric BL·shortwave·Lagrangian·horizontal/vertical mixing·GLS·MY25·KPP·Richardson·3 BBL closures·lateral BC·tidal forcing·driver·TL/RPR/ADJ·6 biology models). 2026-10-14 ROMS recovery 대조 보고서 반영"` | `"Options.wiki (revid=6053, 2026-05-03 수집)의 인용문과 현재 코드 및 인용된 과거 판본을 대조했다. roms-build-options-history-vs-code.md §5와 최종 전수 검증 기록을 대조했다. ROMS-git-verify-A2.md·A3.md·D1.md의 해당 행을 대조했다."` | [manifest.json](../../../models/ROMS/raw/manuals/wiki/manifest.json):1141은 `"title": "Options",`를 기록한다. 1143행은 `"revid": 6053,`을 기록한다. 4행의 수집일은 `2026-05-03T14:20:20Z`이다. [대조 보고서](../compare/roms-build-options-history-vs-code.md):4007–4205의 배정 행은 모두 Options.wiki를 인용한다. 부모 노트의 cppdefs.h 목차 검증 방법을 이 파일에 복사한 오류를 고쳤다. |
| [roms-wiki-cppdefs-options-differences-2.md:22](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md#L22) | 부모 노트 표시명의 `32+ CPP option category 종합` | 부모 노트 표시명의 `대표 CPP 범주` | [대조 보고서](../compare/roms-build-options-history-vs-code.md):3592, RBH-3479의 수정안은 `대표 CPP 범주라는 편집 제목으로 표시한다.`이다. [부모 노트](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options.md):2의 제목도 `ROMS cppdefs.h — 대표 CPP 범주 (myroms.org/wiki/cppdefs.h)`이다. |

### 대조 결과

- 차이 표의 199행을 [배정표](../assign/note-job-6.tsv)의 해당 노트 행과 대조했다. 누락 행과 중복 행은 없다.
- 199행의 항목·분류·결론 문장은 [대조 보고서](../compare/roms-build-options-history-vs-code.md):4007–4205와 같다. 위키 마크업의 HTML 표기와 코드 서식만 정규화했다. 최종 전수 검증 기록의 작업 2/7을 적용한 결론을 기준으로 삼았다.
- 차이 표의 결론 칸에서 센 분류는 A 168행, B 28행, C 2행, D 1행이다. E 행은 없다.
- A 168행의 결론 칸에 적힌 커밋·날짜 쌍 188건을 git 판정표의 변경 근거와 대조했다. 대응 판정표는 [A2](../compare/ROMS-git-verify-A2.md) 71행, [A3](../compare/ROMS-git-verify-A3.md) 91행, [D1](../compare/ROMS-git-verify-D1.md) 6행이다. 모든 쌍이 일치한다.
- 노트에 날짜와 함께 적힌 고유 커밋 20개를 소스 저장소의 읽기 전용 `git show -s`로 대조했다. 모든 저자 날짜가 일치한다. 인용된 태그와 커밋 식별자도 일치한다.
- `경로:줄` 뒤 원문 인용 2,214건을 실제 파일에서 대조했다. 위키는 204건이다. 현재 코드는 833건이다. 과거 판본은 1,177건이다. 과거 판본은 읽기 전용 `git show REV:path`로 열었다. 인용 위치의 중복을 제거한 수는 1,107개이다. 불일치는 없다.
- 원문 인용의 조건문·식·부호·단위는 원문과 같다. 경계 방향과 변수 성분을 대조했다. radiation 안의 nudging 분기와 SOLVE3D·난류 폐쇄 조건을 대조했다. IMPACT_INNER의 배열 크기와 OBS_IMPACT 조건을 대조했다. NO_WRITE_GRID의 station 예외와 수심 기록 조건을 대조했다.
- RBH-1017·1051은 git 판정표의 초기 설명 대신 최종 보고서가 정정한 MAX_SLOPE·MIN_STRAT 해제 조건을 반영한다. RBH-1217은 NUDGING_SSH의 자료 읽기와 ASSIMILATION_SSH의 해수면 갱신을 구분한다. 해당 결론과 원문이 일치한다.
- 본문의 코드 HEAD와 날짜는 `57aecf589a408b1e5490d2db7f9bd0196062a44e`, `2026-09-18`이다. 소스 저장소의 `git show -s` 결과와 같다. `ROMS/Modules/mod_ncparam.F:653`의 `version = '4.3  '`이 본문의 버전 표기를 뒷받침한다.
- frontmatter의 관련 파일과 본문 링크를 합친 고유 상대 경로 10개는 모두 실제 파일을 가리킨다. 대상 노트에는 `/home/firesinger/`와 `[[`가 없다. 사용자가 지정한 한계 문장도 없다. mermaid 블록은 없다.
- 최종 frontmatter는 YAML로 정상 해석된다. 차이 표 199행은 모두 6열이다. 작업 시작본과 최종본의 차이는 정정 목록의 3줄뿐이다. 34–232행의 차이 표는 작업 시작본과 같다.

검증 방식은 원문과 보고서의 정적 대조이다. 대상 노트의 전체 줄 대조를 마쳤다. 미해결 항목은 없다.
