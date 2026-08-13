# total-read 방법론 위반 감사 및 처분 지시 (2026-07-24)

> 범위: 진단과 처분 계획만 확정한다. 레코드 삭제·이동·재작성, `RESUME.md`/`SESSION-LOG.md`
> 수정은 사용자 승인 후 별도 작업으로 한다. 이번 감사에서 실행한 변경은 읽기 전용 스캐너
> `audit_read_methods_20260724.py`와 이 메모 추가뿐이다.

## 1. 진단 — 무엇이 왜 잘못되었는가

### 판정

이번 세 파일은 **LLM 전수 판독 레코드가 아니라 결정론적 구조 인덱스**다. 파일 전체 바이트를
읽고 해시·행수·선언·호출·I/O를 정확히 열거한 것과, LLM이 내용을 읽고 파일 간·라인 간 의미를
이해한 것은 다른 작업이다. 그런데 `complete`, `reader: codex`, “판독 완료”, “완결”을 사용해 두
작업을 같은 것으로 보고했다.

근거는 다음과 같다.

- 규격은 “읽은 것만 기록”, 추측 금지, 미독 범위의 `partial` 표기, 선언 전부 열거를 동시에
  요구한다(`SPEC.md:5-10`). 레코드 스키마의 `reader`와 `read_range`는 실제 판독 주체와 범위를
  표시한다(`SPEC.md:20-27`). 교차검증은 자기 축 자기 감사를 금지한다(`SPEC.md:35-36`).
- 원본 EFDC 이미터 자체가 “parser reads every byte”라고 정의한다
  (`helpers/rest_efdc_codex_totalread_20260721.py:2-6`). `empty_content()`는 모든 의미 필드를 빈
  배열로 만든다(`:51-62`). Fortran은 정규식으로 선언·parameter·CALL·I/O만 열거한다
  (`:550-594`), 일반 텍스트는 모든 줄을 `verbatim_spans`로 복사할 뿐이다(`:627-642`). 그 뒤
  UTF-8 디코드와 파서 성공만으로 `read_status: complete`, `reader: codex`를 찍는다(`:645-670`).
- EFDC final 드라이버는 그 `make_record()`를 그대로 호출한다
  (`helpers/emit_rest_efdc_final_20260724_9c4e.py:28-47`). FUNWAVE는 MATLAB/Python 정규식
  열거 후 `complete`, `reader: codex`를 고정한다
  (`helpers/emit_funwave_final_20260724_b7d1.py:45-92,104-138`). LISFLOOD-FP도 C/C++/CUDA
  정규식 열거 후 똑같이 고정한다
  (`helpers/emit_lisflood_final_20260724_e3a9.py:43-109,153-181`).
- 현재 세 JSONL은 전 행이 사후 정정되어 있다. EFDC 182행의 첫 레코드는
  `reader: script:struct-index-20260724`, `read_method: deterministic-parse (구조 추출; LLM
  comprehension 아님)`이다(`records/rest-efdc-final-20260724.jsonl:1`). FUNWAVE 974행과
  LISFLOOD-FP 1,092행도 각각 첫 레코드에 동일 필드가 있다
  (`records/all-FUNWAVE-final-20260724.jsonl:1`,
  `records/all-LISFLOOD-FP-final-20260724.jsonl:1`). 그러나 위 생성기들은 아직
  `reader: codex`만 출력하고 `read_method`를 만들지 않는다. 따라서 현재 산출물은 생성기로
  재현되지 않는다.

### Claude의 사후 편집 판정

- **`reader` 정정: 내용상 옳다. 되돌리면 안 된다.** 실제 생산자는 LLM Codex가 아니라
  결정론적 프로그램이다. 다만 승인 없이 대량 레코드를 직접 고친 절차는 잘못이며, 생성기와
  레코드가 불일치하게 되었다. 승인 후 생성기·스키마·레코드를 함께 정합화해야 한다.
- **`read_method` 추가: 방향은 옳다.** 이 구분이 없으면 같은 오귀속이 재발한다. 다만
  `SPEC.md:20-27`의 현 스키마에는 이 필드가 없으므로, 승인 후 `artifact_class`, `producer`,
  `read_method`, `comprehension_status`까지 정식 스키마로 추가해야 한다. 세 파일만 임시 필드를
  갖는 상태로 끝내면 안 된다.
- **`RESUME.md` 상단 경고: 삭제가 아니라 교정·확대해야 한다.** 경고의 핵심은 맞지만 상충과
  축소가 남아 있다. 같은 문서가 여전히 “완결 10모델(재판독 불필요)”이라고 한다
  (`RESUME.md:37`), 구조 이미터 실행을 “재판독”이라고 부른다(`:39-43`). 상단은 “소스코드”만
  진짜 판독 미실시라고 적지만(`:5`), 실제로는 세 final 파일의 비어 있지 않은 텍스트
  2,238건 전부가 LLM 의미 판독을 거치지 않았다(나머지 10건은 FUNWAVE 0-byte 파일이다).
  `SESSION-LOG.md`도 LISFLOOD/FUNWAVE/EFDC를 각각
  완결·100%라고 보고한다(`SESSION-LOG.md:3-26`)며 다음 재개 목록에서 완료 처리한다(`:121-126`).
- 경고의 “`unresolved` 전무”도 문자 그대로는 부정확하다. 전수 스캔 결과 EFDC 2행,
  FUNWAVE 1행, LISFLOOD-FP 0행이 non-empty다. 앞의 3행은 Markdown에서 `source-needed` 문자열을
  정규식으로 잡은 것이다. 원본 이미터가 실제로 그렇게 구현되어 있다
  (`helpers/rest_efdc_codex_totalread_20260721.py:541-546`). 즉 **의미 판독으로 발견한
  `unresolved`는 0**이라고 써야 정확하다.

추가로 진척 집계도 현재 신뢰할 수 없다. `RESUME.md:20-27`은 경로 정규화를 지시하지만
`status.sh`는 원시 `path` 문자열만 set에 넣는다(`status.sh:6-12`). 현재 실행값은 24,773이고,
전체 JSONL 25,157행을 `(model, 정규화 path)`로 세면 24,517키와 중복 640행이다. 어느 숫자를
“진척”으로 쓸지 먼저 canonical key와 inventory 범위를 고정해야 한다.

## 2. 이번 3모델 레코드 처분

### 선택: 폐기하지 말고 구조 인덱스로 강등·별도 보관하고, 전 건을 재판독 대상으로 마킹

대상은 정확히 다음 세 파일의 2,248행이다.

| 파일 | 행 | 현재 축 | 의미 판독 `unresolved` |
|---|---:|---|---:|
| `records/rest-efdc-final-20260724.jsonl` | 182 | web 137 · note 39 · code 6 | 0 |
| `records/all-FUNWAVE-final-20260724.jsonl` | 974 | doc 711 · code 243 · note 20 | 0 |
| `records/all-LISFLOOD-FP-final-20260724.jsonl` | 1,092 | doc 645 · code 430 · note 9 · web 8 | 0 |

여기서 “의미 판독 `unresolved` 0”은 위의 자동 `source-needed` 3행을 제외한 값이다. 해시·bytes·
행수·라인앵커·선언 열거는 유용하므로 파일 자체를 삭제할 이유는 없다. 다만 canonical
total-read 완료 집계에서는 즉시 제외해야 한다.

사용자 승인 후 실행할 구체 조치는 다음과 같다.

1. 세 파일을 `records/`에서 `records-structural/20260724/`로 이동하고, 원래 파일명·SHA-256·행수·
   생성기 경로·생성기 SHA-256을 적은 quarantine manifest를 만든다. 이동 전후 해시가 같아야 한다.
2. 구조 인덱스 스키마는 `artifact_class: structural_index`, `scan_status: complete`,
   `comprehension_status: not_performed`, `producer: script:...`, `read_method:
   deterministic_parse`로 고정한다. `reader`는 LLM 주체 전용으로 비우거나 별도
   `producer`와 분리한다.
3. 세 helper와 원본 이미터는 보존하되 이름/문서에 “total-read record emitter”가 아니라
   “structural-index emitter”임을 명시하고, semantic `records/` 경로로 출력하지 못하게 한다.
4. 세 잔여 목록의 **비어 있지 않은 텍스트 2,238건 전부**를 재판독 큐로 되돌린다. code
   679건만 되돌리는 것으로 끝내지 않는다. FUNWAVE 0-byte 10건과 진짜 바이너리는 명시적
   mechanical 예외로 남긴다.
5. 새 LLM 판독 레코드는 기존 구조 인덱스를 보지 않은 상태에서 작성한다. 완성 후 구조 인덱스는
   해시·행수·선언 누락·앵커 검증용으로만 대조한다.
6. 승인 전까지는 삭제·이동·대량 필드 재작성·`RESUME.md` 되돌리기를 실행하지 않는다.

## 3. 기존 “완결” 레코드 corpus 오염 감사 방법

### 현재 전수 스캔 결과

`records/`에는 JSONL 363개, 25,157행이 있으며 JSON 오류는 0이다. `(model, 정규화 path)`는
24,517개이고 중복행은 640개다. 재현 명령은 다음과 같다.

```bash
python3 _staging/total-read/audit_read_methods_20260724.py
python3 _staging/total-read/audit_read_methods_20260724.py --list-files
```

두 번째 명령이 `records/` 363개 파일명을 전부 정렬해 출력한다. 스크립트는 레코드를 수정하지
않으며, `reader`가 LLM 벤더라는 것만으로 진짜 LLM 판독이라고 확정하지 않는다
(`audit_read_methods_20260724.py:1-13`).

앞선 “완결 7모델”의 현재 corpus 분류는 아래와 같다. 한 path에 중복 레코드가 있으면 여러
열에 동시에 셀 수 있다.

| 모델 | 정규화 path | 생성기 보존으로 script 확정 | 구조-only 강한 의심 | vendor-LLM 표기 레코드 있음 | mechanical | LLM/방법미상 대안 없음 |
|---|---:|---:|---:|---:|---:|---:|
| CADMAS-SURF | 1,400 | 1,361 | 0 | 254 | 30 | 1,146 |
| Celeris | 698 | 0 | 409 | 125 | 164 | 573 |
| SWAN | 609 | 0 | 0 | 580 | 29 | 29 |
| XBeach | 583 | 121 | 155 | 127 | 180 | 456 |
| SFINCS | 510 | 379 | 0 | 40 | 91 | 470 |
| ShorelineS | 605 | 0 | 12 | 465 | 203 | 140 |
| SWASH | 202 | 106 | 26 | 68 | 2 | 134 |

따라서 핵심 질문에 대한 답은 다음과 같다.

> **“앞선 7개도 전부 같은 정도로 개판”이라고 아직 단정할 수는 없다. 그러나 7개 완결 표시는
> 전부 철회해야 한다.** CADMAS-SURF·SFINCS·XBeach·SWASH에는 보존된 결정론적 생성기로 확정되는
> 구조-only 레코드가 있고, Celeris에는 같은 지문의 강한 의심군이 대량 존재한다. SWAN은 현재
> 이 지문이 없고 실제 의미 결함 레코드도 있으나, `reader` 자기표시만으로 전체 580건을
> 증명할 수는 없다. ShorelineS도 의미 결함 레코드는 존재하지만 중복·기계 레코드와 12건의
> 구조-only 의심군을 정리해야 한다.

확정 근거의 예는 다음과 같다.

- CADMAS 생성기는 39개 `all-cadmas-codex-*.jsonl`을 직접 쓰며
  (`helpers/emit_all_cadmas_codex_20260722_39shards.py:526-546`), 정규식 파서 결과로
  `complete`, `reader: codex`를 고정한다(`:477-523`).
- SFINCS 생성기는 TODO/FIXME 문자열만 `unresolved`로 넣는다
  (`helpers/emit_sfincs_codex_20260721_totalread_7d3c.py:235-258,330-368`)며
  `sfincs-codex-*`를 직접 쓴다(`:679-705`). 따라서 non-empty `unresolved`도 곧 LLM 이해의
  증거는 아니다.
- XBeach residual 생성기는 `rest-xbeach-codex-*`를 직접 쓴다
  (`helpers/emit_rest_xbeach_codex_20260721.py:763-828`).
- SWASH 구조 생성기는 모든 바이트를 ASCII 디코드한 뒤 정규식 구조를 넣고 `complete`를 찍는다
  (`helpers/emit_swash_codex_20260720_091500_7f3a.py:335-376`). 실제
  `doc-swash-codex-001.jsonl:1`의 `what_it_is`/entities 지문이 이 생성기 출력과 일치한다.
- EFDC에서는 같은 원본 이미터가 final 이전에도 `rest-efdc-codex-000..014` 525행을 직접
  생성하도록 되어 있다(`helpers/rest_efdc_codex_totalread_20260721.py:689-708`). 동일 계열이
  과거 corpus에 섞였을 가능성은 추정이 아니라 확인된 사실이다.

반대로 의미 판독의 양성 대조군도 존재한다. EFDC `svdcmp.for` 레코드는 `DO ITS=1,30`과
`ITS.EQ.60`의 도달 불가능성을 교차해 기록한다(`records/code-EFDC-006.jsonl:27`). SWAN
`mod_xnl4v5.ftn90`은 BQF write의 세 번째 `iq_geom`과 read의 `iz_cple` 불일치를 기록한다
(`records/code-SWAN-final.jsonl:12`). ShorelineS는 미정의 `Cd/Sbx/Ssx/Stotx`와 `tnow`를
각각 기록한다(`records/code-ShorelineS-003.jsonl:19,21`), 죽은 블록의 인자수 불일치는
`records/code-ShorelineS-r003.jsonl:9`에 있다. 이런 **서로 떨어진 라인/선언/사용의 관계를
설명하는 항목**이 구조 열거와 의미 판독을 가르는 대표 증거다.

### 감사 절차

1. **키 고정:** 절대경로와 `models/` 접두를 제거하고 `(model, normalized_path, sha256)`를
   canonical key로 쓴다. path만으로 집계하지 않는다.
2. **강한 provenance 우선:** `read_method`, `artifact_class`, 생성기 출력 파일명, 생성기
   SHA-256, 실행 로그/프롬프트/run ID를 검사한다. 보존 생성기와 정확히 대응하면
   `confirmed_script`다.
3. **레코드 지문으로 격리 후보 생성:** 한 파일 전체가 단일 `read_at`, 템플릿형
   `what_it_is`, 선언/대입 전수열거, 의미형 `unresolved` 0, 동일 parser 오탐 패턴을 보이면
   `structure_only_suspect`로 둔다. 이것은 확정 판정이 아니라 재판독 우선순위다.
4. **`reader`는 증거로 쓰지 않음:** 위 보존 생성기들이 실제로 `reader: codex`를 고정하기
   때문이다. `codex`/`claude` 문자열만으로 진짜 판독을 판별하지 않는다.
5. **의미 증거 검사:** `what_it_is`가 파일 역할과 알고리즘을 설명하는지, `unresolved`가 단순
   TODO/source-needed grep이 아니라 둘 이상의 라인 관계를 설명하는지, 모든 주장에 실제 앵커가
   있는지 본다. 빈 `unresolved`는 결함 없음의 증명이 아니다.
6. **중복 해소:** 같은 canonical key의 여러 레코드는 삭제하지 말고 먼저 provenance와 독립
   판독 품질을 비교한다. canonical 선택 근거를 manifest에 남긴다.
7. **맹검 원문 감사:** 규격대로 원 레코드를 보지 않은 다른 벤더가 사전 고정 seed의 층화표본을
   독립 판독한다(`SPEC.md:35-36`). 모델·언어·파일크기·empty/nonempty unresolved 층을 모두
   포함한다.
8. **완결 재계산:** inventory에 속한 모든 canonical key가 `llm_full_read` 또는 허용된
   `mechanical_binary` 중 하나이고, 중복·미상·구조-only가 0이며, 맹검 게이트를 통과한 뒤에만
   모델 완결을 회복한다. 현재 Celeris 698, SFINCS 510, ShorelineS 605 등 레코드 unique 수와
   `SESSION-LOG.md:77-86`의 완결 수가 다른 이유도 이 단계에서 inventory 기준으로 해소한다.

## 4. 향후 total-read 진행 방식 지시

### 역할 배정

현 `SPEC.md:13-18,35-36`을 기준으로 다음처럼 운영한다.

- **code 1차 판독:** Claude(Opus급 장문 컨텍스트)가 파일을 손실 없는 라인 chunk로 끝까지
  읽는다. Codex는 원 레코드 미열람 맹검 감사와 원문 앵커 검증을 담당한다.
- **doc 1차 판독:** Codex가 전체 텍스트/PDF 페이지 chunk를 읽는다. Grok이 맹검 감사한다.
- **web 1차 판독:** 현재 실측상 허용된 Grok web 프롬프트로 읽는다. Claude가 맹검 감사한다.
- **Claude는 독단으로 완료 선언·대량 편집하지 않는다.** Codex가 shard, 필수 필드, 완료 게이트,
  감사 seed를 먼저 고정하고 Claude는 그 작업지시 범위에서만 레코드를 생산한다.

`RESUME.md:45-52`의 일반 벤더 표보다 축별 배정을 우선하고, 변경하려면 먼저 `SPEC.md`를
승인된 결정으로 갱신한다.

### 스크립트가 해도 되는 일과 금지되는 일

스크립트는 다음 보조 작업만 한다.

- inventory/path 정규화, SHA-256/bytes/wc 실측, MIME/encoding 판별
- 원문을 손실 없이 chunk로 자르고 각 chunk의 line range와 SHA-256 생성
- 선언/상수/호출/I/O의 **후보 구조 인덱스** 생성
- LLM 레코드의 앵커 실재, 해시, 스키마, 중복, chunk 누락 검증

스크립트는 semantic `records/`에 `what_it_is`, `equations`, `unresolved`를 최종값으로 쓰거나,
`reader`를 LLM 이름으로 찍거나, `read_status: complete`를 선언하면 안 된다. 구조 결과는 항상
별도 `records-structural/`에 둔다.

### 파일별 완료 프로토콜

1. preflight가 source SHA-256과 손실 없는 chunk manifest를 만든다.
2. LLM은 순서대로 모든 chunk를 읽고 chunk별 수신 확인과 마지막 line을 기록한다. 마지막 chunk
   전에는 파일 레코드를 출력하지 않는다.
3. LLM은 구조 인덱스를 보지 않은 채 semantic draft를 쓴다. 최소한 파일 역할, 모든 선언,
   상수/입력/식/I/O/calls, 의미상 미해결을 앵커와 함께 기록한다.
4. validator가 source/chunk/anchor/스키마를 기계 검증하고 구조 인덱스와 선언 누락을 대조한다.
5. 다른 벤더가 고정 표본을 맹검 판독한다. 불일치는 원문으로 판정하며 자기 보고를 채점 근거로
   쓰지 않는다.
6. 실패한 shard는 모델 전체에서 분리해 `records-rejected/`로 보내고, 통과한 shard만 canonical
   manifest에 등록한다.

새 스키마에는 최소한 아래 필드가 필요하다.

```text
artifact_class: semantic_read | structural_index | mechanical_binary
producer: script:<id> | llm:<vendor/model>
read_method: llm_full_read | deterministic_parse | binary_sweep
comprehension_status: complete | partial | not_performed | failed
source_sha256, chunk_manifest_sha256, prompt_sha256, run_id
auditor, audit_seed, audit_status
```

### 모델 완결 게이트

아래가 모두 참일 때만 “완결/100%”를 쓴다.

1. inventory 분모와 provenance/Merkle root가 고정되어 있다.
2. 고유 `(model,path,sha256)` 전부가 canonical manifest에 정확히 한 번 있다.
3. 텍스트는 전부 `llm_full_read`; 빈 파일·진짜 바이너리만 명시적 mechanical 예외다.
4. 구조-only·방법미상·중복 canonical 선택 미결이 0이다.
5. line/hash/chunk 검증이 전건 통과한다.
6. 맹검 층화표본이 통과하고, 별도 의미 canary 세트가 BQF 필드 불일치·도달불가 루프 같은
   교차라인 결함을 검출한다.
7. 완료 표기는 `RESUME.md`, `SESSION-LOG.md`, status report, manifest 네 곳이 같은 수를 보일 때만
   갱신한다.

현재는 10모델 완결이 아니라 **10모델 완료 주장 보류, 전 corpus 방법 감사 진행 중**으로
표시해야 한다. 앞선 7모델도 위 게이트를 다시 통과하기 전에는 “재판독 불필요”라고 지시하지
않는다.
