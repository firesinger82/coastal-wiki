---
title: "SWASH 대조 결론 노트 반영 — 배정 4"
citation_status: verified
last_source_check: "2026-10-15 (recovery 대조 반영)"
verification_method: "2026-10-15 SWASH recovery 대조 보고서 반영"
---

# SWASH 대조 결론 노트 반영 — 배정 4

배정 근거는 [SWASH-note-job-4.tsv](../assign/SWASH-note-job-4.tsv)다.

배정표는 `swash-explicit-depthavg-flow.md`에 68행을 배정한다.
배정표는 `swash-linear-solvers.md`에 15행을 배정한다.
배정표는 `swash-turbulence-closure.md`에 9행을 배정한다.

파일별 반영 결과는 아래에 기록했다.

## swash-explicit-depthavg-flow.md

대상은 [명시적 수심평균 노트](../../../models/SWASH/source-analysis/swash-explicit-depthavg-flow.md)다.
표에 배정표의 68행을 넣었다.
표의 행 ID·분류·결론 문장은 최종 보고서와 대응한다.
표 위치는 `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:333–402`이다.

추가·수정 줄 범위는 다음과 같다.

- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:7–8`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:88–91`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:223–226`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:247–248`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:271–273`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:275–283`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:303–304`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:308–312`
- `models/SWASH/source-analysis/swash-explicit-depthavg-flow.md:321–402`

반영한 수정안 행 ID는 `theory-framework:ST1-324`, `theory-unstructured:ST2-146`, `theory-unstructured:ST2-150`, `theory-unstructured:ST2-039`, `callflow:RF-022`다.
본문의 CFL 평가 집합에는 `callflow:RF-021`의 결론을 반영했다.
본문의 체적 진단에는 `theory-framework:ST1-310`의 결론을 반영했다.
수위 적분의 기존 입력 선택 설명은 유지했다.
상대 링크의 대상 파일은 모두 존재한다.
넣지 않은 배정 행은 없다.

## swash-linear-solvers.md

대상은 [선형 솔버 노트](../../../models/SWASH/source-analysis/swash-linear-solvers.md)다.
표에 배정표의 15행을 넣었다.
표의 행 ID·분류·결론 문장은 최종 보고서와 대응한다.
표 위치는 `models/SWASH/source-analysis/swash-linear-solvers.md:134–150`이다.

추가·수정 줄 범위는 다음과 같다.

- `models/SWASH/source-analysis/swash-linear-solvers.md:6–7`
- `models/SWASH/source-analysis/swash-linear-solvers.md:21`
- `models/SWASH/source-analysis/swash-linear-solvers.md:26`
- `models/SWASH/source-analysis/swash-linear-solvers.md:30–35`
- `models/SWASH/source-analysis/swash-linear-solvers.md:75–76`
- `models/SWASH/source-analysis/swash-linear-solvers.md:84–87`
- `models/SWASH/source-analysis/swash-linear-solvers.md:115–117`
- `models/SWASH/source-analysis/swash-linear-solvers.md:121–123`
- `models/SWASH/source-analysis/swash-linear-solvers.md:125–150`

반영한 수정안 행 ID는 `theory-unstructured:ST2-225`, `theory-unstructured:ST2-403`, `theory-unstructured:ST2-430`이다.
ST2-225는 일치 행이므로 격자 조건 보완만 본문에 반영했다.
본문의 1DH 직접해법과 PCG 초기 기준에는 `inputs-physics-numerics:SI2-189`, `inputs-physics-numerics:SI2-279`의 결론을 반영했다.
SIP 완화계수의 기존 설명은 유지했다.
기존 위키 링크는 상대 Markdown 링크로 바꿨다.
상대 링크의 대상 파일은 모두 존재한다.
넣지 않은 배정 행은 없다.

## swash-turbulence-closure.md

대상은 [난류 폐합 노트](../../../models/SWASH/source-analysis/swash-turbulence-closure.md)다.
표에 배정표의 9행을 넣었다.
표의 행 ID·분류·결론 문장은 최종 보고서와 대응한다.
표 위치는 `models/SWASH/source-analysis/swash-turbulence-closure.md:213–223`이다.

추가·수정 줄 범위는 다음과 같다.

- `models/SWASH/source-analysis/swash-turbulence-closure.md:7–8`
- `models/SWASH/source-analysis/swash-turbulence-closure.md:29`
- `models/SWASH/source-analysis/swash-turbulence-closure.md:136–138`
- `models/SWASH/source-analysis/swash-turbulence-closure.md:190–191`
- `models/SWASH/source-analysis/swash-turbulence-closure.md:204–223`

반영한 수정안 행 ID는 `inputs-physics-numerics:SI2-288`이다.
1DH 혼합길이 식의 중복된 수평 간격 나눗셈을 고쳤다.
기존에 해소한 `iturb=2` 작업 메모를 사실 문장으로 바꿨다.
2DH z-plane 확산의 작업 메모는 `inputs-physics-numerics:SI2-284`가 인용한 코드 원문으로 바꿨다.
SI2-284의 별도 표 행은 추가하지 않았다.
상대 링크의 대상 파일은 모두 존재한다.
넣지 않은 배정 행은 없다.

## 최종 대조

[배정표](../assign/SWASH-note-job-4.tsv)의 92행을 모두 반영했다.
파일별 반영 행 수는 배정표의 68·15·9행과 각각 같다.
표의 행 ID와 분류는 보고서의 최종 결론 행과 대응한다.
표의 코드·식 인용은 입력 보고서 원문과 대조했다.
중복 행은 없다.
H 행과 일치 행은 차이 표에 넣지 않았다.
담당 노트의 수정안 9행은 파일별 반영 목록에 기록했다.
세 노트의 기존 `citation_status`는 유지했다.
세 노트와 이 기록의 `last_source_check`는 `2026-10-15 (recovery 대조 반영)`이다.
세 노트와 이 기록의 `verification_method`에는 `2026-10-15 SWASH recovery 대조 보고서 반영`을 적었다.
넣지 않은 배정 행은 없다.
누락 사유는 해당 없다.
