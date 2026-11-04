---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/vertex_wgsl.md
lines: 20
sha256: 61ee67748e87c634e06d896289b1201e137704a27f42dd1c49af6f255d8c2638
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vertex_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/vertex.wgsl`

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 원문 링크와 `vertex_index`로 `four-vertex strip`을 만드는 전체 화면 `2D` vertex 역할이다(1–7). clip-space는 전체 viewport, `uv`는 `[0, 0]`부터 `[1, 1]`까지다(11–12). 정규화 UV 좌표는 fragment shader에 전달한다(7). [11-04 전수 검증 보완] |
| 14–20 | `fragment.wgsl` 또는 실험 fragment와 `2D` pipeline을 구성하며 정점 버퍼가 필요 없다(16). UV는 `fragment.wgsl`·지도 overlay·시계열 marker와 맞춰야 한다(20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
