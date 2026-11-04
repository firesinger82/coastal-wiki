---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/js/Handler_Pass3_js.md
lines: 49
sha256: bc049cc767416f4fa7dfde25c23fab3df5cd4c085ef98c269cb5374cf289bbc0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Handler_Pass3_js.md — 판독 구간 기록

설명 대상 코드 파일: `js/Handler_Pass3.js`

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–8 | 원문 링크와 물리·시간 적분 및 `two` COULWAVE 보조 pass의 바인드 그룹(bind group)을 적는다. `Pass3`에서 유량·발생항·쇄파·마찰·예측/수정이 결합한다(1–7). 이 파일은 해당 pass들의 bind-group layout을 정의한다(7). 원문은 여러 계산이 만나는 지점이므로 가장 중요한 handler 파일 중 하나라고 설명한다(7). [11-04 전수 검증 보완] |
| 9–34 | `Pass3_NLSW.wgsl`, `Pass3_Bous.wgsl`, `Pass3_COULWAVE.wgsl` 공통 배치다(11). `0` uniform, `1` `txState`, `2` `txBottom`, `3` `3D` `txCW_groupings`(비-COULWAVE에서 `Dummy 1x1`), `4` `txXFlux`, `5` `txYFlux`, `6` `oldGradients`, `7` `oldOldGradients`, `8` `predictedGradients`, `9` `F_G_star_oldGradients`, `10` `F_G_star_oldOldGradients`, `11` `txstateUVstar`, `12` `txBoundaryForcing`, `13` 출력 `txNewState`, `14` 출력 `dU_by_dt`, `15` 출력 `F_G_star`, `16` 출력 `current_stateUVstar`, `17` `txBottomFriction`, `18` `txBreaking`, `19` `txDissipationFlux`(구면 NLSW에서는 `txSphericalMetrics`), `20` `txContSource`다(13–33). |
| 35–49 | `Pass3A_COULWAVE`는 상태·바닥·`txU`·`txV`를 읽고 모델 속도·`txCW_zalpha`·`txCW_uvhuhv`를 쓴다(37–40). `Pass3B_COULWAVE`는 상태·바닥·`txCW_uvhuhv`·`txCW_zalpha`·`dU_by_dt`를 읽고 `txCW_STval`, `txCW_STgrad`, `txCW_Eterms`, `txCW_FGterms`를 쓴다(42–45). 변형에서 안 쓰는 바인딩도 유지하며 주 COULWAVE 전 JavaScript가 보조 `2D` 출력을 `txCW_groupings` 층으로 복사해야 한다(49). 주 layout을 넓게 두는 이유는 모든 방정식 계열 shader가 공유하게 하기 위해서다(49). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
