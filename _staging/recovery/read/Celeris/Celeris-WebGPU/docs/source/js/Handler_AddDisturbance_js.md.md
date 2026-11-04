---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_AddDisturbance_js.md
lines: 26
sha256: 51cb458152b715ba76c03daba19dd1e43b0d44300118845f085517f693ce9a5e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_AddDisturbance_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_AddDisturbance.js`

구간은 1행부터 26행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `AddDisturbance.wgsl`의 초기·상호작용 파랑 교란과 지정 바닥 운동을 위한 바인드 그룹(bind group)을 만든다(7). |
| 9–26 | `0` 교란 uniform, `1` `txBottom`, `2` `txState`, `3` `txBottomInitial`, `4` 임시 교란 상태, `5` 압력/수심 강제 `txBoundaryForcing`, `6` 임시 바닥, `7` 초기 바닥 참조용 누적 변위 `txBotChange_Sed`다(11–18). 고립파·산사태형·지정 수심 운동을 지원하며 JavaScript가 상태/바닥 텍스처(texture)로 복사하고 진단·시계열을 초기화한다(22). 교란형 `5`는 시간에 따라 바닥을 바꾸므로 near-dry와 분산성(dispersive) 모드의 삼중대각 계수 갱신이 뒤따라야 한다(26). binding `5`는 pressure/depth-change forcing 출력이다(16). `txBotChange_Sed`의 누적 변화는 퇴적물 바닥 변화다(18). 초기화 대상은 관련 진단과 시계열 상태다(22). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
