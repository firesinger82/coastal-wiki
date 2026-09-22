---
title: "복합침수 확률 해석 — 결합확률(JPM)의 전제와 '빈도가 붙지 않은 외력'"
topic: compound-flooding
canonical_source: self
citation_status: verified
has_source_needed: true
verification_method: "선정 범위를 두 문헌의 특정 장으로 고정하고 그 범위만 판독했다. (1) [sea-level] Pugh §8:3~8:4 (PAGE-280~303) — 재현기간·조우확률 식(8:1), 연최대치 순위+GEV, 조석⊗해일 결합확률과 convolution 식(8:5), 장단점 목록, 열대저기압 한계, 설계 외력 결합에 대한 비판. 인용한 문장은 전부 해당 PAGE 마커 범위에서 직접 read 후 원문 그대로 옮겼고, 줄번호→PAGE 매핑을 awk 로 실측했다. (2) [hydraulics-and-hydrology] = **USACE LACPR Hydraulics & Hydrology Appendix** (2026-07-14 textbook/notes/theory-ch02-continuity.md 가 기록한 정체 정정. 본 세션에서 sources.yml title·topics 를 그에 맞게 갱신) §1·§3.1·§5.2·§6 (PAGE-7~9·13·38·40·61·62·65·66·69) — 4단계 해석 체인, JPM-OS, 월류율 Monte Carlo, 내수 box model·강우·펌핑. **한계**: 두 문헌 전권을 읽지 않았다. copula·조건부 표본추출 등 현대 다변량 기법, 한국 사례, 모델측 구현 연결은 본 노트 범위 밖이며 §6 에 source-needed 로 남겼다."
note_author: "Claude Opus 5 (1M context)"
note_date: 2026-09-22
related:
  - concepts/compound-flooding/01-concept.md
  - concepts/compound-flooding/06-model-application.md
  - concepts/storm-surge/03-analysis-methods.md
  - concepts/swash-zone/03-analysis-methods.md
---

# 복합침수 확률 해석

> [[01-concept]] 은 복합침수를 "여러 인자가 겹쳐 합산을 초과하는 침수" 로 정의했다.
> 그 정의를 **수치로 바꾸려면 결합확률이 필요하다.** 본 노트는 그 계산법과,
> 실무가 그 계산을 어디까지 하고 어디서 멈추는지를 다룬다.

## 1. 구하려는 양 — 재현기간과 조우확률

설계가 요구하는 것은 "수위 $\eta$" 가 아니라 **$\eta$ 를 넘을 확률**이다. 한 해에 $\eta$ 를
넘을 확률이 $Q_Y(\eta)$ 이면 재현기간은 그 역수로 정의된다. 이 정의는 **"같은 통계가 전 기간에
유효하다" 는 암묵적 가정**을 깔고 있다.[^pugh-rp]

구조물 수명 $T_L$ 동안 한 번이라도 넘을 확률(조우확률·설계위험)은

$$\text{Risk} = 1 - \left[1 - Q_Y(\eta)\right]^{T_L} \tag{8:1}$$

수명 100년, 허용위험 0.1 이면 $T(\eta) \approx 950$ 년이 필요하다.[^pugh-risk]
**재현기간을 수명과 같게 잡으면 조우확률이 약 0.635 다** — 즉 설계수위의 재현기간은
수명을 상당히 초과해야 한다.[^pugh-0635] 허용 $Q_Y$ 는 자산 가치로 갈린다:
원자력발전소 $10^{-5}$~$10^{-6}$, 네덜란드 연안방호 $10^{-4}$, 영국의 다수 사업은 $10^{-3}$ 이상.[^pugh-qy]

## 2. 두 고전 경로 — 연최대치 vs 결합확률

| | **A. 연최대치 순위 + GEV** | **B. 조석⊗해일 결합확률(JPM)** |
|---|---|---|
| 입력 | 연 1개 최대치 | 조위 예측 + 잔차 전 시계열 |
| 적합 | 축소변량 $X$ 에 GEV 3형(Fisher–Tippett 2·1·3) 최소자승[^pugh-gev] | 두 확률밀도의 **합성곱** 식 (8:5) |
| 필요 자료길이 | **최소 25년** 권장[^pugh-25] | **4년이면 충분**, 1년도 유용[^pugh-adv] |
| 외삽 | 필수. 자료기간의 **4배 이내**로 제한[^pugh-extrap] | **외삽 없음**[^pugh-adv] |
| 자료 낭비 | 큼 — 1년이 통계 1개 | 없음[^pugh-adv] |

B 의 핵심은 조석 확률밀도 $D_T$ 와 해일잔차 확률밀도 $D_S$ 를 합성해 총수위 밀도 $D_0$ 를 얻는 것이다.

$$D_0(\eta) = \int D_T(\eta - \gamma)\, D_S(\gamma)\, d\gamma \tag{8:5}$$

실무 계산은 0.1 m 계급의 결합확률 행렬을 만들고 **대각선을 따라 합산**한다 — 3.2 m 조위+0.0 m 해일,
3.1 m+0.1 m, 3.0 m+0.2 m 이 모두 총수위 3.2 m 를 만들므로 세 결합확률의 합이 그 수위의 확률이다.[^pugh-diag]

**무차원 확률을 재현기간으로 바꾸는 단계가 별도로 필요하다.** 영국 항만에 대해서는 확률의 역수를
**시간 단위 재현기간**으로 취할 수 있음이 관측 대조로 확인됐다($\log_{10}P = -5.94$ → 100년).[^pugh-timescale]
고조위만 쓰는 간이판에서는 반일주조 연 705회를 써서 환산한다.[^pugh-705]

B 는 **저수위 초과확률이 계산 과정에서 자동으로 따라 나온다**는 부수 이점이 있고,
조석 체계 변화(하구언 건설)·기상 추세·평균해수면 상승을 **각 분포를 따로 조정해 반영**할 수 있다.[^pugh-adv]

## 3. 결합확률이 기대는 전제와 그 붕괴

식 (8:5) 가 성립하려면 **조석과 해일이 독립**이어야 한다.[^pugh-indep] 그런데 [[01-concept]] §3.2 가
다룬 tide–surge interaction 이 바로 그 독립성을 깨뜨린다.

| 붕괴 양상 | 대응 | 근거 |
|---|---|---|
| 해일 잔차 분포가 조위에 의존(Southend — 큰 해일이 만조를 회피) | 조위에 따라 변하는 조건부 해일 분포로 확장 | [^pugh-indep] |
| JPM 이 연최대치보다 **약간 높은 값**을 준다 | 약한 tide-surge interaction 탓으로 해석 | [^pugh-disadv] |
| 열대저기압 — 한 지점에서 너무 드물어 신뢰할 통계가 불가 | **통계를 포기하고 모델링 경로로** | [^pugh-tropical] |

세 번째가 결정적이다. Pugh 는 연최대치 순위와 조석-해일 결합확률 두 방법 모두
**"열대 밖 지역에 가장 효과적"** 이라고 못박고, 대서양·멕시코만 연안은 극한 폭풍을 수치모델에
입력해 응답을 계산하는 쪽이 적절하다고 한다.[^pugh-tropical] §4 의 LACPR 이 정확히 그 경로다.

> [!source-needed]
> copula·조건부 표본추출·다변량 POT 등 1990년대 이후 결합확률 기법은 본 노트가 판독한
> 범위 밖이다(Pugh 는 threshold 법(Smith 1984)과 Middleton–Thompson(1986) 초과확률법을
> **이름만** 언급한다[^pugh-other]). 현재 복합침수 문헌의 주류인 copula 기반 의존성 모델링은
> 별도 출처 확보 후 보강한다.

## 4. 실무 체인 — USACE LACPR (모델 기반 결합확률)

루이지애나 연안방호 기술평가(LACPR)의 수리·수문 해석은 **4단계 연속 체인**이다.[^lacpr-steps]

| 단계 | 내용 | 산출 |
|---|---|---|
| 1 | ADCIRC(해일) + WAM/STWAVE(파) 수치계산, 허리케인 조건 56종(2010 기준상태) | 수위·파랑 시계열 |
| 2 | **JPM-OS** 빈도해석 | 외수(exterior) stage frequency |
| 3 | 제방고 결정 + 월류량 | 월류 hydrograph |
| 4 | **강우 포함** 내수위 결정 | 내수(interior) stage frequency |

**JPM-OS(Joint Probability Method with Optimal Sampling)** 는 2006–07년 USACE·FEMA·NOAA·학계
합동으로 만든 절차로, 허리케인의 **전진속도·크기·최저기압·접근각·지리분포의 결합확률**을 다룬다.
일반 JPM 이 수천 사상을 평가하는 데 비해 최적표본추출로 **152개 폭풍 집합**으로 줄인 것이 핵심이다.[^lacpr-jpmos]
이 집합은 연 1/50 ~ 1/3,500 확률 범위를 덮도록 선정됐고, 상단(1/2,000)은 더 불확실하다고 문서 스스로 밝힌다.[^lacpr-range]
대안별로는 시간 제약 때문에 56개 이하만 실제 계산하고 나머지는 상관관계로 채웠다.[^lacpr-corr]

월류는 확정값이 아니라 **Monte Carlo(N = 5,000)** 로 신뢰수준 10·50·90% 를 산출한다.
hydrograph 폭, 파고·주기, 월류식 계수의 불확실성을 각각 추출한다.[^lacpr-mc]
해일수위가 마루를 넘으면 자유월류 항이 파랑월류 항에 더해진다.[^lacpr-eq51]

$$q_{tot} = m\,(\eta - z_{crest})^{3/2} + 0.13\sqrt{g H_s^3}$$

내수는 계획소구역마다 **box model + stage–storage 곡선**으로 두고, 허리케인 동안의 물수지를
**강우·월류·펌핑** 셋이 지배한다고 명시한다.[^lacpr-box] 매 시간단계에서 유입률이 펌프 용량을
초과하는 분만 누적해 총 침수체적을 만들고, 그 체적을 stage–storage 곡선에 보간해 내수위를 얻는다.[^lacpr-stage]

## 5. ★ 어느 외력에 빈도가 붙었는가

LACPR 에서 **강우에는 재현기간이 붙지 않는다.** 모든 해일 사상(100·400·1,000·2,000년),
모든 신뢰대, 모든 계획단위에 **고정된 10년 빈도 강우**가 부과된다.[^lacpr-fixed]
그 근거로 문서가 대는 것은 두 가지다.

1. **비동시성 주장** — 가장 강한 강우는 허리케인 미만 강도의 폭풍에서 나왔다는 관측(Shoner & Molansky 1956).
   따라서 "극한 허리케인 사상이 희귀 강우 사상과 동시에 일어날 가능성은 낮다".[^lacpr-noncoinc]
2. **대안 비교가능성** — 내수 조건을 고정해야 제방 대안 간 응답을 직접 비교할 수 있다.[^lacpr-fixed]

강우 사상 자체는 정밀하게 고른다. 뉴올리언스 시가지 펌프가 첫 시간 1인치·이후 시간당 0.5인치를
처리한다는 가정 아래 3·6·12·24시간 지속시간을 비교해 **펌프 초과율이 가장 큰 6시간 지속**을
택했고, 총우량 6.5인치를 6시간 sinusoidal 로 분포시켰다.[^lacpr-rain6h]

**그래서 stage frequency curve 의 "100년" 은 침수사상의 재현기간이 아니라 외수(해일·파)의 재현기간이다.**
같은 곡선 위 모든 점에 동일한 10년 강우가 들어 있다. 복합침수를 다루는 해석인데
복합 재현기간은 산출되지 않는다 — 이것은 결함이 아니라 **명시된 설계 선택**이고,
그 선택의 유효성은 (1)의 비동시성 주장에 전적으로 얹혀 있다.

이것이 Pugh 가 지적한 두 극단 사이의 **세 번째 선택**이라는 점이 중요하다. 전통적 설계 관행은
바람·파·흐름·수위의 극한값을 **각각 추정해 동시발생을 가정하고 더하는 것**인데, 이는 완전상관을
가정하는 것이어서 **필연적으로 과대설계**가 된다. 그렇다고 **완전독립 가정도 무효**다.[^pugh-combine]
LACPR 은 두 외력 계열 중 하나(해일·파)에만 결합확률을 적용하고 다른 하나(강우)를 상수로 고정한다.
**의존성을 모델링하지도, 완전상관으로 더하지도 않고, 한쪽을 빈도 축에서 제거한 것이다.**

같은 논리가 파랑에도 적용된 사례가 있다. 방호벽 설계에서 특정 '설계폭풍' 대신
**'설계 월류유량(design overtopping discharge)'** 을 쓰자는 제안은, 수위·유의파고·주기·파향의
모든 조합에 대해 월류량을 구해 두고 **부지의 수위-파랑 결합 발생확률**로 초과확률을 합산한다.
Pugh 는 이 접근의 최대 난점이 "가능한 모든 수위·파랑 조합의 발생확률을 신뢰성 있게 추정하는 것"
이라고 적는다.[^pugh-overtop] LACPR 의 강우 고정은 그 난점을 한 차원 줄이는 실무적 타협이다.

## 6. 남은 것

- **현대 다변량 기법 미판독** — copula, 조건부 표본추출, 다변량 POT. §3 콜아웃 참조. `source-needed`
- **한국 사례 정량 부재** — [[01-concept]] §4.1 이 남긴 공백 그대로. KHOA·적응계획 자료 확보 후. `source-needed`
- **모델 구현과의 연결 미작성** — [[06-model-application]] 이 다루는 SFINCS·LISFLOOD-FP 가
  실제로 외력을 어떻게 동시 부과하는지(입력 파일·시간축 정렬)는 본 노트가 다루지 않았다.
  확률 해석(본 노트)과 모델 강제(06)를 잇는 고리가 비어 있다.
- **§4 는 단일 사업 문서** — LACPR 한 건의 방법론이다. 이것을 일반 실무 관행으로 확대 해석하지 않는다.

## 출처

[^pugh-rp]: [sea-level] PAGE-281 (§8:3): "If the probability of a level n being exceeded in a single year is QY(t]), the level is often said to have a return period J(r|) of [ S Y O I ) ]1 years. This makes the implicit assumption that the same statistics are valid for the whole period." (OCR 손상 — 기호는 원문 식 (8:1) 문맥으로 복원)
[^pugh-risk]: [sea-level] PAGE-281: "Risk = 1 - [1 - eY(n)]rL (8:1) where TL is the design lifetime. As an example, suppose that the envisaged life of a structure is 100 years, then for a risk factor of 0.1 for exceedence during this period, equation (8:1) shows that the design level should have a probability: so that r(n) = 950 years."
[^pugh-0635]: [sea-level] PAGE-281: "It should be remembered that a structure has a probability of near 0.635 of encountering a level which has a return period equal to its design life; for acceptable risk factors the design level must have a return period which considerably exceeds the expected lifetime of the structure."
[^pugh-qy]: [sea-level] PAGE-281: "Nuclear power stations may specify 10 ~5 or 10~6. For the coastal protection of the Netherlands a value of 10\"4 is adopted (Delta Committee, 1962), but for many British coastal protection schemes values of 10\"3 or greater are accepted."
[^pugh-gev]: [sea-level] PAGE-286 (§8:3:2): "This family of curves is known as the Generalized Extreme Value (GEV) distribution. The fit is usually obtained by the method of least-squares." / "If k is zero the plot of X against r\\ is a straight line, sometimes called the Gumbel distribution… The distributions corresponding to k negative, zero and positive are sometimes referred to as Fisher-Tippett Types 2, 1 and 3 respectively." 극한수위에서는 $k>0$(상한 존재)이 통상이나 남부 북해 등에서는 $k<0$ 으로 상한이 나타나지 않는다고 같은 페이지가 적는다.
[^pugh-25]: [sea-level] PAGE-287: "Although as few as ten annual maxima have been used to compute probability curves, experience suggests that at least 25 values are needed for a satisfactory analysis. The major disadvantage of the method is the waste of data, a complete year of observations being represented by a single statistic."
[^pugh-extrap]: [sea-level] PAGE-286: "As a general rule extrapolation should be limited to return periods not longer than four times the period of annual maximum levels available for analysis, but even within this limit extrapolated values should be interpreted with caution."
[^pugh-adv]: [sea-level] PAGE-290 (결합확률법의 장점 (a)~(f)): "(a) Stable values are obtained from the relatively short periods of data. Even a single year can yield useful results, but four years is a desirable minimum (Pugh and Vassie, 1980). Using the annual maxima method perhaps 25 years of data are normally required. (b) There is no waste of data. (c) The probabilities are not based on extrapolation. (d) Estimates of low-water level probabilities are also produced. (e) Separate changes in the physical factors which affect levels may be identified and incorporated… (f) Projected changes in mean sea-level may be incorporated by simple addition."
[^pugh-diag]: [sea-level] PAGE-288 (Table 8:3 설명): "The joint probability of a 3.2 m predicted tide and a 0.0 m surge is 0.04, the product of their individual probabilities… Any of these three joint events will produce a total observed high-water level of 3.2 m, and so the total probability of a 3.2 m level, obtained by scanning along the dashed diagonal, is the sum of the three probabilities, 0.11."
[^pugh-timescale]: [sea-level] PAGE-289: "To convert these dimensionless probabilities to return periods some time-scale has to be determined: analysis, supported by comparison with observations, shows that the inverse of the probability may be taken as the return period in hours, at least for British ports. Thus the levels corresponding to Log10P = —5.94 have a 100-year return period."
[^pugh-705]: [sea-level] PAGE-289: "Suppose that some particular level has a joint probability of 0.0001 for each high-water level. For a semidiurnal tidal regime with 705 tides in each year, the return period for this level is 10 000 tidal cycles, 14.2 years." 같은 문단이 이 고조위 기반 간이법의 한계도 밝힌다 — "it fails to take account of large positive surges which occur at times other than those of predicted tidal high water."
[^pugh-indep]: [sea-level] PAGE-289 (식 8:5 직후): "For this to be a valid estimate of D0(r\\) the tide and surge probabilities must be independent. However, an extension of the method which allows the surge probability density functions to vary as the tidal level changes has been applied to the case of Southend (Pugh and Vassie, 1980), where the maximum surge levels have a marked statistical tendency to avoid tidal high waters (Section 7:8)."
[^pugh-disadv]: [sea-level] PAGE-291 (단점 (c)): "Slightly higher values are obtained by the joint probability method, which may be due to weak tide-surge interaction (Section 7:8). Where the surge residual distribution is significantly dependent on the tidal level, more elaborate joint probability computations are necessary." 단점 (a)(b)는 자료 품질(수분 이내 시각 정확도)과 계산 부담이다.
[^pugh-tropical]: [sea-level] PAGE-291: "On the Atlantic and Gulf Coast of the United States the extreme sea levels are produced by hurricanes, which are too rare at any particular place to permit the calculation of reliable probabilities. Some kind of modelling approach as discussed in the next section is more appropriate. The methods which we have discussed of ranking annual maxima, and of computing joint tide-surge probabilities are most effective for calculating extremes for regions outside the tropics."
[^pugh-other]: [sea-level] PAGE-291: "Smith (1984) describes a method which analyses peaks which exceed some specified threshold. Middleton and Thompson (1986) have developed a rigorous exceedence probability approach which remains effective where surge variations dominate the tidal variations, and avoids the difficulties of relating joint probabilities to return periods."
[^pugh-combine]: [sea-level] PAGE-299 (§8:4): "Traditional design practice has been to estimate the probabilities of extreme winds, waves, currents and levels independently, and to add these extreme values, assuming they occur simultaneously, to obtain the extreme environmental design conditions. This assumes that they are statistically totally correlated, which is not the case as we have already discussed for joint probability distributions of tides and surges. Inevitably the traditional assumptions must result in some over-design. However, the assumption of total independence of the parameters is also invalid."
[^pugh-overtop]: [sea-level] PAGE-302: "instead of designing defence walls to prevent overtopping by some specified 'design storm' conditions of still-water level and wave height, engineers should work with the concept of 'design overtopping discharge' (Owen, 1983)… The total probability of overtopping discharges exceeding some specified value is given by summing the probability of all these joint sea-level/wave conditions which individually exceed that value." / PAGE-303: "the major environmental problem with this approach is to obtain a reliable estimate of the probability of occurrence of all possible combinations of water level and wave conditions."
[^lacpr-steps]: [hydraulics-and-hydrology] (= USACE LACPR *Hydraulics and Hydrology Appendix*) PAGE-7 (§1): "The hydraulic analysis of each alternative in LACPR consisted of the following consecutive steps: 1. Numerical computations of surge levels and wave characteristics using ADCIRC, WAM and STWAVE; 2. Frequency analysis using the JPM-OS method and the determination of exterior stage frequency; 3. Determination of the levee heights and overtopping volumes; 4. Determination of the interior stages including rainfall;". 56개 폭풍 기준상태는 PAGE-8 (Step 1): "A base set of 56 hurricane conditions have been evaluated with the modeling suite ADCIRC/STWAVE for the 2010 base condition."
[^lacpr-jpmos]: [hydraulics-and-hydrology] PAGE-38 (§3.1): "In 2006 and 2007, a team from the Corps of Engineers, FEMA, NOAA, private sector, and academia developed a new process for estimating hurricane inundation probabilities, the Joint Probability Method with Optimal Sampling process (JPM-OS)." / "For most Joint Probability Methods, several thousand events are evaluated. With the JPM-OS method, optimal sampling allows for a smaller number of events to be used… JPM-OS takes into account the joint probability of forward speed, size, minimum pressure, angle of approach and geographic distribution of the hurricanes." 152개 폭풍 집합의 구성(중심기압·최대풍반경·전진속도·접근각·경로 조합)은 PAGE-13 (§2).
[^lacpr-range]: [hydraulics-and-hydrology] PAGE-40: "The original set of 152 storms was selected in such a way that it covered the probabilities in the range of 1/50 – 1/3,500 per year with main emphasis on the range 1/50 – 1/500 year… The 1/2,000 year return period is near the upper end of the original storm set limits and it can be expected that the results for the upper end are more uncertain than the results for the 1/100 – 1/1,000 year range."
[^lacpr-corr]: [hydraulics-and-hydrology] PAGE-8 (Step 2): "This method requires a set of 152 storms to establish the frequency curves for surge and waves. Since the various alternatives were only run for 56 or less storms, the results for the remaining storms were established using correlation techniques in order to carry out the frequency analysis with the JPM-OS method."
[^lacpr-mc]: [hydraulics-and-hydrology] PAGE-61~62 (§5.2): "The overtopping rates have been computed using a Monte Carlo Simulation to account for the various uncertainties. The uncertainty in hydrograph width is initially considered, followed by the uncertainties in wave height, wave period and the coefficients of the overtopping formulation." / "i) Repeat the steps c) through h) a large number of times (N = 5,000)".
[^lacpr-eq51]: [hydraulics-and-hydrology] PAGE-61 (식 5.1, TAW 2003): "qtot = m (η− zcrest)3/2 +0.13 gHs3" — 분기 조건은 같은 페이지: "Surge level below the crest level : only wave overtopping / Surge level above the crest level : wave overtopping and free flow". $m$ 은 위어계수 $\approx 3.1\ \mathrm{ft}^{0.5}/\mathrm{s}$, 단위는 원문이 ft·s 계다. 원문 표기상 두 번째 항의 제곱근 범위가 명시적이지 않아 본 노트는 $\sqrt{gH_s^3}$ 로 읽었다 — 차원(유량/폭)이 맞는 유일한 해석이다.
[^lacpr-box]: [hydraulics-and-hydrology] PAGE-65 (§6.2): "Each internal or semi-internal planning subunit has been schematized as a box model for which a stage-storage curve has been established… During a hurricane event the water balance is dominated by rainfall, wave or surge water overtopping and pumping (see Figure 6.2). The interior stage frequency has been based on the sum of the overtopping volume together with rainfall in the subunit. The effect of pumping in reducing flood volume has been taken into account if applicable."
[^lacpr-stage]: [hydraulics-and-hydrology] PAGE-69 (§6.6): "The rate of flooding in each time step is considered by comparing the rate to the pumping rate and then if the difference is positive, recording the difference. These positive rates are then summated… This gives a total volume of flooding for this condition." / "The flood stage in each internal planning subunit is established by interpolating the total flood volume into the stage storage relationship."
[^lacpr-fixed]: [hydraulics-and-hydrology] PAGE-66 (§6.3): "In order to evaluate the large number of LACPR alternatives on a comparable basis, a constant rainfall event was applied across all storm surge events (100-year, 400-year, etc.), confidence bands (10%, 50% and 90%) and for all planning units. Interior drainage is in essence fixed so that interior responses to overtopping over the flood risk reduction system can directly be compared from one plan to another." 10년 강우라는 값은 PAGE-65: "The rainfall used in the evaluation was the 10-year rainfall".
[^lacpr-noncoinc]: [hydraulics-and-hydrology] PAGE-66 (§6.3): "Based on earlier work, it appears that the heaviest rainfall have been from storms of less than hurricane intensity (Shoner and Molansky, 1956). In other words, it is not likely that an extreme hurricane event (100-year event, 400-year event, etc.) coincides with a rare rainfall event."
[^lacpr-rain6h]: [hydraulics-and-hydrology] PAGE-66 (§6.3): "The basic assumption in the populated areas of New Orleans is that pumping can cope with 1\" of rainfall in the first hour, and 0.5\" in subsequent hours. Using this assumption, the various 10-year rainfall events (3-hour, 6-hour, 12-hour, 24-hour) were evaluated and the 6 hour duration storm was shown to give the highest rainfall rate over pumping." / "The total rainfall is 6.5\" for a 10-year rainfall event of 6 hours according to TP40 documentation. The rainfall hydrograph was calculated as a sinusoidal distribution over a six hourly period". 같은 페이지가 그 한계도 밝힌다 — "Note that in reality, the temporal development of rainfall events can be quite different from a sinusoidal shape."
