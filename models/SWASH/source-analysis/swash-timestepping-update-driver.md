---
title: "SWASH time-stepping driver + field update — Main 시간루프·ComputStruc/CompUnstruc orchestration·Flowdata 전역 모듈"
model: SWASH
component: src (time-stepping driver / field update / data module)
canonical_source: self
citation_status: verified
verification_method: "SWASH v12.01 소스 직접 read (raw/source_code/swash/src/). SwashMain.ftn90(시간루프·dt 적응·노드동기), SwashComputStruc/CompUnstruc/ComputFlow/CompUFlow(시뮬레이션 스텝 orchestration), SwashUpdateData/UpdateUData(BC+필드 갱신·old-time 저장), SwashUpdFlowFlds/UpdUFlowFlds·UpdateFld(입력필드 매핑·시간보간), SwashFlowDP/FlowUDP(bottom depth), SwashPresFlow·UpdPress/UpdUPress(pressurized-flow mask·대기압), SwashFlowdata/Module1/Module2/Solvedata(전역 data module) file:line 인용"
note_author: "Claude Opus 4.8 (1M context)"
note_date: 2026-06-16
related:
  - models/SWASH/source-analysis/swash-architecture-source-map.md
  - models/SWASH/source-analysis/swash-nonhydrostatic-pressure-solver.md
  - models/SWASH/README.md
---

# SWASH time-stepping driver + field update

> Main 시간루프와 한 스텝의 orchestration(BC갱신 → flow solve → depth/mask 갱신 → transport/turbulence), 그리고 이를 떠받치는 전역 data module을 정리. 경로: `raw/source_code/swash/src/`. 비정수압 압력 projection의 내부 메커닉은 [swash-nonhydrostatic-pressure-solver.md] 참조 — 여기서는 호출 흐름(update orchestration)만 다룬다.

## 1. 전체 콜 그래프 (한 스텝)

```
SwashMain (timeloop)                          SwashMain.ftn90:201
 ├─ SwashUpdateData(it)  [구조격자, optg/=5]   :220
 │   or SwashUpdateUData(it) [비구조, optg==5] :222
 └─ if comput/='NOCO' .and. it>0:
     SwashComputStruc    [구조]                :241
       or SwashCompUnstruc [비구조]            :247
```

`SwashMain`의 시간루프 입구에서 `optg` (격자 종류)로 분기: `optg /= 5` → 구조격자 경로(`SwashUpdateData`/`SwashComputStruc`), `optg == 5` → 비구조 삼각망 경로(`SwashUpdateUData`/`SwashCompUnstruc`) — SwashMain.ftn90:219-249. 각 호출 사이마다 `SWSYNC`(노드 동기화)와 `STPNOW()` 체크 — SwashMain.ftn90:213-265.

Purpose verbatim:
- `SwashMain`: *"Main subroutine ... performs initialization ... pre processing ... simulation run ... post processing"* — SwashMain.ftn90:38-46.
- `SwashComputStruc`: *"Performs one full simulation step with structured grid"* — SwashComputStruc.ftn90:40-42.
- `SwashCompUnstruc`: *"Performs one full simulation step with unstructured grid"* — SwashCompUnstruc.ftn90:38-40.

## 2. SwashMain — 시간루프 driver

`repeatloop`(명령 단위) 안에 `timeloop`(시간 적분 단위) 중첩 — SwashMain.ftn90:135,201.

| 단계 | 동작 | file:line |
|---|---|---|
| 초기화 | `SwashInit` | :126 |
| 명령 읽기 | `SwashReadInput(comput)`; `comput=='STOP'`이면 `norm_end` 쓰고 exit | :140-153 |
| 준비 | `SwashCheckPrep` (입력 일관성) | :158 |
| 시작 카운터 | `nstatc==1`(동적)→`it0=0`, 아니면 `it0=1` | :192-196 |
| 루프 종료 | `real(timco) > real(tfinc)`이면 exit | :203 |
| BC/필드 갱신 | `SwashUpdateData(it)` / `SwashUpdateUData(it)` | :219-223 |
| 시뮬레이션 | `it>0 .and. comput/='NOCO'` 일 때만 compute | :232-253 |
| 출력 | `SwashOutput` | :263 |
| 시간 전진 | `timco = timco + dt`; `it=it+1` | :303,320,324 |

`it0=0` 의미: 동적 계산은 `it=0`(=초기 BC 적용·출력만, compute는 `it>0` 조건 :232로 skip)부터 시작.

### 2.1 적응 시간스텝 (명시적 적분만)

`mtimei == 1`(explicit/leap-frog)일 때만 CFL 기반 dt 조정 — SwashMain.ftn90:275:
- `cflmax > pnums(3)` → `dt = 0.5*dt` (halving), `istep=0` 리셋 — :277-284.
- `cflmax < pnums(2)` → 지난 20 스텝 동안 dt가 일정했을 때(`.not. istep < 20`)만 `dt = 2.0*dt` (doubling) — :285-297.

즉 dt 더블링은 20스텝 안정 후에만 허용, 헐빙은 즉시. `istep`은 `timco += dt` 후 `istep=istep+1` — :325. 암시적(`mtimei==2`)은 이 블록을 타지 않으므로 dt 고정. (`mtimei`/`pnums` 의미는 SwashCommdata3 — source-needed, 본 배정 외 파일.)

### 2.2 종료/정리

루프 종료 후: PVD collection 파일 마감 :345-351, `PRINTF` 제외 모든 열린 unit close :355-358, 병렬 시 `IMRGE==1`이면 `SWCOLLECT`/`SWCOLOUT`으로 서브도메인 출력 병합 :364-377, `SwashCleanMem`으로 전 배열 해제 :390.

## 3. SwashComputStruc — 구조격자 한 스텝 orchestration

핵심 시퀀스 (SwashComputStruc.ftn90):

| 순서 | 호출 | 조건 | file:line |
|---|---|---|---|
| 1 | `SwashUpdKBCrigb` (강체 운동학 BC) | FSI loop 내 | :118 |
| 2 | **`SwashComputFlow`** (SWE 풀기) | `.not.momskip` | :125 |
| 3 | `SwashForcesRigidBod` | | :132 |
| 4 | `SwashMotionRigidBod` | | :144 |
| 5 | `SwashUpdateDepths` | `kmax==1`→`(u1,v1)`, else `(udep,vdep)` | :216-220 |
| 6 | `SwashLayerIntfaces` | `kmax>1` | :227 |
| 7 | `SwashDryWet` (wetting/drying mask) | | :233 |
| 8 | `SwashPresFlow` (pressurized mask) | `ifloat /= 0` | :240 |
| 9 | `SwashBreakPoint` (breaking mask) | `isurf /= 0` | :247 |
| 10 | `SwashComputTrans` (수송) | `itrans /= 0` | :254 |
| 11 | `SwashComputTurb` (3D 난류) | `iturb /= 0` | :261 |

스텝 1-4는 **FSI(fluid-structure interaction) iteration loop** (label `10`, :107-183): floating body 변위 수렴(`resm > epslin`)까지 flow+force+motion 반복. `maxit = nint(pship(9))`, 허용오차 `epslin` = `pship(8)` 스케일 — :92-100. body가 없으면(`mbod=0`) 루프는 1회로 수렴. 비수렴 경고/통계는 `ifloat==2 .and. INODE==MASTER`에서 출력 — :187-211.

## 4. SwashCompUnstruc — 비구조 한 스텝 orchestration

구조 경로의 단순화판 (FSI/floating body 없음) — SwashCompUnstruc.ftn90:

| 순서 | 호출 | 조건 | file:line |
|---|---|---|---|
| 1 | **`SwashCompUFlow`** | `.not.momskip` | :67 |
| 2 | `SwashUpdateUDepths` | `kmax==1`→`u1`, else `udep` | :74-78 |
| 3 | `SwashLayUIntfaces` | `kmax>1` | :85 |
| 4 | `SwashUDryWet` | | :91 |
| 5 | `SwashUBreakPoint` | `isurf /= 0` | :98 |
| 6 | `SwashCompUTrans` | `itrans /= 0` | :105 |
| 7 | `SwashCompUTurb` | `iturb /= 0` | :112 |

## 5. SwashComputFlow — SWE solver dispatch (구조격자)

Purpose: *"Computes water level and flow velocities by means of solving the shallow water equations"* — SwashComputFlow.ftn90:38-40. Method: *"Time integration is based on a semi-implicit approach that is unconditionally stable ... Alternatively, water level gradients and the depth-integrated continuity equation are treated explicitly using the leap-frog technique"* — :42-47.

분기 매트릭스 — `oned`(1D/2D) × `kmax`(층수) × `mtimei`(시간적분) × `mimetic`/`lsubg`:

| 차원 | 층 | mtimei=1 (explicit) | mtimei=2 (semi-implicit) |
|---|---|---|---|
| 1D | `kmax==1` | `SwashExpDep1DHflow` :86 | `SwashImpDep1DHflow` / mimetic→`SwashImpDepM1DHflow` :94-96 |
| 1D | `kmax>1` | `SwashExpLay1DHflow` / lsubg→`SwashExpLayP1DHflow` :111-113 | `SwashImpLayM/P/1DHflow` :121-126 |
| 2D | `kmax==1` | `SwashExpDep2DHflow` :146 | `SwashImpDep2DHflow` / mimetic→`SwashImpDepM2DHflow` :153-156 |
| 2D | `kmax>1` | `SwashExpLay2DHflow` / lsubg→`SwashExpLayP2DHflow` :170-173 | `SwashImpLay2DHflow` / lsubg→`SwashImpLayP2DHflow` :181-184 |

`Dep`=depth-averaged(`kmax==1`), `Lay`=layer-averaged(`kmax>1`), `M`=mimetic, `P`=subgrid(`lsubg`). 솔버 인자로 `u1,u0,ua,up,qx,qm,q,dq,gmatu,rho,ui,dqgrd` 등 전역 Flowdata 배열을 명시 전달 — :86,94. `q`=비정수압, `dq`=압력 보정, `gmatu`=u-point 압력 gradient matrix, `ui`=projection 중간속도 (§9 참조). 끝에 출력용 setup/wave-height/current가 필요하면 `SwashAverOutp(1)` — :196.

`SwashCompUFlow`(비구조)는 같은 dispatch의 삼각망 판: `kmax==1`/`mtimei` 4-way로 `SwashExpDepUflow`/`SwashImpDepUflow`/`SwashExpLayUflow`/`SwashImpLayUflow` — SwashCompUFlow.ftn90:70-106. 인자에 `uvc`(circumcenter 속도), `qn`(face mass flux), `quf` 등 비구조 전용 배열 — :78,84.

## 6. SwashUpdateData — BC + 입력필드 갱신 (구조격자)

Purpose: *"Updates flow data, boundary conditions and input fields"* — SwashUpdateData.ftn90:52-54. Method가 지원 BC를 verbatim 열거: *"1) water level / 2) velocity or discharge / 3) Riemann invariant or Sommerfeld radiation or weakly reflective / 4) outflow in case of supercritical flow"* — :58-63.

### 6.1 Old-time 저장 (핵심 update 흐름)

`nstatc == 1`(동적)일 때 현재→이전 시간레벨 복사 — :219-285:
- `s0 = s1`, `u0 = u1`, (2D) `v0 = v1` — :224-226. (`relwav`이면 `so = s0` 먼저 — :223.)
- 비정수압(`ihydro/=0`): `kmax==1 .or. ihydro==3` → `w0bot=w1bot;w0top=w1top` (1DH/2DH bottom·top w), else `w0=w1` (+`lsubg`이면 `u0p/v0p/w0p`) — :228-244.
- `hso = hs`, `kmax>1`→`hkso=hks`, `icreep/=0`→`zkso=zks` — :248-250.
- 이동 강체(`ifloat==2`): 변위/속도/가속도/힘/토크/계류 연장 6쌍 `*0 = *1` — :253-274.
- Coriolis AB2 부트스트랩: `it==1` → `epsab2=pcor(2); pcor(2)=-0.5` (1스텝 explicit Euler), `it>1` → `pcor(2)=epsab2` (modified AB2) — :276-283.

이 old-time 저장이 leap-frog/AB2 시간적분의 전제. `s0/u0/v0/w0`는 솔버(§5)에서 이전 레벨로 소비된다.

### 6.2 BC 처리 → 입력필드 → 파생량

순서 (SwashUpdateData.ftn90):
1. Fourier/시계열 기반 경계값 계산 (MASTER에서 `SwashReadBndval`) — :289-328.
2. `bndval` scatter, 격자 경계점에 경계값 결정; 단파/속박파/Stokes/transfer는 `it==0`에만 1회 — :343,742-754.
3. closed boundary에서 법선속도 0: `ibl/ibr==1`→`u1=0`, `ibb/ibt==1`→`v1=0` (반복격자 아닐 때) — :2170-2201.
4. 서브도메인 교환 `SWEXCHG(s1/u1/v1)` + 반복격자 `periodic` — :2205-2214.
5. 내부조파 source `SwashIntWavgen` (`iwvgen/=0`, `it==0`) — :2218-2251.
6. 입력필드 갱신 `SwashUpdateFld(...)`: 속도(2,3)/마찰(4)/바람(5,6)/수위(7)/대기압(13) — :2490-2518.
7. `SwashUpdFlowFlds` (필드→flow 변수) — :2524.
8. 마찰 `SwashLogLaw`/`SwashBotFrict`, 바람응력 `SwashWindStress`, 대기압 `SwashUpdPress`, 수평/수직 점성, Reynolds 응력, 포러스/식생/밀도 — :2531-2594.

`SwashUpdateUData`(비구조)는 동일 패턴: BC 지원은 1)-3)만 (outflow 없음, Method :48-52), old-time 저장에 `bcso=bcs`(face 수위), `ltrans>0`→`bcrpo=bcrp` 추가 — :214-251, 파생량은 `SwashULogLaw`/`SwashUBotFrict`/`SwashUWindStress`/`SwashUpdUPress`/`SwashUHorzVisc` 등 U-접두 변형 — :1331-1383.

## 7. 입력필드 매핑·시간보간 — SwashUpdateFld

Purpose: *"Updates user-defined input fields, maps onto computational grid and interpolates in time"* — SwashUpdateFld.ftn90:38-40.

3-time-level 버퍼 `arrfx(:,1/2/3)`: `1`=직전, `2`=현재(보간결과), `3`=마지막 읽은 값. 흐름 (:104-262):
1. shift: `arrfx(:,1) = arrfx(:,2)` — :106.
2. `timco > ifltim(igr1)`인 동안 새 필드 read (`INAR2D`, MASTER) + `SWBROADC` → 계산격자 매핑(`SVALQI` 보간 또는 직접 인덱싱) → `arrfx(:,3)`; 벡터면 회전 `uu*cosfc+vv*sinfc` — :117-226.
3. **시간선형보간**: `wf3 = (timco-timlr)/(ifltim-timlr)`, `wf1=1-wf3`, `arrfx(i,2)=wf1*arrfx(i,1)+wf3*arrfx(i,3)` — :230-239.
4. 벡터는 크기 손실 방지: 보간 후 방향만 쓰고 크기는 `fac=wf1*|f1|+wf3*|f3|`로 재정규화 — :246-253.

`outval`(격자밖 값)은 필드종류로 분기: 속도/바람(2,5)=0, 마찰/수위/대기압(4,7,13)=`NEAREST` — :109-113. 구조/비구조 매핑 분기 `optg/=5` vs nverts 루프 — :167-224.

## 8. flow 변수 초기화/갱신 — SwashUpdFlowFlds / SwashUpdUFlowFlds

Purpose(구조): *"Initializes / updates flow variables based on space varying input fields"* — SwashUpdFlowFlds.ftn90:38-40.

- 수위: `initsf .or. ifldyn(7)==1`이면 wl-point에 `wlevf` 보간 (1D 2점평균, 2D 4점평균) → `s1`; `SWEXCHG`/`periodic`; `initsf=.false.` — :75-138.
- u-속도: `inituf .or. ifldyn(2)==1`이면 `uxf`→`u1(:,1)`; 비스태거드면 곡선격자 변환 `(ycgrid diff)/guu` — :141-204. `kmax>1`이면 연직 균일가정으로 `u1(:,k)=udep` 확장 — :215-227.
- v-속도: 2D·`initvf .or. ifldyn(3)==1` 유사 처리 — :233-305.

비구조판 `SwashUpdUFlowFlds`(:81-123): 셀 3정점 평균으로 `s1(icell)`, face에 법선투영 `u1(iface,1)=nx*ux+ny*uy` (vertex 속도 평균) — :93,116.

## 9. bottom depth 결정 — SwashFlowDP / SwashFlowUDP

Purpose: *"Determines bottom values in water level and velocity points"* — SwashFlowDP.ftn90:38-40.

`dpsopt`로 wl-point bottom `dps` 산정 (1=min, 2=mean, 3=max, 4=local) — SwashFlowDP.ftn90:98-106(1D), :151-159(2D). dry 가드: `s1 < epsdry-dps`이면 `s1 = 0.99*epsdry-dps` — :108-112. velocity-point는 **tiled** 최소값: `dpu(nm)=min(dps(nm),dps(nmu))`, `dpv` 동일 — :240,265,284. virtual point 미러링·`SWEXCHG`·`periodic` 포함 — :123-225.

비구조판 `SwashFlowUDP`(:81-170): `dpsopt==1`은 face=min(vertex), centroid=min(face) tiled; `dpsopt==2`는 centroid=3정점평균, face=min(인접셀); `MAX/SHIFT`는 미지원 `msgerr(2,...)` — :168.

## 10. pressurized-flow mask & 대기압 — SwashPresFlow / SwashUpdPress / SwashUpdUPress

`SwashPresFlow` (Purpose: *"Updates mask arrays for pressurized flow in water level and velocity points"* — :38-40): `s1 < -flos`(floating object draft 초과)이면 `presp=0`(free surface) else `1`(pressurized) — :80-88. u/v-point는 양쪽 wl-point가 모두 0일 때만 0: `presp(nm)==0 .and. presp(nmu)==0` → `presu=0` — :106-114. `SWEXCHGI`/`periodici`로 정수 mask 교환 — :94,156. `SwashComputStruc`에서 `ifloat/=0`일 때만 호출 — SwashComputStruc.ftn90:240.

`SwashUpdPress` (Purpose: *"Initializes / updates atmospheric pressure ... Also correct water level on open boundaries"* — :38-41): `ifldyn(13)==1`이면 `presf`→`patm` 보간(1D 2점/2D 4점) + 경계 미러/periodic — :84-217. 그리고 `prmean>0`이면 수위 보정 경계조건(`ibl/ibr/ibb/ibt==2`인 water-level opening): `s1 += (prmean-patm)/(rhow*grav)` (inverse barometer) — :221-258. 비구조판 `SwashUpdUPress`는 셀 3정점 평균 `patm`, 경계 face btype==2에서 `bcs += (prmean-patm)/(rhow*grav)` — SwashUpdUPress.ftn90:81-112.

## 11. 전역 data module

### 11.1 SwashFlowdata — flow 상태 중앙 저장소

Purpose: *"Module containing data for flow computation"* — SwashFlowdata.ftn90:38-40. 거의 모든 compute/update 서브루틴이 `use SwashFlowdata`로 공유.

| 그룹 | 대표 변수 | file:line |
|---|---|---|
| 격자 인덱스 한계 | `mf/mfu/ml/mlu`, `nf/nfu/nl/nlu` (virtual/internal 경계) | :58-77 |
| mask | `presp/presu/presv`(pressurized), `wets/wetu/wetv`(wet-dry), `brks`(breaking) | :79-125 |
| 수위/속도 (2-level) | `s0/s1`, `u0/u1`, `v0/v1`, `w0/w1` | :307-352 |
| depth | `dps`(wl), `dpu/dpv`(u/v tiled), `hs/hso`(water depth) | :198-200,243-248 |
| 비정수압 | `q`(압력), `dq`(보정), `qv`, `dqgrd/dqgrdu/dqgrdv` | :201-205,273-275 |
| gradient/divergence matrix | `gmatu/gmatv/gmatw`, `dmat/dmatu`, `amatp`(Poisson), `rhsp` | :193-222,137,288 |
| projection 중간속도 | `ui/vi` | :331,341 |
| BC 타입 | `ibb/ibl/ibr/ibt` (1=closed,2=wl,3=vel,5=disch,6=Riemann,7=weakly refl,8=Sommerfeld,10=outflow) | :82-98 |
| 강체/floating | `flos/flou/flov`(draft), `lfbs`, `skc` | :99,211-213,309 |
| 층 (3D) | `hks/hkso`, `zks/zkso`(interface), `wom`(relative w) | :226-369 |

`s0/s1`·`u0/u1` 등 2-time-level 명명이 §6.1 old-time 저장의 대상.

### 11.2 SwashSolvedata — 선형솔버 작업공간

Purpose: *"Module containing data for the linear solvers"* — SwashSolvedata.ftn90:38-40. `iamout`(출력량 0-3 :58), `icond`(BiCGSTAB 전처리 선택 :63), CSR 포맷 배열 `ia/ja/ax2`(BiCGSTAB) vs `ias/jas/axs`(PCG) :68-82, 전처리 `prec*`/`cmat`(SIP·ILU·RILU) :84-95, nested Newton 변수 `amata/ba/da/p0/p1/q0/q1/sol*` :79-110, CG/BiCGSTAB 작업벡터 `r/s/z/p/t/u/v/w` :89-119. `iamout`은 `SwashComputStruc`이 FSI 수렴 출력 제어에 사용 — SwashComputStruc.ftn90:50,170.

### 11.3 SwashModule1 (SwashCommdata1) — 단위·출력 메타

`SwashCommdata1`은 *"data of units and output"* — SwashModule1.ftn90:48-50. 단위 문자열 `uc/ud/...uv` :71-82, 출력변수 메타 `nmovar=120`개 (`ovsvty` 타입, `ovexcv` 예외값, `ovkeyw/ovlnam/ovsnam/ovunit` 이름) :64-118, 출력 frame 기하 `alcq/xpq/...` :94-113. (Commdata2/3/4·Timecomm은 같은 파일 내 다른 모듈 — 본 노트 범위는 1만 인용, 나머지는 source-needed.)

### 11.4 SwashModule2 — 출력/BC/일반배열 모듈 3종

한 파일에 3 모듈 (SwashModule2.ftn90:1-7):
- `outp_data` (*"Contains data needed during generation of output"* :48-50): `max_outp_req=250`, `mopa=31` :64-66, PVD/VTK 속성(v41.95) :46.
- `m_bndspec` (BC 명세, :294): linked-list delete 인터페이스 `deletebfl/bfs/bgp` :474-476.
- `m_genarr` (*"Creates several allocatable arrays for Swash computation"* :595-597): **`kgrpnt`**(active 격자점 주소 인덱스 테이블, 모든 구조격자 루프의 핵심) :620, 입력필드 3-level 버퍼 `uxf/uyf/wlevf/presf/fricf`(§7 매핑 타깃) :680-684, 곡선격자 메트릭 `guu/gvv/gsqs/xcgrid/ycgrid` :650-693, 층 두께 `hlay` :657, 경계 prescribe 플래그 `slimp/srimp/...` :695-699.

## 12. 발견·주의

- **dt 적응은 explicit 전용**: `mtimei==1`에서만 CFL 더블/헐빙 — SwashMain.ftn90:275. 암시적은 dt 고정. doubling은 20-step 안정 후에만(`.not. istep<20`) — :287.
- **`it=0` 특수 스텝**: 동적계산은 `it0=0`(SwashMain.ftn90:193)에서 시작하나 compute는 `it>0`에서만(:232) — `it=0`은 초기 BC/단파·Stokes 1회 셋업 + 출력 전용.
- **old-time 저장은 update 안에**: leap-frog/AB2의 `s0/u0/...`·Coriolis `pcor(2)` 부트스트랩이 `SwashUpdateData`(:219-285)에서 일어남 — compute 직전 단계임에 유의.
- **구조 vs 비구조 대칭**: 거의 모든 driver/update 서브루틴이 `Swash*`(구조)와 `Swash*U*`/`SwashU*`(비구조) 쌍으로 존재 (UpdateData↔UpdateUData, ComputFlow↔CompUFlow, FlowDP↔FlowUDP, UpdPress↔UpdUPress). 비구조는 outflow BC·floating body·icreep(creep) 미지원이 차이.
- **압력 projection 자체**는 본 노트 범위 밖 — `SwashComputFlow`가 호출하는 `SwashImp*flow` 내부에서 `q/dq/gmatu/ui` 사용. 메커닉은 [swash-nonhydrostatic-pressure-solver.md] 참조. 여기서는 호출·인자 전달만 인용 — SwashComputFlow.ftn90:94,154.
