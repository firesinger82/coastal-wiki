---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/site_js.md
lines: 15
sha256: 26aabcfbc12e8cfdb57f3225b47b73e0a3548fbe03630b50a0d603abb2c542b5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# site_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/site.js`

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 현재 활성 simulator 로직을 갖지 않는 placeholder 또는 사이트 template 잔재로 보인다는 설명이다(1–7). [11-04 전수 검증 정정] |
| 9–15 | 현재 소스 트리에서 의미 있는 앱 코드가 실행되지 않으며 실제 로직은 `main.js`와 관련 모듈에 있다고 적는다(11). 이름만으로 진입점이라 가정하지 말고 새 사이트 스크립트는 특별한 이유가 없으면 수치 WebGPU 제어와 분리하라고 적는다(15). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·11: 문서는 `js/site.js`를 현재 비활성 placeholder로 설명한다.
