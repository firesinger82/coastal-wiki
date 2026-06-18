---
title: "ROMS Exercises 1-9 + tidal_ellipse 카탈로그 (WC13 4D-Var 실습 인덱스)"
model: ROMS
doc: WC13 4D-Var Tutorial Exercises (Exercise_1~9.pdf), tidal_ellipse.pdf (Zhigang Xu, 2000)
canonical_source: manual
citation_status: verified
verification_method: "각 Exercise_N.pdf 를 pdfinfo 로 페이지 수 확인 후 pdftotext 로 표지(p1)+필요시 p2 직접 추출. tidal_ellipse.pdf 는 CID Identity-H 폰트라 pdftotext 추출 불가 → pdftoppm 으로 p1(표지+Contents)·p2(서문) PNG 렌더 후 직접 read, 동봉 ap2ep.m 헤더(file:line)로 e-parameter 정의 교차확인. 모든 page 인용은 직접 추출/렌더 확인."
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-18
related:
  - models/ROMS/README.md
---

# ROMS Exercises 1-9 + tidal_ellipse 카탈로그 (WC13 4D-Var 실습 인덱스)

> ROMS 소스트리 `roms_test/WC13/` 에 동봉된 9개 실습 PDF 는 범용 ROMS 입문 튜토리얼이 아니라 **WC13 (U.S. West Coast, 30 km / 30 level, California Current System) 테스트케이스를 대상으로 한 4D-Var 자료동화 강의 실습 시리즈**다. 각 Exercise 는 Lecture N 강의와 짝을 이루며 primal(I4D-Var) → dual(RBL4D-Var) → weak constraint → observation impact/sensitivity → array modes → forecast impact/sensitivity 순으로 누적 진행된다. 별도로 `roms_matlab/tidal_ellipse/` 의 tidal_ellipse.pdf 는 Zhigang Xu(BIO, 2000)의 조석타원/연직 조류속 프로파일 MATLAB 툴박스 문서다.

## WC13 공통 설정 (Exercise 1-9 베이스)

| 항목 | 값 | 출처 |
|---|---|---|
| 도메인 | U.S. 서해안 / California Current System (WC13) | Ex1 p1 |
| 해상도 | 수평 30 km, 연직 30 level | Ex1 p1 |
| 동화 사이클 | 3–6 Jan 2004 (Ex1 기본) | Ex1 p1 |
| Control vector $\delta z$ | 초기조건 $\delta x(t_0)$ + 표면강제력 $\delta f(t)$ + 개방경계 $\delta b(t)$ | Ex1 p1 |
| Prior 강제력 | 풍응력·열속·담수속(ROMS bulk flux, COAMPS 근지표 대기자료) | Ex1 p2 |
| 개방경계 prior | global ECCO (Wunsch & Heimbach 2007), Chapman+Flather | Ex1 p2 |
| 동화 관측 | 위성 SST, Aviso gridded SSH, Argo·GLOBEC/LTOP·CalCOFI 수온·염분 | Ex1 p2 |

> ⚠ Exercise 파일들은 PDF 표지에 별도 발행연도가 없으나 본문이 Moore et al.(2011) experiments 를 참조하므로 ROMS 4D-Var tutorial 계열(Moore/Arango 그룹)임. 강의(Lecture N) 본체는 PDF 에 미포함.

## Exercise 카탈로그

| Ex | 제목 (verbatim) | 페이지 | 위치(CPP/디렉토리) | 주제·학습목표 |
|---|---|---|---|---|
| 1 | EXERCISE 1: Incremental, Strong Constraint 4D-Var | 4 p | `WC13/I4DVAR` | Primal form **I4D-Var** (강제약). WC13 으로 1회 동화 사이클(3–6 Jan 2004) 수행, control vector = IC+강제력+경계 증분. 입문 베이스라인. (Ex1 p1) |
| 2 | EXERCISE 2: I4D-Var with Multiple Outer-loops | 1 p | `WC13/I4DVAR` | Ex1 반복 변형. **outer-loop** 개념 — 비선형 cost $J_{NL}$ 를 연속 선형 최소화로 근사. `Ninner*Nouter~25` 조합을 바꿔 효과 관찰. (Ex2 p1) |
| 3 | EXERCISE 3: Dual Formulation 4D-Var - RBL4D-Var | 3 p | `WC13/RBL4DVAR` | Dual form **RBL4D-Var** (관측공간). primal vs dual 비교. 3 가지 preconditioning: $R^{-1/2}$+CG / $R^{-1/2}$+MINRES / RPCG. NHIS(2h vs daily) 로 tangent-linear 근사 타당성 실습. (Ex3 p1) |
| 4 | EXERCISE 4: Weak Constraint Dual Formulation 4D-Var | 3 p | `WC13/RBL4DVAR` | **약제약(weak constraint)** RBL4D-Var(RPCG). 모델오차 보정항을 control vector 에 추가. Broquet et al.(2011)·Crawford et al.(2016) upwelling SST 모델오차 사례. (Ex4 p1) |
| 5 | EXERCISE 5: Analysis Cycle Observation Impacts | 2 p | `WC13/RBL4DVAR_analysis_impact` | **관측 impact** — gain $\tilde K^T$ 의 adjoint 로 37°N 상층 500 m 평균수송 $I_{37N}$ 에 대한 각 관측의 기여 $\Delta I$ 계산. (Ex5 p1) |
| 6 | EXERCISE 6: Analysis Cycle Observation Sensitivity | 2 p | `WC13/RBL4DVAR_analysis_sensitivity` | **관측 sensitivity** — $(\partial K/\partial y)^T$ 로 관측·관측배열 변화에 대한 $I_{37N}$ 민감도. (4D-Var)$^T$ = inner-loop 역순 재실행 + Lanczos adjoint. (Ex6 p1) |
| 7 | EXERCISE 7: Reduced-Rank Array Modes | 2 p | `WC13/ARRAY_MODES` | **Array modes** — preconditioned stabilized representer 행렬 고유쌍. 비물리 노이즈 모드 배제(과적합 방지), Bennett & McIntosh(1984) "1% rule" 로 inner-loop 종료점 추정. (Ex7 p1) |
| 8 | EXERCISE 8: Forecast Cycle Observation Impacts | 6 p | `WC13/RBL4DVAR_forecast_impact` | **예보 사이클 관측 impact** — 분석-예보 사이클(FCSTA red vs FCSTB green) 구성, 예보오차 metric $e=(x_f-x_t)^TC(x_f-x_t)$ 로 동화 관측이 예보 skill 에 준 영향 정량화. 다단계 절차. (Ex8 p1-2) |
| 9 | EXERCISE 9: Forecast Cycle Observation Sensitivities | 2 p | `WC13/RBL4DVAR_forecast_sensitivity` | **예보 사이클 관측 sensitivity** — Ex8 와 set-up 동일, step 5·8 만 상이. $\delta e$ 를 3차까지 전개, $(\partial K/\partial y)^T$ = 전체 ROMS 4D-Var adjoint. CPP: `RBL4DVAR_FCT_SENSITIVITY`+`AD_IMPULSE`+`RPCG`. (Ex9 p1) |

### 진행 의존성

- **Ex1 → Ex2**: Ex2 는 Ex1 의 outer-loop 변형(같은 `I4DVAR` 디렉토리).
- **Ex3 → Ex4**: Ex4 는 Ex3 의 약제약 확장(같은 `RBL4DVAR` 디렉토리).
- **Ex5/6**: RBL4D-Var(Ex3) 선행 필수 — 분석 사이클 impact/sensitivity 짝.
- **Ex8 → Ex9**: Ex9 는 Ex8 의 forecast NetCDF(FCSTAT/FCSTA/FCSTB) 재사용, step 1-4·7 공유.

## tidal_ellipse.pdf — 조석타원 변환 & 연직 조류속 프로파일 (Zhigang Xu, 2000)

> 위치: `roms_matlab/tidal_ellipse/tidal_ellipse.pdf` (20 p). 제목 **"Ellipse Parameters Conversion and Vertical Velocity Profiles for Tidal Currents"**, 저자 Zhigang Xu (Ocean Science Division, Fisheries and Oceans Canada / Bedford Institute of Oceanography, Dartmouth NS), 발행 November 21, 2000. (표지 p1 렌더 확인)

ap-파라미터(진폭·위상지연)와 e-파라미터(조석타원)의 상호변환 및 선형 조석 운동량방정식 decoupling 으로 연직 조류속 프로파일을 푸는 MATLAB 툴박스 문서. (서문 p2)

### 목차 (표지 Contents, page 직접 확인)

| 절 | 제목 (verbatim) | page |
|---|---|---|
| 1 | **Theory** | 3 |
| 1.1 | Tidal ellipse and rotary components | 3 |
| 1.2 | Decoupling of the linear tidal momentum equations | 7 |
| 1.3 | Solutions to $w_p$ and $w_m$ when $\nu$ is depth invariant | 8 |
| 2 | **Programs** | 11 |
| 2.1 | ap2ep.m | 11 |
| 2.2 | ep2ap.m | 13 |
| 2.3 | plot_ell.m | 14 |
| 2.4 | example.m | 17 |
| 2.5 | cBEpm.m | 18 |

### 동봉 MATLAB 함수 (디렉토리 실파일)

| 파일 | 역할 |
|---|---|
| `ap2ep.m` | ap-파라미터 → e-파라미터(SEMA, ECC, INC, PHA, w) 변환 (ap2ep.m:1) |
| `ep2ap.m` | e-파라미터 → ap-파라미터 (역변환) |
| `cBEpm.m` | 연직 조류 프로파일 계산(rotary $w_p$/$w_m$) |
| `plot_ell.m` | 조석타원 작도 |
| `example.m` | ap2ep/ep2ap 사용 데모 |
| `tanh_v5_2.m` | 보조(MATLAB v5 호환 tanh) |

**e-파라미터 정의** (ap2ep.m:22-33, verbatim 발췌):
- `SEMA`: Semi-major axes, 최대 유속
- `ECC`: Eccentricity = semi-minor/semi-major; 음수면 시계방향 회전
- `INC`: Inclination, semi-major 축과 u-축 사이 각(deg)
- `PHA`: Phase angle, 최대유속 도달 시각 $=\omega t_{max}$ (deg)

> 문서 본체(이론 §1)는 CID Identity-H 폰트(Unicode 매핑 없음)로 pdftotext 추출 불가 → 표지·서문만 렌더 확인. §1.2-1.3 수식 본문은 ⚠ 미확인 (필요 시 페이지별 PNG 렌더 추가).

## 출처

- `models/ROMS/raw/source_code/roms_test/WC13/I4DVAR/Exercise_1.pdf` ~ `Exercise_9.pdf` (각 해당 RBL4DVAR* / ARRAY_MODES 서브디렉토리)
- `models/ROMS/raw/source_code/roms_matlab/tidal_ellipse/tidal_ellipse.pdf` 및 동봉 `.m` 파일
