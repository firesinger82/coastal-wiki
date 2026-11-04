---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_SedTrans_UpdateBottom_js.md
lines: 27
sha256: 5e30b8150c7af456936d6bbd1f2e4283f2ad2440f5a1ca77a4d55ef31a28334a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_SedTrans_UpdateBottom_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_SedTrans_UpdateBottom.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 `SedTrans_UpdateBottom.wgsl`의 침식·퇴적에 따른 지형 갱신 바인드 그룹(bind group)이다(1–7). |
| 9–27 | `0` 퇴적물/바닥 uniform, `1` `txBottom`, `2` `txBotChange_Sed`, `3` `erosion_Sed`, `4` `depostion_Sed`, `5` 임시 바닥, `6` 임시 누적 변위, `7` `txHardBottom`, `8` `txBottomInitial`이다(11–19). 발생/소멸률을 바닥고·누적 변위로 변환하고 JavaScript가 `txBottom`·`txBotChange_Sed`로 복사한다(23). 이후 near-dry와 분산성(dispersive) 모드의 삼중대각 계수를 갱신해야 한다. hard-bottom을 읽지만 모든 출력 채널을 강하게 제한하지는 않는다고 적는다(27). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27: 문서는 hard-bottom 자료를 읽지만 모든 출력 채널을 강하게 제한하지는 않는다고 적는다.
