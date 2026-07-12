---
title: "이론 ch09 — Stokes 비선형 · 쇄파 한계 · 불규칙파 스펙트럼·통계"
topic: waves
layer: 1
depends_on:
  - textbook/notes/theory-ch08-linear-waves.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch09(AI 합성 MDX, 무인용) 이식분 — 2026-07-12 원자 단언 분해·(source_id, page) 부착. ★원문 연도 오기 1건 정정(Hasselmann 4파 상호작용 1957→1962), 미매칭 삭제 4건(Beaufort별 경사 표·'19세기 Sverdrup-Munk-Bretschneider' 시대 오류·Jeffreys 1932 sheltering·Draupner 수치/freak 임계 2.2Hs). 게이트 ⓒ ④: Stokes 2차 수면형 앵커 p.302(속도·수송 문맥)→p.318-319(Eq. 11.29·11.32·11.33) 정밀화 + α 계수 정의 명시. T3([THEORY-LEDGER](../THEORY-LEDGER.md)), 게이트 ⓒ MODIFY 반영 완료."
verification_method: "water-wave-mechanics(D&D) p.13·128-129·186·285·318-319·351 + holthuijsen2007 p.5·42·52·74·79·101·103·163·178·203·207·260 — textbook/md 미러 페이지 직접 대조 (2026-07-12, 게이트 ⓒ 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-12
related:
  - textbook/notes/theory-ch08-linear-waves.md
  - concepts/waves/02-theory.md
  - concepts/waves/wave-breaking-cross-model.md
---

# Stokes 비선형 · 쇄파 한계 · 불규칙파 스펙트럼

> 4-레이어 **① 이론** 노트. [[theory-ch08-linear-waves]] 의 두 한계(소진폭·단일 사인)를 확장(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 쇄파의 모델별 구현 [[wave-breaking-cross-model]] · 도메인 요약 `concepts/waves/`.

## 1. Stokes 비선형 보정

- 파 경사 $\epsilon = ka$ 를 소매개변수로 한 섭동 전개 — 수렴성은 전개의 성립 조건이며 2차 이론에서 점검 가능 (water-wave-mechanics, p.319).
- **2차 수면형**: $\eta = a\cos(kx-\sigma t) + a^2k\,\alpha\cos 2(kx-\sigma t)$, 계수 $\alpha = \dfrac{\cosh kh\,(2+\cosh 2kh)}{4\sinh^3 kh}$ — 2배 주파수 성분이 더해져 **마루 첨예·골 평탄**의 비대칭 파형 (water-wave-mechanics, p.318, Eq. 11.29 $\eta_2$·Eq. 11.32 합성 $\eta=\epsilon\eta_1+\epsilon^2\eta_2$; 차원형 $H$ 표기는 p.319 상단). **분산관계는 2차에서 불변** $\sigma^2=gk\tanh kh$ — 보정은 3차부터 (p.319, Eq. 11.33).
- **Stokes drift(질량 수송)**: 선형 궤도는 닫히지만 2차에서 순 평균 이동 발생 — mass transport 로 다룸 (water-wave-mechanics, ch.10 §10.2 Mass Transport, p.285; 실험 맥락 p.186).

## 2. 쇄파 한계와 쇄파 유형

- **깊은물 경사 한계**: $H/L_0 = 0.142$ (Eq. 12.12; 비선형 효과 포함 시 $L_0 = 1.2\,gT^2/2\pi$ 보정 병기) (water-wave-mechanics, p.351). 심해 관측은 경사 ~0.14 부근 쇄파와 정합 (holthuijsen2007, p.207).
- **얕은물 수심 한계**: $H_b/h_b = 0.78$ — Weggel(1972)이 실험 재해석으로 경사 의존성을 제시 (water-wave-mechanics, p.129).
- **쇄파 유형 판별은 Iribarren 수 ξ**: spilling / plunging(0.5<ξ∞<3.3) / collapsing·surging(ξ∞>3.3) — Battjes(1974) 정리 (holthuijsen2007, p.260). plunging 은 가파른 해빈에서 발생 (water-wave-mechanics, p.128-129).
- 쇄파 = 지배적 에너지 소산 경로(천해 §9.3.4 축) (holthuijsen2007, p.207) — 모델별 소산 정식화는 [[wave-breaking-cross-model]](탐색).

## 3. 불규칙파 — 스펙트럼 기술

- 실해면은 다수 성분의 중첩 — **분산밀도 스펙트럼(variance density spectrum)** 이 수면 변위 분산의 주파수 분포를 기술 (holthuijsen2007, p.42; 정의·해석 §3.5).
- 스펙트럼 모멘트 $m_n = \int f^n S(f)df$ — $m_0$=분산, $m_2$ 와 함께 **zero-crossing 주기 $T_{m02}=\sqrt{m_0/m_2}$** (holthuijsen2007, p.79, Eq. 4.2.2 문맥; zero-crossing 정의 p.44).
- **유의파고**: $H_{m0} = 4\sqrt{m_0}$ — 시계열 직접 추정 $H_{1/3}$ 보다 **통상 5-10% 큼**(두 정의의 실측 괴리까지 출처 명시) (holthuijsen2007, p.74). ※원문 교재의 "19세기 Sverdrup-Munk-Bretschneider 정의" 는 시대 오류(해당 계보는 20세기 중반) — 미매칭 삭제.
- **Pierson-Moskowitz(완전발달)**: $f^{-5}$ 꼬리의 경험 스펙트럼 (holthuijsen2007, p.163). **JONSWAP**: PM 에 peak-enhancement $G(f)=\gamma^{\exp[\ldots]}$ 를 곱한 fetch 제한 스펙트럼 (Eq. 6.3.14, holthuijsen2007, p.178; JONSWAP 프로젝트의 의의 p.5).

## 4. 개별 파고 통계

- 협대역 가정에서 진폭/파고는 **Rayleigh 분포** (holthuijsen2007, p.52).
- **장기(파랑 기후) 통계**: 전 관측 사용(initial-distribution)·폭풍 피크(peak-over-threshold) 접근으로 **return period** 추정 — 설계 파고의 근거 (holthuijsen2007, p.103, §4.3). 천해 개별 파고는 Rayleigh 에서 벗어나 Weibull 형 보정(Fig 4.12) (holthuijsen2007, p.91).
- **Freak(rogue) wave**: 관측 빈도가 선형 통계 기대를 초과하는 극단파 — "기원은 여전히 미해결"(Note 4E) (holthuijsen2007, p.101). ※원문 교재의 Draupner 수치·임계 2.2Hs 는 코퍼스 미확인 — 미이식.

## 5. 역사 연표 (코퍼스 실측분)

Stokes 고차 이론 1847 · Michell 한계 1893 · McCowan 한계 1894 (water-wave-mechanics, p.13 verbatim 연표) → **Hasselmann 4파(quadruplet) 상호작용 1962** — Boltzmann 적분 정식화 (holthuijsen2007, p.203; ★원문 교재의 "1957" 은 오기, 출처 기준 정정) → Pierson-Moskowitz 1964 (p.163) → JONSWAP 1973 (p.5·178).

## 6. 연결

- [[theory-ch08-linear-waves]] — 선형해·에너지 기초 (근거 의존)
- [[wave-breaking-cross-model]] · `concepts/waves/` — 모델 구현·도메인 (탐색)
- 다음: ch10 해안 변형(shoaling·refraction) — 본 장의 스펙트럼·H_s 가 입력 변수.
