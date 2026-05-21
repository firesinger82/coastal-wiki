# CONVENTIONS — 작성 규약

이 위키 내 문서가 따라야 할 공통 규약. plan.md의 Governance Decisions에서 파생.

## 1. Frontmatter 필수 필드

모든 `.md` 문서 상단(`---` 블록)에 다음 필드:

```yaml
---
title: "<문서 제목>"
topic: <concepts/topic/ 경로의 토픽명. 없으면 생략>
canonical_source: <이 정보의 진짜 위치. 자기 자신이면 self>
citation_status: draft-unsourced | source-needed | verified
note_author: "<Claude Opus 4.7 (1M context) | Codex | 사용자 | ...>"
note_date: YYYY-MM-DD
verification_by: "<사용자 또는 verifier 명, verified 단계에서만 필수>"
verification_date: YYYY-MM-DD
---
```

예외: `_template/` 내 파일, `INDEX.md`, `README.md`는 frontmatter 자유.

## 2. 인용 상태 모델

| 상태 | 의미 | 허용 위치 |
|---|---|---|
| `draft-unsourced` | 초안. 출처·검증 미수행 | canonical 위치 그대로. frontmatter `citation_status: draft-unsourced` 명시 필수 |
| `source-needed` | 골격 OK, 인용 누락. 출처 보강 대기 | 같음 |
| `verified` | 출처 명시 + 사용자 검증 완료 | canonical 페이지로 정식 승격 |

**규칙**:
- 별도 `drafts/` 트리 **만들지 않음** (parallel tree drift 방지)
- 미검증 노트도 canonical 위치(`concepts/<topic>/01-concept.md` 등)에 둠. frontmatter 상태가 진실
- `INDEX.md`는 비-`verified` 항목을 **상태 컬럼**으로 표시
- `concepts/<topic>/`에서 다른 노트 인용 시 그 노트의 `citation_status`가 `verified`가 아니면 인용하는 쪽도 `source-needed`로 강등

## 2.1 Governance 문서의 frontmatter 예외

다음 문서는 정책·메타 성격이라 frontmatter 의무 면제:

- `README.md`, `CLAUDE.md`, `AGENTS.md`, `INDEX.md`, `plan.md`, `CONVENTIONS.md`, `BOUNDARY.md`
- 각 디렉토리의 `README.md`
- `_template/` 내 파일
- `textbook/POLICY.md`, `textbook/INDEX.md`, `textbook/sources.yml`

이 파일들은 콘텐츠가 아닌 거버넌스 layer. 변경 이력은 git이 책임.

## 3. Canonical Source 규칙

- 같은 정보가 두 위치에 있으면 **canonical 한 곳만 사실의 출처**
- 다른 곳은 **요약 + canonical로의 링크**만
- 문서 상단에 `Canonical source: <경로>` 명시. self면 `self`

**구체 규칙**:
- 모델 메커닉 (서브루틴·알고리즘·구현) → `models/<model>/`이 canonical
- 도메인 개념 (정의·이론·분석법) → `concepts/<topic>/`이 canonical
- 교과서 발췌 → `textbook/notes/`가 canonical, 인용된 곳은 링크

## 4. 인용 표기

### 본문 내

- 직접 인용: `> "원문…" (source_id, p.NN)`
- paraphrase: `… (source_id, ch3 §3.2)`
- 소스코드: `<repo>/path/file.f90:LN-LN`
- 외부 URL: `[제목](URL) (acc. YYYY-MM-DD)`

### source_id 사용

- `textbook/sources.yml`에 등록된 안정적 ID 사용 (예: `holthuijsen2007`)
- raw 파일명·Windows 경로 직접 사용 **금지**

## 5. 파일·디렉토리 명명

- 디렉토리·파일: **영문 lowercase + hyphen** (`tidal-analysis.md`)
- 본문 내용: 한·영 자유
- 6단계 파일은 `01-concept.md` ~ `06-model-application.md` (concepts 토픽 한정)
- textbook 노트: `<topic>-<source_id>-<chapter>.md` (예: `tides-holthuijsen2007-ch5.md`)

## 6. 화법 제한

| 위치 | 화법 |
|---|---|
| `concepts/`, `models/` | 객관 (3인칭, 출처 기반). "내가 해보니", "경험상" 금지 |
| `experience/` | 객관화 시도 (반복 관찰·재현 가능 명시) |
| `drafts/` | 자유 (단 frontmatter `citation_status: draft-unsourced` 명시) |

## 7. 변경 이력

큰 변경(구조·규약 변경): commit message 첫 줄에 `policy:` 또는 `structure:` prefix.

## 8. 새 토픽 최소 시작

기존 plan은 6파일 전체 생성을 요구했으나 Codex MODIFY 검토 반영해 **최소 시작 2파일**로 완화:

- 새 토픽 생성 시 **`README.md` + `01-concept.md`만 필수**
- 나머지 (02~06)는 sourced claim이 생기면 생성
- `INDEX.md`에 "미생성 섹션" 컬럼으로 진척 추적

## 관련 문서

- [plan.md](plan.md) — 결정 기록 (G1-G7)
- [BOUNDARY.md](BOUNDARY.md) — modeling-wiki와의 경계
- [textbook/POLICY.md](textbook/POLICY.md) — textbook 통합 정책
- [textbook/sources.yml](textbook/sources.yml) — source_id 매니페스트
