# 구조 개편 실행 기록 — 2026-09-13

사용자의 “진행해” 지시에 따라 [검토된 계획](../wiki-structure-20260912/plan.md)을 구현한다. 현재 작업은 루트 [plan.md](../../plan.md#현재-작업)에서 진입한다. XBeach 감사는 중단 상태이며 이 기록은 모델 완료·새 사람 승인이 아니다.

## P1·P3 — 탐색 안내

상태: 8개 파일의 Fable·Codex 검토 및 설치 완료([설치 확인](installation.json)). 입력과 원래 해시는 [inputs.json](inputs.json), 사본은 `before/`·`candidate/`에 보존한다. 원본 위치·기술 본문·검색 코드·기존 승인 기록은 이번 편집 대상이 아니다.

변경 전에 [12문항](questions.json)을 동결했다. [기준선](navigation-before.json)은 직접 링크 4/12, README·INDEX를 통한 3회 이내 이동 4/12다. 이는 정해진 문서까지의 탐색 측정이며 정확도·모델 완료율·검색 성능이 아니다. [원출처 위치 확인](locator-checks.json)도 주제·위치의 한정 대조다.

검토는 사용자가 지정한 `claude-fable-5-1`과 기존 절차의 Codex 최종 검토를 사용한다. 요청 모델과 실제 응답 모델은 결과 JSON의 `modelUsage`로 구별한다. 작성은 기존 절차에 따라 Opus가 맡는다.

## P2 — 작업 규칙

상태: P1 전후 비교 완료. P1 설치 후 별도 5파일 정책 패치를 반영한다. Fable·Codex 검토 완료, P1 설치 후 적용 대기. 개별 보강과 전체 감사의 분리, 현재 작업 포인터를 명시하며 기존 전수 집합·승인·종료 조건은 유지한다.

## 한계와 실행 메모

- [범위 밖 기존 링크 문제](out-of-scope-findings.md)는 보존·보고하고 다른 토픽으로 편집을 확대하지 않는다.
- 최초 Opus 작성 시도 `claude-write.json`은 Edit 권한 경로 불일치로 파일을 수정하지 못했다. [Claude 공식 경로 규칙](https://code.claude.com/docs/en/permissions)의 절대 경로 `//` 표기로 candidate 하위 권한만 수정해 재시도한다. 작업 승인 거절이나 작성 성공으로 기록하지 않는다.
- 작업 전 존재한 plan.md의 R1-G2/G3 미완 계획 6줄과 `interfaces-20260912/`는 이번 변경 묶음에 포함하지 않는다.

## 검토 결과

[Fable 탐색 검토](fable-review.md)와 [Codex 탐색 검토](codex-review.txt)는 차단 문제 없이 반영 가능 판정이다. [Fable 정책 검토](fable-policy-review.md)도 반영 가능 판정이며 실제 사용 모델은 [응답 확인](review-models.json)에 기록한다. P2의 구체적 diff·검토·적용 증거도 함께 커밋해 정책 개정 기록을 보존한다.

P1 비차단 관찰은 범위 밖 기존 상태로 남긴다: Q3D·비정수압 보고서의 정정 frontmatter 공백, 기존 참고 노트 2편의 직접 링크 부재, 목차의 날짜별 상태 스냅샷. 새 감사·편집 묶음으로 자동 확장하지 않는다. P2는 P1의 plan after 해시에 의존하므로 반드시 P1 뒤에 설치한다.

[Codex 정책 검토](codex-policy-review.txt)도 도입 결함 없음으로 판정했다. P1 설치는 검토한 후보 8개와 바이트가 같고 원래 소유자·권한을 보존했다. 전체 검증기 결과는 커밋 시 기록한다.
