# Celeris — 원자료 판독 사실표 (2026-10-02)

원자료: `models/Celeris/raw/` 파일 995개. 판독 기록: `_staging/total-read/records/`·`model-audit/`(07-19~09). 파일별 목록: [Celeris-files.tsv](Celeris-files.tsv).

"노트언급" = `models/Celeris/` 노트(raw 제외)에 그 파일명이 나옴(이름 일치일 뿐 분석 증거는 아님, 같은 이름 파일은 함께 셈). "LLM판독" = Claude·Codex·grok 이 내용을 읽고 남긴 파일별 기록(질 미검증). "결함감사만" = 파일별 판독 기록은 없고 Codex 결함 감사(`codex-defect-reports/`, 08-29)에서 코어 파일로 다뤄짐. "실패" = 기계 sweep 이 못 읽음(대부분 바이너리). 파서 구조 추출(07-24 적발분)은 판독으로 세지 않음.


## 파일 종류별

| 종류 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 코드 | 279 | 164 | 0 | 0 | 0 | 115 | 138 |
| 문서 | 363 | 160 | 66 | 0 | 4 | 133 | 92 |
| 웹문서 | 9 | 6 | 0 | 0 | 0 | 3 | 0 |
| 기타(설정·입력·빌드) | 146 | 90 | 1 | 0 | 2 | 53 | 69 |
| 바이너리 | 198 | 0 | 1 | 0 | 158 | 39 | 0 |

## 폴더별 (모델 자체 / 외부 라이브러리 / 테스트·예제 구분은 사용자 확정 대상)

| 폴더 | 파일 | LLM판독 | 부분판독 | 결함감사만 | 실패 | 기록없음 | 노트언급 |
|---|--:|--:|--:|--:|--:|--:|--:|
| `source_code/Celeris-WebGPU/examples` | 237 | 133 | 60 | 0 | 39 | 5 | 116 |
| `source_code/Celeris-WebGPU/benchmarks` | 170 | 0 | 0 | 0 | 0 | 170 | 21 |
| `source_code/Celeris-WebGPU/CelerisAgent` | 156 | 0 | 0 | 0 | 0 | 156 | 3 |
| `source_code/Celeris-WebGPU/transect_version` | 149 | 86 | 5 | 0 | 58 | 0 | 66 |
| `source_code/Celeris-WebGPU/docs` | 95 | 88 | 0 | 0 | 3 | 4 | 13 |
| `source_code/Celeris-WebGPU/shaders` | 45 | 43 | 0 | 0 | 0 | 2 | 38 |
| `source_code/Celeris-WebGPU/js` | 37 | 35 | 0 | 0 | 0 | 2 | 35 |
| `source_code/Celeris-WebGPU/skybox` | 27 | 0 | 0 | 0 | 27 | 0 | 0 |
| `source_code/Celeris-WebGPU/textures` | 26 | 0 | 0 | 0 | 26 | 0 | 0 |
| `source_code/Celeris-WebGPU` | 24 | 16 | 0 | 0 | 5 | 3 | 3 |
| `source_code/Celeris-WebGPU/automation` | 10 | 6 | 1 | 0 | 2 | 1 | 2 |
| `source_code/Celeris-WebGPU/automation_edge_browser` | 4 | 2 | 1 | 0 | 1 | 0 | 1 |
| `source_code/Celeris-WebGPU/automation_firefox_browser` | 4 | 2 | 1 | 0 | 1 | 0 | 1 |
| `source_code/Celeris-WebGPU/.github` | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| `source_code/Celeris-WebGPU/assets` | 3 | 1 | 0 | 0 | 2 | 0 | 0 |
| `source_code/Celeris-WebGPU/externals` | 3 | 3 | 0 | 0 | 0 | 0 | 0 |
| `source_code/Celeris-WebGPU/scripts` | 2 | 2 | 0 | 0 | 0 | 0 | 0 |
