# FUNWAVE — 원자료 판독 사실표 (2026-10-02)

원자료: `models/FUNWAVE/raw/` 파일 1,376개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [FUNWAVE-files.tsv](FUNWAVE-files.tsv).

"노트언급" = `models/FUNWAVE/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 277 | 34 | 0 | 4 | 0 | 239 | 85 |
| 문서 | 380 | 24 | 17 | 0 | 71 | 268 | 100 |
| 기타(설정·입력·빌드) | 461 | 36 | 0 | 0 | 272 | 153 | 1 |
| 바이너리 | 258 | 9 | 13 | 0 | 226 | 10 | 0 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/FUNWAVE-TVD/simple_cases` | 749 | 0 | 0 | 0 | 410 | 339 | 50 |
| `source_code/FUNWAVE-TVD/benchmarks` | 341 | 38 | 30 | 0 | 61 | 212 | 51 |
| `source_code/FUNWAVE-GPU/src` | 99 | 30 | 0 | 0 | 39 | 30 | 39 |
| `source_code/FUNWAVE-TVD/funwave-work` | 70 | 0 | 0 | 0 | 36 | 34 | 0 |
| `source_code/FUNWAVE-TVD/src` | 42 | 0 | 0 | 4 | 1 | 37 | 36 |
| `source_code/FUNWAVE-TVD/GNUMake` | 27 | 27 | 0 | 0 | 0 | 0 | 0 |
| `source_code/FUNWAVE-TVD` | 15 | 7 | 0 | 0 | 8 | 0 | 1 |
| `source_code/FUNWAVE-TVD/tools` | 13 | 0 | 0 | 0 | 6 | 7 | 5 |
| `source_code/FUNWAVE-GPU/cases` | 8 | 0 | 0 | 0 | 2 | 6 | 1 |
| `source_code/FUNWAVE-TVD/doc` | 5 | 0 | 0 | 0 | 4 | 1 | 2 |
| `source_code/FUNWAVE-TVD/test_bathy` | 5 | 0 | 0 | 0 | 2 | 3 | 1 |
| `manuals` | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| `source_code/FUNWAVE-GPU` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
