---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Pass0_js.md
lines: 22
sha256: 68f435a665cdc25decb52e31f3e6cb3e5f01363fb05b3cd22145e91084d77597
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass0_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Pass0.js`

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `Pass0.wgsl`의 습윤/건조 유량용 이웃 수심 계산에 필요한 바인드 그룹(bind group)·배치를 만든다(7). |
| 9–22 | `0` 계산 uniform, `1` 현재 `txState`, `2` 지형 `txBottom`, `3` 북/동/남/서 이웃 수심 출력 `txHnear`다(11–14). 재구성·유량 전에 실행하고 `Pass2`가 출력 텍스처(texture)로 건조/준건조 이웃을 판별해 불안정한 질량 차이를 억제한다(18). 머리말/주석은 다른 handler에서 복사된 것으로 보이며 위 배치와 `Pass0.wgsl` 선언을 우선하라고 적는다(22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22: 문서는 머리말/주석이 다른 handler에서 복사된 것으로 보인다고 적는다.
