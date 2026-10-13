---
file: models/ROMS/raw/source_code/roms/ROMS/Include/cppdefs.h
lines: 763
sha256: 95c42f1ebe00d4b26adbb6f69ee9fa985798e608ca68ae610c1e59a43e7e43ef
reader: codex gpt-6.1-sol
read_date: 2026-10-13
---

# cppdefs.h — 판독 구간 기록

구간은 1행부터 763행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–62 | 시작 시 열린 전처리 조건 없음. 저작권·라이선스와 CPP 옵션 설명의 큰 주석을 시작한다(1–12). 주석은 운동량 이류 기본값을 3차원 수평 3차 상류 편향(upstream bias), 2차원 수평 및 3차원 수직 4차 중심(centered)으로 적는다(15–18). UV_U3ADV_SPLIT의 이류/점성 분리와 globaldefs.h·hmixing.F를 설명한다(20–28). UV_SADVECTION 사용 제약과 운동량/항력/점성 옵션을 열거한다(30–47). 순압 시간 적분(barotropic time stepping)의 기본 LF-AM3와 Forward-Backward 선택 옵션·LIMIT_BSTRESS를 설명한다(49–62). 이 구간은 옵션 설명 주석이며 매크로를 실행 정의하지 않는다. |
| 63–105 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 추적자 확산·고정장·수동 추적자·평균 연령(mean age)·상태방정식·열/담수 플럭스 보정·염분·복사·수직 스플라인·수형 옵션을 열거한다(63–78). 결빙점 이하 표면 냉각 억제와 MPDATA 보정 플럭스 제한 옵션을 설명한다(80–88). 선택이 없을 때 표준 밀도 야코비안(density Jacobian) 압력 경도와 다른 야코비안 옵션, ATM_PRESS/PRESS_COMPENSATE를 설명한다(90–105). |
| 106–141 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 대기 경계층(atmospheric boundary layer)의 bulk flux 옵션을 설명한다(106–122). 장파복사(longwave radiation)는 LONGWAVE 내부 계산, LONGWAVE_OUT의 하향 입력+상향 계산, 기본 순복사 입력의 세 방법을 적는다(109–115). 파랑 거칠기(wave roughness) 관계 옵션과 심해 근사(deep water approximation)를 열거한다(124–129). 단파복사 알베도(albedo)·운량 보정과 24시간 이상 자료의 일주기(diurnal cycle) 변조를 설명한다(131–141). |
| 142–170 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 3차원·곡선 격자·육해 마스크·체적력(body force)·시간 프로파일링(time profiling)·평균/진단/관측점 출력·빙붕(ice shelf)·단정도(single precision)·구면 격자(spherical grid) 옵션을 열거한다(142–161). 라그랑주 표류자(Lagrangian drifter), 굴(oyster) 행동·표면/바닥 반사·수직 무작위 보행(vertical random walk) 옵션을 설명한다(163–170). |
| 171–215 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. analytical.F의 해석장 옵션을 설명한다(171–174). ANA_BIOLOGY부터 ANA_WWAVE까지 초기장·경계·마스크·너징·대기 입력·점원·플럭스·회전·스펀지(sponge)·수면/수온/염분·기후장·수직 혼합·바람/파랑 옵션을 열거한다(175–214). 구분 주석을 포함한다(215). |
| 216–243 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 운동량 수평 혼합의 VISC_GRID와 S/지오포텐셜(geopotential) 면 옵션을 설명한다(216–220). 추적자의 DIFF_GRID·S/지오포텐셜/등밀도(epineutral) 혼합·기후장 섭동·최대 기울기·최소 성층(stratification)·시간 가중 옵션을 설명한다(222–231). BVF/GLS/MY25/LMD 난류 폐쇄(turbulence closure) 중 하나만 활성화하도록 적고 수직 확산/점성 상한 옵션을 열거한다(233–243). |
| 244–289 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. GLS와 MY25의 기본 수평 3차 상류 편향·수직 4차 중심 이류를 적는다(246–247·263–264). 안정도 함수(stability function), 표면 거칠기·파랑 쇄파·TKE·2차/4차 이류·수평 평활화(smoothing)·스플라인 옵션을 열거한다(249–259·266–270). LMD K-profile parameterization의 BKPP/CONVEC/DDMIX/NONLOCAL/RIMIX/SHAPIRO/SKPP와 Richardson 수(Richardson number) 스플라인 또는 수평/수직 평활화 옵션을 설명한다(272–289). |
| 290–320 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. MB_BBL 계열의 바닥 거칠기·궤도 속도(orbital velocity)·생물/소류사(bedload)/사련(ripple) 옵션과 MB_Z0BL/MB_Z0RIP 동시 사용 주석을 포함한다(290–299). SG_BBL 계열 옵션을 설명한다(301–306). SSW_BBL 계열의 로그 보간(logarithmic interpolation)·파랑 경계층 높이 또는 사용자 높이·형상 항력(form drag)·거칠기 옵션을 열거한다(308–320). |
| 321–349 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 측방 경계(lateral boundary)의 IMPLICIT_NUDGING·RADIATION_2D를 설명한다(321–324). 조석 강제력(tidal forcing)의 전 격자 처리·개방 경계 자료 가산을 설명한다(326–331). 조위만 있을 때 축약 물리(reduced physics)로 유속을 추정하는 설명과 관련 파일명을 적는다(333–340). SSH_TIDES/UV_TIDES·하루 상승 RAMP_TIDES·조석 생성력(tide-generating force)·FSOBC_REDUCED/ADD_FSOBC/ADD_M2OBC를 열거한다(342–349). |
| 350–394 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. ROMS 구동기 옵션을 열거한다(350–393). 수반·접선 선형·representer 모델, 민감도·고유모드(eigenmode)·상관(correlation)·앙상블(ensemble)·특이벡터(singular vector)·4D-Var·최적 관측/섭동·검사·실행 파일 분리·확률 최적(stochastic optimal) 옵션을 설명한다. JEDI와 INITIALIZE_AUTOMATIC 설명도 포함한다(368–369). 구분 주석을 포함한다(394). |
| 395–452 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 접선 선형·representer·수반 모델 옵션을 설명한다(395–445). 충격(impulse)·경계/표면 플럭스/바람 응력(wind stress)의 상태 포함·분석 분리·균형 연산자(balance operator)·공분산(covariance)·품질 관리(quality control)·순방향장(forward solution) 입출력·혼합·합성곱(convolution)·관측 영향(observation impact)·최소화(minimization)·사후 오차(posterior error)·완화·검증 옵션을 열거한다. FULL_GRID는 자료동화(data assimilation)·안정도 분석에서 내부와 경계점을 포함하며 기본은 내부점만 처리한다고 적는다(447–452). |
| 453–500 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. Fennel 질소 기반 모델의 탄소·탈질(denitrification)·퇴적물·산소·Schmidt 수(Schmidt number)·pCO2·인산염·하천 DON·알칼리도(alkalinity) 옵션을 열거한다(453–467). ECB의 질소/탄소·황산염 환원(sulfate reduction)·해리 상수(dissociation constant)·광 감쇠(light attenuation) 등의 옵션을 설명한다(469–486). HYPOXIA_SRM과 NPZD_FRANKS/NPZD_IRON/NPZD_POWELL·철 제한/완화 옵션을 설명한다(488–500). |
| 501–540 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. ECOSIM·BIO_OPTICAL의 수중 분광 광학(spectral light) 옵션을 설명한다(501–504). NEMURO 주석은 HOLLING_GRAZING 또는 IVLEV_EXPLICIT을 선택하도록 적고 기본 implicit IVLEV가 아직 작동하지 않는다고 적는다(506–515). RED_TIDE를 설명한다(517–519). 퇴적물 수송(sediment transport)의 소류사·응집성(cohesive)/비응집성(noncohesive) 바닥·플록 응집(flocculation)·생물 확산(biodiffusion)·밀도 효과·지형 변화(morphology)·퇴적 임계응력(critical stress)·부유사(suspended load) 옵션을 열거한다(521–540). |
| 541–591 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 파랑의 흐름 영향(wave effects on currents), 바닥/표면 streaming·roller·파랑 혼합·소산 모형·WEC_VF·WET_DRY 옵션을 설명한다(541–555). 격자 둥지화(grid nesting)의 보존 검사·양방향 보정·단방향·경계 평균·플럭스 시간 보간(time interpolation) 옵션을 설명한다(557–564). ESMF/NUOPC 또는 MCT를 통한 지구시스템모델(Earth System Model) 결합과 결합 대상·시간 보간/평균 옵션을 열거한다(566–587). 근해·천해(nearshore and shallow water) WET_DRY 설명을 포함한다(588–591). |
| 592–619 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. distribution.F의 mp_assemble/mp_collect/mp_reduce는 기본 저수준 MPI 전송, mp_boundary는 기본 mpi_allreduce라고 적는다(592–599). 구현 선택의 성능이 컴퓨터에 따라 달라지고 벤치마크가 필요하다는 주석을 포함한다(601–607). ASSEMBLE/BOUNDARY/COLLECT/REDUCE별 ALLGATHER/ALLREDUCE 옵션을 열거한다(609–619). MPI 라이브러리 내부는 이 대상 파일에 포함하지 않는다. |
| 620–677 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. NetCDF 입출력의 체크섬(checksum)·파일 수·압축(compression)·지연 동기화(delayed synchronization)·메타데이터·재시작(restart) 속성·고스트점(ghost point)·격자·정밀도·병렬 I/O·물점(water point)·평활화·로그·재시작 옵션을 열거한다(620–643). INLINE_2DIO는 분산 메모리(distributed memory)의 메모리 절감을 위해 3차원 자료를 수직 레벨별 2차원 slab으로 처리한다고 적는다(645–649). 해빙(sea ice)의 열역학·알베도·운동량·유변학(rheology)·이류·플럭스·눈 전환·강도·염분 보정·유출 마스크 옵션을 설명한다(651–668). DEBUGGING의 NetCDF 머리말 날짜/CPP 옵션 생략 목적을 설명한다(670–677). |
| 678–750 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 구분 주석과 이상화 시험 BASIN부터 WINDBASIN, 기후 응용 DAMEE_4, 실제 응용 ADRIA02/NJ_BIGHT/WC13 목록을 포함한다(678–726). 주석은 makefile의 `ROMS_APPLICATION ?= UPWELLING` 선택과 소문자 .h 파일명 변환, 예시 `ROMS_HEADER="upwelling.h"`를 설명한다(731–744). 새 응용의 고유 CPP 플래그와 헤더 작성 안내를 포함한다(746–750). |
| 751–763 | 시작 시 열린 전처리 조건 없음. 시작 시 1행 `/*` 주석 안. 큰 옵션 설명 주석을 닫는다(751). ROMS_HEADER가 정의되어 있으면 해당 매크로가 지정한 헤더를 포함한다(753–754). ELSE는 응용 선택을 요구하는 비주석 문장이다(755–757). 내부 CPP 정의 주석 뒤 `globaldefs.h`를 포함한다(759–763). 원문: `#if defined ROMS_HEADER` (753); `# include ROMS_HEADER` (754); `#else` (755); `#endif` (757); `#include "globaldefs.h"` (763). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 152–153: 옵션 설명 주석은 RP_AVERAGES를 TLM 출력으로 적는다. TL_AVERAGES는 ADM 출력으로 적는다.
- 753–757: ROMS_HEADER가 없을 때 ELSE에는 `CPPDEFS - Choose an appropriate ROMS application.` 비주석 문장이 남는다.
- 464·483: Fennel 옵션 설명의 매크로 표기는 `RW14_C02_SC`이다. ECB 옵션 설명의 매크로 표기는 `RW14_CO2_SC`이다.
