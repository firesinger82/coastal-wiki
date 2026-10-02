# Delft3D — 원자료 판독 사실표 (2026-10-02)

원자료: `models/Delft3D/raw/` 파일 19,121개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [Delft3D-files.tsv](Delft3D-files.tsv).

"노트언급" = `models/Delft3D/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 7,436 | 0 | 0 | 33 | 12 | 7,391 | 775 |
| 문서 | 598 | 62 | 0 | 0 | 69 | 467 | 254 |
| 웹문서 | 119 | 104 | 0 | 0 | 0 | 15 | 0 |
| 기타(설정·입력·빌드) | 10,654 | 0 | 0 | 0 | 141 | 10,513 | 29 |
| 바이너리 | 314 | 0 | 0 | 0 | 282 | 32 | 3 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/Delft3D/src` | 9,727 | 118 | 0 | 33 | 302 | 9,274 | 971 |
| `source_code/Delft3D/test` | 7,629 | 2 | 0 | 0 | 70 | 7,557 | 19 |
| `source_code/Delft3D/examples` | 835 | 1 | 0 | 0 | 80 | 754 | 16 |
| `source_code/Delft3D/ci` | 260 | 7 | 0 | 0 | 0 | 253 | 4 |
| `source_code/Delft3D/conan` | 176 | 0 | 0 | 0 | 0 | 176 | 15 |
| `source_code/hydromt_delft3dfm/examples` | 111 | 1 | 0 | 0 | 6 | 104 | 2 |
| `source_code/Delft-FIAT/docs` | 58 | 4 | 0 | 0 | 1 | 53 | 0 |
| `manuals/pdfs` | 37 | 0 | 0 | 0 | 37 | 0 | 28 |
| `source_code/hydromt_delft3dfm/hydromt_delft3dfm` | 36 | 0 | 0 | 0 | 0 | 36 | 0 |
| `source_code/Delft-FIAT/src` | 30 | 0 | 0 | 0 | 0 | 30 | 0 |
| `source_code/Delft3D/tools` | 29 | 2 | 0 | 0 | 0 | 27 | 1 |
| `source_code/hydromt_delft3dfm/docs` | 27 | 16 | 0 | 0 | 2 | 9 | 0 |
| `source_code/Delft3D/.github` | 19 | 1 | 0 | 0 | 0 | 18 | 0 |
| `source_code/Delft-FIAT/.github` | 17 | 1 | 0 | 0 | 0 | 16 | 0 |
| `source_code/Delft3D` | 16 | 1 | 0 | 0 | 0 | 15 | 3 |
| `source_code/Delft3D/doc` | 15 | 6 | 0 | 0 | 5 | 4 | 0 |
| `source_code/Delft-FIAT/.build` | 14 | 0 | 0 | 0 | 0 | 14 | 0 |
| `source_code/Delft-FIAT/test` | 14 | 0 | 0 | 0 | 0 | 14 | 0 |
| `source_code/Delft-FIAT/.archive` | 13 | 0 | 0 | 0 | 1 | 12 | 0 |
| `source_code/Delft-FIAT` | 12 | 2 | 0 | 0 | 0 | 10 | 1 |
| `source_code/hydromt_delft3dfm/.github` | 11 | 1 | 0 | 0 | 0 | 10 | 0 |
| `source_code/hydromt_delft3dfm/tests` | 11 | 0 | 0 | 0 | 0 | 11 | 0 |
| `source_code/Delft3D/.devcontainer` | 9 | 1 | 0 | 0 | 0 | 8 | 1 |
| `source_code/hydromt_delft3dfm` | 7 | 1 | 0 | 0 | 0 | 6 | 0 |
| `source_code/Delft-FIAT/res` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/Delft-FIAT/.testdata` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `source_code/Delft3D/.dvc` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `manuals/refs` | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
