# resume-gate 외부 judge adapter

이 디렉토리는 4단계 외부 의미 판정 adapter만 구현한다. adapter의 `VALIDATED`는
외부 출력이 계약·binding 검사를 통과했다는 뜻이며 완료 판정이 아니다. 유효한
`FAIL`·`INCONCLUSIVE`도 `VALIDATED`로 반환된다. adapter 파이프라인 자체의 오류는
항상 `status=FAIL`이고 외부 judge 출력으로 복구할 수 없다.

## 파일과 고정값

- `adapter.py`: deterministic 재검증, DATA 조립, 주입 가능한 runner, CLI wrapper
  decode, judge schema·echo 검증.
- `prompt.fixed.txt`: 사용자 승인 고정 지시부. LF, 마지막 newline 포함 SHA-256은
  `7a71c502a919bfb3ca70e18f1aca7dbb392dd5e7808f4962e7237ef9f75fe8b0`이며
  `adapter.py`의 `PROMPT_SHA256`에 고정했다.
- judge 계약 schema는 `../schemas/judge.schema.json`, deterministic 결박과 source
  snapshot은 기존 `../validator/validate.py`를 직접 로드해 재사용한다. CLI 생성
  보조에는 이 객체에서 최상위 `allOf`만 제거한 런타임 파생본을 두 judge에 동일하게
  사용하며, 계약 검증은 계속 원본 전체 schema로 수행한다.

adapter는 시작할 때 prompt 해시와 API-key 환경을 먼저 검사한 후 다음 순서로
진행한다.

1. stage-3 `validate_submission`을 다시 실행한다.
2. manifest와 source를 다시 검증해 source SHA-256 확인 뒤 생성된 snapshot만
   사용한다. code는 등록된 정확한 line range, PDF는 validator의
   `/usr/bin/pdftotext -f N -l N ... -` 단일 physical page 결과를 사용한다.
3. slice에는 NFKC를 적용하되 line/page 구조와 whitespace는 보존한다.
4. strict-decoded allowlist로 DATA를 조립한다. `schema_version`은 submission의
   strict-decoded 정수 값을 사용하고, `attempt_reason`은 읽어 전달하지 않는다.
5. 원본 schema에서 최상위 `allOf`만 메모리에서 제거해 생성 보조 schema를 만든 뒤,
   runner preflight 후 한 번만 외부 CLI를 호출한다.
6. Codex JSONL 또는 Grok JSON wrapper를 strict decode하고, 그 안의 judge JSON도
   duplicate-key를 거부하는 strict decode를 한다.
7. 원본 `judge.schema.json` 전체로 검증한 뒤 `contract_version`, `manifest_id`,
   `manifest_sha256`, `submission_sha256`, `judge`를 UTF-8 bytes로 비교하고,
   `engine_version`도 고정 기대값과 비교한다.

Codex 생성 보조 schema는 owner-only secure temporary file로 기록해
`--output-schema`에 넘기고 프로세스 종료 즉시 삭제한다. Grok은 같은 파생 객체를
compact JSON argv로 넘긴다. CLI가 nonzero exit하거나 Codex가 `error` 또는
`turn.failed`를 내면 마지막 error event message를 최대 500자로 잘라
`failure.detail`에 포함한다.

DATA 문법은 다음 순서로 고정한다. JSON scalar/object는 UTF-8, compact JSON이며
object 내부 key 순서도 adapter 코드에 고정되어 있다.

```text
<<<RESUME_GATE_DATA_BEGIN>>>
JUDGE_NAME=<JSON string>
ENGINE_VERSION=<JSON string>
schema_version=<compact JSON integer; strict-decoded submission value>
contract_version=<JSON string>
manifest_id=<JSON string>
manifest_sha256=<JSON string>
submission_sha256=<JSON string>
candidate={"source_id":...,"claim_type":...,"claim":...}
evidence[0].locator=<compact JSON object>
evidence[0].quote=<JSON string>
evidence[0].frozen_slice=
<<<SLICE_0_BEGIN>>>
<NFKC frozen source slice>
<<<SLICE_0_END>>>
...
<<<RESUME_GATE_DATA_END>>>
```

delimiter 문자열이 allowlisted scalar, quote, slice에 나타나면 framing을 추정하지
않고 `DATA_ASSEMBLY_FAILED`로 닫는다.

## runner와 인증

`JudgeRunner`는 `preflight`와 `invoke` 두 메서드뿐이다. 테스트는 전부
`MockRunner`를 주입하며 `SubprocessJudgeRunner`나 외부 judge를 호출하지 않는다.

API-key 인증은 다음처럼 거부한다.

- 호출 환경에 `OPENAI_API_KEY`, `XAI_API_KEY`, 또는 legacy
  `GROK_CODE_XAI_API_KEY` 이름이 존재하면 빈 값이어도 runner 전에 거부.
- Codex는 owner-only `auth.json`의 `auth_mode=chatgpt`, API key 부재, cached token
  존재와 `codex login status`의 stdout 또는 stderr 한 스트림에서 정확한
  `Logged in using ChatGPT` 출력을 요구.
- Grok은 owner-only `auth.json`의 모든 entry가 `https://auth.x.ai::` issuer,
  `auth_mode=oidc`, refresh token 존재 조건을 만족해야 한다. custom
  model/auth section과 credential-bearing config, external auth/OIDC/proxy 환경
  override는 거부한다.
- Grok은 exact empty cwd에서 `grok inspect --json`을 실행해 project instruction,
  hook, plugin, MCP server, non-bundled skill, non-builtin agent와 enabled external
  compatibility가 하나라도 있으면 호출 전에 거부한다. `config.toml`도 `cli`·`ui`
  이외 section을 허용하지 않는다.
- 실제 child 환경에서도 API-key 변수를 제거하고 `/usr/bin/env -u`를 호출
  command에 명시한다.
- Grok `0.2.112`의 local headless 문서가 정의한
  `GROK_DISABLE_AUTOUPDATER=1`을 child 환경에 강제로 넣어 version preflight와
  실제 판정 사이의 자동 업데이트를 막는다.

## 설치 버전에서 고정한 CLI

2026-07-27 이 PC에서 다음을 직접 확인했다.

```text
codex --version       -> codex-cli 0.144.1
codex exec --help     -> --ephemeral, --sandbox read-only, --cd,
                         --skip-git-repo-check, --ignore-user-config,
                         --ignore-rules, --json, --output-schema, stdin "-"

grok --version        -> grok 0.2.112 (9bbd559437)
grok --help           -> --cwd, --sandbox, --tools, --disallowed-tools,
                         --deny, --permission-mode, --no-plan,
                         --no-subagents, --no-memory, --disable-web-search,
                         --max-turns, --output-format, --json-schema,
                         --verbatim, -p
```

Codex 고정 argv:

```text
/usr/bin/env -u OPENAI_API_KEY -u XAI_API_KEY \
  /home/firesinger/.local/bin/codex exec \
  --ephemeral --sandbox read-only \
  --cd /opt/coastal-resume/empty \
  --skip-git-repo-check --ignore-user-config --ignore-rules \
  --json \
  --output-schema /tmp/resume-gate-codex-schema-<random>.json \
  -
```

Grok 고정 argv:

```text
/usr/bin/env -u OPENAI_API_KEY -u XAI_API_KEY \
  GROK_DISABLE_AUTOUPDATER=1 \
  /home/firesinger/.local/bin/grok \
  --cwd /opt/coastal-resume/empty \
  --sandbox read-only \
  --tools '' \
  --disallowed-tools Agent \
  --deny MCPTool \
  --permission-mode dontAsk \
  --no-plan --no-subagents --no-memory --disable-web-search \
  --max-turns 1 \
  --output-format json \
  --json-schema '<최상위 allOf만 제거한 런타임 파생 schema의 compact JSON>' \
  --verbatim \
  -p '<prompt.fixed.txt + blank LF + generated DATA>'
```

`--tools ''`는 built-in tool allowlist를 비우고, 항상 남을 수 있는 MCP meta-tool은
`--deny MCPTool`로 차단한다. `--disallowed-tools Agent`와 `--no-subagents`는
subagent surface를 이중 차단한다. cwd는 존재하는 빈 디렉토리여야 하며 adapter가
호출 전에 이를 확인한다.

## 테스트

```bash
.venv/bin/python tools/resume-gate/tests/test_judge.py
```

mock suite는 canary DATA golden bytes, `attempt_reason` 제외, echo/engine 변조,
생성 보조 schema의 단일-key 파생·두 judge 동일성, 원본 schema 집행 유지
(`PASS`+non-empty issues 거부), CLI error event 진단 전파, `INCONCLUSIVE`,
timeout, nonzero exit, API-key env, prompt hash mismatch, CLI argv와 Grok
customization preflight를 검사한다.

## 알려진 경계

- `engine_version`은 승인 범위대로 설치 CLI build 문자열을 고정한다. provider가
  subscription 뒤의 model revision을 바꾸는 것은 이 값만으로 탐지할 수 없다.
- read-only sandbox는 repository write를 막지만 CLI 자체의 subscription token
  refresh·session runtime state 기록까지 금지하지는 않는다.
- 현재 사용자 Grok profile처럼 marketplace/plugin/hook/MCP가 로드되는 profile은
  preflight에서 거부된다. live 검증자는 cached OAuth auth는 유지하되 customization이
  없는 격리된 `GROK_HOME`을 준비해야 한다.
- 이 단계는 decision engine, 두 judge 만장일치, control 결과, evidence chain 또는
  root 설치를 구현하지 않는다.
