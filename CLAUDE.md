# coastal-wiki — Claude 진입점

## 이 위키의 정체

연안공학 도메인 지식의 **객관(canonical) 레이어**를 모은 single-writer 위키. 1차 축은 도메인 개념(concepts), 2차 축은 모델(models). 교과서(textbook)와 실습(examples)이 횡축. 개인 경험(experience)은 객관화 통과 후 별도 레이어로 추가.

전반은 [README.md](README.md) 참조.

## 절대 규칙 (위키 무결성)

1. **객관 레이어가 먼저**. `concepts/`와 `models/` 안의 단언은 **모두 출처 인용** 필수 (소스코드 file:line, 메뉴얼 페이지, 논문 인용, 교과서 챕터).
2. **개인 경험은 `experience/`에만**. 그것도 (a) 반복 관찰 (b) 객관 데이터 근거 (c) 다른 곳에서 재현 가능 — 세 조건 모두 만족 시.
3. **AI 요약은 원본과 명확히 구분**. frontmatter `citation_status` 필드 ([CONVENTIONS.md](CONVENTIONS.md) §2) — `draft-unsourced` / `source-needed` / `verified`.
4. **모델 적용 케이스는 객관 가능한 것만**. "내가 해보니" 화법 금지 (`experience/`로 이동).
5. **단일 writer**. 다른 PC에서는 절대 수정 금지(읽기 전용). 동시 편집 conflict 방지.
6. **Canonical source 분리** ([CONVENTIONS.md](CONVENTIONS.md) §3): 모델 메커닉 → `models/<model>/`, 도메인 개념 → `concepts/<topic>/`. 다른 곳에는 요약 + 링크만.
7. **textbook 인용은 `source_id` 기반**. canonical 본문에서 raw 파일명·작성자 로컬 경로 직접 사용 금지 (repo-상대 `file:line`·공식 vendor 경로 인용·`sources.yml` 레지스트리는 예외 — [CONVENTIONS.md](CONVENTIONS.md) §4). 매니페스트는 [textbook/sources.yml](textbook/sources.yml).
8. **위키는 케이스 *공급원*, 저장소가 아니다**. 개인 run 결과·calibration 수치·작성자/프로젝트 실행에만 의존하는 운영 지침은 canonical(`concepts/`·`models/`·`textbook/`)에 두지 않는다 — 위키를 바탕으로 케이스는 별도에서 구축. 단, 소스코드·식·알고리즘이 *main claim*인 실패패턴·휴리스틱·플레이북은 `models/<model>/source-analysis/{failure-patterns,heuristics,playbooks}/` 허용([plan.md](plan.md) G8/triage), `06-model-application.md`는 요약+source-analysis 링크 wrapper로 유지. 제거할 자산은 마이그레이션 중이면 `_staging/`·`_archive/` 경유(즉시 삭제는 별도 게이트). 근거: reference↔how-to 분리(Diátaxis)·SSOT/DRY. ([CONVENTIONS.md](CONVENTIONS.md) §3·§4·§6, [plan.md](plan.md) G8.)

## 디렉토리 책임

| 경로 | 무엇이 들어가는가 | 무엇이 안 들어가는가 |
|---|---|---|
| `concepts/<topic>/` | 개념·이론·분석법·코드·예제·모델적용 (도메인 관점) | 특정 사례의 개인 결론 |
| `models/<model>/source-analysis/` | 모델 소스코드 분석 (서브루틴별·모듈별) | 모델 사용 후기 |
| `models/<model>/manual-notes/` | 공식 메뉴얼 발췌·정리 (페이지 인용 필수) | 메뉴얼 없는 추정 |
| `models/<model>/web-refs/` | 공식 위키·논문·블로그 인용 정리 | 비인용 추측 |
| `textbook/notes/` | 교과서 챕터별 발췌·요약 (출처: `source_id` + 페이지, [textbook/sources.yml](textbook/sources.yml)) | 교과서 본문 그대로 복붙 |
| `examples/` | 개념을 가로지르는 실습 (재현 가능 코드/데이터) | 특정 프로젝트 산출물 |
| `experience/` | 위 3조건 통과한 검증 경험 | 미검증 직관 |

## 새 토픽 생성 워크플로 (최소 시작)

[CONVENTIONS.md](CONVENTIONS.md) §8 — 6파일 전체 생성 강제하지 않음.

1. `concepts/<topic>/` 디렉토리 생성
2. **최소 필수 2 파일**: `README.md` + `01-concept.md` (frontmatter `citation_status` 명시)
3. 나머지 (02~06)는 sourced claim이 생기면 그때 생성
4. 관련 textbook 챕터는 `textbook/notes/<topic>-<source_id>-chN.md`로 발췌 (인용은 [textbook/sources.yml](textbook/sources.yml)의 `source_id` 사용)
5. `INDEX.md`에 토픽 등록 (미생성 섹션 컬럼으로 진척 추적)

전체 6파일 템플릿이 필요하면 `concepts/_template/`에서 골라 복사.

## 새 모델 추가 워크플로

1. `models/_template/` 복사해 `models/<model>/`로
2. `README.md`에 모델 정체성·라이선스·공식 사이트
3. `source-analysis/` — 주요 서브루틴별 노트
4. `manual-notes/` — 메뉴얼 챕터별 노트
5. `web-refs/` — 공식 wiki·논문·기술 블로그 인용

## 작업 진입 시 우선 읽을 것

1. [README.md](README.md) — 전반
2. [INDEX.md](INDEX.md) — 현재 채워진 항목 맵
3. [CONVENTIONS.md](CONVENTIONS.md) — 작성 규약 (frontmatter, citation_status, canonical source)
4. [BOUNDARY.md](BOUNDARY.md) — modeling-wiki와의 경계
5. [textbook/POLICY.md](textbook/POLICY.md) — textbook 통합 규칙
6. [textbook/sources.yml](textbook/sources.yml) — source_id 매니페스트
7. [plan.md](plan.md) — 결정 기록 (Governance Decisions G1-G8 포함)

## 검색

- `mcp__qmd__query` — BM25/시맨틱 (수동 인덱스 빌드 필요, [plan.md G6](plan.md))
- 빠른 키워드: `rg "키워드" ~/coastal-wiki -g "*.md" -g "*.yml"` — 전체 트리 스코프 (concepts/models/textbook/examples/experience/governance 문서 포함)
- 토픽·상태 필터: frontmatter 검색 — `rg "citation_status: verified" -l ~/coastal-wiki`
- 큰 출력은 `ctx_execute(language: "shell", code: "rg ...")` 경유

## 사용자 워크플로 (santa-method)

큰 산출물 작성·구조 변경 시:
1. `plan.md`에 변경 계획 작성 (Opus, Plan mode)
2. `/codex:adversarial-review`로 비판 검토
3. 피드백 반영
4. Opus로 실제 변경
5. `/codex:review`로 최종 검토

미세 노트 추가나 출처 인용 보강은 위 사이클 skip 가능.

## 동기화

- writer = 이 PC (WSL2 ext4, `~/coastal-wiki`)
  - Windows 측 접근: `\\wsl$\Ubuntu\home\firesinger\coastal-wiki` (Obsidian 등 Windows 앱)
- reader = 다른 PC (git clone 후 git pull)
- 작업 후 항상 `git commit && git push`
