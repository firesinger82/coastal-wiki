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

## 작업 규범

모델별 행동 특성 차이를 흡수하기 위한 공통 작업 규범이다. 위 절대 규칙과 충돌하면 절대 규칙이 우선한다.

1. **명시 지시 없이는 수정하지 않는다.** 읽기·조사·보고가 기본값. 요청 범위를 임의로 넓히거나 좁히지 않는다. 인접한 개선점이 보이면 실행 대신 보고한다. 애매하면 신중한 동료처럼 판단하되, 해석에 따라 결과물이 달라지는 지점에서만 묻는다. (근거: 2026-07-24 total-read 사고)
2. **응답과 산출물 길이는 과제에 비례.** 노트·리포트에 요약 반복·보일러플레이트 절을 덧붙이지 않는다. 실질이 끝나면 멈춘다. 짧게 쓰려고 문장을 파편·화살표·약어로 압축하지 말고, 넣을 내용을 고르는 쪽으로 줄인다.
3. **subagent·workflow는 요청 시에만.** 직접 몇 번의 tool call로 끝나는 일을 위임하지 않는다. 검증 목적 위임은 금지 — 검증은 4항 소관.
4. **완료 판정은 자기신고가 아니다.** [`coastal-audit`](.claude/skills/coastal-audit/SKILL.md)의 Adversary·human gate와 [`tools/resume-gate/`](tools/resume-gate/README.md)의 `decision.json`은 모델 자기검증을 대체하는 장치가 아니라, 자기신고에 완료 권한을 주지 않기 위한 **외부 게이트**다. 모델의 자기검증 능력 향상을 이유로 제거·완화하지 않는다.
5. **자기수정은 짧게.** 사용자의 판단·코드·결론을 바꾸는 오류만 정정하고 계속 진행한다. 경위 서술·자책·오류 집계는 하지 않는다. 후속 질문이 곧 지적은 아니다 — 물은 것에 답한다.
6. **장기 작업은 첫 턴에 전체 사양을.** 자율·다단계 작업(전수 감사, 마이그레이션, 파일럿)은 목표·제약·완료조건을 처음에 모두 주는 편이 여러 턴에 걸쳐 점증적으로 지시하는 것보다 결과가 낫다. 사용자·AI 양쪽에 해당.

## 디렉토리 책임

| 경로 | 무엇이 들어가는가 | 무엇이 안 들어가는가 |
|---|---|---|
| `concepts/<topic>/` | 개념·이론·분석법·코드·예제·모델적용 + 응용 연구노트(`NN-applied-*`, [CONVENTIONS.md](CONVENTIONS.md) §8.1) | 특정 사례의 개인 결론 |
| `textbook/notes/theory-*` | 4-레이어 ① 이론 canonical — 교재 인용보강 이식분 (§8.1, [textbook/THEORY-LEDGER.md](textbook/THEORY-LEDGER.md) 추적) | 무인용 AI 합성 잔존 단언 |
| `models/<model>/source-analysis/` | 모델 소스코드 분석 (서브루틴별·모듈별) | 모델 사용 후기 |
| `models/<model>/manual-notes/` | 공식 메뉴얼 발췌·정리 (페이지 인용 필수) | 메뉴얼 없는 추정 |
| `models/<model>/web-refs/` | 공식 위키·논문·블로그 인용 정리 | 비인용 추측 |
| `textbook/notes/` | 교과서 챕터별 발췌·요약 (출처: `source_id` + 페이지, [textbook/sources.yml](textbook/sources.yml)) | 교과서 본문 그대로 복붙 |
| `examples/` | 개념을 가로지르는 실습 (재현 가능 코드/데이터) | 특정 프로젝트 산출물 |
| `experience/` | 위 3조건 통과한 검증 경험 | 미검증 직관 |

## 새 토픽·새 모델 생성 워크플로

- 새 토픽: [CONVENTIONS.md](CONVENTIONS.md) §8 (최소 시작 2파일 — 6파일 강제 없음, 템플릿은 `concepts/_template/`에서 작업내용에 맞게 복사)
- 새 모델: `models/_template/` 복사 → `models/<model>/` (구조·필수 항목은 템플릿 자체 참조)

## 작업 진입 시 우선 읽을 것

1. [README.md](README.md) — 전반
2. [INDEX.md](INDEX.md) — 현재 채워진 항목 맵
3. [CONVENTIONS.md](CONVENTIONS.md) — 작성 규약 (frontmatter, citation_status, canonical source)
4. [BOUNDARY.md](BOUNDARY.md) — modeling-wiki와의 경계
5. [textbook/POLICY.md](textbook/POLICY.md) — textbook 통합 규칙
6. [textbook/sources.yml](textbook/sources.yml) — source_id 매니페스트
7. [plan.md](plan.md) — 결정 기록 (Governance Decisions G1-G8 포함)

## 검색

- **`coastal-wiki` MCP** (`.mcp.json`) — `wiki_search`(BM25 + `citation_status`/`path_class` 필터, canonical만: concepts/models/textbook/experience, research·_archive·raw 제외) / `wiki_read`(section·grep·full, read-only sandbox) / `wiki_manifest`(git sha·dirty·doc count). 구현 `tools/llm-wiki-poc/`(FTS5, 순수 stdlib), 인덱스는 기동 시 자동 빌드(~0.5s, gitignore). 설계 [plan.md "LLM-Wiki 서빙 레이어"](plan.md), [plan.md G6](plan.md). (~~`mcp__qmd__query`~~ = 미설치 stale, 2026-06-21 FTS5로 대체)
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

- writer = 이 PC (WSL2 ext4, `~/coastal-wiki`) — **coastal-wiki 유일 writer**. 이 PC가 계산도 겸할 수 있으나 그 결과는 위키가 아닌 `coastal-runs`로(아래).
  - Windows 측 접근: `\\wsl$\Ubuntu\home\firesinger\coastal-wiki` (Obsidian 등 Windows 앱)
- reader = 다른 PC (git clone 후 git pull) — 위키에 대해 **pull 전용**. 리더 머신은 `git config pull.ff only` 권장(로컬 커밋 시 조용한 merge 대신 즉시 에러 → divergence 방지).
- **계산결과 → experience 채널**: 개인 run 결과는 위키에 직접 넣지 않고([RUNS-CHANNEL.md](RUNS-CHANNEL.md)) 별도 `coastal-runs` repo에 축적 → 3조건 게이트 통과분만 이 PC(writer)가 `experience/`로 promote. run 생산자는 여러 머신 가능(머신별 `runs/<host>/` 서브트리, 절대규칙 #8).
- 작업 후 항상 `git commit && git push` (push 전 `git pull` 로 origin 동기화 — 리더가 올린 변경 합류)
- **clone/세팅 시 1회 `bash tools/install-hooks.sh --writer|--reader`** — pre-commit(검증 + ★리더 커밋 거부 가드, R1 I-4) + post-merge·post-checkout·post-commit(검색 인덱스 자동 재빌드)을 설치. **리더 머신은 반드시 `--reader`** — 실수 커밋을 pre-commit 이 거부(미커밋 편집은 못 막으므로 리더 세션 지침은 별도 유지). 이후 `git pull`/커밋마다 `coastal-wiki` MCP 검색 인덱스 자동 갱신. python3 만 있으면 됨.
