# ADCIRC 노트 전수 검증 — 묶음 A

검증일: 2026-10-12.

대상은 `git diff -U0 c6d72f64 8a943078 -- <노트>`의 추가 줄 전부다. 작업 직전에 대상 노트의 현재 내용을 다시 읽었다. 대상 추가 줄은 현재 파일에서도 모두 식별했다.

코드와 rst의 인용 위치는 `nl -ba`로 주변 줄과 함께 열었다. 조건·비교 연산자·바깥 분기·전처리 조건·변수·수치·단위·실행 경로·식·문서 의미를 대조했다. 수정안의 범위는 기존 비교 보고서 §4와 호출 흐름 보고서 §6–7의 주장 및 원문에서 확인한 조건·분기 보완으로 제한했다.

코드·rst의 상대 경로 기준은 `models/ADCIRC/raw/source_code/adcirc/`다. 아래 노트 링크의 줄 번호는 작업 후 파일을 가리킨다. 괄호의 `+줄` 번호는 커밋 `8a943078`의 줄 번호다.

## 대조한 추가 줄 수

집계 단위는 원래 diff의 `+` 줄이다. 한 줄에 여러 문장이 있어도 한 줄로 센다. 같은 줄에 정정과 보완이 함께 있으면 정정으로 센다. 빈 줄·표 구분선·코드 울타리·메타데이터도 전체 대조 수에 포함한다. 이 구조 줄에는 코드 주장 판정을 적용하지 않았으며 변경하지 않았다.

| 노트 | 대조한 + 줄 | 그중 빈 줄 | 정정 | 보완 | 이상 없음 |
| --- | ---: | ---: | ---: | ---: | ---: |
| [adcirc-3d-mode.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md) | 33 | 3 | 1 | 11 | 21 |
| [adcirc-3d-vssol-vertical-scheme.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md) | 3 | 0 | 0 | 2 | 1 |
| [adcirc-baroclinic-coupling.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md) | 12 | 1 | 1 | 5 | 6 |
| [adcirc-boundary-conditions.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-boundary-conditions.md) | 8 | 1 | 0 | 0 | 8 |
| [adcirc-gwce-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-gwce-implementation.md) | 8 | 0 | 0 | 3 | 5 |
| [adcirc-momentum-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md) | 8 | 0 | 0 | 5 | 3 |
| [adcirc-nffr-periodic-flux-boundary.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md) | 9 | 2 | 0 | 1 | 8 |
| [adcirc-parallel-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-parallel-implementation.md) | 70 | 6 | 1 | 3 | 66 |
| [adcirc-timestep-orchestration.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md) | 185 | 7 | 6 | 28 | 151 |
| [adcirc-transport-solver.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-transport-solver.md) | 2 | 0 | 0 | 0 | 2 |
| [adcirc-weir-boundary.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md) | 15 | 1 | 0 | 6 | 9 |
| [adcirc-wetting-drying-implementation.md](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md) | 13 | 0 | 1 | 4 | 8 |
| 합계 | 366 | 21 | 10 | 68 | 288 |

## 정정 목록

| 노트:줄 | 이전 문장 요지 | 새 문장 요지 | 근거 경로:줄과 원문 |
| --- | --- | --- | --- |
| [adcirc-3d-mode.md:43](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:43) (+줄 43) | ABS(IDEN)>=8에서 node/nele 검사 | 양수 IDEN>=8 검사와 ABS>=8 reader 선택을 구분; rank 0 읽기 명시 | `src/couple2baroclinic3D.F:253` `IF (IDEN.GE.8) THEN`<br>`src/couple2baroclinic3D.F:128` `IF (abs(IDEN).GE.8) THEN`<br>`src/couple2baroclinic3D.F:499` `IF (MYPROC.EQ.0) THEN` |
| [adcirc-baroclinic-coupling.md:41](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:41) (+줄 41) | ABS(IDEN)>=8에서 node/nele 검사 | 양수 IDEN>=8 검사와 ABS>=8 reader 선택을 구분; rank 0 읽기 명시 | `src/couple2baroclinic3D.F:253` `IF (IDEN.GE.8) THEN`<br>`src/couple2baroclinic3D.F:128` `IF (abs(IDEN).GE.8) THEN`<br>`src/couple2baroclinic3D.F:499` `IF (MYPROC.EQ.0) THEN` |
| [adcirc-parallel-implementation.md:230](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:230) (+줄 230) | WarnElevSum 호출부에도 MPI 조건이 있는 것으로 기술 | MPI 합산 구현과 호출부 조건을 구분; WarnElevDump·EarlyTermSum의 CMPI 추가 | `src/timestep.F:1310` `IF(WarnElevDump)THEN`<br>`src/timestep.F:1311` `call WarnElevSum(WarnElevExceeded)`<br>`src/timestep.F:1333` `call WarnElevSum(ErrorElevExceeded)`<br>`src/messenger.F90:1388` `call MPI_ALLREDUCE(WarnElevExceeded, SumWarnElevExceeded, kount, &`<br>`src/timestep.F:1472` `#ifdef CMPI` |
| [adcirc-timestep-orchestration.md:189](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:189) (+줄 184) | 외부/내부 위어를 SET_SUBMERGED64_AT보다 앞에 배치 | 외부 위어만 먼저 배치하고 내부 위어는 침수 판정 뒤에 배치 | `src/timestep.F:966` `CALL COMPUTE_EXTERNAL_BOUNDARY_FLUX(I,TIMELOC,QN2(I))`<br>`src/timestep.F:982` `CALL SET_SUBMERGED64_AT(I,J,K,TIMELOC)`<br>`src/timestep.F:1030` `CALL COMPUTE_INTERNAL_BOUNDARY_FLUX(I,J,K,` |
| [adcirc-timestep-orchestration.md:192](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:192) (+줄 186) | SET_SUBMERGED64_AT와 type64 유량의 게이트를 합침 | 침수 상태 판정과 내부 유량 계산의 순서·게이트 구분 | `src/timestep.F:973` `IF(NFLUXIB64.EQ.1) THEN`<br>`src/timestep.F:979` `CASE(64)`<br>`src/timestep.F:982` `CALL SET_SUBMERGED64_AT(I,J,K,TIMELOC)` |
| [adcirc-timestep-orchestration.md:194](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:194) (+줄 187) | 내부 위어를 침수 상태 판정보다 앞에 배치 | 침수 상태 판정 뒤 내부 위어 및 type64 유량을 계산 | `src/timestep.F:1022` `IF(NFLUXIB.EQ.1) THEN`<br>`src/timestep.F:1027` `CASE(4,24,5,25)`<br>`src/timestep.F:1030` `CALL COMPUTE_INTERNAL_BOUNDARY_FLUX(I,J,K,`<br>`src/timestep.F:1033` `CASE(64)`<br>`src/timestep.F:1041` `CALL COMPUTE_INTERNAL_BOUNDARY64_FLUX(I,J,K,` |
| [adcirc-timestep-orchestration.md:200](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:200) (+줄 191) | NCChange/CGWCE_HDP를 LHS·RHS 공통 조건으로 표시 | 좌변 재조립 조건과 조건 블록 밖 우변 조립 구분 | `src/gwce.F:427` `NCIFBLCK: IF(NCChange.GT.0 .or. CGWCE_HDP ) THEN`<br>`src/gwce.F:1000` `DO IE=1,NE` |
| [adcirc-timestep-orchestration.md:208](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:208) (+줄 197) | wetdry→lookup 순서 및 NOLIFA 호출 게이트 | lookup→wetdry 순서와 level0/ADCNETCDF 호출 조건; NOLIFA는 내부 반환 조건 | `src/timestep.F:1078` `IF(level0)THEN`<br>`src/timestep.F:1079` `#ifdef ADCNETCDF`<br>`src/timestep.F:1081` `call getVertLookup()`<br>`src/timestep.F:1083` `call computeWettingAndDrying(it)`<br>`src/timestep.F:1092` `call computeWettingAndDrying(it)`<br>`src/wetdry.F:204` `if (nolifa.ne.2) then` |
| [adcirc-timestep-orchestration.md:254](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:254) (+줄 241) | 3D VSSOL 밀도 갱신을 native 2D BPG에도 연결 | 3D 수송 밀도 지연으로 한정; 2D 경로와 분리 | `src/vsmy.F:1546` `IF(C3D_BTrans) THEN`<br>`src/vsmy.F:1632` `IF(IDEN.GT.1) CALL CALC_SIGMAT_3D ()`<br>`src/timestep.F:859` `IF (C2DDI) CALL BPG2D(IT,TimeLoc)`<br>`src/timestep.F:1127` `IF (C3DVS) THEN` |
| [adcirc-wetting-drying-implementation.md:69](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:69) (+줄 69) | NODECODE를 직전 단계 상태로 설명 | 같은 호출의 선행 처리로 이미 바뀐 NODECODE로 설명 | `src/wetdry.F:275` `NODECODE(I) = 0`<br>`src/wetdry.F:314` `NODECODE(I)=1`<br>`src/wetdry.F:850` `NCTOT=NODECODE(NM1)+NODECODE(NM2)+NODECODE(NM3)` |

## 보완 목록

| 노트:줄 | 이전 문장 요지 | 새 문장 요지 | 근거 경로:줄과 원문 |
| --- | --- | --- | --- |
| [adcirc-3d-mode.md:25](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:25) (+줄 25) | 3D 밀도 적분과 구배 계산 조건 생략 | 비영 IDEN, 젖은 이웃 요소, 보간값 유효성 조건 명시 | `src/timestep.F:2163` `IF((IDEN.GE.1).OR.(IDEN.LE.-1)) THEN`<br>`src/timestep.F:2306` `IF(NCEle.EQ.0) CYCLE`<br>`src/timestep.F:2331` `IF((BCPN2.GT.-990.).AND.(BCPN3.GT.-990.))THEN` |
| [adcirc-3d-mode.md:27](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:27) (+줄 27) | 연직 세 층 BPG의 적용 절점 범위 생략 | 내부 절점 k=2..NFEN-1로 한정 | `src/vsmy.F:1019` `DO k=2,NFEN-1` |
| [adcirc-3d-mode.md:37](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:37) (+줄 37) | 외부 결합의 실행 조건만 표기 | ADCNETCDF 빌드 조건 추가 | `src/cstart.F:348` `#ifdef ADCNETCDF`<br>`src/cstart.F:350` `IF (C2DDI.and.CBaroclinic.and.abs(IDEN).ge.5) THEN` |
| [adcirc-3d-mode.md:41](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:41) (+줄 41) | 2DDI 경압의 fort.11 읽기 | abs(IDEN)<5 텍스트 입력 조건 명시 | `src/read_input.F:3091` `IF (abs(IDEN).lt.5) THEN` |
| [adcirc-3d-mode.md:42](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:42) (+줄 42) | time 차원과 날짜 문자열 읽기의 분기 생략 | 첫 호출·양수 IDEN·DATETIME 및 대체 간격 구분 | `src/couple2baroclinic3D.F:193` `if (BC3D_IT > 1) then`<br>`src/couple2baroclinic3D.F:222` `if (iden.gt.0) then`<br>`src/couple2baroclinic3D.F:223` `#ifdef DATETIME`<br>`src/couple2baroclinic3D.F:246` `BC3D_DT = 3600d0*3d0` |
| [adcirc-3d-mode.md:77](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:77) (+줄 77) | fort.36/37의 RES_BC_FLAG 조건 생략 | fort.36 RES=2/4, fort.37 RES=3/4 추가 | `src/cstart.F:860` `IF ((ABS(RES_BC_FLAG).EQ.2).OR.(ABS(RES_BC_FLAG).EQ.4)) THEN`<br>`src/cstart.F:875` `IF ((ABS(RES_BC_FLAG).EQ.3).OR.`<br>`src/cstart.F:876` `&            (ABS(RES_BC_FLAG).EQ.4)) THEN` |
| [adcirc-3d-mode.md:78](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:78) (+줄 78) | fort.38 RES 조건만 명시 | 양수 IDEN 및 CBaroclinic 바깥 조건 추가 | `src/cstart.F:835` `IF ((CBAROCLINIC).AND.(IDEN.GE.1)) THEN` |
| [adcirc-3d-mode.md:107](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:107) (+줄 107) | 저면 응력을 TK 식으로만 설명 | ISlip 비영 TK 식과 0의 EV·DUDS 식 구분 | `src/vsmy.F:1192` `IF(ISlip.NE.0) THEN`<br>`src/vsmy.F:1187` `IF(ISlip.EQ.0) THEN`<br>`src/vsmy.F:1189` `BSX(NH) = EV(NH,1)*REAL(DUDS)` |
| [adcirc-3d-mode.md:108](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:108) (+줄 108) | VSDISP 호출 조건 생략 | 0 초기화 뒤 IFNLCT=1일 때 VSDISP 호출 | `src/vsmy.F:1200` `DUU(NH) = 0.d0`<br>`src/vsmy.F:1213` `IF(IFNLCT.EQ.1) THEN` |
| [adcirc-3d-mode.md:126](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:126) (+줄 126) | BPG3D 및 수송·상태방정식의 실행 조건 생략 | METONLY/CBaroclinic/C3DVS 및 C3D_BTrans/양수 IDEN 조건 추가 | `src/timestep.F:852` `IF (CBaroclinic) THEN`<br>`src/vsmy.F:1546` `IF(C3D_BTrans) THEN`<br>`src/vsmy.F:1632` `IF(IDEN.GT.1) CALL CALC_SIGMAT_3D ()` |
| [adcirc-3d-mode.md:189](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-mode.md:189) (+줄 189) | IDEN별 출력 필드 순서의 형식 조건 생략 | 인용문을 ASCII 직렬/지역 파일 경로로 한정 | `src/write_output.F:3508` `SELECT CASE(ABS(I3DSD))`<br>`src/write_output.F:3509` `CASE(1)`<br>`src/write_output.F:3511` `IF ((MNPROC.EQ.1).OR.(WRITE_LOCAL_FILES.eqv..true.)) THEN` |
| [adcirc-3d-vssol-vertical-scheme.md:66](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:66) (+줄 66) | VSSOL의 TK 사용 조건 생략 | ISlip=0의 ELSE로 한정 | `src/vsmy.F:997` `IF(ISlip.EQ.0) THEN    !no slip bottom boundary condition`<br>`src/vsmy.F:1002` `ELSE                   ! slip bottom boundary condition` |
| [adcirc-3d-vssol-vertical-scheme.md:85](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-3d-vssol-vertical-scheme.md:85) (+줄 85) | VSSOL의 TK 사용 조건 생략; wetdry의 3D 조건 생략 | ISlip=0의 ELSE로 한정; W1 C3D 조건 추가 | `src/vsmy.F:997` `IF(ISlip.EQ.0) THEN    !no slip bottom boundary condition`<br>`src/vsmy.F:1002` `ELSE                   ! slip bottom boundary condition`<br>`src/wetdry.F:473` `ELSEIF(C3D)THEN` |
| [adcirc-baroclinic-coupling.md:31](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:31) (+줄 31) | time 차원과 날짜 문자열 읽기의 분기 생략 | 첫 호출·양수 IDEN·DATETIME 및 대체 간격 구분 | `src/couple2baroclinic3D.F:193` `if (BC3D_IT > 1) then`<br>`src/couple2baroclinic3D.F:222` `if (iden.gt.0) then`<br>`src/couple2baroclinic3D.F:223` `#ifdef DATETIME`<br>`src/couple2baroclinic3D.F:246` `BC3D_DT = 3600d0*3d0` |
| [adcirc-baroclinic-coupling.md:38](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:38) (+줄 38) | ADCIRC 격자의 MLD 읽기 rank 조건 생략 | MYPROC=0 조건 추가 | `src/couple2baroclinic3D.F:499` `IF (MYPROC.EQ.0) THEN` |
| [adcirc-baroclinic-coupling.md:57](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:57) (+줄 57) | 자유수면 경압 추가 항의 분기 생략 | NOFSBPG, SigTS 유효값/0 분기, TotalArea 조건 명시 | `src/couple2baroclinic3D.F:1057` `#ifndef NOFSBPG`<br>`src/couple2baroclinic3D.F:1095` `IF (SigTS(NM1) < -1d2.or.SigTS(NM2) < -1d2.or.`<br>`src/couple2baroclinic3D.F:1096` `&       SigTS(NM3) < -1d2) THEN`<br>`src/couple2baroclinic3D.F:1132` `IF (TotalArea(J).NE.0.d0) THEN` |
| [adcirc-baroclinic-coupling.md:58](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:58) (+줄 58) | 분산 전달과 NB/NM 사용 분기 생략 | TotalArea, LoadIT_Fric, 외부 결합 및 속성 개수 조건 명시 | `src/couple2baroclinic3D.F:1132` `IF (TotalArea(J).NE.0.d0) THEN`<br>`src/nodalattr.F:2619` `LoadITFric: IF (LoadIT_Fric) THEN`<br>`src/nodalattr.F:2656` `Baroc: IF (CBaroclinic.and.abs(IDEN).ge.5) THEN`<br>`src/nodalattr.F:2666` `IF (omega > NB(I).or.omega < CORIF(I)) THEN`<br>`src/nodalattr.F:2687` `ELSEIF (IT_FricNoOfVals == 3.or.IT_FricNoOfVals == 1) THEN` |
| [adcirc-baroclinic-coupling.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-baroclinic-coupling.md:73) (+줄 73) | NB/NM 및 DispX/Y의 조건 생략 | 속성 개수·외부 결합·LoadIT_Fric·TotalArea 조건 추가 | `src/nodalattr.F:2619` `LoadITFric: IF (LoadIT_Fric) THEN`<br>`src/nodalattr.F:2687` `ELSEIF (IT_FricNoOfVals == 3.or.IT_FricNoOfVals == 1) THEN`<br>`src/couple2baroclinic3D.F:1132` `IF (TotalArea(J).NE.0.d0) THEN` |
| [adcirc-gwce-implementation.md:49](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:49) (+줄 49) | lumped 경로는 대각 역산 | COEFDTemp=0이면 RDIAG=0, 나머지는 역수 | `src/gwce.F:2011` `IF (COEFDTemp(I).eq.0.0d0) THEN`<br>`src/gwce.F:2012` `RDIAG = 0.0d0`<br>`src/gwce.F:2013` `ELSE`<br>`src/gwce.F:2014` `RDIAG = 1.0d0 / COEFDTemp(I)` |
| [adcirc-gwce-implementation.md:90](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:90) (+줄 90) | lumped 경로는 대각 역산 | COEFDTemp=0이면 RDIAG=0, 나머지는 역수 | `src/gwce.F:2011` `IF (COEFDTemp(I).eq.0.0d0) THEN`<br>`src/gwce.F:2012` `RDIAG = 0.0d0`<br>`src/gwce.F:2013` `ELSE`<br>`src/gwce.F:2014` `RDIAG = 1.0d0 / COEFDTemp(I)` |
| [adcirc-gwce-implementation.md:97](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-gwce-implementation.md:97) (+줄 97) | LoadTau0MinMax가 거짓이면 값 복사 | Tau0Dig1=-5 바깥 조건 추가 | `src/nodalattr.F:1977` `IF ( Tau0Dig1.eq.-5 ) THEN` |
| [adcirc-momentum-implementation.md:59](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:59) (+줄 59) | TKM 합성 예를 일반화; 분산 보정 깊이 조건 생략 | TKM 분기와 DP>=1000 조건 명시 | `src/nodalattr.F:2619` `LoadITFric: IF (LoadIT_Fric) THEN`<br>`src/nodalattr.F:2656` `Baroc: IF (CBaroclinic.and.abs(IDEN).ge.5) THEN`<br>`src/nodalattr.F:2757` `IF (IT_FricNoOfVals == 3) THEN`<br>`src/nodalattr.F:2822` `IF (DP(I).LT.1000d0) CYCLE` |
| [adcirc-momentum-implementation.md:67](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:67) (+줄 67) | 심해 분산 보정의 깊이 문턱 생략 | HBREAK>0 및 DP>=1000 조건 명시 | `src/nodalattr.F:2818` `IF (NOLIBF.NE.3.OR.HBREAK.LE.0d0) RETURN`<br>`src/nodalattr.F:2822` `IF (DP(I).LT.1000d0) CYCLE` |
| [adcirc-momentum-implementation.md:68](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:68) (+줄 68) | H가 HBREAK보다 작으면 혼합 마찰 근사 | 거듭제곱 항이 1보다 훨씬 큰 조건으로 한정 | `src/nodalattr.F:2471` `&                     IFHYBF*(1+(HBREAK/H1)**FTHETA)**(FGAMMA/FTHETA)) ), ! hybrid` |
| [adcirc-momentum-implementation.md:74](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:74) (+줄 74) | 시간 가변 Tau0의 TK 계산 조건 생략 | NCChange 또는 CGWCE_HDP 및 시간 가변 플래그 전체 명시 | `src/gwce.F:427` `NCIFBLCK: IF(NCChange.GT.0 .or. CGWCE_HDP ) THEN`<br>`src/gwce.F:437` `IF(C2DDI.AND.`<br>`src/gwce.F:438` `&       ((FullDomainTimeVaryingTau0.or.HighResTimeVaryingTau0)))`<br>`src/gwce.F:439` `&   THEN` |
| [adcirc-momentum-implementation.md:76](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-momentum-implementation.md:76) (+줄 76) | VSSOL의 METONLY 조건 생략 | METONLY가 거짓인 블록으로 한정 | `src/timestep.F:813` `IF (.NOT.METONLY) THEN` |
| [adcirc-nffr-periodic-flux-boundary.md:31](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-nffr-periodic-flux-boundary.md:31) (+줄 31) | 처음 한 번의 시간 간격 입력 | COLDSTART와 NPEBC/subdomainOn 및 NFLUXF/NFFR 조건 추가 | `src/cstart.F:198` `IF (NPEBC) THEN`<br>`src/cstart.F:206` `if (subdomainOn.eqv..false.) then`<br>`src/cstart.F:226` `IF(NFLUXF.EQ.1.AND.NFFR.LE.0)THEN` |
| [adcirc-parallel-implementation.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:73) (+줄 73) | fort.18 레코드 순서의 반복·조건부 읽기를 생략 | READ 묶음 순서와 반복·조건부 레코드 명시 | `src/messenger.F90:350` `do I = 1, MNE`<br>`src/messenger.F90:455` `do J = 1, NEIGHPROC`<br>`src/messenger.F90:463` `do J = 1, NEIGHPROC`<br>`src/messenger.F90:469` `if (C3D .and. present(NSTA3DD_IN) .and. present(NSTA3DV_IN) .and. &`<br>`src/messenger.F90:470` `present(NSTA3DT_IN)) then` |
| [adcirc-parallel-implementation.md:131](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:131) (+줄 131) | GWCE 통신의 분기 생략 | CMPI, ILump, NPERSEG 통신 선택 추가 | `src/gwce.F:1869` `#ifdef CMPI`<br>`src/gwce.F:1871` `IF (ILump.eq.0) THEN ! default, fully consistent LHS`<br>`src/gwce.F:1873` `IF(NPERSEG.GT.0)THEN`<br>`src/gwce.F:2030` `#ifdef CMPI` |
| [adcirc-parallel-implementation.md:217](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-parallel-implementation.md:217) (+줄 217) | forecastRmax 상수 옵션 | 양수 입력 조건 추가 | `wind/aswip.F:2939` `IF ( forecastRmax.gt.0 ) THEN`<br>`wind/aswip.F:2940` `constantRmax=.true.` |
| [adcirc-timestep-orchestration.md:22](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:22) (+줄 22) | SWAN 시간 반복의 빌드 조건 생략 | CSWAN 빌드 조건 추가 | `src/adcirc.F:478` `#ifdef CSWAN` |
| [adcirc-timestep-orchestration.md:30](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:30) (+줄 30) | 시변 수심 NDDT=1만 기술 | abs(NDDT)=2 분기 추가 | `src/timestep.F:519` `IF(abs(NDDT).EQ.2) THEN` |
| [adcirc-timestep-orchestration.md:33](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:33) (+줄 33) | 동적 수위 보정 호출 조건 생략 | 사용 플래그 조건 명시 | `src/timestep.F:646` `if (usingDynamicWaterLevelCorrection.eqv..true.) then` |
| [adcirc-timestep-orchestration.md:37](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:37) (+줄 37) | C3DVS/C2DDI로 경압 선택 | CBaroclinic 바깥 조건 추가 | `src/timestep.F:852` `IF (CBaroclinic) THEN` |
| [adcirc-timestep-orchestration.md:40](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:40) (+줄 40) | 선택 경로의 침수·노출 호출 | level0/ADCNETCDF의 lookup 순서와 ELSE 구분 | `src/timestep.F:1078` `IF(level0)THEN`<br>`src/timestep.F:1079` `#ifdef ADCNETCDF`<br>`src/timestep.F:1081` `call getVertLookup()`<br>`src/timestep.F:1083` `call computeWettingAndDrying(it)`<br>`src/timestep.F:1089` `ELSE`<br>`src/timestep.F:1092` `call computeWettingAndDrying(it)` |
| [adcirc-timestep-orchestration.md:46](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:46) (+줄 46) | 핫스타트 writer 선택 조건 생략 | 출력 시각과 MNWPROH/C3D/CMPI 분기 명시 | `src/timestep.F:1200` `if ((ABS(NHSTAR) > 0 .and. ITEST == IT) .or. (-IHOT == IT)) then`<br>`src/timestep.F:1201` `if( (MNWPROH > 0) ) then`<br>`src/timestep.F:1202` `if( (.not.C3D) ) then`<br>`src/timestep.F:1203` `#ifdef CMPI` |
| [adcirc-timestep-orchestration.md:47](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:47) (+줄 47) | 두 2D 출력 호출을 나열 | earlyterminate에 따른 출력 인수 분기 명시 | `src/adcirc.F:485` `if ( earlyterminate.ne.0 ) then`<br>`src/adcirc.F:488` `else` |
| [adcirc-timestep-orchestration.md:78](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:78) (+줄 78) | 시간 가변 Tau0의 TK 계산 조건 생략 | NCChange 또는 CGWCE_HDP 및 시간 가변 플래그 전체 명시 | `src/gwce.F:427` `NCIFBLCK: IF(NCChange.GT.0 .or. CGWCE_HDP ) THEN`<br>`src/gwce.F:437` `IF(C2DDI.AND.`<br>`src/gwce.F:438` `&       ((FullDomainTimeVaryingTau0.or.HighResTimeVaryingTau0)))`<br>`src/gwce.F:439` `&   THEN` |
| [adcirc-timestep-orchestration.md:86](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:86) (+줄 86) | CH1 갱신의 젖은 절점 조건 생략 | NCI!=0 절점으로 한정 | `src/timestep.F:1834` `IF(NCI.NE.0) CH1(I)=TRANS_LV_B(I)/TRANS_LV_A(I)` |
| [adcirc-timestep-orchestration.md:88](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:88) (+줄 88) | 외부 BPG2D의 FBPG 제외 조건 생략 | abs(IDEN)>=5 및 7/9 제외 조건 구분 | `src/timestep.F:1923` `IF (abs(IDEN).ge.5) THEN`<br>`src/timestep.F:1927` `if (abs(IDEN).ne.7.AND.abs(IDEN).ne.9) then` |
| [adcirc-timestep-orchestration.md:94](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:94) (+줄 94) | GWCE 뒤 침수·노출 호출의 선택 분기 생략 | level0 lookup 경로와 ELSE 호출 구분 | `src/timestep.F:1078` `IF(level0)THEN`<br>`src/timestep.F:1079` `#ifdef ADCNETCDF`<br>`src/timestep.F:1081` `call getVertLookup()`<br>`src/timestep.F:1083` `call computeWettingAndDrying(it)`<br>`src/timestep.F:1089` `ELSE`<br>`src/timestep.F:1092` `call computeWettingAndDrying(it)` |
| [adcirc-timestep-orchestration.md:98](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:98) (+줄 98) | CPRECOR의 침수·노출을 ELSE 호출만으로 인용 | level0/ADCNETCDF 경로도 명시 | `src/timestep.F:1078` `IF(level0)THEN`<br>`src/timestep.F:1079` `#ifdef ADCNETCDF`<br>`src/timestep.F:1081` `call getVertLookup()`<br>`src/timestep.F:1083` `call computeWettingAndDrying(it)`<br>`src/timestep.F:1089` `ELSE`<br>`src/timestep.F:1092` `call computeWettingAndDrying(it)` |
| [adcirc-timestep-orchestration.md:99](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:99) (+줄 99) | 강제력 복사 및 PR2 경계의 조건 생략 | NWS/NRS/CTIP 및 역기압 경계·sponge 조건 추가 | `src/timestep.F:397` `IF((NWS.NE.0).OR.(NRS.NE.0)) THEN`<br>`src/timestep.F:411` `if(CTIP) then`<br>`src/gwce.F:1697` `IF (NO_MET_IN_SPONGE.eqv..false.) THEN`<br>`src/gwce.F:1698` `if (invertedBarometerOnElevationBoundary.eqv..true.) then` |
| [adcirc-timestep-orchestration.md:108](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:108) (+줄 108) | lumped 경로는 대각 역산 | COEFDTemp=0이면 RDIAG=0, 나머지는 역수 | `src/gwce.F:2011` `IF (COEFDTemp(I).eq.0.0d0) THEN`<br>`src/gwce.F:2012` `RDIAG = 0.0d0`<br>`src/gwce.F:2013` `ELSE`<br>`src/gwce.F:2014` `RDIAG = 1.0d0 / COEFDTemp(I)` |
| [adcirc-timestep-orchestration.md:119](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:119) (+줄 119) | SWAN 시간 반복의 빌드 조건 생략 | CSWAN 빌드 조건 추가 | `src/adcirc.F:478` `#ifdef CSWAN` |
| [adcirc-timestep-orchestration.md:139](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:139) (+줄 139) | 핫스타트 형식 선택만 명시 | NetCDF 핫스타트의 빌드 조건과 CASE 추가 | `src/hstart.F:673` `#ifdef ADCNETCDF`<br>`src/hstart.F:674` `CASE(367,368,567,568)` |
| [adcirc-timestep-orchestration.md:156](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:156) (+줄 155) | 다음 회차 설명에서 DO 종료 범위 생략 | DO의 종료 인덱스도 반복을 제한 | `src/adcirc.F:475` `DO ITIME=ITIME_BGN,ITIME_END`<br>`src/adcirc.F:485` `if ( earlyterminate.ne.0 ) then`<br>`src/adcirc.F:487` `exit` |
| [adcirc-timestep-orchestration.md:172](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:172) (+줄 170) | 초반 SPONGE_SHIFT_SOLN의 초기화 조건 생략 | FIRST_ENTER 초기화 분기의 SHIFT로 한정 | `src/timestep.F:427` `IF ( LoadAbsLayerSigma ) THEN`<br>`src/timestep.F:429` `IF ( .NOT. FIRST_ENTER ) THEN`<br>`src/timestep.F:432` `ELSE`<br>`src/timestep.F:444` `CALL SPONGE_SHIFT_SOLN( ) ;` |
| [adcirc-timestep-orchestration.md:174](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:174) (+줄 171) | NDDT2GET를 NDDT=1/2 모두에 연결 | NDDT2GET는 abs(NDDT)=2와 자료 시각 조건으로 한정 | `src/timestep.F:519` `IF(abs(NDDT).EQ.2) THEN`<br>`src/timestep.F:521` `IF(TimeLoc.GT.BTIME2) THEN`<br>`src/timestep.F:531` `CALL NDDT2GET( 141,DP2(:),-99999.d0 )` |
| [adcirc-timestep-orchestration.md:186](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:186) (+줄 182) | CTIP를 helper 호출의 조건처럼 표시 | 호출 조건과 helper 내부 CTIP 조건 구분 | `src/timestep.F:813` `IF (.NOT.METONLY) THEN`<br>`src/timestep.F:845` `call applyTidePotentialForcing(TimeLoc, TimeH)`<br>`src/timestep.F:1521` `IF(CTIP) THEN` |
| [adcirc-timestep-orchestration.md:203](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:203) (+줄 193) | lumped 대각 역산만 표시 | 대각 계수가 0인 분기 추가 | `src/gwce.F:2011` `IF (COEFDTemp(I).eq.0.0d0) THEN`<br>`src/gwce.F:2012` `RDIAG = 0.0d0`<br>`src/gwce.F:2014` `RDIAG = 1.0d0 / COEFDTemp(I)` |
| [adcirc-timestep-orchestration.md:210](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:210) (+줄 198) | predictor에서 wetdry로 바로 연결 | CPRECOR에서는 운동량 predictor와 GWCE corrector를 거친 뒤 wetdry로 진행 | `src/gwce.F:182` `IF(CPRECOR) THEN`<br>`src/gwce.F:192` `CALL Mom_Eqs_New_NC()`<br>`src/gwce.F:198` `CALL GWCE_New_pc(IT,TimeLoc,TimeH)` |
| [adcirc-timestep-orchestration.md:243](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:243) (+줄 230) | GWCE 유량을 QX1/QY1만으로 일반화 | 일반 GWCE_New로 한정하고 corrector의 3수준 구분 | `src/gwce.F:2553` `QX0N1=QX0(NM1)`<br>`src/gwce.F:2556` `QX1N1=QX1(NM1)`<br>`src/gwce.F:2559` `QX2N1=QX2(NM1)` |
| [adcirc-timestep-orchestration.md:247](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:247) (+줄 234) | 침수·노출의 면적 재계산 조건 생략 | NOLIFA=2 및 TotalArea!=0 조건 추가 | `src/wetdry.F:204` `if (nolifa.ne.2) then`<br>`src/momentum.F:715` `IF (TotalArea(I).ne.0.d0) THEN` |
| [adcirc-timestep-orchestration.md:248](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:248) (+줄 235) | NB/NM/MLD 보간·소비 조건 생략 | LoadIT_Fric, NOLIBF, HBREAK ELSE, 깊이 조건 명시 | `src/couple2baroclinic3D.F:806` `IF (LoadIT_Fric) then`<br>`src/couple2baroclinic3D.F:813` `IF (NOLIBF.eq.3) then`<br>`src/couple2baroclinic3D.F:814` `IF (HBREAK.gt.0d0) then`<br>`src/couple2baroclinic3D.F:822` `MLD(J) = CD_F(1,J) + DTRATIO*(CD_F(2,J)-CD_F(1,J))` |
| [adcirc-timestep-orchestration.md:253](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:253) (+줄 240) | 방사 응력 호출 및 보간의 선택 조건 생략 | 자료 시각·NRS·CSWAN·limiter 조건 추가 | `src/timestep.F:690` `IF(TimeLoc>RSTIME2) THEN`<br>`src/timestep.F:699` `#ifdef CSWAN`<br>`src/timestep.F:724` `IF (Limit_WaveStressGrad.eqv..false.) then` |
| [adcirc-timestep-orchestration.md:255](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:255) (+줄 242) | 저면 응력·분산 쓰기를 조건 없이 나열 | ISlip 분기 및 IFNLCT 호출 조건 추가 | `src/vsmy.F:1187` `IF(ISlip.EQ.0) THEN`<br>`src/vsmy.F:1192` `IF(ISlip.NE.0) THEN`<br>`src/vsmy.F:1213` `IF(IFNLCT.EQ.1) THEN` |
| [adcirc-timestep-orchestration.md:256](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-timestep-orchestration.md:256) (+줄 243) | CH1 갱신 및 핫스타트 저장 조건 생략 | wet 절점과 출력 선택·IM=10 바이너리 경로로 한정 | `src/timestep.F:1834` `IF(NCI.NE.0) CH1(I)=TRANS_LV_B(I)/TRANS_LV_A(I)`<br>`src/timestep.F:1200` `if ((ABS(NHSTAR) > 0 .and. ITEST == IT) .or. (-IHOT == IT)) then`<br>`src/write_output.F:5044` `IF (IM.eq.10) THEN`<br>`src/write_output.F:5046` `WRITE(hss % lun,REC=IHOTSTP) CH1Descript % array_g(I)` |
| [adcirc-weir-boundary.md:34](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:34) (+줄 34) | 내부 상류 실제 수두와 0.04 비교 | AVERAGEWEIRFLOW의 ELSE 경로로 한정 | `src/weir_boundary.F90:1847` `#if AVERAGEWEIRFLOW`<br>`src/weir_boundary.F90:1860` `#else`<br>`src/weir_boundary.F90:1862` `RBARWL1 = ETA2(NNBB1) - BARINHT2(I)` |
| [adcirc-weir-boundary.md:41](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:41) (+줄 41) | 상태 해제의 바깥 조건과 이웃 수 분기 생략 | submerged/wet/HTOT 조건 및 NWETNEI<3 분기 추가 | `src/weir_boundary.F90:2116` `if (ISSUBMERGED64(I) /= 0 .and. &`<br>`src/weir_boundary.F90:2117` `NODECODE(NNBB1) /= 0 .and. &`<br>`src/weir_boundary.F90:2118` `HTOT < 4.d0*H0) then`<br>`src/weir_boundary.F90:2153` `if (NWETNEI < 3) then` |
| [adcirc-weir-boundary.md:45](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:45) (+줄 45) | TVW 높이 갱신의 실행 조건 생략 | EXT_TVW/INT_TVW 및 BAR_DEG 조건 명시 | `src/weir_boundary.F90:1741` `if (EXT_TVW) then`<br>`src/weir_boundary.F90:1742` `if (BAR_DEG(BARRIER_INDEX)) then`<br>`src/weir_boundary.F90:1833` `if (INT_TVW) then`<br>`src/weir_boundary.F90:1834` `if (BAR_DEG(I)) then` |
| [adcirc-weir-boundary.md:48](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:48) (+줄 48) | HOT=1이면 offset에 핫스타트 시간 추가 | 핫스타트 형식 CASE와 DEFAULT 분기 추가 | `src/weir_boundary.F90:1105` `case (17, 67, 68, 367, 368, 567, 568)`<br>`src/weir_boundary.F90:1117` `case DEFAULT`<br>`src/weir_boundary.F90:1118` `HOTADD = 0d0` |
| [adcirc-weir-boundary.md:52](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:52) (+줄 52) | 내부 경계 높이 하한을 두 지형고의 최댓값으로 설명 | 선형 높이 루틴의 유형 3 / 최종 높이 / 지형고 분기 구분 | `src/weir_boundary.F90:641` `DEPTH = max(-DP(NBV(MYIDX)), -DP(IBCONN(MYIDX)))`<br>`src/weir_boundary.F90:644` `if (BAR_VARYTYPE(MYIDX) == 3) then`<br>`src/weir_boundary.F90:647` `if (BARHT_FINAL(MYIDX) >= DEPTH) then`<br>`src/weir_boundary.F90:649` `BAR_HEIGHT = BARHT_FINAL(MYIDX)`<br>`src/weir_boundary.F90:659` `BAR_HEIGHT = DEPTH` |
| [adcirc-weir-boundary.md:53](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-weir-boundary.md:53) (+줄 53) | 핫스타트 쓰기 뒤 높이를 복사 | 핫스타트 조건 블록 밖의 높이 복사로 명확화 | `src/timestep.F:1200` `if ((ABS(NHSTAR) > 0 .and. ITEST == IT) .or. (-IHOT == IT)) then`<br>`src/timestep.F:1224` `ENDIF`<br>`src/timestep.F:1227` `IF(NFLUXIB.EQ.1)THEN` |
| [adcirc-wetting-drying-implementation.md:42](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:42) (+줄 42) | D1 노출 조건은 HTOT<=H0 | 현재 wet인 절점에 대한 조건 추가 | `src/wetdry.F:235` `IF(NODECODE(I).EQ.1) THEN` |
| [adcirc-wetting-drying-implementation.md:73](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:73) (+줄 73) | fort.15의 NODEDRYMIN/NODEWETMIN 또는 VELMIN 읽기 | NOLIFA=2 조건 추가 | `src/read_input.F:3020` `IF(NOLIFA.EQ.2) THEN` |
| [adcirc-wetting-drying-implementation.md:96](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:96) (+줄 96) | fort.15의 NODEDRYMIN/NODEWETMIN 또는 VELMIN 읽기 | NOLIFA=2 조건 추가 | `src/read_input.F:3020` `IF(NOLIFA.EQ.2) THEN` |
| [adcirc-wetting-drying-implementation.md:109](/home/firesinger/coastal-wiki/models/ADCIRC/source-analysis/adcirc-wetting-drying-implementation.md:109) (+줄 109) | fort.15의 NODEDRYMIN/NODEWETMIN 또는 VELMIN 읽기 | NOLIFA=2 조건 추가 | `src/read_input.F:3020` `IF(NOLIFA.EQ.2) THEN` |

## 전체 대상 줄 원장

아래 번호는 `8a943078`의 줄 번호다. 전체 대상에서 정정·보완 목록의 줄을 제외한 나머지가 이상 없음이다. 인용 없는 제목·구조 줄도 이 원장에 포함했다.

| 노트 | 전체 대상 + 줄 | 변경하지 않은 + 줄 |
| --- | --- | --- |
| adcirc-3d-mode.md | 6, 17, 25, 27, 37–44, 75–79, 88–90, 96, 98, 102, 104–108, 125–126, 189, 196, 203 | 6, 17, 38–40, 44, 75–76, 79, 88–90, 96, 98, 102, 104–106, 125, 196, 203 |
| adcirc-3d-vssol-vertical-scheme.md | 6, 66, 85 | 6 |
| adcirc-baroclinic-coupling.md | 6, 30–31, 37–41, 57–58, 65, 73 | 6, 30, 37, 39–40, 65 |
| adcirc-boundary-conditions.md | 6, 35, 40–45 | 6, 35, 40–45 |
| adcirc-gwce-implementation.md | 6, 38, 44, 48–49, 89–90, 97 | 6, 38, 44, 48, 89 |
| adcirc-momentum-implementation.md | 6, 56–57, 59, 67–68, 74, 76 | 6, 56–57 |
| adcirc-nffr-periodic-flux-boundary.md | 6, 27–34 | 6, 27–30, 32–34 |
| adcirc-parallel-implementation.md | 6, 73–106, 131, 189–221, 230 | 6, 74–106, 189–216, 218–221 |
| adcirc-timestep-orchestration.md | 6, 22, 29–49, 54–75, 78, 80, 86–88, 93–99, 105–106, 108, 119–243 | 6, 29, 31–32, 34–36, 38–39, 41–45, 48–49, 54–75, 80, 87, 93, 95–97, 105–106, 120–138, 140–154, 156–169, 172–181, 183, 185, 188–190, 192, 194–196, 199–229, 231–233, 236–239 |
| adcirc-transport-solver.md | 6, 32 | 6, 32 |
| adcirc-weir-boundary.md | 6, 28, 34–36, 41, 45–53 | 6, 28, 35–36, 46–47, 49–51 |
| adcirc-wetting-drying-implementation.md | 6, 29, 42, 53, 67, 69, 73, 81, 95–96, 102, 108–109 | 6, 29, 53, 67, 81, 95, 102, 108 |

## 열어 본 근거 범위

아래는 `nl -ba`로 연 코드·rst 범위의 합집합이다. 겹친 범위는 합쳤다. 원래 추가 줄에 있는 코드·rst 인용 위치는 모두 이 범위에 포함된다.

| 경로 | 연 줄 범위 |
| --- | --- |
| `docs/technical_reference/input_files/fort10.rst` | 15–30 |
| `docs/technical_reference/input_files/fort11.rst` | 17–23 |
| `docs/technical_reference/input_files/fort14.rst` | 23–29 |
| `docs/technical_reference/input_files/fort39.rst` | 22–28 |
| `docs/technical_reference/input_files/time_varying_weirs.rst` | 1–6 |
| `docs/technical_reference/parameter_definitions/index.rst` | 25–31, 1284–1294, 1472–1478 |
| `docs/user_guide/running_adcirc/command_line_options.rst` | 38–53, 96–102 |
| `docs/user_guide/special_features/adcirc2d_plus.rst` | 34–40, 45–51, 91–97 |
| `prep/adcprep.F` | 178–259 |
| `prep/prep.F` | 3018–3048, 3061–3072, 3137–3179 |
| `prep/read_global.F` | 226–252 |
| `src/adcirc.F` | 105–125, 169–418, 430–507, 516–636 |
| `src/boundaries.F` | 339–361 |
| `src/constants.F90` | 45–52 |
| `src/couple2baroclinic3D.F` | 1–38, 105–300, 470–520, 627–840, 1025–1148 |
| `src/couple2swan.F` | 206–220, 943–957, 1106–1120, 1309–1323 |
| `src/cstart.F` | 27–45, 190–262, 340–355, 810–982, 1010–1035 |
| `src/driver.F` | 20–90 |
| `src/global_3dvs.F` | 475–497 |
| `src/global.F` | 318–328 |
| `src/globalio.F` | 1657–1671 |
| `src/gwce.F` | 116–140, 166–245, 418–452, 490–547, 994–1045, 1138–1218, 1278–1305, 1382–1403, 1529–1548, 1615–1635, 1685–1715, 1861–1886, 1984–2032, 2120–2140, 2508–2600, 2618–2638, 2690–2735, 3056–3085 |
| `src/harm.F` | 487–506, 609–626, 995–1012, 2022–2075 |
| `src/hstart.F` | 39–61, 500–526, 557–647, 662–694, 1438–1455 |
| `src/itpackv.F` | 59–73 |
| `src/mesh.F` | 140–160, 394–425, 453–496, 1384–1417, 2583–2665, 3372–3398 |
| `src/messenger.F90` | 90–116, 302–505, 1364–1425 |
| `src/momentum.F` | 90–109, 117–182, 300–319, 391–410, 437–450, 703–790, 1119–1141, 1171–1186, 1884–1903 |
| `src/netcdfio.F90` | 7900–7914 |
| `src/nodalattr.F` | 1018–1032, 1807–1821, 1964–1989, 2010–2046, 2327–2341, 2405–2580, 2586–2600, 2609–2624, 2628–2709, 2747–2847 |
| `src/owi_ice.F` | 209–223 |
| `src/read_input.F` | 34–46, 870–945, 1170–1390, 1471–1495, 2496–2545, 3004–3046, 3074–3157, 3418–3438, 4614–4630, 5520–5635, 5845–5912, 6315–6337 |
| `src/rs2.F` | 731–745 |
| `src/sizes.F` | 200–299 |
| `src/sponge_layer.F90` | 118–132, 156–170, 638–652, 748–762 |
| `src/subdomain.F` | 201–215, 267–281, 333–347, 509–523, 556–570, 608–622 |
| `src/subgridLookup.F` | 348–362 |
| `src/terminate.F90` | 49–63 |
| `src/timestep.F` | 10–80, 120–161, 270–665, 676–742, 805–922, 949–1258, 1280–1343, 1413–1482, 1490–1567, 1575–1585, 1620–1676, 1683–1702, 1821–1949, 1960–2022, 2038–2065, 2121–2220, 2240–2358 |
| `src/transport.F` | 40–54, 217–278 |
| `src/vsmy.F` | 138–152, 459–485, 538–569, 578–590, 965–1034, 1125–1220, 1538–1560, 1600–1652, 3874–3888, 3955–3969, 4326–4393 |
| `src/weir_boundary.F90` | 42–54, 234–248, 250–267, 314–356, 559–672, 977–1007, 1059–1151, 1319–1398, 1723–1768, 1770–1784, 1821–1958, 1968–2168, 2177–2191, 2464–2478 |
| `src/wetdry.F` | 112–134, 136–150, 194–389, 456–503, 833–878, 1070–1097, 1125–1152, 1208–1233, 1340–1475 |
| `src/wind.F` | 319–342, 852–872, 1435–1472, 1762–1785, 2081–2105, 7510–7536, 7606–7640, 7765–7796, 9330–9357 |
| `src/write_output.F` | 345–359, 1815–1829, 2176–2190, 2984–2998, 3030–3049, 3460–3558, 4514–4528, 4908–4930, 5036–5053, 5136–5152, 6336–6350, 6428–6442 |
| `src/writer.F` | 88–102, 168–182, 991–1011, 1065–1079 |
| `wind/aswip.F` | 2848–2956 |

PDF의 밀도 다항식은 [_staging/recovery/read/ADCIRC/manuals/pdfs/2004_Pandoe01.pdf/p037-054.md:30](/home/firesinger/coastal-wiki/_staging/recovery/read/ADCIRC/manuals/pdfs/2004_Pandoe01.pdf/p037-054.md:30)의 PDF 54쪽 판독 기록과 대조했다. 이 기록은 `+1.001685E-4*T`와 `-8.2467E-7*T^3*S`에 대응하는 항을 적는다. 해당 두 문장은 수정하지 않았다.

위어 schedule의 `TimeEndSec` 문서 인용은 [website_markdown의 schedule-file/index.md:418](/home/firesinger/coastal-wiki/models/ADCIRC/raw/manuals/website_markdown/home/documentation/users-manual-v53/input-file-descriptions/schedule-file/index.md:418)과 대조했다. 문서 원문은 `**TimeEndSec** – number of seconds since the beginning of the schedule when the change in weir height is complete`다. 이 문장은 수정하지 않았다.

## 검증 범위와 제한

- 변경한 줄의 코드·rst 인용문은 실제 파일의 지정 줄과 다시 대조했다.
- 기존 주장과 관계없는 문체 수정은 하지 않았다.
- 모델을 실행하거나 컴파일하지 않았다.
- git 상태를 바꾸는 명령은 실행하지 않았다.
- 호출 흐름도는 로컬 Mermaid·JSDOM으로 SVG를 생성했다. 글자 크기는 기존 로컬 렌더러의 글꼴 계측값을 사용했다. 브라우저별 화면 배치는 검증하지 않았다.

## 원문을 열지 못한 인용 목록

없음. PDF 인용은 사용자가 지정한 Markdown 판독 기록으로 대조했다.

정정 10, 보완 68, 이상 없음 288
