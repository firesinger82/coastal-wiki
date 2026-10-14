---
title: "ROMS 테스트 사례 — 문서와 코드 차이 (10-14 대조)"
model: ROMS
doc: "ROMS 위키 Test_Cases·SHOREFACE_CASE"
canonical_source: manual
citation_status: verified
verification_method: "ROMS recovery 대조 보고서의 최종 결론·원문 인용을 note-job-3.tsv와 대조. 2026-10-14 ROMS recovery 대조 보고서 반영"
verification_by: "Codex — recovery 보고서 대조"
verification_date: 2026-10-14
last_source_check: "2026-10-14 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-10-14
related:
  - roms-wiki-overview.md
---

# ROMS 테스트 사례 — 문서와 코드 차이 (10-14 대조)

출처: [testcases 대조 보고서](../../../_staging/recovery/compare/roms-testcases-vs-code.md#5-차이-결론), [최종 검증 기록](../../../_staging/recovery/compare/roms-testcases-vs-code.md#전수-검증-기록-10-14).

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| testcases:RT1-275 | Test_Cases 빈 SHOREFACE 표기 | `Test_Cases.wiki:141` `: shore face planar beach test case (empty)`<br>`SHOREFACE_CASE.wiki:7` `The case consists of spectral waves approaching a mild sloping (1/80) plane beach with an oblique angle of incidence. The wave forcing is obtained by first running SWAN separately by specifying a JONSWAP spectrum for 2 m offshore wave height with a peak period of 10 s at an angle of 10 degrees for the incoming wave field. SWAN was configured to use 90 directional bins and 30 frequency bins between 0.04 and 0.5 Hz.`<br>`SHOREFACE_CASE.wiki:14` `Results are shown after the model reaches steady state.` | `ROMS/Include/cppdefs.h:709` `** SHOREFACE           Shore Face Planar Beach Test Case                     **` | B 문서 오기 | SHOREFACE_CASE에는 평면 해빈의 경사와 강제력 및 결과 설명이 있다. |
