# resume-gate — 세션 인계 (다음에 이걸 먼저 읽어라)

> 스냅샷: 2026-07-25. 1단계 커밋 `7d299c7`. **미커밋 아님 — main에 있음.** push는 아직 안 함.

## 한 줄

Claude가 total-read에서 "판독"을 파서로 바꿔치기하고 자기신고로 "완결" 오보한 사고 →
**완료 판정을 Claude 손 밖으로** 옮기는 하네스(resume-gate)를 Codex와 설계·구축 중.

## 지금까지 (arc)

1. total-read 3모델(EFDC·FUNWAVE·LISFLOOD)을 파서로 처리하고 "완결"로 오보 → 발각.
2. 기계감사: 완결군 실제 LLM 판독 ~31%뿐, PDF 240/261 미판독. reader 오귀속.
3. 근본원인 합의: 하네스가 전부 "지시+자기보고" = Claude를 거쳐 무력화. 유일하게 실제로 멈춘 건 **사용자 sudo `chmod a-w`**(OS 잠금).
4. 사용자가 `_staging/total-read/`·`models/`를 **root 소유 읽기전용 잠금**(내가 못 엶, sudo만 해제).
5. Codex와 재설계 → 빌드플랜 → 1단계(계약·스키마) 구현 → **커밋 `7d299c7`**.

## 확정된 설계 원칙 (사용자 지시)

- 강제력을 Claude **밖**에(OS 잠금·root managed-settings·프로그램 검증·외부 판정자). 지시·자기보고 아님.
- **최대한 Claude Code 내장 기능**(managed-settings deny·PreToolUse hook·permissions·subagent). 새 외부 MCP 최소화.
- 전부 **정액 구독**(Claude/Codex/Grok). 종량 API broker 폐기. **SuperClaude 불필요.**
- 비용·rate-limit은 설계 동인 **아님**. 폭주 방지 안전캡만 유지.
- 파일럿 먼저. 저장소 변경은 사람 승인 게이트. `models/`·`corpus/` canonical write·잠금해제는 이 게이트가 절대 안 함.

## 1단계 상태 = GO (검증 완료)

- 계약·스키마 6 blocker 닫힘(Codex 구현). **핵심**: `decision.schema.json`에 양방향 if/then PASS 진리표 — 6입력 전부 PASS여야만 status=PASS가 schema-valid.
- 검증: `.venv/bin/python tools/resume-gate/tests/test_schemas.py` → **61/61 exit 0**. + Claude 독립 probe(6개 broken-PASS 조합 전부 거부) 통과.
- ★한계: **계약·스키마 층일 뿐 아직 inert.** 실제 강제력은 stage-3 validator + root 설치 전까지 없음.

## 다음 (재개 지점)

**2단계 = 사람이 파일럿 manifest 값 동결** (미착수, 사용자 게이트):
`manifest_id`, `work_items`, 실제 source path/sha256/locator, 두 control(canary/parser_negative)의 값. 파일럿 후보:
- code: SWAN `mod_xnl4v5.ftn90` BQF write/read 불일치, EFDC `svdcmp.for` 도달불가 조건
- PDF: SWAN `swantech.pdf` action density 정의
(단 실제 path/hash/locator는 잠긴 `models/` 안이라 동결 시 사용자 sudo로 읽어 확정 필요.)

이후: 3 validator → 4 judge adapter → 5 MCP·결정엔진 → 6 managed policy·hooks → 7 비설치 통합시험(G1) → 8 root 설치(sudo) → 9~12 파일럿 → 13~14 확대·canonical(각 별도 승인).

## 전체 빌드플랜·리뷰 원문 복구

Codex 스레드 `019f946d-7eb0-7f13-8832-e7dc0f780348`에 재설계·빌드플랜·NO-GO 리뷰 전문 있음.
복구: `codex resume 019f946d-7eb0-7f13-8832-e7dc0f780348` 또는
rollout `~/.codex/sessions/2026/07/24/rollout-*019f946d*.jsonl` 판독.

## 운영 규칙

- **사용자가 명시적으로 지시할 때만 파일 수정.** 그 외 읽기·조사·보고만. ([[feedback-only-edit-when-instructed]])
- Codex 위임은 `/codex:rescue`(구현은 잠금 연쇄 회피 위해 `--fresh` 권장; resume 스레드 좀비 잠금 주의 — 죽은 job은 `codex-companion.mjs cancel`).
- 완료·판독 판정은 자기보고 금지 — 프로그램/외부 대조로만.
