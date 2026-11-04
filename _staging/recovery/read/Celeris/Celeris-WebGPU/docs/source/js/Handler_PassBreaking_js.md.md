---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_PassBreaking_js.md
lines: 27
sha256: 783e925b1bc4620041e379d23813c27c9320dd436b8d624684daa855248f360c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_PassBreaking_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_PassBreaking.js`

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 `Pass_Breaking.wgsl`의 쇄파·와점성 보조 바인드 그룹(bind group)을 적는다(1–7). |
| 9–27 | `0` 쇄파/계산 uniform, `1` `txState`, `2` `txBottom`, `3` `dU_by_dt`, `4` `txXFlux`, `5` `txYFlux`, `6` 이전 `txBreaking`, `7` 출력 `txDissipationFlux`, `8` 임시 쇄파 출력이다(11–19). 발생·경과·강도·점성 가중 운동량 경사를 계산하며 `Pass3_Bous`·`Pass3_COULWAVE`가 확산에 사용한다(23). JavaScript가 임시 결과를 `txBreaking`에 복사하며 채널 변경 시 복사·렌더도 수정해야 한다(27). 후속 pass가 더하는 확산은 `txDissipationFlux`를 쓰는 쇄파 운동량 확산이다(23). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
