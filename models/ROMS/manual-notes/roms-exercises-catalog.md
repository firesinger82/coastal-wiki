---
title: "ROMS Exercises 1-9 + tidal_ellipse 카탈로그 (WC13 4D-Var 실습 인덱스)"
model: ROMS
doc: WC13 4D-Var Tutorial Exercises (Exercise_1~9.pdf), tidal_ellipse.pdf (Zhigang Xu, 2000)
canonical_source: manual
citation_status: verified
verification_method: "각 Exercise_N.pdf 를 pdfinfo 로 페이지 수 확인 후 pdftotext 로 표지(p1)+필요시 p2 직접 추출. tidal_ellipse.pdf 는 CID Identity-H 폰트라 pdftotext 추출 불가 → pdftoppm 으로 p1(표지+Contents)·p2(서문) PNG 렌더 후 직접 read, 동봉 ap2ep.m 헤더(file:line)로 e-parameter 정의 교차확인. 모든 page 인용은 직접 추출/렌더 확인. 2026-10-14 ROMS recovery 대조 보고서 반영."
last_source_check: "2026-10-14 (recovery 대조 반영)"
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
| 2 | EXERCISE 2: I4D-Var with Multiple Outer-loops | 1 p | `WC13/I4DVAR` | Ex1 반복 변형. **outer-loop** 개념 — 일련의 선형 최소제곱 최소화로 비선형 비용함수 $J_{NL}$의 최소화를 근사하려는 절차. `Ninner*Nouter~25` 조합을 바꿔 효과 관찰. (Ex2 p1) `Ninner*Nouter~25`는 실습 비교 조건이다. 실제 내부 driver 통과 수는 `(Ninner+1)*Nouter`이다. (`ROMS/Drivers/i4dvar_roms.h:292`, `ROMS/Drivers/i4dvar.F:1232`; [da-4dvar:DA1-822](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md)) [10-14 전수 검증 정정] |
| 3 | EXERCISE 3: Dual Formulation 4D-Var - RBL4D-Var | 3 p | `WC13/RBL4DVAR` | Dual form **RBL4D-Var** (관측공간). primal vs dual 비교. 세 가지 해법 조합: $R^{-1/2}$+CG / $R^{-1/2}$+MINRES / RPCG. NHIS(2h vs daily) 로 tangent-linear 근사 타당성 실습. (Ex3 p1) RPCG를 정의하면 rbl4dvar의 최소화기는 rpcg_lanczos이다. MINRES는 일반 congrad 경로 안의 선택이다. (`ROMS/Drivers/rbl4dvar.F:1304–1364`, `ROMS/Utility/congrad.F:4–7`, `ROMS/Utility/congrad.F:577`; [callflow-da:RF2-008](../../../_staging/recovery/flow/ROMS-callflow-da.md)) [10-14 전수 검증 정정] |
| 4 | EXERCISE 4: Weak Constraint Dual Formulation 4D-Var | 3 p | `WC13/RBL4DVAR` | **약제약(weak constraint)** RBL4D-Var(RPCG). 모델오차 보정항을 control vector 에 추가. Broquet et al.(2011)·Crawford et al.(2016) upwelling SST 모델오차 사례. (Ex4 p1) |
| 5 | EXERCISE 5: Analysis Cycle Observation Impacts | 2 p | `WC13/RBL4DVAR_analysis_impact` | **관측 impact** — 분석 관측 영향은 저장된 Lanczos 벡터를 이용한 gain 전치 작용의 근사로 설명한다. 37°N 상층 500 m 평균수송 $I_{37N}$에 대한 각 관측의 기여 $\Delta I$를 계산한다. (Ex5 p1; `ROMS/Utility/rep_matrix.F:12–13`; [da-representer:RT2-400](../../../_staging/recovery/compare/roms-da-representer-vs-code.md)) |
| 6 | EXERCISE 6: Analysis Cycle Observation Sensitivity | 2 p | `WC13/RBL4DVAR_analysis_sensitivity` | **관측 sensitivity** — $(\partial K/\partial y)^T$ 로 관측·관측배열 변화에 대한 $I_{37N}$ 민감도. (4D-Var)$^T$ = inner-loop 역순 재실행 + Lanczos adjoint. (Ex6 p1) 외부 반복 범위는 `AD_OUTER_LOOP : DO my_outer=Nimpact,Nimpact`이다. (`ROMS/Drivers/obs_sen_rbl4dvar_analysis.h:1384`; [da-representer:RT2-401](../../../_staging/recovery/compare/roms-da-representer-vs-code.md)) |
| 7 | EXERCISE 7: Reduced-Rank Array Modes | 2 p | `WC13/ARRAY_MODES` | **Array modes** — preconditioned stabilized representer 행렬의 고유쌍으로 구성한 모드. 비물리 노이즈 모드 배제(과적합 방지), Bennett & McIntosh(1984) "1% rule" 로 inner-loop 종료점 추정. (Ex7 p1) 1% rule은 종료 기본값이 아니다. ([da-4dvar:DA1-822](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md)) [10-14 전수 검증 정정] |
| 8 | EXERCISE 8: Forecast Cycle Observation Impacts | 6 p | `WC13/RBL4DVAR_forecast_impact` | **예보 사이클 관측 impact** — 분석-예보 사이클(FCSTA red vs FCSTB green) 구성, 예보오차 metric $e=(x_f-x_t)^TC(x_f-x_t)$ 로 동화 관측이 예보 skill 에 준 영향 정량화. 다단계 절차. (Ex8 p1-2) 예보 오류 척도는 상태 공간과 관측 공간의 외부 forcing 정의로 구분한다. (`ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:815–829`; [da-representer:RT2-402](../../../_staging/recovery/compare/roms-da-representer-vs-code.md)) |
| 9 | EXERCISE 9: Forecast Cycle Observation Sensitivities | 2 p | `WC13/RBL4DVAR_forecast_sensitivity` | **예보 사이클 관측 sensitivity** — Ex8 와 set-up 동일, step 5·8 만 상이. $\delta e$ 를 3차까지 전개한다. 예보 감도는 `ImpOrd=3` forcing과 선택한 `Nimpact` outer의 동화 수반을 사용한다. CPP: `RBL4DVAR_FCT_SENSITIVITY`+`AD_IMPULSE`+`RPCG`. (Ex9 p1; `ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:573`, `ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:957`, `ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:1128`; [da-representer:RT2-403](../../../_staging/recovery/compare/roms-da-representer-vs-code.md)) |

약제약 전체 최소화기의 수반과 I4DVAR의 첫 외부 반복 역근사를 구분한다. I4DVAR의 구현을 약제약 전체 수반으로 일반화하지 않는다. ([da-4dvar:DA1-823](../../../_staging/recovery/compare/roms-da-4dvar-vs-code.md))

### 진행 의존성

- **Ex1 → Ex2**: Ex2 는 Ex1 의 outer-loop 변형(같은 `I4DVAR` 디렉토리).
- **Ex3 → Ex4**: Ex4 는 Ex3 의 약제약 확장(같은 `RBL4DVAR` 디렉토리).
- **Ex5/6**: RBL4D-Var(Ex3) 선행 필수 — 분석 사이클 impact/sensitivity 짝.
- **Ex8 → Ex9**: Ex9 는 Ex8 의 forecast NetCDF(FCSTAT/FCSTA/FCSTB) 재사용, step 1-4·7 공유.

## tidal_ellipse.pdf — 조석타원 변환 & 연직 조류속 프로파일 (Zhigang Xu, 2000)

> 위치: `roms_matlab/tidal_ellipse/tidal_ellipse.pdf` (20 p). 제목 **"Ellipse Parameters Conversion and Vertical Velocity Profiles for Tidal Currents"**, 저자 Zhigang Xu (Ocean Science Division, Fisheries and Oceans Canada / Bedford Institute of Oceanography, Dartmouth NS), 발행 November 21, 2000. (표지 p1 렌더 확인)

ap-파라미터(진폭·위상지연)와 e-파라미터(조석타원)의 상호변환 및 선형 조석 운동량방정식 decoupling 으로 연직 조류속 프로파일을 푸는 MATLAB 툴박스 문서. (서문 p2)

PDF 2쪽은 조석타원 변환 함수와 연직 조류속 프로파일 함수를 소개한다. ([tidal_ellipse.pdf p.2](../raw/source_code/roms_matlab/tidal_ellipse/tidal_ellipse.pdf#page=2); [tools-guides:RTG-1989](../../../_staging/recovery/compare/roms-tools-guides-vs-code.md))
ROMS `set_tides`나 `step3d_uv`의 지배식 구현 근거로 사용하지 않는다. ([theory-numerics:RTN-412](../../../_staging/recovery/compare/roms-theory-numerics-vs-code.md))

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

## 문서와 코드 차이 (10-14 대조)

문서 판은 ROMS 위키 wikitext(2026-05-03 받음)이다. 쪽별 revid는 [manifest.json](../raw/manuals/wiki/manifest.json)에 있다. 코드 판은 원본 저장소 HEAD `57aecf58`(2026-09-18, roms-4.2 이후 4.3 개발)이다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| callflow-da:RF2-008 | [RPCG와 MINRES의 우선순위](../../../_staging/recovery/flow/ROMS-callflow-da.md) | ` RBL4D-Var_Tutorial.wiki:25 ` <code>&#91;&#91;Options#MINRES\|MINRES&#93;&#93;</code>`                   Minimal Residual Method for 4D-Var minimization `<br>` RBL4D-Var_Tutorial.wiki:25 ` <code>&#91;&#91;Options#RPCG\|RPCG&#93;&#93;</code>`                     Restricted B-preconditioned Lanczos minimization ` | ` ROMS/Drivers/rbl4dvar.F:1304 ` ` # ifdef RPCG `<br>` ROMS/Drivers/rbl4dvar.F:1354 ` ` CALL rpcg_lanczos (ng, iTLM, my_outer, inner, Ninner, Lcgini) `<br>` ROMS/Drivers/rbl4dvar.F:1356 ` ` # else `<br>` ROMS/Utility/congrad.F:577 ` ` # ifdef MINRES ` | C 문서 누락 | RPCG를 정의하면 rbl4dvar의 최소화기는 rpcg_lanczos이다. MINRES는 일반 congrad 경로 안의 선택이다. |
| da-representer:RT2-117 | [예보 감도 식 (1)](../../../_staging/recovery/compare/roms-da-representer-vs-code.md) | ` RBL4D-Var_Forecast_Observation_Sensitivity_Tutorial.wiki:22 ` `  <math display="block">e=(\bold{x}_f-\bold{x}_a)^T\bold{C}(\bold{y}_f-\bold{y})</math>  ` | ` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:815 ` `  #ifdef OBS_SPACE  `<br>` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:820 ` `  WRITE (OBS(ng)%name,90) TRIM(OIFB(ng)%head)  `<br>` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:822 ` `  WRITE (OBS(ng)%name,90) TRIM(OIFA(ng)%head)  `<br>` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:824 ` `  #else  ` | B 문서 오기 | 예보 감도 식 (1)의 양쪽 차이는 같은 상태 공간 변수로 적는다. |
| da-representer:RT2-119 | [영향 쪽의 식 번호 참조](../../../_staging/recovery/compare/roms-da-representer-vs-code.md) | ` RBL4D-Var_Forecast_Observation_Impact_Tutorial.wiki:20 ` `  equation (2)  `<br>` RBL4D-Var_Forecast_Observation_Impact_Tutorial.wiki:21 ` `  equation (3)  ` | ` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:815 ` `  #ifdef OBS_SPACE  ` | B 문서 오기 | 예보 영향 튜토리얼의 식 (2)·(3) 참조는 실제 식과 함께 고친다. |
| da-representer:RT2-167 | [정규화 목록의 모델 STD 파일 오기](../../../_staging/recovery/compare/roms-da-representer-vs-code.md) | ` RBL4D-Var_Analysis_Observation_Sensitivity_Tutorial.wiki:44 ` `  ../Data/wc13_std_m.nc</span>     model error (if weak constraint)  `<br>` RBL4D-Var_Analysis_Observation_Sensitivity_Tutorial.wiki:27 ` ` <div class="box">                       <span class="twilightBlue">Grid File:</span>  ../Data/wc13_grd.nc<br />          <span class="twilightBlue">Nonlinear Initial File:</span>  wc13_ini.nc<br />                 <span class="twilightBlue">Forcing File 01:</span>  ../Data/coamps_wc13_lwrad_down.nc<br />                 <span class="twilightBlue">Forcing File 02:</span>  ../Data/coamps_wc13_Pair.nc<br />                 <span class="twilightBlue">Forcing File 03:</span>  ../Data/coamps_wc13_Qair.nc<br />                 <span class="twilightBlue">Forcing File 04:</span>  ../Data/coamps_wc13_rain.nc<br />                 <span class="twilightBlue">Forcing File 05:</span>  ../Data/coamps_wc13_swrad.nc<br />                 <span class="twilightBlue">Forcing File 06:</span>  ../Data/coamps_wc13_Tair.nc<br />                 <span class="twilightBlue">Forcing File 07:</span>  ../Data/coamps_wc13_wind.nc<br />                   <span class="twilightBlue">Boundary File:</span>  ../Data/wc13_ecco_bry.nc<br /><br />        <span class="twilightBlue">Adjoint Sensitivity File:</span>  wc13_ads.nc<br />     <span class="twilightBlue">Initial Conditions STD File:</span>  ../Data/wc13_std_i.nc<br />                  <span class="twilightBlue">Model STD File:</span>  ../Data/wc13_std_m.nc<br />    <span class="twilightBlue">Boundary Conditions STD File:</span>  ../Data/wc13_std_b.nc<br />        <span class="twilightBlue">Surface Forcing STD File:</span>  ../Data/wc13_std_f.nc<br />    <span class="twilightBlue">Initial Conditions Norm File:</span>  ../Data/wc13_nrm_i.nc<br />                 <span class="twilightBlue">Model Norm File:</span>  ../Data/wc13_nrm_m.nc<br />   <span class="twilightBlue">Boundary Conditions Norm File:</span>  ../Data/wc13_nrm_b.nc<br />       <span class="twilightBlue">Surface Forcing Norm File:</span>  ../Data/wc13_nrm_f.nc<br/>               <span class="twilightBlue">Observations File:</span>  wc13_obs.nc<br />            <span class="twilightBlue">Lanczos Vectors File:</span>  wc13_lcz.nc</div> ` | ` ROMS/Drivers/r4dvar.F:1873 ` `  CALL get_state (ng, 11, 11, STD(2,ng), STDrec, Tindex)  `<br>` ROMS/Drivers/r4dvar.F:1994 ` `  IF (NSA.eq.2) THEN  `<br>` ROMS/Drivers/r4dvar.F:1995 ` `  CALL get_state (ng, 15, 15, NRM(2,ng), NRMrec, 2)  ` | B 문서 오기 | 모델오차 정규화 파일 목록에는 wc13_nrm_m.nc를 적는다. |
| da-representer:RT2-400 | [분석 관측 영향 요약](../../../_staging/recovery/compare/roms-da-representer-vs-code.md) | ` models/ROMS/manual-notes/roms-exercises-catalog.md:40 ` ``  \| 5 \| EXERCISE 5: Analysis Cycle Observation Impacts \| 2 p \| `WC13/RBL4DVAR_analysis_impact` \| **관측 impact** — gain $\tilde K^T$ 의 adjoint 로 37°N 상층 500 m 평균수송 $I_{37N}$ 에 대한 각 관측의 기여 $\Delta I$ 계산. (Ex5 p1) \|  `` | ` ROMS/Utility/rep_matrix.F:12 ` `  !  This routine estimates the TRANSPOSE of the inverse of the          !  `<br>` ROMS/Utility/rep_matrix.F:13 ` `  !  stabilized representer matrix using the Lanczos vectors from        !  ` | C 문서 누락 | 분석 관측 영향은 저장된 Lanczos 벡터를 이용한 gain 전치 작용의 근사로 설명한다. |
| da-representer:RT2-403 | [예보 3차 수반 요약](../../../_staging/recovery/compare/roms-da-representer-vs-code.md) | ` models/ROMS/manual-notes/roms-exercises-catalog.md:44 ` ``  \| 9 \| EXERCISE 9: Forecast Cycle Observation Sensitivities \| 2 p \| `WC13/RBL4DVAR_forecast_sensitivity` \| **예보 사이클 관측 sensitivity** — Ex8 와 set-up 동일, step 5·8 만 상이. $\delta e$ 를 3차까지 전개, $(\partial K/\partial y)^T$ = 전체 ROMS 4D-Var adjoint. CPP: `RBL4DVAR_FCT_SENSITIVITY`+`AD_IMPULSE`+`RPCG`. (Ex9 p1) \|  `` | ` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:573 ` `  ImpOrd=3  `<br>` ROMS/Drivers/obs_sen_rbl4dvar_forecast.h:957 ` `  IF (ImpOrd.gt.1) THEN  ` | C 문서 누락 | 예보 감도는 `ImpOrd=3` forcing과 선택한 Nimpact outer의 동화 수반을 사용한다. |

## 출처

- `models/ROMS/raw/source_code/roms_test/WC13/I4DVAR/Exercise_1.pdf` ~ `Exercise_9.pdf` (각 해당 RBL4DVAR* / ARRAY_MODES 서브디렉토리)
- `models/ROMS/raw/source_code/roms_matlab/tidal_ellipse/tidal_ellipse.pdf` 및 동봉 `.m` 파일
