# resume-gate — 외부 완료판정 게이트 (설계/1단계)

> 상태: **1단계(계약·스키마) 완료.** 아직 실행 권한은 없다. root 설치, MCP 서버, hook, validator 실행 로직은 후속 단계이며 이 디렉토리의 스키마만으로는 강제력이 생기지 않는다.

## 목적과 권한 경계

`decision.json(status=PASS)`만 판독 완료를 뜻한다. worker 자연어, 자기평가, confidence, TODO, `attempt_reason`, subagent 요약은 완료 권한이 없다. 결정 파일은 worker submit 경로가 아니라 결정 엔진만 생성한다.

**이 게이트는 모델의 자기검증을 대체·보완하는 장치가 아니다.** 모델이 스스로 검증을 얼마나 잘하게 되든, 자기신고에 완료 권한이 없다는 사실은 변하지 않는다. 모델 세대 교체(자기검증 능력 향상, "재검토 지시는 불필요"류 마이그레이션 권고)를 이유로 이 계약을 제거·완화하지 않는다. (CLAUDE.md 작업 규범 #4)

방어 대상은 관리형 Claude Code 세션과 그 세션의 tool·subagent·MCP다. 악성 사람/root 또는 같은 UID의 별도 악성 프로세스에 대한 비부인성은 범위 밖이다. 보호된 source tree와 설치될 실행기는 root-owned read-only라는 전제를 둔다.

## 1단계 계약

| 파일 | 생성자 | 핵심 책임 |
|---|---|---|
| `schemas/manifest.schema.json` | 사람 승인 후 동결 | 분모 SSOT, source registry, canary/parser-negative control backing |
| `schemas/submission.schema.json` | worker | claim과 source anchor만 제출; 완료 권위 없음 |
| `schemas/judge.schema.json` | Codex/Grok adapter | exact manifest/submission/engine에 묶인 외부 판정 |
| `schemas/decision.schema.json` | 결정 엔진 | PASS 진리표, provenance, evidence-chain binding |

모든 객체는 `additionalProperties: false`를 사용한다. 계약 버전은 `resume-gate/1`, 현재 각 schema version은 `1`이다.

### 고정 분모

`manifest.work_items`가 유일한 분모 SSOT다. 요구 work-item 수는 항상 `len(work_items)`로 계산하며 수동 `denominator`나 별도 code/PDF count는 존재하지 않고 입력하면 schema-invalid다. `work_items`는 source ID 문자열의 `uniqueItems` 배열이고, source 메타데이터는 `sources.<source_id>` map에 한 번만 둔다.

따라서 예전처럼 work item은 1개인데 `denominator={code_units:2,pdf_claims:1}`인 manifest는 유효하지 않다. raw JSON에서 동일 source key를 두 번 쓴 경우에는 schema 이전 strict decoder가 `JSON_DUPLICATE_KEY`로 거부한다.

### source와 locator

- source path는 repo-relative POSIX lexical path만 허용한다. 절대경로, Windows drive/separator, `..` segment, NUL은 schema-invalid다.
- `artifact_type=code`이면 모든 locator는 `line_range`, `artifact_type=pdf`이면 모두 `page_range`여야 한다. 이 관계는 schema `if/then`으로 강제한다.
- locator의 `start`와 `end`는 각각 1 이상이다. 두 값의 상호 비교는 표준 JSON Schema가 표현하지 못하므로 stage-3가 `start <= end`를 검사한다.

### frozen controls

manifest는 정확히 `controls.canary`와 `controls.parser_negative`를 요구한다. 각 control에는 사람이 동결한 다음 값이 모두 있어야 한다.

- 공통: `control_id`, `kind`, `expected_status`, `allowed_failure_codes`, `input_artifact_sha256`, `execution_artifact_sha256`
- canary: 고정 `source_id`와 `locator`, `kind=canary`, `expected_status=CAUGHT`
- parser-negative: 고정 `mutation`(`mutation_id`, `operation`, `target`), `kind=parser_negative`, `expected_status=REJECTED`

decision의 실제 control result도 같은 control ID와 input/execution artifact hash를 운반한다. stage-3는 이를 동결 manifest와 대조하고 status 및 failure code allowlist까지 일치해야만 control input을 통과시킨다.

### submission과 judge 입력 smuggling 방지

submission에는 `schema_version`, `contract_version`, frozen manifest의 `manifest_id+sha256`가 필수다. `complete`, `pass`, `verified`, `confidence`, `reader`, `status`, 출력경로, 명령, judge prompt/model 등 미등록 필드는 거부된다.

evidence에는 별도 `source_id`가 없다. 모든 evidence가 `candidate.source_id`를 상속하므로 candidate와 evidence가 서로 다른 source를 지칭하는 상태는 표현할 수 없다. claim, quote, reasoning, issue는 whitespace-only 문자열을 허용하지 않는다.

`attempt_reason`은 제출 감사 메타데이터일 뿐 judge 입력에서 반드시 제외한다. judge adapter는 strict-decoded submission에서 아래 allowlist만 새 데이터 객체로 구성해야 한다.

```text
contract_version
manifest { manifest_id, sha256 }
submission_sha256
candidate { source_id, claim, claim_type }
evidence[] { locator, quote }
frozen source slices
```

claim과 quote는 prompt 명령이 아니라 JSON data field로 전달한다. `attempt_reason`이나 worker가 만든 prompt 문자열을 judge system/developer instruction에 이어 붙이면 `JUDGE_INPUT_SMUGGLING`이다.

judge가 `verdict=PASS`를 내리려면 `claim_supported_by_evidence=true`이고 `issues=[]`여야 한다. 이 일관성은 judge schema의 `if/then`, `const`, `maxItems`로 직접 강제한다.

## PASS 진리표

```text
PASS =
      deterministic.status   == PASS
  AND codex.verdict          == PASS
  AND grok.verdict           == PASS
  AND canary.status          == CAUGHT
  AND parser_negative.status == REJECTED
  AND evidence_chain.status  == VALID
```

`decision.schema.json`은 위 식을 양방향으로 인코딩한다.

- `status=PASS`이면 여섯 입력이 모두 정확한 통과값이어야 한다.
- 여섯 입력이 모두 통과값이면 `status`는 반드시 `PASS`다.
- deterministic `PASS`는 `failure_codes=[]`, deterministic `FAIL`은 failure code가 1개 이상이어야 한다.
- 어느 judge든 FAIL/INCONCLUSIVE, canary MISSED/NA, parser-negative ACCEPTED/NA, invalid evidence chain이면 PASS record 자체가 schema-invalid다.

deterministic hard fail은 judge가 뒤집지 못한다. 동일 candidate/evidence hash의 두 번째 실패, 연속 3회 같은 failure code이면서 새 evidence 없음, attempt 6회 초과는 후속 결정 엔진이 `HARD_STOP`/`FAILED_STOPPED`로 처리하며 PASS를 만들지 않는다.

## version/provenance와 evidence-chain binding

해시는 lowercase SHA-256이다. stage-3는 입력을 UTF-8 strict decode하고 duplicate key를 거부한 뒤 RFC 8785 JSON Canonicalization Scheme(JCS) 표현을 해시한다. 비정규 원문 바이트나 Python의 기본 key-preserving decoder 결과를 곧바로 신뢰하지 않는다.

binding 순서는 다음과 같다.

1. submission은 exact `contract_version`과 frozen `manifest_id+manifest_sha256`를 싣는다.
2. 각 judge result는 `schema_version`, `contract_version`, 동일 manifest binding, `submission_sha256`, `judge`, `engine_version`을 싣는다.
3. decision은 top-level decision `schema_version+contract_version`과 `provenance`에 manifest `(schema_version,id,sha256)`, submission `(schema_version,sha256)`, Codex/Grok `(schema_version,engine_version,result_sha256)`, `decision_engine_version`을 모두 싣는다.
4. `inputs.evidence_chain.provenance_sha256`는 `SHA256(JCS(decision.provenance))`여야 한다.
5. `chain_root`는 아래 canonical envelope의 SHA-256이다. `deterministic_sha256`는 canonical deterministic input에서 계산하고 나머지 hash는 decision provenance/control results에서 가져온다.

```json
{
  "schema_version": 1,
  "contract_version": "resume-gate/1",
  "run_id": "...",
  "attempt_id": 1,
  "provenance_sha256": "...",
  "deterministic_sha256": "...",
  "codex_result_sha256": "...",
  "grok_result_sha256": "...",
  "canary_input_artifact_sha256": "...",
  "canary_execution_artifact_sha256": "...",
  "parser_negative_input_artifact_sha256": "...",
  "parser_negative_execution_artifact_sha256": "..."
}
```

schema는 이 binding의 필수 필드·형식·버전을 강제한다. 실제 hash 재계산과 문서 간 equality는 stage-3 책임이다.

## stage-3 validator 필수 fail-closed 검사

아래는 여러 instance/file 또는 두 숫자 값을 비교하거나 파일시스템을 읽어야 하므로 표준 Draft 2020-12 JSON Schema만으로는 완전하게 표현할 수 없다. 하나라도 실패하면 deterministic FAIL이며 명시된 failure code를 낸다.

| 검사 | failure code | schema만으로 불가능한 이유 |
|---|---|---|
| strict JSON decode에서 모든 중복 key 거부 | `JSON_DUPLICATE_KEY` | decoder가 중복 key를 덮어쓰면 schema에는 이미 정보가 사라짐 |
| locator `start <= end` | `LOCATOR_RANGE_REVERSED` | JSON Schema에는 instance 숫자 두 개의 대소 비교 연산이 없음 |
| `work_items`·control·candidate source ID가 frozen `sources` key에 존재 | `SOURCE_ID_UNKNOWN` | 같은/다른 문서의 동적 key membership 비교가 없음 |
| source hash가 보호된 실제 file bytes와 일치 | `SOURCE_HASH_MISMATCH` | schema는 파일을 읽거나 SHA-256을 계산하지 않음 |
| locator가 실제 line/page 범위 안에 존재 | `LOCATOR_OUT_OF_RANGE` | 외부 code/PDF 내용 접근 필요 |
| quote가 지정 locator 원문에 실제 존재 | `QUOTE_MISMATCH` | 외부 원문 extraction/byte·page 대조 필요 |
| lexical path를 realpath로 해석해 허용 root 내부이고 symlink escape가 없음 | `PATH_OUTSIDE_PROTECTED_ROOT` | schema는 filesystem realpath/symlink를 해석하지 않음 |
| launcher run ID와 submission run ID 일치 | `RUN_ID_MISMATCH` | launcher 상태와 문서 간 비교 필요 |
| contract/schema/manifest ID+hash가 모든 문서에서 동일 | `MANIFEST_BINDING_MISMATCH` / `CONTRACT_VERSION_MISMATCH` | 독립 JSON instance 간 equality 비교 필요 |
| submission/judge result hash와 engine version provenance 대조 | `SUBMISSION_HASH_MISMATCH` / `JUDGE_BINDING_MISMATCH` | canonical hash 계산 및 문서 간 비교 필요 |
| control ID, kind, source/mutation, expected status, allowed code, input/exec hashes 대조 | `CONTROL_BINDING_MISMATCH` / `CONTROL_STATUS_MISMATCH` / `CONTROL_FAILURE_CODE_NOT_ALLOWED` | result와 frozen manifest 간 비교 필요 |
| judge input allowlist 및 `attempt_reason` 제외 | `JUDGE_INPUT_SMUGGLING` | adapter가 실제 구성한 외부 호출 payload 감사 필요 |
| JCS canonical hash, provenance hash, chain root 재계산 | `CANONICALIZATION_ERROR` / `PROVENANCE_HASH_MISMATCH` / `EVIDENCE_CHAIN_INVALID` | schema는 canonicalization/cryptographic hash를 계산하지 않음 |

stage-3는 이 표의 검사를 생략하거나 예외를 삼키면 fail-open이 아니라 `VALIDATOR_INTERNAL_ERROR`로 FAIL해야 한다. 실제 validator 실행 로직은 1단계 범위 밖이며 이 README는 3단계 구현자가 지켜야 할 계약이다.

## fixture 자가검증

```bash
.venv/bin/python tools/resume-gate/tests/test_schemas.py
```

테스트는 Draft 2020-12 runtime validator로 schema 자체와 positive/negative fixture를 검증한다. 각 schema-negative는 단순 invalid 여부뿐 아니라 기대한 validator keyword/message로 실패했는지 확인한다. raw duplicate-key는 schema 이전 strict decoder fixture, `start>end`는 JSON Schema 통과 후 위임된 stage-3 failure-code fixture로 각각 따로 검증한다.

## 현재 하지 않은 것과 다음 단계

- root 설치, MCP 서버, hook, validator/decision-engine 실행 로직, pilot 실행은 하지 않았다.
- 보호 tree나 canonical model 파일을 접근·수정하지 않는다.
- 2단계에서 사람이 실제 pilot `manifest_id`, `work_items`, source path/hash/locator, 두 control과 artifact hash를 검토·동결해야 한다.

1단계 schema와 PASS 행렬 승인 후 2단계 pilot manifest 값 고정으로 진행할 수 있다. 실제 강제력은 후속 stage-3 validator와 root-owned 설치가 완료되기 전까지 없다.
