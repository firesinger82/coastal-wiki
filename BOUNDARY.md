# BOUNDARY — modeling-wiki와의 경계

`D:\modeling-wiki/`와 `~/coastal-wiki/`는 별개 wiki. 다음 규칙으로 충돌·중복 방지.

## 두 wiki의 정체성

| 항목 | `D:\modeling-wiki/` | `~/coastal-wiki/` |
|---|---|---|
| 주된 콘텐츠 | 경험·실험 로그 (experiments/, knowledge/, failure-patterns/) | 객관 도메인 지식 (concepts/, models/, textbook/) + experience/ |
| 작성 시기 | 2026-04 ~ | 2026-05-21 ~ |
| 작성 원칙 | 시행착오 보존, "promote-from-experiments-to-knowledge" | 출처 인용 우선, "객관 레이어 first" |
| 화법 | 1인칭 OK (실험 기록) | 객관 (3인칭, 출처 기반) |
| 출처 | 실험 조건 + 결과 | 소스코드 file:line, 메뉴얼 페이지, 논문 인용 |

## 어디에 무엇을 적는가

### `coastal-wiki/`에 들어가는 것
- 모델 소스코드 구조·메커닉 (객관) → `models/<model>/source-analysis/`
- 모델 공식 메뉴얼 발췌 (객관) → `models/<model>/manual-notes/`
- 도메인 개념·이론 (객관) → `concepts/<topic>/`
- 교과서 발췌·요약 → `textbook/notes/`
- 검증 통과한 경험 (반복 관찰 + 객관 데이터 + 재현 가능) → `experience/`

### `modeling-wiki/`에 남는 것
- 진행 중인 실험·시행착오 기록 → `experiments/`
- 아직 검증 안 된 휴리스틱 → `knowledge/heuristics/`
- 단발성 failure pattern → `knowledge/failure-patterns/`
- 진행 중 컨텍스트 → `context/`

### 양쪽 다 적지 않는 것
- 특정 프로젝트(축산항·고현·거제 등)의 raw 결과·산출물 — 각 프로젝트 디렉토리에 (현재 `D:\Projects\`)

## 마이그레이션 규칙

`modeling-wiki/knowledge/`의 항목이 다음 조건 만족하면 `coastal-wiki/experience/`로 이전 검토:

1. 같은 패턴이 2회 이상 독립 관측 (다른 프로젝트·다른 모델·다른 시기)
2. 객관적 데이터로 근거 명시 (수치·플롯·비교)
3. 다른 사람이 같은 조건으로 재현 가능

조건 충족 시 → `coastal-wiki/experience/`에 frontmatter `verification_by`, `verification_date` 명시하고 새 파일 생성, `modeling-wiki/` 원본은 보존 (단방향 promote, 양방향 sync 금지).

이전된 항목이 한 번 더 검증되면 (도메인 일반 지식 수준) `concepts/<topic>/`로 승격 가능.

## 새 객관 자료는 한쪽에만

- 새 객관 자료 (소스 분석, 메뉴얼 발췌, 교과서 노트) → **`coastal-wiki/`에만**
- `modeling-wiki/`에 새 객관 노트 작성 **금지**
- 기존 `modeling-wiki/`의 객관성 있는 노트(`indexes/`, `protocols/`)는 점진 이전 검토 (별도 의사결정)

## 크로스 링크

- `coastal-wiki/experience/<항목>.md`에서 원본 `modeling-wiki/...` 위치를 frontmatter `origin:` 필드로 기록
- 반대 방향 (`modeling-wiki`에서 `coastal-wiki` 참조)는 본문 내 텍스트 링크로 자유

## 외부 편집 인테이크 (단일 writer 정책 예외 처리)

다른 PC에서 오류·추가 항목 발견 시 우회 워크플로 (read-only 원칙 유지하면서):

1. **메모 적기**: 다른 PC에서 발견한 수정 사항을 `~/coastal-wiki-intake.txt` 같은 임시 파일에 기록 (이 wiki 외부)
2. **patch 파일 생성** (선택): 사소한 typo면 `git diff > intake.patch`를 메모 첨부
3. **writer PC에서 처리**: writer PC로 돌아와 sync 후 직접 편집·커밋
4. **issue tracker 대체**: GitHub repo 호스팅 후엔 Issues 활용 가능

**금지**:
- reader PC에서 직접 commit
- reader PC와 writer PC에서 동시 편집
- 다른 PC의 로컬 staging area에 변경 유지 (sync 충돌 원인)

## 통합 결정 시점

다음 트리거 중 하나 발생 시 두 wiki 통합 재검토:
- `coastal-wiki/concepts/` 토픽 5개 이상 verified 상태
- `coastal-wiki/models/` 모델 2개 이상 verified 상태
- `coastal-wiki/experience/` 항목 10개 이상 누적
- 사용자가 "modeling-wiki 더 이상 분리 의미 없음" 판단

위 시점에 별도 plan.md 작성 → adversarial review → 통합 또는 분리 유지.
