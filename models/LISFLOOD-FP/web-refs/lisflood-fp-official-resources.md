---
title: "LISFLOOD-FP 공식 자료 — Bristol·SEAMLESS-WAVE·Zenodo 8.2·공식 8.3 패치·핵심 논문"
model: LISFLOOD-FP
canonical_source: external
external_source: "Zenodo API(record 13121102) 직접 query(2026-06-18) 로 v8.2 메타·라이선스·doi 확인 + WebSearch(2026-06-18) 로 Bristol/SEAMLESS-WAVE 공식 페이지 확인. 핵심 논문은 bibliographic."
citation_status: verified
verification_method: "Zenodo API 직접 query verbatim(title·version 8.2·doi:10.5281/zenodo.13121102·license gpl-2.0·pub 2024-07-29·LISFLOOD-FP-v8.2.zip 348MB). 공식 URL은 WebSearch landing. 핵심 논문 서지는 bibliographic. 2026-10-21 LISFLOOD-FP recovery 대조 보고서 반영"
last_source_check: "2026-10-21 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - ../README.md
  - ../source-analysis/lisflood-fp-architecture-source-map.md
---

# LISFLOOD-FP 공식 자료

> ⚠ **LISFLOOD-FP**(Bristol/Sheffield 수리 침수) ≠ **LISFLOOD**(EC-JRC 분포형 강우-유출). 별개 모델.

## 1. 공식 채널

| 자료 | URL |
|---|---|
| Bristol 페이지 | `https://www.bristol.ac.uk/geography/research/hydrology/models/lisflood/` |
| SEAMLESS-WAVE (v8.x) | `https://www.seamlesswave.com/LISFLOOD8.0.html` |
| **v8.2 정본 소스** | Zenodo **doi:10.5281/zenodo.13121102** (`https://zenodo.org/records/13121102`) |
| 공식 8.3 패치 | [배포 설명](../raw/source_code/LISFLOOD-FP-8.3-package/README.md); [패치 원문](../raw/source_code/LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch). 공식 8.2에 8.3 변경을 적용하는 자료다(배포 README:19–24, [최종 근거 LB1-408](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LB1b.md)). [10-21 대조 정정] [10-21 전수 검증 정정] |

## 2. v8.2 메타 (Zenodo API verbatim)

- title: "LISFLOOD-FP v8.2 hydrodynamic model" · version **8.2** · pub **2024-07-29**
- doi: **10.5281/zenodo.13121102** · creators: "LISFLOOD-FP developers"
- license: **GPL-2.0** · file: LISFLOOD-FP-v8.2.zip (348 MB, 3170 files)
- 빌드: CMake ≥3.13, Windows(MSVC/Intel)·Linux. netCDF·libnuma 의존.

## 3. 현재 적용한 8.3(8.2 + 공식 패치) [10-21 대조 정정]

현재 원자료는 공식 8.2에 공식 8.3 변경을 적용한 코드이다 (`../LISFLOOD-FP-8.3-package/README.md:19–24`). [10-21 대조 정정]
현재 배포판 표시는 8.3이다 (`VersionHistory.h:23`의 `#define LF_Release "8.3"`). [10-21 대조 정정]
숫자 판 8.1.0은 checkpoint 호환을 위해 유지한다 (`VersionHistory.h:16–22`). [10-21 대조 정정]
v8.3 별도 패키지는 GPL v3 본문을 동봉한다 (`../LISFLOOD-FP-8.3-package/LICENSE:1–2`의 `GNU GENERAL PUBLIC LICENSE`·`Version 3, 29 June 2007`). [10-21 대조 정정]
8.2 메타데이터와 8.3 동봉 파일의 판 귀속을 나누어 적는다 (`bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:27–31`, `../LISFLOOD-FP-8.3-package/LICENSE:1–2`). [10-21 대조 정정]

### 패치의 판 구분 [10-21 대조 정정]

- CUDA 최대 수심 격자: E·강함, 8.2 결함, 8.3에서 고침. 8.3은 전체 device 격자·0 초기화·host 복사로 메모리 문제를 고쳤다 (`cuda/cuda_max_field.cu:96–98,124–127`; docx-manual:LV1-286 최종 근거). [10-21 대조 정정]
- CUDA flux 동기화: E·강함, 8.2 결함, 8.3에서 고침. 8.2의 기존 barrier는 다음 writer가 이전 pass의 마지막 reader보다 먼저 실행되는 일을 막지 않는다 (`v8.2:cuda/fv1/cuda_fv1_solver.cu:328–383`, `cuda/fv1/cuda_fv1_solver.cu:354–381`; docx-manual:LV1-287 최종 근거). [10-21 대조 정정]
- DG2 전처리 NoData 기본값: E·강함, 8.2 결함, 8.3에서 고침. v8.3은 `pars.nodata_elevation = DEM_NO_DATA;`를 추가했다 (`preprocess/generateDG2DEM.cpp:43–62`, `preprocess/generateDG2start.cpp:43–45`; docx-manual:LV1-288 최종 근거). [10-21 대조 정정]
- NoData 질량 계산: v8.3은 `if (Hold == C(0.0)) continue;`로 0인 질량수지 덧셈을 건너뛴다 (`../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:75–89`; files-output:LI2-342 최종 근거). [10-21 대조 정정]
- Metal FV1은 v8.3에서 추가되었다 (`VersionHistory.h:31–32`). [10-21 대조 정정]
- v8.2 루트의 `format` 파일(내용 `5`)은 macOS에서 C++ 표준 헤더 이름을 가렸다(8.2 빌드 결함, 8.3에서 고침). E 코드 결함 후보의 강도는 중간이다 (`v8.2:format:1`, `../LISFLOOD-FP-8.3-package/README.md:37`; [Claude 최종 조정 LN1-127](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-claude-final.md)). [10-21 대조 정정] [10-21 전수 검증 정정]
- 8.3 패치는 format 파일을 삭제한다 (`../LISFLOOD-FP-8.3-package/lisflood-8.2-to-8.3.patch:264–268`; build-83:LN1-127 최종 근거). [10-21 대조 정정]

## 4. 핵심 논문 서지

- **Bates, Horritt, Fewtrell (2010)** — "A simple inertial formulation of the shallow water equations for efficient two-dimensional flood inundation modelling." *J. Hydrology* 387:33-45. → **ACC(local inertia) 솔버**(`fp_acc.cpp`)의 정식 근거.
- **Neal, Schumann, Bates (2012)** — sub-grid channel(SGC) 정식화. → `sgc.cpp`.
- **Shaw, Kesserwani, Neal, Bates, Sharifian (2021)** — "LISFLOOD-FP 8.0: the new model release including FV1/DG2 solvers and GPU." *Geosci. Model Dev.* → swe/ FV1·DG2·GPU 도입.
- **Kesserwani & Sharifian (2020)** — DG2 + **multiwavelet 적응 격자**(SEAMLESS-WAVE). → 실구현은 `cuda/adaptive/`(hwfv1/mwdg2, [적응 MRA 노트](../source-analysis/lisflood-fp-mwdg2-adaptive-mra.md)). `swe/dg2new.cpp`는 비가동 CPU 리팩터([SWE 노트](../source-analysis/lisflood-fp-swe-fv1-dg2.md)의 정정). 코드 내 인용 `cuda/adaptive/cuda_adaptive_simulate.cu:104`.

## 5. 연결

- [모델 개요](../README.md) · [아키텍처 맵](../source-analysis/lisflood-fp-architecture-source-map.md).
- 자매: [SFINCS](../../SFINCS/README.md) (Deltares reduced-complexity compound flooding) — ACC 계열과 동류 reduced-physics.
- 개념: [고속 침수 계열 비교](../../../concepts/storm-surge/07-ml-emulators.md).

## 문서와 코드 차이 (10-21 대조)

이 절은 최종 대조 기록의 결론을 옮긴 AI 정리이다.
표의 원문 인용은 결론 문장과 구분한다.
코드 인용의 기준은 `../raw/source_code/LISFLOOD-FP/`이다.
`../LISFLOOD-FP-8.3-package/` 인용은 코드 기준 경로의 형제 패키지를 뜻한다.
`v8.2:`는 이전 배포본을 뜻한다.
`bf804e23:models/LISFLOOD-FP/`는 반영 전 노트의 커밋과 경로를 뜻한다.

문서의 메타데이터 기록은 Zenodo 8.2를 가리킨다. 현재 코드는 Zenodo 8.2(10.5281/zenodo.13121102)에 8.3 변경을 적용한 판이다 (`../LISFLOOD-FP-8.3-package/README.md:19–24`, 최종 근거 LB1-408). 내부 숫자 판은 8.1.0이다 (`VersionHistory.h:16–18`). 릴리스 이름은 8.3이다 (`VersionHistory.h:23`). [10-21 전수 검증 정정]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| build-83:LN1-232 | 라이선스 기록의 판 귀속 | `bf804e23:models/LISFLOOD-FP/README.md:12` `- **라이선스**: **GNU GPL-2.0** (Zenodo 메타데이터; repo LICENSE 파일 본문 부재).`·`bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:31` `- license: **GPL-2.0** · file: LISFLOOD-FP-v8.2.zip (348 MB, 3170 files)` | 8.3 별도 패키지 `../LISFLOOD-FP-8.3-package/LICENSE:1–2` `GNU GENERAL PUBLIC LICENSE`<br>`Version 3, 29 June 2007`·`../LISFLOOD-FP-8.3-package/README.md:141–142`<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/README.md:12`; `bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:27–31`; `../LISFLOOD-FP-8.3-package/LICENSE:1–2`; `../LISFLOOD-FP-8.3-package/README.md:141–142` | A 판 차이 | v8.2 노트는 Zenodo 메타데이터의 라이선스를 GPL-2.0으로 기록한다. v8.3 별도 패키지는 GPL v3 본문을 동봉한다. 8.2 메타데이터와 8.3 동봉 파일의 판 귀속을 나누어 적는다. [10-21 전수 검증 정정] |
| build-83:LN1-248 | 8.2 서지·8.3 패키지 | `bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:25` `**v8.2 정본 소스**`·`bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:29–30`의 8.2·2024-07-29·10.5281/zenodo.13121102 | `../LISFLOOD-FP-8.3-package/README.md:19–24`의 8.2 기반 패치 설명·현재 `VersionHistory.h:23`의 LF_Release<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:25,29–30`; `../LISFLOOD-FP-8.3-package/README.md:19–24`; `VersionHistory.h:23` | A 판 차이 | 8.2 서지를 보존하고 현재 적용한 8.3 패키지를 별도로 연결한다. |
| theory:LT1-421 | 공식 자료의 적용 판 | `bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:25` “**v8.2 정본 소스**”; `bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:29` “version **8.2** · pub **2024-07-29**” | `../LISFLOOD-FP-8.3-package/README.md:19–26`의 8.2 원자료·패치 구조.<br>`VersionHistory.h:23` `#define LF_Release "8.3"`.<br>확인한 원문: `bf804e23:models/LISFLOOD-FP/web-refs/lisflood-fp-official-resources.md:25–31`; `VersionHistory.h:21–23`; `../LISFLOOD-FP-8.3-package/README.md:19–26` | A 판 차이 | 8.2 원 배포본과 현재 적용한 공식 8.3 패치를 별도 자료로 나열한다. 현재 원자료의 배포판은 8.3이라고 표시한다. |

## 대조 근거

- build-83: [보고서](../../../_staging/recovery/compare/lisflood-build-83-vs-code.md), [최종 근거 LN1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LN1.md).
- theory: [보고서](../../../_staging/recovery/compare/lisflood-theory-vs-code.md), [최종 근거 LT1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LT1.md).
- docx-manual의 적용 내역: [보고서 §4](../../../_staging/recovery/compare/lisflood-docx-manual-vs-code.md#4-노트-대조와-수정안), [최종 근거 LV1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LV1.md).
- files-output의 판 식별: [보고서 §4](../../../_staging/recovery/compare/lisflood-files-output-vs-code.md#4-노트-대조와-수정안), [최종 근거 LI2](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI2.md).
- par의 서지 유지안: [보고서 §4](../../../_staging/recovery/compare/lisflood-par-vs-code.md#4-노트-대조와-수정안), [최종 근거 LI1](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-LI1.md).
- callflow의 판 구분: [보고서 §6](../../../_staging/recovery/flow/LISFLOOD-FP-callflow.md#6-기존-노트-대조와-수정안), [최종 근거 RF](../../../_staging/recovery/compare/LISFLOOD-FP-conclusion-verify-RF.md).
