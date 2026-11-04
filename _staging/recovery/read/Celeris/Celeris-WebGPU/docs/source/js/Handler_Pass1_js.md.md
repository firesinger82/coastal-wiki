---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Pass1_js.md
lines: 25
sha256: c981e1553d703371b0eba842e8ecac490cd8e580162262debe58f4e117a5729f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass1_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Pass1.js`

구간은 1행부터 25행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 `Pass1.wgsl`·`Pass1_HighOrder.wgsl`이 공유하는 면 상태 재구성 바인드 그룹(bind group)의 역할을 적는다(1–7). |
| 9–25 | 바인딩 `0` 계산 uniform, `1` 현재 `txState`, `2` `txBottom`, `3/4/5/6`은 재구성 수심/x속도/y속도/스칼라 출력 `txH`/`txU`/`txV`/`txC`다(11–17). `Pass1`은 셀 중심 값을 Riemann/유량용 면 값으로 바꾸며 고차는 더 넓은 계산 격자 묶음(stencil)을 쓰되 출력 계약은 같다(21). `Pass2`·진단·렌더 포장·퇴적물 경로가 기존 채널 순서에 의존한다(25). 새 면 물리량을 추가할 때 기존 채널 순서 의존성에 주의하라고 안내한다(25). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
