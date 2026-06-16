---
title: "SWASH 기술문서(swashtech.pdf) 구조·범위 검수 — mimetic discretization 이론서"
model: SWASH
doc: swashtech.pdf
canonical_source: manual
citation_status: verified
verification_method: "swashtech.pdf (swash/doc/swashtech.pdf) full text 직접 추출(pdftotext -layout, /tmp/swashtech.txt 5010줄) 후 TOC + Ch1 §1.4-1.6 + Ch2 §2.1 + Ch7 §7 말미 + Ch8/9/10/12 stub + Ch11.1 SIP 직접 인용. 페이지는 PDF TOC 기준. 완성도(‘under preparation’/‘yet empty’) 표기는 본문 verbatim 확인."
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

> SWASH 공식 기술문서(Scientific/Technical documentation)의 구조·완성도·핵심 내용 검수. **AUDIT-LEDGER §1** SWASH manual-notes=0 갭의 첫 노트. ⚠ 본 문서는 **부분 완성** — 실질 내용은 Ch 2·5·7·11.1, 나머지 다수는 "under preparation" 또는 빈 챕터.

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
| 4 | Mimetic discretization on curvilinear grids | 57 | ⚠ 거의 빈약 |
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
- **mimetic 원리**: 연속 PDE 의 보존성을 **이산 레벨에서 모방(mimic)** 하면 비선형 불안정이 제거됨 (§2.1, p5-6). → C-grid 가 이 성질을 자연히 갖춤 = SWASH robustness 의 근거.
- 전개 도구 (§2.3-2.6): Hamiltonian formulation(p12) · differential forms + 일반화 Stokes 정리(p17) · 대수위상(cell complex·chain/cochain·coboundary·discrete Hodge star·de Rham complex, p25-44) · 직교격자 mimetic framework(§2.6, p45).

→ deep-dive 후보: Ch 2 의 mimetic framework 자체는 별도 source-analysis(SWASH C-grid 구현)와 연결할 가치. 본 노트는 overview 수준.

## 4. Ch 5 — 삼각격자 mimetic 이산화 (★ 보존성)

직교 삼각격자 상 천수방정식 mimetic 이산화 (p59-87): 도메인 이산화·metrics·exact discretization·dual-to-primal 보간·edge-based 보간·이류항 mimetic·벡터장 mimetic 재구성. **보존성 증명 3종** (§5.7, p75-82): 질량·운동량·에너지 보존. 운동량 force 이산화는 conserving vs non-conserving 분리(§5.8, p83-87).

## 5. Ch 7 — staggered mesh 분산 해석 (★)

격자 분산 관계 분석. SWASH 적용 차분: **2차 중심차분**(예시) + **1차 upwind**(dissipative). 결론(p100, verbatim 요지): "in SWASH, we also apply the first order upwind scheme. Since this scheme is dissipative, the associated modified wavenumber consists of the real part and the imaginary part. The real part is equal to that of the second order central differences ... the above analysis and conclusions also apply to the first order upwind scheme." → upwind 의 실수부 modified wavenumber = 중심차분과 동일, 허수부 = 소산 오차.

## 6. Ch 8 — 3D SWE (⚠ 빈 챕터, 외부 참조)

p101 verbatim: "This chapter is **yet empty**. The following link is left here to give an idea of what the content of this material will look like: SWASH − sigma layers." §1.5(p2) 보충: SWASH 의 3D(layer-averaged) 방정식 유도는 **TRIWAQ-in-SIMONA 기술문서 [111] (Marcel Zijlema, 1998)** 에서 다뤄졌고 SWASH 에 성공 적용. 추가 논문 [116,117,88,118].

→ 따라서 SWASH 3D sigma-layer 지배방정식은 본 문서로 검수 불가 — source-analysis(SwashImpLay* 등) + 원논문으로 보강 필요.

## 7. Ch 11.1 — SIP 선형 solver (★) + 문서 불일치 주의

penta-diagonal 비대칭 선형계 $A\vec{N}=\vec{b}$ (Eq 11.1) 를 **Strongly Implicit Procedure**(Stone 1968; Ferziger & Perić 1999)로 해결:

- ILU 근사 분해 $M=LU=A+K$ (Eq 11.2), $K$ small. elliptic PDE 해의 smoothness 가정 → 추가 대각 성분을 주변점 보간으로 근사, $K\phi\approx 0$.
- 반복 (Eq 11.3): $U\vec{N}^{s+1} = L^{-1}K\vec{N}^s + L^{-1}\vec{b}$, $U$ upper-triangular → back substitution, $L$ 가역.

⚠ **문서 불일치**: §11.1 본문이 미지수를 "**wave action vector** $\vec{N}$" 로 기술 — 이는 **SWAN 기술문서(swantech Ch 6 SIP)에서 복사된 흔적**. SWASH 는 위상해상(phase-resolving) 비정수압 모델로 **wave action 을 풀지 않음**(수위·유속·비정수압 압력을 품). 즉 SIP solver 메커닉(LU/ILU/penta-diagonal)은 유효하나 "wave action" 명명은 SWASH 문맥상 오기. 실제 SWASH 에서 SIP 가 푸는 대상 = **비정수압 압력 Poisson 계**([[swash-nonhydrostatic-pressure-solver]] 참조).

## 8. 검수 결론 + 후속

- **본 문서로 verified 가능**: SWASH 정체·범위·기원, mimetic 이산화 근거(C-grid 채택 이유), 삼각격자 보존성, 분산해석(중심/upwind), SIP solver.
- **본 문서로 불가(미완성)**: 3D sigma-layer 지배방정식(Ch 8 빈), 경계조건 구현(Ch 10), 수치 접근 종합(Ch 9), 병렬화(Ch 12) → **swashuse.pdf + source-analysis + 원논문**(Zijlema-Stelling 2005; Smit-Zijlema-Stelling 2013 등)으로 보강.
- AUDIT-LEDGER §1.1: swashtech.pdf 행 ⬜ → 🟡(overview, Ch2/5 deep 잔여).
- 후속 deep 후보: Ch 2 mimetic framework deep-note · swashuse.pdf 사용자 매뉴얼 검수 · SwashExp*/SwashImp* flow solver source-analysis.
