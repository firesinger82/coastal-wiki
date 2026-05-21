# models/SWAN

> **Canonical source**: 이 디렉토리(`models/SWAN/`)가 SWAN 모델의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: SWAN (Simulating WAves Nearshore)
- **저자/관리주체**: Delft University of Technology. 공동 개발자: **Leo H. Holthuijsen** (`Waves-Holthuijsen2007` 저자)
- **라이선스**: GPL-3.0
- **공식 사이트**: [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/)
- **공식 메뉴얼**: 별도 다운로드 (Scientific/Technical Documentation, Implementation Manual, User Manual)
- **공식 교과서**: **Holthuijsen (2007) Chapter 9 전체** ([`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md))
- **사용 도메인**: 천해·연안 풍파 (waves in coastal waters)
- **격자**: 직교/곡선/비구조(unstructured) 모두 지원, spectral 도메인 (주파수 × 방향)

## 하위 디렉토리

| 경로 | 내용 |
|---|---|
| `manual-notes/` | 공식 메뉴얼 발췌·정리 (TBD) |
| `source-analysis/` | 소스코드·알고리즘 분석. WINK 패턴 등 사용자 SWAN library 발췌 |
| `web-refs/` | 공식 사이트·논문·기술 자료 |

## 사용자 SWAN library 통합

본 디렉토리는 사용자 본인 자료 (`swan-library-firesinger` source = `D:\Numerical_models\01_Models\swan\Fin\07_SWAN_LIBRARY\`)와 연결:

- `source-analysis/wink-pattern.md` — WINK middle/detail 도메인 패턴 (사용자 정리)
- `source-analysis/jma-msm-wind-workflow.md` — JMA-MSM 바람 입력 파이프라인
- `manual-notes/swan-action-balance.md` — Holthuijsen Ch.9 §9.3 action balance equation 발췌

## 작성 우선순위

1. ~~생성~~ (완료, 2026-05-21)
2. `manual-notes/swan-action-balance.md` — Holthuijsen Ch.9 §9.3 action balance + source terms
3. `source-analysis/wink-pattern.md` — 사용자 WINK middle/detail
4. `web-refs/swan-official-resources.md` — 공식 사이트·논문 인용
5. `source-analysis/swan-input-cards.md` — SWAN INPUT/READINP 카드 정리

## 연결

- `concepts/waves/06-model-application.md` — 본 디렉토리를 canonical으로 인용
- `textbook/notes/waves-holthuijsen-toc.md` — Holthuijsen 2007 TOC + Ch.9 SWAN 발췌
- `swan-library-firesinger` source (`textbook/sources.yml`)
- 외부: [SWAN sourceforge](https://swanmodel.sourceforge.io/)
