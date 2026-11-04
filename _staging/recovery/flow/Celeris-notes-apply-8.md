---
title: "Celeris 노트 대조 반영 — 배정 8"
citation_status: verified
last_source_check: "2026-11-04 (recovery 대조 반영)"
verification_method: "2026-11-04 Celeris recovery 대조 보고서 반영"
---

# Celeris 노트 대조 반영 — 배정 8

배정 근거는 [Celeris-note-job-8.tsv](../assign/Celeris-note-job-8.tsv)다.
최종 결론은 배정표에 지정된 근거 파일의 같은 행 ID를 따른다.
아래 기록은 두 대상 노트의 최종 반영 내역이다.

## celeris-boussinesq-solver.md

대상은 [celeris-boussinesq-solver.md](../../../models/Celeris/source-analysis/celeris-boussinesq-solver.md)다.
배정표의 이 파일 대상 행 수는 71개다.
차이 표에 넣은 행 수는 71개다.
차이 표의 행 범위는 `models/Celeris/source-analysis/celeris-boussinesq-solver.md:273–343`이다.
절 제목·비교 판·표 머리의 범위는 `models/Celeris/source-analysis/celeris-boussinesq-solver.md:267–272`이다.
frontmatter 수정 범위는 `models/Celeris/source-analysis/celeris-boussinesq-solver.md:5–6`이다.
본문 추가·수정 범위는 `models/Celeris/source-analysis/celeris-boussinesq-solver.md:19–22,80–82,93–108,125–129,173–174,201,218–237,260–264`이다.

반영한 수정안 행 ID는 다음과 같다.

- tavakkol2017: CP1-141·142·143·150·160.
- tavakkol2020: CP2-168. AB3·AM4 계수 설명은 유지했다. Base 논문과 현행 기본 경로의 구분을 덧붙였다.
- lynett2026: CP3-003·028·031·034–036. 기존 차분·계수 전사는 유지했다. 단일 보정 호출을 덧붙였다.
- docs-architecture: CD1-1338. 방향별 해 복사 설명은 유지했다.
- docs-source: CD2-465·466. Pass1·Pass2 역할과 계수 갱신 조건을 고쳤다. AB·AM 계수와 x 다음 y의 순서는 유지했다.
- transect: CT1-358. 최종 근거의 조건·식·강도를 본문에 덧붙였다. 배정표 밖의 행이므로 차이 표에는 넣지 않았다.
- callflow: RF-023·015·014. 계수 갱신 조건과 도함수 시각을 반영했다. Bous 적분·PCR 유지 행의 기존 설명은 보존했다. Claude 렌더 확인 절의 분산 모델 조건은 계수·호출 설명에 적용했다.

넣지 않은 배정 행은 없다.

## celeris-source-map.md

대상은 [celeris-source-map.md](../../../models/Celeris/source-analysis/celeris-source-map.md)다.
배정표의 이 파일 대상 행 수는 47개다.
차이 표에 넣은 행 수는 47개다.
차이 표의 행 범위는 `models/Celeris/source-analysis/celeris-source-map.md:239–285`이다.
절 제목·비교 판·표 머리의 범위는 `models/Celeris/source-analysis/celeris-source-map.md:233–238`이다.
frontmatter의 5–6행은 요청한 값이 이미 있으므로 유지했다.
본문 추가·수정 범위는 `models/Celeris/source-analysis/celeris-source-map.md:33–35,47–53,66–79,85,123,177–198,231`이다.
기존에 반영된 본문 정정의 범위는 `models/Celeris/source-analysis/celeris-source-map.md:15,27–31,55–63`이다.

반영한 수정안 행 ID는 다음과 같다.

- tavakkol2017: CP1-138·153. 기존 AB3·AM4 명칭과 보조 저장 층 설명을 유지했다. 기존 단일 보정과 교차항 시간 가중 설명을 유지했다.
- tavakkol2020: CP2-166. 기존 시간 적분 선택 설명을 유지했다.
- lynett2026: CP3-041·090·099·108. 기존 기준판·Pass2·f16 호출 인용 정정을 유지했다.
- docs-architecture: CD1-1359–1380. 기존 호출표 정정에 최종 근거의 Pass0 보정 호출과 호출 조건을 반영했다. CD1-1378의 기존 f16 호출 인용도 유지했다. CD1-1378은 배정표 밖의 행이므로 차이 표에는 넣지 않았다.
- docs-source: CD2-461·462. 세 방정식 계열과 구면 NLSW 제한 설명은 유지했다. 기존 COULWAVE 저장 층 정정을 유지했다. 배정 행 CD2-459의 현행 파일 수와 과거 수집 기록을 구분했다.
- transect: CT1-356. 기존 본판 HLLC와 단면판 HLLEM 구분을 유지했다.
- callflow: RF-013·009·015. 현재 줄 번호를 유지하고 최종 호출 조건을 덧붙였다. 두 번째 경계 호출의 분산 모델 조건을 반영했다. 도함수 시각을 덧붙였다. 본판 모드·PCR 유지 행에는 단면판 링크를 덧붙였다. Claude 렌더 확인 절의 분산 모델·퇴적물 호출 조건을 호출표에 적용했다.

넣지 않은 배정 행은 없다.

## 최종 확인

배정표의 118행과 두 노트 차이 표의 118행을 대조했다.
배정 행의 누락은 0개다.
배정 행의 중복은 0개다.
차이 표의 배정 외 행은 0개다.
최종 결론표와 근거 파일의 분류가 두 노트의 분류와 같다.
결론 문장은 인용 형식과 경로 표기를 정규화하여 근거 파일과 대조했다.
CP2-052의 조사 범위 문장은 한계 문장을 넣지 말라는 사용자 규칙에 따라 옮기지 않았다.
CP2-052의 Base 구조 설명과 판 구분은 반영했다.
근거 파일의 확인한 원문 인용은 두 노트의 문서 원문·코드 원문 칸에서 대응한다.
A 행은 결론 문장에 문서 판 또는 근거 커밋을 포함한다.
E 행은 결론 문장에 강도를 포함한다.
노트 자기 줄 인용은 반영 전 커밋 d8157c80을 사용한다.
두 노트의 상대 파일 링크는 모두 존재한다.
Markdown 파서는 두 차이 표를 각각 71행과 47행의 6열 표로 읽는다.
두 노트의 last_source_check는 요청한 값이다.
두 노트의 기존 citation_status는 verified로 유지했다.
두 노트의 verification_method는 요청한 구절을 포함한다.
두 노트의 금지 문자열 검사는 통과했다.
두 노트의 git diff 공백 오류 검사는 통과했다.
