---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Model_Loaders_js.md
lines: 27
sha256: 1cbcfde40a7975fdc7920bf6c376cb190dfa68f0deef47554105d94dd5b4d8dc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Model_Loaders_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Model_Loaders.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크와 `gl-matrix`를 쓰는 `3D` 상자·prototype glTF 준비 역할이다(1–7). `loadModelDefinitions()`는 URL/파일 정의를 읽고 `loadSceneModels()`는 행렬·상자 객체를 준비한다. `makeModelMatrix()`와 보조 함수는 위치·크기·회전을 조합하며 현재 상자/모델 셰이더와 맞는 경로다(11–13). |
| 15–27 | `loadglTFModel()`은 glTF JSON·이진 버퍼·텍스처(texture)를 읽고 첫 primitive의 `POSITION`, `NORMAL`, `TEXCOORD`, 인덱스를 추출해 GPU 버퍼·albedo·경계를 반환한다(17). Duck/glTF는 주 표시 경로가 아닌 prototype 성격이다(19). 단순 모델은 위치 정점·view/projection/model/camera uniform, glTF는 위치·법선·UV·albedo를 요구한다(23). 별도 결합이 없으면 모델 로딩은 수리 텍스처를 바꾸지 않아야 한다(27). `loadglTFModel()`은 albedo 텍스처를 GPU에 업로드한다(17). 단순 모델 uniform은 모델마다 하나씩 둔다(23). 모델은 시각적·맥락적 객체이며 로딩을 simulation 상태와 분리하라고 안내한다(27). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17: 문서는 glTF 추출 대상이 첫 primitive라고 적는다.
- 19: 문서는 Duck/glTF 경로를 prototype으로 구분한다.
