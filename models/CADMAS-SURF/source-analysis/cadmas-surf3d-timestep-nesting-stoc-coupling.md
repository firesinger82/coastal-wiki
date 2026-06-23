---
title: "CADMAS-SURF/3D 시간刻み·격자 nesting·STOC 결합 — CFL 적응 Δt·親子 telescoping 격자·MPMD STOC 핸드오프 (vf_cdtcal·pmg*·stoc_*·mod_comm)"
model: CADMAS-SURF
component: src (timestep control + grid nesting + STOC coupling infra)
canonical_source: self
verification_method: "CADMAS-SURF/3D-MG 소스 직접 read (raw/.../CADMAS-SURF-3D/Source code/). CFL: vf_cdtcal.f 안전율·이류CFL·확산한계(:58-147)+VF_ATIMER.h DTSAFE+drive vf_a1main.f:937-943·1017-1019. nesting: vf_pmginp.f env+vf_pmgset.f 親子설정+vf_pmgp2c/c2p.f 전송+pmgp2c_cf.f 보간(XPF/YPF/ZPF)+VF_APARAI.h MGPARE/MGCPOS 토폴로지. STOC: vf_stoc_init.f MPI_COMM_SPLIT(:43-45)+stoc_recv/send.f 경계값 U/V/W/HU+mod_comm.f90 MPMD comm(:143-179)+NB_SC 게이트 VF_ASTOCI.h:41+vf_a1main.f:1010-1027. file:line 직접 인용. disclosed gap 2건 명시."
citation_status: verified
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-23
related:
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-architecture-source-map.md
  - models/CADMAS-SURF/source-analysis/cadmas-surf3d-smac-velocity-pressure-solver.md
  - models/CADMAS-SURF/README.md
---

# CADMAS-SURF/3D 시간刻み·격자 nesting·STOC 결합

> CADMAS-SURF/3D 를 **멀티스케일 tsunami 프레임워크**(STOC-ML/IC 광역 → CADMAS 국소)에 연결하는 인프라 3종. (A) 적응 Δt(CFL) (B) "MG"=親子 telescoping 격자 nesting (C) STOC 결합(MPMD). 메인루프 [architecture-source-map §4](cadmas-surf3d-architecture-source-map.md#4-smacvof-시간적분-루프-vf_a1mainf915-1145)의 ①PMGP2C/C2P ②CDTCAL ⑤STOC 단계. 경로 루트 동일.

## A. 적응 시간刻み (CFL) — vf_cdtcal.f

헤더 `VF_CDTCAL:時間刻み幅の計算`(`vf_cdtcal.f:5-7`). 드라이버 분기(`vf_a1main.f:937-943`): `IDTTYP=0`→고정 `DT=DTCNST`, `≠0`→자동(`VF_CDTCAL`). 디폴트 `IDTTYP=1`·`DTCNST=1e-3`(`vf_a2dflt.f:223·230`).

산정 순서:
1. **안전율 적용 초기상한**: `DT=DTMAX/DTSAFE` (`vf_cdtcal.f:58-59`, `DTSAFE`=安全率 `VF_ATIMER.h:18`)
2. **확산한계 사전계산**: `ANU`(분자+渦점성)·열전도·스칼라확산의 max → `WK01` (`vf_cdtcal.f:61-87`)
3. **이류 CFL**(porous Courant): 셀 유체체적 `V=GGV·Δx·Δy·Δz`, 6면 체적플럭스 `FL1..6=|면적·투과율·속도|` →
   ```
   vf_cdtcal.f:130 :  DT = V / MAX(FL1,FL2,FL3,FL4,FL5,FL6, V/DT)
   ```
   (셀 물체적 ÷ 최대 유출 체적플럭스)
4. **확산(점성)한계**(`vf_cdtcal.f:132-134`):
   ```
   V  = 0.5 / (1/Δx² + 1/Δy² + 1/Δz²)
   DT = V / MAX(WK01, V/DT)
   ```
   고전 명시적 확산한계 `Δt ≤ 0.5/[ν(1/Δx²+1/Δy²+1/Δz²)]`
5. **최종조립**(`vf_cdtcal.f:141-147`): 전 PE 전역 min `VF_P0MIND` → `DT=MAX(MIN(DT·DTSAFE, 1.2·DT_prev), DTMIN)` (안전율·전스텝 1.2배 상한·하한 DTMIN). 결합셋 전역 동기 `MPI_ALLREDUCE...MPI_MIN`(`vf_a1main.f:1017-1019`).

> ⚠️ **disclosed gap**: `vf_cdtcal.f` 는 **이류 CFL + 확산한계만** 보유 — 명시적 표면파 celerity `√(gH)` 항 **없음**. 자유수면 안정성은 VOF 속도장의 이류 CFL 로 지배(중력은 속도를 통해서만 진입). celerity 안정항을 주장하지 말 것.

## B. 親子 격자 nesting ("MG" = 공간 telescoping, 대수 multigrid 아님)

물리적 親子 sub-domain 이 경계/내부 flow 변수를 교환하는 **공간 telescoping nesting** — residual·smoother·coarse-grid correction V-cycle 없음(헤더·토폴로지 변수가 모두 물리적).

- **환경파일 읽기** `VF_PMGINP:マルチグリッド環境ファイルを読み込む`(`vf_pmginp.f:5-6`) — `data.env`에서 영역명·프로세스수·**親 영역번호** `MGPARE`(`:33`), 자기自身 親 금지(`:46`)
- **설정** `VF_PMGSET:…親子関係をチェックし設定`(`vf_pmgset.f:12`) — P2C/C2P 리스트 구축(`:19`)
- **토폴로지**(`VF_APARAI.h`): `MGRANK`(자기 전역rank :28)·`MGPARE`(親 영역 :34)·`MGPRNK`(親 rank, `<0`=親無 :36-38)·`MGCNUM`(子 수 :50)·`MGCRNK`(子 rank :51)·`MGCPOS(6,*)`(親 내 子 위치 셀범위 :63-69)
- **親→子 전송**(子 경계 보간) `VF_PMGP2C:…親の情報を子へ転送`(`vf_pmgp2c.f:9`), **子→親 전송**(親 내부 restriction) `VF_PMGC2P`(`vf_pmgc2p.f:9`) — 매스텝 연속 호출(`vf_a1main.f:923·929`)
- **보간계수 XPF/YPF/ZPF**(2011.04 추가, `vf_pmgp2c.f:2-4·31-33` `親格子に対する補間係数`): 실제 보간은 `vf_pmgp2c_cf.f` — `FACTZ=0.5(ZPF(KC)+ZPF(KC+1))-Z0`·`RDZ=1/(ZPF(KC+1)-ZPF(KC))`·`VV=BCV(L)+(YPF(JC)-Y0)·BC(8)`(`:79-91`) = 親장을 細격자 子셀에 선형보간
- **포러스/플럭스 헬퍼**: `pmgggt`(親→子 포러스 수신)·`pmggpt`(親→子 포러스 송신)·`pmgflx`/`pmgfly`(VOF-F 플럭스 면정합, `IMPLICIT NONE`+INTENT 신식)

## C. STOC 결합 (정수압 광역 STOC-ML/IC → CADMAS 국소)

- **초기화** `VF_STOC_INIT:STOCとの通信環境を初期化`(`vf_stoc_init.f:5-6`) — `NB_SC` 로 split 하여 STOC↔CADMAS 서브커뮤니케이터 생성: `MPI_COMM_SPLIT(comm_work_ic_mg,NB_SC,...,comm_ic_mg)`(`vf_stoc_init.f:43-45`), 메인 `vf_a1main.f:394`
- **MPMD 메커니즘**(`mod_comm.f90`): `init_mpmd`(`vf_a1main.f:351`). 모델 enum `l_stoc_ml=0·l_stoc_ic=1·l_stoc_ds=2·l_cadmas_mg=10·l_cadmas_2fc=11`(`:23-26`). 커뮤니케이터 `comm_ic_mg`(STOC-IC↔CADMAS/MG :54)·`comm_mlicdsmg2fc`(전 결합셋 :59). `mpi_init`(:98)+`mpi_comm_split(mpi_comm_world,...)` 모델번호 키(`:143-179`) → STOC·CADMAS 별도 실행파일이 한 WORLD 안에서 split
- **게이트 `NB_SC`**(`VF_ASTOCI.h:41-42` `STOC-CADMAS接続에 참가 여부 0/>0`): 매스텝(`vf_a1main.f:1010-1027`)
  ```
  IF (NB_SC.GT.0) THEN
    CALL VF_STOC_RECV(...)   ! STOC→CADMAS 경계값 수신
    CALL VF_STOC_SEND(...)   ! CADMAS→STOC 송신
  ENDIF
  ```
  수신 후 경계 재적용 `VF_BWUWN/BWUWT/BWFF`(`:1020-1027`)
- **STOC→CADMAS**(수신): `VF_STOC_RECV:STOCから境界値を受信`(`vf_stoc_recv.f:5`) — 4측면(W/E/S/N) `MPI_IRECV`(comm_ic_mg, `:47-49`), 면셀당 **4성분**(U,V,W + 수위/수심 HU) → `UWST/UEST/VSST/VNST(*,*,1:4)`(`VF_ASTOCR.h:1-3·12-15`)
- **CADMAS→STOC**(송신): `VF_STOC_SEND`(`vf_stoc_send.f`) — 면블록 `西側U,V,W,HU`(`:38`), VOF 가중 면평균 U,V,W + 플럭스 `H=-A·FFLXX/DTWORK`(`:60-66`) → `STBUF` 패킹·`MPI_ISEND`(`:73-76·135`). 국소해상 속도+경계 체적플럭스를 정수압 親 STOC 로 환류
- **보조**: `stoc_area`(격자정보 교환)·`stoc_obst`(지형 OBST 수신)·`stoc_pors`(포러스 GGV/GGX/GGY/GGZ 수신)·`stoc_1d`(1D 1층 송수신)·`stoc_fconv`(STOC 연성 VOF-F 플럭스)

> ⚠️ **disclosed gap**: STOC↔CADMAS 채널은 `MPI_INTERCOMM_CREATE` 가 아니라 **MPMD 하 `MPI_COMM_SPLIT` 파생 intra-communicator**(`comm_ic_mg`, 두 실행파일이 공유, `mod_comm.f90:143-179`). "MPMD inter-communicator" 는 MPMD 의미로는 정확하나 MPI 객체 자체는 split 커뮤니케이터.

## 전역 동기 (A↔C 연결)

매 교환 전 결합셋이 종료플래그(`MPI_ALLREDUCE...MPI_MAX`, `vf_a1main.f:1003-1004`)·최소 Δt(`MPI_ALLREDUCE...MPI_MIN`, `:1017-1019`)를 `comm_mlicdsmg2fc` 로 합의 → 적응 Δt(§A)가 STOC↔CADMAS↔nest 계층 전체에 묶임.
