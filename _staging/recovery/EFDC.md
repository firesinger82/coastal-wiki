# EFDC — 원자료 판독 사실표 (2026-10-02)

원자료: `models/EFDC/raw/` 파일 10,012개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [EFDC-files.tsv](EFDC-files.tsv).

"노트언급" = `models/EFDC/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 563 | 555 | 0 | 0 | 0 | 8 | 168 |
| 문서 | 737 | 729 | 0 | 0 | 8 | 0 | 14 |
| 기타(설정·입력·빌드) | 748 | 605 | 0 | 0 | 5 | 138 | 5 |
| 바이너리 | 7,964 | 36 | 0 | 0 | 7,928 | 0 | 2 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `manuals/confluence` | 9,308 | 1,313 | 0 | 0 | 7,858 | 137 | 5 |
| `source_code/EFDC-GVC` | 313 | 313 | 0 | 0 | 0 | 0 | 41 |
| `source_code/EFDCPlus_Stable/EFDC` | 256 | 247 | 0 | 0 | 0 | 9 | 132 |
| `source_code/EFDCPlus_Stable/lib` | 57 | 2 | 0 | 0 | 55 | 0 | 1 |
| `source_code/EFDCPlus_Stable/redist` | 37 | 37 | 0 | 0 | 0 | 0 | 0 |
| `source_code/EFDCPlus_Stable/include` | 27 | 4 | 0 | 0 | 23 | 0 | 0 |
| `source_code/EFDCPlus_Stable` | 6 | 6 | 0 | 0 | 0 | 0 | 3 |
| `manuals/pdfs` | 5 | 0 | 0 | 0 | 5 | 0 | 5 |
| `manuals/refs` | 3 | 3 | 0 | 0 | 0 | 0 | 2 |
