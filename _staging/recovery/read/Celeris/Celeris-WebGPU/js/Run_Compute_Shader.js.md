---
file: models/Celeris/raw/source_code/Celeris-WebGPU/js/Run_Compute_Shader.js
lines: 89
sha256: 1419cd614e6adf42312dc078e66ce9ddb582e4dc5be46e82efa547f3c39e14dd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# Run_Compute_Shader.js — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | runComputeShader는 명령 인코더(command encoder)를 생성한다. uniform 버퍼 오프셋 0 쓰기, 계산 패스(compute pass) 시작, 파이프라인(pipeline)·바인드 그룹(bind group) 0 설정, dispatchWorkgroups, 패스 종료, 제출 순서로 실행한다. 원문(행 순서): `export function runComputeShader(device, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {` (3); `const commandEncoder = device.createCommandEncoder();` (6); `device.queue.writeBuffer(uniformBuffer, 0, uniforms);` (9); `const computePass = commandEncoder.beginComputePass();` (12); `computePass.setPipeline(computePipeline);` (15); `computePass.setBindGroup(0, computeBindGroup);` (16); `computePass.dispatchWorkgroups(dispatchX, dispatchY);` (19); `computePass.end();` (22); `device.queue.submit([commandEncoder.finish()]);` (25). |
| 28–37 | fetchShader는 URL을 fetch하고 response.text를 반환한다. 원문(행 순서): `export async function fetchShader(url) {` (30); `const response = await fetch(url);` (32); `return await response.text();` (35). |
| 38–54 | runCopyTextures는 새 명령 인코더에서 텍스처(texture)를 WIDTH·HEIGHT·깊이 1 범위로 복사한다. 명령을 제출한다. 원문(행 순서): `export function runCopyTextures(device, calc_constants, src_texture, dst_texture) {` (38); `const commandEncoder = device.createCommandEncoder();` (41); `commandEncoder.copyTextureToTexture(` (44); `{ texture: src_texture },  //src` (45); `{ texture: dst_texture },  //dst` (46); `{ width: calc_constants.WIDTH, height: calc_constants.HEIGHT, depthOrArrayLayers: 1 }` (47); `device.queue.submit([commandEncoder.finish()]);` (51). |
| 55–77 | runComputeShader_EncStack은 device.queue.writeBuffer로 uniform 버퍼에 쓴다. 계산 패스·파이프라인·바인드 그룹·디스패치(dispatch)·패스 종료는 전달받은 명령 인코더에 기록한다. 인코더를 반환한다. 원문(행 순서): `export function runComputeShader_EncStack(device, commandEncoder, uniformBuffer, uniforms, computePipeline, computeBindGroup, dispatchX, dispatchY) {` (55); `device.queue.writeBuffer(uniformBuffer, 0, uniforms);` (58); `const computePass = commandEncoder.beginComputePass();` (61); `computePass.setPipeline(computePipeline);` (64); `computePass.setBindGroup(0, computeBindGroup);` (65); `computePass.dispatchWorkgroups(dispatchX, dispatchY);` (68); `computePass.end();` (71); `return commandEncoder;` (74). [11-04 전수 검증 정정] |
| 78–89 | runCopyTextures_EncStack은 전달받은 인코더에 WIDTH·HEIGHT·깊이 1 텍스처 복사를 기록한다. 인코더를 반환한다. 원문(행 순서): `export function runCopyTextures_EncStack(commandEncoder, calc_constants, src_texture, dst_texture) {` (78); `commandEncoder.copyTextureToTexture(` (81); `{ texture: src_texture },  //src` (82); `{ texture: dst_texture },  //dst` (83); `{ width: calc_constants.WIDTH, height: calc_constants.HEIGHT, depthOrArrayLayers: 1 }` (84); `return commandEncoder;` (88). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–35: fetchShader는 응답을 텍스트로 반환하며 response.ok 검사는 없다.
- 55–75·78–89: EncStack 루틴은 인코더를 반환한다. 이 두 루틴에는 queue.submit 호출이 없다.
