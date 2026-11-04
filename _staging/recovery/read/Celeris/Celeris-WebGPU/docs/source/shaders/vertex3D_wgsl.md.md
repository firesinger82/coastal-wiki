---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/vertex3D_wgsl.md
lines: 22
sha256: 9dbffa7c143997da081d3b9ce2a34777b7f580252573fedb19de6caaff6093ae
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vertex3D_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/vertex3D.wgsl`

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | 원문 링크와 정규화 격자·수면 표본·세계 좌표·수직 확대·카메라 투영의 `3D` 물 표면 역할이다(1–7). 정점 location `0`은 `vec2<f32>`, render uniform은 격자 크기·`dx`, `dy`, `renderZScale`, `viewProj`, 바인딩 `1`은 물 상태 텍스처(texture)이며 공통 바인드 그룹(bind group)으로 캐시·sampler도 받는다(11–14). |
| 16–22 | UV를 fragment에 보내 같은 `fragment.wgsl`로 `3D` 표면을 색칠한다(18). 현재 고도는 `txRenderVarsf16`만이 아니라 전정밀도 상태에서 표본하므로 캐시 의미 변경 시 기하 표본 원천도 확인해야 한다(22). 캐시 의미 변경 시 3D 기하가 cache와 full state 중 어느 것을 써야 하는지 확인하라고 안내한다(22). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22: 문서는 현재 고도 표본 원천이 전정밀도 상태 텍스처라고 적는다.
