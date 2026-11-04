---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass2_HighOrder_HLLEM_wgsl.md
lines: 23
sha256: eb44101bf50af0b7020628f3ceb48090e114723c9cef2019d69fc78defd32a41
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass2_HighOrder_HLLEM_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass2_HighOrder_HLLEM.wgsl`

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). 기본 HLL에 HLLEM형 접촉면 복원을 더하는 대체 고차 셰이더다(1–7). handler 배치는 공통이지만 현재 `main.js`는 `Pass2_HighOrder_HLLC.wgsl`을 선택하므로 대안/실험 변형으로 취급한다(11). |
| 13–23 | HLL flux를 계산한다(15). Roe형 속도를 추정한다(15). 저확산 선형화 flux를 만든다(15). 제한자를 써서 그 flux 쪽으로 혼합한다(15). 건조 근처에서는 HLL 부분의 질량 jump를 영값으로 만든다(15). 퇴적물은 활성 시 같은 HLLEM helper를 쓰며 확산항 미통합 주석이 있다(19). 재활성 시 HLLC와 습윤/건조·퇴적물 안정성을 비교하라고 적는다(23). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 문서는 현재 고차 경로에서 HLLEM이 선택되지 않는다고 적는다.
- 19: 문서는 퇴적물 확산항이 이 유량식에 통합되지 않았다는 주석을 적는다.
