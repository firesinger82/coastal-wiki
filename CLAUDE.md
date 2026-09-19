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

## 작업 규범

모델별 행동 특성 차이를 흡수하기 위한 공통 작업 규범이다. 위 절대 규칙과 충돌하면 절대 규칙이 우선한다.

1. **현재 요청의 범위와 완료 조건을 따른다.** 조사 요청은 조사 결과까지, 변경 요청은 필요한 구현·수정·검증까지 마친다. 조사·질문만 요청된 경우 분석 대상 원문을 임의로 수정하지 않는다. 이미 허가된 범위의 되돌릴 수 있는 작업은 중간 확인 없이 계속한다. 인접 개선점은 별도로 보고하고 범위를 임의로 넓히거나 좁히지 않는다. 결과를 좌우하는 정보가 없거나 적용되는 별도 승인 조건이 충족되지 않은 경우에만 묻는다. 기존 모델 감사의 범위·사람 게이트는 유지한다. (근거: 2026-07-24 total-read 사고와 현재 사용자 지시 우선 원칙)
2. **응답과 산출물 길이는 과제에 비례.** 노트·리포트에 요약 반복·보일러플레이트 절을 덧붙이지 않는다. 실질이 끝나면 멈춘다. 짧게 쓰려고 문장을 파편·화살표·약어로 압축하지 말고, 넣을 내용을 고르는 쪽으로 줄인다.
3. **위임은 아래 [역할 분담](#역할-분담-claude--codex)의 Codex 계약으로.** 그 밖의 subagent·workflow는 요청 시에만 쓴다. 직접 몇 번의 tool call로 끝나는 일은 위임하지 않는다. 검증 *실행*(테스트·검사·evidence 수집)은 Codex에 맡길 수 있으나 완료 *판정*은 위임하지 않는다 — 판정은 4항 소관.
4. **완료 판정은 자기신고가 아니다.** [`coastal-audit`](.claude/skills/coastal-audit/SKILL.md)의 Adversary·human gate와 [`tools/resume-gate/`](tools/resume-gate/README.md)의 `decision.json`은 모델 자기검증을 대체하는 장치가 아니라, 자기신고에 완료 권한을 주지 않기 위한 **외부 게이트**다. 모델의 자기검증 능력 향상을 이유로 제거·완화하지 않는다.
5. **자기수정은 짧게.** 사용자의 판단·코드·결론을 바꾸는 오류만 정정하고 계속 진행한다. 경위 서술·자책·오류 집계는 하지 않는다. 후속 질문이 곧 지적은 아니다 — 물은 것에 답한다.
6. **장기 작업은 첫 턴에 전체 사양을.** 자율·다단계 작업(전수 감사, 마이그레이션, 파일럿)은 목표·제약·완료조건을 처음에 모두 주는 편이 여러 턴에 걸쳐 점증적으로 지시하는 것보다 결과가 낫다. 사용자·AI 양쪽에 해당.

## 모델 분석 범위 통제

2026-09-12 사용자 정정: XBeach 분석에서 부속 MPI/Jumpshot 뷰어 내부 판독으로 이탈한 작업을 중단한다. 모든 모델 분석과 재개 작업에 다음을 적용한다.

- **“전수”, “완벽 마무리”, “GOAL”, “계속 진행”은 범위 확장 허가가 아니다.** 대상은 요청한 모델의 물리·수치해법·입출력·실행 흐름·모델 문서와 그 연결 검증이다. 파일이 동봉되어 있거나 인벤토리에 unread로 남았다는 이유로 분석 대상을 늘리지 않는다.
- MPI/Jumpshot 뷰어, 범용 라이브러리, 설치 도구의 내부 구현·클래스·바이트코드를 재귀적으로 판독하지 않는다. 의존성은 모델에 필요한 버전·빌드·링크·실행·호출 인터페이스까지만 확인한다. 모델 자체의 MPI 호출과 병렬 수치 동작은 모델 분석 범위에 포함된다.
- 예외는 사용자가 해당 부속 구성요소 분석을 명시적으로 요청했거나, 구체적으로 재현된 모델 문제 해결에 필요한 경우뿐이다. 후자는 조사 전에 모델 문제, 필요한 구성요소, 조사 종료 조건을 기록하고 필요한 부분만 확인한다.
- 다음 자료를 열기 전에 **어떤 모델 질문이나 산출물을 해결하는지** 판단한다. 직접 관련성을 설명할 수 없으면 그 분기를 중단하고 모델의 남은 작업으로 돌아간다. 이미 쓴 시간·토큰이나 남은 파일 수는 계속할 근거가 아니다.
- 부속 도구의 클래스 수·파일 수·검사 PASS 수를 모델 진행률로 보고하거나 모델 완료의 필수 조건으로 삼지 않는다. 진행 보고는 모델 산출물과 실제 미해결 사항을 기준으로 한다.
- 이 사용자 정정은 과거 plan·RESUME·GOAL 기록의 부속 도구 전수 판독 지시보다 우선한다. 과거 판독 영수증과 원본은 보존하되 현재 할 일로 재사용하지 않는다. 범위 제외를 판독 완료·검증 통과·사람 승인으로 바꾸지 않으며, 모델 자체의 검토·승인 조건은 유지한다.

## 지식 보강과 전체 감사의 작업 단위

개별 지식 보강과 모델 전체 감사는 별도 작업 단위다. 개별 보강은 그 주장에 필요한 원문·식·조건·코드 대조를 수행하고 적용되는 독립 검토와 사람 결정을 거치면, 해당 모델의 전체 감사 완료를 기다리지 않고 반영할 수 있다. 이는 XBeach R3에서 이미 허용한 개별 정정과 전체 감사의 분리를 공통 원칙으로 명시한 것이며, 기존 전체 감사 상태는 독립적으로 유지한다. 개별 보강 반영을 미완인 전체 감사의 완료로 간주하지 않는다. 전체 감사를 기다릴 필요가 없다는 것이 개별 보강의 대조·검토·게이트를 면제한다는 뜻은 아니다.

- “전수”·“진행”은 분석 범위의 자동 확장 허가도, 자동 축소 허가도 아니다. 기존에 승인된 고정 집합과 종료 조건을 바꾸려면 사용자의 별도 명시 결정, 원래 snapshot 보존, 개정 기록이 필요하다. 구조 개편이나 일반적인 진행 지시를 그 결정으로 대체하지 않는다.
- 읽지 않은 driver·이론을 이름만 보고 비핵심으로 분류하지 않는다. 기존 note_worthy 판정의 근거 기록 의무는 그대로 유지한다.
- 기존 판독 기록·승인·게이트는 유지한다. 개별 보강은 이를 우회하는 경로가 아니다.
- 현재 작업은 [plan.md의 현재 작업](plan.md#현재-작업)을 따르고, 현재 사용자 지시가 우선한다. 과거 RESUME·GOAL 기록의 재개 목록은 자동 실행하지 않는다.

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

## 역할 분담 (Claude ↔ Codex)

2026-09-19 사용자 지시. 기본 역할이며 기계적으로 적용하지 않는다.

- **Claude = Lead / Planner / Reviewer** — objective·scope 관리, 요구사항 해석, 작업 분해, engineering/content decision, acceptance criteria·stop condition 설정, Codex 결과 검증, 최종 판단.
- **Codex = Executor / Investigator** — 저장소 조사, 코드·문서 수정, 반복 작업, 테스트·검증 실행, evidence 수집, bounded task 결과 반환.

Codex 위임 우선: 대량 파일 조사, 여러 파일에 걸친 수정, 반복적 refactor, 테스트·검증, 코드 구현, 로그·데이터 분석. Claude가 직접 하는 편이 더 싸고 단순한 소규모 작업은 위임하지 않아도 된다.

Codex 호출은 항상 다음 계약으로 한다.

```
OBJECTIVE:      달성할 결과
SCOPE:          대상 경로·파일, 허용 동작(읽기/쓰기), 금지 사항
STOP CONDITION: 종료 조건. 범위 밖 판단이 필요하면 확대하지 않고 Claude에게 반환
DELIVERABLE:    반환 형식(diff·표·로그 요약)과 근거(파일:줄·명령 출력)
```

Codex 결과는 그대로 채택하지 않는다. Claude가 evidence와 [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md)·이 문서·[CONVENTIONS.md](CONVENTIONS.md)에 대조해 검증한 뒤 판단한다.

**`models/` 잠금**: `models/`는 root 소유 읽기 전용이며 현재 운영 제약으로 유지한다. Claude·Codex 모두 우회하지 않는다. 절차: 기본 잠금 → 변경안(diff/script) 생성 → 사용자 승인 → 사용자 sudo 적용 → `validate-all` → 결과 검증 → 재잠금 ([PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md#models-잠금-절차)).

**Claude 모델 지정** (역할 규칙과 별개 설정): 현재 기본 모델은 **Fable 5.1 (`claude-fable-5-1`)**. 자동 fallback 금지 — 다른 모델로 대체하지 않고 실제 응답의 모델 정보를 확인한다. 모델명은 사용자 지시로 변경하며, 사용자가 특정 작업에 한해 승인한 예외는 그 작업에만 적용된다.

큰 산출물 작성·구조 변경 시:
1. `plan.md`에 현재 계획 포인터, 상세 계획·acceptance criteria는 해당 작업 문서에 작성 (Claude)
2. `/codex:adversarial-review`로 계획 비판 검토, Claude가 반영 여부 판단
3. 구현을 Codex에 bounded task로 위임 (`models/`는 diff/script까지)
4. Claude가 결과 검증 — diff·검사 출력·요구사항 대조
5. 사람 게이트(해당 시 sudo 적용·승인) 후 커밋

미세 노트 추가나 출처 인용 보강은 위 사이클 skip 가능. 검사는 변경한 주장·코드·링크에 맞춰 수행하며, 통과 뒤에는 새 변경·실패·미해결 우려가 있을 때만 확대하거나 반복한다. 적용되는 독립 검토·사람 게이트·필수 훅은 유지한다.

## 동기화

- writer = 이 PC (WSL2 ext4, `~/coastal-wiki`) — **coastal-wiki 유일 writer**. 이 PC가 계산도 겸할 수 있으나 그 결과는 위키가 아닌 `coastal-runs`로(아래).
  - Windows 측 접근: `\\wsl$\Ubuntu\home\firesinger\coastal-wiki` (Obsidian 등 Windows 앱)
- reader = 다른 PC (git clone 후 git pull) — 위키에 대해 **pull 전용**. 리더 머신은 `git config pull.ff only` 권장(로컬 커밋 시 조용한 merge 대신 즉시 에러 → divergence 방지).
- **계산결과 → experience 채널**: 개인 run 결과는 위키에 직접 넣지 않고([RUNS-CHANNEL.md](RUNS-CHANNEL.md)) 별도 `coastal-runs` repo에 축적 → 3조건 게이트 통과분만 이 PC(writer)가 `experience/`로 promote. run 생산자는 여러 머신 가능(머신별 `runs/<host>/` 서브트리, 절대규칙 #8).
- 작업 후 항상 `git commit && git push` (push 전 `git pull` 로 origin 동기화 — 리더가 올린 변경 합류)
- **clone/세팅 시 1회 `bash tools/install-hooks.sh --writer|--reader`** — pre-commit(검증 + ★리더 커밋 거부 가드, R1 I-4) + post-merge·post-checkout·post-commit(검색 인덱스 자동 재빌드)을 설치. **리더 머신은 반드시 `--reader`** — 실수 커밋을 pre-commit 이 거부(미커밋 편집은 못 막으므로 리더 세션 지침은 별도 유지). 이후 `git pull`/커밋마다 `coastal-wiki` MCP 검색 인덱스 자동 갱신. python3 만 있으면 됨.
