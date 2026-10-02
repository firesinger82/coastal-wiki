# LISFLOOD-FP — 원자료 판독 사실표 (2026-10-02)

원자료: `models/LISFLOOD-FP/raw/` 파일 1,672개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [LISFLOOD-FP-files.tsv](LISFLOOD-FP-files.tsv).

"노트언급" = `models/LISFLOOD-FP/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 874 | 440 | 0 | 0 | 0 | 434 | 109 |
| 문서 | 116 | 20 | 0 | 0 | 46 | 50 | 2 |
| 기타(설정·입력·빌드) | 586 | 15 | 0 | 0 | 59 | 512 | 13 |
| 바이너리 | 96 | 0 | 0 | 0 | 92 | 4 | 0 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/LISFLOOD-FP/testing` | 671 | 8 | 0 | 0 | 127 | 536 | 12 |
| `source_code/LISFLOOD-FP/cuda` | 493 | 444 | 0 | 0 | 0 | 49 | 67 |
| `source_code/LISFLOOD-FP/windep` | 331 | 0 | 0 | 0 | 37 | 294 | 0 |
| `source_code/LISFLOOD-FP` | 55 | 11 | 0 | 0 | 8 | 36 | 22 |
| `source_code/LISFLOOD-FP/swe` | 33 | 0 | 0 | 0 | 0 | 33 | 16 |
| `source_code/LISFLOOD-FP/postprocess` | 16 | 0 | 0 | 0 | 2 | 14 | 0 |
| `source_code/LISFLOOD-FP/DLL's` | 13 | 0 | 0 | 0 | 13 | 0 | 0 |
| `source_code/LISFLOOD-FP/lisflood2` | 13 | 0 | 0 | 0 | 0 | 13 | 6 |
| `source_code/LISFLOOD-FP/preprocess` | 11 | 0 | 0 | 0 | 0 | 11 | 0 |
| `source_code/LISFLOOD-FP/config` | 10 | 10 | 0 | 0 | 0 | 0 | 0 |
| `source_code/LISFLOOD-FP/test` | 8 | 0 | 0 | 0 | 0 | 8 | 0 |
| `source_code/LISFLOOD-FP/dll_intel` | 7 | 0 | 0 | 0 | 7 | 0 | 0 |
| `source_code/LISFLOOD-FP/rain` | 5 | 0 | 0 | 0 | 0 | 5 | 1 |
| `source_code/LISFLOOD-FP/linuxdep` | 4 | 0 | 0 | 0 | 3 | 1 | 0 |
| `source_code/LISFLOOD-FP/cmake` | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
