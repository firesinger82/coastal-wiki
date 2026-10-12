---
title: "EFDC 보조 모듈 맵 — calstepd(dynamic dt CFL) + calvegser(식생 시계열) + cellmask(셀 mask) + negdep(음수수심) + mhkpwr(MHK 터빈) + mod_fields(field) + runcontrol + 로그/유틸(showval/timelog/tmsr/welcome)"
topic: efdc
canonical_source: self
citation_status: verified
verification_method: "models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/ 직접 read — calstepd.f90(387 dynamic dt) + calvegser.f90(69) + cellmask.f90(358) + negdep.f90(311) + mhkpwr.f90(324) + mod_fields.f90(585) + runcontrol.f90(71) + showval/timelog/tmsr/welcome 헤더 file:line 인용."
note_author: "Claude Opus 4.8 (1M context) source-code direct read"
note_date: 2026-06-04
verification_by: "Claude Opus 4.8 (1M context) — 보조 모듈 인벤토리 verbatim"
verification_date: 2026-06-04
related:
  - models/EFDC/source-analysis/efdc_hydro_core.md
  - models/EFDC/source-analysis/efdc_wetdry.md
last_source_check: 2026-10-12 (recovery 차이 결론 반영)
---

# EFDC 보조 모듈 맵

> EFDC+ 최상위의 **보조·제어·유틸 모듈** 종합(물리 solver 외). 전 소스 커버 완결용 map.

## 1. 시간·안정성

- **calstepd.f90**(387): **dynamic time step** — Courant(CFL) 조건으로 `DTDYN` 산출(`ISDYNSTP`). 격자/유속/수심으로 안정 dt 계산, time step 적응(빠른 흐름·얕은 셀 제약). [[efdc_hydro_core]] 의 시간적분 안정.
- **negdep.f90**(311): **음수 수심 처리** — wetting/drying 또는 강한 flux 로 수심이 음수 되는 것 방지(질량 보정·재분배). [[efdc_wetdry]] 보조.

## 2. 격자·셀

- **cellmask.f90**(358): cell **활성/비활성 mask** 설정(LMASKDRY·land/water·boundary type). 계산영역 정의(LA active cell). 격자 전처리.
- **mod_fields.f90**(585): field 변수 module(공간장 자료구조·할당).

## 3. 외력·물리 옵션

- calvegser.f90는 줄기 밀도·줄기 지름·식생 높이를 시간 보간한다. (`calvegser.f90:58` — `RDLPSQ(M) = VEGSERRT(NSTMP)`; `calvegser.f90:59` — `BPVEG(M) = VEGSERBT(NSTMP)`; `calvegser.f90:60` — `HPVEG(M) = VEGSERHT(NSTMP)`) 이 루틴은 PVEGZ도 다시 계산한다. (`calvegser.f90:62` — `PVEGZ(M) = 1.-ALPVEG(M)*BDLTMP`) 이 재계산에는 입력 단계의 PVEGZ 하한을 적용하지 않는다. (`calvegser.f90:62` — `PVEGZ(M) = 1.-ALPVEG(M)*BDLTMP`) 결론: 문서 누락. EFDC+ 12.5의 식생 시계열은 밀도·지름·높이를 갱신한 뒤 입력 단계의 PVEGZ 하한 없이 PVEGZ를 재계산한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p019-036.md:29`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7325` — `PVEGZ(M) = max(1.E-18,(1. - ALPVEG(M)*BDLTMP))  ! *** Turbulence/canopy adjustment factor to increase drag and turbulence. 0-No adjustment, 1-Infinite drag (invalid) (dimensionless)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calvegser.f90:58` — `RDLPSQ(M) = VEGSERRT(NSTMP)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calvegser.f90:59` — `BPVEG(M) = VEGSERBT(NSTMP)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calvegser.f90:60` — `HPVEG(M) = VEGSERHT(NSTMP)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calvegser.f90:62` — `PVEGZ(M) = 1.-ALPVEG(M)*BDLTMP`; [EFDC-theory-wq-vs-code §5 행 L619, L667](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:832))
- 코드는 `NFLAGPWR == 1`일 때 읽은 CTMHK에 장치 밀도 DENMHK를 곱한다 [10-12 검증 보완]. (`input.f90:7427` — `if( NFLAGPWR == 1 )then`; `input.f90:7430` — `CTMHK(M) = CTMHK(M)*DENMHK(M)`; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽) 코드는 `if( LAYFRACM(K) > 0.0 )then` 안에서 최소 작동 속도 이상일 때 CTMHK를 비선형 추력계수로 변환한다. (`mhkpwr.f90:203` — `THRSTCOEF = 4.0*(1.0-SQRT(1.0-CTMHK(M)))/(1.0+SQRT(1.0-CTMHK(M))) !From Roc paper`; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽) (`mhkpwr.f90:199` — `if( LAYFRACM(K) > 0.0 )then`; `mhkpwr.f90:200` — `if( VELUP<VMINCUT(M) )then`) [10-12 전수 검증 보완] 추력은 평가 속도의 제곱에 비례한다. (`mhkpwr.f90:212` — `FMHK = (B(L,K)+1.0)/DXMHK*0.5*THRSTCOEF*VELUP*VELUP*HP(L)*DZC(L,K)*WIDTHMHK(M)*LAYFRACM(K)*DENMHK(M)  ! area is ASSUMED square`; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽) 출력은 그 추력에 국소 속도를 곱한다. (`mhkpwr.f90:214` — `PMHK(L,K) = FMHK*FLOWSPEED(K) !ThrustCoef*|u|u^2*area [m^5/s^3] (will yield different power outputs depending on UPSTREAM)`; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽) 코드 출력에는 밀도 보정의 추가 곱셈이 있다. (`mhkpwr.f90:223` — `PMHK(L,K) = PMHK(L,K)*(B(L,K)+1.0)*1000.0`; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽) Theory 식 10.1–10.2와 Confluence의 단순 속도 세제곱 설명은 이 코드식과 다르다. (`mhkpwr.f90:212` — `FMHK = (B(L,K)+1.0)/DXMHK*0.5*THRSTCOEF*VELUP*VELUP*HP(L)*DZC(L,K)*WIDTHMHK(M)*LAYFRACM(K)*DENMHK(M)  ! area is ASSUMED square`; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽, 식 10.1; EFDC_Theory_Document_Ver_12.pdf, PDF 247쪽·인쇄 234쪽, 식 10.2) 최소 작동 속도 미만의 분기는 `THRSTCOEF = 0.0`을 대입한다. (`mhkpwr.f90:201` — `THRSTCOEF = 0.0`) [10-12 전수 검증 보완] 코드는 `elseif(VELUP<VMAXCUT(M) )then`의 ELSE에서 평가 속도를 `VELUP = VMAXCUT(M)`으로 제한한다. (`mhkpwr.f90:202` — `elseif(VELUP<VMAXCUT(M) )then`; `mhkpwr.f90:206` — `VELUP = VMAXCUT(M)`) [10-12 전수 검증 보완] 결론: 문서 누락. EFDC+ 12.5는 장치 밀도를 반영한 CTMHK를 비선형 변환하고 층 점유율과 유속 제한을 추력에 적용한다. (근거: `models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Marine_Hydrokinetic_Devices.md:22` — `In the *Marine Hydrokinetics Device* form, the *General* tab is shown in [Figure 2](#Figure2), where the user can specify the power extracted from the flow. There are different methods for computing power extracted from flow, though currently only one method is enabled. The method is to use the specified thrust coefficient that is multiplied by velocity cubed. The user may specify the *Velocity Source for Power Calculations required for computation of power*. The available options are local cell velocity and upstream velocity.`<br>`models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Model_Control_Form/Modules/Marine_Hydrokinetic_Devices.md:24` — `In the *MHK Interaction with Flow Field* frame, the user must specify coefficients. Guidance on how to determine these definitions can be found in the SNL user guide ([James, 2010](/wiki/spaces/EEREF/pages/2387016/References)).`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:25`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:26`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/input.f90:7430` — `CTMHK(M) = CTMHK(M)*DENMHK(M)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:156` — `if( (LAYFRACM(K) == 0.0 .and. LAYFRACS(K) == 0.0) .or. FLOWSPEED(K)<1.0E-03) CYCLE  ! no MHK or support or velocity in this layer`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:203` — `THRSTCOEF = 4.0*(1.0-SQRT(1.0-CTMHK(M)))/(1.0+SQRT(1.0-CTMHK(M))) !From Roc paper`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:206` — `VELUP = VMAXCUT(M)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:212` — `FMHK = (B(L,K)+1.0)/DXMHK*0.5*THRSTCOEF*VELUP*VELUP*HP(L)*DZC(L,K)*WIDTHMHK(M)*LAYFRACM(K)*DENMHK(M)  ! area is ASSUMED square`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:175` — `if( UPSTREAM == 1 )then         ! use the upstream flowspeed to assess power extraction (not typical)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:191` — `VELUP = FLOWSPEED(K)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:214` — `PMHK(L,K) = FMHK*FLOWSPEED(K) !ThrustCoef*\|u\|u^2*area [m^5/s^3] (will yield different power outputs depending on UPSTREAM)`; [EFDC-theory-wq-vs-code §5 행 L440, L444, L562, L589, L621, L668](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:783)) 결론: 코드 결함 후보. EFDC+ 12.5의 MHK 출력은 밀도 보정 중복과 출력 단위의 길이 환산이 충돌하는 결함 후보를 포함한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:25`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:194` — `DXMHK = DYP(L)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:211` — `! FMHK = 0.5*ThrustCoef*Area*(U_inf)^2 where U_inf is the upstream velocity, VELUP [m^4/s^2]`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:212` — `FMHK = (B(L,K)+1.0)/DXMHK*0.5*THRSTCOEF*VELUP*VELUP*HP(L)*DZC(L,K)*WIDTHMHK(M)*LAYFRACM(K)*DENMHK(M)  ! area is ASSUMED square`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:214` — `PMHK(L,K) = FMHK*FLOWSPEED(K) !ThrustCoef*\|u\|u^2*area [m^5/s^3] (will yield different power outputs depending on UPSTREAM)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:223` — `PMHK(L,K) = PMHK(L,K)*(B(L,K)+1.0)*1000.0`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mod_var_global.f90:2400` — `real,allocatable,dimension(:)      :: DENMHK       !< density of MHK devices (#/cell) (MHKTYPE)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/calbuoy.f90:137` — `B(L,K) = (RHO1/RHOO)-1._8       ! *** Buoyancy [dimensionless]`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:248` — `EMHK(MHKCOUNT,L) = EMHK(MHKCOUNT,L) + DT*SUM(PMHK(L,KSZ(L):KC))*2.7778E-10  ! factor converts to MW-hr`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/showval.f90:319` — `if( LMHK .and. ETIME > 0.01 ) WRITE(*,'("MHK POWER OUTPUT   ",F10.4," kW")') SUM(PMHK(:,:))*1E-3`; [EFDC-theory-wq-vs-code §5 행 L441](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:784))

결론: C 문서 누락. EFDC+ 12.5는 MHK의 격자면 힘을 수직 평균과 잔차로 나누고 내부 잔차에 차단 보정과 활성 층 수를 곱한다. (추가 근거: `mhkpwr.f90:259–263`은 `if( PB_COEF == 0.0 )then`에서 `BLOCKAGE_RATIO = 1.0 + (ZMAXMHK(M,L)-ZMINMHK(M,L))/HP(L)`을 계산한다. ELSE는 `BLOCKAGE_RATIO = PB_COEF`를 대입한다. :272–273은 이를 평균을 뺀 내부 힘의 배율로 사용한다. 높이 비율 자체와 1+비율은 다르다. Theory 식 10.17–10.25는 이 배율의 독립 정의를 제시하지 않는다. 1을 더한 것이 계산 오류인지 설계 선택인지는 확인하지 못했다. 주석의 fraction 표현은 계산식 설명으로 그대로 쓰지 않는다.) (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:27`<br>문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:28`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:219` — `FXMHK(L ,K) = FXMHK(L ,K) + AWEIGHTXW*SUB(L )*FMHK*UVEC/FLOWSPEED(K)               ! SUB(L)*FMHK(L,K)*(Uvel/q) [m^4/s^2]`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:242` — `FYMHKE(L) = FYMHKE(L)+ABS(FYMHK(L,K))/VELUP;FYMHKE(LN) = FYMHKE(LN)+ABS(FYMHK(LN,K))/VELUP  ! Sum layer force magnitudes for external mode solution (these forces are later multiplied by a directional velocity so they need to be absolute values here)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:260` — `BLOCKAGE_RATIO = 1.0 + (ZMAXMHK(M,L)-ZMINMHK(M,L))/HP(L)  ! This acts as a force multiplier to take the blockage ratio into account. If it is specified as nonzero in MHK.INP, then PB_COEF is used, otherwise it is approximated as the fraction of the water column that is occupied by the turbine`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:267` — `FXMHKA = SUM(FXMHK(L,KSZ(L):KC)*DZC(L,KSZ(L):KC))`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:272` — `FXTEMP(L,K) = BLOCKAGE_RATIO*( FXMHK(L,K)-FXMHKA + FXSUP(L,K)-FXSUPA )*FLOAT(KC-KSZ(L)+1)  ! Pull x-force out of MHK/support layer for internal mode - push forces in other layers`; [EFDC-theory-wq-vs-code §5 행 L446, L447, L448, L449, L450, L451, L452, L453, L454, L455, L456, L457, L458, L460, L461, L462, L463, L464, L622](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:787)) [10-12 결론 검증 보완]

결론: 문서에만 있음. EFDC+ 12.5의 MHK 내부·외부 모드 분리는 독립 평균속도 대입 대신 DZC로 가중한 힘의 평균을 사용한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p235-252.md:28`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/mhkpwr.f90:267` — `FXMHKA = SUM(FXMHK(L,KSZ(L):KC)*DZC(L,KSZ(L):KC))`; [EFDC-theory-wq-vs-code §5 행 L459](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:788))

결론: 문서 누락. EFDC+ 12.5는 식생 항력계수에 셀 면별 상한을 적용한다. (근거: 문서: `_staging/recovery/read/EFDC/manuals/pdfs/EFDC_Theory_Document_Ver_12.pdf/p019-036.md:29`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/caltbxy.f90:803` — `FXVEG(L,K) = min(FXVEG(L,K),CDMAXU)`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/caltbxy.f90:804` — `FYVEG(L,K) = min(FYVEG(L,K),CDMAXV)`; [EFDC-theory-wq-vs-code §5 행 L620](../../../_staging/recovery/compare/EFDC-theory-wq-vs-code.md:833))


## 4. 제어·로그·유틸

- **runcontrol.f90**(71): run control(시뮬레이션 흐름 제어 플래그).
- **showval.f90 / timelog.f90 / tmsr.f90 / welcome.f90**: 화면 출력(진행률·값 표시) / 시간 로깅 / timer / 시작 배너. 진단·로그 유틸.

## 5. 서브디렉토리 모듈 (Transport/ · Utilities/)

- **`Transport/coare36.f90`**(639): **COARE 3.6 bulk flux 알고리즘**(Fairall et al.) — 풍속·기온·습도·SST 로 air-sea 운동량(wind stress)·잠열·현열 flux 계산. ROMS [[../../ROMS/source-analysis/roms_bulk_flux_coare]] 와 동일 계열. EFDC heat budget(temperature 모듈, raw manual `Surface_Heat_Exchange`)의 표면 flux 산출 — heat 전용 source-analysis 노트 미작성(후속).
- **`Transport/mod_diffuser.f90`**(1780): **diffuser/outfall(점 배출구) 모델** — 산업·하수 방류 diffuser 의 jet momentum·부력 plume → 운동량/scalar source. near-field 희석.
- **`Transport/calsft.f90`**(351): surface flux 시계열(scalar 표면 flux 입력).
- **`Utilities/mod_xyijconv.f90`**(491): **xy(물리좌표)↔ij(격자 index) 변환** — 관측위치·track·diffuser 위치를 격자 cell 로 매핑(좌표 변환 유틸).

결론: H 코드 대조 대상 아님. Confluence의 지리 좌표계 설정은 Explorer UI 기능이며 엔진의 지리 좌표·UTM 변환 유틸리티와 구분해야 한다. (근거: `models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Setting_the_Coordinate_System.md:18` — `The ability of the Geographic Coordinate System`<br>`models/EFDC/raw/manuals/confluence/spaces/EK/pages/EFDC_Explorer_12_Knowledge_Base/EFDC_Explorer_12_User_Guide/Working_with_Models/Setting_the_Coordinate_System.md:18` — `The ability of the Geographic Coordinate System to define two-dimensional coordinates longitude and latitude based on the Earth’s surface not only preserves the accuracy of visualizations of data points under a single projection but also avoids spatial distortion of the model and data.`<br>`models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Utilities/mod_convertwgs84.f90:10` — `! *** CONVERT GEOGRAPHIC COORDINATES TO UTM AND REVERSE`; [EFDC-theory-hydro-vs-code §5 행 confluence-36](../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md:739)) [10-12 결론 검증 정정]


**문서와 코드 차이 · eq-2-157**

결론: B 문서 오기(잠정).
문서 식 2.157의 sin 항 앞 부호는 빼기이다.
코드는 `ETOP = 0.057 + 0.554*SINPHJ*FRD2I`로 더하기 형을 쓴다.
2차 문헌 3종의 sin 항 앞 부호도 더하기이다.
(EFDC_Theory_Document_Ver_12.pdf, PDF 63쪽·인쇄 50쪽, 식 2.157; `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/mod_diffuser.f90:981`; 아래 2차 문헌의 식.)
2차 문헌 기준: Lai 외, [Mixing of inclined dense jets in stationary ambient](https://lai-etal-lab.github.io/publication/mixing-of-inclined-dense-jets-in-stationary-ambient/Mixing-of-inclined-dense-jets-in-stationary-ambient.pdf), 식 (4)와 본문; Socolofsky 외, [TAMOC](https://link.springer.com/content/pdf/10.1007/s10652-018-9591-y.pdf), Environ. Fluid Mech. 18 (2018), 1167–1202, 식 (5); [MOHIDJET 매뉴얼](http://www.mohid.com/PublicData/Products/Manuals/MOHIDJET.pdf), 7쪽 JETLAG 표.

Lai 외의 θ는 수평면에서 잰 제트 경사각이다.
문서의 θ는 수평 방위각이다.
코드 SINPHJ는 연직각 PHJ의 사인이다.
기호 정의 부분은 F로 둔다.
(EFDC_Theory_Document_Ver_12.pdf, PDF 62쪽·인쇄 49쪽, 기호 정의; `models/EFDC/raw/source_code/EFDCPlus_Stable/EFDC/Transport/mod_diffuser.f90:955`; Lai 외, 식 (4)와 본문.)
Lee·Cheung(1990) 원본 확인 전까지 부호 판정은 잠정이다.
분모는 판정하지 못했다.
([외부 판정 eq-2-157](../../../_staging/recovery/compare/external-results-ef.md); [대조 보고서 §5 행 eq-2-157](../../../_staging/recovery/compare/EFDC-theory-hydro-vs-code.md#5-차이-결론)) [10-12 외부 원문 판정]

## 6. 연결

- [[efdc_hydro_core]] — calstepd dynamic dt, mod_fields 자료구조
- [[efdc_wetdry]] — negdep·cellmask wet/dry
- coare36 air-sea flux → EFDC temperature/heat 모듈(전용 source-analysis 노트 미작성, raw manual `Surface_Heat_Exchange`)
- [[efdc_turbulence]] / [[efdc_external_mode_solver]] — 본 보조가 지원하는 핵심 solver
