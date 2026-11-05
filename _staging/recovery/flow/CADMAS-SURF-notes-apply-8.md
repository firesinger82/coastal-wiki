# CADMAS-SURF 노트 반영 8

작업 기준은 [배정표 8](../assign/CADMAS-SURF-note-job-8.tsv)이다.
최종 결론은 배정표가 지정한 결론 검증 파일의 같은 행 ID를 따른다.
대상은 STR 차이 노트와 FEM 이론·입력 노트다.

배정표 행 수는 195개다.
파일별 반영 결과는 각 파일을 마친 뒤 아래에 기록한다.

## STR 차이 노트

파일은 [cadmas-str-manual-differences.md](../../../models/CADMAS-SURF/manual-notes/cadmas-str-manual-differences.md)다.
추가 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-differences.md:1–234`다.
표 행 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-differences.md:40–234`다.
넣은 표 행 수는 배정표의 195행과 같다.
보고서별 행 수는 str-datatable 71행과 str-theory 124행이다.
분류별 행 수는 A 10행, B 58행, C 114행, F 13행이다.
위 개수는 배정표의 행 ID와 새 표의 행 ID를 대조한 값이다.
배정표에서 넣지 않은 행은 없다.
이 파일을 직접 가리키는 별도 노트 수정안 행은 없다.

## FEM 이론·입력 노트

파일은 [cadmas-str-manual-fem-theory-input.md](../../../models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md)다.
frontmatter 수정 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md:2–9`다.
문서 역할·쪽수·근거 안내의 추가·수정 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md:20–31`이다.
FEM 본문과 기존 대조 표의 수정 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md:35–53`이다.
입력 설명의 수정 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md:55–70`이다.
참고문헌·solver 설명의 수정 범위는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md:74–80`이다.
상대 링크 추가 위치는 `models/CADMAS-SURF/manual-notes/cadmas-str-manual-fem-theory-input.md:82`다.
배정표의 차이 표 행은 이 파일에 넣지 않았다.
기존 대조 표의 항목 수는 유지했다.
본문 수정안은 str-theory:KT1-844, str-theory:KT1-845, str-theory:KT1-846, str-theory:KT1-847, str-theory:KT1-848, str-theory:KT1-849, str-theory:KT1-850을 반영했다.
본문 수정안은 str-datatable:KT2-576, str-datatable:KT2-577, str-datatable:KT2-578, str-datatable:KT2-579, str-datatable:KT2-580을 반영했다.
KT1-844와 KT1-850은 문서 역할과 참고문헌 설명에 반영했다.
KT1-844와 KT1-850의 H 분류는 차이 표 행으로 넣지 않았다.
KT2-576은 최종 F 판정에 따라 PDF 쪽과 인쇄 쪽을 병기했다.
기존 citation_status는 verified를 유지했다.
Biot의 기존 source-needed 문장은 코드 대조 사실로 바꿨다.
has_source_needed는 false로 바꿨다.
미반영 수정안 행은 없다.

## 최종 확인

배정표 195행과 새 표 195행의 행 ID·분류가 모두 같다.
새 표에는 중복 행 ID가 없다.
최종 결론 TSV의 분류·보고서 약칭·근거 파일이 배정표와 모두 같다.
새 표 195행의 결론 문장은 최종 근거 파일의 문장과 같다.
새 표 195행의 확인한 원문 참조는 최종 근거 파일의 참조와 같다.
전사 비교는 코드 경로 약칭과 문서 쪽 인용 형식의 정규화를 적용했다.
두 노트의 상대 링크는 모두 존재하는 파일을 가리킨다.
두 노트의 frontmatter는 지정한 last_source_check와 verification_method 문구를 포함한다.
두 노트에는 금지 경로 문자열과 백틱 안쪽의 앞뒤 공백이 없다.
두 노트에는 행 끝 공백이 없다.
기존 노트의 `git diff --check`는 통과했다.
