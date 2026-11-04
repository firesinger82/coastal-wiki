---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_CalcMeans_js.md
lines: 32
sha256: 8cd2a23dc2ab527655a0f487a17349fd43aa03626d28be0cb69310510979d2d0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_CalcMeans_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_CalcMeans.js`

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크·역할 설명(1–7). `CalcMeans.wgsl`의 평균·최대·운동량 유량·와도·모델 속도 진단용 바인드 그룹(bind group)을 만든다(7). |
| 9–32 | `0` 진단 uniform, `1` `txMeans`, `2` `txMeans_Speed`, `3` `txMeans_Momflux`, `4/5/6` `txH`/`txU`/`txV`, `7` `txBottom`, `8` 임시 평균, `9` 임시 속도/최대, `10` 임시 운동량/와도, `11` 출력 `txModelVelocities`, `12` `txC`, `13` `txNewState`다(11–24). 면속도를 셀 평균 진단으로 바꾸고 렌더·출력·`3D` 모델용 시간 평균장을 유지한다(28). `txModelVelocities`에는 COULWAVE 보조 로직도 값을 기록하며 표시 자료 포장도 이에 의존한다고 적는다(32). [11-04 전수 검증 정정] binding `8`·`9`·`10`은 임시 출력이다(19–21). 속도 정의를 바꿀 때 주의하라고 안내한다(32). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
