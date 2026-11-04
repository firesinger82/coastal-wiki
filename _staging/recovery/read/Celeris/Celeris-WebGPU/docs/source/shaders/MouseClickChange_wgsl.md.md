---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/MouseClickChange_wgsl.md
lines: 29
sha256: 0c162c2cc421882f952663faeec98dd0ef9ba6b48544b176bb04b6d3d22ce937
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# MouseClickChange_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/MouseClickChange.wgsl`

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 원문 링크·설명이다(1–3). 마우스 브러시 임시 출력을 `main.js`가 활성 패널에 따라 복사한다(1–7). 대상은 지형·마찰·오염원/발생원·자유수면·해수면/지형 offset이다(11–17). 설계는 구성 ID·마찰을 쓰며 선형 구조 add 플래그에서는 지형을 쓴다(19). |
| 21–29 | 대부분 표면은 Gaussian 방사형, 설계 ID는 원판·마찰은 Gaussian 혼합이다(23). 선형 구조는 유한 선분/캡슐 거리로 끝을 둥글게 하고 crest width 밖은 side slope로 낮춘다. `max(existingBottom, targetElevation)`로 올리기만 하며 중심·북·동 채널을 맞춘다(25). 새 모드는 `main.js` 복사 분기도 수정해야 한다(29). crest는 사용자 시작/끝 선을 따른다(25). 둥근 end cap은 유한 선분까지의 거리를 clamp하여 만든다(25). 범용 임시 텍스처의 의미는 `main.js`가 정한다(29). 새 편집 모드는 shader 자체도 수정해야 한다(29). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
