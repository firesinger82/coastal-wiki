---
title: "이론 ch05 — RANS: Reynolds 분해 · Reynolds 응력 · 닫힘 문제 · eddy viscosity · mixing length"
topic: fluid-foundations
layer: 1
depends_on:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch00_5-math-tools.md
canonical_source: self
citation_status: verified
has_source_needed: true
provenance: "교재 프로젝트 textbook-ai-data-full ch05(AI 합성 MDX, 무인용) 이식분 — 2026-07-14 원자 단언 분해·(source_id, page) 부착. 주 출처 = **stewart-physical-ocean §8(Turbulence) + mechanics-of-sediment-transport(mixing length·Kolmogorov)**. ★삭제 전 전체 코퍼스 grep(정확 용어+개념 동의어+주 출처 절 통독): k-ε 모델 정식·상수(Cμ 0.09·Launder-Sharma)·TKE 정확식·LES/subgrid = 전 코퍼스 **0건** — 모델 구현은 `models/`(EFDC·ROMS·SWASH k-ε/GLS) 탐색 링크(복제 금지, THEORY-LEDGER 방침)·Kolmogorov -5/3 멱법칙도 코퍼스 미확인(scale η 만 실존). Clay Millennium 문제 = stewart 오탐(ch04 동일). 미이식: Boussinesq 1877 eddy 가설 명시식·워크예제·DNS 격자 Re^{9/4} 정량. depends_on ch04(N-S 평균)·ch00.5(텐서). T12([THEORY-LEDGER](../THEORY-LEDGER.md))."
verification_method: "stewart-physical-ocean p.128·130-133·136(§8 난류·Re·Reynolds 분해 Eq.8.5·Reynolds 응력 Eq.8.13·eddy viscosity·closure) + mechanics-of-sediment-transport p.136·883(Prandtl-Kármán mixing length·Kolmogorov scale Ch.4 Eq.4.7) — textbook/md 미러 ---PAGE-N--- 마커 실측 대조 (2026-07-14)."
note_author: "Claude Fable 5 (citation-grounded port)"
note_date: 2026-07-14
related:
  - textbook/notes/theory-ch04-navier-stokes.md
  - textbook/notes/theory-ch09-nonlinear-spectra.md
  - textbook/notes/theory-ch00_5-math-tools.md
---

# RANS — Reynolds 분해 · Reynolds 응력 · 닫힘 · eddy viscosity

> 4-레이어 **① 이론** 노트. [[theory-ch04-navier-stokes]] 의 N-S 를 시간 평균하여 난류 유동을 다루는 통계적 방정식(근거 의존 ①→①). N-S 의 비선형 대류항이 난류의 기원.
> 탐색 링크(근거 의존 아님): 난류 모델 구현 `models/`(EFDC·ROMS·SWASH k-ε/GLS) · 비선형 스펙트럼 [[theory-ch09-nonlinear-spectra]].

## 1. 난류의 기원과 Reynolds 수

- **난류는 운동량 방정식의 비선형 항($u\,\partial u/\partial x$ 등)에서 발생** — 그 중요도는 무차원수 **Reynolds 수 = 비선형/점성 항의 비**로 판정 (stewart-physical-ocean, p.128, §8.1). 분자 점성은 수 mm 거리에서만 중요, 경계 영향이 내부로 전달되는 통로가 곧 난류.
- **환경 유동은 거의 항상 난류**: 대양은 $U\sim0.1$ m/s·$L\sim1$ Mm 로 $\mathrm{Re}\sim10^{11}$ — 비선형 항이 $\mathrm{Re}>10\text{–}1000$ 에서 중요하므로 "the ocean is turbulent" (stewart-physical-ocean, p.128). 파이프 층류→난류 천이는 $\mathrm{Re}\approx2000$(근거 [[theory-ch04-navier-stokes]] §5).
- **같은 기하·같은 Re → 같은 유동 패턴**(1 mm vs 1 m 원기둥 동일) (stewart-physical-ocean, p.130, Fig. 8.3). ※원문 교재의 난류 5특성 정식 목록(비가역성 등)은 stewart 서술로 응축.

## 2. Reynolds 분해와 평균

- 순간량을 **평균 + 변동으로 분해**: $u=U+u'$, $v=V+v'$, $w=W+w'$, $p=P+p'$ — 평균 $U$ 는 시간(또는 공간) 평균 (stewart-physical-ocean, p.131, §8.2, Eq. 8.5). 정의상 변동의 평균은 0.
- 이 분해를 [[theory-ch04-navier-stokes]] 의 N-S 에 대입·평균하면 평균 변수의 방정식(RANS)을 얻되, **변동의 곱 항이 0 이 아니어서 새 항으로 살아남음**(비선형이 정보 소실을 만듦) — 이것이 Reynolds 응력.

## 3. Reynolds 응력과 닫힘 문제

- **Reynolds 응력**: 난류 변동이 운동량을 수송 — Prandtl·Kármán 은 난류 유체 덩어리가 층류의 분자처럼 운동량을 옮긴다고 가정 (stewart-physical-ocean, p.130-131, §8.2). 응력 형태 $-\rho\langle u'w'\rangle=T_{xz}$ (stewart-physical-ocean, p.133, Eq. 8.13). 대각($\langle u'^2\rangle$ 등)=난류 강도, 비대각=변동 상관.
- **virtual stress**: $\partial\langle u'w'\rangle/\partial z$ 등을 점성항과 같은 역할로 가정하기에 '가상 응력'이라 부름 (stewart-physical-ocean, p.132, §8.3).
- **닫힘 문제(closure problem)**: 더 진행하려면 **Reynolds 응력의 값 또는 함수형이 필요** — 방정식 수보다 미지수가 많아 닫히지 않음 (stewart-physical-ocean, p.132; hudspeth2005-wave-forces 도 closure 언급). 실험 직접 측정은 정확하나 일반화 어려움 → 더 일반적 접근 모색 (stewart-physical-ocean, p.132). ※원문 교재의 "10 미지수 4 식·3차 모멘트 계층" 정량 셈은 코퍼스 직접 미확인 — 개념만.

## 4. Eddy viscosity와 mixing length

- **Eddy viscosity 가설**: Reynolds 응력을 평균 속도 구배에 비례로 모델 — $-\rho\langle u'w'\rangle=T_{xz}=\rho A_z\dfrac{\partial U}{\partial z}$, $A_z$ 가 분자 점성 $\nu$ 를 대체하는 **eddy viscosity(eddy diffusivity)** (stewart-physical-ocean, p.133, Eq. 8.13). 분자 점성보다 훨씬 큼.
- **한계**: $A_z$ 는 **이론으로 얻을 수 없고 데이터로 산정** — 대부분 해양 유동에서 정확히 구하기 어려움 (stewart-physical-ocean, p.136). ※Boussinesq(1877) eddy 가설의 명시식·트레이스 보정 $-\tfrac23k\delta_{ij}$ 는 코퍼스 미확인 — 미이식.
- **Mixing length 모델**: Prandtl·Kármán 이 1925-1930 에 도입한 고전 이론 — 한 길이 척도로 eddy viscosity 추정 (mechanics-of-sediment-transport, p.136; 벽 근처 유동에 유효). 상세 정식은 표사 이송 [[theory-ch13-sediment-transport]] 문맥 및 `models/` 축.

## 5. 난류 모델·에너지 캐스케이드

- **난류 모델(k-ε 등)은 모델 구현 축**: eddy viscosity 를 난류 운동에너지·소산률의 추가 PDE 로 결정하는 k-ε·k-ω·GLS 정식·상수는 `models/`(EFDC·ROMS·SWASH source-analysis)가 canonical — 복제 금지. ※k-ε 정확식·상수(Cμ=0.09·Launder-Sharma 1972)·TKE $k=\tfrac12\langle u_i'u_i'\rangle$·DNS/LES/subgrid 는 textbook 코퍼스 미확인. <!-- citation_status: source-needed -->
- **Kolmogorov 캐스케이드**: 큰 와류가 부서져 작은 와류로, 최종적으로 **가장 작은 와류(Kolmogorov scale) $\eta$** 에서 점성 소산 — $\eta$ 는 점성·소산률로 결정 (mechanics-of-sediment-transport, p.883, Ch.4 Eq.4.7 "size of the smallest eddy"; 고분자 첨가가 소에디 억제로 drag reduction 하는 문맥). ※Kolmogorov -5/3 관성영역 멱법칙 $E(k)=C_K\varepsilon^{2/3}k^{-5/3}$ 는 코퍼스 미확인 — 미이식(스펙트럼 계보는 [[theory-ch09-nonlinear-spectra]] 파랑 축과 별개). <!-- citation_status: source-needed -->

## 6. 연결

- [[theory-ch04-navier-stokes]] — N-S(평균 대상)·Reynolds 응력 선취 (근거 의존)
- [[theory-ch00_5-math-tools]] — 텐서·평균 연산 (근거 의존)
- `models/`(EFDC·ROMS·SWASH) — k-ε/GLS 난류 폐합 구현 (탐색, canonical)
- [[theory-ch09-nonlinear-spectra]] — 파랑 스펙트럼(별개 계보) (탐색)
- 다음: ch06 경계층(Prandtl·d'Alembert 해결)·ch07 와도방정식.
