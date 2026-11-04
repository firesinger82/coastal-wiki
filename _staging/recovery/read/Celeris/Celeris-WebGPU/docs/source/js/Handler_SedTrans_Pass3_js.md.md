---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_SedTrans_Pass3_js.md
lines: 36
sha256: fd8f055bba6cfb05b2068a2cee2af55d7d9af1fc37b7f43d10a1005bca42846f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_SedTrans_Pass3_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_SedTrans_Pass3.js`

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 `SedTrans_Pass3.wgsl`의 부유사·침식·퇴적·소류사 경사 바인드 그룹(bind group)이다(1–7). |
| 9–36 | `0` 퇴적물 uniform, `1` `txState_Sed`, `2` `txXFlux_Sed`, `3` `txYFlux_Sed`, `4` `oldGradients_Sed`, `5` `oldOldGradients_Sed`, `6` `predictedGradients_Sed`, `7` `txBottom`, `8` 물 `txState`, `9` 출력 `txNewState_Sed`, `10` 출력 `dU_by_dt_Sed`, `11` 출력 `erosion_Sed`, `12` 출력 `depostion_Sed`, `13` `txBreaking`, `14` `txU`, `15` `txV`, `16` `txSed_C1`, `17` `txHardBottom`이다(11–28). 물과 같은 시간 적분 패턴으로 농도를 갱신하고 `SedTrans_UpdateBottom`용 침식·퇴적률을 계산한다(32). 철자 `depostion_Sed`를 그대로 유지하라고 적는다(36). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23·36: 문서는 퇴적 출력 이름을 `depostion_Sed`로 쓰며 이 철자를 유지하라고 명시한다.
