# XBeach 차이 결론 노트 반영 기록

작성일: 2026-10-12.
입력은 [XBeach 매뉴얼·보고서와 소스코드 대조 §5](../compare/XBeach-manual-vs-code.md#5-차이-결론)이다.
집계 단위는 §5 결론표의 행 ID이다.
1068행은 총괄행으로 집계한다.
E 행의 결함 후보 표 기재는 반영 행 수에 중복으로 세지 않는다.

재개 시작 때 아래 노트에는 결론 문장과 결함 후보 표가 이미 있었다.
이번 실행은 노트 현재 내용을 다시 읽었다.
이번 실행은 기존 반영을 유지했다.
이번 실행은 이 반영 기록 파일을 새로 작성했다.

## 보고서별 반영 행 수

아래 수치는 입력 보고서 §5 결론표에서 센 값이다.

| 보고서 | 반영 행 수 | 분류별 반영 행 수 | 넣지 않은 X·G 행 수 |
|---|---|---|---|
| `XBeach-manual-vs-code.md` §5 | 9 | B 문서 오기 5, C 문서 누락 2, E 코드 결함 후보 2 | X 0, G 0 |

같은 결론표의 A·D·F·H 행은 각각 0개다.
A 판 차이 행이 없으므로 문서 판과 코드 판을 적는 줄은 추가하지 않았다.
308행의 `[10-12 G 재판정]`은 최종 분류 E 코드 결함 후보를 가리킨다.
524행은 `[10-12 결론 정정]`에 따른 E 코드 결함 후보로 반영되어 있다.

## 행별 반영 위치

아래 줄 번호는 이번 실행에서 노트 현재 내용을 읽어 확인한 위치다.
결론 문장에는 분류 이름과 보고서의 노트용 결론 문장이 붙어 있다.
각 위치에는 경로와 줄 번호를 붙인 백틱 원문 인용이 있다.
입력 보고서 행 ID를 인용한 기존 문서와 코드 차이 표는 없었다.
기존 문장에 붙인 결론을 확인했다.

| 보고서 행 ID | 최종 결론 | 결론 문장 위치(노트:줄) | 코드 결함 후보 표 위치(노트:줄) |
|---|---|---|---|
| 295 (A절) | C 문서 누락 | `models/XBeach/source-analysis/xbeach_vegetation.md:71` | 해당 없음 |
| 308 (A절) | E 코드 결함 후보 | `models/XBeach/source-analysis/xbeach_vegetation.md:70` | `models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md:112` |
| 510 (B절) | C 문서 누락 | `models/XBeach/source-analysis/xbeach_vegetation.md:72` | 해당 없음 |
| 524 (B절) | E 코드 결함 후보 | `models/XBeach/source-analysis/xbeach_vegetation.md:73` | `models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md:113` |
| 1068 (C절 총괄) | B 문서 오기 | `models/XBeach/source-analysis/xbeach_nonh.md:52` | 해당 없음 |
| 1075 (C절 표) | B 문서 오기 | `models/XBeach/source-analysis/xbeach_nonh.md:66` | 해당 없음 |
| 1077 (C절 표) | B 문서 오기 | `models/XBeach/source-analysis/xbeach_nonh.md:67` | 해당 없음 |
| 1079 (C절 표) | B 문서 오기 | `models/XBeach/source-analysis/xbeach_nonh.md:54` | 해당 없음 |
| 1080 (C절 표) | B 문서 오기 | `models/XBeach/source-analysis/xbeach_nonh.md:65` | 해당 없음 |

## 넣지 않은 X·G 행 목록

X 행은 없다.
G 행은 없다.
이 목록은 입력 보고서 §5의 최종 결론표를 기준으로 한다.

## 코드 결함 후보 절

절 위치는 `models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md:106`이다.
표의 데이터 행 수는 2개다.
이 수치는 해당 절의 표에서 센 값이다.
출처 보고서 행 ID는 308과 524다.
두 행에는 자기 주석과 다른 코드 경로의 원문 근거가 있다.
두 행에는 영향 범위와 근거 강도의 이유가 있다.
의도된 변경 주석으로 설명되어 제외한 E 행은 없다.
절 첫머리는 사용자가 지정한 문구와 일치한다.

## 고친 노트 목록

아래 목록은 재개 시작 때 이미 고쳐져 있던 결론 반영 노트다.
이번 실행은 이 노트들에 새 본문 수정을 하지 않았다.
각 노트의 `last_source_check`는 `2026-10-12 (recovery 차이 결론 반영)`이다.
각 노트의 `citation_status`는 재개 시작 때의 값을 유지했다.

| 노트 | 결론 반영 위치 | citation_status |
|---|---|---|
| `models/XBeach/source-analysis/xbeach_vegetation.md` | 70·71·72·73행 | `verified` |
| `models/XBeach/source-analysis/xbeach_nonh.md` | 52·54·65·66·67행 | `verified` |
| `models/XBeach/source-analysis/xbeach-coupled-physics-contracts.md` | 106행의 절과 112·113행의 표 | `draft-unsourced` |

## 확인 범위

§5 결론표의 9개 행 ID 모두에 결론 문장 위치가 있다.
각 결론 문장은 해당 행의 분류 이름과 노트용 결론 문장에 일치한다.
보고서 행 ID를 인용한 노트의 문장과 결함 후보 표에서 경로·줄·원문 인용 76건을 추출했다.
이 76건의 인용 문구는 지정한 원문 줄에 모두 있다.
이 대조는 인용 위치와 문구를 확인한 것이다.
이번 실행은 결함의 실제 수치 영향을 확인하지 않았다.
이번 실행은 모델을 실행하거나 컴파일하지 않았다.
이번 실행은 git 상태를 바꾸는 명령을 실행하지 않았다.
