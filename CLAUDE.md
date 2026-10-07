# coastal-wiki — Claude 진입점

## 이 위키의 정체

연안공학 도메인 지식의 **객관(canonical) 레이어**를 모은 single-writer 위키. 1차 축은 도메인 개념(concepts), 2차 축은 모델(models). 교과서(textbook)와 실습(examples)이 횡축. 개인 경험(experience)은 객관화 통과 후 별도 레이어로 추가.

전반은 [README.md](README.md) 참조. 요구사항·범위·운영 제약의 기준선(SSOT)은 [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md)다. 문서 간 충돌 시 **최신 사용자 명시 지시 > PROJECT_REQUIREMENTS.md > CLAUDE.md·AGENTS.md·BUILD-PLAN.md > 기타 문서**.

## 절대 규칙 (위키 무결성)

1. **객관 레이어가 먼저**. `concepts/`와 `models/` 안의 단언은 **모두 출처 인용** 필수 (소스코드 file:line, 메뉴얼 페이지, 논문 인용, 교과서 챕터).
2. **개인 경험은 `experience/`에만**. 그것도 (a) 반복 관찰 (b) 객관 데이터 근거 (c) 다른 곳에서 재현 가능 — 세 조건 모두 만족 시.
3. **AI 요약은 원본과 명확히 구분**. frontmatter `citation_status` 필드 ([CONVENTIONS.md](CONVENTIONS.md) §2) — `draft-unsourced` / `source-needed` / `verified`.
4. **모델 적용 케이스는 객관 가능한 것만**. "내가 해보니" 화법 금지 (`experience/`로 이동).
5. **단일 writer**. 다른 PC에서는 절대 수정 금지(읽기 전용). 동시 편집 conflict 방지.
6. **Canonical source 분리** ([CONVENTIONS.md](CONVENTIONS.md) §3): 모델 메커닉 → `models/<model>/`, 도메인 개념 → `concepts/<topic>/`. 다른 곳에는 요약 + 링크만.
7. **textbook 인용은 `source_id` 기반**. canonical 본문에서 raw 파일명·작성자 로컬 경로 직접 사용 금지 (repo-상대 `file:line`·공식 vendor 경로 인용·`sources.yml` 레지스트리는 예외 — [CONVENTIONS.md](CONVENTIONS.md) §4). 매니페스트는 [textbook/sources.yml](textbook/sources.yml).
8. **위키는 케이스 *공급원*, 저장소가 아니다**. 개인 run 결과·calibration 수치·작성자/프로젝트 실행에만 의존하는 운영 지침은 canonical(`concepts/`·`models/`·`textbook/`)에 두지 않는다 — 위키를 바탕으로 케이스는 별도에서 구축. 단, 소스코드·식·알고리즘이 *main claim*인 실패패턴·휴리스틱·플레이북은 `models/<model>/source-analysis/{failure-patterns,heuristics,playbooks}/` 허용([plan.md](plan.md) G8/triage), `06-model-application.md`는 요약+source-analysis 링크 wrapper로 유지. 제거할 자산은 마이그레이션 중이면 `_staging/`·`_archive/` 경유(즉시 삭제는 별도 게이트). 근거: reference↔how-to 분리(Diátaxis)·SSOT/DRY. ([CONVENTIONS.md](CONVENTIONS.md) §3·§4·§6, [plan.md](plan.md) G8.)

## 작업 방식

2026-10-02 사용자 결정으로 하네스·계약·승인 절차를 걷어냈다. 위키의 일은 자료를 읽고 출처를 달아 노트로 정리하고 커밋하는 것이며, 절차도 그 크기에 맞춘다.

1. **요청받은 범위만 한다.** "전수·계속·완벽"을 범위 확장으로 읽지 않는다. 모델 분석 대상은 모델의 물리·수치해법·입출력·실행 흐름·문서까지이고, MPI 뷰어·범용 라이브러리·설치 도구 내부는 판독하지 않는다.
2. **토큰이 많이 드는 일은 Codex가 한다.** 대량 판독(코드·문서·PDF 쪽 이미지 포함), 기록 작성, 반복 수정은 Codex(`gpt-6.1-sol`, `--model` 명시)에 맡긴다. Claude는 작업 나누기, 지시문, 기계 확인, 다른 모델로서의 소량 표본 검증, 판단과 보고를 맡는다. 몇 번의 도구 호출로 끝나는 작은 일은 Claude가 직접 한다. 형식 계약·의무 리뷰 사이클은 없다(2026-10-03 사용자 지시).
3. **완료 보고는 사실대로.** 실제로 확인한 것과 하지 않은 것(실행·수치·물리 검증 등)을 구분해 적는다. 확인하지 않은 것을 완료·검증으로 쓰지 않는다.
4. **커밋 전 diff 요약을 보여준다.** 묻는 것은 결론이 바뀌는 판단뿐이다.
5. **산출물 길이는 과제에 비례.** 요약 반복·보일러플레이트를 붙이지 않는다.
   - **보고 문체(ASD-STE100식 통제 문체, 2026-10-03 사용자 승인):** 한 문장에 한 사실. 주어를 밝히고 능동형으로 쓴다. 같은 대상은 처음 정한 용어로만 부른다. 화살표·약어·기호로 문장을 압축하지 않는다. 확인한 것, 확인하지 않은 것, 추정을 문장마다 구분한다. 숫자에는 어디서 센 값인지 붙인다.
   - **그림 우선:** 계산 흐름·호출 순서·격자 위치처럼 관계가 핵심인 내용은 mermaid 그림으로 그리고, 상자마다 file:line 출처를 단다. 진행 현황은 [판독 원장 대시보드](_staging/recovery/dashboard.html)(판독 기록에서 스크립트로 집계)로 본다.
   - **의미 보존:** 원문을 요약하거나 옮길 때 부정·조건·수량·의무·불확실성을 그대로 유지한다(2026-10-07, kar-plain에서 차용).
   - **렌더 확인:** 그림·페이지·영상은 실제로 렌더해 확인하기 전에는 완료로 보고하지 않는다(2026-10-07, kar-plain에서 차용).
6. 사용자 요청 없이 게이트·계약·승인 절차를 다시 만들지 않는다. **sudo는 쓰지 않는다** — 실행도, 사용자에게 제안도 하지 않는다(root 소유·root 설치가 필요한 설계 금지).

Claude 모델 지정: 기본 **Fable 5.1 (`claude-fable-5-1`)**, 자동 fallback 금지. 변경은 사용자 지시로.

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

## 작업별 문서 안내

매 작업마다 아래 문서를 모두 읽지 않는다. 필요한 문서의 관련 절을 찾고, 이미 읽은 지침은 변경되었거나 새 판단에 필요한 경우에만 다시 읽는다.

- 구조를 파악할 때: [README.md](README.md)와 해당 디렉터리 README. 항목을 찾을 때는 [INDEX.md](INDEX.md)의 관련 부분.
- 모델 기능 근거를 보강·비교·결합할 때: [BUILD-PLAN.md](BUILD-PLAN.md)의 해당 단계와 완료 조건.
- 노트·인용·frontmatter를 바꿀 때: [CONVENTIONS.md](CONVENTIONS.md)의 해당 규칙.
- 다른 위키와 책임 경계를 바꿀 때: [BOUNDARY.md](BOUNDARY.md).
- 교과서를 편입·인용할 때: [textbook/POLICY.md](textbook/POLICY.md)와 [textbook/sources.yml](textbook/sources.yml)의 해당 source_id.
- 중단 작업을 재개할 때: [plan.md의 현재 작업](plan.md#현재-작업)과 연결된 실행 기록. 과거 결정이 필요한 경우에만 해당 절을 검색한다. 현재 사용자 지시가 우선한다.

## 검색

- **`coastal-wiki` MCP** (`.mcp.json`) — `wiki_search`(BM25 + `citation_status`/`path_class` 필터, canonical만: concepts/models/textbook/experience, research·_archive·raw 제외) / `wiki_read`(section·grep·full, read-only sandbox) / `wiki_manifest`(git sha·dirty·doc count). 구현 `tools/llm-wiki-poc/`(FTS5, 순수 stdlib), 인덱스는 기동 시 자동 빌드(~0.5s, gitignore). 설계 [plan.md "LLM-Wiki 서빙 레이어"](plan.md), [plan.md G6](plan.md). (~~`mcp__qmd__query`~~ = 미설치 stale, 2026-06-21 FTS5로 대체)
- 빠른 키워드: `rg "키워드" ~/coastal-wiki -g "*.md" -g "*.yml"` — 전체 트리 스코프 (concepts/models/textbook/examples/experience/governance 문서 포함)
- 토픽·상태 필터: frontmatter 검색 — `rg "citation_status: verified" -l ~/coastal-wiki`
- 큰 출력은 `ctx_execute(language: "shell", code: "rg ...")` 경유

## 동기화

- writer = 이 PC (WSL2 ext4, `~/coastal-wiki`) — **coastal-wiki 유일 writer**. 이 PC가 계산도 겸할 수 있으나 그 결과는 위키가 아닌 `coastal-runs`로(아래).
  - Windows 측 접근: `\\wsl$\Ubuntu\home\firesinger\coastal-wiki` (Obsidian 등 Windows 앱)
- reader = 다른 PC (git clone 후 git pull) — 위키에 대해 **pull 전용**. 리더 머신은 `git config pull.ff only` 권장(로컬 커밋 시 조용한 merge 대신 즉시 에러 → divergence 방지).
- **계산결과 → experience 채널**: 개인 run 결과는 위키에 직접 넣지 않고([RUNS-CHANNEL.md](RUNS-CHANNEL.md)) 별도 `coastal-runs` repo에 축적 → 3조건 게이트 통과분만 이 PC(writer)가 `experience/`로 promote. run 생산자는 여러 머신 가능(머신별 `runs/<host>/` 서브트리, 절대규칙 #8).
- 작업 후 항상 `git commit && git push` (push 전 `git pull` 로 origin 동기화 — 리더가 올린 변경 합류)
- **clone/세팅 시 1회 `bash tools/install-hooks.sh --writer|--reader`** — pre-commit(검증 + ★리더 커밋 거부 가드, R1 I-4) + post-merge·post-checkout·post-commit(검색 인덱스 자동 재빌드)을 설치. **리더 머신은 반드시 `--reader`** — 실수 커밋을 pre-commit 이 거부(미커밋 편집은 못 막으므로 리더 세션 지침은 별도 유지). 이후 `git pull`/커밋마다 `coastal-wiki` MCP 검색 인덱스 자동 갱신. python3 만 있으면 됨.
