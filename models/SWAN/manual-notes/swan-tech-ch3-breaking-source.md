---
title: "SWAN swantech Ch 3.17 Computation of breaking source term — Battjes-Janssen Newton 선형화 verified verbatim"
topic: swan
canonical_source: external
external_source: "swantech.pdf (SWAN Cycle III version 41.51) §3.17 Computation of breaking source term, doc p.114-115 (Eq 3.93-3.106). Reference: Battjes-Janssen 1978."
citation_status: verified
verification_method: "swantech.pdf (v41.51) §3.17 직접 read via pdftotext (식 번호 context-verified: D_tot 3.93·S_i 3.94·D̃ 3.95·B 3.96·Newton 3.97·∂S/∂E<0 3.98·deriv chain 3.99-101·Q_b 관계 3.102·Q'_b 3.103-104·∂S/∂E 3.105·final 3.106) + website_markdown node63.md LaTeX alt-text. 식 번호는 PDF 번호 (online HTML +43 offset).; 2026-10-13 recovery 대조 보고서 R1–R8 반영"
last_source_check: "2026-10-13 (recovery 대조 반영)"
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

> swantech.pdf (v41.51) §3.17의 쇄파항 선형화이다. 문서의 양성 보존 설명은 쇄파항 선형화와 $\partial S/\partial E<0$ 조건에 관한 것이다. 전체 SWAN 해의 엄격한 $E>0$ 보장으로 확장하지 않는다. (swantech PDF 123쪽 / 인쇄 115쪽, 식 (3.98), 원문 `This preserves positivity of energy density E`; R2:SS-719)
>
> **식 번호 주의**: PDF 번호 사용 (online HTML +43 offset, 예: final HTML 3.149 = PDF 3.106).

## 1. Battjes-Janssen dissipation (Eq 3.93-3.96)

Surf breaking 총 소산 (BJ 1978, [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) Eq 2.64):
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

$Q_b$ 정의 관계 ([swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) Eq 2.65 의 형):
$$1 - Q_b + \mathcal{B}\ln Q_b = 0 \quad \text{(3.102)}$$
$\mathcal{B}$ 미분:
$$-Q_b' + \ln Q_b + \frac{\mathcal{B}}{Q_b}Q_b' = 0 \quad \text{(3.103)}$$
$$Q_b' = \frac{\ln Q_b}{1 - \mathcal{B}/Q_b} = \frac{Q_b}{\mathcal{B}}\frac{Q_b-1}{Q_b-\mathcal{B}} \quad \text{(3.104)}$$
> (3.102) 이용. $Q_b' > 0$ ($0<Q_b<1$, $\mathcal{B}>Q_b$).

## 4. 최종 (Eq 3.105-3.106)

(3.104)를 (3.101)에 대입:
$$\frac{\partial S}{\partial E}\Big|_i = \tilde{D}\,\frac{Q_b-1}{Q_b-\mathcal{B}}\Big|_i < 0 \quad \text{(3.105)}$$
> 문서의 양성 보존 설명은 쇄파항 선형화와 $\partial S/\partial E<0$ 조건에 관한 것이다. (swantech PDF 123쪽 / 인쇄 115쪽, 식 (3.98)·(3.105); R2:SS-719)

BJ의 포화 처리는 `REAL(BB) .GT. 0. .AND. REAL(ABS(BB - DBLE(QB))) .GT. 0.`을 만족하고 `BB .LT. 1D0`이 거짓일 때 적용한다. 이 분기에서 BJ의 상대 소산을 $\alpha_{BJ}\widetilde\sigma/\pi$로 포화시킨다. `BB=QB=1`이면 `SURFA0`과 `SURFA1`을 0으로 둔다. 강한 쇄파 구간에서 인쇄식의 단순 연장을 사용하지 않는다. (`src/swancom2.ftn:2110–2112`의 조건; `src/swancom2.ftn:2117` `WS = ( DBLE(PSURF(1)) / DBLE(PI)) * DBLE(FMEAN)`; `src/swancom2.ftn:2118` `SbrD = 0D0`; `src/swancom2.ftn:2122–2124`의 0 대입; R2:SS-511·SS-719) [10-13 전수 검증 정정]

최종 source term 근사:
$$S_i^{n+1} = \tilde{D}\left(1 + \frac{Q_b-1}{Q_b-\mathcal{B}}\right)_i^n E_i^{n+1} - \tilde{D}\,\frac{Q_b-1}{Q_b-\mathcal{B}}\Big|_i^n E_i^n \quad \text{(3.106)}$$
> 형태: $S_i^{n+1} = (S^p)_i + (S^n)_i E_i^{n+1}$ ([swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) Eq 3.17 의 $S_{\text{tot}}^p + S_{\text{tot}}^n N$ 선형화 형). $E_i^{n+1}$ 계수 = $a_P$ 의 $-S^n$ 기여 (diagonal dominance 강화 → 안정).

## 5. 의의

- 문서의 양성 보존 설명은 쇄파항 선형화와 $\partial S/\partial E<0$ 조건에 관한 것이다. (swantech PDF 123쪽 / 인쇄 115쪽, 식 (3.98); R2:SS-719)
- $\partial S/\partial E < 0$ 해석적 보장 (3.105) → iteration matrix diagonal dominance.
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) §3.3 의 일반 Newton-Raphson(3.18)을 breaking 에 구체 적용한 것.

## 6. SWAN 옵션 매핑

| Tech (PDF §3.17) | User cmd | 비고 |
|---|---|---|
| 3.93-3.106 breaking 수치 | `BREAKING CONSTANT [alpha] [gamma]` | α_BJ=1, γ=0.73 (물리는 §2.3.3) |
| Newton 선형화 | (internal, 안정화) | positivity-preserving |

## 7. 한계

- $H_{\max} = \gamma d$, $\gamma$ 기본값·variable γ 옵션은 물리식 [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) §6.1 참조.
- Thornton-Guza(2.69-74) 대안 breaking 의 Newton 형은 §3.17 미수록 (BJ만) — 별도.

## 8. 연결

- [swan-tech-ch2-dissipation-detailed](swan-tech-ch2-dissipation-detailed.md) — §2.3.3 §6 depth-breaking 물리 (D_tot Eq 2.64, Q_b Eq 2.65-67)
- [swan-tech-ch3-solution-iteration-limiter](swan-tech-ch3-solution-iteration-limiter.md) — §3.3 Newton-Raphson(Eq 3.18) + source 선형화(Eq 3.17)
- [swan-tech-ch3-obstacles-spectral-ops](swan-tech-ch3-obstacles-spectral-ops.md) — §3.12-3.16 (이전)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md#5-차이-결론).

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-511 | BJ 상대 소산의 포화 분기와 선행 조건 | swantech PDF 123쪽 / 인쇄 115쪽, (3.96) $\mathcal B=8E_{tot}/H_{max}^2=(H_{rms}/\gamma d)^2$. | `src/swancom2.ftn:2117` `WS = ( DBLE(PSURF(1)) / DBLE(PI)) * DBLE(FMEAN)`<br>`src/swancom2.ftn:2118` `SbrD = 0D0`<br>`src/swancom2.ftn:2110–2112`의 선행 조건<br>`src/swancom2.ftn:2122–2124`의 `SURFA0 = 0D0`과 `SURFA1 = 0D0` | C | 해석: 강한 쇄파 구간에서 인쇄식의 단순 연장을 사용하지 않는다. BJ의 포화 처리는 `REAL(BB) .GT. 0. .AND. REAL(ABS(BB - DBLE(QB))) .GT. 0.`을 만족하고 `BB .LT. 1D0`이 거짓일 때 적용한다. `BB=QB=1`이면 `SURFA0`과 `SURFA1`을 0으로 둔다. [10-13 전수 검증 정정] |
| R2:SS-719 | 노트 · manual-notes/swan-tech-ch3-breaking-source.md:20 | swantech PDF 123쪽 / 인쇄 115쪽, (3.98): $\partial S/\partial E<0$. 원문 `This preserves positivity of energy density E`. | `src/swancom2.ftn:2115` `SbrD = WS * (1D0 - DBLE(QB)) / (BB - DBLE(QB))`<br>`src/swancom2.ftn:2117` `WS = ( DBLE(PSURF(1)) / DBLE(PI)) * DBLE(FMEAN)`<br>`src/swancom2.ftn:2118` `SbrD = 0D0` | C | 해석: 문서의 양성 보존 설명은 쇄파항 선형화와 $\partial S/\partial E<0$ 조건에 관한 것이다. 전체 SWAN 해의 엄격한 $E>0$ 보장으로 확장하지 않는다. $BB\ge1$에서의 별도 계산도 적는다. |
| R2:SS-539 | 원천항 적분 전·후 스펙트럼 총량 처리 | — | `src/swancom1.ftn:5801`의 `SIGPOW(:,2)` 적분; `src/swancom1.ftn:5807`의 꼬리 추가; `src/swancom1.ftn:5811` `EMAX = 0.25 * ( PSURF(2) * DEP2(KCGRD(1)) )**2`; `src/swancom1.ftn:5815–5817` `IF (ACUPDA .AND. ETOT .GT. EMAX .AND. ISURF .GE. 1 .AND. IQCM .EQ. 0) THEN`; `src/swancom1.ftn:5815–5817` `AC2(:,:,KCGRD(1)) = MAX(0.,(EMAX/ETOT)*AC2(:,:,KCGRD(1)))`. | C 문서 누락 | 해석: $d\sigma=\sigma\,d\log\sigma$와 $E=N\sigma$ 때문에 적분에서 $\sigma^2$가 나온다. `ACUPDA`가 참이고 쇄파가 켜져 있으며 `IQCM=0`일 때 상한을 넘는 스펙트럼을 같은 비율로 줄인다. 에너지 상한의 쇄파지수는 고정 배열값 `PSURF(2)`이다. 이 처리는 (3.106)의 source 선형화와 별도이다. C는 swantech 3.17의 쇄파항 선형화 설명에 이 별도 총량 제한이 없는 점이다. 실행 조건과 음수 제거는 인용한 코드 그대로 적용된다. [10-13 결론 검증 보완] [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md#5-차이-결론) |
