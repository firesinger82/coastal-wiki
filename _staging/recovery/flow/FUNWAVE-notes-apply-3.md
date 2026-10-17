---
title: "FUNWAVE 대조 보고서 노트 반영 기록 — 작업 3"
citation_status: verified
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
---

# FUNWAVE 대조 보고서 노트 반영 기록 — 작업 3

배정표는 [FUNWAVE-note-job-3.tsv](../assign/FUNWAVE-note-job-3.tsv)다.
대상 노트는 [funwave-physics-sources.md](../../../models/FUNWAVE/source-analysis/funwave-physics-sources.md)다.
배정표의 224개 행을 담당 노트에 반영했다.

## 파일별 결과

- 메타데이터 수정: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:5–6`.
- 쇄파 계수·점성 분기 수정: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:18–27`.
- WK_TIME 성분표 수정: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:39`, `models/FUNWAVE/source-analysis/funwave-physics-sources.md:43–44`.
- 마찰 적용 조건·nu_smg 생산 경로·상대풍속 조건 수정: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:61–74`.
- 평균 출력·질량 보정 조건 수정: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:78–84`.
- 차이 절 추가: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:89–332`.
- 배정 행 표 추가: `models/FUNWAVE/source-analysis/funwave-physics-sources.md:109–332`.

반영한 수정안 행 ID는 `theory-numerics:FT1-280`, `theory-numerics:FT1-281`, `examples:FX1-912`, `examples:FX1-913`, `v21-manual:FV1-561`, `v21-manual:FV1-562`, `v21-manual:FV1-563`, `v21-examples:FV2-403`, `v21-examples:FV2-404`, `v21-examples:FV2-409`, `aux-docs-build:FN1-922`, `callflow:RF-050`이다.
callflow §6.1의 행 ID 없는 `MIXING_STUFF` 수정안도 반영했다.
기존 `MIXING_STUFF` 설명은 유지했다.

## 배정표 대조 집계

집계 단위는 배정표의 서로 다른 행 ID다.
넣은 행 수는 224개다.
배정표 행 수는 224개다.

- theory-numerics: 35개, 노트 109–143행.
- inputs: 16개, 노트 144–159행.
- examples: 12개, 노트 160–171행.
- v21-manual: 48개, 노트 172–219행.
- v21-examples: 17개, 노트 220–236행.
- aux-docs-build: 37개, 노트 237–273행.
- gpu-vs-tvd: 52개, 노트 274–325행.
- callflow: 7개, 노트 326–332행.

넣지 않은 배정 행은 없다.
배정표 밖의 표 행은 없다.

## 확인 결과

보고서 최종 결론 224개와 노트의 결론 문구는 일치한다.
보고서 최종 근거의 원문 인용 2,465개를 노트의 표 렌더 토큰과 대조했다.
이 원문 인용의 불일치는 없다.
Markdown 표 파서는 배정 행 224개를 모두 6열로 읽었다.
행 ID 중복과 누락은 없다.
A 행 25개에는 커밋 HASH와 날짜가 있다.
E 행 9개에는 근거 강도가 있다.
노트와 이 기록의 상대 링크는 모두 유효하다.
금지 문자열은 없다.
