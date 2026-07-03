---
title: "파-흐름 상호작용 (Wave–Current Interaction) — Doppler shift·굴절·blocking·radiation stress feedback"
topic: waves
canonical_source: external
external_source: "arXiv:2511.12711v1 (Violante-Carvalho et al. 2025, Current effects on wind generated waves near an Ocean Eddy Dipole) + arXiv:2606.03231v1 (Onuki & Fujiwara 2026, A reduced model for surface wave–current interactions without spatial scale separation) — 양편 full PDF 직접 read"
citation_status: verified
has_source_needed: true
verification_method: "arXiv 2511.12711·2606.03231 full PDF (curl https://arxiv.org/pdf/...) pdftotext 직접 read. abstract·introduction·방법(§3 WW3 / §2 reduced model)·결과(Hs 상대차·% 증폭·dispersion·conservation) 인용분만 verified. 일부 일반 이론(radiation stress feedback·blocking 정의)은 본 두 논문에 명시 없어 source-needed."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - concepts/waves/01-concept.md
  - concepts/currents/01-concept.md
  - concepts/waves/07-wave-transmission.md
  - models/SWAN/manual-notes/swan-tech-ch2-7-qcm-theory.md
  - models/SWAN/manual-notes/swan-action-balance.md
  - models/SWAN/source-analysis/swan-gse-correction.md
---

# 08 — 파-흐름 상호작용 (Wave–Current Interaction)

> **흐름이 파에 미치는 효과**(current-on-wave)를 다룬다. 핵심 메커니즘: ① **Doppler shift**(이동 좌표계 frequency 변화) ② **굴절**(refraction, 흐름 vorticity에 의한 진행방향 휨) ③ **advection**(파 에너지의 이류) ④ **blocking/breaking**(역류에서 군속도 한계) ⑤ **radiation stress feedback**(파→흐름 역방향, two-way coupling).
> 본 노트는 inbox 2편(eddy dipole 풍파 효과 / reduced two-way model)을 promote한 객관 레이어. [[01-concept]](파의 기본)·[[../currents/01-concept]](흐름의 기본)과 연계하고, SWAN의 ambient-current 처리([[../../models/SWAN/manual-notes/swan-action-balance]] action balance, [[../../models/SWAN/manual-notes/swan-tech-ch2-7-qcm-theory]] QC scattering, [[../../models/SWAN/source-analysis/swan-gse-correction]] GSE)와 대비한다.

---

## 1. 운동학적 기초 — Doppler shift와 분산관계

흐름 $U$ 위를 진행하는 파의 **절대 진동수**(고정 좌표계 관측) $\omega$와 **고유 진동수**(intrinsic, 흐름과 함께 움직이는 좌표계) $\sigma$는

$$\omega = \sigma + \mathbf{k}\cdot\mathbf{U}$$

로 연결된다 (arXiv:2511.12711 Eq. 1; Peregrine 1976 인용). $\mathbf{k}\cdot\mathbf{U}>0$ (흐름·파 동방향)이면 파장이 길어지고, 역방향이면 짧아진다. 흐름에 **직교**로 진행하면 영향 없음. 정지수 분산관계

$$\sigma^2 = gk\tanh kh \quad\text{(Eq. 3)}$$

는 흐름 위에서 Doppler 관계를 대입해

$$(\omega - \mathbf{k}\cdot\mathbf{U})^2 = gk\tanh kh \quad\text{(Eq. 4)}$$

가 된다 (arXiv:2511.12711). 이 분산관계가 흐름 위 파 운동학의 출발점이며, SWAN의 action balance가 풀어내는 것과 동일한 frame 변환이다 ([[../../models/SWAN/manual-notes/swan-action-balance]]).

---

## 2. 흐름이 파에 미치는 효과 — eddy dipole 사례 (arXiv:2511.12711)

Violante-Carvalho et al. (2025)는 **WW3 (WAVEWATCH III v7.14, ST4 source term, $\beta_{max}=1.55$)** 로 ocean eddy dipole 주변 풍파장을 모사했다. eddy dipole = 반대 극성 회전류 한 쌍 → 중앙에 좁고 빠른 **central jet** 형성.

### 2.1 핵심 결과 — "수렴 렌즈"

| 항목 | 내용 (verified) |
|---|---|
| 메커니즘 | dipole가 표면파에 대해 **수렴 렌즈(converging lens)** 로 작용 — central jet 쪽으로 파를 굴절시켜 에너지 집중 |
| 최대 $H_s$ 증가 (이상화) | 7 s 파에서 central jet에서 **50% 초과** 증가 (Fig. 2c, 약 43°W) |
| 이상화 다른 주기 | 더 긴 주기 파는 최대 **33%** 증가 (intensification 작음) |
| 선형이론 비교 | 7 s 단색파 균일 역류: 선형이론 예측 **≈25%** 증가 (Eq. 5); 10% 증폭은 더 긴 파 |
| refraction + advection | 두 효과 **결합** 시 각각 독립 작용보다 훨씬 큰 에너지 증가 |
| 방향 휨 | 휨은 surface current speed가 아니라 **vorticity 연직성분 / 군속도 비**에 의존 |

### 2.2 흐름 product 비교 (hindcast)

2010년 8–9월 남서대서양 강한 dipole event를 3개 표면류 product로 hindcast:

| product | 특징 (verified) |
|---|---|
| HYCOM NCODA | **ageostrophic 효과 포함** → 총 에너지 표현 가장 상세, broader dynamics |
| SSalto/Duacs | geostrophic 주체. 해상도 낮지만 연구해역(geostrophy 우세)에서 **더 신뢰성 있는 $H_s$** field |
| GlobCurrent | geostrophic 주체. Ekman 성분 추가해도 substantial enhancement 없음 |

- 최대 파에너지 증가는 **양·음 vorticity peak 사이 영역**(반대 흐름이 최대 강도로 충돌하는 곳)에서 발생.
- $H_s$ 공간변동성은 흐름의 **vorticity 양**과 연결. $H_s$ 파수 스펙트럼은 파장 100–35 km에서 기울기 약 $k^{-2.5}$ (흐름 KE 스펙트럼과 유사 trend).
- altimeter $H_s$: denoised CCI-Hs(다중위성 retracking, **약 6 km** 해상도), 모든 mission positive bias·normalized mean <11%·scatter index <9%. altimeter 상관(Table 2): HYCOM 구동 **CORR 0.64**(전체)/0.55(central-jet), SSalto/Duacs 구동 0.68/0.65 — geostrophy 우세 영역서 SSalto/Duacs 가 더 정합.

> **메모**: opposing current에서 $U/c_g$ 비가 0.1–0.4면 단색파 진폭이 크게 증가(Onorato et al. 2011, mNLS), 더 큰 비에서는 **wave breaking·blocking** 가능 — 2511 introduction이 인용한 선행연구. blocking의 정량 한계식 자체는 본 논문에 명시 없음 (source-needed).

---

## 3. Two-way 결합 reduced model (arXiv:2606.03231)

Onuki & Fujiwara (2026)는 **공간 scale 분리 없이(without spatial-scale separation)** 약비선형 표면중력파와 느린 비압축성 흐름의 **상호** 작용을 다루는 reduced asymptotic model을 제안. 표적: deep water, weakly nonlinear, non-breaking.

### 3.1 동기 — CL 이론의 한계

- 표준 **Craik–Leibovich (CL)** 이론: 파 효과가 **Stokes drift**와 vortex force를 통해 wave-averaged 운동량식에 진입 → Langmuir circulation 설명.
- 통상 CL은 Stokes drift를 **외부에서 prescribe** (McWilliams et al. 1997) → 파장이 동역학적 에너지 reservoir가 아님.
- 실제 파는 흐름에 의해 advect·refract·scatter·진폭변조됨(DNS Fujiwara & Yoshikawa 2020 등). → **wave-resolving closure** 필요.

### 3.2 방법·구조 (verified)

| 요소 | 내용 |
|---|---|
| 베이스 | CL wave-averaged 운동량식 (Eq. 2.2): $\mathbf{U}^L_t + \mathbf{U}^L\!\cdot\!\nabla\mathbf{U}^L + (f\mathbf{z}-\nabla\times\mathbf{U}^s)\times\mathbf{U}^L = -\nabla\Pi + \mathbf{U}^s_t$ |
| 파장 가정 | intrinsic frequency $\omega$ 근방 **narrow-band**, 단 방향 미국소화 — 수평 스펙트럼이 **원 $\|\mathbf{k}\|=\kappa$** 근방 집중(단일 carrier wavevector 아님) → multidirectional scattering 표현 |
| 흐름 가정 | 느림, 속도가 **Stokes drift와 동차수**, advective 시간척도 진화 |
| 닫힘 | wave steepness 다중시간척도 전개 + quartic wave–wave 무시·**3차 Stokes 보정 retain**하는 phenomenological closure |
| Stokes drift | 외부 prescribe 아니라 narrow-band 진폭 $A$의 companion **amplitude equation**으로 결정 (양방향) |
| 보존 | **wave action invariant** + 결합계의 closed **energy·momentum budget** |

> Stokes drift는 진폭 $A$로부터 계산되며 $C^2=g\kappa/(\omega\omega_\kappa)$ 형태 분산 인자 사용. 가장 가까운 선행 양방향 모델은 Xie & Vanneste (2015, near-inertial wave ↔ QG flow).

### 3.3 의의

WKB-type ray/action 기술(Vanneste & Young 2026 등)이 scale 분리에 의존하는 것과 달리, 이 모델은 **파장과 같은 수평 척도의 흐름(Langmuir circulation 등)**에 의한 multidirectional scattering·directional spectral redistribution을 일반 형태로 다룬다. CL framework의 **에너지정합 양방향 확장**.

---

## 4. SWAN의 current-on-wave 처리와 대비

| 처리 | SWAN | 본 논문들 |
|---|---|---|
| Doppler/굴절 | action balance (ambient current $\sigma$↔$\omega$ frame) — [[../../models/SWAN/manual-notes/swan-action-balance]] | 동일 운동학 Eq. 1·4 (2511, WW3) |
| scattering·diffraction | Quasi-Coherent (QC) Wigner/Weyl — [[../../models/SWAN/manual-notes/swan-tech-ch2-7-qcm-theory]] | scale 분리 없는 reduced model이 multidirectional scattering 표현 (2606) |
| 수치 분산(garden-sprinkler) | GSE correction subroutine — [[../../models/SWAN/source-analysis/swan-gse-correction]] | (해당 없음 — spectral phase-averaged 모델의 수치 artifact 보정) |
| two-way feedback | phase-averaged action balance(파→흐름 radiation stress는 별도 coupling 필요) | CL closure 자체에 **양방향** wave↔current 내장 (2606) |

> SWAN/WW3는 **phase-averaged** spectral 모델(action balance), 2606은 **wave-resolving** reduced PDE — 적용 regime이 다르다. 2511은 WW3로 mesoscale current가 $H_s$에 미치는 효과를 정량화한 사례.

---

## 5. 미정리 (source-needed)

- **radiation stress feedback**(파→평균류 운동량 전달, Longuet-Higgins & Stewart)의 정식 정의·식: 본 두 논문에 명시 없음 → 별도 교과서 출처 필요.
- **wave blocking** 정량 한계(군속도=역류 조건, $U_c = -c_g/4$ 등): 2511이 개념 언급만, 식 미제시.
- radiation stress·set-up과 surf zone current 결합은 [[../currents/01-concept]] / [[07-wave-transmission]] 와 교차 — 후속 연계 필요.
