---
title: "SWASH 대조 결론 노트 반영 — 배정 5"
citation_status: verified
last_source_check: "2026-10-15 (recovery 대조 반영)"
verification_method: "2026-10-15 SWASH recovery 대조 보고서 반영"
---

# SWASH 대조 결론 노트 반영 — 배정 5

배정 기준은 [SWASH-note-job-5.tsv](../assign/SWASH-note-job-5.tsv)이다.
배정표에서 경계·파 생성 노트는 62행이다.
배정표에서 명시적 다층 흐름 노트는 21행이다.
배정표에서 경계 스펙트럼 전달 노트는 8행이다.

파일별 반영 결과는 각 노트를 마친 뒤 아래에 기록한다.

## swash-boundary-wave-forcing.md

대상은 [swash-boundary-wave-forcing.md](../../../models/SWASH/source-analysis/swash-boundary-wave-forcing.md)이다.
추가·수정 줄 범위: `models/SWASH/source-analysis/swash-boundary-wave-forcing.md:7–8`, `models/SWASH/source-analysis/swash-boundary-wave-forcing.md:95–96`, `models/SWASH/source-analysis/swash-boundary-wave-forcing.md:149–152`, `models/SWASH/source-analysis/swash-boundary-wave-forcing.md:195–198`, `models/SWASH/source-analysis/swash-boundary-wave-forcing.md:221–294`.
차이 표 절은 `models/SWASH/source-analysis/swash-boundary-wave-forcing.md:224–294`이다.
넣은 행 수는 62행이다.
배정표의 이 파일 행 수는 62행이다.
반영한 수정안 행 ID는 `inputs-setup:SI1-711`, `theory-unstructured:ST2-416`, `guide-syntax-build:SG1-927`, `guide-syntax-build:SG1-928`, `guide-syntax-build:SG1-929`이다.
`SG1-927`의 NUMDISP·0.9 문턱 설명은 유지했다.
`SG1-928`의 Beji 변형 Ursell 식은 유지했다.
`SG1-929`의 10% 이상 경고 문장은 유지했다.
`SG1-929`의 경고 억제는 보고서 코드 원문의 `.not.nowarn`과 `nowarn = .true.`를 인용했다.
스펙트럼 읽기의 다른 경로를 추정한 기존 문장은 경계 스펙트럼 전달 노트의 `inputs-setup:SI1-319` 근거 위치로 바꿨다.
넣지 않은 배정 행은 없다.

## swash-explicit-layered-flow.md

대상은 [swash-explicit-layered-flow.md](../../../models/SWASH/source-analysis/swash-explicit-layered-flow.md)이다.
추가·수정 줄 범위: `models/SWASH/source-analysis/swash-explicit-layered-flow.md:7–8`, `models/SWASH/source-analysis/swash-explicit-layered-flow.md:98–100`, `models/SWASH/source-analysis/swash-explicit-layered-flow.md:135–137`, `models/SWASH/source-analysis/swash-explicit-layered-flow.md:163–164`, `models/SWASH/source-analysis/swash-explicit-layered-flow.md:200–202`, `models/SWASH/source-analysis/swash-explicit-layered-flow.md:204–234`.
차이 표 절은 `models/SWASH/source-analysis/swash-explicit-layered-flow.md:205–234`이다.
넣은 행 수는 21행이다.
배정표의 이 파일 행 수는 21행이다.
반영한 수정안 행 ID는 `theory-framework:ST1-334`, `theory-framework:ST1-337`, `theory-unstructured:ST2-428`, `theory-unstructured:ST2-429`이다.
`ST1-337`의 최상층 1·최하층 kmax 정의는 유지했다.
`ST1-334`는 자유수면 경계면의 압력 계수 1·3 제거로 고쳤다.
`ST2-428`은 바닥에서 자유수면으로 상대 연직속도를 복원하는 방향으로 고쳤다.
`ST2-429`는 아래쪽 qlay개 층의 압력 자유도 축소로 고쳤다.
기존 gmatw 미전사 문장은 `theory-unstructured:ST2-392`의 압력 계수 사실로 바꿨다.
넣지 않은 배정 행은 없다.

## swash-boundary-spectral-transfer.md

대상은 [swash-boundary-spectral-transfer.md](../../../models/SWASH/source-analysis/swash-boundary-spectral-transfer.md)이다.
추가·수정 줄 범위: `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:7–8`, `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:101–104`, `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:198–200`, `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:203–223`.
차이 표 절은 `models/SWASH/source-analysis/swash-boundary-spectral-transfer.md:207–223`이다.
넣은 행 수는 8행이다.
배정표의 이 파일 행 수는 8행이다.
반영한 수정안 행 ID는 `inputs-setup:SI1-319`, `inputs-setup:SI1-714`, `inputs-setup:SI1-712`, `inputs-setup:SI1-713`이다.
`SI1-319`의 SPEC1D에 한정한 주기 보정은 유지했다.
`SI1-714`는 fac의 열린 부등식과 양 끝 1% 구간의 보정으로 고쳤다.
`SI1-712`는 seedf·seedt의 m_bndspec 선언 위치로 고쳤다.
`SI1-713`은 전달함수 배열의 선언 모듈과 차원으로 고쳤다.
넣지 않은 배정 행은 없다.

## 최종 점검

배정표의 총 행 수는 91행이다.
세 노트에 넣은 총 행 수는 91행이다.
담당 노트를 가리키는 수정안은 보고서 §4에서 센 13행이다.
이 13행의 정정·추가·유지 지시를 반영했다.
callflow §6에는 담당 세 노트를 가리키는 수정안 행이 없다.
넣지 않은 배정 행은 없다.
행 ID의 중복과 배정 파일 불일치는 없다.
차이 표의 H·일치 행은 없다.
보고서의 백틱 인용과 수식을 표의 해당 칸과 비교했다.
조건문과 수식의 원문은 보존했다.
세 노트의 문서 판·코드 판 표기는 요청한 판 정보와 일치한다.
세 노트와 이 기록의 frontmatter·상대 링크를 점검했다.
기존 citation_status는 유지했다.
세 노트의 `git diff --check`는 통과했다.
이 기록의 추가·수정 줄 범위는 세 노트의 diff와 일치한다.
