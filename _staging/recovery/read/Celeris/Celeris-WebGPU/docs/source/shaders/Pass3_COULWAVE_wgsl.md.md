---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass3_COULWAVE_wgsl.md
lines: 31
sha256: b15fbfd7ee3e55887eb98c31af9b1e6529fb86f8fd56b2d3e2f171120823baf7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass3_COULWAVE_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass3_COULWAVE.wgsl`

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). 공통 `Pass3` 배치의 주 COULWAVE 적분이며 `txCW_groupings`의 보조층을 읽는다(1–7). `Pass3A_COULWAVE`·`Pass3B_COULWAVE` 출력의 속도·수직좌표·S/T·E·F/G를 JavaScript가 `3D` 텍스처(texture)로 복사한다(11). 보조층은 고차 COULWAVE source term을 추가하기 위해 읽는다(7). [11-04 전수 검증 보완] |
| 13–31 | 항은 `txXFlux`·`txYFlux` 발산, friction/Manning·압력/수심 변화·쇄파 확산·스칼라 확산/감쇠, 질량 `E_src`, 운동량 `Psi1x`, `Psi2x`, `Psi1y`, `Psi2y`다(15–23). 출력은 `Pass3_Bous`와 같은 새 상태·미분·F/G 이력·암시 우변 `current_stateUVstar`다(27). 변경 시 보통 `Pass3A_COULWAVE`, `Pass3B_COULWAVE`, `Update_TriDiag_coef_COULWAVE`, PCR 변형·JavaScript 층 복사 순서를 함께 수정해야 한다(31). [11-04 전수 검증 정정] 원문은 이 shader가 프로젝트에서 가장 긴밀하게 결합된 WGSL 파일이라고 설명한다(31). 쇄파 확산 대상은 운동량이다(20). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
