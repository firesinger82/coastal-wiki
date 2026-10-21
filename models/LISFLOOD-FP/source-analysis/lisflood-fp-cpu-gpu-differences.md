---
title: "LISFLOOD-FP CPU·CUDA·Metal — 시간 간격과 수치 형식"
model: LISFLOOD-FP
component: cpu-cuda-metal-comparison
canonical_source: self
citation_status: verified
verification_method: "2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
verification_by: "Codex (최종 근거 행 전사 대조)"
verification_date: 2026-10-21
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Codex"
note_date: 2026-10-21
related:
  - lisflood-fp-architecture-source-map.md
  - lisflood-fp-metal-fv1.md
  - lisflood-fp-swe-fv1-dg2.md
  - lisflood-fp-cuda-gpu.md
source_scope: LISFLOOD-FP/*
---

# LISFLOOD-FP CPU·CUDA·Metal의 차이

이 노트는 최종 대조 기록의 결론을 옮긴 AI 정리이다.
표의 원문 인용은 결론 문장과 구분한다.
`cpu-gpu-swe` 행의 문서 원문 칸은 구현 대조의 CPU 원문을 싣는다.
해당 행의 코드 원문 칸은 CUDA·Metal 원문을 싣는다.
코드 인용의 기준은 `../raw/source_code/LISFLOOD-FP/`이다.

## 문서와 코드 차이 (10-21 대조)

PDF 매뉴얼의 표지는 `Code release 6.1.1`을 적는다. 표지 날짜는 2013-11-25이다. (user manual.pdf p.1) [10-21 전수 검증 정정]
`user manual.docx`의 표지는 변경 추적으로 `6.1.1`을 삭제하고 `8.0.0`을 추가한다. (user manual.docx p.1(변환본)) [10-21 전수 검증 정정]
이 DOCX의 판 이력 최상단에는 `8.0 Jul 20 2020`이 변경 추적으로 추가되어 있다. 기존 `5.9` 행은 그 아래에 있다. (user manual.docx p.5(변환본); [DOCX 판 식별](../../../_staging/recovery/compare/lisflood-docx-manual-vs-code.md#11-판-식별)) [10-21 전수 검증 정정]
`user manual +bridge.docx`의 표지는 `Code release 4.3.6`을 적는다. 표지 날짜는 2008-04-25이다. (user manual +bridge.docx p.1(변환본)) [10-21 전수 검증 정정]
현재 분석 코드는 Zenodo 8.2(`10.5281/zenodo.13121102`)에 공식 8.3 패치를 적용한 코드이다. ([8.3 배포 README](../raw/source_code/LISFLOOD-FP-8.3-package/README.md)의 19–24행) [10-21 전수 검증 정정]
내부 숫자 판은 8.1.0이다. (`VersionHistory.h:16–18`) [10-21 전수 검증 정정]
릴리스 이름은 8.3이다. (`VersionHistory.h:21–23`) [10-21 전수 검증 정정]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow:RF-007 | 첫 시간 간격·CFL 시점 | user manual.pdf p.16; user manual.docx p.20(변환본) `Initial guess for the optimum time step and maximum possible time step.` | CPU FV1: `swe/fv1.cpp:23–30`의 `if (Statesptr->adaptive_ts == ON)`, `Solverptr->Tstep = 1e-6;`, `Solverptr->Tstep = Solverptr->InitTstep;`.<br>CPU FV1: `swe/fv1.cpp:58` `Solverptr->t += Solverptr->Tstep;` 뒤 `swe/fv1.cpp:63`의 CFL.<br>CUDA FV1: `cuda/fv1/cuda_fv1_simulate.cu:161–170`의 현재 단계 CFL.<br>CUDA adaptive: `cuda/adaptive/cuda_adaptive_simulate.cu:184` `real dt        = C(0.001);`.<br>확인한 원문: user manual.pdf p.16; user manual.docx p.20(변환본); user manual +bridge.docx p.21(변환본) 쪽 이미지; `swe/fv1.cpp:23–30,58–64`; `cuda/fv1/cuda_fv1_simulate.cu:93–94,161–170`; `cuda/cuda_solver.templates.cu:19,36–39,74–84`; `cuda/adaptive/cuda_adaptive_simulate.cu:184,422–430,798` | C 문서 누락 | initial_tstep의 뜻과 별도로 해법별 첫 간격과 CFL 산정 시점을 적는다. CPU FV1은 `if (Statesptr->adaptive_ts == ON)`일 때 `Solverptr->Tstep = 1e-6;`로 시작한다. 그 조건이 거짓이면 `Solverptr->Tstep = Solverptr->InitTstep;`를 사용한다. 적응 시간 간격을 켠 CPU FV1은 전진 뒤 다음 CFL 간격을 구한다. 적응 시간 간격을 켠 CUDA FV1은 ghost 갱신 뒤 현재 전진 전에 CFL 간격을 구한다. CUDA adaptive는 `real dt        = C(0.001);`로 초기화한다. adaptive는 `if ( (current_time - sim_params.time) > C(0.0) )` 안에서 `current_time -= dt;`를 먼저 수행한다. 이어서 `dt = sim_params.time - current_time;`를 대입한다. 마지막으로 `current_time += dt;`를 수행한다. |
| cpu-gpu-swe:LG1-002 | 수치 형식과 기본 설정 | 구현 대조의 CPU 원문: `lisflood.h:76` `#define NUMERIC_TYPE double`; `lisflood.h:87` `#define NUMERIC_TYPE float` | CUDA: `cuda/cuda_flow.cuh:11-13` `NUMERIC_TYPE H;` / `NUMERIC_TYPE HU;` / `NUMERIC_TYPE HV;`<br>Metal: `metal/fv1/metal_fv1_kernels.metal:116–118` `float H;   // water height` / `float HU;  // x-momentum` / `float HV;  // y-momentum`<br>확인한 원문: `lisflood.h:75–93`; `config.default.cmake:2`; `cuda/cuda_flow.cu:4–12`; `metal/fv1/metal_fv1_kernels.metal:115–118`; `metal/fv1/metal_fv1_simulate.mm:575–580` | C 문서 누락 | CPU·CUDA의 수치 형식은 `_NUMERIC_MODE`에 따라 double 또는 float이다. 기본 CMake 설정은 `_NUMERIC_MODE=1`이다. Metal의 보존변수는 float이다. 식 대응은 부동소수점 재현성을 보장하지 않는다. |

## 연결

전체 해법의 실행 선택은 [아키텍처 맵](lisflood-fp-architecture-source-map.md)에 정리한다.
Metal의 fixed 설정·CFL 임계값·원천·출력 차이는 [Metal FV1 노트](lisflood-fp-metal-fv1.md)에 정리한다.

## 대조 근거

- callflow: [보고서](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md), [최종 근거 RF](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md).
- cpu-gpu-swe: [보고서](../../../_staging/recovery/compare/lisflood-cpu-gpu-swe.md), [최종 근거 LG1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LG1.md).
