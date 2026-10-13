---
last_source_check: "2026-10-13 (recovery 대조 반영)"
verification_method: "2026-10-13 recovery 대조 보고서 R1–R8 반영"
---

# models/SWAN

> **Canonical source**: 이 디렉토리(`models/SWAN/`)가 SWAN 모델의 구현·메커닉에 대한 진실의 원천.

## 정체 카드

- **이름**: SWAN (Simulating WAves Nearshore)
- **저자/관리주체**: Delft University of Technology. 공동 개발자: **Leo H. Holthuijsen** (`Waves-Holthuijsen2007` 저자)
- **라이선스**: GPL-3.0
- **공식 사이트**: [SWAN 공식 자료](web-refs/swan-official-resources.md)
- **공식 메뉴얼**: 별도 다운로드 (Scientific/Technical Documentation, Implementation Manual, User Manual)
- **공식 교과서**: **Holthuijsen (2007) Chapter 9 전체** ([`textbook/notes/waves-holthuijsen-toc.md`](../../textbook/notes/waves-holthuijsen-toc.md))
- **사용 도메인**: 천해·연안 풍파 (waves in coastal waters)
- **격자**: 직교/곡선/비구조(unstructured) 모두 지원, spectral 도메인 (주파수 × 방향)

전체 격자 지원을 모든 물리 모듈의 지원으로 해석하지 않는다. (R3:NT-051; [set-up 대조](../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#5-차이-결론).)

## 소스 스냅샷

코드 VERNUM 41.51, 원본 저장소 HEAD 43e9bbb(2026-07-13 patch B), 이력 98커밋(2022-07-30~2026-07-13), 공개판 커밋 41.45(2023-02-27~28)·41.51(7ee8981 2024-09-02).

코드 기준은 43e9bbb의 41.51AB이다. (`src/swanmain.ftn:965` `VERNUM = 41.51`; `src/swanmain.ftn:967` `CALL BUGFIX ('A')`; `src/swanmain.ftn:968` `CALL BUGFIX ('B')`; [R7 판 정보](../../_staging/recovery/compare/swan-implementation-history-vs-code.md#1-요약), [git 판정](../../_staging/recovery/compare/SWAN-git-verify-A.md). 이력 수 98커밋은 [git 판정 D §1](../../_staging/recovery/compare/SWAN-git-verify-D.md#1-요약)의 집계이다. 이력 기간은 [노트 반영 기록 7](../../_staging/recovery/flow/SWAN-notes-apply-7.md)의 원본 저장소 `git log` 집계이다.) [10-13 전수 검증 보완]

## 하위 디렉토리

| 경로 | 내용 |
|---|---|
| `manual-notes/` | 공식 매뉴얼 4종(swanuse·swantech·swanimp·swanpgr) 발췌·정리 — **29 노트** <!-- count: models/SWAN/manual-notes/swan-*.md = 29 --> (swantech Ch2-8 전장 deep + swanuse §4 command 3부작). swanuse·swantech·swanimp는 Cycle III 41.51이다. swanpgr는 v1.3이다. 마지막 문서 이력은 2006-03-22이다. (swanuse·swantech·swanimp 각 PDF 1쪽; [swanpgr PDF 51쪽 / 인쇄 45쪽](raw/manuals/pdfs/swanpgr.pdf); R7:N-033.) [10-13 전수 검증 보완]
| `source-analysis/` | 소스코드·알고리즘 분석 (Swan*.ftn90 서브루틴별 + swancom1 cross-walk·setup 솔버, **28 노트**) |
| `web-refs/` | **4 노트** — official-resources · foundational-papers(8 원논문) · ml-surrogate-models(DELWAVE·DeepONet·Ferdaus 등 full-PDF) · recent-research-2024-2026 |

## 주요 노트

- `manual-notes/swan-action-balance.md` — Holthuijsen Ch.9 §9.3 action balance + source terms
- `source-analysis/swan-command-file-reference.md` — SWAN INPUT/READINP 카드 정리 — [R5 물리·수치 명령 대조](../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#5-차이-결론).
<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn90 = 57 -->
<!-- count: models/SWAN/raw/source_code/swan/src/*.ftn = 18 -->
- `source-analysis/swan-source-coverage-audit.md` — 75 source file 인벤토리(`.ftn90` 57 + `.ftn` 18)
- [R2 원천항 이론·코드 대조](../../_staging/recovery/compare/swan-theory-sources-vs-code.md#5-차이-결론) — 코드 기준은 43e9bbb의 41.51AB이다.
- [R4 설정·입력 명령 대조](../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#1-요약) — [명령별 조건](../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#2-대조-표).
- `web-refs/swan-official-resources.md` — 공식 사이트·논문 인용

## recovery 대조 보고서

2026-10-13 recovery 전수 판독·대조 반영.

| 보고서 | 범위 | 확정 결론 |
|---|---|---|
| R1 | 이론·수치해법 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-theory-numerics-vs-code.md#4-노트-대조와-수정안) |
| R2 | 이론·원천항 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-theory-sources-vs-code.md#4-노트-대조와-수정안) |
| R3 | 장애물·set-up·QC·경계조건 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-theory-obstacles-setup-qc-bc-vs-code.md#4-노트-대조와-수정안) |
| R4 | 입력·설정 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-inputs-setup-vs-code.md#4-노트-대조와-수정안) |
| R5 | 입력·물리·수치 명령 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-inputs-physics-numerics-vs-code.md#4-노트-대조와-수정안) |
| R6 | 출력 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-outputs-vs-code.md#4-노트-대조와-수정안) |
| R7 | 구현·프로그래밍 규칙·수정 이력·패치 | [노트 수정안·차이 결론](../../_staging/recovery/compare/swan-implementation-history-vs-code.md#4-노트-대조와-수정안) |
| R8 | 실행·호출 흐름 | [호출 흐름도](../../_staging/recovery/flow/SWAN-callflow.md#4-호출-흐름도), [노트 수정안](../../_staging/recovery/flow/SWAN-callflow.md#6-기존-노트-대조와-수정안), [차이 결론](../../_staging/recovery/flow/SWAN-callflow.md#8-차이-결론) |

## 연결

- `concepts/waves/06-model-application.md` — 본 디렉토리를 canonical으로 인용
- `textbook/notes/waves-holthuijsen-toc.md` — Holthuijsen 2007 TOC + Ch.9 SWAN 발췌
- 외부: [SWAN 공식 자료](web-refs/swan-official-resources.md)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치 (swanpgr v1.3, 2006-03-22). 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb (2026-07-13 patch B).

표의 원문 인용과 AI 결론은 [R7 §5](../../_staging/recovery/compare/swan-implementation-history-vs-code.md#5-차이-결론)에서 옮겼다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R7:N-033 | 모델 README의 문서 판 | `models/SWAN/README.md:20` ``\| `manual-notes/` \| 공식 매뉴얼 4종(swanuse·swantech·swanimp·swanpgr) 발췌·정리 — **29 노트** (swantech Ch2-8 전장 deep + swanuse §4 command 3부작 + v41.51 기준) \|``; swanpgr PDF 51쪽(인쇄 45쪽), 쪽 이미지 `swanpgr-51.png`의 마지막 문서 이력 `1.3`, `March 22, 2006`. | `src/swanmain.ftn:965–968` `VERNUM = 41.51`, `CALL BUGFIX ('A')`, `CALL BUGFIX ('B')`. | C 문서 누락 | README의 문서 판 표기에서 swanuse·swantech·swanimp의 41.51과 swanpgr v1.3을 구분한다. swanpgr의 마지막 문서 이력은 2006-03-22이다. 코드 기준은 43e9bbb의 41.51AB이다. |
