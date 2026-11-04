---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Create_Textures_js.md
lines: 32
sha256: b3c1d0a2eabe9152ba39833ba186087b688068b7cadc71ed73c217207c85358f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Create_Textures_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Create_Textures.js`

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | WebGPU 텍스처(texture)·uniform buffer의 형식과 사용 계약을 정의한다(1–7). 팩토리는 계산 `rgba32float` `2D`, 표시 캐시 `rgba16float` `2D-array`, 영상 `bgra8unorm`, COULWAVE 중간항 `3D` `rgba32float`, `3D` 영상·큐브, 파랑/관측 위치 `1D-like` `rgba32float`, `3D` 깊이, uniform buffer를 만든다(13–20). 생성한 모든 텍스처를 `allTextures`에 추가해 `main.js`가 시나리오 교체 시 해제·재생성한다(22). [11-04 전수 검증 정정] 모듈은 자원을 직접 할당하며 거의 모든 simulation·renderer 텍스처의 format/usage 계약을 맡는다(7). `rgba32float` 2D의 용도는 상태·지형·flux·진단·대부분의 compute 출력이다(13). `bgra8unorm`의 용도는 map overlay·UI draw layer·sampled visual asset이다(15). uniform buffer에는 WebGPU usage flag를 지정한다(20). [11-04 전수 검증 보완] |
| 24–32 | 계산 텍스처는 저장·표본·복사 원본·복사 대상 플래그를 넓게 사용한다(26). 영상은 캔버스·회수·렌더 배치와 맞는 `bgra8unorm`이다(28). `rgba32float`에서 `rgba16float`로 변경하면 handler·WGSL의 예상 형식·표본형도 맞춰야 하며 unfilterable-float 가정을 깨뜨릴 수 있다고 적는다(32). usage flag를 넓게 두는 이유는 pass가 임시 출력을 쓰고 복사한 뒤 나중 pass에서 표본으로 읽을 수 있기 때문이다(26). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
