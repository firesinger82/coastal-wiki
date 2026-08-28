# SPEC.md 완결게이트 amendment 초안 v2 — supplement 수용 (2026-08-27)

> Codex 적대검증 REJECT(10 findings) 반영 개정. santa-method: 이 v2 → Codex 재검증 → 사용자 승인 → SPEC.md 적용.
> 목적: MERGE-PLAN §3-4 canonical supplement 를 완결게이트가 **좁게** 수용. canonical selected_record 는 base 불변.
> 원칙 요약: supplement 는 (1) 새 canonical key 를 만들지 않고 (2) 완결/100% 판정에 필요·충분조건이 아니며 (3) 기계검증 + **사람 승인(decision.json)** 이중 게이트를 통과해야 canonical 유효.

## 변경 1 — §80 item 2 (finding 10)
기존: `2. 고유 canonical key 가 manifest 에 정확히 1회`
개정:
> 2. 고유 canonical key 가 canonical manifest 에 정확히 1회 — 각 key 는 **selected_record 정확히 1개**(1차 판독, base). key 는 선택적으로 hash-고정 `supplements[]`(감사 confirmed_delta, §80.S)를 참조할 수 있으나 **별도 canonical key·별도 selected_record 를 만들지 않는다**. supplement 는 완결/100% 판정의 필요조건도 충분조건도 아니며, **게이트 1-7(§6 맹검 감사 포함)은 그대로 필수**다.

## 변경 2 — 신규 §80.S "canonical supplement (감사 delta 승격)"
```
### canonical supplement — MERGE-PLAN §3-4, Codex-hardened

crosswalk 에서 confirmed_delta 로 판정되고 원문 span 재확인 + 사람 승인을 통과한 감사(2차)
finding 만 canonical 을 보강한다. selected_record 는 변경하지 않는다.

레이어:
- selected_record: canonical key 의 1차(base) 레코드. 불변. supplement manifest 는 이를
  **복제하지 않고 crosswalk(path+bytes-hash) 로 핀 고정 참조**하며, 그 record.source_sha256
  == canonical_key.source_sha256 을 검증기가 확인한다(제2 selector 금지, finding 7).
- supplement: (source_sha256, audit_id) 로 키잉된 감사 delta. `supplement-manifest.json`
  (supplement-manifest/v2). 필드는 SUPPLEMENT-SCHEMA.md. 다중 증거는 `evidence_sources[]`
  ·`source_span`(각 사실 전제마다 span, finding 5). doc-vs-code delta 는 evidence 경로가
  canonical 파일과 다를 수 있고, 각 evidence 소스는 개별 sha 로 고정한다(finding 2).

기계 게이트(verify_supplement.py, 저장필드 신뢰 금지 — 전부 소스 재도출):
M1 selected_record·감사 레코드 bytes 해시 재계산 == 저장.
M2 각 레코드의 source_sha256(파싱) == canonical_key.source_sha256.
M3 crosswalk bytes 해시 재계산 == 저장; 해당 crosswalk 에 동일 audit_id confirmed_delta 처분 존재;
   crosswalk.source_sha256 == key.
M4 audit_id 인덱스 in-range AND finding_text == 감사레코드 unresolved[idx] (문자열 실재 증명).
M5 evidence 소스 exact-path 해석(basename fallback 금지); sha 재계산 == 저장; evidence==canonical 경로면 sha==key.
M6 span 범위 1<=a<=b<=nlines; quote 재추출 == 저장; source_span_hash==sha256(quote); 빈 quote 금지.
M7 canonical key 유일; (source_sha256,audit_id) 전역 유일; member_input_ids 비어있지 않음.

사람 게이트(decision.json, finding 4 — 자기신고 완결권한 금지, 작업규범 #4):
H1 `supplement-decisions.json` 에 (canonical_source_sha256, audit_id) 승인 receipt 존재,
   `crosswalk_sha256_bytes`·`source_span_hash` 바인딩 일치, status==approved,
   approver 는 사람(모델 identity `llm:*`·claude/gpt/codex/grok/gemini 거부) 이며 producer 와 분리.
   receipt 는 **의미-함의 판정**(quote 가 finding_text 를 실제로 뒷받침하는가)을 사람이 확정하는 지점 —
   기계 M6 의 바이트 일치와 구분(finding 5).

무효화·수명(finding 8):
- 바인딩된 어느 해시(crosswalk·레코드·evidence 소스)라도 바뀌면 supplement 무효 → **재판정+재승인** 필요
  (자동 재빌드로 통과 금지). 소스가 정당히 수정되면 옛 라인 재추출로 통과할 수 없다(sha 불일치로 차단).
- verify_supplement.py 는 canonical status·release 게이트마다 실행한다.

경계:
- supplement 는 canonical key·selected_record 를 추가하지 않는다(§80 item2 불변).
- 미확정 HIGH(distinct_unconfirmed)·기각·MED 는 supplement 아님(오버레이/큐 전용).
- .m/.py 후처리 스크립트 delta 는 범위밖(절대규칙 #8).
```

## 변경 3 — §80 item 7 (finding 1·10)
canonical manifest 갱신 시 supplement-manifest.json 도 함께 스냅샷하되, **verify_supplement.py 가
canonical manifest/inventory 를 입력으로 받아 supplement 의 key·selected_record 가 완결게이트
모집단과 정확히 조인됨을 확인한 PASS** 를 전제로 한다(현 구현은 crosswalk 를 authority 로 바인딩;
정식 canonical manifest 도입 시 그 조인을 추가). supplement count 는 7개 완결조건 어디에도 계입되지 않는다.

## 근거
- 오버레이+delta(MERGE-PLAN, 전량 union 폐기): precision 우선, 소비자 "2벤더 검증" 오인 차단.
- 작업규범 #4: 완결게이트=자기신고 대체 아님. supplement 도 사람 receipt 필수(resume-gate decision.json 형식 준용).
- SSOT: canonical 진실원=1차 base 단일 selector; 감사는 hash-핀 보강 레이어(제2 selector 금지).

## 잔여 한계 (Codex 2라운드 후 정직 공시)
- **finding 1 (canonical population join) — 부분/이연**: reread-20260728 코퍼스에는 아직 단일 canonical
  manifest 파일이 없다(전수판독 진행 중). 현 검증기는 **crosswalk 를 authority 로** 바인딩하고
  selected_record 가 그 crosswalk 의 base(run_id·record_file·hash)와 정확히 일치함을 확인한다. 정식
  canonical manifest 도입 시 그 모집단 조인을 검증기에 추가한다(그 전까지 supplement 는 완결표기 근거 아님).
- **finding 4 (외부성) — 실현가능 최대**: `--allow-pending` 우회 제거(pending 은 항상 FAIL), approver 는
  사람(모델 identity 거부)·producer 분리·receipt 를 crosswalk/span/audit-record/evidence 해시에 바인딩.
  단 "approver 가 사람"은 궁극적으로 **사용자가 decisions 파일을 직접 작성**함으로써 보장된다(서명 PKI 는 범위밖).
  producer(Claude)는 approved receipt 를 작성하지 않는다.
- **finding 5 (다전제 함의) — 사람 게이트 소관**: 기계 검증은 인용 span 바이트 일치까지만. 인용이 finding 을
  실제로 뒷받침하는지(예 note-000 은 io.F 파서키가 근거이나 매뉴얼 L223/250 불일치는 사람이 대조,
  EtaBlowVal 은 io.f90 use 와 mod_global 선언을 함께 판단)는 **승인자(사람)의 함의 판정**에 위임한다.

## 현재 자산 (적용 시)
supplement-manifest/v2: 16 entries·23 supplements. verify_supplement.py: mechanical PASS,
사람 승인 0/23(전부 pending — supplement-decisions.json). tamper 7종(crosswalk-hash·finding-text·
evidence-sha·OOB-span·producer-self-approve·receipt-hash·pending) 전건 차단 확인.
```
