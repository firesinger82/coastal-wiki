---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass_Breaking_wgsl.md
lines: 22
sha256: 82276434324e346b9b1dbf51d55f8d9eeb4e58e8fe138e8b604201046fc54017
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass_Breaking_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass_Breaking.wgsl`

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 원문 링크와 Kennedy형 한계에 따른 쇄파 활성·와점성 역할이다(1–7). 현재 상태·바닥·`dU_by_dt`·유량·이전 쇄파를 읽고 `txDissipationFlux`의 점성 가중 운동량 경사, 임시 시간 표식·점성·강도·subgrid placeholder를 쓴다(11–14). |
| 16–22 | `detadt`를 추정한다(18). 국소 수심과 쇄파 경과 시간으로 임계값을 선택한다(18). 쇄파 강도를 계산하여 와점성으로 바꾼다(18). Boussinesq/COULWAVE `Pass3`가 `txDissipationFlux`를 미분해 운동량 확산을 더한다(18). 지배 운동량 방향의 상류 이웃 선택으로 쇄파 상태를 근사 이류하며 물리·거품/추적자 표시에 영향을 준다(22). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
