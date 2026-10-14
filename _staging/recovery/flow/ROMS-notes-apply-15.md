---
title: "ROMS 대조 결론 노트 반영 — 배정 15"
canonical_source: self
citation_status: verified
last_source_check: "2026-10-14 (recovery 대조 반영)"
verification_method: "2026-10-14 ROMS recovery 대조 보고서 반영"
note_author: "Codex"
note_date: 2026-10-14
verification_by: "Codex — 배정표·보고서·노트 대조"
verification_date: 2026-10-14
---

# ROMS 대조 결론 노트 반영 — 배정 15

[배정표](../assign/note-job-15.tsv)는 주 실행 노트에 128행을 배정한다.
배정표는 bulk flux 노트에 36행을 배정한다.
배정표는 지원 모듈 노트에 24행을 배정한다.
보고서 끝의 전수 검증 기록을 최종 결론으로 적용한다.
파일별 완료 기록은 아래에 덧붙인다.

## roms_main_driver_dispatch.md

- 파일: [roms_main_driver_dispatch.md](../../../models/ROMS/source-analysis/roms_main_driver_dispatch.md).
- 추가·수정 범위: `models/ROMS/source-analysis/roms_main_driver_dispatch.md:1–8`의 frontmatter.
- 추가·수정 범위: `models/ROMS/source-analysis/roms_main_driver_dispatch.md:23–163`의 드라이버 분류·선택·결합·시간 단계·응용 헤더·관련 링크.
- 추가 범위: `models/ROMS/source-analysis/roms_main_driver_dispatch.md:166–339`의 비선형 계산 흐름.
- 추가 범위: `models/ROMS/source-analysis/roms_main_driver_dispatch.md:341–474`의 문서와 코드 차이 표.
- 넣은 행 수: 128행이다.
- 배정표의 이 파일 행 수: 128행이다.
- 반영한 수정안 행 ID: `build-options-history:RBH-3497`, `RBH-3498`, `RBH-3499`, `RBH-3500`, `RBH-3501`, `RBH-3502`, `RBH-3503`.
- 반영한 수정안 행 ID: `coupling-nesting-parallel:RCN-1956`, `RCN-1957`, `RCN-1958`.
- 반영한 수정안 행 ID: `da-4dvar:DA1-807`, `DA1-809`.
- 반영한 수정안 행 ID: `da-representer:RT2-389`.
- 반영한 수정안 행 ID: `callflow-da:RF2-031`과 6.2절의 IS4DVAR 호환 표기 보충.
- 반영한 수정안 행 ID: `callflow-nonlinear:RF1-027`, `RF1-028`.
- 참조 연결을 포함해 반영한 수정안 행 ID: `build-options-history:RBH-3489`, `coupling-nesting-parallel:RCN-1960`, `theory-numerics:RTN-389`, `callflow-nonlinear:RF1-021`.
- Mermaid 블록: 보고서 4절의 3개 블록과 노트의 3개 블록이 동일하다.
- 넣지 않은 배정 행과 이유: 없다.

## roms_bulk_flux_coare.md

- 파일: [roms_bulk_flux_coare.md](../../../models/ROMS/source-analysis/roms_bulk_flux_coare.md).
- 추가·수정 범위: `models/ROMS/source-analysis/roms_bulk_flux_coare.md:6–8`의 frontmatter.
- 추가·수정 범위: `models/ROMS/source-analysis/roms_bulk_flux_coare.md:72–185`의 COARE 선택·Qair 입력·내부 단위·NetCDF 환산·옵션 조건·해빙 강우 식·호출 순서.
- 추가·수정 범위: `models/ROMS/source-analysis/roms_bulk_flux_coare.md:187–218`의 관련 링크·대조 근거.
- 추가 범위: `models/ROMS/source-analysis/roms_bulk_flux_coare.md:220–261`의 문서와 코드 차이 표.
- 넣은 행 수: 36행이다.
- 배정표의 이 파일 행 수: 36행이다.
- 반영한 수정안 행 ID: `build-options-history:RBH-3509`, `RBH-3510`, `RBH-3511`.
- 참조 연결을 포함해 반영한 수정안 행 ID: `build-options-history:RBH-3482`.
- RBH-3511의 한국 운영 일반화 문장은 벌크 구현 설명에서 제거했다.
- 반영한 수정안 행 ID: `mixing-bc-forcing:RMF1-958`, `RMF1-959`, `RMF1-960`, `RMF1-961`, `RMF1-970`.
- 반영한 수정안 행 ID: `outputs-metadata:OMD-N012`, `OMD-N013`, `OMD-N014`.
- OMD-N012·OMD-N013·OMD-N014가 대조한 sensible·latent·evap 출력 표의 세 행은 유지했다.
- 넣지 않은 배정 행과 이유: 없다.

## roms_support_modules.md

- 파일: [roms_support_modules.md](../../../models/ROMS/source-analysis/roms_support_modules.md).
- 추가·수정 범위: `models/ROMS/source-analysis/roms_support_modules.md:2–8`의 frontmatter.
- 추가 범위: `models/ROMS/source-analysis/roms_support_modules.md:30–35`의 float 12열 입력·시작 시각 변환·좌표 변환 조건.
- 수정 범위: `models/ROMS/source-analysis/roms_support_modules.md:41–66`의 주기 경계 복사·MPI halo 교환·초기화·입력 역할.
- 수정 범위: `models/ROMS/source-analysis/roms_support_modules.md:39`와 `:70–86`의 관련 링크.
- 추가 범위: `models/ROMS/source-analysis/roms_support_modules.md:89–118`의 문서와 코드 차이 표.
- 넣은 행 수: 24행이다.
- 배정표의 이 파일 행 수: 24행이다.
- 반영한 수정안 행 ID: `coupling-nesting-parallel:RCN-1983`.
- 반영한 수정안 행 ID: `inputs:RI1-1055`.
- 반영한 수정안 행 ID: `callflow-nonlinear:RF1-026`.
- RI1-1055가 대조한 float 시간 전진·보간·연직 무작위 보행 설명은 유지했다.
- 넣지 않은 배정 행과 이유: 없다.

## 반영 확인

배정표의 고유 행 188개가 지정한 세 파일의 표에 한 번씩 들어갔다.
188개 행의 결론 분류는 보고서의 최종 결론 표와 같다.
결론 문장은 커밋 날짜·강도·백틱 표기를 보충한 뒤에도 보고서의 뜻을 유지한다.
결론 표의 열 수는 각 행에서 6개이다.
A 행의 결론 문장에는 커밋 HASH와 날짜가 있다.
E 행의 결론 문장에는 근거 강도가 있다.
세 노트의 기존 citation_status는 유지했다.
네 파일의 last_source_check와 verification_method는 요청한 날짜·문구를 반영했다.
원문 인용의 위키 링크는 이중 대괄호 안의 문자열을 남겼다.
표에 넣지 않은 배정 행은 없다.
