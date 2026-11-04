---
file: models/Celeris/raw/source_code/Celeris-WebGPU/docs/README.md
lines: 31
sha256: 282f892bb9f11aeb883b7f22a16e052f9dff6a83be77cee6804243f5d3049e61
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# README.md — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | 비-transect 코드의 손으로 작성한 문서 지도라고 설명한다(1–3). `transect` 구현은 의도적으로 제외하며 이 문서에서 동작이나 판독 범위를 추론하지 말라고 적는다(5). 문서 목적은 긴 세션 사이에서 각 파일의 책임·의존 GPU 텍스처와 binding·전체 연안 파랑 계산에서 pass의 위치에 관한 작업 지식을 보존하는 것이다(3). [11-04 전수 검증 보완] |
| 7–21 | `../ARCHITECTURE.md`, `architecture/SIMULATION_PIPELINE.md`, `architecture/DATA_AND_TEXTURES.md`, `architecture/CONFIGURATION.md`, `architecture/WEBGPU_BINDING_PATTERN.md`, `architecture/REFERENCE_PAPERS.md`를 역할별로 안내한다(9–14). 소스 안내는 `source/js/README.md`, `source/shaders/README.md`, `source/externals/README.md`이며 각각 JavaScript 제어·입출력, WGSL 계산 셰이더(compute shader)·렌더링, 외부 보조 스크립트다(16–20). 텍스처(texture)·바인딩(binding) 계약을 보존하는 목적을 적는다(3·11·13). `../ARCHITECTURE.md`는 상위 모델과 dataflow를 설명한다(9). `architecture/SIMULATION_PIPELINE.md`는 프레임별·timestep별 순서를 설명한다(10). `architecture/CONFIGURATION.md`는 기본값·예제 설정·파생 상수를 설명한다(12). `architecture/WEBGPU_BINDING_PATTERN.md`는 JavaScript handler와 WGSL shader의 일치 필요를 설명한다(13). `architecture/REFERENCE_PAPERS.md`는 저장소에 포함된 기술 논문을 요약한다(14). JavaScript 안내는 orchestration·data loading·texture allocation·handlers·rendering·output·UI modules를 포함한다(18). WGSL 안내는 수치 역할별로 셰이더를 묶는다(19). 외부 스크립트 안내는 local third-party/minified helper script를 다룬다(20). [11-04 전수 검증 보완] |
| 22–31 | 일반 변경 시 아키텍처 문서, JavaScript handler/orchestrator 문서, WGSL 문서, 실제 소스 순으로 읽으라고 적는다(24–29). 활성 파일과 prototype/stale 파일을 구별하며 오래된 handler 주석보다 실제 바인딩 순서와 현재 `main.js` 실행 경로를 우선하라고 적는다(31). 활성·prototype/stale 구별은 현재 코드 경로에서 확인 가능한 경우에 표시한다(31). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
