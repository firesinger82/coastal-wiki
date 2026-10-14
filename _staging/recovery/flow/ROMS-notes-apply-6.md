# ROMS 노트 반영 기록 — 작업 6

배정표: [note-job-6.tsv](../assign/note-job-6.tsv).

배정표의 차이 행은 201개다.
`roms-wiki-cppdefs-options-differences-2.md`의 배정 행은 199개다.
`roms_adjoint_framework.md`의 배정 행은 2개다.
`manifest.md`에는 배정된 차이 행이 없다.

## 파일별 반영 결과

### CPP 옵션 차이 노트

파일: [roms-wiki-cppdefs-options-differences-2.md](../../../models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md).

추가 범위: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md:1–232`.
차이 표 범위: `models/ROMS/manual-notes/roms-wiki-cppdefs-options-differences-2.md:34–232`.
넣은 행 수는 199개다.
이 수는 배정표에서 이 파일에 배정한 199개 행과 같다.
차이 행 ID는 `build-options-history:RBH-0769`부터 배정표 순서대로 `build-options-history:RBH-1232`까지다.
이 새 파일을 가리키는 수정안 행은 없다.
넣지 않은 배정 행은 없다.

### 자료동화 framework 노트

파일: [roms_adjoint_framework.md](../../../models/ROMS/source-analysis/roms_adjoint_framework.md).

frontmatter 수정 범위: `models/ROMS/source-analysis/roms_adjoint_framework.md:2`, `models/ROMS/source-analysis/roms_adjoint_framework.md:6–7`.
본문 수정 범위: `models/ROMS/source-analysis/roms_adjoint_framework.md:20`, `models/ROMS/source-analysis/roms_adjoint_framework.md:22`, `models/ROMS/source-analysis/roms_adjoint_framework.md:28`, `models/ROMS/source-analysis/roms_adjoint_framework.md:30`, `models/ROMS/source-analysis/roms_adjoint_framework.md:33–37`, `models/ROMS/source-analysis/roms_adjoint_framework.md:47–50`, `models/ROMS/source-analysis/roms_adjoint_framework.md:56`, `models/ROMS/source-analysis/roms_adjoint_framework.md:62–64`, `models/ROMS/source-analysis/roms_adjoint_framework.md:69`, `models/ROMS/source-analysis/roms_adjoint_framework.md:73–77`.
표 앞 빈 줄 추가 위치: `models/ROMS/source-analysis/roms_adjoint_framework.md:25`.
차이 절 추가 범위: `models/ROMS/source-analysis/roms_adjoint_framework.md:79–89`.
차이 표 범위: `models/ROMS/source-analysis/roms_adjoint_framework.md:88–89`.
넣은 행 수는 2개다.
이 수는 배정표에서 이 파일에 배정한 2개 행과 같다.
차이 행 ID는 `biology:CD-003`과 `callflow-da:RF2-020`이다.
반영한 수정안 행 ID는 `da-4dvar:DA1-824`와 `callflow-da:RF2-020`이다.
`DA1-824`의 수정안은 hand-coded 수반의 의도된 transpose 관계를 설명하도록 반영했다.
`RF2-020`의 수정안은 I4·RBL의 비선형 기본 상태 갱신과 R4의 외부 반복별 궤적을 구분하도록 반영했다.
`biology:CD-003`의 dispatcher 범위는 본문에도 반영했다.
넣지 않은 배정 행은 없다.

### 자료 목록

파일: [manifest.md](../../../models/ROMS/manifest.md).

추가·수정 범위는 없다.
배정된 차이 행 수는 0개다.
입력 보고서의 수정안 절에서 이 파일을 가리키는 행 수는 0개다.
이 파일은 원문을 유지했다.

## 최종 검증

배정표의 201개 행을 모두 반영했다.
노트 표에서 센 행 수는 CPP 옵션 차이 노트 199개와 자료동화 노트 2개다.
두 파일의 합계는 배정표의 201개 행과 같다.
배정표 기준 결론별 행 수는 A 168개, B 29개, C 3개, D 1개다.
누락 행, 중복 행, 배정표 밖 행, 배정 파일 불일치는 각각 0개다.
넣지 않은 행과 이유는 없다.

CPP 옵션 차이 노트의 결론 199개는 보고서 §5의 최종 결론과 같다.
CPP 옵션 차이 노트의 원문 인용 3507개는 보고서 표의 인용과 같다.
원문 인용 수는 HTML로 렌더한 문서 원문·코드 원문 칸의 code 요소에서 셌다.
A 행 168개의 결론 칸에는 보고서의 git 판정 HASH와 날짜를 넣었다.
자료동화 노트의 두 차이 행은 보고서의 원문 인용과 최종 결론을 반영했다.
담당 노트를 가리키는 수정안 행 `DA1-824`와 `RF2-020`을 반영했다.
`DA1-824`는 수정안으로만 반영했다.
차이 표에는 H 행과 일치 행이 없다.

frontmatter의 last_source_check는 두 노트 모두 `2026-10-14 (recovery 대조 반영)`이다.
두 노트의 verification_method에는 `2026-10-14 ROMS recovery 대조 보고서 반영`을 덧붙였다.
기존 자료동화 노트의 citation_status를 유지했다.
새 CPP 옵션 차이 노트의 citation_status는 verified다.
새 노트의 첫 본문 줄과 related에는 부모 노트를 연결했다.

차이 표의 각 행은 지정한 6개 열로 렌더된다.
두 노트의 Markdown 링크는 상대 링크이며 대상 파일이 존재한다.
두 노트에는 금지한 로컬 절대 경로와 이중 대괄호 문자열이 없다.
공백 오류 검사는 통과했다.
부모 노트와 manifest.md는 작업 시작 시점의 원문과 같다.
