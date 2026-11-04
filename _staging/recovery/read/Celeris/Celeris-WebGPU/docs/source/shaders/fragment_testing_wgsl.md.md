---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/fragment_testing_wgsl.md
lines: 19
sha256: b38d5caa64e569acc411e9110756ef8aeb7853e234c675fb7feab6ac906e2aef
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fragment_testing_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/fragment_testing.wgsl`

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). `fragment.wgsl`의 실험 대체형으로 실사 조명·거칠기·화살표 합성 매개변수가 다르다(1–7). 정상 경로는 `fragment.wgsl`이며 `main.js` 선택 변경 없이는 활성으로 가정하지 말라고 적는다(11). 원문은 이 변형이 `fragment.wgsl`과 대체로 같으며 다른 부분은 조명/roughness 매개변수와 화살표 합성 세부 동작이라고 설명한다(7). [11-04 전수 검증 보완] |
| 13–19 | 주 렌더를 보존하며 실험 비교에 쓸 수 있다(15). `fragment.wgsl`로 도입할 때 채널/표면 모드가 바뀌면 `Handler_Render.js`·색상 막대·캐시 문서도 갱신한다(19). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11: 문서는 현재 정상 렌더가 `fragment.wgsl`을 선택한다고 적는다.
