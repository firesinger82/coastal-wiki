---
file: models/EFDC/raw/manuals/confluence/spaces/ECIG/pages/Overview/Unit_Testing.md
lines: 34
sha256: e84ad7dec0a2ce0483275aefd9463300fc833f7351d989da0e3a99ea10376428
reader: codex gpt-6.1-sol
read_date: 2026-10-07
---

# Unit_Testing.md — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–9 | 문서 머리말 — 페이지 제목은 Unit Testing이다(3). 페이지 ID, space, URL, 버전, 갱신 시각과 문서 경로를 기록한다(2–8). |
| 10–19 | Tests Created — EFDC 저장소에 특정 코드 부분을 테스트하는 Zofu 단위 테스트(unit testing) 프레임워크를 넣었다고 적는다(10). 프로펠러 후류(propwash) 모듈 테스트는 EFDC 내부 유속장(velocity field)과 Luis가 작성한 유속장을 비교하며 성분 6개를 비교한다고 적는다(14–18). 연결된 Zofu 설명은 이번 판독에서 읽지 않았다. 원문: `    - Compares 6 of the components of the velocity field` (18). |
| 20–34 | Running Tests — EFDC 저장소의 테스트 경로와 run_tests.bat 배치 스크립트로 실행하는 방법을 제시한다(22–31). 수행한 테스트 수와 통과·실패를 보고한다고 적는다(34). 경로와 스크립트 이름을 그대로 옮긴다. 원문: `efdc\zofu_unit_testing\tests` (25); `run_tests.bat` (31). |

## 판독 중 확인된 사실 (판단 아님, 후속 검토 대상)

- 18행: 유속장 성분 6개를 비교한다고 적지만 비교하는 성분의 이름은 이 파일에 없다.

