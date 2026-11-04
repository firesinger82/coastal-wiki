---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Copytxf32_txf16_wgsl.md
lines: 34
sha256: c3928f1204d6fa966be24f6fd82a29b094cdd7cedb836f18c1fe14ace06dcebf
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Copytxf32_txf16_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Copytxf32_txf16.wgsl`

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 원문 링크·설명이다(1–3). 선택 전정밀도 상태·진단을 반정밀도 캐시 `txRenderVarsf16`에 포장한다(1–7). `Layer 0`의 `r/g/b/a`는 eta(건조 `-10 * base_depth`)/최대 eta/바닥/거품·추적자(건조 시 영값)다(11–16). |
| 18–34 | `Layer 1`의 `r/g/b/a`는 u/v/unused/평균 절대 와도, `Layer 2`는 바닥/hard bottom/가용 세굴 깊이/unused다(18–30). 층·채널은 `fragment.wgsl`·`vertex3D.wgsl`과 직접 결합하는 렌더 API다(34). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22·30: 문서는 `Layer 1`의 `b`, `Layer 2`의 `a`를 unused로 표시한다.
