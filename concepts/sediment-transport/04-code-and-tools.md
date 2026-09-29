---
title: "표사이동 — 04 코드와 도구 (EFDC SED · Delft3D-SED · CSTMS · XBeach SED)"
topic: sediment-transport
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "AI cross-reference: textbook 자료 + WebSearch 공식 모델 페이지 + Soulsby 1997 implementation guidance. §10.1 full PDF 격상 (2026-09-28): arXiv 2005.00920v3·2010.06167v1·2603.27604v1·1804.04541v1 전문 판독(서브에이전트 판독 + 핵심 인용 원문 grep 대조). ★ swash 분산 해상 과장·φ 사례별 수동 설정·DMD 는 수조/저장률·copula 대상은 SPM 으로 abstract 기반 요약 4건 모두 정정."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-21
verification_by: "Claude Opus 4.7 (1M context) — cross-ref"
verification_date: 2026-05-21
---

# 표사이동 — 04 코드와 도구

## 1. 모델 비교

| 모델 | 종류 | 라이선스 | 표사 모듈 | 비고 |
|---|---|---|---|---|
| **EFDC SED** | hydrodynamic + sediment (3D) | open source (DSI, USEPA 등) | 자체 모듈 | USEPA 수질·침퇴적 |
| **Delft3D-SED** | hydrodynamic + sediment | GPL-3.0 | D3D-4 또는 FM | 표준 (Deltares) |
| **MIKE 21/3 ST · MT** | 상용 | 상용 (DHI) | ST = Sand Transport(비점착성), MT = Mud Transport(점착성) — **별개 모듈** (§6) | — |
| **XBeach sedtrans** | 폭풍 침식 | GPL-3.0 | non-cohesive · 비점착성 | 폭풍 시뮬 |
| **CSTMS / COAWST** | combined ocean·atm·wave·sed | open source | ROMS + SWAN + CSTMS | 학술 |
| **TELEMAC-MASCARET (SISYPHE → GAIA)** | unstructured | open source | GAIA 가 SISYPHE 를 대체하는 표사·지형 모듈 (§6.1) | — |

## 2. EFDC SED

> **Canonical**: [`models/EFDC/`](../../models/EFDC/) (source-analysis 30 verified: [[../../models/EFDC/source-analysis/sediment/efdc_sediment]]·[[../../models/EFDC/source-analysis/sediment/efdc_sedzlj]]) + `efdc-sed-trans-2003` source (`textbook/md/86899804-EFDC-Theory-Tech-Aspects-of-Sed-Trans-2003-05.md`).

### 2.1 EFDC 표사이동 이론 — Tech Aspects (2003)

본 PDF는 EFDC의 표사이동 구현 이론서. 핵심:
- **Multi-class** sediment (비점착성 + 점착성 동시)
- **Bedload + Suspended** 양쪽 추적
- 자체 **bed layer** 다층 추적 (수직 격자 + bed 다층)
- Rouse profile (`02-theory.md` §3) 기반 부유 농도 평형

### 2.2 입력 카드 (EFDC)

- `efdc.inp`:
  - `NSED` (cohesive 점착성 sediment class 수)
  - `NSND` (non-cohesive sand class 수)
  - `RSED1NS` (각 class의 초기 부유 농도)
  - `SDEN(NS)` (각 class 입경)
  - `TAUR`, `TAUC` (재부유 임계, 침전 임계)
  - `RKTR`, `RKAGG` (재부유 속도, aggregation 속도 점착성)
- `aser.inp` / `wser.inp`: 외력 시계열
- `bed_layer.inp`: 초기 bed 다층 구성

→ 정확한 카드는 [`models/EFDC/manual-notes/`](../../models/EFDC/manual-notes/) (작성 예정).

### 2.3 출력

- 각 sediment class 부유 농도 (mg/L) 3D 격자
- Bed 표고 변화 (m) 시계열
- Bed 입자 분포 변화 (multi-layer)
- 침전·재부유 flux

### 2.4 한국 적용 사례

> 한국 항만 EFDC SED 적용 사례는 바이블 검증(객관 데이터) 후 `experience/` 에 카테고리화 — 본 canonical 미수록. citation_status: source-needed.

## 3. Delft3D-SED

### 3.1 D3D-4 SED

- FLOW + SED 모듈 연결
- 입력 파일: `.mor`, `.sed` (sediment fraction, bed composition)
- non-cohesive: van Rijn (1984·2007) + bedload 별도
- cohesive: Partheniades-Krone (재부유) + settling

### 3.2 Delft3D FM (Flexible Mesh)

- D-Morphology 모듈
- Sand + mud transport 통합

→ [`models/Delft3D/`](../../models/Delft3D/) (source-analysis 38 verified: [[../../models/Delft3D/source-analysis/delft3d_sediment_transport_formulae]]·[[../../models/Delft3D/source-analysis/delft3d_sediment_morphology]]).

## 4. CSTMS / COAWST

- Community Sediment Transport Modeling System
- ROMS (ocean) + SWAN (wave) + CSTMS (sediment) coupling
- 공식 GitHub: [https://github.com/DOI-USGS/COAWST](https://github.com/DOI-USGS/COAWST) (확인 필요)

## 5. XBeach Sediment

### 5.1 모드

- `morphology = 1`: bed update 활성
- Bedload (Soulsby-van Rijn 식)
- Suspended (advection-diffusion + settling)
- Avalanching (사구 붕괴 dune front)

### 5.2 적용

- 폭풍 침식·붕괴 시뮬 (수일 단위)
- Beach-dune system: erosion·breaching
- 한국 적용 사례 (서해 폭풍 침식): 별도 보강

## 6. MIKE 21/3 ST·MT (상용, DHI)

- **ST (Sand Transport) 는 비점착성(모래) 전용** — DHI 모듈 설명서: *"The MIKE 21 & MIKE 3 Flow Model FM, Sand Transport Module (ST) is the module for the calculation of sediment transport capacity and related initial rates of bed level changes for noncohesive sediment (sand) due to currents or combined waves-currents."* ([DHI, Sand Transport Module short description](https://www.dhigroup.com/upload/dhisoftwarearchive/shortdescriptions/marine/SandTransportModuleST.pdf), 2026-09-28 확인)
- **점착성(펄)은 별도 MT (Mud Transport) 모듈** — *"a specialised software module designed for simulating the transport of fine-grained sediments, particularly mud, in coastal and marine environments"* ([DHI, MIKE 21/3 Mud Transport](https://www.dhigroup.com/technologies/mikepoweredbydhi/mike-21-3-mud-transport)).
- ★정정 (2026-09-29 L4 감사): 구판의 "비점착성 + 점착성 통합", "한국 항만 설계 사용 빈도 높음" 은 출처가 없어 뺐다 — 앞의 것은 모듈 구분과도 맞지 않는다.

### 6.1 TELEMAC-MASCARET GAIA

GAIA 는 TELEMAC-MASCARET 의 표사·하상변동 모듈로, 기존 SISYPHE 를 바탕으로 만들어 이를 대체한다 — 여러 입경 분급의 비점착성·점착성 표사를 함께 다룬다
("GAIA – a unified framework for sediment transport and bed evolution in rivers, coastal seas and transitional waters in the TELEMAC-MASCARET modelling system", *Environmental Modelling & Software*, doi:10.1016/j.envsoft.2022.105544 — 초록 기준, 전문 미판독 `source-needed`).
구판 표의 "유럽 표준" 은 출처가 없어 뺐다.

## 7. Python 도구

| 도구 | 기능 | 출처 |
|---|---|---|
| **pyDGS** | 이미지 기반 입도 분포 추정 (Digital Grain Size) | [github.com/DigitalGrainSize/pyDGS](https://github.com/DigitalGrainSize/pyDGS) |
| **GrainSizeTools** | 입도 분포 통계·정상상태 입도 해석 | [github.com/marcoalopez/GrainSizeTools](https://github.com/marcoalopez/GrainSizeTools) |
| Soulsby formulae (NumPy) | `02-theory.md`·`03-analysis-methods.md` 식 직접 구현 | 자체 |

## 8. 도구 선택 가이드

| 상황 | 권장 |
|---|---|
| 침퇴적 + 수질 결합 (3D) | **EFDC SED** + manual + `efdc-sed-trans-2003` |
| 단순 항만 (단기 설계) | **MIKE 21 ST** 또는 **Delft3D-SED** |
| 폭풍 침식 시뮬 | **XBeach** sediment + morphology |
| 학술 ocean-atm-wave-sed coupling | **CSTMS / COAWST** |
| 평형 단면 검토 (Dean profile) | 수동 (`02-theory.md` §5 식) |
| 정점별 d_{50} 분석 | scipy, scikit (sieve curve fit) |

## 9. SWAN ↔ EFDC coupling (프로그램 간 연관성)

- SWAN 출력 (radiation stress, H_s, T_p) → EFDC SED 입력 (wave forcing)
- KHOA 수치조류도 (`tides-khoa-cross-verification.md` §5) → EFDC 외해 흐름 boundary 조건
- wave + current 조합 시 합성 bed shear stress 로 재부유 임계 평가

## 10. 보강

- EFDC 표사이동 source-code (`models/EFDC/source-analysis/sediment.md`) 발췌
- Delft3D-SED 입력 카드 정리
- CSTMS Python interface

### 10.1 연구 문헌 4편 ✅ verified (full PDF 판독 2026-09-28)

네 편 모두 **정량 검증 지표가 약하다** — 공통 결론: 방법 아이디어로 인용하고 수치는 옮기지 말 것.

#### 10.1.1 GN 분산파 + bed-load DG — Kazhyken·Videman·Dawson, arXiv:[2005.00920](https://arxiv.org/abs/2005.00920)v3 (2020-10-04)

Bonneton 형 단일모수 Green-Naghdi(GN) + Exner 를 DG(p = 1)로 풀고, Strang 분할 $S(\Delta t)=S_1(\Delta t/2)S_2(\Delta t)S_1(\Delta t/2)$ 로
분산 보정 $S_2$ 를 떼어 **쇄파 셀에서는 $S_2=1$(= NSWE)** 로 끈다. 쇄파 감지는 Krivodonova 불연속 지시자(Duran & Marche).
bed-load 는 **Grass, $m=3$, $A=4.75\cdot10^{-3}$** 만 쓰고 Exner 에 공극률·임계전단·경사항이 없다.[^kz1]
- ★ **"swash zone 까지 분산효과 해상" 은 과장** — 초록은 *"sufficient accuracy up to swash zones"* 라 쓰지만 본문은
  *"neither model is able to accurately capture the water motion in the swash zone"*(Sumer 2011 1:14 경사 solitary 파),
  run-down 도 못 잡는다고 적는다. 분산 보정은 wet/dry 전선을 반사벽으로 두고, 쇄파 셀에서는 꺼진다.[^kz1]
- 재현 불가 설정: 쇄파 임계값(*"typically O(1)"* 이라고만), GN 모수 α(§4.2–4.5), 최소수심 $h_0$ 미기재.
- 검증: 실측 대조 3건(Dodd 쇄파 solitary·Dingemans bar·Sumer 이동상)이 **전부 육안 비교, 오차 지표 없음**. 이동상 검증은 Sumer 1건.
  2D 비구조 코드이나 검증 격자는 전부 1셀 폭 띠(사실상 1D). Faro-Olhão 조석 입구 사례는 **관측 없이 GN vs NSWE 비교**뿐이다.
- 코드: `dgswemv2` (UT-CHG). **본문은 ADCIRC 를 언급하지 않는다**(Dawson 은 저자 중 1인일 뿐).

#### 10.1.2 GN + 부유사·이동상(SHSM) DG — 同 저자, arXiv:[2010.06167](https://arxiv.org/abs/2010.06167)v1 (2020-10-11)

위 틀에 부유사 농도 $hc$, 침식-퇴적 교환 $E-D$(질량·운동량·지반), 혼합밀도 압력항을 더한 SHSM. 침식 $E=\varphi(\theta-\theta_c)|u|h$,
퇴적은 Cao et al. 형 $D=\omega_o C_a(1-C_a)^2$.[^kz2]
- ★ **"보정"의 실체는 침식계수 φ 하나를 사례마다 손으로 정한 것** — φ = 0.015 · 4.0(Louvain) · 2.5(Taipei) · 0.35 · 0.05 · 0.35,
  두 자릿수 이상 범위이고 목적함수·절차가 없다. 침강속도 $\omega_o$ 값은 어느 사례에도 적혀 있지 않다.[^kz2]
- ★ **분산(GN)을 실제로 쓴 사례는 마지막 하나** — 댐붕괴 4 사례는 *"dispersive wave effects are negligible; therefore, S2 = 1"*.
  이동상+GN 증거는 Young et al. (2010) solitary 파 3회 1건이고, bed-load(Grass $A=2\cdot10^{-4}$)를 넣은 경우와 안 넣은 경우가
  **둘 다 "good agreement"** 로 판정돼 bed-load 기여가 구분되지 않는다. 오차 지표 없음.
- 저자 단서: *"a close calibration for the empirical models' parameters may be required"*, swash 에서 *"less precise in resolving water waves"*.
- 이 논문은 2005.00920 을 인용하지 않는다(동일 코드·동일 저자라 "확장" 은 본 노트의 해석).

#### 10.1.3 bedform DMD — Mustavee·Singh·Agarwal, arXiv:[2603.27604](https://arxiv.org/abs/2603.27604)v1 (2026-03-29, 6p)

- ★ **"하천" 이 아니라 실험수조** — SAFL Main Channel(85 m × 2.75 m, 순환식) 레이저 스캔 12 m × 0.5 m, 9.71 시간·약 2 분 간격 300 장.
  유량·수심·입경은 본문에 없다(선행 논문 인용).[^md]
- 방법: 표준(exact) DMD 한 번 — 제목의 "time-varying" 은 창(window) DMD 가 아니다. 지반 변화율 모드를 적분 Exner 식에 넣어
  $q^{net}_{s,x}(y,t) := q_{s,x}(x_{max})-q_{s,x}(x_{min})$ 를 구한다 — **패치 양끝 flux 차 = 저장률이지 수송률 $q_s$ 자체가 아니다**
  (본 노트 판단). 모드 celerity(파장×DMD 주파수)는 모드 정렬에만 쓴다.
- 결과: *"just the 7 slowest modes account for 50.9% of the total transport"*. **실측 flux 와의 대조는 없다** — 문헌의 $q_s(f)\propto f^{-0.6}$ 과
  정성 비교만. 복원 상관 0.9 는 full-rank DMD 라 보간에 가깝다.
- ★ 최빈 주기대 *"3.90 − 6 min (N = 47)"* 의 하단 3.90 분은 스냅샷 간격(9.71 h/300 ≈ 1.94 분)의 **나이퀴스트 주기(≈ 3.9 분)** 와 같다 — 분해능 한계대(본 노트 계산).

#### 10.1.4 copula-Morris 민감도 — Ţene·Stuparu·Kurowicka·El Serafy, arXiv:[1804.04541](https://arxiv.org/abs/1804.04541)v1 (2018, EMS 투고 preprint)

- ★ **표사(모래) 가 아니라 미세 부유사(SPM)** — Delft3D-WAQ(DELWAQ 4.5208) 남북해 모델, 무기 입자 3분급(1–40 µm),
  van Kessel (2011) 2층 bed buffer(S1 fluff·S2 sand buffer) 재부유·침강. 출력 = MERIS 위성 표층 SPM 과의 평균절대오차.[^tn]
- 14 모수 중 7쌍을 전문가 판단으로 **완전 순위상관(±1)** 으로 묶고 Gaussian copula + LHSD 로 표본(p = 4, r = 10, 80 run).
  ±1 이면 각 쌍이 한 인자처럼 움직이므로 사실상 **7인자 grouped Morris** 다 — 80 = (7+1) × 10 (본 노트 계산).
- 결과: copula 방식 1위 TauShields–FactResPup(μ* 2.857), 독립 가정 방식 1위 VResIM1(μ* 5.002)이고 FactResPup 는 독립 방식 꼴찌(0.749).
  "물리적으로 더 일관" 판단 근거는 **전문가 기대와의 부합뿐** — test function·Sobol 교차검증·신뢰구간 없음.
- 실무 교훈(본 노트 해석): 서로 상쇄하는 모수 쌍(예: VRes–TaucRS1)은 screening 전에 묶어야 개별 효과가 과대평가되지 않는다.

[^kz1]: Kazhyken, Videman & Dawson, arXiv:2005.00920v3 — Grass *"m = 3"*, *"A = 4.75 · 10−3"* (§4.4); 초록·결론 *"with sufficient accuracy up to swash zones"*; §4.4 *"neither model is able to accurately capture the water motion in the swash zone as evidenced by the free surface elevation measurements at the onshore section 8"*; 결론 *"the developed model is limited to bed-load transport"*.
[^kz2]: 同 저자, arXiv:2010.06167v1 — §4 *"calibration parameter is set as φ = 0.015"*, *"φ, is set as 4.0 for the Louvain experiment, and 2.5 for the Taipei experiment"*, *"φ, to 0.35"*, *"entrainment rate model φ = 0.05"*, §4.5 *"φ, is set to 0.35; and the Grass model with A = 2 · 10−4"*; 댐붕괴 사례 *"dispersive wave effects are negligible; therefore, S2 = 1 in the simulations. The last example uses the full"* model; §4.5 *"less precise in resolving water waves in the swash zone"*; §5 *"a close calibration for the empirical models' parameters may be required"*.
[^md]: Mustavee, Singh & Agarwal, arXiv:2603.27604v1 [eess.SY] — 데이터 *"9.71 hours"*, *"98% of the data"*; §III-B *"The range 3.90 − 6 min contains the majority of the periods (N = 47)"*, *"12 eigenvalues inside the unit circle"*, *"The correlation score is 0.9"*; §V *"just the 7 slowest modes account for 50.9% of the total transport"*, *"qs (f ) ∝ f −0.6 [1], [2]"*.
[^tn]: Ţene, Stuparu, Kurowicka & El Serafy, arXiv:1804.04541v1 — *"Preprint submitted to Environmental Modelling & Software"*; DELWAQ 4.5208; *"a total number of 80 simulations were performed"*; Table 2 *"Completely rank-correlated pairs of parameters"*; Table 3·4 μ* 2.857 (TauShields–FactResPup), 5.002 (VResIM1), 0.749 (FactResPup); §6 *"the results of the copula-based sensitivity analysis have a better correspondence with the expected system behavior."*

## 11. 연결

- `01`-`03` — 도메인 지식
- `05-examples.md` — 한국 사례 (작성 예정)
- `06-model-application.md` — 모델 적용 워크플로
- 외부:
  - **EFDC**: [https://www.epa.gov/exposure-assessment-models/efdc](https://www.epa.gov/exposure-assessment-models/efdc)
  - **Delft3D**: [https://oss.deltares.nl/web/delft3d](https://oss.deltares.nl/web/delft3d)
  - **XBeach**: [https://xbeach.readthedocs.io/](https://xbeach.readthedocs.io/)
  - **COAWST**: NOAA/USGS open source
