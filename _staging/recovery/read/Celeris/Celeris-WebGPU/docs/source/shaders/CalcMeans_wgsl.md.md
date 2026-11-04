---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/CalcMeans_wgsl.md
lines: 21
sha256: f98d8b9912c4ff04b6f44fe44971dd9e633226e4ffd061e4ddfa0e3126a28392
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# CalcMeans_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/CalcMeans.wgsl`

구간은 1행부터 21행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 원문 링크·설명이다(1–3). 평균 eta/u/v/scalar·최대 속도/eta·운동량 유량·평균 절대 와도·모델 속도를 갱신한다(1–7). 재구성 `txH`, `txU`, `txV`, `txC`, 바닥·이전 진단·`txNewState`를 읽고 임시 진단·`txModelVelocities`를 쓴다(11). |
| 13–21 | 면 값을 중심 수심·속도로 평균하며 갱신 비율은 `1 / n_time_steps_means`다. 최대값은 counter가 한 단계를 초과한 뒤에만 누적한다(15). 건조 eta는 큰 음수 placeholder로 둔다(17). `txMeans_Speed`·`txMeans_Momflux` 채널 변경 시 `fragment.wgsl`, `Copytxf32_txf16.wgsl`, 출력을 수정한다(21). [11-04 전수 검증 정정] 큰 음수 placeholder는 최대 처오름 시각화가 건조 셀을 유효한 물로 취급하지 않게 한다(17). 이 pass는 렌더링과 출력에 자료를 공급한다(21). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
