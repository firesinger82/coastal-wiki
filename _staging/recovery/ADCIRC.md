# ADCIRC — 원자료 판독 사실표 (2026-10-02)

원자료: `models/ADCIRC/raw/` 파일 10,725개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [ADCIRC-files.tsv](ADCIRC-files.tsv).

"노트언급" = `models/ADCIRC/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 1,505 | 0 | 0 | 32 | 0 | 1,473 | 139 |
| 문서 | 1,751 | 1,263 | 0 | 0 | 105 | 383 | 132 |
| 웹문서 | 1,086 | 1,086 | 0 | 0 | 0 | 0 | 461 |
| 기타(설정·입력·빌드) | 4,581 | 0 | 0 | 0 | 84 | 4,497 | 370 |
| 바이너리 | 1,802 | 0 | 0 | 0 | 515 | 1,287 | 0 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/asgs/input` | 3,370 | 21 | 0 | 0 | 6 | 3,343 | 15 |
| `manuals/website` | 1,824 | 884 | 0 | 0 | 50 | 890 | 493 |
| `source_code/adcirc/thirdparty` | 962 | 12 | 0 | 0 | 71 | 879 | 14 |
| `manuals/website_markdown` | 884 | 884 | 0 | 0 | 0 | 0 | 0 |
| `source_code/adcirc-testsuite/adcirc` | 767 | 0 | 0 | 0 | 378 | 389 | 316 |
| `manuals/wiki` | 484 | 322 | 0 | 0 | 0 | 162 | 1 |
| `source_code/asgs/output` | 438 | 2 | 0 | 1 | 47 | 388 | 29 |
| `source_code/asgs/t` | 393 | 0 | 0 | 0 | 0 | 393 | 0 |
| `source_code/gahm/thirdparty` | 211 | 18 | 0 | 0 | 3 | 190 | 4 |
| `source_code/adcirc/docs` | 194 | 150 | 0 | 0 | 37 | 7 | 42 |
| `source_code/StormEvents/tests` | 155 | 0 | 0 | 0 | 0 | 155 | 1 |
| `source_code/asgs/doc` | 93 | 22 | 0 | 0 | 42 | 29 | 0 |
| `source_code/asgs/util` | 78 | 0 | 0 | 0 | 0 | 78 | 4 |
| `source_code/adcircpy/tests` | 62 | 0 | 0 | 0 | 0 | 62 | 16 |
| `source_code/adcirc-testsuite/adcirc-swan` | 60 | 0 | 0 | 0 | 22 | 38 | 16 |
| `source_code/adcircpy/adcircpy` | 58 | 0 | 0 | 0 | 0 | 58 | 0 |
| `source_code/adcirc/src` | 56 | 0 | 0 | 31 | 0 | 25 | 49 |
| `source_code/asgs/cloud` | 55 | 0 | 0 | 0 | 0 | 55 | 0 |
| `source_code/asgs` | 47 | 1 | 0 | 0 | 0 | 46 | 13 |
| `source_code/gahm/src` | 45 | 0 | 0 | 0 | 0 | 45 | 22 |
| `source_code/asgs/patches` | 44 | 1 | 0 | 0 | 0 | 43 | 1 |
| `manuals/pdfs` | 42 | 1 | 0 | 0 | 41 | 0 | 31 |
| `source_code/asgs/bin` | 35 | 0 | 0 | 0 | 0 | 35 | 0 |
| `source_code/FigureGen/autotest` | 26 | 0 | 0 | 0 | 4 | 22 | 6 |
| `source_code/asgs/monitoring` | 25 | 0 | 0 | 0 | 0 | 25 | 0 |
| `source_code/asgs/platforms` | 25 | 0 | 0 | 0 | 0 | 25 | 0 |
| `source_code/adcirc/cmake` | 24 | 0 | 0 | 0 | 0 | 24 | 0 |
| `source_code/adcirc/prep` | 18 | 0 | 0 | 0 | 0 | 18 | 9 |
| `source_code/adcircpy/docs` | 18 | 8 | 0 | 0 | 0 | 10 | 1 |
| `source_code/adcirc` | 16 | 4 | 0 | 0 | 0 | 12 | 1 |
| `source_code/adcirc/util` | 16 | 0 | 0 | 0 | 0 | 16 | 0 |
| `source_code/asgs/PERL` | 15 | 0 | 0 | 0 | 0 | 15 | 0 |
| `source_code/StormEvents/stormevents` | 13 | 0 | 0 | 0 | 0 | 13 | 0 |
| `source_code/gahm/tests` | 13 | 0 | 0 | 0 | 0 | 13 | 0 |
| `source_code/gahm` | 10 | 3 | 0 | 0 | 0 | 7 | 1 |
| `source_code/adcirc/.github` | 9 | 3 | 0 | 0 | 0 | 6 | 0 |
| `source_code/asgs/docs` | 9 | 2 | 0 | 0 | 0 | 7 | 0 |
| `source_code/asgs/tides` | 9 | 0 | 0 | 0 | 0 | 9 | 6 |
| `source_code/StormEvents/docs` | 8 | 5 | 0 | 0 | 0 | 3 | 1 |
| `source_code/adcirc/work` | 8 | 0 | 0 | 0 | 0 | 8 | 0 |
| `source_code/adcircpy` | 8 | 1 | 0 | 0 | 0 | 7 | 1 |
| `source_code/asgs/archive` | 8 | 0 | 0 | 0 | 0 | 8 | 0 |
| `source_code/FigureGen` | 7 | 1 | 0 | 0 | 0 | 6 | 1 |
| `source_code/StormEvents` | 7 | 1 | 0 | 0 | 0 | 6 | 1 |
| `source_code/adcirc-testsuite` | 7 | 1 | 0 | 0 | 0 | 6 | 2 |
| `source_code/adcirc/wind` | 7 | 0 | 0 | 0 | 0 | 7 | 2 |
| `source_code/gahm/cmake` | 6 | 0 | 0 | 0 | 0 | 6 | 0 |
| `source_code/FigureGen/container-files` | 5 | 0 | 0 | 0 | 0 | 5 | 0 |
| `source_code/adcircpy/examples` | 5 | 0 | 0 | 0 | 0 | 5 | 0 |
| `source_code/asgs/config` | 5 | 0 | 0 | 0 | 0 | 5 | 0 |
| `source_code/StormEvents/.github` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/adcirc-testsuite/test_runner` | 3 | 0 | 0 | 0 | 0 | 3 | 1 |
| `source_code/adcircpy/.github` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/asgs/READMEs` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/asgs/benchmarking` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/asgs/etc` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/asgs/ssh-servers` | 3 | 0 | 0 | 0 | 0 | 3 | 0 |
| `source_code/gahm/doc` | 3 | 0 | 0 | 0 | 3 | 0 | 0 |
| `source_code/adcirc/scripts` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `source_code/asgs/.github` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `source_code/asgs/my-bin` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `source_code/gahm/.github` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `source_code/gahm/examples` | 2 | 0 | 0 | 0 | 0 | 2 | 0 |
| `manuals/notes` | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| `manuals/refs` | 1 | 1 | 0 | 0 | 0 | 0 | 1 |
| `source_code/FigureGen/cmake` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `source_code/StormEvents/examples` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `source_code/adcirc/.circleci` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `source_code/adcirc/containers` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `source_code/asgs/.vscode` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
