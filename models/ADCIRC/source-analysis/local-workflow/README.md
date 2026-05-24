# models/ADCIRC/source-analysis/local-workflow

> 사용자 본인의 ADCIRC 운영 환경 (`E:\` 경로) 분석 노트. **2026-05-24 manual-notes/ 에서 이관** — manual-notes 는 외부 docs catalog 전용이라 local-workflow 노트와 성격이 다름.

## 내용 (11 노트, 모두 `classification: local-workflow-notes`, `citation_status: source-needed`)

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

## 검증 상태

모두 `source-needed` 유지. 사유:
- 외부 인용 불가 (`E:\` 사용자 local paths, 본 위키 외부)
- 객관 데이터 (재현 가능) 보장 어려움
- → 본 노트들의 verified 승격은 **raw 파일을 본 위키 안으로 가져오거나** (mesh·input file 일부 복사), 또는 **사용자 직접 검증** 후 가능

## 향후 후보 작업

- 일부 객관화 가능한 사례 (예: wide6 fort.14 structural check) → 결과를 `experience/adcirc-wide6-mesh-validation.md` 로 정식 experience 작성
- E:\ raw 파일 일부 (wide6 mesh fort.14 등) 를 `models/ADCIRC/raw/local/` 로 복사 → reproducibility 확보
- 그 외 일반 workflow 안내는 `concepts/` 또는 별도 `tutorials/` 디렉토리 후보
