---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/architecture/REFERENCE_PAPERS.md
lines: 50
sha256: 513a096b3b345ac16dda5a61bfa271bab6e6a008bf56b88534764a15924c850d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# REFERENCE_PAPERS.md — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | `docs/`의 논문과 소스 계보를 연결하는 안내이며 논문 자체의 대체물이 아니라고 적는다(3). `Lynett Et Al. 2026`은 서버 계산·빌드가 없는 브라우저 WebGPU와 WGSL 계산 셰이더(compute shader)를 설명한다고 적는다(5–7). 비선형 천수·Boussinesq·고차/COULWAVE, 쌍곡항의 유한체적법(finite-volume)과 분산성(dispersive) 항의 유한차분법(finite-difference)·암시 풀이 혼합, 지형 편집·교란·설계·지도·시계열 상호작용을 연결한다(11–14). WebGPU compute는 이전 graphics/engine 전용 GPU shader 접근을 대체한다(11). 상호작용은 뒤늦게 붙인 기능이 아니라 모델 설계의 일부라고 설명한다(14). [11-04 전수 검증 보완] |
| 16–36 | `Tavakkol And Lynett 2017`은 이전 GPU 셰이더 기반 Boussinesq 선행 연구라고 적는다(16–18). 명시 유한체적 갱신과 분산 보정 분리, 이동 해안선/습윤·건조, 삼중대각 병렬 순환 축소(Parallel Cyclic Reduction), 상호작용 시각화를 연결한다(22–25). `Tavakkol And Lynett 2020`의 Celeris Base는 지도·관측점·몰입형 표시 작업 흐름을 강조했다고 적는다(27–29). `main.js`, `File_Loader.js`, `File_Writer.js`와 렌더 셰이더, 스펀지·경계·GPU 자원 관리를 연결한다(33–35). 2017 연구는 browser WebGPU를 사용하지 않았지만 수치 구조를 현재 저장소에서 알아볼 수 있다고 설명한다(18). 이동 해안선·wet/dry 논리는 solver의 중심이다(23). 상호작용 시각화와 빠른 시나리오 피드백은 후처리 단계가 아니라 핵심 목표다(25). 2020 연구는 모델을 접근하기 더 쉬운 앱 환경으로 옮겼다(29). WebGPU판은 상호작용 시나리오 설계를 정적 browser 앱으로 구현한다(33). 해당 파일의 UI·overlay 영상·시계열 관측·export 기능이 이 작업 흐름을 잇는다(34). sponge·경계·시각화·GPU 자원 관리는 방정식 kernel만큼 앱에 중요하다고 적는다(35). [11-04 전수 검증 보완] |
| 37–50 | 수치 커널 변경 시 WebGPU 논문, 이전 Celeris 논문, `docs/architecture/SIMULATION_PIPELINE.md`, `docs/source/shaders/` 순서를 권한다(39–44). UI·표시·시나리오 로딩 변경 시 WebGPU 논문, `2020` Celeris Base 논문, `main.js`, `File_Loader.js`, `File_Writer.js`, `Handler_Render.js`, `fragment.wgsl`, `Copytxf32_txf16.wgsl` 문서를 권한다(46–50). 수치 kernel 변경 시 WebGPU 논문은 현재 아키텍처를 위해 읽는다(41). 이전 논문은 Boussinesq/PCR·wet-dry 계보를 위해 읽는다(42). UI 계열 변경 시 WebGPU 논문은 browser 모델을 위해 읽는다(48). 2020 논문은 작업 흐름 맥락을 위해 읽는다(49). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
