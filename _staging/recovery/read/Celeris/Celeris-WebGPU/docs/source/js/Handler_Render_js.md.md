---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Render_js.md
lines: 37
sha256: c57bd79eee5c6fdc2d2b16f86703aed56bc5556c388ccde83e8fef11d0678dc6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Render_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Render.js`

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 `2D`·`3D` 시각화 바인드 그룹(bind group), 색상 막대/문자/로고 텍스처(texture) 갱신 역할이다(1–7). 이 모듈은 render bind-group layout도 생성한다(7). [11-04 전수 검증 보완] |
| 9–30 | `0` 렌더 uniform, `1` eta/상태 입력, `2` `txBottom`, `3` `txMeans`, `4` `txWaveHeight`, `5` `txBaseline_WaveHeight`, `6` `txBottomFriction`, `7` `txNewState_Sed`, `8` 호출별 `erosion_Sed` 또는 이전 깊이 참조, `9` `txBotChange_Sed`, `10` `txDesignComponents`, `11` `txOverlayMap`, `12` `txDraw`, `13` nearest/non-filtering sampler, `14` `txTimeSeries_Locations`, `15` `txBreaking`, `16` `txSamplePNGs` `2D-array`, `17` linear/filtering sampler, `18` `txRenderVarsf16` `2D-array`다(11–29). `txSamplePNGs`는 image texture이며 `txRenderVarsf16`은 render cache다(27·29). [11-04 전수 검증 보완] |
| 31–37 | `update_colorbar()`가 화면 밖 canvas에 로고·이름·눈금·값을 그려 `txDraw`로 보낸다. fragment는 흰색이 아닌 픽셀을 합성한다(33). `main.js`는 시작 시 생성하고 Google Maps/위성 영상 재선택 때 재생성할 수 있다. 모든 호출에 `txDesignComponents`, `textureSampler_linear`, `txRenderVarsf16`을 포함한 전체 인수가 필요하며 뒤 인수 누락은 overlay 전환 중 루프를 멈출 수 있다고 적는다(37). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
