# ADCIRC 노트 수정 반영 기록 — 묶음 C

작업일: 2026-10-11.

사용자가 지정한 묶음 C 노트에 수정안을 반영했다. 보고서의 `notes/` 경로를 `models/ADCIRC/` 경로로 해석했다. 보고서의 검증 정정·보완 내용을 적용했다.

## 보고서별 반영한 수정안

각 보고서의 행 ID를 한 건으로 센다. 한 행이 여러 노트를 겨냥해도 같은 보고서에서는 한 건으로 센다. 여러 보고서가 같은 문장을 고치도록 지시한 경우 한 번의 수정에 합쳤다. 해당 행 ID는 각 보고서의 집계에 남겼다.

| 보고서 | 반영한 수정안 수 | 행 ID |
|---|---:|---|
| [ADCIRC-fort15-vs-code.md](../compare/ADCIRC-fort15-vs-code.md) | 12 | `C13`, `C14`, `C15`, `C16`, `C17`, `C18`, `C19`, `C20`, `C21`, `C22`, `C23`, `C24` |
| [ADCIRC-inputfiles-vs-code.md](../compare/ADCIRC-inputfiles-vs-code.md) | 9 | `C-15`, `C-16`, `C-17`, `C-19`, `C-20`, `C-21`, `C-22`, `C-23`, `C-24` |
| [ADCIRC-outputs-vs-code.md](../compare/ADCIRC-outputs-vs-code.md) | 0 | 해당 행 없음 |
| [ADCIRC-theory-vs-code.md](../compare/ADCIRC-theory-vs-code.md) | 4 | `C09`, `C10`, `C11`, `C12` |
| [ADCIRC-features-vs-code.md](../compare/ADCIRC-features-vs-code.md) | 17 | `C16`, `C17`, `C18`, `C19`, `C20`, `C21`, `C22`, `C23`, `C24`, `C25`, `C34`, `C35`, `C36`, `C37`, `C38`, `C39`, `C40` |
| [ADCIRC-callflow.md](ADCIRC-callflow.md) | 1 | `F16` |
| 합계 | 43 | 위 행 ID의 합계 |

outputs 보고서의 수정안에는 묶음 C 노트 대상이 없다.

callflow §7.1의 기존 수정안 참조는 아래 비교 보고서 행과 합쳤다. callflow의 새 수정안은 §7.2의 F16만 집계했다.

| callflow §6 항목 | 한 번 반영한 비교 보고서 행 |
|---|---|
| N-MET01 | fort15 C13 |
| N-MET03 | fort15 C15 |
| N-MET04 | fort15 C16 |
| N-SWAN01 | features C34·C35 |
| N-ICE01 | features C18·C24·C25 |
| N-MANUAL01 | theory C12 |

callflow §3·§4·§6의 TIMESTEP 다음 PADCSWAN_RUN 호출 순서를 SWAN 노트의 C34 반영문에 함께 적었다.

theory C15는 보고서가 “수정 불필요”로 판정했다. [기상 외력 노트](../../../models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md)의 대조 전 102–104줄에 있는 Garratt 식과 WindDragLimit=0.0035 설명을 유지했다. 이 행은 반영 건수에 넣지 않았다.

## 원문을 찾지 못해 반영하지 않은 수정안

없음. 반영 대상 행에서 인용한 묶음 C 원문 문장을 모두 찾았다.

## 새로 만든 절

- [models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md](../../../models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md)의 `## 이론 문서와 코드(v56.2.1)의 식 차이`. theory §1.3의 주요 불일치를 표로 정리했다. 표에 문서 위치·원문 식 또는 항·코드 위치·코드 원문을 적었다. v44.XX(2004)와 v56.2.1의 판 차이를 명시했다. 해석은 “해석: …(정적 판독, 실행 미확인)”으로 표시했다.

## 고친 노트

- [models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md](../../../models/ADCIRC/manual-notes/04-theory-pdf-v44xx.md)
- [models/ADCIRC/manual-notes/18-nws13-schema-and-local-jma-msm-branch.md](../../../models/ADCIRC/manual-notes/18-nws13-schema-and-local-jma-msm-branch.md)
- [models/ADCIRC/manual-notes/19-ice-coverage.md](../../../models/ADCIRC/manual-notes/19-ice-coverage.md)
- [models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-met-forcing-implementation.md)
- [models/ADCIRC/source-analysis/adcirc-swan-coupling.md](../../../models/ADCIRC/source-analysis/adcirc-swan-coupling.md)
- [models/ADCIRC/source-analysis/adcirc-tidal-forcing.md](../../../models/ADCIRC/source-analysis/adcirc-tidal-forcing.md)
- [models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md](../../../models/ADCIRC/source-analysis/adcirc_gahm_vortex_model.md)
- [models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md](../../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-foundation.md)
- [models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md](../../../models/ADCIRC/source-analysis/storm-surge/adcirc-storm-surge-nws-families.md)

위 목록의 노트 9개에 `last_source_check: 2026-10-11 (recovery 재판독 대조)`를 넣었다. `citation_status` 값은 유지했다.

코드 인용문을 해당 원문 줄과 대조했다. SWAN 내부 파랑 감쇠와 외부 GAHM C++ 재검증 등 미확인 사항을 “확인하지 않음”으로 표시했다. 내부 조석 마찰의 dominant sink 주장은 출처가 없으므로 `[source-needed]`를 유지했다.

목록 밖 노트는 수정하지 않았다. git을 사용하지 않았다. 모델을 실행하지 않았다. 모델을 컴파일하지 않았다.
