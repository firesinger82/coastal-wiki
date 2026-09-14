# 최종 구축 계획 적용 — 2026-09-14

사용자가 기능 수행·세팅·입력 신뢰성·매뉴얼/식/코드/실행·수치/물리 적합성을 연결하고, 그 기반에서 모델 비교·분석·융합을 진행하는 계획을 최종 수립·Claude 검토 후 반영하도록 지시했다. [BUILD-PLAN.md](../../BUILD-PLAN.md)에 방법과 종료 조건을 반영했다. 계획 작성과 Claude 검토는 사용자 지정 Fable 5.1이다.

- [범위](brief.md), [Fable 작성 프롬프트](fable-plan-prompt.txt), [작성 응답](fable-plan.json). 실제 modelUsage `claude-fable-5-1` 확인. CLI 파일 쓰기는 허용되지 않아 응답의 Markdown 초안을 그대로 저장하고 Codex가 검토 보완했다. Opus 실행·응답은 없었다.
- [Fable 계획 검토](fable-plan-review.md), [Codex 비판 검토](codex-plan-review.txt): 모두 채택 블로커 없음. 기능 지도는 인용·frontmatter를 가진 모델 노트를 가리키고, 확인 수준 표기 및 조사만 요청된 경우의 원문 보존을 보완했다. 모델 지정 누락과 문서 안내는 실제 적용에서 반영했다.
- 적용: BUILD-PLAN 신설, README/AGENTS/CLAUDE의 목적·문서 안내·완료 기준, Claude 기본 `claude-fable-5-1`, 두 스킬 description만 정비, CONVENTIONS governance 예외 목록에 BUILD-PLAN 추가. 스킬 본문·전역 설정·기존 감사/승인 상태는 유지한다.
- 첫 실행: [ADCIRC 조석 입력 한정 보강](../adcirc-tide-20260914/README.md). 전체 모델 실행·물리 검증 완료로 표시하지 않는다.

[Codex 최종 검토](codex-final-review.txt)는 운영 지침과 ADCIRC 설명 변경에 새 결함이 없음을 확인했다. 설치기 P2 한 건은 명시 예외 검사로 보완하고 최적화 모드의 변조 거부·정상 설치를 확인했다. 검토 이후 설치한 두 노트가 검토 후보 SHA와 일치하며 XBeach 불변 292파일이 유지된다.

두 스킬은 quick_validate 통과했고 본문은 HEAD와 동일하다. 문서 링크와 변경 공백 검사를 통과했다. [Claude 모델 확인](claude-model-check.json)은 주 작성·검토 3응답의 Fable 5.1과 CLI 보조 Haiku를 구분하며 Opus 응답은 없다. 기존 plan.md 미커밋 6줄과 XBeach interfaces 작업은 그대로 보존하고 이번 커밋에서 제외한다.
