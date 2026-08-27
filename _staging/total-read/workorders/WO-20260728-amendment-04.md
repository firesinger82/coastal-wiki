# WO-20260728 부속서 04 — 맹검 감사 전수 census + 병합(union) 처분 설계 (2026-08-27)

## 1. 완료된 것 — code+note 269 전수 교차판독
- 감사자: Codex `openai/gpt-5.6-sol` (rollout 실측, 자기신고 금지 가드 적용).
- 방식: 게이트 재사용, 1차 레코드 **미열람** 맹검. 감사 run 은 별도 run_id(`*-codexaudit-*`),
  1차(`*-fable5-*`)와 물리 분리. 표본 아닌 **전수 269**(사용자 결정, WO §6 10% 상회 = 강화).
- 표본 manifest: `audit-selection-census-20260826.json` (sha 5104049d, seed 6465d0b8).
- selector: `audit_select_20260826.py` (§6.2 층화, 전수 모드). 판정 보조: `adjudicate_20260826.py`.
- 스트림 유지: `audit_maintain.sh` (30분 크론, FW004 롱테일은 004a/b/c 3분할 병렬로 가속).
- run 레지스트리: `audit-run-registry/`.

## 2. 판정 기준 (보정, 2026-08-26 사용자 승인)
- **material 정합성 결함**(use-before-assign·인터페이스 불일치·범위초과·특이점검사 무력화·복붙오류)만
  shard 불합격 사유. 경미·문체·사장코드·문서 nit 은 보강노트.
- 확정 clean miss(소스 검증): **EFDC aaefdc.f90 DETTMP 특이점검사 무력화**(역수 후 ==0 비교) — Claude 1차 누락.
- 나머지 shard: Codex material 후보 다수(shard당 Fortran ~30건)이나 **대부분 Claude 1차와 겹침**
  (Claude 판독이 강함). 겹치지 않는 신규 후보는 `AUDIT-DISPOSITIONS-20260826.md` 에 shard별 기록.

## 3. 처분 = 병합(union) (2026-08-27 사용자 결정)
canonical 승격 시 unresolved(및 관련 findings)를 **Claude 1차 ∪ Codex 감사**의 합집합으로 구성한다.
재판독 아님(Codex 가 이미 gap 을 채웠으므로 낭비). Codex 감사 레코드는 별도 감사 층으로 보존.

### 병합 절차 (별도 전용 패스 — 미실행)
1. 파일별로 1차 unresolved + 감사 unresolved 를 모은다.
2. **의미 중복 제거**: 같은 결함을 두 벤더가 다른 문장으로 적은 것을 1건으로 합친다(LLM 판정 필요,
   순수 문자열 dedup 불가). 신규 결함은 출처 태그(claude/codex)와 함께 보존.
3. 병합 결과를 canonical 후보 레코드로. §7 canonical 선택·완결 게이트 7항 절차로 승격.
4. ★canonical 무결성 작업이므로 santa-method(plan.md → codex adversarial-review → 실행 → review) 적용 권장.

## 4. 미해결/주의
- 병합은 269파일 semantic dedup — 큰 작업. 성급히 하지 말 것.
- 두 레코드 층(1차 pending + 감사 pending)은 병합 전까지 **모두 보존**(삭제 금지).
- FW004 감사는 메인 run(16) + 004a/b/c(32) 4 run 분산 — 병합 시 union 으로 대조.
