---
title: "Delft3D dflowfm (Flexible Mesh) — 3 packages 구조 + D3D-4 vs FM 차이"
topic: delft3d-dflowfm-overview
canonical_source: self
citation_status: verified
verification_method: "models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/dflowfm/ + packages/ 직접 ls — 3 packages (dflowfm-cli_exe, dflowfm_kernel, dflowfm_lib) + 보조 디렉토리 (docs, interacter, res, scripts, tests, version) 직접 인용. Stelling & Duinmeijer (2003) + Kernkamp et al. (2011) 의 unstructured shallow water scheme reference (web-refs)."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-24
verification_by: "Claude Opus 4.7 (1M context) — 디렉토리 ls 직접"
verification_date: 2026-05-24
related:
  - models/Delft3D/source-analysis/delft3d_engines_overview.md
  - models/Delft3D/source-analysis/delft3d_flow2d3d_dispatcher.md
  - models/Delft3D/source-analysis/delft3d_dimr_coupling.md
---

# Delft3D `dflowfm` (Flexible Mesh) — 모던 unstructured 엔진

> 출처: [`models/Delft3D/raw/source_code/Delft3D/src/engines_gpl/dflowfm/`](../raw/source_code/Delft3D/src/engines_gpl/dflowfm/) 직접 구조. **Delft3D-FM (Flexible Mesh)** 의 핵심 엔진 — 2010년대 이후 Deltares 의 modernization 결과.

## 1. dflowfm 디렉토리 layout

```
engines_gpl/dflowfm/
├── docs/        — FM 별도 문서
├── interacter/  — 인터랙티브 UI
├── packages/    — 3 Fortran package (아래 §2)
├── res/         — 리소스
├── scripts/     — 빌드·운영 스크립트
├── tests/       — 단위·통합 테스트
└── version/     — 버전 관리
```

## 2. 3 Packages 구조 (verified)

| Package | 역할 |
|---|---|
| `dflowfm-cli_exe` | **Command-line executable** — standalone CLI launcher |
| `dflowfm_kernel` | **수치 핵심** — Stelling-Kernkamp staggered unstructured scheme |
| `dflowfm_lib` | **공유 라이브러리** — Python/Java/C 바인딩 + dimr integration |

→ flow2d3d (8 packages) 보다 단순. 모던 SOLID 설계.

## 3. D3D-4 (flow2d3d) vs Delft3D-FM (dflowfm) 비교

| 항목 | **flow2d3d** (D3D-4, 1990s legacy) | **dflowfm** (D3D-FM, 2010s+) |
|---|---|---|
| 격자 | structured curvilinear | **unstructured** (triangle/quad mixed) |
| 수치 scheme | TRISULA ADI (Stelling-Leendertse) | **Stelling-Kernkamp staggered** (Stelling-Duinmeijer 2003, Kernkamp 2011) |
| Time-stepping | implicit ADI | semi-implicit |
| Vertical | sigma (또는 z) | sigma + z + sigma-z (hybrid) |
| Packages | 8 (flow2d3d + 7 sub) | **3** (cli·kernel·lib) — 단순화 |
| Coupling | dimr 외 한정 | **dimr native** |
| Bench example | 호수·하구·연안 (curvilinear) | 비정형 영역 (강 분류·complex 해안선·범람) |
| 본 위키 분석 | [[delft3d_flow2d3d_dispatcher]] | 본 노트 (M-D 2차 신설) |
| 사용 시기 | 1990s-2020s (legacy operation) | 2015s~ 현대 (신규 프로젝트 권장) |

## 4. 수치 scheme — Stelling & Duinmeijer 2003

> "A staggered conservative scheme for every Froude number in rapidly varied shallow water flows" *Int. J. Numer. Meth. Fluids* 43:1329-1354

핵심 특징:
- **Staggered grid** — water level at cell centers, momentum at edges
- **Conservative** — mass + momentum 모두 conservation
- **Sub-critical → super-critical 전이** 자동 처리 (Froude 임의)
- **Unstructured** mesh 지원 (triangle/quad)

Kernkamp et al. 2011 (Continental Shelf 확장) — efficient 대규모 도메인.

## 5. 운영 결정 — D3D-4 vs FM 선택

| 시나리오 | 권장 엔진 |
|---|---|
| 기존 D3D-4 모델 운영 (legacy MDF) | flow2d3d (변경 없음) |
| 신규 모델 — complex 해안선 (만 + 강 + 섬) | **dflowfm** |
| 신규 모델 — rectangular curvilinear | flow2d3d 또는 dflowfm 둘 다 가능 |
| 다른 모델 결합 (FLOW+WAVE+WAQ+RTC) | **dflowfm + dimr** (native integration) |
| 강 범람·sub-super-critical 전이 | **dflowfm** (Stelling 2003 scheme) |
| 표사 + morphology (검증 history) | flow2d3d (validation literature 풍부) |

→ **2026 신규 한국 적용** = dflowfm 검토 권장 (모던 + complex coast 지원). Legacy operation 은 flow2d3d 유지.

## 6. dimr 결합 (별도 노트)

dflowfm 는 dimr framework 와 native 결합 → [[delft3d_dimr_coupling]] (신설 M-D 2차) 참조.

## 7. 본 위키 dflowfm 분석 현황

| 항목 | 상태 |
|---|---|
| 디렉토리 구조 | ✅ 본 노트 (verified) |
| kernel scheme 상세 | 미분석 (Stelling-Duinmeijer paper 직접 인용 필요) |
| Python/Java binding 사용법 | 미분석 |
| MDU file (FM input) 운영 | 미분석 (D3D-4 MDF 와 다른 포맷) |
| hydromt_delft3dfm Python 자동화 | [`raw/source_code/hydromt_delft3dfm/`](../raw/source_code/hydromt_delft3dfm/) 참조 |

## 8. 작성 우선순위 (남은 M-D)

- `delft3d_dflowfm_kernel_scheme.md` — Stelling-Duinmeijer + Kernkamp scheme equation level
- `delft3d_dflowfm_mdu_input.md` — MDU file 카드 family (FM의 MDF 대체)
- `delft3d_hydromt_dflowfm.md` — Python automation framework

## 9. 관련 자료

- [[delft3d_engines_overview]] — 12 engines 개관
- [[delft3d_flow2d3d_dispatcher]] — D3D-4 legacy 엔진 (대비)
- [[delft3d_dimr_coupling]] — dflowfm 의 native coupling (신설)
- [[../manual-notes/delft3d-manuals-overview]] — 53 PDFs 인덱스
- [[../web-refs/delft3d-official-resources]] — Stelling-Duinmeijer 2003 + Kernkamp 2011 인용
- 외부: [Deltares OSS Delft3D-FM](https://oss.deltares.nl/web/delft3dfm), [hydromt_delft3dfm](https://github.com/Deltares/hydromt_delft3dfm)
