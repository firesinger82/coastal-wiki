---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass0_wgsl.md
lines: 26
sha256: 3ec2229b0eb32566c4cbb96cf676fdd0606d32299e3209218b44c6500b8bffa0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass0_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass0.wgsl`

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | 원문 링크·설명이다(1–3). `txState` 자유수면과 `txBottom` 바닥으로 이웃 수심 `txHnear`를 계산한다(1–7). `x/y/z/w`는 북/동/남/서 이웃 수심이며 이후 near-dry 유량 판별에 쓴다(11–18). |
| 20–26 | 무거운 재구성/유량 전 보조 계산이며 영역 끝 이웃 인덱스를 제한한다. 물리 경계는 `BoundaryPass`가 처리한다(22). 채널 변경은 `Pass2`·관련 진단/문서를 수정해야 한다(26). 가벼운 사전 pass로 wet/dry 검사를 무거운 재구성·flux 논리 밖에 둔다(22). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
