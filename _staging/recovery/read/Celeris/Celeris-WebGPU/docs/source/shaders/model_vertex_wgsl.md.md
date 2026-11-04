---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/model_vertex_wgsl.md
lines: 20
sha256: 394435cf62461a25197e8c9b8fedafd8c6d9c69944b0a3b56779dc680e431a1d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# model_vertex_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/model.vertex.wgsl`

구간은 1행부터 20행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크와 단순 상자/모델 vertex 역할이다(1–7). 위치 전용 정점을 model·view-projection 행렬로 바꾸고 국소 위치를 fragment에 전달한다(7). 바인딩 `0` uniform은 `viewProj`, `model`, `cameraPos`, padding이다(11). |
| 13–20 | 출력은 clip-space 위치와 면 색상용 local position이다(15–16). 단순 맥락 기하 경로이며 시뮬레이션 상태를 표본하지 않는다(20). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
