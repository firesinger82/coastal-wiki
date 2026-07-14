---
title: "이론 ch04 — Navier-Stokes: 변형률 텐서 · Newtonian 구성식 · Stokes 법칙 · Reynolds 수 · Poiseuille"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
provenance: "교재 프로젝트 textbook-ai-data-full ch04(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(T11) MODIFY 반영. 주 출처 = **hudspeth2005-wave-forces §3.3.3-4·§3.6 + water-wave-mechanics(D&D) + stewart §8.3 + MST**. ★삭제 판정: Millennium/Clay N-S 문제 = stewart 오탐(기상학회 서지·점토광물) 삭제 적정. Codex 게이트 정정(★개념 동의어 grep도 놓침): second viscosity = Hudspeth p.86 실존('Stokes hypothesis 1845'·negative-definite 논쟁, Lamb1932·Schlichting1979 — 'bulk viscosity 0건' 오판)·Poiseuille = MST p.828 Eq.17.4 Q=πR⁴ΔP/(8μL)(포물선 아닌 Hagen-Poiseuille R⁴, 실존근거 놓침)·Re 임계 2300→**2000**(stewart p.130)·상사 3종 p.101→**p.102**·Strouhal b/(UT_s)·Froude Fr²·Re 단독 상사 과장 완화·RANS = stewart §8.3 Reynolds 응력 ρ⟨u'u'⟩ 앵커로 축소('RANS 필수·k-ε' 무앵커 제거)·변형률식 ch00.5 §6 canonical 링크 소비·λ=-2μ/3 등가환산 명시. depends_on ch03·ch00.5. T11([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "hudspeth2005-wave-forces p.82-83·86-90·102(§3.3.3 Newtonian·Stokes hypothesis·second viscosity·§3.3.4 N-S Eq.3.36·§3.6 상사·Table 3.2) + water-wave-mechanics(D&D) p.280(no-slip) + mechanics-of-sediment-transport p.828(Hagen-Poiseuille Eq.17.4) + stewart-physical-ocean p.130·132-133·136(Re≈2000·Reynolds 응력·eddy viscosity) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch03-euler.md
  - textbook/notes/theory-ch00_5-math-tools.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
  - textbook/notes/theory-ch13-sediment-transport.md
---

# Navier-Stokes — 변형률 텐서 · Newtonian 구성식 · Reynolds 수

> 4-레이어 **① 이론** 노트. [[theory-ch03-euler]] 의 Cauchy 운동량 방정식에 **점성(Newtonian 구성식)** 을 넣어 완전한 운동량 보존을 얻음 — Euler(무점성)의 확장(근거 의존 ①→①).
> 탐색 링크(근거 의존 아님): 난류·비선형 스펙트럼 [[theory-ch09-nonlinear-spectra]] · RANS(ch05)·경계층(ch06).

## 1. 점성 응력 — 편차 응력텐서

- 점성 유체의 총 응력 $\tau_{ij}$ 은 **등방 압력 $-p\delta_{ij}$ + 편차 응력(deviatoric stress) $\sigma_{ij}^{dev}$**(점성·속도구배 기인): $\tau_{ij}=-p\delta_{ij}+\sigma_{ij}^{dev}$ (hudspeth2005-wave-forces, p.87, Eq. 3.29, Batchelor 1983 p.142). 무점성(Euler)은 편차부가 0 — [[theory-ch03-euler]] §3 의 $\boldsymbol\sigma=-p\mathbf{I}$. (이하 총응력 $\tau_{ij}$·편차 $\sigma_{ij}^{dev}$ 표기 통일.)
- 압력 $p$ 측정이 어려운 이유: 편차 정규응력이 있어 속도구배가 0 이거나 유체가 정지해야 순수 압력을 잼 (hudspeth2005-wave-forces, p.87).

## 2. 변형률 텐서 — 속도구배 분해

- 속도구배 $\partial u_i/\partial x_j$ 의 **대칭부=변형률률 텐서(strain-rate) $\varepsilon_{ij}$·반대칭부=회전 텐서(vorticity) $\omega_{ij}$** 분해는 [[theory-ch00_5-math-tools]] §6 canonical(hudspeth2005-wave-forces p.82-83, Eq. 3.20) — 변형률=모양 변화(전단·팽창), 회전=강체 회전. 본 장은 이 분해를 점성 응력 구성에 적용.
- ★**점성 응력은 변형률에만 응답, 순수 회전에는 발생하지 않음** — Stokes 점성마찰법칙은 편차 전단응력을 **각변형률(rate of angular deformation)** 에 관계 (hudspeth2005-wave-forces, p.87, §3.3.3). 강체 회전에는 상대 운동이 없어 마찰 무발생.

## 3. Newtonian 구성식과 Stokes 가정

- **Stokes 점성마찰법칙(Newtonian)**: 탄성 고체 응력과의 유추(동점성계수 $\mu$ ↔ 전단 탄성계수)로 편차 정규응력을 $\sigma_{xx}^{dev}=2\mu\!\left(\dfrac{\partial u}{\partial x}-\dfrac13\nabla\cdot\mathbf{q}\right)$ 꼴로 씀 (hudspeth2005-wave-forces, p.87-89, Eq. 3.29d; Daily & Harleman 1966). 일반형 $\tau_{ij}=-p\delta_{ij}+2\mu\!\left(\varepsilon_{ij}-\tfrac13(\nabla\cdot\mathbf{q})\delta_{ij}\right)$.
- **Stokes hypothesis(1845)와 second viscosity**: 탄성 유추 유도는 **두 Lamé 상수를 피함** — 이는 곧 **second viscosity(팽창률 $\nabla\cdot\mathbf{q}$ 에만 응답하는 두 번째 점성)가 음의 정부호여야 한다는 논쟁적 요구**를 함축 (hudspeth2005-wave-forces, p.86, "Stokes hypothesis, 1845"; Lamb 1932 Ch.325-326·Schlichting 1979). 위 $-\tfrac13\nabla\cdot\mathbf{q}$ 항으로부터 체적 점성 $\lambda=-\tfrac23\mu$ 가 **등가 환산**됨(출처는 $\lambda$ 기호를 직접 쓰지 않음). ※연안 비압축 유동($\nabla\cdot\mathbf{q}=0$)에서는 이 팽창항 자체가 소거됨.

## 4. Navier-Stokes 방정식

- Cauchy 운동량([[theory-ch03-euler]] §3)에 Newtonian 응력 발산을 대입 → **비압축 N-S**: $\rho\dfrac{\partial\mathbf{q}}{\partial t}+\rho(\mathbf{q}\cdot\nabla)\mathbf{q}=-\gamma\nabla(U+z)+\mu\nabla^2\mathbf{q}$ ($\gamma=\rho g$, 중력 체적력 $F_B=-\rho g\nabla z$) (hudspeth2005-wave-forces, p.90, §3.3.4, Eq. 3.36, Lamb 1932). 동점성 $\nu=\mu/\rho$ 로 나눈 kinematic 형: $\partial_t\mathbf{u}+(\mathbf{u}\cdot\nabla)\mathbf{u}=-\tfrac1\rho\nabla p+\nu\nabla^2\mathbf{u}+\mathbf{f}$.
- 5항의 의미: 국소가속·**비선형 대류가속** $(\mathbf{u}\cdot\nabla)\mathbf{u}$·압력구배·**점성 확산** $\nu\nabla^2\mathbf{u}$·체적력. 비선형 대류항이 무점성 극한의 [[theory-ch03-euler]] §5 d'Alembert 역설과 대비되는 실제 유동(항력·박리)의 근원. ※원문 교재의 "난류·와류·박리를 모두 만든다"는 일반화 단정·Clay Millennium 문제(3D N-S 매끄러움)는 코퍼스 미확인 — 미이식.

## 5. 무차원화 — Reynolds 수와 상사

- 물리 모델링은 **3가지 상사(similitude)** 보존 필요: 기하(geometric)·운동학(kinematic)·동역학(dynamic) (hudspeth2005-wave-forces, p.102, §3.6). N-S 무차원화에서 **무차원 힘비**들이 등장 (Table 3.2).
- **Reynolds 수 $\mathrm{Re}=\dfrac{Ub}{\nu}=\dfrac{\rho Ub}{\mu}$ = 관성/점성 힘비** (hudspeth2005-wave-forces, p.102, Table 3.2). 같은 표의 병렬 무차원수: **Froude** $\mathrm{Fr}^2=U^2/gb$(관성/중력)·**Cauchy** $\rho U^2/E$(관성/탄성)·**Euler** $\rho U^2/2\Delta p$(관성/압력)·**Weber** $\rho bU^2/\sigma$(관성/표면장력)·**Keulegan-Carpenter** $UT/b$·**Strouhal** $b/(UT_s)$(와류 방출). ※동역학 상사는 기하·운동학 상사가 성립하고 **지배 힘비가 일치**할 때 성립 — Re 하나만으로는 일반 동역학 상사를 선언할 수 없음(같은 표가 Froude·Weber 등 추가 힘비를 열거).
- $\mathrm{Re}\gg1$ 관성 압도(경계층·난류 가능), $\mathrm{Re}\ll1$ 점성 압도(Stokes 흐름). 파이프 층류→난류 천이는 **$\mathrm{Re}\approx2000$** (stewart-physical-ocean, p.130, Reynolds 1883 실험, $\mathrm{Re}=VD/\nu$). ※Re 일상값 표는 미이식.

## 6. Poiseuille 흐름·경계조건

- **no-slip 경계조건**: 벽에서 유체 속도 = 0 (water-wave-mechanics, p.280, 파 경계층 문맥 $u=0$ at bed).
- **Poiseuille 흐름**: 압력구배 구동 원형 관 층류의 유량 정확해 **$Q=\dfrac{\pi R^4\,\Delta P}{8\mu L}$**(Hagen-Poiseuille, 반지름 4제곱 비례) — N-S 가 해석적으로 풀리는 대표 예 (mechanics-of-sediment-transport, p.828, Eq. 17.4 "conventional Poiseuille formula"). ※평판 유동 포물선 분포 전개·마이크로유체 응용은 직접 앵커 없어 미이식.

## 7. 한계 — 난류·Reynolds 응력(RANS 예고)

- 난류 흐름에서 속도를 **평균+변동으로 분해**하면 평균 운동량식에 **Reynolds 응력** $\rho\langle u_i'u_j'\rangle$(난류가 수송하는 운동량, "virtual stress")이 등장 (stewart-physical-ocean, p.130-132, §8.3, Prandtl·Kármán 계보; 예: $\rho\langle u'w'\rangle$=동쪽 운동량의 연직 하향 수송). 이를 mean flow 에 관계짓는 **eddy viscosity** 는 이론으로 얻을 수 없고 데이터로 산정 — 대부분 해양 유동에서 정확히 구하기 어려움 (stewart-physical-ocean, p.133·136). 난류 모델(k-ε 등) 정식은 ch05·`models/`(탐색; [[theory-ch09-nonlinear-spectra]] 스펙트럼과 연결). ※원문 교재의 'DNS 격자 ∝Re^{9/4}·RANS 필수' 정량 단정은 코퍼스 미확인 — 미이식.

## 8. 연결

- [[theory-ch03-euler]] — Cauchy 운동량·무점성 Euler (근거 의존)
- [[theory-ch00_5-math-tools]] — 변형률/회전 분해·발산·Laplacian (근거 의존)
- [[theory-ch09-nonlinear-spectra]] — 난류·비선형 (탐색)
- 다음: ch05 RANS(난류 평균)·ch06 경계층(Prandtl·d'Alembert 해결)·ch07 와도방정식.
