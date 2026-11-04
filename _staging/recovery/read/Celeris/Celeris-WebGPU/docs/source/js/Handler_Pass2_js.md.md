---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Pass2_js.md
lines: 31
sha256: 0f09a7fa03c3e74c57fd36b49a15d0a32587036a797245f0c8da49acc495fdc3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass2_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Pass2.js`

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 표준 `Pass2.wgsl`·고차 HLLC/HLLEM이 공유하는 수리·퇴적물 유량 바인드 그룹(bind group)을 적는다(1–7). |
| 9–31 | 바인딩 `0` 계산 uniform, `1` `txH`, `2` `txU`, `3` `txV`, `4` `txBottom`, `5` `txC`, `6` `txHnear`, `7` 출력 `txXFlux`, `8` 출력 `txYFlux`, `9` to `12`는 `txSed_C1` through `txSed_C4`, `13` 출력 `txXFlux_Sed`, `14` 출력 `txYFlux_Sed`, `15` 퇴적물 분산용 `txBreaking`이다(11–23). `Pass3`의 유량 발산 입력을 계산하며 조건 `useSedTransModel == 1`일 때만 퇴적물 출력이 의미 있다고 적는다(27). 퇴적물 비활성 때도 바인딩을 유지한다(31). `txH`는 재구성 면 수심이다(12). `txU`·`txV`는 재구성 x/y 속도다(13–14). `txBottom`은 지형이며 `txC`는 재구성 스칼라/추적자다(15–16). `txHnear`는 이웃 수심 보조값이다(17). `txSed_C1`부터 `txSed_C4`는 퇴적물 면 농도다(20). `txBreaking`은 퇴적물 분산용 쇄파 강도다(23). flux 변형을 추가할 때 퇴적물 binding 호환성을 유지하라고 안내한다(31). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
