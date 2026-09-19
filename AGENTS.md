# coastal-wiki — Codex/Agents 진입점

상세는 [CLAUDE.md](CLAUDE.md), [README.md](README.md) 참조. 요구사항·범위·운영 제약 기준선은 [PROJECT_REQUIREMENTS.md](PROJECT_REQUIREMENTS.md) (충돌 시 최신 사용자 명시 지시 > PROJECT_REQUIREMENTS.md > CLAUDE.md·AGENTS.md·BUILD-PLAN.md > 기타). 이 파일은 thin pointer.

## 핵심 규칙 (재인용)

1. 객관 레이어(`concepts/`, `models/`)는 **출처 인용 필수**.
2. 개인 경험은 `experience/`에만 (객관화 3조건 통과 후).
3. AI 요약은 원본·요약 명확히 구분.
4. "내가 해보니" 화법은 객관 레이어 금지.
5. 단일 writer (이 PC).
6. **모델 분석 범위 이탈 금지.** “전수·완벽·GOAL·계속”은 동봉된 의존성 전체 역어셈블리 지시가 아니다. MPI/Jumpshot 뷰어 등 부속 도구 내부를 모델 완료 조건으로 삼지 않는다. 재개 시에도 [CLAUDE.md의 범위 통제](CLAUDE.md#모델-분석-범위-통제)를 먼저 적용한다.

## 작업 진입 시

1. 중단 작업을 재개하거나 현재 범위가 불명확할 때 [plan.md 최상단 "현재 작업"](plan.md#현재-작업)만 확인 — 활성 작업과 그 실행 기록의 포인터다. **현재 사용자 지시가 이 포인터보다 우선**하며, 포인터나 과거 재개 기록을 자동 실행 명령으로 해석하지 않는다.
2. 작업에 필요한 문서만 읽는다. 구조 파악은 [README.md](README.md)·해당 디렉터리 README, 항목 찾기는 [INDEX.md](INDEX.md)의 관련 부분, 작성 규칙은 [CLAUDE.md](CLAUDE.md)의 문서 안내를 따른다. 이미 확인한 지침은 변경되었거나 새 판단에 필요한 경우에만 다시 읽는다.
3. 새 토픽: `concepts/_template/`에서 `README.md` + `01-concept.md` 두 파일부터 ([CONVENTIONS.md §8](CONVENTIONS.md)), 02~06은 sourced claim이 생기면 추가
4. 새 모델: `models/_template/` 복제

모델 기능 근거의 구축·비교·결합은 [BUILD-PLAN.md](BUILD-PLAN.md)의 해당 단계·완료 조건을 따른다.

**역할** ([CLAUDE.md 역할 분담](CLAUDE.md#역할-분담-claude--codex)): Claude = Lead / Planner / Reviewer, Codex = Executor / Investigator. Codex는 OBJECTIVE / SCOPE / STOP CONDITION / DELIVERABLE 계약 범위에서 조사·수정·검사를 수행하고 evidence와 함께 반환한다. 범위 밖 판단이 필요하면 작업을 확대하지 않고 Claude에게 반환한다. `models/`는 root 잠금 — 우회하지 않고 diff/script까지만 만든다. Claude 모델 지정은 CLAUDE.md를 따른다.

## 큰 변경 시 워크플로

Claude 계획(`plan.md` 포인터 + 작업 문서) → `/codex:adversarial-review`(계획 비판) → Claude 반영 판단 → Codex 구현(bounded task, `models/`는 diff/script까지) → Claude 검증 → 사람 게이트 → 커밋
