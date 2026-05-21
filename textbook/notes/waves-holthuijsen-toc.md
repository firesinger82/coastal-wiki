---
title: "Waves in Oceanic and Coastal Waters — Holthuijsen 2007 TOC + 핵심 발췌"
source_id: holthuijsen2007
chapter: "전권 (Ch.1-9 + Appendix A-E)"
pages: "1-405"
page_offset_applied: false
topic: waves
canonical_source: self
citation_status: verified
verification_method: "AI cross-reference against textbook/md/Waves-Holthuijsen2007.md (850 KB, 405 pages, 16 headings 자체 추출 + TOC 직접 파싱). Holthuijsen 본인이 SWAN 공동 개발자라 Ch.9 전체가 SWAN의 1차 reference."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# Holthuijsen 2007 — *Waves in Oceanic and Coastal Waters*

> **출처**: Holthuijsen, L. H. (2007). *Waves in Oceanic and Coastal Waters*. Cambridge University Press. ISBN 978-0-521-86028-4. 405 pages.

**저자 소개**: Leo H. Holthuijsen (Delft University of Technology / UNESCO-IHE). JONSWAP 프로젝트 참여, 현대 wave forecasting 모델 개발 초기 멤버. **SWAN의 공동 개발자** (Simulating WAves Nearshore). Waves in Shallow Environments (WISE) group 10년 공동 의장.

## 1. TOC (verified, 직접 파싱)

### Ch.1 Introduction (p.1)
- 1.1 Key concepts
- 1.2 This book and its reader
- 1.3 Physical aspects and scales
- 1.4 The structure of the book

### Ch.2 Observation techniques (p.10)
- 2.2 Introduction
- 2.3 In situ techniques (wave buoys, wave poles, others)
- 2.4 Remote-sensing techniques (imaging, altimetry — laser/acoustic/radar)

### Ch.3 Description of ocean waves (p.24)
- 3.3 Wave height and period
- 3.4 Visual observations and instrumental measurements
- **3.5 The wave spectrum** (p.31)
  - random-phase/amplitude model
  - variance density spectrum
  - frequency–direction spectrum
  - wave-number spectra
- 3.6 Transfer functions and response spectra

### Ch.4 Statistics (p.56)
- 4.2 Short-term statistics — instantaneous elevation, wave height/period, wave groups, extreme values
- 4.3 Long-term statistics (wave climate) — initial-distribution, peak-over-threshold, annual-maximum, wave atlases

### Ch.5 Linear wave theory (oceanic waters) (p.106)
- 5.3 Basic equations and boundary conditions
- 5.4 Propagating harmonic wave (kinematics, dynamics, **dispersion relationship**, phase/group velocity, capillary)
- **5.5 Wave energy (transport)** (p.131)
- 5.6 Nonlinear, permanent waves (Stokes, cnoidal, solitary)

### Ch.6 Waves in oceanic waters (p.145)
- 6.3 Idealised cases (idealised wind, significant wave, 1D/2D spectrum)
- **6.4 Arbitrary cases** — **energy balance equation**, wave propagation·swell, generation by wind, nonlinear wave–wave interactions (**quadruplet**), dissipation (**white-capping**), energy flow, **first-/second-/third-generation wave models**

### Ch.7 Linear wave theory (coastal waters) (p.197)
- **7.3 Propagation** — **shoaling, refraction, diffraction**, tides·currents, reflections
- 7.4 Wave-induced **set-up and currents** (radiation stress, set-up/set-down)
- 7.5 Nonlinear, evolving waves — **Boussinesq model**
- 7.6 Breaking waves

### Ch.8 Waves in coastal waters (p.244)
- 8.3 Idealised cases (significant wave, 1D/2D spectrum)
- 8.4 Arbitrary cases — **action balance equation**, generation, nonlinear (quadruplet + **triad**), dissipation (white-capping, **bottom friction**, **depth-induced surf-breaking**), energy flow

### Ch.9 The SWAN wave model (p.286) — **canonical SWAN reference**
- 9.1 Key concepts
- 9.2 Introduction
- **9.3 Action balance**
  - 9.3.1 The action balance equation
  - 9.3.2 Generation by wind
  - 9.3.3 Nonlinear wave–wave interactions (quadruplet, triad)
  - 9.3.4 Dissipation (white-capping, bottom friction, depth-induced surf-breaking, reflection/transmission/absorption)
- 9.4 Wave-induced set-up
- 9.5 Numerical techniques (schemes, solvers, grids, boundaries, source terms, stability)

### Appendices
- A Random variables (p.310)
- B Linear wave theory (p.318)
- C Spectral analysis (p.324)
- D Tides and currents (... 별도 확인)
- E ... (확인)

## 2. 핵심 개념 (페이지별)

### 2.1 Significant wave (signiﬁcant wave height) — Ch.3, Ch.4

- 페이지: p.27-29 (definition), p.150 (modeling), p.85 (statistics)
- 통상 표기 H_s 또는 H_{m0}
- 정의: 1/3 highest waves의 평균 (H_{1/3}) 또는 spectral 0차 모먼트의 4√m₀
- 시각 평균에 가까운 인지값

### 2.2 Wave spectrum — Ch.3 §3.5

- p.31-51
- variance density spectrum E(f), frequency–direction spectrum E(f, θ)
- 1D, 2D, wave-number spectra
- random-phase/amplitude model (p.33)

### 2.3 Linear wave theory (분산 관계) — Ch.5 §5.4

- p.123: dispersion relationship `ω² = gk·tanh(kh)`
- 심해: `ω² = gk` (h → ∞)
- 천해: `ω² = ghk²` (kh → 0)
- 위상 속도 c = ω/k, 군 속도 c_g = ∂ω/∂k

### 2.4 Energy balance & action balance — Ch.6 §6.4, Ch.8 §8.4

- 오션: energy balance equation
- 천해 + 흐름: action balance (action density N = E/σ) — 흐름 보정에 필수
- Source terms:
  - **S_in**: generation by wind
  - **S_nl4**: nonlinear quadruplet (오션·천해)
  - **S_nl3**: triad (천해만)
  - **S_ds**: dissipation (white-capping + bottom friction + depth-induced breaking)

### 2.5 천해 변형 — Ch.7

- p.199: **Shoaling** (수심 감소에 따른 진폭 증가)
- p.202: **Refraction** (수심 변화에 따른 진행방향 변화)
- p.210: **Diffraction** (장애물·구조물 우회)
- p.225: **Wave-induced set-up** — radiation stress 결과 평균 해면 변동

### 2.6 SWAN — Ch.9 (전 챕터)

- p.286-309
- 3rd-generation phase-averaged spectral model
- Action balance + 4 source terms
- 직교·곡선·**비구조 격자** 지원
- Implicit numerical scheme (안정적, 천해 친화)

## 3. 검증된 발췌 (다른 source와의 정합)

### 3.1 산호 형식 (key concept 호환)

| 항목 | Holthuijsen | 한국 KHOA glossary | 정합 |
|---|---|---|---|
| Significant wave height H_s | Ch.3-4 | (별도 확인) | (조사 보강) |
| 풍파 (wind sea) | Ch.6 §6.3.1 idealised wind | [KHOA] 풍파 | (조사) |
| 너울 (swell) | Ch.6 §6.4.2 propagation | [KHOA] 너울 | (조사) |
| 천해파 (shallow water wave) | Ch.5 §5.4.3 dispersion 천해 한계 | [KHOA] (별도) | (조사) |
| Wave spectrum | Ch.3 §3.5 | [KHOA] 파랑 스펙트럼 | (조사) |

→ 한국 [KHOA]·[PORTCALS] glossary의 파랑 용어 정합은 별도 cross-check 노트 보강 예정.

### 3.2 다른 textbook과 비교

| 주제 | Holthuijsen 2007 | Hudspeth 2005 *Waves and Wave Forces* | Water Wave Mechanics |
|---|---|---|---|
| Linear theory | Ch.5 (oceanic), Ch.7 (coastal) | 더 광범위, 파력 중심 | 수파역학 일반 |
| Spectrum | Ch.3 §3.5 | (구조물 응답 중심) | 일반 spectrum |
| SWAN | **Ch.9 전부** | 미언급 | 미언급 |
| 천해 surf-breaking | Ch.8 §8.4.5 + Ch.9 §9.3.4 | 별도 | 일반 |

→ Holthuijsen은 **SWAN modeling의 canonical educational source**. 천해 spectral 모델링 시 Ch.6-9가 핵심.

## 4. 적용 — coastal-wiki 작성에 활용

- `concepts/waves/01-concept.md` — Ch.1, Ch.3 (정의·관측·파라미터)
- `concepts/waves/02-theory.md` — Ch.5, Ch.7 (linear theory, dispersion, energy)
- `concepts/waves/03-analysis-methods.md` — Ch.3 §3.5, Ch.4 (spectrum, statistics)
- `concepts/waves/04-code-and-tools.md` — Ch.6 §6.4.7 (1st/2nd/3rd-generation models) + Ch.9 (SWAN)
- `concepts/waves/05-examples.md` — DASHBOARD MPT 정점 데이터 + (시계열 분석)
- `concepts/waves/06-model-application.md` — SWAN canonical (Ch.9) + `models/SWAN/` link

## 5. 보강·미해결

- 한국 KHOA·PORTCALS glossary 파랑 용어 cross-check 별도 노트
- Hudspeth 2005 파력 챕터 발췌 (구조물 적용)
- Water Wave Mechanics 정밀 인용 (수파역학 기초)
- Holthuijsen Appendix B (Linear wave theory) 정밀 수식 인용

## 6. 연결

- `concepts/waves/` 6 파일 — 본 노트가 1차 source
- `models/SWAN/` — Ch.9 전체가 canonical
- `models/SWAN/manual-notes/swan-action-balance.md` — Holthuijsen §9.3 발췌 (작성 예정)
- 외부:
  - 책 정보: [Cambridge University Press 9780521860284](https://www.cambridge.org/9780521860284)
  - SWAN: [https://swanmodel.sourceforge.io/](https://swanmodel.sourceforge.io/)
