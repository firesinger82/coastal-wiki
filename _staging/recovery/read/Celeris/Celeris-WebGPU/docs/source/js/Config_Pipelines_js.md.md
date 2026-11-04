---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Config_Pipelines_js.md
lines: 31
sha256: c338f0661f2ba0ea26c03ce79bdff50cec4e67d6e49f81e44b7496198affc198
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Config_Pipelines_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Config_Pipelines.js`

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | `js/Config_Pipelines.js` 원문 링크와 `main.js`의 WebGPU 계산·렌더 파이프라인 생성 역할을 설명한다(1–7). `createComputePipeline(...)`은 WGSL `main` 진입점과 `allComputePipelines` 추적, `createRenderPipeline(...)`은 `vertex.wgsl`·`fragment.wgsl`의 `2D`, `createRenderPipeline_vertexgrid(...)`는 `vertex3D.wgsl`의 `3D` 물 표면, `createSkyboxPipeline(...)`은 전체 화면 삼각형, `createModelPipeline(...)`은 triangle-list 모델, `createDuckPipeline(...)`은 위치·법선·UV의 glTF prototype이다(11–16). 생성 입력은 shader module과 bind-group layout이며 `main.js`의 low-level pipeline descriptor를 한곳에 모은다(7). `createRenderPipeline_vertexgrid(...)`는 main fragment shader도 쓴다(13). `createModelPipeline(...)`은 box/model 렌더용이다(15). [11-04 전수 검증 보완] |
| 18–31 | `2D`는 `vertex.wgsl`의 `vertex_index`로 quad를 만들어 정점 버퍼가 필요 없다. `3D` 물 격자는 `float32x2`, 모델은 `float32x3`, Duck은 위치·법선·UV 버퍼다(20–25). `3D` 물·모델은 깊이 검사를 켜며 전체 화면 경로는 끄거나 조정한다(27). 진입점·바인드 그룹(bind group) 배치를 맞춰야 하고 빌드가 없어 컴파일 오류는 브라우저 실행 때 나타난다고 적는다(31). 새 pipeline descriptor는 최소한으로 유지하고 기존 사용 방식과 일치시키라고 안내한다(31). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
