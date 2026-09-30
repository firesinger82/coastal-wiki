---
title: "SST 이론 — 해양 열수지·열팽창·해류 forcing (Stewart §5)"
topic: sst
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "Stewart 'Introduction to Physical Oceanography' Chapter 5 (Oceanic Heat Budget) + Chapter 6 (Temperature, Salinity, Density) 직접 인용. equation 번호·페이지 (eq 5.1-5.6, eq 6.x) Stewart textbook (textbook/md/stewart_textbook.md) 와 1:1 대응."
note_author: "Claude Opus 4.7 (1M context)"
note_date: 2026-05-23
verification_by: "Claude Opus 4.7 (1M context) — Stewart 본문 직접 인용 + 한국 SST cross-validation"
verification_date: 2026-05-23
related:
  - concepts/sst/01-concept.md
  - experience/khoa-sst-warming-trend.md (§4 열팽창 기여 계산)
  - experience/khoa-sst-global-crosscheck.md (§5 SLR cross-check)
  - experience/khoa-annual-climate-trend.md
---

# SST 이론 — 해양 열수지·열팽창·해류 forcing

> Stewart 'Introduction to Physical Oceanography' §5 Oceanic Heat Budget + §6 Temperature/Salinity/Density 직접 인용.

## 1. 해양 표층 열수지 (Stewart eq. 5.1)

표층에서의 열 보존:

$$Q = Q_{SW} + Q_{LW} + Q_S + Q_L + Q_V$$

(Stewart eq. 5.1, p.52)

| 항 | 의미 | 부호 관례 |
|---|---|---|
| $Q_{SW}$ | 입사 단파복사 (insolation) | + (해양으로) |
| $Q_{LW}$ | 순 장파복사 (net infrared) | − (대기로) |
| $Q_S$ | sensible heat flux (전도) | − (보통) |
| $Q_L$ | latent heat flux (증발) | − (보통) |
| $Q_V$ | advection (해류 운송) | ± |

한국 연안의 항별 계절 크기(W/m²)는 지역·기간이 명시된 관측·재분석 출처가 필요하다 (source-needed).

총합 $Q$ 의 부호:
- 여름·열대: Q > 0 → 표층 가열
- 겨울·중위도: Q < 0 → 표층 냉각
- **전 지구·다년 평균**: Q ≈ 0 (해양 전체로는 평형)

## 2. 수온 변화와 비열 (Stewart eq. 5.2-5.3)

질량 $m$ 인 수괴의 온도 변화 $\Delta T$ 에 필요한 에너지:

$$\Delta E = C_p \cdot m \cdot \Delta T \quad (\text{eq. 5.2})$$

$C_p$ = 해수 비열 (specific heat at constant pressure):

$$C_p \approx 4.0 \times 10^3 \ \text{J} \cdot \text{kg}^{-1} \cdot {}^\circ\text{C}^{-1} \quad (\text{eq. 5.3})$$

(Stewart p.53: "Thus, 4,000 joules of energy are required to heat 1.0 kilogram of sea water by 1.0°C")

육지 (rock, soil) 와 비교:

$$C_p(\text{rock}) \approx 800 \ \text{J} \cdot \text{kg}^{-1} \cdot {}^\circ\text{C}^{-1} = 0.2 \cdot C_p(\text{water}) \quad (\text{eq. 5.4})$$

**해양의 climate buffer 역할** (Stewart p.53-54): 계절 cycle 동안 100 m 표층 (100,000 kg/m²) vs 1 m 토양·암석 (3,000 kg/m²) 비교:

$$\frac{\Delta E_{\text{ocean}}}{\Delta E_{\text{land}}} = \frac{C_p^w \cdot m_w \cdot 10}{C_p^r \cdot m_r \cdot 20} = \frac{(4000)(10^5)(10)}{(800)(3000)(20)} = \mathbf{100}$$

→ 해양은 육지의 **100배 많은 계절 열을 저장**. 연안 도시의 기온 진폭이 내륙보다 작은 근본 원인. 시베리아 내륙 60°C 진폭 vs 한국 연안 ~10°C.

## 3. 각 열수지 항의 결정 요인 (Stewart §5.2)

### 3.1 입사 단파복사 $Q_{SW}$

결정 요인 (Stewart p.53-54):
1. **태양 고도**: 위도·계절·시각에 의존
2. **낮 길이**: 위도·계절
3. **표면 흡수 단면적**: 태양 고도에 비례
4. **감쇠 (attenuation)**:
   - 구름 (반사·산란)
   - 대기 path length $\sim \csc\phi$ ($\phi$ = 태양 고도)
   - 흡수 가스 (H₂O, O₃, CO₂)

**한국 연안 적용**:
- 인천 (37.5°N): 하지 정오 $\phi \approx 76°$ → $\csc\phi \approx 1.03$ (거의 직사)
- 동지 정오 $\phi \approx 29°$ → $\csc\phi \approx 2.06$ (감쇠 2배)
- 정오 광로만 비교한 것이며, 계절 일평균 $Q_{SW}$ 비율은 일조 시간·운량까지 필요하다 (source-needed).

### 3.2 장파복사 $Q_{LW}$

Stefan-Boltzmann 법칙 기반 net flux:

$$Q_{LW,\ \text{net}} = \varepsilon \sigma (T_s^4 - T_a^4)$$

- $\varepsilon$ ≈ 0.97 (해수 emissivity)
- $\sigma$ = 5.67×10⁻⁸ W·m⁻²·K⁻⁴
- $T_s$ = 표면 온도, $T_a$ = effective 대기 온도 (cloud-corrected)

위 식은 해양의 순 장파 손실을 양으로 둔다(표 §1 의 부호 관례에서는 음). 한국 연안의 계절별 크기는 관측·재분석 출처 필요 (source-needed).

### 3.3 Sensible heat flux $Q_S$

대기와의 전도 (bulk formula):

$$Q_S = \rho_a c_{p,a} C_S U (T_a - T_s)$$

- $\rho_a$ = 공기 밀도 (1.3 kg/m³), $c_{p,a}$ = 1030 J·kg⁻¹·K⁻¹ (Stewart Table 5.1)
- $C_S$ = bulk transfer coefficient (~ 1.0×10⁻³ for 중립 대기)
- $U$ = 풍속 (m/s, 10m 기준), $T_a - T_s$ = 공기 - 해수 온도 차이

**한국 연안**: 보통 $T_s > T_a$ (특히 겨울) → $Q_S < 0$ (해양→대기 전도). 한반도 동해는 한겨울 시베리아 cold-air-outbreak 시 $Q_S$ 매우 음 → 표층 급랭 → marine fog 형성.

### 3.4 Latent heat flux $Q_L$

증발 latent heat:

$$Q_L = \rho_a L_v C_L U (q_a - q_s)$$

- $L_v$ ≈ 2.5×10⁶ J/kg (증발 잠열)
- $C_L$ ≈ 1.0×10⁻³ (bulk transfer)
- $q_a, q_s$ = 공기·해표면 specific humidity

**한국 연안**: 일반적으로 $q_s > q_a$ → $Q_L < 0$ (증발). $Q_L$ 이 $Q_S$ 보다 크기 일반적 (약 3~5배). 한국 SST 의 latent heat 손실은 typically 80-100 W/m² (Park et al. 2015 결과 인용 가능, 추후 source 명시).

### 3.5 Advection $Q_V$

해류 운송 — Kuroshio·황해 난류·동한 난류 등의 효과. 한국 연안에서 특히 중요한 항:

- **서귀포·제주**: 해류 열 수송과 SST 변화의 관계를 검토할 후보 지역. 지역별 해류 설명은 독립 문헌 인용 보강 필요(`source-needed`).
- **인천·서해** (Yellow Sea cold pool): $Q_V$ 비교적 작음
- **동해** (East Korea Warm Current): 부분 영향, 시기별 변동

## 4. 열팽창과 해수면 (관련: SLR cross-check)

해수 열팽창 계수:

$$\alpha = -\frac{1}{\rho}\frac{\partial \rho}{\partial T} \approx 1.5 \times 10^{-4} \ \text{°C}^{-1}$$

(전형값, 25°C 표층 해수; 더 자세히는 Stewart §6.x 참조)

effective depth $H$ 의 표층이 $\Delta T$ 가열되면 해수면 상승:

$$\Delta L = \alpha \cdot H \cdot \Delta T$$

**한국 연안 적용 시 고려사항**: 열팽창 기여를 평가하려면 수온 추세의 분석 기간, 유효 수심, 해수면 변화의 다른 성분을 구분해야 한다. 사례 계산은 [`experience/khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md) §5를 탐색용으로 참조한다.

## 5. SST anomaly 와 climate variability

### 5.1 PDO (Pacific Decadal Oscillation)

20-30 년 주기의 북태평양 SST 패턴. 한국에 영향:
- PDO+ phase: 적도 동태평양 warm → Kuroshio 강화 가능 → 한국 연안 SST 상승
- PDO− phase: 반대

한국 연안 SST의 장단기 추세 비교와 PDO/ENSO 관련 해석 사례는 [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §3.2를 탐색용으로 참조한다.

### 5.2 ENSO

El Niño year 한국 영향:
- 1997-98, 2015-16, 2023-24 강한 El Niño 시기 한국 SST 양의 anomaly
- KHOA Annual Report 2024: **2024년 9월** 한국 평균 수온 편차 +3.40 °C (월별 편차 표). 원인 귀속(El Niño 등)은 원문에 없다.

### 5.3 Marine Heatwave (MHW)

해양 폭염 정의 (Hobday 2016): 일 SST 가 climatology 90 percentile 5일 연속 초과.
- 한국 최근 고온 사례는 [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §7을 탐색용으로 참조한다.
- 양식·어업·생태계 직접 피해

## 6. 해양 mixed layer

표층 열수지가 영향을 미치는 깊이 = mixed layer depth (MLD):
- 한국 연안 계절별 MLD 범위는 지역 관측 출처 필요 (source-needed). 일반적으로 여름에 얕고 겨울에 깊다.
- $Q_{net} > 0$ 시 stratification 강화 → MLD 감소
- $Q_{net} < 0$ 시 convection → MLD 증가

→ 열팽창 계산의 effective $H$ 결정 시 시기·해역별 MLD 차이를 고려해야 한다.

## 7. 인용 정형

본 §의 핵심 수식:
- $Q = Q_{SW} + Q_{LW} + Q_S + Q_L + Q_V$ — (Stewart eq. 5.1, p.52)
- $\Delta E = C_p \cdot m \cdot \Delta T$ — (eq. 5.2)
- $C_p \approx 4.0 \times 10^3$ J/(kg·°C) — (eq. 5.3)
- 해양 100× 육지 열 저장 비율 — (Stewart p.53-54 본문 계산, 식 번호 없음)

다음 절 (`03-analysis-methods.md`, `04-code-and-tools.md`) 에서 위 이론을 실제 시계열·격자 데이터에 적용.

## 8. 연결

- [`01-concept.md`](01-concept.md) — SST 정의·측정 정형화
- [`experience/khoa-sst-warming-trend.md`](../../experience/khoa-sst-warming-trend.md) §4 — 열팽창 사례 계산(탐색용)
- [`experience/khoa-sst-global-crosscheck.md`](../../experience/khoa-sst-global-crosscheck.md) §5 — 자료별 열팽창 계산 비교(탐색용)
- [`concepts/tides/02-theory.md`](../tides/02-theory.md) §8.6 — 평균해면 trend (SLR-SST 인과 연결)
- 외부:
  - Stewart, R.H., 'Introduction to Physical Oceanography' (textbook/md/stewart_textbook.md) — Ch 5 + 6
  - IPCC AR6 WG1 Ch.9 Ocean — 글로벌 SST trend·열팽창 정량
  - Park et al. 2015 — 한국 연안 satellite vs in-situ ([Ocean Sci J](https://link.springer.com/article/10.1007/s12601-015-0009-1))
