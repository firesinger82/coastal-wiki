---
title: "ROMS 전처리 도구 — 문서와 코드 차이 (10-14 대조)"
topic: roms-tools
canonical_source: self
citation_status: verified
verification_method: "확정 보고서의 결론 문장과 원문 인용 대조. 2026-10-14 ROMS recovery 대조 보고서 반영"
note_author: "Codex"
note_date: 2026-10-14
verification_by: "Codex — recovery 보고서 대조"
verification_date: 2026-10-14
last_source_check: "2026-10-14 (recovery 대조 반영)"
related:
  - models/ROMS/manual-notes/roms-wiki-getting-started.md
  - models/ROMS/source-analysis/roms_include_cppdefs.md
---

# ROMS 전처리 도구 — 문서와 코드 차이 (10-14 대조)

AI 정리의 출처는 [빌드·옵션·이력 대조 보고서](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#5-차이-결론)이다.
최종 결론의 기준은 보고서 끝의 `전수 검증 기록 (10-14)`이다.

문서 판: ROMS 위키 wikitext, 2026-05-03 받음, 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json). 코드 판: 원본 저장소 HEAD `57aecf58`, 2026-09-18, roms-4.2 이후 4.3 개발.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| [build-options-history:RBH-3400](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#5-차이-결론) | cpp_clean의 제거 대상 | — | `ROMS/Bin/cpp_clean:35` `   next if /^#/;`<br>`ROMS/Bin/cpp_clean:36` `   next if /^!#/;`<br>`ROMS/Bin/cpp_clean:37` `   next if /^!!/;`<br>`ROMS/Bin/cpp_clean:38` `   next if /^!\$\!/;`<br>`ROMS/Bin/cpp_clean:39` `   next if /^\s*$/;` | C 문서 누락 | 도구는 #·!#·!!·!$!로 시작하는 줄을 건너뛴다. 도구는 빈 줄도 건너뛴다. |
| [build-options-history:RBH-3401](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#5-차이-결론) | cpp_clean의 소스 경로 정규화 | — | `ROMS/Bin/cpp_clean:40` `   if(/".*\/ROMS\/.*(\.F\|\.h)"/){`<br>`ROMS/Bin/cpp_clean:41` `      $_=~s/".*\/ROMS\/(.*)(\.F\|\.h)"/"ROMS\/$1$2"/;` | C 문서 누락 | cpp_clean은 큰따옴표로 둘러싸인 경로가 40행 정규식과 맞으면 /ROMS/ 앞부분을 제거한다. 이 정규식은 경로가 절대 경로인지 검사하지 않는다. [10-14 결론 검증 정정] |
| [build-options-history:RBH-3402](../../../_staging/recovery/compare/roms-build-options-history-vs-code.md#5-차이-결론) | cpp_clean의 연속행 위치 보정 | — | `ROMS/Bin/cpp_clean:43` `   $ind=rindex($_,"&");`<br>`ROMS/Bin/cpp_clean:44` `   if(/\&(\ )*$/ && $ind!=72){`<br>`ROMS/Bin/cpp_clean:46` `      if($ind<72){`<br>`ROMS/Bin/cpp_clean:47` `	      $t=($ind-1)-72;`<br>`ROMS/Bin/cpp_clean:53` `	      substr($_,-2,-$t-1)="$sp&\n";`<br>`ROMS/Bin/cpp_clean:55` `      if($ind>72){`<br>`ROMS/Bin/cpp_clean:56` `	      $t=72-($l);`<br>`ROMS/Bin/cpp_clean:57` `	      substr($_,$t,-$t-1) = "&";` | C 문서 누락 | cpp_clean은 줄 끝의 & 뒤에 공백만 있는 패턴에서 마지막 &의 인덱스를 검사한다. 인덱스가 72와 다르면 인용한 substr 분기로 공백 또는 부분 문자열을 바꾼다. 72는 44행 비교식의 상수이다. [10-14 결론 검증 정정] |
