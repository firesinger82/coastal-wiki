---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass3_Bous_wgsl.md
lines: 28
sha256: 8bd593de9f86b105e968cd82a5a2ff165c259c3417f52e3b12c175d07e2591ba
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass3_Bous_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass3_Bous.wgsl`

구간은 1행부터 28행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | 원문 링크·설명이다(1–3). Boussinesq 발생항·시간 적분으로 NLSW 유량 발산·발생항에 분산성(dispersive) 항을 더하고 이후 삼중대각으로 보정한다(1–7). 건조지 근처와 주기 경계 guard 영역이 아닌 셀에서 eta·수심·운동량 고차 미분을 계산해 `F_star`, `G_star`를 `F_G_star`에 쓰고 `Psi`를 운동량에 더한다(11). 시간 차분은 `F_G_star_oldGradients`, `F_G_star_oldOldGradients`를 쓴다(13). |
| 15–28 | 쇄파 활성 시 `txDissipationFlux` 운동량 확산, 바닥/Manning 마찰·압력·침투·스칼라 확산/감쇠·와도 혼합을 쓴다(17). 출력은 후보 `txNewState`, 미분 `dU_by_dt`, 이력 `F_G_star`, 암시 우변 `current_stateUVstar`다(21–24). 명시·암시 쌍인 `Update_TriDiag_coef.wgsl`, `TriDiag_PCRx.wgsl`, `TriDiag_PCRy.wgsl`를 함께 확인한다(28). 쇄파 운동량 확산 사용은 NLSW pass와 다르다(17). Manning 마찰은 선택 사항이다(17). `txNewState`는 풀이 전/후 상태 후보이며 `dU_by_dt`는 이력과 쇄파에 쓰인다(21–22). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
