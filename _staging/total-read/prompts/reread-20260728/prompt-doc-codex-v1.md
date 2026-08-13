# 판독 프롬프트 doc-v1 — doc 축 1차 판독자 (Codex)

너는 total-read 재판독의 doc축 1차 판독자다. 아래 WO-20260728 전문이 규격이다. 요점:

1. 파일 접근은 오직 게이트로만:
   python3 /home/firesinger/coastal-wiki/_staging/total-read/reread_gate_20260728.py next <run_id>
   가 출력하는 CHUNK-HEADER + 본문(===END-CHUNK=== 까지)이 유일한 원문 공급원이다.
   ★models/·records/·records-structural/ 직접 열람 금지(위반=shard 실패).
2. chunk 마다 receipt 제출: ack <run_id> '<JSON한줄>' — 필드 run_id, path, source_sha256,
   chunk_index, first_line, last_line, chunk_sha256, last_line_seen(=last_line),
   eof(파일 마지막 chunk 만 true), ack("ACK <chunk_index>/<total_chunks> <last_line> <chunk_sha256>").
3. 파일 전 chunk ack 후 token → 레코드 JSON 작성 → verify (PASS 까지 정정) → submit.
   레코드 필수 필드: axis="doc", model=<모델>, path/sha256=source_sha256/bytes/lines_or_pages/
   chunk_manifest_sha256 은 CHUNK-HEADER 값, read_status="complete",
   read_range="1-<logical_lines>", reader="openai/<실제 런타임 모델 ID>", read_at=실제 UTC,
   artifact_class="semantic_read", producer="llm:openai/<실제 런타임 모델 ID>",
   read_method="llm_full_read", comprehension_status="complete", prompt_sha256=이 파일의 sha256,
   audit_seed(WO §6.1), run_id, auditor="llm:xai/grok", audit_status="pending",
   content={what_it_is, entities[], constants[], params_defined[], equations[], io[], calls[],
   verbatim_spans[], unresolved[]} — doc 파일이라 entities 는 섹션/제목/정의 항목,
   constants·params 는 문서에 명시된 수치·파라미터(라인앵커 필수), unresolved 는 의미상
   모순·불명(문서 내 상충 수치, 참조 깨짐 등)만.
4. 앵커 규율: name 은 bare 식별자/토큰만(소수 리터럴 name 금지), line 은 그 토큰이 실재하는
   바로 그 줄(등차 추정 금지), 제출 전 전 앵커 자가대조(source행 = first_line + scratch행 − 2).
5. 판단·중요도 필드(note_worthy·importance·tier·core) 절대 금지. 요약 아닌 열거.
   미독 범위를 complete 로 위장 금지(그 shard 는 실패다).
6. 데이터성 텍스트(입력 카드·par·bathy 소형 파일)는 구조(필드명·값·단위)를 열거하고,
   스크립트가 아닌 문서(md·tex·txt)는 섹션 구조와 명시 수치를 열거한다.

--- 이하 WO-20260728-reread.md 전문 ---

# WO-20260728 — EFDC·FUNWAVE·LISFLOOD-FP semantic 재판독

상태: **고정(frozen)**  
승인 근거: 2026-07-28 사용자 승인, `METHOD-AUDIT-20260724.md` §3-§4 및 `SPEC.md` 스키마 v2  
범위: 재판독 큐의 비어 있지 않은 텍스트 2,238건. 큐 원본과 `records-structural/20260724/`는 읽기 전용이다.

이 문서는 Claude가 생산을 시작하기 전에 Codex가 고정해야 하는 shard, 역할, 레코드 필드,
파일별 완료 프로토콜, validator/완료 게이트, 맹검 seed 및 중복 선택 규칙이다. 이 문서와
`SPEC.md`가 충돌하면 사용자 승인 사항을 구체화한 이 문서를 이번 재판독에 적용하되, 판단·중요도
금지와 원문 전수 판독 규칙은 완화할 수 없다.

## 1. 입력 동결과 분모

### 1.1 입력 해시

| 입력 | 행 | SHA-256 |
|---|---:|---|
| `reread-queue/reread-EFDC-20260728.txt` | 182 | `8952443a7beea9011f817458b82a9df7e08c020cea981d986bf100e9d1fd14dd` |
| `reread-queue/reread-FUNWAVE-20260728.txt` | 964 | `4a4c4a7619cfee1e5c83d76f5688315c79027f5587d92377f95c60cc23b83c7e` |
| `reread-queue/reread-LISFLOOD-FP-20260728.txt` | 1,092 | `73e8434cfa0122c34f71dca6e16e17337f8fdc28c81290a930650da6f63342eb` |
| `reread-queue/mechanical-exceptions-20260728.txt` | 10 | `f2e6c382f6de4330b4717e403a3fe1ab0b2179f89ada41122753d46f6f9b3085` |
| `records-structural/20260724/manifest.json` | 3 entries | `edad4acd32d519834c8cb05d7e7fde7cbe17d2cb3e4347d8e845b7c4f9687f26` |

큐 3파일은 `axis<TAB>path` 2열이며 path는 `models/` 접두 없는 정규형이다. 2,238개 path는
중복 0, 누락 0, 0-byte 0임을 preflight에서 다시 확인한다. 입력 해시가 하나라도 다르면 작업을
시작하지 않고 새 승인본을 요구한다. 큐 파일을 정렬하거나 다시 쓰지 않는다.

### 1.2 수치 정합

| 구분 | EFDC | FUNWAVE | LISFLOOD-FP | semantic 재판독 |
|---|---:|---:|---:|---:|
| code | 6 | 243 | 430 | **679** |
| doc | 0 | 701 | 645 | **1,346** |
| web | 137 | 0 | 8 | **145** |
| note | 39 | 20 | 9 | **68** |
| 합계 | **182** | **964** | **1,092** | **2,238** |

`doc 1,356`은 원래 구조 인덱스의 doc 분모(711+645)다. 그중 FUNWAVE 0-byte 10건은
`mechanical-exceptions-20260728.txt`에 있으므로 LLM semantic 재판독량은 **1,346**이다. 즉 전체
축 분모는 doc 1,356으로 유지하되, Codex가 실제로 읽을 nonempty doc은 1,346이고 나머지 10은
기존 mechanical 예외다. 2,248 = semantic 2,238 + mechanical 10이다.

## 2. 역할과 shard 고정

### 2.1 역할

| 큐 축 | 1차 판독자 | 맹검 감사자 | 비고 |
|---|---|---|---|
| code 679 | Claude | Codex | EFDC 6·FUNWAVE 243·LISFLOOD-FP 430 |
| doc 1,346 nonempty | Codex | Grok | FUNWAVE 701·LISFLOOD-FP 645; mechanical 10은 LLM에 보내지 않음 |
| web 145 | Grok | Claude | EFDC 137·LISFLOOD-FP 8 |
| note 68 | Claude | Codex | `RESUME.md` 벤더 표의 note=Claude 선례 적용 |

`note`는 이번 큐에서 독립 운영 축 및 레코드 `axis: "note"`로 유지한다. doc으로 이름만 바꾸거나
doc 분모에 합치지 않는다. 감사자는 1차 레코드와 구조 인덱스를 보지 않고 원문을 독립 판독한 뒤
대조한다. 실행 시 `producer`, `reader`, `auditor`에는 `claude` 같은 통칭 대신 실제
`vendor/model-id`를 기록한다.

### 2.2 분할 알고리즘과 확정 shard 수

각 `(axis, model)` 그룹을 큐에서 필터한 뒤 path의 UTF-8 바이트를 `LC_ALL=C`로 오름차순 정렬한다.
목표 상한은 shard당 50파일이다. 그룹 크기를 `N`, shard 수를 `k=ceil(N/50)`, `q=floor(N/k)`,
`r=N mod k`라 하면 앞 `r`개 shard에 `q+1`, 나머지에 `q`개를 연속 배정한다. 따라서 같은 입력
해시에서는 언제나 같은 경계가 나온다.

| 축 | 모델 | N | shard ID | 확정 크기 |
|---|---|---:|---|---|
| code | EFDC | 6 | 000 | 6 |
| code | FUNWAVE | 243 | 000-004 | 49×3, 48×2 |
| code | LISFLOOD-FP | 430 | 000-008 | 48×7, 47×2 |
| doc | FUNWAVE | 701 | 000-014 | 47×11, 46×4 |
| doc | LISFLOOD-FP | 645 | 000-012 | 50×8, 49×5 |
| web | EFDC | 137 | 000-002 | 46×2, 45×1 |
| web | LISFLOOD-FP | 8 | 000 | 8 |
| note | EFDC | 39 | 000 | 39 |
| note | FUNWAVE | 20 | 000 | 20 |
| note | LISFLOOD-FP | 9 | 000 | 9 |

총 **50 shard**(code 15, doc 28, web 4, note 3)다. `SPEC.md`의 30~60파일 원칙보다 작은 것은
모델·축 경계를 섞지 않기 위한 네 개의 완결 그룹(code/EFDC 6, web/LISFLOOD-FP 8,
note/FUNWAVE 20, note/LISFLOOD-FP 9)뿐이다. 임의 합치기, 파일 이동, shard 재균형은 금지한다.

### 2.3 이름과 충돌 방지

- shard 목록: `shards/reread-20260728/<axis>-<MODEL>-reread20260728-<NNN>.txt`
- preflight manifest: `chunk-manifests/reread-20260728/<run_id>/<path-id>.json`
- chunk 수신확인: `chunk-receipts/reread-20260728/<run_id>/<path-id>.jsonl`
- 합격 semantic 레코드: `records/<axis>-<MODEL>-semantic-reread20260728-<NNN>.jsonl`
- 불합격 레코드: `records-rejected/<axis>-<MODEL>-semantic-reread20260728-<NNN>--<run_id>.jsonl`

`NNN`은 위 표의 0 기반 3자리 ID다. `path-id`는
`SHA256(model + "\0" + normalized_path + "\0" + source_sha256)`의 64자리 hex다. `run_id`는
`reread20260728-<axis>-<MODEL>-<NNN>-<producer-slug>-<UTC YYYYMMDDThhmmssZ>-<8hex nonce>` 형식으로
전역 유일해야 한다. `semantic-reread20260728` 표지가 없는 기존 파일명과 충돌할 수 없으며,
어떤 단계도 기존 파일을 덮어쓰지 않는다. 목표 파일이 이미 있으면 즉시 실패한다. 재시도는 새
`run_id`로 pending/rejected 산출물을 만들며, 합격 canonical 파일은 아직 없을 때만 생성한다.

## 3. semantic 레코드 스키마

JSONL은 UTF-8, 파일당 입력 파일 하나에 정확히 한 JSON object 한 행이다. 기존 content 스키마와
v2 provenance 필드를 모두 유지한다. 아래는 형식 예시이며 `<...>` 값은 생산 시 실측값으로
치환해야 한다.

```json
{"axis":"code","model":"EFDC","path":"EFDC/raw/source_code/EFDCPlus_Stable/EFDC/aaefdc.f90","sha256":"<64-lowercase-hex>","bytes":12345,"lines_or_pages":842,"read_status":"complete","read_range":"1-842","reader":"anthropic/<exact-runtime-model-id>","read_at":"2026-07-28T12:34:56Z","artifact_class":"semantic_read","producer":"llm:anthropic/<exact-runtime-model-id>","read_method":"llm_full_read","comprehension_status":"complete","source_sha256":"<same-64-lowercase-hex-as-sha256>","chunk_manifest_sha256":"<64-lowercase-hex>","prompt_sha256":"<64-lowercase-hex>","run_id":"reread20260728-code-EFDC-000-anthropic-model-20260728T123456Z-a1b2c3d4","auditor":"llm:openai/<exact-runtime-model-id>","audit_seed":"6465d0b8bd3f7acb9a2a437da66cfb37e1a0f0a8033b44214f49f1907e393ae6","audit_status":"pending","content":{"what_it_is":"<파일 역할과 실제 알고리즘을 앵커에 근거해 기술>","entities":["<선언된 entity 전부와 loc>"],"constants":[{"name":"<name>","value":"<value>","line":1}],"params_defined":[{"name":"<name>","default":"<default>","range":"<range 또는 빈 문자열>","loc":1}],"equations":[{"expr":"<expr>","ref":"<원문 근거>","loc":1}],"io":[{"kind":"<kind>","name":"<name>","loc":1}],"calls":["<call과 loc>"],"verbatim_spans":[{"text":"<짧은 원문>","loc":1}],"unresolved":["<의미상 미해결 사항과 관련 line들>"]}}
```

필드 규칙은 다음과 같다.

1. `artifact_class="semantic_read"`, `read_method="llm_full_read"`만 허용한다. 이번 2,238건에
   `structural_index`, `deterministic_parse`, `binary_sweep`, `mechanical_binary`를 쓰지 않는다.
2. `producer="llm:<vendor>/<exact-model-id>"`; `reader`는 같은 `<vendor>/<exact-model-id>`다.
   스크립트가 `producer`, `reader`, complete 상태 또는 content 최종값을 대신 만들 수 없다.
3. 합격 레코드는 `read_status="complete"`, `comprehension_status="complete"`여야 한다. 읽지 못한
   경우 `partial|failed`로 정직하게 기록하되 그 shard는 불합격이다.
4. `sha256 == source_sha256 == sha256sum(models/<path>)`여야 한다. path는 절대경로와 `models/`
   접두가 없어야 한다. `bytes`는 byte 실측값이다.
5. `lines_or_pages`는 LF 개수에, nonempty이고 마지막 byte가 LF가 아니면 1을 더한 논리 line
   수다. manifest에는 `wc_lf_count`와 `final_newline`도 따로 둔다. `read_range`는 complete일 때
   정확히 `1-<lines_or_pages>`다.
6. `chunk_manifest_sha256`은 immutable manifest 파일 원바이트의 SHA-256,
   `prompt_sha256`은 역할 지시·이 work order·실제 판독 prompt를 합친 immutable prompt 파일
   원바이트의 SHA-256이다.
7. `audit_status` 허용값은 `pending|not_sampled|passed|failed`다. canonical 승격 시 pending은 0,
   표본은 `passed`, 비표본은 `not_sampled`여야 한다. `auditor`는 해당 축의 실제 감사 모델이다.
8. `content`의 여덟 필드는 모두 존재해야 한다. 빈 배열은 원문 전수 판독 결과 해당 항목이
   없다는 뜻이다. 미판독 범위를 빈 배열로 위장할 수 없다. `what_it_is`, 모든 선언/entity,
   상수·입력·식·I/O·호출, 짧은 원문 span, 의미상 미해결을 실제 line/page 앵커와 함께 기록한다.
9. `note_worthy`, `importance`, `tier`, `core` 및 동의어인 가치·우선순위·점수·순위·판단 필드는
   어느 깊이에도 만들지 않는다. 레코드는 중요도를 고르거나 요약하지 않고 원문 내용을 열거한다.

## 4. 파일별 완료 프로토콜

### 4.1 preflight와 chunk

1. preflight만 source SHA-256, bytes, MIME/encoding, 논리 line 수를 실측한다.
2. 텍스트를 **논리 line 200개 단위**로 앞에서부터 자른다. chunk `i`는 원문의 byte와 newline을
   그대로 보존하며, 전체 chunk를 순서대로 이어 붙인 byte열은 source와 정확히 같아야 한다.
   마지막 newline 없는 마지막 line도 한 line이다. 200 line을 넘는 chunk는 금지하되, 단일
   line 자체가 커도 그 line을 byte로 쪼개지 않고 1-line chunk로 둔다.
3. manifest에는 `chunk_index`(0 기반), `first_line`, `last_line`, `bytes`, `chunk_sha256`,
   `source_sha256`, `total_chunks`, `logical_lines`, `wc_lf_count`, `final_newline`을 기록한다.
   range는 1부터 EOF까지 공백·중복 없이 이어져야 한다.

### 4.2 순차 수신확인과 출력 잠금

1. 1차 판독자에게 chunk를 index 순으로 하나씩 전달한다. 각 chunk 뒤 판독자는 receipt에
   `run_id`, path, source hash, index, line range, chunk hash, 실제로 본 마지막 line 번호,
   `eof`와 `ACK <index>/<total> <last_line> <chunk_sha256>`를 한 행으로 남긴다.
2. 다음 chunk는 직전 receipt의 index/range/hash가 manifest와 일치할 때만 전달한다. receipt의
   누락, 역순, 중복, hash 불일치가 있으면 그 파일과 shard를 실패 처리한다.
3. 1차 판독 실행환경에는 source chunk, shard 목록, 고정 prompt만 제공한다.
   `records-structural/`, 기존 `records/`, 기존 semantic 레코드는 mount/allowlist에서 제외한다.
   접근 로그에 해당 경로 접근이 하나라도 있으면 실패다. 구조 인덱스는 semantic draft가
   동결된 뒤 별도 validator 프로세스만 연다.
4. 마지막 chunk receipt가 `eof=true`, `last_line=logical_lines`로 검증되기 전에는 writer 권한과
   `EMIT_ALLOWED` 토큰을 주지 않는다. 판독자가 그 전에 완성 레코드 JSON을 출력하면 protocol
   위반으로 해당 shard 전체를 rejected 처리한다. 중간 메모는 content 최종값이나 complete
   선언이 아닌 reader-local scratch에만 둘 수 있다.
5. 모든 receipt가 통과하면 orchestrator가
   `SHA256("EMIT_ALLOWED\0" + run_id + "\0" + source_sha256 + "\0" + chunk_manifest_sha256)`
   토큰을 발급한다. 이 토큰 이후에만 1차 판독자가 semantic record를 한 번 출력한다.
6. 생산물은 audit 종료 전 pending 영역에 둔다. validator·맹검이 끝난 후 합격 파일만 위의
   고정 `records/` 이름으로 원자적 승격하고, 불합격 shard는 `records-rejected/`로 이동한다.

## 5. validator와 완료 게이트

### 5.1 파일/레코드 기계검증

validator는 다음을 전건 검사하고 결과 manifest를 남긴다.

- 큐 3파일의 행수·SHA-256 불변, 2열 형식, path 정규형, 중복 0, source 실재·nonempty.
- JSONL 구문, object당 1행, shard membership과 행수의 정확한 일치, 누락·외부 path·중복 0.
- `(model, normalized_path, source_sha256)` canonical key와 현재 inventory의 정확한 일치.
- 모든 기존/v2 필드와 content 여덟 필드의 존재·type·enum; 금지 판단 필드의 재귀적 부재.
- 역할표와 `axis/model/producer/reader/auditor`의 일치, 구체 model-id, `run_id` 전역 유일성.
- `artifact_class=semantic_read`, `read_method=llm_full_read`, 두 complete 상태.
- source의 SHA-256·bytes·논리 line 수 재계산 및 `sha256==source_sha256`; read range가 1..EOF.
- prompt/manifest 파일의 SHA-256 재계산; chunk range 연속성, chunk hash, byte 재결합이 source와
  동일함을 확인; receipt 전건·순서·마지막 line·EOF·`EMIT_ALLOWED` 발급 시각 확인.
- 모든 `loc`, `line`, page/range 앵커가 범위 안이고 해당 원문에 실제 span/식별자가 존재함을
  확인. complete인데 미판독 range가 있거나 빈 배열로 은폐된 흔적이 있으면 실패.
- semantic draft 동결 후에만 `records-structural/20260724/`와 대조하여 선언/상수/호출/I/O 후보
  누락을 검사한다. 구조 인덱스는 정답이나 content 생성원으로 쓰지 않으며, 차이는 원문으로
  판정한다. validator가 content 최종값을 자동 보충해서는 안 된다.
- 구조 인덱스/기존 레코드 미열람을 실행 allowlist와 접근 로그로 검증한다.
- `audit_seed`, 표본 manifest, `audit_status` 및 auditor 결과의 상호 일치.

### 5.2 shard 판정

shard는 아래가 **모두** 참일 때만 합격한다.

1. 배정 path가 정확히 한 번씩 있고 모든 파일 레코드가 5.1을 통과한다.
2. partial/failed/pending, 구조-only, 방법미상, 금지 필드, 미해결 canonical 중복이 0이다.
3. 그 shard에 고정된 맹검 표본이 최소 1건 있으며 전부 `audit_status=passed`다.
4. 해당되는 의미 canary가 교차라인 관계를 검출한다.

한 건이라도 실패하면 **shard 전체**를 고정 이름으로 canonical 등록하지 않고
`records-rejected/`에 둔다. 합격 행만 떼어내는 부분 승격은 금지한다. 원문 재판독과 새 run으로
shard 전체를 다시 생산·검증하며, 최초에 표본으로 고정된 path는 재시도에서도 계속 감사한다.

### 5.3 모델/전체 완결 게이트

`SPEC.md` v2에 따라 다음이 모두 참일 때만 완결/100%를 표기한다.

1. inventory 분모, provenance와 Merkle root가 고정되어 있다.
2. 고유 `(model,path,sha256)`가 canonical manifest에 정확히 한 번 있다.
3. nonempty 텍스트는 전부 `llm_full_read`; FUNWAVE 0-byte 10건과 진짜 바이너리만 명시적
   mechanical 예외다.
4. structural-only, 방법미상, canonical 중복 선택 미결이 모두 0이다.
5. line/hash/chunk/receipt/anchor/schema 검증이 전건 통과한다.
6. §6의 맹검 층화표본이 무오류로 통과한다. 별도 의미 canary는 최소한
   `EFDC/raw/source_code/EFDC-GVC/svdcmp.for`의 `DO ITS=1,30` 대 `ITS.EQ.60` 도달불가 관계와
   `SWAN/raw/source_code/swan/src/mod_xnl4v5.ftn90`의 BQF write 세 번째 `iq_geom` 대 read
   `iz_cple` 불일치를 독립 판독에서 검출해야 한다. canary 원 레코드는 감사자에게 보이지 않는다.
7. `RESUME.md`, `SESSION-LOG.md`, status report, canonical manifest 네 곳의 분모·완료 수가 같을
   때만 완료 표기를 갱신한다.

이 work order의 레코드 생산 완료는 모델 완결과 같지 않다. 위 일곱 게이트 이전에는 완료를
자기 선언하지 않는다.

## 6. 맹검 감사 seed와 표본

### 6.1 고정값

- seed 문자열: `WO-20260728-reread|blind-audit|v1`
- `audit_seed`: `6465d0b8bd3f7acb9a2a437da66cfb37e1a0f0a8033b44214f49f1907e393ae6`
- 표본 크기: **224건** (`ceil(2,238 × 0.10)`)

표본은 semantic draft와 validator 1차 검사가 끝난 뒤 한 번 고정하며, audit selection manifest의
원바이트 SHA-256을 canonical manifest에 기록한다. 생산자나 감사자가 재추첨할 수 없다.

### 6.2 층화와 선택 알고리즘

층은 다음 네 변수의 교차다.

- model: EFDC / FUNWAVE / LISFLOOD-FP
- axis: code / doc / web / note
- source file size: small=`1..4,096 bytes`, medium=`4,097..65,536`, large=`65,537 이상`
- producer 레코드의 `content.unresolved`: empty=`[]`, nonempty=`1개 이상`

실재하지 않는 교차층은 만들지 않는다. 각 레코드의 순위키는 아래 64자리 hex의 사전식
오름차순이다.

```text
SHA256(audit_seed + "\0" + model + "\0" + axis + "\0" + normalized_path + "\0" + source_sha256)
```

먼저 각 nonempty 층의 최저 순위 1건과 각 shard의 최저 순위 1건을 합집합으로 강제 선택한다.
그 뒤 남은 표본 수를 각 층의 미선택 모집단 크기에 비례해 Hamilton 최대잔여법으로 배분하고,
동률은 `(model,axis,size_band,unresolved_band)`의 UTF-8 byte 오름차순으로 푼다. 각 층에서는 아직
선택되지 않은 순위키가 작은 순으로 채운다. 이 방식으로 모든 실재 층과 50 shard가 최소 1회
감사되며 총수는 정확히 224다.

감사자에게는 선택 path, source hash와 원문 chunk만 준다. 1차 semantic 레코드,
`records-structural/`, 선택에 사용된 unresolved 내용은 주지 않는다. 감사자는 같은 파일별 완료
프로토콜로 독립 레코드를 만든 후 adjudicator가 원문으로 대조한다. 문체 차이는 실패가 아니지만,
원문 역할/알고리즘의 모순, 선언·상수·입력·식·I/O·호출의 누락, 거짓 주장, 잘못된 앵커,
교차라인 의미 결함 누락은 실패다. 허용 오차는 0건이다. 한 표본이라도 실패하면 그 표본이 속한
shard가 불합격하며, 실패를 제거한 재추첨은 금지한다.

## 7. 기존 중복 640행의 canonical 선택

감사 당시 25,157행과 24,517개 `(model, normalized_path)`의 차이인 **640행은 삭제하지 않는다**.
먼저 SHA-256을 포함한 canonical key로 다시 묶는다. 같은 path라도 source SHA-256이 다르면 서로
다른 source version이므로 중복행으로 합치지 않는다. 같은 `(model, normalized_path, sha256)`에
여러 후보가 있을 때 아래 순서로 선택한다.

1. 현재 고정 inventory의 source SHA-256과 일치하지 않는 후보는 그 snapshot의 canonical이 될
   수 없다. 보존은 하되 manifest에서 `inventory_mismatch`로 표시한다.
2. 실제 원문이 nonempty text면 검증된 `semantic_read + llm_full_read`만 eligible이다. 빈 파일·진짜
   바이너리만 검증된 `mechanical_binary + binary_sweep`가 eligible이다. `structural_index`,
   `deterministic_parse`, 방법미상은 canonical 후보가 아니다.
3. eligible 후보끼리는 강한 provenance를 비교한다. source/chunk/prompt hash, 전 chunk receipt,
   구체 producer/model, run ID, 접근 로그, validator 통과가 모두 보존된 v2 후보가 이 증거가
   없거나 불완전한 legacy 후보보다 우선한다. `reader` 문자열이나 최신 timestamp만으로 우선하지
   않는다.
4. provenance가 모두 유효하면 맹검 `passed` 후보가 `not_sampled` 후보보다 우선하고,
   `pending|failed`는 선택하지 않는다. 원문 대조에서 선언·상수·입력·식·I/O·호출을 빠짐없이
   앵커로 뒷받침하고 교차라인 관계를 설명한 독립 판독을 우선한다. 템플릿형 구조 열거,
   TODO grep만의 unresolved, 빈 unresolved 자체는 의미 판독 증거가 아니다.
5. 위 증거가 같은 두 후보가 의미상 동등함을 원문 대조로 확인한 경우에만
   `(record_file UTF-8 bytes, 1-based JSONL line, SHA256(JCS-canonicalized record))`의 사전식
   최소값을 deterministic tie-break로 선택한다. 증거가 같지만 내용이 충돌하면 임의 선택하지
   않고 `selection_status="unresolved"`로 두며 완료 게이트를 실패시킨다.

canonical manifest는 key마다 `selected_record`, 모든 `candidate_records`, 각 후보의
`artifact_class`, `producer`, `read_method`, source/chunk/prompt hash, run ID, validator/audit 결과,
`selected: true|false`, `selection_reason`, `selection_rule_step`을 기록한다. 비선택 후보와 원 JSONL은
삭제·덮어쓰기·행 제거하지 않는다. canonical manifest만 정확히 한 후보를 가리키며, 선택 근거가
없는 key는 미결로 남는다.

## 8. 생산 개시 조건

Claude를 포함한 어느 생산자도 다음이 갖춰지기 전 시작하지 않는다: 입력 해시 일치, 위 알고리즘으로
생성한 50 shard manifest, immutable prompt와 hash, source chunk manifest, 순차 receipt writer,
구조 인덱스가 보이지 않는 1차 판독 실행환경, pending/rejected/canonical 출력 잠금. 이 조건은
생산 편의를 이유로 완화할 수 없다.
