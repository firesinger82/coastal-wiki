---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/source/shaders/Pass3_NLSW_wgsl.md
lines: 31
sha256: 3297f6f8923c29d6e78dd1b7752db2efd5a79cfb066d08a35e73742b65bf0c72
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Pass3_NLSW_wgsl.md — 판독 구간 기록

설명 대상 코드 파일: `shaders/Pass3_NLSW.wgsl`

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | 원문 링크·설명이다(1–3). 비선형 천수 유량 발산·발생항·시간 적분의 출력은 `txNewState`, `dU_by_dt`, `F_G_star`, `current_stateUVstar`다(1–7). 자유수면 경사·바닥/Manning 마찰·선택 `txBoundaryForcing`·와도 혼합·양의 지형 침투/넘침 손실·스칼라 확산/감쇠·쇄파 스칼라 표시를 포함하나 NLSW 쇄파 운동량 확산은 포함하지 않는다(11–19). `txBoundaryForcing`의 선택 강제는 압력/수심 변화다(15). 와도 기반 혼합 대상은 운동량이다(16). [11-04 전수 검증 보완] |
| 21–31 | 명시·예측/수정은 `oldGradients`, `oldOldGradients`, `predictedGradients`를 쓴다(23). 건조 이웃으로 둘러싼 건조 셀은 조기 영값, 건조 이웃 옆 수면 경사는 편측이다(27). NLSW는 삼중대각을 우회해 경계 처리 후 `current_stateUVstar`·`txNewState`가 직접 대응하며 분산성(dispersive) 항 추가 시 solver 경로도 갱신해야 한다(31). 편측 경사는 해안선 셀이 유효하지 않은 중심 경사를 쓰지 않게 한다(27). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19: 문서는 NLSW 변형에 쇄파 운동량 확산을 포함하지 않는다고 적는다.
