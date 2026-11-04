---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass1_HighOrder_wgsl.md
lines: 30
sha256: 0243b2b062efcecb6cb2b4a827cb975f6865c8448c3d0ab148475c82e9d3d554
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass1_HighOrder_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass1_HighOrder.wgsl`

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). 조건 `Accuracy_mode == 1`의 고차 변형으로 `Pass1.wgsl`과 같은 바인딩·출력을 쓰고 내부 습윤 영역은 `fourth-order` MUSCL/TVD다(1–7). 이웃 `up to three cells away`를 읽고 건조·기준면 위 지형·경계형 조건 근처에서는 표준 minmod, 나머지는 제한 경사·삼차 차분의 `ReconstructMUSCL4()`다(11). |
| 13–30 | 출력 `x/y/z/w`는 북/동/남/서면이며 `txH`, `txU`, `txV`, `txC`를 쓴다(15–22). 내부 고차·습윤/건조 및 지형 불연속 저차 대체가 목적이다(26). 넓은 계산 격자 묶음(stencil) 때문에 `BoundaryPass`·고차 `Pass2`를 함께 확인해야 한다(30). 넓은 stencil 때문에 표준 pass보다 경계·주기 동작이 더 민감하다(30). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
