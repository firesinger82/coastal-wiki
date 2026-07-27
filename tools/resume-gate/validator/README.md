# resume-gate stage-3 validator

`validate.py`는 judge를 호출하지 않는 결정론 계층이다. strict JSON decode가
Draft 2020-12 schema보다 먼저 실행되고, 그 뒤 manifest membership, JCS binding,
realpath containment, source SHA-256, locator 범위, code/PDF quote를 검사한다.
실패는 이후 judge가 뒤집을 수 없다.

## 실행

```bash
.venv/bin/python tools/resume-gate/validator/validate.py manifest \
  --repo-root . \
  --manifest tools/resume-gate/fixtures/pilot/manifest.draft.json

.venv/bin/python tools/resume-gate/validator/validate.py submission \
  --repo-root . \
  --manifest <동결 manifest> \
  --submission <submission JSON> \
  --launcher-run-id <run_id>
```

stdout은 `status`, 정렬·중복 제거된 `failure_codes`, `issues`와 계산 가능한
JCS hash를 담은 단일 JSON 객체다. PASS는 exit 0, FAIL은 exit 1이다. 현재 draft는
control hash 네 필드의 의도적인 `TBD` 때문에 `SCHEMA_VALIDATION_FAILED`가 정상이다.

PDF는 `/usr/bin/pdftotext`만 사용한다. 각 물리 1-기반 페이지 `N`을
`["/usr/bin/pdftotext", "-f", "N", "-l", "N", path, "-"]`,
`shell=False`로 따로 추출한다. 전체 문서 출력 분할은 사용하지 않는다. code와 PDF
quote는 모두 Unicode NFKC 후 연속 whitespace를 한 칸으로 바꿔 비교한다.

## failure code enum

| code | 의미 |
|---|---|
| `JSON_DECODE_ERROR` | UTF-8 strict decode 또는 JSON 문법 실패 |
| `JSON_DUPLICATE_KEY` | object key 중복; schema 이전 거부 |
| `SCHEMA_VALIDATION_FAILED` | Draft 2020-12 instance 검증 실패 |
| `CANONICALIZATION_ERROR` | integer-only RFC 8785/JCS 표현 생성 실패 |
| `CONTRACT_VERSION_MISMATCH` | contract version const/문서 간 결박 불일치 |
| `MANIFEST_BINDING_MISMATCH` | submission의 manifest ID/JCS SHA 불일치 |
| `RUN_ID_MISMATCH` | launcher와 submission run ID 불일치 |
| `SOURCE_ID_UNKNOWN` | work_items↔sources, control 또는 candidate membership 불일치 |
| `LOCATOR_NOT_REGISTERED` | control/submission locator가 frozen source locator에 없음 |
| `LOCATOR_RANGE_REVERSED` | locator `start > end` |
| `PATH_OUTSIDE_PROTECTED_ROOT` | realpath가 repo root 밖이거나 symlink로 탈출 |
| `SOURCE_READ_ERROR` | source/schema/input이 없거나 regular file로 읽히지 않음 |
| `SOURCE_HASH_MISMATCH` | 보호 source의 실제 bytes SHA-256 불일치 |
| `LOCATOR_OUT_OF_RANGE` | 실제 code line/PDF 물리 page 범위 밖 |
| `QUOTE_MISMATCH` | 정규화한 quote가 지정 source slice에 없음 |
| `PDF_EXTRACTION_FAILED` | 고정 `pdftotext` 실행·출력 실패 |
| `CANARY_FABRICATED_CLAIM` | stage-4 judge가 semantic canary를 적발할 때 쓰는 frozen control code; stage-3는 의미 판정을 하지 않음 |
| `VALIDATOR_INTERNAL_ERROR` | 예외·schema 자체 오류 등 validator fail-closed |

모든 값은 manifest의 failure-code pattern
`^[A-Z][A-Z0-9_]{2,63}$`을 만족한다.

## control input artifact

- canary:
  `tools/resume-gate/fixtures/pilot/canary-fabricated-claim.submission.json`
- parser-negative:
  `tools/resume-gate/fixtures/pilot/parser-negative-duplicate-source.manifest.json`
- execution:
  `tools/resume-gate/validator/validate.py`

각 파일의 raw bytes를 그대로 SHA-256 한다.

canary 파일의 manifest SHA는 64자리 `0`인 의도적인 binding slot이다. 최종 manifest가
canary input SHA를 포함하고 submission이 다시 최종 manifest SHA를 포함하면 해시
자기참조가 생기므로, stage-3 test/runtime은 input artifact hash를 먼저 확인한 뒤 이
slot만 현재 manifest JCS SHA로 메모리에서 결박한다. 원본 input artifact bytes는
변경하지 않는다. `CAUGHT` 여부와 `CANARY_FABRICATED_CLAIM`은 stage-4의 두 독립
judge가 판단한다. stage-3의 기대 결과는 실제 locator와 quote에 대한 deterministic
PASS다.

parser-negative 파일은 `sources.swan_xnl4v5_bqf` key를 두 번 가진 raw JSON이다.
strict decoder가 draft의 의도적인 TBD schema 오류를 보기 전에
`JSON_DUPLICATE_KEY`로 거부해야 하며, 기대 control status는 `REJECTED`다.
