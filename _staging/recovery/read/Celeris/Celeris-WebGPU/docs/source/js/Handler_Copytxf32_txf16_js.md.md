---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Copytxf32_txf16_js.md
lines: 27
sha256: 17edb421bc2a8ea394e23012afd643b5713a8adf658124aef07c34f02b3a924a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Copytxf32_txf16_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Copytxf32_txf16.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `Copytxf32_txf16.wgsl`의 표시 캐시 포장용 바인드 그룹(bind group)을 만든다(7). |
| 9–27 | `0` 렌더/계산 uniform, `1` `txNewState`, `2` `txBottom`, `3` `txMeans_Speed`, `4` `2D-array` `rgba16float` 출력 `txRenderVarsf16`, `5` `txMeans_Momflux`, `6` `txModelVelocities`, `7` `txMeans`, `8` `txHardBottom`이다(11–19). 자주 읽는 표시 변수를 반정밀도 층에 묶어 fragment·`3D` vertex의 전정밀도 텍스처(texture) 표본 수를 줄인다(23). 층/채널 변경은 `fragment.wgsl`, `vertex3D.wgsl`, `docs/architecture/DATA_AND_TEXTURES.md`에 반영해야 한다(27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
