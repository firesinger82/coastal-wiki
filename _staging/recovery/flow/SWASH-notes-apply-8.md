---
title: "SWASH 노트 대조 반영 — 작업 8"
citation_status: verified
last_source_check: "2026-10-15 (recovery 대조 반영)"
verification_method: "2026-10-15 SWASH recovery 대조 보고서 반영"
---

# SWASH 노트 대조 반영 — 작업 8

배정 기준은 [SWASH-note-job-8.tsv](../assign/SWASH-note-job-8.tsv)다.

배정표의 행 수는 바닥마찰·바람응력 노트 30행, wetting-drying 노트 27행, 수심평균 흐름 노트 21행, SWASH README 6행이다.

루트 README에는 보고서의 E 결론 41행을 별도 표로 반영한다.

## 파일별 반영 기록

### 바닥마찰·바람응력

- 대상: [swash-bottom-friction-wind.md](../../../models/SWASH/source-analysis/swash-bottom-friction-wind.md).
- 추가·수정 줄: `models/SWASH/source-analysis/swash-bottom-friction-wind.md:7–8,54,56–57,110,177–179,213–219,228–231,244,258,260–307`.
- 차이 표: `models/SWASH/source-analysis/swash-bottom-friction-wind.md:268–307`.
- 넣은 행 수: 배정표 30행 중 30행.
- 반영한 수정안 행 ID: inputs-physics-numerics:SI2-030·SI2-038·SI2-039·SI2-287; theory-framework:ST1-339; theory-unstructured:ST2-359·ST2-370·ST2-406.
- 유지한 수정안 행 ID: theory-framework:ST1-338.
- 넣지 않은 행과 이유: 없음.

### Wetting-drying·처오름

- 대상: [swash-wetting-drying-runup.md](../../../models/SWASH/source-analysis/swash-wetting-drying-runup.md).
- 추가·수정 줄: `models/SWASH/source-analysis/swash-wetting-drying-runup.md:7–8,46–48,81,127,167,171–173,199,211,213,215–219,221–258`.
- 차이 표: `models/SWASH/source-analysis/swash-wetting-drying-runup.md:222–258`.
- 넣은 행 수: 배정표 27행 중 27행.
- 반영한 수정안 행 ID: inputs-physics-numerics:SI2-159·SI2-164; outputs:SO1-299.
- 기존 보류 문장의 근거: guide-syntax-build:SG1-130; inputs-physics-numerics:SI2-243; outputs:SO1-184·SO1-266; theory-unstructured:ST2-358.
- 넣지 않은 행과 이유: 없음.

### 암시적 수심평균 흐름

- 대상: [swash-implicit-depthavg-flow.md](../../../models/SWASH/source-analysis/swash-implicit-depthavg-flow.md).
- 추가·수정 줄: `models/SWASH/source-analysis/swash-implicit-depthavg-flow.md:7–8,29,141–144,146–148,155–158,166–170,211,222–224,254,257,259–290`.
- 차이 표: `models/SWASH/source-analysis/swash-implicit-depthavg-flow.md:260–290`.
- 넣은 행 수: 배정표 21행 중 21행.
- 반영한 수정안 행 ID: theory-framework:ST1-322·ST1-323·ST1-333; theory-unstructured:ST2-365.
- 넣지 않은 행과 이유: 없음.

### SWASH README

- 대상: [models/SWASH/README.md](../../../models/SWASH/README.md).
- 추가·수정 줄: `models/SWASH/README.md:1–5,10–14,27,36,49–50,53–56,61,64–80`.
- 차이 표: `models/SWASH/README.md:65–80`.
- 넣은 행 수: 배정표 6행 중 6행.
- 반영한 수정안 행 ID: inputs-setup:SI1-710; outputs:SO1-297; theory-framework:ST1-330·ST1-331·ST1-332; theory-unstructured:ST2-427·ST2-421; guide-syntax-build:SG1-931·SG1-932.
- 유지한 수정안 행 ID: guide-syntax-build:SG1-933.
- 현황 수량은 대조 보고서의 집계 기준을 명시했다.
- 넣지 않은 행과 이유: 없음.

### 루트 README

- 대상: [README.md](../../../README.md).
- 추가·수정 줄: `README.md:1–5,110–161`.
- 코드 결함 후보 표: `README.md:111–161`.
- 넣은 행 수: 모든 보고서의 최종 E 결론 41행 중 41행.
- 강도 집계: 보고서의 최종 E 결론은 강함 30행·중간 10행·약함 1행이다.
- 내용 문장은 각 보고서의 최종 결론 문장에서 한 문장씩 옮겼다.
- 상세 노트는 각 `SWASH-assign-*.tsv`의 배정 파일을 연결했다.
- 반영한 수정안 행 ID: 루트 README를 가리키는 별도 수정안은 없다.
- E 행 ID: theory-framework:ST1-294·ST1-310·ST1-333; theory-unstructured:ST2-039·ST2-365·ST2-371·ST2-403·ST2-416; inputs-setup:SI1-155·SI1-229·SI1-260·SI1-355·SI1-513·SI1-534·SI1-535·SI1-549·SI1-560·SI1-571; inputs-physics-numerics:SI2-030·SI2-111·SI2-141·SI2-181·SI2-194; outputs:SO1-067·SO1-100·SO1-115·SO1-119·SO1-128·SO1-140·SO1-149·SO1-150·SO1-158·SO1-170·SO1-205·SO1-220·SO1-267·SO1-271; guide-syntax-build:SG1-612·SG1-795·SG1-796; callflow:RF-016.
- 넣지 않은 행과 이유: 없음.

## 최종 확인

- 배정표의 84개 행 ID가 지정된 네 파일의 차이 표와 일치한다.
- 최종 E 결론의 41개 행 ID가 루트 README 표와 일치한다.
- E 표의 강도와 상세 노트 링크가 최종 결론·배정표와 일치한다.
- 원문 인용과 식의 보존 검사를 통과했다.
- 기존 citation_status를 유지했다.
- 지정한 frontmatter 문구를 반영했다.
- 대상 파일의 상대 링크가 존재하는 파일을 가리킨다.
- 대상 파일에 금지된 절대 경로와 위키 링크 문자열이 없다.
- 파일별 추가·수정 줄 범위가 최종 diff와 일치한다.
- 대상 파일의 git diff --check가 통과했다.

### Claude 정정 (10-15)

- 이 작업은 코드 결함 후보 표를 저장소 루트 `README.md`에 넣었다. 지시문이 `models/SWASH/` 접두어 없이 `README.md`라고 적었기 때문이다.
- Claude가 그 절을 `models/SWASH/README.md` 끝으로 옮겼다. 링크는 새 위치 기준 상대 경로로 바꿨다. 루트 `README.md`는 원래 내용으로 되돌렸다.
