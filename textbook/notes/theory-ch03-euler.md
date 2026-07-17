---
title: "이론 ch03 — Euler 방정식: 운동량 보존 · Cauchy 응력텐서 · 무점성 · Bernoulli · d'Alembert"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch01-conservation.md
  - textbook/notes/theory-ch02-continuity.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
claims_total: 23
claims_attached: 21
claims_dropped: 2
claims_source_needed: 0
claims_basis: legacy-ledger
has_source_needed: false
provenance: "교재 프로젝트 textbook-ai-data-full ch03(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **hudspeth2005-wave-forces §3.3(운동량·응력·대칭성·Euler) + water-wave-mechanics(D&D) §2(Bernoulli·Euler·d'Alembert)** — 본 노트가 **Cauchy 응력텐서·Euler·Bernoulli 의 canonical 소유자**(ch01 §4·ch02 의 Euler 언급은 선취 미리보기). ★삭제 전 전체 코퍼스 grep(T9 심화 교훈=정확 용어+개념 동의어): Torricelli = 0건 확정 삭제. Codex 게이트(T10) 정정: d'Alembert 앵커 'Eq.7.27'→'Eq.7.23·7.26 뒤 설명'·무점성 σ=-pI = Hudspeth p.91 Eq.3.38a 부착·4식→'속도(연속)·압력(운동량)' Hudspeth p.74 축소·★Prandtl 1904 경계층 = stewart p.134 실존 부착(연도 미지지 아님)·Cauchy traction 정확식 source-needed 토큰화. 미이식: 워크예제(호스·사이펀·Torricelli)·Bernoulli 효과 일상예. depends_on ch01(운동량 마스터·관성력)·ch02(연속 약분·비압축)·ch00.5(물질미분·발산·벡터항등식). T10([THEORY-LEDGER](../THEORY-LEDGER.md)). ★R1 I-3 코퍼스 확장(2026-07-17): kundu-cohen-2008(4판, 사용자 제공) 등록으로 source-needed 소진 — 테트라헤드론 traction(p.61)·Cauchy 운동방정식(p.122 Eq.4.15) 부착 — sn 1 해소."
verification_method: "hudspeth2005-wave-forces p.74·78-80·84-86·90-92·532(§3.3 운동량·§3.3.2 표면응력·대칭성·§3.3.5 Euler·Bernoulli·PST·d'Alembert) + water-wave-mechanics(D&D) p.22·44·50-51·231(Euler 전기·Euler 벡터형·Bernoulli·d'Alembert) + stewart-physical-ocean p.134(Prandtl 1904 경계층) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함). + kundu-cohen-2008 실측(2026-07-17): p.61·122 마커 실측."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch01-conservation.md
  - textbook/notes/theory-ch02-continuity.md
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch00_5-math-tools.md
---

# Euler 방정식 — 운동량 보존 · Cauchy 응력 · 무점성 · Bernoulli

> 4-레이어 **① 이론** 노트. [[theory-ch01-conservation]] 의 마스터에 강도량 $\phi=\rho\mathbf{u}$(운동량)를 대입 → Cauchy 운동량 방정식 → 무점성 가정 → Euler → Bernoulli(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 선형파 퍼텐셜 유동·Bernoulli 응용 [[theory-ch08-linear-waves]].

## 1. 운동량 원리와 표면·체적력

- 미분 검사체적의 **운동량 원리**: 단위체적당 힘은 **체적력 $F_B$ + 표면응력 구배 $F_S$** — 표면응력은 다시 **수직(normal) $F_N$ + 접선(tangential) $F_T$** 으로 분해 (hudspeth2005-wave-forces, p.78, §3.3, Eq. 3.12-3.13). 운동량 마스터 형태·관성력=국소+대류가속은 [[theory-ch01-conservation]] §5 canonical.
- 운동량은 벡터라 플럭스가 **2차 텐서**(운동량 플럭스 $\rho u_i u_j$) — 표면응력의 부피 기여는 발산정리로 $\int_V\nabla\cdot\boldsymbol\sigma\,dV$([[theory-ch00_5-math-tools]] §5 근거).

## 2. Cauchy 응력텐서 — 정의와 대칭성

- 표면응력 성분 $\sigma_{ij}$: **첫 첨자=면의 법선축, 둘째=응력 방향** — 미소 체적 면의 수직·접선 응력을 Taylor 급수로 표현 (hudspeth2005-wave-forces, p.84, §3.3.2, Fig. 3.7; Taylor 근거 [[theory-ch00_5-math-tools]] §2). 3면×3방향 = 9 성분.
- **대칭성 $\sigma_{ij}=\sigma_{ji}$**: 미분 체적의 **각운동량 balance**(모멘트 합 = 각운동량, $\sum M_A=\rho\Delta V(\Delta R)^2\ddot\theta$)에서, 체적이 0으로 가면 대각 외 응력이 짝지어 상쇄되어야 함 → $\sigma_{zx}=\tau_{xz}$ 등 → **9 성분이 6 독립 성분으로 축약** (hudspeth2005-wave-forces, p.84-86, Eq. 3.26). **임의 면의 응력은 응력텐서에서 결정**: 테트라헤드론 요소의 힘 balance 로 임의 방향 면의 응력이 $\tau_{ij}$(좌표 변환 Eq. 2.12)로 정해짐 (kundu-cohen-2008, p.61, §2.7; Sommerfeld 1964 참조 표기) — 이를 미소 요소에 적용한 **Cauchy 운동방정식** $\rho\,Du_i/Dt=\rho g_i+\partial\tau_{ij}/\partial x_j$ (p.122, Eq. 4.15; R1 코퍼스 확장으로 승격).

## 3. Cauchy 운동량 방정식 → 무점성 Euler

- 종합하면 **비보존형 운동량 방정식** $\rho\dfrac{D\mathbf{u}}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\mathbf{f}$ — 좌변=단위체적 질량×가속도(물질미분, [[theory-ch01-conservation]] §5 관성력 canonical), 우변=표면응력 발산+체적력, 곧 연속체판 $F=ma$ (hudspeth2005-wave-forces, p.78-80, §3.3; [[theory-ch02-continuity]] 연속식으로 $u_i$ 곱 항 약분). 어떤 **구성식(응력↔변형)** 을 넣느냐가 물질을 결정 — 무점성→Euler, Newtonian→N-S(ch04).
- **무점성(inviscid) 가정**: 전단응력 0, 응력텐서는 등방 압력뿐 $\boldsymbol\sigma=-p\mathbf{I}$ → $\nabla\cdot\boldsymbol\sigma=-\nabla p$ (hudspeth2005-wave-forces, p.91, Eq. 3.38a; Kronecker δ 치환 [[theory-ch00_5-math-tools]] §4). 대입 →
- **Euler 방정식** $\rho\dfrac{D\mathbf{u}}{Dt}=-\nabla p+\rho\mathbf{f}$, 즉 $\dfrac{D\mathbf{q}}{Dt}=-\nabla\!\left(\dfrac{p}{\rho}+gz\right)$ — 자유표면 중력파의 비회전 무점성 유동 근사 (hudspeth2005-wave-forces, p.91, §3.3.5, Eq. 3.41, Lamb 1932; water-wave-mechanics, p.44, Euler 벡터형). **Euler + 연속 = 닫힌 계** — 비압축 유체는 속도(연속식)·압력(운동량식) 두 미지장으로 환원 (hudspeth2005-wave-forces, p.74).

## 4. Bernoulli 적분

- **가정**: 무점성·비회전($\nabla\times\mathbf{u}=0$, 속도 퍼텐셜 $\phi$ 존재)·보존력. Euler 를 **유선(streamline)을 따라 적분**하면 Bernoulli (hudspeth2005-wave-forces, p.91, §3.3.5).
- **비정상형**: $-\dfrac{\partial\phi}{\partial t}+\dfrac{1}{2}(u^2+w^2)+\dfrac{p}{\rho}+gz=C(t)$ — **Bernoulli 상수 $Q(t)$ 는 시간만의 함수**(공간 적분 결과) (hudspeth2005-wave-forces, p.92, Eq. 3.45, Eagleson & Dean 1966; water-wave-mechanics, p.50-51, Eq. 2.92·2.93 velocity potential 형). 정상·비압축이면 $\dfrac{1}{2}|\mathbf{u}|^2+\dfrac{p}{\rho}+gz=\text{const}$.
- **에너지 해석**: 세 항 = 운동/압력/위치 에너지(단위질량당) — 유선 따라 합이 일정(속도↑→압력↓). 대안 유도: 운동량식과 속도의 내적으로 얻는 **역학 에너지 원리** (hudspeth2005-wave-forces, p.91-92, §3.4, Eq. 3.42; Landau & Lifshitz 1987, Phillips 1977). ※원문 교재의 Bernoulli 효과 일상예(비행기 양력·스프레이)·워크예제(호스·사이펀·Torricelli $\sqrt{2gh}$)는 미이식(Torricelli 코퍼스 0건).

## 5. d'Alembert 역설 — 무점성의 한계

- **역설**: 이상(무점성·비회전) 유체에서 매끄러운 물체(원기둥·파일) 주위 흐름은 **압력 대칭 때문에 알짜 항력 = 0** — 실제 유동의 저항과 모순 (water-wave-mechanics, p.231; hudspeth2005-wave-forces, p.532, Eq. 7.23·7.26 뒤 설명, "d'Alembert's paradox", Milne-Thompson 1968).
- 이것이 **점성(ch04 N-S)의 필요성**을 보이는 동기 — 아무리 작은 점성도 경계 근처에서 박리·와류를 만들어 항력의 원천이 됨. **Prandtl 이 1904 논문에서 경계층(boundary layer) 개념 도입** (stewart-physical-ocean, p.134, Anderson 2005) — 상세는 ch06 로 이연.

## 6. 연결

- [[theory-ch01-conservation]] — 운동량 마스터·관성력 분해 (근거 의존)
- [[theory-ch02-continuity]] — 연속식(비보존형 약분·비압축) (근거 의존)
- [[theory-ch00_5-math-tools]] — 물질미분·발산·벡터 항등식 (근거 의존)
- [[theory-ch08-linear-waves]] — 퍼텐셜 유동·Bernoulli 응용 (탐색)
- 다음: ch04 N-S(응력텐서에 Newtonian 구성식)·ch06 경계층(d'Alembert 해결).
