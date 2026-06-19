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
| `verified` | 출처 명시 + 검증 완료 (AI cross-reference 또는 사용자 직접) | canonical 페이지로 정식 승격 |

**검증 방법 (2종)**:

- **AI cross-reference** (자동, 권장 1차): PDF를 markdown으로 변환(`textbook/md/`)한 뒤, 인용 문장을 페이지별로 프로그래밍 lookup. 글자 중복·OCR artifact는 정규화 후 매칭. `verification_method` 필드에 "AI programmatic cross-reference …" 명시, `verification_by`에 모델명 + "cross-ref" 명시.
- **사용자 직접 검토** (수동, 최종 권위): 원본 PDF 페이지 직접 확인. `verification_by`에 사용자 명시.

**사용자 override**: AI 검증된 `verified`는 사용자가 언제든 `source-needed`로 강등 가능. AI는 검증 책임의 1차 게이트, 사용자는 최종 권위.

**규칙**:
- 별도 `drafts/` 트리 **만들지 않음** (parallel tree drift 방지)
- 미검증 노트도 canonical 위치(`concepts/<topic>/01-concept.md` 등)에 둠. frontmatter 상태가 진실
- `INDEX.md`는 비-`verified` 항목을 **상태 컬럼**으로 표시
- `concepts/<topic>/`에서 다른 노트 인용 시 그 노트의 `citation_status`가 `verified`가 아니면 인용하는 쪽도 `source-needed`로 강등

## 2.1 Governance · Raw 문서의 frontmatter 예외

다음 문서는 정책·메타 성격이라 frontmatter 의무 면제:

- `README.md`, `CLAUDE.md`, `AGENTS.md`, `INDEX.md`, `plan.md`, `CONVENTIONS.md`, `BOUNDARY.md`
- 각 디렉토리의 `README.md`
- `_template/` 내 파일
- `textbook/POLICY.md`, `textbook/INDEX.md`, `textbook/sources.yml`

이 파일들은 콘텐츠가 아닌 거버넌스 layer. 변경 이력은 git이 책임.

### Vendor 원본 (raw) 예외 — D4 (2026-05-23)

다음은 우리 위키의 authored 콘텐츠가 아니라 외부 vendor 원본이라 frontmatter 규약을 적용하지 않는다:

- `models/*/raw/**` — 모델 공식 GitHub repo clone, 공식 PDF·website·wiki 다운로드
- `_staging/from-modeling-wiki/**` — 흡수 대기 자산 (promote 시 frontmatter 부여)
- `_archive/**` — 통합 이전 자산 보존본

이 트리는 또한 `.gitignore` 대상이거나(`models/*/raw/source_code/`, `models/*/raw/manuals/`) 일시 staging 이다. authored 노트(`source-analysis/`, `manual-notes/`, `web-refs/`, `manifest.md`, `README.md`)에서만 인용된다.

## 3. Canonical Source 규칙

- 같은 정보가 두 위치에 있으면 **canonical 한 곳만 사실의 출처**
- 다른 곳은 **요약 + canonical로의 링크**만
- 문서 상단에 `Canonical source: <경로>` 명시. self면 `self`

**구체 규칙**:
- 모델 메커닉 (서브루틴·알고리즘·구현) → `models/<model>/`이 canonical
- 도메인 개념 (정의·이론·분석법) → `concepts/<topic>/`이 canonical
- 교과서 발췌 → `textbook/notes/`가 canonical, 인용된 곳은 링크

**source_id 식별 단위 — 출처 구별 (G8c)**:

- 하나의 `source_id` = 하나의 bibliographic/work 단위 + edition/version. 같은 자료의 PDF·HTML 미러·로컬 사본은 동일 출처라 alias 허용.
- 별개 문서·에디션·repo·매뉴얼·논문·데이터셋·릴리스노트 시리즈는 **별도 source_id** 요구 — 이질 출처를 한 ID로 뭉뚱그리지 않는다 (예: 국립해양조사원고시 비조화상수 `khoa-notice-2021-7` ≠ 수치조류도·통합 조화상수 DB `khoa-tide-model`).
- 근거: FAIR R1.2 (정확한 provenance).

## 4. 인용 표기

### 본문 내

- 직접 인용: `> "원문…" (source_id, p.NN)`
- paraphrase: `… (source_id, ch3 §3.2)`
- 소스코드: `<repo>/path/file.f90:LN-LN`
- 외부 URL: `[제목](URL) (acc. YYYY-MM-DD)`

### source_id 사용 + 경로 표기 (G8b)

- 인용은 `textbook/sources.yml`에 등록된 안정적 ID 사용 (예: `holthuijsen2007`)
- **개인 절대경로 금지** (canonical 어디에도): 작성자의 로컬 머신·마운트·홈·드라이브·실행 워크스페이스를 **식별하는** 경로 — `D:\`·`E:\`·`C:\Users\`·`/mnt/[de]/`·`~/...`·`\\wsl$`. textbook 인용은 source_id로, 코드 예시 경로는 placeholder(`<KHOA_*.csv>`)나 repo-상대로, provenance(소스스캔 위치 등)는 repo-상대·중립 표기
- **허용 (개인환경 식별 아님)**: ① 소스코드 인용의 repo-상대 `models/<model>/raw/source_code/…/file.f90:LN` 또는 `file:line` 형식, ② 공식 매뉴얼·vendor 가 표기하는 설치·배포 경로(`C:\Program Files\…`, `/opt/…`)를 `manual-notes/`에서 *출처로* 인용
- 근거: Wilson et al. 2017 "Good enough practices in scientific computing"(portable paths), FAIR provenance

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
| `research/` | 후보·digest·watchlist. 검색 샘플과 AI 요약임을 명시. 본문에서 직접 인용 금지 |
| `drafts/` | 자유 (단 frontmatter `citation_status: draft-unsourced` 명시) |

**개인사례 자리표시자 금지 (G8d)**: canonical(`concepts/`·`models/`) 노트에 개인·프로젝트·실행 사례 기입을 요청하거나 공간을 예약하는 빈 heading·TODO·체크박스·프롬프트(예: `▢ User-experience cases`) **금지** — 개인 사례는 `experience/`. 면제: 공식 인용 대기 `source-needed` placeholder, 일반 미작성 섹션 stub, `_template/` 파일. 근거: canonical/experience 분리 + Diátaxis(reference 에 task 금지).

## 7. 변경 이력

큰 변경(구조·규약 변경): commit message 첫 줄에 `policy:` 또는 `structure:` prefix.

## 8. 새 토픽 최소 시작

기존 plan은 6파일 전체 생성을 요구했으나 Codex MODIFY 검토 반영해 **최소 시작 2파일**로 완화:

- 새 토픽 생성 시 **`README.md` + `01-concept.md`만 필수**
- 나머지 (02~06)는 sourced claim이 생기면 생성
- `INDEX.md`에 "미생성 섹션" 컬럼으로 진척 추적

## 9. 위키 무결성 검증 도구

`research/` 격리 enforce 와 본문 무결성 검증은 다음 스크립트로 수행 (정책 출처: [plan.md](plan.md) D3, M10):

- `tools/validate-research-isolation.sh` — concepts/, models/, experience/ 가 research/ 를 직접 참조하는지 + research/ 내 .md 가 `citation_status: draft-unsourced` 인지 검증. exit 0/1/2/3.
- `tools/install-hooks.sh` — `.git/hooks/pre-commit` 에 위 스크립트를 등록. 한 번 실행하면 commit마다 자동 검증.

새 PC 에서 clone 후: `bash tools/install-hooks.sh` 한 번 실행.

## 관련 문서

- [plan.md](plan.md) — 결정 기록 (G1-G7, M1-M10, D1-D4)
- [BOUNDARY.md](BOUNDARY.md) — modeling-wiki와의 경계 (통합 이전 정책의 역사적 기록)
- [textbook/POLICY.md](textbook/POLICY.md) — textbook 통합 정책
- [textbook/sources.yml](textbook/sources.yml) — source_id 매니페스트
