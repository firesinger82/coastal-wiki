# coastal-wiki — Codex/Agents 진입점

상세는 [CLAUDE.md](CLAUDE.md), [README.md](README.md) 참조. 이 파일은 thin pointer.

## 핵심 규칙 (재인용)

1. 객관 레이어(`concepts/`, `models/`)는 **출처 인용 필수**.
2. 개인 경험은 `experience/`에만 (객관화 3조건 통과 후).
3. AI 요약은 원본·요약 명확히 구분.
4. "내가 해보니" 화법은 객관 레이어 금지.
5. 단일 writer (이 PC).
6. **모델 분석 범위 이탈 금지.** “전수·완벽·GOAL·계속”은 동봉된 의존성 전체 역어셈블리 지시가 아니다. MPI/Jumpshot 뷰어 등 부속 도구 내부를 모델 완료 조건으로 삼지 않는다. 재개 시에도 [CLAUDE.md의 범위 통제](CLAUDE.md#모델-분석-범위-통제)를 먼저 적용한다.

## 작업 진입 시

1. [plan.md 최상단 "현재 작업"](plan.md#현재-작업) 확인 — 활성 작업과 그 실행 기록의 포인터다. **현재 사용자 지시가 이 포인터보다 우선**하며, 포인터나 과거 재개 기록을 자동 실행 명령으로 해석하지 않는다.
2. [README.md](README.md) → [INDEX.md](INDEX.md) → 해당 디렉토리 확인
3. 새 토픽: `concepts/_template/`에서 `README.md` + `01-concept.md` 두 파일부터 ([CONVENTIONS.md §8](CONVENTIONS.md)), 02~06은 sourced claim이 생기면 추가
4. 새 모델: `models/_template/` 복제

## 큰 변경 시 워크플로

`plan.md` 작성 → `/codex:adversarial-review` → 반영 → 구현 → `/codex:review`
