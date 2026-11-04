---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass2_HighOrder_HLLC_wgsl.md
lines: 23
sha256: 0dbd32be462311ed63980215b1d3550df78d59c1808314b62c6846da1e14e7b1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass2_HighOrder_HLLC_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass2_HighOrder_HLLC.wgsl`

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). 재구성 면 상태의 HLLC형 고차 유량이며 현재 `main.js`가 선택한다(1–7). x/y 좌·우 상태와 한계 파속을 만들고 HLL에서 접촉면 복원 HLLC star 유량으로 혼합한다. 건조 근처는 `DU_flag`로 질량 jump 항을 끈다(11). |
| 13–23 | 퇴적물 활성 시 같은 helper로 농도 유량을 계산하며 일부 확산항이 HLLEM/HLLC형 경로에 포함되지 않았다는 주석을 적는다(15). `Pass1_HighOrder.wgsl`과 결합하며 표준 scalar HLL보다 덜 확산적인 유량이 목적이다(19). 나눗셈·건조 상태의 GPU 보호 조건을 보존하라고 적는다(23). `Pass1_HighOrder.wgsl`은 고차 면 상태를 제공한다(19). 보호 조건 유지 지침은 wave-speed 또는 star-state 논리를 수정할 때 적용한다(23). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15: 문서는 일부 퇴적물 확산항이 HLLEM/HLLC형 유량 경로에 포함되지 않았다는 주석을 적는다.
