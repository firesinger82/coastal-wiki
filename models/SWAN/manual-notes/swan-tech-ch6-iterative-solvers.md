---
title: "SWAN swantech Ch 6 Iterative solvers — Strongly Implicit Procedure (SIP) + SOR verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) Ch 6 Iterative solvers §6.1 Strongly Implicit Procedure (SIP) + §6.2 Successive Over Relaxation (SOR) technique, doc p.127-128 (Eq 6.1-6.3). References: Stone 1968, Ferziger-Perić 1999, Botta-Ellenbroek 1985."
citation_status: verified
verification_method: "swantech.pdf (v41.51) Ch 6 직접 read via pdftotext (식 번호 context-verified: AN=b 6.1·M=LU=A+K 6.2·SIP iteration 6.3) + website_markdown node78-80.md LaTeX alt-text. Ch 6은 chapter-local 번호라 website=PDF 일치. §6.2 SOR은 PDF 'under preparation' (Botta-Ellenbroek 1985 참조만)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 6.1-6.3 verbatim, PDF 식 번호 context-검증, SOR stub 명시"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch4-5-bc-2d-setup.md
---

# swantech Ch 6 Iterative solvers (SIP/SOR) — verified verbatim

> swantech.pdf (v41.51) Ch 6 직접 read. SWAN 의 **두 선형계 iterative solver** — **SIP** (action balance spectral 계, §3.3 에서 참조) + **SOR** (2D setup Poisson 계, Ch 5 에서 참조). §3.3([[swan-tech-ch3-solution-iteration-limiter]])의 "SIP" 와 Ch 5([[swan-tech-ch4-5-bc-2d-setup]])의 "modified SOR" 를 형식화.
>
> **식 번호 주의**: Ch 6은 chapter-local 번호 → **website = PDF 일치**.

## 1. §6.1 Strongly Implicit Procedure (SIP)

선형계:
$$A\vec{N} = \vec{b} \quad \text{(6.1)}$$
- $A$ = 비대칭 **penta-diagonal** 행렬, $\vec{N}$ = wave action vector, $\vec{b}$ = source term + 경계값
> ([[swan-tech-ch3-solution-iteration-limiter]] §3.3 Eq 3.20 의 $A\vec{N}=\vec{b}$ 와 동일 — directional quadrant 의 spectral 계.)

### 1.1 SIP 원리 (Stone 1968, Ferziger-Perić 1999)

LU 분해는 우수한 범용 solver 이나 sparseness 활용 못함. Iterative method 서 $M = LU$ 가 $A$ 의 좋은 근사면 빠른 수렴 → **$A$ 의 근사 LU 분해를 iteration matrix $M$ 으로**:
$$M = L\,U = A + K \quad \text{(6.2)}$$
- $L, U$ sparse, $K$ small
- **ILU (incomplete LU)**: $A$ 의 0 원소엔 $L$/$U$ 대응 원소도 0. 단 $LU$ 는 $A$ 보다 비영 대각 증가 → $K$ 가 그 추가 대각 포함 (느린 수렴)
- **Stone 통찰**: elliptic PDE 근사면 해 smooth → 추가 대각 unknown 을 주변 점 보간으로 근사. $K$ 가 7 대각 모두 비영 허용 + 보간 → 주어진 근사해 $\phi$ 서 **$K\phi \approx 0$** → $M$ 이 $A$ 에 근접 (6.2)

### 1.2 SIP iteration (Eq 6.3)

초기 추정 $\vec{N}^0$ 부터:
$$U\vec{N}^{s+1} = L^{-1}K\vec{N}^s + L^{-1}\vec{b} \quad \text{(6.3)}$$
- $U$ upper triangular → **back substitution** 효율
- $L$ 쉽게 invertible (핵심 feasibility)
- $s=0,1,2,\cdots$ 수렴까지 반복

## 2. §6.2 Successive Over Relaxation (SOR)

> **PDF "This section is under preparation. See also Botta and Ellenbroek (1985)."** — 식 미수록.

SWAN 의 **2D wave setup Poisson 식**(Ch 5 Eq 5.2, 5.25 $Ax=f$)을 **modified SOR** (Botta-Ellenbroek 1985)로 해법 ([[swan-tech-ch4-5-bc-2d-setup]] §B.6). 비대칭·singular(전 Neumann) 가능 행렬 대응.

## 3. 두 solver 의 역할 구분

| solver | 적용 계 | 행렬 | 위치 |
|---|---|---|---|
| **SIP** (§6.1, Eq 6.1-6.3) | action balance spectral 계 ($A\vec{N}=\vec{b}$) | 비대칭 penta-diagonal | [[swan-tech-ch3-solution-iteration-limiter]] §3.3 |
| **modified SOR** (§6.2, stub) | 2D setup Poisson 계 ($Ax=f$) | 비대칭 9-point, singular 가능 | [[swan-tech-ch4-5-bc-2d-setup]] Ch 5 |

> 무전류 시 spectral $A$ 는 tri-diagonal 환원 → Thomas algorithm (§3.3).

## 4. 한계

- §6.2 SOR 은 PDF 미완성 (under preparation) — modified SOR 알고리즘 식은 Botta-Ellenbroek(1985) 원논문 참조.
- SIP 의 $L,U,K$ 구체 7-대각 구성·보간 계수는 Stone(1968)/Ferziger-Perić(1999) 참조 (본 절은 원리 + iteration 식만).

## 5. 연결

- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3 SIP 적용 (action balance $A\vec{N}=\vec{b}$, penta-diagonal)
- [[swan-tech-ch4-5-bc-2d-setup]] — Ch 5 SOR 적용 (2D setup Poisson $Ax=f$)
