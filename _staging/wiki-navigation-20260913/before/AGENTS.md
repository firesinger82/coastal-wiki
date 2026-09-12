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

1. [README.md](README.md) → [INDEX.md](INDEX.md) → 해당 디렉토리 확인
2. 새 토픽: `concepts/_template/` 복제
3. 새 모델: `models/_template/` 복제

## 큰 변경 시 워크플로

`plan.md` 작성 → `/codex:adversarial-review` → 반영 → 구현 → `/codex:review`
