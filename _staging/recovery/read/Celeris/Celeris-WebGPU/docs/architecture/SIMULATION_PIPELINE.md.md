---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/architecture/SIMULATION_PIPELINE.md
lines: 66
sha256: b7e497be388fd477f81b56294b7f61375aca90c274a14fe6e8705b69719c94f1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# SIMULATION_PIPELINE.md — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | JavaScript가 일정·텍스처(texture) 복사를, WGSL이 수치 커널을 맡는다(3). `js/main.js`의 `frame()`은 `requestAnimationFrame`으로 호출되며 `render_step`으로 프레임당 시간 단계 수를 조절한다(7). 프레임은 `html_update`, `click_update`, `add_Disturbance`, `render_step` 단계 계산, 반정밀도 표시 묶기, `2D`/`3D` 표시, tooltip/시계열 추출, 요청 출력을 처리한다(11–18). WebGPU 큐를 주기적으로 비운다고 적는다(20). GPU의 계산 pass 순서는 고정되어 있다(3). GPU가 빠르면 렌더 사이 계산을 늘리고 브라우저 응답성이 필요하면 줄인다(7). `html_update`는 대기 중 UI/config 변경이며 `click_update`는 마우스 편집이다(11–12). 요청 출력은 images·GIF slices·output surfaces다(18). 주기적인 queue flush는 장시간 GPU 명령 누적 위험을 줄인다(20). [11-04 전수 검증 보완] |
| 22–40 | 순서는 `Pass0.wgsl`, `Pass1.wgsl`/`Pass1_HighOrder.wgsl`, 퇴적물 활성 시 `SedTrans_Pass1.wgsl`, `Pass2.wgsl`/`Pass2_HighOrder_HLLC.wgsl`/`Pass2_HighOrder_HLLEM.wgsl`이며 현재 고차 선택은 HLLC다(26–29). 활성 시 `Pass_Breaking.wgsl`, COULWAVE에서 `Pass3A_COULWAVE.wgsl`·`Pass3B_COULWAVE.wgsl`와 `txCW_groupings`, `Pass3_NLSW.wgsl`/`Pass3_NLSW_Spherical.wgsl`/`Pass3_Bous.wgsl`/`Pass3_COULWAVE.wgsl`, `BoundaryPass.wgsl`로 이어진다(30–33). Boussinesq/COULWAVE는 필요 시 `Update_TriDiag_coef*.wgsl`을 갱신하고 `Run_Tridiag_Solver.js`가 `TriDiag_PCRx*.wgsl` 후 `TriDiag_PCRy*.wgsl`을 실행한다. NLSW는 중간 상태를 `txNewState`로 복사한다(34–35). 다시 `BoundaryPass.wgsl`, 선택 바닥 변경·near-dry·계수 갱신, 이력 이동·`txNewState`의 `txState` 전환, 면속도·평균·파고·표시 진단 순서다(36–39). 핵심 timestep은 유한체적 갱신과 선택 분산 보정이다(24). `Pass0.wgsl`은 각 셀 주변 수심을 구하여 flux pass의 dry/wet 논리를 돕는다(26). `Pass1` 계열은 셀 중심 상태와 지형에서 면 수심·속도·스칼라를 재구성한다(27). `SedTrans_Pass1.wgsl`은 면 농도를 재구성한다(28). `Pass2` 계열은 셀 면을 통과하는 수치 flux를 계산한다(29). `Pass_Breaking.wgsl`은 쇄파 경과 시간·강도와 와점성 flux 보조값을 계산한다(30). COULWAVE 보조 pass는 보조항을 생성하여 묶는다(31). `Pass3` 계열은 flux 발산·마찰·압력 강제·쇄파/확산·스칼라 감쇠/분산·예측/수정 갱신을 계산한다(32). 첫 `BoundaryPass.wgsl`은 명시적·중간 상태의 경계와 wet/dry 정리를 수행한다(33). 바닥 갱신은 `txBottom`과 누적 bed-change 텍스처도 바꾼다(37). [11-04 전수 검증 보완] |
| 41–54 | 조건 `timeScheme == 0`은 단일 명시 단계, `timeScheme != 0`과 `pred_or_corrector == 1`은 현재·이전·더 이전 미분을 쓰는 Adams-Bashforth 예측, `pred_or_corrector == 2`는 새 미분·예측·이력 미분의 수정이다(45–47). 물·퇴적물은 경사 이력을, Boussinesq/COULWAVE는 `F_G_star` 이력을 보존한다(49). 경계는 암시 풀이 전 상태 정리와 풀이 후 운동량 일관성 복원을 위해 `twice` 적용한다고 설명한다(53). `F_G_star` 이력은 `Pass3`에 쓰는 분산 보조항을 보존한다(49). 삼중대각 solver가 운동량을 바꿀 수 있으므로 다음 단계의 canonical 상태가 되기 전에 두 번째 경계 pass를 적용한다(53). [11-04 전수 검증 보완] |
| 55–66 | `main.js`의 활성 선택은 표준 `Pass1.wgsl`·`Pass2.wgsl`, 고차 `Pass1_HighOrder.wgsl`·`Pass2_HighOrder_HLLC.wgsl`이다(57–60). NLSW는 `Pass3_NLSW.wgsl`, 조건 `grid_type == 2`는 `Pass3_NLSW_Spherical.wgsl`이며 둘 다 PCR을 생략한다(61–62). Boussinesq는 `Pass3_Bous.wgsl`, `Update_TriDiag_coef.wgsl`, `TriDiag_PCRx.wgsl`, `TriDiag_PCRy.wgsl`이다(63). COULWAVE는 `Pass3A_COULWAVE.wgsl`, `Pass3B_COULWAVE.wgsl`, `Pass3_COULWAVE.wgsl`, `Update_TriDiag_coef_COULWAVE.wgsl`, `TriDiag_PCRx_COULWAVE.wgsl`, `TriDiag_PCRy_COULWAVE.wgsl`이다(64). 실험·이전 변형은 `docs/source/shaders/`에 문서화되지만 현재 경로 확인이 필요하다고 적는다(66). `main.js`는 설정에 따라 WGSL 파일을 fetch하고 compile한다(57). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
