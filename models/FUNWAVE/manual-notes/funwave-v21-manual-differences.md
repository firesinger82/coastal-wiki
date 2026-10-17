---
title: "FUNWAVE-TVD 2.1 매뉴얼의 실행 경로 차이"
model: FUNWAVE
canonical_source: self
citation_status: verified
verification_method: "2026-10-18 FUNWAVE recovery 대조 보고서 반영"
last_source_check: "2026-10-18 (recovery 대조 반영)"
verification_by: "Codex (recovery 보고서 반영)"
verification_date: 2026-10-18
note_author: "Codex"
note_date: 2026-10-18
source_scope: FUNWAVE-TVD
---

# FUNWAVE-TVD 2.1 매뉴얼의 실행 경로 차이

## 1. 범위와 근거

이 노트는 배정된 callflow:RF-018의 세 이름을 다룬다.
문서 범위는 `funwave_tvd_2.1_manual.pdf p.29–31`이다.
근거 보고서는 [FUNWAVE-callflow §5·8](../../../_staging/recovery/flow/FUNWAVE-callflow.md#8-차이-결론)다.
보고서의 최종 전수 검증 기록(10-18)을 반영한다.
커밋 근거는 [FUNWAVE-git-verify-AD1의 RF-018](../../../_staging/recovery/compare/FUNWAVE-git-verify-AD1.md)에 있다.

## 문서와 코드 차이 (10-18 대조)

문서 판: 2.1 매뉴얼 `b9c035d`(2016-11-03). 코드 판: 공개 저장소 `github.com/fengyanshi/FUNWAVE-TVD` HEAD `b4c322e`(2025-01-24), `FUNWAVE-TVD/src/main.F:47` `!    VERSION 3.0`.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-018 | TRIDxyNoParallel·GatherVariable·ScatterVariable | `funwave_tvd_2.1_manual.pdf p.29–31` `TRIDxyNoParallel`, `GatherVariable`, `ScatterVariable` | `cab9425:etauv_solver.F:354` `# if defined (PARALLEL)`; `cab9425:etauv_solver.F:355` `call TRIDx(myA,myC,myD,myF)`; `cab9425:etauv_solver.F:358` `call TRIDx_ser(myA,myC,myD,myF)` | D 문서에만 있음 | TRIDxyNoParallel·GatherVariable·ScatterVariable은 공개 소스 이력의 계산 경로에 없다. [10-18 결론 검증 보완] [10-18 git 이력 판정] |
