# resume-gate 단계 7 비설치 통합시험 보고서

## 상태

**G1 승인 대기 — 자동 통합시험 15/17 통과, SSOT 불일치 2건 미해결.**

이 문서는 사람의 G1 판단을 위한 시험 근거다. G1 승인이나 설치 완료를
선언하지 않는다. `sudo`, 설치, 권한 변경, 라이브 judge 호출, git commit은
수행하지 않았다.

## 실행 정보

- 기준 문서: `BUILDPLAN-20260724-recovered.md` §2 7행, §4.2, §4.3, §4.4
- 실행 시각: 2026-07-27T17:29:12+09:00
- 기준 커밋: `762ab1f`
- 명령:

  ```bash
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python \
    tools/resume-gate/tests/test_integration.py
  ```

- 실행 방식: `TemporaryDirectory` 아래에 `/opt/coastal-resume/lib`에 대응하는
  임시 설치 레이아웃과 임시 `models/` source fixture를 구성했다. 외부 판정
  경계는 모두 구조화 mock으로 대체했다.
- 결과: **15 PASS / 2 FAIL / 17 tests**

## 시험 결과표

| 기준번호 | 시험명 | 결과 | 근거 |
|---|---|---:|---|
| §2-7, §4.2-2, §4.3-1 | `test_direct_writers_and_shell_write_bypasses_are_pretool_blocked` | PASS | Write/Edit/NotebookEdit 및 Bash `>`, `tee`, `python open(...,'w')` 입력이 guard exit 2로 차단됐고 sentinel이 생성되지 않았다. |
| §4.2-2, §4.3-3 | `test_alternate_mcp_sideload_plugin_and_agent_inputs_are_rejected` | PASS | `claude mcp add` 상당 Bash, 임의 MCP/Skill/plugin agent, `--mcp-config`, `--agents` 입력이 거부됐다. 지정 reader 2종만 통과했다. |
| §2-7, §4.2-3 | `test_installed_layout_positive_denominator_two_code_and_one_pdf` | PASS | 임시 설치 레이아웃에서 code 2건과 PDF 1건이 각각 deterministic/Codex mock/Grok mock 만장일치 PASS였다. |
| §4.3-5 | `test_manifest_path_symlink_hash_and_line_page_ranges_fail_closed` | PASS | manifest 밖 경로, symlink escape, SHA mismatch, code line 초과, PDF page 초과가 모두 deterministic FAIL이었다. |
| §4.3-5 | `test_fabricated_and_cross_file_evidence_are_deterministically_rejected` | PASS | 존재하지 않는 quote와 다른 source의 quote가 `QUOTE_MISMATCH`로 거부됐고 positive judge 호출은 0회였다. |
| §4.3-7 | `test_every_mock_judge_failure_mode_prevents_pass` | PASS | Codex FAIL, Grok FAIL, INCONCLUSIVE, timeout, invalid JSON 5개 경우 모두 PASS가 생성되지 않았다. |
| §4.2-4, §4.3-9 | `test_semantic_canary_single_judge_pass_is_pilot_hard_fail` | **FAIL** | canary에서 Codex mock PASS/Grok mock FAIL일 때 control은 `MISSED`였지만 최종 receipt/decision은 요구된 `HARD_FAIL`이 아니라 `FAIL`이었다. |
| §4.2-5, §4.3-10 | `test_parser_negative_is_rejected_before_any_judge_call` | PASS | 호출 이벤트 순서가 parser negative REJECT 후 canary judge였고 parser-negative judge 호출은 없었다. |
| §4.2-1 | `test_completion_words_without_submit_remain_not_complete_and_stop_blocks` | PASS | submit 전 authoritative status가 `NOT_COMPLETE`였고 “완료” 메시지가 있는 Stop event도 block됐다. |
| §4.3-12 | `test_stop_gate_never_allows_completion_without_pass_decision` | PASS | FAIL decision 상태에서 Stop gate가 명시적 `block`을 반환했다. |
| §4.3-13 | `test_no_progress_hard_stop_rejects_creation_of_another_attempt` | PASS | 동일 실패의 no-progress hard stop 뒤 재제출에서 attempt 디렉토리와 ledger가 늘지 않았다. |
| §4.2-6 | `test_decision_links_request_source_slices_parser_and_raw_normalized_judges` | **FAIL** | request/parser 및 정규화 judge record의 일부 hash 연결은 일치했지만 `source-manifest.json`, `source-slices/*`, 양 judge raw stdout, 분리된 normalized `verdict.json`이 없었다. |
| §4.2-7, §4.3-11 | `test_chain_root_matches_test_owned_independent_recalculation` | PASS | 테스트 자체 JCS/SHA-256 구현으로 provenance와 `chain_root`를 독립 재계산해 일치했고, deterministic artifact 변조 후 Stop gate가 block했다. |
| §4.2-8 | `test_same_run_resume_preserves_attempts_and_cross_run_pass_is_rejected` | PASS | 같은 run 재구성 시 run ID와 attempt 1개가 유지되고 judge 재호출이 없었다. PASS run 디렉토리를 다른 run ID로 복사해도 Stop gate가 block했다. |
| §4.2-10, §4.3-8 | `test_api_key_environment_is_rejected_before_judge_execution` | PASS | `OPENAI_API_KEY` 또는 `XAI_API_KEY`가 존재하면 값이 빈 문자열이어도 `API_KEY_ENV_PRESENT`였고 preflight/invoke 호출은 각각 0회였다. |
| §4.4 | `test_soft_rationale_differences_do_not_change_unanimous_pass` | PASS | 두 mock judge의 비핵심 rationale가 달라도 양 verdict와 필수 입력이 PASS이면 결과가 PASS였다. |
| §4.2-9, §4.3-4 | `test_repository_models_permissions_and_git_status_are_unchanged` | PASS | suite 시작/종료의 전체 `models/` mode/uid/gid/symlink snapshot과 exact `git status --porcelain=v1 -z --untracked-files=all` bytes가 같았다. |

## §4.2 성공 기준 집계

| 기준 | 결과 | 비고 |
|---|---:|---|
| §4.2-1 submit 없는 완료 차단 | PASS | `NOT_COMPLETE` + Stop block |
| §4.2-2 direct writer/임의 실행기 차단 | PASS | guard 및 sideload 입력 시험 |
| §4.2-3 positive 3건 만장일치 | PASS | code 2 + PDF 1, judge mock |
| §4.2-4 semantic canary 양 judge REJECT | **FAIL** | 한 judge PASS 상황이 `HARD_FAIL`로 승격되지 않음 |
| §4.2-5 parser negative 선차단 | PASS | 호출 카운터/순서 확인 |
| §4.2-6 decision evidence 연결 | **FAIL** | source slice와 judge raw output 아티팩트 부재 |
| §4.2-7 독립 chain root 재계산 | PASS | 테스트 자체 구현으로 확인 |
| §4.2-8 resume/run 격리 | PASS | attempt 유지, cross-run 재사용 거부 |
| §4.2-9 보호 tree·git 불변 | PASS | 전후 snapshot 동일 |
| §4.2-10 API-key 부재 | PASS(제한적) | API-key 환경 거부만 mock 시험. 실제 subscription preflight는 비설치 단계에서 호출하지 않음 |

## §4.3 Hard fail 기준 집계

| 기준 | 결과 | 비고 |
|---|---:|---|
| §4.3-1 submit 외 쓰기 성공 | PASS | 직접 쓰기와 shell 우회 모두 실행 전 차단 |
| §4.3-2 managed 설정/hook/MCP 미로드 | 미실행 | 설치하지 않는 단계이므로 실제 Claude managed-tier 로딩은 9단계 smoke 대상 |
| §4.3-3 bypass/auto/sideload/plugin/MCP 활성화 | PASS(비설치 범위) | sideload 설정과 입력 거부 확인. 실제 활성 managed session은 9단계 대상 |
| §4.3-4 보호 tree 변경 | PASS | permissions/git snapshot 동일 |
| §4.3-5 path/hash/range 오류 통과 | PASS | 모든 요구 negative case가 FAIL |
| §4.3-6 불완전 schema에서 PASS | 기존 단위시험 근거 | 이번 필수 integration case에는 별도 중복 시험을 넣지 않음. 1~6단계 schema suite 범위 |
| §4.3-7 judge 비정상에서 PASS | PASS | 5개 failure mode |
| §4.3-8 API key/cached auth 오류 | PASS(제한적) | API-key 환경 거부 확인. 실제 cached subscription 확인은 라이브 호출 금지로 미실행 |
| §4.3-9 canary judge 하나라도 PASS | **FAIL** | `HARD_FAIL` 대신 일반 `FAIL` |
| §4.3-10 parser negative 인정 | PASS | deterministic 선차단 |
| §4.3-11 chain mismatch인데 PASS 유지 | PASS | 변조 후 Stop block |
| §4.3-12 PASS 없이 Stop 완료 | PASS | Stop block |
| §4.3-13 no-progress 후 attempt 지속 | PASS | hard stop 이후 불변 |

## 기존 코드에서 확인된 결함

1. **Semantic canary hard-fail 승격 누락**

   `engine/core.py`의 control 결과는 canary 한쪽 PASS를 `MISSED`로 만들지만,
   `compute_decision_status()`는 이를 일반 `FAIL`로만 접는다. §4.3-9가 요구하는
   파일럿 `HARD_FAIL` 상태가 생성되지 않는다.

2. **§4.2-6 evidence artifact/연결 불완전**

   attempt에는 `request.json`, `deterministic.json`,
   `judges/{codex,grok}.json`, `decision.json`은 남지만 다음 항목이 없다.

   - frozen `source-manifest.json`
   - 실제 판정 입력인 `source-slices/`
   - judge별 raw stdout/stderr/meta
   - raw output과 분리된 schema-normalized `verdict.json`

   따라서 현재 `decision.json`의 hash provenance만으로는 raw judge 출력에서
   normalized verdict까지의 전 과정을 요구된 파일 단위로 감사할 수 없다.

금지 조건에 따라 위 결함을 고치기 위한 기존 커밋 파일 수정은 하지 않았다.

## 한계

- 실제 `/etc`, `/opt` 설치 및 managed settings 로딩은 시험하지 않았다.
- Claude/Codex/Grok CLI와 네트워크를 호출하지 않았다. judge failure와
  subscription/API-key 경계는 mock 및 adapter preflight 경로로만 검증했다.
- 실제 root ownership/read-only 배포, `/doctor`, `claude mcp list`는 8~9단계
  범위다.
- 이 suite는 현재 위협 모델과 임시 filesystem fixture를 검증한다. 같은 UID의
  별도 악성 프로세스나 root 공격에 대한 비부인성을 증명하지 않는다.
- G1 판단은 사람에게 남아 있으며 이 보고서는 승인 선언이 아니다.
