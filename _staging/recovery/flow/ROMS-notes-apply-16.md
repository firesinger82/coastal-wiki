# ROMS 대조 보고서의 노트 반영 — 배정 16

배정 근거는 [note-job-16.tsv](../assign/note-job-16.tsv)이다.
반영 근거는 대조 보고서의 수정안과 결론 및 최종 「전수 검증 기록 (10-14)」이다.

## 파일별 반영 기록

### roms_analytical_functionals-differences-1.md

- 파일: [roms_analytical_functionals-differences-1.md](../../../models/ROMS/source-analysis/roms_analytical_functionals-differences-1.md).
- 추가 범위: `models/ROMS/source-analysis/roms_analytical_functionals-differences-1.md:1–166`.
- 표 행 범위: `models/ROMS/source-analysis/roms_analytical_functionals-differences-1.md:33–166`.
- 넣은 행 수: 134행이다. [note-job-16.tsv](../assign/note-job-16.tsv)의 이 파일 배정도 134행이다.
- 수정안에서 차이 표로 옮긴 행 ID: `biology:NT-022`, `build-options-history:RBH-3507`, `mixing-bc-forcing:RMF1-952`, `mixing-bc-forcing:RMF1-949`, `mixing-bc-forcing:RMF1-951`.
- 넣지 않은 배정 행: 없다.

- A 행의 커밋 날짜는 [A7](../compare/ROMS-git-verify-A7.md), [A8](../compare/ROMS-git-verify-A8.md), [D1](../compare/ROMS-git-verify-D1.md)의 커밋 근거를 반영했다.
- `testcases:RT1-538`, `testcases:RT1-547`, `testcases:RT1-548`은 최종 보고서의 A 판정을 반영했다.
- 원문 인용의 위키 링크 마크업은 표시 이름으로 옮겼다.

### roms_grid_metrics.md

- 파일: [roms_grid_metrics.md](../../../models/ROMS/source-analysis/roms_grid_metrics.md).
- frontmatter 범위: `models/ROMS/source-analysis/roms_grid_metrics.md:6–7`.
- 본문 추가·수정 범위: `models/ROMS/source-analysis/roms_grid_metrics.md:28–29`, `models/ROMS/source-analysis/roms_grid_metrics.md:40–42`, `models/ROMS/source-analysis/roms_grid_metrics.md:58–60`, `models/ROMS/source-analysis/roms_grid_metrics.md:101–102`, `models/ROMS/source-analysis/roms_grid_metrics.md:104–113`, `models/ROMS/source-analysis/roms_grid_metrics.md:125–126`, `models/ROMS/source-analysis/roms_grid_metrics.md:130–131`, `models/ROMS/source-analysis/roms_grid_metrics.md:174`, `models/ROMS/source-analysis/roms_grid_metrics.md:176`, `models/ROMS/source-analysis/roms_grid_metrics.md:182–190`, `models/ROMS/source-analysis/roms_grid_metrics.md:193–200`, `models/ROMS/source-analysis/roms_grid_metrics.md:206–209`, `models/ROMS/source-analysis/roms_grid_metrics.md:226`.
- 차이 절 추가 범위: `models/ROMS/source-analysis/roms_grid_metrics.md:228–279`.
- 표 행 범위: `models/ROMS/source-analysis/roms_grid_metrics.md:236–279`.
- 넣은 행 수: 44행이다. [note-job-16.tsv](../assign/note-job-16.tsv)의 이 파일 배정도 44행이다.
- 반영한 수정안 행 ID: `coupling-nesting-parallel:RCN-1977`, `coupling-nesting-parallel:RCN-1978`, `coupling-nesting-parallel:RCN-1979`, `coupling-nesting-parallel:RCN-1980`, `inputs:RI1-1051`, `inputs:RI1-1052`, `inputs:RI1-1053`, `testcases:RT1-1537`, `theory-numerics:RTN-398`, `tools-guides:RTG-1978`, `tools-guides:RTG-1979`, `tools-guides:RTG-1980`.
- `theory-numerics:RTN-398`의 CPP·runtime 구분 문장은 유지했다.
- `tools-guides:RTG-1979`의 pm·pn·pmask 정의는 유지했다.
- `testcases:RT1-1537`의 MPI scaling benchmark 후속 계획은 유지했다.
- 넣지 않은 배정 행: 없다.

### roms_stability_gst.md

- 파일: [roms_stability_gst.md](../../../models/ROMS/source-analysis/roms_stability_gst.md).
- frontmatter 범위: `models/ROMS/source-analysis/roms_stability_gst.md:6–7`, `models/ROMS/source-analysis/roms_stability_gst.md:13–14`.
- 본문 추가·수정 범위: `models/ROMS/source-analysis/roms_stability_gst.md:19`, `models/ROMS/source-analysis/roms_stability_gst.md:36–43`, `models/ROMS/source-analysis/roms_stability_gst.md:53`, `models/ROMS/source-analysis/roms_stability_gst.md:57`, `models/ROMS/source-analysis/roms_stability_gst.md:61–62`.
- 차이 절 추가 범위: `models/ROMS/source-analysis/roms_stability_gst.md:65–98`.
- 표 행 범위: `models/ROMS/source-analysis/roms_stability_gst.md:73–98`.
- 넣은 행 수: 26행이다. [note-job-16.tsv](../assign/note-job-16.tsv)의 이 파일 배정도 26행이다.
- 반영한 수정안 행 ID: `da-4dvar:DA1-808`.
- FTE·AFTE의 고유모드와 OP의 특이벡터를 구분한 기존 표는 유지했다.
- E 행의 강도는 최종 보고서의 강함 판정을 반영했다.
- 기존 위키 링크는 상대 Markdown 링크로 바꿨다.
- 넣지 않은 배정 행: 없다.

## 최종 대조

배정표의 204행은 지정 파일의 차이 표에 각각 한 번씩 있다.
담당 노트를 가리키는 수정안 13행은 보고서의 수정안 절에서 셌다.
이 수정안 13행을 모두 반영했다.
표의 문서 원문·코드 원문 408칸을 보고서의 해당 행과 대조했다.
표의 결론 문장 204칸을 보고서의 최종 결론과 대조했다.
A 행에는 커밋 HASH와 날짜를 넣었다.
E 행에는 근거 강도를 넣었다.
과거 판의 태그 인용은 같은 판의 커밋 HASH 표기로 옮겼다.
복합 결론 문장은 사실별 문장으로 나눴다.
네 파일의 상대 링크 54개는 대상 파일이 있다.
세 노트의 last_source_check는 `2026-10-14 (recovery 대조 반영)`이다.
세 노트의 verification_method에는 `2026-10-14 ROMS recovery 대조 보고서 반영`을 넣었다.
기존 두 노트의 citation_status는 유지했다.
새 노트의 citation_status는 verified이다.
넣지 않은 배정 행은 없다.
반영하지 않은 담당 수정안 행은 없다.
