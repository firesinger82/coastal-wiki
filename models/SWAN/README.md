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
| `source-analysis/` | 소스코드·알고리즘 분석 (Swan*.ftn90 서브루틴별, 27 노트) |
| `web-refs/` | swan-official-resources.md (verified 2026-05-24) — sourceforge·공식 매뉴얼·핵심 논문 (Booij-Ris-Holthuijsen 1999·Zijlema 2010·Rogers 2003·Dietrich 2011 SWAN+ADCIRC) |

## 주요 노트

- `manual-notes/swan-action-balance.md` — Holthuijsen Ch.9 §9.3 action balance + source terms
- `source-analysis/swan-command-file-reference.md` — SWAN INPUT/READINP 카드 정리
- `source-analysis/swan-source-coverage-audit.md` — 58 source file 인벤토리
- `web-refs/swan-official-resources.md` — 공식 사이트·논문 인용

## 연결

- `concepts/waves/06-model-application.md` — 본 디렉토리를 canonical으로 인용
- `textbook/notes/waves-holthuijsen-toc.md` — Holthuijsen 2007 TOC + Ch.9 SWAN 발췌
- 외부: [SWAN sourceforge](https://swanmodel.sourceforge.io/)
