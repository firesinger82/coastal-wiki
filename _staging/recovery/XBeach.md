# XBeach — 원자료 판독 사실표 (2026-10-02)

원자료: `models/XBeach/raw/` 파일 543개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [XBeach-files.tsv](XBeach-files.tsv).

"노트언급" = `models/XBeach/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 167 | 167 | 0 | 0 | 0 | 0 | 84 |
| 문서 | 78 | 59 | 1 | 0 | 18 | 0 | 19 |
| 웹문서 | 15 | 15 | 0 | 0 | 0 | 0 | 1 |
| 기타(설정·입력·빌드) | 133 | 115 | 6 | 0 | 12 | 0 | 26 |
| 바이너리 | 150 | 0 | 0 | 0 | 150 | 0 | 9 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/trunk/lib` | 172 | 73 | 0 | 0 | 99 | 0 | 15 |
| `source_code/trunk/src` | 129 | 128 | 0 | 0 | 1 | 0 | 82 |
| `source_code/trunk/scripts` | 59 | 6 | 0 | 0 | 53 | 0 | 2 |
| `manuals/readthedocs` | 42 | 40 | 0 | 0 | 2 | 0 | 1 |
| `source_code/trunk/doc` | 37 | 18 | 0 | 0 | 19 | 0 | 17 |
| `source_code/trunk` | 26 | 26 | 0 | 0 | 0 | 0 | 5 |
| `manuals/examples` | 25 | 18 | 7 | 0 | 0 | 0 | 4 |
| `source_code/trunk/config` | 17 | 15 | 0 | 0 | 2 | 0 | 6 |
| `manuals/readthedocs_markdown` | 15 | 15 | 0 | 0 | 0 | 0 | 0 |
| `source_code/trunk/m4` | 10 | 10 | 0 | 0 | 0 | 0 | 2 |
| `source_code/trunk/test` | 6 | 6 | 0 | 0 | 0 | 0 | 1 |
| `manuals/pdfs` | 2 | 0 | 0 | 0 | 2 | 0 | 2 |
| `manuals/reports` | 2 | 0 | 0 | 0 | 2 | 0 | 2 |
| `manuals/refs` | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
