# supplement 게이트 — Codex 적대검증 경위 (santa-method, 2026-08-27~28)

> amendment(SPEC.md §80 item2 보강 + canonical supplement) + verifier/builder 를 Codex 로 4라운드
> 적대검증. clean ACCEPT 는 R4 에서 Codex 자체 사이버-안전 필터 트립으로 미도달(코드 결함 아님).
> 사용자 결정(2026-08-28): 4라운드 하드닝된 v4 를 트리 커밋 + amendment 적용.

## 라운드 요약
- **R1 REJECT (10 findings)**: verifier 가 canonical manifest·감사레코드·crosswalk·human 게이트에 미바인딩.
- **R2 REJECT**: F2·9·10 resolved. 신규 blocking 4(audit-ID alias·모순 disposition·중복 receipt·builder
  problem 시 write). F4(human gate) OPEN — `--allow-pending` 우회·approver 문자열 위조.
- **R3 REJECT (실행 기반)**: Codex 가 verifier 를 실제 실행해 우회 5건 재현 —
  ①감사레코드 치환 ②canonical key 재라벨 ③crosswalk `B01` alias 모순우회 ④approver `LLM`·키릴 homoglyph
  ⑤confirmed_delta 누락. `cwroot` 인자 미사용 지적.
- **R4 미완(필터 트립)**: 트립 전 R3 우회 6건 전부 exit 1 **폐쇄 재확인**·builder 정상. 신규 후보 1건
  (canonical_key dedup 삽입순서 의존) 제기 후 Codex 필터로 턴 실패.

## v4 에서 폐쇄한 것 (R1-R4 전 발견 항목)
- 감사레코드/ selected_record/ canonical model·path 를 crosswalk 에 핀 고정(치환·재라벨 차단).
- crosswalk 를 delta authority 로 전량 열거 → manifest exact+complete(누락·초과 0). `cwroot` 사용.
- 전 crosswalk audit_id 문법검사(B01/X1 거부)·모순 disposition 거부.
- approver is_human(): ASCII-only(homoglyph 차단)+모델 denylist(`LLM` 등)+producer 분리.
- `--allow-pending` 제거(pending 항상 FAIL, 우회 없음); receipt 4-해시 바인딩+approved_at 필수.
- evidence/records realpath containment(abs·`..` 이탈 거부); schema/corpus/decision_count 강제.
- builder: containment+crosswalk 검증, problem 시 nonzero·미기록. dedup 삽입순서 버그 수정.

## tamper 스위트 (v4, 전건 차단 확인)
canonical-relabel · audit-record-subst · delta-omission · LLM/homoglyph approver · B01-alias ·
exact-contradiction · cwroot-wrong · dup-receipt · pending(무우회) · 4-hash-binding 각각 · empty-manifest ·
abs/`..`-escape · insertion-order dup-key → 전부 FAIL. baseline human-approved → PASS.

## 잔여 (공시)
- **F1 canonical 모집단 조인**: reread 코퍼스에 단일 canonical manifest 파일 없음 → crosswalk authority 로
  바인딩. 정식 manifest 도입 시 조인 추가. (그 전까지 supplement 는 완결표기 근거 아님.)
- **F4 사람성**: 서명 PKI 는 범위밖 — 사용자가 decisions 파일을 **직접 작성**함으로써 externality 보장.
  producer 자기승인 불가(코드가 모델 approver 거부).
- **F5 의미 함의**: 기계는 인용 바이트 일치까지. 인용이 finding 을 실제 뒷받침하는지는 승인자(사람) 판정.
- **TOCTOU**: 해시-후-재읽기 창(read-only 트리 전제, static-only 한계로 수용).

## Codex 세션
R1 (task a3eac97) · R2 (b8k1yyz) · R3 (task-mtb9hkux, 13m36s) · R4 (task-mtc6rrgu, 필터 트립 5m34s).
