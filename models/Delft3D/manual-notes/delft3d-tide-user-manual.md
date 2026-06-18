---
title: "Delft3D-TIDE User Manual — 조석 조화분석·예측 (개념·식·input reference)"
model: Delft3D
doc: Delft3D-TIDE_User_Manual.pdf
canonical_source: manual
citation_status: verified
verification_method: "Delft3D-TIDE_User_Manual.pdf pdftotext -layout 직접 추출 후 TOC + 핵심 장 페이지 인용. 표지(p.iii 직전, 버전 5.00)·Ch 2 sub-system(p.4)·Ch 8 Conceptual description 지배식/Nyquist/Rayleigh/astronomical coupling/least squares/median error/prediction/tide table(p.45-51)·App A ANALYSIS·PREDICT input format(p.53-62)·App B tidal component base(p.73-75) 인용. 페이지는 매뉴얼 footer 'NN of 95' 기준."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/Delft3D/README.md
---

# Delft3D-TIDE User Manual — 조석 조화분석·예측

> Deltares Delft3D-TIDE는 관측 수위/유속 시계열로부터 조석 조화상수 $A_0, A_i, G_i$를 최소제곱으로 추정(ANALYSIS)하고, 이를 이용해 임의 기간의 조석을 예측(PREDICT)·고저조표 작성(HILOW)·천문인자 계산(ASCON)·Fourier 분석(FOURIER)하는 5개 서브시스템 도구. 본 노트는 GUI 절차가 아니라 **물리/수학(Ch 8)과 input reference(App A/B)**에 집중. 매뉴얼 개요·FLOW 조석경계는 [[delft3d-manuals-overview]], [[delft3d-flow-user-manual]] 참조.

## 문서 정체

- 제목: **Delft3D-TIDE, User Manual — Analysis and prediction of tides** (표지, p.1)
- 발행처: Deltares, Boussinesqweg 1, 2629 HV Delft, The Netherlands (p.1 직후 판권면)
- **Version 5.00, Revision 80716, 3 May 2026** (표지, p.1). Copyright © 2026 Deltares.
- 총 103 PDF 페이지 (본문 footer는 "of 95" 체계).

### 버전 변화 (§1.4, p.3)
| Version | 변경 |
|---|---|
| 1.0 | 모든 입력파일에 header line 5줄, 첫 글자 제한 없음 |
| 2.01 | header line 첫 글자에 `+` 삽입 |
| 5.00 | 공백 포함 경로/파일명 지원 신규 GUI. PREDICT 메모리 550,000으로 증가 → 1분 간격 1년 예측 가능($550000 > 531360 = 369\times24\times60$). SFT/FFT 시계열 수도 550,000(synodic period 369.0일 지원) |

## 전체 TOC (장별 페이지)

| 장 | 제목 | p. |
|---|---|---|
| 1 | Guide to this manual | 1 |
| 2 | Introduction to Delft3D-TIDE | 4 |
| 3 | Getting started (Delft3D module로 진입) | 5 |
| 4 | Menu options (File / Subsystem / Help) | 11 |
| 5 | General operation of the subsystems | 19 |
| 5.1 | ANALYSIS (input `.ina`/`.obs`, output `.pra/.cmp/.hdc/.res/.tka`) | 19 |
| 5.2 | PREDICT (output `.prp/.prd/.tkp`) | 24 |
| 5.3 | HILOW (고저조; output `.prh/.hlw`) | 29 |
| 5.4 | ASCON | 33 |
| 5.5 | FOURIER (SFT / FFT) | 36 |
| 6 | Graphics (Delft3D-QUICKPLOT) | 39 |
| 7 | Tutorial | 40 |
| **8** | **Conceptual description** | **45** |
| — | References | 52 |
| A | Input file formats | 53 |
| B | List of tidal components (internal component base) | 73 |
| C | Filename conventions | 80 |
| D | Messages from Delft3D-TIDE | 83 |
| E | Content of the TIDE tutorial cases | 91 |

## 5개 서브시스템 개요 (§2.1, p.4)

| 서브시스템 | 기능 |
|---|---|
| **Analysis** | 관측 조석 등록계열의 조화분석. 옵션: astronomical coupling, multiple instruments, sub-series(데이터 결측 대응), linear trend, accuracy analysis (p.4) |
| **Predict** | 조화상수 세트로 임의 기간 수위/유속 예측 (p.4) |
| **Hilow** | 공급 시계열(관측/hindcast/예측)에 대한 고저조표 작성 (p.4) |
| **Ascon** | 임의 component·date-time에 대한 조석 주파수·astronomical argument·nodal factor 계산 (p.4) |
| **Fourier** | 시계열 Fourier 분석 (p.4) |

최소 1개월 등록계열로 천문조 부분과 기상조 부분 분리 가능; 400+ 지점에서 사용됨 (p.4).

---

## Chapter 8 — 개념·수학 (핵심)

### 8.1 조석의 수학적 표현 (p.45)

천문조는 sun–moon–earth 중력의 결과. 주요 운동: 지구 자전(1일), 달의 공전(27.32일), 지구 공전(365.25일) (p.45). 관측 조석은 각자 고유 각속도 $\omega_i$를 갖는 단순조화 성분의 합으로 표현. 천해역에서는 advection·진폭/수심비·bottom friction 비선형 상호작용으로 compound·higher harmonic 성분 추가 (p.45).

**일반식 (Eq. 8.1, p.45):**
$$ H(t) = A_0 + \sum_{i=1}^{k} A_i F_i \cos\!\big(\omega_i t + (V_0+u)_i - G_i\big) $$

| 기호 | 의미 (p.45) |
|---|---|
| $H(t)$ | 시각 $t$의 수위 |
| $A_0$ | 일정 기간 평균수위 |
| $k$ | 관련 성분 수 |
| $A_i$ | 성분 $i$의 국지 조석 진폭 |
| $F_i$ | nodal amplitude factor |
| $\omega_i$ | 각속도 |
| $(V_0+u)_i$ | astronomical argument |
| $G_i$ | improved kappa number (= 국지 위상지연, local phase lag) |

- $F$, $(V_0+u)$, $\omega$는 시간의존이며 tidal year book에 tabulate됨. $V_0$=위상보정인자(국지시간↔국제 천체시간 연결, 주파수 의존). $F, u$는 천천히 변하는 진폭/위상 보정(대부분 주파수에서 18.6년 주기) (p.45).
- $A_0, A_i, G_i$는 **위치 의존(국지 특성)** (p.45). 알면 $H(t)$ 예측, 반대로 관측 $W(t_j)$가 있으면 최소제곱으로 추정 (p.45).

### 8.2 조류 (p.46)
조류(수평조)와 수위(수직조)는 동일 현상의 두 표현. Eq.(8.1)이 유속에도 동일 적용($\omega$ 동일, $A_0,A_i,G_i$만 다름). 유속은 벡터이므로 먼저 직교성분(예: N/E)으로 분해 후 스칼라처럼 처리 (p.46).

### 8.3 조석 분석

**8.3.1 수학적 모델 (p.46):** $W(t_j)$로부터 상수 추정. 1개월 데이터로도 양호한 특성화 가능하나 모든 성분 독립 분해는 불가; 1년이면 장주기·소성분도 명시적 분해. mean level slow 변화 대응 위해 trend 항 $Bt$ 추가 가능. $k$개 성분이면 미지수 $(2k+1)$개(trend 포함 시 $(2k+2)$), 최소제곱으로 추정 (Eq.8.2, p.46):
$$ \sum_j \big(W(t_j) - H(t_j)\big)^2 \ \to\ \min $$
모델 정식화의 4개 핵심: ① 측정간격(Nyquist) ② 등록 총기간(Rayleigh) ③ astronomical coupling ④ 최소제곱 해법 (p.46).

**8.3.2 Nyquist 조건 (p.47):** 측정간격 $\Delta t$는 신호 최소 파주기 $T_{min}$의 절반 이하여야 함 (Eq.8.3):
$$ \Delta t \le \tfrac{1}{2} T_{min} $$
- 해양/연안에서 식별 가능 조석 주파수 일반적으로 $<180°/\text{hour}$ → 파주기 $>120$분 → 측정간격 60분이면 충분 (p.47).
- 하구/하천(예: 프랑스 Gironde)은 720 degr/hour(주기 30분)까지 발생 → 측정간격 15분 이하 필요 (p.47).
- Nyquist frequency: $f_{Nyquist} = 180/\Delta t$ [degr/hour]; $\Delta t=1$h이면 180 degr/hour (§5.5, p.38).

**8.3.3 Rayleigh 기준 (p.47):** 독립 분해를 위해 성분 주파수 차이가 최소 (Eq.8.4):
$$ \Delta\omega = \frac{360°}{T} \quad (T=\text{관측기간[hours]}) $$
- $\Delta\omega$는 해당 시계열에서 분해 가능한 최소 Fourier 주파수 성분 (p.47).
- 예: 30일 → $\Delta\omega = 360/(30\times24)=0.5$ degr/hour (Eq.8.5, p.47). 180일→0.08333, 360일→0.04166 (p.48).
- Appendix B가 모든 성분·주파수를 주파수 오름차순으로 제공; 대부분 분석에서 Rayleigh가 선택 가능 성분을 크게 제한 (p.48).

**8.3.4 Astronomical coupling (p.48):** 1개월 계열에서는 반년/1년 데이터로만 분해 가능한 성분을 그냥 넣으면 Rayleigh 위반→불신뢰. 대신 main component 1개와 주파수가 가까운 sub-component들 사이의 **진폭·위상 관계를 사전 규정**, 수치해에서 하나의 "lumped" 성분으로 풀고, 이후 규정 관계로 개별 진폭/위상 복원 (main이 sub보다 충분히 커야 함) (p.48).
- 결합식 (Eq.8.6–8.7, p.48): $\tau$=결합군 수, $\xi$=군 번호, $\lambda_\xi$=군 내 sub-component 수, $\upsilon_\xi$=index.
- 잘 알려진 결합: **(K1,P1), (N2,NU2), (S2,K2)** (p.48).
- 우선 인접 station의 장기 분석 기반 관계 사용; 없으면 App B의 equilibrium tide 관계(진폭비 규정, 위상관계=0) 사용 (p.48).
- Remark: 충분히 길면 이 3군은 항상 독립 분해 권장. **30일 미만(예:15일) 분석 비권장**(너무 많은 결합 → 모델 과경직). 최적은 synodic period 1개월/6개월/1년 (p.48).

**8.3.5 최소제곱 해법 (p.49):** 모델 고정 후 Eq.(8.8) 최소화로 수치해:
$$ \sum_{i=1}^{N}\big(W(t_i)-H(t_i)\big)^2 $$
- $(2k+1)$ 또는 $(2k+2)$ 선형방정식계를 **LU-decomposition**으로 해. 양호 분해엔 $N \gg (2k+2)$ 필요 → 성분 수 최소화 권장 (p.49).

### 8.4 특수 기능 (p.49)
| 기능 | 내용 |
|---|---|
| Trends (8.4.1) | 분해 불가 장주기 또는 풍 등 비천문 현상으로 평균수위 slow 변화/계기 위치변화 시 trend $B_0 t$ 추가 (p.49) |
| Astron. coupled (8.4.2) | §8.3.4 참조; 작은 성분을 main에 묶어 implicit 분해 후 천문관계로 분리 (p.49) |
| Sub-series (8.4.3) | 계기 고장/불신뢰 구간을 gap으로 정의, sub-series별 $F,(V_0+u)$ 별도로 gap 제외 추정 (p.49) |
| Multiple instruments (8.4.4) | 다중 계기 연속 사용 시 sub-series별 $A_{0j},B_{0j}$ 별도, $A_i,G_i$는 전체 계열 기반 (p.49) |
| Accuracy analysis (8.4.5) | 표준편차 + 성분별 median error + residue autocorrelation (p.49) |

**Median error (Eq.8.9, p.50):**
$$ \varepsilon_i = \sqrt{\frac{VV2 \times L_i}{N-Z}} $$
$VV2$=잔차 표준편차, $L_i$=역행렬 해 행렬 i번째 주대각 원소, $N$=관측 수, $Z$=총 미지수 (p.50). 실제 해는 진폭/위상식을 cos/sin식으로 재작성 (Eq.8.10): $A\cos(\omega t-\psi)=a\cos\omega t + b\sin\omega t$ (p.50). Print file `.pra`에 **$VV1$(선형계 condition number 관련), $VV2$(잔차 표준편차)** 출력 (p.50).

### 8.5 조석 예측 (p.50)
$A_0,A_i,G_i$ 세트(문헌 또는 ANALYSIS 결과)로 임의 기간 예측. 흔한 간격: **5, 6, 10, 15, 30, 60분** (p.50). $F, u$ 시간변화 반영 가능, linear trend 포함 가능. 문헌의 $A_i,G_i$는 station 국지시간대 기준 → 예측도 국지시간 (p.50). 참고 자료: UKHO Admiralty Tide Tables(O1,K1,M2,S2만), SHOM(1982) 최대 10성분(SA,Q1,O1,K1,N2,M2,S2,MN4,M4,MS4; 2000년부터 폐지) (p.50).

### 8.6 Tide tables (p.50)
HILOW가 예측/관측 시계열로 고저조 시각·높이 산출. diurnal/semi-diurnal/mixed 특성을 windowing으로 고려, 우발적 peak·측정오류 무시하는 special filter 기법 적용; 결측·계기교체 자동 처리 (p.50). sub-series별 통계(average level, max/min, mean rise/fall) 추가 (p.51). **Eq.(8.1) 미분에 기반하지 않음** → 기상효과 포함 임의 관측계열도 처리 가능; 관측계열 처리 시 physical extreme 검출 옵션 유용(App A.3 filter parameters) (p.51).

---

## Appendix A — Input file format reference

### 공통 규칙 (A, p.53)
- 형식: **free**(순서만 중요), **fixed**(지정 column 범위), **text**(좌측정렬 col.1 시작) (p.53).
- date-time group: `yymmdd hhmmss` (날짜+공백 2칸+시각), 좌측정렬. 예: 1989-10-20 14:55:00 → `891020  145500` (p.53).
- Header lines (1~20줄): 첫 글자 `+`=출력파일로 복사, `*`=복사 안 함. 라인당 최대 255자 (p.53–54).

### A.1 ANALYSIS — `.ina` 입력 (p.53–59)
입력: `.ina`(input data) + `.obs`(observations). 주요 record:

| 항목 | 파라미터 | 의미 / 조건 |
|---|---|---|
| Tidal series | `Nobs` | `.obs`에서 읽을 관측 총수(.obs 6번째 줄 첫 숫자; 5줄 ID header 뒤) (p.54) |
| | `TB`/`TE` | 첫/마지막 관측의 date-time (p.54) |
| | `UNIT` | 단위 텍스트(최대 8자, 예 `CM WATER`; 내부변환 없음) (p.54) |
| Options | `INFO(1:5)` | 5개 옵션 배열 (p.54) |
| | `INFO(1)` | 0=GRAPHICS 파일 없음 / 1=원계열·hindcast·residue 생성 / 2=계기별 평균보정 (p.55) |
| | `INFO(2)` | 0/1 = normal equation matrix 출력 여부(수치문제 진단) (p.55) |
| | `INFO(3)` | 0/1 = accuracy analysis(진폭·위상 mean error + residue autocorr) (p.55) |
| | `INFO(4)` | 0/1 = 평균수위 linear trend(계기별) 계산 여부 (p.55) |
| | `INFO(5)` | inactive option (p.55) |
| Component set | `Ncomp` | 선택 main 성분 수, **≤234** (p.55) |
| | `COMP(i)` | App B의 234개 내부 성분명, **대문자·좌측정렬**, 주파수 오름차순 권장 (p.55) |
| Coupled groups | `Ncoupl` | 결합군 수, **0≤Ncoupl≤10** (p.56) |
| | `MAIN(i) SUB(i,j) RHO(i,j) PSI(i,j)` | main명 + sub명 + 진폭비 + 위상차(한 군=한 record). RHO=sub진폭/main진폭, PSI=sub천문위상−main천문위상, `Nsub(i)≤10`, free format (p.56) |
| Instruments | `Nins`, `N1(i)/N2(i)`, `T1ins/T2ins` | 계기 수 **≤10**, 각 계기 첫/마지막 관측 sequence number와 date-time (p.56) |
| Sub-series | `Nsub`, `T1sub/T2sub` | sub-series 수 **≤10**(최소1=무결측 단일계열), 각 sub의 첫/마지막 date-time (p.56) |
| Block filter | `Afilter Nfilter Mfilter` | HILOW용 smoothing; 조석/비조석 극값 분리(계기오류·기상효과) (p.56) |

### A.2 PREDICT 입력 (p.60–62)
| 항목 | 의미 |
|---|---|
| `COMP(i)` | App B 성분명, 대문자, format A8 (p.60) |
| `A(i)` | station 진폭(예측 시계열 단위 결정), format F10.3, col 9–18 (p.60) |
| `G(i)` | 위상/improved Kappa, **반드시 degrees**, F10.1, col 19–28 (p.60) |
| `DELT` | 예측 time step, **단위 MINUTES** (p.60) |
| Sub-series | `Nsub`, `T1sub A B` — nodal factor $u,F$가 18.61년 주기로 slow 변화하므로 **2개월 초과 예측은 ≤2개월 블록으로 분할**; sub별 $u,F$ 계산으로 정확도 향상. trend $B$는 (sub)series **중간 시점** 기준, record format `A6,2X,A6,F10.3,F10.3` (p.62) |

(HILOW 입력 `.inh`/필터파라미터 §5.3.2 p.32, ASCON §5.4 p.33, FOURIER §5.5 p.36은 본 노트 미상세 — 필요 시 후속)

---

## Appendix B — 내부 component base (p.73–75)

- 총 **234개** 내부 성분: primary(평형조에 등장, 육지無 단일 심해) + compound(primary의 선형결합) (p.73). 각 성분 angular frequency(degr/hour) 제공, primary는 equilibrium tide 상대크기, 결합 후보는 main 대비 equilibrium 진폭관계(위상관계=0) 제공 (p.73).
- **북해**: §A.3 직전 예제의 60-constituent 세트가 좋은 선택 (p.73).
- 우선순위: 결합 필요 시 인접 station 장기 분석 관계 우선, 없을 때만 아래 equilibrium 관계 사용 (p.73).

주요 성분 발췌 (Name | Frequency degr/hour | equilibrium amplitude | coupling relation):

| 성분 | Frequency | eq. amp | coupling |
|---|---|---|---|
| SA | 0.0410686 | 0.01156 | (장주기, band 0) (p.73) |
| MM | 0.5443747 | 0.08254 | (p.73) |
| MF | 1.0980331 | 0.15647 | (p.73) |
| Q1 | 13.3986609 | 0.07343 | 0.191 × O1 (p.73) |
| O1 | 13.9430356 | 0.38358 | (p.74) |
| P1 | 14.9589314 | 0.17543 | **0.328 × K1** (p.74) |
| K1 | 15.0410686 | 0.53496 | (p.74) |
| J1 | 15.5854433 | 0.03022 | 0.079 × O1 (p.74) |
| 2N2 | 27.8953548 | 0.02303 | 0.132 × N2 (p.75) |
| MU2 | 27.9682084 | 0.02776 | 0.031 × M2 (p.75) |
| N2 | 28.4397295 | 0.17398 | **0.191 × M2** (p.75) |
| NU2 | 28.5125831 | 0.03304 | **0.194 × N2** (p.75) |
| **M2** | 28.9841042 | 0.90872 | (최대 성분) (p.75) |
| L2 | 29.5284789 | 0.02663 | 0.029 × M2 (p.75) |
| T2 | 29.9589333 | 0.02476 | 0.059 × S2 (p.75) |
| **S2** | 30.0000000 | 0.42248 | (p.75) |
| R2 | 30.0410667 | 0.00366 | 0.009 × S2 (p.75) |
| **K2** | 30.0821373 | 0.12004 | **0.284 × S2** (p.75) |

→ §8.3.4의 잘 알려진 결합 (K1,P1)·(N2,NU2)·(S2,K2)가 App B의 coupling relation으로 정량화됨 (p.74–75).

---

## FOURIER 보조 개념 (§5.5, p.36–38)

- **Synodic period**: 주요 조석 주기 배수를 포함하는 시간간격; FOURIER 지원값 **15.0, 29.5, 30.0, 355.0, 369.0 일** (p.37). 잔차 시계열 Fourier 분석은 길이를 synodic period에 (거의) 맞추는 것이 바람직(스펙트럼이 주요 조석 주파수 포함) (p.37).
- **Tidal band 0–12**: 동일 diurnality 성분 묶음. band 2 = 하루 약 2회(M2 대표), band 0 = 장주기. 특정 band로 제한 시 계산 속도 향상 (p.37).
- **FFT**: Markel and Ritea 방법, 데이터 수는 2의 거듭제곱 기대; 긴 시계열(수천 step+)에 유용 (p.38).

## 미커버 / source-needed
- §3–4 GUI 절차, §5.x 각 서브시스템 실행 상세, App C(filename conventions), App D(error/warning 메시지), App E(tutorial cases) — 본 노트 범위 외(reference 필요 시 후속).
- HILOW `.inh` filter parameter(Afilter/Nfilter/Mfilter) 상세값, ASCON 출력 포맷, FOURIER 입력 — ⚠ 미상세.
