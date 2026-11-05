---
title: "CADMAS-SURF/3D 시간刻み·격자 nesting·STOC 결합 — CFL 적응 Δt·親子 telescoping 격자·MPMD STOC 핸드오프 (vf_cdtcal·pmg*·stoc_*·mod_comm)"
model: CADMAS-SURF
component: src (timestep control + grid nesting + STOC coupling infra)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/.../CADMAS-SURF-3D/Source code/). CFL: vf_cdtcal.f 안전율·이류CFL·확산한계(:58-147)+VF_ATIMER.h DTSAFE+drive vf_a1main.f:937-943·1017-1019. nesting: vf_pmginp.f env+vf_pmgset.f 親子설정+vf_pmgp2c/c2p.f 전송+pmgp2c_cf.f 보간(XPF/YPF/ZPF)+VF_APARAI.h MGPARE/MGCPOS 토폴로지. STOC: vf_stoc_init.f MPI_COMM_SPLIT(:43-45)+stoc_recv/send.f 경계값 U/V/W/HU+mod_comm.f90 MPMD comm(:143-179)+NB_SC 게이트 VF_ASTOCI.h:41+vf_a1main.f:1010-1027. file:line 직접 인용. 2026-11-04 CADMAS-SURF recovery 대조 보고서 반영." # [11-04 대조 정정]
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
last_source_check: "2026-11-04 (recovery 대조 반영)"
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
  - models/CADMAS-SURF/README.md
source_scope: Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D
---

# CADMAS-SURF/3D 시간刻み·격자 nesting·STOC 결합

> CADMAS-SURF/3D 를 **멀티스케일 tsunami 프레임워크**(STOC-ML/IC 광역 → CADMAS 국소)에 연결하는 인프라 3종. (A) 적응 Δt(CFL) (B) "MG"=親子 telescoping 격자 nesting (C) STOC 결합(MPMD). 메인루프 [architecture-source-map §4](cadmas-surf3d-architecture-source-map.md#4-smacvof-시간적분-루프-vf_a1mainf915-1145)의 ①PMGP2C/C2P ②CDTCAL ⑤STOC 단계. 경로 루트 동일.

## A. 적응 시간刻み (CFL) — vf_cdtcal.f

헤더 `VF_CDTCAL:時間刻み幅の計算`(`vf_cdtcal.f:5-7`). 드라이버 분기(`vf_a1main.f:937-943`): `IDTTYP=0`→고정 `DT=DTCNST`, `≠0`→자동(`VF_CDTCAL`). 디폴트 `IDTTYP=1`·`DTCNST=1e-3`(`vf_a2dflt.f:223·230`).

산정 순서:
1. **안전율 적용 초기상한**: `DT=DTMAX/DTSAFE` (`vf_cdtcal.f:58-59`, `DTSAFE`=安全率 `VF_ATIMER.h:18`)
2. **확산한계 사전계산**: `ANU`(분자+渦점성)·열전도·스칼라확산의 max → `WK01` (`vf_cdtcal.f:61-87`)
3. **이류 CFL**: 분자는 공극 체적이다. 원문은 `V=GGV(I,J,K)*DX*DY*DZ`이다. 분모는 여섯 면에서 조건별로 정한 절대 체적유량 최댓값이다. 원문은 `DT=V/MAX(FL1,FL2,FL3,FL4,FL5,FL6,V/DT)`이다. 경계 면의 내부 F와 경계 F가 모두 0 이하이면 해당 유량을 0으로 둔다 (`3D/vf_cdtcal.f:105–130`). 근거는 [KS1-720·626](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md)이다. [11-04 대조 정정]
4. **확산(점성)한계**(`vf_cdtcal.f:132-134`):
   ```
   V  = 0.5 / (1/Δx² + 1/Δy² + 1/Δz²)
   DT = V / MAX(WK01, V/DT)
   ```
   고전 명시적 확산한계 `Δt ≤ 0.5/[ν(1/Δx²+1/Δy²+1/Δz²)]`
5. **최종조립**: 전 PE 최솟값을 구한다. 기준값은 `W=DTNOW`이다. 첫 단계에서는 `IF (NNOW.EQ.0) W=DTINIT`를 적용한다. 최종 식은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`이다 (`3D/vf_cdtcal.f:141–147`). `DTMIN`은 바깥쪽 `MAX`에서 하한으로 적용한다. 근거는 [RF-020](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-RF.md)과 [KU1-804](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md)이다. [11-04 대조 정정]

3D의 확산 제한은 운동량·온도·농도 확산 중 가장 큰 계수로 정한다 (`3D/vf_cdtcal.f:65–83,133–134`). 근거는 [KS1-328](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md)이다. 3D2F의 열확산 제한은 `RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)`를 쓴다. `RHOG` 대체 줄은 주석이다 (`3D2F/vf_cdtcal.f:67–98,144–145`). 근거는 [KF2-357](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF2.md)이다. [11-04 대조 정정]

## B. 親子 격자 nesting ("MG" = 공간 telescoping, 대수 multigrid 아님)

물리적 親子 sub-domain 이 경계/내부 flow 변수를 교환하는 **공간 telescoping nesting** — residual·smoother·coarse-grid correction V-cycle 없음(헤더·토폴로지 변수가 모두 물리적).

- **환경파일 읽기**: `data.env`의 첫 정수는 영역 수다. 각 영역의 이름·PE 수·부모 번호가 뒤따른다 (`3D/vf_pmginp.f:25–52`). 공급 3D 코드의 병렬 목록 파일은 `<영역명>.list<5자리 PE>`이다 (`3D/vf_a1main.f:376–379`). 매뉴얼의 `<영역명><6자리 PE>.list`와 다르다 (`3D manual p.146`). 근거는 [3d-input §4 KS3-406](../../../_staging/recovery/compare/cadmas-3d-manual-input-vs-code.md#4-노트-대조와-수정안)이다. [11-04 대조 정정]
- **설정** `VF_PMGSET:…親子関係をチェックし設定`(`vf_pmgset.f:12`) — P2C/C2P 리스트 구축(`:19`)
- **토폴로지**(`VF_APARAI.h`): `MGRANK`(자기 전역rank :28)·`MGPARE`(親 영역 :34)·`MGPRNK`(親 rank, `<0`=親無 :36-38)·`MGCNUM`(子 수 :50)·`MGCRNK`(子 rank :51)·`MGCPOS(6,*)`(親 내 子 위치 셀범위 :63-69)
- **親→子 전송**(子 경계 보간) `VF_PMGP2C:…親の情報を子へ転送`(`vf_pmgp2c.f:9`), **子→親 전송**(親 내부 restriction) `VF_PMGC2P`(`vf_pmgc2p.f:9`) — 매스텝 연속 호출(`vf_a1main.f:923·929`)
- **보간계수 XPF/YPF/ZPF**(2011.04 추가, `vf_pmgp2c.f:2-4·31-33` `親格子に対する補間係数`): 실제 보간은 `vf_pmgp2c_cf.f` — `FACTZ=0.5(ZPF(KC)+ZPF(KC+1))-Z0`·`RDZ=1/(ZPF(KC+1)-ZPF(KC))`·`VV=BCV(L)+(YPF(JC)-Y0)·BC(8)`(`:79-91`) = 親장을 細격자 子셀에 선형보간
- **포러스/플럭스 헬퍼**: `pmgggt`(親→子 포러스 수신)·`pmggpt`(親→子 포러스 송신)·`pmgflx`/`pmgfly`(VOF-F 플럭스 면정합, `IMPLICIT NONE`+INTENT 신식)

## C. STOC 결합 (STOC-IC 부모와 CADMAS 국소) [11-04 대조 정정]

STOC-ML은 정수압 모델이다. STOC-IC는 비정수압 모델이다. CADMAS의 부모는 STOC-IC이다. STOC-IC와 CADMAS의 수직분할을 같게 한다. CADMAS 수평 병렬 분할선은 STOC-IC 격자선에 맞춘다. `data.env`는 첫 줄의 영역 수와 다음 줄의 영역명·프로세스 수·부모 `-1`을 분리한다. 근거는 [tutorials-build §4 KU1-063·069·075·076·814](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md#4-노트-대조와-수정안)이다. [11-04 대조 정정]

- **초기화** `VF_STOC_INIT:STOCとの通信環境を初期化`(`vf_stoc_init.f:5-6`) — `NB_SC` 로 split 하여 STOC↔CADMAS 서브커뮤니케이터 생성: `MPI_COMM_SPLIT(comm_work_ic_mg,NB_SC,...,comm_ic_mg)`(`vf_stoc_init.f:43-45`), 메인 `vf_a1main.f:394`
- **MPMD 메커니즘**(`mod_comm.f90`): `init_mpmd`(`vf_a1main.f:351`). 모델 enum `l_stoc_ml=0·l_stoc_ic=1·l_stoc_ds=2·l_cadmas_mg=10·l_cadmas_2fc=11`(`:23-26`). 커뮤니케이터 `comm_ic_mg`(STOC-IC↔CADMAS/MG :54)·`comm_mlicdsmg2fc`(전 결합셋 :59). `mpi_init`(:98)+`mpi_comm_split(mpi_comm_world,...)` 모델번호 키(`:143-179`) → STOC·CADMAS 별도 실행파일이 한 WORLD 안에서 split
- 3D의 자기 모델은 `l_cadmas_mg`이다. 3D2F는 `l_cadmas_2fc`이다. 판 근거는 `mod_comm.f90:41`의 자기 모델 대입 변경 diff이다. 3D2F는 STM 집합을 구성한다. `3D2F/vf_stoc_init.f:39–42`는 2FC의 직접 STOC 접속을 조기 반환한다. 근거는 [KD1-908](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KD1f.md)이다. [11-04 대조 정정]
- **게이트 `NB_SC`**(`VF_ASTOCI.h:41-42` `STOC-CADMAS接続에 참가 여부 0/>0`): 매스텝(`vf_a1main.f:1010-1027`)
  ```
  IF (NB_SC.GT.0) THEN
    CALL VF_STOC_RECV(...)   ! STOC→CADMAS 경계값 수신
    CALL VF_STOC_SEND(...)   ! CADMAS→STOC 송신
  ENDIF
  ```
  수신 후 경계 재적용 `VF_BWUWN/BWUWT/BWFF`(`:1020-1027`)
- **STOC→CADMAS**(수신): `VF_STOC_RECV:STOCから境界値を受信`(`vf_stoc_recv.f:5`) — 4측면(W/E/S/N) `MPI_IRECV`(comm_ic_mg, `:47-49`), 면셀당 **4성분**(U,V,W + 수위/수심 HU) → `UWST/UEST/VSST/VNST(*,*,1:4)`(`VF_ASTOCR.h:1-3·12-15`)
- **CADMAS→STOC**(송신): VOF 가중 면평균 속도와 경계 체적플럭스를 STOC-IC 부모에 보낸다 (`3D/vf_stoc_send.f:38–76,135`). 근거는 [tutorials-build §4 KU1-063·069·075·076·814](../../../_staging/recovery/compare/cadmas-tutorials-build-vs-code.md#4-노트-대조와-수정안)이다. [11-04 대조 정정]
- **보조**: `stoc_area`(격자정보 교환)·`stoc_obst`(지형 OBST 수신)·`stoc_pors`(포러스 GGV/GGX/GGY/GGZ 수신)·`stoc_1d`(1D 1층 송수신)·`stoc_fconv`(STOC 연성 VOF-F 플럭스)

STOC와 CADMAS는 MPMD에서 `MPI_COMM_SPLIT`으로 만든 `comm_ic_mg`를 공유한다 (`3D/mod_comm.f90:143–179`). [11-04 대조 정정]

## 전역 동기 (A↔C 연결)

종료 플래그 합의는 STOC 교환 앞이다. 최소 시간 간격 합의는 STOC 교환 뒤이다. `IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`에서 종료하지 않은 경로가 뒤의 교환·시간 간격 합의에 도달한다. STOC 수신·송신은 `IF (NB_SC.GT.0) THEN` 안에서 실행한다 (`3D/vf_a1main.f:997–1019`). 근거는 [RF-009](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-RF.md)이다. [11-04 대조 정정]

## 문서와 코드 차이 (11-04 대조)

비교한 판: 코드는 github.com/CADMAS-SURF/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami `da7668f`(2024-08-30, 커밋 1개)의 Simulators/이며, 문서는 `CADMAS-SURF3D_Manural_English.pdf`, `CADMAS-2F_Manural_English.pdf`, 두 모델의 영문 튜토리얼·`A11111.in`, `STOC-CADMAS_Manual_Japanese.pdf`이다.

결론 문장은 AI 대조 해석이다. 백틱은 문서·코드 원문이다. 코드 약칭은 해당 시뮬레이터의 Source code/를 기준으로 한다.

| 행 ID | 항목 | 문서 원문 | 코드 원문 | 결론 | 결론 문장 |
|---|---|---|---|---|---|
| 2f-input:KF3-122 | DT 식 조판 | `DT: time step width (= tn - tn - 1)` | `3D2F/vf_a1main.f:1190`; 2F manual p.150; JP p.137<br>`TNOW =TNOW+DTNOW`<br>`DTNOW=DT` | B 문서 오기 | DT는 현재 시각과 이전 시각의 차이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF3.md) |
| 2f-input:KF3-178 | 시간 간격·종료 보정 | (문서에 해당 문장 없음) | 2F manual p.122(584); `3D2F/vf_cdtcal.f:152–157`; `3D2F/vf_a1main.f:1050–1052`<br>`DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`<br>`W=DTNOW`<br>`IF (NNOW.EQ.0) W=DTINIT`<br>`IF (NNOW.GE.NEND .OR. (TNOW+0.5D0*DT).GE.TEND) IEND(1) = 1` | C 문서 누락 | AUTO 시간 간격은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`으로 정한다. `W=DTNOW`이며 `IF (NNOW.EQ.0) W=DTINIT`를 적용한다. DTMIN이 1.20D0*W보다 크면 결과는 DTMIN이다. 종료 판정은 `IF (NNOW.GE.NEND .OR. (TNOW+0.5D0*DT).GE.TEND) IEND(1) = 1`이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF3.md) |
| 2f-program:KF2-020 | CFL 부호·공극 유량 | `\Delta t\le\min(\Delta x/u,\Delta y/v,\Delta z/w)=\Delta t_c` | `3D2F/vf_cdtcal.f:104–145`; 2F manual p.64 식 (3.129)<br>`V=GGV(I,J,K)*DX*DY*DZ`<br>`FL1=ABS(DYZ*GGX(I  ,J,K)*UU(I  ,J,K))`<br>`FL2=ABS(DYZ*GGX(I+1,J,K)*UU(I+1,J,K))`<br>`FL3=ABS(DXZ*GGY(I,J  ,K)*VV(I,J  ,K))`<br>`FL4=ABS(DXZ*GGY(I,J+1,K)*VV(I,J+1,K))` | B 문서 오기 | 이류 시간 간격은 셀 공극 체적과 여섯 면의 최대 절댓값 유량으로 제한한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF2.md) |
| 2f-program:KF2-022 | 자동 시간 간격 보정 | `\Delta t=\alpha\min(\Delta t_c,\Delta t_\nu)` | `3D2F/vf_cdtcal.f:65,152–157`; 2F manual p.64 식 (3.131)<br>`IF (NNOW.EQ.0) W=DTINIT`<br>`DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`<br>`DT=DTMAX/DTSAFE`<br>`CALL VF_P0MIND(W,DT)` | C 문서 누락 | 자동 시간 간격은 전역 최솟값·DTMAX·DTMIN·1.20배 증가 제한을 반영한다. `IF (NNOW.EQ.0) W=DTINIT`를 적용한 뒤 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`를 계산한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF2.md) |
| 2f-program:KF2-023 | 안전계수 상한 검사 | `0. 0 <α <1.0` | `3D2F/vf_iitime.f:38–44`; 2F manual p.64<br>`IF (DTSAFE.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')`<br>`ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN`<br>`CALL VF_ZSTOR(DTSAFE,TEXT(IS(4):IE(4)))` | C 문서 누락 | TIME AUTO 입력은 DTSAFE의 상한 1을 검사하지 않는다. 오류 조건은 `IF (DTSAFE.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')`이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF2.md) |
| 2f-program:KF2-349 | p.70·93–94 통신 영역의 실제 크기·검사 | (문서에 해당 분할 폭·국소 배열 크기 검사 설명 없음) | `3D2F/vf_cpara.f:34–49,64–87,102–106`; 2F manual p.70,93–94<br>`IF (NUMNPI.GT.1) THEN`<br>`IF (NUMNPJ.GT.1) THEN`<br>`IF (NPROCS.NE.NUMNPI*NUMNPJ)`<br>`DO 120 I=1,NUMNPI`<br>`IF (IPROCS(I)-IPROCS(I-1).LT.2)`<br>`&                      CALL VF_A2ERR('VF_CPARA','2 > IC2-IC1.')`<br>`120    CONTINUE` | C 문서 누락 | `IF (NUMNPI.GT.1) THEN`에서 x 분할 폭을 2 이상으로 검사한다. `IF (NUMNPJ.GT.1) THEN`에서 y 분할 폭을 2 이상으로 검사한다. `IF (NPROCS.NE.NUMNPI*NUMNPJ)`이면 오류 처리한다. 물리 경계 가상 셀 두께는 1이다. 내부 프로세스 경계 두께는 2다. NUMI·NUMJ는 이 두께를 더한 국소 배열 크기다. NUMBUF는 max(NUMI,NUMJ)*NUMK다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF2.md) |
| 2f-program:KF2-357 | p.64 점성 안정성 식에 없는 열·농도 확산 시간 제한 | (문서에 해당 문장 없음) | `3D2F/vf_cdtcal.f:67–98,144–145`; 2F manual p.64<br>`IF (LEQT.NE.0) THEN`<br>`DO 190 LC=1,LEQC`<br>`RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)`<br>`WK01(I,J,K)=ANU(I,J,K)`<br>`C2F     W=1.0D0/(RHO0*TCP0)`<br>`DO 150 K=2,NUMK-1`<br>`DO 140 J=MYJS,MYJE` | C 문서 누락 | WK01은 ANU로 시작한다. `IF (LEQT.NE.0) THEN`에서는 ALM/(RHO2*TCP0)와의 최댓값을 취한다. `DO 190 LC=1,LEQC`에서는 각 DD와의 최댓값을 취한다. 열 제한의 혼합 밀도는 `RHO2=FF(I,J,K)*RHO0(1)+(1.0D0-FF(I,J,K))*RHO0(2)`다. RHOG를 사용하는 대체 줄은 주석이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KF2.md) |
| 3d-input:KS3-256 | 환경 파일 첫 정수 | `A number of nesting` | `3D/vf_pmginp.f:28–33`; 3D manual p.146–147; JP p.138–139<br>`READ(IENFIL,*,END=9020,ERR=9020) MGARAN`<br>`:32`<br>`DO 120 I=1,MGARAN` | F 표기 차이 | data.env 첫 정수는 전체 해석 영역 수이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md) |
| 3d-input:KS3-257 | 병렬 파일명 번호 규칙 | `edata-ch000000.list` | `3D/vf_a1main.f:376–379`; `3D/vf_og1ini.f:49–52`; `3D2F/vf_a1main.f:314–320`; `3D2F/vf_og1ini.f:52–57`; 전체 Simulators rg -i; 3D manual p.146; JP p.139<br>`WRITE(TEXTP,'(I5.5)') MYRANK`<br>`OPEN(MFILLP,ERR=9010,`<br>`&       FILE=MGNAME(MGRANK+1)(1:MGNLEN(MGRANK+1))//'.list'//TEXTP,`<br>`&       STATUS='NEW',FORM='FORMATTED' )` | D 문서에만 있음 | 공급 코드의 병렬 목록·도화 파일명은 영역명+확장자+5자리 PE 번호이다. 문서의 6자리·확장자 앞 번호 규칙을 적용하면 안 된다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md) |
| 3d-input:KS3-303 | AUTO 시간 간격 증가 한도 | (문서에 해당 AUTO 증가 제한 문장 없음) | `3D/vf_cdtcal.f:59,141–147`; 3D manual p.109<br>`W=DTNOW`<br>`IF (NNOW.EQ.0) W=DTINIT`<br>`DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`<br>`DT=DTMAX/DTSAFE`<br>`:145–147` | C 문서 누락 | AUTO 시간 간격의 증가 제한 기준은 `W=DTNOW`이다. 초기 단계에서는 `IF (NNOW.EQ.0) W=DTINIT`를 적용한다. 최종 시간 간격은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md) |
| 3d-input:KS3-314 | 환경 파일 추가 검사 | (문서에 해당 환경 파일 검사 문장 없음) | `3D/vf_pmginp.f:28–52,64–82`; 3D manual p.146<br>`IF (MGPARE(I).GT.MGARAN) GOTO 9040`<br>`IF (MGARAN.GT.MAXPRO) GOTO 9030`<br>`IF (MGARAN.LE.0     ) GOTO 9040`<br>`IF (MGNPIN(I).LE.0     ) GOTO 9040`<br>`IF (MGPARE(I).EQ.I     ) GOTO 9040` | C 문서 누락 | 환경 파일은 영역 수·PE 총수·부모 번호 상한·자기 부모·부모 순환·중복 영역명을 검사한다. 부모 번호 상한 조건은 `IF (MGPARE(I).GT.MGARAN) GOTO 9040`이다. 음수 부모를 금지하던 줄은 `CCC IC-MG COUPLING` 표지로 주석 처리되어 있다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS3.md) |
| 3d-program:KS2-611 | p.60의 처리 흐름은 부모·자식 자료 교환을 쓰지 않는다. | (문서 흐름도에 해당 부모·자식 자료 교환 경로 없음) | 3D manual p.60; `3D/vf_a1main.f:923–933`<br>`CALL VF_PMGP2C(XX,YY,ZZ,UU,VV,WW,FF,`<br>`C----------------------------------------------------------2011.04 start`<br>`&                 GGV,GGX,GGY,XPF,YPF,ZPF,IPF,JPF,KPF,`<br>`C----------------------------------------------------------2011.04 end`<br>`&                 BCU,BCV,BCW,BCF,DBUF,NF,INDX,INDY,INDB)` | C 문서 누락 | 시간 간격 계산 전에 부모에서 자식으로 자료를 보내고 자식에서 부모로 자료를 보낸다. 2011.04 표지의 XPF·YPF·ZPF·IPF·JPF·KPF가 이 경로의 인수이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS2.md) |
| 3d-program:KS2-624 | p.60 시간 간격 계산 상자와 p.83 병렬 변수 표에는 결합 참여 프로세스 사이의 최소 시간 간격 합의가 없다. | (문서에 해당 문장 없음) | 3D manual p.60; 3D manual p.83; `3D/vf_a1main.f:1017–1019`; `3D/vf_a1main.f:1029`<br>`DTNOW=DT/DBLE(LOOPS)`<br>`DT0 = DT`<br>`CALL MPI_ALLREDUCE( DT0,DT,1,MPI_DOUBLE_PRECISION,MPI_MIN,`<br>`$                      comm_mlicdsmg2fc,IERR )` | C 문서 누락 | 시간 간격 DT를 comm_mlicdsmg2fc의 MPI_MIN으로 합의한다. 하위 반복에는 `DTNOW=DT/DBLE(LOOPS)`를 적용한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS2.md) |
| 3d-theory:KS1-327 | 식 (3.127) | `\displaystyle \Delta t\leq\min\left(\frac{\Delta x}{u},\frac{\Delta y}{v},\frac{\Delta z}{w}\right)=\Delta t_c` | `3D/vf_cdtcal.f:105–130`; 3D manual p.56<br>`V=GGV(I,J,K)*DX*DY*DZ`<br>`FL1=ABS(DYZ*GGX(I  ,J,K)*UU(I  ,J,K))`<br>`FL2=ABS(DYZ*GGX(I+1,J,K)*UU(I+1,J,K))`<br>`FL3=ABS(DXZ*GGY(I,J  ,K)*VV(I,J  ,K))`<br>`FL4=ABS(DXZ*GGY(I,J+1,K)*VV(I,J+1,K))` | B 문서 오기 | 식 (3.127)의 속도 분모에는 절댓값이 필요하다. 코드의 실제 CFL은 공극 체적과 면 유량으로 계산한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| 3d-theory:KS1-328 | 식 (3.128) | `\displaystyle \Delta t\leq\frac{1}{2}\frac{1}{\nu\left[\left(\frac{1}{\Delta x}\right)^2+\left(\frac{1}{\Delta y}\right)^2+\left(\frac{1}{\Delta z}\right)^2\right]}=\Delta t_\nu` | `3D/vf_cdtcal.f:65–83,133–134`; 3D manual p.56<br>`WK01(I,J,K)=ANU(I,J,K)`<br>`IF (LEQT.NE.0) THEN`<br>`W=1.0D0/(RHO0*TCP0)`<br>`DO 150 K=2,NUMK-1`<br>`DO 140 J=MYJS,MYJE` | C 문서 누락 | 자동 시간간격의 확산 제한은 운동량·온도·농도 확산 중 가장 큰 계수로 정한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| 3d-theory:KS1-329 | 식 (3.129) | `\displaystyle \Delta t=\alpha\min(\Delta t_c,\Delta t_\nu)` | `3D/vf_cdtcal.f:59,141–147`; 3D manual p.56<br>`DT=DTMAX/DTSAFE`<br>`DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`<br>`IF (NNOW.EQ.0) W=DTINIT`<br>`CD    -- 安全率を乗じ、1.2倍以下と最小値による制限を加える --`<br>`W=DT`<br>`CALL VF_P0MIND(W,DT)`<br>`CAKIY CALL VF_P1MIND(W,DT)` | C 문서 누락 | 자동 시간 간격은 `DT=DTMAX/DTSAFE`에서 시작한다. 마지막에 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`을 적용한다. W는 직전 시간 간격이다. `IF (NNOW.EQ.0) W=DTINIT`로 초기값을 정한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| 3d-theory:KS1-514 | 3D manual p.56 | `0.0<α<1.0` | `3D/vf_iitime.f:30–44`; `3D/vf_a1main.f:937–943`; `3D/vf_a2dflt.f:230–234`; 3D manual p.56<br>`CD    -- TIME CONSTを解釈する --`<br>`IF (TEXT(IS(2):IE(2)).EQ.'CONST') THEN`<br>`IF (NWD.LT.3) CALL VF_A2ERR('VF_IITIME','SYNTAX ERROR.')`<br>`CALL VF_ZSTOR(DTCNST,TEXT(IS(3):IE(3)))`<br>`IF (DTCNST.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` | C 문서 누락 | 안전계수 `0<α<1`은 매뉴얼의 사용 조건이다. 입력 파서는 `α<1`을 강제하지 않는다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| 3d-theory:KS1-623 | 코드 추가 처리 | (문서에 해당 문장 없음) | `3D/vf_iitime.f:38–52`; `3D/vf_a2dflt.f:223–234`; `3D/vf_cdtcal.f:69–83,141–147`; 3D manual p.56<br>`ELSEIF (TEXT(IS(2):IE(2)).EQ.'AUTO') THEN`<br>`IF (NWD.LT.4) CALL VF_A2ERR('VF_IITIME','SYNTAX ERROR.')`<br>`CALL VF_ZSTOR(DTINIT,TEXT(IS(3):IE(3)))`<br>`CALL VF_ZSTOR(DTSAFE,TEXT(IS(4):IE(4)))`<br>`IF (DTINIT.LT.ZERO) CALL VF_A2ERR('VF_IITIME','INVALID VALUE.')` | C 문서 누락 | 자동 시간간격의 입력·기본값·확산계수·최종 제한을 함께 기록한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| 3d-theory:KS1-626 | 자동 시간 간격의 기체 경계면 제외 | (문서에 해당 문장 없음) | `3D/vf_cdtcal.f:112–130`; 3D manual p.56<br>`IF (INDX(I  ,J,K).GE.1) THEN`<br>`IF (MAX(FC,BCF(INDX(I  ,J,K))).LE.0.0D0) FL1=0.0D0`<br>`ENDIF`<br>`IF (INDX(I+1,J,K).GE.1) THEN`<br>`IF (MAX(FC,BCF(INDX(I+1,J,K))).LE.0.0D0) FL2=0.0D0` | C 문서 누락 | 자동 시간 간격 계산은 경계 면의 내부 F와 경계 F가 모두 0 이하일 때 해당 면 유량을 0으로 둔다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| 3d-theory:KS1-720 | 현재 노트 | `V=GGV·Δx·Δy·Δz`<br>`FL1..6=\|면적·투과율·속도\|` | `05fdbedb:models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:28–32`; `3D/vf_cdtcal.f:105–130`; 3D manual p.56<br>`V=GGV(I,J,K)*DX*DY*DZ`<br>`FL1=ABS(DYZ*GGX(I  ,J,K)*UU(I  ,J,K))`<br>`FL2=ABS(DYZ*GGX(I+1,J,K)*UU(I+1,J,K))`<br>`FL3=ABS(DXZ*GGY(I,J  ,K)*VV(I,J  ,K))`<br>`FL4=ABS(DXZ*GGY(I,J+1,K)*VV(I,J+1,K))` | B 문서 오기 | CFL 분자는 공극 체적 γvΔxΔyΔz다. 분모는 여섯 면에서 조건별로 정한 절대 체적유량 최댓값이다. 경계 면에서는 내부 F와 경계 F가 모두 0 이하일 때 해당 유량을 0으로 둔다. 근거는 KS1-626이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KS1.md) |
| callflow:RF-009 | STOC 교환과 최소 시간 간격 합의의 순서 | `MPI_ALLREDUCE...MPI_MAX`<br>`MPI_ALLREDUCE...MPI_MIN`<br>`:1017-1019`<br>`comm_mlicdsmg2fc` | `05fdbedb:models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:74`. `3D/vf_a1main.f:997–1019`.<br>`IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`<br>`IF (NB_SC.GT.0) THEN` | B 문서 오기 | 종료 플래그 합의는 STOC 교환 앞이다. 최소 시간 간격 합의는 STOC 교환 뒤이다. `IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`에서 종료하지 않은 경로가 뒤의 교환·시간 간격 합의에 도달한다. STOC 수신·송신은 `IF (NB_SC.GT.0) THEN` 안에서 실행한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-RF.md) |
| callflow:RF-016 | 3D 흐름도의 중첩 격자·STOC 생략 | (문서 흐름도에 해당 중첩 격자·STOC 경로 없음) | 3D manual p.60(372), Figure 0-4-1. `3D/vf_a1main.f:919–940,1003–1019`.<br>`IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`<br>`IF (NB_SC.GT.0) THEN` | C 문서 누락 | 중첩 격자 교환은 반복 머리에 있다. STOC 교환은 종료 분기 뒤에 있다. `IF (IE.EQ.1 .OR. IEE.EQ.1) GOTO 1000`에서 종료하지 않은 경로가 STOC 교환 위치에 도달한다. STOC 교환은 `IF (NB_SC.GT.0) THEN` 안에서 수행한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-RF.md) |
| callflow:RF-020 | 자동 시간 간격의 첫 단계 기준 | `VF_P0MIND`<br>`DT=MAX(MIN(DT·DTSAFE, 1.2·DT_prev), DTMIN)`<br>`MPI_ALLREDUCE...MPI_MIN` | `05fdbedb:models/CADMAS-SURF/source-analysis/cadmas-surf3d-timestep-nesting-stoc-coupling.md:39`. `3D/vf_cdtcal.f:141–147`.<br>`IF (NNOW.EQ.0) W=DTINIT`<br>`DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)` | C 문서 누락 | NNOW.EQ.0이면 성장 상한의 기준은 DTINIT이다. 이후 기준은 DTNOW이다. 원문의 선택문은 `IF (NNOW.EQ.0) W=DTINIT`이다. 최종 식은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`이다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-RF.md) |
| tutorials-build:KU1-076 | data.env의 레코드 분리 | `1 'a08_cad' 64 -1` | STOC manual p.9; `3D/vf_pmginp.f:25–33`; `3D2F/vf_pmginp.f:29–49`<br>`READ(IENFIL,*,END=9020,ERR=9020) MGARAN`<br>`IF (MGARAN.GT.MAXPRO) GOTO 9030`<br>`IF (MGARAN.LE.0     ) GOTO 9040`<br>`N=0`<br>`DO 120 I=1,MGARAN` | C 문서 누락 | data.env는 첫 줄에 영역 수 1을 쓰고 다음 줄에 `'a08_cad' 64 -1`을 쓴다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) |
| tutorials-build:KU1-804 | 시간간격 증가 제한 | (문서에 해당 문장 없음) | 3D·2F tutorial p.6; 3D·`3D2F/A11111.in:53–69`; `3D/vf_cdtcal.f:141–147`<br>`DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`<br>`W=DTNOW`<br>`IF (NNOW.EQ.0) W=DTINIT`<br>`W=DT`<br>`CALL VF_P0MIND(W,DT)`<br>`CAKIY CALL VF_P1MIND(W,DT)` | C 문서 누락 | 자동 시간간격은 `DT=MAX(MIN(DT*DTSAFE,1.20D0*W),DTMIN)`을 적용한다. 기준값은 `W=DTNOW`다. `IF (NNOW.EQ.0) W=DTINIT`를 적용한다. DTMIN은 MIN 계산 뒤에 하한으로 적용한다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) |
| tutorials-build:KU1-814 | STOC 수평 분할선 검사 | (문서에 해당 문장 없음) | STOC manual p.7–9; `3D/vf_stoc_area.f:121–165`<br>`IF( IS*IE*JS*JE.EQ.0 ) THEN`<br>`WRITE(*,*) 'ERROR: CADMAS DOMAIN DIVISION LINE MUST BE',`<br>`$        '       PLACED ON STOC-IC GRID LINE.'`<br>`WRITE(ILPFIL,*) 'ERROR: CADMAS DOMAIN DIVISION LINE MUST BE',`<br>`$        ' PLACED ON STOC-IC GRID LINE.'` | C 문서 누락 | STOC 연성에서는 CADMAS의 수평 병렬 분할선을 STOC-IC 격자선에 맞춘다. [최종 근거](../../../_staging/recovery/compare/CADMAS-SURF-conclusion-verify-KU1.md) |
