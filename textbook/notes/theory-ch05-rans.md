---
title: "이론 ch05 — RANS: Reynolds 분해 · Reynolds 응력 · 닫힘 문제 · eddy viscosity · mixing length"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch04-navier-stokes.md
canonical_source: self
citation_status: verified
claims_total: 20
claims_attached: 15
claims_dropped: 2
claims_source_needed: 3
claims_basis: legacy-ledger
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch05(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착 + 같은 날 Codex 게이트(T12) MODIFY 반영. 주 출처 = **stewart-physical-ocean §8(Turbulence) + mechanics-of-sediment-transport(mixing length·Kolmogorov)**. Codex 게이트 정정(★마커·0건 오판): stewart 페이지 정정(난류/Re p.128→p.129·대양 10^11 p.128→p.130·상사 p.130-131·closure p.132+p.135)·mixing length = MST p.154 Prandtl 1925 확립(p.136 개괄 아님, Kármán similarity 별도)·Kolmogorov = MST p.151-152 원 위치(p.883 응용). ★'0건' 철회: TKE·LES/subgrid·k-ε 상수는 일반 교재 미확정이나 모델 매뉴얼·구현 증거 존재(ROMS TKE=½q²·EFDC Smagorinsky·stewart p.272·275 subgrid Mellor-Yamada·SWASH/CADMAS Cμ0.09) → 구현별은 models canonical·일반 이론은 ch05 source-needed. Kolmogorov -5/3 멱법칙·Boussinesq 1877 eddy 정확식·Clay Millennium = 코퍼스 미확인. depends_on ch04(N-S 평균, ch00.5는 특정 정의 미사용이라 의존 제거). T12([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "stewart-physical-ocean p.129-133·135-136·272·275(§8 난류·Re·Reynolds 분해 Eq.8.5·Reynolds 응력 Eq.8.13·eddy viscosity·closure·subgrid) + mechanics-of-sediment-transport p.151-152·154(Kolmogorov scale Eq.4.7·Prandtl 1925 mixing length) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14, Codex 게이트 재검증 포함)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
  - textbook/notes/theory-ch13-sediment-transport.md
---

# RANS — Reynolds 분해 · Reynolds 응력 · 닫힘 · eddy viscosity

> 4-레이어 **① 이론** 노트. [[theory-ch04-navier-stokes]] 의 N-S 를 시간 평균하여 난류 유동을 다루는 통계적 방정식(근거 의존 ①→①). N-S 의 비선형 대류항이 난류의 기원.
> 탐색 링크(근거 의존 아님): 난류 모델 구현 `models/`(EFDC·ROMS·SWASH k-ε/GLS) · 비선형 스펙트럼 [[theory-ch09-nonlinear-spectra]].

## 1. 난류의 기원과 Reynolds 수

- **난류는 운동량 방정식의 비선형 항($u\,\partial u/\partial x$ 등)에서 발생** — 그 중요도는 **Reynolds 수 = 비선형/점성 항의 비**(상세 정의는 [[theory-ch04-navier-stokes]] §5 canonical)로 판정 (stewart-physical-ocean, p.129, §8.2). 분자 점성은 수 mm 거리에서만 중요, 경계 영향이 내부로 전달되는 통로가 곧 난류.
- **환경 유동은 거의 항상 난류**: 대양은 $U\sim0.1$ m/s·$L\sim1$ Mm 로 $\mathrm{Re}\sim10^{11}$ — 비선형 항이 $\mathrm{Re}>10\text{–}1000$ 에서 중요하므로 "the ocean is turbulent" (stewart-physical-ocean, p.130).
- **같은 기하·같은 Re → 같은 유동 패턴**(1 mm vs 1 m 원기둥 동일) (stewart-physical-ocean, p.130-131, Fig. 8.3). ※원문 교재의 난류 5특성 정식 목록(비가역성 등)은 stewart 서술로 응축.

## 2. Reynolds 분해와 평균

- 순간량을 **평균 + 변동으로 분해**: $u=U+u'$, $v=V+v'$, $w=W+w'$, $p=P+p'$ — 평균 $U$ 는 시간(또는 공간) 평균 (stewart-physical-ocean, p.131, §8.2, Eq. 8.5). 정의상 변동의 평균은 0.
- 이 분해를 [[theory-ch04-navier-stokes]] 의 N-S 에 대입·평균하면 평균 변수의 방정식(RANS)을 얻되, **변동의 곱 항이 0 이 아니어서 새 항으로 살아남음**(비선형이 정보 소실을 만듦) — 이것이 Reynolds 응력 (stewart-physical-ocean, p.131-132, Eq. 8.7-8.11 직접 유도).

## 3. Reynolds 응력과 닫힘 문제

- **Reynolds 응력**: 난류 변동이 운동량을 수송 — Prandtl·Kármán 은 난류 유체 덩어리가 층류의 분자처럼 운동량을 옮긴다고 가정 (stewart-physical-ocean, p.130-131, §8.2). 응력 형태 $-\rho\langle u'w'\rangle=T_{xz}$ (stewart-physical-ocean, p.133, Eq. 8.13). 대각 성분($\langle u'^2\rangle$ 등)은 변동 분산, 비대각은 변동 상관을 나타냄(표준 텐서 해석).
- **virtual stress**: $\partial\langle u'w'\rangle/\partial z$ 등을 점성항과 같은 역할로 가정하기에 '가상 응력'이라 부름 (stewart-physical-ocean, p.132, §8.3).
- **닫힘 문제(closure problem)**: 더 진행하려면 **Reynolds 응력의 값 또는 함수형이 필요** — 방정식 수보다 미지수가 많아 닫히지 않음 (stewart-physical-ocean, p.132; 고차 모멘트가 다시 생기는 계층은 p.135). 실험 직접 측정은 정확하나 일반화 어려움 → 더 일반적 접근 모색 (stewart-physical-ocean, p.132). ※원문 교재의 "10 미지수 4 식" 정량 셈은 코퍼스 직접 미확인 — 개념만.

## 4. Eddy viscosity와 mixing length

- **Eddy viscosity 가설**: Reynolds 응력을 평균 속도 구배에 비례로 모델 — $-\rho\langle u'w'\rangle=T_{xz}=\rho A_z\dfrac{\partial U}{\partial z}$, $A_z$ 가 분자 점성 $\nu$ 를 대체하는 **eddy viscosity(eddy diffusivity)** (stewart-physical-ocean, p.133, Eq. 8.13). 분자 점성보다 훨씬 큼.
- **한계**: $A_z$ 는 **이론으로 얻을 수 없고 데이터로 산정** — 대부분 해양 유동에서 정확히 구하기 어려움 (stewart-physical-ocean, p.136). ※Boussinesq(1877) eddy 가설의 역사 귀속·트레이스 보정 정확식은 코퍼스 미확인 — 미이식(정식은 아래 §5 source-needed). <!-- citation_status: source-needed -->
- **Mixing length 모델**: **Prandtl 이 1925 에 확립** — 기체 분자운동에 유추해 유체 요소(eddy)의 평균자유행로에 해당하는 **혼합길이(mixing length) $l$** 로 난류 혼합을 기술 (mechanics-of-sediment-transport, p.154; Kármán 은 이후 similarity hypothesis 로 보강). 상세 정식은 표사 이송 [[theory-ch13-sediment-transport]] 문맥 및 `models/` 축.

## 5. 난류 모델·에너지 캐스케이드

- **난류 모델(k-ε 등)의 구현별 정식·상수는 모델 축, 일반 이론은 보류**: eddy viscosity 를 난류 운동에너지·소산률의 추가 PDE 로 결정하는 k-ε·k-ω·GLS 의 **구현별 정식·상수**(예 $C_\mu=0.09$·Launder-Spalding k-ε)는 `models/`(EFDC·ROMS·SWASH·CADMAS source-analysis)가 canonical — 복제 금지. **일반 이론**(TKE $k=\tfrac12\langle u_i'u_i'\rangle$·Boussinesq eddy 가설·k-ε 두 방정식의 의미)은 textbook 코퍼스 일반 출처 미확정이라 ch05 보류(모델 매뉴얼 증거는 존재: ROMS TKE=$\tfrac12q^2$·EFDC Smagorinsky subgrid closure·stewart p.272·275 subgrid eddy viscosity·Mellor-Yamada). <!-- citation_status: source-needed -->
- **Kolmogorov 캐스케이드**: 중간 크기 와류가 최대 운동에너지("energy-containing")를 갖고, 작아질수록 점성 소산 증가, **가장 작은 와류 $l_k$**(eddy Reynolds 수 ~1)에서 점성·관성 균형 — Kolmogorov 가 차원해석으로 $l_k$·변동속도를 소산률 $\varepsilon$·동점성 $\nu$ 로 정의 (mechanics-of-sediment-transport, p.151-152, §4, Eq. 4.7; p.883 은 고분자 drag reduction 응용 재인용). ※Kolmogorov -5/3 관성영역 멱법칙 $E(k)=C_K\varepsilon^{2/3}k^{-5/3}$ 는 코퍼스 미확인 — 미이식(스펙트럼 계보는 [[theory-ch09-nonlinear-spectra]] 파랑 축과 별개). <!-- citation_status: source-needed -->

## 6. 연결

- [[theory-ch04-navier-stokes]] — N-S(평균 대상)·Re 정의·Reynolds 응력 선취 (근거 의존)
- `models/`(EFDC·ROMS·SWASH) — k-ε/GLS 난류 폐합 구현 (탐색, canonical)
- [[theory-ch09-nonlinear-spectra]] — 파랑 스펙트럼(별개 계보) (탐색)
- 다음: ch06 경계층(Prandtl·d'Alembert 해결)·ch07 와도방정식.
