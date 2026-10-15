---
title: "SWASH 기술문서(swashtech.pdf) 구조·범위 검수 — mimetic discretization 이론서"
model: SWASH
doc: swashtech.pdf
canonical_source: manual
citation_status: verified
verification_method: "swashtech.pdf의 쪽별 판독 기록과 추출 텍스트를 대조했다. 식·수치·명칭은 해당 쪽 이미지로 확인했다. 코드 주장은 raw/source_code/swash/의 원문과 대조했다. 2026-10-15 recovery 보고서의 최종 수정안과 결론을 대조했다. PDF 쪽과 인쇄 쪽을 구분했다." # [10-15 전수 검증 정정]
last_source_check: "2026-10-15 (recovery 대조 반영)"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
verification_by: "Claude Opus 4.8 (1M context) — swashtech.pdf 직접 추출·인용"
verification_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWAN/manual-notes/swan-documentation-stack.md
---

# SWASH 기술문서 (swashtech.pdf) 구조·범위 검수

> SWASH 공식 기술문서(Scientific/Technical documentation)의 구조·완성도·핵심 내용 검수. ⚠ 본 문서는 **부분 완성** — 실질 내용은 Ch 2·5·7·11.1, 나머지 다수는 "under preparation" 또는 빈 챕터. [10-15 대조 정정]

## 1. 문서 정체

- **목적** (§1.2, p1): SWASH 의 수학 모델·수치 기법 + 구현 단계 reference. "the structure of the SWASH program" 에 대한 reference.
- **대상 독자** (§1.3, p1): 1차적으로 수학·수치 모델을 **수정·확장하려는 사람**. 해석·PDE·수치수학 기초 가정.
- **범위** (§1.4, p2, verbatim): "SWASH is a general-purpose numerical tool for simulating unsteady, **non-hydrostatic, free-surface, rotational flow and transport phenomena** in coastal waters as driven by waves, tides, buoyancy and wind forces." — 심해→해변/항만 파 변형, 급변류, 밀도류(하구·호수·강).
- **모델 핵심 목표** (Ch1 머리, p1): "solve the **nonhydrostatic, nonlinear, shallow water equations on a regular grid**."
- **기원** (§1.6, p3): 원저자 **Guus Stelling + Marcel Zijlema**, TU Delft, 2002. 기여자 Pieter Smit·Dirk Rijnsdorp·Tomo Suzuki·Panagiotis Vasarmidis·Joao Dobrochinski.
- **본 문서 미포함 주제** (§1.5, p2): 식생 wave damping · 부분 반사/투과 · 3D wave-induced current subgrid · floating objects (저널/논문 참조).

## 2. 챕터 맵 + 완성도 (★ = 실질 내용 / ⚠ = 미완성)

| Ch | 제목 | p | 완성도 |
|---|---|--:|---|
| 1 | Introduction | 1 | 부분 (§1.4·1.6 내용, §1.1 "under preparation") |
| **2** | **Physics-compatible discretizations on simplicial and cubical meshes** | 5 | ★ 핵심(~50p) |
| 3 | Mimetic discretization on Cartesian meshes | 55 | 단편 |
| 4 | Mimetic discretization on curvilinear grids | 57 | 제4장은 제목과 준비 중 문장만 있다. (`swashtech PDF p.65`: `This chapter is under preparation.`; [theory-framework ST1-319 수정안](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)) [10-15 대조 정정] |
| **5** | **Mimetic discretization on triangular meshes** | 59 | ★ 실질 (보존성 증명 포함) |
| 6 | Time integration | 89 | 단편 |
| **7** | **Dispersion analysis of staggered mesh discretizations** | 91 | ★ 실질 |
| 8 | Three-dimensional shallow water equations | 101 | ⚠ **"This chapter is yet empty"** (sigma layer 예정) |
| 9 | Numerical approaches | 103 | ⚠ "under preparation" |
| 10 | Implementation of boundary conditions | 105 | ⚠ "under preparation" |
| **11** | Iterative solvers (§11.1 SIP) | 107 | ★ §11.1만 |
| 12 | Parallel implementation aspects | 109 | ⚠ "under preparation" |

## 3. Ch 2 — physics-compatible(mimetic) 이산화 근거 (★ 핵심)

SWASH 의 공간 이산화는 **staggered Arakawa C-grid** 유한차분(직교 삼각·사각·곡선격자). Ch 2 는 *왜 C-grid 인가* 를 Hamiltonian 형식론 + 대수위상(algebraic topology)으로 정당화 (§2.1, p5):

- **두 가지 핵심 이슈** (§2.1, p5):
  1. **비선형 계산 불안정**(nonlinear computational instability) — 고비선형 천수계 수치모의에서 빈발. 선형 안정성과 달리 시간스텝 축소로 제어 안 됨 (Phillips 1950s [77] 최초 연구).
  2. **1차·2차 보존성**(primary/secondary conservation) — 물리·기하에서 자연 발생.
- **mimetic 이론의 설계 동기**: 원문은 이류 형식과 이산 보존 성질의 역할을 설명한다. (`swashtech PDF p.13–14`; [theory-framework 수정안](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)) [10-15 대조 정정]
- 전개 도구 (§2.3-2.6): Hamiltonian formulation(p12) · differential forms + 일반화 Stokes 정리(p17) · 대수위상(cell complex·chain/cochain·coboundary·discrete Hodge star·de Rham complex, p25-44) · 직교격자 mimetic framework(§2.6, p45).

코드의 곡선 격자 계량은 기술문서 제4장에서 유도하지 않는다. ([theory-framework ST1-319 수정안](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)) [10-15 대조 정정]

## 4. Ch 5 — 삼각격자 mimetic 이산화 (★ 보존성)

직교 삼각격자 상 천수방정식 mimetic 이산화 (p59-87): 도메인 이산화·metrics·exact discretization·dual-to-primal 보간·edge-based 보간·이류항 mimetic·벡터장 mimetic 재구성. **보존성 증명 3종** (§5.7, p75-82): 질량·운동량·에너지 보존. 운동량 force 이산화는 conserving vs non-conserving 분리(§5.8, p83-87).

## 5. Ch 7 — staggered mesh 분산 해석 (★)

swashtech PDF p.108은 1차 상류법도 사용한다고 적는다. ([theory-unstructured ST2-379 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
swashuse PDF p.96–97은 일반 수평 이류 기본값 BDF와 BREAKING 예외를 설명한다. ([theory-unstructured ST2-379 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
중심 차분으로 바꾸는 조건은 `src/SwashCheckPrep.ftn90:1072`의 `if ( isurf == 1 ) then` 내부에 있다. ([theory-unstructured ST2-379](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
또한 `pnums(6)`이 미지정 값일 때만 이 자동 선택을 적용한다. (`src/SwashCheckPrep.ftn90:1088–1091`; [theory-unstructured ST2-379](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
자동 선택 조건문은 `if ( .not. psurf(2) /= 0.3 .and. pnums(6) == -1. ) then`이다. (`src/SwashCheckPrep.ftn90:1088`; [theory-unstructured ST2-379](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
LINEAR의 후속 이류 해제는 [입력 파싱 노트의 theory-unstructured:ST2-356](../source-analysis/swash-input-parsing-check.md#문서와-코드-차이-10-15-대조)에 연결한다. ([theory-unstructured ST2-379 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]

분산 해석의 원문은 "in SWASH, we also apply the first order upwind scheme. Since this scheme is dissipative, the associated modified wavenumber consists of the real part and the imaginary part. The real part is equal to that of the second order central differences ... the above analysis and conclusions also apply to the first order upwind scheme."이다. (`swashtech PDF p.108`, 인쇄 p.100) [10-15 대조 정정]

## 6. Ch 8 — 3D SWE (⚠ 빈 챕터, 외부 참조)

제8장 본문은 비어 있다. (`swashtech PDF p.109`, 인쇄 p.101; [theory-unstructured 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
표시된 링크 글자는 `SWASH − sigmal layers`다. (`swashtech PDF p.109`; [theory-unstructured 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
링크 안내 원문은 `The following link is left here to give an idea of what the content of this material will look like: SWASH − sigmal layers.`이다. (`swashtech PDF p.109`) [10-15 대조 정정]

§1.5(p2) 보충: SWASH 의 3D(layer-averaged) 방정식 유도는 **TRIWAQ-in-SIMONA 기술문서 [111] (Marcel Zijlema, 1998)** 에서 다뤄졌고 SWASH 에 성공 적용. 추가 논문 [116,117,88,118].

## 7. Ch 11.1 — SIP 선형 solver (★) + 문서 불일치 주의

penta-diagonal 비대칭 선형계 $A\vec{N}=\vec{b}$ (Eq 11.1) 를 **Strongly Implicit Procedure**(Stone 1968; Ferziger & Perić 1999)로 해결:

- ILU 근사 분해 $M=LU=A+K$ (Eq 11.2), $K$ small. elliptic PDE 해의 smoothness 가정 → 추가 대각 성분을 주변점 보간으로 근사, $K\phi\approx 0$.
- 반복 (Eq 11.3): $U\vec{N}^{s+1} = L^{-1}K\vec{N}^s + L^{-1}\vec{b}$, $U$ upper-triangular → back substitution, $L$ 가역.

제11장의 `wave action vector`는 SWASH 호출 대상과 맞지 않는 명명이다. (`swashtech PDF p.115–116`; [theory-unstructured ST2-216 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
구조 격자 SIP 호출은 압력 보정 또는 수평 속도 성분을 전달한다. (`src/SwashExpDep2DHflow.ftn90:4092` `call sip( amat, rhs, dq )`; `src/SwashImpDepM2DHflow.ftn90:744` `call sip( amat, rhs, u1 )`; `src/SwashImpDepM2DHflow.ftn90:1194` `call sip( amat, rhs, v1 )`; [theory-unstructured ST2-216 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md)) [10-15 대조 정정]
비구조 압력 경로는 BiCGSTAB를 사용한다. (`src/SwashExpDepUflow.ftn90:1440`; `src/SwashImpDepUflow.ftn90:1749`; `src/SwashExpLayUflow.ftn90:2450`; [theory-unstructured ST2-216 수정안](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md); [비정수압 압력 솔버 노트](../source-analysis/swash-nonhydrostatic-pressure-solver.md)) [10-15 대조 정정] [10-15 전수 검증 보완]

## 8. 문서의 내용 범위 [10-15 대조 정정]

- **본 문서로 verified 가능**: SWASH 정체·범위·기원, mimetic 이산화 근거(C-grid 채택 이유), 삼각격자 보존성, 분산해석(중심/upwind), SIP solver.
- **미완성 장 목록**: 제4장 곡선 격자 이산화, 제8장 3D sigma-layer 지배방정식, 제10장 경계조건 구현, 제9장 수치 접근, 제12장 병렬화를 포함한다. (`swashtech PDF p.65,109,111,113,117`; [theory-framework ST1-321 수정안](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)) [10-15 대조 정정] [10-15 전수 검증 보완]
- 제4장은 제목과 준비 중 문장만 있다. (`swashtech PDF p.65`: `This chapter is under preparation.`; [theory-framework ST1-319 수정안](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)) [10-15 대조 정정]
- 곡선 격자 코드의 면적 식 원문은 `gsqs(indx) = dx1 * dy1`이다. (`src/SwashGeometrics.ftn90:328`; [theory-framework ST1-321](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md)) [10-15 대조 정정]

## 문서와 코드 차이 (10-15 대조)

확정 보고서: [theory-framework](../../../_staging/recovery/compare/swash-theory-framework-vs-code.md) · [theory-unstructured](../../../_staging/recovery/compare/swash-theory-unstructured-vs-code.md).

문서 판: SWASH 12.01 매뉴얼 swashuse·swashtech, 공개 저장소 `7949227` 2026-05-06 "release v12.01"에서 마지막 변경. 코드 판: VERNUM 12.01, 공개 저장소 main `a486d5f` 2026-05-26, 12.01 뒤 `608ffd7`·`9554c98` 포함. 문서 인용은 PDF 쪽 기준이다(본문 인쇄 쪽 = PDF 쪽 − 8).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| theory-framework:ST1-319 | 곡선 격자 장의 실제 상태 | `manual-notes/swash-tech-documentation-overview.md:38` `⚠ 거의 빈약`<br>swashtech PDF p.65: `This chapter is under preparation.`; p.66은 본문 없음. | — | C 문서 누락 (현재 노트) | 제4장은 제목과 준비 중 문장만 있다. 코드의 곡선 격자 계량은 기술문서 제4장에서 유도하지 않는다. |
| theory-framework:ST1-321 | 미완성 장 목록의 곡선 격자 누락 | `manual-notes/swash-tech-documentation-overview.md:86` `**본 문서로 불가(미완성)**: 3D sigma-layer 지배방정식(Ch 8 빈), 경계조건 구현(Ch 10), 수치 접근 종합(Ch 9), 병렬화(Ch 12)`<br>swashtech PDF p.65: `This chapter is under preparation.` | `src/SwashGeometrics.ftn90:328` `gsqs(indx) = dx1 * dy1` | C 문서 누락 (현재 노트) | 제4장 곡선 격자 이산화도 미완성 장에 포함된다. 이 노트에서 연결한 곡선 격자 코드의 근거는 `src/SwashGeometrics.ftn90:328`의 면적 식이다. [10-15 전수 검증 정정] |
| theory-unstructured:ST2-216 | `wave action vector` | swashtech PDF p.115: `N⃗ is the wave action vector to be solved`; p.116: `an initial guess for the wave action vector` | `src/SwashExpDep2DHflow.ftn90:4092` `call sip( amat, rhs, dq )`; `src/SwashImpDepM2DHflow.ftn90:744` `call sip( amat, rhs, u1 )`; `src/SwashImpDepM2DHflow.ftn90:1194` `call sip( amat, rhs, v1 )` | B 문서 오기 | 해석: SWASH의 구조 격자 호출자는 SIP에 비정수압 압력 보정 또는 수평 속도 성분을 미지수로 전달한다. 따라서 제11장의 `wave action vector`는 호출 대상과 맞지 않는 명명이며 B를 유지한다. 비구조 압력의 BiCGSTAB 호출과 구분한다(ST2-225). [10-15 결론 검증 정정] [10-15 결론 검증 보완] |
| theory-unstructured:ST2-379 | 수평 이류의 기본 고차 선택 | swashuse PDF p.96–97은 수평 BDF 기본값과 BREAKING 사용 시 중심 차분을 설명한다. swashtech PDF p.108은 1차 상류법도 사용한다고 적는다. | `src/SwashInit.ftn90:409` `pnums( 6) = -1.`; `src/SwashCheckPrep.ftn90:1102–1106` `if ( pnums(6) == -1. ) then`, `!`, `pnums(6) =  3.`, `pnums(7) = -1.`, `!`; `src/SwashCheckPrep.ftn90:1088–1091` `if ( .not. psurf(2) /= 0.3 .and. pnums(6) == -1. ) then`, `!`, `pnums(6) = 3.`, `pnums(7) = 1.`; `src/SwashCheckPrep.ftn90:1072–1109`의 전체 분기; `src/SwashReadInput.ftn90:909–918`의 BREAKING 입력. | C 문서 누락 | 일반 수평 이류 기본값은 BDF다. 중심 차분으로 바꾸는 조건은 `src/SwashCheckPrep.ftn90:1072`의 `if ( isurf == 1 ) then` 내부에 있다. 또한 pnums(6)이 미지정 값일 때만 이 자동 선택을 적용한다. C는 명령의 존재가 아니라 beta와 기존 이류 선택을 결합하는 준비 조건에 한정한다. MODE LINEAR의 후속 이류 해제는 ST2-356이다. [SWASH-git-verify-AD.md §3의 후속 변경 무관 목록](../../../_staging/recovery/compare/SWASH-git-verify-AD.md)에 포함된다. 문서 마지막 변경은 `7949227 2026-05-06 release v12.01`이다. 뒤의 `608ffd7`·`9554c98`은 이 행의 조건·식을 바꾸지 않았다. 판 차이 A의 근거가 아니다. [10-15 결론 검증 정정] [10-15 git 이력 판정] [10-15 전수 검증 정정] |
