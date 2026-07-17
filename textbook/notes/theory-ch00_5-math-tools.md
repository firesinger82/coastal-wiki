---
title: "이론 ch00.5 — 수학 도구: 벡터·텐서 표기 · 미분연산자 · 적분정리 · 물질미분 · RTT"
topic: math-foundations
layer: 1
depends_on: []
canonical_source: self
citation_status: verified
claims_total: 31
claims_attached: 24
claims_dropped: 7
claims_source_needed: 0
claims_basis: legacy-ledger
provenance: "교재 프로젝트 textbook-ai-data-full ch00.5(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(파일럿) MODIFY 반영. ★주 출처 정정: 원장 후보 hydraulics-and-hydrology 에는 벡터·텐서 미적분·물질미분·RTT·발산정리가 전무(스캔 0건) → 실제 주 출처는 **hudspeth2005-wave-forces(Hudspeth, Waves and Wave Forces) §2 수학 도구·§3 유체역학 기초**로 확정. Codex 게이트 정정: 페이지 마커 실측 정정(Levi-Civita p.29·gradient p.31·Laplacian p.32·Leibnitz p.34·Taylor p.36-38·속도구배 p.80-83 §3.3.1·Green 제2 Eq.2.123c·경계 ∂D 통일)·Einstein summation p.666 부착·rank 일반분류/공변반변 삭제(직접 출처 없음)·★pathline 복원(stewart-physical-ocean p.199-201 실존 — 삭제 오판, streakline 만 미이식). 미매칭 삭제/미이식: 순수 수학사(사원수 '벡터 전쟁'·∂ 기호 1786·오일러/라그랑주 연도·야코비 1841)·streakline·Stokes 정리(코퍼스 0건)·워크 예제. 이 노트는 후속 ch01(보존)·ch02(연속)·ch04(N-S) 의 유도 기반(①→① depends_on 대상). T7 기초 파일럿([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "hudspeth2005-wave-forces p.27-29·31-34·36-38·69-70·78·80-83·91-92·666(§2.2 표기·연산자·§2.3.3 Taylor·§2.6 적분정리·§3.2-3.3 유체역학 기초·강체 텐서합) + stewart-physical-ocean p.199-201(유선·입자경로·유선함수) — textbook/md 미러 페이지 직접 대조 (2026-07-14, Codex 게이트 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch08-linear-waves.md
  - textbook/notes/tides-stewart-ch17.md
---

# 수학 도구 — 벡터·텐서 표기 · 미분연산자 · 적분정리 · 물질미분

> 4-레이어 **① 이론** 노트. 유체역학(보존법칙·연속·Euler·N-S)의 유도에 필요한 벡터·텐서 미적분 도구 모음 — 후속 기초 챕터가 근거 의존할 토대.
> ※주 출처는 **Hudspeth §2(수학 예비)·§3(유체역학 기초)** — 이 책이 물질미분·적분정리·연속·속도구배를 직접 다룸(단 §2는 "briefly outlined" 요약 성격, p.26). 원장의 hydraulics-and-hydrology 후보는 미커버로 정정. 유선/입자경로는 stewart-physical-ocean 보강.
> 탐색 링크(근거 의존 아님): 선형파 응용 [[theory-ch08-linear-waves]].

## 1. 표기 — 벡터·텐서와 인덱스 합 규약

- 텐서·행렬·벡터 표기에서 **Levi-Civita 순열 기호**가 복잡한 연산(강체 동역학 등)을 콤팩트하게 표현하는 핵심 도구 (hudspeth2005-wave-forces, p.28, §2.2.4). 응력·변형률 같은 2차 텐서의 정식 취급은 §6.
- **합 규약(Einstein summation)**: 반복 첨자는 자동으로 텐서 합을 의미 (hudspeth2005-wave-forces, p.666; Levi-Civita 와 함께 강체 관성 텐서 등에 적용). ※원문 교재의 벡터 표기 역사(사원수 '벡터 전쟁'·∂ 기호 연도)·rank 일반 분류표·공변/반변 관례는 코퍼스 직접 지지 없음 — 미이식.

## 2. 함수의 종속성 — Euler장 vs Lagrange 입자

- 유동량은 두 관점으로 기술: **Eulerian field**(공간 고정점 $ (x,y,z,t) $, 변수 독립)와 **Lagrangian particle**(입자 라벨을 따라감). Stokes material surface $S(x,y,z,t)$ 는 두 문제에 모두 등장하며, 그 물질미분은 곧 **면 함수의 전미분**(total derivative) (hudspeth2005-wave-forces, p.32, §2.2.10). ※원문 교재의 오일러(1755)·라그랑주(1788) 연도·강물 비유는 코퍼스 미확인 — 미이식(개념만).
- **편미분 vs 전미분**: $\partial f/\partial t$ 는 공간 고정점의 시간 변화율, 전미분 $df/dt$ 는 경로를 따라간 변화율. 다변수 전개의 근거는 **Taylor/Maclaurin 급수** (hudspeth2005-wave-forces, p.36-38, §2.3.3, Eq. 2.18·다변수 Eq. 2.22; 1차 항의 합 구조가 연쇄법칙·전미분의 형태를 결정). ※원문 교재의 ∂ 기호 역사(1786 Legendre)·야코비(1841) 연도는 미이식.

## 3. 미분 연산자 — ∇·∇·×∇·∇²

- **Gradient(나블라) $\nabla$**: 좌표 방향의 변화율을 주는 유사벡터 연산자. 데카르트 $\nabla=(\partial_x,\partial_y,\partial_z)$·원통좌표 형식 병기 (hudspeth2005-wave-forces, p.31, §2.2.7). $(\cdot)$ 와 교환하지 않으므로 pseudo-vector.
- **Curl $\nabla\times$**: 회전면에 수직인 회전 벡터 — 데카르트(p.31)·원통좌표(p.32) 행렬식 형식 (hudspeth2005-wave-forces, p.31-32, §2.2.8, Eq. 2.11). 유체 회전(vorticity)의 기반 — ch07(와도 동역학) 축.
- **Laplacian $\nabla^2=\Delta$**: 2차 편미분의 합 스칼라 연산자 (hudspeth2005-wave-forces, p.32, §2.2.9) — 퍼텐셜 유동·확산의 핵심.

## 4. 기본 텐서 기호 — Kronecker·Levi-Civita

- **Kronecker delta $\delta_{mn}$**: $n=m$ 이면 1, 아니면 0 (이산 함수용) (hudspeth2005-wave-forces, p.28, §2.2.3, Eq. 2.2).
- **Levi-Civita 순열 기호 $\varepsilon_{ijk}$**: 두 첨자 이상 같으면 0, 123의 **짝(cyclic)순열이면 +1**(예 $\varepsilon_{231}$)·**홀(anticyclic)순열이면 −1**(예 $\varepsilon_{321}$) (hudspeth2005-wave-forces, p.29, §2.2.4, Eq. 2.5·Fig. 2.1; 절 시작 p.28). 외적 $v_i=\varepsilon_{ijk}a_jb_k$ 등 텐서 조작을 압축.
- **Dirac delta 분포·Heaviside 계단함수**: 적분 안에서만 의미를 갖는 일반화 함수 — Dirac delta 는 Heaviside 의 형식적 도함수 (hudspeth2005-wave-forces, p.27-28, §2.2.2-2.2.3, Eq. 2.1·2.4).

## 5. 적분 정리 — Gauss·Green

- **Gauss 발산정리**: 체적적분과 경계면 적분을 잇는다 $\iiint_D \nabla\cdot\mathbf{F}\,dV = \iint_{\partial D}\mathbf{F}\cdot\mathbf{n}\,dS$ (hudspeth2005-wave-forces, p.69, §2.6, Eq. 2.122a). 연속·운동량 방정식의 미분형↔적분형 변환의 핵심.
- **Green 항등식**: 발산정리에 $\mathbf{F}=\psi\nabla\phi$ 를 대입해 **Green 제1항등식** $\iiint_D(\psi\nabla^2\phi+\nabla\psi\cdot\nabla\phi)dV=\iint_{\partial D}\psi\frac{\partial\phi}{\partial n}dS$ (Eq. 2.123a), $\mathbf{F}=\phi\nabla\psi$ 로 재정의해 빼면 **제2항등식** (hudspeth2005-wave-forces, p.70, Eq. 2.123a·2.123c) — 퍼텐셜 유동 경계요소법의 토대. ※원문 교재의 Stokes 정리 절은 코퍼스 미확인 — 미이식.

## 6. 2차 텐서 — 속도구배의 대칭/반대칭 분해

- 속도구배 텐서 $\partial u_i/\partial x_j$ 는 **대칭부(변형률률 텐서, strain-rate)** 와 **반대칭부(회전 텐서)** 로 분해된다 — 각도 변형·회전의 기하에서 유도되며(Eq. 3.15-3.19), 해석함수 분해 정리로도 동일 결과 (hudspeth2005-wave-forces, p.80-83, §3.3.1, Eq. 3.18-3.20). 이 분해가 점성 응력↔변형률률 구성관계(N-S)의 출발점. ※원문 교재의 trace·행렬식·고윳값 불변량 일반론·좌표변환 상세는 코퍼스에서 이 문맥으로 직접 미확인 — 미이식(N-S 유도 시 재도입).

## 7. 물질미분·Leibniz·RTT — 유체역학 유도의 핵심 도구

- **Stokes 물질미분 연산자**: Eulerian 장 $V(x,y,z,t)$ 에 대해 $\dfrac{D}{Dt}=\dfrac{\partial}{\partial t}+\mathbf{q}\cdot\nabla$ — 공간 고정 변화($\partial/\partial t$)와 이류(advection, $\mathbf{q}\cdot\nabla$)의 합 (hudspeth2005-wave-forces, p.32-33, §2.2.10, Eq. 2.13). ch01(보존법칙)·ch04(N-S) 좌변 $\rho D\mathbf{u}/Dt$ 의 정의.
- **Leibnitz 적분 미분 규칙**: 매개변수를 포함한 적분의 미분 — 적분 상·하한이 움직일 때 경계 기여 항이 추가 (hudspeth2005-wave-forces, p.34, §2.2.11, Eq. 2.14). 3차원 이동 영역으로 일반화하면 RTT.
- **Reynolds 수송정리(RTT)**: 임의 검사체적에 대한 보존의 적분형 — 연속의 예로 $\dfrac{d}{dt}\iiint_{cv(t)}\rho\,dV+\oiint_{cs}\rho\mathbf{q}\cdot\mathbf{n}\,dS=0$ (hudspeth2005-wave-forces, p.78, §3.2, Eq. 3.11). 미분형 연속방정식 $\dfrac{D\rho}{Dt}+\rho\nabla\cdot\mathbf{q}=0$ 과 등가 (Eq. 3.10b) — ch01·ch02 의 핵심 결과를 선취.

## 8. 흐름의 기하 — 유선·입자경로

- **유선(streamline)** = 매 순간 속도 벡터에 처처에서 접하는 순간 곡선; 비정상류면 유선 패턴이 시간에 따라 변함. **입자경로(pathline)** = 유체 입자(Lagrangian drifter)의 궤적 — **정상류에서는 유선과 일치, 비정상류에서는 다름** (stewart-physical-ocean, p.199-200, "Stream Lines, Path Lines, and the Stream Function"; Kundu 1990 인용). 2D 비압축류는 **유선함수 $\psi$** 로 기술, 두 유선 사이 체적유량 = $\psi_1-\psi_2$ (stewart-physical-ocean, p.200-201). ※자취선(streakline)은 코퍼스 미확인 — 미이식.
- **유선(streamline)**을 따라 Euler 방정식을 적분하면 **Bernoulli 방정식**을 얻는다 — 파 이론에서 반복 사용 (hudspeth2005-wave-forces, p.91-92; 비정상형은 §3.4).

## 9. 연결

- 후속 기초 챕터 ch01(보존법칙)·ch02(연속)·ch03(Euler·Bernoulli)·ch04(N-S) 가 본 노트의 물질미분·RTT·발산정리·텐서 분해를 근거 의존(depends_on 대상).
- [[theory-ch08-linear-waves]] — 퍼텐셜 유동·Laplacian 응용 (탐색).
- 다음: ch01 보존법칙 (T7 트랙) — RTT·물질미분을 검사체적 보존에 적용.
