---
title: ROMS 대조 결론 노트 반영 10
canonical_source: self
citation_status: verified
note_author: Codex
note_date: 2026-10-14
verification_by: Codex
verification_date: 2026-10-14
last_source_check: 2026-10-14 (recovery 대조 반영)
verification_method: 2026-10-14 ROMS recovery 대조 보고서 반영
---

# ROMS 대조 결론 노트 반영 10

배정 근거는 [note-job-10.tsv](../assign/note-job-10.tsv)다.
배정표의 차이 행은 퇴적물 노트 134개, 전역 상태 모듈 노트 32개, 추적자 시간전진 노트 17개다.
공식 자료 노트에는 수정안 행만 적용한다.

상태: 완료.

## 퇴적물 노트

파일: [models/ROMS/source-analysis/sediment/roms_sediment.md](../../../models/ROMS/source-analysis/sediment/roms_sediment.md).
추가·수정 줄 범위: `models/ROMS/source-analysis/sediment/roms_sediment.md:6–7`, `models/ROMS/source-analysis/sediment/roms_sediment.md:37`, `models/ROMS/source-analysis/sediment/roms_sediment.md:41–46`, `models/ROMS/source-analysis/sediment/roms_sediment.md:55–58`, `models/ROMS/source-analysis/sediment/roms_sediment.md:84–92`, `models/ROMS/source-analysis/sediment/roms_sediment.md:124–128`, `models/ROMS/source-analysis/sediment/roms_sediment.md:136`, `models/ROMS/source-analysis/sediment/roms_sediment.md:139–142`, `models/ROMS/source-analysis/sediment/roms_sediment.md:156–158`, `models/ROMS/source-analysis/sediment/roms_sediment.md:175–177`, `models/ROMS/source-analysis/sediment/roms_sediment.md:179–180`, `models/ROMS/source-analysis/sediment/roms_sediment.md:182–183`, `models/ROMS/source-analysis/sediment/roms_sediment.md:204`, `models/ROMS/source-analysis/sediment/roms_sediment.md:208–210`, `models/ROMS/source-analysis/sediment/roms_sediment.md:214–216`, `models/ROMS/source-analysis/sediment/roms_sediment.md:218`, `models/ROMS/source-analysis/sediment/roms_sediment.md:225–227`, `models/ROMS/source-analysis/sediment/roms_sediment.md:229–231`, `models/ROMS/source-analysis/sediment/roms_sediment.md:239–241`, `models/ROMS/source-analysis/sediment/roms_sediment.md:244–245`, `models/ROMS/source-analysis/sediment/roms_sediment.md:247`, `models/ROMS/source-analysis/sediment/roms_sediment.md:249–254`, `models/ROMS/source-analysis/sediment/roms_sediment.md:270–411`.
넣은 차이 행 수: 134개. 배정표의 이 파일 행 수는 134개다.
반영한 수정안 행 ID: biology:NT-010; mixing-bc-forcing:RMF1-966, RMF1-967, RMF1-971; outputs-metadata:OMD-N034; sediment-ice-vegetation:RN1-018, RN1-019, RN1-020, RN1-021, RN1-022, RN1-023, RN1-024, RN1-025, RN1-026, RN1-027, RN1-028, RN1-029, RN1-030, RN1-031, RN1-032, RN1-033, RN1-034; testcases:RT1-1529, RT1-1530.
넣지 않은 배정 행: 없음.
반영하지 않은 수정안 행: 없음.

## 전역 상태 모듈 노트

파일: [models/ROMS/source-analysis/roms_global_state_modules.md](../../../models/ROMS/source-analysis/roms_global_state_modules.md).
추가·수정 줄 범위: `models/ROMS/source-analysis/roms_global_state_modules.md:7–8`, `models/ROMS/source-analysis/roms_global_state_modules.md:21`, `models/ROMS/source-analysis/roms_global_state_modules.md:25–27`, `models/ROMS/source-analysis/roms_global_state_modules.md:58–62`, `models/ROMS/source-analysis/roms_global_state_modules.md:84–87`, `models/ROMS/source-analysis/roms_global_state_modules.md:89–90`, `models/ROMS/source-analysis/roms_global_state_modules.md:92–99`, `models/ROMS/source-analysis/roms_global_state_modules.md:103–105`, `models/ROMS/source-analysis/roms_global_state_modules.md:108–111`, `models/ROMS/source-analysis/roms_global_state_modules.md:115`, `models/ROMS/source-analysis/roms_global_state_modules.md:154–157`, `models/ROMS/source-analysis/roms_global_state_modules.md:165–169`, `models/ROMS/source-analysis/roms_global_state_modules.md:176`, `models/ROMS/source-analysis/roms_global_state_modules.md:183–185`, `models/ROMS/source-analysis/roms_global_state_modules.md:188`, `models/ROMS/source-analysis/roms_global_state_modules.md:194`, `models/ROMS/source-analysis/roms_global_state_modules.md:198`, `models/ROMS/source-analysis/roms_global_state_modules.md:204`, `models/ROMS/source-analysis/roms_global_state_modules.md:210–212`, `models/ROMS/source-analysis/roms_global_state_modules.md:229`, `models/ROMS/source-analysis/roms_global_state_modules.md:234–237`, `models/ROMS/source-analysis/roms_global_state_modules.md:239`, `models/ROMS/source-analysis/roms_global_state_modules.md:241–280`.
넣은 차이 행 수: 32개. 배정표의 이 파일 행 수는 32개다.
반영한 수정안 행 ID: biology:NT-024; build-options-history:RBH-3506; da-4dvar:DA1-810; inputs:RI1-1054; outputs-metadata:OMD-N031, OMD-N032, OMD-N033, OMD-N049; testcases:RT1-1534, RT1-1535; theory-numerics:RTN-371, RTN-372, RTN-383, RTN-391; callflow-nonlinear:N-04, RF1-032.
넣지 않은 배정 행: 없음.
반영하지 않은 수정안 행: 없음.

## 추적자 시간전진 노트

파일: [models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md](../../../models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md).
추가·수정 줄 범위: `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:2`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:6–7`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:21–22`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:24`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:26–33`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:35`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:37`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:39–43`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:45–49`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:52–53`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:60–66`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:73–75`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:78–80`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:86–91`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:94–96`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:102–105`, `models/ROMS/source-analysis/roms_tracer_timestep_step3d_t.md:108–132`.
넣은 차이 행 수: 17개. 배정표의 이 파일 행 수는 17개다.
반영한 수정안 행 ID: inputs:RI1-1056; theory-numerics:RTN-375, RTN-384, RTN-386, RTN-387, RTN-392; callflow-nonlinear:RF1-024.
넣지 않은 배정 행: 없음.
반영하지 않은 수정안 행: 없음.

## 공식 자료 노트

파일: [models/ROMS/web-refs/roms-official-resources.md](../../../models/ROMS/web-refs/roms-official-resources.md).
추가·수정 줄 범위: 없음.
넣은 차이 행 수: 0개. 배정표의 이 파일 행 수는 0개다.
수정안 행 ID: 없음.
보고서의 수정안 절에 이 파일을 가리키는 행이 없어 원문을 유지했다.
차이 절은 추가하지 않았다.
넣지 않은 배정 행: 없음.

## 최종 확인

배정표의 183행과 세 노트의 차이 표 183행이 일치한다.
행 ID의 누락과 중복은 없다.
각 표의 열 수는 6개다.
A 행의 결론 문장에는 git 판정의 커밋 HASH와 날짜가 있다.
E 행의 결론 문장에는 근거 강도가 있다.
추가·수정한 파일의 링크는 상대 경로다.
추가·수정한 파일의 frontmatter는 지정한 대조 날짜와 반영 방법을 포함한다.
기존 노트의 citation_status는 유지했다.
넣지 않은 배정 행과 반영하지 않은 수정안 행은 없다.
