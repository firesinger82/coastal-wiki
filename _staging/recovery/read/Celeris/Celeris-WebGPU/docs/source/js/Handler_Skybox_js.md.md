---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Skybox_js.md
lines: 21
sha256: 51c4620dbd2a560eb09b5698f574a4b742fe564f94e219222b1353ea212eba3c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Skybox_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Skybox.js`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크와 `3D` skybox 바인드 그룹(bind group) 설명이다(1–7). 바인딩 `0` 역 view-projection uniform matrix, `1` cube-map 텍스처(texture) view, `2` skybox sampler다(11–13). |
| 15–21 | vertex가 전체 화면 삼각형과 역행렬 기반 세계 방향을 만들고 fragment가 cube-map을 표본한다(17). 시각화 전용 경로이며 시뮬레이션 텍스처에 의존하지 않아야 한다고 적는다(21). [11-04 전수 검증 정정] 이 지침은 3D 환경을 모델 상태와 독립적으로 유지한다(21). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
