---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/skybox_vertex_wgsl.md
lines: 21
sha256: b2da9f88d4dc07ff012cafe2d6bbeacb82014790b63ecbadc57738dc6f33195b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# skybox_vertex_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/skybox.vertex.wgsl`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크와 전체 화면 삼각형·역 view-projection 기반 세계 방향 생성 역할이다(1–7). 바인딩 `0`은 역 view-projection 행렬 uniform이며 fragment가 방향으로 cube-map을 읽는다(11–13). |
| 15–21 | 재구성 방향의 `Y`와 `Z`를 교환해 프로젝트 `3D` 방향과 맞춘다(17). 카메라 좌표계 변경 시 이 파일·`3D` 물/모델 행렬 구성을 함께 확인한다(21). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
