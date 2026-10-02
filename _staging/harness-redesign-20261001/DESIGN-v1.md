# 하네스 v1 설계 (2026-10-02, 사용자 확정)

근거: [Codex 검토](codex-review.md) · [Fable 재검토](fable-review.md) · [웹·논문](web-research.md) · [X 검색](hermes-x-result.md) · [weave-router 검토](weave-router-review.md).
사용자 확정(2026-10-02 "그대로 확정하고 진행해"): Fable 최소 v1 + 목표 고정 hook + 루프·예산 탐지. 첫 파일럿 = XBeach 식생 항력 기능 사슬. 기존 전수 감사 = 동결 보존(발견 3건만 개별 계약). 검증 = 결정적 검사 + 다른 계열 독립 검토자 1명(`models/` 반영 시 2명).

## 0. 무엇을 막는가

| 실패 | 사례 | v1 장치 |
|---|---|---|
| A. 자기 완료 선언·기준 변경 | 07-24 "완결" 오보, R2 실행 중 종결 규칙 재분류 | 승인은 sudo, receipt 는 결정적 재계산, 승인 후 계약 수정 = 새 revision·재승인 |
| B. 목적 이탈(계약 안에서도) | R1 3,228·R2 443 전수 처분 — 기능 질문과 무관 | 계약 필수 `function_question`·`budget`, 승인 화면이 이를 앞세움, 검토자 첫 질문 = 목적 반증, 예산 초과 시 실행 거부 |
| C. 지시만 있는 규칙 | 메모리 규칙 무시, 하네스 우회, `--model` 누락 | codex-run 이 모델·권한·입력 해시를 강제·기록, 직접 codex 호출 차단 hook, pre-commit 이 최종선 |
| D. 컨텍스트에서 목표 소실 | "다음 후보"가 목표를 대체 | 목표 고정 hook(SessionStart·UserPromptSubmit 재주입) |

알려진 한계(v1 수용): Bash·Python 으로 파일을 직접 쓰는 우회는 hook 문자열 검사로 완전 차단 불가 → **커밋 경계와 sudo 가 최종선**. 검토자 verdict 파일의 진위는 codex-run 로그 해시 사슬로 추적만 가능(위조 방지는 v2: root 소유 실행기).

## 1. 구성 (`tools/task/`)

```
tools/task/
  bin/new-task      계약 초안 생성(템플릿) — Claude 사용 가능
  bin/approve       승인 — sudo 전용. 계약을 보여주고 사용자가 기능명을 타이핑해야 승인
  bin/codex-run     Codex 실행 래퍼 — 유일한 Codex 진입점
  bin/receipt       완료 영수증 결정적 생성
  bin/status        활성 작업·예산 사용·남은 done_when 출력 (hook 이 사용)
  hooks/pretooluse.py   직접 codex 호출 차단, 승인된 계약 파일 편집 차단
  hooks/goal-pin.py     SessionStart·UserPromptSubmit 에 활성 작업 요약 주입
  lib/                  공통(해시·스키마·검사)
  schemas/{contract,approval,run,verdict,receipt}.schema.json
  tests/                정상 경로 + 부정 fixture
tasks/<task_id>/        작업 단위 (repo 안, git 추적)
  CONTRACT.json  runs.jsonl  verdicts/  outputs/  RECEIPT.json
/var/lib/coastal-task/approvals/<task_id>.<rev>.json   root 소유 0644, 디렉터리 0755 root — sudo approve 만 씀
ACTIVE                  repo 루트 아닌 tools/task/state/ACTIVE — 현재 활성 task_id 1개
```

## 2. 계약 `CONTRACT.json`

필수: `task_id`, `revision`(정수), `model`, `function`(기능명), `function_question`(이 작업이 답할 질문 1문장), `build_plan_levels`(BUILD-PLAN §4: 문서 지원·코드 구현·실행 확인·수치 검증·물리 검증 중 이번에 목표로 하는 것과 미수행으로 남길 것), `inputs[{path,sha256}]`, `allowed_outputs[glob]`, `constraints[]`, `done_when[{id, kind: check|review, spec}]`, `budget{codex_runs, max_records, wall_hours}`, `verifier{family, second_for_models:true}`, `out_of_scope[]`.

- `check` 항목 = 결정적 검사(스크립트·validator·파일 존재·해시). `review` 항목 = 독립 검토자 질문.
- **검토자 고정 첫 질문**(스키마가 강제): "이 산출물이 function_question 에 답하는가? done_when 이 그 질문에 비해 과하거나(전수·소진형) 모자라지 않은가?"

## 3. 승인 `sudo tools/task/bin/approve <task_id>`

- 계약의 `function`·`function_question`·`budget`·`out_of_scope` 를 먼저 보여주고, 사용자가 `function` 문자열을 그대로 입력해야 승인.
- `/var/lib/coastal-task/approvals/<task_id>.<rev>.json` 에 `{task_id, revision, contract_sha256, approved_at, approver: SUDO_USER}` 기록.
- 계약이 바뀌면(sha 불일치) 승인 무효 → revision 을 올리고 재승인. 이전 revision·승인은 보존.

## 4. `codex-run`

- 인자: `--task <id> --role worker|verifier --model <slug> [--write]` + 프롬프트 파일.
- 거부 조건: 활성 승인 없음, 계약 sha ≠ 승인 sha, `budget.codex_runs` 초과, `--model` 없음, verifier 인데 `verifier.family` 와 다른 계열, worker 의 `--write` 범위가 `allowed_outputs` 밖.
- 기본 read-only(`codex exec -s read-only`, stdin `/dev/null`). `--write` 는 `tasks/<id>/outputs/` 한정.
- `runs.jsonl` 에 `{run_id, role, model, argv, sandbox, prompt_sha256, input_sha256s, started, ended, exit, output_paths+sha256, codex_session_id}` 를 append. 직전 줄 해시를 포함(해시 사슬).
- verifier 출력은 `verdicts/<run_id>.json`(스키마: `{questions:[{id, verdict: PASS|FAIL|UNCERTAIN, evidence}]}`).

## 5. `receipt <task_id>`

결정적으로 계산해 `RECEIPT.json` 작성: 계약 sha·승인 파일 sha, `check` 항목 각각 실행 결과, `validate-all.sh` 결과, 각 `review` 항목의 최신 verifier verdict(runs.jsonl 사슬에서 찾은 run_id·해시), outputs 해시 목록, `build_plan_levels` 별 상태(목표/미수행). `status = complete` 는 모든 check PASS + 모든 review PASS(+ `models/` 반영 산출물이면 다른 verifier 2명) 일 때만, 아니면 `incomplete` + 사유.

## 6. 강제 지점

| 지점 | 검사 |
|---|---|
| PreToolUse(Bash) | `codex exec`·`codex-companion`·`codex ` 직접 호출 거부 → `tools/task/bin/codex-run` 사용 안내(`continueOnBlock`). |
| PreToolUse(Write/Edit) | 승인된 revision 의 `CONTRACT.json` 편집 거부(새 revision 은 `new-task --revise`). `RECEIPT.json`·`runs.jsonl`·`verdicts/` 직접 편집 거부. |
| goal-pin | SessionStart·UserPromptSubmit 에 `status` 출력(활성 task·function_question·done_when 미충족·예산 사용) 주입. 활성 task 없으면 "활성 작업 없음 — 모델 분석 대량 작업 금지" 한 줄. |
| pre-commit | `tasks/**` 변경 시: 계약 스키마, 승인 존재·sha 일치, runs.jsonl 사슬 무결성, RECEIPT.json 이 staged 면 재계산 결과와 일치. `status: complete` 표기는 유효 receipt 없으면 거부. |
| sudo | 승인. `models/` 반영(기존 SCOPED EDIT). |

## 7. 시험 (구현 완료 조건)

정상: 견본 계약 → sudo 없이 approve 시도 거부 → 테스트용 approvals 경로로 승인 → codex-run(가짜 codex stub) → receipt complete → commit 통과.
부정 fixture(각각 거부돼야 함): ① 위조 RECEIPT.json(complete) ② 예산 초과 codex-run ③ 승인 후 계약 수정 ④ `--model` 누락 ⑤ 같은 계열 verifier ⑥ allowed_outputs 밖 쓰기 ⑦ 직접 `codex exec` 호출(hook) ⑧ runs.jsonl 중간 줄 변조 ⑨ review 항목 FAIL 인데 complete 표기.
라이브 1회: 첫 파일럿 계약(XBeach 식생 항력)으로 실제 codex-run 1회 + receipt incomplete 확인.

## 8. 이행 (Codex 권고 순서)

1. 보존: 현 설치본·설정·승인 기록 스냅샷(`_staging/harness-redesign-20261001/preserve/`).
2. 동결: 기존 R1/R2·13모델 공정표 = 상태 보존, 자동 재개·승격 금지(문서 명시).
3. v1 구현·시험(위 §7).
4. 전환: 옛 resume-gate 설치분(`/etc/claude-code/managed-mcp.json`, `managed-settings.d/*.bak`, `/etc/claude-code/.claude/agents/`, `/opt/coastal-resume`) 한 묶음 제거 — sudo 스크립트. `tools/resume-gate/` 는 `_archive/` 로 이동(결정적 검사 코드는 v1 lib 로 흡수한 뒤).
5. 문서: CLAUDE.md·PROJECT_REQUIREMENTS 에 검증 정책·작업 진입 절차 반영, 메모리 규칙은 포인터로 축소, plan.md 현재 작업 = 활성 task 포인터.
6. 첫 파일럿 실행 → 실패를 회귀 fixture 로 축적 → 다음 작업 종류로 확대.
