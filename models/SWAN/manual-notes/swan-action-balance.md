---
title: "SWAN — Action Balance Equation + Source Terms (Holthuijsen Ch.9 §9.3 발췌)"
source_id: holthuijsen2007
chapter: "9.3 Action balance (p.288-296)"
pages: "286-296"
page_offset_applied: false
topic: waves
canonical_source: self
citation_status: verified
verification_method: "2026-10-13 추가·수정 줄을 swantech.pdf PDF 25·59–60쪽, swanuse.pdf PDF 65–66·69·74쪽, 현재 SWAN 코드 및 R2:SS-741–743의 최종 결론과 대조했다." # [10-13 전수 검증 정정]
last_source_check: "2026-10-13 (recovery 대조 반영)"
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# SWAN Action Balance + Source Terms

> 출처: Holthuijsen, L. H. (2007). *Waves in Oceanic and Coastal Waters*. Cambridge UP. Chapter 9 §9.3 (p.286-296) + Ch.8 §8.4 (천해 모델링).

## 1. Action Balance Equation (§9.3.1, p.288)

SWAN의 핵심 방정식:

```
∂N/∂t + ∇_x · (c_x N) + ∂(c_θ N)/∂θ + ∂(c_σ N)/∂σ
   = (S_in + S_nl4 + S_nl3 + S_ds + S_bot + S_brk) / σ
```

여기서:
- **N(x, y, σ, θ; t)** = action density = E/σ
- **σ** = intrinsic (relative) frequency (rad/s, 흐름 기준)
- **ω** = absolute frequency (관측자 기준) = σ + **k**·**U**
- **(c_x, c_y)** = action 전파 속도 (지리적, c_g·cosθ 등)
- **c_θ** = 방향 회전 (refraction + current)
- **c_σ** = 주파수 shift (수심·흐름 비정상)
- **(S_*)** = source/sink terms ((m²·Hz·rad)/s)

### 1.1 왜 N (action) 인가? — Energy E 대신

흐름이 있을 때 (waves on currents) **E는 보존되지 않지만 N은 보존** (Bretherton & Garrett 1969 정리; holthuijsen2007 본문 §7.3.5 및 참고문헌 표기 기준 — 타 문헌에선 1968로도 인용됨). 즉:
- 정수 + 흐름 없음: ∂E/∂t + ∇·(c_g E) = ΣS_E
- 흐름 + 비정상: ∂N/∂t + ∇·(c_g N) + ... = ΣS_E / σ

→ 한국 천해·하구 (조류 영향 강한 곳)에서 N-formulation 필수.

## 2. Source Terms (§9.3.2-9.3.4)

### 2.1 S_in — Generation by Wind (§9.3.2 p.289)

```
S_in(σ, θ) = A + B · E(σ, θ)
```

- A: linear growth (Phillips 1957) — 초기 시작 (~0 진폭에서 wavelet 형성)
- B: exponential growth (Miles 1957 + Janssen 1991 feedback) — feedback 메커니즘

핵심 파라미터: **U_*/c** (마찰 속도 / 위상 속도). 천해에서 c 감소 → U/c 증가 → S_in 증가 (Ch.8 §8.4.3).

**SWAN 옵션**:

GEN1/2는 포화 스펙트럼 완화 모형이다. GEN3는 여러 바람·백파 선택을 제공한다. 현재 기본 조합은 WESTH이다. (swantech PDF 59–60쪽 / 인쇄 51–52쪽의 포화 스펙트럼·완화식; swanuse PDF 65–66쪽 / 인쇄 57–58쪽 및 PDF 69쪽 / 인쇄 61쪽; `src/swanpre1.ftn:2907` `CALL INKEYW ('STA', 'WESTH')`; R2:SS-741) [10-13 전수 검증 보완]

### 2.2 S_nl4 — Quadruplet Wave–Wave Interactions (§9.3.3 p.292, Ch.8 §8.4.4 p.287-288)

4 분조 resonance:
```
f₁ + f₂ = f₃ + f₄
k₁ + k₂ = k₃ + k₄
```

심해·천해 모두 작동. 4파 상호작용은 **WAM·SWAN 등 3rd-gen 모델의 핵심** (1·2nd gen은 parameterized).

천해에서는 quadruplet이 더 강해지며 low-frequency lobe shift (Fig. 8.11 in Holthuijsen). SWAN은 DIA (Discrete Interaction Approximation, Hasselmann et al. 1985) 후 천해 보정 계수 적용:

```
S_nl4_shallow = R(k_p · h) · S_nl4_deep_DIA
```

R은 k_p·h 함수 (Herterich & Hasselmann 1980, p.288 Fig.8.12). SWAN 입력: `GEN3 ... NONLINEAR`.

### 2.3 S_nl3 — Triad Wave–Wave Interactions (§9.3.3, Ch.8 §8.4.4 p.288-289)

3 분조 resonance:
```
f₁ + f₂ = f₃
k₁ + k₂ = k₃
```

**심해에서 불가능** (linear dispersion satisfy 안 됨). **천해 (kd < 1)에서만** 가능. Biphase β = φ₁ + φ₂ − φ₃ 가 핵심 (p.289 eq. 8.4.7).

천해 진입 시 다음 발생:
- 풍파 (k_p) → 2k_p 분조에 새 peak 출현
- surf zone 멀어지면서 다시 사라짐
- 결과: spectral tail k^(−4/3) for kd < 1, k^(−5/2) for kd > 1

**SWAN 옵션**: LTA (Lumped Triad Approximation, Eldeberky 1996). 입력: `TRIAD ... LTA`.

### 2.4 S_ds — Dissipation (§9.3.4 p.294-296)

3 메커니즘 합:

#### 2.4.1 White-capping (deep + transitional)

```
S_wc(σ, θ) = -Γ · σ̃ · (k/k̃) · E(σ, θ)
```

Γ = steepness 의존 계수 (Komen 1984 또는 van der Westhuysen 2007). 진폭이 크면 무너짐 — Stokes 한계 (H/L ≈ 0.14) 근처에서 폭증.

현재 기본 조합은 WESTH이다. (swanuse PDF 69쪽 / 인쇄 61쪽; `src/swanpre1.ftn:2907` `CALL INKEYW ('STA', 'WESTH')`; R2:SS-741)

#### 2.4.2 Bottom Friction (천해)

```
S_bf(σ, θ) = -C_bf · (σ²/(g²·sinh²(kh))) · E(σ, θ)
```

C_bf 계수 (JONSWAP/Madsen/Collins):
- 현재 JONSWAP 마찰 기본 계수는 $.038\,m^2s^{-3}$이다. (swanuse PDF 74쪽 / 인쇄 66쪽; `src/swanmain.ftn:1396` `PBOT(3) = 0.038`; R2:SS-742)
- Madsen: roughness 기반
- Collins: drag coefficient 기반

`FRICTION JONSWAP 0.067`은 .067을 사용할 수 있는 입력 예이다. 현재 기본값은 .038이다. (swanuse PDF 74쪽 / 인쇄 66쪽; `src/swanmain.ftn:1396` `PBOT(3) = 0.038`; `src/swanpre1.ftn:2556–2558` `CALL IGNORE ('CON')`; `CALL INREAL('CFJON',PBOT(3),'UNC',0.)`; R2:SS-742) [10-13 전수 검증 보완]

#### 2.4.3 Depth-Induced Surf-Breaking (천해 한계)

Battjes & Janssen (1978) **statistical breaker model**:
```
S_brk(σ, θ) = D_tot / E_tot · E(σ, θ)
```

- 매뉴얼 기호는 $D_{tot}<0$이다. (swantech PDF 25쪽 / 인쇄 17쪽 원문 `Dtot < 0`; R2:SS-743)
- 소산 크기를 양수 $D_{loss}=-D_{tot}>0$로 정의하면 $S_{br}=-D_{loss}E/E_{tot}$이다. (swantech PDF 25쪽 / 인쇄 17쪽, 식 (2.31); R2:SS-743) [10-13 전수 검증 보완]
- 쇄파 부분 Q_b: H_rms이 H_max로 truncated 가정 (Rayleigh)
- H_max = γ · D (D = set-up 포함 총수심; **SWAN 기본 γ = 0.73** — holthuijsen2007 §9.3.4. ※0.78 은 천해 개별파 한계비(H_b/h_b, Weggel 문맥)로 별개 — 혼동 주의)

SWAN 입력: `BREAKING CONSTANT 1.0 0.73` (α=1.0, γ=0.73).

#### 2.4.4 Reflection·Transmission·Absorption (구조물 인근)

방파제·해벽 등 명시적 obstacle:
```
S_obs(σ, θ) = ...     (구조물별, refl·trans·absorb 계수)
```

SWAN 입력: `OBSTACLE TRANS ... REFL ...`.

## 3. 추가 — Wave-Induced Set-Up (§9.4 p.296)

Radiation stress (`concepts/waves/02-theory.md` §6.6) 결과로 평균 해면 상승:
```
gh · d(η̄)/dx + (1/ρ) dS_xx/dx = 0
```

쇄파 영역에서 dS_xx/dx ≠ 0 → η̄ 변동. SWAN 출력 옵션: `SETUP`.

## 4. 수치 기법 (§9.5)

### 4.1 Propagation (§9.5.2)

- **Implicit upwind scheme** — SWAN 특징 (WW3는 explicit)
- BSBT (Backward Space Backward Time) 또는 S&L (Stelling-Leendertse) 옵션
- **장점**: 안정도 좋음, 큰 timestep 가능 (Courant 제약 완화)
- **단점**: numerical diffusion (격자 거칠수록 심함)

### 4.2 Source Terms (§9.5.3)

- Positive (S_in): explicit
- Negative (S_ds): semi-implicit (안정도)
- Numerical stability: limit on growth/decay per iteration

### 4.3 Boundary Conditions

- **Open boundary**: 외부 spectrum 입력 (NESTOUT or specfile)
- **Closed boundary**: zero spectrum
- **Periodic** (대양 nesting): wrap-around

## 5. SWAN 입력 카드 — 표준 시퀀스

```
$ Mode and time control
MODE NONSTATIONARY TWODIMENSIONAL
COMPUTE STAT          ! 또는 NONSTAT
TIME 20250101.000000 20251231.000000 1 HR

$ Coordinates and grid
COORDINATES SPHERICAL
CGRID REGULAR 124.4500 37.4000 0 1.5 0.9 300 180 CIRCLE 36 0.04 1.0 31

$ Bottom topography
INPGRID BOTTOM REGULAR 124.4500 37.4000 0 300 180 0.005 0.005
READINP BOTTOM 1.0 'depth.dat' 1 0 FREE

$ Wind input
INPGRID WIND REGULAR 124.4500 37.4000 0 300 180 0.005 0.005
READINP WIND 1.0 'wind.dat' 1 0 FREE

$ Boundary
BOUNDSPEC SIDE W CONSTANT FILE 'boundary.spec' 1

$ Physics
GEN3 JANSSEN
FRICTION JONSWAP 0.067
BREAKING CONSTANT 1.0 0.73
TRIAD
QUAD

$ Numerical
NUMERIC ACCUR 0.02 0.02 0.02 95 STAT 50

$ Output
POINTS 'STATIONS' 'stations.txt'
TABLE 'STATIONS' HEAD 'output.tab' HSIGN TPS DIR DSPR WIND DEP
BLOCK 'COMPGRID' NOHEAD 'output.mat' HSIGN TPS DIR DEP

COMPUTE
STOP
```

> 정확한 입력은 SWAN User Manual 본문 (별도 다운로드) — 본 노트는 Holthuijsen Ch.9 algorithmic 인용 중심.

## 6. 보강

- SWAN Technical Documentation (Booij·Ris·Holthuijsen 1999 + 후속) 발췌
- SWAN User Manual 입력 카드 전체 정리 → `models/SWAN/source-analysis/swan-command-file-reference.md`

## 7. 연결

- `concepts/waves/04-code-and-tools.md` §2 — SWAN 개관
- `concepts/waves/06-model-application.md` §3 — SWAN canonical
- [`textbook/notes/waves-holthuijsen-toc.md`](../../../textbook/notes/waves-holthuijsen-toc.md) §Ch.9
- 외부:
  - Holthuijsen (2007) Ch.9
  - Booij, Ris, Holthuijsen (1999) seminal paper
  - [SWAN 공식 자료](../web-refs/swan-official-resources.md)

## 문서와 코드 차이 (10-13 대조)

문서 판: SWAN Cycle III 41.51 매뉴얼; 웹 수정 이력·패치. 코드 판: VERNUM 41.51, 원본 저장소 HEAD 43e9bbb 2026-07-13 patch B.

확정 결론과 원문 인용: [R2](../../../_staging/recovery/compare/swan-theory-sources-vs-code.md#5-차이-결론). 아래 결론 문장은 R2의 AI 해석이다. 기존 노트 줄 번호는 반영 전 HEAD 기준이다. [10-13 전수 검증 보완]

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| R2:SS-741 | 노트 · manual-notes/swan-action-balance.md:61 | 기존 노트 `GEN1`: Komen et al. (1984); `GEN3`: Janssen (1991) — 표준; `WCAP KOMEN` (기본). swanuse PDF 65–66쪽 / 인쇄 57–58쪽 및 PDF 69쪽 / 인쇄 61쪽. | `src/swanpre1.ftn:2907` `CALL INKEYW ('STA', 'WESTH')` | B | 해석: GEN1/2는 포화 스펙트럼 완화 모형이다. GEN3는 여러 바람·백파 선택을 제공한다. 현재 기본 조합은 WESTH이다. |
| R2:SS-742 | 노트 · manual-notes/swan-action-balance.md:121 | 기존 노트 `C_bf = 0.067 (sandy bottom, 표준)`. swanuse PDF 74쪽 / 인쇄 66쪽은 JONSWAP 기본값 .038을 명시한다. | `src/swanmain.ftn:1396` `PBOT(3) = 0.038` | B | 해석: 현재 JONSWAP 마찰 기본 계수는 $.038\,m^2s^{-3}$이다. .067을 사용할 수 있는 입력 예와 현재 기본값을 구별한다. |
| R2:SS-743 | 노트 · manual-notes/swan-action-balance.md:131 | 기존 노트 `S_brk(σ, θ) = -D_tot / E_tot · E(σ, θ)`. swantech PDF 25쪽 / 인쇄 17쪽 원문 `Dtot < 0`. | `src/swancom2.ftn:2114` `DBLE(QB) * DBLE(FMEAN) / BB`<br>`src/swancom2.ftn:2120` `SURFA0 = SbrD`<br>`src/swancom2.ftn:2121` `SURFA1 = WS + SbrD`<br>`src/swancom2.ftn:2188` `IMATDA(ID,IS) = IMATDA(ID,IS) + REAL(SURFA1)`<br>`src/swancom2.ftn:2190` `IMATRA(ID,IS) = IMATRA(ID,IS) + REAL(DIS0)` | F | 해석: 소산 크기를 양수 $D_{loss}=-D_{tot}>0$로 정의하면 $S_{br}=-D_{loss}E/E_{tot}$이다. 매뉴얼 기호 $D_{tot}<0$를 유지하면 앞의 음수를 제거한다. |
