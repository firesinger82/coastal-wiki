# models/ADCIRC/source-analysis/local-workflow

> 사용자 본인의 ADCIRC 운영 환경 (`E:\` 경로) 분석 노트. **2026-05-24 manual-notes/ 에서 이관** — manual-notes 는 외부 docs catalog 전용이라 local-workflow 노트와 성격이 다름.

> **2026-06-12 2차 이관**: 메인 `source-analysis/` 에 섞여 있던 **wide6/wide7 한국 광역 메시 구축 프로젝트 클러스터 12 노트**를 여기로 통합. 사유 — 이들은 모델 소스코드 분석(canonical)이 아니라 **사용자 개인 메시 구축 프로젝트**(개인 run·로컬 `E:\` 파일 의존)이므로, 위키의 canonical 원칙(소스코드·매뉴얼·논문 기반)상 메인 source-analysis 네임스페이스에 두면 안 됨. **전부 `citation_status: verified → source-needed` 강등 + `classification: local-workflow-notes`**. ⚠️ **stale 경로 주의**: 본문이 인용하는 `E:\numerical_models\adcirc\projects\korea_wide\mesh_dev\wide6·wide7` 는 2026-05-11 `archive\wide_legacy_2026-05-11\mesh_dev\` 로 이동됨(추후 디스크 cleanup 시 삭제 가능). 경로는 provenance 기록일 뿐 재현 보장 아님.

## 1차 이관 (2026-05-24, 11 노트, 모두 `classification: local-workflow-notes`, `citation_status: source-needed`)

| # | 노트 | 주제 |
|---|---|---|
| 19 | [local-adcirc-essential-workflow](19-local-adcirc-essential-workflow.md) | E:\ADCIRC_essential — 본인 운영 디렉토리 구조 |
| 20 | [local-tidal-and-nws13-link](20-local-tidal-and-nws13-link.md) | 본인 fort.15 + 01_Input_BC + 02_Run |
| 21 | [local-jma-converter-project](21-local-jma-converter-project.md) | E:\numerical_models\adcirc\data\wind\jma → NWS=13 converter |
| 22 | [local-utilities-workflow](22-local-utilities-workflow.md) | 본인 util 스크립트 |
| 23 | [local-jma-gui-contract](23-local-jma-gui-contract.md) | JMA-MSM GUI 인터페이스 명세 |
| 24 | [local-fort22-structure-compatibility](24-local-fort22-structure-compatibility.md) | fort.22 호환성 |
| 25 | [local-wide6-mesh-evidence](25-local-wide6-mesh-evidence.md) | wide6 mesh (한국 광역) 자료 |
| 26 | [local-fortran-utilities-assessment](26-local-fortran-utilities-assessment.md) | 본인 Fortran utility |
| 30 | [local-python-mesh-install-and-api-check](30-local-python-mesh-install-and-api-check.md) | Python mesh tool 설치·API |
| 31 | [wide6-fort14-structural-check](31-wide6-fort14-structural-check.md) | wide6 fort.14 무결성 |
| 32 | [wide6-open-boundary-depth-check](32-wide6-open-boundary-depth-check.md) | wide6 open boundary depth |

## 2차 이관 (2026-06-12, 메인 source-analysis/ 에서 통합한 wide6/wide7 메시 프로젝트 12 노트)

| 노트 | 주제 |
|---|---|
| [adcirc-wide6-provenance-gap](adcirc-wide6-provenance-gap.md) | wide6 메시 재현불가 문제 진단 (failure-pattern은 `experience/failure-patterns/` 에도 별도 존재) |
| [adcirc-wide6-fort14-replay-recipe](adcirc-wide6-fort14-replay-recipe.md) | wide6 fort.14 재생성 레시피 |
| [adcirc-wide6-validation-principles](adcirc-wide6-validation-principles.md) | wide6 검증 원칙 |
| [adcirc-wide6-validation-checklist](adcirc-wide6-validation-checklist.md) | wide6 검증 체크리스트 |
| [adcirc-wide6-replay-candidate-matrix](adcirc-wide6-replay-candidate-matrix.md) | wide6 replay 후보 매트릭스 |
| [adcirc-wide7-bootstrap](adcirc-wide7-bootstrap.md) | wide7 메시 bootstrap |
| [adcirc-ocsmesh-vs-fort14-replay-mapping](adcirc-ocsmesh-vs-fort14-replay-mapping.md) | OCSMesh ↔ fort.14 replay 매핑 |
| [adcirc-oceanmesh-vs-ocsmesh-comparison](adcirc-oceanmesh-vs-ocsmesh-comparison.md) | OceanMesh2D vs OCSMesh 비교 (wide6 맥락) |
| [adcirc-oceanmesh2d-translation-review](adcirc-oceanmesh2d-translation-review.md) | OceanMesh2D 변환 리뷰 |
| [adcirc-mesh-revalidation-principles](adcirc-mesh-revalidation-principles.md) | 메시 재검증 원칙 |
| [adcirc-mesh-tool-selection](adcirc-mesh-tool-selection.md) | 메시 도구 선택 (프로젝트) |
| [adcirc-information-gaps](adcirc-information-gaps.md) | 프로젝트 정보 gap |

> 메인 `source-analysis/` 에는 canonical(ADCIRC 소스코드 file:line 기반)만 잔류. 잔류 판정 예: `adcirc-domain-design-process`(topic=general, 메시 프로젝트 인용 0) · `adcirc-wetting-drying-implementation`(NOLIFA/H0/NODECODE 소스분석 — wide6는 응용 맥락으로만 언급) · baseline/fort15/preprocessing 등 일반 방법론·소스분석.

## 검증 상태

모두 `source-needed` 유지. 사유:
- 외부 인용 불가 (`E:\` 사용자 local paths, 본 위키 외부)
- 객관 데이터 (재현 가능) 보장 어려움
- → 본 노트들의 verified 승격은 **raw 파일을 본 위키 안으로 가져오거나** (mesh·input file 일부 복사), 또는 **사용자 직접 검증** 후 가능

## 향후 후보 작업

- 일부 객관화 가능한 사례 (예: wide6 fort.14 structural check) → 결과를 `experience/adcirc-wide6-mesh-validation.md` 로 정식 experience 작성
- E:\ raw 파일 일부 (wide6 mesh fort.14 등) 를 `models/ADCIRC/raw/local/` 로 복사 → reproducibility 확보
- 그 외 일반 workflow 안내는 `concepts/` 또는 별도 `tutorials/` 디렉토리 후보
