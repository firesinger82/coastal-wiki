---
title: "SWAN swantech Ch 3.17 Computation of breaking source term — Battjes-Janssen Newton 선형화 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.17 Computation of breaking source term, doc p.114-115 (Eq 3.93-3.106). Reference: Battjes-Janssen 1978."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.17 직접 read via pdftotext (식 번호 context-verified: D_tot 3.93·S_i 3.94·D̃ 3.95·B 3.96·Newton 3.97·∂S/∂E<0 3.98·deriv chain 3.99-101·Q_b 관계 3.102·Q'_b 3.103-104·∂S/∂E 3.105·final 3.106) + website_markdown node63.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +43 offset)."
note_author: "Claude Opus 4.8 (1M context) raw PDF direct read"
note_date: 2026-06-02
verification_by: "Claude Opus 4.8 (1M context) — Eq 3.93-3.106 verbatim, PDF 식 번호 context-검증"
verification_date: 2026-06-02
related:
  - models/SWAN/manual-notes/swan-tech-ch2-dissipation-detailed.md
  - models/SWAN/manual-notes/swan-tech-ch3-solution-iteration-limiter.md
  - models/SWAN/manual-notes/swan-tech-ch3-obstacles-spectral-ops.md
---

# swantech Ch 3.17 Breaking source term Newton 선형화 — verified verbatim

> swantech.pdf (v41.51) §3.17 직접 read. [[swan-tech-ch2-dissipation-detailed]] §6 의 **depth-induced breaking $S_{\text{ds,br}}$(Eq 2.64-2.68)을 수치적으로 안정하게 푸는 Newton 선형화**. [[swan-tech-ch3-solution-iteration-limiter]] §3.3 의 Newton-Raphson(Eq 3.18)의 구체화 — 양에너지 보존($E>0$) 보장.
>
> **식 번호 주의**: PDF 번호 사용 (online HTML +43 offset, 예: final HTML 3.149 = PDF 3.106).

## 1. Battjes-Janssen dissipation (Eq 3.93-3.96)

Surf breaking 총 소산 (BJ 1978, [[swan-tech-ch2-dissipation-detailed]] Eq 2.64):
$$D_{\text{tot}} = -\alpha_{\text{BJ}}Q_b\tilde{\sigma}\frac{H_{\max}^2}{8\pi} \quad \text{(3.93)}$$

Spectral bin $i$ source:
$$S_i = \frac{D_{\text{tot}}}{E_{\text{tot}}}E_i = \tilde{D}\,E_i \quad \text{(3.94)}$$

정규화 총소산:
$$\tilde{D} = -\frac{\alpha_{\text{BJ}}\tilde{\sigma}Q_b}{\pi\mathcal{B}} < 0 \quad \text{(3.95)}$$
$$\mathcal{B} = \frac{8E_{\text{tot}}}{H_{\max}^2} = \left(\frac{H_{\text{rms}}}{\gamma d}\right)^2 \quad \text{(3.96)}$$
> $\mathcal{B} \propto E$ (즉 $E_{\text{tot}}$ 에 비례) — source 가 $E$ 에 **강한 비선형** ($\tilde{D}$ 가 $\mathcal{B}$ 통해 $E$ 의존).

## 2. Newton 선형화 (Eq 3.97-3.101)

강한 비선형 → iteration level $n+1$ 에서 Newton:
$$S_i^{n+1} \approx \tilde{D}E_i^n + \left(\frac{\partial S}{\partial E}\right)_i^n(E_i^{n+1} - E_i^n) \quad \text{(3.97)}$$

> **SWAN 안정화 변형**: 우변 첫 항 $\tilde{D}E_i^n \to \tilde{D}E_i^{n+1}$ 로 교체 → **energy density $E$ 양수 보존** (조건 $\partial S/\partial E < 0$):
$$\frac{\partial S}{\partial E} < 0 \quad \text{(3.98)}$$

도함수 유도 ((3.94)에서):
$$\frac{\partial S}{\partial E}\Big|_i = \frac{\partial\tilde{D}}{\partial E}\Big|_i E_i + \tilde{D} \quad \text{(3.99)}$$
$\tilde{D}$ 는 $\mathcal{B}\propto E$ 함수:
$$\frac{\partial S}{\partial E}\Big|_i = \frac{\partial\tilde{D}}{\partial\mathcal{B}}\Big|_i\mathcal{B}_i + \tilde{D} \quad \text{(3.100)}$$
$Q_b$ 가 $\mathcal{B}$ 함수 (quotient rule):
$$\frac{\partial S}{\partial E}\Big|_i = -\frac{\alpha_{\text{BJ}}\tilde{\sigma}}{\pi}\frac{\partial Q_b}{\partial\mathcal{B}} \quad \text{(3.101)}$$

## 3. $Q_b$ 도함수 (Eq 3.102-3.104)

$Q_b$ 정의 관계 ([[swan-tech-ch2-dissipation-detailed]] Eq 2.65 의 형):
$$1 - Q_b + \mathcal{B}\ln Q_b = 0 \quad \text{(3.102)}$$
$\mathcal{B}$ 미분:
$$-Q_b' + \ln Q_b + \frac{\mathcal{B}}{Q_b}Q_b' = 0 \quad \text{(3.103)}$$
$$Q_b' = \frac{\ln Q_b}{1 - \mathcal{B}/Q_b} = \frac{Q_b}{\mathcal{B}}\frac{Q_b-1}{Q_b-\mathcal{B}} \quad \text{(3.104)}$$
> (3.102) 이용. $Q_b' > 0$ ($0<Q_b<1$, $\mathcal{B}>Q_b$).

## 4. 최종 (Eq 3.105-3.106)

(3.104)를 (3.101)에 대입:
$$\frac{\partial S}{\partial E}\Big|_i = \tilde{D}\,\frac{Q_b-1}{Q_b-\mathcal{B}}\Big|_i < 0 \quad \text{(3.105)}$$
> $\partial S/\partial E < 0$ 확인 (조건 3.98 만족) → 양에너지 보존.

최종 source term 근사:
$$S_i^{n+1} = \tilde{D}\left(1 + \frac{Q_b-1}{Q_b-\mathcal{B}}\right)_i^n E_i^{n+1} - \tilde{D}\,\frac{Q_b-1}{Q_b-\mathcal{B}}\Big|_i^n E_i^n \quad \text{(3.106)}$$
> 형태: $S_i^{n+1} = (S^p)_i + (S^n)_i E_i^{n+1}$ ([[swan-tech-ch3-solution-iteration-limiter]] Eq 3.17 의 $S_{\text{tot}}^p + S_{\text{tot}}^n N$ 선형화 형). $E_i^{n+1}$ 계수 = $a_P$ 의 $-S^n$ 기여 (diagonal dominance 강화 → 안정).

## 5. 의의

- BJ breaking 의 $E$-비선형성을 Newton 으로 선형화 + **첫 항 implicit 처리($E^{n+1}$)로 positivity 보장** — surf zone 안정 핵심.
- $\partial S/\partial E < 0$ 해석적 보장 (3.105) → iteration matrix diagonal dominance.
- [[swan-tech-ch3-solution-iteration-limiter]] §3.3 의 일반 Newton-Raphson(3.18)을 breaking 에 구체 적용한 것.

## 6. SWAN 옵션 매핑

| Tech (PDF §3.17) | User cmd | 비고 |
|---|---|---|
| 3.93-3.106 breaking 수치 | `BREAKING CONSTANT [alpha] [gamma]` | α_BJ=1, γ=0.73 (물리는 §2.3.3) |
| Newton 선형화 | (internal, 안정화) | positivity-preserving |

## 7. 한계

- $H_{\max} = \gamma d$, $\gamma$ 기본값·variable γ 옵션은 물리식 [[swan-tech-ch2-dissipation-detailed]] §6.1 참조.
- Thornton-Guza(2.69-74) 대안 breaking 의 Newton 형은 §3.17 미수록 (BJ만) — 별도.

## 8. 연결

- [[swan-tech-ch2-dissipation-detailed]] — §2.3.3 §6 depth-breaking 물리 (D_tot Eq 2.64, Q_b Eq 2.65-67)
- [[swan-tech-ch3-solution-iteration-limiter]] — §3.3 Newton-Raphson(Eq 3.18) + source 선형화(Eq 3.17)
- [[swan-tech-ch3-obstacles-spectral-ops]] — §3.12-3.16 (이전)
