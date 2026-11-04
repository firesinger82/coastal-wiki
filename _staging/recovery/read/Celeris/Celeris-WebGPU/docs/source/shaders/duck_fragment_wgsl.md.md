---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/duck_fragment_wgsl.md
lines: 21
sha256: 2e3e7fc3acfb825f526353d059dfb6929c33ec2481c11bc8a5b56cde69b54f72
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# duck_fragment_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/duck.fragment.wgsl`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크·설명이다(1–3). prototype 모델 fragment가 보간 UV로 albedo 텍스처(texture)를 읽고 Lambert 확산·작은 주변광을 적용한다(1–7). 바인딩 `0` model uniform, `1` albedo, `2` albedo sampler다(11–13). |
| 15–21 | 핵심 파랑이 아닌 prototype duck/glTF 경로다(17). 사용자 기능으로 확대하면 재질·법선·조명을 개선할 필요가 있을 가능성이 높다고 적는다(21). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 17: 문서는 이 파일을 prototype duck/glTF 경로로 구분한다.
