---
title: "adcirc 3d mode"
topic: general
canonical_source: self
citation_status: verified
last_source_check: 2026-10-11 (recovery 재판독 대조)
has_source_needed: true
verification_method: "ADCIRC source code 직접 분석 (models/ADCIRC/raw/source_code/, codex 보조). 본 노트는 _staging/from-modeling-wiki/knowledge/methods/adcirc-3d-mode.md (at commit a9618df^) (modeling-wiki 4-5월 작성) 의 마이그레이션. source-code 라인 인용은 본문 내 file:line 명시."
note_author: "사용자 + codex source-code 분석 (2026-04~05 modeling-wiki) → Claude Opus 4.7 (1M context) 마이그레이션 2026-05-23"
note_date: 2026-04~05 (original) / 2026-05-23 (promote)
verification_by: "사용자 + codex source-code analysis"
verification_date: 2026-04
---

## Scope

`couple2baroclinic3D.F`는 외부 3D 자료를 2DDI 경압 강제력으로 읽는다 (`src/couple2baroclinic3D.F:137` `BC3D_BX = read_nc_var(NC_ID,'BPGX',BC3D_IT,XIc,NXc,YI,NY)`; `src/couple2baroclinic3D.F:139` `BC3D_BY = read_nc_var(NC_ID,'BPGY',BC3D_IT,XI,NX,YIc,NYc)`). `IM=1·11·21·31`은 `C3D·C3DVS`를 참으로 대입한다 (`src/read_input.F:1190` `ELSEIF (IM.EQ.1) THEN`; `src/read_input.F:1191` `C3D           = .TRUE.`; `src/read_input.F:1192` `C3DVS         = .TRUE.`; `src/read_input.F:1197` `ELSEIF (IM.EQ.11) THEN`; `src/read_input.F:1198` `C3D           = .TRUE.`; `src/read_input.F:1199` `C3DVS         = .TRUE.`; `src/read_input.F:1205` `ELSEIF (IM.EQ.21) THEN`; `src/read_input.F:1206` `C3D           = .TRUE.`; `src/read_input.F:1207` `C3DVS         = .TRUE.`; `src/read_input.F:1213` `ELSEIF (IM.EQ.31) THEN`; `src/read_input.F:1214` `C3D           = .TRUE.`; `src/read_input.F:1215` `C3DVS         = .TRUE.`). `IM=2`는 `C3D·C3DDSS`를 참으로 대입한다 (`src/read_input.F:1222` `ELSEIF (IM.EQ.2) THEN`; `src/read_input.F:1223` `C3D           = .TRUE.`; `src/read_input.F:1224` `C3DDSS        = .TRUE.`). 허용 구간의 여섯 자리 `IM`은 첫 자리가 6 또는 7이면 `C3D·C3DVS`를 참으로 대입한다 (`src/read_input.F:1233` `ELSEIF ((IM.GE.111111).AND.(IM.LE.734323)) THEN`; `src/read_input.F:1267` `ELSEIF(IMDig1.EQ.6) THEN`; `src/read_input.F:1270` `C3D           = .TRUE.`; `src/read_input.F:1271` `C3DVS         = .TRUE.`; `src/read_input.F:1274` `ELSEIF(IMDig1.EQ.7) THEN`; `src/read_input.F:1277` `C3D           = .TRUE.`; `src/read_input.F:1278` `C3DVS         = .TRUE.`). 이 설명은 입력 플래그의 설정 범위다.

## Source basis

- `read_input.F:1190-1205, 3072, 5139-5482, 5682` — `IM, IDEN, IGC/NFEN, EQNSTATE`, 3D output controls.
- `adcirc.F:316-319, 348` — top-level dispatch, baroclinic init.
- `couple2baroclinic3D.F:39-787` — external-coupling module.
- `cstart.F:348` — `Initial_BC3D_NetCDF` call.
- native 3D의 활성 밀도 적분에는 timestep.F의 trapezoidal 경로가 있다 (`src/timestep.F:2169` `IF(densityIntegrationID == DENSITY_INTEGRATION_TRAPEZOIDAL)THEN`; `src/timestep.F:2172` `SigTAvg=(SigT(NH,k+1)+SigT(NH,k))/2.d0`; `src/timestep.F:2174` `BCP(NH,k)=BCP(NH,k+1)+HGORhoOAMB*(SigTAvg-SigT0)*DelSig`). 같은 루틴에는 Simpson 적분 선택 경로도 있다 (`src/timestep.F:2176` `ELSEIF( densityIntegrationID == DENSITY_INTEGRATION_SIMPSON )THEN`). 수평 경압 구배는 같은 실제 z 높이로 보간한 뒤 계산한다 (`src/timestep.F:2309` `Zk=HsOAMB*(Sigma(k)-B)-DP(N1)`; `src/timestep.F:2313` `SigmaNN=B+AMB*(Zk+DP(N2))/HsN2`; `src/timestep.F:2340` `DBCPDX2A=DBCPDX2A+(BCPN1*b1+BCPN2*b2+BCPN3*b3)`; `src/timestep.F:2341` `DBCPDY2A=DBCPDY2A+(BCPN1*a1+BCPN2*a2+BCPN3*a3)`).
- `gwce.F:780-1450` — GWCE 3D additions.
- VSSOL은 연직 세 층의 `BPG`를 운동량 우변에 넣는다 (`src/vsmy.F:1021` `&           -DelT*(LAdvec(k-1)+LStress(k-1)+BPG(NH,k-1)))*Inm(k,1)`; `src/vsmy.F:1023` `&           -DelT*(LAdvec(k)  +LStress(k)  +BPG(NH,k)  ))*Inm(k,2)`; `src/vsmy.F:1025` `&           -DelT*(LAdvec(k+1)+LStress(k+1)+BPG(NH,k+1)))*Inm(k,3)`). 이 노트는 vsmy.F의 옛 BCP 적분 주석을 활성 계산의 근거로 쓰지 않는다.
- `global_3dvs.F:94, 193, 568` — symbols, FEGRIDS.
- `write_output.F:3053-3391` — 3D output dispatch.

## A. Two distinct paths

ADCIRC has **two different 3D paths** that are easy to confuse:

| Path | Activation | What it does |
|---|---|---|
| External baroclinic coupling | `C2DDI .and. CBaroclinic .and. abs(IDEN) >= 5` | 직교·staggered 경로는 `abs(IDEN)!=7`이면 `BPGX·BPGY·SigTS`를 읽는다 (`src/couple2baroclinic3D.F:134` `if (abs(iden).ne.7) then`; `src/couple2baroclinic3D.F:137` `BC3D_BX = read_nc_var(NC_ID,'BPGX',BC3D_IT,XIc,NXc,YI,NY)`; `src/couple2baroclinic3D.F:139` `BC3D_BY = read_nc_var(NC_ID,'BPGY',BC3D_IT,XI,NX,YIc,NYc)`; `src/couple2baroclinic3D.F:141` `BC3D_SigTS = read_nc_var(NC_ID,'SigTS',BC3D_IT,XI,NX,YI,NY)`). `LoadIT_Fric`은 해저 부력진동수 `NB`와 수심 평균 부력진동수 `NM`의 읽기를 제어한다 (`src/couple2baroclinic3D.F:144` `if (LoadIT_Fric) then`; `src/couple2baroclinic3D.F:145` `! Buoyancy frequency at the seabed`; `src/couple2baroclinic3D.F:146` `BC3D_NB = read_nc_var(NC_ID,'NB',BC3D_IT,XI,NX,YI,NY)`; `src/couple2baroclinic3D.F:147` `! Depth-averaged nuoyancy frequency`; `src/couple2baroclinic3D.F:148` `BC3D_NM = read_nc_var(NC_ID,'NM',BC3D_IT,XI,NX,YI,NY)`). 직교·staggered 경로의 `NOLIBF=3` 분기는 `HBREAK>0`이면 `MLD`를 읽는다 (`src/couple2baroclinic3D.F:151` `if (NOLIBF.eq.3) then`; `src/couple2baroclinic3D.F:152` `if (HBREAK.gt.0d0) then`; `src/couple2baroclinic3D.F:154` `BC3D_MLD = read_nc_var(NC_ID,'MLD',BC3D_IT,XI,NX,YI,NY)`). 그 외 `HBREAK` 값에서는 `CDisp`를 읽는다 (`src/couple2baroclinic3D.F:152` `if (HBREAK.gt.0d0) then`; `src/couple2baroclinic3D.F:157` `BC3D_CD = read_nc_var(NC_ID,'CDisp',BC3D_IT,XI,NX,YIs,NYs)`). `abs(IDEN)=6`이면 `DispX·DispY`를 읽는다 (`src/couple2baroclinic3D.F:161` `if (abs(iden).eq.6) then`; `src/couple2baroclinic3D.F:163` `BC3D_DX = read_nc_var(NC_ID,'DispX',BC3D_IT,XI,NX,YIs,NYs)`; `src/couple2baroclinic3D.F:165` `BC3D_DY = read_nc_var(NC_ID,'DispY',BC3D_IT,XI,NX,YIs,NYs)`). |
| Native 3D 입력 플래그 | `IM=1·11·21·31`은 `C3D·C3DVS`를 참으로 대입한다 (`src/read_input.F:1190` `ELSEIF (IM.EQ.1) THEN`; `src/read_input.F:1191` `C3D           = .TRUE.`; `src/read_input.F:1192` `C3DVS         = .TRUE.`; `src/read_input.F:1197` `ELSEIF (IM.EQ.11) THEN`; `src/read_input.F:1198` `C3D           = .TRUE.`; `src/read_input.F:1199` `C3DVS         = .TRUE.`; `src/read_input.F:1205` `ELSEIF (IM.EQ.21) THEN`; `src/read_input.F:1206` `C3D           = .TRUE.`; `src/read_input.F:1207` `C3DVS         = .TRUE.`; `src/read_input.F:1213` `ELSEIF (IM.EQ.31) THEN`; `src/read_input.F:1214` `C3D           = .TRUE.`; `src/read_input.F:1215` `C3DVS         = .TRUE.`). `IM=2`는 `C3D·C3DDSS`를 참으로 대입한다 (`src/read_input.F:1222` `ELSEIF (IM.EQ.2) THEN`; `src/read_input.F:1223` `C3D           = .TRUE.`; `src/read_input.F:1224` `C3DDSS        = .TRUE.`). 허용 구간의 여섯 자리 `IM`은 첫 자리가 6 또는 7이면 `C3D·C3DVS`를 참으로 대입한다 (`src/read_input.F:1233` `ELSEIF ((IM.GE.111111).AND.(IM.LE.734323)) THEN`; `src/read_input.F:1267` `ELSEIF(IMDig1.EQ.6) THEN`; `src/read_input.F:1270` `C3D           = .TRUE.`; `src/read_input.F:1271` `C3DVS         = .TRUE.`; `src/read_input.F:1274` `ELSEIF(IMDig1.EQ.7) THEN`; `src/read_input.F:1277` `C3D           = .TRUE.`; `src/read_input.F:1278` `C3DVS         = .TRUE.`). | 3D 경압의 직접 `IM` 값은 21과 31이다 (`src/read_input.F:1205` `ELSEIF (IM.EQ.21) THEN`; `src/read_input.F:1208` `CBaroclinic   = .TRUE.`; `src/read_input.F:1213` `ELSEIF (IM.EQ.31) THEN`; `src/read_input.F:1217` `CBaroclinic   = .TRUE.`). 허용 구간의 여섯 자리 `IM`은 첫 자리가 7이면 `CBaroclinic`을 참으로 대입한다 (`src/read_input.F:1233` `ELSEIF ((IM.GE.111111).AND.(IM.LE.734323)) THEN`; `src/read_input.F:1274` `ELSEIF(IMDig1.EQ.7) THEN`; `src/read_input.F:1279` `CBaroclinic   = .TRUE.`). 여섯 번째 자리가 3보다 큰 경우에도 `CBaroclinic`을 참으로 대입한다 (`src/read_input.F:1372` `IF (IMDig6 > 3) THEN`; `src/read_input.F:1373` `CBaroclinic = .TRUE.`). |

- fort.10의 해당 reader는 2DDI scalar 초기값을 읽는다 (`src/read_input.F:3135` `IF((C2DDI).AND.(C2D_PTrans)) THEN`; `src/read_input.F:3139` `READ(10,*) NP2`; `src/read_input.F:3148` `READ(10,*) JKI,DAConc(JKI)`). 문서는 별도의 3D fort.10 형식을 적는다 (`docs/technical_reference/input_files/fort10.rst:18` `File structure for a 3D run:`; `docs/technical_reference/input_files/fort10.rst:24` `` :ref:`NVN <NVN>`, :ref:`NVP <NVP>` ``; `docs/technical_reference/input_files/fort10.rst:27` `` :ref:`NHNN <NHNN>`, :ref:`NVNN <NVNN>`, :ref:`CONC(NHNN,NVNN) <CONC>` ``). 확인하지 않음: 이 3D 형식에 대응하는 reader.
- fort.11의 2DDI 경로는 둘째 레코드에서 `BC3D_DT`를 실수로 읽는다 (`src/read_input.F:3086` `BC2D: IF ((C2DDI).AND.(CBaroclinic)) THEN`; `src/read_input.F:3093` `READ(11,*)`; `src/read_input.F:3094` `READ(11,*) BC3D_DT`; `src/read_input.F:3095` `READ(11,*) NP11`). 현행 rst는 둘째 레코드를 `Header Line 2`로 적는다 (`docs/technical_reference/input_files/fort11.rst:20` `Header Line 2`).
- fort.11.nc의 기본 파일명은 `densityFileName`의 `fort.11.nc`다 (`src/read_input.F:882` `densityFileName = 'fort.11.nc';`). 외부 결합 schema는 `time·strlen` 차원과 날짜 문자열을 읽는다 (`src/couple2baroclinic3D.F:213` `call check_err(nf90_inq_dimid(nc_id,'time', Temp_ID))`; `src/couple2baroclinic3D.F:215` `call check_err(nf90_inq_dimid(nc_id,'strlen', Temp_ID))`; `src/couple2baroclinic3D.F:220` `call Check_err(NF90_INQ_VARID(NC_ID,'time',Temp_ID))`; `src/couple2baroclinic3D.F:228` `TNDT = strptime(trim(TSS),"%Y-%m-%d %H:%M")`).
- `ABS(IDEN)>=8`의 ADCIRC 격자 schema는 `node·nele` 길이를 전역 격자 수와 비교한다 (`src/couple2baroclinic3D.F:253` `IF (IDEN.GE.8) THEN`; `src/couple2baroclinic3D.F:255` `call Check_err(NF90_INQ_DIMID(NC_ID,'node',Temp_ID))`; `src/couple2baroclinic3D.F:257` `IF (NY.NE.NP_G) THEN`; `src/couple2baroclinic3D.F:267` `call Check_err(NF90_INQ_DIMID(NC_ID,'nele',Temp_ID))`; `src/couple2baroclinic3D.F:269` `IF (NY.NE.NE_G) THEN`). 이 reader는 `BPGX·BPGY·SigTS`를 읽는다 (`src/couple2baroclinic3D.F:501` `bpgx_g  = read_nc_var_adc(NC_ID,'BPGX',BC3D_IT,np_g)`; `src/couple2baroclinic3D.F:502` `bpgy_g  = read_nc_var_adc(NC_ID,'BPGY',BC3D_IT,np_g)`; `src/couple2baroclinic3D.F:503` `sigts_g = read_nc_var_adc(NC_ID,'SigTS',BC3D_IT,np_g)`). 이 reader는 `NOLIBF=3`에서 `HBREAK`와 관계없이 `MLD`를 읽는다 (`src/couple2baroclinic3D.F:509` `IF (NOLIBF.EQ.3) THEN`; `src/couple2baroclinic3D.F:511` `mld_g = read_nc_var_adc(NC_ID,'MLD',BC3D_IT,np_g)`). 확인하지 않음: 외부 변수별 입력 단위.
- binary hotstart의 3D 블록은 `C3D` 조건에서 읽는다 (`src/hstart.F:568` `IF (C3D) THEN`). 3D 상태는 변수별 배열을 읽는다 (`src/hstart.F:612` `CALL readAndMapToSubdomain3D(RealQ_Tmp, NFEN, IHOT, IHOTSTP, moderbin)`; `src/hstart.F:613` `CALL readAndMapToSubdomain3D(ImQ_Tmp, NFEN, IHOT, IHOTSTP, moderbin)`; `src/hstart.F:616` `CALL readAndMapToSubdomain3D(WZ, NFEN, IHOT, IHOTSTP, moderbin)`; `src/hstart.F:617` `CALL readAndMapToSubdomain3D(q20, NFEN, IHOT, IHOTSTP, moderbin)`; `src/hstart.F:618` `CALL readAndMapToSubdomain3D(l, NFEN, IHOT, IHOTSTP, moderbin)`). 3D 배열의 수직 인덱스는 바깥 루프다 (`src/harm.F:2057` `DO j=1, jLength`; `src/harm.F:2058` `DO i=1, iLength`; `src/harm.F:2059` `READ(lun,REC=counter) array(i,j)`). scalar 종류 선택은 `ABS(IDen)`을 사용한다 (`src/hstart.F:633` `SELECT CASE(ABS(IDen))`).

The **external coupling** is for ADCIRC users who run an external 3D ocean model (e.g., HYCOM, ROMS) and want its baroclinic effects in their 2D ADCIRC tide+surge run. It does **not** require running ADCIRC in 3D mode.

## B. Sigma layers

Vertical grid via `IGC, NFEN`:
- `NFEN` = number of vertical finite-element nodes (`read_input.F:5153-5153`).
- `IGC=0`: read sigma levels directly; bottom `B=-1`, surface `A=1` required (`read_input.F:5204`).
- `IGC≠0`: call `FEGRIDS()` (`:5225`).

`FEGRIDS` supports (`global_3dvs.F:568`):
- Evenly spaced.
- Logarithmic.
- Log-linear.
- Double-log.
- p-grid.
- Sine grids.

Coordinate constants: `A=1`, `B=-1`, `AMB=A-B` (`global_3dvs.F:193`).

## C. Density / EOS

Salinity/temperature transport when `C3D_BTrans=.TRUE.` (`vsmy.F:1550-1555` 은 **dispatch만** — 실제 solver 는 `transport.F`/`TRANS_3D`, [[adcirc-transport-solver]] 참조):

| `IDEN` | Transports |
|---|---|
| `2` | Salinity only |
| `3` | Temperature only |
| `4` | Both |

- fort.39 reader는 river 경계와 `IDEN=2·3·4`를 요구한다 (`src/cstart.F:961` `IF (BndBCRiver .AND. (IDEN.EQ.2 .OR. IDEN.EQ.3 .OR.`; `src/cstart.F:962` `&    IDEN.EQ.4)) THEN`; `src/cstart.F:963` `OPEN(39,FILE=TRIM(INPUTDIR)//'/'//'fort.39',`). river 분류에는 `102·112·122·152`가 있다 (`src/mesh.F:1405` `case(102,112,122,152)`; `src/mesh.F:1406` `bndBCRiver=.true.`). `simpleFluxBoundaries` 할당 분기는 `102·112`를 포함하지 않는다 (`src/boundaries.F:353` `case(0,1,2,10,11,12,20,21,22,30,32,52,94,122)`; `src/boundaries.F:354` `allocate(simpleFluxBoundaries(sfCount)%nodes(nvell(i)))`). 확인하지 않음: 읽기 분기만으로 `102·112`의 실행 지원을 확정하지 않았다.
- reader는 `RIVBCSTATIM`에 `86400.d0`을 곱한다 (`src/cstart.F:965` `READ(39,*) RIVBCTIMINC, RIVBCSTATIM`; `src/cstart.F:966` `RIVBCTIME1=RIVBCSTATIM*86400.d0`). 해석: 이 입력 시작 시각의 단위는 일이다 (`src/cstart.F:966` `RIVBCTIME1=RIVBCSTATIM*86400.d0`). fort.39 문서는 초를 적는다 (`docs/technical_reference/input_files/fort39.rst:25` `- RIVBCSTATIM is the time (in seconds) when the boundary condition data start, relative to the cold start time`).
- fort.36·37의 해당 reader는 `CBaroclinic`이 참이고 `IDEN`이 양수인 경로에 있다 (`src/cstart.F:835` `IF ((CBAROCLINIC).AND.(IDEN.GE.1)) THEN`). 두 파일을 열려면 `NOPE>0`을 요구한다 (`src/cstart.F:861` `IF (NOPE.GT.0) THEN`; `src/cstart.F:862` `OPEN(36,FILE=TRIM(INPUTDIR)//'/'//'fort.36')`; `src/cstart.F:877` `IF (NOPE.GT.0) THEN`; `src/cstart.F:878` `OPEN(37,FILE=TRIM(INPUTDIR)//'/'//'fort.37')`). 음수 `IDEN` 경로는 이 두 파일을 읽지 않는다 (`src/cstart.F:940` `ELSE IF ((CBAROCLINIC).AND.(IDEN.LE.-1)) THEN`; `src/cstart.F:941` `IF ((RES_BC_FLAG.LT.0).AND.(NOPE.GT.0)) THEN`).
- fort.38은 `ABS(RES_BC_FLAG)=3·4`에서 읽는다 (`src/cstart.F:875` `IF ((ABS(RES_BC_FLAG).EQ.3).OR.`; `src/cstart.F:876` `&            (ABS(RES_BC_FLAG).EQ.4)) THEN`). `BCFLAG_TEMP=1·2·3`이 입력 형식을 선택한다 (`src/cstart.F:890` `IF (BCFLAG_TEMP.EQ.1) THEN ! read in file with multiple values but no calcs`; `src/cstart.F:900` `ELSE IF (BCFLAG_TEMP.EQ.2) THEN ! read in from file with 6 components`; `src/cstart.F:920` `ELSE IF (BCFLAG_TEMP.EQ.3) THEN ! read in from file with 4 components`). fort.38 읽기는 `NOPE>0` 검사 밖에 있다 (`src/cstart.F:877` `IF (NOPE.GT.0) THEN`; `src/cstart.F:878` `OPEN(37,FILE=TRIM(INPUTDIR)//'/'//'fort.37')`; `src/cstart.F:890` `IF (BCFLAG_TEMP.EQ.1) THEN ! read in file with multiple values but no calcs`; `src/cstart.F:891` `OPEN(38,FILE=TRIM(INPUTDIR)//'/'//'fort.38')`). 확인하지 않음: TMP 성분별 물리량과 단위.

After transport, `CALC_SIGMAT_3D()` for `IDEN > 1` (`vsmy.F:1632-1632`).

`Eqnstate` from input (`read_input.F:5720-5720`):

| `Eqnstate` | EOS | Code lines |
|---|---|---|
| `1` | Simple linear (Mellor / Cushman-Roisin) | `vsmy.F:4081-4081` |
| `2` | McDougall et al. 2003 | `:4174` |
| `3` | UNESCO 1980 | 현재 `EqnState=3`의 `c13`은 `T³` 계수다 (`src/vsmy.F:3961` `REAL(8), PARAMETER :: c12=-0.00909529d0, c13=0.0001001685d0`; `src/vsmy.F:4362` `RHO(NH,N) = c00 + (c11 + (c12 +(c13 +(c14 + c15*`; `src/vsmy.F:4363` `&         TEMP(NH,N))*TEMP(NH,N))*TEMP(NH,N))*TEMP(NH,N))*`; `src/vsmy.F:4364` `&         TEMP(NH,N) + (c21 + (c22 + (c23 + (c24 + c25*`). 현재 `c24`는 양수다 (`src/vsmy.F:3964` `REAL(8), PARAMETER :: c23=0.000076438d0, c24=0.00000082467d0`; `src/vsmy.F:4364` `&         TEMP(NH,N) + (c21 + (c22 + (c23 + (c24 + c25*`; `src/vsmy.F:4365` `&         TEMP(NH,N))*TEMP(NH,N))*TEMP(NH,N))*TEMP(NH,N))*`; `src/vsmy.F:4366` `&         SAL(NH,N) + (c31 + (c32 + c33*TEMP(NH,N))*`). |

PDF는 해당 `c13` 항을 `+1.001685E-4*T`로 인쇄했다 (`models/ADCIRC/raw/manuals/pdfs/2004_Pandoe01.pdf`, PDF 54쪽 / 인쇄 39쪽, 밀도 다항식 `+1.001685E-4*T`). PDF는 `S*T³` 항을 `-8.2467E-7*T^3*S`로 인쇄했다 (`models/ADCIRC/raw/manuals/pdfs/2004_Pandoe01.pdf`, PDF 54쪽 / 인쇄 39쪽, 밀도 다항식 `-8.2467E-7*T^3*S`). 현재 경로는 고정 기준 밀도와 `Kappa` 압력 보정을 구분한다 (`src/constants.F90:49` `real(8), parameter :: RhoWat0 = 1000.0d0`; `src/vsmy.F:4387` `RHO(NH,N) = RHO(NH,NFEN)/(1.d0+(Z(NH,N)/Kappa))`). 확인하지 않음: 어느 식이 의도된 IES80인지.

**Limitation**: no TEOS-10 (Conservative Temperature, Absolute Salinity). For modern ocean accuracy, this is a gap.

## D. Internal vs external mode

GWCE는 `METONLY`가 거짓인 유동 계산 블록에서 실행한다 (`src/timestep.F:813` `IF (.NOT.METONLY) THEN`; `src/timestep.F:1073` `call solveGWCE(it, ITIME_BGN, timeloc, timeh)`). `solveMomentumEq`의 2D 풀이 선택은 `C2DDI` 조건 안에 있다 (`src/momentum.F:125` `IF (C2DDI) THEN`). `C3DVS` 경로의 VSSOL은 깊이 평균 `UU2·VV2·QX2·QY2`를 갱신한다 (`src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`; `src/global_3dvs.F:484` `UU => UU2`; `src/global_3dvs.F:485` `VV => VV2`; `src/global_3dvs.F:486` `DAFluxX => QX2`; `src/global_3dvs.F:487` `DAFluxY => QY2`; `src/vsmy.F:1181` `UU(NH) = REAL(VIVel)`; `src/vsmy.F:1182` `VV(NH) = AIMAG(VIVel)`; `src/vsmy.F:1184` `DAFluxX(NH)=UU(NH)*Hsp1`; `src/vsmy.F:1185` `DAFluxY(NH)=VV(NH)*Hsp1`).

TIMESTEP은 `C3DVS` 조건에서 `VSSOL(IT,TimeLoc)`을 호출한다 (`src/timestep.F:1127` `IF (C3DVS) THEN`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`).

VSSOL 내부의 연직 시간적분(2TL θ³-가중 Alp1/Alp2/Alp3·복소 q=u+iv tridiagonal·연직 linear FE·w adjoint 보정)은 → **[[adcirc-3d-vssol-vertical-scheme]]** (2026-07-11 신설, 본 노트의 미커버 갭 해소).

VSSOL 전에 TIMESTEP은 `MOM_LV_X`에 수위·기압·조석 포텐셜의 시간 평균 순압 항을 준비한다 (`src/timestep.F:1135` `MOM_LV_X(I)=ETA1(I)+ETA2(I)`; `src/timestep.F:1136` `IF(NWS.NE.0) MOM_LV_X(I)=MOM_LV_X(I)+PR1(I)+PR2(I) !atmospheric pressure`; `src/timestep.F:1137` `IF (CTIP) MOM_LV_X(I)=MOM_LV_X(I)-TIP1(I)-TIP2(I) !tidal potential`; `src/timestep.F:1138` `MOM_LV_X(I)=G*MOM_LV_X(I)/2.d0`). `BTP`는 `MOM_LV_X`의 별칭이다 (`src/global_3dvs.F:491` `BTP => MOM_LV_X`).

VSSOL은 `Qkp1`을 연직 적분하여 깊이 평균 유속과 유량을 만든다 (`src/vsmy.F:1178` `VIVel = VIVel + Qkp1(NH,k)*LVn(k)`; `src/vsmy.F:1180` `VIVel = VIVel/amb`; `src/vsmy.F:1181` `UU(NH) = REAL(VIVel)`; `src/vsmy.F:1182` `VV(NH) = AIMAG(VIVel)`; `src/vsmy.F:1184` `DAFluxX(NH)=UU(NH)*Hsp1`; `src/vsmy.F:1185` `DAFluxY(NH)=VV(NH)*Hsp1`).
- 깊이 평균 유속의 별칭은 `UU2·VV2`를 가리킨다 (`src/global_3dvs.F:484` `UU => UU2`; `src/global_3dvs.F:485` `VV => VV2`).
- 깊이 평균 유량의 별칭은 `QX2·QY2`를 가리킨다 (`src/global_3dvs.F:486` `DAFluxX => QX2`; `src/global_3dvs.F:487` `DAFluxY => QY2`).
- VSSOL은 `BSX1·BSY1` 별칭에 저면 응력을 쓴다 (`src/global_3dvs.F:482` `BSX => BSX1`; `src/global_3dvs.F:483` `BSY => BSY1`; `src/vsmy.F:1196` `BSX(NH) = TK(NH)*REAL(Qkp1(NH,1))`; `src/vsmy.F:1197` `BSY(NH) = TK(NH)*AIMAG(Qkp1(NH,1))`).
- VSSOL은 `VSDISP`로 유속 분산을 만든다 (`src/vsmy.F:1214` `CALL VSDISP (IT,NH,Hsp1,UU(NH),VV(NH),`; `src/global_3dvs.F:488` `DUU => DUU1`; `src/global_3dvs.F:489` `DUV => DUV1`; `src/global_3dvs.F:490` `DVV => DVV1`). 이 별칭 쓰기는 이번 단계 GWCE 뒤에 있다 (`src/timestep.F:1073` `call solveGWCE(it, ITIME_BGN, timeloc, timeh)`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`). GWCE의 3D 저면 응력·분산 소비는 직전 단계 값 사용(지연)이다 (`src/gwce.F:1197` `BSXN1=BSX1(NM1)`; `src/gwce.F:1286` `DispX = (DUU1(NM1)*FDX1+DUU1(NM2)*FDX2+DUU1(NM3)*FDX3`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`).

## E. GWCE modification for 3D

GWCE receives two 3D/baroclinic additions:
1. **Velocity dispersion** (from 3D shear).
2. **Depth-integrated baroclinic pressure gradient**.

If `C3D=.FALSE.`, dispersion averages zeroed (`gwce.F:780`).
If `CBaroclinic=.FALSE.`, baroclinic gradient averages zeroed (`gwce.F:786`).

For 3D mode (`gwce.F:1196, 1283, 1405, 1450`):
- Bottom stresses: `BSX1/BSY1` (3D-derived).
- Velocity-dispersion gradients from `DUU1, DUV1, DVV1`.
- Baroclinic forcing from `VIDBCPDXOH/VIDBCPDYOH`.
- Enter GWCE forcing as `−DispXAvg − BCXAvg` and `−DispYAvg − BCYAvg`.

3D 경압의 직접 `IM` 값은 21과 31이다 (`src/read_input.F:1205` `ELSEIF (IM.EQ.21) THEN`; `src/read_input.F:1208` `CBaroclinic   = .TRUE.`; `src/read_input.F:1213` `ELSEIF (IM.EQ.31) THEN`; `src/read_input.F:1217` `CBaroclinic   = .TRUE.`). 허용 구간의 여섯 자리 `IM`은 첫 자리가 7이면 `CBaroclinic`을 참으로 대입한다 (`src/read_input.F:1233` `ELSEIF ((IM.GE.111111).AND.(IM.LE.734323)) THEN`; `src/read_input.F:1274` `ELSEIF(IMDig1.EQ.7) THEN`; `src/read_input.F:1279` `CBaroclinic   = .TRUE.`). 여섯 번째 자리가 3보다 큰 경우에도 `CBaroclinic`을 참으로 대입한다 (`src/read_input.F:1372` `IF (IMDig6 > 3) THEN`; `src/read_input.F:1373` `CBaroclinic = .TRUE.`). 3D 경계 블록을 읽는 조건은 `C3D` 경로 안의 `CBaroclinic`이다 (`src/read_input.F:4622` `IF(C3D) THEN`; `src/read_input.F:4623` `CALL READ_INPUT_3D(StaTim,NT)`; `src/read_input.F:5528` `IF (CBAROCLINIC) THEN`; `src/read_input.F:5529` `READ(15,*) RES_BC_FLAG, BCFLAG_LNM, BCFLAG_TEMP !bc flags for elevation and temperature`).
- `BPG3D`는 GWCE와 VSSOL보다 먼저 실행한다 (`src/timestep.F:855` `IF (C3DVS) CALL BPG3D(IT)`; `src/timestep.F:1073` `call solveGWCE(it, ITIME_BGN, timeloc, timeh)`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`). `BPG3D`는 그 시점의 `SIGT`로 경압을 계산한다 (`src/timestep.F:2172` `SigTAvg=(SigT(NH,k+1)+SigT(NH,k))/2.d0`; `src/timestep.F:2174` `BCP(NH,k)=BCP(NH,k+1)+HGORhoOAMB*(SigTAvg-SigT0)*DelSig`). 이번 단계의 `TRANS_3D·CALC_SIGMAT_3D`는 뒤의 VSSOL 안에서 실행한다 (`src/vsmy.F:1550` `CALL TRANS_3D(SAL,NLSD,NVSD,SALkp1,IDEN,TimeLoc)`; `src/vsmy.F:1552` `CALL TRANS_3D(TEMP,NLTD,NVTD,TEMPkp1,IDEN,TimeLoc)`; `src/vsmy.F:1554` `CALL TRANS_3D(SAL,NLSD,NVSD,SALkp1,IDEN-2,TimeLoc)`; `src/vsmy.F:1555` `CALL TRANS_3D(TEMP,NLTD,NVTD,TEMPkp1,IDEN-1,TimeLoc)`; `src/vsmy.F:1632` `IF(IDEN.GT.1) CALL CALC_SIGMAT_3D ()`). `BPG3D`의 수송 밀도 소비는 직전 단계 값 사용(지연)이다 (`src/timestep.F:855` `IF (C3DVS) CALL BPG3D(IT)`; `src/timestep.F:1143` `CALL VSSOL(IT,TimeLoc)`; `src/vsmy.F:1632` `IF(IDEN.GT.1) CALL CALC_SIGMAT_3D ()`).

## F. Vertical mixing

Vertical eddy viscosity controlled by `IEVC, EVMin, EVCon` (`read_input.F:5249-5249`).

| `IEVC` | Profile |
|---|---|
| `0` | Read profile from input |
| (other) | Empirical: constant, `ω H²`, `κ u* z`, `H Uavg`, `Uavg²` (`vsmy.F:1825-1825, 1840, 1870, 1931, 1983`) |
| `50, 51` | **MY2.5 quasi-equilibrium** (`vsmy.F:2037-2037, 2403`) |

MY2.5 closure:
- Solves `q²` and `q²L`.
- `Km = Sm q l`.
- Stratification through `SIGT` gradients; shear from `Q` (`vsmy.F:2742-2742`).
- Computes `Km, Kq, Kh` (`vsmy.F:2825`).

**Limitation**: this is built-in MY2.5 — older, lacks GLS / k-ε / k-ω modern alternatives. For full closure flexibility, ADCIRC would need GOTM-style integration (not present).

## G. 3D output (fort.41-46)

Station output:
- `fort.41` — 3D density/salinity/temperature stations (`read_input.F:5310-5310`, `write_output.F:3053-3053`).
- `fort.42` — 3D velocity stations (real/imaginary horizontal + `WZ`) (`:5439`, `:3059, 3623`).
- `fort.43` — 3D turbulence stations (`q20, l, EV`) (`:5484`, `:3185`).

Global output:
- `fort.44` — 3D density/salinity/temperature global (`:5527`, `:3269`).
- `fort.45` — 3D velocity global (`:5549`, `:3314`).
- `fort.46` — 3D turbulence global (`:5571`, `:3359`).

Optional: `fort.48` — internal BPG output (`global_3dvs.F:335`, `write_output.F:3391-3391`).

## H. Limitations vs full ocean model

External coupling (`couple2baroclinic3D.F:39-787`):
- Consumes external fields, interpolates spatially/temporally.
- Injects depth-integrated terms into 2D ADCIRC.
- **NOT** a 3D ocean solver inside ADCIRC.

True ADCIRC-3D:
- Prognostic S/T transport ✓.
- Baroclinic pressure gradients ✓.
- MY2.5 closure (legacy) — no GLS/k-ε/k-ω.
- EOS: simple / McDougall 2003 / UNESCO 1980 — **no TEOS-10**.
- The coupling module itself comments that "better practice would be conservative-temperature/absolute-salinity interpolation before density calculation" (`couple2baroclinic3D.F:40`).
- Vertical mixing options largely prescribed/empirical or built-in MY2.5.

Bottom line: ADCIRC-3D is suitable for **storm surge with stratification effects** or **coastal estuarine** problems where MY2.5 is sufficient. For deep-ocean or fully baroclinic ocean studies, use ROMS/HYCOM and couple via `couple2baroclinic3D.F`.

## Decision Guide

| Application | Setting |
|---|---|
| 2D tide/surge with prescribed baroclinic forcing | `IM=0`, `IDEN=5+` baroclinic coupling NetCDF (`Initial_BC3D_NetCDF`) |
| 3D barotropic (no S/T) | `IM=11`, `IDEN=0`, prescribed `IEVC` |
| 3D salinity transport only | `IM=21`, `IDEN=2` |
| 3D temperature only | `IM=21`, `IDEN=3` |
| 3D both S/T (estuarine) | `IM=21`, `IDEN=4`, `Eqnstate=2` (McDougall) |
| 3D + MY2.5 turbulence | `IM=21`, `IEVC=50` or `51` |
| Storm surge with stratification | `IM=21`, `IDEN=4`, `MY2.5` |
| Modern EOS needs (TEOS-10) | Not supported — use external ROMS/HYCOM |
| fort.41 density station 출력 | fort.41의 출력 형식은 `I3DSD`다 (`src/write_output.F:3040` `SigTStaDescript % specifier            =  I3DSD`). 출력 간격은 `NSPO3DSD`다 (`src/cstart.F:1027` `CALL initOutput3D(41, I3DSD, NDSET3DSD, NSTA3DD, NSTA3DD_G,`; `src/cstart.F:1028` `&                  NSPO3DSD, IRType, I3DSDRec)`; `docs/technical_reference/parameter_definitions/index.rst:1475` `The number of time steps at which data is written to unit 41. (i.e., data is output to unit 41 every NSPO3DSD time steps after TO3DSSD.)`). 출력 창은 3D density station 설정이다 (`src/read_input.F:5903` `startTS=INT((startTime-StaTime)*Day2Sec/DTDP+0.5d0) !jgf45.11 was NINT`; `src/read_input.F:5904` `endTS=INT((endTime-StaTime)*Day2Sec/DTDP+0.5d0) !jgf45.11 was NINT`). `ABS(IDEN)=1·2·3·4`의 출력 필드는 각각 밀도, 밀도·염분, 밀도·온도, 밀도·염분·온도 순서다 (`src/write_output.F:3515` `SELECT CASE(ABS(IDEN))`; `src/write_output.F:3520` `WRITE(41,1104) NN,(SigTSta(NN,k),k=1,NFEN)`; `src/write_output.F:3529` `&                     (SigTSta(NN,k),SalSta(NN,k),k=1,NFEN)`; `src/write_output.F:3538` `&                     (SigTSta(NN,k),TempSta(NN,k),k=1,NFEN)`; `src/write_output.F:3546` `WRITE(41,1104) NN,(SigTSta(NN,k),`; `src/write_output.F:3547` `&                      SalSta(NN,k),TempSta(NN,k),k=1,NFEN)`). [검증 보고서 §2.4의 IDEN별 표](/home/firesinger/coastal-wiki/_staging/recovery/compare/ADCIRC-outputs-vs-code.md:298)로 연결한다. |
| Output 3D velocity globally | `fort.45` |

## Working Rules

- `IM=21` is the most common 3D-baroclinic configuration. <!-- source-needed: 커뮤니티 관행 단언 — ADCIRC 매뉴얼/문헌/공식 예제 인용 필요 -->
- `NFEN=21` (20 sigma layers) is standard for shelf/estuary; up to `NFEN=51` for deep stratification. <!-- source-needed: 관행 수치 — 매뉴얼/문헌 인용 필요 -->
- 경압 3D 입력은 `RES_BC_FLAG`와 `IDEN`이 같아야 한다 (`src/read_input.F:5528` `IF (CBAROCLINIC) THEN`; `src/read_input.F:5535` `if (RES_BC_FLAG.ne.IDEN) then`; `src/read_input.F:5536` `call terminate(exit_code=ADCIRC_EXIT_FAILURE,`; `src/read_input.F:5538` `&                     "must be the same as the value of IDEN.")`). `RES_BC_FLAG` 양수 분기는 1·2·3·4를 처리한다 (`src/read_input.F:5550` `IF (ABS(RES_BC_FLAG).EQ.1) THEN ! only read in the elevation changes`; `src/read_input.F:5558` `ELSE IF ((ABS(RES_BC_FLAG).EQ.2)) THEN`; `src/read_input.F:5570` `ELSE IF ((ABS(RES_BC_FLAG).EQ.3).OR.`; `src/read_input.F:5571` `&               (ABS(RES_BC_FLAG).EQ.4)) THEN`). 그 밖의 양수 값은 종료한다 (`src/read_input.F:5613` `CALL terminate(exit_code=ADCIRC_EXIT_FAILURE,`; `src/read_input.F:5614` `&               message="Invalid RES_BC_FLAG value read from "//`; `src/read_input.F:5615` `&                       "fort.15 file.")`). 해석: `IM=21, IDEN>=5`의 외부장 결합 권고는 이 입력 조건으로 정당화하지 못한다 (`src/read_input.F:5535` `if (RES_BC_FLAG.ne.IDEN) then`; `src/read_input.F:5614` `&               message="Invalid RES_BC_FLAG value read from "//`).
- MY2.5 (`IEVC=50/51`) is recommended over prescribed profiles for stratified runs.
- Output `fort.41` (T/S stations) early in run to verify EOS computation.
- Boundary conditions for S/T need their own time series (typically from external model or climatology).

## Common Pitfalls

- `IM=11`은 경압 플래그를 켜는 직접 3D 설정이 아니다 (`src/read_input.F:1197` `ELSEIF (IM.EQ.11) THEN`; `src/read_input.F:1198` `C3D           = .TRUE.`; `src/read_input.F:1199` `C3DVS         = .TRUE.`). 3D 경압의 직접 `IM` 값은 21과 31이다 (`src/read_input.F:1205` `ELSEIF (IM.EQ.21) THEN`; `src/read_input.F:1208` `CBaroclinic   = .TRUE.`; `src/read_input.F:1213` `ELSEIF (IM.EQ.31) THEN`; `src/read_input.F:1217` `CBaroclinic   = .TRUE.`). 허용 구간의 여섯 자리 `IM`은 첫 자리가 7이면 `CBaroclinic`을 참으로 대입한다 (`src/read_input.F:1233` `ELSEIF ((IM.GE.111111).AND.(IM.LE.734323)) THEN`; `src/read_input.F:1274` `ELSEIF(IMDig1.EQ.7) THEN`; `src/read_input.F:1279` `CBaroclinic   = .TRUE.`). 여섯 번째 자리가 3보다 큰 경우에도 `CBaroclinic`을 참으로 대입한다 (`src/read_input.F:1372` `IF (IMDig6 > 3) THEN`; `src/read_input.F:1373` `CBaroclinic = .TRUE.`).
- ▢ Setting `IDEN=4` without providing both S and T BCs — model crashes. <!-- source-needed: crash 경로 file:line 인용 필요 -->
- ▢ Using simple linear EOS (`Eqnstate=1`) for realistic ocean — gives unrealistic pycnocline. <!-- source-needed: 물리 결과 단언 — 문헌/교과서 인용 필요 -->
- ▢ Confusing `couple2baroclinic3D.F` (external coupling) with true 3D — they look similar but only the latter solves 3D internally.
- ▢ `IEVC=50` (MY2.5) cold-started with zero `q²` — singular dissipation; init with positive minimum. <!-- source-needed: singular 거동 file:line 또는 문헌 인용 필요 -->
- ▢ Hot-start with different `IM` — 3D state arrays incompatible. <!-- source-needed: hot-start 3D 상태배열 재로드 경로 hstart.F file:line 인용 필요 -->
- ▢ Comparing ADCIRC-3D temperature to TEOS-10 reference — slight bias due to legacy EOS; document explicitly.
- ▢ Forgetting to set bottom drag for 3D — bottom stress comes from 3D BBL, not 2D Manning.

## Next expansion

- HYCOM → couple2baroclinic3D.F NetCDF format example.
- MY2.5 (IEVC=50) calibration recipe.
- IM=21 vs IM=31 differences.
- Coupling external WAVES (SWAN-3D not standard).

## References

- Luettich & Westerink (ADCIRC theory v53+ docs).
- Mellor & Yamada 1982 (MY2.5).
- McDougall et al. 2003 (EOS).
- UNESCO 1981 (EOS-80).
- Source: paths above.

## Provenance

Generated 2026-05-03 from Codex `gpt-5.3-codex` analysis of `models/adcirc/source_code/adcirc/src`. Auto-draft = false; review_required = true.
