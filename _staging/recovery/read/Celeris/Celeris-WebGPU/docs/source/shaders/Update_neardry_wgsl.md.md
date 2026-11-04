---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Update_neardry_wgsl.md
lines: 28
sha256: 5e2e4b7e1018cb2d5e45f11bd92582d0df6646b5bbb327c007f01271d99747e9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Update_neardry_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Update_neardry.wgsl`

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 원문 링크·설명이다(1–3). 바닥 변경 후 near-dry·작은 지형 정리를 수행한다(1–7). `txBottom`을 읽어 `txtemp_bottom`에 쓰며 `x/y/z/w`는 북면/동면/중심 바닥고/near-dry다(11–16). |
| 18–28 | 반경 `3-cell`을 훑어 근처 중심고가 비음수이면 음의 near-dry 플래그, 아니면 양수다(20). 습윤/깊은 이웃에 둘러싸인 건조 지형점을 수면선 쪽으로 낮춰 단일 셀 섬을 제거한다(24). 모든 바닥 변경 뒤 실행해야 한다고 안내한다(28). Boussinesq/COULWAVE는 플래그로 해안선의 분산성(dispersive) 보정을 억제한다(28). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
