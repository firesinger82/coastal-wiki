# coastal-wiki

연안공학 도메인 지식의 객관 레이어(canonical)를 집적하는 단일 writer 위키.

## 정체성

- **1차 축**: `concepts/` — 도메인 개념(조석, 파랑, 표사이동, 흐름 등). 개념 → 일반론 → 분석법 → 코드 → 예제 → 모델적용.
- **2차 축**: `models/` — 모델별 객관 자료(소스코드 분석, 메뉴얼 발췌, 웹/논문 자료).
- **횡축**: `textbook/` — `D:\Study\textbook`의 교과서 자료를 참조·인용해 노트화.
- **연결**: `examples/` — 개념을 가로지르는 통합 실습.
- **유보**: `experience/` — 모델링 경험에서 객관화·논리정밀화 검증을 통과한 정보만. 객관 레이어가 어느 정도 자리잡은 후 추가.

## 핵심 규칙

1. **객관 레이어 우선**. 개인 경험은 `experience/`에만, 그것도 통과 기준 만족 후.
2. **모든 단언은 출처 명시** (소스코드 라인, 메뉴얼 페이지, 논문 인용, 교과서 챕터).
3. **AI 요약은 검증된 요약만**. 원본·요약 구분 명확화. 원본 위치 링크 필수.
4. **단일 writer**. 이 PC가 작성자, 다른 PC는 read-only.
5. **수정 이력은 git이 책임진다**. 임의 삭제·재구성 시 reasoning을 커밋 메시지에 기록.

## 디렉토리

| 경로 | 역할 |
|---|---|
| `concepts/<토픽>/` | 도메인 개념 (1차 축). `_template/` 복제해서 새 토픽 생성 |
| `models/<모델>/` | 모델별 객관 자료 (2차 축). `source-analysis/`, `manual-notes/`, `web-refs/` |
| `textbook/` | `D:\Study\textbook` 통합 노트와 인용. 원본 PDF는 wiki에 복사 안 함 |
| `examples/` | 개념을 가로지르는 실습 |
| `experience/` | 객관화 통과한 경험 (지금은 비어 있음, 정책 문서만) |

## 진입 순서

새 토픽 작업 시:
1. `concepts/_template/` 복제해 `concepts/<topic>/` 생성
2. 해당 토픽 관련 textbook 참조를 `textbook/notes/`에 추출
3. 관련 모델 항목은 `models/<model>/`에 객관 분석을 두고 `concepts/<topic>/06-model-application.md`에서 링크
4. 예제는 `examples/<scenario>/`에 둠

## 동기화

이 PC = writer, 다른 PC = reader. git push/pull로 sync.

## 우선 읽을 문서

- [CLAUDE.md](CLAUDE.md) — Claude 진입점
- [AGENTS.md](AGENTS.md) — Codex 진입점
- [INDEX.md](INDEX.md) — 전체 맵
- [plan.md](plan.md) — 초기 구조 결정 기록
- [textbook/POLICY.md](textbook/POLICY.md) — textbook 통합 정책
