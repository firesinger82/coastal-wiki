# ADCIRC 노트 묶음 B 수정 기록

작성일: 2026-10-11.

## 보고서별 반영한 수정안

아래 수는 묶음 B 노트를 겨냥한 수정안 행을 센 값이다. 한 행이 여러 노트 또는 여러 원문 줄을 지정해도 한 번 센다. 같은 원문에 겹친 수정안은 한 번 교체하고 각 보고서의 행 ID로 기록했다. 유지 판정은 원문을 보존하고 근거를 추가한 행으로 센다. 출력 보고서 §4.1의 묶음 ID는 표의 한 행을 한 수정안으로 센다. 아래 표의 합계는 86개다.

| 보고서 | 반영한 수정안 수 | 행 ID 목록 |
|---|---:|---|
| [ADCIRC-fort15-vs-code.md](../compare/ADCIRC-fort15-vs-code.md) | 12 | `C01`, `C03`, `C04`, `C05`, `C06`, `C07`, `C08`, `C09`, `C10`, `C11`, `C12`, `C25` |
| [ADCIRC-inputfiles-vs-code.md](../compare/ADCIRC-inputfiles-vs-code.md) | 29 | `C-01`, `C-03`, `C-04`, `C-05`, `C-06`, `C-07`, `C-08`, `C-09`, `C-10`, `C-11`, `C-12`, `C-13`, `C-15`, `C-17`, `C-18`, `C-20`, `C-23`, `C-24`, `C-25`, `C-26`, `C-27`, `C-29`, `C-30`, `C-31`, `C-32`, `C-33`, `C-35`, `C-36`, `C-37` |
| [ADCIRC-outputs-vs-code.md](../compare/ADCIRC-outputs-vs-code.md) | 31 | `N01`, `N02`, `N03`, `N04`, `N05`, `N06`, `N07`, `N08`, `N09`, `N10`, `N11`, `N12`, `N13`, `N14`, `N15`, `N16`, `N17`, `N18`, `N19`, `N21`, `N22`, `N23`, `N24`, `D02–D04, D08–D10, D12–D13`, `D14–D21, D44, D66`, `D22–D26`, `D27–D30, D35–D38`, `D32–D34, D39–D41, D67`, `D42, D47, D60`, `D48–D55, D57, D63`, `D61, D64–D65와 코드 전용 schema` |
| [ADCIRC-theory-vs-code.md](../compare/ADCIRC-theory-vs-code.md) | 4 | `C04`, `C07`, `C13`, `C14` |
| [ADCIRC-features-vs-code.md](../compare/ADCIRC-features-vs-code.md) | 7 | `C13`, `C14`, `C15`, `C26`, `C41`, `C42`, `C43` |
| [ADCIRC-callflow.md](../flow/ADCIRC-callflow.md) | 3 | `F17`, `F18`, `F19` |

출력 보고서의 31개는 §4의 N 행 23개와 §4.1의 추가안 행 8개다. callflow §7.1의 대조 보고서 ID 포인터는 위 해당 보고서 행으로 반영했다. 그 포인터를 callflow의 새 수정안 수에 더하지 않았다. callflow의 3개는 §7.2의 F17·F18·F19다.

## 찾지 못해 반영하지 않은 수정안

없음. 위 표에 포함한 수정안의 원문 문장을 모두 찾았다. 코드 블록에 대한 추가 인용은 닫는 백틱 다음 줄에 두었다. 여러 줄을 묶은 추가안은 해당 원문 묶음의 첫 줄 또는 마지막 줄 다음에 두었다.

보류·미검증·코드에서 찾지 못한 판정은 해당 노트에서 “확인하지 않음”으로 표시했다. 실행 결과의 근거가 없는 손상·표류·주파수 누락 단언을 삭제했다. 해당 결과의 source-needed 표시는 남겼다.

## 새로 만든 절

| 노트 | 새 절 |
|---|---|
| [source-analysis/adcirc-fort-files-reference.md](../../../models/ADCIRC/source-analysis/adcirc-fort-files-reference.md) | fort.22 NWS별 입력 형식 대조 (v56.2.1) |
| [source-analysis/adcirc-fort-files-reference.md](../../../models/ADCIRC/source-analysis/adcirc-fort-files-reference.md) | 문서와 코드(v56.2.1) 입력이 다른 곳 |
| [source-analysis/adcirc-output-writers-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md) | netCDF 변수 이름과 정의 원문 (v56.2.1) |
| [source-analysis/adcirc-output-writers-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md) | XDMF Information과 경계 자료 (v56.2.1) |
| [source-analysis/adcirc-output-writers-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md) | 문서와 코드(v56.2.1) 출력이 다른 곳 |

입력 차이 절은 fort.15 보고서 §1의 주요 불일치와 입력 파일 보고서 §1이 가리키는 불일치 행을 옮겼다. 출력 차이 절은 출력 보고서 §1의 불일치 유형을 모두 옮겼다. 문서 위치·코드 위치·원문과 최종 판정 이유를 표에 넣었다. 문서 판 차이의 이유를 유지했다.

## 고친 노트

아래 14개 노트만 고쳤다. 각 노트의 frontmatter에 `last_source_check: 2026-10-11 (recovery 재판독 대조)`를 추가했다. 기존 citation_status 값을 유지했다. README에는 frontmatter가 없었으므로 last_source_check만 담은 frontmatter를 추가했다.

| 노트 | 해당 보고서 수정안 |
|---|---|
| [README.md](../../../models/ADCIRC/README.md) | ADCIRC-fort15: `C25`; ADCIRC-inputfiles: `C-24`; ADCIRC-theory: `C14`; ADCIRC-features: `C26` |
| [manual-notes/05-input-files-reference.md](../../../models/ADCIRC/manual-notes/05-input-files-reference.md) | ADCIRC-inputfiles: `C-11`, `C-29`, `C-36` |
| [manual-notes/06-parameter-definitions.md](../../../models/ADCIRC/manual-notes/06-parameter-definitions.md) | ADCIRC-theory: `C13` |
| [manual-notes/14-fort14-grid-bathymetry-boundaries.md](../../../models/ADCIRC/manual-notes/14-fort14-grid-bathymetry-boundaries.md) | ADCIRC-inputfiles: `C-01` |
| [manual-notes/16-bathymetry-and-subgrid-paths.md](../../../models/ADCIRC/manual-notes/16-bathymetry-and-subgrid-paths.md) | ADCIRC-inputfiles: `C-27`, `C-35` |
| [manual-notes/17-boundary-and-forcing-inputs.md](../../../models/ADCIRC/manual-notes/17-boundary-and-forcing-inputs.md) | ADCIRC-inputfiles: `C-12`, `C-25` |
| [source-analysis/adcirc-bathymetry-input-foundation.md](../../../models/ADCIRC/source-analysis/adcirc-bathymetry-input-foundation.md) | ADCIRC-inputfiles: `C-27`, `C-35`; ADCIRC-features: `C43` |
| [source-analysis/adcirc-fort-files-reference.md](../../../models/ADCIRC/source-analysis/adcirc-fort-files-reference.md) | ADCIRC-fort15: `C03`, `C04`, `C05`, `C06`, `C07`, `C08`; ADCIRC-inputfiles: `C-03`, `C-13`, `C-15`, `C-17`, `C-18`, `C-20`, `C-23`, `C-25`, `C-26`, `C-29`; ADCIRC-outputs: `N15`, `N16`, `N17`, `N18`, `N19`, `N24`, `D02–D04, D08–D10, D12–D13` |
| [source-analysis/adcirc-hotstart.md](../../../models/ADCIRC/source-analysis/adcirc-hotstart.md) | ADCIRC-fort15: `C12`; ADCIRC-inputfiles: `C-31`, `C-32`, `C-33`, `C-37`; ADCIRC-outputs: `N10`, `N11`, `N12`, `N13`, `N14`, `N21`, `D48–D55, D57, D63`; ADCIRC-callflow: `F19` |
| [source-analysis/adcirc-nodal-attributes.md](../../../models/ADCIRC/source-analysis/adcirc-nodal-attributes.md) | ADCIRC-inputfiles: `C-03`, `C-04`, `C-05`, `C-06`, `C-07`, `C-08`, `C-09`, `C-10`, `C-35`; ADCIRC-theory: `C07`; ADCIRC-features: `C13`, `C14`, `C15` |
| [source-analysis/adcirc-output-writers-implementation.md](../../../models/ADCIRC/source-analysis/adcirc-output-writers-implementation.md) | ADCIRC-fort15: `C09`, `C10`, `C11`; ADCIRC-outputs: `N01`, `N02`, `N03`, `N04`, `N05`, `N06`, `N07`, `N08`, `N09`, `N22`, `N23`, `D14–D21, D44, D66`, `D22–D26`, `D27–D30, D35–D38`, `D32–D34, D39–D41, D67`, `D42, D47, D60`, `D61, D64–D65와 코드 전용 schema`; ADCIRC-callflow: `F17`, `F18` |
| [source-analysis/adcirc-parameter-glossary-v1.md](../../../models/ADCIRC/source-analysis/adcirc-parameter-glossary-v1.md) | ADCIRC-fort15: `C01`; ADCIRC-theory: `C04` |
| [source-analysis/adcirc-preprocessing-foundation.md](../../../models/ADCIRC/source-analysis/adcirc-preprocessing-foundation.md) | ADCIRC-inputfiles: `C-30` |
| [source-analysis/adcirc-topic-map.md](../../../models/ADCIRC/source-analysis/adcirc-topic-map.md) | ADCIRC-features: `C41`, `C42` |

## 확인한 범위

수정안의 원문 위치와 반영 행 ID를 대조했다. 새 인용의 경로·줄 번호·백틱 원문을 입력 보고서와 대조했다. Markdown 표의 열 수와 코드 블록 경계를 확인했다. frontmatter를 읽어 last_source_check 값을 확인했다. citation_status의 변경이 없는지 확인했다. 허용 목록 중 나머지 노트는 준비 시점의 내용과 같음을 확인했다.

git을 사용하지 않았다. ADCIRC 모델을 실행하지 않았다. ADCIRC를 컴파일하지 않았다.
