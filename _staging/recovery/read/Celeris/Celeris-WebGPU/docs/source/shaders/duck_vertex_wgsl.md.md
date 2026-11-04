---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/duck_vertex_wgsl.md
lines: 19
sha256: 87036bdf3d88e92f0c182358551207bc489280c4183f80d3013182b3d010e5dd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# duck_vertex_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/duck.vertex.wgsl`

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). prototype 모델 vertex는 위치·법선·UV를 받고 `Y/Z`를 바꿔 세운 뒤 world/clip으로 변환해 world position·normal·UV를 fragment에 보낸다(1–7). 바인딩 `0`은 view-projection·model matrix·camera position·padding uniform이다(11). |
| 13–19 | duck/glTF는 주 시각화가 아니며 현재 단순 모델·물 격자가 중심이다(15). 이 좌표 교환은 모델 경로 전용이므로 물 렌더에 복사 전 장면 규약을 확인하라고 적는다(19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15: 문서는 duck/glTF를 현재 주 시각화 경로와 구분한다.
