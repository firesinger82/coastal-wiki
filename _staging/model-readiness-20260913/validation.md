# 준비 상태 조사 검토 — 2026-09-14 완료

- 13모델 본체·지정 문서 경로 존재, 추적 기술 노트 437편과 독립 비교 노트 5편의 기존 snapshot SHA 일치. 비교 본문 링크 해석 실패 0. 이는 내용 전체의 정확성 판정이 아니다.
- [Fable 응답 원문](fable-review.md), [실행 결과 JSON](fable-review.json)의 실제 `modelUsage`에 `claude-fable-5-1` 확인. CLI 보조 호출 Haiku도 별도 기록되어 있다. 판정은 블로커 없음이며 사람 승인이 아니다.
- 낮음 1–3: frontmatter 기준·추적 파일/하위 폴더·`not-issued` 집계 기준을 보고서에 명시했다. 낮음 4–5: full-formula 내부 ETRF 적용 여부 미확인, 다음 대조 구간, 잘못된 SWASH beta 입력의 0.3 처리 조건을 관찰 기록에 추가했다. 낮음 6은 외부 검토 미대조 범위이며 조사자의 로컬 문서 확인과 구분한다. 이 서술 보완 뒤 동일 외부 검토를 반복하지 않았다.
- evidence_sha256의 원문·원장·문서 해시 재확인, XBeach 기존 immutable-baseline 292파일 해시 일치. canonical 모델/개념 노트·AGENTS/CLAUDE·스킬 변경 없음.
- 두 보고서 묶음의 로컬 Markdown 대상 경로 확인. 지침 수정안은 `git apply --check` 통과한 미적용 패치다.
- 커밋 대상은 plan.md의 이번 현재 포인터/이력, 준비 상태 조사와 지침 점검 묶음이다. 기존 plan.md 미커밋 6줄은 그대로 보존하고 index 패치에서 제외했다. XBeach interfaces 미추적 작업도 커밋 대상에서 제외한다.
