---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_UpdateTrid_js.md
lines: 23
sha256: 60a45a8e59305710efdc9a4aee7ca3bdc380d46212e1b01aa86206253dd68318
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_UpdateTrid_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_UpdateTrid.js`

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | 원문 링크와 `Update_TriDiag_coef.wgsl`·`Update_TriDiag_coef_COULWAVE.wgsl` 공통 바인드 그룹(bind group) 설명이다(1–7). `0` 계산/삼중대각 uniform, `1` `txBottom`, `2` 변형별 현재 상태 또는 `current_stateUVstar`, `3` 출력 `coefMatx`, `4` 출력 `coefMaty`다(11–15). |
| 17–23 | 시작 시와 바닥/지형 또는 관련 COULWAVE 상태가 새 계수를 필요로 할 만큼 바뀔 때 PCR용 x/y 계수 행렬을 갱신한다(19). COULWAVE는 표준 Boussinesq와 현재 수면·국소 수심 사용이 다르므로 두 셰이더 문서를 공통 handler와 맞추라고 적는다(23). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
