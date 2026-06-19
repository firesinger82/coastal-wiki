# coastal-wiki

연안공학 도메인 지식의 객관 레이어(canonical)를 집적하는 단일 writer 위키.

## 정체성

- **1차 축**: `concepts/` — 도메인 개념(조석, 파랑, 표사이동, 흐름 등). 개념 → 일반론 → 분석법 → 코드 → 예제 → 모델적용.
- **2차 축**: `models/` — 모델별 객관 자료(소스코드 분석, 메뉴얼 발췌, 웹/논문 자료).
- **횡축**: `textbook/` — `D:\Study\textbook`의 교과서 자료를 참조·인용해 노트화.
- **연결**: `examples/` — 개념을 가로지르는 통합 실습.
- **유보**: `experience/` — 모델링 경험에서 객관화·논리정밀화 검증을 통과한 정보만. 객관 레이어가 어느 정도 자리잡은 후 추가.

## 핵심 규칙

1. **객관 레이어 우선**. 개인 경험은 `experience/`에만, 그것도 통과 기준 만족 후.
2. **모든 단언은 출처 명시** (소스코드 라인, 메뉴얼 페이지, 논문 인용, 교과서 챕터).
3. **AI 요약은 frontmatter `citation_status`로 추적** ([CONVENTIONS.md](CONVENTIONS.md) §2). `verified` 승격 책임자 = 사용자.
4. **Canonical source 분리**: 모델 메커닉 → `models/`, 도메인 개념 → `concepts/`. 다른 곳은 요약 + 링크만.
5. **canonical 은 안정 식별자만**. textbook 인용 = `source_id` ([textbook/sources.yml](textbook/sources.yml)), 소스코드 = repo-상대 `file:line`. 작성자 로컬 절대경로(`D:\`·`E:\`·`/mnt/`·`~/`) 금지 ([CONVENTIONS.md](CONVENTIONS.md) §4). 개인 케이스·run 결과는 위키 밖 — 위키는 케이스 *공급원* ([CLAUDE.md](CLAUDE.md) 절대규칙 8).
6. **단일 writer**. 이 PC가 작성자, 다른 PC는 read-only.
7. **수정 이력은 git이 책임진다**. 임의 삭제·재구성 시 reasoning을 커밋 메시지에 기록.

## 디렉토리

| 경로 | 역할 |
|---|---|
| `concepts/<토픽>/` | 도메인 개념 (1차 축). `_template/` 복제해서 새 토픽 생성 |
| `models/<모델>/` | 모델별 객관 자료 (2차 축). `source-analysis/`, `manual-notes/`, `web-refs/` |
| `textbook/` | `D:\\Study\\textbook` 통합 노트와 인용. 원본 PDF는 wiki에 복사 안 함 |
| `examples/` | 개념을 가로지르는 실습 |
| `experience/` | 객관화 통과한 경험 |
| `research/` | Hermes `coastal-research` 워크벤치. X·arXiv·블로그·툴 후보 수집, digest, watchlist. 본문에서 직접 인용 금지 |

## 진입 순서

새 토픽 작업 시 (최소 시작, [CONVENTIONS.md](CONVENTIONS.md) §8):
1. `concepts/<topic>/` 디렉토리 생성
2. **2 파일 우선 작성**: `README.md` + `01-concept.md` (frontmatter `citation_status` 명시)
3. 해당 토픽 관련 textbook 참조를 `textbook/notes/`에 추출 (`source_id` 페어 사용)
4. 02~06 단계 파일은 sourced claim이 쌓이면 생성 (전체 템플릿은 `concepts/_template/`에서 골라 복사)
5. 관련 모델 객관 분석은 `models/<model>/`에 두고 `concepts/<topic>/06-model-application.md`에서 링크
6. 예제는 `examples/<scenario>/`에 둠

## 동기화

이 PC = writer, 다른 PC = reader. git push/pull로 sync.

## 우선 읽을 문서

- [CLAUDE.md](CLAUDE.md) — Claude 진입점
- [AGENTS.md](AGENTS.md) — Codex 진입점
- [INDEX.md](INDEX.md) — 전체 맵
- [CONVENTIONS.md](CONVENTIONS.md) — 작성 규약 (frontmatter, citation_status, canonical source)
- [BOUNDARY.md](BOUNDARY.md) — modeling-wiki와의 경계 정책
- [plan.md](plan.md) — 결정 기록 (Governance Decisions G1-G7 포함)
- [textbook/POLICY.md](textbook/POLICY.md), [textbook/sources.yml](textbook/sources.yml) — textbook 통합 정책 + 매니페스트
