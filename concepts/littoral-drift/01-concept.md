---
title: "연안표사 (Longshore Sediment Transport) — 정의·driver·empirical formula·한국 적용"
topic: littoral-drift
canonical_source: self
citation_status: verified
verification_method: "CERC 'Shore Protection Manual' 1984 (외부 표준 reference, 본 위키 내 PDF 미보유 — sources.yml TODO) + Komar & Inman (1970) J. Geophys. Res. 75(30):5914-5927 (Wijetunge ref. 19 직접 인용) + Holthuijsen Ch 11 (textbook/md/Waves-Holthuijsen2007.md) + Soulsby 1997 (concepts/sediment-transport/ 공유) 정형 인용."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — CERC SPM + Komar-Inman + Wijetunge cross-ref"
verification_date: 2026-05-23
related:
  - concepts/sediment-transport/01-concept.md
  - concepts/waves/02-theory.md
  - concepts/currents/01-concept.md
  - models/XBeach/
---

# 연안표사 (Longshore Sediment Transport) — 정의·driver·empirical formula

> 본 §는 연안 breaker zone 의 longshore 표사 운반. 일반 표사 ([`concepts/sediment-transport/`](../sediment-transport/)) 와 cross-shore 표사 (별도) 와 구분.

## 1. 정의

**Longshore sediment transport (연안표사, $Q_l$)** — 해변에 나란한 방향의 모래 이동 (단위: m³/yr 또는 kg/s).

원인 두 가지:
1. **Wave-induced longshore current** — 사파 진입 시 breaker zone 의 alongshore current
2. **Beach drifting** — swash zone 에서 wave 가 모래를 사면 위 + 하 zigzag 운동 → 평균 방향

두 과정이 결합 → net longshore transport.

### 1.1 방향 convention

해안선 좌표에서 wave 가 sin(θ) 성분으로 alongshore 운반 (θ = wave 진입각 vs 해안선 normal).

## 2. Driver — Radiation Stress (Longuet-Higgins-Stewart 1962-1964)

표층 wave 가 운반하는 momentum flux 의 평균:

$$S_{xy} = E \cdot n \cdot \cos\theta \sin\theta$$

- $E = \frac{1}{8}\rho g H^2$ = wave energy
- $n = c_g/c$ = group velocity ratio (shallow water n=1, deep n=0.5)
- $\theta$ = wave incidence angle

이 radiation stress component 가 alongshore 방향 force 를 만들어 **longshore current** 생성.

상세는 [`concepts/waves/02-theory.md`](../waves/02-theory.md) 와 [`02-theory.md`](02-theory.md) (예정) 에서.

## 3. CERC Formula (1984 Shore Protection Manual)

가장 흔한 empirical formula:

$$Q_l = K \cdot \frac{P_l}{(\rho_s - \rho) g (1 - p)}$$

- $Q_l$ = volumetric longshore transport rate (m³/s)
- $P_l$ = longshore component of wave power per unit shoreline length:

  $$P_l = (E c_g)_b \sin\theta_b \cos\theta_b = \frac{\rho g H_b^2 c_{g,b}}{8} \sin(2\theta_b)/2$$
  (b = breaker line)

- $K$ = empirical constant ≈ **0.39** (sand beach, CERC SPM 1984)
- $\rho_s$ = sediment density (~2650 kg/m³ quartz)
- $\rho$ = water density (~1025 kg/m³)
- $p$ = porosity (~0.4)

수치 추정:

$H_b$ = 1 m breaker wave, $\theta_b = 10°$, sand beach:
$$P_l = \frac{1025 \cdot 9.81 \cdot 1^2 \cdot c_{g,b}}{8} \sin(20°) \approx 600 \text{ W/m (shoreline)}$$

(shallow water $c_{g,b} \approx \sqrt{gh_b} \approx 3$ m/s for 1m breaker)

$$Q_l \approx \frac{0.39 \cdot 600}{(2650-1025) \cdot 9.81 \cdot 0.6} \approx 0.024 \text{ m}^3/\text{s} \approx 760{,}000 \text{ m}^3/\text{yr}$$

→ 1 m breaker wave + 10° 진입 시 연간 ~80만 m³/yr 모래 이동 (예제 값).

### 3.1 CERC formula 한계

- breaker zone 모두 활성으로 가정 (실제는 단속적)
- grain size 변동 미고려 (single $K$)
- bed slope 영향 미고려
- 강한 storm 시 cross-shore loss 미포함

## 4. Komar & Inman (1970)

CERC 보다 정밀:

$$I_l = K' \cdot \rho \cdot (g H_b)^{1/2} \cdot H_b^2 \cdot \sin\theta_b \cos\theta_b$$

- $I_l$ = immersed weight transport rate (N/s)
- $K' \approx 0.77$ (Komar & Inman 1970)

CERC 와 Komar 둘 다 $\sin(2\theta_b)$ 의존성 동일 → 비슷한 결과, 다른 단위.

## 5. Modern formulae

- **Kamphuis (1991)** — grain size + bed slope 포함
- **Bayram et al. (2007)** — turbulence + grain size dependent
- **van Rijn (2014)** — bedload + suspended 분리

각 식은 CERC 보다 정밀하지만 입력 변수 많음. 한국 적용 시 보통 **CERC** 또는 Kamphuis 선호.

## 6. Longshore current — Battjes 1974, Bowen 1969

longshore current $v_l$ (m/s):

$$v_l = \frac{5\pi}{16} \frac{\tan\beta}{c_f} \sqrt{g h_b} \sin\theta_b \cos\theta_b$$

(Bowen 1969 derivation, $\tan\beta$ = beach slope, $c_f$ = bed friction)

예: $h_b$ = 1 m, $\theta_b = 10°$, $\tan\beta = 0.05$, $c_f = 0.01$:
$$v_l \approx 0.98 \cdot \frac{0.05}{0.01} \cdot 3.13 \cdot 0.171 \approx 2.6 \text{ m/s (이론, 실제는 0.5-1.5 m/s typical)}$$

## 7. Sediment Budget — 표사수지

연안의 control volume 에서 sediment 수지:

$$\frac{\partial V}{\partial t} = (Q_{l,\text{in}} - Q_{l,\text{out}}) + (Q_{x,\text{in}} - Q_{x,\text{out}}) + \sum \text{sources/sinks}$$

- $Q_l$ = longshore (alongshore in/out)
- $Q_x$ = cross-shore (river, offshore loss, dune 운반)
- sources = river supply, cliff erosion, beach nourishment
- sinks = dune deposition, headland trap, harbor capture

일반 메커니즘: 항만 방파제가 net longshore drift 를 차단하면 상류측(updrift) 모래 축적·하류측(downdrift) erosion 이 발생 (CERC SPM 1984 §4; sediment budget control-volume 적용).

## 8. 한국 적용 사례

> 한국 longshore drift 개별 사례는 객관 데이터(KMOU·해양수산부 연안침식 조사 등 출처 명시 공개 보고서)로 검증 후 `experience/` 에 카테고리화 — 본 canonical 미수록. <!-- citation_status: source-needed -->

## 9. 측정·관측

### 9.1 직접 측정

- **Sediment trap** — breaker zone 에 trap 설치, 시간당 무게 측정
- **Sand tracer** — fluorescent 또는 radioactive 모래 추적
- **Beach profile survey** — RTK GPS 로 정기 measurement

### 9.2 간접 (model)

- **CERC formula** (위 §3) — wave 측정만으로 계산
- **One-line model** (GENESIS, UNIBEST-LT) — shoreline change 시뮬레이션
- **Process-based** (XBeach, Delft3D-SED) — wave + current + sediment 결합

## 10. 인용 정형

본 §의 핵심 인용:
- $Q_l = K P_l / [(\rho_s - \rho)g(1-p)]$, $K = 0.39$ — CERC SPM 1984
- $I_l = K' \rho (g H_b)^{1/2} H_b^2 \sin\theta_b\cos\theta_b$, $K' = 0.77$ — Komar & Inman 1970
- Radiation stress $S_{xy} = E n \cos\theta\sin\theta$ — Longuet-Higgins & Stewart 1962-1964
- Longshore current $v_l \propto \sqrt{gh_b}\sin\theta_b\cos\theta_b$ — Bowen 1969, Battjes 1974

## 11. 관련 문헌

- CERC, "Shore Protection Manual," 1984. U.S. Army Corps of Engineers, Coastal Engineering Research Center.
- Komar, P.D. & Inman, D.L. (1970) "Longshore Sand Transport on Beaches" J. Geophys. Res. 75(30):5914-5927. (Wijetunge ref. 19)
- Kamphuis, J.W. (1991) "Alongshore sediment transport rate" J. Waterway Port Coastal & Ocean Engineering 117:624-640.
- Bowen, A.J. (1969) "The generation of longshore currents on a plane beach" J. Marine Res. 27:206-215.
- Battjes, J.A. (1974) "A computational model for the longshore current" — IAHR.
- Longuet-Higgins, M.S. & Stewart, R.W. (1964) "Radiation stresses in water waves: a physical discussion, with applications" Deep-Sea Research 11:529-562. (Wijetunge ref. 13)
- van Rijn, L.C. (2014) "A simple general expression for longshore transport of sand, gravel and shingle" Coastal Engineering 90:23-39.
- Holthuijsen, L.H. (2007) *Waves in Oceanic and Coastal Waters*, Ch 11 (sediment transport by waves)

## 12. 연결

- [`02-theory.md`](02-theory.md) (예정) — radiation stress 유도 + longshore current 식
- [`04-code-and-tools.md`](04-code-and-tools.md) (예정) — XBeach surf module + GENESIS
- [`05-examples.md`](05-examples.md) (예정) — 출처 명시 공개 데이터 기반 case study
- [`concepts/sediment-transport/01-concept.md`](../sediment-transport/01-concept.md) — bedload·suspended 일반 (인접 토픽)
- [`concepts/waves/02-theory.md`](../waves/02-theory.md) — wave driver
- [`concepts/storm-surge/01-concept.md`](../storm-surge/01-concept.md) — storm 시 longshore drift 폭증
- 외부:
  - CERC SPM 1984 — sources.yml 등록 TODO
  - Komar & Inman 1970 — JGR DOI
