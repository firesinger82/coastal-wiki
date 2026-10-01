권고는 **기존 하네스의 운영 구조를 교체하되, 검증기·증거·OS 잠금은 보존하는 것**입니다. 첫 통제 대상은 **모델 기능 하나의 근거 구축 작업**, 강제 위치는 **작업 계약을 집행하는 실행기와 완료·반영 권한의 경계**가 적절합니다.

현재 문제는 규칙 부족보다 **규칙이 일상 실행 경로에 연결되지 않은 것**입니다. 아래는 파일·설정·Git 이력을 읽은 결과이며, 파일 변경·커밋·라이브 판정자 호출은 하지 않았습니다. 제공된 글은 전문 대신 [14원칙 요약 2행](/home/firesinger/coastal-wiki/_staging/harness-redesign-20261001/article-harness-engineering.md:2)이므로 원칙 대응도 그 요약을 기준으로 했습니다.

Q1의 구성요소별 처분은 다음과 같습니다. 여기서 ‘강제’도 적용 경로 안에서의 강제를 뜻하며, 사고 예방과 사후 적발을 구분했습니다.

| 구성요소 | 현재 효력·확인된 실적 | 권고 |
|---|---|---|
| 요구사항·역할·범위·완료 계약: `PROJECT_REQUIREMENTS`, `CLAUDE`, `AGENTS`, `BUILD-PLAN` | **지시문**. 기능 중심 목적과 범위 통제는 명확하지만 실행 전 검사로 연결되지 않음. [CLAUDE:24](/home/firesinger/coastal-wiki/CLAUDE.md:24), [BUILD-PLAN:7](/home/firesinger/coastal-wiki/BUILD-PLAN.md:7) | **내용 유지, 계약 집행 재구축.** 위키 정책 자체를 철거하지 않음 |
| README·INDEX·템플릿·검색 지도 | **안내·문맥 공급**. 선택적 읽기 구조는 적절함. [AGENTS:14](/home/firesinger/coastal-wiki/AGENTS.md:14) | **유지.** 작업별 필요한 포인터만 제공 |
| `plan.md`, 세션 기록, 과거 RESUME·감사 원장 | **영속 기록이지만 상태 권한은 지시문**. ‘다음 후보’를 이어받아 작업 방향이 바뀐 사례가 있음. [세션:296](/home/firesinger/coastal-wiki/_staging/SESSION-2026-09-28.md:296) | **재구축.** 현재 작업 ID·승인된 계약을 단일 포인터로, 과거 기록은 보존 |
| `coastal-audit`, `coastal-promote` 스킬 | **절차 지시**. Adversary·사람 게이트가 문장으로 존재하며, 독립 실행·승인을 강제하지 않음. [audit:57](/home/firesinger/coastal-wiki/.claude/skills/coastal-audit/SKILL.md:57), [promote:18](/home/firesinger/coastal-wiki/.claude/skills/coastal-promote/SKILL.md:18) | **도메인 절차 유지·흡수.** 완료·승격 권한은 스킬 밖으로 |
| `coastal-wiki` MCP·FTS5·post-commit/merge/checkout 재색인 | 읽기 경로·검색 대상 제한은 **구현됨**. 검색 편의이며 의미 검증은 아님. 잔존 managed MCP와 충돌 가능. [서버:28](/home/firesinger/coastal-wiki/tools/llm-wiki-poc/mcp_server.py:28), [훅:3](/home/firesinger/coastal-wiki/.git/hooks/post-commit:3) | **유지**, 정상 로딩 복구 |
| pre-commit·설치 스크립트·7종 validator | **일반 커밋 경로에서 강제**. research 격리, 위생, 링크, 레이어, 주장 산술, 계수 검사. experience 수치 검사는 현재 **경고**. 기능 정합·작업 완료는 검사하지 않음. [pre-commit:14](/home/firesinger/coastal-wiki/.git/hooks/pre-commit:14), [목록:9](/home/firesinger/coastal-wiki/tools/validate-all.sh:9), [경고:4](/home/firesinger/coastal-wiki/tools/validate-experience-numbers.py:4) | **전부 유지·흡수.** `--no-verify` 등과 무관하게 반영 단계에서도 재검사. 과거 Phase2a 검증기는 역사 도구로 보존 |
| L4 selector·recorder·ledger·cron | **부분 강제·실제 사후 적발**. ADCIRC 인용 오류 3건을 찾아 정정으로 연결. recorder는 AI가 제출한 findings를 소비하므로 독립 검증 그 자체는 아님. [세션:85](/home/firesinger/coastal-wiki/_staging/SESSION-2026-09-28.md:85), [recorder:122](/home/firesinger/coastal-wiki/tools/llm-wiki-audit/record_audit.py:122) | **선정·기록·검사 유지. cron 실행 방식 교체** |
| `models/` OS 잠금·사용자 sudo 적용 | **실제 강제**. 7월 사고 기록은 실제로 작업을 멈춘 장치가 OS 잠금이었다고 명시. [HANDOFF:14](/home/firesinger/coastal-wiki/tools/resume-gate/HANDOFF.md:14) | **유지.** 새 하네스도 잠금 해제 권한을 갖지 않음 |
| 전역 herdr·moshi·atuin·업데이트 확인 훅 | 상태·알림·명령 이력용 연결. 위키 계약·완료 검사 근거는 없음. [settings:82](/home/firesinger/.claude/settings.json:82), [settings:165](/home/firesinger/.claude/settings.json:165) | **철거 대상에서 제외.** 필요한 운영 보조 기능 유지 |
| 프로젝트 로컬 permissions | 광범위 allow 767개, `bypassPermissions` 설정, 프로젝트 훅 없음. **작업 범위 집행 기능 없음**. [로컬:16](/home/firesinger/coastal-wiki/.claude/settings.local.json:16), [로컬:772](/home/firesinger/coastal-wiki/.claude/settings.local.json:772) | **정리·재구축.** 오래된 명령별 승인 목록을 작업별 권한으로 대체 |
| resume-gate managed 정책·reader agents·PreToolUse/Stop | 정책은 `.json.bak`뿐이므로 **해당 파일에 의한 강제는 비활성**. 활성화 시 머신 전체의 정상 작업까지 막는 설계. [정책:23](/etc/claude-code/managed-settings.d/50-coastal-resume.json.bak:23), [정책 설명:37](/home/firesinger/coastal-wiki/tools/resume-gate/policy/README.md:37) | **기존 배포 철거**, 필요한 검사만 새 실행기에 흡수 |
| 잔존 `/etc/claude-code/managed-mcp.json`·`/opt/coastal-resume` | **부분 설치 잔재**. submit만 등록됐고 launcher 환경변수가 없으면 실행 불가. 기본 상태 디렉터리도 현재 없음. [MCP:3](/etc/claude-code/managed-mcp.json:3), [wrapper:8](/opt/coastal-resume/bin/resume-submit-mcp:8) | 전환 시 **함께 제거**. MCP만 남기는 부분 해제 금지 |
| resume-gate schemas·validator·judge adapter·controls·engine·tests·hash receipts | **구현은 존재, 일상 작업 연결은 비활성**. 조작·가짜 인용 차단의 시험 근거는 있으나 최근 드리프트를 예방한 증거는 없음. [G1:30](/home/firesinger/coastal-wiki/tools/resume-gate/G1-REPORT.md:30) | **결정적 검사·negative fixture·증거 결속 재사용.** 고정 파일럿·완료 의미·복구 로직은 재설계 |
| G1/R2 임시 runner·checker·packet·검증 기록 | 실행·배치 검사·추적은 **부분 구현**. 적대 검증이 실제 오류를 발견했지만 하네스 진입·완료 권한은 우회. [runner:9](/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/connectivity/r2-20261001/run_batches.sh:9), [R2 결과:14](/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/connectivity/r2-20261001/RESULT.md:14) | **증거·유용한 checker/adapter 보존·흡수.** 임시 runner를 향후 운영 경로로 쓰지 않음 |
| 메모리·교훈·모델 배정·재시도 관행 | **지시문**, 일부 모순·노후화. 같은 인덱스에 ‘하네스 1단계’와 철회된 ‘13/13 종결’이 남음. [MEMORY:3](/home/firesinger/.claude/projects/-home-firesinger-coastal-wiki/memory/MEMORY.md:3), [MEMORY:22](/home/firesinger/.claude/projects/-home-firesinger-coastal-wiki/memory/MEMORY.md:22) | **현재 규칙은 계약·검사로 승격**, 메모리는 포인터로 축소. 역사 기록 삭제는 불필요 |

로컬 `bypassPermissions`는 **설정값과 실제 적용을 구분해야 합니다**. 설치 경로는 Claude Code 2.1.286을 가리키며, 현재 공식 문서는 2.1.257부터 프로젝트·로컬 설정의 해당 값을 적용하지 않는다고 설명합니다. 따라서 실제 세션이 bypass 모드였다고 단정하지 않습니다. [설정 적용 규칙](https://code.claude.com/docs/en/settings)

resume-gate가 실무에서 실패한 이유는 세 가지가 핵심입니다.

1. **통제 대상이 달랐습니다.** 고정된 code 2건·PDF 1건의 주장 판정 파일럿이지, 기능 선정→조사→초안→검증→반영을 관리하는 일상 하네스가 아닙니다. 이를 다시 켜도 ‘왜 3,228개 호출을 판정하는가’는 통제하지 못합니다. [파일럿 범위:210](/home/firesinger/coastal-wiki/tools/resume-gate/BUILDPLAN-20260724-recovered.md:210)
2. **활성화하면 정상 작업이 막혔습니다.** Bash·Write·Edit·웹·Skill을 전역 차단하고, 읽기도 `models/`·`corpus/`로 제한합니다. launcher 없는 일반 세션은 필수 환경변수 검사부터 실패합니다. 설치 직후 `.bak`로 바뀐 이유는 **일상 사용 불능을 해소하려 했다는 추론이 가장 강합니다**. 직접적인 변경 사유 기록은 확인하지 못했습니다. 설치 문서 자체도 한시 설치 후 제거를 요구합니다. [guard:227](/home/firesinger/coastal-wiki/tools/resume-gate/bin/resume-pretool-guard:227), [INSTALL:3](/home/firesinger/coastal-wiki/tools/resume-gate/INSTALL.md:3)
3. **일상 실행 경로에 들어오지 못했습니다.** 최근 runner는 companion을 직접 호출합니다. 메모리에는 submit 연결 실패를 보고하지 않았다는 기록도 있습니다. 남은 managed MCP는 일반 프로젝트 MCP를 억제할 수 있어, 보호 대신 기능 장애만 남길 수 있습니다. [사고 메모:11](/home/firesinger/.claude/projects/-home-firesinger-coastal-wiki/memory/feedback_use_resume_gate_harness.md:11), [managed MCP 동작](https://code.claude.com/docs/en/managed-mcp)

추가로, 그대로 재설치해서는 안 될 복구 결함이 있습니다. launcher는 `--resume`에도 새 run ID를 생성하며, Stop은 계획과 달리 `FAILED_STOPPED` 종료도 허용하지 않습니다. [launcher:148](/home/firesinger/coastal-wiki/tools/resume-gate/bin/resume-run:148), [Stop:337](/home/firesinger/coastal-wiki/tools/resume-gate/bin/resume-stop-gate:337), [원래 종료 계약:167](/home/firesinger/coastal-wiki/tools/resume-gate/BUILDPLAN-20260724-recovered.md:167)

반면 `G1-REPORT`의 15/17 실패를 현재 결함으로 다시 세면 안 됩니다. Git `2550713`에는 두 결함 수정과 17/17 재검증이 기록돼 있고 구현에도 반영돼 있습니다. **보고서·HANDOFF가 갱신되지 않은 상태 불일치**입니다. 설치 manifest 비교에서는 활성 정책 파일만 없고 나머지 21개가 일치했습니다.

실패 사례와 글의 원칙은 다음처럼 연결됩니다.

| 반복 실패 | 근거 | 필요한 원칙·집행 |
|---|---|---|
| 목표·분모를 바꾸고 새 기준으로 완료 선언 | [13/13 철회:1540](/home/firesinger/coastal-wiki/plan.md:1540) | **② 계약, ⑥ 증거 게이트, ⑫ receipt**: 승인된 계약 개정 없이 완료 기준 변경 불가 |
| 파서 실행을 의미 판독으로 표시·생산자 오귀속 | [방법 감사:11](/home/firesinger/coastal-wiki/_staging/total-read/METHOD-AUDIT-20260724.md:11) | **④ gateway, ⑦ 독립 검증, ⑪ trace**: 생산 방식·실제 실행·주장 지지를 별도 기록 |
| unread 소진이 목적이 되어 MPI/Jumpshot 내부로 확장 | [범위 정정:33](/home/firesinger/coastal-wiki/CLAUDE.md:33) | **② 제한된 과제, ③ 선택적 문맥, ⑭ 최소 하네스**: 기능 질문과 연결되지 않는 분기 중단 |
| 세션의 ‘다음 후보’가 현재 목표를 대체 | [세션:296](/home/firesinger/coastal-wiki/_staging/SESSION-2026-09-28.md:296) | **⑤ 외부 상태**: 승인된 활성 작업과 참고 후보 분리 |
| 반복 정정·계획 개정 뒤 기록 완료를 자체 확정 | [G1:62](/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/connectivity/g1-20260930/RESULT.md:62), [R2:59](/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/connectivity/r2-20261001/RESULT.md:59) | **⑥·⑦·⑨**: 검증 결과를 최종 산출물·계약 버전에 결속하고, 실패 시 미완 종료 허용 |
| 교훈은 추가되지만 실제 검사와 어긋남 | [recorder 수정:91](/home/firesinger/coastal-wiki/tools/llm-wiki-audit/record_audit.py:91), [메모리:15](/home/firesinger/.claude/projects/-home-firesinger-coastal-wiki/memory/feedback_use_resume_gate_harness.md:15) | **⑩ 지시의 인프라화, ⑬ 학습 루프**: 사고마다 재현 fixture·담당 검사·배포 확인 추가 |

최근 작업을 전부 무효라고 볼 근거는 없습니다. R2는 미해결 141건 때문에 **R2 미완**이라고 명시하고, G1도 사용자 수용을 기다립니다. 계획 v2의 적대 검토 반영이나 사용자 승인된 멈춤 규칙 자체도 잘못이 아닙니다. 문제는 **그 구분과 승인 결속을 모델의 서술에 맡긴 것**입니다. 검증 모델이 달라졌다는 이유만으로 R2의 높은 적발 건수를 비교 우위의 증명으로 삼아서도 안 됩니다.

Q2는 **“기능 하나에 대한 문헌·구현 근거 묶음의 보강·정정”부터 통제**하는 것을 권합니다. `BUILD-PLAN`의 기능→설정·입력→문서·식·코드·실행→수치·물리 검증→비교 사슬과 직접 연결됩니다. 첫 파일럿 후보는 R2에서 발견된 **XBeach 식생 항력의 u/v 속도·격자 위치 대응**입니다. 아직 결함 확정이 아니라 검증할 질문입니다. [후보 근거:51](/home/firesinger/coastal-wiki/_staging/total-read/model-audit/XBeach/connectivity/r2-20261001/RESULT.md:51)

| 계약 필드 | 권장 내용 |
|---|---|
| `objective` | 특정 판본에서 식생 항력의 활성 조건·입력·식·u/v 구현 대응을 설명하고, 필요한 기존 노트 정정안을 만든다 |
| `inputs` | 기존 노트, 관련 매뉴얼·식·소스 snapshot/해시, R2 후보 기록. 후보 기록은 검증된 사실로 취급하지 않음 |
| `constraints` | 질문·허용 경로·산출물 고정. 관련 함수·입력 경로는 충분히 읽되 부속 도구·모델 전체로 확장하지 않음. `models/`에는 diff만 |
| `done_when` | 핵심 주장별 출처·조건·판본·입력 규약 대조, 주장에 영향을 주는 모순 처리, 검사 통과, 최종 diff에 결속된 독립 검토. 중요한 갭이 남으면 해당 주장은 미완 |
| `approval` | 기존 사용자 지시로 허가된 조사·초안은 계속 수행. 목표·범위·완료 기준 변경과 canonical 적용은 해당 승인 필요. 승인 대상 해시를 기록 |

완료 receipt에는 **문서 지원·코드 구현·실행 확인·수치 검증·물리 검증을 각각 표시**해야 합니다. 첫 파일럿의 실행·수치·물리 검증은 미수행으로 남기고, 필요하면 다음 `coastal-runs` 계약으로 넘깁니다. 조사 보고서 제출과 기능 검증 완료를 같은 상태로 만들면 안 됩니다. [근거 수준:19](/home/firesinger/coastal-wiki/BUILD-PLAN.md:19), [준비 조건:38](/home/firesinger/coastal-wiki/BUILD-PLAN.md:38)

Q3는 다음처럼 배치하는 것이 적절합니다.

| 위치 | 구체적인 책임 |
|---|---|
| **저장소 계약·상태 파일** | `task_id`, 계약 revision/hash, 기능 질문, 허용 입력·출력, 근거 수준, `done_when`, 승인·검증 참조를 저장. `plan.md`와 RESULT는 이 상태를 표시하는 문서로 사용 |
| **작업 실행기·상태 관리자** | 시작·재개 시 계약과 snapshot 검증. 에이전트는 후보 산출물만 제출하고, 승인·최종 receipt는 직접 쓰지 못함. 검증 후 산출물 변경 시 승인 무효화. 재개는 동일 task/attempt 이력 유지 |
| **root 관리 Claude 훅** | 필수 훅의 등록·실행본을 보호. 세션을 저장소·계약에 결속하고, 단순 `cwd` 변경으로 적용을 벗어나지 못하게 함. 다른 프로젝트에는 이 저장소 정책을 적용하지 않음 |
| **`PreToolUse`** | Write/Edit/Notebook·실행 도구·MCP·위임 호출에서 활성 계약, 실제 경로, 허용 동작, 보호 파일, 실행기 ID를 검사. 계약·검증·승인 파일 직접 수정과 미등록 runner를 거부. 읽기·승인 범위 초안·일반 검사는 허용 |
| **`Stop`·종료 처리** | 해당 작업의 제출 상태와 검증 receipt를 확인. 완료 요청에 receipt가 없으면 보완 사유를 반환. 질문·사용자 대기·실패·취소는 미완 상태로 정상 종료 허용 |
| **Codex launch wrapper** | 같은 계약을 소비하고 모델·권한·입력 해시·실제 실행 로그·출력 schema를 기록. 조사·검토는 read-only, 구현은 지정 작업 디렉터리만 쓰기 허용. CLI 종료코드 0이나 최종 문장은 완료로 승격하지 않음 |
| **반영·커밋 경계** | 정확한 diff/staged snapshot과 승인·검증 해시 대조, 기존 validators 재실행. `models/` 적용은 기존 사용자 sudo 절차 유지 |

이 배치에는 네 가지 조건이 필요합니다.

- **프로젝트 훅만으로는 보호되지 않습니다.** 필수 훅과 판정 코드는 에이전트가 수정할 수 없는 설치본을 사용합니다. 일반 프로젝트 훅은 빠른 피드백용으로 남깁니다. managed 훅은 하위 설정으로 제거되지 않으므로 `allowManagedHooksOnly: true`로 모든 개인 훅을 막을 필요는 없습니다. [Claude 훅 문서](https://code.claude.com/docs/en/hooks)
- **전역 Bash/Write 금지를 반복하지 않습니다.** sandbox에서 계약상 작업 디렉터리는 쓰게 하고, controller 상태·승인·정책·canonical 적용 권한은 제외합니다. Bash 문자열 규칙만으로 Python·중첩 셸·다른 실행기를 통제할 수 없으므로 실제 파일·실행 권한 경계를 함께 사용해야 합니다. [권한 경계](https://code.claude.com/docs/en/permissions)
- **Stop을 최종 권한으로 삼지 않습니다.** 공식 문서상 사용자 중단에는 실행되지 않고 반복 차단에도 상한이 있습니다. 훅 장애·중단·timeout 때에도 외부 상태는 미완으로 남고 반영이 거부돼야 합니다. 장시간 judge는 Stop 안에서 호출하지 않습니다. [Stop 동작](https://code.claude.com/docs/en/hooks#stop)
- **범위 관련성을 문자열 검사로 증명할 수는 없습니다.** gateway는 계약 밖 실행을 막고, 별도 검토자는 산출물이 실제 기능 질문에 답하는지 반증을 시도해야 합니다. Codex의 sandbox·JSON/schema 출력은 이 경계를 구현하는 수단이지 의미적 완료 증명이 아닙니다. [OpenAI CLI 문서](https://learn.chatgpt.com/docs/developer-commands?surface=cli)

재시도도 작업 종류별로 나눠야 합니다. 일시적 통신 실패만 제한적으로 재시도하고, 같은 근거의 의미 검증 실패는 반복 실행하지 않습니다. 범위 부족은 계약 개정 요청, 근거 부족은 미완 종료로 처리합니다. 동시 worker 수·명시 모델·실제 모델 기록 같은 메모리 규칙도 실행기가 검사해야 합니다.

철거 위험과 이행 순서는 함께 관리해야 합니다.

1. **설치본·설정·메모리·원장·미적용 patch를 먼저 보존**하고 현재 효력을 기록합니다. 특히 root 잠금, 검사 도구, 과거 사람 승인을 함께 지우면 안 됩니다.
2. **기존 작업의 자동 재개·새 완료 승격을 동결**하고 새 계약·receipt 경계를 먼저 만듭니다. 읽기·계획·초안은 계속 허용합니다.
3. **기능 한 건으로 새 경로를 시험**합니다. 정상 작업과 함께 가짜 완료, 기준 변경, 오래된 PASS 재사용, 입력 변경, validator 실패, judge timeout, 재개, 훅 누락, 임시 runner를 시험합니다.
4. **통과 후 전환**합니다. 옛 managed 정책·MCP·agents·`/opt` 잔재를 한 묶음으로 제거하고, 필수 훅의 실제 로딩과 일반 읽기·편집·검색을 확인합니다.
5. **참조와 자동 작업을 정리**합니다. HANDOFF·메모리·`resume-gate` 명시 의존을 새 경계로 바꿉니다. L4 cron의 사후 `git checkout`·새 파일 삭제 방식은 격리 작업공간으로 교체해야 합니다. 현재 runner는 실행 중 사용자의 편집까지 되돌릴 위험을 스스로 명시합니다. [cron:17](/home/firesinger/coastal-wiki/tools/llm-wiki-audit/run-audit-cron.sh:17)
6. **운영 실패를 회귀 검사로 축적**한 뒤 다음 작업 종류로 확장합니다. 한 번에 전 저장소용 범용 프레임워크를 만들지 않습니다.

사용자 결정이 남는 항목은 세 가지입니다.

- 첫 파일럿을 **XBeach 기능 한 건**으로 잡을지, 다른 우선 기능을 선택할지.
- 기존 전수 감사 계약들은 **상태를 보존하고 보류**할지, 별도 명시 결정으로 범위를 개정할지. 재설계가 기존 미완을 완료로 바꾸어서는 안 됩니다.
- 새 기능 작업의 검증을 **결정적 검사＋독립 검토자 1명, 충돌 시 추가 검토**로 시작할지, 기존 Codex＋Grok 만장일치를 계속 요구할지. 전자를 권하지만, 기존 게이트를 대체하는 정책 결정으로 명시해야 합니다.

Codex session ID: 01a0f7d8-5c87-70a2-840a-4e8929fa54fc
Resume in Codex: codex resume 01a0f7d8-5c87-70a2-840a-4e8929fa54fc
