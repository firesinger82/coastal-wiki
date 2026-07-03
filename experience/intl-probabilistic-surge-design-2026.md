---
title: "확률론적 폭풍해일 설계해일고 국제 사례 (미·일·중·네덜란드) — JPM-OS·설계기준·검증·ML 벤치마크"
topic: storm-surge
canonical_source: self
citation_status: source-needed
note_author: "Claude Opus 4.8 (1M context) — deep-research 3회(각 105~107 에이전트, 적대검증 3-0)"
note_date: 2026-06-21
verification_by: ""
verification_date: ""
experience_evidence:
  repeated_observation: false
  objective_data: true        # FEMA/USACE 1차 정부보고서·중국 GB표준·네덜란드 Water Act + 피어리뷰
  reproducible: false
---

# 확률론적 폭풍해일 설계해일고 — 국제 사례

한국 JPM+ADCIRC 가상태풍 설계해일 연구([[khoa-adcirc-typhoon-forcing-design-2026]])의 국제 벤치마크. deep-research 3회(2026-06-21): ①미·일 ②중·네덜란드 ③ML surrogate·EVA. 모든 finding 3-0 만장일치.

## 4개국 비교 (완성)

| | 🇺🇸 미국 | 🇯🇵 일본 | 🇨🇳 중국 | 🇳🇱 네덜란드 |
|---|---|---|---|---|
| 설계방식 | **확률론 JPM-OS** | **결정론**(지정태풍) | **혼합**(관측EVA+PMSS+합성SDTM) | **완전확률론**(파괴확률) |
| 기준/규범 | NACCS·FEMA MsCIP·Region II | 3대만 이세만급 최악경로 | GB/T 17839-2011(경계조위)·**GB/T 51015-2014 방조제** | Water Act 2017(→환경법 2024) |
| 재현기간 | 10/50/100/500yr | 설계수위=3옵션 max·설계파 30–50yr | 방조제 "200/12"(200yr해일+12급태풍) | **연 파괴확률 1/300~1/100,000**(LIR 1e-5/yr) |
| 방법 | JPM-OS(quadrature·response surface) | 지정태풍 수치모의 | 관측 Gumbel/GEV/GPD(명목 Pearson-III)·**SDTM 합성~10,000yr** | 하중적분·결합확률 |
| 모델 | ADCIRC+WAM+STWAVE/SWAN(CSTORM-MS) | (연구별) | **FVCOM(GBASSP·GRAPES 80m)·ADCIRC-SWAN** | Delft3D-FM·DCSM·SFINCS·Hydra-NL/Ring |
| 기관 | USACE ERDC·FEMA·NOAA | MLIT·기상청·중방회 | MNR(구SOA)·NMEFC | Deltares·Rijkswaterstaat |

## 🇺🇸 미국 — JPM-OS 정전 (우리가 차용할 핵심)
- **JPM-OS**: 브루트포스 JPM(수천) → 최적표집 **~100-200개**(가우시안과정 quadrature[Toro/Niedoroda] 또는 response surface[Resio]), ~1자릿수 축소·정확도 유지. Katrina 이후 FEMA/USACE 표준.
- **파라미터 벡터(직접 차용)**: ΔP·Rmax·진행방위 θ·이동속도 Vf·상륙위치 + **Holland B=Rmax·위도 2차함수**(Vickery&Wadhera 2008: `B=1.881−0.00557·Rmax−0.01295·ψ`).
- **NACCS**(ERDC/CHL TR-15-14): 1050 합성열대+100 온대, CSTORM-MS, ΔP 28–98 hPa(5간격)·Rmax 25–174 km·θ −60~+40°.
- **FEMA Region II(Sandy)**: 7ΔP×5Rp×3Vf×3θ×3B=945 → **159 최적 합성태풍**.
- **MsCIP**: Monte Carlo·EST 명시 폐기 → JPM 채택("MC는 극치에 비효율"). 228 태풍 → 10/2/1/0.2% 연초과.
- **검증=우리 Gate-4 평행**: 133 NOAA 검조소, **IMEDS 0.83-0.89·bias ±0.04 m**, 3.1M절점. (IMEDS는 정규화 skill, RMSE 아님 — 방법론적 평행.)

## 🇯🇵 일본 — 결정론 (핵심 대비점)
도쿄·오사카·이세만을 **1959 이세만(Vera)급 지정태풍 최악경로**로 결정론 설계. 설계수위=max(①기록최고조위 ②MHWS+기록최대편차 ③MHWS+지정태풍추정편차), 설계파 30-50yr. **아시아 태풍권에서 확률론 해일은 연구용, 법정 설계근거 아님** → 한국 JPM 도입의 포지셔닝 논거.

## 🇨🇳 중국 — 혼합 (가장 유사한 태풍성 사례)
- **규범**: GB/T 17839-2011(경계조위, 4단계 청황적적, blue=2-5yr HWL) / **GB/T 51015-2014 방조제 설계**("200/12"=200yr 해일+12급태풍). MWR 2014 빈도분석 지침.
- **3방법**: (a)관측 극치분석 (b)결정론 PMSS(상하이 진산구) (c)**SDTM 합성동역학 TC**(~10,000yr 합성, JPM-OS 유사, 단기·장기 재현기간 모두 robust; HSM 역사기반은 단기만).
- **명목 Pearson-III이나 실제 연구는 Gumbel/GEV/GPD** — EVA 방법선택이 ~0.5-1.0 m 불확실성(Kanmen 100yr ESL 4.69-5.18m). **= 우리 메인논문 '방법이 결론 좌우'와 동일 교훈**, 우리 GEV/GPD 정당화.
- 모델: FVCOM(GBASSP·GRAPES 80m)·ADCIRC-SWAN. 결합확률은 구조응답(SR) 표집이 wave/surge-dominated보다 우수.

## 🇳🇱 네덜란드 — 완전확률론 (전이 주의)
- **2017 Water Act**: 설계수위 초과확률(하중) → **연 침수(제방파괴)확률**로 전환, 제방구간별 기준. 1958/1996 기준 대체.
- **1/300 ~ 1/100,000/yr**, 기본안전 LIR 1e-5/yr(국회 고정), 10배당 2등급 로그분할. WTI2017→WBI2017/BOI(Deltares), 3,600 km 1차방어선.
- ⚠**전이 주의**: 네덜란드는 **온대성·광역·장시간** 폭풍해일용. 한국(중국과 같이)은 **태풍성·공간집중·단기첨두** → 합성TC/JPM + GEV/GPD 꼬리가 더 적합. 네덜란드 하중적분/파괴확률 프레임은 직접 이식 곤란(방법론적 영감만).

## 🤖 최신기술 — ML surge surrogate (우리 emulator·JPM 가속 직접 적용)
*(deep-research ③, 23/25 claim이 ML쪽; Taflanidis 계보 등 1차 피어리뷰)*

**대표 surrogate**:
- **C1PKNet**(1D-CNN+PCA+kmeans, Lee/Irish 2021): 1031 합성TC 학습, 첨두해일 **RMSE 0.17m vs ADCIRC**, wet/dry 98%.
- **DeepSurge**(CNN+LSTM 1.7M, PNNL 2025): 트랙시계열+128² 수심격자 → 절점별 첨두 **R²0.815**, **96× 가속**, CMIP6로 **900,000 합성TC** 앙상블.
- **ConvLSTM 시공간출력**(Adeli-Taflanidis 2022): 시계열 전체 출력, GP대비 **RMSE 절반**.
- **GP/Kriging**(Taflanidis 계보: Zhang2018·Kyprioti2021/23·Jung2024): ~5cm RMSE·**불확실성 정량 내장**·<1s/태풍.
- **PCE**(Sochala 2019): 다항카오스 response surface.

**JPM 가속(우리 emulator-스크리닝 용도와 동일)**: 적응적 순차 DoE — 정확도 가장 높일 합성태풍을 반복 선택(Zhang2018), 배치선택(Jung2024), global-Kriging DoE(예측분산+LOOCV, Kyprioti2020).

**★우리 R²0.57 꼬리과소 해법 3가지(직접 적용 가능)**:
1. **2단계 분류후회귀**(Pachev 2023): wet/dry 분류 → 침수위 회귀, zero-inflation 제거(꼬리 회귀 오염 해소).
2. **비대칭 손실(quantile+expectile)**(Longo 2026): 희소극치 예측 개선, 아키텍처 무관.
3. **PCA 차원축소+출력 스케일링**(Kyprioti 2021): 소규모 DB 과적합 완화.
+ **필드/격자 CNN 입력**(DeepSurge식)으로 점-특징 한계 극복.

**기후주입**: CMIP6(HighResMIP) + quantile delta mapping으로 TC 강도 보정 → 합성TC/JPM에 미래기후 반영(PNNL 2025).

## ✅ surge hindcast 검증 정확도 벤치마크 (deep-research ⑥, 9 finding 3-0)

우리 매미 49정점 **첨두해일 RMSE 16~18cm**를 위치시킬 통상값 + 30cm 게이트 정당화.

**peak/HWM RMSE(우리와 직접 비교 가능)**:
| 사례 | 모델 | peak RMSE | 출처 |
|---|---|---|---|
| 한국 마이삭·하이선 | JMA-MSM ADCIRC-SWAN | **0.066–0.070m** | 황태건 외 2026 JKWRA 59(2) |
| 한국 매미 | JMA-MSM | 0.15m | 윤 외 2020 JKSCOE 32(5) |
| 한국 볼라벤 | ADCIRC+SWAN | 0.17–0.19m·첨두시각 ~1h | 서승원 외 2012 JKSCOE 24(5) |
| 미국 Ike | ADCIRC+SWAN | MAD 0.12–0.17m·HWM 94% within ±0.5m·R²0.91 | Hope 외 2013 JGR |
| 중국 GBASSP(운영) | FVCOM | MAE 19.7cm | Nat Hazards 2025 |
| 중국 보하이·남동해 | ADCIRC/FVCOM | 0.21–0.66m(대조차·풍장의존) | 2025 |

→ **통상 peak RMSE ≈ 0.1–0.3m(우수~양호), 시계열·대조차·약강제력 0.2–0.6m**. **우리 매미 16–18cm = 그 정중앙**, 한국 단일태풍 선행(0.15–0.19m)과 동급/우수(매미는 JTWC계열인데도).
- **매미 RMSE는 강제력 의존**: JMA-MSM 0.15 < JTWC 0.20 < ERA5 0.35 < CFSR 0.56(윤2020) — 우리 A(JTWC)/B(MSM) 결과와 정합.
- **30cm 게이트 = 공학목표로 정당화**(보편 문헌 임계 없음; Campos-Caba 2024 Ocean Sci는 RMSE 단독기준 한계 지적). 통상범위 0.1–0.3m의 보수적 상한으로 제시, 더 엄격히는 **±0.2m**(한국 선행 근거)도 가능 — 우리 16–18cm는 둘 다 통과.
- ⚠메트릭 클래스 구분 필수: peak/HWM RMSE ≠ time-series RMSE ≠ scatter index(무차원) ≠ MAE. 인용 시 종류 병기.

## 📊 EVA측 격상 — 비정상성·SLR·copula·Bayesian (deep-research ④, 9 finding 3-0)

**우리 4개 자산 → SOTA 격상 매핑**:

| 우리 자산 | 격상 기법 | 도구·문헌 |
|---|---|---|
| 정상 GEV/GPD | **비정상 GEV/GPD**(location/scale를 시간·MSL·기후지수 공변량) | R **texmex**(evm, 공변량 any param + ML/Bayesian-MCMC/bootstrap 일체)·extRemes(fevd) |
| 모델선택 | 정상 vs 비정상 AIC/BIC/LRT | **Kim·Kwon·Han(2017) J.Hydrol 547:557 — 한국저자**: 정상GEV=BIC(>90%), 비정상GEV 소표본=AIC. ⚠AIC 저파시모니→허위추세 위험 |
| MSL 빈도증폭 | **증폭계수 AF=N(z−δ)/N(z)** + allowance | **Buchanan2017** ERL 12:064009(RCP4.5 25배·RCP8.5 40배@2050)·**Hunter2012** allowance(Gumbel scale로 기대초과빈도 보존)·**Tebaldi2021** NCC(온난화수준 100배=100yr→매년, POT Poisson-GPD 우리와 동족) |
| joint tide-surge MC | **skew surge 결합확률(SSJPM)** → copula | **Williams2016** GRL(skew surge=조석권 최선변수). ★**서해 macrotidal 주의: 천해서 tide-skew surge 독립가정 붕괴**(Santamaria-Aguilar&Vafeidis2018)→copula 필수 |
| M4 비정상 조석(간척) | 비정상 EVA 공변량 or Hunter 가정위반 | (open — 비정상 TIDE 문헌 후속) |

**핵심 정량근거**:
- 비정상성 필수: SLR로 **현 >200년 사건이 2050엔 <30년(GEV/GPD)·<50년(PP)화**(Venice SSP2-4.5 +51cm, NHESS 2022). = 우리 빈도증폭(SSP5-8.5 매년화)의 학술 정합.
- **증폭은 GPD shape ξ가 지배**: 양(heavy-tail, 태풍 Gulf/Atlantic)=덜극단 사건 대증폭 / 음(thin-tail, Pacific)=극단 사건 대증폭. → **서해 정점별 ξ로 증폭 클 곳 플래그**(우리 EVA가 이미 ξ 산출).
- **skew surge**(관측−예측 고조, 조석주기내) = 조석권 폭풍해일 최선 척도. 우리 MC 분해를 SSJPM/copula로 격상 시 표준 변수.

### 🔗 copula 결합확률 + 공간극치 격상 상세 (deep-research ⑤, 12 finding 3-0)

**copula 워크플로(목포 joint MC 대체/검증)**:
1. 주변분포 GPD/GEV 적합 → 2. **chi-plot으로 의존 진단** → 3. **상한꼬리 의존 copula**(Gumbel-Hougaard·Galambos·Hüsler-Reiss; **Gaussian은 태풍극치 부적합**=꼬리의존 없음) → 4. CML(pseudo-obs) 추정 → 5. 선택=**꼬리의존계수+AIC/BIC+평균오차** 조합. **보편 최선 copula 없음→서해 데이터로 재진단 필수**(결과가 copula 선택에 매우 민감).
- 총수위 산정: **failure region 직접적분** 또는 **2-D convolution(joint(driver,surge)⊗조석)** — 후자가 우리 MC 분해와 직접 등가(단 convolution 단계는 tide-surge 독립 가정 — 우리 목포 std축소가 이걸 위배하므로 (skew surge, 고조) copula가 더 타당).
- 도구: **MvCAT**(Sadegh2017 MATLAB, 26 copula·Bayesian MCMC 사후분포)·R copula/VineCopula. Wahl2012(Archimedean으로 peak+적분강도 다변량). ⚠대부분 선행은 **wave-surge·rainfall-surge** 결합이고 **tide-surge 직접 사례는 드묾** → 우리 적용은 다소 신규(서해 의존성 발견이 동기).

**공간 극치(49정점 격상)**: Davison-Padoan-Ribatet(2012) 3분류 — latent Bayesian/copula/max-stable. **latent는 주변분포만 잘 맞고 결합극치는 부실→copula·max-stable 필요**. R **SpatialExtremes**(rmaxstab/fitmaxstab, Smith·Schlather·Brown-Resnick, pairwise composite likelihood, 공간변동 GEV margin). Reich&Shaby2012 hierarchical 대안. → 우리 RFA를 정점간 의존·무검조 보간으로 격상.

**★주제3(비정상 조석=M4 간척변화를 EVA 공변량) = 1차문헌 미생존**: deep-research ④⑤ 모두 못 찾음 → **연구 부재 영역 = 우리 M4(70년 관측, 간척 조석변화)의 신규성 기회**. Hunter allowance '조석통계 불변' 가정을 우리가 정면 위배 입증 → 비정상 TIDE를 EVA에 넣는 건 미개척(잠재 독자기여).

## 공백·후속 (open questions)
1. 중국 코드가 공식 mandate하는 분포(Pearson-III vs Gumbel)·구조물별 재현기간(원전·항만) — 코드 원문 미확보.
2. 네덜란드 모델/소프트웨어(Delft3D-FM·DCSM6·Hydra-NL/Ring) 결합확률 계산법(copula vs 수치적분) 상세.
3. ~~EVA측 공백~~ **대부분 해소(deep-research ④⑤)** — 잔여: ①**비정상 조석(M4)을 EVA 공변량으로**=1차문헌 미발견(미개척, 우리 신규성 기회) ②**tide-surge copula 직접사례 희소**(선행은 wave/rainfall-surge)→서해 적용은 우리가 개척 ③**비정상+공간 결합**(non-stationary spatial GEV, margin·의존 동시 비정상)=확인 claim은 정상모델만 ④vine vs max-stable(점근독립 regime, Wadsworth-Tawn 조건부극치) 미해소.
4. 한국 조건(북서태평양 태풍·서해 대조차 조석-해일) 검증된 surrogate/EVA 사례 — 전무(전이 스킬 미검증, 우리가 첫 검증 가능).

## 핵심 인용 문헌
- Resio·Irish·Cialone(2009) *Ocean Eng* S0029801809002236; Toro et al.(2010) ResearchGate 229357841 — JPM-OS
- USACE NACCS ERDC/CHL TR-15-14 (apps.dtic.mil ADA621343; erdc-library 81b728f7)
- FEMA Region II Joint Probability Analysis (region2coastal.com)
- Niedoroda et al.(2010) MsCIP *Ocean Eng* S0029801809002157
- 중국: NHESS 23/127/2023(GB/T 17839); Ocean&Coastal Mgmt S096456912300399X(GB/T 51015·"200/12"); Coastal Eng 2024 S0378383924001522(SDTM); Fang et al.2021 10.1007/s00477-020-01964-0(EVA 불확실성)
- 네덜란드: Deltares flood protection standards(deltares.nl); Hydra-Ring 과학문서(iplo.nl); Delta Programme(deltaprogramma.nl)
- ML: Lee/Irish(2021) Coastal Eng S0378383921001691(C1PKNet); Rice/Balaguru(2025) ERL 20:104013(DeepSurge); Adeli et al. arXiv 2204.09501(ConvLSTM); Kyprioti et al.(2021) Nat Hazards 10.1007/s11069-021-04881-9(GP); Pachev(2023); Longo(2026) Earth's Future(quantile+expectile)
- EVA격상: **Kim·Kwon·Han(2017)** J.Hydrol 547:557 10.1016/j.jhydrol.2017.02.005(비정상 모델선택, 한국저자); **Buchanan·Oppenheimer·Kopp(2017)** ERL 12:064009(증폭계수 AF); **Hunter(2012)** Climatic Change 10.1007/s10584-011-0332-1(allowance); **Vitousek et al.(2017)** Sci Rep s41598-017-01362-7(doubling); **Tebaldi et al.(2021)** Nat Clim Change s41558-021-01127-1(온난화수준 100배); **Williams et al.(2016)** GRL 2016GL069522(skew surge SSJPM); NHESS 22:3663(2022, 비정상성 필수성); R **texmex** CRAN(비정상+Bayesian+bootstrap 일체)
- hindcast검증: **Hope et al.(2013)** JGR(Ike ADCIRC+SWAN HWM R²0.91·MAD0.12-0.17m); **서승원 외(2012)** JKSCOE 24(5)(볼라벤 0.17-0.19m); **윤 외(2020)** JKSCOE 32(5)(매미 강제력별 0.15-0.56m); **황태건 외(2026)** JKWRA 59(2)(마이삭·하이선 0.066-0.070m); **Campos-Caba et al.(2024)** Ocean Sci 20:1513(RMSE 단독기준 한계)
- copula·공간: **Mazas&Hamm(2017)** Coastal Eng S0378383917300947(chi-plot→EV copula→convolution); **Masina et al.(2015)** S0378383914002270; **Wahl·Mudersbach·Jensen(2012)** NHESS 12:495(Archimedean 다변량 해일); **Sadegh et al.(2017)** WRR 2016WR020242(MvCAT 26copula Bayesian); **Davison·Padoan·Ribatet(2012)** Stat Sci 27:2(공간극치 3분류); R **SpatialExtremes**(Ribatet, rmaxstab/fitmaxstab); Smith(1990)·Reich&Shaby(2012) max-stable

관련: [[khoa-adcirc-typhoon-forcing-design-2026]] [[khoa-design-surge-eva-2026]] · KHOA 프로젝트 메모(위키 외부): `storm-surge-100yr-obs-vs-report` · `three-reference-papers-2026-06`.

## 🌊 추가 취합(2026-07-03): JPM 내 조석-해일 상호작용 + Rmax 표집 + 한국 2023-26

48c(120태풍 surge-only JPM) 서해 경기만 과대 진단과 Rmax 공격면 방어를 위한 표적 조사(웹검색 2에이전트, 원문 5건 확인).

### 조석-해일 상호작용(TSI)의 JPM 내 처리 — 3갈래 관행
1. **FEMA Region II(NY/NJ)**: 159 JPM-OS 태풍 각각에 **랜덤 조석위상 1개 배정, 완전결합 실행**이 공인 표준(간만차 1.6m인데도 선형중첩 배격 명시). [R2 JPA PDF](https://feedback.region2coastal.com/NationalDisasters/Hurricane%20Sandy/RiskMAP/Public/Public_Documents/Storm_Surge_Reports/R2_Joint_Probablity_Analysis.pdf)
2. **USACE NACCS/CHS**: 1050폭풍 surge-only + 랜덤조석 재실행 + **"base+96 tides" 선형중첩**(96 랜덤위상, 조석=불확실성 항). 중간조차라 선형중첩 허용 — 대조차 직수입 불가 논거. [TR-15-5](https://apps.dtic.mil/sti/tr/pdf/ADA627157.pdf)
3. **통계 TSI 보정 convolution — Zhuge et al. 2024 OE 298:117151**: 결합/비결합 모의 차로 TSI 추출→회귀모형→ "surge+랜덤조석+통계TSI" 중첩으로 빈도수위. **재실행 없이 surge-only 결과 보정하는 선례 = 48c에 가장 현실적 경로.** TSI는 대체로 음(-)기여.
- **영국 SSJPM(skew-surge JPM)**: 여전히 state-of-the-art(EA SC060064/TR2, Ocean Science 2026 재확인). skew surge로 조석종속성 회피 — 관측EVA↔JPM 교차검증 틀로 채택 가능.

### 대조차만 surge-only 과대의 정량 근거(경기만 방어 인용처)
- **Li et al. 2022 Frontiers**(항저우만, 대조차): TSI가 해일 ±0.5m(해일고의 ~절반) 변조, 최대해일=저조 슬랙. Bhola1970 선형가산 ~1m 과대.
- **Guo et al. 2025 Frontiers**(샤먼만, 평균조차 4m): 비선형 TSI 첨두 -0.31m(하구 -0.40), 선형중첩 대비 침수면적 **-24%**.
- → 대조차 천해만 surge-only 과대 0.3~1m급 국제 반복확인 = 인천305·평택331 과대와 정합. 목포 관측(std 저조24.7→고조18.5)과 같은 방향.

### Rmax 표집 — 축소의 위험 정량
- **FEMA R2 기준 JPM**: ΔP 7 × **Rp|ΔP 조건부 5노드** × Vf·θ·B 각3 = 945조합 → JPM-OS-Q(Toro 2010, Bayesian quadrature ~1/10 축소)로 159개, **반드시 기준세트 대비 1%·0.2% 수위 오차 검증**.
- **천해일수록 Rmax 민감**(Irish 2008; Gori et al. 2023 JGR-A). Water 2024(MDPI): Rmax 30→15km 보정만으로 최대해일 오차 47.7%→11.8%.
- → 48c의 Rmax 조건부평균 고정은 얕은 경기만에서 특히 위험 — 표적 ±σ 런으로 유계화 + FEMA식 오차 정량화 필수.

### 한국 2023-26 (경쟁·신규성)
- **★MOF 2022 설계값 감사 공표논문 부재**(KCI·JKSCOE·JOET·KWRA 확인) — 우리 논문 신규성 유효.
- 최근접 = 경상국립대(이우동)-KAERI 연작: Jin 2024 KWRA 57-12(가상시나리오 체적지표, "피크 단독 불충분"), **Kim 2025 JOET 39-2(강화 시나리오 남해 내만 5.5~21.8배 증폭 — 검조소EVA 내만 과소평가 반론 근거, §4.2 광양 선제방어 검토)**, Kim 2025 JOET 39-5(TCRM 33앙상블+ADCIRC 한빛원전, 빈도값·MOF비교 없음).
- Liu & Bensi 2025 arXiv:2511.02058: 미국 JPM을 한국 이식 제안 — "한국 JPM 부재" 문제의식 공유.
- **KHOA 2024 「연안재해 위험평가 결과보고서」 존재**(MOF 2022 후속 갱신판 성격) — 감사 대상 버전 확인 필요, 원문 확보 권장.
- 서해 TSI 정량 최신연구도 공백(최신 논거가 Ko et al. 2018, 서해 30년빈도이하 조석기여 90%+).

### 48c 후속 우선순위(이 조사 기준)
① **Zhuge식 통계 TSI 보정**(재실행 최소: 결합/비결합 쌍 몇 런으로 TSI 회귀 → 48c 보정열) ② Rmax ±σ 표적 민감도 런(경기만+남해 대표점) ③ skew-surge 프레임 교차검증 ④ KHOA 2024 보고서 확보.
