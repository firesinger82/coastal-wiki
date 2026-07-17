---
title: "이론 ch02 — 연속방정식: 질량보존 · 보존/비보존 형태 · incompressible 조건"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch01-conservation.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
claims_total: 25
claims_attached: 22
claims_dropped: 2
claims_source_needed: 1
claims_basis: legacy-ledger
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch02(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(T9) MODIFY 반영. 주 출처 = **water-wave-mechanics(D&D) §2.2 + hudspeth2005-wave-forces §3.2 + stewart-physical-ocean §7**. ★주 출처 정정: 원장 후보 hydraulics-and-hydrology 미러(801443089)는 실제로 **USACE LACPR Hydraulics & Hydrology Appendix**(surge/wave modeling·JPM-OS·levee)라 기초 유체역학 교재 아님. Codex 게이트 정정(★전 코퍼스 grep도 정확 용어만 검색해 개념표현 누락): 저마하 물리근거 = stewart p.125-126 Boussinesq 실존('0건' 오판)·1D 도관 = D&D p.158 Eq.5.34a 속도×단면적 연속조건 실존(복원)·Euler 역사 = D&D p.22 '1761 Principia motus fluidorum'+stewart p.125 압축성 연속식 귀속(원문 '1755' 오기→1761 정정)·약한 비압축 성층 = stewart p.126 Boussinesq 부착·압력 = Hudspeth p.74 범위(속도 질량식·압력 운동량/에너지식)로 축소, Lagrange승수/Poisson 은 ch04 이연(source-needed). 미이식: Mach 수치기준 0.3·venturi·Navier 1822·워크예제. depends_on ch01·ch00.5. T9([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "water-wave-mechanics(D&D) p.22·25-26·38-39·44·158(§2.2 연속·압축률·incompressible·§2.3.4 발산·Euler·Euler 전기·step 연속조건) + hudspeth2005-wave-forces p.74·77-78(§3.2 연속 3형태·PST 속도/압력) + stewart-physical-ocean p.125-126(§7 Euler 압축성 연속식·Boussinesq) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch01-conservation.md
  - textbook/notes/theory-ch00_5-math-tools.md
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/theory-ch12-tides.md
---

# 연속방정식 — 질량보존 · 보존/비보존 · incompressible 조건

> 4-레이어 **① 이론** 노트. [[theory-ch01-conservation]] 의 마스터 balance 에 강도량 $\mu=\rho$(질량밀도)·$S=0$ 을 대입한 결과(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 선형파 이론의 비압축·비회전 가정 [[theory-ch08-linear-waves]].

## 1. 질량 보존 — 보존형·비보존형·텐서형

- 마스터 balance 에 $\mu=\rho$, $S=0$ 대입 → **연속방정식(보존형)** $\dfrac{\partial\rho}{\partial t}+\nabla\cdot(\rho\mathbf{u})=0$ (water-wave-mechanics, p.25, Eq. 2.10 "conservation of mass equation"; hudspeth2005-wave-forces, p.78, Eq. 3.10a). "한 점의 밀도 변화 = 그 점에서 알짜 빠져나가는 질량 플럭스".
- **비보존형** $\dfrac{D\rho}{Dt}+\rho\nabla\cdot\mathbf{q}=0$ — 물질미분으로 표현(곱규칙 전개; 물질미분 정의는 [[theory-ch00_5-math-tools]] §7 canonical) (hudspeth2005-wave-forces, p.78, Eq. 3.10b; water-wave-mechanics, p.39: $\tfrac{1}{\rho}\tfrac{D\rho}{Dt}$ 형). **텐서형** $\partial_t\rho+u_j\partial_j\rho+\rho\partial_j u_j=0$ 병기 (hudspeth2005-wave-forces, p.78, Eq. 3.10c).
- 세 형태는 수학적으로 등가 — **순수 운동학적 원리**(속도장·밀도장만 관여). 본 §1 이 연속식 3형태의 canonical(상세 소유자); 작은 검사체적 6면 직접 유도는 비례성상 생략하고 differential control volume 방법론만 [[theory-ch01-conservation]] §1 참조. ※"conservative/non-conservative" 명명은 코퍼스 미확인.
- **역사**: 연속·Euler 방정식의 현대적 정식화는 **Leonhard Euler(1707-1783)** — 1761 monograph *"Principia motus fluidorum"* 에서 제시 (water-wave-mechanics, p.22); 압축성 연속식의 최초 유도자로도 귀속 (stewart-physical-ocean, p.125, Eq. 7.17). ★원문 교재의 "1755" 는 오기 — 출처 기준 **1761** 로 정정.

## 2. Incompressible 가정 — 정량 근거

- 물은 압축률이 매우 작음: 체적탄성계수 $E=2.07\times10^9\ \mathrm{N\,m^{-2}}$ — $1\times10^6\ \mathrm{N\,m^{-2}}$(1 MPa) 압력 증가에 밀도 변화 **0.05%** 에 불과 → "henceforth water is incompressible" (water-wave-mechanics, p.26, Eq. 2.12 문맥).
- **저마하 물리 근거(Boussinesq)**: 비압축 근사는 (1) 유속이 음속 $c$ 보다 충분히 작고 (2) 파·교란의 위상속도가 $c$ 보다 작으며 (3) 연직 규모가 $c^2/g$ 보다 작을 때 성립 — 해양 유동은 이를 만족(음파 제외) (stewart-physical-ocean, p.125-126, Boussinesq 근사). ※원문 교재의 수치 기준 $\mathrm{Ma}<0.3$ 자체는 코퍼스 미확인 — 미이식(물리 근거는 위 3조건으로 부착).
- **비압축 조건 $\nabla\cdot\mathbf{u}=0$**: 비압축 유체는 $\tfrac{1}{\rho}\tfrac{D\rho}{Dt}=0$ 이므로 연속 비보존형에서 속도 발산이 0 → **divergenceless(nondivergent) flow** (water-wave-mechanics, p.26 Eq. 2.13·p.39, §2.3.4). 모든 위치에서 성립.
- 물리 의미: 한 방향 유량 변화가 있으면 다른 방향에 상쇄 유량 변화가 있어 **큐브 내 유체 축적 없음** (water-wave-mechanics, p.26, Fig. 2.1). 예: 2D corner 가속류 $u=-Axt,\ w=Azt$ → $\nabla\cdot\mathbf{u}=-At+At=0$ 비압축 (water-wave-mechanics, p.26, Example 2.1).
- **연안 응용 — 단면 변화 연속조건**: 폭적분(width-integrated) 연속식에서, 수심이 급변하는 step 을 지날 때 두 영역의 질량유량이 같아야 함 → **수평 입자속도 × 단면적**의 연속조건(균질 유체에서는 체적유량 매칭) (water-wave-mechanics, p.158, Eq. 5.34a·5.44; 파 반사·투과 경계조건 문맥). 이것이 1D 도관 $A\cdot u=\text{const}$ 의 연안공학 대응.

## 3. 두 가지 "비압축" 의미

- **강한 의미**: 밀도가 시공간 모두 상수 $\rho=\rho_0$ (water-wave-mechanics, p.26, "water is incompressible" 가정).
- **약한 의미**: 입자 따라간 밀도 일정 $D\rho/Dt=0$ — 공간적으로는 다를 수 있음. 둘 다 연속 비보존형에서 $\nabla\cdot\mathbf{u}=0$ 로 귀결 (water-wave-mechanics, p.39). **Boussinesq 근사**가 대표: 해양 밀도는 거의 일정하나 압력 계산의 $g$ 곱 항에서만 밀도 변화를 유지 — 성층(stratification) 하에서도 유동을 비압축으로 취급 (stewart-physical-ocean, p.126, Boussinesq 1842-1929). ※원문 교재의 명시적 "정의 A/정의 B" 이분 표기는 D&D·Stewart 서술로 대체.

## 4. 응용 — 비회전·압력의 역할

- **무점성+비압축 → Euler**: inviscid·incompressible 유체는 수직응력(압력)만 작용, 전단응력 0 이라 유체 입자에 회전을 줄 응력이 없음 → 비회전 입자는 비회전 유지(초기 와도는 보존) (water-wave-mechanics, p.44, §2.3 Euler 벡터형). 선형파 이론의 퍼텐셜 유동 전제 → [[theory-ch08-linear-waves]].
- **압력의 역할**: 비압축 유체의 근본 문제는 **속도(벡터)·압력(스칼라) 두 미지장**을 구하는 것으로 환원 — 표준 풀이는 **속도를 연속(질량)식에서, 압력을 운동량(또는 에너지) 원리에서** 구함 (hudspeth2005-wave-forces, p.74). 비회전 이상유체에서는 단일 속도 퍼텐셜 $\phi$ 로 더 축약 (p.74) → [[theory-ch08-linear-waves]]. ※압력을 $\nabla\cdot\mathbf{u}=0$ 제약의 Lagrange 승수로 보는 해석·Poisson 방정식 $\nabla^2 p=\ldots$ 전개는 코퍼스 직접 지지 없음 — ch04 N-S 로 이연. <!-- citation_status: source-needed -->

## 5. 연결

- [[theory-ch01-conservation]] — 마스터 balance(μ=ρ 대입 원천, 근거 의존)
- [[theory-ch00_5-math-tools]] — 물질미분·발산 (근거 의존)
- [[theory-ch08-linear-waves]] — 비압축·비회전 퍼텐셜 유동 응용 (탐색)
- 다음: ch03 Euler(마스터에 $\phi=\rho\mathbf{u}$+무점성)·ch04 N-S(+Newtonian 응력) — 연속은 이후 모든 장의 제약조건.
