# 전수 판독 기록 규격 (Total Read) — 판단 금지

사용자 지시(2026-07-19): **"판단하지 말고 모든 코드·모든 매뉴얼(pdf·md·웹정보)·크롤링분 싹 다 읽고 읽은 결과를 저장"**

## 절대 규칙
1. **중요도·가치 판정 금지.** `note_worthy`·`core/non-core`·티어 필드를 만들지 않는다.
2. **읽은 것만 기록.** 추측·보간 금지. 못 읽으면 `read_status: failed` + 사유.
3. **원문 위치 필수.** 모든 항목에 라인/페이지 앵커.
4. **요약 금지, 열거 강제.** "주요 서브루틴" 아님 — 선언된 것 **전부**.
5. **빈 배열 = 없음.** 안 읽은 범위는 `read_status: partial` + `read_range` — "안 봄"을 "없음"으로 위장 불가.
6. **PDF 추출 = opendataloader-pdf** (.venv). pdftotext 금지(2026-07-19 사용자 지시). 스캔본은 300dpi 재렌더+tesseract.

## 축 분담 (페르소나)
| 축 | reader | 대상 |
|---|---|---|
| code | **claude** | `models/*/raw/source_code/**` 전 파일 (확장자 무관) |
| doc | **codex** | opendataloader 재추출 PDF 260 + raw 비HTML 문서(tex·doc·txt ~1,600) + `textbook/md` 21 |
| web | **grok** | raw HTML/MD/RST 미러 ~6,232 + `research/` 크롤분 102 |

## 레코드 (JSONL: `records/<axis>-<model|영역>-<shard>.jsonl`, 파일당 1행)
```json
{"axis":"code|doc|web","model":"","path":"","sha256":"","bytes":0,"lines_or_pages":0,
 "read_status":"complete|partial|failed","read_range":"","reader":"","read_at":"",
 "content":{"what_it_is":"","entities":[],"constants":[{"name":"","value":"","line":0}],
  "params_defined":[{"name":"","default":"","range":"","loc":0}],
  "equations":[{"expr":"","ref":"","loc":0}],"io":[],"calls":[],
  "verbatim_spans":[{"text":"","loc":0}],"unresolved":[]}}
```

## 실행
- 샤드 = 30~60파일. `(path,sha256)` 키 — 재개 시 레코드 없는 파일만 재실행.
- 진척 = `레코드 수 / find 전수`. 분모 축소 금지.
- 순서: ShorelineS→SWAN→XBeach 파일럿 → 대형(Delft3D·ROMS) 서브트리 분할.

## 교차 검증 (자기 축 자기 감사 금지)
code(claude 판독)→codex 표본감사 / doc(codex)→grok / web(grok)→claude. 표본 사전 고정(seed 기록), 감사자는 원 레코드 미열람 독립 판독 후 대조.

## 병렬 실행 규칙 (2026-07-19 추가 — 실사고 반영)
1. **스크래치패드 파일명 유일화 필수.** 헬퍼 스크립트는 반드시  식으로 유일하게. 공용 이름(emit.py 등) 사용 시 동시 실행 에이전트가 서로 덮어써 실패(SWASH r000 실사고).
2. **레코드 파일 중복 금지.** 같은 샤드를 재판독할 때는 기존 레코드 파일을 확인하고, 중복 생성 시 어느 것이 canonical 인지 병합 단계에서 판정(현재 code-SWASH-000 vs -r000 동일 40 path 중복 존재).
3. **집계는 고유 path 기준.** 레코드 행수가 아니라 path 유일값으로 진척을 센다.

## 벤더 판정 (2026-07-21, 실측 기반)
- **codex** ✅ 채택 — read_range·라인앵커·해시 전건 정확, 행수 176/176 일치(SWASH 전수 대조)
- **claude** ✅ 채택 — 전건 실측·재검증 보고
- **grok** — 웹축 ✅(read_range 결측 0, entities 중앙값 55) / 코드축 ❌(read_range 전건 결측) → 웹축 전용
- **agy-gemini** ❌ **제외 확정(2026-07-21, 사용자 결정)** — 진단 결과: bytes·행수는 40/40 정확(파일은 실제로 읽음)하나 sha256 40건이 전부 형식만 맞는 창작값. 즉 도구 실행 대신 그럴듯한 출력을 생성. 원 — 1차: sha256 전건 결측 + 허위 complete(index.rst 76행 기록/실측 123행). 2차(경고 명시 후): sha256 40/40 **날조**(실제 파일 해시와 전건 불일치). 두 번 모두 검증 없이 값을 지어냄.

## 스키마 v2 + 완결 게이트 (2026-07-28 사용자 승인 — METHOD-AUDIT-20260724.md §2·§4)

### canonical key
`(model, normalized_path, sha256)` — 절대경로·`models/` 접두 제거 후. path 단독 집계 금지.

### 추가 필수 필드 (신규 레코드부터)
```text
artifact_class: semantic_read | structural_index | mechanical_binary
producer: script:<id> | llm:<vendor/model>     # reader 는 LLM 주체 전용
read_method: llm_full_read | deterministic_parse | binary_sweep
comprehension_status: complete | partial | not_performed | failed
source_sha256, chunk_manifest_sha256, prompt_sha256, run_id
auditor, audit_seed, audit_status
```

### 스크립트 허용/금지
- 허용: inventory·정규화, sha256/bytes/wc 실측, MIME 판별, 무손실 chunk 분할(+line range·sha), 후보 구조 인덱스, LLM 레코드의 앵커·해시·스키마·중복·chunk 검증.
- 금지: semantic `records/` 에 `what_it_is`·`equations`·`unresolved` 최종값 기록, `reader` 에 LLM 이름, `read_status/comprehension_status: complete` 선언. 구조 산출물은 `records-structural/` 전용.

### 역할 배정 (축별 — RESUME 의 일반 벤더 표보다 우선)
| 축 | 1차 판독 | 맹검 감사 |
|---|---|---|
| code | Claude (무손실 chunk 순차 완독) | Codex (원 레코드 미열람 + 앵커 검증) |
| doc | Codex | Grok |
| web | Grok | Claude |

Claude 는 독단으로 완료 선언·대량 편집하지 않는다. Codex 가 shard·필수 필드·완료 게이트·감사 seed 를 먼저 고정하고 그 범위에서만 생산한다.

### 파일별 완료 프로토콜
preflight(sha256+chunk manifest) → LLM 이 전 chunk 순차 완독(chunk별 수신확인, 마지막 chunk 전 레코드 출력 금지) → 구조 인덱스 **미열람** semantic draft → validator 기계검증(+구조 인덱스와 선언누락 대조) → 타 벤더 맹검 표본 → 실패 shard 는 `records-rejected/`, 통과분만 canonical manifest 등록.

### 모델 "완결/100%" 게이트 (전부 참일 때만)
1. inventory 분모·provenance 고정  2. 고유 canonical key 가 manifest 에 정확히 1회
3. 텍스트 전부 `llm_full_read` (빈 파일·진짜 바이너리만 mechanical 예외)
4. 구조-only·방법미상·중복 미결 0  5. line/hash/chunk 검증 전건 통과
6. 맹검 층화표본 통과 + 의미 canary(교차라인 결함) 검출 확인
7. RESUME·SESSION-LOG·status·manifest 4곳 동수일 때만 표기 갱신

### 게이트 3항 예외 확장 — 수치격자 (2026-07-28 사용자 승인)

mechanical 예외에 **수치격자(numeric_grid)** 를 추가한다: `bytes >= 100,000` AND 선두
65,536바이트의 수치문자비율(문자집합 `[0-9]`·공백·`.,+-eE`) `>= 0.95` 인 텍스트 파일
(bathymetry DEM·격자 데이터 등). 판정은 결정론 — 승인 목록
`reread-queue/numeric-grid-exceptions-20260728.txt` (sha256 `c3e33097…5a899`, 355건 = doc축
FUNWAVE 278·LISFLOOD-FP 77) 로 고정. 레코드는 `artifact_class: mechanical_binary`,
`read_method: numeric_grid_sweep`(허용값 추가), `comprehension_status: not_performed` 로
`records/numgrid-<MODEL>-20260728.jsonl` 등록. 완결 게이트 3항의 "빈 파일·진짜 바이너리"에
이 승인 목록이 추가되며, 이에 따라 LLM semantic 재판독 분모는 2,238 → **1,883**
(code 679 · doc 991 · web 145 · note 68)이다.

### 게이트 3항 예외 보완 — 수치벌크 (2026-08-04 사용자 승인)

수치격자 기준(선두 64KB 0.95)이 놓치는 헤더 혼재 대용량 수치 파일 보완:
`logical_lines >= 10,000` AND `axis != code` AND `min(선두 64KB, 중간 64KB) 수치문자비율 >= 0.70`.
승인 목록 `reread-queue/numeric-bulk-exceptions-20260804.txt` (sha256 `939869dd4556da5c…`, 8건),
레코드 `records/numbulk-*.jsonl` (`read_method: numeric_bulk_sweep` 허용값 추가). 단일 판독자
컨텍스트 완독 불가 규모(10만 행급)가 근거이며 code 축은 제외(코드는 크기 무관 판독 대상).
