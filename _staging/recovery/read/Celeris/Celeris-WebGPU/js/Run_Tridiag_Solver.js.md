---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Run_Tridiag_Solver.js
lines: 93
sha256: 7fdbb2ffe4dea0fe31480df31c2b8cddac587fe66cb73565d24a47b976687d08
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Run_Tridiag_Solver.js — 판독 구간 기록

구간은 1행부터 93행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–36 | runTridiagSolver의 인수를 선언한다. X/Y 계산 파이프라인(pipeline)·바인드 그룹(bind group)·uniform 버퍼 및 실행·복사 콜백을 받는다. 주석은 계수 전달을 위한 ping-pong 자원 추가를 설명한다. 원문(행 순서): `export function runTridiagSolver(` (3); `device,` (4); `commandEncoder,` (5); `calc_constants,` (6); `current_stateUVstar,` (7); `txNewState,` (8); `coefMatx,` (9); `coefMaty,` (10); `newcoef_x,` (11); `newcoef_y,` (12); `txtemp_PCRx,` (13); `txtemp_PCRy,` (14); `txtemp2_PCRx,` (15); `txtemp2_PCRy,` (16); `TridiagX_uniformBuffer,` (17); `TridiagX_uniforms,` (18); `TridiagX_Pipeline,` (19); `TridiagX_BindGroup,` (20); `TridiagX_BindGroup_BaseToA,` (22); `TridiagX_BindGroup_BToA,` (23); `TridiagX_view,` (24); `TridiagY_uniformBuffer,` (25); `TridiagY_uniforms,` (26); `TridiagY_Pipeline,` (27); `TridiagY_BindGroup,` (28); `TridiagY_BindGroup_BaseToA,` (30); `TridiagY_BindGroup_BToA,` (31); `TridiagY_view,` (32); `runComputeShader,` (33); `runCopyTextures` (34); `) {` (35). 21·29행 주석은 추가 바인드 그룹의 목적을 복사 없는 PCR 계수 전달이라고 설명한다. [11-04 전수 검증 보완] |
| 37–67 | 시작 시 3행 runTridiagSolver 루틴 안. NLSW_or_Bous가 0이면 상태 텍스처(texture)를 복사한다. else에서는 X 반복을 수행한다. s를 비트 시프트(bit shift)로 계산한다. uniform p·s를 바이트 오프셋 8·12에 little-endian Int32로 쓴다. 첫 반복·홀수·짝수에 따라 바인드 그룹을 골라 계산 셰이더(compute shader)를 호출한다. X 결과를 txNewState로 복사한다. 원문(행 순서): `if (calc_constants.NLSW_or_Bous == 0) {` (37); `runCopyTextures(device, calc_constants, current_stateUVstar, txNewState)` (38); `else` (40); `for (let p = 0; p < calc_constants.Px; p++) {` (48); `let s = 1 << p;` (50); `TridiagX_view.setInt32(8, p, true);             // i32, holds "p"` (52); `TridiagX_view.setInt32(12, s, true);            // i32, hols "s"` (53); `const TridiagX_BindGroup_Current = (p == 0) ? TridiagX_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagX_BindGroup : TridiagX_BindGroup_BToA);` (57); `runComputeShader(device, TridiagX_uniformBuffer, TridiagX_uniforms, TridiagX_Pipeline, TridiagX_BindGroup_Current, calc_constants.DispatchX, calc_constants.DispatchY);` (59); `runCopyTextures(device, calc_constants, txtemp2_PCRx, txNewState)` (66). 45–47행 주석은 첫 반복의 계수 복사 호출을 비활성화하고 기본 계수 행렬을 직접 읽는다고 설명한다. 56행 주석은 newcoef_x와 txtemp_PCRx 사이에서 계수를 교대로 사용한다고 설명한다. 58행의 고정 바인드 그룹 실행 호출은 주석이다. 60–62행 주석은 다음 반복이 선택된 바인드 그룹의 출력 텍스처를 읽는다고 설명한다. 65행 주석은 새 상태를 current state로 복사한다고 표현하지만 실제 목적지는 txNewState이다. X 반복문은 63행에서 닫힌다. else 블록은 92행에서 닫힌다. 바깥 함수는 93행에서 닫힌다. [11-04 전수 검증 보완] |
| 68–93 | 시작 시 3행 루틴·40행 else 안. Y 반복에서 p·s를 오프셋 8·12에 쓴다. 첫 반복·홀수·짝수에 따라 바인드 그룹을 골라 계산을 호출한다. Y 결과를 txNewState로 복사한다. 계수 복사 호출은 주석 처리되어 있다. 원문(행 순서): `for (let p = 0; p < calc_constants.Py; p++) {` (73); `let s = 1 << p;` (75); `TridiagY_view.setInt32(8, p, true);             // i32, holds "p"` (77); `TridiagY_view.setInt32(12, s, true);            // i32, hols "s"` (78); `const TridiagY_BindGroup_Current = (p == 0) ? TridiagY_BindGroup_BaseToA : ((p % 2 == 1) ? TridiagY_BindGroup : TridiagY_BindGroup_BToA);` (82); `runComputeShader(device, TridiagY_uniformBuffer, TridiagY_uniforms, TridiagY_Pipeline, TridiagY_BindGroup_Current, calc_constants.DispatchX, calc_constants.DispatchY);` (84); `runCopyTextures(device, calc_constants, txtemp2_PCRy, txNewState)` (91). 바깥 else는 37행 `if (calc_constants.NLSW_or_Bous == 0) {`의 거짓 가지이다. 70–72행 주석은 첫 반복의 계수 복사를 비활성화하고 기본 계수 행렬을 직접 읽는다고 설명한다. 81행 주석은 newcoef_y와 txtemp_PCRy 사이에서 계수를 교대로 사용한다고 설명한다. 83행의 고정 바인드 그룹 실행 호출은 주석이다. 85–87행 주석은 다음 반복이 선택된 바인드 그룹의 출력 텍스처를 읽는다고 설명한다. 90행 주석의 current state에 해당하는 실제 복사 목적지는 txNewState이다. Y 반복문·else·함수는 각각 88·92·93행에서 닫힌다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·9–16·37–93: commandEncoder, coefMatx, coefMaty, newcoef_x, newcoef_y, txtemp_PCRx, txtemp_PCRy는 인수이지만 실행문에서 직접 참조하지 않는다.
- 48–66·73–91: 결과 복사는 각 반복문 밖에 있다. 반복 수가 0인 경우를 별도로 처리하는 분기는 이 파일에 없다.
