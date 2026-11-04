---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/architecture/WEBGPU_BINDING_PATTERN.md
lines: 71
sha256: 2d5aeef60c8155e1e8ad49c3f02c086a2dc617d823ce9ecd9faec270de3c0773
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# WEBGPU_BINDING_PATTERN.md — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 계산·렌더 pass별 JavaScript handler가 WGSL의 바인드 그룹(bind group) 배치를 만든다(3). `@group(0) @binding(N)` 번호와 handler 순서·`main.js` 인수가 일치해야 한다(5). handler는 `create_*_BindGroupLayout(device)`, `create_*_BindGroup(...)`, 텍스처(texture)/버퍼 번호 대응을 맡는다(11–13). 실행은 보통 `Run_Compute_Shader.js`, `Run_Tridiag_Solver.js`, `main.js`가 맡는다(15). WGSL은 `Globals`·바인딩·설정 크기 일치, 입력과 저장 출력 분리, 보통 `16 x 16` 작업 그룹을 전제하며 시계열·일부 전체 화면 경로는 예외다(19–23). handler는 하나 이상의 WGSL shader가 기대하는 layout과 bind group을 모두 만든다(3). handler 자체는 보통 dispatch하지 않는다(15). 입력·저장 출력 분리에는 JavaScript가 임시 텍스처를 쓰고 나중에 복사하는 경우라는 예외를 붙인다(22). [11-04 전수 검증 보완] |
| 25–47 | 동일 텍스처 읽기·쓰기를 피하려고 `txtemp_boundary`, `txtemp_Breaking`, `txtemp_bottom`, `txtemp_PCRx`, `txtemp_WaveHeight`를 쓴다고 설명한다(27). `BoundaryPass`·`Pass_Breaking`·`CalcMeans`·`CalcWaveHeight`는 임시 출력을 복사하고 PCR은 반복 중 교대한다(31–34). 공통 handler는 `Handler_Pass1.js`(표준/고차), `Handler_Pass2.js`(표준/HLLC/HLLEM), `Handler_Pass3.js`(NLSW/Boussinesq/COULWAVE), `Handler_Tridiag.js`(표준/COULWAVE), `Handler_UpdateTrid.js`(계수 변형)다(40–44). 일부 WGSL이 사용하지 않는 바인딩도 호환 계약으로 취급하라고 적는다(43·46). 임시 텍스처 사용 이유는 단일 pass에서 수치 알고리즘이 원하는 방식으로 동일 텍스처를 읽고 쓰는 것을 WebGPU가 허용하지 않기 때문이다(27). `BoundaryPass`의 임시 출력은 물·퇴적물·쇄파 상태다(31). `Pass_Breaking`의 복사 목적지는 `txBreaking`이다(32). `CalcMeans`와 `CalcWaveHeight`는 누적 진단 텍스처를 교체한다(33). `Handler_Pass3.js` 공유 이유는 세 변형의 넓은 binding layout이 같기 때문이다(42). `Handler_Tridiag.js`에서 모든 binding을 쓰지 않는 것은 표준 WGSL 파일이다(43). 공유 layout은 pipeline 선택을 단순화하지만 미사용 또는 오해를 부르는 binding 위험을 높인다(46). [11-04 전수 검증 보완] |
| 48–71 | 계산 handler에도 `fragment shader` 주석이 남고 복사된 머리말이 있으므로 선언·현재 호출을 우선하라고 적는다(50). 초기 `createRenderBindGroup()`은 `19-binding` 서명이며 일부 overlay 갱신 호출은 이전 인수 집합으로 보인다고 적는다(52). 변경 확인 대상은 셰이더 `@binding`, `Handler_*.js`, `main.js`의 `create_*_BindGroup()`, `Create_Textures.js`, 실행 뒤 복사·채널 의미다(56–63). 새 설정은 `constants_load_calc.js` 기본값·필요한 파생 계산·uniform 작성부·정확한 바이트 위치의 WGSL `Globals`·영향받은 pipeline/group 갱신을 안내한다(65–71). render bind group 변경을 계획하면 오래된 서명의 호출부를 주의 깊게 감사하라고 안내한다(52). `main.js`의 그룹 생성 호출은 모두 확인해야 한다(60). `Create_Textures.js`에서 확인하는 것은 texture format이다(61). 채널 재사용 전에 문서의 채널 의미를 확인한다(63). pipeline/bind group 재생성·갱신은 binding 계약이 바뀌는 경우다(71). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 50: 문서는 계산 바인딩에도 `fragment shader`라는 오래된 주석이 남아 있다고 적는다.
- 52: 문서는 초기 `createRenderBindGroup()`의 `19-binding` 서명과 일부 overlay 갱신 인수 집합의 차이 가능성을 적는다. 실제 호출부는 이 파일 판독 범위가 아니다.
