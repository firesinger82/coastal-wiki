---
file: models/Celeris/raw/source_code/Celeris-WebGPU/transect_version/js/Run_Tridiag_Solver.js
lines: 77
sha256: 392c8d30c49ab59193f0ead094a62bad187822701581e8f44c6310ff31c833b6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Run_Tridiag_Solver.js — 판독 구간 기록

구간은 1행부터 77행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | runTridiagSolver의 인수 목록이다(3–29). 상태 텍스처(texture), x·y 계수 및 작업 텍스처, uniform·파이프라인(pipeline)·바인드 그룹(bind group), 실행·복사 함수를 받는다. 원문: `// Run_Tridiag_Solver.js` (1); `export function runTridiagSolver(` (3); `device,` (4); `commandEncoder,` (5); `calc_constants,` (6); `current_stateUVstar,` (7); `txNewState,` (8); `coefMatx,` (9); `coefMaty,` (10); `newcoef_x,` (11); `newcoef_y,` (12); `txtemp_PCRx,` (13); `txtemp_PCRy,` (14); `txtemp2_PCRx,` (15); `txtemp2_PCRy,` (16); `TridiagX_uniformBuffer,` (17); `TridiagX_uniforms,` (18); `TridiagX_Pipeline,` (19); `TridiagX_BindGroup,` (20); `TridiagX_view,` (21); `TridiagY_uniformBuffer,` (22); `TridiagY_uniforms,` (23); `TridiagY_Pipeline,` (24); `TridiagY_BindGroup,` (25); `TridiagY_view,` (26); `runComputeShader,` (27); `runCopyTextures` (28); `) {` (29) |
| 31–56 | 시작 시 3행 runTridiagSolver 함수 안. NLSW 분기는 current_stateUVstar를 txNewState로 복사한다(31–33). else에서는 x 계수를 복사하고 Px번 반복한다(34–41). 각 반복은 s 비트 이동, p·s의 little-endian i32 기록(오프셋 8·12), 계산 셰이더(compute shader) 실행, 축약 계수 복사 순서이다(43–51). 반복 종료 후 txtemp2_PCRx를 txNewState로 복사한다(55). 원문: `if (calc_constants.NLSW_or_Bous == 0) {` (31); `runCopyTextures(device, commandEncoder, calc_constants, current_stateUVstar, txNewState)` (32); `}` (33); `else` (34); `{` (35); `//Tridiag` (36); `// X-Solve` (37); `// Copy tridaig coef into newcoef for first loop` (39); `runCopyTextures(device, commandEncoder, calc_constants, coefMatx, newcoef_x)` (40); `for (let p = 0; p < calc_constants.Px; p++) {` (41); `let s = 1 << p;` (43); `TridiagX_view.setInt32(8, p, true);             // i32, holds "p"` (45); `TridiagX_view.setInt32(12, s, true);            // i32, hols "s"` (46); `// Dispatch the shader computation.` (48); `runComputeShader(device, commandEncoder, TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` (49); `// Copy reduced tridaig coef into newcoef for next loop` (50); `runCopyTextures(device, commandEncoder, calc_constants, txtemp_PCRx, newcoef_x)` (51); `}` (52); `// After all the iterations, copy the new state into current state.` (54); `runCopyTextures(device, commandEncoder, calc_constants, txtemp2_PCRx, txNewState)` (55) |
| 57–77 | 시작 시 3행 runTridiagSolver 함수 안이다. 바깥 분기는 31행 `if (calc_constants.NLSW_or_Bous == 0) {`의 34–35행 `else`이다. 이 `else`는 76행에서 닫힌다. Y-Solve의 계수 복사·Py 루프·uniform 기록·셰이더 호출·최종 상태 복사는 모두 주석이다(60–75). else와 함수가 끝난다(76–77). 원문: `// Y-Solve` (57); `// Copy tridaig coef into newcoef for first loop` (59); `// runCopyTextures(device, commandEncoder, calc_constants, coefMaty, newcoef_y)` (60); `// for (let p = 0; p < calc_constants.Py; p++) {` (61); `//     let s = 1 << p;` (63); `//     TridiagY_view.setInt32(8, p, true);             // i32, holds "p"` (65); `//     TridiagY_view.setInt32(12, s, true);            // i32, hols "s"` (66); `// Dispatch the shader computation.` (68); `//     runComputeShader(device, commandEncoder, TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup, calc_constants.DispatchX, calc_constants.DispatchY);` (69); `// Copy reduced tridaig coef into newcoef for next loop` (70); `//     runCopyTextures(device, commandEncoder, calc_constants, txtemp_PCRy, newcoef_y)` (71); `// }` (72); `// After all the iterations, copy the new state into current state.` (74); `// runCopyTextures(device, commandEncoder, calc_constants, txtemp2_PCRy, txNewState)` (75); `}` (76); `}` (77) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–75: Y-Solve의 실행문 전체가 주석 처리되어 있다.
- 41–55: Px 루프 뒤 txtemp2_PCRx 복사는 루프 반복 횟수와 별도 조건 없이 실행된다.
