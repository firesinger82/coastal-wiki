---
name: coastal-promote
description: research/inbox/_archive 항목을 concepts/<topic>/ 또는 models/<MODEL>/web-refs/manual-notes/source-analysis/ 의 정확한 위치로 promote. 분류→사용자 승인→본문 edit + archive 역추적 마킹. citation_status 자동 verified 부여 금지. 트리거: "promote", "inbox 정리", "W## archive promote".
---

# coastal-promote

`research/inbox/_archive/` 에 모인 트리아지 통과 항목을 `concepts/` · `models/` 의 canonical 위치로 옮기는 좁은 워크플로 skill.

이 skill은 `research/README.md` 의 Promote 정책과 `CLAUDE.md` 절대규칙 #1·#3·#6 의 실행 도구이다. 정책 자체를 바꾸지 않는다.

## 언제 작동

- 사용자가 "promote", "inbox 정리", "archive promote", "W## promote" 같은 표현을 쓸 때
- 새 Hermes ingest commit 후 `research/inbox/_archive/<YEAR>/` 에 promote 후보가 쌓였을 때
- INDEX.md 의 `WIP`/`DRAFT` 토픽에 채울 새 출처가 archive 에 있을 때

## 절대 금지

1. **`citation_status: verified` 자동 부여 금지.** archive 의 arxiv abstract·github issue body 는 1차 출처일 뿐. promote 후 기본값은 `source-needed` (또는 archive 가 이미 source-needed 면 그대로). verified 승격은 사용자 또는 사용자 승인 받은 AI cross-reference 의 책임.
2. **`_template/`, `_archive/` 자체, governance 문서 (README/CLAUDE/INDEX/CONVENTIONS/BOUNDARY/plan.md) 수정 금지.**
3. **archive 원본 파일 삭제 금지.** `promoted_to` + `promoted_date` frontmatter 필드만 추가 (역추적 + 중복감지).
4. **사용자 승인 없이 본문 파일 edit 금지.** 분류표 출력 → 승인 → edit 순서 엄수.

## 입력

- archive 디렉토리 (예: `research/inbox/_archive/2026/`) — 기본값: 가장 최신 연도
- 또는 명시적 파일 path list
- 또는 주차 식별자 (예: `--week 2026-W22` → discovered_date 기준 필터)

## 5단계 워크플로

### 1. 읽기

대상 archive `.md` 들의 frontmatter 와 본문 핵심을 읽는다:

- frontmatter: `title`, `source_url`, `source_type`, `promote_candidate`, `citation_status`, `query`
- Hermes 강화 prompt 가 채워뒀다면: `suggested_destination`, `suggested_section`, `classification_confidence`
- 본문 첫 단락 + 키워드 섹션 (`## 관련 모델/개념 키워드`)

이미 `promoted_to` 필드가 있는 파일은 skip (중복 promote 방지).

### 2. 분류

각 항목의 destination 을 다음 룰셋으로 추론:

| 입력 패턴 | Destination |
|---|---|
| `source_type: github` + URL 의 repo 가 `adcirc/adcirc`, `Deltares/Delft3D`, `myroms/roms`, `openearth/xbeach`, `NOAA-EMC/WW3`, `dsi-llc/EFDC`, `SCHISM-Dev/schism` 등 모델 repo | `models/<MODEL>/web-refs/<topic-or-feature>.md` |
| `source_type: github` + 이슈/PR이 알고리즘·코드 변경 본질 | `models/<MODEL>/source-analysis/` (사용자 확인) |
| `source_type: github` + release notes | `models/<MODEL>/web-refs/releases.md` (있으면 append, 없으면 신규) |
| `source_type: arxiv` + 키워드 `storm surge` `surge emulation` `ML emulator` | `concepts/storm-surge/07-ml-emulators.md` (PACT 사례 참조) |
| `source_type: arxiv` + 키워드 `wave` `spectral` `swan` | `concepts/waves/04-code-and-tools.md` 또는 `02-theory.md` |
| `source_type: arxiv` + 키워드 `sediment` `morphology` | `concepts/sediment-transport/05-examples.md` 또는 `04-code-and-tools.md` |
| `source_type: arxiv` + 키워드 `tide` | `concepts/tides/<적절 0X>` |
| `source_type: arxiv` + 키워드 `SST` `ocean temperature` `MHW` | `concepts/sst/<적절 0X>` |
| `source_type: arxiv` + 키워드 `current` `circulation` | `concepts/currents/<적절 0X>` |
| `source_type: arxiv` + 키워드 `longshore` `littoral` | `concepts/littoral-drift/<적절 0X>` |
| `source_type: blog` + 공식기관 (NOAA/USGS/KHOA/Deltares/JMA) + 도메인 적합 | `models/<MODEL>/web-refs/` 또는 `concepts/<topic>/04-code-and-tools.md` web-refs 절 |
| `source_type: blog` + landing page (USGS coastal-change 같은 evergreen) | archive 유지 (`promote_candidate: undecided` → `watchlist`로 강등 제안) |
| `source_type: paper` (journal) | `source_type: arxiv` 와 동일 규칙 |
| `promote_candidate: undecided` 인 항목 전체 | 사용자에게 한 줄씩 묻기 |

대상 파일이 없으면 신규 생성 후보로 표시 (예: `models/Delft3D/web-refs/releases.md`).

### 3. 분류표 출력

다음 형식의 마크다운 표로 사용자에게 보여준다:

```
| # | archive 파일 | source_type | 추천 destination | 추천 섹션/엔트리 | confidence | 사유 |
|---|---|---|---|---|---|---|
| 1 | 2026-05-25-arxiv-pact-...md | arxiv | concepts/storm-surge/07-ml-emulators.md | 새 entry "PACT (Liu 2026)" | high | "storm surge" + "emulation" 키워드, INDEX 상 07 이미 PACT 등재됨 → SKIP |
| 2 | 2026-05-25-deltares-delft3d-2026-02.md | github release | models/Delft3D/web-refs/releases.md (신규) | "2026.02 release" | high | Deltares/Delft3D repo, release notes 발췌됨 |
| ...
```

각 행 끝에 사용자 확인 액션 명시: **promote** / **skip** / **재분류 필요** / **사용자 결정 필요**.

### 4. 실행 (사용자 승인 후)

승인된 항목에 대해서만:

**4-1. 대상 파일 edit**

- 파일이 있으면: 적절한 절 (예: `## ML emulators` 또는 `## Web references`) 끝에 새 entry 추가. 형식:
  ```markdown
  ### <title>
  - 출처: [<source_url>](<source_url>) (<source_type>, discovered <discovered_date>)
  - 요약: <archive 본문 첫 단락 또는 abstract 핵심 1-2문장>
  - citation_status: source-needed
  - <필요 시> 인용 검증 TODO: <무엇을 verify 해야 verified 가 되는지>
  ```
- 파일이 없으면: `concepts/<topic>/_template/` 또는 `models/_template/` 구조 참조해 신규 파일 작성. frontmatter `citation_status: source-needed` 명시.
- 파일 상단 frontmatter `citation_status` 가 verified 면 그대로 두고, 새 entry 만 source-needed 로 추가 (CONVENTIONS §3 의 mixed 정책).

**4-2. archive 파일 마킹**

archive 원본 frontmatter 에 다음 2개 필드 추가 (삭제 절대 금지):

```yaml
promoted_to: <relative-path-to-destination-file>
promoted_date: YYYY-MM-DD
```

본문은 손대지 않는다.

**4-3. INDEX.md 갱신 영역 표시**

각 promote 가 INDEX.md 의 어느 행을 영향주는지 출력 (자동 edit X — 사용자가 직접 갱신).

### 5. 마무리

- 변경된 파일 목록 출력
- commit 메시지 초안 출력 (사용자가 직접 commit):
  ```
  refactor(research): promote N items from <archive-scope> to <destinations>

  - <archive 파일> → <destination> (citation_status: source-needed)
  - ...

  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
  ```
- pre-commit hook (`tools/validate-research-isolation.sh`) 위반 여부 사전 점검: archive 파일은 inbox 트리 안에 있어 frontmatter `citation_status` 가 변하지 않아야 함 — 새 필드 `promoted_to` 만 추가하므로 통과해야 정상.

## Skill 호출 예시

사용자: "W22 archive promote 진행하자"

→ skill 은 `research/inbox/_archive/2026/` 의 `discovered_date: 2026-05-25` 항목 16건 중 `promoted_to` 가 없는 것만 대상으로 잡고, 위 5단계 실행. 첫 응답은 분류표 (단계 3) 까지만.

## 후속 정책

- promote 후에도 `citation_status: source-needed` 상태인 entry 는 INDEX.md 의 해당 토픽 상태에 `(N source-needed pending)` 로 표기 (사용자 결정).
- 사용자가 cross-reference 검증 후 verified 로 승격 (이는 별도 워크플로, 본 skill 영역 아님).
- archive `promoted_to` 가 채워진 파일은 다음 트리아지 사이클에서 `## 출처` 인용 변경 시 reference graph 로 자동 활용 가능.
